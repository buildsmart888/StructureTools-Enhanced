#!/usr/bin/env python3
"""
Material Properties Fix Script

This script fixes incorrect material properties in existing FreeCAD documents.
Specifically addresses the issue where ACI_Normal_30MPa concrete materials 
show steel properties instead of concrete properties.

Usage:
1. Open your FreeCAD document with the problematic materials
2. Run this script in the FreeCAD Python console:
   exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\fix_material_properties.py').read())
"""

import FreeCAD as App

def fix_concrete_material_properties():
    """Fix concrete materials that have incorrect properties."""
    
    print("="*80)
    print("MATERIAL PROPERTIES FIX SCRIPT")
    print("="*80)
    
    if not App.ActiveDocument:
        print("❌ No active document. Please open a document first.")
        return False
    
    # Find all material objects
    materials = []
    for obj in App.ActiveDocument.Objects:
        if hasattr(obj, 'Density') and hasattr(obj, 'ModulusElasticity'):
            materials.append(obj)
    
    if not materials:
        print("❌ No material objects found in the document")
        return False
    
    print(f"✅ Found {len(materials)} material objects")
    
    # Load material standards database
    try:
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
        print("✅ Material standards database loaded")
    except ImportError:
        print("❌ Cannot load material standards database")
        return False
    
    # Process each material
    fixed_materials = []
    problematic_materials = []
    
    for material in materials:
        print(f"\n🔍 Checking material: {material.Label}")
        
        # Check if this is an ACI concrete material with wrong properties
        is_problematic = False
        
        # Check for concrete material with steel properties
        if hasattr(material, 'Density'):
            density_str = str(material.Density)
            if "7850" in density_str:  # Steel density
                # Check if this should be concrete
                if ("ACI" in material.Label and ("30MP" in material.Label or "25MP" in material.Label)):
                    is_problematic = True
                    print(f"  ❌ Found concrete material with steel density: {density_str}")
                elif hasattr(material, 'MaterialStandard') and "ACI_Normal" in str(material.MaterialStandard):
                    is_problematic = True
                    print(f"  ❌ Found ACI concrete with steel density: {density_str}")
        
        if hasattr(material, 'ModulusElasticity'):
            modulus_str = str(material.ModulusElasticity)
            if "200000" in modulus_str or "200.00 GPa" in modulus_str:  # Steel modulus
                if ("ACI" in material.Label and ("30MP" in material.Label or "25MP" in material.Label)):
                    is_problematic = True
                    print(f"  ❌ Found concrete material with steel modulus: {modulus_str}")
                elif hasattr(material, 'MaterialStandard') and "ACI_Normal" in str(material.MaterialStandard):
                    is_problematic = True
                    print(f"  ❌ Found ACI concrete with steel modulus: {modulus_str}")
        
        if is_problematic:
            problematic_materials.append(material)
        
        # Try to determine correct standard and fix
        if is_problematic:
            # Determine which concrete standard to apply
            standard_to_apply = None
            
            if "30MP" in material.Label or (hasattr(material, 'MaterialStandard') and "30MP" in str(material.MaterialStandard)):
                standard_to_apply = "ACI_Normal_30MPa"
            elif "25MP" in material.Label or (hasattr(material, 'MaterialStandard') and "25MP" in str(material.MaterialStandard)):
                standard_to_apply = "ACI_Normal_25MPa"
            
            if standard_to_apply and standard_to_apply in MATERIAL_STANDARDS:
                print(f"  🔧 Applying standard: {standard_to_apply}")
                
                # Get correct properties from database
                correct_props = MATERIAL_STANDARDS[standard_to_apply]
                
                # Apply correct properties
                properties_fixed = 0
                
                for prop_name, correct_value in correct_props.items():
                    if hasattr(material, prop_name):
                        try:
                            current_value = getattr(material, prop_name)
                            if str(current_value) != str(correct_value):
                                setattr(material, prop_name, correct_value)
                                print(f"    ✅ Fixed {prop_name}: {current_value} → {correct_value}")
                                properties_fixed += 1
                        except Exception as e:
                            print(f"    ❌ Error fixing {prop_name}: {e}")
                
                # Update MaterialStandard if property exists
                if hasattr(material, 'MaterialStandard'):
                    if str(material.MaterialStandard) != standard_to_apply:
                        material.MaterialStandard = standard_to_apply
                        print(f"    ✅ Updated MaterialStandard to: {standard_to_apply}")
                        properties_fixed += 1
                
                if properties_fixed > 0:
                    fixed_materials.append((material, properties_fixed))
                    print(f"    ✅ Fixed {properties_fixed} properties")
                else:
                    print(f"    ℹ️ No fixes needed")
    
    # Summary and recompute
    if fixed_materials:
        print(f"\n{'='*80}")
        print("FIX SUMMARY")
        print(f"{'='*80}")
        print(f"Total materials checked: {len(materials)}")
        print(f"Problematic materials found: {len(problematic_materials)}")
        print(f"Materials fixed: {len(fixed_materials)}")
        
        for material, fix_count in fixed_materials:
            print(f"  - {material.Label}: {fix_count} properties fixed")
        
        # Recompute document
        try:
            App.ActiveDocument.recompute()
            print(f"\n✅ Document recomputed successfully")
        except Exception as e:
            print(f"\n❌ Error recomputing document: {e}")
        
        return True
    else:
        print(f"\n✅ No problematic materials found - all materials have correct properties")
        return True

def verify_concrete_properties():
    """Verify that concrete materials have correct properties."""
    print(f"\n{'='*60}")
    print("VERIFICATION: CONCRETE MATERIAL PROPERTIES")
    print(f"{'='*60}")
    
    if not App.ActiveDocument:
        return
    
    # Expected concrete properties
    expected_concrete_props = {
        "ACI_Normal_25MPa": {
            "Density": "2400 kg/m^3",
            "ModulusElasticity": "25000 MPa",
            "PoissonRatio": 0.20
        },
        "ACI_Normal_30MPa": {
            "Density": "2400 kg/m^3", 
            "ModulusElasticity": "27000 MPa",
            "PoissonRatio": 0.20
        }
    }
    
    # Find concrete materials
    for obj in App.ActiveDocument.Objects:
        if hasattr(obj, 'Density') and hasattr(obj, 'ModulusElasticity'):
            # Check if this looks like a concrete material
            is_concrete = False
            expected_standard = None
            
            if hasattr(obj, 'MaterialStandard'):
                std = str(obj.MaterialStandard)
                if "ACI_Normal" in std:
                    is_concrete = True
                    expected_standard = std
            elif "ACI" in obj.Label and ("25MP" in obj.Label or "30MP" in obj.Label):
                is_concrete = True
                if "30MP" in obj.Label:
                    expected_standard = "ACI_Normal_30MPa"
                elif "25MP" in obj.Label:
                    expected_standard = "ACI_Normal_25MPa"
            
            if is_concrete and expected_standard in expected_concrete_props:
                print(f"\n📋 Verifying: {obj.Label}")
                print(f"   Expected standard: {expected_standard}")
                
                expected = expected_concrete_props[expected_standard]
                all_correct = True
                
                # Check density
                if hasattr(obj, 'Density'):
                    current_density = str(obj.Density)
                    expected_density = expected["Density"]
                    if current_density == expected_density:
                        print(f"   ✅ Density: {current_density}")
                    else:
                        print(f"   ❌ Density: {current_density} (expected: {expected_density})")
                        all_correct = False
                
                # Check modulus
                if hasattr(obj, 'ModulusElasticity'):
                    current_E = str(obj.ModulusElasticity)
                    expected_E = expected["ModulusElasticity"]
                    if current_E == expected_E:
                        print(f"   ✅ Modulus: {current_E}")
                    else:
                        print(f"   ❌ Modulus: {current_E} (expected: {expected_E})")
                        all_correct = False
                
                # Check Poisson ratio
                if hasattr(obj, 'PoissonRatio'):
                    current_nu = obj.PoissonRatio
                    expected_nu = expected["PoissonRatio"]
                    if abs(current_nu - expected_nu) < 0.01:
                        print(f"   ✅ Poisson Ratio: {current_nu}")
                    else:
                        print(f"   ❌ Poisson Ratio: {current_nu} (expected: {expected_nu})")
                        all_correct = False
                
                if all_correct:
                    print(f"   ✅ All properties correct!")
                else:
                    print(f"   ❌ Some properties need fixing")

if __name__ == "__main__":
    # Run the fix
    success = fix_concrete_material_properties()
    
    # Verify the results
    verify_concrete_properties()
    
    print(f"\n{'='*80}")
    print("MATERIAL FIX COMPLETE")
    print(f"{'='*80}")
    
    if success:
        print("✅ Material properties have been checked and fixed if necessary")
        print("ℹ️  Your concrete materials should now show correct properties:")
        print("   - Density: 2400 kg/m³ (not 7850 kg/m³)")
        print("   - Modulus: 25000-27000 MPa (not 200000 MPa)")
        print("   - Poisson Ratio: 0.20 (not 0.30)")
    else:
        print("❌ Some issues occurred during the fix process")
        print("ℹ️  Please check the output above for details")
    
    print("\n📝 To prevent this issue in the future:")
    print("   1. Always use the MaterialHelper.create_concrete_30mpa() function")
    print("   2. Or ensure MaterialStandard is set correctly before setting other properties")
    print("   3. Verify properties after creating materials")