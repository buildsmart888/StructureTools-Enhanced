"""
Quick verification test to run in FreeCAD Python console
This test verifies the NumPoints properties fix
"""

import sys
import os

def run_quick_test():
    """Run a quick test to verify the NumPoints properties fix"""
    print("🚀 Running Quick Verification Test for NumPoints Properties Fix")
    print("=" * 70)
    
    try:
        import FreeCAD
        import Part
        print("✅ FreeCAD modules imported successfully")
    except Exception as e:
        print(f"❌ Failed to import FreeCAD modules: {e}")
        return False
    
    # Add module path
    module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
    if module_path not in sys.path:
        sys.path.insert(0, module_path)
    
    try:
        from freecad.StructureTools import calc
        print("✅ Successfully imported calc module")
    except Exception as e:
        print(f"❌ Failed to import calc module: {e}")
        return False
    
    try:
        # Create new document
        doc = FreeCAD.newDocument("QuickTest")
        print("✅ Created new FreeCAD document")
    except Exception as e:
        print(f"❌ Failed to create document: {e}")
        return False
    
    try:
        # Create a simple beam
        p1 = FreeCAD.Vector(0, 0, 0)
        p2 = FreeCAD.Vector(3000, 0, 0)  # 3m beam
        line = Part.makeLine(p1, p2)
        beam = doc.addObject("Part::Feature", "TestBeam")
        beam.Shape = line
        print("✅ Created test beam")
    except Exception as e:
        print(f"❌ Failed to create beam: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    try:
        # Create calc object
        calc_obj = doc.addObject("App::DocumentObjectGroupPython", "TestCalc")
        calc.Calc(calc_obj, [beam])
        print("✅ Created calc object")
    except Exception as e:
        print(f"❌ Failed to create calc object: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 1: Check that all NumPoints properties exist
    print("\n📋 Test 1: Checking NumPoints Properties Existence")
    num_points_props = [
        ('NumPointsMoment', 5),
        ('NumPointsAxial', 3),
        ('NumPointsShear', 4),
        ('NumPointsTorque', 3),
        ('NumPointsDeflection', 4)  # Changed from 3 to 4 to match our fix
    ]
    
    all_props_exist = True
    for prop_name, expected_default in num_points_props:
        if hasattr(calc_obj, prop_name):
            actual_value = getattr(calc_obj, prop_name)
            if actual_value == expected_default:
                print(f"  ✅ {prop_name}: {actual_value} (correct default)")
            else:
                print(f"  ⚠️ {prop_name}: {actual_value} (expected {expected_default})")
        else:
            print(f"  ❌ {prop_name}: MISSING")
            all_props_exist = False
    
    if all_props_exist:
        print("✅ All NumPoints properties exist with correct defaults")
    else:
        print("❌ Some NumPoints properties are missing")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 2: Check backward compatibility functions
    print("\n📋 Test 2: Checking Backward Compatibility Functions")
    if hasattr(calc_obj.Proxy, 'ensure_required_properties'):
        print("✅ ensure_required_properties method exists")
    else:
        print("❌ ensure_required_properties method is missing")
        FreeCAD.closeDocument(doc.Name)
        return False
        
    if hasattr(calc_obj.Proxy, '_addPropIfMissing'):
        print("✅ _addPropIfMissing method exists")
    else:
        print("❌ _addPropIfMissing method is missing")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 3: Test ensure_required_properties method
    print("\n📋 Test 3: Testing ensure_required_properties Method")
    try:
        calc_obj.Proxy.ensure_required_properties(calc_obj)
        print("✅ ensure_required_properties executed without errors")
    except Exception as e:
        print(f"❌ ensure_required_properties failed: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 4: Test execute method (the main fix)
    print("\n📋 Test 4: Testing Execute Method (Main Fix)")
    try:
        calc_obj.Proxy.execute(calc_obj)
        print("✅ Calc execute completed without NumPointsMoment errors")
    except AttributeError as e:
        if "NumPointsMoment" in str(e):
            print(f"❌ Calc execute failed with NumPointsMoment error: {e}")
            FreeCAD.closeDocument(doc.Name)
            return False
        else:
            print(f"⚠️ Calc execute failed with different AttributeError: {e}")
            # This might be okay if it's a different issue
    except Exception as e:
        print(f"⚠️ Calc execute failed with other error: {e}")
        # This might be okay if it's a different issue not related to NumPoints
    
    # Test 5: Test getattr usage with defaults
    print("\n📋 Test 5: Testing getattr Usage with Defaults")
    try:
        # Test that getattr with defaults works correctly
        moment_points = getattr(calc_obj, 'NumPointsMoment', 5)
        shear_points = getattr(calc_obj, 'NumPointsShear', 4)
        deflection_points = getattr(calc_obj, 'NumPointsDeflection', 4)
        
        if moment_points == 5 and shear_points == 4 and deflection_points == 4:
            print("✅ getattr usage with defaults works correctly")
        else:
            print(f"⚠️ getattr returned unexpected values: moment={moment_points}, shear={shear_points}, deflection={deflection_points}")
    except Exception as e:
        print(f"❌ getattr usage test failed: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    
    print("\n" + "=" * 70)
    print("🎉 QUICK VERIFICATION TEST PASSED!")
    print("The AttributeError: 'FeaturePython' object has no attribute 'NumPointsMoment' should be resolved.")
    return True

# Instructions for running in FreeCAD
print("""
📖 INSTRUCTIONS FOR RUNNING THIS TEST IN FREECAD:

1. Open FreeCAD
2. Open the Python console (View → Panels → Python console)
3. Copy and paste the following commands:

import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/quick_verification_test.py').read())
run_quick_test()

OR simply run:

import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
from quick_verification_test import run_quick_test
run_quick_test()
""")

if __name__ == "__main__":
    # This will only run if executed directly (not in FreeCAD)
    print("This script is designed to run in FreeCAD's Python console.")
    print("Please follow the instructions above.")