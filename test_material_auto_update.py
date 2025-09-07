#!/usr/bin/env python3
"""
Test Material Auto-Update

Simple test to verify that material properties automatically update 
when MaterialStandard is selected.

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_material_auto_update.py').read())
"""

import FreeCAD as App

def test_material_auto_update():
    """Test that material properties auto-update when MaterialStandard is selected."""
    print("🧪 TESTING MATERIAL AUTO-UPDATE")
    print("=" * 60)
    
    # Create document if needed
    if not App.ActiveDocument:
        App.newDocument("MaterialAutoTest")
        print("✅ Created new document")
    
    print("\n🔧 Step 1: Creating new material object...")
    
    try:
        # Create material object
        mat_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "TestAutoUpdate")
        
        # Apply Material class
        from freecad.StructureTools.material import Material
        Material(mat_obj)
        
        print("✅ Material object created")
        print(f"   Initial Density: {mat_obj.Density}")
        print(f"   Initial Modulus: {mat_obj.ModulusElasticity}")
        print(f"   Initial Poisson: {mat_obj.PoissonRatio}")
        print(f"   Available MaterialStandards: {mat_obj.MaterialStandard}")
        
        print("\n🔧 Step 2: Testing Concrete (ACI_Normal_30MPa)...")
        
        # Set to concrete - this should trigger onChanged -> _update_standard_properties
        print("   Setting MaterialStandard = 'ACI_Normal_30MPa'")
        mat_obj.MaterialStandard = "ACI_Normal_30MPa"
        
        print("   Properties after setting concrete:")
        print(f"   Density: {mat_obj.Density}")
        print(f"   Modulus: {mat_obj.ModulusElasticity}")
        print(f"   Poisson: {mat_obj.PoissonRatio}")
        
        # Check if concrete values are correct
        density_str = str(mat_obj.Density)
        modulus_str = str(mat_obj.ModulusElasticity)
        poisson = mat_obj.PoissonRatio
        
        concrete_correct = True
        if "2400" not in density_str:
            print("   ❌ Concrete density wrong (should be 2400 kg/m³)")
            concrete_correct = False
        else:
            print("   ✅ Concrete density correct (2400 kg/m³)")
            
        if "27000" not in modulus_str:
            print("   ❌ Concrete modulus wrong (should be 27000 MPa)")
            concrete_correct = False
        else:
            print("   ✅ Concrete modulus correct (27000 MPa)")
            
        if abs(poisson - 0.20) > 0.01:
            print("   ❌ Concrete Poisson wrong (should be 0.20)")
            concrete_correct = False
        else:
            print("   ✅ Concrete Poisson correct (0.20)")
        
        print("\n🔧 Step 3: Testing Steel (ASTM_A992)...")
        
        # Switch to steel
        print("   Setting MaterialStandard = 'ASTM_A992'")
        mat_obj.MaterialStandard = "ASTM_A992"
        
        print("   Properties after setting steel:")
        print(f"   Density: {mat_obj.Density}")
        print(f"   Modulus: {mat_obj.ModulusElasticity}")
        print(f"   Poisson: {mat_obj.PoissonRatio}")
        
        # Check if steel values are correct
        density_str = str(mat_obj.Density)
        modulus_str = str(mat_obj.ModulusElasticity)
        poisson = mat_obj.PoissonRatio
        
        steel_correct = True
        if "7850" not in density_str:
            print("   ❌ Steel density wrong (should be 7850 kg/m³)")
            steel_correct = False
        else:
            print("   ✅ Steel density correct (7850 kg/m³)")
            
        if "200000" not in modulus_str:
            print("   ❌ Steel modulus wrong (should be 200000 MPa)")  
            steel_correct = False
        else:
            print("   ✅ Steel modulus correct (200000 MPa)")
            
        if abs(poisson - 0.30) > 0.01:
            print("   ❌ Steel Poisson wrong (should be 0.30)")
            steel_correct = False
        else:
            print("   ✅ Steel Poisson correct (0.30)")
        
        # Final results
        print("\n" + "=" * 60)
        print("RESULTS")
        print("=" * 60)
        
        if concrete_correct:
            print("🎉 ✅ CONCRETE AUTO-UPDATE: WORKING!")
        else:
            print("❌ CONCRETE AUTO-UPDATE: NOT WORKING")
            
        if steel_correct:
            print("🎉 ✅ STEEL AUTO-UPDATE: WORKING!")
        else:
            print("❌ STEEL AUTO-UPDATE: NOT WORKING")
        
        if concrete_correct and steel_correct:
            print("\n🎉 SUCCESS! Material properties auto-update is working perfectly!")
            print("   ✅ When you select ACI_Normal_30MPa → Concrete properties appear")
            print("   ✅ When you select ASTM_A992 → Steel properties appear")
            print("\n💡 How to use:")
            print("   1. Create Material object")
            print("   2. In Property Panel, select MaterialStandard dropdown")
            print("   3. Choose material (e.g., ACI_Normal_30MPa)")
            print("   4. Properties will update automatically!")
        else:
            print("\n❌ AUTO-UPDATE NOT WORKING PROPERLY")
            print("   Check FreeCAD console for error messages")
            print("   Make sure MaterialStandards.py is properly imported")
        
        return mat_obj
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    test_material_auto_update()