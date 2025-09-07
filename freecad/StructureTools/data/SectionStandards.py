# -*- coding: utf-8 -*-
"""
Section Standards Database

This module contains standard structural section properties for various design codes
and specifications used in structural engineering.

All dimensions in millimeters (mm) and areas in mm²
Moments of inertia in mm⁴, section moduli in mm³
"""

import math

# AISC Steel Sections - Wide Flange (W-shapes)
AISC_W_SECTIONS = {
    "W12x26": {
        "Type": "Wide Flange",
        "Depth": 310.0,  # mm
        "FlangeWidth": 165.0,
        "WebThickness": 6.1,
        "FlangeThickness": 9.9,
        "Area": 3355.0,  # mm²
        "Weight": 26.3,  # kg/m
        "Ix": 149.7e6,   # mm⁴ 
        "Iy": 17.5e6,
        "Zx": 1064000,   # mm³
        "Zy": 185000,
        "rx": 211.0,     # mm
        "ry": 72.4,
        "J": 120000,     # mm⁴ (Torsional constant)
        "Cw": 72.1e9,    # mm⁶ (Warping constant)
        "Standard": "AISC 360",
        "Grade": "A992"
    },
    "W14x22": {
        "Type": "Wide Flange",
        "Depth": 349.0,
        "FlangeWidth": 127.0,
        "WebThickness": 5.8,
        "FlangeThickness": 8.9,
        "Area": 2806.0,
        "Weight": 22.0,
        "Ix": 146.1e6,
        "Iy": 7.0e6,
        "Zx": 970000,
        "Zy": 97000,
        "rx": 228.0,
        "ry": 50.0,
        "J": 89000,
        "Cw": 26.8e9,
        "Standard": "AISC 360",
        "Grade": "A992"
    },
    "W16x31": {
        "Type": "Wide Flange", 
        "Depth": 394.0,
        "FlangeWidth": 140.0,
        "WebThickness": 6.4,
        "FlangeThickness": 11.2,
        "Area": 3935.0,
        "Weight": 30.9,
        "Ix": 226.1e6,
        "Iy": 12.1e6,
        "Zx": 1319000,
        "Zy": 155000,
        "rx": 240.0,
        "ry": 55.6,
        "J": 165000,
        "Cw": 56.2e9,
        "Standard": "AISC 360",
        "Grade": "A992"
    },
    "W18x35": {
        "Type": "Wide Flange",
        "Depth": 444.0,
        "FlangeWidth": 152.0,
        "WebThickness": 6.9,
        "FlangeThickness": 11.7,
        "Area": 4516.0,
        "Weight": 35.4,
        "Ix": 316.8e6,
        "Iy": 16.4e6,
        "Zx": 1574000,
        "Zy": 190000,
        "rx": 265.0,
        "ry": 60.2,
        "J": 195000,
        "Cw": 80.9e9,
        "Standard": "AISC 360", 
        "Grade": "A992"
    }
}

# European IPE Sections (EN 10025)
EN_IPE_SECTIONS = {
    "IPE100": {
        "Type": "I-Beam",
        "Depth": 100.0,
        "FlangeWidth": 55.0,
        "WebThickness": 4.1,
        "FlangeThickness": 5.7,
        "Area": 1032.0,
        "Weight": 8.1,
        "Ix": 1.71e6,
        "Iy": 0.159e6,
        "Zx": 39300,
        "Zy": 6580,
        "rx": 40.7,
        "ry": 12.4,
        "J": 3460,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "IPE120": {
        "Type": "I-Beam",
        "Depth": 120.0,
        "FlangeWidth": 64.0,
        "WebThickness": 4.4,
        "FlangeThickness": 6.3,
        "Area": 1319.0,
        "Weight": 10.4,
        "Ix": 3.18e6,
        "Iy": 0.278e6,
        "Zx": 60700,
        "Zy": 9280,
        "rx": 49.2,
        "ry": 14.5,
        "J": 6000,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "IPE160": {
        "Type": "I-Beam",
        "Depth": 160.0,
        "FlangeWidth": 82.0,
        "WebThickness": 5.0,
        "FlangeThickness": 7.4,
        "Area": 2010.0,
        "Weight": 15.8,
        "Ix": 8.69e6,
        "Iy": 0.683e6,
        "Zx": 123000,
        "Zy": 17400,
        "rx": 65.7,
        "ry": 18.4,
        "J": 12800,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "IPE200": {
        "Type": "I-Beam",
        "Depth": 200.0,
        "FlangeWidth": 100.0,
        "WebThickness": 5.6,
        "FlangeThickness": 8.5,
        "Area": 2848.0,
        "Weight": 22.4,
        "Ix": 19.4e6,
        "Iy": 1.42e6,
        "Zx": 221000,
        "Zy": 30100,
        "rx": 82.6,
        "ry": 22.4,
        "J": 22800,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "IPE240": {
        "Type": "I-Beam",
        "Depth": 240.0,
        "FlangeWidth": 120.0,
        "WebThickness": 6.2,
        "FlangeThickness": 9.8,
        "Area": 3912.0,
        "Weight": 30.7,
        "Ix": 38.9e6,
        "Iy": 2.84e6,
        "Zx": 367000,
        "Zy": 50900,
        "rx": 99.7,
        "ry": 27.0,
        "J": 47300,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "IPE300": {
        "Type": "I-Beam",
        "Depth": 300.0,
        "FlangeWidth": 150.0,
        "WebThickness": 7.1,
        "FlangeThickness": 10.7,
        "Area": 5381.0,
        "Weight": 42.2,
        "Ix": 83.6e6,
        "Iy": 6.04e6,
        "Zx": 628000,
        "Zy": 89300,
        "rx": 124.0,
        "ry": 33.5,
        "J": 90200,
        "Standard": "EN 10025",
        "Grade": "S355"
    }
}

# European HE Sections (Heavy European)
EN_HE_SECTIONS = {
    "HEB100": {
        "Type": "H-Beam",
        "Depth": 100.0,
        "FlangeWidth": 100.0,
        "WebThickness": 6.0,
        "FlangeThickness": 10.0,
        "Area": 2600.0,
        "Weight": 20.4,
        "Ix": 4.50e6,
        "Iy": 1.67e6,
        "Zx": 104000,
        "Zy": 38500,
        "rx": 41.7,
        "ry": 25.3,
        "J": 41700,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "HEB120": {
        "Type": "H-Beam", 
        "Depth": 120.0,
        "FlangeWidth": 120.0,
        "WebThickness": 6.5,
        "FlangeThickness": 11.0,
        "Area": 3400.0,
        "Weight": 26.7,
        "Ix": 8.64e6,
        "Iy": 3.18e6,
        "Zx": 165000,
        "Zy": 60700,
        "rx": 50.4,
        "ry": 30.6,
        "J": 72600,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "HEB160": {
        "Type": "H-Beam",
        "Depth": 160.0,
        "FlangeWidth": 160.0,
        "WebThickness": 8.0,
        "FlangeThickness": 13.0,
        "Area": 5430.0,
        "Weight": 42.6,
        "Ix": 24.9e6,
        "Iy": 8.89e6,
        "Zx": 354000,
        "Zy": 125000,
        "rx": 67.8,
        "ry": 40.5,
        "J": 188000,
        "Standard": "EN 10025",
        "Grade": "S355"
    },
    "HEB200": {
        "Type": "H-Beam",
        "Depth": 200.0,
        "FlangeWidth": 200.0,
        "WebThickness": 9.0,
        "FlangeThickness": 15.0,
        "Area": 7810.0,
        "Weight": 61.3,
        "Ix": 56.9e6,
        "Iy": 20.1e6,
        "Zx": 642000,
        "Zy": 226000,
        "rx": 85.3,
        "ry": 50.8,
        "J": 386000,
        "Standard": "EN 10025",
        "Grade": "S355"
    }
}

# Hollow Structural Sections (HSS) - Rectangular
HSS_RECTANGULAR = {
    "HSS6x4x1/4": {
        "Type": "Rectangular HSS",
        "Depth": 152.4,  # 6 inches
        "Width": 101.6,  # 4 inches 
        "WallThickness": 6.35,  # 1/4 inch
        "Area": 1419.4,
        "Weight": 11.1,
        "Ix": 12.1e6,
        "Iy": 5.91e6,
        "Zx": 186000,
        "Zy": 135000,
        "rx": 92.5,
        "ry": 64.5,
        "J": 17.2e6,
        "Standard": "AISC 360",
        "Grade": "A500"
    },
    "HSS8x6x1/4": {
        "Type": "Rectangular HSS",
        "Depth": 203.2,
        "Width": 152.4,
        "WallThickness": 6.35,
        "Area": 2032.3,
        "Weight": 16.0,
        "Ix": 27.7e6,
        "Iy": 17.7e6,
        "Zx": 314000,
        "Zy": 269000,
        "rx": 117.0,
        "ry": 93.2,
        "J": 39.2e6,
        "Standard": "AISC 360",
        "Grade": "A500"
    }
}

# Hollow Structural Sections (HSS) - Circular
HSS_CIRCULAR = {
    "HSS4.000x0.250": {
        "Type": "Circular HSS",
        "Diameter": 101.6,  # 4 inches
        "WallThickness": 6.35,  # 0.250 inches
        "Area": 1890.3,
        "Weight": 14.8,
        "I": 7.07e6,  # Same for both axes
        "Z": 178000,
        "r": 61.2,
        "J": 14.1e6,
        "Standard": "AISC 360",
        "Grade": "A500"
    },
    "HSS6.625x0.280": {
        "Type": "Circular HSS",
        "Diameter": 168.3,
        "WallThickness": 7.11,
        "Area": 3590.3,
        "Weight": 28.2,
        "I": 22.5e6,
        "Z": 343000,
        "r": 79.2,
        "J": 45.0e6,
        "Standard": "AISC 360",
        "Grade": "A500"
    }
}

# Angles (L-shapes)
ANGLE_SECTIONS = {
    "L4x4x1/2": {
        "Type": "Equal Angle",
        "LegWidth": 101.6,  # 4 inches
        "LegHeight": 101.6,
        "Thickness": 12.7,  # 1/2 inch
        "Area": 2387.1,
        "Weight": 18.7,
        "Ix": 5.63e6,
        "Iy": 5.63e6,
        "Ixy": 2.89e6,  # Product of inertia
        "rx": 48.5,
        "ry": 48.5,
        "xc": 29.5,  # Centroid location
        "yc": 29.5,
        "Standard": "AISC 360",
        "Grade": "A36"
    },
    "L6x4x1/2": {
        "Type": "Unequal Angle",
        "LegWidth": 152.4,  # 6 inches
        "LegHeight": 101.6,  # 4 inches
        "Thickness": 12.7,
        "Area": 3032.3,
        "Weight": 23.8,
        "Ix": 16.8e6,
        "Iy": 6.27e6,
        "Ixy": 6.27e6,
        "rx": 74.4,
        "ry": 45.5,
        "xc": 39.9,
        "yc": 19.1,
        "Standard": "AISC 360",
        "Grade": "A36"
    }
}

# Standard Channels (C-shapes)
CHANNEL_SECTIONS = {
    "C9x13.4": {
        "Type": "Channel",
        "Depth": 228.6,  # 9 inches
        "FlangeWidth": 58.7,
        "WebThickness": 8.4,
        "FlangeThickness": 13.0,
        "Area": 1706.5,
        "Weight": 13.4,
        "Ix": 47.9e6,
        "Iy": 3.88e6,
        "Zx": 447000,
        "Zy": 47600,
        "rx": 167.6,
        "ry": 47.8,
        "x0": 17.5,  # Shear center location
        "Standard": "AISC 360",
        "Grade": "A36"
    },
    "C12x20.7": {
        "Type": "Channel",
        "Depth": 304.8,
        "FlangeWidth": 76.2,
        "WebThickness": 10.2,
        "FlangeThickness": 17.4,
        "Area": 2641.9,
        "Weight": 20.7,
        "Ix": 129.0e6,
        "Iy": 8.13e6,
        "Zx": 916000,
        "Zy": 84700,
        "rx": 221.0,
        "ry": 55.6,
        "x0": 19.6,
        "Standard": "AISC 360",
        "Grade": "A36"
    }
}

# Combine all section standards
SECTION_STANDARDS = {
    **AISC_W_SECTIONS,
    **EN_IPE_SECTIONS,
    **EN_HE_SECTIONS,
    **HSS_RECTANGULAR,
    **HSS_CIRCULAR,
    **ANGLE_SECTIONS,
    **CHANNEL_SECTIONS
}

# Section categories for organization
SECTION_CATEGORIES = {
    "AISC Wide Flange": list(AISC_W_SECTIONS.keys()),
    "European IPE": list(EN_IPE_SECTIONS.keys()),
    "European HEB": list(EN_HE_SECTIONS.keys()),
    "HSS Rectangular": list(HSS_RECTANGULAR.keys()),
    "HSS Circular": list(HSS_CIRCULAR.keys()),
    "Angles": list(ANGLE_SECTIONS.keys()),
    "Channels": list(CHANNEL_SECTIONS.keys())
}

def get_sections_by_category(category: str) -> dict:
    """
    Get all sections in a specific category.
    
    Args:
        category: Section category name
        
    Returns:
        Dictionary of sections in the category
    """
    if category not in SECTION_CATEGORIES:
        return {}
    
    sections = {}
    for section_name in SECTION_CATEGORIES[category]:
        if section_name in SECTION_STANDARDS:
            sections[section_name] = SECTION_STANDARDS[section_name]
    
    return sections

def get_section_info(section_name: str) -> dict:
    """
    Get detailed information for a specific section.
    
    Args:
        section_name: Name of the section
        
    Returns:
        Section properties dictionary
    """
    return SECTION_STANDARDS.get(section_name, {})

def calculate_section_modulus(I: float, c: float) -> float:
    """
    Calculate section modulus from moment of inertia and distance to extreme fiber.
    
    Args:
        I: Moment of inertia (mm⁴)
        c: Distance from neutral axis to extreme fiber (mm)
        
    Returns:
        Section modulus (mm³)
    """
    if c <= 0:
        return 0
    return I / c

def calculate_radius_of_gyration(I: float, A: float) -> float:
    """
    Calculate radius of gyration.
    
    Args:
        I: Moment of inertia (mm⁴) 
        A: Cross-sectional area (mm²)
        
    Returns:
        Radius of gyration (mm)
    """
    if A <= 0:
        return 0
    return math.sqrt(I / A)

def find_sections_by_depth_range(min_depth: float, max_depth: float) -> dict:
    """
    Find all sections within a depth range.
    
    Args:
        min_depth: Minimum depth in mm
        max_depth: Maximum depth in mm
        
    Returns:
        Dictionary of sections within the range
    """
    matching_sections = {}
    
    for section_name, properties in SECTION_STANDARDS.items():
        if "Depth" in properties:
            depth = properties["Depth"]
            if min_depth <= depth <= max_depth:
                matching_sections[section_name] = properties
    
    return matching_sections

def find_sections_by_weight_limit(max_weight: float) -> dict:
    """
    Find all sections under a weight limit.
    
    Args:
        max_weight: Maximum weight in kg/m
        
    Returns:
        Dictionary of sections under the limit
    """
    matching_sections = {}
    
    for section_name, properties in SECTION_STANDARDS.items():
        if "Weight" in properties:
            weight = properties["Weight"]
            if weight <= max_weight:
                matching_sections[section_name] = properties
    
    return matching_sections

def validate_section_selection(section_name: str, required_properties: list) -> bool:
    """
    Validate that a section has all required properties.
    
    Args:
        section_name: Name of the section
        required_properties: List of required property names
        
    Returns:
        True if section has all required properties
    """
    if section_name not in SECTION_STANDARDS:
        return False
    
    section_props = SECTION_STANDARDS[section_name]
    
    for prop in required_properties:
        if prop not in section_props:
            return False
    
    return True

# Default section for new objects
DEFAULT_SECTION = "W12x26"

# Section property groups for UI organization
SECTION_PROPERTY_GROUPS = {
    "Dimensions": ["Depth", "FlangeWidth", "WebThickness", "FlangeThickness", "Diameter", "WallThickness"],
    "Properties": ["Area", "Weight", "Ix", "Iy", "Zx", "Zy", "rx", "ry", "J", "Cw"],
    "Classification": ["Type", "Standard", "Grade"]
}