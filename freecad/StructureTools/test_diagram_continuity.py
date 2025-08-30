import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from diagram_core import separates_ordinates, generate_coordinates, make_member_diagram_coords

class TestDiagramContinuity(unittest.TestCase):
    def test_separates_ordinates_continuity(self):
        """Test that separates_ordinates maintains continuity"""
        # Test values that cross zero: positive -> negative -> positive
        values = [1.0, 0.5, 0.1, -0.1, -0.5, -1.0, -0.5, 0.1, 0.5, 1.0]
        
        # Should return a single continuous loop
        result = separates_ordinates(values)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], values)
        
    def test_generate_coordinates_continuity(self):
        """Test that generate_coordinates maintains continuity"""
        # Test with a single continuous loop
        ordinates = [[1.0, 0.5, -0.5, -1.0, -0.5, 0.5, 1.0]]
        dist = 1.0
        
        result = generate_coordinates(ordinates, dist)
        
        # Should have one loop
        self.assertEqual(len(result), 1)
        
        # Should have the correct number of points (original + 2 for start/end on x-axis)
        self.assertEqual(len(result[0]), len(ordinates[0]) + 2)
        
        # First point should be on x-axis
        self.assertEqual(result[0][0], (0.0, 0.0))
        
        # Last point should be on x-axis
        self.assertEqual(result[0][-1][1], 0.0)
        
    def test_make_member_diagram_coords_continuity(self):
        """Test that make_member_diagram_coords maintains continuity"""
        values_original = [1.0, 0.5, -0.5, -1.0, -0.5, 0.5, 1.0]
        dist = 1.0
        scale = 2.0
        
        coordinates, values_scaled = make_member_diagram_coords(values_original, dist, scale)
        
        # Should have one continuous loop
        self.assertEqual(len(coordinates), 1)
        
        # Values should be scaled correctly
        expected_scaled = [v * scale for v in values_original]
        self.assertEqual(values_scaled, expected_scaled)

if __name__ == '__main__':
    unittest.main()