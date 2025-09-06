"""
Unit tests for Buckling Analysis
"""
import sys
import os
import numpy as np

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, project_root)

import pytest
from unittest.mock import Mock, patch, MagicMock

# Mock FreeCAD before importing
class MockConsole:
    @staticmethod
    def PrintMessage(msg): pass
    @staticmethod 
    def PrintWarning(msg): pass
    @staticmethod
    def PrintError(msg): pass

class MockApp:
    Console = MockConsole()
    Vector = lambda x=0,y=0,z=0: (x,y,z)

sys.modules['FreeCAD'] = MockApp

from freecad.StructureTools.analysis.BucklingAnalysis import BucklingAnalysis, BucklingAnalysisResults


class TestBucklingAnalysis:
    """Test the BucklingAnalysis class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        # Create mock structural model
        self.mock_model = Mock()
        self.mock_model.Nodes = {
            'N1': Mock(X=0, Y=0, Z=0),
            'N2': Mock(X=5000, Y=0, Z=0),  # 5m span
            'N3': Mock(X=0, Y=0, Z=3000)   # 3m height
        }
        
        # Mock members
        mock_member = Mock()
        mock_member.i_node = self.mock_model.Nodes['N1']
        mock_member.j_node = self.mock_model.Nodes['N2']
        mock_member.A = 5000  # mm²
        mock_member.Iz = 50e6  # mm⁴
        mock_member.E = 200000  # MPa
        mock_member.L = 5000   # mm
        
        self.mock_model.Members = {'M1': mock_member}
        
        # Create buckling analysis instance
        self.buckling_analysis = BucklingAnalysis(self.mock_model)
    
    def test_analysis_initialization(self):
        """Test proper initialization of buckling analysis"""
        assert self.buckling_analysis.model == self.mock_model
        assert self.buckling_analysis.num_modes == 5
        assert self.buckling_analysis.max_iterations == 1000
        assert self.buckling_analysis.convergence_tolerance == 1e-8
    
    def test_parameter_validation(self):
        """Test validation of analysis parameters"""
        # Test setting parameters
        self.buckling_analysis.set_analysis_parameters(num_modes=10)
        assert self.buckling_analysis.num_modes == 10
        
        # Test parameter validation
        self.buckling_analysis.set_analysis_parameters(
            num_modes=3,
            tolerance=1e-6,
            method="Lanczos"
        )
        assert self.buckling_analysis.num_modes == 3
        assert self.buckling_analysis.convergence_tolerance == 1e-6
        assert self.buckling_analysis.analysis_method == "Lanczos"
    
    @patch('freecad.StructureTools.analysis.BucklingAnalysis.scipy')
    def test_matrix_assembly(self, mock_scipy):
        """Test stiffness matrix assembly"""
        # Test elastic stiffness matrix
        K_elastic = self.buckling_analysis._build_elastic_stiffness_matrix()
        assert K_elastic is not None
        assert K_elastic.shape == (self.mock_model.num_dofs, self.mock_model.num_dofs)
        
        # Test geometric stiffness matrix  
        mock_load_combo = Mock()
        mock_load_combo.factors = {'DL': 1.0}
        
        K_geometric = self.buckling_analysis._build_geometric_stiffness_matrix(mock_load_combo)
        assert K_geometric is not None
        assert K_geometric.shape == (self.mock_model.num_dofs, self.mock_model.num_dofs)
    
    def test_member_geometric_stiffness(self):
        """Test geometric stiffness matrix for individual member"""
        mock_member = self.mock_model.members['M1']
        mock_axial_force = -50000  # 50 kN compression
        
        kg_member = self.buckling_analysis._calculate_member_geometric_stiffness(
            mock_member, mock_axial_force
        )
        
        # Should be 12x12 matrix for 3D beam element
        assert kg_member.shape == (12, 12)
        
        # Should be symmetric
        assert np.allclose(kg_member, kg_member.T, atol=1e-10)
        
        # Should have expected pattern for beam geometric stiffness
        # Non-zero terms should exist for relevant DOFs
        assert not np.allclose(kg_member, np.zeros((12, 12)))
    
    @patch('scipy.linalg.eigh')
    def test_eigenvalue_problem_solving(self, mock_eigh):
        """Test eigenvalue problem solution"""
        # Mock eigenvalue results
        mock_eigenvalues = np.array([2.5, 4.2, 6.8, 9.1, 12.3])
        mock_eigenvectors = np.random.rand(12, 5)  # 12 DOFs, 5 modes
        mock_eigh.return_value = (mock_eigenvalues, mock_eigenvectors)
        
        # Create mock matrices
        K_elastic = np.eye(12) * 1000
        K_geometric = np.eye(12) * -1
        
        eigenvalues, eigenvectors = self.buckling_analysis._solve_buckling_eigenvalue_problem(
            K_elastic, K_geometric
        )
        
        # Should return the mocked values
        np.testing.assert_array_equal(eigenvalues, mock_eigenvalues)
        np.testing.assert_array_equal(eigenvectors, mock_eigenvectors)
        
        # scipy.linalg.eigh should have been called
        mock_eigh.assert_called_once()
    
    def test_critical_load_factor_calculation(self):
        """Test critical load factor extraction"""
        mock_eigenvalues = np.array([2.5, 4.2, 6.8, 9.1, 12.3])
        
        # Extract critical load factors
        load_factors = self.buckling_analysis._extract_critical_load_factors(mock_eigenvalues)
        
        # Should match eigenvalues for linear buckling
        np.testing.assert_array_equal(load_factors, mock_eigenvalues)
        
        # Should be sorted in ascending order
        assert np.all(load_factors[:-1] <= load_factors[1:])
    
    def test_buckling_mode_classification(self):
        """Test classification of buckling modes"""
        mock_eigenvector = np.zeros(12)
        # Simulate lateral-torsional buckling pattern
        mock_eigenvector[1] = 0.8   # Lateral displacement
        mock_eigenvector[5] = 0.6   # Torsional rotation
        mock_eigenvector[7] = -0.8  # Lateral displacement at other end
        mock_eigenvector[11] = -0.6 # Torsional rotation at other end
        
        mode_type = self.buckling_analysis._classify_buckling_mode(mock_eigenvector)
        
        # Should identify as lateral-torsional buckling
        assert 'lateral' in mode_type.lower()
    
    def test_safety_factor_calculation(self):
        """Test safety factor calculations"""
        critical_load_factors = np.array([2.5, 4.2, 6.8, 9.1, 12.3])
        
        # Calculate safety factors with default factor (2.0)
        safety_factors = self.buckling_analysis._calculate_safety_factors(critical_load_factors)
        
        expected_factors = critical_load_factors / 2.0
        np.testing.assert_array_equal(safety_factors, expected_factors)
        
        # Test with custom safety factor
        custom_safety_factors = self.buckling_analysis._calculate_safety_factors(
            critical_load_factors, safety_factor=2.5
        )
        
        expected_custom = critical_load_factors / 2.5
        np.testing.assert_array_equal(custom_safety_factors, expected_custom)
    
    @patch('freecad.StructureTools.analysis.BucklingAnalysis.scipy')
    def test_full_buckling_analysis_run(self, mock_scipy):
        """Test complete buckling analysis execution"""
        # Mock eigenvalue solution
        mock_eigenvalues = np.array([2.5, 4.2, 6.8, 9.1, 12.3])
        mock_eigenvectors = np.random.rand(12, 5)
        mock_scipy.linalg.eigh.return_value = (mock_eigenvalues, mock_eigenvectors)
        
        # Create mock load combination
        mock_load_combo = Mock()
        mock_load_combo.factors = {'DL': 1.2, 'LL': 1.6}
        mock_load_combo.name = "1.2DL + 1.6LL"
        
        # Run analysis
        results = self.buckling_analysis.run_buckling_analysis(mock_load_combo)
        
        # Check results type
        assert isinstance(results, BucklingAnalysisResults)
        
        # Check that results contain expected data
        assert hasattr(results, 'critical_load_factors')
        assert hasattr(results, 'buckling_modes')
        assert hasattr(results, 'safety_factors')
        
        # Check that critical load factors match eigenvalues
        np.testing.assert_array_equal(results.critical_load_factors, mock_eigenvalues)
        
        # Check that buckling modes match eigenvectors
        np.testing.assert_array_equal(results.buckling_modes, mock_eigenvectors)
    
    def test_boundary_condition_handling(self):
        """Test handling of boundary conditions in buckling analysis"""
        # Add boundary conditions to mock model
        self.mock_model.nodes['N1'].support_DX = True
        self.mock_model.nodes['N1'].support_DY = True  
        self.mock_model.nodes['N1'].support_DZ = True
        self.mock_model.nodes['N1'].support_RX = True
        self.mock_model.nodes['N1'].support_RY = True
        self.mock_model.nodes['N1'].support_RZ = True
        
        # Get constrained DOFs
        constrained_dofs = self.buckling_analysis._get_constrained_dofs()
        
        # Should identify the 6 constrained DOFs at node N1
        assert len(constrained_dofs) == 6
        assert all(dof < 6 for dof in constrained_dofs)  # First 6 DOFs
    
    def test_error_handling(self):
        """Test error handling for various failure modes"""
        # Test with invalid model
        with pytest.raises(ValueError):
            BucklingAnalysis(None)
        
        # Test with empty model
        empty_model = Mock()
        empty_model.members = {}
        empty_model.nodes = {}
        
        with pytest.raises(ValueError, match="No structural members found"):
            BucklingAnalysis(empty_model)


class TestBucklingAnalysisResults:
    """Test the BucklingAnalysisResults class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.critical_load_factors = np.array([2.5, 4.2, 6.8, 9.1, 12.3])
        self.buckling_modes = np.random.rand(12, 5)
        self.load_combination = Mock()
        self.load_combination.name = "1.2DL + 1.6LL"
        
        self.results = BucklingAnalysisResults(
            load_factors=self.critical_load_factors,
            buckling_modes=self.buckling_modes,
            applied_loads={'DL': 1.2, 'LL': 1.6},
            critical_loads=[{'mode': i+1, 'factor': self.critical_load_factors[i]} 
                           for i in range(len(self.critical_load_factors))]
        )
    
    def test_results_initialization(self):
        """Test proper initialization of results object"""
        assert hasattr(self.results, 'load_factors')
        assert hasattr(self.results, 'buckling_modes') 
        assert hasattr(self.results, 'applied_loads')
        assert hasattr(self.results, 'safety_factors')
        assert hasattr(self.results, 'mode_classifications')
        
        # Check data integrity
        np.testing.assert_array_equal(self.results.load_factors, self.critical_load_factors)
        np.testing.assert_array_equal(self.results.buckling_modes, self.buckling_modes)
    
    def test_get_critical_mode(self):
        """Test retrieval of critical buckling mode"""
        critical_mode_idx, critical_load_factor = self.results.get_critical_mode()
        
        # Should return first mode (lowest load factor)
        assert critical_mode_idx == 0
        assert critical_load_factor == self.critical_load_factors[0]
    
    def test_get_mode_data(self):
        """Test retrieval of specific mode data"""
        mode_data = self.results.get_mode_data(1)  # Second mode
        
        assert 'load_factor' in mode_data
        assert 'mode_shape' in mode_data
        assert 'classification' in mode_data
        assert 'safety_factor' in mode_data
        
        # Check values
        assert mode_data['load_factor'] == self.critical_load_factors[1]
        np.testing.assert_array_equal(mode_data['mode_shape'], self.buckling_modes[:, 1])
    
    def test_results_summary(self):
        """Test generation of results summary"""
        summary = self.results.get_summary()
        
        # Should contain key information
        assert 'critical_load_factor' in summary
        assert 'load_combination' in summary
        assert 'num_modes' in summary
        assert 'minimum_safety_factor' in summary
        
        # Check values
        assert summary['critical_load_factor'] == self.critical_load_factors[0]
        assert summary['num_modes'] == len(self.critical_load_factors)
    
    def test_export_functionality(self):
        """Test results export capabilities"""
        # Test CSV export
        csv_data = self.results.export_to_csv()
        assert isinstance(csv_data, str)
        assert 'Load Factor' in csv_data
        assert 'Safety Factor' in csv_data
        
        # Test JSON export
        json_data = self.results.export_to_json()
        assert isinstance(json_data, str)
        
        import json
        parsed_data = json.loads(json_data)
        assert 'critical_load_factors' in parsed_data
        assert 'load_combination' in parsed_data


class TestBucklingAnalysisIntegration:
    """Test integration aspects of buckling analysis"""
    
    def setup_method(self):
        """Setup integration test fixtures"""
        self.mock_calc_object = Mock()
        self.mock_calc_object.ListElements = []
        
        # Add mock structural elements
        mock_beam = Mock()
        mock_beam.Type = "StructuralBeam"
        mock_beam.StartNode = Mock(Position=(0, 0, 0))
        mock_beam.EndNode = Mock(Position=(5000, 0, 0))
        self.mock_calc_object.ListElements.append(mock_beam)
    
    def test_calc_object_integration(self):
        """Test integration with calc.py calculation object"""
        # Should be able to extract structural model from calc object
        buckling_analysis = BucklingAnalysis.from_calc_object(self.mock_calc_object)
        
        assert buckling_analysis is not None
        assert hasattr(buckling_analysis, 'structural_model')
    
    def test_load_combination_integration(self):
        """Test integration with load combination system"""
        # Create load combination from calc object
        load_combos = self.mock_calc_object.get_load_combinations()
        
        # Should be able to use for buckling analysis
        if load_combos:
            combo = load_combos[0]
            assert hasattr(combo, 'factors')
            assert hasattr(combo, 'name')
    
    def test_results_storage_integration(self):
        """Test storage of results in calc object"""
        # Mock results
        mock_results = Mock()
        mock_results.critical_load_factors = np.array([2.5, 4.2])
        
        # Store in calc object
        self.mock_calc_object.buckling_results = mock_results
        
        # Should be retrievable
        stored_results = getattr(self.mock_calc_object, 'buckling_results', None)
        assert stored_results is not None
        assert hasattr(stored_results, 'critical_load_factors')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])