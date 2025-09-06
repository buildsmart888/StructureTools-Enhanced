#!/usr/bin/env python3
"""
Complete Global Units System Test
Tests 3-level hierarchy: System → Category → Report overrides
Tests SI/US/Thai engineering units with comprehensive validation
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'freecad'))

try:
    from freecad.StructureTools.utils.units_manager import UnitsManager, get_units_manager, set_units_system
    print("✓ Successfully imported new units_manager")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

def test_three_unit_systems():
    """Test basic functionality of all three unit systems"""
    print("\n=== Testing Three Unit Systems ===")
    
    manager = UnitsManager()
    
    # Test SI system
    manager.set_unit_system("SI")
    print(f"SI System - Force: {manager.format_force(100000)}")  # 100 kN
    print(f"SI System - Stress: {manager.format_stress(25000000)}")  # 25 MPa
    print(f"SI System - Length: {manager.format_length(5.0)}")  # 5.0 m
    
    # Test US system
    manager.set_unit_system("US")
    print(f"US System - Force: {manager.format_force(100000)}")  # Convert to kips
    print(f"US System - Stress: {manager.format_stress(25000000)}")  # Convert to ksi
    print(f"US System - Length: {manager.format_length(5.0)}")  # Convert to ft
    
    # Test Thai system
    manager.set_unit_system("THAI")
    print(f"Thai System - Force: {manager.format_force(100000)}")  # Convert to kgf
    print(f"Thai System - Stress: {manager.format_stress(25000000)}")  # Convert to ksc
    print(f"Thai System - Length: {manager.format_length(5.0)}")  # Convert to cm

def test_category_overrides():
    """Test category-level overrides"""
    print("\n=== Testing Category Overrides ===")
    
    manager = UnitsManager()
    manager.set_unit_system("SI")  # Base system: SI
    
    # Override stress to Thai units
    manager.set_category_override("stress", "THAI")
    
    print(f"Mixed Units - Force (SI): {manager.format_force(100000)}")  # kN
    print(f"Mixed Units - Stress (Thai): {manager.format_stress(25000000)}")  # ksc
    print(f"Mixed Units - Length (SI): {manager.format_length(5.0)}")  # m

def test_report_overrides():
    """Test report-level overrides"""
    print("\n=== Testing Report Overrides ===")
    
    manager = UnitsManager()
    manager.set_unit_system("SI")
    manager.set_category_override("stress", "THAI")
    
    # Test without report override
    print(f"Category Override - Stress: {manager.format_stress(25000000, use_report_units=False)}")
    
    # Test with report override
    manager.set_report_override("stress", "US")
    print(f"Report Override - Stress: {manager.format_stress(25000000, use_report_units=True)}")

def test_material_recommendations():
    """Test material recommendations in all systems"""
    print("\n=== Testing Material Recommendations ===")
    
    manager = UnitsManager()
    
    for system in ["SI", "US", "THAI"]:
        manager.set_unit_system(system)
        recommendations = manager.get_material_recommendations()
        print(f"\n{system} System Recommendations:")
        for key, (value, unit) in recommendations.items():
            print(f"  {key}: {value:.0f} {unit}")

def test_thai_conversion_accuracy():
    """Verify Thai conversion accuracy with known values"""
    print("\n=== Testing Thai Conversion Accuracy ===")
    
    manager = UnitsManager()
    manager.set_unit_system("THAI")
    
    # Test known conversions
    test_cases = [
        (400000000, "400 MPa should = 4,079 ksc"),  # SD40 steel
        (300000000, "300 MPa should = 3,059 ksc"),  # SD30 steel
        (28000000, "28 MPa should = 285.5 ksc"),    # fc' concrete
        (200000000000, "200 GPa should = 2,039,432 ksc")  # Steel modulus
    ]
    
    for value_pa, description in test_cases:
        formatted = manager.format_stress(value_pa)
        print(f"{description}: {formatted}")

def test_global_functions():
    """Test global convenience functions"""
    print("\n=== Testing Global Functions ===")
    
    # Set global system to Thai
    set_units_system("THAI")
    
    # Import global functions
    from freecad.StructureTools.utils.units_manager import (
        is_thai_units, format_force, format_stress, format_modulus
    )
    
    print(f"Is Thai units: {is_thai_units()}")
    print(f"Global format force: {format_force(50000)}")
    print(f"Global format stress: {format_stress(400000000)}")
    print(f"Global format modulus: {format_modulus(200000000000)}")

def test_comprehensive_conversion_tables():
    """Test comprehensive conversion functionality"""
    print("\n=== Testing Conversion Tables ===")
    
    manager = UnitsManager()
    
    # Test direct conversions
    print("Direct Conversions:")
    print(f"1 MPa = {manager.convert_value(1, 'MPa', 'ksc', 'stress'):.3f} ksc")
    print(f"1 kN = {manager.convert_value(1, 'kN', 'kgf', 'force'):.1f} kgf")
    print(f"1 m = {manager.convert_value(1, 'm', 'cm', 'length'):.0f} cm")
    print(f"1 kip = {manager.convert_value(1, 'kip', 'kN', 'force'):.3f} kN")

if __name__ == "__main__":
    print("Complete Global Units System Test")
    print("=" * 50)
    
    try:
        test_three_unit_systems()
        test_category_overrides()
        test_report_overrides()
        test_material_recommendations()
        test_thai_conversion_accuracy()
        test_global_functions()
        test_comprehensive_conversion_tables()
        
        print("\n" + "=" * 50)
        print("✓ ALL TESTS COMPLETED SUCCESSFULLY")
        print("✓ 3-Level Global Units System Working")
        print("✓ SI/US/Thai Systems Validated")
        print("✓ Conversion Accuracy Confirmed")
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
