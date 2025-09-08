# -*- coding: utf-8 -*-
"""
StructuralProfile Custom Document Object

A parametric 2D profile object that extends Arch Profile functionality
with structural engineering properties for integration with calc system.
"""

import FreeCAD as App
import Part
import Draft
import math
import os
from typing import Dict, Any, Optional

# Safe GUI imports
try:
    import FreeCADGui as Gui
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

# Import structural database integration
try:
    from ..data.SectionStandards import SECTION_STANDARDS, get_section_info
    from ..data.ProfileGeometryGenerator import generate_geometry_from_properties
    SECTION_DATABASE_AVAILABLE = True
except ImportError:
    SECTION_DATABASE_AVAILABLE = False
    SECTION_STANDARDS = {}
    get_section_info = lambda x: {}
    generate_geometry_from_properties = lambda x, y: {}

# Import enhanced database if available
try:
    from ..data.EnhancedSteelDatabase import (
        get_enhanced_database, get_enhanced_sections, 
        get_enhanced_section_data, get_section_geometry_data
    )
    ENHANCED_DATABASE_AVAILABLE = True
except ImportError:
    ENHANCED_DATABASE_AVAILABLE = False

class StructuralProfile:
    """Custom Document Object for parametric structural profiles"""
    
    def __init__(self, obj):
        self.Type = "StructuralProfile"
        obj.Proxy = self
        
        # Profile identification
        obj.addProperty("App::PropertyString", "ProfileName", "Profile", 
                       "Profile name/designation")
        obj.addProperty("App::PropertyEnumeration", "ProfileType", "Profile",
                       "Type of structural profile")
        obj.ProfileType = ["I-Beam", "Wide Flange", "Channel", "Angle", "HSS Rectangular", 
                          "HSS Circular", "Rectangle", "Circle", "T-Section", "Custom"]
        obj.ProfileType = "I-Beam"
        
        # Standard section selection
        if SECTION_DATABASE_AVAILABLE or ENHANCED_DATABASE_AVAILABLE:
            obj.addProperty("App::PropertyEnumeration", "StandardSection", "Profile",
                           "Standard section from database")
            self._update_standard_sections(obj)
        
        # Geometric parameters for I-Beam/Wide Flange
        obj.addProperty("App::PropertyLength", "Height", "Dimensions", 
                       "Overall height of the profile").Height = "200 mm"
        obj.addProperty("App::PropertyLength", "Width", "Dimensions", 
                       "Overall width/flange width").Width = "100 mm"
        obj.addProperty("App::PropertyLength", "WebThickness", "Dimensions", 
                       "Web thickness").WebThickness = "8 mm"
        obj.addProperty("App::PropertyLength", "FlangeThickness", "Dimensions", 
                       "Flange thickness").FlangeThickness = "12 mm"
        
        # Additional parameters for other sections
        obj.addProperty("App::PropertyLength", "Thickness", "Dimensions", 
                       "Wall thickness (for HSS, angles)").Thickness = "6 mm"
        obj.addProperty("App::PropertyLength", "Diameter", "Dimensions", 
                       "Diameter (for circular sections)").Diameter = "100 mm"
        obj.addProperty("App::PropertyLength", "Leg1", "Dimensions", 
                       "First leg length (for angles)").Leg1 = "75 mm"
        obj.addProperty("App::PropertyLength", "Leg2", "Dimensions", 
                       "Second leg length (for angles)").Leg2 = "50 mm"
        
        # Calculated structural properties
        obj.addProperty("App::PropertyArea", "Area", "Properties", 
                       "Cross-sectional area").Area = 0.0
        obj.addProperty("App::PropertyFloat", "MomentInertiaX", "Properties", 
                       "Moment of inertia about X axis").MomentInertiaX = 0.0
        obj.addProperty("App::PropertyFloat", "MomentInertiaY", "Properties", 
                       "Moment of inertia about Y axis").MomentInertiaY = 0.0
        obj.addProperty("App::PropertyFloat", "PolarMomentInertia", "Properties", 
                       "Polar moment of inertia").PolarMomentInertia = 0.0
        obj.addProperty("App::PropertyFloat", "SectionModulusX", "Properties", 
                       "Section modulus about X axis").SectionModulusX = 0.0
        obj.addProperty("App::PropertyFloat", "SectionModulusY", "Properties", 
                       "Section modulus about Y axis").SectionModulusY = 0.0
        obj.addProperty("App::PropertyFloat", "RadiusGyrationX", "Properties", 
                       "Radius of gyration about X axis").RadiusGyrationX = 0.0
        obj.addProperty("App::PropertyFloat", "RadiusGyrationY", "Properties", 
                       "Radius of gyration about Y axis").RadiusGyrationY = 0.0
        obj.addProperty("App::PropertyFloat", "Weight", "Properties", 
                       "Weight per unit length (kg/m)").Weight = 0.0
        
        # Visual properties
        obj.addProperty("App::PropertyBool", "ShowDimensions", "Visualization", 
                       "Show dimension annotations").ShowDimensions = True
        obj.addProperty("App::PropertyBool", "ShowCenterLines", "Visualization", 
                       "Show center lines").ShowCenterLines = True
        obj.addProperty("App::PropertyFloat", "Scale", "Visualization", 
                       "Scale factor for display").Scale = 1.0
        
        # Integration properties
        obj.addProperty("App::PropertyPythonObject", "CalcProperties", "Integration", 
                       "Properties formatted for calc integration")
        obj.addProperty("App::PropertyPythonObject", "GeometryData", "Integration", 
                       "Geometry data for advanced operations")
    
    def _update_standard_sections(self, obj):
        """Update available standard sections based on databases"""
        sections = ["Custom"]
        
        if ENHANCED_DATABASE_AVAILABLE:
            try:
                # Get all available sections from enhanced database
                db = get_enhanced_database()
                if db and db.available:
                    all_sections = []
                    shape_types = db.get_available_shape_types()
                    for shape_type in shape_types:
                        sections_for_type = get_enhanced_sections(shape_type)
                        all_sections.extend(sections_for_type)
                    sections.extend(sorted(set(all_sections)))
            except Exception as e:
                App.Console.PrintWarning(f"Enhanced database error: {e}\n")
        
        if SECTION_DATABASE_AVAILABLE:
            sections.extend(sorted(SECTION_STANDARDS.keys()))
        
        if hasattr(obj, "StandardSection"):
            obj.StandardSection = sections
        else:
            obj.addProperty("App::PropertyEnumeration", "StandardSection", "Profile",
                           "Standard section from database")
            obj.StandardSection = sections
            
        obj.StandardSection = "Custom"
    
    def onChanged(self, obj, prop):
        """Handle property changes"""
        if prop == "ProfileType":
            self._update_visibility_based_on_type(obj)
        elif prop == "StandardSection" and obj.StandardSection != "Custom":
            self._apply_standard_section(obj)
        elif prop in ["Height", "Width", "WebThickness", "FlangeThickness", 
                     "Thickness", "Diameter", "Leg1", "Leg2", "ProfileType"]:
            self._update_calculated_properties(obj)
    
    def _update_visibility_based_on_type(self, obj):
        """Update property visibility based on profile type"""
        profile_type = obj.ProfileType
        
        # Define which properties are relevant for each profile type
        visibility_map = {
            "I-Beam": ["Height", "Width", "WebThickness", "FlangeThickness"],
            "Wide Flange": ["Height", "Width", "WebThickness", "FlangeThickness"],
            "Channel": ["Height", "Width", "WebThickness", "FlangeThickness"],
            "HSS Rectangular": ["Height", "Width", "Thickness"],
            "HSS Circular": ["Diameter", "Thickness"],
            "Rectangle": ["Height", "Width"],
            "Circle": ["Diameter"],
            "Angle": ["Leg1", "Leg2", "Thickness"],
            "T-Section": ["Height", "Width", "WebThickness", "FlangeThickness"],
        }
        
        # Note: FreeCAD doesn't directly support property visibility
        # This is a placeholder for future implementation
        relevant_props = visibility_map.get(profile_type, [])
        App.Console.PrintLog(f"Profile type {profile_type} uses properties: {relevant_props}\n")
    
    def _apply_standard_section(self, obj):
        """Apply standard section properties from database"""
        if obj.StandardSection == "Custom":
            return
        
        section_data = None
        geometry_data = None
        
        # Try enhanced database first
        if ENHANCED_DATABASE_AVAILABLE:
            try:
                db = get_enhanced_database()
                if db and db.available:
                    # Find which shape type contains this section
                    shape_types = db.get_available_shape_types()
                    for shape_type in shape_types:
                        sections = get_enhanced_sections(shape_type)
                        if obj.StandardSection in sections:
                            section_data = get_enhanced_section_data(shape_type, obj.StandardSection)
                            geometry_data = get_section_geometry_data(shape_type, obj.StandardSection)
                            break
            except Exception as e:
                App.Console.PrintWarning(f"Enhanced database error: {e}\n")
        
        # Fallback to basic database
        if not section_data and SECTION_DATABASE_AVAILABLE:
            section_data = get_section_info(obj.StandardSection)
        
        if section_data:
            self._update_from_database(obj, section_data, geometry_data)
            obj.ProfileName = obj.StandardSection
    
    def _update_from_database(self, obj, section_data, geometry_data=None):
        """Update object properties from database data"""
        def extract_value(data, keys, default=0.0):
            """Extract numeric value from various data formats"""
            for key in keys if isinstance(keys, list) else [keys]:
                if key in data:
                    value = data[key]
                    if isinstance(value, dict) and 'value' in value:
                        return float(value['value'])
                    elif isinstance(value, (int, float)):
                        return float(value)
            return default
        
        # Geometric properties
        height = extract_value(section_data, ['height', 'Depth', 'd', 'h'])
        width = extract_value(section_data, ['width', 'FlangeWidth', 'bf', 'b'])
        web_thickness = extract_value(section_data, ['web_thickness', 'WebThickness', 'tw'])
        flange_thickness = extract_value(section_data, ['flange_thickness', 'FlangeThickness', 'tf'])
        thickness = extract_value(section_data, ['thickness', 't'])
        diameter = extract_value(section_data, ['diameter', 'outer_diameter', 'OD', 'd'])
        
        # Update dimensions based on available data (check if property exists first)
        if height > 0 and hasattr(obj, 'Height'):
            obj.Height = f"{height} mm"
        if width > 0 and hasattr(obj, 'Width'):
            obj.Width = f"{width} mm"
        if web_thickness > 0 and hasattr(obj, 'WebThickness'):
            obj.WebThickness = f"{web_thickness} mm"
        if flange_thickness > 0 and hasattr(obj, 'FlangeThickness'):
            obj.FlangeThickness = f"{flange_thickness} mm"
        if thickness > 0 and hasattr(obj, 'Thickness'):
            obj.Thickness = f"{thickness} mm"
        if diameter > 0 and hasattr(obj, 'Diameter'):
            obj.Diameter = f"{diameter} mm"
        
        # Structural properties
        area = extract_value(section_data, ['area', 'Area', 'A'])
        ix = extract_value(section_data, ['moment_inertia_x', 'ix', 'Ix'])
        iy = extract_value(section_data, ['moment_inertia_y', 'iy', 'Iy'])
        sx = extract_value(section_data, ['section_modulus_x', 'sx', 'Sx'])
        sy = extract_value(section_data, ['section_modulus_y', 'sy', 'Sy'])
        weight = extract_value(section_data, ['weight', 'Weight', 'w'])
        
        # Update structural properties (check if property exists first)
        if area > 0 and hasattr(obj, 'Area'):
            obj.Area = area  # Area in mm², PropertyArea handles units automatically
        if ix > 0 and hasattr(obj, 'MomentInertiaX'):
            obj.MomentInertiaX = ix / 1e6  # Convert mm⁴ to m⁴
        if iy > 0 and hasattr(obj, 'MomentInertiaY'):
            obj.MomentInertiaY = iy / 1e6
        if sx > 0 and hasattr(obj, 'SectionModulusX'):
            obj.SectionModulusX = sx / 1e9  # Convert mm³ to m³
        if sy > 0 and hasattr(obj, 'SectionModulusY'):
            obj.SectionModulusY = sy / 1e9
        if weight > 0 and hasattr(obj, 'Weight'):
            obj.Weight = weight
        
        # Calculate polar moment and radii of gyration
        if ix > 0 and iy > 0:
            obj.PolarMomentInertia = (ix + iy) / 1e6
        if area > 0:
            if ix > 0:
                obj.RadiusGyrationX = math.sqrt(ix / area) / 1000  # Convert to m
            if iy > 0:
                obj.RadiusGyrationY = math.sqrt(iy / area) / 1000
        
        # Store enhanced data for integration
        if geometry_data:
            obj.GeometryData = geometry_data
        
        # Prepare calc integration properties
        calc_props = {
            'Area': area / 1e6 if area > 0 else 0,  # Convert to m²
            'Iy': ix / 1e12 if ix > 0 else 0,       # Convert to m⁴
            'Iz': iy / 1e12 if iy > 0 else 0,
            'J': (ix + iy) / 1e12 if ix > 0 and iy > 0 else 0,
            'Sy': sx / 1e9 if sx > 0 else 0,        # Convert to m³
            'Sz': sy / 1e9 if sy > 0 else 0
        }
        obj.CalcProperties = calc_props
        
        App.Console.PrintMessage(f"Applied standard section {obj.StandardSection}\n")
    
    def _update_calculated_properties(self, obj):
        """Calculate structural properties from geometric parameters"""
        if obj.StandardSection != "Custom":
            return  # Don't override database values
        
        profile_type = obj.ProfileType
        
        try:
            if profile_type in ["I-Beam", "Wide Flange"]:
                self._calculate_i_beam_properties(obj)
            elif profile_type == "HSS Rectangular":
                self._calculate_rectangular_hss_properties(obj)
            elif profile_type == "HSS Circular":
                self._calculate_circular_hss_properties(obj)
            elif profile_type == "Rectangle":
                self._calculate_rectangle_properties(obj)
            elif profile_type == "Circle":
                self._calculate_circle_properties(obj)
            elif profile_type == "Angle":
                self._calculate_angle_properties(obj)
            elif profile_type == "Channel":
                self._calculate_channel_properties(obj)
            
        except Exception as e:
            App.Console.PrintError(f"Property calculation error: {e}\n")
    
    def _safe_get_dimension(self, obj, property_name, default_value):
        """Safely get dimension value from property"""
        if not hasattr(obj, property_name):
            return default_value
        
        prop_value = getattr(obj, property_name)
        
        try:
            # If it's a FreeCAD Quantity object
            if hasattr(prop_value, 'getValueAs'):
                return prop_value.getValueAs('mm')
            # If it's a string with units
            elif isinstance(prop_value, str):
                # Parse string like "200 mm" 
                import re
                match = re.match(r'([0-9.]+)\s*mm', prop_value)
                if match:
                    return float(match.group(1))
            # If it's a number
            elif isinstance(prop_value, (int, float)):
                return float(prop_value)
        except:
            pass
        
        return default_value
    
    def _safe_set_property(self, obj, property_name, value):
        """Safely set property value"""
        try:
            if hasattr(obj, property_name):
                setattr(obj, property_name, value)
                return True
            else:
                App.Console.PrintWarning(f"Property {property_name} not found on object\n")
                return False
        except Exception as e:
            App.Console.PrintError(f"Failed to set {property_name}: {e}\n")
            return False
    
    def _calculate_i_beam_properties(self, obj):
        """Calculate I-beam structural properties"""
        h = self._safe_get_dimension(obj, 'Height', 200.0)
        b = self._safe_get_dimension(obj, 'Width', 100.0)
        tw = self._safe_get_dimension(obj, 'WebThickness', 8.0)
        tf = self._safe_get_dimension(obj, 'FlangeThickness', 12.0)
        
        # Cross-sectional area
        area = 2 * b * tf + (h - 2 * tf) * tw  # mm²
        
        # Moment of inertia about X axis (strong axis)
        ix = (b * h**3 - (b - tw) * (h - 2*tf)**3) / 12  # mm⁴
        
        # Moment of inertia about Y axis (weak axis)
        iy = (2 * tf * b**3 + (h - 2*tf) * tw**3) / 12  # mm⁴
        
        # Section moduli
        sx = ix / (h/2) if h > 0 else 0  # mm³
        sy = iy / (b/2) if b > 0 else 0  # mm³
        
        # Radii of gyration
        rx = math.sqrt(ix / area) if area > 0 else 0  # mm
        ry = math.sqrt(iy / area) if area > 0 else 0  # mm
        
        # Weight (assuming steel density 7850 kg/m³)
        weight = area * 7.85e-6  # kg/m
        
        # Update properties safely
        self._safe_set_property(obj, 'Area', area)  # Area in mm², no unit string needed
        self._safe_set_property(obj, 'MomentInertiaX', ix / 1e6)  # Convert to m⁴
        self._safe_set_property(obj, 'MomentInertiaY', iy / 1e6)
        self._safe_set_property(obj, 'PolarMomentInertia', (ix + iy) / 1e6)
        self._safe_set_property(obj, 'SectionModulusX', sx / 1e9)  # Convert to m³
        self._safe_set_property(obj, 'SectionModulusY', sy / 1e9)
        self._safe_set_property(obj, 'RadiusGyrationX', rx / 1000)  # Convert to m
        self._safe_set_property(obj, 'RadiusGyrationY', ry / 1000)
        self._safe_set_property(obj, 'Weight', weight)
        
        # Prepare calc properties
        calc_props = {
            'Area': area / 1e6,     # m²
            'Iy': ix / 1e12,        # m⁴ (major axis)
            'Iz': iy / 1e12,        # m⁴ (minor axis)
            'J': (ix + iy) / 1e12,  # m⁴
            'Sy': sx / 1e9,         # m³
            'Sz': sy / 1e9          # m³
        }
        self._safe_set_property(obj, 'CalcProperties', calc_props)
    
    def _calculate_rectangular_hss_properties(self, obj):
        """Calculate rectangular HSS properties"""
        h = self._safe_get_dimension(obj, 'Height', 200.0)
        b = self._safe_get_dimension(obj, 'Width', 100.0)
        t = self._safe_get_dimension(obj, 'Thickness', 6.0)
        
        # Cross-sectional area
        area = 2 * (h * t + b * t) - 4 * t * t  # mm²
        
        # Moment of inertia
        ix = (b * h**3 - (b - 2*t) * (h - 2*t)**3) / 12  # mm⁴
        iy = (h * b**3 - (h - 2*t) * (b - 2*t)**3) / 12  # mm⁴
        
        # Section moduli
        sx = ix / (h/2) if h > 0 else 0
        sy = iy / (b/2) if b > 0 else 0
        
        # Update properties safely
        self._safe_set_property(obj, 'Area', area)  # Area in mm², no unit string needed
        self._safe_set_property(obj, 'MomentInertiaX', ix / 1e6)
        self._safe_set_property(obj, 'MomentInertiaY', iy / 1e6)
        self._safe_set_property(obj, 'PolarMomentInertia', (ix + iy) / 1e6)
        self._safe_set_property(obj, 'SectionModulusX', sx / 1e9)
        self._safe_set_property(obj, 'SectionModulusY', sy / 1e9)
        self._safe_set_property(obj, 'RadiusGyrationX', math.sqrt(ix / area) / 1000 if area > 0 else 0)
        self._safe_set_property(obj, 'RadiusGyrationY', math.sqrt(iy / area) / 1000 if area > 0 else 0)
        self._safe_set_property(obj, 'Weight', area * 7.85e-6)
        
        # Calc properties
        calc_props = {
            'Area': area / 1e6,
            'Iy': ix / 1e12,
            'Iz': iy / 1e12,
            'J': (ix + iy) / 1e12,
            'Sy': sx / 1e9,
            'Sz': sy / 1e9
        }
        self._safe_set_property(obj, 'CalcProperties', calc_props)
    
    def _calculate_circular_hss_properties(self, obj):
        """Calculate circular HSS properties"""
        d = self._safe_get_dimension(obj, 'Diameter', 100.0)
        t = self._safe_get_dimension(obj, 'Thickness', 6.0)
        
        # Cross-sectional area
        area = math.pi * (d * t - t * t)  # mm²
        
        # Moment of inertia
        ix = iy = math.pi * (d**4 - (d - 2*t)**4) / 64  # mm⁴
        j = 2 * ix  # Polar moment for circular sections
        
        # Section modulus
        sx = sy = ix / (d/2) if d > 0 else 0
        
        # Update properties
        obj.Area = f"{area} mm^2"
        obj.MomentInertiaX = ix / 1e6
        obj.MomentInertiaY = iy / 1e6
        obj.PolarMomentInertia = j / 1e6
        obj.SectionModulusX = sx / 1e9
        obj.SectionModulusY = sy / 1e9
        obj.RadiusGyrationX = math.sqrt(ix / area) / 1000 if area > 0 else 0
        obj.RadiusGyrationY = math.sqrt(iy / area) / 1000 if area > 0 else 0
        obj.Weight = area * 7.85e-6
        
        # Calc properties
        calc_props = {
            'Area': area / 1e6,
            'Iy': ix / 1e12,
            'Iz': iy / 1e12,
            'J': j / 1e12,
            'Sy': sx / 1e9,
            'Sz': sy / 1e9
        }
        obj.CalcProperties = calc_props
    
    def _calculate_rectangle_properties(self, obj):
        """Calculate solid rectangle properties"""
        h = self._safe_get_dimension(obj, 'Height', 200.0)
        b = self._safe_get_dimension(obj, 'Width', 100.0)
        
        area = b * h
        ix = b * h**3 / 12
        iy = h * b**3 / 12
        
        obj.Area = f"{area} mm^2"
        obj.MomentInertiaX = ix / 1e6
        obj.MomentInertiaY = iy / 1e6
        obj.PolarMomentInertia = (ix + iy) / 1e6
        obj.SectionModulusX = (ix / (h/2)) / 1e9 if h > 0 else 0
        obj.SectionModulusY = (iy / (b/2)) / 1e9 if b > 0 else 0
        obj.Weight = area * 7.85e-6
        
        calc_props = {
            'Area': area / 1e6,
            'Iy': ix / 1e12,
            'Iz': iy / 1e12,
            'J': (ix + iy) / 1e12,
            'Sy': (ix / (h/2)) / 1e9 if h > 0 else 0,
            'Sz': (iy / (b/2)) / 1e9 if b > 0 else 0
        }
        obj.CalcProperties = calc_props
    
    def _calculate_circle_properties(self, obj):
        """Calculate solid circle properties"""
        d = self._safe_get_dimension(obj, 'Diameter', 100.0)
        r = d / 2
        
        area = math.pi * r**2
        ix = iy = math.pi * r**4 / 4
        j = math.pi * r**4 / 2
        
        obj.Area = f"{area} mm^2"
        obj.MomentInertiaX = ix / 1e6
        obj.MomentInertiaY = iy / 1e6
        obj.PolarMomentInertia = j / 1e6
        obj.SectionModulusX = (ix / r) / 1e9 if r > 0 else 0
        obj.SectionModulusY = (iy / r) / 1e9 if r > 0 else 0
        obj.Weight = area * 7.85e-6
        
        calc_props = {
            'Area': area / 1e6,
            'Iy': ix / 1e12,
            'Iz': iy / 1e12,
            'J': j / 1e12,
            'Sy': (ix / r) / 1e9 if r > 0 else 0,
            'Sz': (iy / r) / 1e9 if r > 0 else 0
        }
        obj.CalcProperties = calc_props
    
    def _calculate_angle_properties(self, obj):
        """Calculate angle section properties (simplified)"""
        leg1 = self._safe_get_dimension(obj, 'Leg1', 75.0)
        leg2 = self._safe_get_dimension(obj, 'Leg2', 50.0)
        t = self._safe_get_dimension(obj, 'Thickness', 6.0)
        
        # Simplified calculation for equal or unequal angles
        area = (leg1 + leg2 - t) * t
        
        # Approximate moments of inertia
        ix = (leg1 * t**3 + t * leg2**3) / 3
        iy = (leg2 * t**3 + t * leg1**3) / 3
        
        obj.Area = f"{area} mm^2"
        obj.MomentInertiaX = ix / 1e6
        obj.MomentInertiaY = iy / 1e6
        obj.PolarMomentInertia = (ix + iy) / 1e6
        obj.Weight = area * 7.85e-6
        
        calc_props = {
            'Area': area / 1e6,
            'Iy': ix / 1e12,
            'Iz': iy / 1e12,
            'J': (ix + iy) / 1e12,
            'Sy': 0,  # Complex for angles
            'Sz': 0
        }
        obj.CalcProperties = calc_props
    
    def _calculate_channel_properties(self, obj):
        """Calculate channel section properties (simplified)"""
        h = self._safe_get_dimension(obj, 'Height', 200.0)
        b = self._safe_get_dimension(obj, 'Width', 75.0)
        tw = self._safe_get_dimension(obj, 'WebThickness', 8.0)
        tf = self._safe_get_dimension(obj, 'FlangeThickness', 12.0)
        
        # Simplified channel calculation
        area = 2 * b * tf + (h - 2 * tf) * tw
        ix = (tw * h**3 + 2 * b * tf * (h - tf)**2) / 12
        iy = (2 * tf * b**3 + (h - 2*tf) * tw**3) / 12
        
        obj.Area = f"{area} mm^2"
        obj.MomentInertiaX = ix / 1e6
        obj.MomentInertiaY = iy / 1e6
        obj.PolarMomentInertia = (ix + iy) / 1e6
        obj.Weight = area * 7.85e-6
        
        calc_props = {
            'Area': area / 1e6,
            'Iy': ix / 1e12,
            'Iz': iy / 1e12,
            'J': (ix + iy) / 1e12,
            'Sy': (ix / (h/2)) / 1e9 if h > 0 else 0,
            'Sz': (iy / (b/2)) / 1e9 if b > 0 else 0
        }
        obj.CalcProperties = calc_props
    
    def execute(self, obj):
        """Generate 2D profile geometry using advanced geometry generator"""
        try:
            # Use AdvancedGeometryGenerator for precise geometry creation
            from ..data.ProfileGeometryGenerator import advanced_geometry_generator
            
            # Extract dimensions from object properties
            dimensions = self._extract_dimensions(obj)
            
            # Generate 2D face using advanced geometry generator
            face = advanced_geometry_generator.create_profile_face(
                profile_type=obj.ProfileType,
                dimensions=dimensions
            )
            
            if face:
                # Scale the face if needed
                if hasattr(obj, 'Scale') and obj.Scale != 1.0:
                    matrix = App.Matrix()
                    matrix.scale(obj.Scale, obj.Scale, 1.0)
                    face = face.transformGeometry(matrix)
                
                obj.Shape = face
                
                # Update calculated properties
                self._update_calculated_properties(obj)
            else:
                # Fallback to legacy geometry creation
                face = self._create_legacy_geometry(obj)
                if face:
                    obj.Shape = face
                    self._update_calculated_properties(obj)
            
        except Exception as e:
            App.Console.PrintError(f"Profile geometry creation failed: {e}\n")
            # Fallback to legacy system
            try:
                face = self._create_legacy_geometry(obj)
                if face:
                    obj.Shape = face
                    self._update_calculated_properties(obj)
                else:
                    obj.Shape = Part.Shape()  # Ensure valid shape
            except:
                obj.Shape = Part.Shape()
    
    def _extract_dimensions(self, obj) -> Dict[str, float]:
        """Extract dimensions from object properties as dictionary"""
        dimensions = {}
        
        # Common dimensions
        if hasattr(obj, 'Height'):
            dimensions['height'] = obj.Height.getValueAs('mm')
        if hasattr(obj, 'Width'):
            dimensions['width'] = obj.Width.getValueAs('mm')
        if hasattr(obj, 'WebThickness'):
            dimensions['web_thickness'] = obj.WebThickness.getValueAs('mm')
        if hasattr(obj, 'FlangeThickness'):
            dimensions['flange_thickness'] = obj.FlangeThickness.getValueAs('mm')
        if hasattr(obj, 'Thickness'):
            dimensions['thickness'] = obj.Thickness.getValueAs('mm')
        if hasattr(obj, 'Diameter'):
            dimensions['diameter'] = obj.Diameter.getValueAs('mm')
        if hasattr(obj, 'Leg1'):
            dimensions['leg1'] = obj.Leg1.getValueAs('mm')
        if hasattr(obj, 'Leg2'):
            dimensions['leg2'] = obj.Leg2.getValueAs('mm')
            
        return dimensions
    
    def _create_legacy_geometry(self, obj):
        """Legacy geometry creation as fallback"""
        profile_type = obj.ProfileType
        
        # Legacy geometry creation methods
        if profile_type in ["I-Beam", "Wide Flange"]:
            return self._create_i_beam_face(obj)
        elif profile_type == "HSS Rectangular":
            return self._create_rectangular_hss_face(obj)
        elif profile_type == "HSS Circular":
            return self._create_circular_hss_face(obj)
        elif profile_type == "Rectangle":
            return self._create_rectangle_face(obj)
        elif profile_type == "Circle":
            return self._create_circle_face(obj)
        elif profile_type == "Angle":
            return self._create_angle_face(obj)
        elif profile_type == "Channel":
            return self._create_channel_face(obj)
        elif profile_type == "T-Section":
            return self._create_t_section_face(obj)
        else:
            return self._create_rectangle_face(obj)  # Default
    
    def _create_i_beam_face(self, obj):
        """Create I-beam face geometry"""
        h = obj.Height.getValueAs('mm')
        b = obj.Width.getValueAs('mm')
        tw = obj.WebThickness.getValueAs('mm')
        tf = obj.FlangeThickness.getValueAs('mm')
        
        # Create I-beam profile points
        points = [
            App.Vector(-b/2, -h/2, 0),    # Bottom left of bottom flange
            App.Vector(b/2, -h/2, 0),     # Bottom right of bottom flange
            App.Vector(b/2, -h/2+tf, 0),  # Top right of bottom flange
            App.Vector(tw/2, -h/2+tf, 0), # Bottom right of web
            App.Vector(tw/2, h/2-tf, 0),  # Top right of web
            App.Vector(b/2, h/2-tf, 0),   # Bottom right of top flange
            App.Vector(b/2, h/2, 0),      # Top right of top flange
            App.Vector(-b/2, h/2, 0),     # Top left of top flange
            App.Vector(-b/2, h/2-tf, 0),  # Bottom left of top flange
            App.Vector(-tw/2, h/2-tf, 0), # Top left of web
            App.Vector(-tw/2, -h/2+tf, 0),# Bottom left of web
            App.Vector(-b/2, -h/2+tf, 0), # Top left of bottom flange
            App.Vector(-b/2, -h/2, 0)     # Close polygon
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)
    
    def _create_rectangular_hss_face(self, obj):
        """Create rectangular HSS face geometry"""
        h = obj.Height.getValueAs('mm')
        b = obj.Width.getValueAs('mm')
        t = obj.Thickness.getValueAs('mm')
        
        # Create outer rectangle
        outer_points = [
            App.Vector(-b/2, -h/2, 0),
            App.Vector(b/2, -h/2, 0),
            App.Vector(b/2, h/2, 0),
            App.Vector(-b/2, h/2, 0),
            App.Vector(-b/2, -h/2, 0)
        ]
        
        # Create inner rectangle
        inner_points = [
            App.Vector(-(b/2-t), -(h/2-t), 0),
            App.Vector((b/2-t), -(h/2-t), 0),
            App.Vector((b/2-t), (h/2-t), 0),
            App.Vector(-(b/2-t), (h/2-t), 0),
            App.Vector(-(b/2-t), -(h/2-t), 0)
        ]
        
        outer_wire = Part.makePolygon(outer_points)
        inner_wire = Part.makePolygon(inner_points)
        
        outer_face = Part.Face(outer_wire)
        inner_face = Part.Face(inner_wire)
        
        return outer_face.cut(inner_face)
    
    def _create_circular_hss_face(self, obj):
        """Create circular HSS face geometry"""
        d = obj.Diameter.getValueAs('mm')
        t = obj.Thickness.getValueAs('mm')
        
        outer_circle = Part.makeCircle(d/2, App.Vector(0,0,0))
        inner_circle = Part.makeCircle(d/2-t, App.Vector(0,0,0))
        
        outer_face = Part.Face(outer_circle)
        inner_face = Part.Face(inner_circle)
        
        return outer_face.cut(inner_face)
    
    def _create_rectangle_face(self, obj):
        """Create solid rectangle face geometry"""
        h = obj.Height.getValueAs('mm')
        b = obj.Width.getValueAs('mm')
        
        points = [
            App.Vector(-b/2, -h/2, 0),
            App.Vector(b/2, -h/2, 0),
            App.Vector(b/2, h/2, 0),
            App.Vector(-b/2, h/2, 0),
            App.Vector(-b/2, -h/2, 0)
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)
    
    def _create_circle_face(self, obj):
        """Create solid circle face geometry"""
        d = obj.Diameter.getValueAs('mm')
        circle = Part.makeCircle(d/2, App.Vector(0,0,0))
        return Part.Face(circle)
    
    def _create_angle_face(self, obj):
        """Create angle face geometry"""
        leg1 = obj.Leg1.getValueAs('mm')
        leg2 = obj.Leg2.getValueAs('mm')
        t = obj.Thickness.getValueAs('mm')
        
        # Create L-shape points
        points = [
            App.Vector(0, 0, 0),
            App.Vector(leg2, 0, 0),
            App.Vector(leg2, t, 0),
            App.Vector(t, t, 0),
            App.Vector(t, leg1, 0),
            App.Vector(0, leg1, 0),
            App.Vector(0, 0, 0)
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)
    
    def _create_channel_face(self, obj):
        """Create channel face geometry"""
        h = obj.Height.getValueAs('mm')
        b = obj.Width.getValueAs('mm')
        tw = obj.WebThickness.getValueAs('mm')
        tf = obj.FlangeThickness.getValueAs('mm')
        
        # Create C-shape points
        points = [
            App.Vector(0, -h/2, 0),
            App.Vector(b, -h/2, 0),
            App.Vector(b, -h/2 + tf, 0),
            App.Vector(tw, -h/2 + tf, 0),
            App.Vector(tw, h/2 - tf, 0),
            App.Vector(b, h/2 - tf, 0),
            App.Vector(b, h/2, 0),
            App.Vector(0, h/2, 0),
            App.Vector(0, -h/2, 0)
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)
    
    def _create_t_section_face(self, obj):
        """Create T-section face geometry"""
        h = obj.Height.getValueAs('mm')
        b = obj.Width.getValueAs('mm')
        tw = obj.WebThickness.getValueAs('mm')
        tf = obj.FlangeThickness.getValueAs('mm')
        
        # Create T-shape points
        points = [
            App.Vector(-b/2, h/2, 0),      # Top left of flange
            App.Vector(b/2, h/2, 0),       # Top right of flange
            App.Vector(b/2, h/2-tf, 0),    # Bottom right of flange
            App.Vector(tw/2, h/2-tf, 0),   # Top right of web
            App.Vector(tw/2, -h/2, 0),     # Bottom right of web
            App.Vector(-tw/2, -h/2, 0),    # Bottom left of web
            App.Vector(-tw/2, h/2-tf, 0),  # Top left of web
            App.Vector(-b/2, h/2-tf, 0),   # Bottom left of flange
            App.Vector(-b/2, h/2, 0)       # Close polygon
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)


class ViewProviderStructuralProfile:
    """View Provider for StructuralProfile"""
    
    def __init__(self, vobj):
        vobj.Proxy = self
        self.Object = vobj.Object
        
        # Display properties (check if they exist first)
        if not hasattr(vobj, "ShowProperties"):
            vobj.addProperty("App::PropertyBool", "ShowProperties", "Display",
                            "Show property annotations")
            vobj.ShowProperties = False
        
        # LineColor often exists by default, only add if missing
        if not hasattr(vobj, "LineColor"):
            vobj.addProperty("App::PropertyColor", "LineColor", "Display", 
                            "Line color")
        vobj.LineColor = (0.0, 0.0, 0.0, 1.0)  # Black
        
        if not hasattr(vobj, "LineWidth"):
            vobj.addProperty("App::PropertyFloat", "LineWidth", "Display", 
                            "Line width")
        vobj.LineWidth = 2.0
        
        # FaceColor and Transparency may also exist
        if not hasattr(vobj, "FaceColor"):
            vobj.addProperty("App::PropertyColor", "FaceColor", "Display", 
                            "Face color")
        vobj.FaceColor = (0.8, 0.8, 0.9, 1.0)  # Light blue
        
        if not hasattr(vobj, "Transparency"):
            vobj.addProperty("App::PropertyPercent", "Transparency", "Display", 
                            "Face transparency")
        vobj.Transparency = 20
    
    def attach(self, vobj):
        """Setup the scene sub-graph"""
        self.ViewObject = vobj
        self.Object = vobj.Object
    
    def updateData(self, obj, prop):
        """Update visualization when data changes"""
        if prop in ["ProfileType", "Height", "Width", "StandardSection"]:
            # Trigger redraw
            pass
    
    def onChanged(self, vobj, prop):
        """Handle view property changes"""
        if prop in ["LineColor", "LineWidth", "FaceColor", "Transparency"]:
            # Update display properties
            pass
    
    def getDisplayModes(self, obj):
        """Return available display modes"""
        return ["Flat Lines", "Shaded", "Wireframe"]
    
    def getDefaultDisplayMode(self):
        """Return default display mode"""
        return "Flat Lines"
    
    def setDisplayMode(self, mode):
        """Set display mode"""
        return mode
    
    def getIcon(self):
        """Return object icon"""
        return os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "structural_profile.svg")
    
    def setEdit(self, vobj, mode):
        """Open task panel for editing"""
        if mode == 0:
            if GUI_AVAILABLE:
                from ..taskpanels.ProfileTaskPanel import ProfileTaskPanel
                self.panel = ProfileTaskPanel(vobj.Object)
                Gui.Control.showDialog(self.panel)
                return True
        return False
    
    def unsetEdit(self, vobj, mode):
        """Close task panel"""
        if GUI_AVAILABLE:
            Gui.Control.closeDialog()
        return True


def create_structural_profile(name=None, profile_type="I-Beam", standard_section="Custom"):
    """Create a StructuralProfile object"""
    if not App.ActiveDocument:
        App.newDocument("StructuralProfiles")
    
    if not name:
        name = f"StructuralProfile_{profile_type}"
    
    # Create object
    obj = App.ActiveDocument.addObject("Part::FeaturePython", name)
    
    # Initialize
    StructuralProfile(obj)
    if GUI_AVAILABLE:
        ViewProviderStructuralProfile(obj.ViewObject)
    
    # Set initial properties
    obj.ProfileType = profile_type
    if standard_section != "Custom":
        obj.StandardSection = standard_section
    
    App.ActiveDocument.recompute()
    
    return obj