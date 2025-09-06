"""
Test runner script to execute all StructureTools tests
"""

import sys
import os
import unittest

def run_all_tests():
    """Run all test suites"""
    print("🚀 Starting StructureTools Comprehensive Test Suite")
    print("=" * 60)
    
    # Add module path
    module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
    if module_path not in sys.path:
        sys.path.insert(0, module_path)
    
    # Import test modules
    try:
        import test_calc_comprehensive
        import test_diagram_comprehensive
        import test_structuretools_full
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Make sure you're running this from the correct directory")
        return False
    
    # Track overall success
    all_passed = True
    
    # Run calc tests
    print("\n🧪 Running Calc Comprehensive Tests...")
    print("-" * 40)
    try:
        calc_success = test_calc_comprehensive.run_tests()
        if calc_success:
            print("✅ Calc tests passed")
        else:
            print("❌ Calc tests failed")
            all_passed = False
    except Exception as e:
        print(f"❌ Calc tests error: {e}")
        all_passed = False
    
    # Run diagram tests
    print("\n🧪 Running Diagram Comprehensive Tests...")
    print("-" * 40)
    try:
        diagram_success = test_diagram_comprehensive.run_tests()
        if diagram_success:
            print("✅ Diagram tests passed")
        else:
            print("❌ Diagram tests failed")
            all_passed = False
    except Exception as e:
        print(f"❌ Diagram tests error: {e}")
        all_passed = False
    
    # Run full integration tests
    print("\n🧪 Running Full Integration Tests...")
    print("-" * 40)
    try:
        full_success = test_structuretools_full.run_full_tests()
        if full_success:
            print("✅ Full integration tests passed")
        else:
            print("❌ Full integration tests failed")
            all_passed = False
    except Exception as e:
        print(f"❌ Full integration tests error: {e}")
        all_passed = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! StructureTools is working correctly.")
        return True
    else:
        print("💥 SOME TESTS FAILED! Please check the output above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    if not success:
        sys.exit(1)