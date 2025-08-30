"""
Verification script to test that the NumPoints properties fixes are working correctly
"""

import sys
import os

def verify_fixes():
    """Verify that all fixes are working correctly"""
    print("🔧 Verifying NumPoints Properties Fixes")
    print("=" * 50)
    
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
        doc = FreeCAD.newDocument("FixVerification")
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
    
    # Test 1: Check that all NumPoints properties exist with correct defaults
    print("\n📋 Test 1: Checking NumPoints Properties")
    expected_defaults = {
        'NumPointsMoment': 5,
        'NumPointsAxial': 3,
        'NumPointsShear': 4,
        'NumPointsTorque': 3,
        'NumPointsDeflection': 4
    }
    
    all_correct = True
    for prop_name, expected_value in expected_defaults.items():
        if hasattr(calc_obj, prop_name):
            actual_value = getattr(calc_obj, prop_name)
            if actual_value == expected_value:
                print(f"  ✅ {prop_name}: {actual_value} (correct)")
            else:
                print(f"  ❌ {prop_name}: {actual_value} (expected {expected_value})")
                all_correct = False
        else:
            print(f"  ❌ {prop_name}: MISSING")
            all_correct = False
    
    if all_correct:
        print("✅ All NumPoints properties have correct defaults")
    else:
        print("❌ Some NumPoints properties have incorrect defaults")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 2: Check backward compatibility functions
    print("\n📋 Test 2: Checking Backward Compatibility Functions")
    if hasattr(calc_obj.Proxy, '_addPropIfMissing'):
        print("✅ _addPropIfMissing method exists")
    else:
        print("❌ _addPropIfMissing method is missing")
        FreeCAD.closeDocument(doc.Name)
        return False
        
    if hasattr(calc_obj.Proxy, 'ensure_required_properties'):
        print("✅ ensure_required_properties method exists")
    else:
        print("❌ ensure_required_properties method is missing")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 3: Test _addPropIfMissing method
    print("\n📋 Test 3: Testing _addPropIfMissing Method")
    try:
        calc_obj.Proxy._addPropIfMissing(calc_obj, "App::PropertyInteger", "TestProperty", "Test", "Test property", 99)
        if hasattr(calc_obj, 'TestProperty') and calc_obj.TestProperty == 99:
            print("✅ _addPropIfMissing works correctly")
        else:
            print("❌ _addPropIfMissing failed to add property correctly")
            FreeCAD.closeDocument(doc.Name)
            return False
    except Exception as e:
        print(f"❌ _addPropIfMissing failed with error: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 4: Test ensure_required_properties method
    print("\n📋 Test 4: Testing ensure_required_properties Method")
    try:
        calc_obj.Proxy.ensure_required_properties(calc_obj)
        print("✅ ensure_required_properties executed without errors")
    except Exception as e:
        print(f"❌ ensure_required_properties failed: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 5: Test execute method
    print("\n📋 Test 5: Testing Execute Method")
    try:
        calc_obj.Proxy.execute(calc_obj)
        print("✅ Execute method completed without errors")
    except Exception as e:
        print(f"❌ Execute method failed: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Test 6: Test getattr usage with defaults
    print("\n📋 Test 6: Testing getattr Usage with Defaults")
    try:
        moment_points = getattr(calc_obj, 'NumPointsMoment', 5)
        shear_points = getattr(calc_obj, 'NumPointsShear', 4)
        deflection_points = getattr(calc_obj, 'NumPointsDeflection', 4)
        
        if moment_points == 5 and shear_points == 4 and deflection_points == 4:
            print("✅ getattr usage with defaults works correctly")
        else:
            print(f"❌ getattr returned unexpected values: moment={moment_points}, shear={shear_points}, deflection={deflection_points}")
            FreeCAD.closeDocument(doc.Name)
            return False
    except Exception as e:
        print(f"❌ getattr usage test failed: {e}")
        FreeCAD.closeDocument(doc.Name)
        return False
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    
    print("\n" + "=" * 50)
    print("🎉 ALL FIXES VERIFIED SUCCESSFULLY!")
    print("The NumPoints properties issue has been resolved.")
    return True

if __name__ == "__main__":
    print("🔧 NumPoints Properties Fix Verification")
    print("=" * 50)
    print("This script verifies that the fixes for the AttributeError:")
    print("'FeaturePython' object has no attribute 'NumPointsMoment' are working.")
    print()
    print("To run this test in FreeCAD:")
    print("1. Open FreeCAD")
    print("2. Open the Python console")
    print("3. Run the following commands:")
    print()
    print("import sys")
    print("sys.path.append('c:/Users/thani/AppData/Roaming/FreecAD/Mod/StructureTools')")
    print("exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/verify_fixes.py').read())")
    print("verify_fixes()")
    print()
    
    # If running directly (not in FreeCAD), show instructions
    try:
        import FreeCAD
        # If FreeCAD is available, run the test
        verify_fixes()
    except ImportError:
        # If FreeCAD is not available, just show instructions
        print("This script is designed to run in FreeCAD's Python console.")
        print("Please follow the instructions above to run the verification.")