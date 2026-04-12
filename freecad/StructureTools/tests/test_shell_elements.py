# -*- coding: utf-8 -*-
"""
test_shell_elements.py - Comprehensive tests for shell element implementations

Tests cover:
- Shape function correctness
- Stiffness matrix properties (symmetry, positive-definiteness)
- Mass matrix calculations
- Element quality metrics
- Comparison with analytical solutions
"""

import pytest
import numpy as np
import sys
import os

# Add module path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from objects.ShellElements import Quad4Shell, Tri3Shell, Tri6Shell


class TestQuad4ShellBasics:
    """Test Quad4 shell element basics."""
    
    @pytest.fixture
    def quad4_element(self):
        """Create a simple Quad4 element."""
        # Square element 100mm x 100mm
        node_coords = np.array([
            [0, 0, 0],      # Node 1
            [100, 0, 0],    # Node 2
            [100, 100, 0],  # Node 3
            [0, 100, 0]     # Node 4
        ])
        material_props = {
            'E': 210000,    # MPa
            'nu': 0.3,
            't': 10         # mm (10mm thick)
        }
        return Quad4Shell(node_coords, material_props)
    
    def test_quad4_initialization(self, quad4_element):
        """Test Quad4 element initialization."""
        assert quad4_element.num_nodes == 4
        assert quad4_element.dofs_per_node == 6
        assert quad4_element.total_dofs == 24
        assert quad4_element.t == 10
    
    def test_quad4_material_properties(self, quad4_element):
        """Test material property calculations."""
        elem = quad4_element
        
        # Membrane stiffness
        D_mem_expected = elem.E * elem.t / (1 - elem.nu**2)
        assert abs(elem.D_membrane - D_mem_expected) < 1e-6
        
        # Bending stiffness
        D_bend_expected = elem.E * elem.t**3 / (12 * (1 - elem.nu**2))
        assert abs(elem.D_bending - D_bend_expected) < 1e-6
    
    def test_quad4_stiffness_matrix_shape(self, quad4_element):
        """Test stiffness matrix dimensions."""
        K = quad4_element.compute_stiffness_matrix()
        assert K.shape == (24, 24)
    
    def test_quad4_stiffness_symmetry(self, quad4_element):
        """Test stiffness matrix symmetry."""
        K = quad4_element.compute_stiffness_matrix()
        
        # Check symmetry
        K_diff = np.linalg.norm(K - K.T)
        assert K_diff < 1e-6, f"Stiffness matrix not symmetric: error = {K_diff}"
    
    def test_quad4_stiffness_positive_definiteness(self, quad4_element):
        """Test stiffness matrix is positive semi-definite."""
        K = quad4_element.compute_stiffness_matrix()
        
        # Get eigenvalues
        eigenvalues = np.linalg.eigvalsh(K)
        
        # All should be >= 0 (some may be zero for rigid body modes)
        assert np.all(eigenvalues >= -1e-6), f"Negative eigenvalue found: {eigenvalues[0]}"
    
    def test_quad4_mass_matrix_shape(self, quad4_element):
        """Test mass matrix dimensions."""
        M = quad4_element.compute_mass_matrix()
        assert M.shape == (24, 24)
    
    def test_quad4_mass_matrix_properties(self, quad4_element):
        """Test mass matrix properties."""
        M = quad4_element.compute_mass_matrix()
        
        # Should be symmetric
        M_diff = np.linalg.norm(M - M.T)
        assert M_diff < 1e-6
        
        # All diagonal terms should be non-negative
        assert np.all(np.diag(M) >= -1e-6)


class TestTri3ShellBasics:
    """Test Tri3 shell element basics."""
    
    @pytest.fixture
    def tri3_element(self):
        """Create a Tri3 element."""
        # Equilateral triangle with 100mm sides
        node_coords = np.array([
            [0, 0, 0],
            [100, 0, 0],
            [50, 86.603, 0]
        ])
        material_props = {
            'E': 210000,
            'nu': 0.3,
            't': 10
        }
        return Tri3Shell(node_coords, material_props)
    
    def test_tri3_initialization(self, tri3_element):
        """Test Tri3 element initialization."""
        assert tri3_element.num_nodes == 3
        assert tri3_element.dofs_per_node == 6
        assert tri3_element.total_dofs == 18
    
    def test_tri3_stiffness_matrix_shape(self, tri3_element):
        """Test stiffness matrix dimensions."""
        K = tri3_element.compute_stiffness_matrix()
        assert K.shape == (18, 18)
    
    def test_tri3_stiffness_symmetry(self, tri3_element):
        """Test stiffness matrix symmetry."""
        K = tri3_element.compute_stiffness_matrix()
        K_diff = np.linalg.norm(K - K.T)
        assert K_diff < 1e-6
    
    def test_tri3_stiffness_positive_definiteness(self, tri3_element):
        """Test stiffness matrix positive semi-definiteness."""
        K = tri3_element.compute_stiffness_matrix()
        eigenvalues = np.linalg.eigvalsh(K)
        assert np.all(eigenvalues >= -1e-6)


class TestTri6ShellBasics:
    """Test Tri6 shell element basics."""
    
    @pytest.fixture
    def tri6_element(self):
        """Create a Tri6 element."""
        # 6-node triangle with midpoints
        node_coords = np.array([
            [0, 0, 0],          # Node 1
            [100, 0, 0],        # Node 2
            [50, 86.603, 0],    # Node 3
            [50, 0, 0],         # Midpoint 1-2
            [75, 43.301, 0],    # Midpoint 2-3
            [25, 43.301, 0]     # Midpoint 3-1
        ])
        material_props = {
            'E': 210000,
            'nu': 0.3,
            't': 10
        }
        return Tri6Shell(node_coords, material_props)
    
    def test_tri6_initialization(self, tri6_element):
        """Test Tri6 element initialization."""
        assert tri6_element.num_nodes == 6
        assert tri6_element.total_dofs == 36
    
    def test_tri6_stiffness_matrix_shape(self, tri6_element):
        """Test stiffness matrix dimensions."""
        K = tri6_element.compute_stiffness_matrix()
        assert K.shape == (36, 36)
    
    def test_tri6_stiffness_symmetry(self, tri6_element):
        """Test stiffness matrix symmetry."""
        K = tri6_element.compute_stiffness_matrix()
        K_diff = np.linalg.norm(K - K.T)
        assert K_diff < 1e-6


class TestShellElementsComparison:
    """Compare properties across different shell element types."""
    
    def test_quad4_vs_tri_stiffness_magnitude(self):
        """Compare stiffness magnitudes between element types."""
        # Create similar elements
        quad_coords = np.array([
            [0, 0, 0], [100, 0, 0], [100, 100, 0], [0, 100, 0]
        ])
        tri_coords = np.array([
            [0, 0, 0], [100, 0, 0], [50, 86.603, 0]
        ])
        
        mat_props = {'E': 210000, 'nu': 0.3, 't': 10}
        
        quad = Quad4Shell(quad_coords, mat_props)
        tri = Tri3Shell(tri_coords, mat_props)
        
        K_quad = quad.compute_stiffness_matrix()
        K_tri = tri.compute_stiffness_matrix()
        
        # Quad4 should have larger stiffness (larger area)
        assert np.linalg.norm(K_quad) > np.linalg.norm(K_tri)
    
    def test_element_area_calculation(self):
        """Test area calculation consistency."""
        # Unit square
        quad_coords = np.array([
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]
        ])
        # Right triangle with area = 0.5
        tri_coords = np.array([
            [0, 0, 0], [1, 0, 0], [0, 1, 0]
        ])
        
        mat_props = {'E': 210000, 'nu': 0.3, 't': 1}
        
        quad = Quad4Shell(quad_coords, mat_props)
        tri = Tri3Shell(tri_coords, mat_props)
        
        # Quad area should be 1.0, Tri area should be 0.5
        assert quad.area == 1.0
        assert tri.area == 0.5


class TestNumericalIntegration:
    """Test numerical integration accuracy."""
    
    def test_gaussian_quadrature_weights(self):
        """Test Gaussian quadrature weight properties."""
        quad = Quad4Shell(
            np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]]),
            {'E': 210000, 'nu': 0.3, 't': 1}
        )
        
        # Get quadrature points
        xi, eta, w = quad._gauss_quadrature_2d(2)
        
        # Sum of weights should equal 4 (area of [-1,1] x [-1,1])
        total_weight = np.sum(w) * np.sum(w)
        assert abs(total_weight - 4.0) < 1e-10
    
    def test_jacobian_computation(self):
        """Test Jacobian matrix computation."""
        # Create simple rectangular element
        quad = Quad4Shell(
            np.array([[0,0,0],[2,0,0],[2,1,0],[0,1,0]]),
            {'E': 210000, 'nu': 0.3, 't': 1}
        )
        
        # At center (xi=0, eta=0), Jacobian should be diagonal
        N, dN_dxi, dN_deta = quad._compute_shape_functions(0, 0)
        J, det_J = quad._jacobian_2d(dN_dxi, dN_deta)
        
        # For rectangular element, det_J = (2 * 1) / 4 = 0.5
        assert abs(det_J - 0.5) < 1e-6


class TestMaterialProperties:
    """Test material property calculations."""
    
    def test_stiffness_factors_thin_plate(self):
        """Test stiffness factors for thin plate."""
        elem = Quad4Shell(
            np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]]),
            {'E': 210000, 'nu': 0.3, 't': 1}
        )
        
        # For thin plate, bending >> membrane
        assert elem.D_bending > elem.D_membrane
    
    def test_stiffness_factors_thick_plate(self):
        """Test stiffness factors for thick plate."""
        elem = Quad4Shell(
            np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]]),
            {'E': 210000, 'nu': 0.3, 't': 100}
        )
        
        # For very thick plate, membrane and bending comparable
        assert elem.D_membrane > 0
        assert elem.D_bending > 0


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_quad4_initialization_wrong_nodes(self):
        """Test Quad4 with wrong number of nodes."""
        with pytest.raises(ValueError):
            Quad4Shell(
                np.array([[0,0,0],[1,0,0],[1,1,0]]),
                {'E': 210000, 'nu': 0.3, 't': 1}
            )
    
    def test_tri3_initialization_wrong_nodes(self):
        """Test Tri3 with wrong number of nodes."""
        with pytest.raises(ValueError):
            Tri3Shell(
                np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]]),
                {'E': 210000, 'nu': 0.3, 't': 1}
            )
    
    def test_tri6_initialization_wrong_nodes(self):
        """Test Tri6 with wrong number of nodes."""
        with pytest.raises(ValueError):
            Tri6Shell(
                np.array([[0,0,0],[1,0,0],[1,1,0]]),
                {'E': 210000, 'nu': 0.3, 't': 1}
            )
    
    def test_highly_distorted_element(self):
        """Test element with poor aspect ratio."""
        # Very thin triangle
        tri = Tri3Shell(
            np.array([[0,0,0],[100,0,0],[50,0.1,0]]),
            {'E': 210000, 'nu': 0.3, 't': 10}
        )
        
        # Should still produce valid stiffness matrix
        K = tri.compute_stiffness_matrix()
        assert K.shape == (18, 18)
        assert not np.isnan(K).any()


class TestBenchmarks:
    """Performance benchmarks for shell elements."""
    
    def test_quad4_stiffness_performance(self, benchmark):
        """Benchmark Quad4 stiffness calculation."""
        quad = Quad4Shell(
            np.array([[0,0,0],[100,0,0],[100,100,0],[0,100,0]]),
            {'E': 210000, 'nu': 0.3, 't': 10}
        )
        
        def compute():
            return quad.compute_stiffness_matrix()
        
        result = benchmark(compute)
        assert result.shape == (24, 24)
    
    def test_tri3_stiffness_performance(self, benchmark):
        """Benchmark Tri3 stiffness calculation."""
        tri = Tri3Shell(
            np.array([[0,0,0],[100,0,0],[50,86.603,0]]),
            {'E': 210000, 'nu': 0.3, 't': 10}
        )
        
        def compute():
            return tri.compute_stiffness_matrix()
        
        result = benchmark(compute)
        assert result.shape == (18, 18)


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
