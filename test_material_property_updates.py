#!/usr/bin/env python3
"""
Test Material Property Updates

This script tests that material properties are correctly updated when
MaterialStandard is selected, particularly for concrete materials.

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_material_property_updates.py').read())
"""

import FreeCAD as App

def test_create_material_and_set_standard():
    """Test creating a material and setting different standards."""
    print("=" * 80)
    print("MATERIAL PROPERTY UPDATE TEST")
    print("=" * 80)
    
    if not App.ActiveDocument:
        print("❌ No active document. Creating one...")
        App.newDocument("MaterialTest")
    
    # Test 1: Create material and set concrete standard
    print("\n🧪 TEST 1: Create material with ACI_Normal_30MPa standard")
    
    try:
        # Create material object  
        mat_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "TestConcrete")
        
        # Import material class
        from freecad.StructureTools.material import Material
        Material(mat_obj)
        
        print("✅ Material object created")
        
        # Check initial minimal values
        print(f"   Initial Density: {mat_obj.Density}")
        print(f"   Initial Modulus: {mat_obj.ModulusElasticity}")  
        print(f"   Initial Poisson: {mat_obj.PoissonRatio}")
        
        # Set to concrete standard
        print("\n🔧 Setting MaterialStandard to ACI_Normal_30MPa...")
        mat_obj.MaterialStandard = "ACI_Normal_30MPa"
        
        # Force recompute
        mat_obj.recompute()
        App.ActiveDocument.recompute()
        
        print(f"   After update Density: {mat_obj.Density}")
        print(f"   After update Modulus: {mat_obj.ModulusElasticity}")
        print(f"   After update Poisson: {mat_obj.PoissonRatio}")
        
        # Check if values are concrete
        density_str = str(mat_obj.Density)
        modulus_str = str(mat_obj.ModulusElasticity)
        poisson = mat_obj.PoissonRatio
        
        if "2400" in density_str:
            print("   ✅ Density correct (2400 kg/m³)")
        else:
            print(f"   ❌ Density wrong: {density_str} (expected 2400)")
        
        if "27000" in modulus_str:
            print("   ✅ Modulus correct (27000 MPa)")
        else:
            print(f"   ❌ Modulus wrong: {modulus_str} (expected 27000)")
            
        if abs(poisson - 0.20) < 0.01:
            print("   ✅ Poisson correct (0.20)")
        else:
            print(f"   ❌ Poisson wrong: {poisson} (expected 0.20)")
        
        return mat_obj
        
    except Exception as e:
        print(f"❌ Error in test: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_debug_material_standards_import():
    """Debug MaterialStandards import and availability."""
    print("\n🔍 DEBUG: Material Standards Import")
    print("-" * 50)
    
    try:
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
        print(f"✅ MATERIAL_STANDARDS imported successfully")
        print(f"   Available standards: {len(MATERIAL_STANDARDS)}")
        
        if "ACI_Normal_30MPa" in MATERIAL_STANDARDS:
            print("✅ ACI_Normal_30MPa found in database")
            props = MATERIAL_STANDARDS["ACI_Normal_30MPa"]
            print(f"   Properties: {props}")
        else:
            print("❌ ACI_Normal_30MPa NOT found in database")
            print(f"   Available concrete standards: {[k for k in MATERIAL_STANDARDS.keys() if 'ACI' in k or 'concrete' in k.lower()]}")
            
    except Exception as e:
        print(f"❌ Error importing MATERIAL_STANDARDS: {e}")
        import traceback
        traceback.print_exc()

def test_manual_property_update():
    """Test manual property update using _update_standard_properties."""
    print("\n🔧 TEST 2: Manual property update")
    print("-" * 50)
    
    # Find existing material objects
    material_objects = []
    for obj in App.ActiveDocument.Objects:
        if hasattr(obj, 'MaterialStandard') and hasattr(obj, 'Density'):
            material_objects.append(obj)
    
    if not material_objects:
        print("❌ No material objects found for manual update test")
        return
    
    for obj in material_objects:
        print(f"\n📊 Testing manual update for: {obj.Label}")
        
        # Get material proxy
        if hasattr(obj, 'Proxy'):
            try:
                # Call _update_standard_properties directly
                obj.Proxy._update_standard_properties(obj)
                print("   ✅ _update_standard_properties called")
                
                # Check results
                print(f"   Result Density: {obj.Density}")
                print(f"   Result Modulus: {obj.ModulusElasticity}")
                print(f"   Result Poisson: {obj.PoissonRatio}")
                
            except Exception as e:
                print(f"   ❌ Error in manual update: {e}")
        else:
            print("   ❌ No Proxy found")

def run_comprehensive_material_test():
    """Run comprehensive material property update test."""
    print("COMPREHENSIVE MATERIAL PROPERTY TEST")
    print("=" * 80)
    
    # Debug import first
    test_debug_material_standards_import()
    
    # Test creating new material
    mat_obj = test_create_material_and_set_standard()
    
    # Test manual update
    test_manual_property_update()
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    if mat_obj:
        print("✅ Material creation test completed")
        
        # Final verification
        density_str = str(mat_obj.Density)
        modulus_str = str(mat_obj.ModulusElasticity)
        
        if "2400" in density_str and "27000" in modulus_str:
            print("🎉 SUCCESS: Material properties updated correctly!")
            print("   Concrete material shows proper values")
        else:
            print("⚠️  WARNING: Material properties may not be updated correctly")
            print(f"   Density: {density_str}")
            print(f"   Modulus: {modulus_str}")
    else:
        print("❌ Material creation test failed")
    
    print("\n💡 If properties are still showing incorrect values:")
    print("   1. Check that MaterialStandards.py contains ACI_Normal_30MPa")
    print("   2. Verify _update_standard_properties method is working")  
    print("   3. Try manually setting MaterialStandard in property panel")

if __name__ == "__main__":
    run_comprehensive_material_test()