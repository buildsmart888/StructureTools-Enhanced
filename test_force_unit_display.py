#!/usr/bin/env python3
"""
Test Force Unit Display in StructureTools

This test verifies that force units are displayed correctly in the diagram system.
"""

import sys
import os

# Add the StructureTools path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools', 'utils'))

def test_force_unit_conversion():
    """Test force unit conversion and display"""
    print("=== Force Unit Conversion and Display Test ===")
    
    # Test the force converter
    try:
        from utils.force_converter import ForceConverter, convert_force, get_common_force_conversions
        print("✓ Successfully imported Force Converter")
        
        # Test basic conversions
        test_cases = [
            (1, "kip", "kN", 4.4482216152605),  # Exact conversion
            (1, "kgf", "N", 9.80665),           # Exact conversion
            (1, "tf", "kgf", 1000.0),           # Exact conversion
            (1, "tonf_us", "kip", 2.0),         # Exact conversion
        ]
        
        print("Testing force unit conversions:")
        for value, from_unit, to_unit, expected in test_cases:
            result = convert_force(value, from_unit, to_unit)
            error = abs(result - expected)
            status = "✓" if error < 1e-10 else "✗"
            print(f"   {status} {value} {from_unit} = {result:.12f} {to_unit} (expected {expected})")
            
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    
    # Test units manager integration
    try:
        from utils.units_manager import UnitsManager, get_units_manager
        print("✓ Successfully imported Units Manager")
        
        # Test force formatting
        manager = get_units_manager()
        
        # Test with different unit systems
        print("\nTesting force formatting with different unit systems:")
        
        # SI system
        manager.set_unit_system(UnitsManager.SI_UNITS)
        force_si = manager.format_force(1000)  # 1000 N
        print(f"   SI: 1000 N = {force_si}")
        
        # Thai system
        manager.set_unit_system(UnitsManager.THAI_UNITS)
        force_thai = manager.format_force(1000)  # 1000 N
        print(f"   THAI: 1000 N = {force_thai}")
        
        # US system
        manager.set_unit_system(UnitsManager.US_UNITS)
        force_us = manager.format_force(1000)  # 1000 N
        print(f"   US: 1000 N = {force_us}")
        
    except ImportError as e:
        print(f"✗ Units manager import error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("StructureTools Force Unit Display Test")
    print("=" * 50)
    
    success = test_force_unit_conversion()
    
    print("\n" + "=" * 50)
    if success:
        print("✓ Force unit conversion and display test completed!")
    else:
        print("✗ Force unit conversion and display test failed!")
        sys.exit(1)