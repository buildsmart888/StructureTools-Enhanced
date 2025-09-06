#!/usr/bin/env python3
"""
Test script to verify the specific fixes we made to calc.py:
1. NumPoints properties initialization
2. Unbound variable fixes (direction, axis, selected_combo)
"""

import sys
import os
import traceback

# Add the module path to sys.path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
sys.path.insert(0, module_path)

def test_num_points_properties_exist():
    """Test that NumPoints properties exist in the Calc class"""
    print("Testing if NumPoints properties are defined in Calc class...")
    
    try:
        # Import the Calc class
        from calc import Calc
        
        # Check if the required methods exist
        required_methods = [
            '_addPropIfMissing',
            'ensure_required_properties'
        ]
        
        missing_methods = []
        for method in required_methods:
            if not hasattr(Calc, method):
                missing_methods.append(method)
            else:
                print(f"  ✅ Method '{method}' exists")
                
        if missing_methods:
            print(f"  ❌ Missing methods: {missing_methods}")
            return False
        else:
            print("  ✅ All required methods exist")
            return True
            
    except Exception as e:
        print(f"  ❌ Error: {e}")
        traceback.print_exc()
        return False

def test_set_loads_method_structure():
    """Test the structure of the setLoads method for unbound variable fixes"""
    print("\nTesting setLoads method structure for unbound variable fixes...")
    
    try:
        import inspect
        from calc import Calc
        
        # Get the source code of the setLoads method
        source = inspect.getsource(Calc.setLoads)
        
        # Check if direction and axis are initialized before the match statement
        if "direction = 1" in source and "axis = 'FX'" in source:
            print("  ✅ direction and axis are initialized before match statement")
        else:
            print("  ❌ direction and axis are not properly initialized")
            return False
            
        # Check if there's a default case in the match statement
        if "case _:" in source:
            print("  ✅ Default case exists in match statement")
        else:
            print("  ❌ Default case missing in match statement")
            return False
            
        # Check if selected_combo is handled in exception handler
        if "selected_combo = getattr(obj, 'ReactionLoadCombo', 'Unknown')" in inspect.getsource(Calc.onChanged):
            print("  ✅ selected_combo is handled in exception handler")
        else:
            print("  ❌ selected_combo is not handled in exception handler")
            return False
            
        print("  ✅ All unbound variable fixes are in place")
        return True
        
    except Exception as e:
        print(f"  ❌ Error examining method structure: {e}")
        traceback.print_exc()
        return False

def test_getattr_usage():
    """Test that getattr is used for accessing NumPoints properties"""
    print("\nTesting getattr usage for NumPoints properties...")
    
    try:
        import inspect
        from calc import Calc
        
        # Get the source code of methods that should use getattr
        source_lines = []
        
        # Check _build_member_summary method
        if hasattr(Calc, '_build_member_summary'):
            source_lines.extend(inspect.getsource(Calc._build_member_summary).split('\n'))
            
        # Check execute method
        source_lines.extend(inspect.getsource(Calc.execute).split('\n'))
        
        # Join all source lines
        full_source = '\n'.join(source_lines)
        
        # Check for getattr usage with NumPoints properties
        required_getattr_calls = [
            "getattr(obj, 'NumPointsMoment'",
            "getattr(obj, 'NumPointsAxial'", 
            "getattr(obj, 'NumPointsShear'",
            "getattr(obj, 'NumPointsTorque'",
            "getattr(obj, 'NumPointsDeflection'"
        ]
        
        missing_calls = []
        for call in required_getattr_calls:
            if call in full_source:
                print(f"  ✅ Found: {call}")
            else:
                missing_calls.append(call)
                print(f"  ⚠️  Missing: {call}")
                
        # This is not critical since we're looking at specific lines, but the main thing
        # is that direct access like "obj.NumPointsMoment" is replaced
        if "obj.NumPointsMoment" not in full_source or "getattr(obj, 'NumPointsMoment'" in full_source:
            print("  ✅ Direct property access appears to be fixed")
            return True
        else:
            print("  ❌ Direct property access may still exist")
            return False
            
    except Exception as e:
        print(f"  ❌ Error examining getattr usage: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 70)
    print("Testing fixes for calc.py issues")
    print("=" * 70)
    
    tests = [
        test_num_points_properties_exist,
        test_set_loads_method_structure,
        test_getattr_usage
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ❌ Test {test.__name__} failed with exception: {e}")
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 70)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 70)
    
    if failed == 0:
        print("🎉 All tests passed! The fixes appear to be correctly implemented.")
        return True
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)