#!/usr/bin/env python3
"""
Test Material Import

Test if material.py can import MaterialStandards correctly.

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_material_import.py').read())
"""

import FreeCAD as App

def test_material_import():
    """Test importing material.py and check MaterialStandards."""
    print("🧪 TESTING MATERIAL.PY IMPORT")
    print("=" * 60)
    
    try:
        # Force reload of material module
        import sys
        module_name = 'freecad.StructureTools.material'
        if module_name in sys.modules:
            print(f"🔄 Reloading existing {module_name} module...")
            del sys.modules[module_name]
        
        # Import material module
        print("📥 Importing material module...")
        import freecad.StructureTools.material as material_module
        
        print("✅ Material module imported successfully")
        
        # Check MATERIAL_STANDARDS
        if hasattr(material_module, 'MATERIAL_STANDARDS'):
            standards = material_module.MATERIAL_STANDARDS
            print(f"📊 MATERIAL_STANDARDS found: {len(standards)} items")
            
            if standards:
                # List available standards
                all_standards = list(standards.keys())
                print(f"📋 Available standards: {all_standards[:10]}{'...' if len(all_standards) > 10 else ''}")
                
                # Check for concrete standard
                if "ACI_Normal_30MPa" in standards:
                    concrete_props = standards["ACI_Normal_30MPa"]
                    print(f"✅ ACI_Normal_30MPa found: {concrete_props}")
                    return True
                else:
                    print("❌ ACI_Normal_30MPa NOT found")
                    concrete_like = [s for s in all_standards if 'ACI' in s or 'concrete' in s.lower()]
                    print(f"🔍 Concrete-like standards: {concrete_like}")
                    return False
            else:
                print("❌ MATERIAL_STANDARDS is empty")
                return False
        else:
            print("❌ No MATERIAL_STANDARDS attribute found")
            return False
            
    except Exception as e:
        print(f"❌ Error importing material: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_create_material_with_working_import():
    """Test creating material with working MaterialStandards."""
    print(f"\n🔧 TESTING MATERIAL CREATION WITH WORKING IMPORT")
    print("-" * 60)
    
    # Ensure we have document
    if not App.ActiveDocument:
        App.newDocument("MaterialImportTest")
    
    try:
        # Import material class
        from freecad.StructureTools.material import Material
        
        # Create material object
        mat_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "TestImport")
        Material(mat_obj)
        
        print("✅ Material object created")
        
        # Check available standards
        if hasattr(mat_obj, 'MaterialStandard'):
            available = mat_obj.MaterialStandard
            print(f"📋 Available MaterialStandards: {len(available)} items")
            
            if "ACI_Normal_30MPa" in available:
                print("✅ ACI_Normal_30MPa is available in dropdown")
                
                # Set to concrete
                print("🔧 Setting MaterialStandard to ACI_Normal_30MPa...")
                mat_obj.MaterialStandard = "ACI_Normal_30MPa"
                
                # Check properties
                print(f"📊 Properties after setting:")
                print(f"   Density: {mat_obj.Density}")
                print(f"   Modulus: {mat_obj.ModulusElasticity}")
                print(f"   Poisson: {mat_obj.PoissonRatio}")
                
                # Check if concrete values are correct
                density_str = str(mat_obj.Density)
                modulus_str = str(mat_obj.ModulusElasticity)
                poisson = mat_obj.PoissonRatio
                
                if "2400" in density_str and "27000" in modulus_str and abs(poisson - 0.20) < 0.01:
                    print("🎉 SUCCESS! Material auto-update is working!")
                    return True
                else:
                    print("⚠️  Properties updated but values may be incorrect")
                    return False
            else:
                print("❌ ACI_Normal_30MPa not in available standards")
                concrete_like = [s for s in available if 'ACI' in s]
                print(f"🔍 ACI-like standards: {concrete_like}")
                return False
        else:
            print("❌ MaterialStandard property not found")
            return False
            
    except Exception as e:
        print(f"❌ Error creating material: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_material_import_test():
    """Run complete material import test."""
    print("MATERIAL IMPORT AND AUTO-UPDATE TEST")
    print("=" * 80)
    
    # Test import first
    import_success = test_material_import()
    
    if import_success:
        # Test material creation
        create_success = test_create_material_with_working_import()
        
        print("\n" + "=" * 80)
        print("FINAL RESULTS")
        print("=" * 80)
        
        if create_success:
            print("🎉 SUCCESS! Material auto-update is working correctly!")
            print("✅ MaterialStandards imported successfully")
            print("✅ Material object creation successful")
            print("✅ ACI_Normal_30MPa properties update automatically")
            print("\n💡 Your original Material_ACI_Normal_30MPa001 should now work.")
            print("   Try selecting different MaterialStandard values in Property Panel!")
        else:
            print("⚠️  Material creation has issues but import works")
    else:
        print("❌ Material import failed - need to fix MaterialStandards import")

if __name__ == "__main__":
    run_material_import_test()