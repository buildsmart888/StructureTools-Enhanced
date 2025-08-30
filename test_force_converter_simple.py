#!/usr/bin/env python3
"""
Simple Test for Force Converter

This test verifies that the force converter works correctly without FreeCAD dependencies.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools', 'utils'))

try:
    from force_converter import ForceConverter, convert_force, get_common_force_conversions
    print("✓ Successfully imported Force Converter")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

def test_basic_conversions():
    """Test basic force conversions"""
    print("\n=== Basic Force Conversion Test ===")
    
    # Test known conversion values
    test_cases = [
        (1, "kip", "kN", 4.4482216152605),  # Exact conversion
        (1, "kgf", "N", 9.80665),           # Exact conversion
        (1, "tf", "kgf", 1000.0),           # Exact conversion
        (1, "tonf_us", "kip", 2.0),         # Exact conversion
        (1000, "N", "kN", 1.0),             # Simple conversion
        (1, "MN", "kN", 1000.0),            # Large unit conversion
    ]
    
    print("Testing known conversion values:")
    all_passed = True
    for value, from_unit, to_unit, expected in test_cases:
        try:
            result = convert_force(value, from_unit, to_unit)
            error = abs(result - expected)
            status = "✓" if error < 1e-10 else "✗"
            if error >= 1e-10:
                all_passed = False
            print(f"   {status} {value} {from_unit} = {result:.12f} {to_unit} (expected {expected}, error: {error:.2e})")
        except Exception as e:
            print(f"   ✗ {value} {from_unit} -> {to_unit} failed: {e}")
            all_passed = False
    
    return all_passed

def test_common_conversions():
    """Test common force conversions"""
    print("\n=== Common Force Conversions Test ===")
    
    try:
        conversions = get_common_force_conversions(1, "kip")
        print("Common conversions for 1 kip:")
        # Show first 5 conversions
        for i, (unit, formatted) in enumerate(conversions.items()):
            if i >= 5:
                break
            print(f"   1 kip = {formatted}")
        print("✓ Common force conversions working")
        return True
    except Exception as e:
        print(f"✗ Common force conversions failed: {e}")
        return False

def test_precision_formatting():
    """Test precision formatting"""
    print("\n=== Precision Formatting Test ===")
    
    try:
        converter = ForceConverter()
        
        # Test different precision levels
        test_value = 1234.56789
        formatted1 = converter.format_value(test_value, "kN", 2)
        formatted2 = converter.format_value(test_value, "kN", 4)
        formatted3 = converter.format_value(test_value, "kN", 0)
        
        print(f"   Value {test_value} formatted:")
        print(f"     2 decimal places: {formatted1}")
        print(f"     4 decimal places: {formatted2}")
        print(f"     0 decimal places: {formatted3}")
        
        # Test without unit
        formatted4 = converter.format_value(test_value, "kN", 2, show_unit=False)
        print(f"     Without unit: {formatted4}")
        
        print("✓ Precision formatting working")
        return True
    except Exception as e:
        print(f"✗ Precision formatting failed: {e}")
        return False

if __name__ == "__main__":
    print("StructureTools Force Converter Simple Test")
    print("=" * 50)
    
    test1_passed = test_basic_conversions()
    test2_passed = test_common_conversions()
    test3_passed = test_precision_formatting()
    
    print("\n" + "=" * 50)
    if test1_passed and test2_passed and test3_passed:
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed!")
        sys.exit(1)