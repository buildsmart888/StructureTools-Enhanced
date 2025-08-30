"""
Test script to verify the fixes for the NumPoints properties and ReactionLoadCombo issues
"""

import sys
import os

def test_fixes():
    """Test that the fixes are working correctly"""
    print("🔧 Testing NumPoints Properties and ReactionLoadCombo Fixes")
    print("=" * 60)
    
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
        doc = FreeCAD.newDocument("FixTest")
        print("✅ Created new FreeCAD document")
    except Exception as e:
        print(f"❌ Failed to create document: {e}")
        return False
    
    try:
        # Create a simple beam
        p1 = FreeCAD.Vector(0, 0, 0)
        p2 = FreeCAD.Vector(1000, 0, 0)  # 1m beam
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
    
    # Test 2: Check ReactionLoadCombo property
    print("\n📋 Test 2: Checking ReactionLoadCombo Property")
    if hasattr(calc_obj, 'ReactionLoadCombo'):
        print("✅ ReactionLoadCombo property exists")
        # Check that it has valid enumeration values
        try:
            # This should not raise an exception
            current_value = calc_obj.ReactionLoadCombo
            print(f"✅ ReactionLoadCombo current value: {current_value}")
        except Exception as e:
            print(f"❌ Failed to access ReactionLoadCombo: {e}")
            all_correct = False
    else:
        print("❌ ReactionLoadCombo property is missing")
        all_correct = False
    
    # Test 3: Test backward compatibility functions
    print("\n📋 Test 3: Checking Backward Compatibility Functions")
    if hasattr(calc_obj.Proxy, '_addPropIfMissing'):
        print("✅ _addPropIfMissing method exists")
    else:
        print("❌ _addPropIfMissing method is missing")
        all_correct = False
        
    if hasattr(calc_obj.Proxy, 'ensure_required_properties'):
        print("✅ ensure_required_properties method exists")
    else:
        print("❌ ensure_required_properties method is missing")
        all_correct = False
    
    # Test 4: Test ensure_required_properties method
    print("\n📋 Test 4: Testing ensure_required_properties Method")
    try:
        calc_obj.Proxy.ensure_required_properties(calc_obj)
        print("✅ ensure_required_properties executed without errors")
    except Exception as e:
        print(f"❌ ensure_required_properties failed: {e}")
        all_correct = False
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    
    print("\n" + "=" * 60)
    if all_correct:
        print("🎉 ALL TESTS PASSED!")
        print("The NumPoints properties and ReactionLoadCombo issues should be resolved.")
        return True
    else:
        print("💥 SOME TESTS FAILED!")
        return False

if __name__ == "__main__":
    print("🔧 NumPoints Properties and ReactionLoadCombo Fix Test")
    print("=" * 60)
    print("This script verifies that the fixes for the AttributeError:")
    print("'FeaturePython' object has no attribute 'NumPointsMoment'")
    print("and the ReactionLoadCombo ValueError are working.")
    print()
    
    # If running directly (not in FreeCAD), show instructions
    try:
        import FreeCAD
        # If FreeCAD is available, run the test
        test_fixes()
    except ImportError:
        # If FreeCAD is not available, just show instructions
        print("This script is designed to run in FreeCAD's Python console.")
        print("Please follow these instructions to run the verification:")
        print()
        print("1. Open FreeCAD")
        print("2. Open the Python console (View → Panels → Python console)")
        print("3. Run the following commands:")
        print()
        print("import sys")
        print("sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')")
        print("exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_fixes.py').read())")
        print("test_fixes()")
        print()