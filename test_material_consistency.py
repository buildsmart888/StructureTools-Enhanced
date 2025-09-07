#!/usr/bin/env python3
"""
Test Material Consistency

This script tests the consistency of the material.py file system:
1. onChanged method triggers correctly
2. _update_standard_properties works as expected
3. MaterialStandards data is accessible
4. Property updates are consistent

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_material_consistency.py').read())
"""

import FreeCAD as App

def test_material_system_consistency():
    """Test the entire material system for consistency."""
    print("MATERIAL SYSTEM CONSISTENCY TEST")
    print("=" * 60)
    
    # Ensure document exists
    if not App.ActiveDocument:
        App.newDocument("ConsistencyTest")
        print("[OK] Created test document")
    
    # Step 1: Test MaterialStandards import
    print("\n1. Testing MaterialStandards import...")
    try:
        # Try direct import first
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
        print(f"[OK] MaterialStandards direct import: {len(MATERIAL_STANDARDS)} standards")
        
        if "ACI_Normal_30MPa" in MATERIAL_STANDARDS:
            concrete_props = MATERIAL_STANDARDS["ACI_Normal_30MPa"]
            print(f"[OK] ACI_Normal_30MPa data: {concrete_props}")
        else:
            print("[ERROR] ACI_Normal_30MPa not found in direct import")
            return False
            
    except Exception as e:
        print(f"[ERROR] MaterialStandards direct import failed: {e}")
        return False
    
    # Step 2: Test Material class import
    print("\n2. Testing Material class import...")
    try:
        from freecad.StructureTools.material import Material
        print("[OK] Material class imported successfully")
    except Exception as e:
        print(f"[ERROR] Material class import failed: {e}")
        return False
    
    # Step 3: Create material object and test initial state
    print("\n3. Creating material object...")
    try:
        mat_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "ConsistencyTest")
        Material(mat_obj)
        
        print("[OK] Material object created")
        print(f"   Initial Density: {mat_obj.Density}")
        print(f"   Initial Modulus: {mat_obj.ModulusElasticity}")
        print(f"   Initial Poisson: {mat_obj.PoissonRatio}")
        print(f"   Available standards: {len(mat_obj.MaterialStandard)} items")
        
    except Exception as e:
        print(f"[ERROR] Material object creation failed: {e}")
        return False
    
    # Step 4: Test MaterialStandards availability in object
    print("\n4. Testing MaterialStandards in object...")
    if "ACI_Normal_30MPa" in mat_obj.MaterialStandard:
        print("[OK] ACI_Normal_30MPa available in object dropdown")
    else:
        print("[ERROR] ACI_Normal_30MPa NOT available in object dropdown")
        available_concrete = [s for s in mat_obj.MaterialStandard if 'ACI' in s]
        print(f"   Available ACI standards: {available_concrete}")
        return False
    
    # Step 5: Test onChanged mechanism
    print("\n5. Testing onChanged mechanism...")
    try:
        print("   Setting MaterialStandard to ACI_Normal_30MPa...")
        
        # This should trigger onChanged -> _update_standard_properties
        mat_obj.MaterialStandard = "ACI_Normal_30MPa"
        
        print("   After setting MaterialStandard:")
        print(f"     Density: {mat_obj.Density}")
        print(f"     Modulus: {mat_obj.ModulusElasticity}")
        print(f"     Poisson: {mat_obj.PoissonRatio}")
        
    except Exception as e:
        print(f"[ERROR] onChanged mechanism failed: {e}")
        return False
    
    # Step 6: Verify correct concrete values
    print("\n6. Verifying concrete values...")
    density_str = str(mat_obj.Density)
    modulus_str = str(mat_obj.ModulusElasticity)
    poisson = mat_obj.PoissonRatio
    
    concrete_correct = True
    
    if "2400" not in density_str:
        print(f"[ERROR] Density wrong: {density_str} (expected 2400 kg/m³)")
        concrete_correct = False
    else:
        print(f"[OK] Density correct: {density_str}")
    
    if "27000" not in modulus_str:
        print(f"[ERROR] Modulus wrong: {modulus_str} (expected 27000 MPa)")
        concrete_correct = False
    else:
        print(f"[OK] Modulus correct: {modulus_str}")
    
    if abs(poisson - 0.20) > 0.01:
        print(f"[ERROR] Poisson wrong: {poisson} (expected 0.20)")
        concrete_correct = False
    else:
        print(f"[OK] Poisson correct: {poisson}")
    
    # Step 7: Test switching to steel
    print("\n7. Testing switch to steel standard...")
    try:
        mat_obj.MaterialStandard = "ASTM_A992"
        
        print("   After switching to ASTM_A992:")
        print(f"     Density: {mat_obj.Density}")
        print(f"     Modulus: {mat_obj.ModulusElasticity}")
        print(f"     Poisson: {mat_obj.PoissonRatio}")
        
        # Check if steel values are correct
        density_str = str(mat_obj.Density)
        modulus_str = str(mat_obj.ModulusElasticity)
        poisson = mat_obj.PoissonRatio
        
        steel_correct = True
        if "7850" not in density_str:
            print(f"[ERROR] Steel density wrong: {density_str}")
            steel_correct = False
        else:
            print(f"[OK] Steel density correct: {density_str}")
        
        if "200000" not in modulus_str:
            print(f"[ERROR] Steel modulus wrong: {modulus_str}")
            steel_correct = False
        else:
            print(f"[OK] Steel modulus correct: {modulus_str}")
        
    except Exception as e:
        print(f"[ERROR] Steel switching failed: {e}")
        steel_correct = False
    
    # Step 8: Switch back to concrete to test consistency
    print("\n8. Testing switch back to concrete...")
    try:
        mat_obj.MaterialStandard = "ACI_Normal_30MPa"
        
        print("   After switching back to ACI_Normal_30MPa:")
        print(f"     Density: {mat_obj.Density}")
        print(f"     Modulus: {mat_obj.ModulusElasticity}")
        print(f"     Poisson: {mat_obj.PoissonRatio}")
        
    except Exception as e:
        print(f"[ERROR] Switch back failed: {e}")
        return False
    
    # Final results
    print("\n" + "=" * 60)
    print("CONSISTENCY TEST RESULTS")
    print("=" * 60)
    
    if concrete_correct and steel_correct:
        print("[SUCCESS] Material system is CONSISTENT and WORKING!")
        print("  - MaterialStandards import: OK")
        print("  - Material object creation: OK")
        print("  - onChanged mechanism: OK")
        print("  - Property updates: OK")
        print("  - Value switching: OK")
        return True
    else:
        print("[ERROR] Material system has CONSISTENCY ISSUES")
        if not concrete_correct:
            print("  - Concrete values: WRONG")
        if not steel_correct:
            print("  - Steel values: WRONG")
        return False

def test_existing_material_object():
    """Test existing Material_ACI_Normal_30MPa001 object."""
    print("\n" + "=" * 60)
    print("TESTING EXISTING MATERIAL OBJECT")
    print("=" * 60)
    
    if not App.ActiveDocument:
        print("[ERROR] No active document for existing object test")
        return
    
    # Find existing object
    target_obj = None
    for obj in App.ActiveDocument.Objects:
        if (hasattr(obj, 'MaterialStandard') and hasattr(obj, 'Density') and
            ('ACI_Normal_30MP' in obj.Label or 'ACI_Normal_30MP' in obj.Name)):
            target_obj = obj
            break
    
    if target_obj:
        print(f"[OK] Found existing object: {target_obj.Label}")
        print(f"   Current MaterialStandard: {getattr(target_obj, 'MaterialStandard', 'None')}")
        print(f"   Current Density: {target_obj.Density}")
        print(f"   Current Modulus: {target_obj.ModulusElasticity}")
        print(f"   Current Poisson: {target_obj.PoissonRatio}")
        
        # Try to trigger update
        print("\n[TEST] Triggering MaterialStandard update...")
        try:
            target_obj.MaterialStandard = "ACI_Normal_30MPa"
            print(f"   After update Density: {target_obj.Density}")
            print(f"   After update Modulus: {target_obj.ModulusElasticity}")
            print(f"   After update Poisson: {target_obj.PoissonRatio}")
        except Exception as e:
            print(f"[ERROR] Update failed: {e}")
    else:
        print("[INFO] No existing Material_ACI_Normal_30MPa001 object found")

def run_full_consistency_test():
    """Run complete consistency test."""
    success = test_material_system_consistency()
    test_existing_material_object()
    
    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    
    if success:
        print("[SUCCESS] Material system is working correctly!")
        print("Your Material_ACI_Normal_30MPa001 should work as expected.")
        print("\nTo use:")
        print("1. Select material object in FreeCAD")
        print("2. Go to Property Panel")
        print("3. Change MaterialStandard dropdown")
        print("4. Values will update automatically!")
    else:
        print("[ERROR] Material system needs debugging")
        print("Check error messages above for specific issues")

if __name__ == "__main__":
    run_full_consistency_test()