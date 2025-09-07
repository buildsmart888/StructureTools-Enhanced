#!/usr/bin/env python3
"""
Debug Material Standards Import

This script debugs why MaterialStandards import is failing
and _update_standard_properties is not working.

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\debug_material_standards_import.py').read())
"""

import FreeCAD as App

def debug_material_standards_import():
    """Debug MaterialStandards import and availability."""
    print("🔍 DEBUG: MaterialStandards Import")
    print("=" * 60)
    
    # Test 1: Direct import of MaterialStandards
    print("\n1️⃣ Testing direct import of MaterialStandards...")
    try:
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS, MATERIAL_CATEGORIES
        print(f"   ✅ Direct import successful")
        print(f"   📊 Total standards: {len(MATERIAL_STANDARDS)}")
        
        if "ACI_Normal_30MPa" in MATERIAL_STANDARDS:
            props = MATERIAL_STANDARDS["ACI_Normal_30MPa"]
            print(f"   ✅ ACI_Normal_30MPa found: {props}")
        else:
            print(f"   ❌ ACI_Normal_30MPa NOT found")
            concrete_standards = [k for k in MATERIAL_STANDARDS.keys() if 'ACI' in k or 'concrete' in k.lower()]
            print(f"   Available concrete-like standards: {concrete_standards}")
            
    except Exception as e:
        print(f"   ❌ Direct import failed: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 2: Import from material.py
    print("\n2️⃣ Testing import from material.py...")
    try:
        from freecad.StructureTools import material
        standards = getattr(material, 'MATERIAL_STANDARDS', None)
        
        if standards:
            print(f"   ✅ material.py has MATERIAL_STANDARDS: {len(standards)}")
            if "ACI_Normal_30MPa" in standards:
                props = standards["ACI_Normal_30MPa"]
                print(f"   ✅ ACI_Normal_30MPa in material.py: {props}")
            else:
                print(f"   ❌ ACI_Normal_30MPa NOT in material.py")
        else:
            print(f"   ❌ material.py has no MATERIAL_STANDARDS or it's empty")
            
    except Exception as e:
        print(f"   ❌ material.py import test failed: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 3: Check if material objects can access standards
    print("\n3️⃣ Testing material object access to standards...")
    
    # Find existing material object
    material_obj = None
    for obj in App.ActiveDocument.Objects if App.ActiveDocument else []:
        if hasattr(obj, 'MaterialStandard') and hasattr(obj, 'Proxy'):
            material_obj = obj
            break
    
    if material_obj:
        print(f"   ✅ Found material object: {material_obj.Label}")
        
        if hasattr(material_obj.Proxy, '_update_standard_properties'):
            print(f"   ✅ Object has _update_standard_properties method")
            
            # Test calling the method directly
            try:
                print(f"   🔧 Testing direct call to _update_standard_properties...")
                material_obj.MaterialStandard = "ACI_Normal_30MPa" 
                material_obj.Proxy._update_standard_properties(material_obj)
                print(f"   ✅ Direct call completed")
                
                print(f"   📊 Results after direct call:")
                print(f"      Density: {material_obj.Density}")
                print(f"      Modulus: {material_obj.ModulusElasticity}")
                print(f"      Poisson: {material_obj.PoissonRatio}")
                
            except Exception as e:
                print(f"   ❌ Direct call failed: {e}")
                import traceback
                traceback.print_exc()
        else:
            print(f"   ❌ Object has no _update_standard_properties method")
    else:
        print(f"   ❌ No material object found for testing")

def test_import_in_different_ways():
    """Test different ways to import MaterialStandards."""
    print("\n🔬 TESTING DIFFERENT IMPORT METHODS")
    print("=" * 60)
    
    import_methods = [
        "from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS",
        "from .data.MaterialStandards import MATERIAL_STANDARDS",
        "import freecad.StructureTools.data.MaterialStandards as MS",
    ]
    
    for i, method in enumerate(import_methods, 1):
        print(f"\n{i}️⃣ Testing: {method}")
        try:
            if "from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS" in method:
                from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
                result = MATERIAL_STANDARDS
            elif "from .data.MaterialStandards import MATERIAL_STANDARDS" in method:
                # This would only work from within the package
                print("   ⏭️ Skipping relative import (only works from within package)")
                continue
            elif "import freecad.StructureTools.data.MaterialStandards as MS" in method:
                import freecad.StructureTools.data.MaterialStandards as MS
                result = MS.MATERIAL_STANDARDS
            
            print(f"   ✅ Import successful: {len(result)} standards")
            
            if "ACI_Normal_30MPa" in result:
                print(f"   ✅ ACI_Normal_30MPa available")
            else:
                print(f"   ❌ ACI_Normal_30MPa missing")
                
        except Exception as e:
            print(f"   ❌ Import failed: {e}")

def check_material_py_import_section():
    """Check how material.py imports MaterialStandards."""
    print("\n📁 CHECKING MATERIAL.PY IMPORT SECTION")
    print("=" * 60)
    
    try:
        # Read the import section of material.py
        import freecad.StructureTools.material as mat_module
        
        # Check if MATERIAL_STANDARDS is available at module level
        if hasattr(mat_module, 'MATERIAL_STANDARDS'):
            standards = getattr(mat_module, 'MATERIAL_STANDARDS')
            if standards:
                print(f"✅ material.py module has MATERIAL_STANDARDS: {len(standards)} items")
                
                # List first few standards
                sample_standards = list(standards.keys())[:5]
                print(f"   Sample standards: {sample_standards}")
                
                if "ACI_Normal_30MPa" in standards:
                    concrete_props = standards["ACI_Normal_30MPa"]
                    print(f"✅ ACI_Normal_30MPa properties: {concrete_props}")
                else:
                    print("❌ ACI_Normal_30MPa not found in module-level MATERIAL_STANDARDS")
            else:
                print("❌ material.py MATERIAL_STANDARDS is empty")
        else:
            print("❌ material.py has no MATERIAL_STANDARDS attribute")
            
        # Check what's available in the module
        available_attrs = [attr for attr in dir(mat_module) if not attr.startswith('_')]
        print(f"📋 Available attributes in material.py: {available_attrs}")
        
    except Exception as e:
        print(f"❌ Error checking material.py: {e}")
        import traceback
        traceback.print_exc()

def run_complete_debug():
    """Run complete debug of MaterialStandards import issues."""
    print("MATERIAL STANDARDS IMPORT DEBUG")
    print("=" * 80)
    
    debug_material_standards_import()
    test_import_in_different_ways()
    check_material_py_import_section()
    
    print("\n" + "=" * 80)
    print("DEBUG SUMMARY")
    print("=" * 80)
    print("🔍 Check the results above to identify the import issue")
    print("📋 Look for any error messages or missing imports")
    print("🎯 Focus on whether ACI_Normal_30MPa is found in each test")

if __name__ == "__main__":
    run_complete_debug()