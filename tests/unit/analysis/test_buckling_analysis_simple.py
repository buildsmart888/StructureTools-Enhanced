"""
Simplified unit tests for Buckling Analysis core functionality
"""
import sys
import os
import numpy as np

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, project_root)

import pytest
from unittest.mock import Mock

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


class TestBucklingAnalysisBasic:
    """Basic functionality tests for BucklingAnalysis"""
    
    def setup_method(self):
        """Setup test fixtures"""
        # Create minimal mock model
        self.mock_model = Mock()
        self.buckling_analysis = BucklingAnalysis(self.mock_model)
    
    def test_initialization(self):
        """Test basic initialization"""
        assert self.buckling_analysis.model == self.mock_model
        assert self.buckling_analysis.num_modes == 5
        assert self.buckling_analysis.analysis_method == "Subspace"
        assert self.buckling_analysis.convergence_tolerance == 1e-8
    
    def test_parameter_setting(self):
        """Test parameter setting methods"""
        # Test set_analysis_parameters
        self.buckling_analysis.set_analysis_parameters(
            num_modes=10,
            tolerance=1e-6,
            method="Lanczos"
        )
        
        assert self.buckling_analysis.num_modes == 10
        assert self.buckling_analysis.convergence_tolerance == 1e-6
        assert self.buckling_analysis.analysis_method == "Lanczos"
        
        # Test set_load_case
        self.buckling_analysis.set_load_case("DL", scale_factor=1.5)
        assert self.buckling_analysis.base_load_case == "DL"
        assert self.buckling_analysis.load_scale_factor == 1.5
    
    def test_analysis_options(self):
        """Test analysis option settings"""
        # Test default options
        assert self.buckling_analysis.include_geometric_stiffness == True
        assert self.buckling_analysis.consider_initial_stress == False
        assert self.buckling_analysis.buckling_solver == "scipy"
        
        # Test option modification
        self.buckling_analysis.include_geometric_stiffness = False
        self.buckling_analysis.consider_initial_stress = True
        self.buckling_analysis.buckling_solver = "arpack"
        
        assert self.buckling_analysis.include_geometric_stiffness == False
        assert self.buckling_analysis.consider_initial_stress == True
        assert self.buckling_analysis.buckling_solver == "arpack"


class TestBucklingAnalysisResultsBasic:
    """Basic functionality tests for BucklingAnalysisResults"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.load_factors = np.array([2.5, 4.2, 6.8, 9.1, 12.3])
        self.buckling_modes = np.random.rand(12, 5)
        self.applied_loads = {'DL': 1.2, 'LL': 1.6}
        self.critical_loads = [
            {'mode': i+1, 'factor': self.load_factors[i]} 
            for i in range(len(self.load_factors))
        ]
        
        self.results = BucklingAnalysisResults(
            load_factors=self.load_factors,
            buckling_modes=self.buckling_modes,
            applied_loads=self.applied_loads,
            critical_loads=self.critical_loads
        )
    
    def test_results_initialization(self):
        """Test proper initialization of results"""
        assert hasattr(self.results, 'load_factors')
        assert hasattr(self.results, 'buckling_modes')
        assert hasattr(self.results, 'applied_loads')
        assert hasattr(self.results, 'critical_loads')
        assert hasattr(self.results, 'num_modes')
        
        # Verify data integrity
        np.testing.assert_array_equal(self.results.load_factors, self.load_factors)
        np.testing.assert_array_equal(self.results.buckling_modes, self.buckling_modes)
        assert self.results.applied_loads == self.applied_loads
        assert self.results.num_modes == len(self.load_factors)
    
    def test_derived_properties(self):
        """Test calculated derived properties"""
        # Safety factors should be calculated
        assert hasattr(self.results, 'safety_factors')
        assert len(self.results.safety_factors) == self.results.num_modes
        
        # Mode classifications should be calculated
        assert hasattr(self.results, 'mode_classifications')
        assert len(self.results.mode_classifications) == self.results.num_modes
    
    def test_basic_accessors(self):
        """Test basic data access methods"""
        # Should be able to access load factors
        first_factor = self.results.load_factors[0]
        assert first_factor == 2.5
        
        # Should be able to access buckling modes
        first_mode = self.results.buckling_modes[:, 0]
        assert len(first_mode) == 12  # Number of DOFs
        
        # Should be able to access critical loads
        first_critical = self.results.critical_loads[0]
        assert first_critical['mode'] == 1
        assert first_critical['factor'] == 2.5


class TestBucklingAnalysisIntegrationBasic:
    """Basic integration tests"""
    
    def test_create_analysis_with_mock_model(self):
        """Test creating analysis with mock model"""
        mock_model = Mock()
        analysis = BucklingAnalysis(mock_model)
        
        # Should not raise errors
        assert analysis.model == mock_model
        assert analysis.results is None
    
    def test_analysis_state_management(self):
        """Test analysis state management"""
        mock_model = Mock()
        analysis = BucklingAnalysis(mock_model)
        
        # Initial state
        assert analysis.results is None
        assert analysis.analysis_time == 0.0
        assert analysis.convergence_info == {}
        
        # Can store results
        mock_results = Mock()
        analysis.results = mock_results
        assert analysis.results == mock_results
        
        # Can store timing information
        analysis.analysis_time = 5.2
        assert analysis.analysis_time == 5.2
    
    def test_results_storage(self):
        """Test results can be properly stored"""
        load_factors = np.array([3.0, 5.0])
        modes = np.random.rand(6, 2)
        applied = {'DL': 1.0}
        critical = [{'mode': 1, 'factor': 3.0}, {'mode': 2, 'factor': 5.0}]
        
        results = BucklingAnalysisResults(
            load_factors=load_factors,
            buckling_modes=modes,
            applied_loads=applied,
            critical_loads=critical
        )
        
        # Store in analysis object
        mock_model = Mock()
        analysis = BucklingAnalysis(mock_model)
        analysis.results = results
        
        # Should be accessible
        assert analysis.results == results
        assert len(analysis.results.load_factors) == 2
        assert analysis.results.num_modes == 2


class TestBucklingAnalysisValidation:
    """Test validation and error handling"""
    
    def test_model_validation(self):
        """Test model validation"""
        # Should handle None model gracefully in basic operations
        try:
            analysis = BucklingAnalysis(None)
            # Basic operations should not crash immediately
            analysis.set_analysis_parameters(num_modes=3)
            analysis.set_load_case("DL")
        except Exception as e:
            # Any exceptions should be informative
            assert isinstance(e, (ValueError, AttributeError, TypeError))
    
    def test_parameter_bounds(self):
        """Test parameter boundary validation"""
        mock_model = Mock()
        analysis = BucklingAnalysis(mock_model)
        
        # Should handle reasonable parameter ranges
        analysis.set_analysis_parameters(num_modes=1)  # Minimum
        assert analysis.num_modes == 1
        
        analysis.set_analysis_parameters(num_modes=50)  # Large
        assert analysis.num_modes == 50
        
        analysis.set_analysis_parameters(tolerance=1e-12)  # Very tight
        assert analysis.convergence_tolerance == 1e-12
        
        analysis.set_analysis_parameters(tolerance=1e-3)  # Loose
        assert analysis.convergence_tolerance == 1e-3
    
    def test_method_validation(self):
        """Test analysis method validation"""
        mock_model = Mock()
        analysis = BucklingAnalysis(mock_model)
        
        # Should accept valid methods
        valid_methods = ["Subspace", "Lanczos", "ARPACK"]
        for method in valid_methods:
            analysis.set_analysis_parameters(method=method)
            assert analysis.analysis_method == method


if __name__ == '__main__':
    pytest.main([__file__, '-v'])