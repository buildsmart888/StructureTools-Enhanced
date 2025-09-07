#!/usr/bin/env python3
"""
Fix Specific Material Object: Material_ACI_Normal_30MPa001

This script specifically fixes the Material_ACI_Normal_30MPa001 object
that is showing steel properties instead of concrete properties.

The object should show:
- Density: 2400 kg/m³ (not 7850 kg/m³)  
- Modulus: 27000 MPa or 27 GPa (not 200 GPa)
- Poisson: 0.20 (not 0.30)

Usage:
1. Make sure the problematic material object exists in your document
2. Run this script in FreeCAD Python console:
   exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\fix_specific_material_object.py').read())
"""

import FreeCAD as App

def find_problematic_material():
    """Find the Material_ACI_Normal_30MPa001 object."""
    if not App.ActiveDocument:
        print("❌ No active document. Please open the document first.")
        return None
    
    # Look for the specific object
    target_names = [
        "Material_ACI_Normal_30MPa001",
        "Material_ACI_Normal_30MPa",  # Might be without the 001 suffix
    ]
    
    found_object = None
    
    for obj in App.ActiveDocument.Objects:
        if obj.Name in target_names or obj.Label in target_names:
            found_object = obj
            break
        # Also check if the name contains the pattern
        if "ACI_Normal_30MP" in obj.Name or "ACI_Normal_30MP" in obj.Label:
            found_object = obj
            break
    
    if found_object:
        print(f"✅ Found material object: {found_object.Label} ({found_object.Name})")
        return found_object
    else:
        print("❌ Material_ACI_Normal_30MPa001 not found in document")
        print("\nAvailable objects:")
        for obj in App.ActiveDocument.Objects:
            if hasattr(obj, 'Density') or 'material' in obj.Name.lower():
                print(f"  - {obj.Label} ({obj.Name})")
        return None

def analyze_material_properties(obj):
    """Analyze current properties of the material object."""
    print(f"\n🔍 Current properties of {obj.Label}:")
    print("="*50)
    
    properties = {}
    
    # Check essential material properties
    if hasattr(obj, 'Density'):
        density_str = str(obj.Density)
        print(f"Density: {density_str}")
        properties['density'] = density_str
        
        # Check if it's steel density (wrong for concrete)
        if '7850' in density_str:
            print("  ❌ PROBLEM: This is STEEL density, not concrete!")
    
    if hasattr(obj, 'ModulusElasticity'):
        modulus_str = str(obj.ModulusElasticity)
        print(f"Modulus Elasticity: {modulus_str}")
        properties['modulus'] = modulus_str
        
        # Check if it's steel modulus (wrong for concrete)
        if '200000' in modulus_str or '200.00 GPa' in modulus_str:
            print("  ❌ PROBLEM: This is STEEL modulus, not concrete!")
    
    if hasattr(obj, 'PoissonRatio'):
        poisson = obj.PoissonRatio
        print(f"Poisson Ratio: {poisson}")
        properties['poisson'] = poisson
        
        # Check if it's steel Poisson ratio (wrong for concrete)
        if abs(poisson - 0.30) < 0.01:
            print("  ❌ PROBLEM: This is STEEL Poisson ratio, not concrete!")
    
    if hasattr(obj, 'MaterialStandard'):
        standard = obj.MaterialStandard
        print(f"Material Standard: {standard}")
        properties['standard'] = standard
    else:
        print("Material Standard: Not set (old Material system)")
        properties['standard'] = None
    
    if hasattr(obj, 'MaterialType'):
        mat_type = obj.MaterialType
        print(f"Material Type: {mat_type}")
        properties['type'] = mat_type
    
    return properties

def fix_concrete_properties(obj):
    """Fix the material object to have correct concrete properties."""
    print(f"\n🔧 Fixing {obj.Label} with correct concrete properties...")
    
    fixes_applied = 0
    
    # Correct concrete properties for ACI Normal 30 MPa
    correct_props = {
        'Density': "2400 kg/m^3",
        'ModulusElasticity': "27000 MPa", 
        'PoissonRatio': 0.20,
        'MaterialStandard': "ACI_Normal_30MPa"
    }
    
    # Fix Density
    if hasattr(obj, 'Density'):
        try:
            current_density = str(obj.Density)
            if current_density != correct_props['Density']:
                obj.Density = correct_props['Density']
                print(f"  ✅ Fixed Density: {current_density} → {correct_props['Density']}")
                fixes_applied += 1
            else:
                print(f"  ✓ Density already correct: {correct_props['Density']}")
        except Exception as e:
            print(f"  ❌ Error fixing Density: {e}")
    
    # Fix Modulus Elasticity
    if hasattr(obj, 'ModulusElasticity'):
        try:
            current_modulus = str(obj.ModulusElasticity)
            if current_modulus != correct_props['ModulusElasticity']:
                obj.ModulusElasticity = correct_props['ModulusElasticity']
                print(f"  ✅ Fixed Modulus: {current_modulus} → {correct_props['ModulusElasticity']}")
                fixes_applied += 1
            else:
                print(f"  ✓ Modulus already correct: {correct_props['ModulusElasticity']}")
        except Exception as e:
            print(f"  ❌ Error fixing Modulus: {e}")
    
    # Fix Poisson Ratio
    if hasattr(obj, 'PoissonRatio'):
        try:
            current_poisson = obj.PoissonRatio
            if abs(current_poisson - correct_props['PoissonRatio']) > 0.01:
                obj.PoissonRatio = correct_props['PoissonRatio']
                print(f"  ✅ Fixed Poisson: {current_poisson} → {correct_props['PoissonRatio']}")
                fixes_applied += 1
            else:
                print(f"  ✓ Poisson already correct: {correct_props['PoissonRatio']}")
        except Exception as e:
            print(f"  ❌ Error fixing Poisson: {e}")
    
    # Fix MaterialStandard (if exists)
    if hasattr(obj, 'MaterialStandard'):
        try:
            current_standard = obj.MaterialStandard
            if current_standard != correct_props['MaterialStandard']:
                obj.MaterialStandard = correct_props['MaterialStandard']
                print(f"  ✅ Fixed MaterialStandard: {current_standard} → {correct_props['MaterialStandard']}")
                fixes_applied += 1
            else:
                print(f"  ✓ MaterialStandard already correct: {correct_props['MaterialStandard']}")
        except Exception as e:
            print(f"  ❌ Error fixing MaterialStandard: {e}")
    else:
        print(f"  ℹ️  No MaterialStandard property (old Material system)")
    
    # Fix MaterialType (if exists)
    if hasattr(obj, 'MaterialType'):
        try:
            current_type = obj.MaterialType
            if current_type != "Concrete":
                obj.MaterialType = "Concrete"
                print(f"  ✅ Fixed MaterialType: {current_type} → Concrete")
                fixes_applied += 1
            else:
                print(f"  ✓ MaterialType already correct: Concrete")
        except Exception as e:
            print(f"  ❌ Error fixing MaterialType: {e}")
    
    return fixes_applied

def force_property_update(obj):
    """Force update of the object to refresh property panel."""
    print(f"\n🔄 Forcing property update for {obj.Label}...")
    
    try:
        # First force a MaterialStandard change to trigger onChanged
        if hasattr(obj, 'MaterialStandard'):
            current_standard = obj.MaterialStandard
            
            # Force onChanged event by temporarily changing MaterialStandard
            print(f"  🔄 Current MaterialStandard: {current_standard}")
            
            # Temporarily set to empty to clear cache, then back to original
            obj.MaterialStandard = ""
            print("  🔄 Temporarily cleared MaterialStandard")
            
            # Set back to original to trigger _update_standard_properties
            obj.MaterialStandard = current_standard
            print(f"  ✅ MaterialStandard restored: {current_standard}")
            
            # This should trigger the onChanged event and _update_standard_properties method
        
        # Force object recompute
        obj.recompute()
        print("  ✅ Object recomputed")
        
        # Force document recompute  
        App.ActiveDocument.recompute()
        print("  ✅ Document recomputed")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error during property update: {e}")
        return False

def verify_fix_success(obj):
    """Verify that the fix was successful."""
    print(f"\n✅ VERIFICATION - Properties after fix:")
    print("="*50)
    
    all_correct = True
    
    # Check Density
    if hasattr(obj, 'Density'):
        density_str = str(obj.Density)
        if '2400' in density_str and 'kg/m' in density_str:
            print(f"✅ Density: {density_str} (CORRECT)")
        else:
            print(f"❌ Density: {density_str} (STILL WRONG)")
            all_correct = False
    
    # Check Modulus
    if hasattr(obj, 'ModulusElasticity'):
        modulus_str = str(obj.ModulusElasticity)
        if '27000' in modulus_str or '27.0' in modulus_str:
            print(f"✅ Modulus: {modulus_str} (CORRECT)")
        else:
            print(f"❌ Modulus: {modulus_str} (STILL WRONG)")
            all_correct = False
    
    # Check Poisson
    if hasattr(obj, 'PoissonRatio'):
        poisson = obj.PoissonRatio
        if abs(poisson - 0.20) < 0.01:
            print(f"✅ Poisson: {poisson} (CORRECT)")
        else:
            print(f"❌ Poisson: {poisson} (STILL WRONG)")
            all_correct = False
    
    return all_correct

def run_specific_material_fix():
    """Run the complete fix process for the specific material."""
    print("SPECIFIC MATERIAL OBJECT FIX")
    print("="*80)
    print("Target: Material_ACI_Normal_30MPa001 (or similar)")
    print("Issue: Showing steel properties instead of concrete properties")
    print()
    
    # Find the problematic material
    material_obj = find_problematic_material()
    if not material_obj:
        return
    
    # Analyze current properties
    properties = analyze_material_properties(material_obj)
    
    # Check if fix is needed
    needs_fix = False
    if 'density' in properties and '7850' in properties['density']:
        needs_fix = True
    if 'modulus' in properties and ('200000' in properties['modulus'] or '200.00 GPa' in properties['modulus']):
        needs_fix = True
    if 'poisson' in properties and abs(properties['poisson'] - 0.30) < 0.01:
        needs_fix = True
    
    if not needs_fix:
        print("\n✅ Material properties are already correct!")
        return
    
    # Confirm fix
    print(f"\n⚠️  Material {material_obj.Label} needs to be fixed!")
    print("It currently shows STEEL properties but should show CONCRETE properties.")
    response = input("Apply concrete properties fix? (y/N): ").lower().strip()
    
    if response not in ['y', 'yes']:
        print("❌ Fix cancelled by user")
        return
    
    # Apply fix
    fixes_applied = fix_concrete_properties(material_obj)
    
    if fixes_applied > 0:
        # Force property update
        force_property_update(material_obj)
        
        # Verify success
        success = verify_fix_success(material_obj)
        
        print(f"\n{'='*80}")
        print("FIX SUMMARY")
        print(f"{'='*80}")
        print(f"Material: {material_obj.Label}")
        print(f"Fixes applied: {fixes_applied}")
        print(f"Fix successful: {'✅ YES' if success else '❌ NO'}")
        
        if success:
            print("\n🎉 SUCCESS!")
            print("The Material Data property panel should now show:")
            print("  - Density: 2400 kg/m³")
            print("  - Modulus Elasticity: 27000 MPa (27 GPa)")  
            print("  - Poisson Ratio: 0.20")
            print()
            print("Please check the FreeCAD Property Panel to confirm the fix.")
        else:
            print("\n⚠️  Some issues may remain.")
            print("Try selecting the object and pressing Ctrl+Shift+R to force refresh.")
    else:
        print("\n✅ No fixes were needed - properties are already correct!")

if __name__ == "__main__":
    run_specific_material_fix()