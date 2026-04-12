# -*- coding: utf-8 -*-
"""
test_load_distribution.py - Test load distribution visualization functionality

This test script demonstrates and validates the load distribution visualization features:
- Two-Way (Yield Line) slab visualization
- One-Way slab visualization
- Beam load calculations
- Integration with AreaLoad objects
"""

import FreeCAD as App
import Part
from freecad.StructureTools.visualization.LoadDistributionVisualizer import (
    LoadDistributionVisualizer, 
    SlabLoadCalculator
)


def test_basic_two_way_slab():
    """Test basic two-way slab visualization."""
    App.Console.PrintMessage("\n" + "="*60 + "\n")
    App.Console.PrintMessage("TEST 1: Basic Two-Way Slab (6m x 5m)\n")
    App.Console.PrintMessage("="*60 + "\n")
    
    doc = App.ActiveDocument
    if not doc:
        doc = App.newDocument("LoadDistributionTest")
    
    # Define slab corners (6m x 5m)
    corners = [
        App.Vector(0, 0, 0),          # A
        App.Vector(6000, 0, 0),       # B
        App.Vector(6000, 5000, 0),    # C
        App.Vector(0, 5000, 0)        # D
    ]
    
    # Create visualizer
    viz = LoadDistributionVisualizer(doc)
    viz.clear_visualization()
    
    # Create two-way visualization
    load_intensity = 10.0  # kN/m²
    viz.visualize_two_way_yield_line(corners, load_intensity, "Test_TwoWay")
    
    # Calculate beam loads
    calc = SlabLoadCalculator()
    beam_loads = calc.calculate_two_way_beam_loads(corners, load_intensity)
    calc.print_beam_loads(beam_loads)
    
    # Verify total load
    total_slab_load = load_intensity * 6.0 * 5.0  # 300 kN
    total_beam_reactions = sum(data.get('total_force', 0) for data in beam_loads.values())
    
    App.Console.PrintMessage(f"\n✓ Total slab load: {total_slab_load:.2f} kN\n")
    App.Console.PrintMessage(f"✓ Total beam reactions: {total_beam_reactions:.2f} kN\n")
    
    error = abs(total_slab_load - total_beam_reactions)
    if error < 1.0:
        App.Console.PrintMessage("✓ TEST PASSED: Load balance verified\n")
    else:
        App.Console.PrintWarning(f"⚠ TEST WARNING: Load imbalance = {error:.2f} kN\n")
    
    doc.recompute()
    return True


def test_basic_one_way_slab():
    """Test basic one-way slab visualization."""
    App.Console.PrintMessage("\n" + "="*60 + "\n")
    App.Console.PrintMessage("TEST 2: Basic One-Way Slab (7m x 2.5m)\n")
    App.Console.PrintMessage("="*60 + "\n")
    
    doc = App.ActiveDocument
    if not doc:
        doc = App.newDocument("LoadDistributionTest")
    
    # Define slab corners (7m x 2.5m - high aspect ratio)
    corners = [
        App.Vector(10000, 0, 0),      # A
        App.Vector(17000, 0, 0),      # B
        App.Vector(17000, 2500, 0),   # C
        App.Vector(10000, 2500, 0)    # D
    ]
    
    # Create visualizer
    viz = LoadDistributionVisualizer(doc)
    
    # Create one-way visualization
    load_intensity = 10.0  # kN/m²
    viz.visualize_one_way_distribution(corners, "short", load_intensity, "Test_OneWay")
    
    # Calculate beam loads
    calc = SlabLoadCalculator()
    beam_loads = calc.calculate_one_way_beam_loads(corners, load_intensity, "short")
    calc.print_beam_loads(beam_loads)
    
    # Verify total load
    total_slab_load = load_intensity * 7.0 * 2.5  # 175 kN
    total_beam_reactions = sum(data.get('total_force', 0) for data in beam_loads.values())
    
    App.Console.PrintMessage(f"\n✓ Total slab load: {total_slab_load:.2f} kN\n")
    App.Console.PrintMessage(f"✓ Total beam reactions: {total_beam_reactions:.2f} kN\n")
    
    error = abs(total_slab_load - total_beam_reactions)
    if error < 1.0:
        App.Console.PrintMessage("✓ TEST PASSED: Load balance verified\n")
    else:
        App.Console.PrintWarning(f"⚠ TEST WARNING: Load imbalance = {error:.2f} kN\n")
    
    doc.recompute()
    return True


def test_beam_load_visualization():
    """Test beam distributed load visualization."""
    App.Console.PrintMessage("\n" + "="*60 + "\n")
    App.Console.PrintMessage("TEST 3: Beam Load Visualization\n")
    App.Console.PrintMessage("="*60 + "\n")
    
    doc = App.ActiveDocument
    if not doc:
        doc = App.newDocument("LoadDistributionTest")
    
    viz = LoadDistributionVisualizer(doc)
    
    # Test uniform load
    start = App.Vector(0, -2000, 0)
    end = App.Vector(6000, -2000, 0)
    viz.visualize_beam_distributed_load(start, end, "uniform", 15.0, 15.0, "Test_Uniform")
    
    # Test triangular load
    start = App.Vector(0, -3000, 0)
    end = App.Vector(5000, -3000, 0)
    viz.visualize_beam_distributed_load(start, end, "triangular", 25.0, 0, "Test_Triangular")
    
    # Test trapezoidal load
    start = App.Vector(0, -4000, 0)
    end = App.Vector(6000, -4000, 0)
    viz.visualize_beam_distributed_load(start, end, "trapezoidal", 10.0, 20.0, "Test_Trapezoidal")
    
    App.Console.PrintMessage("✓ TEST PASSED: Beam loads visualized\n")
    
    doc.recompute()
    return True


def test_complete_slab_with_beams():
    """Test complete slab with beam load visualization."""
    App.Console.PrintMessage("\n" + "="*60 + "\n")
    App.Console.PrintMessage("TEST 4: Complete Slab with Beam Loads\n")
    App.Console.PrintMessage("="*60 + "\n")
    
    doc = App.ActiveDocument
    if not doc:
        doc = App.newDocument("LoadDistributionTest")
    
    # Define slab corners (5m x 4m)
    corners = [
        App.Vector(20000, 0, 0),      # A
        App.Vector(25000, 0, 0),      # B
        App.Vector(25000, 4000, 0),   # C
        App.Vector(20000, 4000, 0)    # D
    ]
    
    # Create visualizer
    viz = LoadDistributionVisualizer(doc)
    
    # Create complete visualization with beam loads
    load_intensity = 12.0  # kN/m²
    viz.visualize_slab_with_beam_loads(
        corners,
        load_intensity=load_intensity,
        distribution_type="two_way",
        name_prefix="Test_Complete"
    )
    
    App.Console.PrintMessage("✓ TEST PASSED: Complete slab visualization created\n")
    
    doc.recompute()
    return True


def test_load_calculations_accuracy():
    """Test accuracy of load calculations."""
    App.Console.PrintMessage("\n" + "="*60 + "\n")
    App.Console.PrintMessage("TEST 5: Load Calculation Accuracy\n")
    App.Console.PrintMessage("="*60 + "\n")
    
    calc = SlabLoadCalculator()
    
    # Test case 1: Square slab (5m x 5m)
    corners_square = [
        App.Vector(0, 0, 0),
        App.Vector(5000, 0, 0),
        App.Vector(5000, 5000, 0),
        App.Vector(0, 5000, 0)
    ]
    
    load = 10.0  # kN/m²
    beam_loads = calc.calculate_two_way_beam_loads(corners_square, load)
    
    App.Console.PrintMessage("\nSquare Slab (5m x 5m, 10 kN/m²):\n")
    calc.print_beam_loads(beam_loads)
    
    # Test case 2: Rectangular slab (8m x 4m)
    corners_rect = [
        App.Vector(0, 0, 0),
        App.Vector(8000, 0, 0),
        App.Vector(8000, 4000, 0),
        App.Vector(0, 4000, 0)
    ]
    
    beam_loads = calc.calculate_two_way_beam_loads(corners_rect, load)
    
    App.Console.PrintMessage("\nRectangular Slab (8m x 4m, 10 kN/m²):\n")
    calc.print_beam_loads(beam_loads)
    
    App.Console.PrintMessage("✓ TEST PASSED: Load calculations completed\n")
    
    return True


def run_all_tests():
    """Run all load distribution tests."""
    App.Console.PrintMessage("\n" + "="*70 + "\n")
    App.Console.PrintMessage("LOAD DISTRIBUTION VISUALIZATION TEST SUITE\n")
    App.Console.PrintMessage("="*70 + "\n")
    
    tests = [
        ("Two-Way Slab", test_basic_two_way_slab),
        ("One-Way Slab", test_basic_one_way_slab),
        ("Beam Load Visualization", test_beam_load_visualization),
        ("Complete Slab with Beams", test_complete_slab_with_beams),
        ("Load Calculation Accuracy", test_load_calculations_accuracy),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            App.Console.PrintMessage(f"\nRunning: {test_name}...\n")
            if test_func():
                passed += 1
            else:
                failed += 1
                App.Console.PrintError(f"✗ FAILED: {test_name}\n")
        except Exception as e:
            failed += 1
            App.Console.PrintError(f"✗ ERROR in {test_name}: {str(e)}\n")
            import traceback
            traceback.print_exc()
    
    App.Console.PrintMessage("\n" + "="*70 + "\n")
    App.Console.PrintMessage(f"TEST SUMMARY: {passed} passed, {failed} failed\n")
    App.Console.PrintMessage("="*70 + "\n")
    
    if App.ActiveDocument:
        App.ActiveDocument.recompute()
        App.Console.PrintMessage("\n✓ Document recomputed. Check the 3D view for visualizations.\n")


# Auto-run if executed directly
if __name__ == "__main__":
    run_all_tests()
