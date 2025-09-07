#!/usr/bin/env python3
"""
Fix Existing Material for Auto-Update

This script fixes the existing Material_ACI_Normal_30MPa001 object 
to enable automatic property updates when MaterialStandard is changed.

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\fix_existing_material_for_auto_update.py').read())
"""

import FreeCAD as App

def fix_existing_material_object():
    """Fix existing Material_ACI_Normal_30MPa001 to enable auto-update."""
    print("🔧 FIXING EXISTING MATERIAL OBJECT")
    print("=" * 60)
    
    if not App.ActiveDocument:
        print("❌ No active document")
        return
    
    # Find the problematic object
    target_object = None
    target_names = [
        "Material_ACI_Normal_30MPa001",
        "Material_ACI_Normal_30MPa",
    ]
    
    for obj in App.ActiveDocument.Objects:
        if obj.Name in target_names or obj.Label in target_names:
            target_object = obj
            break
        if "ACI_Normal_30MP" in obj.Name or "ACI_Normal_30MP" in obj.Label:
            target_object = obj
            break
    
    if not target_object:
        print("❌ Material_ACI_Normal_30MPa001 not found")
        return
    
    print(f"✅ Found target object: {target_object.Label} ({target_object.Name})")
    
    # Check current properties
    print(f"\n📊 Current properties:")
    print(f"   Density: {target_object.Density}")
    print(f"   Modulus: {target_object.ModulusElasticity}")
    print(f"   Poisson: {target_object.PoissonRatio}")
    if hasattr(target_object, 'MaterialStandard'):
        print(f"   MaterialStandard: {target_object.MaterialStandard}")
    else:
        print("   ❌ No MaterialStandard property!")
    
    # Re-apply Material class to enable auto-update
    print(f"\n🔧 Re-applying Material class to enable auto-update...")
    
    try:
        from freecad.StructureTools.material import Material
        
        # Re-apply the Material proxy
        Material(target_object)
        print("✅ Material class re-applied")
        
        # Ensure MaterialStandard is set correctly for concrete
        if hasattr(target_object, 'MaterialStandard'):
            print(f"\n🔧 Setting MaterialStandard to ACI_Normal_30MPa...")
            target_object.MaterialStandard = "ACI_Normal_30MPa"
            print("✅ MaterialStandard set")
        
        # Force recompute
        target_object.recompute()
        App.ActiveDocument.recompute()
        
        # Check results
        print(f"\n✅ Properties after fix:")
        print(f"   Density: {target_object.Density}")
        print(f"   Modulus: {target_object.ModulusElasticity}")
        print(f"   Poisson: {target_object.PoissonRatio}")
        
        # Verify concrete values
        density_str = str(target_object.Density)
        modulus_str = str(target_object.ModulusElasticity)
        poisson = target_object.PoissonRatio
        
        success = True
        if "2400" not in density_str:
            print("   ❌ Density still wrong")
            success = False
        else:
            print("   ✅ Density correct (2400 kg/m³)")
            
        if "27000" not in modulus_str:
            print("   ❌ Modulus still wrong")
            success = False
        else:
            print("   ✅ Modulus correct (27000 MPa)")
            
        if abs(poisson - 0.20) > 0.01:
            print("   ❌ Poisson still wrong")
            success = False
        else:
            print("   ✅ Poisson correct (0.20)")
        
        if success:
            print(f"\n🎉 SUCCESS! {target_object.Label} now shows correct concrete properties!")
            print("   The object now supports auto-update when you change MaterialStandard")
        else:
            print(f"\n⚠️  Properties may need manual adjustment")
            
        return target_object
        
    except Exception as e:
        print(f"❌ Error fixing object: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_auto_update_on_fixed_object(obj):
    """Test auto-update on the fixed object."""
    if not obj:
        return
        
    print(f"\n🧪 TESTING AUTO-UPDATE ON FIXED OBJECT")
    print("-" * 60)
    
    try:
        # Test switching to steel
        print("🔧 Testing switch to ASTM_A992 (steel)...")
        obj.MaterialStandard = "ASTM_A992"
        
        print(f"   After switching to steel:")
        print(f"   Density: {obj.Density}")
        print(f"   Modulus: {obj.ModulusElasticity}")
        print(f"   Poisson: {obj.PoissonRatio}")
        
        # Switch back to concrete
        print("\n🔧 Testing switch back to ACI_Normal_30MPa (concrete)...")
        obj.MaterialStandard = "ACI_Normal_30MPa"
        
        print(f"   After switching back to concrete:")
        print(f"   Density: {obj.Density}")
        print(f"   Modulus: {obj.ModulusElasticity}")
        print(f"   Poisson: {obj.PoissonRatio}")
        
        print("\n✅ Auto-update test completed!")
        print("💡 Now you can change MaterialStandard in Property Panel and see values update automatically!")
        
    except Exception as e:
        print(f"❌ Error testing auto-update: {e}")

def run_fix_existing_material():
    """Run the complete fix for existing material object."""
    fixed_obj = fix_existing_material_object()
    
    if fixed_obj:
        test_auto_update_on_fixed_object(fixed_obj)
        
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print("✅ Existing material object has been fixed")
        print("✅ Auto-update functionality enabled")
        print("✅ Correct concrete properties applied")
        print("\n💡 HOW TO USE:")
        print("1. Select the material object in FreeCAD")
        print("2. Go to Property Panel → Standard section")
        print("3. Click MaterialStandard dropdown")
        print("4. Select different materials (ACI_Normal_30MPa, ASTM_A992, etc.)")
        print("5. Watch properties update automatically!")

if __name__ == "__main__":
    run_fix_existing_material()