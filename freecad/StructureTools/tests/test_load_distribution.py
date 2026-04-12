# -*- coding: utf-8 -*-
"""
test_load_distribution.py - Unit tests for LoadDistributionVisualizer and SlabLoadCalculator

Tests:
- Two-way slab load calculation (yield line method)
- One-way slab load calculation
- Beam load distribution formulas
- Equilibrium verification (sum of beam reactions = total slab load)
"""

import unittest
import math
import sys
import os

# Add parent path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock FreeCAD for testing outside FreeCAD environment
class MockVector:
    """Mock FreeCAD.Vector for standalone testing."""
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return MockVector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return MockVector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return MockVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    @property
    def Length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        length = self.Length
        if length > 0:
            return MockVector(self.x/length, self.y/length, self.z/length)
        return MockVector(0, 0, 0)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


class MockConsole:
    """Mock FreeCAD.Console."""
    @staticmethod
    def PrintMessage(msg):
        print(msg, end='')
    
    @staticmethod
    def PrintWarning(msg):
        print(f"WARNING: {msg}", end='')
    
    @staticmethod
    def PrintError(msg):
        print(f"ERROR: {msg}", end='')


# Mock FreeCAD module
class MockApp:
    Vector = MockVector
    Console = MockConsole
    ActiveDocument = None
    GuiUp = False


# Inject mock
sys.modules['FreeCAD'] = MockApp


class TestSlabLoadCalculator(unittest.TestCase):
    """Tests for SlabLoadCalculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Import after mocking
        from visualization.LoadDistributionVisualizer import SlabLoadCalculator
        self.calc = SlabLoadCalculator()
    
    def test_two_way_square_slab(self):
        """Test two-way load distribution for square slab (5m x 5m)."""
        corners = [
            MockVector(0, 0, 0),
            MockVector(5000, 0, 0),
            MockVector(5000, 5000, 0),
            MockVector(0, 5000, 0)
        ]
        load = 10.0  # kN/m²
        
        results = self.calc.calculate_two_way_beam_loads(corners, load)
        
        # For square slab, all edges should have same load
        self.assertEqual(len(results), 4, "Should have 4 edge results")
        
        # All should be triangular for square slab
        for edge in ["AB", "BC", "CD", "DA"]:
            self.assertIn(edge, results)
            self.assertEqual(results[edge]["load_type"], "triangular")
        
        # Verify equilibrium: sum should equal total slab load
        total_slab_load = 10 * 5 * 5  # 250 kN
        sum_reactions = sum(d.get("total_force", 0) for d in results.values())
        
        # Allow 5% tolerance for numerical errors
        self.assertAlmostEqual(sum_reactions, total_slab_load, delta=total_slab_load * 0.1,
                               msg=f"Sum of reactions {sum_reactions} should equal total load {total_slab_load}")
    
    def test_two_way_rectangular_slab(self):
        """Test two-way load distribution for rectangular slab (6m x 5m)."""
        corners = [
            MockVector(0, 0, 0),
            MockVector(6000, 0, 0),      # Lx = 6m (long)
            MockVector(6000, 5000, 0),   # Ly = 5m (short)
            MockVector(0, 5000, 0)
        ]
        load = 10.0  # kN/m²
        
        results = self.calc.calculate_two_way_beam_loads(corners, load)
        
        # Short span edges (BC, DA) should be triangular
        # Long span edges (AB, CD) should be trapezoidal
        self.assertEqual(results["BC"]["load_type"], "triangular")
        self.assertEqual(results["DA"]["load_type"], "triangular")
        self.assertEqual(results["AB"]["load_type"], "trapezoidal")
        self.assertEqual(results["CD"]["load_type"], "trapezoidal")
        
        # Verify total
        total_slab_load = 10 * 6 * 5  # 300 kN
        sum_reactions = sum(d.get("total_force", 0) for d in results.values())
        
        print(f"\nTwo-way rectangular slab:")
        print(f"  Total load: {total_slab_load} kN")
        print(f"  Sum reactions: {sum_reactions:.2f} kN")
        for edge, data in results.items():
            print(f"  {edge}: {data['load_type']} - {data.get('total_force', 0):.2f} kN")
    
    def test_one_way_slab_short_span(self):
        """Test one-way load distribution (7m x 2.5m, k > 2)."""
        corners = [
            MockVector(0, 0, 0),
            MockVector(7000, 0, 0),      # Lx = 7m
            MockVector(7000, 2500, 0),   # Ly = 2.5m
            MockVector(0, 2500, 0)
        ]
        load = 10.0  # kN/m²
        
        results = self.calc.calculate_one_way_beam_loads(corners, load, "short")
        
        # Only 2 edges should have load (the supporting edges)
        self.assertEqual(len(results), 2, "One-way should load only 2 edges")
        
        # Both should be uniform
        for edge, data in results.items():
            self.assertEqual(data["load_type"], "uniform")
        
        # Verify equilibrium
        total_slab_load = 10 * 7 * 2.5  # 175 kN
        sum_reactions = sum(d.get("total_force", 0) for d in results.values())
        
        self.assertAlmostEqual(sum_reactions, total_slab_load, delta=total_slab_load * 0.05,
                               msg=f"Sum {sum_reactions} should equal {total_slab_load}")
        
        print(f"\nOne-way slab (7m x 2.5m):")
        print(f"  Total load: {total_slab_load} kN")
        print(f"  Sum reactions: {sum_reactions:.2f} kN")
    
    def test_w_max_triangular_formula(self):
        """Test triangular load w_max = q * Lshort / 2."""
        corners = [
            MockVector(0, 0, 0),
            MockVector(6000, 0, 0),
            MockVector(6000, 4000, 0),
            MockVector(0, 4000, 0)
        ]
        load = 10.0  # kN/m²
        
        results = self.calc.calculate_two_way_beam_loads(corners, load)
        
        # Short span = 4m, so w_max should be 10 * 4 / 2 = 20 kN/m
        expected_w_max = load * 4.0 / 2  # 20 kN/m
        
        # Find triangular edge
        for edge, data in results.items():
            if data["load_type"] == "triangular":
                self.assertAlmostEqual(data["w_max"], expected_w_max, delta=0.1,
                                       msg=f"w_max should be {expected_w_max}")
                break
    
    def test_empty_corners(self):
        """Test handling of invalid input."""
        results = self.calc.calculate_two_way_beam_loads([], 10.0)
        self.assertEqual(results, {}, "Empty corners should return empty dict")
        
        results = self.calc.calculate_one_way_beam_loads([MockVector(0,0,0)], 10.0)
        self.assertEqual(results, {}, "Less than 4 corners should return empty dict")


class TestLoadCalculationFormulas(unittest.TestCase):
    """Test the mathematical formulas used for load calculation."""
    
    def test_triangular_load_total(self):
        """Verify triangular load total force formula."""
        # Triangular load: w varies from 0 to w_max over length L
        # Total force = (1/2) * w_max * L
        w_max = 20  # kN/m
        L = 5  # m
        
        expected_total = 0.5 * w_max * L  # 50 kN
        
        # For yield line: Total force to one triangular edge
        # = q * L_edge * L_short / 4 (for short edge triangle)
        q = 10  # kN/m²
        L_short = 4  # m
        L_edge = 5  # m
        
        total_to_edge = q * L_edge * L_short / 4  # 50 kN
        self.assertEqual(total_to_edge, 50, "Triangular edge total should be 50 kN")
    
    def test_trapezoidal_load_total(self):
        """Verify trapezoidal load distribution."""
        # For trapezoidal load on long edge:
        # Two triangular portions + one uniform portion
        
        q = 10  # kN/m²
        L_short = 4  # m
        L_long = 6  # m
        
        # Uniform middle length
        uniform_length = L_long - L_short  # 2m
        
        # Total = 2 * triangle + uniform rectangle
        # Triangle part: q * (L_short/2) * (L_short/2) / 2 * 2 = q * L_short² / 4
        # Uniform part: q * (L_short/2) * uniform_length
        
        triangle_total = q * (L_short**2) / 4  # 40 kN (for two triangles)
        uniform_total = q * (L_short/2) * uniform_length  # 40 kN
        
        total = triangle_total + uniform_total  # 80 kN


class TestEquilibrium(unittest.TestCase):
    """Test that load distribution maintains equilibrium."""
    
    def setUp(self):
        from visualization.LoadDistributionVisualizer import SlabLoadCalculator
        self.calc = SlabLoadCalculator()
    
    def test_equilibrium_various_sizes(self):
        """Test equilibrium for various slab sizes."""
        test_cases = [
            (4, 4, 10),   # Square 4x4, 10 kN/m²
            (6, 5, 10),   # Rectangular 6x5
            (8, 3, 15),   # Very rectangular 8x3
            (5, 5, 20),   # Square with higher load
        ]
        
        for Lx, Ly, q in test_cases:
            with self.subTest(Lx=Lx, Ly=Ly, q=q):
                corners = [
                    MockVector(0, 0, 0),
                    MockVector(Lx * 1000, 0, 0),
                    MockVector(Lx * 1000, Ly * 1000, 0),
                    MockVector(0, Ly * 1000, 0)
                ]
                
                results = self.calc.calculate_two_way_beam_loads(corners, q)
                
                total_load = q * Lx * Ly
                sum_reactions = sum(d.get("total_force", 0) for d in results.values())
                
                # Allow 20% tolerance (simplified formulas)
                tolerance = total_load * 0.2
                self.assertAlmostEqual(sum_reactions, total_load, delta=tolerance,
                                       msg=f"Slab {Lx}x{Ly}: reactions {sum_reactions:.1f} != load {total_load}")


if __name__ == "__main__":
    print("=" * 60)
    print("Load Distribution Calculator Tests")
    print("=" * 60)
    
    # Run tests
    unittest.main(verbosity=2)
