#!/usr/bin/env python3
"""
Direct Material Fix

This script directly imports MaterialStandards and fixes existing material objects
without going through the full module system that may have encoding issues.

Usage in FreeCAD:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_direct_material_fix.py').read())
"""

import sys
import os

# Add current path
sys.path.insert(0, os.path.dirname(__file__))

def direct_import_material_standards():
    """Directly import MaterialStandards without full module."""
    try:
        # Import only the MaterialStandards data
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
        print(f"[OK] MaterialStandards imported: {len(MATERIAL_STANDARDS)} standards")
        
        if "ACI_Normal_30MPa" in MATERIAL_STANDARDS:
            props = MATERIAL_STANDARDS["ACI_Normal_30MPa"]
            print(f"[OK] ACI_Normal_30MPa found: {props}")
            return MATERIAL_STANDARDS
        else:
            print("[ERROR] ACI_Normal_30MPa not found")
            return None
            
    except Exception as e:
        print(f"[ERROR] Import failed: {e}")
        return None

def fix_existing_material_directly():
    """Fix existing material object directly using FreeCAD API."""
    import FreeCAD as App
    
    if not App.ActiveDocument:
        print("[ERROR] No active document")
        return False
    
    # Import MaterialStandards directly
    standards = direct_import_material_standards()
    if not standards:
        return False
    
    # Find target material object
    target_obj = None
    for obj in App.ActiveDocument.Objects:
        if (hasattr(obj, 'MaterialStandard') and hasattr(obj, 'Density') and
            ('ACI_Normal_30MP' in obj.Label or 'ACI_Normal_30MP' in obj.Name)):
            target_obj = obj
            break
    
    if not target_obj:
        print("[ERROR] Target material object not found")
        return False
    
    print(f"[OK] Found target object: {target_obj.Label}")
    
    # Get concrete properties
    if "ACI_Normal_30MPa" not in standards:
        print("[ERROR] ACI_Normal_30MPa not in standards")
        return False
    
    concrete_props = standards["ACI_Normal_30MPa"]
    print(f"[OK] Using concrete properties: {concrete_props}")
    
    # Apply properties directly
    try:
        target_obj.Density = concrete_props["Density"]
        target_obj.ModulusElasticity = concrete_props["ModulusElasticity"]
        target_obj.PoissonRatio = concrete_props["PoissonRatio"]
        
        # Also set MaterialStandard to ensure consistency
        target_obj.MaterialStandard = "ACI_Normal_30MPa"
        
        # Force recompute
        target_obj.recompute()
        App.ActiveDocument.recompute()
        
        print(f"[SUCCESS] Properties updated:")
        print(f"  Density: {target_obj.Density}")
        print(f"  Modulus: {target_obj.ModulusElasticity}")
        print(f"  Poisson: {target_obj.PoissonRatio}")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Failed to apply properties: {e}")
        return False

def test_material_standards_values():
    """Test what values are actually in MaterialStandards."""
    standards = direct_import_material_standards()
    if not standards:
        return
    
    print("\n[INFO] Testing MaterialStandards values:")
    
    # Test concrete standards
    concrete_standards = [k for k in standards.keys() if 'ACI' in k or 'concrete' in k.lower()]
    print(f"[INFO] Concrete standards: {concrete_standards}")
    
    for std_name in concrete_standards:
        props = standards[std_name]
        print(f"\n[INFO] {std_name}:")
        print(f"  Density: {props.get('Density', 'missing')}")
        print(f"  ModulusElasticity: {props.get('ModulusElasticity', 'missing')}")
        print(f"  PoissonRatio: {props.get('PoissonRatio', 'missing')}")

def run_direct_material_fix():
    """Run the direct material fix."""
    print("DIRECT MATERIAL FIX")
    print("=" * 50)
    
    # Test MaterialStandards values first
    test_material_standards_values()
    
    print("\n" + "=" * 50)
    print("APPLYING FIX TO EXISTING OBJECT")
    print("=" * 50)
    
    # Fix existing object
    success = fix_existing_material_directly()
    
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    
    if success:
        print("[SUCCESS] Material object fixed!")
        print("Check the Property Panel - values should now be:")
        print("  Density: 2400 kg/m³")
        print("  ModulusElasticity: 27000 MPa") 
        print("  PoissonRatio: 0.20")
    else:
        print("[ERROR] Fix failed - check error messages above")

if __name__ == "__main__":
    run_direct_material_fix()