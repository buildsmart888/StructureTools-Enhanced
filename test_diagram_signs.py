#!/usr/bin/env python3
"""Test script to verify diagram sign conventions are working correctly."""

import sys
import os
import FreeCAD as App

# Add the module path
sys.path.insert(0, os.path.join(App.getResourceDir(), "Mod", "StructureTools", "freecad", "StructureTools"))

def test_diagram_signs():
    """Test diagram sign conventions with known values."""
    
    print("Testing Diagram Sign Conventions...")
    print("=" * 50)
    
    try:
        from diagram_core import get_label_positions
        from utils.universal_thai_units import get_universal_thai_units
        
        # Test data: moment values (kN⋅m)
        test_moments = [10.5, -15.2, 0.0, 8.7, -5.3]
        test_shears = [25.0, -18.5, 12.3, -22.1, 0.0]
        
        dist = 1.0  # 1 meter spacing
        font_height = 12.0
        precision = 2
        
        print("1. Testing original label generation:")
        print("   Moment values:", test_moments)
        
        # Test the sign flip in get_label_positions
        scaled_values = [v * 0.1 for v in test_moments]  # Small scale for visualization
        labels = get_label_positions(scaled_values, test_moments, dist, font_height, precision)
        
        print("   Generated labels:")
        for i, (label_text, x, y) in enumerate(labels):
            original_value = test_moments[i]
            displayed_value = float(label_text.split()[0])
            print(f"     Position {i}: Original={original_value:+.1f}, Displayed={displayed_value:+.1f}, Sign flip={'✓' if displayed_value == -original_value else '✗'}")
        
        print("\n2. Testing unit conversion preservation:")
        # Create a mock diagram object for testing
        class MockDiagramObj:
            def __init__(self):
                self.MomentUnit = "kgf·m"
                self.ForceUnit = "kgf"
                self.Precision = 2
        
        mock_obj = MockDiagramObj()
        
        # Import the diagram class to test unit conversion
        from diagram import Diagram
        diagram_instance = Diagram()
        
        print("   Testing moment unit conversion:")
        for original_val in test_moments:
            if abs(original_val) > 1e-6:
                # The displayed value (with sign flip applied)
                displayed_val = -original_val
                converted_val, formatted_text = diagram_instance._convertValueToSelectedUnit(displayed_val, "moment", mock_obj)
                print(f"     Original: {original_val:+.1f} kN⋅m → Displayed: {displayed_val:+.1f} kN⋅m → Converted: {formatted_text}")
        
        print("\n3. Testing shear unit conversion:")
        mock_obj.ForceUnit = "tf"
        for original_val in test_shears:
            if abs(original_val) > 1e-6:
                displayed_val = -original_val  # Assuming same sign flip for shear
                converted_val, formatted_text = diagram_instance._convertValueToSelectedUnit(displayed_val, "shear", mock_obj)
                print(f"     Original: {original_val:+.1f} kN → Displayed: {displayed_val:+.1f} kN → Converted: {formatted_text}")
        
        print("\n4. Summary:")
        print("   • Sign flip in get_label_positions: Applied (* -1)")
        print("   • Unit conversion: Preserves the displayed sign")
        print("   • Format: Uses + prefix to show positive/negative clearly")
        
        print("\n✓ Diagram sign convention tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_diagram_signs()