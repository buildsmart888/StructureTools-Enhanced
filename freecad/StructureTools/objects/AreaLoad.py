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
import math
import FreeCAD as App
import Part

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
        
        # Ensure we're starting with a clean object
        self._ensure_property_exists = self._create_property_adder(obj)
        
        # Target geometry
        obj.addProperty("App::PropertyLinkList", "TargetFaces", "Geometry",
                       "Faces or surfaces to apply load")
        
        obj.addProperty("App::PropertyArea", "LoadedArea", "Geometry",
                       "Total loaded area (calculated)")
        
        obj.addProperty("App::PropertyVector", "LoadDirection", "Geometry",
                       "Load direction vector (global coordinates)")
        obj.LoadDirection = App.Vector(0, 0, -1)  # Downward default
        
        obj.addProperty("App::PropertyEnumeration", "Direction", "Geometry",
                       "Load direction")
        obj.Direction = ["+X Global", "-X Global", "+Y Global", "-Y Global", "+Z Global", "-Z Global", "Normal", "Custom"]
        obj.Direction = "-Z Global"  # Downward default
        
        obj.addProperty("App::PropertyVector", "CustomDirection", "Geometry",
                       "Custom load direction vector")
        obj.CustomDirection = App.Vector(0, 0, -1)  # Downward default
        
        # Load definition
        obj.addProperty("App::PropertyEnumeration", "LoadType", "Load",
                       "Type of area load")
        obj.LoadType = [
            "Dead Load (DL)", "Live Load (LL)", "Live Load Roof (LL_Roof)",
            "Wind Load (W)", "Earthquake (E)", "Earth Pressure (H)",
            "Fluid Pressure (F)", "Thermal (T)", "Custom Pressure"
        ]
        obj.LoadType = "Dead Load (DL)"
        
        obj.addProperty("App::PropertyEnumeration", "LoadCategory", "Load",
                       "Load category for combinations")
        obj.LoadCategory = ["DL", "LL", "LL_Roof", "W", "E", "H", "F", "T", "CUSTOM"]
        obj.LoadCategory = "DL"
        
        # Load intensity and distribution
        obj.addProperty("App::PropertyPressure", "LoadIntensity", "Load",
                       "Load intensity (pressure)")
        obj.LoadIntensity = "2.4 kN/m^2"  # Typical dead load
        
        obj.addProperty("App::PropertyEnumeration", "Distribution", "Load",
                       "Load distribution type")
        obj.Distribution = ["Uniform", "Linear X", "Linear Y", "Parabolic", "Point Load"]
        obj.Distribution = "Uniform"
        
        obj.addProperty("App::PropertyFloatList", "DistributionParameters", "Load",
                       "Parameters for load distribution")
        obj.DistributionParameters = [1.0]  # Default uniform distribution
        
        obj.addProperty("App::PropertyEnumeration", "DistributionPattern", "Load",
                       "Load distribution pattern")
        obj.DistributionPattern = [
            "Uniform", "Linear X", "Linear Y", "Bilinear", "Radial", 
            "Point Load", "Line Load", "Custom Pattern"
        ]
        obj.DistributionPattern = "Uniform"
        
        obj.addProperty("App::PropertyFloatList", "DistributionFactors", "Load",
                       "Distribution factors for non-uniform patterns")
        obj.DistributionFactors = [1.0, 1.0, 1.0, 1.0]  # Corner factors
        
        # Load distribution method (based on RISA documentation)
        obj.addProperty("App::PropertyEnumeration", "LoadDistribution", "Distribution",
                       "Method for distributing load to supporting elements")
        obj.LoadDistribution = ["OneWay", "TwoWay", "OpenStructure"]
        obj.LoadDistribution = "TwoWay"  # Default to two-way distribution
        
        # Direction specification for one-way loads
        obj.addProperty("App::PropertyEnumeration", "OneWayDirection", "Distribution",
                       "Direction for one-way load distribution")
        obj.OneWayDirection = ["X", "Y", "Custom"]
        obj.OneWayDirection = "X"
        
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
        obj.addProperty("App::PropertyEnumeration", "BuildingCode", "Code",
                       "Building code standard")
        obj.BuildingCode = [
            "ASCE 7-16", "IBC 2018", "NBCC 2015", "Eurocode 1", 
            "AS/NZS 1170", "Custom"
        ]
        obj.BuildingCode = "ASCE 7-16"
        
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
        
        obj.addProperty("App::PropertyEnumeration", "ExposureCategory", "Environmental",
                       "Wind exposure category")
        obj.ExposureCategory = ["A", "B", "C", "D"]
        obj.ExposureCategory = "B"
        
        obj.addProperty("App::PropertyFloat", "SeismicAcceleration", "Environmental",
                       "Peak ground acceleration for seismic")
        obj.SeismicAcceleration = 0.2
        
        # Thai Units Support
        obj.addProperty("App::PropertyBool", "UseThaiUnits", "Thai Units",
                       "Enable Thai units for load calculations")
        obj.UseThaiUnits = False
        
        obj.addProperty("App::PropertyPressure", "LoadIntensityKsc", "Thai Units", 
                       "Load intensity in ksc/m² (Thai units)")
        obj.LoadIntensityKsc = "240 kgf/cm^2/m^2"  # Equivalent to 2.4 kN/m²
        
        obj.addProperty("App::PropertyPressure", "LoadIntensityTfM2", "Thai Units",
                       "Load intensity in tf/m² (Thai units)")
        obj.LoadIntensityTfM2 = "0.24 tf/m^2"
        
        obj.addProperty("App::PropertyFloat", "LoadFactorThai", "Thai Units",
                       "Load factor per Thai Ministry B.E. 2566")
        obj.LoadFactorThai = 1.4
        
        obj.addProperty("App::PropertyFloat", "TemperatureChange", "Environmental",
                       "Temperature change (°C)")
        obj.TemperatureChange = 0.0
        
        # Load application properties
        obj.addProperty("App::PropertyVector", "ReferencePoint", "Application",
                       "Reference point for load application")
        
        obj.addProperty("App::PropertyVector", "LoadCenter", "Application",
                       "Center point of the load application")
        obj.LoadCenter = App.Vector(0, 0, 0)
        
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
        
        obj.addProperty("App::PropertyVector", "LoadResultant", "Results",
                       "Resultant load vector")
        obj.LoadResultant = App.Vector(0, 0, 0)
        
        obj.addProperty("App::PropertyBool", "IsValid", "Validation",
                       "Whether the load definition is valid")
        obj.IsValid = True
        
        # Visualization properties
        obj.addProperty("App::PropertyBool", "ShowLoadArrows", "Display",
                       "Show load arrows")
        obj.ShowLoadArrows = True
        
        obj.addProperty("App::PropertyFloat", "ArrowScale", "Display",
                       "Scale factor for load arrows")
        obj.ArrowScale = 1.0
        
        obj.addProperty("App::PropertyInteger", "ArrowDensity", "Display",
                       "Density of load arrows")
        obj.ArrowDensity = 5
        
        obj.addProperty("App::PropertyColor", "LoadColor", "Display",
                       "Color for load display")
        obj.LoadColor = (1.0, 0.0, 0.0)  # Red
        
        obj.addProperty("App::PropertyLinkList", "LoadVisualization", "Display",
                       "Visualization objects for the load")
        obj.LoadVisualization = []
        
        obj.addProperty("App::PropertyBool", "ShowLoadDistribution", "Display",
                       "Show load distribution pattern")
        obj.ShowLoadDistribution = True
        
        obj.addProperty("App::PropertyInteger", "DisplayDensity", "Display",
                       "Density of load visualization")
        obj.DisplayDensity = 10
        
        # Analysis properties
        obj.addProperty("App::PropertyBool", "IncludeInAnalysis", "Analysis",
                       "Include this load in structural analysis")
        obj.IncludeInAnalysis = True
        
        obj.addProperty("App::PropertyEnumeration", "LoadMethod", "Analysis",
                       "Method for load application in FEA")
        obj.LoadMethod = ["Nodal Forces", "Pressure", "Body Force"]
        obj.LoadMethod = "Pressure"
        
        obj.addProperty("App::PropertyForce", "Magnitude", "Load",
                       "Load magnitude")
        obj.Magnitude = "2.4 kN/m^2"  # Typical dead load
        
        obj.addProperty("App::PropertyInteger", "LoadSteps", "Analysis",
                       "Number of load steps for nonlinear analysis")
        obj.LoadSteps = 1
        
        # Identification
        obj.addProperty("App::PropertyString", "LoadID", "Identification",
                       "Unique load identifier")
        
        obj.addProperty("App::PropertyString", "Description", "Identification",
                       "Load description or notes")
        
        obj.addProperty("App::PropertyString", "DesignCode", "Identification",
                       "Applicable design code")
        obj.DesignCode = "IBC 2018"
        
        # Status
        obj.addProperty("App::PropertyBool", "IsActive", "Status",
                       "Load is active in analysis")
        obj.IsActive = True
        
        obj.addProperty("App::PropertyBool", "IsValid", "Status",
                       "Load definition is valid")
        obj.IsValid = True
        
        # Initialize calculations
        self.calculateLoadProperties(obj)
    
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
            obj.LoadIntensityKsc = f"{intensity_ksc:.2f} kgf/cm^2/m^2"
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
            self.updateLoadVisualization(obj)
            self._calculate_total_load(obj)
    
    def updateLoadVisualization(self, obj) -> None:
        """Update visual representation of the load including distribution patterns."""
        try:
            if not obj.ShowLoadArrows:
                self._clear_visualization(obj)
                return
                
            # Clear existing visualization
            self._clear_visualization(obj)
            
            # Create load vectors
            self._createLoadVectors(obj)
            
            # Show load distribution pattern if requested
            if obj.ShowLoadDistribution:
                self._create_load_distribution(obj)
                
        except Exception as e:
            App.Console.PrintError(f"Error updating load visualization: {e}\n")
    
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
        
        except Exception as e:
            App.Console.PrintError(f"Error creating load vectors: {e}\n")
    
    def _createArrow(self, doc, position, direction, magnitude, scale):
        """Create a load arrow at the specified position."""
        try:
            # Calculate arrow length based on magnitude and scale
            arrow_length = magnitude * scale * 100  # Scale factor in mm
            if arrow_length < 10:  # Minimum length for visibility
                arrow_length = 10
            
            # Create arrow parts
            arrow_radius = arrow_length * 0.03  # Arrow shaft radius
            head_radius = arrow_radius * 3     # Arrow head radius
            head_length = arrow_length * 0.2   # Arrow head length
            
            # Create arrow shaft
            shaft_end = position + direction * (arrow_length - head_length)
            shaft = Part.makeCylinder(arrow_radius, arrow_length - head_length, position, direction)
            
            # Create arrow head (cone)
            head = Part.makeCone(head_radius, 0, head_length, shaft_end, direction)
            
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
    
    def _clear_visualization(self, obj) -> None:
        """Clear existing load visualization objects."""
        try:
            doc = App.ActiveDocument
            if not doc:
                return
            
            # Remove all visualization objects
            if hasattr(obj, 'LoadVisualization') and obj.LoadVisualization:
                for vis_obj in obj.LoadVisualization:
                    if vis_obj and hasattr(doc, 'getObject') and doc.getObject(vis_obj.Name):
                        doc.removeObject(vis_obj.Name)
                
                # Clear visualization list
                obj.LoadVisualization = []
        
        except Exception as e:
            App.Console.PrintWarning(f"Error clearing visualization: {e}\n")
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        # Ensure critical properties exist
        if not hasattr(obj, 'LoadCategory'):
            self._ensure_property_exists("App::PropertyEnumeration", "LoadCategory", "Load",
                       "Load category for combinations", "DL")
        
        if not hasattr(obj, 'ShowLoadArrows'):
            self._ensure_property_exists("App::PropertyBool", "ShowLoadArrows", "Display",
                       "Show load arrows", True)
        
        if not hasattr(obj, 'LoadCenter'):
            self._ensure_property_exists("App::PropertyVector", "LoadCenter", "Application",
                       "Center point of the load application", App.Vector(0, 0, 0))
        
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
            self._update_visualization(obj)
        elif prop in ["ArrowDensity", "ArrowScale"]:
            if hasattr(obj, 'ShowLoadArrows') and obj.ShowLoadArrows:
                self._update_visualization(obj)
    
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
            obj.LoadCategory = category_map[load_type]
    
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
        if prop in ["TargetFaces", "Magnitude", "ShowLoadArrows"]:
            # Trigger visual update
            pass

def makeAreaLoad(target_faces=None, magnitude="5.0 kN/m^2", load_type="Dead Load (DL)", name="AreaLoad"):
    """
    Create a new AreaLoad object.
    
    Args:
        target_faces: List of faces to apply load to
        magnitude: Load magnitude
        load_type: Type of load
        name: Object name
        
    Returns:
        Created AreaLoad object
    """
    doc = App.ActiveDocument
    if not doc:
        App.Console.PrintError("No active document. Please create or open a document first.\n")
        return None
    
    # Create the object
    obj = doc.addObject("App::DocumentObjectGroupPython", name)
    AreaLoad(obj)
    
    # Create ViewProvider
    if App.GuiUp:
        ViewProviderAreaLoad(obj.ViewObject)
    
    # Set properties
    if target_faces:
        obj.TargetFaces = target_faces if isinstance(target_faces, list) else [target_faces]
    obj.Magnitude = magnitude
    obj.LoadType = load_type
    
    # Generate unique ID
    load_count = len([o for o in doc.Objects if hasattr(o, 'Proxy') and hasattr(o.Proxy, 'Type') and o.Proxy.Type == "AreaLoad"])
    obj.LoadID = f"AL{load_count + 1:03d}"
    
    # Recompute to update properties
    obj.recompute()
    doc.recompute()
    
    App.Console.PrintMessage(f"Created AreaLoad: {obj.Label} with ID: {obj.LoadID}\n")
    return obj