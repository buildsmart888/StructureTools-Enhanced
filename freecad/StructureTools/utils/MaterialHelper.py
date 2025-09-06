# -*- coding: utf-8 -*-
"""
Material Helper Utilities

This module provides utility functions for working with material databases
and standards in StructureTools.
"""

import FreeCAD as App

# Import Global Units System
try:
    from .units_manager import (
        get_units_manager, format_force, format_stress, format_modulus
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e9:.0f} GPa"

# Import material standards database
try:
    from ..data.MaterialStandards import MATERIAL_STANDARDS, MATERIAL_CATEGORIES, get_material_info
    HAS_DATABASE = True
except ImportError:
    MATERIAL_STANDARDS = {}
    MATERIAL_CATEGORIES = {}
    HAS_DATABASE = False
    def get_material_info(standard_name):
        return {}


def create_material_from_database(standard_name, material_name=None):
    """
    Create a FreeCAD material object from database standard.
    
    Args:
        standard_name: Name of standard in database (e.g., 'ASTM_A992')
        material_name: Optional custom name for material object
        
    Returns:
        Created material object or None if failed
    """
    if not HAS_DATABASE or standard_name not in MATERIAL_STANDARDS:
        App.Console.PrintError(f"Material standard '{standard_name}' not found in database\n")
        return None
    
    doc = App.ActiveDocument
    if not doc:
        App.Console.PrintError("No active document\n")
        return None
    
    # Determine material type based on standard
    material_type = "Steel"  # Default
    props = MATERIAL_STANDARDS[standard_name]
    if 'CompressiveStrength' in props:
        material_type = "Concrete"
    elif 'ACI_Normal' in standard_name or 'EN_C' in standard_name:
        material_type = "Concrete"
    
    App.Console.PrintMessage(f"Creating {material_type} material from standard {standard_name}\n")
    
    try:
        # Try new StructuralMaterial first
        from ..objects.StructuralMaterial import StructuralMaterial, ViewProviderStructuralMaterial
        
        name = material_name or f"Material_{standard_name}"
        obj = doc.addObject("App::DocumentObjectGroupPython", name)
        
        StructuralMaterial(obj)
        ViewProviderStructuralMaterial(obj.ViewObject)
        
        # Set material type
        if hasattr(obj, 'MaterialType'):
            obj.MaterialType = material_type
        
        # Set standard - this will automatically update all properties
        obj.MaterialStandard = standard_name
        
        App.Console.PrintMessage(f"Created StructuralMaterial '{name}' with standard {standard_name}\n")
        doc.recompute()
        return obj
        
    except ImportError:
        # Fallback to basic Material
        from ..material import Material, ViewProviderMaterial
        
        name = material_name or f"Material_{standard_name}"
        obj = doc.addObject("Part::FeaturePython", name)
        
        Material(obj)
        ViewProviderMaterial(obj.ViewObject)
        
        # Set standard and properties
        obj.MaterialStandard = standard_name
        
        # Manually set properties from database
        props = get_material_info(standard_name)
        if 'ModulusElasticity' in props and hasattr(obj, 'ModulusElasticity'):
            obj.ModulusElasticity = props['ModulusElasticity']
        if 'PoissonRatio' in props and hasattr(obj, 'PoissonRatio'):
            obj.PoissonRatio = props['PoissonRatio']
        if 'Density' in props and hasattr(obj, 'Density'):
            obj.Density = props['Density']
        if 'YieldStrength' in props and hasattr(obj, 'YieldStrength'):
            obj.YieldStrength = props['YieldStrength']
        if 'UltimateStrength' in props and hasattr(obj, 'UltimateStrength'):
            obj.UltimateStrength = props['UltimateStrength']
        
        App.Console.PrintMessage(f"Created Material '{name}' with standard {standard_name}\n")
        doc.recompute()
        return obj


def get_calc_properties_from_database(standard_name, unit_length='m', unit_force='kN'):
    """
    Get material properties for calc from database standard.
    
    Args:
        standard_name: Name of standard in database
        unit_length: Target length unit
        unit_force: Target force unit
        
    Returns:
        Dictionary with calc-compatible properties
    """
    if not HAS_DATABASE or standard_name not in MATERIAL_STANDARDS:
        return None
    
    props = get_material_info(standard_name)
    
    try:
        # Extract and convert properties
        E_str = props.get('ModulusElasticity', '200000 MPa')
        E = float(E_str.replace(' MPa', ''))
        
        nu = props.get('PoissonRatio', 0.3)
        G = E / (2 * (1 + nu))
        
        density_str = props.get('Density', '7850 kg/m^3')
        density_kg_m3 = float(density_str.replace(' kg/m^3', ''))
        density_kn_m3 = density_kg_m3 * 9.81 / 1000  # Convert to kN/m³
        
        return {
            'name': standard_name,
            'E': float(E),
            'G': float(G),
            'nu': float(nu),
            'density': float(density_kn_m3),
            'unit_system': f'{unit_force}-{unit_length}'
        }
        
    except Exception as e:
        App.Console.PrintError(f"Error processing database material {standard_name}: {e}\n")
        return None


def list_available_standards():
    """Get list of all available material standards."""
    if not HAS_DATABASE:
        return []
    return list(MATERIAL_STANDARDS.keys())


def list_standards_by_category(category):
    """Get material standards by category."""
    if not HAS_DATABASE or category not in MATERIAL_CATEGORIES:
        return []
    return MATERIAL_CATEGORIES[category]


def search_materials(search_term):
    """
    Search for materials containing the search term.
    
    Args:
        search_term: Term to search for in material names/properties
        
    Returns:
        List of matching material standard names
    """
    if not HAS_DATABASE:
        return []
    
    matches = []
    search_lower = search_term.lower()
    
    for standard_name, props in MATERIAL_STANDARDS.items():
        # Search in name
        if search_lower in standard_name.lower():
            matches.append(standard_name)
            continue
        
        # Search in grade designation
        grade = props.get('GradeDesignation', '')
        if search_lower in grade.lower():
            matches.append(standard_name)
            continue
        
        # Search in testing standard
        test_std = props.get('TestingStandard', '')
        if search_lower in test_std.lower():
            matches.append(standard_name)
    
    return matches


def validate_material_properties(material_obj):
    """
    Validate material properties against database standards.
    
    Args:
        material_obj: Material object to validate
        
    Returns:
        List of validation warnings/issues
    """
    warnings = []
    
    if not hasattr(material_obj, 'MaterialStandard'):
        warnings.append("No material standard specified")
        return warnings
    
    standard = material_obj.MaterialStandard
    if not HAS_DATABASE or standard not in MATERIAL_STANDARDS:
        warnings.append(f"Material standard '{standard}' not found in database")
        return warnings
    
    # Get reference properties from database
    ref_props = get_material_info(standard)
    
    # Check Poisson ratio
    if hasattr(material_obj, 'PoissonRatio'):
        nu = material_obj.PoissonRatio
        if not (0.0 <= nu <= 0.5):
            warnings.append(f"Invalid Poisson ratio: {nu} (must be 0.0-0.5)")
        
        # Check against database value
        ref_nu = ref_props.get('PoissonRatio', 0.3)
        if abs(nu - ref_nu) > 0.05:  # Allow 5% tolerance
            warnings.append(f"Poisson ratio {nu} differs significantly from standard {ref_nu}")
    
    # Check strength properties if available
    if hasattr(material_obj, 'YieldStrength') and hasattr(material_obj, 'UltimateStrength'):
        try:
            fy = material_obj.YieldStrength.getValueAs('MPa')
            fu = material_obj.UltimateStrength.getValueAs('MPa')
            
            if fy >= fu:
                warnings.append(f"Yield strength ({fy} MPa) should be less than ultimate strength ({fu} MPa)")
            
            # Check against database values
            ref_fy_str = ref_props.get('YieldStrength', '0 MPa')
            ref_fu_str = ref_props.get('UltimateStrength', '0 MPa')
            
            if ref_fy_str and ref_fu_str:
                ref_fy = float(ref_fy_str.replace(' MPa', ''))
                ref_fu = float(ref_fu_str.replace(' MPa', ''))
                
                if abs(fy - ref_fy) > ref_fy * 0.1:  # 10% tolerance
                    warnings.append(f"Yield strength differs from standard: {fy} vs {ref_fy} MPa")
                
                if abs(fu - ref_fu) > ref_fu * 0.1:  # 10% tolerance
                    warnings.append(f"Ultimate strength differs from standard: {fu} vs {ref_fu} MPa")
        
        except Exception as e:
            warnings.append(f"Error validating strength properties: {e}")
    
    return warnings


def update_material_from_database(material_obj, standard_name=None):
    """
    Update material properties from database standard.
    
    Args:
        material_obj: Material object to update
        standard_name: Optional standard name (uses current if not specified)
        
    Returns:
        True if successful, False otherwise
    """
    if standard_name:
        if hasattr(material_obj, 'MaterialStandard'):
            material_obj.MaterialStandard = standard_name
        else:
            App.Console.PrintWarning("Material object does not support MaterialStandard property\n")
            return False
    
    if not hasattr(material_obj, 'MaterialStandard'):
        App.Console.PrintError("Material object has no MaterialStandard property\n")
        return False
    
    standard = material_obj.MaterialStandard
    if not HAS_DATABASE or standard not in MATERIAL_STANDARDS:
        App.Console.PrintError(f"Material standard '{standard}' not found in database\n")
        return False
    
    try:
        props = get_material_info(standard)
        
        # Update properties if they exist
        if 'ModulusElasticity' in props and hasattr(material_obj, 'ModulusElasticity'):
            material_obj.ModulusElasticity = props['ModulusElasticity']
        
        if 'PoissonRatio' in props and hasattr(material_obj, 'PoissonRatio'):
            material_obj.PoissonRatio = props['PoissonRatio']
        
        if 'Density' in props and hasattr(material_obj, 'Density'):
            material_obj.Density = props['Density']
        
        if 'YieldStrength' in props and hasattr(material_obj, 'YieldStrength'):
            material_obj.YieldStrength = props['YieldStrength']
        
        if 'UltimateStrength' in props and hasattr(material_obj, 'UltimateStrength'):
            material_obj.UltimateStrength = props['UltimateStrength']
        
        if 'GradeDesignation' in props and hasattr(material_obj, 'GradeDesignation'):
            material_obj.GradeDesignation = props['GradeDesignation']
        
        App.Console.PrintMessage(f"Updated material properties from database standard: {standard}\n")
        return True
        
    except Exception as e:
        App.Console.PrintError(f"Error updating material from database: {e}\n")
        return False


def export_material_database(file_path):
    """
    Export material database to JSON file.
    
    Args:
        file_path: Path to save JSON file
    """
    if not HAS_DATABASE:
        App.Console.PrintError("Material database not available\n")
        return False
    
    try:
        import json
        
        export_data = {
            'standards': MATERIAL_STANDARDS,
            'categories': MATERIAL_CATEGORIES,
            'version': '1.0',
            'description': 'StructureTools Material Database Export'
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        App.Console.PrintMessage(f"Material database exported to: {file_path}\n")
        return True
        
    except Exception as e:
        App.Console.PrintError(f"Error exporting material database: {e}\n")
        return False


# Convenience functions for common materials
def create_steel_a992(name="Steel_A992"):
    """Create ASTM A992 steel material."""
    return create_material_from_database("ASTM_A992", name)

def create_steel_a36(name="Steel_A36"):
    """Create ASTM A36 steel material."""
    return create_material_from_database("ASTM_A36", name)

def create_concrete_25mpa(name="Concrete_25MPa"):
    """Create 25 MPa concrete material."""
    return create_material_from_database("ACI_Normal_25MPa", name)

def create_concrete_30mpa(name="Concrete_30MPa"):
    """Create 30 MPa concrete material."""
    return create_material_from_database("ACI_Normal_30MPa", name)