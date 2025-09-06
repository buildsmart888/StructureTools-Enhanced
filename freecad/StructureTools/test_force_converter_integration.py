#!/usr/bin/env python3
"""
Test Force Converter Integration with Units Manager

This test verifies that the force converter is properly integrated
with the existing units manager system.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from utils.units_manager import (
        UnitsManager, get_units_manager, set_units_system, 
        format_force, format_stress, format_modulus,
        is_thai_units, is_si_units, is_us_units
    )
    print("✓ Successfully imported Units Manager")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

def test_force_converter_integration():
    """Test force converter integration with units manager"""
    print("\n=== Force Converter Integration Test ===")
    
    # Get units manager instance
    manager = get_units_manager()
    
    # Test enhanced force conversion
    print("\n1. Testing Enhanced Force Conversion:")
    try:
        # Test basic conversions
        result1 = manager.convert_force_enhanced(1, "kip", "kN")
        print(f"   1 kip = {result1:.5f} kN")
        
        result2 = manager.convert_force_enhanced(1000, "N", "kgf")
        print(f"   1000 N = {result2:.5f} kgf")
        
        result3 = manager.convert_force_enhanced(1, "tf", "kip")
        print(f"   1 tf = {result3:.5f} kip")
        
        print("   ✓ Enhanced force conversion working")
    except Exception as e:
        print(f"   ✗ Enhanced force conversion failed: {e}")
    
    # Test common force conversions
    print("\n2. Testing Common Force Conversions:")
    try:
        conversions = manager.get_common_force_conversions(1, "kip")
        print("   Common conversions for 1 kip:")
        for unit, formatted in list(conversions.items())[:5]:  # Show first 5
            print(f"     1 kip = {formatted}")
        print("   ✓ Common force conversions working")
    except Exception as e:
        print(f"   ✗ Common force conversions failed: {e}")
    
    # Test with different unit systems
    print("\n3. Testing with Different Unit Systems:")
    systems = ["SI", "US", "THAI"]
    
    for system in systems:
        try:
            set_units_system(system)
            force_str = format_force(100000)  # 100 kN
            print(f"   {system} system: {force_str}")
        except Exception as e:
            print(f"   {system} system test failed: {e}")
    
    print("\n✓ Force converter integration test completed")

def test_precision_and_accuracy():
    """Test precision and accuracy of force conversions"""
    print("\n=== Precision and Accuracy Test ===")
    
    manager = get_units_manager()
    
    # Test known conversion values
    test_cases = [
        (1, "kip", "kN", 4.4482216152605),  # Exact conversion
        (1, "kgf", "N", 9.80665),           # Exact conversion
        (1, "tf", "kgf", 1000.0),           # Exact conversion
        (1, "tonf_us", "kip", 2.0),         # Exact conversion
    ]
    
    print("Testing known conversion values:")
    for value, from_unit, to_unit, expected in test_cases:
        try:
            result = manager.convert_force_enhanced(value, from_unit, to_unit)
            error = abs(result - expected)
            status = "✓" if error < 1e-10 else "✗"
            print(f"   {status} {value} {from_unit} = {result:.12f} {to_unit} (expected {expected}, error: {error:.2e})")
        except Exception as e:
            print(f"   ✗ {value} {from_unit} -> {to_unit} failed: {e}")

if __name__ == "__main__":
    print("StructureTools Force Converter Integration Test")
    print("=" * 50)
    
    test_force_converter_integration()
    test_precision_and_accuracy()
    
    print("\n" + "=" * 50)
    print("Test completed!")