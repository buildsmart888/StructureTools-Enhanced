# -*- coding: utf-8 -*-
"""
test_phases_2_4.py - Tests for Phase 2-4 (Solver, Transformation, Load Distribution, Post-Processing)

Tests:
- Phase 2: 6-DOF Solver
- Phase 2: Coordinate transformation
- Phase 3: Load distribution
- Phase 4: Stress calculation and post-processing
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analysis.Solver6DOF import Solver6DOF, DOFMapping, BoundaryCondition
from analysis.CoordinateTransformation import (
    CoordinateTransformer, DrillingDOFHandler, ElementOrientation
)
from analysis.LoadDistribution import (
    LoadDistributor, ThermalLoadCalculator, LoadCombination
)
from analysis.PostProcessing import StressCalculator, StructuralAnalysisResults


class TestDOFMapping:
    """Test DOF mapping functionality."""
    
    def test_add_3dof_node(self):
        """Test adding 3-DOF node (beam)."""
        mapper = DOFMapping()
        mapper.add_node(1, 3)
        
        assert len(mapper.node_to_dofs) == 1
        assert mapper.global_dofs == 3
        assert mapper.node_to_dofs[1] == [0, 1, 2]
    
    def test_add_6dof_node(self):
        """Test adding 6-DOF node (plate)."""
        mapper = DOFMapping()
        mapper.add_node(1, 6)
        
        assert mapper.global_dofs == 6
        assert mapper.node_to_dofs[1] == [0, 1, 2, 3, 4, 5]
    
    def test_mixed_dof_nodes(self):
        """Test mixing 3-DOF and 6-DOF nodes."""
        mapper = DOFMapping()
        mapper.add_node(1, 3)  # Beam node
        mapper.add_node(2, 6)  # Plate node
        
        assert mapper.global_dofs == 9
        assert mapper.node_to_dofs[1] == [0, 1, 2]
        assert mapper.node_to_dofs[2] == [3, 4, 5, 6, 7, 8]
    
    def test_add_element(self):
        """Test adding element to DOF map."""
        mapper = DOFMapping()
        mapper.add_node(1, 3)
        mapper.add_node(2, 3)
        mapper.add_element(1, [1, 2])
        
        elem_dofs = mapper.get_element_dofs(1)
        assert elem_dofs == [0, 1, 2, 3, 4, 5]


class TestBoundaryConditions:
    """Test boundary condition management."""
    
    def test_fixed_support(self):
        """Test fixed support BC."""
        bc = BoundaryCondition(node_id=1, dof=0, value=0.0)
        
        assert bc.node_id == 1
        assert bc.dof == 0
        assert bc.value == 0.0
    
    def test_pinned_support(self):
        """Test pinned support (3 BCs)."""
        bcs = [
            BoundaryCondition(1, 0, 0.0),  # Ux
            BoundaryCondition(1, 1, 0.0),  # Uy
            BoundaryCondition(1, 2, 0.0)   # Uz
        ]
        
        assert len(bcs) == 3


class TestSolver6DOF:
    """Test 6-DOF solver."""
    
    @pytest.fixture
    def simple_beam_system(self):
        """Create simple 2-node beam system."""
        solver = Solver6DOF(sparse=False)
        
        # Add nodes
        solver.add_node(1, 3)  # 3-DOF beam node
        solver.add_node(2, 3)
        
        # Simple beam stiffness (EI/L = 1000 N/mm)
        L = 100  # mm
        K_beam = np.array([
            [12000, 0, 0, -12000, 0, 0],
            [0, 1000, 0, 0, -1000, 0],
            [0, 0, 1000, 0, 0, -1000],
            [-12000, 0, 0, 12000, 0, 0],
            [0, -1000, 0, 0, 1000, 0],
            [0, 0, -1000, 0, 0, 1000]
        ]) / L
        
        solver.add_element(1, [1, 2], K_beam, "Beam")
        
        # Boundary conditions
        solver.add_boundary_condition(BoundaryCondition(1, 0, 0.0))  # Fixed
        solver.add_boundary_condition(BoundaryCondition(1, 1, 0.0))
        solver.add_boundary_condition(BoundaryCondition(1, 2, 0.0))
        
        # Load
        solver.add_load(2, 1, 1000)  # 1000 N vertical
        
        return solver
    
    def test_solver_assembly(self, simple_beam_system):
        """Test system assembly."""
        K, F = simple_beam_system.assemble()
        
        assert K.shape == (6, 6)
        assert F.shape == (6,)
        assert F[4] == 1000  # Load on node 2, Y-DOF
    
    def test_solver_boundary_conditions(self, simple_beam_system):
        """Test BC application."""
        K_bc, F_bc = simple_beam_system.apply_boundary_conditions()
        
        # First 3 DOFs should be constrained
        assert K_bc[0, 0] == 1.0  # Diagonal
        assert K_bc[1, 1] == 1.0
        assert K_bc[2, 2] == 1.0
    
    def test_solver_solution(self, simple_beam_system):
        """Test solving system."""
        U = simple_beam_system.solve()
        
        assert U.shape == (6,)
        assert U[0] == 0.0  # Fixed nodes
        assert U[1] == 0.0
        assert U[2] == 0.0


class TestCoordinateTransformation:
    """Test coordinate transformation."""
    
    @pytest.fixture
    def plate_element(self):
        """Create simple plate element."""
        coords = np.array([
            [0, 0, 0],
            [100, 0, 0],
            [100, 100, 0],
            [0, 100, 0]
        ])
        return CoordinateTransformer(coords)
    
    def test_local_system_computation(self, plate_element):
        """Test local coordinate system."""
        R = plate_element.get_rotation_matrix()
        
        assert R.shape == (3, 3)
        
        # Check orthonormality
        det = np.linalg.det(R)
        assert abs(det - 1.0) < 1e-6
    
    def test_vector_transformation(self, plate_element):
        """Test vector transformation."""
        v_local = np.array([1, 0, 0])  # Along local X
        v_global = plate_element.local_to_global_vector(v_local)
        
        assert len(v_global) == 3
        assert np.linalg.norm(v_global) == pytest.approx(1.0)
    
    def test_element_orientation(self):
        """Test element orientation."""
        normal = np.array([0, 0, 1])
        orient = ElementOrientation(normal)
        
        x, y, z = orient.get_axes()
        
        # Check orthonormality
        assert abs(np.dot(x, y)) < 1e-10
        assert abs(np.dot(y, z)) < 1e-10


class TestLoadDistribution:
    """Test load distribution."""
    
    def test_uniform_load_distribution(self):
        """Test uniform load distribution."""
        pressure = 10.0  # kN/m²
        area = 1000.0    # mm²
        num_nodes = 4
        
        loads = LoadDistributor.uniform_load(pressure, area, num_nodes)
        
        assert len(loads) == 4
        assert sum(loads) == pytest.approx(10.0 * 1000.0)
        assert all(l == loads[0] for l in loads)  # Uniform
    
    def test_linear_x_load(self):
        """Test linear load in X direction."""
        coords = np.array([
            [0, 0, 0],
            [100, 0, 0],
            [100, 100, 0],
            [0, 100, 0]
        ])
        
        loads = LoadDistributor.linear_x_load(10.0, 20.0, 10000, coords)
        
        assert len(loads) == 4
        # Higher pressure on right side
        assert loads[1] > loads[0]
        assert loads[2] > loads[3]
    
    def test_thermal_load_uniform(self):
        """Test uniform thermal load."""
        calc = ThermalLoadCalculator(alpha=1.2e-5, E=210000, nu=0.3, t=10)
        
        results = calc.uniform_temperature_change(50, 10000)
        
        assert results['thermal_strain'] > 0
        assert results['thermal_stress'] > 0
        assert results['total_thermal_force'] > 0
    
    def test_load_combination(self):
        """Test load combination."""
        combo = LoadCombination()
        combo.add_load_case('DL', 'Dead load')
        combo.add_load_case('LL', 'Live load')
        
        combo.add_load_to_case('DL', 1, 2, 1000)
        combo.add_load_to_case('LL', 1, 2, 500)
        
        combo.add_combination('ULS', {'DL': 1.2, 'LL': 1.6})
        
        combined = combo.get_combined_loads('ULS')
        
        assert (1, 2) in combined
        assert combined[(1, 2)] == pytest.approx(1.2 * 1000 + 1.6 * 500)


class TestPostProcessing:
    """Test post-processing and stress calculation."""
    
    @pytest.fixture
    def stress_calculator(self):
        """Create stress calculator."""
        return StressCalculator(E=210000, nu=0.3, t=10)
    
    def test_membrane_stress(self, stress_calculator):
        """Test membrane stress calculation."""
        strains = {'ex': 0.001, 'ey': 0.0005, 'exy': 0.0001}
        
        stresses = stress_calculator.calculate_membrane_stresses(strains)
        
        assert 'sigma_x' in stresses
        assert 'sigma_y' in stresses
        assert 'tau_xy' in stresses
        assert stresses['sigma_x'] > 0
    
    def test_bending_stress(self, stress_calculator):
        """Test bending stress calculation."""
        curvatures = {'kappa_x': 0.01, 'kappa_y': 0.005}
        
        stresses = stress_calculator.calculate_bending_stresses(curvatures)
        
        assert 'M_x' in stresses
        assert 'M_y' in stresses
        assert stresses['M_x'] > 0
    
    def test_principal_stresses(self, stress_calculator):
        """Test principal stress calculation."""
        s1, s2, tau_max = stress_calculator.calculate_principal_stresses(
            sigma_x=100, sigma_y=-50, tau_xy=30
        )
        
        assert s1 >= s2  # Ordered
        assert tau_max > 0
    
    def test_von_mises(self, stress_calculator):
        """Test Von Mises stress."""
        vm = stress_calculator.calculate_von_mises(
            sigma_x=100, sigma_y=50, tau_xy=30
        )
        
        assert vm > 0
        assert vm > abs(100)  # Must exceed max normal stress
    
    def test_results_summary(self):
        """Test structural analysis results."""
        results = StructuralAnalysisResults()
        
        results.global_max_displacement = 5.0
        results.global_max_stress = 150.0
        results.critical_element = 5
        
        # Serviceability check
        check = results.check_serviceability(span=2000, ratio_limit=240)
        
        assert check['actual_ratio'] == 2000 / 5.0
        assert check['status'] == 'OK'
        
        # Strength check
        check = results.check_strength(material_yield=250, safety_factor=1.5)
        
        assert check['allowable_stress'] == 250 / 1.5
        assert check['status'] == 'OK'


class TestIntegration:
    """Integration tests combining multiple components."""
    
    def test_plate_analysis_workflow(self):
        """Test complete plate analysis workflow."""
        # 1. Create solver
        solver = Solver6DOF(sparse=False)
        
        # 2. Add nodes (6-DOF each for plate elements)
        for i in range(1, 5):
            solver.add_node(i, 6)
        
        # 3. Create element stiffness (simplified)
        K_plate = np.eye(24) * 1000
        solver.add_element(1, [1, 2, 3, 4], K_plate, "Quad4")
        
        # 4. Apply boundary conditions
        for dof in range(6):
            solver.add_boundary_condition(BoundaryCondition(1, dof, 0.0))
        
        # 5. Apply loads
        solver.add_load(3, 2, -1000)  # Vertical load
        
        # 6. Solve
        U = solver.solve()
        
        assert U is not None
        assert len(U) == 24
        
        # 7. Post-process
        calc = StressCalculator()
        summary = solver.get_summary()
        
        assert summary['num_nodes'] == 4
        assert summary['num_dofs'] == 24


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
