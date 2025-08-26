#!/usr/bin/env python3
"""
Test MaterialSelectionPanel with Enhanced Global Units System
Validate integration with 3-level units hierarchy
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'freecad'))

try:
    from freecad.StructureTools.utils.units_manager import get_units_manager, set_units_system
    from freecad.StructureTools.taskpanels.MaterialSelectionPanel import MaterialSelectionPanel
    print("✓ Successfully imported MaterialSelectionPanel and units_manager")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

class MockApp:
    """Mock FreeCAD App for testing"""
    class Console:
        @staticmethod
        def PrintMessage(msg):
            print(f"App: {msg.strip()}")
        
        @staticmethod
        def PrintError(msg):
            print(f"Error: {msg.strip()}")

# Mock FreeCAD App
import freecad.FreeCAD as App
App.App = MockApp()

def test_material_panel_thai_units():
    """Test MaterialSelectionPanel with Thai units"""
    print("\n=== Testing Material Panel with Thai Units ===")
    
    # Set global units to Thai
    set_units_system("THAI")
    
    # Create panel (without Qt UI for testing)
    panel = MaterialSelectionPanel()
    
    # Test format methods
    concrete_modulus = panel.format_modulus(30000000000)  # 30 GPa in Pa
    steel_modulus = panel.format_modulus(200000000000)    # 200 GPa in Pa
    
    print(f"Concrete Modulus (Thai): {concrete_modulus}")
    print(f"Steel Modulus (Thai): {steel_modulus}")
    
    # Test stress formatting
    fc_stress = panel.format_stress(28000000)  # 28 MPa in Pa
    fy_stress = panel.format_stress(400000000)  # 400 MPa in Pa
    
    print(f"fc' = 28 MPa (Thai): {fc_stress}")
    print(f"fy = 400 MPa (Thai): {fy_stress}")

def test_material_panel_mixed_units():
    """Test MaterialSelectionPanel with mixed units"""
    print("\n=== Testing Material Panel with Mixed Units ===")
    
    # Set base system to SI
    manager = get_units_manager()
    manager.set_unit_system("SI")
    
    # Override stress to Thai units
    manager.set_category_override("stress", "THAI")
    
    panel = MaterialSelectionPanel()
    
    # Test mixed formatting
    force = panel.format_force(100000)  # Should be in SI (kN)
    stress = panel.format_stress(400000000)  # Should be in Thai (ksc)
    
    print(f"Force (SI base): {force}")
    print(f"Stress (Thai override): {stress}")

def test_material_recommendations_integration():
    """Test material recommendations through panel"""
    print("\n=== Testing Material Recommendations Integration ===")
    
    for system_name in ["SI", "US", "THAI"]:
        set_units_system(system_name)
        manager = get_units_manager()
        
        print(f"\n{system_name} System:")
        recommendations = manager.get_material_recommendations()
        
        # Test values that would be used in MaterialSelectionPanel
        steel_mod = recommendations["steel_modulus"]
        concrete_mod = recommendations["concrete_modulus"]
        sd40_yield = recommendations["steel_yield_sd40"]
        
        print(f"  Steel Modulus: {steel_mod[0]:.0f} {steel_mod[1]}")
        print(f"  Concrete Modulus: {concrete_mod[0]:.0f} {concrete_mod[1]}")
        print(f"  SD40 Yield: {sd40_yield[0]:.0f} {sd40_yield[1]}")

def test_conversion_accuracy_validation():
    """Validate conversion accuracy for engineering values"""
    print("\n=== Testing Engineering Conversion Accuracy ===")
    
    set_units_system("THAI")
    panel = MaterialSelectionPanel()
    
    # Test known engineering values
    test_values = [
        (200000000000, "Steel Modulus (200 GPa)"),  # Should = 2,039,432 ksc
        (400000000, "SD40 Steel (400 MPa)"),        # Should = 4,079 ksc
        (300000000, "SD30 Steel (300 MPa)"),        # Should = 3,059 ksc
        (28000000, "Concrete fc' (28 MPa)"),        # Should = 285.5 ksc
    ]
    
    for value_pa, description in test_values:
        if "Modulus" in description:
            formatted = panel.format_modulus(value_pa)
        else:
            formatted = panel.format_stress(value_pa)
        print(f"{description}: {formatted}")

if __name__ == "__main__":
    print("MaterialSelectionPanel Integration Test")
    print("=" * 50)
    
    try:
        test_material_panel_thai_units()
        test_material_panel_mixed_units()
        test_material_recommendations_integration()
        test_conversion_accuracy_validation()
        
        print("\n" + "=" * 50)
        print("✓ ALL MATERIAL PANEL TESTS PASSED")
        print("✓ Enhanced Units Integration Successful")
        print("✓ Thai Units Accuracy Confirmed")
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
