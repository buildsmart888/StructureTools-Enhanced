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
        
        # Target geometry
        obj.addProperty("App::PropertyLinkList", "TargetFaces", "Geometry",
                       "Faces or surfaces to apply load")
        
        obj.addProperty("App::PropertyArea", "LoadedArea", "Geometry",
                       "Total loaded area (calculated)")
        
        obj.addProperty("App::PropertyVector", "LoadDirection", "Geometry",
                       "Load direction vector (global coordinates)")
        obj.LoadDirection = App.Vector(0, 0, -1)  # Downward default
        
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
        
        obj.addProperty("App::PropertyBool", "ProjectToSurface", "Application",
                       "Project load normal to surface")
        obj.ProjectToSurface = True
        
        obj.addProperty("App::PropertyFloat", "LoadEccentricity", "Application",
                       "Load eccentricity from surface centroid")
        obj.LoadEccentricity = 0.0
        
        # Results and integration
        obj.addProperty("App::PropertyForce", "TotalForce", "Results",
                       "Total applied force")
        
        obj.addProperty("App::PropertyFloat", "MomentX", "Results",
                       "Moment about X-axis")
        
        obj.addProperty("App::PropertyFloat", "MomentY", "Results",
                       "Moment about Y-axis")
        
        obj.addProperty("App::PropertyVector", "CenterOfPressure", "Results",
                       "Center of pressure location")
        
        # Visualization properties
        obj.addProperty("App::PropertyBool", "ShowLoadVectors", "Display",
                       "Show load vectors")
        obj.ShowLoadVectors = True
        
        obj.addProperty("App::PropertyFloat", "VectorScale", "Display",
                       "Scale factor for load vectors")
        obj.VectorScale = 1.0
        
        obj.addProperty("App::PropertyColor", "LoadColor", "Display",
                       "Color for load display")
        obj.LoadColor = (1.0, 0.0, 0.0)  # Red
        
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
        
        obj.addProperty("App::PropertyInteger", "LoadSteps", "Analysis",
                       "Number of load steps for nonlinear analysis")
        obj.LoadSteps = 1
        
        # Initialize calculations
        self.calculateLoadProperties(obj)
    
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
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating load properties: {e}\n")
    
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
    
    def execute(self, obj):
        """Update load visualization and integration."""
        if obj.TargetFaces:
            self.updateLoadVisualization(obj)
            self.calculateTotalLoad(obj)
    
    def updateLoadVisualization(self, obj):
        """Update visual representation of the load."""
        try:
            if not obj.ShowLoadVectors:
                return
                
            # Clear existing visualization
            doc = App.ActiveDocument
            if not doc:
                return
                
            # Create load vectors
            self.createLoadVectors(obj)
            
            # Show load distribution if requested
            if obj.ShowLoadDistribution:
                self.createLoadDistribution(obj)
                
        except Exception as e:
            App.Console.PrintError(f"Error updating load visualization: {e}\n")
    
    def createLoadVectors(self, obj):
        """Create load vector visualization."""
        try:
            doc = App.ActiveDocument
            if not doc or not obj.TargetFaces:
                return
                
            for i, face_obj in enumerate(obj.TargetFaces):
                if hasattr(face_obj, 'Shape'):
                    # Get face center
                    center = face_obj.Shape.CenterOfMass
                    
                    # Calculate load direction and magnitude
                    direction = obj.LoadDirection
                    if obj.ProjectToSurface and hasattr(face_obj.Shape, 'normalAt'):
                        # Use surface normal
                        u, v = face_obj.Shape.Surface.parameter(center)
                        direction = face_obj.Shape.normalAt(u, v)
                        direction = direction * -1  # Point inward for loads
                    
                    # Create arrow for visualization
                    self.createLoadArrow(doc, center, direction, obj, i)
                    
        except Exception as e:
            App.Console.PrintError(f"Error creating load vectors: {e}\n")
    
    def createLoadArrow(self, doc, position, direction, load_obj, index):
        """Create a single load arrow."""
        try:
            arrow_name = f"LoadArrow_{load_obj.Label}_{index}"
            
            # Remove existing arrow
            if hasattr(doc, 'getObject') and doc.getObject(arrow_name):
                doc.removeObject(arrow_name)
            
            # Create arrow geometry
            arrow_length = 100.0 * load_obj.VectorScale  # mm
            arrow_head = 20.0  # mm
            
            # Scale by load magnitude
            intensity = self.parseLoadIntensity(load_obj.LoadIntensity)
            if intensity > 0:
                arrow_length *= min(intensity / 2.4, 5.0)  # Scale relative to 2.4 kN/m²
            
            direction_norm = direction.normalize()
            end_point = position + (direction_norm * arrow_length)
            
            # Create arrow shaft
            shaft = Part.makeCylinder(2.0, arrow_length)
            
            # Create arrow head
            cone = Part.makeCone(0, 8.0, arrow_head)
            cone.translate(App.Vector(0, 0, arrow_length))
            
            # Combine shaft and head
            arrow = shaft.fuse(cone)
            
            # Rotate to align with direction
            # (Implementation would need proper rotation matrix)
            
            # Create object
            arrow_obj = doc.addObject("Part::Feature", arrow_name)
            arrow_obj.Shape = arrow
            arrow_obj.Placement.Base = position
            
            # Set color
            if hasattr(arrow_obj, 'ViewObject'):
                color = load_obj.LoadColor if hasattr(load_obj, 'LoadColor') else (1.0, 0.0, 0.0)
                arrow_obj.ViewObject.ShapeColor = color
                arrow_obj.ViewObject.LineColor = color
                
        except Exception as e:
            App.Console.PrintError(f"Error creating load arrow: {e}\n")
    
    def calculateTotalLoad(self, obj):
        """Calculate total load and moments."""
        try:
            if not obj.TargetFaces:
                return
                
            total_force = 0.0
            moment_x = 0.0
            moment_y = 0.0
            
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    area = face_obj.Shape.Area / 1000000  # Convert mm² to m²
                    force = intensity * area  # kN
                    total_force += force
                    
                    # Calculate moments about origin
                    center = face_obj.Shape.CenterOfMass
                    moment_x += force * (center.y / 1000)  # kN⋅m
                    moment_y += force * (center.x / 1000)  # kN⋅m
            
            obj.TotalForce = f"{total_force:.2f} kN"
            obj.MomentX = moment_x
            obj.MomentY = moment_y
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating total load: {e}\n")
        
        # Load magnitude and direction
        obj.addProperty("App::PropertyPressure", "Magnitude", "Load",
                       "Load magnitude per unit area")
        obj.Magnitude = "5.0 kN/m^2"
        
        obj.addProperty("App::PropertyEnumeration", "Direction", "Load",
                       "Load direction")
        obj.Direction = ["Normal", "+X Global", "-X Global", "+Y Global", "-Y Global", "+Z Global", "-Z Global", "Custom"]
        obj.Direction = "Normal"
        
        obj.addProperty("App::PropertyVector", "CustomDirection", "Load",
                       "Custom load direction vector (normalized)")
        obj.CustomDirection = App.Vector(0, 0, -1)
        
        # Load distribution
        obj.addProperty("App::PropertyEnumeration", "Distribution", "Distribution",
                       "Load distribution pattern")
        obj.Distribution = ["Uniform", "Linear X", "Linear Y", "Bilinear", "Parabolic", "Point Load", "User Defined"]
        obj.Distribution = "Uniform"
        
        obj.addProperty("App::PropertyFloatList", "DistributionParameters", "Distribution",
                       "Parameters for distribution pattern")
        obj.DistributionParameters = [1.0]  # Default uniform
        
        obj.addProperty("App::PropertyString", "DistributionFunction", "Distribution",
                       "Custom distribution function (Python expression)")
        obj.DistributionFunction = "1.0"  # Default uniform
        
        # Spatial variation
        obj.addProperty("App::PropertyVector", "VariationCenter", "Distribution",
                       "Center point for load variation")
        
        obj.addProperty("App::PropertyFloat", "VariationRadius", "Distribution",
                       "Characteristic radius for load variation (mm)")
        obj.VariationRadius = 1000.0
        
        # Load case information
        obj.addProperty("App::PropertyString", "LoadCaseName", "Case",
                       "Load case name/identifier")
        obj.LoadCaseName = "DL1"
        
        obj.addProperty("App::PropertyString", "LoadCombination", "Case",
                       "Load combination identifier")
        obj.LoadCombination = ""
        
        obj.addProperty("App::PropertyFloat", "LoadFactor", "Case",
                       "Load factor for combinations")
        obj.LoadFactor = 1.0
        
        # Time variation
        obj.addProperty("App::PropertyBool", "IsTimeDependent", "Time",
                       "Time-dependent load")
        obj.IsTimeDependent = False
        
        obj.addProperty("App::PropertyEnumeration", "TimeFunction", "Time",
                       "Time variation function")
        obj.TimeFunction = ["Constant", "Linear", "Sinusoidal", "Custom"]
        obj.TimeFunction = "Constant"
        
        obj.addProperty("App::PropertyFloatList", "TimeParameters", "Time",
                       "Parameters for time function")
        obj.TimeParameters = [1.0]
        
        obj.addProperty("App::PropertyFloat", "Duration", "Time",
                       "Load duration (seconds)")
        obj.Duration = 0.0
        
        # Thermal properties (for thermal loads)
        obj.addProperty("App::PropertyFloat", "Temperature", "Thermal",
                       "Temperature change (°C)")
        obj.Temperature = 0.0
        
        obj.addProperty("App::PropertyFloat", "TemperatureGradient", "Thermal",
                       "Temperature gradient through thickness (°C/mm)")
        obj.TemperatureGradient = 0.0
        
        # Wind load properties
        obj.addProperty("App::PropertyFloat", "WindSpeed", "Wind",
                       "Design wind speed (m/s)")
        obj.WindSpeed = 0.0
        
        obj.addProperty("App::PropertyFloat", "PressureCoefficient", "Wind",
                       "Wind pressure coefficient")
        obj.PressureCoefficient = 1.0
        
        obj.addProperty("App::PropertyEnumeration", "WindDirection", "Wind",
                       "Wind direction")
        obj.WindDirection = ["0°", "45°", "90°", "135°", "180°", "225°", "270°", "315°"]
        obj.WindDirection = "0°"
        
        # Visualization properties
        obj.addProperty("App::PropertyBool", "ShowLoadArrows", "Visualization",
                       "Show load arrows")
        obj.ShowLoadArrows = True
        
        obj.addProperty("App::PropertyInteger", "ArrowDensity", "Visualization",
                       "Number of arrows per edge")
        obj.ArrowDensity = 5
        
        obj.addProperty("App::PropertyFloat", "ArrowScale", "Visualization",
                       "Arrow scale factor")
        obj.ArrowScale = 1.0
        
        obj.addProperty("App::PropertyColor", "LoadColor", "Visualization",
                       "Load visualization color")
        obj.LoadColor = (1.0, 0.0, 0.0)  # Red
        
        # Analysis integration
        obj.addProperty("App::PropertyPythonObject", "LoadVisualization", "Internal",
                       "Load arrow visualization objects")
        obj.LoadVisualization = []
        
        obj.addProperty("App::PropertyFloat", "TotalLoad", "Results",
                       "Total applied load (calculated)")
        obj.TotalLoad = 0.0
        
        obj.addProperty("App::PropertyVector", "LoadResultant", "Results",
                       "Load resultant vector")
        obj.LoadResultant = App.Vector(0, 0, 0)
        
        obj.addProperty("App::PropertyVector", "LoadCenter", "Results",
                       "Center of load application")
        
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
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        if prop == "TargetFaces":
            self._update_loaded_area(obj)
            self._update_load_center(obj)
        elif prop == "LoadType":
            self._update_load_category(obj)
        elif prop in ["Magnitude", "Distribution", "DistributionParameters"]:
            self._calculate_total_load(obj)
        elif prop == "Direction":
            self._update_direction_vector(obj)
        elif prop == "ShowLoadArrows":
            self._update_visualization(obj)
        elif prop in ["ArrowDensity", "ArrowScale"]:
            if obj.ShowLoadArrows:
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
        if not hasattr(obj, 'LoadType'):
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
    
    def _calculate_total_load(self, obj) -> None:
        """Calculate total applied load."""
        if not hasattr(obj, 'LoadedArea') or not hasattr(obj, 'Magnitude'):
            return
        
        try:
            area = obj.LoadedArea.getValueAs('mm^2')
            magnitude = obj.Magnitude.getValueAs('N/mm^2')  # Convert to N/mm²
            
            # Apply distribution factor
            distribution_factor = 1.0
            if hasattr(obj, 'Distribution') and obj.Distribution != "Uniform":
                distribution_factor = self._get_distribution_factor(obj)
            
            total_load = magnitude * area * distribution_factor
            obj.TotalLoad = total_load
            
            # Calculate load resultant vector
            direction_vector = self._get_direction_vector(obj)
            obj.LoadResultant = direction_vector * total_load
            
            App.Console.PrintMessage(f"Total load calculated: {total_load:.2f} N\n")
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating total load: {e}\n")
            obj.TotalLoad = 0.0
    
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
    
    def _update_direction_vector(self, obj) -> None:
        """Update direction vector when direction changes."""
        self._calculate_total_load(obj)
    
    def _update_load_center(self, obj) -> None:
        """Calculate center of load application."""
        if not hasattr(obj, 'TargetFaces') or not obj.TargetFaces:
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
        if not obj.ShowLoadArrows:
            self._clear_visualization(obj)
            return
        
        self._create_load_arrows(obj)
    
    def _clear_visualization(self, obj) -> None:
        """Clear existing load visualization."""
        if hasattr(obj, 'LoadVisualization') and obj.LoadVisualization:
            doc = App.ActiveDocument
            for vis_obj in obj.LoadVisualization:
                if hasattr(vis_obj, 'Name') and doc.getObject(vis_obj.Name):
                    doc.removeObject(vis_obj.Name)
            obj.LoadVisualization = []
    
    def _create_load_arrows(self, obj) -> None:
        """Create 3D arrows for load visualization."""
        if not hasattr(obj, 'TargetFaces') or not obj.TargetFaces:
            return
        
        self._clear_visualization(obj)
        
        direction_vector = self._get_direction_vector(obj)
        magnitude = obj.Magnitude.getValueAs('N/mm^2') if hasattr(obj, 'Magnitude') else 0.0
        scale = obj.ArrowScale if hasattr(obj, 'ArrowScale') else 1.0
        density = obj.ArrowDensity if hasattr(obj, 'ArrowDensity') else 5
        
        arrow_objects = []
        
        for face_obj in obj.TargetFaces:
            if hasattr(face_obj, 'Shape'):
                shape = face_obj.Shape
                if hasattr(shape, 'Faces'):
                    for face in shape.Faces:
                        arrows = self._create_arrows_on_face(obj, face, direction_vector, magnitude, scale, density)
                        arrow_objects.extend(arrows)
        
        obj.LoadVisualization = arrow_objects
    
    def _create_arrows_on_face(self, obj, face, direction, magnitude, scale, density) -> List:
        """Create arrows on a specific face."""
        arrows = []
        
        try:
            # Create grid of points on face
            u_params = np.linspace(0.1, 0.9, density)
            v_params = np.linspace(0.1, 0.9, density)
            
            for u in u_params:
                for v in v_params:
                    try:
                        # Get point on surface
                        point = face.valueAt(u, v)
                        
                        # Get load magnitude at this point
                        local_magnitude = self._get_load_at_point(obj, point, magnitude)
                        
                        # Create arrow
                        arrow = self._create_single_arrow(point, direction, local_magnitude, scale)
                        if arrow:
                            arrows.append(arrow)
                            
                    except Exception as e:
                        continue  # Skip problematic points
        
        except Exception as e:
            App.Console.PrintWarning(f"Error creating arrows on face: {e}\n")
        
        return arrows
    
    def _get_load_at_point(self, obj, point: App.Vector, base_magnitude: float) -> float:
        """Get load magnitude at a specific point based on distribution."""
        if not hasattr(obj, 'Distribution'):
            return base_magnitude
        
        distribution = obj.Distribution
        
        if distribution == "Uniform":
            return base_magnitude
        elif distribution == "Linear X":
            # Simplified linear variation in X direction
            if len(obj.DistributionParameters) >= 2:
                min_factor = obj.DistributionParameters[0]
                max_factor = obj.DistributionParameters[1]
                # Assume variation from 0 to face width
                factor = min_factor + (max_factor - min_factor) * 0.5  # Simplified
                return base_magnitude * factor
        # Add more distribution types as needed
        
        return base_magnitude
    
    def _create_single_arrow(self, start_point: App.Vector, direction: App.Vector, magnitude: float, scale: float):
        """Create a single load arrow."""
        try:
            doc = App.ActiveDocument
            
            # Calculate arrow length based on magnitude and scale
            arrow_length = magnitude * scale * 100  # Scale factor
            if arrow_length < 10:  # Minimum arrow length
                arrow_length = 10
            
            # Create arrow geometry
            end_point = start_point + (direction * arrow_length)
            
            # Create arrow line
            arrow_line = Part.makeLine(start_point, end_point)
            
            # Create arrow head (cone)
            head_radius = arrow_length * 0.1
            head_height = arrow_length * 0.2
            head_center = end_point - (direction * head_height * 0.5)
            
            # Create cone for arrow head
            cone = Part.makeCone(0, head_radius, head_height, head_center, direction)
            
            # Combine line and cone
            arrow_shape = Part.makeCompound([arrow_line, cone])
            
            # Create FreeCAD object
            arrow_obj = doc.addObject("Part::Feature", f"LoadArrow_{obj.Label}")
            arrow_obj.Shape = arrow_shape
            
            # Set visual properties
            if App.GuiUp:
                arrow_obj.ViewObject.ShapeColor = obj.LoadColor if hasattr(obj, 'LoadColor') else (1.0, 0.0, 0.0)
                arrow_obj.ViewObject.LineColor = obj.LoadColor if hasattr(obj, 'LoadColor') else (1.0, 0.0, 0.0)
                arrow_obj.ViewObject.Transparency = 20
            
            return arrow_obj
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating arrow: {e}\n")
            return None
    
    def execute(self, obj) -> None:
        """
        Update area load and validate properties.
        
        Args:
            obj: The DocumentObject being executed
        """
        # Update geometric properties
        self._update_loaded_area(obj)
        self._update_load_center(obj)
        
        # Calculate loads
        self._calculate_total_load(obj)
        
        # Update visualization
        if obj.ShowLoadArrows:
            self._update_visualization(obj)
        
        # Validate load definition
        self._validate_load(obj)
    
    def _validate_load(self, obj) -> None:
        """Validate load definition and set validity flag."""
        is_valid = True
        warnings = []
        
        # Check if target faces exist
        if not hasattr(obj, 'TargetFaces') or not obj.TargetFaces:
            is_valid = False
            warnings.append("No target faces defined")
        
        # Check magnitude
        if hasattr(obj, 'Magnitude'):
            try:
                mag = obj.Magnitude.getValueAs('N/mm^2')
                if mag <= 0:
                    warnings.append("Load magnitude should be positive")
            except:
                is_valid = False
                warnings.append("Invalid load magnitude")
        
        # Check load factors for time dependent loads
        if hasattr(obj, 'IsTimeDependent') and obj.IsTimeDependent:
            if not hasattr(obj, 'Duration') or obj.Duration <= 0:
                warnings.append("Time dependent load requires positive duration")
        
        obj.IsValid = is_valid
        
        if warnings:
            App.Console.PrintWarning(f"Load {obj.Label} warnings: {'; '.join(warnings)}\n")
    
    def get_equivalent_nodal_loads(self, obj, target_nodes: List) -> Dict:
        """
        Calculate equivalent nodal loads for finite element analysis.
        
        Args:
            obj: The DocumentObject
            target_nodes: List of nodes to distribute loads to
            
        Returns:
            Dictionary of nodal loads
        """
        nodal_loads = {}
        
        if not obj.IsValid or obj.TotalLoad == 0:
            return nodal_loads
        
        try:
            total_load = obj.TotalLoad
            direction = self._get_direction_vector(obj)
            
            # Simple distribution - divide total load among nodes
            load_per_node = total_load / len(target_nodes) if target_nodes else 0
            
            for node in target_nodes:
                if hasattr(node, 'Name'):
                    nodal_loads[node.Name] = {
                        'Fx': direction.x * load_per_node,
                        'Fy': direction.y * load_per_node,
                        'Fz': direction.z * load_per_node
                    }
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating nodal loads: {e}\n")
        
        return nodal_loads


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