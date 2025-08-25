"""
Unit tests for Modal Analysis module
"""
import sys
import os

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, project_root)

import pytest
import numpy as np
from unittest.mock import Mock, patch, MagicMock

# Import the modules to test
from freecad.StructureTools.analysis.ModalAnalysis import (
    ModalAnalysis, 
    ModalAnalysisResults,
    run_modal_analysis_on_calc
)
from freecad.StructureTools.utils.exceptions import AnalysisError


class TestModalAnalysisResults:
    """Test the ModalAnalysisResults class"""
    
    def test_results_initialization(self):
        """Test proper initialization of results"""
        frequencies = np.array([1.5, 3.2, 5.8, 8.1])
        mode_shapes = np.random.rand(100, 4)  # 100 DOFs, 4 modes
        participation_factors = np.random.rand(4, 3)  # 4 modes, 3 directions
        effective_mass = {'X': 0.85, 'Y': 0.78, 'Z': 0.92}
        
        results = ModalAnalysisResults(
            frequencies=frequencies,
            mode_shapes=mode_shapes,
            participation_factors=participation_factors,
            effective_mass=effective_mass
        )
        
        assert results.num_modes == 4
        np.testing.assert_array_equal(results.frequencies, frequencies)
        np.testing.assert_array_equal(results.mode_shapes, mode_shapes)
        np.testing.assert_array_equal(results.participation_factors, participation_factors)
    
    def test_periods_calculation(self):
        """Test period calculation from frequencies"""
        frequencies = np.array([2.0, 4.0, 10.0])
        effective_mass = {'X': 0.85, 'Y': 0.78, 'Z': 0.92}
        results = ModalAnalysisResults(
            frequencies=frequencies,
            mode_shapes=np.random.rand(10, 3),
            participation_factors=np.random.rand(3, 3),
            effective_mass=effective_mass
        )
        
        expected_periods = np.array([0.5, 0.25, 0.1])
        np.testing.assert_array_almost_equal(results.periods, expected_periods, decimal=6)
    
    def test_fundamental_period(self):
        """Test fundamental period calculation"""
        frequencies = np.array([1.5, 3.0, 5.0])
        effective_mass = {'X': 0.85, 'Y': 0.78, 'Z': 0.92}
        results = ModalAnalysisResults(
            frequencies=frequencies,
            mode_shapes=np.random.rand(10, 3),
            participation_factors=np.random.rand(3, 3),
            effective_mass=effective_mass
        )
        
        assert abs(results.get_fundamental_period() - (1/1.5)) < 1e-6
    
    def test_dominant_modes(self):
        """Test dominant mode identification"""
        frequencies = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        # Create participation factors where modes 0, 2, 4 are dominant
        participation_factors = np.array([
            [0.8, 0.1, 0.1],   # Mode 0 - dominant in X
            [0.2, 0.1, 0.1],   # Mode 1 - not dominant
            [0.1, 0.9, 0.1],   # Mode 2 - dominant in Y  
            [0.1, 0.2, 0.1],   # Mode 3 - not dominant
            [0.1, 0.1, 0.8]    # Mode 4 - dominant in Z
        ])
        
        effective_mass = {'X': 0.85, 'Y': 0.78, 'Z': 0.92}
        results = ModalAnalysisResults(
            frequencies=frequencies,
            mode_shapes=np.random.rand(10, 5),
            participation_factors=participation_factors,
            effective_mass=effective_mass
        )
        
        dominant_modes = results.get_dominant_modes(threshold=0.5)
        expected_dominant = [0, 2, 4]
        
        assert dominant_modes == expected_dominant


class TestModalAnalysis:
    """Test the ModalAnalysis class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        # Create a mock structural model
        self.mock_model = Mock()
        self.mock_model.nodes = {
            'N1': Mock(ID=0, X=0, Y=0, Z=0),
            'N2': Mock(ID=1, X=1, Y=0, Z=0), 
            'N3': Mock(ID=2, X=0, Y=1, Z=0),
            'N4': Mock(ID=3, X=1, Y=1, Z=0)
        }
        self.mock_model.members = {
            'M1': Mock(iNode=self.mock_model.nodes['N1'], jNode=self.mock_model.nodes['N2']),
            'M2': Mock(iNode=self.mock_model.nodes['N2'], jNode=self.mock_model.nodes['N3'])
        }
        
        # Set up DOF mapping
        self.mock_model.num_dofs = 12  # 4 nodes × 3 DOFs each
        
    def test_modal_analysis_initialization(self):
        """Test proper initialization of modal analysis"""
        modal_analysis = ModalAnalysis(self.mock_model)
        
        assert modal_analysis.model == self.mock_model
        assert modal_analysis.num_modes == 10  # default
        assert modal_analysis.frequency_range == (0.1, 100.0)  # default
        assert modal_analysis.solver_type == "subspace_iteration"
        assert modal_analysis.mass_type == "consistent"
    
    def test_settings_validation(self):
        """Test validation of analysis settings"""
        modal_analysis = ModalAnalysis(self.mock_model)
        
        # Test valid settings
        modal_analysis.set_num_modes(15)
        assert modal_analysis.num_modes == 15
        
        modal_analysis.set_frequency_range(0.5, 50.0)
        assert modal_analysis.frequency_range == (0.5, 50.0)
        
        # Test invalid settings
        with pytest.raises(ValueError):
            modal_analysis.set_num_modes(0)
        
        with pytest.raises(ValueError):
            modal_analysis.set_num_modes(1001)
        
        with pytest.raises(ValueError):
            modal_analysis.set_frequency_range(-1.0, 10.0)
        
        with pytest.raises(ValueError):
            modal_analysis.set_frequency_range(10.0, 5.0)
    
    @patch('scipy.linalg.eigh')
    def test_eigenvalue_solution(self, mock_eigh):
        """Test eigenvalue problem solving"""
        # Mock eigenvalue solution
        mock_eigenvals = np.array([10.0, 25.0, 40.0, 60.0])  # ω²
        mock_eigenvecs = np.eye(4)  # Identity matrix for simplicity
        mock_eigh.return_value = (mock_eigenvals, mock_eigenvecs)
        
        modal_analysis = ModalAnalysis(self.mock_model)
        modal_analysis.num_modes = 4
        
        # Mock matrix building methods
        modal_analysis._build_global_stiffness_matrix = Mock(return_value=np.eye(4) * 100)
        modal_analysis._build_global_mass_matrix = Mock(return_value=np.eye(4))
        modal_analysis._apply_boundary_conditions = Mock(return_value=(np.eye(4), np.eye(4)))
        modal_analysis._calculate_participation_factors = Mock(return_value=np.ones((4, 3)))
        modal_analysis._classify_modes = Mock(return_value=['Bending'] * 4)
        
        # Run analysis
        results = modal_analysis.run_modal_analysis()
        
        # Verify results
        expected_frequencies = np.sqrt(mock_eigenvals) / (2 * np.pi)
        np.testing.assert_array_almost_equal(results.frequencies, expected_frequencies)
        assert results.num_modes == 4
        assert isinstance(results.mode_classifications, list)
        assert len(results.mode_classifications) == 4
    
    def test_analysis_error_handling(self):
        """Test error handling in analysis"""
        modal_analysis = ModalAnalysis(self.mock_model)
        
        # Mock methods that could fail
        modal_analysis._build_global_stiffness_matrix = Mock(side_effect=Exception("Matrix build failed"))
        
        with pytest.raises(AnalysisError):
            modal_analysis.run_modal_analysis()
    
    def test_mass_matrix_types(self):
        """Test different mass matrix types"""
        modal_analysis = ModalAnalysis(self.mock_model)
        
        # Test consistent mass matrix
        modal_analysis.mass_type = "consistent"
        modal_analysis._build_consistent_mass_matrix = Mock(return_value=np.eye(4))
        
        result = modal_analysis._build_global_mass_matrix()
        modal_analysis._build_consistent_mass_matrix.assert_called_once()
        
        # Test lumped mass matrix
        modal_analysis.mass_type = "lumped"
        modal_analysis._build_lumped_mass_matrix = Mock(return_value=np.eye(4))
        
        result = modal_analysis._build_global_mass_matrix()
        modal_analysis._build_lumped_mass_matrix.assert_called_once()


class TestModalAnalysisIntegration:
    """Test integration with calc objects"""
    
    def test_run_modal_analysis_on_calc(self):
        """Test running modal analysis on calc object"""
        # Create mock calc object
        mock_calc = Mock()
        mock_calc.ListElements = []
        
        # Mock the model conversion
        with patch('freecad.StructureTools.analysis.ModalAnalysis.ModalAnalysis') as MockModalAnalysis:
            mock_analysis_instance = Mock()
            mock_results = Mock()
            mock_results.frequencies = np.array([2.5, 5.1, 8.3])
            mock_analysis_instance.run_modal_analysis.return_value = mock_results
            MockModalAnalysis.return_value = mock_analysis_instance
            
            # Run the function
            results = run_modal_analysis_on_calc(mock_calc, num_modes=3)
            
            # Verify
            MockModalAnalysis.assert_called_once()
            mock_analysis_instance.set_num_modes.assert_called_once_with(3)
            mock_analysis_instance.run_modal_analysis.assert_called_once()
            assert results == mock_results
    
    def test_calc_object_validation(self):
        """Test validation of calc object"""
        # Test with None
        with pytest.raises(AnalysisError, match="Calc object cannot be None"):
            run_modal_analysis_on_calc(None)
        
        # Test with object without ListElements
        mock_calc = Mock()
        del mock_calc.ListElements
        
        with pytest.raises(AnalysisError, match="Invalid calc object"):
            run_modal_analysis_on_calc(mock_calc)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])