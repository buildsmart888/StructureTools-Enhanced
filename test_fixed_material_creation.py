#!/usr/bin/env python3
"""
Test Fixed Material Creation

Test the fixed material.py with intelligent defaults and auto-update.

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_fixed_material_creation.py').read())
"""

import FreeCAD as App

def test_new_material_creation():
    """Test creating new material objects with fixed system."""
    print("TESTING FIXED MATERIAL CREATION")
    print("=" * 60)
    
    # Ensure document exists
    if not App.ActiveDocument:
        App.newDocument("FixedMaterialTest")
        print("[OK] Created test document")
    
    # Test 1: Create concrete material with intelligent naming
    print("\n1. Creating concrete material with ACI name...")
    try:
        # Create object with concrete-indicating name
        concrete_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Material_ACI_Normal_30MPa_Test")
        
        # Apply Material class
        from freecad.StructureTools.material import Material
        Material(concrete_obj)
        
        print(f"[OK] Concrete material created: {concrete_obj.Label}")
        print(f"   Auto-selected standard: {concrete_obj.MaterialStandard}")
        print(f"   Properties after creation:")
        print(f"     Density: {concrete_obj.Density}")
        print(f"     Modulus: {concrete_obj.ModulusElasticity}")
        print(f"     Poisson: {concrete_obj.PoissonRatio}")
        
        # Check if values are concrete
        density_str = str(concrete_obj.Density)
        modulus_str = str(concrete_obj.ModulusElasticity)
        poisson = concrete_obj.PoissonRatio
        
        concrete_success = True
        if "2400" not in density_str:
            print(f"   [ERROR] Density wrong: {density_str} (expected 2400)")
            concrete_success = False
        else:
            print(f"   [OK] Density correct: {density_str}")
            
        if "27000" not in modulus_str:
            print(f"   [ERROR] Modulus wrong: {modulus_str} (expected 27000)")
            concrete_success = False
        else:
            print(f"   [OK] Modulus correct: {modulus_str}")
            
        if abs(poisson - 0.20) > 0.01:
            print(f"   [ERROR] Poisson wrong: {poisson} (expected 0.20)")
            concrete_success = False
        else:
            print(f"   [OK] Poisson correct: {poisson}")
        
    except Exception as e:
        print(f"[ERROR] Concrete material creation failed: {e}")
        concrete_success = False
    
    # Test 2: Create steel material with intelligent naming
    print("\n2. Creating steel material with ASTM name...")
    try:
        # Create object with steel-indicating name
        steel_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Material_ASTM_A992_Test")
        
        # Apply Material class
        Material(steel_obj)
        
        print(f"[OK] Steel material created: {steel_obj.Label}")
        print(f"   Auto-selected standard: {steel_obj.MaterialStandard}")
        print(f"   Properties after creation:")
        print(f"     Density: {steel_obj.Density}")
        print(f"     Modulus: {steel_obj.ModulusElasticity}")
        print(f"     Poisson: {steel_obj.PoissonRatio}")
        
        # Check if values are steel
        density_str = str(steel_obj.Density)
        modulus_str = str(steel_obj.ModulusElasticity)
        poisson = steel_obj.PoissonRatio
        
        steel_success = True
        if "7850" not in density_str:
            print(f"   [ERROR] Steel density wrong: {density_str} (expected 7850)")
            steel_success = False
        else:
            print(f"   [OK] Steel density correct: {density_str}")
            
        if "200000" not in modulus_str:
            print(f"   [ERROR] Steel modulus wrong: {modulus_str} (expected 200000)")
            steel_success = False
        else:
            print(f"   [OK] Steel modulus correct: {modulus_str}")
            
        if abs(poisson - 0.30) > 0.01:
            print(f"   [ERROR] Steel Poisson wrong: {poisson} (expected 0.30)")
            steel_success = False
        else:
            print(f"   [OK] Steel Poisson correct: {poisson}")
        
    except Exception as e:
        print(f"[ERROR] Steel material creation failed: {e}")
        steel_success = False
    
    # Test 3: Create generic material (should default to concrete)
    print("\n3. Creating generic material (should default to concrete)...")
    try:
        # Create object with generic name
        generic_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Material_Generic_Test")
        
        # Apply Material class
        Material(generic_obj)
        
        print(f"[OK] Generic material created: {generic_obj.Label}")
        print(f"   Auto-selected standard: {generic_obj.MaterialStandard}")
        print(f"   Properties after creation:")
        print(f"     Density: {generic_obj.Density}")
        print(f"     Modulus: {generic_obj.ModulusElasticity}")
        print(f"     Poisson: {generic_obj.PoissonRatio}")
        
        # Should default to concrete
        generic_success = (generic_obj.MaterialStandard == "ACI_Normal_30MPa")
        if generic_success:
            print(f"   [OK] Generic object correctly defaulted to concrete")
        else:
            print(f"   [ERROR] Generic object wrong default: {generic_obj.MaterialStandard}")
        
    except Exception as e:
        print(f"[ERROR] Generic material creation failed: {e}")
        generic_success = False
    
    # Test 4: Test manual MaterialStandard switching
    print("\n4. Testing manual MaterialStandard switching...")
    if 'concrete_obj' in locals():
        try:
            print("   Switching concrete object to steel standard...")
            concrete_obj.MaterialStandard = "ASTM_A992"
            
            print(f"   After switching to steel:")
            print(f"     Density: {concrete_obj.Density}")
            print(f"     Modulus: {concrete_obj.ModulusElasticity}")
            print(f"     Poisson: {concrete_obj.PoissonRatio}")
            
            # Check if it switched to steel values
            switching_success = ("7850" in str(concrete_obj.Density))
            if switching_success:
                print(f"   [OK] Manual switching works!")
            else:
                print(f"   [ERROR] Manual switching failed")
            
        except Exception as e:
            print(f"[ERROR] Manual switching failed: {e}")
            switching_success = False
    else:
        switching_success = False
    
    # Results summary
    print("\n" + "=" * 60)
    print("FIXED MATERIAL CREATION TEST RESULTS")
    print("=" * 60)
    
    all_success = concrete_success and steel_success and generic_success and switching_success
    
    if all_success:
        print("[SUCCESS] ALL TESTS PASSED!")
        print("  - Concrete creation with correct values: OK")
        print("  - Steel creation with correct values: OK")
        print("  - Generic default to concrete: OK")
        print("  - Manual MaterialStandard switching: OK")
        print("\nYour fixed material system is working!")
    else:
        print("[ERROR] Some tests failed:")
        if not concrete_success:
            print("  - Concrete creation: FAILED")
        if not steel_success:
            print("  - Steel creation: FAILED")
        if not generic_success:
            print("  - Generic default: FAILED")
        if not switching_success:
            print("  - Manual switching: FAILED")
    
    return all_success

def test_existing_object_fix():
    """Test fixing existing problematic objects."""
    print("\n" + "=" * 60)
    print("TESTING EXISTING OBJECT FIX")
    print("=" * 60)
    
    if not App.ActiveDocument:
        print("[INFO] No document to test existing objects")
        return
    
    # Look for existing problematic objects
    problematic_objects = []
    for obj in App.ActiveDocument.Objects:
        if (hasattr(obj, 'Density') and hasattr(obj, 'MaterialStandard') and
            ('ACI_Normal_30MP' in obj.Label or 'Material' in obj.Label)):
            
            density_str = str(obj.Density)
            if "1" in density_str and "kg/m^3" in density_str:  # Wrong value
                problematic_objects.append(obj)
    
    if problematic_objects:
        print(f"[OK] Found {len(problematic_objects)} problematic objects")
        
        for obj in problematic_objects:
            print(f"\n  Fixing: {obj.Label}")
            try:
                # Re-apply Material class with fixes
                from freecad.StructureTools.material import Material
                Material(obj)
                
                print(f"    After fix:")
                print(f"      Density: {obj.Density}")
                print(f"      Modulus: {obj.ModulusElasticity}")
                print(f"      Poisson: {obj.PoissonRatio}")
                
            except Exception as e:
                print(f"    [ERROR] Fix failed: {e}")
    else:
        print("[INFO] No problematic objects found")

def run_complete_fixed_material_test():
    """Run complete test of fixed material system."""
    success = test_new_material_creation()
    test_existing_object_fix()
    
    print("\n" + "=" * 80)
    print("COMPLETE TEST SUMMARY")
    print("=" * 80)
    
    if success:
        print("[SUCCESS] Fixed material system is working correctly!")
        print("\nHow to create materials now:")
        print("1. Create Material object (will auto-detect type from name)")
        print("2. Properties are automatically set based on intelligent defaults")
        print("3. You can manually change MaterialStandard dropdown anytime")
        print("4. Properties will update automatically!")
    else:
        print("[ERROR] Fixed material system still needs work")
        print("Check error messages above for debugging")

if __name__ == "__main__":
    run_complete_fixed_material_test()