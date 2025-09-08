# -*- coding: utf-8 -*-
"""
AreaLoad - Professional area load object for surface loading

This module provides comprehensive area loading capabilities for structural surfaces
including pressure loads, distributed loads, wind loads, and thermal effects.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Any
try:
    from PySide2 import QtCore, QtWidgets, QtGui
except ImportError:
    try:
        from PySide import QtCore, QtGui
        QtWidgets = QtGui
    except ImportError:
        QtCore = QtWidgets = QtGui = None
import os

class AreaLoad:
    """
    Professional area load object for structural surfaces.
    
    Provides comprehensive area loading capabilities including:
    - Pressure loads (uniform, linear, point)
    - Building code loads (dead, live, wind, seismic)
    - Load patterns and distributions
    - Load combinations integration
    """
    
    def __init__(self, obj):
        """
        Initialize AreaLoad object.
        
        Args:
            obj: FreeCAD DocumentObject to be enhanced
        """
        self.Type = "AreaLoad"
        obj.Proxy = self
        
        # Create property helper method
        self._ensure_property_exists = self._create_property_helper(obj)
        
        # Target geometry
        if not hasattr(obj, "TargetFaces"):
            obj.addProperty("App::PropertyLinkList", "TargetFaces", "Geometry",
                           "Faces or surfaces to apply load")
        
        if not hasattr(obj, "LoadedArea"):
            obj.addProperty("App::PropertyArea", "LoadedArea", "Geometry",
                           "Total loaded area (calculated)")
        
        if not hasattr(obj, "LoadDirection"):
            obj.addProperty("App::PropertyVector", "LoadDirection", "Geometry",
                           "Load direction vector (global coordinates)")
            obj.LoadDirection = App.Vector(0, 0, -1)  # Downward default
        
        # Load direction
        direction_list = ["+X Global", "-X Global", "+Y Global", "-Y Global", "+Z Global", "-Z Global", "Normal", "Custom"]
        self._add_enumeration_property(obj, "Direction", "Geometry",
                                      "Load direction", direction_list, "-Z Global")
        
        if not hasattr(obj, "CustomDirection"):
            obj.addProperty("App::PropertyVector", "CustomDirection", "Geometry",
                           "Custom load direction vector")
            obj.CustomDirection = App.Vector(0, 0, -1)  # Downward default
        
        # Load definition - Using new enumeration helper
        load_type_list = [
            "Dead Load (DL)", "Live Load (LL)", "Live Load Roof (LL_Roof)",
            "Wind Load (W)", "Earthquake (E)", "Earth Pressure (H)",
            "Fluid Pressure (F)", "Thermal (T)", "Custom Pressure"
        ]
        self._add_enumeration_property(obj, "LoadType", "Load", 
                                      "Type of area load", load_type_list, "Dead Load (DL)")
        
        # LoadCategory - Using string property  
        self._ensure_property_exists("App::PropertyString", "LoadCategory", "Load",
                                    "Load category for combinations", "DL")
        
        # Load intensity and distribution
        if not hasattr(obj, "LoadIntensity"):
            obj.addProperty("App::PropertyPressure", "LoadIntensity", "Load",
                           "Load intensity (pressure)")
            obj.LoadIntensity = "2.4 kN/m^2"  # Typical dead load
        
        # Distribution pattern
        dist_list = ["Uniform", "Linear X", "Linear Y", "Parabolic", "Point Load"]
        self._add_enumeration_property(obj, "Distribution", "Load",
                                      "Load distribution type", dist_list, "Uniform")
        
        if not hasattr(obj, "DistributionParameters"):
            obj.addProperty("App::PropertyFloatList", "DistributionParameters", "Load",
                           "Parameters for load distribution")
            obj.DistributionParameters = [1.0]  # Default uniform distribution
        
        # Distribution pattern
        pattern_list = [
            "Uniform", "Linear X", "Linear Y", "Bilinear", "Radial", 
            "Point Load", "Line Load", "Custom Pattern"
        ]
        self._add_enumeration_property(obj, "DistributionPattern", "Load",
                                      "Load distribution pattern", pattern_list, "Uniform")
        
        obj.addProperty("App::PropertyFloatList", "DistributionFactors", "Load",
                       "Distribution factors for non-uniform patterns")
        obj.DistributionFactors = [1.0, 1.0, 1.0, 1.0]  # Corner factors
        
        # Load distribution method (based on RISA documentation)
        distribution_list = ["OneWay", "TwoWay", "OpenStructure"]
        self._add_enumeration_property(obj, "LoadDistribution", "Distribution",
                                      "Method for distributing load to supporting elements", 
                                      distribution_list, "TwoWay")
        
        # Direction specification for one-way loads
        # One-way direction
        direction_list = ["X", "Y", "Custom"]
        self._add_enumeration_property(obj, "OneWayDirection", "Distribution",
                                      "Direction for one-way load distribution", 
                                      direction_list, "X")
        
        obj.addProperty("App::PropertyVector", "CustomDistributionDirection", "Distribution",
                       "Custom direction vector for one-way distribution")
        obj.CustomDistributionDirection = App.Vector(1, 0, 0)  # X-direction default
        
        # Edge-specific load distribution factors
        obj.addProperty("App::PropertyFloatList", "EdgeDistributionFactors", "Distribution",
                       "Distribution factors for load attribution to edges")
        obj.EdgeDistributionFactors = [1.0, 1.0, 1.0, 1.0]  # Default equal distribution
        
        # Load case properties
        obj.addProperty("App::PropertyString", "LoadCase", "Case",
                       "Load case identifier")
        obj.LoadCase = "DL1"
        
        obj.addProperty("App::PropertyString", "LoadCombination", "Case",
                       "Load combination identifier")
        
        obj.addProperty("App::PropertyFloat", "LoadFactor", "Case",
                       "Load factor for combinations")
        obj.LoadFactor = 1.0
        
        # Time-dependent properties
        obj.addProperty("App::PropertyBool", "IsTimeDependent", "Time",
                       "Time-dependent load")
        obj.IsTimeDependent = False
        
        obj.addProperty("App::PropertyPythonObject", "TimeFunction", "Time",
                       "Time variation function")
        
        # Building code specific properties
        # Building code
        code_list = [
            "ASCE 7-16", "IBC 2018", "NBCC 2015", "Eurocode 1", 
            "AS/NZS 1170", "Custom"
        ]
        self._add_enumeration_property(obj, "BuildingCode", "Code",
                                      "Building code standard", code_list, "ASCE 7-16")
        
        obj.addProperty("App::PropertyString", "OccupancyType", "Code",
                       "Building occupancy type")
        obj.OccupancyType = "Office"
        
        obj.addProperty("App::PropertyFloat", "ImportanceFactor", "Code",
                       "Importance factor for design")
        obj.ImportanceFactor = 1.0
        
        # Load reduction and modification
        obj.addProperty("App::PropertyBool", "ApplyLoadReduction", "Reduction",
                       "Apply live load reduction")
        obj.ApplyLoadReduction = True
        
        obj.addProperty("App::PropertyFloat", "ReductionFactor", "Reduction",
                       "Live load reduction factor")
        obj.ReductionFactor = 1.0
        
        obj.addProperty("App::PropertyFloat", "TributaryArea", "Reduction",
                       "Tributary area for load reduction")
        
        # Environmental loads
        obj.addProperty("App::PropertyFloat", "WindSpeed", "Environmental",
                       "Basic wind speed (m/s)")
        obj.WindSpeed = 50.0
        
        # Exposure category
        exposure_list = ["A", "B", "C", "D"]
        self._add_enumeration_property(obj, "ExposureCategory", "Environmental",
                                      "Wind exposure category", exposure_list, "B")
        
        obj.addProperty("App::PropertyFloat", "SeismicAcceleration", "Environmental",
                       "Peak ground acceleration for seismic")
        obj.SeismicAcceleration = 0.2
        
        # Thai Units Support
        obj.addProperty("App::PropertyBool", "UseThaiUnits", "Thai Units",
                       "Enable Thai units for load calculations")
        obj.UseThaiUnits = False
        
        obj.addProperty("App::PropertyString", "LoadIntensityKsc", "Thai Units", 
                       "Load intensity in kgf/m² (Thai units)")
        obj.LoadIntensityKsc = "240 kgf/m^2"  # Equivalent to 2.4 kN/m²
        
        obj.addProperty("App::PropertyString", "LoadIntensityTfM2", "Thai Units",
                       "Load intensity in tf/m² (Thai units)")
        obj.LoadIntensityTfM2 = "0.24 tf/m^2"
        
        obj.addProperty("App::PropertyFloat", "LoadFactorThai", "Thai Units",
                       "Load factor per Thai Ministry B.E. 2566")
        obj.LoadFactorThai = 1.4
        
        obj.addProperty("App::PropertyFloat", "TemperatureChange", "Environmental",
                       "Temperature change (°C)")
        obj.TemperatureChange = 0.0
        
        # Advanced Meshing Properties (RISA-3D Enhancement)
        obj.addProperty("App::PropertyFloat", "MeshSize", "Meshing",
                       "Target mesh size for load breakdown (mm)")
        obj.MeshSize = 500.0  # 500mm default
        
        obj.addProperty("App::PropertyInteger", "MinMeshElements", "Meshing",
                       "Minimum mesh elements per face")
        obj.MinMeshElements = 4
        
        obj.addProperty("App::PropertyInteger", "MaxMeshElements", "Meshing",
                       "Maximum mesh elements per face")
        obj.MaxMeshElements = 1000
        
        obj.addProperty("App::PropertyBool", "AdaptiveMeshing", "Meshing",
                       "Use adaptive mesh refinement")
        obj.AdaptiveMeshing = True
        
        obj.addProperty("App::PropertyFloat", "LoadAccuracyTolerance", "Meshing",
                       "Load distribution accuracy tolerance (%)")
        obj.LoadAccuracyTolerance = 5.0  # 5% tolerance
        
        # Mesh type
        mesh_type_list = ["Triangular", "Quadrilateral", "Mixed", "Adaptive"]
        self._add_enumeration_property(obj, "MeshType", "Meshing",
                                      "Type of mesh elements to generate", 
                                      mesh_type_list, "Adaptive")
        
        # Distribution method
        method_list = ["TributaryArea", "InfluenceCoefficient", "DirectProjection", "WeightedAverage", "FiniteElement"]
        self._add_enumeration_property(obj, "DistributionMethod", "Advanced",
                                      "Load distribution algorithm", 
                                      method_list, "TributaryArea")
        
        # Load application properties
        if not hasattr(obj, "ReferencePoint"):
            obj.addProperty("App::PropertyVector", "ReferencePoint", "Application",
                           "Reference point for load application")
        
        if not hasattr(obj, "LoadCenter"):
            obj.addProperty("App::PropertyVector", "LoadCenter", "Application",
                           "Center point of the load application")
            obj.LoadCenter = App.Vector(0, 0, 0)
        
        # Member Attribution Controls (RISA-3D Enhancement)
        obj.addProperty("App::PropertyBool", "IncludeBeams", "Attribution",
                       "Include beams in load attribution")
        obj.IncludeBeams = True
        
        obj.addProperty("App::PropertyBool", "IncludeColumns", "Attribution",
                       "Include columns in load attribution")
        obj.IncludeColumns = True
        
        obj.addProperty("App::PropertyBool", "IncludeBraces", "Attribution",
                       "Include braces in load attribution")
        obj.IncludeBraces = False
        
        obj.addProperty("App::PropertyBool", "IncludeTrusses", "Attribution",
                       "Include truss members in load attribution")
        obj.IncludeTrusses = True
        
        obj.addProperty("App::PropertyBool", "IncludeGravityMembers", "Attribution",
                       "Include gravity-only members")
        obj.IncludeGravityMembers = True
        
        obj.addProperty("App::PropertyFloat", "MemberInfluenceRadius", "Attribution",
                       "Influence radius for member selection (mm)")
        obj.MemberInfluenceRadius = 1000.0  # 1m default
        
        # Enhanced Projection System
        obj.addProperty("App::PropertyVector", "ProjectionPlane", "Projection",
                       "Custom projection plane normal")
        obj.ProjectionPlane = App.Vector(0, 0, 1)  # XY plane default
        
        obj.addProperty("App::PropertyBool", "UseCoplanarProjection", "Projection",
                       "Project loads to coplanar surfaces")
        obj.UseCoplanarProjection = True
        
        obj.addProperty("App::PropertyFloat", "ProjectionTolerance", "Projection",
                       "Coplanarity tolerance (mm)")
        obj.ProjectionTolerance = 10.0  # 10mm tolerance
        
        obj.addProperty("App::PropertyBool", "ConsiderShielding", "OpenStructure",
                       "Consider member shielding effects for open structures")
        obj.ConsiderShielding = False
        
        obj.addProperty("App::PropertyFloat", "ShieldingFactor", "OpenStructure",
                       "Shielding effectiveness factor (0.0-1.0)")
        obj.ShieldingFactor = 0.8  # 80% shielding
        
        # Load Validation Properties
        obj.addProperty("App::PropertyPythonObject", "LoadValidation", "Validation",
                       "Load validation results")
        obj.LoadValidation = {}
        
        obj.addProperty("App::PropertyBool", "ShowValidationWarnings", "Validation",
                       "Show load validation warnings")
        obj.ShowValidationWarnings = True
        
        obj.addProperty("App::PropertyBool", "AutoValidateOnChange", "Validation",
                       "Automatically validate when properties change")
        obj.AutoValidateOnChange = True
        
        # Enhanced Visualization
        obj.addProperty("App::PropertyBool", "ShowLoadDistribution", "Visualization",
                       "Show load distribution pattern")
        obj.ShowLoadDistribution = False
        
        obj.addProperty("App::PropertyBool", "ShowMemberTributary", "Visualization",
                       "Show tributary areas for members")
        obj.ShowMemberTributary = False
        
        obj.addProperty("App::PropertyBool", "ShowPressureContours", "Visualization",
                       "Show pressure contour lines")
        obj.ShowPressureContours = False
        
        obj.addProperty("App::PropertyInteger", "ContourLevels", "Visualization",
                       "Number of pressure contour levels")
        obj.ContourLevels = 10
        
        obj.addProperty("App::PropertyBool", "ShowMeshElements", "Visualization",
                       "Show generated mesh elements")
        obj.ShowMeshElements = False
        
        # Transient Load Case Generation
        obj.addProperty("App::PropertyBool", "GenerateTransientCase", "Advanced",
                       "Generate transient load case for verification")
        obj.GenerateTransientCase = False
        
        obj.addProperty("App::PropertyString", "TransientCaseName", "Advanced",
                       "Name for generated transient load case")
        
        # Results and integration
        obj.addProperty("App::PropertyBool", "ProjectToSurface", "Application",
                       "Project load normal to surface")
        obj.ProjectToSurface = True
        
        obj.addProperty("App::PropertyFloat", "LoadEccentricity", "Application",
                       "Load eccentricity from surface centroid")
        obj.LoadEccentricity = 0.0
        
        obj.addProperty("App::PropertyForce", "TotalLoad", "Results",
                       "Total applied load")
        obj.TotalLoad = 0.0
        
        obj.addProperty("App::PropertyPythonObject", "MeshData", "Results",
                       "Generated mesh data for load distribution")
        obj.MeshData = {}
        
        obj.addProperty("App::PropertyPythonObject", "TributaryAreas", "Results",
                       "Calculated tributary areas for members")
        obj.TributaryAreas = {}
        
    
    
    def _create_property_adder(self, obj):
        """
        Create a helper function to safely add properties with error handling.
        
        Args:
            obj: The DocumentObject to add properties to
            
        Returns:
            A function that can be used to add properties to the object
        """
        def ensure_property_exists(prop_type, prop_name, prop_group, prop_doc, default=None):
            try:
                if not hasattr(obj, prop_name):
                    obj.addProperty(prop_type, prop_name, prop_group, prop_doc)
                    if default is not None:
                        setattr(obj, prop_name, default)
                return True
            except Exception as e:
                App.Console.PrintWarning(f"Error creating property {prop_name}: {e}\n")
                return False
        return ensure_property_exists
    
    def _create_property_helper(self, obj):
        """Create property helper function."""
        def ensure_property_exists(prop_type, prop_name, prop_group, prop_doc, default=None):
            try:
                if not hasattr(obj, prop_name):
                    obj.addProperty(prop_type, prop_name, prop_group, prop_doc)
                    if default is not None:
                        setattr(obj, prop_name, default)
                return True
            except Exception as e:
                App.Console.PrintWarning(f"Error creating property {prop_name}: {e}\n")
                return False
        return ensure_property_exists
    
    def _add_enumeration_property(self, obj, prop_name, prop_group, prop_doc, enum_list, default_value):
        """
        Safely add enumeration property - simplified approach.
        """
        try:
            if not hasattr(obj, prop_name):
                # Create string property instead of enumeration to avoid issues
                App.Console.PrintMessage(f"Creating property {prop_name} as string (fallback)\n")
                obj.addProperty("App::PropertyString", prop_name, prop_group, prop_doc)
                
                # Set default value
                if default_value:
                    setattr(obj, prop_name, default_value)
                elif enum_list:
                    setattr(obj, prop_name, enum_list[0])
                
                # Store enum list for reference (for future GUI use)
                enum_prop_name = f"{prop_name}_EnumList"
                if not hasattr(obj, enum_prop_name):
                    obj.addProperty("App::PropertyPythonObject", enum_prop_name, prop_group, 
                                   f"Available options for {prop_name}")
                    setattr(obj, enum_prop_name, enum_list)
                
                return True
            else:
                # Property exists, just try to set default if current value is empty
                try:
                    current_value = getattr(obj, prop_name)
                    if not current_value and default_value:
                        setattr(obj, prop_name, default_value)
                except:
                    pass
                return True
                
        except Exception as e:
            App.Console.PrintError(f"Error creating property {prop_name}: {e}\n")
            return False
    
    def parseLoadIntensity(self, intensity_str):
        """Parse load intensity string to numerical value."""
        try:
            if isinstance(intensity_str, (int, float)):
                return float(intensity_str)
            
            # Handle unit strings like "2.4 kN/m^2"
            value_str = str(intensity_str).split()[0]
            return float(value_str)
        except:
            return 0.0
    
    def getLoadInThaiUnits(self, obj):
        """Get load values in Thai units"""
        if not hasattr(obj, 'UseThaiUnits') or not obj.UseThaiUnits:
            return None
            
        try:
            # Import Thai units converter
            from ..utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            
            # Get load intensity in SI units
            intensity_kn_m2 = self.parseLoadIntensity(obj.LoadIntensity)
            
            # Convert to Thai units
            intensity_ksc = converter.kn_m2_to_ksc_m2(intensity_kn_m2)
            intensity_tf_m2 = converter.kn_m2_to_tf_m2(intensity_kn_m2)
            
            # Update Thai unit properties
            obj.LoadIntensityKsc = f"{intensity_ksc:.2f} kgf/m^2"
            obj.LoadIntensityTfM2 = f"{intensity_tf_m2:.3f} tf/m^2"
            
            thai_results = {
                'intensity_ksc': intensity_ksc,
                'intensity_tf_m2': intensity_tf_m2,
                'total_force_kgf': converter.kn_to_kgf(obj.TotalForce) if hasattr(obj, 'TotalForce') else 0,
                'total_force_tf': converter.kn_to_tf(obj.TotalForce) if hasattr(obj, 'TotalForce') else 0,
                'area_m2': obj.LoadedArea if hasattr(obj, 'LoadedArea') else 0,
                'load_factor_thai': obj.LoadFactorThai if hasattr(obj, 'LoadFactorThai') else 1.4
            }
            
            return thai_results
            
        except Exception as e:
            App.Console.PrintError(f"Error converting to Thai units: {e}\n")
            return None
    
    def updateThaiUnits(self, obj):
        """Update Thai units when properties change"""
        if hasattr(obj, 'UseThaiUnits') and obj.UseThaiUnits:
            self.getLoadInThaiUnits(obj)
    
    def calculateLoadProperties(self, obj):
        """Calculate basic load properties."""
        try:
            if not obj.TargetFaces:
                return
                
            # Calculate total loaded area
            total_area = 0.0
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape') and hasattr(face_obj.Shape, 'Area'):
                    total_area += face_obj.Shape.Area
                    
            obj.LoadedArea = total_area
            
            # Calculate total force
            if hasattr(obj, 'LoadIntensity'):
                intensity = self.parseLoadIntensity(obj.LoadIntensity)
                obj.TotalForce = intensity * total_area
                
            # Calculate center of pressure
            self.calculateCenterOfPressure(obj)
            
            # Update Thai units if enabled
            if hasattr(obj, 'UseThaiUnits') and obj.UseThaiUnits:
                self.updateThaiUnits(obj)
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating load properties: {e}\n")
    
    def calculateCenterOfPressure(self, obj):
        """Calculate center of pressure for the load."""
        try:
            if not obj.TargetFaces:
                return
                
            total_area = 0.0
            weighted_center = App.Vector(0, 0, 0)
            
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape') and hasattr(face_obj.Shape, 'CenterOfMass'):
                    area = face_obj.Shape.Area
                    center = face_obj.Shape.CenterOfMass
                    
                    weighted_center = weighted_center + (center * area)
                    total_area += area
            
            if total_area > 0:
                obj.CenterOfPressure = weighted_center / total_area
                
        except Exception as e:
            App.Console.PrintError(f"Error calculating center of pressure: {e}\n")
    
    def applyBuildingCodeLoads(self, obj):
        """Apply building code specific loads."""
        try:
            code = obj.BuildingCode
            load_type = obj.LoadType
            occupancy = obj.OccupancyType
            
            if code == "ASCE 7-16":
                self.applyASCE7Loads(obj, load_type, occupancy)
            elif code == "IBC 2018":
                self.applyIBCLoads(obj, load_type, occupancy)
            elif code == "Eurocode 1":
                self.applyEurocodeLoads(obj, load_type, occupancy)
                
        except Exception as e:
            App.Console.PrintError(f"Error applying building code loads: {e}\n")
    
    def applyASCE7Loads(self, obj, load_type, occupancy):
        """Apply ASCE 7-16 loads."""
        if "Dead Load" in load_type:
            # Typical dead load values
            if "concrete" in occupancy.lower():
                obj.LoadIntensity = "3.6 kN/m^2"  # 75 psf
            else:
                obj.LoadIntensity = "2.4 kN/m^2"  # 50 psf typical
                
        elif "Live Load" in load_type:
            # ASCE 7 Table 4.3-1
            live_loads = {
                "office": "2.4 kN/m^2",     # 50 psf
                "residential": "1.9 kN/m^2", # 40 psf
                "retail": "4.8 kN/m^2",     # 100 psf
                "classroom": "1.9 kN/m^2",  # 40 psf
                "corridor": "3.8 kN/m^2"    # 80 psf
            }
            
            for key, value in live_loads.items():
                if key in occupancy.lower():
                    obj.LoadIntensity = value
                    break
            else:
                obj.LoadIntensity = "2.4 kN/m^2"  # Default
                
        elif "Wind Load" in load_type:
            # Simplified wind pressure calculation
            # qz = 0.613 * Kz * Kzt * Kd * V^2 * I
            v = obj.WindSpeed  # m/s
            kz = 0.85  # Exposure factor
            kzt = 1.0  # Topographic factor
            kd = 0.85  # Directionality factor
            i = obj.ImportanceFactor
            
            qz = 0.613 * kz * kzt * kd * (v ** 2) * i / 1000  # kN/m²
            obj.LoadIntensity = f"{qz:.2f} kN/m^2"
    
    def applyIBCLoads(self, obj, load_type, occupancy):
        """Apply IBC 2018 loads."""
        # Simplified implementation
        pass

    def applyEurocodeLoads(self, obj, load_type, occupancy):
        """Apply Eurocode 1 loads."""
        # Simplified implementation
        pass

    def execute(self, obj):
        """Update load visualization and integration."""
        if obj.TargetFaces:
            # Update basic properties (updateLoadVisualization has built-in duplicate prevention)
            self.updateLoadVisualization(obj)
            self._calculate_total_load(obj)
            
            # Auto-generate mesh and calculate tributary areas if enabled
            if hasattr(obj, 'AutoValidateOnChange') and obj.AutoValidateOnChange:
                # Generate mesh if needed
                if not obj.MeshData or not obj.MeshData.get('elements'):
                    self.generateAdvancedMesh(obj)
                
                # Calculate tributary areas
                self.calculateTributaryAreas(obj)
                
                # Validate configuration
                self.validateLoadConfiguration(obj)
            
            # Create advanced visualization if enabled
            if (hasattr(obj, 'ShowLoadDistribution') and obj.ShowLoadDistribution) or \
               (hasattr(obj, 'ShowPressureContours') and obj.ShowPressureContours) or \
               (hasattr(obj, 'ShowMemberTributary') and obj.ShowMemberTributary):
                self.createAdvancedVisualization(obj)
            
            # Generate transient load case if enabled
            if hasattr(obj, 'GenerateTransientCase') and obj.GenerateTransientCase:
                self.generateTransientLoadCase(obj)
            
            # Apply performance optimizations
            try:
                self.optimizePerformance(obj)
            except AttributeError:
                # Method not available, skip optimization
                pass
    
    def updateLoadVisualization(self, obj) -> None:
        """Update visual representation of the load including distribution patterns."""
        try:
            # Check if visualization should be shown
            show_arrows = hasattr(obj, 'ShowLoadArrows') and obj.ShowLoadArrows
            
            if not show_arrows:
                self._clear_visualization(obj)
                return
            
            # Check if visualization already exists and is current
            if hasattr(obj, 'LoadVisualization') and obj.LoadVisualization:
                # Skip recreation if arrows already exist (unless forced update)
                if not hasattr(obj, '_force_visualization_update'):
                    App.Console.PrintMessage(f"Load visualization already exists for {obj.Label} - skipping recreation\n")
                    return
                else:
                    # Clear force flag
                    delattr(obj, '_force_visualization_update')
            
            # Clear existing visualization before creating new ones
            self._clear_visualization(obj)
            
            # Create load vectors
            App.Console.PrintMessage(f"Creating new load visualization for {obj.Label}\n")
            self._createLoadVectors(obj)
            
            # Show load distribution pattern if requested
            if hasattr(obj, 'ShowLoadDistribution') and obj.ShowLoadDistribution:
                self._create_load_distribution(obj)

            # Apply per-element pressure heatmap when requested
            try:
                if hasattr(obj, 'ShowPressureHeatmap') and obj.ShowPressureHeatmap:
                    # For each targeted plate, attempt to color mesh overlay objects
                    self._apply_pressure_heatmap(obj)
            except Exception as e:
                App.Console.PrintWarning(f"Heatmap generation failed: {e}\n")

        except Exception as e:
            App.Console.PrintError(f"Error updating load visualization: {e}\n")

    def _apply_pressure_heatmap(self, obj) -> None:
        """Apply a simple pressure heatmap to mesh overlay objects of targeted plates.

        This is a lightweight visualization helper that queries the plate payload and
        the area-load solver mapping (via to_solver_loads) and colors mesh features.
        """
        try:
            doc = App.ActiveDocument
            if not doc or not hasattr(obj, 'TargetFaces') or not obj.TargetFaces:
                return

            # Gather pressure entries using solver-friendly mapping
            for tgt in obj.TargetFaces:
                plate = tgt
                try:
                    # get payload from plate
                    payload = None
                    if hasattr(plate, 'Proxy') and hasattr(plate.Proxy, 'to_calc_payload'):
                        payload = plate.Proxy.to_calc_payload(plate)

                    # Ask this AreaLoad for per-element pressures if possible
                    mesh_payload = payload if payload else None
                    try:
                        loads = self.to_solver_loads(obj, mesh_payload=mesh_payload)
                    except Exception:
                        loads = {'entries': []}

                    # Build element->pressure mapping
                    pmap = {}
                    pressures = []
                    for entry in loads.get('entries', []):
                        if 'element' in entry:
                            pmap[str(entry['element'])] = float(entry.get('pressure', 0.0))
                            pressures.append(float(entry.get('pressure', 0.0)))

                    if not pmap:
                        continue

                    pmin = min(pressures) if pressures else 0.0
                    pmax = max(pressures) if pressures else 1.0
                    if pmax - pmin < 1e-9:
                        pmax = pmin + 1.0

                    # Color mesh visualization objects owned by the plate
                    if hasattr(plate, 'MeshVisualization') and plate.MeshVisualization:
                        for vis in plate.MeshVisualization:
                            try:
                                name = getattr(vis, 'Name', '')
                                # Infer element id from visualization name (expect "{PlateName}_Mesh_{eid}")
                                if not name.startswith(plate.Name + "_Mesh_"):
                                    continue
                                eid = name.split(plate.Name + "_Mesh_")[-1]
                                key = eid
                                # if exporter used numeric element names, allow full name match
                                if key not in pmap and plate.Name + "_" + key in pmap:
                                    key = plate.Name + "_" + key
                                if key not in pmap:
                                    continue
                                val = pmap[key]
                                # map val to color (blue -> red)
                                t = (val - pmin) / (pmax - pmin)
                                r = min(max(t, 0.0), 1.0)
                                b = 1.0 - r
                                g = 0.2 + 0.6 * (1.0 - abs(0.5 - t))  # small green for contrast
                                color = (r, g, b)
                                if hasattr(vis, 'ViewObject'):
                                    try:
                                        vis.ViewObject.ShapeColor = color
                                    except Exception:
                                        pass
                            except Exception:
                                continue

                except Exception:
                    continue

        except Exception as e:
            App.Console.PrintError(f"Error applying pressure heatmap: {e}\n")
            return
    
    def _createLoadVectors(self, obj) -> None:
        """Create load vector visualization."""
        try:
            doc = App.ActiveDocument
            if not doc or not obj.TargetFaces:
                return
                
            visualization_objects = []
            
            # Get load properties
            direction_vector = self._get_direction_vector(obj)
            intensity = self.parseLoadIntensity(obj.LoadIntensity) if hasattr(obj, 'LoadIntensity') else 0.0
            arrow_scale = obj.VectorScale if hasattr(obj, 'VectorScale') else 1.0
            arrow_density = obj.DisplayDensity if hasattr(obj, 'DisplayDensity') else 10
            
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    for face in face_obj.Shape.Faces:
                        # Get face boundaries
                        try:
                            u_range = face.ParameterRange[0:2]
                            v_range = face.ParameterRange[2:4]
                        except:
                            u_range = [0, 1]
                            v_range = [0, 1]
                        
                        # Get face normal at center
                        u_center = (u_range[0] + u_range[1]) / 2
                        v_center = (v_range[0] + v_range[1]) / 2
                        face_normal = face.normalAt(u_center, v_center)
                        
                        # Create arrows following load direction
                        for u_idx in range(arrow_density):
                            for v_idx in range(arrow_density):
                                u_param = u_range[0] + (u_range[1] - u_range[0]) * (u_idx + 0.5) / arrow_density
                                v_param = v_range[0] + (v_range[1] - v_range[0]) * (v_idx + 0.5) / arrow_density
                                
                                try:
                                    # Get point on surface
                                    point = face.valueAt(u_param, v_param)
                                    
                                    # Calculate projection factor
                                    proj_factor = abs(face_normal.x * direction_vector.x + 
                                                    face_normal.y * direction_vector.y + 
                                                    face_normal.z * direction_vector.z)
                                    
                                    # Create arrow with projected intensity
                                    arrow_obj = self._createArrow(doc, point, direction_vector, intensity * proj_factor, arrow_scale)
                                    if arrow_obj:
                                        visualization_objects.append(arrow_obj)
                                except Exception as e:
                                    continue  # Skip problematic points
            
            # Store visualization objects in the object
            obj.LoadVisualization = visualization_objects
            
            # Add load distribution direction visualization if applicable
            if hasattr(obj, 'LoadDistribution') and obj.LoadDistribution == "OneWay":
                direction_arrows = self._createLoadDistributionVisualization(obj)
                if direction_arrows:
                    obj.LoadVisualization.extend(direction_arrows)
        
        except Exception as e:
            App.Console.PrintError(f"Error creating load vectors: {e}\n")
    
    def _createArrow(self, doc, position, direction, magnitude, scale):
        """Create a load arrow with tip positioned on face surface."""
        try:
            # Calculate arrow length based on magnitude and scale
            arrow_length = magnitude * scale * 100  # Scale factor in mm
            if arrow_length < 50:  # Minimum length for visibility
                arrow_length = 50
            
            # Create arrow parts
            arrow_radius = arrow_length * 0.02  # Arrow shaft radius (thinner)
            head_radius = arrow_radius * 4     # Arrow head radius
            head_length = arrow_length * 0.25  # Arrow head length
            
            # IMPORTANT: Position arrow so tip is ON the surface, shaft extends outward
            # Normalize direction vector
            dir_length = direction.Length
            if dir_length > 0:
                unit_direction = App.Vector(direction.x/dir_length, direction.y/dir_length, direction.z/dir_length)
            else:
                unit_direction = App.Vector(0, 0, -1)  # Default downward
            
            # Arrow tip position (ON the face surface)
            arrow_tip = position
            
            # Arrow base position (extends outward from face)
            arrow_base = position - unit_direction * arrow_length
            
            # Create arrow shaft (from base to near tip)
            shaft_end = arrow_tip - unit_direction * head_length
            shaft = Part.makeCylinder(arrow_radius, arrow_length - head_length, arrow_base, unit_direction)
            
            # Create arrow head (cone pointing in load direction)
            head = Part.makeCone(head_radius, 0, head_length, shaft_end, unit_direction)
            
            # Combine shaft and head
            arrow = Part.makeCompound([shaft, head])
            
            # Create arrow object
            arrow_name = f"LoadArrow_{len(doc.Objects)}"
            arrow_obj = doc.addObject("Part::Feature", arrow_name)
            arrow_obj.Shape = arrow
            
            # Set visual properties
            if hasattr(arrow_obj, 'ViewObject'):
                color = (0.8, 0.0, 0.8)  # Purple for load arrows
                arrow_obj.ViewObject.ShapeColor = color
                arrow_obj.ViewObject.LineColor = color
            
            return arrow_obj
        
        except Exception as e:
            App.Console.PrintWarning(f"Error creating arrow: {e}\n")
            return None
    
    def _createLoadDistributionVisualization(self, obj):
        """Create visualization arrows showing load distribution direction."""
        try:
            doc = App.ActiveDocument
            if not doc or not obj.TargetFaces:
                return []
            
            distribution_arrows = []
            
            # Get distribution direction
            distribution_dir = self._getLoadDistributionDirection(obj)
            if not distribution_dir:
                return []
            
            # Create distribution direction arrows on face edges
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    for face in face_obj.Shape.Faces:
                        # Get face center
                        face_center = face.CenterOfMass
                        
                        # Create larger directional arrow showing load transfer direction
                        arrow_length = 300  # mm - larger than load arrows
                        arrow_radius = 5    # mm - thicker than load arrows
                        
                        # Create arrow shaft
                        shaft_start = face_center - distribution_dir * (arrow_length / 2)
                        shaft_end = face_center + distribution_dir * (arrow_length / 2)
                        shaft = Part.makeCylinder(arrow_radius, arrow_length, shaft_start, distribution_dir)
                        
                        # Create arrow heads at both ends
                        head_length = arrow_length * 0.15
                        head_radius = arrow_radius * 3
                        
                        # Arrow head at positive end
                        head_pos = shaft_end - distribution_dir * head_length
                        head1 = Part.makeCone(head_radius, 0, head_length, head_pos, distribution_dir)
                        
                        # Arrow head at negative end (reversed)
                        head_neg = shaft_start + distribution_dir * head_length
                        head2 = Part.makeCone(head_radius, 0, head_length, head_neg, -distribution_dir)
                        
                        # Combine parts
                        direction_arrow = Part.makeCompound([shaft, head1, head2])
                        
                        # Create FreeCAD object
                        arrow_obj = doc.addObject("Part::Feature", f"LoadDistribution_{obj.Label}_{len(distribution_arrows)}")
                        arrow_obj.Shape = direction_arrow
                        
                        # Set appearance (different color from load arrows)
                        if hasattr(arrow_obj, 'ViewObject'):
                            arrow_obj.ViewObject.ShapeColor = (0.0, 0.8, 0.2)  # Green for distribution direction
                            arrow_obj.ViewObject.Transparency = 30
                        
                        distribution_arrows.append(arrow_obj)
                        
                        # Add text label showing distribution method
                        text_pos = face_center + App.Vector(0, 0, 100)  # Offset upward
                        self._createDistributionLabel(doc, text_pos, obj.LoadDistribution, obj.OneWayDirection if hasattr(obj, 'OneWayDirection') else "")
            
            App.Console.PrintMessage(f"Created {len(distribution_arrows)} load distribution arrows for {obj.Label}\n")
            return distribution_arrows
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating load distribution visualization: {e}\n")
            return []
    
    def _getLoadDistributionDirection(self, obj):
        """Get the load distribution direction vector."""
        try:
            if not hasattr(obj, 'LoadDistribution') or obj.LoadDistribution != "OneWay":
                return None
            
            if hasattr(obj, 'OneWayDirection'):
                oneway_dir = obj.OneWayDirection
                
                if oneway_dir == "X":
                    return App.Vector(1, 0, 0)
                elif oneway_dir == "Y":
                    return App.Vector(0, 1, 0)
                elif oneway_dir == "Custom":
                    if hasattr(obj, 'CustomDistributionDirection'):
                        custom_dir = obj.CustomDistributionDirection
                        # Normalize the vector
                        length = custom_dir.Length
                        if length > 0:
                            return App.Vector(custom_dir.x/length, custom_dir.y/length, custom_dir.z/length)
            
            # Default to X direction
            return App.Vector(1, 0, 0)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error getting load distribution direction: {e}\n")
            return None
    
    def _createDistributionLabel(self, doc, position, method, direction):
        """Create text label for distribution method."""
        try:
            # Create text annotation showing distribution info
            label_text = f"{method}"
            if method == "OneWay" and direction:
                label_text += f" ({direction})"
            
            # For now, we'll skip text creation as it requires additional FreeCAD text features
            # This could be enhanced later with proper text annotations
            App.Console.PrintMessage(f"Distribution method: {label_text} at {position}\n")
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating distribution label: {e}\n")
    
    def _clear_visualization(self, obj) -> None:
        """Clear existing load visualization objects efficiently."""
        try:
            doc = App.ActiveDocument
            if not doc:
                return
            
            # Method 1: Remove from LoadVisualization property
            if hasattr(obj, 'LoadVisualization') and obj.LoadVisualization:
                for vis_obj in obj.LoadVisualization:
                    try:
                        if vis_obj and hasattr(vis_obj, 'Name'):
                            if doc.getObject(vis_obj.Name):
                                doc.removeObject(vis_obj.Name)
                    except:
                        continue
                obj.LoadVisualization = []
            
            # Method 2: Remove by name pattern (more thorough cleanup)
            all_objects = doc.Objects
            arrows_to_remove = []
            
            # Find all LoadArrow objects related to this AreaLoad
            area_load_label = obj.Label if hasattr(obj, 'Label') else 'AreaLoad'
            
            for obj_in_doc in all_objects:
                if hasattr(obj_in_doc, 'Label') and obj_in_doc.Label:
                    # Match LoadArrow patterns
                    if (obj_in_doc.Label.startswith('LoadArrow_') or 
                        obj_in_doc.Label.startswith(f'LoadArrow_{area_load_label}') or
                        (hasattr(obj_in_doc, 'Name') and obj_in_doc.Name.startswith('LoadArrow'))):
                        arrows_to_remove.append(obj_in_doc.Name)
                    # Also match LoadDistribution patterns
                    elif (obj_in_doc.Label.startswith('LoadDistribution_') or
                          obj_in_doc.Label.startswith(f'LoadDistribution_{area_load_label}') or
                          (hasattr(obj_in_doc, 'Name') and obj_in_doc.Name.startswith('LoadDistribution'))):
                        arrows_to_remove.append(obj_in_doc.Name)
            
            # Remove found arrows
            for arrow_name in arrows_to_remove:
                try:
                    if doc.getObject(arrow_name):
                        doc.removeObject(arrow_name)
                except:
                    continue
            
            if arrows_to_remove:
                App.Console.PrintMessage(f"Cleared {len(arrows_to_remove)} existing load arrows for {area_load_label}\n")
        
        except Exception as e:
            App.Console.PrintWarning(f"Error clearing visualization: {e}\n")
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        # Ensure the property-adder helper exists (some existing objects may miss initialization)
        if not hasattr(self, '_ensure_property_exists'):
            try:
                self._ensure_property_exists = self._create_property_adder(obj)
            except Exception:
                # Fallback: define a minimal adder that only adds property if missing
                def _fallback_adder(prop_type, prop_name, prop_group, prop_doc, default=None):
                    try:
                        if not hasattr(obj, prop_name):
                            obj.addProperty(prop_type, prop_name, prop_group, prop_doc)
                            if default is not None:
                                try:
                                    setattr(obj, prop_name, default)
                                except Exception:
                                    pass
                        return True
                    except Exception:
                        return False
                self._ensure_property_exists = _fallback_adder

        # Ensure critical properties exist (use the safe adder)
        try:
            if not hasattr(obj, 'LoadCategory'):
                self._ensure_property_exists("App::PropertyString", "LoadCategory", "Load",
                           "Load category for combinations", "DL")
        except Exception:
            pass

        try:
            if not hasattr(obj, 'ShowLoadArrows'):
                self._ensure_property_exists("App::PropertyBool", "ShowLoadArrows", "Display",
                           "Show load arrows", True)
            if not hasattr(obj, 'LoadVisualization'):
                self._ensure_property_exists("App::PropertyPythonObject", "LoadVisualization", "Display",
                           "Load visualization objects", [])
        except Exception:
            pass

        try:
            if not hasattr(obj, 'LoadCenter'):
                self._ensure_property_exists("App::PropertyVector", "LoadCenter", "Application",
                           "Center point of the load application", App.Vector(0, 0, 0))
        except Exception:
            pass
        
        # Handle property changes
        if prop == "TargetFaces":
            self._update_loaded_area(obj)
            self._update_load_center(obj)
        elif prop == "LoadType":
            self._update_load_category(obj)
        elif prop in ["Magnitude", "Distribution", "DistributionParameters"]:
            self._calculate_total_load(obj)
        elif prop == "Direction":
            self._update_direction_vector(obj)
        elif prop == "LoadDistribution":
            # Handle changes in load distribution method
            self._update_distribution_visualization(obj)
        elif prop == "OneWayDirection":
            # Update custom direction when one-way direction changes
            self._update_one_way_direction(obj)
        elif hasattr(obj, 'ShowLoadArrows') and prop == "ShowLoadArrows":
            # Force visualization update when ShowLoadArrows changes
            try:
                obj._force_visualization_update = True
            except AttributeError:
                # Create the attribute if it doesn't exist
                setattr(obj, '_force_visualization_update', True)
            self._update_visualization(obj)
        elif prop in ["ArrowDensity", "ArrowScale", "LoadIntensity", "Direction"]:
            if hasattr(obj, 'ShowLoadArrows') and obj.ShowLoadArrows:
                # Force visualization update for visual properties
                try:
                    obj._force_visualization_update = True
                except AttributeError:
                    # Create the attribute if it doesn't exist
                    setattr(obj, '_force_visualization_update', True)
                self._update_visualization(obj)
        elif prop in ["MeshSize", "AdaptiveMeshing", "MeshType", "DistributionMethod"]:
            # Regenerate mesh when meshing parameters change
            if hasattr(obj, 'AutoValidateOnChange') and obj.AutoValidateOnChange:
                self.generateAdvancedMesh(obj)
                self.calculateTributaryAreas(obj)
        elif prop in ["IncludeBeams", "IncludeColumns", "IncludeBraces", "IncludeTrusses", "IncludeGravityMembers", "MemberInfluenceRadius"]:
            # Recalculate tributary areas when member filtering changes
            if hasattr(obj, 'AutoValidateOnChange') and obj.AutoValidateOnChange:
                self.calculateTributaryAreas(obj)
        elif hasattr(obj, 'AutoValidateOnChange') and obj.AutoValidateOnChange and prop in ["LoadIntensity", "Direction", "LoadType", "LoadCategory"]:
            # Auto-validate when critical properties change
            self.validateLoadConfiguration(obj)
    
    def _update_loaded_area(self, obj) -> None:
        """Calculate total loaded area from target faces."""
        if not hasattr(obj, 'TargetFaces') or not obj.TargetFaces:
            obj.LoadedArea = "0 mm^2"
            return
        
        total_area = 0.0
        for face_obj in obj.TargetFaces:
            if hasattr(face_obj, 'Shape'):
                shape = face_obj.Shape
                if hasattr(shape, 'Faces'):
                    for face in shape.Faces:
                        total_area += face.Area
                elif hasattr(shape, 'Area'):
                    total_area += shape.Area
        
        obj.LoadedArea = f"{total_area} mm^2"
        App.Console.PrintMessage(f"Updated loaded area: {total_area:.2f} mm²\n")
    
    def _update_load_category(self, obj) -> None:
        """Update load category based on load type."""
        if not hasattr(obj, 'LoadType') or not hasattr(obj, 'LoadCategory'):
            return
        
        load_type = obj.LoadType
        category_map = {
            "Dead Load (DL)": "DL",
            "Live Load (LL)": "LL", 
            "Live Load Roof (LL_Roof)": "LL_Roof",
            "Wind Load (W)": "W",
            "Earthquake (E)": "E",
            "Earth Pressure (H)": "H",
            "Fluid Pressure (F)": "F",
            "Thermal (T)": "T",
            "Custom Pressure": "CUSTOM"
        }
        if load_type in category_map:
            target = category_map[load_type]
            try:
                obj.LoadCategory = target
                App.Console.PrintMessage(f"Set LoadCategory to: {target}\n")
            except Exception as e:
                App.Console.PrintWarning(f"Could not set LoadCategory to '{target}': {e}\n")
    
    def _calculate_total_load(self, obj):
        """Calculate total load and moments."""
        # Simplified implementation
        pass

    def _create_load_distribution(self, obj) -> None:
        """Create visual representation of load distribution pattern."""
        # Simplified implementation
        pass

    def _get_distribution_factor(self, obj) -> float:
        """Get distribution factor based on distribution type."""
        if not hasattr(obj, 'Distribution'):
            return 1.0
        
        distribution = obj.Distribution
        
        if distribution == "Uniform":
            return 1.0
        elif distribution in ["Linear X", "Linear Y"]:
            # For linear distribution, average is 0.5 * (min + max)
            # Assuming parameters are [min_factor, max_factor]
            if len(obj.DistributionParameters) >= 2:
                return 0.5 * (obj.DistributionParameters[0] + obj.DistributionParameters[1])
            return 1.0
        elif distribution == "Parabolic":
            # For parabolic distribution, integrate over area
            return 2.0/3.0  # Simplified
        elif distribution == "Point Load":
            return 1.0  # Full load at a point
        else:
            return 1.0
    
    def _update_distribution_visualization(self, obj) -> None:
        """Update visualization based on load distribution method."""
        if not hasattr(obj, 'LoadDistribution'):
            return
            
        # Clear existing visualization
        self._clear_visualization(obj)
        
        # Update visualization based on distribution method
        if hasattr(obj, 'ShowLoadArrows') and obj.ShowLoadArrows:
            self._create_load_arrows(obj)
            
        # Calculate edge factors based on distribution method
        if hasattr(obj, 'EdgeDistributionFactors'):
            if obj.LoadDistribution == "OneWay":
                # For one-way distribution, calculate edge factors based on direction
                self._calculate_one_way_edge_factors(obj)
            elif obj.LoadDistribution == "TwoWay":
                # For two-way distribution, calculate tributary areas
                self._calculate_two_way_edge_factors(obj)
            elif obj.LoadDistribution == "OpenStructure":
                # For open structure, use projected area
                self._calculate_projected_edge_factors(obj)
    
    def _update_one_way_direction(self, obj) -> None:
        """Update custom direction vector based on one-way direction selection."""
        if not hasattr(obj, 'OneWayDirection') or not hasattr(obj, 'CustomDistributionDirection'):
            return
            
        # Set default direction vector based on selection
        if obj.OneWayDirection == "X":
            obj.CustomDistributionDirection = App.Vector(1, 0, 0)
        elif obj.OneWayDirection == "Y":
            obj.CustomDistributionDirection = App.Vector(0, 1, 0)
            
        # Update visualization
        self._update_distribution_visualization(obj)
    
    def _update_direction_vector(self, obj) -> None:
        """Update direction vector when direction changes."""
        self._calculate_total_load(obj)
    
    def _update_load_center(self, obj) -> None:
        """Calculate center of load application."""
        if not hasattr(obj, 'TargetFaces') or not obj.TargetFaces or not hasattr(obj, 'LoadCenter'):
            if hasattr(obj, 'LoadCenter'):
                obj.LoadCenter = App.Vector(0, 0, 0)
            return
        
        total_area = 0.0
        weighted_center = App.Vector(0, 0, 0)
        
        for face_obj in obj.TargetFaces:
            if hasattr(face_obj, 'Shape'):
                shape = face_obj.Shape
                if hasattr(shape, 'Faces'):
                    for face in shape.Faces:
                        area = face.Area
                        center = face.CenterOfMass
                        weighted_center = weighted_center + (center * area)
                        total_area += area
        
        if total_area > 0:
            obj.LoadCenter = weighted_center * (1.0 / total_area)
        else:
            obj.LoadCenter = App.Vector(0, 0, 0)
    
    def _update_visualization(self, obj) -> None:
        """Update load arrow visualization."""
        if not hasattr(obj, 'ShowLoadArrows') or not obj.ShowLoadArrows:
            self._clear_visualization(obj)
            return
        
        self._create_load_arrows(obj)
    
    def _create_load_arrows(self, obj) -> None:
        """Create 3D arrows for load visualization."""
        if not hasattr(obj, 'TargetFaces') or not obj.TargetFaces:
            return
        
        self._clear_visualization(obj)
        
        direction_vector = self._get_direction_vector(obj)
        magnitude = obj.Magnitude.getValueAs('N/mm^2') if hasattr(obj, 'Magnitude') else 0.0
        
        # For now, we'll just print a message that visualization would be created
        App.Console.PrintMessage(f"Load visualization would be created for {len(obj.TargetFaces)} faces\n")
    
    def _get_direction_vector(self, obj) -> App.Vector:
        """Get normalized direction vector for load."""
        if not hasattr(obj, 'Direction'):
            return App.Vector(0, 0, -1)
        
        direction = obj.Direction
        
        if direction == "Normal":
            return self._get_surface_normal(obj)
        elif direction == "+X Global":
            return App.Vector(1, 0, 0)
        elif direction == "-X Global":
            return App.Vector(-1, 0, 0)
        elif direction == "+Y Global":
            return App.Vector(0, 1, 0)
        elif direction == "-Y Global":
            return App.Vector(0, -1, 0)
        elif direction == "+Z Global":
            return App.Vector(0, 0, 1)
        elif direction == "-Z Global":
            return App.Vector(0, 0, -1)
        elif direction == "Custom":
            if hasattr(obj, 'CustomDirection'):
                custom = obj.CustomDirection
                # Normalize the vector
                length = math.sqrt(custom.x**2 + custom.y**2 + custom.z**2)
                if length > 0:
                    return App.Vector(custom.x/length, custom.y/length, custom.z/length)
            return App.Vector(0, 0, -1)
        else:
            return App.Vector(0, 0, -1)
    
    def _get_surface_normal(self, obj) -> App.Vector:
        """Get average surface normal from target faces."""
        if not hasattr(obj, 'TargetFaces') or not obj.TargetFaces:
            return App.Vector(0, 0, -1)
        
        total_normal = App.Vector(0, 0, 0)
        face_count = 0
        
        for face_obj in obj.TargetFaces:
            if hasattr(face_obj, 'Shape'):
                shape = face_obj.Shape
                if hasattr(shape, 'Faces'):
                    for face in shape.Faces:
                        try:
                            normal = face.normalAt(0.5, 0.5)  # Normal at center
                            total_normal = total_normal + normal
                            face_count += 1
                        except:
                            continue
        
        if face_count > 0:
            avg_normal = total_normal * (1.0 / face_count)
            length = math.sqrt(avg_normal.x**2 + avg_normal.y**2 + avg_normal.z**2)
            if length > 0:
                return App.Vector(avg_normal.x/length, avg_normal.y/length, avg_normal.z/length)
        
        return App.Vector(0, 0, -1)
    
    def _calculate_one_way_edge_factors(self, obj) -> None:
        """Calculate edge distribution factors for one-way load distribution."""
        # Placeholder implementation
        pass
    
    def _calculate_two_way_edge_factors(self, obj) -> None:
        """Calculate edge distribution factors for two-way load distribution."""
        # Placeholder implementation
        pass
    
    def _calculate_projected_edge_factors(self, obj) -> None:
        """Calculate edge distribution factors for open structure load distribution."""
        # Placeholder implementation
        pass
    
    # ===== ADVANCED MESHING SYSTEM =====
    
    def generateAdvancedMesh(self, obj):
        """Generate advanced mesh for load distribution based on RISA-3D methodology."""
        try:
            if not obj.TargetFaces:
                return None
            
            mesh_data = {
                'elements': {},
                'nodes': {},
                'element_areas': {},
                'element_centroids': {},
                'mesh_quality': {}
            }
            
            element_id = 0
            node_id = 0
            
            for face_obj in obj.TargetFaces:
                if not hasattr(face_obj, 'Shape'):
                    continue
                    
                for face in face_obj.Shape.Faces:
                    # Calculate appropriate mesh size
                    target_size = self._calculateOptimalMeshSize(obj, face)
                    
                    # Generate mesh based on type
                    if obj.MeshType == "Adaptive":
                        face_mesh = self._generateAdaptiveMesh(face, target_size, obj)
                    elif obj.MeshType == "Triangular":
                        face_mesh = self._generateTriangularMesh(face, target_size)
                    elif obj.MeshType == "Quadrilateral":
                        face_mesh = self._generateQuadMesh(face, target_size)
                    else:  # Mixed
                        face_mesh = self._generateMixedMesh(face, target_size)
                    
                    # Validate mesh quality
                    quality = self._validateMeshQuality(face_mesh)
                    
                    # Add to overall mesh data
                    for elem in face_mesh['elements']:
                        mesh_data['elements'][element_id] = elem
                        mesh_data['element_areas'][element_id] = elem['area']
                        mesh_data['element_centroids'][element_id] = elem['centroid']
                        element_id += 1
                    
                    for node in face_mesh['nodes']:
                        mesh_data['nodes'][node_id] = node
                        node_id += 1
                    
                    mesh_data['mesh_quality'][face_obj.Name] = quality
            
            # Store mesh data
            obj.MeshData = mesh_data
            
            # Calculate mesh statistics
            self._calculateMeshStatistics(obj, mesh_data)
            
            return mesh_data
            
        except Exception as e:
            App.Console.PrintError(f"Error generating advanced mesh: {e}\n")
            return None
    
    def _calculateOptimalMeshSize(self, obj, face):
        """Calculate optimal mesh size based on face geometry and settings."""
        try:
            # Get face area and dimensions
            area = face.Area
            bbox = face.BoundBox
            max_dim = max(bbox.XLength, bbox.YLength)
            min_dim = min(bbox.XLength, bbox.YLength)
            
            # Base size from user settings
            base_size = obj.MeshSize
            
            # Adaptive sizing
            if obj.AdaptiveMeshing:
                # Adjust based on face aspect ratio
                aspect_ratio = max_dim / min_dim if min_dim > 0 else 1.0
                
                if aspect_ratio > 3.0:  # Long narrow face
                    base_size = min(base_size, min_dim / 3)
                elif aspect_ratio < 0.5:  # Unusual aspect ratio
                    base_size = min(base_size, max_dim / 5)
                
                # Ensure minimum/maximum element counts
                estimated_elements = area / (base_size * base_size)
                
                if estimated_elements < obj.MinMeshElements:
                    base_size = math.sqrt(area / obj.MinMeshElements)
                elif estimated_elements > obj.MaxMeshElements:
                    base_size = math.sqrt(area / obj.MaxMeshElements)
            
            return base_size
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating mesh size: {e}\n")
            return obj.MeshSize
    
    def _generateAdaptiveMesh(self, face, target_size, obj):
        """Generate adaptive mesh with quality control."""
        try:
            # Simple triangular mesh with adaptive refinement
            mesh_elements = []
            mesh_nodes = []
            
            # Get face parameter ranges
            u_range = face.ParameterRange[0:2]
            v_range = face.ParameterRange[2:4]
            
            # Calculate grid density
            bbox = face.BoundBox
            u_divisions = max(3, int(bbox.XLength / target_size))
            v_divisions = max(3, int(bbox.YLength / target_size))
            
            # Generate grid points
            node_id = 0
            nodes_grid = {}
            
            for i in range(u_divisions + 1):
                for j in range(v_divisions + 1):
                    u = u_range[0] + (u_range[1] - u_range[0]) * i / u_divisions
                    v = v_range[0] + (v_range[1] - v_range[0]) * j / v_divisions
                    
                    try:
                        point = face.valueAt(u, v)
                        nodes_grid[(i, j)] = {
                            'id': node_id,
                            'point': point,
                            'u': u, 'v': v
                        }
                        mesh_nodes.append(nodes_grid[(i, j)])
                        node_id += 1
                    except:
                        continue
            
            # Generate triangular elements
            element_id = 0
            for i in range(u_divisions):
                for j in range(v_divisions):
                    # Create two triangles per grid cell
                    corners = [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
                    valid_corners = [c for c in corners if c in nodes_grid]
                    
                    if len(valid_corners) >= 3:
                        # First triangle
                        if len(valid_corners) >= 3:
                            elem = {
                                'id': element_id,
                                'nodes': [nodes_grid[valid_corners[0]], 
                                         nodes_grid[valid_corners[1]], 
                                         nodes_grid[valid_corners[2]]],
                                'type': 'triangle'
                            }
                            elem['area'] = self._calculateTriangleArea(elem['nodes'])
                            elem['centroid'] = self._calculateTriangleCentroid(elem['nodes'])
                            mesh_elements.append(elem)
                            element_id += 1
                        
                        # Second triangle (if quad)
                        if len(valid_corners) == 4:
                            elem = {
                                'id': element_id,
                                'nodes': [nodes_grid[valid_corners[0]], 
                                         nodes_grid[valid_corners[2]], 
                                         nodes_grid[valid_corners[3]]],
                                'type': 'triangle'
                            }
                            elem['area'] = self._calculateTriangleArea(elem['nodes'])
                            elem['centroid'] = self._calculateTriangleCentroid(elem['nodes'])
                            mesh_elements.append(elem)
                            element_id += 1
            
            return {
                'elements': mesh_elements,
                'nodes': mesh_nodes,
                'type': 'adaptive_triangular'
            }
            
        except Exception as e:
            App.Console.PrintError(f"Error generating adaptive mesh: {e}\n")
            return {'elements': [], 'nodes': [], 'type': 'error'}
    
    def _calculateTriangleArea(self, nodes):
        """Calculate area of triangle from three nodes."""
        if len(nodes) < 3:
            return 0.0
        
        p1 = nodes[0]['point']
        p2 = nodes[1]['point']
        p3 = nodes[2]['point']
        
        # Vector cross product for area
        v1 = p2 - p1
        v2 = p3 - p1
        cross = v1.cross(v2)
        
        return cross.Length / 2.0
    
    def _calculateTriangleCentroid(self, nodes):
        """Calculate centroid of triangle."""
        if len(nodes) < 3:
            return App.Vector(0, 0, 0)
        
        p1 = nodes[0]['point']
        p2 = nodes[1]['point']
        p3 = nodes[2]['point']
        
        return App.Vector(
            (p1.x + p2.x + p3.x) / 3.0,
            (p1.y + p2.y + p3.y) / 3.0,
            (p1.z + p2.z + p3.z) / 3.0
        )
    
    def _generateTriangularMesh(self, face, target_size):
        """Generate triangular mesh."""
        # Simplified triangular meshing
        return self._generateAdaptiveMesh(face, target_size, None)
    
    def _generateQuadMesh(self, face, target_size):
        """Generate quadrilateral mesh."""
        # Placeholder for quad meshing
        return self._generateAdaptiveMesh(face, target_size, None)
    
    def _generateMixedMesh(self, face, target_size):
        """Generate mixed element mesh."""
        # Placeholder for mixed meshing
        return self._generateAdaptiveMesh(face, target_size, None)
    
    def _validateMeshQuality(self, mesh_data):
        """Validate mesh quality metrics."""
        try:
            quality_metrics = {
                'total_elements': len(mesh_data['elements']),
                'total_nodes': len(mesh_data['nodes']),
                'min_element_area': float('inf'),
                'max_element_area': 0.0,
                'avg_element_area': 0.0,
                'aspect_ratios': [],
                'quality_score': 0.0
            }
            
            total_area = 0.0
            for element in mesh_data['elements']:
                area = element['area']
                total_area += area
                
                quality_metrics['min_element_area'] = min(quality_metrics['min_element_area'], area)
                quality_metrics['max_element_area'] = max(quality_metrics['max_element_area'], area)
            
            if quality_metrics['total_elements'] > 0:
                quality_metrics['avg_element_area'] = total_area / quality_metrics['total_elements']
                
                # Calculate quality score (0-100)
                area_uniformity = 1.0 - (quality_metrics['max_element_area'] - quality_metrics['min_element_area']) / quality_metrics['max_element_area'] if quality_metrics['max_element_area'] > 0 else 1.0
                quality_metrics['quality_score'] = area_uniformity * 100.0
            
            return quality_metrics
            
        except Exception as e:
            App.Console.PrintError(f"Error validating mesh quality: {e}\n")
            return {'quality_score': 0.0}
    
    def _calculateMeshStatistics(self, obj, mesh_data):
        """Calculate and display mesh statistics."""
        try:
            total_elements = len(mesh_data['elements'])
            total_nodes = len(mesh_data['nodes'])
            
            if total_elements == 0:
                return
            
            avg_element_size = sum(mesh_data['element_areas'].values()) / total_elements if mesh_data['element_areas'] else 0.0
            
            App.Console.PrintMessage(f"Mesh Statistics for {obj.Label}:\n")
            App.Console.PrintMessage(f"  Total Elements: {total_elements}\n")
            App.Console.PrintMessage(f"  Total Nodes: {total_nodes}\n")
            App.Console.PrintMessage(f"  Average Element Size: {avg_element_size:.2f} mm²\n")
            
            # Check mesh quality
            overall_quality = 0.0
            quality_count = 0
            
            for face_name, quality in mesh_data['mesh_quality'].items():
                if 'quality_score' in quality:
                    overall_quality += quality['quality_score']
                    quality_count += 1
                    App.Console.PrintMessage(f"  {face_name} Quality: {quality['quality_score']:.1f}%\n")
            
            if quality_count > 0:
                overall_quality /= quality_count
                App.Console.PrintMessage(f"  Overall Mesh Quality: {overall_quality:.1f}%\n")
                
                if overall_quality < 70.0:
                    App.Console.PrintWarning(f"Mesh quality is below recommended threshold (70%)\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating mesh statistics: {e}\n")
    
    # ===== LOAD VALIDATION FRAMEWORK =====
    
    def validateLoadConfiguration(self, obj):
        """Comprehensive load validation based on RISA-3D standards."""
        try:
            validation_results = {
                'is_valid': True,
                'warnings': [],
                'errors': [],
                'checks': {
                    'coplanarity': self._checkCoplanarity(obj),
                    'load_magnitude': self._checkLoadMagnitude(obj),
                    'tributary_areas': self._checkTributaryAreas(obj),
                    'member_attribution': self._checkMemberAttribution(obj),
                    'load_direction': self._checkLoadDirection(obj),
                    'mesh_quality': self._checkMeshQuality(obj)
                }
            }
            
            # Compile warnings and errors
            for check_name, check_result in validation_results['checks'].items():
                if not check_result['passed']:
                    if check_result['severity'] == 'error':
                        validation_results['errors'].append(f"{check_name}: {check_result['message']}")
                        validation_results['is_valid'] = False
                    else:
                        validation_results['warnings'].append(f"{check_name}: {check_result['message']}")
            
            # Store validation results
            obj.LoadValidation = validation_results
            
            # Display results if warnings enabled
            if obj.ShowValidationWarnings and (validation_results['warnings'] or validation_results['errors']):
                self._displayValidationResults(obj, validation_results)
            
            return validation_results
            
        except Exception as e:
            App.Console.PrintError(f"Error during load validation: {e}\n")
            return {'is_valid': False, 'errors': [f'Validation failed: {e}']}
    
    def _checkCoplanarity(self, obj):
        """Check if target faces are reasonably coplanar."""
        try:
            if not obj.TargetFaces or len(obj.TargetFaces) < 2:
                return {'passed': True, 'message': 'Single face - coplanarity N/A', 'severity': 'info'}
            
            if not obj.UseCoplanarProjection:
                return {'passed': True, 'message': 'Coplanar projection disabled', 'severity': 'info'}
            
            # Get reference normal from first face
            reference_normal = None
            tolerance = obj.ProjectionTolerance
            
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    for face in face_obj.Shape.Faces:
                        try:
                            normal = face.normalAt(0.5, 0.5)
                            if reference_normal is None:
                                reference_normal = normal
                            else:
                                # Check angle between normals
                                angle = math.degrees(reference_normal.getAngle(normal))
                                if angle > tolerance:
                                    return {
                                        'passed': False,
                                        'message': f'Faces not coplanar - angle difference: {angle:.1f}°',
                                        'severity': 'warning'
                                    }
                        except:
                            continue
            
            return {'passed': True, 'message': 'Faces are reasonably coplanar', 'severity': 'info'}
            
        except Exception as e:
            return {'passed': False, 'message': f'Coplanarity check failed: {e}', 'severity': 'error'}
    
    def _checkLoadMagnitude(self, obj):
        """Check if load magnitude is reasonable."""
        try:
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            
            # Reasonable ranges for different load types
            load_ranges = {
                'DL': (0.5, 15.0),    # kN/m² - Dead load
                'LL': (0.5, 25.0),    # kN/m² - Live load  
                'W': (0.1, 5.0),      # kN/m² - Wind load
                'E': (0.1, 2.0),      # kN/m² - Seismic
                'H': (1.0, 50.0),     # kN/m² - Earth pressure
                'F': (1.0, 100.0),    # kN/m² - Fluid pressure
                'T': (0.0, 5.0)       # kN/m² - Thermal
            }
            
            category = obj.LoadCategory if hasattr(obj, 'LoadCategory') else 'LL'
            min_val, max_val = load_ranges.get(category, (0.1, 50.0))
            
            if intensity < min_val:
                return {
                    'passed': False,
                    'message': f'Load intensity ({intensity:.2f} kN/m²) unusually low for {category}',
                    'severity': 'warning'
                }
            elif intensity > max_val:
                return {
                    'passed': False,
                    'message': f'Load intensity ({intensity:.2f} kN/m²) unusually high for {category}',
                    'severity': 'warning'
                }
            else:
                return {'passed': True, 'message': f'Load magnitude reasonable for {category}', 'severity': 'info'}
                
        except Exception as e:
            return {'passed': False, 'message': f'Load magnitude check failed: {e}', 'severity': 'error'}
    
    def _checkTributaryAreas(self, obj):
        """Check tributary area calculations."""
        try:
            if not obj.TargetFaces:
                return {'passed': False, 'message': 'No target faces defined', 'severity': 'error'}
            
            total_area = 0.0
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    total_area += face_obj.Shape.Area
            
            if total_area <= 0:
                return {'passed': False, 'message': 'Zero or negative total area', 'severity': 'error'}
            
            # Check for reasonable area size
            if total_area < 1000:  # Less than 1m²
                return {
                    'passed': False,
                    'message': f'Very small loaded area: {total_area:.2f} mm²',
                    'severity': 'warning'
                }
            elif total_area > 1e9:  # More than 1000 m²
                return {
                    'passed': False,
                    'message': f'Very large loaded area: {total_area:.2f} mm²',
                    'severity': 'warning'
                }
            
            return {'passed': True, 'message': f'Tributary area acceptable: {total_area:.2f} mm²', 'severity': 'info'}
            
        except Exception as e:
            return {'passed': False, 'message': f'Tributary area check failed: {e}', 'severity': 'error'}
    
    def _checkMemberAttribution(self, obj):
        """Check member attribution settings."""
        try:
            # Check if any member types are included
            include_any = (obj.IncludeBeams or obj.IncludeColumns or 
                          obj.IncludeBraces or obj.IncludeTrusses or 
                          obj.IncludeGravityMembers)
            
            if not include_any:
                return {
                    'passed': False,
                    'message': 'No member types selected for load attribution',
                    'severity': 'error'
                }
            
            # Check influence radius
            if obj.MemberInfluenceRadius <= 0:
                return {
                    'passed': False,
                    'message': 'Member influence radius must be positive',
                    'severity': 'error'
                }
            
            return {'passed': True, 'message': 'Member attribution settings valid', 'severity': 'info'}
            
        except Exception as e:
            return {'passed': False, 'message': f'Member attribution check failed: {e}', 'severity': 'error'}
    
    def _checkLoadDirection(self, obj):
        """Check load direction settings."""
        try:
            direction_vector = self._get_direction_vector(obj)
            
            # Check for zero vector
            length = math.sqrt(direction_vector.x**2 + direction_vector.y**2 + direction_vector.z**2)
            if length < 1e-6:
                return {
                    'passed': False,
                    'message': 'Load direction vector is zero or near-zero',
                    'severity': 'error'
                }
            
            # Check for reasonable direction
            if obj.Direction == "Custom" and hasattr(obj, 'CustomDirection'):
                custom_length = math.sqrt(obj.CustomDirection.x**2 + obj.CustomDirection.y**2 + obj.CustomDirection.z**2)
                if custom_length < 1e-6:
                    return {
                        'passed': False,
                        'message': 'Custom direction vector is zero or near-zero',
                        'severity': 'error'
                    }
            
            return {'passed': True, 'message': 'Load direction is valid', 'severity': 'info'}
            
        except Exception as e:
            return {'passed': False, 'message': f'Load direction check failed: {e}', 'severity': 'error'}
    
    def _checkMeshQuality(self, obj):
        """Check mesh quality if mesh exists."""
        try:
            if not hasattr(obj, 'MeshData') or not obj.MeshData:
                return {'passed': True, 'message': 'No mesh generated yet', 'severity': 'info'}
            
            mesh_data = obj.MeshData
            if 'mesh_quality' not in mesh_data:
                return {'passed': True, 'message': 'Mesh quality not calculated', 'severity': 'info'}
            
            # Check overall mesh quality
            total_quality = 0.0
            quality_count = 0
            
            for face_quality in mesh_data['mesh_quality'].values():
                if 'quality_score' in face_quality:
                    total_quality += face_quality['quality_score']
                    quality_count += 1
            
            if quality_count == 0:
                return {'passed': True, 'message': 'No mesh quality data available', 'severity': 'info'}
            
            avg_quality = total_quality / quality_count
            
            if avg_quality < 50.0:
                return {
                    'passed': False,
                    'message': f'Poor mesh quality: {avg_quality:.1f}% (recommend >70%)',
                    'severity': 'error'
                }
            elif avg_quality < 70.0:
                return {
                    'passed': False,
                    'message': f'Low mesh quality: {avg_quality:.1f}% (recommend >70%)',
                    'severity': 'warning'
                }
            else:
                return {'passed': True, 'message': f'Good mesh quality: {avg_quality:.1f}%', 'severity': 'info'}
                
        except Exception as e:
            return {'passed': False, 'message': f'Mesh quality check failed: {e}', 'severity': 'error'}
    
    def _displayValidationResults(self, obj, results):
        """Display validation results in console."""
        try:
            App.Console.PrintMessage(f"\nLoad Validation Results for {obj.Label}:\n")
            App.Console.PrintMessage(f"Overall Status: {'✓ VALID' if results['is_valid'] else '✗ INVALID'}\n")
            
            if results['errors']:
                App.Console.PrintError("ERRORS:\n")
                for error in results['errors']:
                    App.Console.PrintError(f"  • {error}\n")
            
            if results['warnings']:
                App.Console.PrintWarning("WARNINGS:\n")
                for warning in results['warnings']:
                    App.Console.PrintWarning(f"  • {warning}\n")
            
            App.Console.PrintMessage("\nDetailed Check Results:\n")
            for check_name, check_result in results['checks'].items():
                status = '✓' if check_result['passed'] else '✗'
                App.Console.PrintMessage(f"  {status} {check_name}: {check_result['message']}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error displaying validation results: {e}\n")
    
    # ===== MEMBER ATTRIBUTION LOGIC ALGORITHMS =====
    
    def calculateTributaryAreas(self, obj):
        """Calculate tributary areas for structural members using RISA-3D methodology."""
        try:
            if not obj.TargetFaces:
                return {}
            
            # Get all structural members from document
            structural_members = self._findStructuralMembers(obj)
            if not structural_members:
                App.Console.PrintWarning("No structural members found for load attribution\n")
                return {}
            
            tributary_areas = {}
            
            # Generate mesh if not exists
            if not obj.MeshData or not obj.MeshData.get('elements'):
                self.generateAdvancedMesh(obj)
            
            mesh_data = obj.MeshData
            if not mesh_data or not mesh_data.get('elements'):
                App.Console.PrintError("Failed to generate mesh for tributary area calculation\n")
                return {}
            
            # Calculate tributary areas based on distribution method
            if obj.DistributionMethod == "TributaryArea":
                tributary_areas = self._calculateTributaryAreaMethod(obj, structural_members, mesh_data)
            elif obj.DistributionMethod == "InfluenceCoefficient":
                tributary_areas = self._calculateInfluenceCoefficientMethod(obj, structural_members, mesh_data)
            elif obj.DistributionMethod == "DirectProjection":
                tributary_areas = self._calculateDirectProjectionMethod(obj, structural_members, mesh_data)
            elif obj.DistributionMethod == "WeightedAverage":
                tributary_areas = self._calculateWeightedAverageMethod(obj, structural_members, mesh_data)
            else:  # FiniteElement
                tributary_areas = self._calculateFiniteElementMethod(obj, structural_members, mesh_data)
            
            # Store results
            obj.TributaryAreas = tributary_areas
            
            # Display summary
            self._displayTributaryAreaSummary(obj, tributary_areas)
            
            return tributary_areas
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating tributary areas: {e}\n")
            return {}
    
    def _findStructuralMembers(self, obj):
        """Find all structural members in the document based on filtering criteria."""
        try:
            doc = App.ActiveDocument
            if not doc:
                return []
            
            structural_members = []
            
            # Search for structural objects
            for doc_obj in doc.Objects:
                # Check if it's a structural member
                if self._isStructuralMember(doc_obj, obj):
                    # Check if it's within influence radius
                    if self._withinInfluenceRadius(doc_obj, obj):
                        structural_members.append(doc_obj)
            
            App.Console.PrintMessage(f"Found {len(structural_members)} structural members for load attribution\n")
            return structural_members
            
        except Exception as e:
            App.Console.PrintError(f"Error finding structural members: {e}\n")
            return []
    
    def _isStructuralMember(self, doc_obj, area_load_obj):
        """Check if an object is a structural member based on type filtering."""
        try:
            # Check object type
            obj_type = getattr(doc_obj, 'Type', '')
            proxy_type = getattr(getattr(doc_obj, 'Proxy', None), 'Type', '')
            
            # Beam members
            if ('Beam' in obj_type or 'Beam' in proxy_type or 'beam' in doc_obj.Label.lower()):
                return area_load_obj.IncludeBeams
            
            # Column members  
            if ('Column' in obj_type or 'Column' in proxy_type or 'column' in doc_obj.Label.lower()):
                return area_load_obj.IncludeColumns
            
            # Brace members
            if ('Brace' in obj_type or 'Brace' in proxy_type or 'brace' in doc_obj.Label.lower()):
                return area_load_obj.IncludeBraces
            
            # Truss members
            if ('Truss' in obj_type or 'Truss' in proxy_type or 'truss' in doc_obj.Label.lower()):
                return area_load_obj.IncludeTrusses
            
            # Generic structural members
            if ('Structural' in obj_type or 'Member' in obj_type):
                return area_load_obj.IncludeGravityMembers
            
            # Wire/Line objects (could be structural members)
            if doc_obj.TypeId in ['Part::Feature', 'Part::Line', 'Draft::Wire']:
                if hasattr(doc_obj, 'Shape') and hasattr(doc_obj.Shape, 'Edges'):
                    return area_load_obj.IncludeGravityMembers
            
            return False
            
        except Exception as e:
            App.Console.PrintWarning(f"Error checking structural member type for {doc_obj.Label}: {e}\n")
            return False
    
    def _withinInfluenceRadius(self, member_obj, area_load_obj):
        """Check if member is within influence radius of loaded area."""
        try:
            if not hasattr(member_obj, 'Shape') or not member_obj.Shape:
                return False
            
            influence_radius = area_load_obj.MemberInfluenceRadius
            load_center = area_load_obj.LoadCenter
            
            # Get member centerline or representative point
            member_center = member_obj.Shape.CenterOfMass if hasattr(member_obj.Shape, 'CenterOfMass') else App.Vector(0, 0, 0)
            
            # Calculate distance
            distance = load_center.distanceToPoint(member_center)
            
            return distance <= influence_radius
            
        except Exception as e:
            App.Console.PrintWarning(f"Error checking influence radius for {member_obj.Label}: {e}\n")
            return False
    
    def _calculateTributaryAreaMethod(self, obj, members, mesh_data):
        """Calculate tributary areas using traditional tributary area method."""
        try:
            tributary_areas = {}
            
            # For each mesh element, determine which member it belongs to
            for element_id, element in mesh_data['elements'].items():
                element_centroid = mesh_data['element_centroids'][element_id]
                element_area = mesh_data['element_areas'][element_id]
                
                # Find closest member
                closest_member = None
                min_distance = float('inf')
                
                for member in members:
                    distance = self._calculateDistanceToMember(element_centroid, member)
                    if distance < min_distance:
                        min_distance = distance
                        closest_member = member
                
                # Assign area to closest member
                if closest_member:
                    member_name = closest_member.Label
                    if member_name not in tributary_areas:
                        tributary_areas[member_name] = {
                            'area': 0.0,
                            'load': 0.0,
                            'elements': [],
                            'member_obj': closest_member
                        }
                    
                    tributary_areas[member_name]['area'] += element_area
                    tributary_areas[member_name]['elements'].append(element_id)
            
            # Calculate loads
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            for member_name, data in tributary_areas.items():
                data['load'] = data['area'] * intensity / 1000000.0  # Convert mm² to m²
            
            return tributary_areas
            
        except Exception as e:
            App.Console.PrintError(f"Error in tributary area method: {e}\n")
            return {}
    
    def _calculateInfluenceCoefficientMethod(self, obj, members, mesh_data):
        """Calculate using influence coefficient method."""
        try:
            tributary_areas = {}
            
            # Calculate influence coefficients for each member
            for element_id, element in mesh_data['elements'].items():
                element_centroid = mesh_data['element_centroids'][element_id]
                element_area = mesh_data['element_areas'][element_id]
                
                # Calculate influence coefficients for all members
                total_influence = 0.0
                member_influences = {}
                
                for member in members:
                    influence = self._calculateInfluenceCoefficient(element_centroid, member)
                    if influence > 0:
                        member_influences[member.Label] = influence
                        total_influence += influence
                
                # Distribute element area based on influence coefficients
                if total_influence > 0:
                    for member_name, influence in member_influences.items():
                        proportion = influence / total_influence
                        distributed_area = element_area * proportion
                        
                        if member_name not in tributary_areas:
                            tributary_areas[member_name] = {
                                'area': 0.0,
                                'load': 0.0,
                                'elements': [],
                                'member_obj': next(m for m in members if m.Label == member_name)
                            }
                        
                        tributary_areas[member_name]['area'] += distributed_area
                        if element_id not in tributary_areas[member_name]['elements']:
                            tributary_areas[member_name]['elements'].append(element_id)
            
            # Calculate loads
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            for member_name, data in tributary_areas.items():
                data['load'] = data['area'] * intensity / 1000000.0  # Convert to m²
            
            return tributary_areas
            
        except Exception as e:
            App.Console.PrintError(f"Error in influence coefficient method: {e}\n")
            return {}
    
    def _calculateDirectProjectionMethod(self, obj, members, mesh_data):
        """Calculate using direct projection method."""
        try:
            # Simplified direct projection - project load directly onto members
            tributary_areas = {}
            
            load_direction = self._get_direction_vector(obj)
            
            for member in members:
                if not hasattr(member, 'Shape'):
                    continue
                
                # Calculate projected area onto member
                projected_area = self._calculateProjectedArea(obj, member, load_direction)
                
                if projected_area > 0:
                    tributary_areas[member.Label] = {
                        'area': projected_area,
                        'load': projected_area * self.parseLoadIntensity(obj.LoadIntensity) / 1000000.0,
                        'elements': [],  # Not element-based for this method
                        'member_obj': member
                    }
            
            return tributary_areas
            
        except Exception as e:
            App.Console.PrintError(f"Error in direct projection method: {e}\n")
            return {}
    
    def _calculateWeightedAverageMethod(self, obj, members, mesh_data):
        """Calculate using weighted average method."""
        # Similar to influence coefficient but with different weighting
        return self._calculateInfluenceCoefficientMethod(obj, members, mesh_data)
    
    def _calculateFiniteElementMethod(self, obj, members, mesh_data):
        """Calculate using finite element method with stiffness-based distribution."""
        try:
            # Simplified FE method - use tributary area as baseline
            tributary_areas = self._calculateTributaryAreaMethod(obj, members, mesh_data)
            
            # Apply stiffness weighting factors (simplified)
            for member_name, data in tributary_areas.items():
                member = data['member_obj']
                stiffness_factor = self._getStiffnessFactor(member)
                data['area'] *= stiffness_factor
                data['load'] *= stiffness_factor
            
            return tributary_areas
            
        except Exception as e:
            App.Console.PrintError(f"Error in finite element method: {e}\n")
            return {}
    
    def _calculateDistanceToMember(self, point, member):
        """Calculate minimum distance from point to member centerline."""
        try:
            if not hasattr(member, 'Shape') or not member.Shape:
                return float('inf')
            
            # For line/wire members, calculate distance to centerline
            if hasattr(member.Shape, 'Edges') and member.Shape.Edges:
                min_distance = float('inf')
                for edge in member.Shape.Edges:
                    try:
                        # Get closest point on edge
                        closest_point = edge.Curve.projectPoint(point, 'NearestPoint')
                        if hasattr(closest_point, 'distanceToPoint'):
                            distance = point.distanceToPoint(closest_point)
                        else:
                            # Fallback to edge center
                            edge_center = edge.CenterOfMass
                            distance = point.distanceToPoint(edge_center)
                        min_distance = min(min_distance, distance)
                    except:
                        # Fallback to edge center distance
                        edge_center = edge.CenterOfMass
                        distance = point.distanceToPoint(edge_center)
                        min_distance = min(min_distance, distance)
                return min_distance
            
            # For other shapes, use center of mass distance
            member_center = member.Shape.CenterOfMass
            return point.distanceToPoint(member_center)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating distance to member {member.Label}: {e}\n")
            return float('inf')
    
    def _calculateInfluenceCoefficient(self, point, member):
        """Calculate influence coefficient for a point relative to a member."""
        try:
            distance = self._calculateDistanceToMember(point, member)
            
            # Simple inverse distance weighting
            if distance <= 0:
                return 1.0
            
            # Influence decreases with distance
            influence = 1.0 / (1.0 + distance / 1000.0)  # Distance in meters
            
            return max(0.0, influence)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating influence coefficient: {e}\n")
            return 0.0
    
    def _calculateProjectedArea(self, obj, member, load_direction):
        """Calculate projected area of loaded surface onto member."""
        try:
            # Simplified projection calculation
            if not obj.TargetFaces:
                return 0.0
            
            total_projected = 0.0
            
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    # Get face area
                    face_area = face_obj.Shape.Area
                    
                    # Calculate projection factor based on member orientation
                    projection_factor = self._getProjectionFactor(face_obj, member, load_direction)
                    
                    total_projected += face_area * projection_factor
            
            return total_projected
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating projected area: {e}\n")
            return 0.0
    
    def _getProjectionFactor(self, face_obj, member, load_direction):
        """Get projection factor for load transfer to member."""
        try:
            # Simplified projection factor - could be enhanced
            return 1.0  # Full projection for now
            
        except Exception as e:
            return 1.0
    
    def _getStiffnessFactor(self, member):
        """Get stiffness factor for finite element distribution."""
        try:
            # Simplified stiffness factor based on member properties
            # Could be enhanced to use actual section properties
            return 1.0
            
        except Exception as e:
            return 1.0
    
    def _displayTributaryAreaSummary(self, obj, tributary_areas):
        """Display summary of tributary area calculations."""
        try:
            if not tributary_areas:
                App.Console.PrintMessage(f"No tributary areas calculated for {obj.Label}\n")
                return
            
            App.Console.PrintMessage(f"\nTributary Area Summary for {obj.Label}:\n")
            App.Console.PrintMessage(f"Distribution Method: {obj.DistributionMethod}\n")
            
            total_area = 0.0
            total_load = 0.0
            
            for member_name, data in tributary_areas.items():
                area_m2 = data['area'] / 1000000.0  # Convert to m²
                load_kn = data['load']
                
                App.Console.PrintMessage(f"  {member_name}: {area_m2:.3f} m², {load_kn:.2f} kN\n")
                
                total_area += area_m2
                total_load += load_kn
            
            App.Console.PrintMessage(f"  Total: {total_area:.3f} m², {total_load:.2f} kN\n")
            
            # Check if total matches loaded area
            loaded_area_m2 = float(str(obj.LoadedArea).split()[0]) / 1000000.0 if hasattr(obj, 'LoadedArea') else 0.0
            if abs(total_area - loaded_area_m2) > 0.01:
                App.Console.PrintWarning(f"Warning: Distributed area ({total_area:.3f} m²) differs from loaded area ({loaded_area_m2:.3f} m²)\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error displaying tributary area summary: {e}\n")
    
    # ===== ENHANCED LOAD PROJECTION SYSTEM =====
    
    def calculateEnhancedProjection(self, obj):
        """Calculate enhanced load projection with coplanarity and shielding."""
        try:
            if not obj.TargetFaces:
                return {}
            
            projection_results = {
                'projected_loads': {},
                'shielding_effects': {},
                'coplanarity_analysis': {}
            }
            
            # Analyze coplanarity if enabled
            if obj.UseCoplanarProjection:
                projection_results['coplanarity_analysis'] = self._analyzeCoplanarity(obj)
            
            # Calculate base projections
            base_projections = self._calculateBaseProjections(obj)
            
            # Apply shielding effects for open structures
            if obj.ConsiderShielding and obj.LoadDistribution == "OpenStructure":
                projection_results['shielding_effects'] = self._calculateShieldingEffects(obj, base_projections)
                projection_results['projected_loads'] = self._applyShielding(base_projections, projection_results['shielding_effects'], obj.ShieldingFactor)
            else:
                projection_results['projected_loads'] = base_projections
            
            return projection_results
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating enhanced projection: {e}\n")
            return {}
    
    def _analyzeCoplanarity(self, obj):
        """Analyze coplanarity of target faces."""
        try:
            analysis = {
                'is_coplanar': True,
                'reference_normal': None,
                'deviations': [],
                'max_deviation': 0.0
            }
            
            if not obj.TargetFaces or len(obj.TargetFaces) < 2:
                return analysis
            
            reference_normal = None
            tolerance = math.radians(obj.ProjectionTolerance)  # Convert to radians
            
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    for face in face_obj.Shape.Faces:
                        try:
                            normal = face.normalAt(0.5, 0.5)
                            
                            if reference_normal is None:
                                reference_normal = normal
                                analysis['reference_normal'] = normal
                            else:
                                angle = reference_normal.getAngle(normal)
                                deviation = math.degrees(angle)
                                analysis['deviations'].append({
                                    'face': face_obj.Label,
                                    'deviation': deviation
                                })
                                
                                analysis['max_deviation'] = max(analysis['max_deviation'], deviation)
                                
                                if angle > tolerance:
                                    analysis['is_coplanar'] = False
                        except:
                            continue
            
            return analysis
            
        except Exception as e:
            App.Console.PrintError(f"Error analyzing coplanarity: {e}\n")
            return {'is_coplanar': False, 'error': str(e)}
    
    def _calculateBaseProjections(self, obj):
        """Calculate base load projections without shielding."""
        try:
            projections = {}
            
            load_direction = self._get_direction_vector(obj)
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            
            # Use custom projection plane if specified
            projection_plane_normal = obj.ProjectionPlane if hasattr(obj, 'ProjectionPlane') else App.Vector(0, 0, 1)
            
            for face_obj in obj.TargetFaces:
                if not hasattr(face_obj, 'Shape'):
                    continue
                
                face_projections = []
                
                for face in face_obj.Shape.Faces:
                    try:
                        # Calculate face normal
                        face_normal = face.normalAt(0.5, 0.5)
                        face_area = face.Area
                        face_center = face.CenterOfMass
                        
                        # Calculate projection factors
                        normal_projection = abs(face_normal.dot(load_direction))
                        plane_projection = abs(face_normal.dot(projection_plane_normal))
                        
                        # Effective load intensity considering projection
                        effective_intensity = intensity * normal_projection
                        
                        face_projection = {
                            'face_center': face_center,
                            'face_normal': face_normal,
                            'face_area': face_area,
                            'normal_projection': normal_projection,
                            'plane_projection': plane_projection,
                            'effective_intensity': effective_intensity,
                            'total_load': effective_intensity * face_area / 1000000.0  # Convert to kN
                        }
                        
                        face_projections.append(face_projection)
                        
                    except Exception as e:
                        App.Console.PrintWarning(f"Error projecting face in {face_obj.Label}: {e}\n")
                        continue
                
                if face_projections:
                    projections[face_obj.Label] = face_projections
            
            return projections
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating base projections: {e}\n")
            return {}
    
    def _calculateShieldingEffects(self, obj, base_projections):
        """Calculate shielding effects for open structures."""
        try:
            shielding_effects = {}
            
            # Get structural members that could provide shielding
            doc = App.ActiveDocument
            if not doc:
                return shielding_effects
            
            load_direction = self._get_direction_vector(obj)
            
            # Find potential shielding members
            shielding_members = []
            for doc_obj in doc.Objects:
                if self._couldProvideShielding(doc_obj):
                    shielding_members.append(doc_obj)
            
            # Calculate shielding for each face
            for face_name, face_projections in base_projections.items():
                face_shielding = []
                
                for face_proj in face_projections:
                    face_center = face_proj['face_center']
                    
                    # Check shielding from each member
                    total_shielding = 0.0
                    
                    for member in shielding_members:
                        shielding_factor = self._calculateMemberShielding(face_center, member, load_direction)
                        total_shielding += shielding_factor
                    
                    # Limit total shielding to maximum factor
                    total_shielding = min(total_shielding, 1.0)
                    
                    face_shielding.append({
                        'face_center': face_center,
                        'shielding_factor': total_shielding,
                        'shielding_members': len(shielding_members)
                    })
                
                shielding_effects[face_name] = face_shielding
            
            return shielding_effects
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating shielding effects: {e}\n")
            return {}
    
    def _couldProvideShielding(self, obj):
        """Check if an object could provide load shielding."""
        try:
            # Check for structural members that could shield loads
            if hasattr(obj, 'Shape') and obj.Shape:
                # Beams, columns, braces could provide shielding
                if ('Beam' in getattr(obj, 'Type', '') or 
                    'Column' in getattr(obj, 'Type', '') or
                    'Brace' in getattr(obj, 'Type', '') or
                    'beam' in obj.Label.lower() or
                    'column' in obj.Label.lower() or
                    'brace' in obj.Label.lower()):
                    return True
                
                # Large surfaces could also provide shielding
                if hasattr(obj.Shape, 'Area') and obj.Shape.Area > 100000:  # > 0.1 m²
                    return True
            
            return False
            
        except Exception as e:
            return False
    
    def _calculateMemberShielding(self, point, member, load_direction):
        """Calculate shielding factor from a member."""
        try:
            if not hasattr(member, 'Shape') or not member.Shape:
                return 0.0
            
            # Simplified shielding calculation
            # Check if member is in the load path
            member_center = member.Shape.CenterOfMass
            
            # Vector from point to member
            to_member = member_center - point
            
            # Check if member is "above" the point in load direction
            dot_product = to_member.dot(load_direction)
            
            if dot_product > 0:  # Member is in load direction
                distance = to_member.Length
                
                # Shielding decreases with distance
                if distance > 0:
                    shielding = 1.0 / (1.0 + distance / 5000.0)  # 5m reference distance
                    return min(shielding, 0.5)  # Max 50% shielding per member
            
            return 0.0
            
        except Exception as e:
            return 0.0
    
    def _applyShielding(self, base_projections, shielding_effects, shielding_factor):
        """Apply shielding effects to base projections."""
        try:
            shielded_projections = {}
            
            for face_name, face_projections in base_projections.items():
                shielded_face_projections = []
                face_shielding = shielding_effects.get(face_name, [])
                
                for i, face_proj in enumerate(face_projections):
                    shielded_proj = face_proj.copy()
                    
                    # Apply shielding if available
                    if i < len(face_shielding):
                        shield = face_shielding[i]
                        shield_reduction = shield['shielding_factor'] * shielding_factor
                        
                        # Reduce effective load due to shielding
                        shielded_proj['effective_intensity'] *= (1.0 - shield_reduction)
                        shielded_proj['total_load'] *= (1.0 - shield_reduction)
                        shielded_proj['shielding_applied'] = shield_reduction
                    else:
                        shielded_proj['shielding_applied'] = 0.0
                    
                    shielded_face_projections.append(shielded_proj)
                
                shielded_projections[face_name] = shielded_face_projections
            
            return shielded_projections
            
        except Exception as e:
            App.Console.PrintError(f"Error applying shielding: {e}\n")
            return base_projections
    
    # ===== ADVANCED VISUALIZATION FEATURES =====
    
    def createAdvancedVisualization(self, obj):
        """Create advanced visualization including contours, tributary areas, and distributions."""
        try:
            visualization_objects = []
            
            # Create load arrows if enabled
            if hasattr(obj, 'ShowLoadArrows') and obj.ShowLoadArrows:
                arrows = self._createAdvancedLoadArrows(obj)
                visualization_objects.extend(arrows)
            
            # Create mesh visualization if enabled
            if hasattr(obj, 'ShowMeshElements') and obj.ShowMeshElements:
                mesh_vis = self._createMeshVisualization(obj)
                visualization_objects.extend(mesh_vis)
            
            # Create pressure contours if enabled
            if hasattr(obj, 'ShowPressureContours') and obj.ShowPressureContours:
                contours = self._createPressureContours(obj)
                visualization_objects.extend(contours)
            
            # Create tributary area visualization if enabled
            if hasattr(obj, 'ShowMemberTributary') and obj.ShowMemberTributary:
                tributary_vis = self._createTributaryVisualization(obj)
                visualization_objects.extend(tributary_vis)
            
            # Create load distribution visualization if enabled
            if hasattr(obj, 'ShowLoadDistribution') and obj.ShowLoadDistribution:
                distribution_vis = self._createLoadDistributionVisualization(obj)
                visualization_objects.extend(distribution_vis)
            
            # Store all visualization objects
            if hasattr(obj, 'LoadVisualization'):
                # Clear existing visualization
                self._clear_visualization(obj)
                obj.LoadVisualization = visualization_objects
            
            App.Console.PrintMessage(f"Created {len(visualization_objects)} visualization objects for {obj.Label}\n")
            return visualization_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating advanced visualization: {e}\n")
            return []
    
    def _createAdvancedLoadArrows(self, obj):
        """Create enhanced load arrows with variable sizes and colors."""
        try:
            arrows = []
            
            if not obj.TargetFaces:
                return arrows
            
            # Enhanced arrow creation with mesh-based positioning
            if obj.MeshData and obj.MeshData.get('elements'):
                arrows = self._createMeshBasedArrows(obj)
            else:
                # Fallback to grid-based arrows
                arrows = self._createGridBasedArrows(obj)
            
            return arrows
            
        except Exception as e:
            App.Console.PrintError(f"Error creating advanced load arrows: {e}\n")
            return []
    
    def _createMeshBasedArrows(self, obj):
        """Create arrows at mesh element centroids."""
        try:
            arrows = []
            doc = App.ActiveDocument
            if not doc:
                return arrows
            
            mesh_data = obj.MeshData
            direction_vector = self._get_direction_vector(obj)
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            arrow_scale = getattr(obj, 'VectorScale', 1.0)
            
            # Create arrow at each element centroid
            for element_id, centroid in mesh_data['element_centroids'].items():
                element_area = mesh_data['element_areas'][element_id]
                
                # Scale arrow size based on element area
                area_factor = math.sqrt(element_area / 10000)  # Normalize by 100mm²
                scaled_intensity = intensity * area_factor
                
                # Create arrow
                arrow = self._createArrow(doc, centroid, direction_vector, scaled_intensity, arrow_scale)
                if arrow:
                    arrows.append(arrow)
                    
                    # Color code based on load intensity
                    self._applyLoadIntensityColor(arrow, scaled_intensity, intensity)
            
            return arrows
            
        except Exception as e:
            App.Console.PrintError(f"Error creating mesh-based arrows: {e}\n")
            return []
    
    def _createGridBasedArrows(self, obj):
        """Create arrows on regular grid (fallback method)."""
        try:
            # Use existing arrow creation method as fallback
            self._createLoadVectors(obj)
            return getattr(obj, 'LoadVisualization', [])
            
        except Exception as e:
            App.Console.PrintError(f"Error creating grid-based arrows: {e}\n")
            return []
    
    def _applyLoadIntensityColor(self, arrow, current_intensity, max_intensity):
        """Apply color coding based on load intensity."""
        try:
            if not hasattr(arrow, 'ViewObject'):
                return
            
            # Normalize intensity (0.0 to 1.0)
            normalized = min(current_intensity / max_intensity, 1.0) if max_intensity > 0 else 0.0
            
            # Color gradient from blue (low) to red (high)
            red = normalized
            blue = 1.0 - normalized
            green = 0.2  # Small green component for visibility
            
            arrow.ViewObject.ShapeColor = (red, green, blue)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error applying color to arrow: {e}\n")
    
    def _createMeshVisualization(self, obj):
        """Create visualization of generated mesh elements."""
        try:
            mesh_objects = []
            
            if not obj.MeshData or not obj.MeshData.get('elements'):
                return mesh_objects
            
            doc = App.ActiveDocument
            if not doc:
                return mesh_objects
            
            # Create wireframe representation of mesh elements
            for element_id, element in obj.MeshData['elements'].items():
                try:
                    mesh_obj = self._createMeshElementVisualization(doc, element, element_id)
                    if mesh_obj:
                        mesh_objects.append(mesh_obj)
                except Exception as e:
                    continue
            
            return mesh_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating mesh visualization: {e}\n")
            return []
    
    def _createMeshElementVisualization(self, doc, element, element_id):
        """Create visualization for a single mesh element."""
        try:
            if element['type'] != 'triangle' or len(element['nodes']) < 3:
                return None
            
            # Create triangle wireframe
            points = [node['point'] for node in element['nodes']]
            points.append(points[0])  # Close the triangle
            
            # Create wire
            edges = []
            for i in range(len(points) - 1):
                edge = Part.makeLine(points[i], points[i + 1])
                edges.append(edge)
            
            if edges:
                wire = Part.makeCompound(edges)
                
                # Create object
                mesh_name = f"Mesh_{obj.Label}_{element_id}"
                mesh_obj = doc.addObject("Part::Feature", mesh_name)
                mesh_obj.Shape = wire
                
                # Set visual properties
                if hasattr(mesh_obj, 'ViewObject'):
                    mesh_obj.ViewObject.LineColor = (0.5, 0.5, 0.5)  # Gray
                    mesh_obj.ViewObject.LineWidth = 1.0
                
                return mesh_obj
            
            return None
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating mesh element visualization: {e}\n")
            return None
    
    def _createPressureContours(self, obj):
        """Create pressure contour lines."""
        try:
            contour_objects = []
            
            if not obj.TargetFaces:
                return contour_objects
            
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            num_levels = getattr(obj, 'ContourLevels', 10)
            
            # Generate contour levels
            contour_levels = [intensity * (i + 1) / (num_levels + 1) for i in range(num_levels)]
            
            doc = App.ActiveDocument
            if not doc:
                return contour_objects
            
            # Create contours for each face
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    face_contours = self._createFaceContours(doc, face_obj, contour_levels)
                    contour_objects.extend(face_contours)
            
            return contour_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating pressure contours: {e}\n")
            return []
    
    def _createFaceContours(self, doc, face_obj, contour_levels):
        """Create contour lines for a face."""
        try:
            contours = []
            
            # Simplified contour creation - concentric rectangles/circles
            for i, level in enumerate(contour_levels):
                try:
                    # Create contour at this level
                    contour = self._createSingleContour(doc, face_obj, level, i)
                    if contour:
                        contours.append(contour)
                except Exception as e:
                    continue
            
            return contours
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating face contours: {e}\n")
            return []
    
    def _createSingleContour(self, doc, face_obj, level, level_index):
        """Create a single contour line."""
        try:
            # Simplified implementation - create offset curve from face boundary
            if not hasattr(face_obj, 'Shape') or not face_obj.Shape.Faces:
                return None
            
            face = face_obj.Shape.Faces[0]
            
            # Get face boundary
            boundary_wires = face.Wires
            if not boundary_wires:
                return None
            
            outer_wire = boundary_wires[0]
            
            # Create offset wire (simplified contour)
            try:
                offset_distance = -level_index * 100  # 100mm offset per level
                if offset_distance > -10:  # Minimum offset
                    offset_distance = -10
                
                offset_wire = outer_wire.makeOffset2D(offset_distance)
                
                # Create object
                contour_name = f"Contour_{face_obj.Label}_{level_index}"
                contour_obj = doc.addObject("Part::Feature", contour_name)
                contour_obj.Shape = offset_wire
                
                # Set visual properties
                if hasattr(contour_obj, 'ViewObject'):
                    # Color based on level
                    color_factor = level_index / 10.0
                    contour_obj.ViewObject.LineColor = (color_factor, 0.5, 1.0 - color_factor)
                    contour_obj.ViewObject.LineWidth = 2.0
                
                return contour_obj
                
            except Exception as e:
                # Fallback - just return the boundary
                contour_name = f"Contour_{face_obj.Label}_{level_index}"
                contour_obj = doc.addObject("Part::Feature", contour_name)
                contour_obj.Shape = outer_wire
                
                if hasattr(contour_obj, 'ViewObject'):
                    contour_obj.ViewObject.LineColor = (1.0, 0.0, 0.0)
                    contour_obj.ViewObject.LineWidth = 1.0
                
                return contour_obj
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating single contour: {e}\n")
            return None
    
    def _createTributaryVisualization(self, obj):
        """Create visualization of tributary areas for members."""
        try:
            tributary_objects = []
            
            if not hasattr(obj, 'TributaryAreas') or not obj.TributaryAreas:
                # Calculate tributary areas if not exists
                self.calculateTributaryAreas(obj)
            
            if not obj.TributaryAreas:
                return tributary_objects
            
            doc = App.ActiveDocument
            if not doc:
                return tributary_objects
            
            # Create visualization for each member's tributary area
            for member_name, data in obj.TributaryAreas.items():
                try:
                    tributary_obj = self._createSingleTributaryVisualization(doc, member_name, data, obj)
                    if tributary_obj:
                        tributary_objects.append(tributary_obj)
                except Exception as e:
                    continue
            
            return tributary_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating tributary visualization: {e}\n")
            return []
    
    def _createSingleTributaryVisualization(self, doc, member_name, tributary_data, obj):
        """Create visualization for a single member's tributary area."""
        try:
            # Create a visual representation of tributary area
            # This could be colored regions, text labels, or connection lines
            
            member_obj = tributary_data.get('member_obj')
            if not member_obj or not hasattr(member_obj, 'Shape'):
                return None
            
            # Create text annotation
            area_m2 = tributary_data['area'] / 1000000.0  # Convert to m²
            load_kn = tributary_data['load']
            
            # Get member center for text placement
            member_center = member_obj.Shape.CenterOfMass
            
            # Create text object (simplified - in real implementation would use Draft.makeText)
            text_name = f"TributaryInfo_{member_name}"
            
            # For now, just print the information
            App.Console.PrintMessage(f"Tributary for {member_name}: {area_m2:.3f} m², {load_kn:.2f} kN at {member_center}\n")
            
            # Could create actual 3D text or annotation object here
            return None  # Placeholder
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating tributary visualization for {member_name}: {e}\n")
            return None
    
    def _createLoadDistributionVisualization(self, obj):
        """Create visualization of load distribution pattern."""
        try:
            distribution_objects = []
            
            # Show distribution method visually
            if obj.LoadDistribution == "OneWay":
                distribution_objects = self._createOneWayVisualization(obj)
            elif obj.LoadDistribution == "TwoWay":
                distribution_objects = self._createTwoWayVisualization(obj)
            elif obj.LoadDistribution == "OpenStructure":
                distribution_objects = self._createOpenStructureVisualization(obj)
            
            return distribution_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating load distribution visualization: {e}\n")
            return []
    
    def _createOneWayVisualization(self, obj):
        """Create visualization for one-way load distribution."""
        try:
            # Show direction arrows indicating one-way distribution
            vis_objects = []
            
            direction = obj.CustomDistributionDirection if hasattr(obj, 'CustomDistributionDirection') else App.Vector(1, 0, 0)
            
            # Create arrows showing distribution direction
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    face_center = face_obj.Shape.CenterOfMass
                    
                    # Create direction arrow
                    doc = App.ActiveDocument
                    if doc:
                        arrow = self._createDirectionArrow(doc, face_center, direction, "OneWay")
                        if arrow:
                            vis_objects.append(arrow)
            
            return vis_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating one-way visualization: {e}\n")
            return []

    def to_solver_loads(self, obj, mesh_payload: dict = None, force_unit: str = 'kN', length_unit: str = 'mm') -> dict:
        """
        Convert this AreaLoad into a simple solver-friendly load description.

        If mesh_payload (from StructuralPlate.to_calc_payload) is provided and contains
        element names, this will return a dict mapping element names to pressure values.
        Otherwise, it returns a high-level {'plate': plate_name, 'pressure': value} entry.
        """
        result = {'entries': [], 'total_force': 0.0}
        try:
            # Parse pressure from LoadIntensity or Magnitude
            intensity = 0.0
            if hasattr(obj, 'LoadIntensity') and obj.LoadIntensity:
                try:
                    # use calc_utils.qty_val when available for unit robustness
                    from ..calc_utils import qty_val
                    intensity = float(qty_val(obj.LoadIntensity, 'N/m^2', force_unit + '/' + length_unit + '^2'))
                except Exception:
                    try:
                        intensity = float(str(obj.LoadIntensity).split()[0])
                    except Exception:
                        intensity = 0.0
            elif hasattr(obj, 'Magnitude') and obj.Magnitude:
                try:
                    from ..calc_utils import qty_val
                    intensity = float(qty_val(obj.Magnitude, 'N/m^2', force_unit + '/' + length_unit + '^2'))
                except Exception:
                    try:
                        intensity = float(str(obj.Magnitude).split()[0])
                    except Exception:
                        intensity = 0.0

            # Determine targets
            targets = []
            if hasattr(obj, 'TargetFaces') and obj.TargetFaces:
                for t in obj.TargetFaces:
                    if getattr(t, 'Type', '') == 'StructuralPlate' or 'Plate' in getattr(t, 'Name', ''):
                        targets.append(t)

            # If mesh payload provides element list, distribute pressure to elements
            if mesh_payload and 'elements' in mesh_payload and mesh_payload['elements']:
                for eid, elem in mesh_payload['elements'].items():
                    # For uniform distribution, pressure same for all elements
                    result['entries'].append({'element': eid, 'pressure': float(intensity)})
                # total force = pressure * area
                area = mesh_payload.get('area', None)
                if area:
                    result['total_force'] = float(intensity) * float(area)
                else:
                    # approximate from node-based polygon if nodes exist
                    result['total_force'] = 0.0
                return result

            # Fallback: per-target plate pressure
            for tgt in targets:
                plate_name = getattr(tgt, 'Name', None)
                result['entries'].append({'plate': plate_name, 'pressure': float(intensity)})
                try:
                    area = 0.0
                    if hasattr(tgt, 'Shape') and hasattr(tgt.Shape, 'Area'):
                        area = float(tgt.Shape.Area)
                    elif hasattr(tgt, 'LoadedArea'):
                        try:
                            area = float(tgt.LoadedArea)
                        except Exception:
                            area = 0.0
                    result['total_force'] += float(intensity) * area
                except Exception:
                    continue

            return result
        except Exception:
            return result

class ViewProviderAreaLoad:
    """
    ViewProvider for AreaLoad with enhanced visualization.
    """
    
    def __init__(self, vobj):
        """Initialize ViewProvider."""
        vobj.Proxy = self
        self.Object = vobj.Object
        
        # Display properties
        vobj.addProperty("App::PropertyBool", "ShowLoadInfo", "Display",
                        "Show load information text")
        vobj.ShowLoadInfo = True
        
        vobj.addProperty("App::PropertyFloat", "TextSize", "Display",
                        "Text size for load information")
        vobj.TextSize = 12.0
    
    def getIcon(self) -> str:
        """Return icon for area load."""
        if not hasattr(self.Object, 'LoadCategory'):
            return self._get_icon_path("area_load_generic.svg")
        
        category = self.Object.LoadCategory
        icon_map = {
            "DL": "area_load_dead.svg",
            "LL": "area_load_live.svg",
            "W": "area_load_wind.svg",
            "E": "area_load_seismic.svg",
            "T": "area_load_thermal.svg"
        }
        
        icon_name = icon_map.get(category, "area_load_generic.svg")
        return self._get_icon_path(icon_name)
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icon_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")
        return os.path.join(icon_dir, icon_name)
    
    def setEdit(self, vobj, mode: int) -> bool:
        """Open area load properties panel."""
        if mode == 0:
            try:
                from ..taskpanels.AreaLoadPanel import AreaLoadApplicationPanel
                self.panel = AreaLoadApplicationPanel(vobj.Object)
                Gui.Control.showDialog(self.panel)
                return True
            except ImportError:
                App.Console.PrintWarning("AreaLoadPanel not yet implemented\n")
                return False
        return False
    
    def unsetEdit(self, vobj, mode: int) -> bool:
        """Close area load editing panel."""
        if hasattr(self, 'panel'):
            Gui.Control.closeDialog()
        return True
    
    def doubleClicked(self, vobj) -> bool:
        """Handle double-click to open properties."""
        return self.setEdit(vobj, 0)
    
    def updateData(self, obj, prop: str) -> None:
        """Update visualization when object data changes."""
        if prop in ["TargetFaces", "Magnitude", "ShowLoadArrows", "ArrowScale", "ArrowDensity", "Distribution"]:
            # Trigger visual update by delegating to object's proxy
            try:
                if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '_update_visualization'):
                    obj.Proxy._update_visualization(obj)
                elif hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '_createLoadVectors'):
                    # fallback to creating vectors directly
                    obj.Proxy._update_visualization(obj)
            except Exception:
                pass

def makeAreaLoad(target_faces=None, magnitude="5.0 kN/m^2", load_type="Dead Load (DL)", name="AreaLoad"):
    """
    Create a new AreaLoad object with robust error handling.
    
    Args:
        target_faces: List of faces to apply load to
        magnitude: Load magnitude
        load_type: Type of load
        name: Object name
        
    Returns:
        Created AreaLoad object or None if failed
    """
    try:
        doc = App.ActiveDocument
        if not doc:
            App.Console.PrintError("No active document. Please create or open a document first.\n")
            return None
        
        App.Console.PrintMessage(f"Creating AreaLoad with magnitude: {magnitude}, type: {load_type}\n")
        
        # Create the object
        obj = doc.addObject("App::DocumentObjectGroupPython", name)
        if not obj:
            App.Console.PrintError("Failed to create DocumentObject\n")
            return None
        
        App.Console.PrintMessage(f"Created DocumentObject: {obj.Name}\n")
        
        # Initialize AreaLoad proxy
        try:
            area_load_proxy = AreaLoad(obj)
            App.Console.PrintMessage("AreaLoad proxy initialized successfully\n")
        except Exception as e:
            App.Console.PrintError(f"Error initializing AreaLoad: {e}\n")
            try:
                doc.removeObject(obj.Name)
            except:
                pass
            return None
        
        # Create ViewProvider
        if App.GuiUp:
            try:
                ViewProviderAreaLoad(obj.ViewObject)
                App.Console.PrintMessage("ViewProvider created successfully\n")
            except Exception as e:
                App.Console.PrintWarning(f"ViewProvider creation warning: {e}\n")
        
    except Exception as e:
        App.Console.PrintError(f"Error creating AreaLoad object: {e}\n")
        return None
    
    # Set properties carefully
    try:
        if target_faces:
            obj.TargetFaces = target_faces if isinstance(target_faces, list) else [target_faces]
        
        # Set magnitude
        if hasattr(obj, 'LoadIntensity'):
            obj.LoadIntensity = magnitude
        else:
            # Fallback: add the property if missing
            obj.addProperty("App::PropertyPressure", "LoadIntensity", "Load", "Load intensity (pressure)")
            obj.LoadIntensity = magnitude
        
        # Set load type carefully
        if hasattr(obj, 'LoadType'):
            try:
                obj.LoadType = load_type
                App.Console.PrintMessage(f"Set LoadType to: {load_type}\n")
            except Exception as e:
                App.Console.PrintWarning(f"Could not set LoadType to '{load_type}': {e}\n")
        
        # Generate unique ID
        load_count = len([o for o in doc.Objects if hasattr(o, 'Proxy') and hasattr(o.Proxy, 'Type') and o.Proxy.Type == "AreaLoad"])
        
        # Add LoadID property if not exists
        if not hasattr(obj, 'LoadID'):
            obj.addProperty("App::PropertyString", "LoadID", "Identification", "Unique load identifier")
        obj.LoadID = f"AL{load_count + 1:03d}"
        
        # Recompute to update properties
        try:
            obj.recompute()
            doc.recompute()
        except Exception as e:
            App.Console.PrintWarning(f"Recompute warning: {e}\n")
        
        App.Console.PrintMessage(f"Created AreaLoad: {obj.Label} with ID: {obj.LoadID}\n")
        return obj
        
    except Exception as e:
        App.Console.PrintError(f"Error setting AreaLoad properties: {e}\n")
        # Clean up partial object
        try:
            doc.removeObject(obj.Name)
        except:
            pass
        return None