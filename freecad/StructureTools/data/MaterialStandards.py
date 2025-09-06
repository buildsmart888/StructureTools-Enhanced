# -*- coding: utf-8 -*-
"""
Material Standards Database

This module contains standard material properties for various design codes
and specifications used in structural engineering.
"""

# ASTM Steel Standards
ASTM_STEEL = {
    "ASTM_A36": {
        "YieldStrength": "250 MPa",
        "UltimateStrength": "400 MPa", 
        "ModulusElasticity": "200000 MPa",
        "Density": "7850 kg/m^3",
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "Grade 36",
        "TestingStandard": "ASTM A6"
    },
    "ASTM_A992": {
        "YieldStrength": "345 MPa",
        "UltimateStrength": "450 MPa",
        "ModulusElasticity": "200000 MPa", 
        "Density": "7850 kg/m^3",
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "Grade 50",
        "TestingStandard": "ASTM A6"
    },
    "ASTM_A572_Gr50": {
        "YieldStrength": "345 MPa",
        "UltimateStrength": "450 MPa",
        "ModulusElasticity": "200000 MPa",
        "Density": "7850 kg/m^3", 
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "Grade 50",
        "TestingStandard": "ASTM A572"
    }
}

# European Standards (EN)
EN_STEEL = {
    "EN_S235": {
        "YieldStrength": "235 MPa",
        "UltimateStrength": "360 MPa",
        "ModulusElasticity": "210000 MPa",
        "Density": "7850 kg/m^3",
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "S235",
        "TestingStandard": "EN 10025"
    },
    "EN_S355": {
        "YieldStrength": "355 MPa", 
        "UltimateStrength": "510 MPa",
        "ModulusElasticity": "210000 MPa",
        "Density": "7850 kg/m^3",
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "S355",
        "TestingStandard": "EN 10025"
    },
    "EN_S460": {
        "YieldStrength": "460 MPa",
        "UltimateStrength": "540 MPa", 
        "ModulusElasticity": "210000 MPa",
        "Density": "7850 kg/m^3",
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "S460",
        "TestingStandard": "EN 10025"
    }
}

# Concrete Standards
CONCRETE_STANDARDS = {
    "ACI_Normal_25MPa": {
        "CompressiveStrength": "25 MPa",
        "YieldStrength": "25 MPa",
        "UltimateStrength": "25 MPa",
        "ModulusElasticity": "25000 MPa",
        "Density": "2400 kg/m^3",
        "PoissonRatio": 0.20,
        "ThermalExpansion": 10e-6,
        "GradeDesignation": "fc' = 25 MPa",
        "TestingStandard": "ACI 318"
    },
    "ACI_Normal_30MPa": {
        "CompressiveStrength": "30 MPa",
        "YieldStrength": "30 MPa", 
        "UltimateStrength": "30 MPa",
        "ModulusElasticity": "27000 MPa", 
        "Density": "2400 kg/m^3",
        "PoissonRatio": 0.20,
        "ThermalExpansion": 10e-6,
        "GradeDesignation": "fc' = 30 MPa",
        "TestingStandard": "ACI 318"
    },
    "EN_C25/30": {
        "CompressiveStrength": "25 MPa",
        "YieldStrength": "25 MPa",
        "UltimateStrength": "25 MPa",
        "ModulusElasticity": "31000 MPa",
        "Density": "2400 kg/m^3",
        "PoissonRatio": 0.20,
        "ThermalExpansion": 10e-6,
        "GradeDesignation": "C25/30",
        "TestingStandard": "EN 206"
    }
}

# Aluminum Standards
ALUMINUM_STANDARDS = {
    "ASTM_6061_T6": {
        "YieldStrength": "276 MPa",
        "UltimateStrength": "310 MPa",
        "ModulusElasticity": "69000 MPa",
        "Density": "2700 kg/m^3",
        "PoissonRatio": 0.33,
        "ThermalExpansion": 23.6e-6,
        "GradeDesignation": "6061-T6",
        "TestingStandard": "ASTM B221"
    },
    "EN_6082_T6": {
        "YieldStrength": "250 MPa",
        "UltimateStrength": "290 MPa",
        "ModulusElasticity": "70000 MPa",
        "Density": "2700 kg/m^3",
        "PoissonRatio": 0.33,
        "ThermalExpansion": 23.1e-6,
        "GradeDesignation": "6082-T6",
        "TestingStandard": "EN 573"
    }
}

# Combine all standards
MATERIAL_STANDARDS = {
    **ASTM_STEEL,
    **EN_STEEL, 
    **CONCRETE_STANDARDS,
    **ALUMINUM_STANDARDS,
    # Add custom option
    "Custom": {
        "YieldStrength": "250 MPa",
        "UltimateStrength": "400 MPa",
        "ModulusElasticity": "200000 MPa",
        "Density": "7850 kg/m^3",
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "Custom",
        "TestingStandard": "User Defined"
    }
}

# Material categories for organization
MATERIAL_CATEGORIES = {
    "Steel": [
        "ASTM_A36", "ASTM_A992", "ASTM_A572_Gr50", 
        "EN_S235", "EN_S355", "EN_S460"
    ],
    "Concrete": [
        "ACI_Normal_25MPa", "ACI_Normal_30MPa", "EN_C25/30"
    ],
    "Aluminum": [
        "ASTM_6061_T6", "EN_6082_T6"
    ],
    "Custom": ["Custom"]
}

def get_materials_by_category(category: str) -> dict:
    """
    Get all materials in a specific category.
    
    Args:
        category: Material category name
        
    Returns:
        Dictionary of materials in the category
    """
    if category not in MATERIAL_CATEGORIES:
        return {}
    
    materials = {}
    for material_name in MATERIAL_CATEGORIES[category]:
        if material_name in MATERIAL_STANDARDS:
            materials[material_name] = MATERIAL_STANDARDS[material_name]
    
    return materials

def get_material_info(standard_name: str) -> dict:
    """
    Get detailed information for a specific material standard.
    
    Args:
        standard_name: Name of the material standard
        
    Returns:
        Material properties dictionary
    """
    return MATERIAL_STANDARDS.get(standard_name, {})

def validate_material_combination(yield_strength: float, ultimate_strength: float) -> bool:
    """
    Validate that material strength properties are physically reasonable.
    
    Args:
        yield_strength: Yield strength in MPa
        ultimate_strength: Ultimate strength in MPa
        
    Returns:
        True if combination is valid
    """
    # Ultimate strength should be greater than yield strength
    if ultimate_strength <= yield_strength:
        return False
    
    # Check reasonable ratios
    ratio = ultimate_strength / yield_strength
    if ratio < 1.1 or ratio > 2.0:  # Typical range for structural materials
        return False
    
    return True