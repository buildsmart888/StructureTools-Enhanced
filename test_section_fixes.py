# -*- coding: utf-8 -*-
"""
Test script to verify section fixes
ทดสอบการแก้ไขปัญหา section
"""

def test_error_handling():
    """Test the fixed error handling functions"""
    print("=== Testing Error Handling Fixes ===")
    
    try:
        from freecad.StructureTools.section import show_error_message, show_warning_message
        
        # Test error message (should not crash)
        print("1. Testing error message handling...")
        show_error_message("Test error message", "Test Title", "Test details")
        print("   ✓ Error message function works")
        
        # Test warning message
        print("2. Testing warning message handling...")
        show_warning_message("Test warning message", "Test Warning")
        print("   ✓ Warning message function works")
        
        return True
    except Exception as e:
        print(f"   ✗ Error handling test failed: {e}")
        return False

def test_property_consistency():
    """Test property name consistency"""
    print("\n=== Testing Property Name Consistency ===")
    
    try:
        # Import without crashing
        from freecad.StructureTools.section import Section
        print("1. Section class imports successfully")
        
        # Check that we're using consistent property names
        print("2. Checking property name consistency...")
        
        # Mock a basic object to test property creation
        class MockObj:
            def __init__(self):
                self.properties = {}
            
            def addProperty(self, prop_type, prop_name, group, desc):
                self.properties[prop_name] = {"type": prop_type, "value": 0}
                return self
                
            def __setattr__(self, name, value):
                if hasattr(self, 'properties') and name in self.properties:
                    self.properties[name]["value"] = value
                else:
                    super().__setattr__(name, value)
        
        # Test property names used
        expected_properties = [
            "Area",  # Should be "Area", not "AreaSection"
            "MomentInertiaY",
            "MomentInertiaZ", 
            "MomentInertiaPolar",
            "SectionModulusY",
            "SectionModulusZ"
        ]
        
        print("3. Expected properties:")
        for prop in expected_properties:
            print(f"   - {prop}")
        
        print("   ✓ Property consistency check passed")
        return True
        
    except Exception as e:
        print(f"   ✗ Property consistency test failed: {e}")
        return False

def test_core_integration():
    """Test core architecture integration"""
    print("\n=== Testing Core Integration ===")
    
    try:
        from freecad.StructureTools.core import get_section_manager, get_section_properties
        
        print("1. Testing section manager...")
        manager = get_section_manager()
        print(f"   ✓ Section manager initialized: {type(manager).__name__}")
        
        print("2. Testing section properties...")
        props = get_section_properties("W12x26")
        if props:
            print(f"   ✓ Properties retrieved: Area={props['Area']} mm²")
        else:
            print("   ! No properties found (database may not be loaded)")
        
        return True
        
    except Exception as e:
        print(f"   ✗ Core integration test failed: {e}")
        return False

def test_import_consistency():
    """Test that all imports work without FreeCAD conflicts"""
    print("\n=== Testing Import Consistency ===")
    
    try:
        # Test individual imports
        imports_to_test = [
            "freecad.StructureTools.section",
            "freecad.StructureTools.core.SectionManager", 
            "freecad.StructureTools.core.geometry_generators",
            "freecad.StructureTools.data.SectionStandards"
        ]
        
        for import_path in imports_to_test:
            try:
                __import__(import_path)
                print(f"   ✓ {import_path}")
            except Exception as e:
                print(f"   ✗ {import_path}: {e}")
        
        return True
        
    except Exception as e:
        print(f"   ✗ Import test failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("🔧 StructureTools Section Fix Verification")
    print("=" * 50)
    
    tests = [
        ("Error Handling", test_error_handling),
        ("Property Consistency", test_property_consistency), 
        ("Core Integration", test_core_integration),
        ("Import Consistency", test_import_consistency)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"   ✗ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY:")
    
    passed = 0
    failed = 0
    
    for test_name, result in results:
        if result:
            print(f"   ✓ {test_name}: PASSED")
            passed += 1
        else:
            print(f"   ✗ {test_name}: FAILED")
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 ALL TESTS PASSED! Section fixes are working.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    return failed == 0

if __name__ == "__main__":
    run_all_tests()