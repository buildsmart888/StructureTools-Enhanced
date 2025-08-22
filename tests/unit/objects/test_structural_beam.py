# -*- coding: utf-8 -*-
"""
Unit tests for StructuralBeam class.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import math
from StructureTools.objects.StructuralBeam import StructuralBeam


@pytest.mark.unit
class TestStructuralBeam:
    """Test suite for StructuralBeam class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock()
        self.beam = StructuralBeam(self.mock_obj)
    
    def test_beam_initialization(self):
        """Test beam object initialization."""
        assert self.beam.Type == "StructuralBeam"
        assert self.mock_obj.Proxy == self.beam
        
        # Verify essential properties were added
        property_calls = [call.args for call in self.mock_obj.addProperty.call_args_list]
        property_names = [call[1] for call in property_calls]
        
        essential_properties = [
            "StartPoint", "EndPoint", "Length", "CrossSectionArea",
            "MomentInertiaY", "MomentInertiaZ", "Material"
        ]
        
        for prop in essential_properties:
            assert prop in property_names, f"Property {prop} not added during initialization"
    
    def test_geometry_calculation(self, mock_vector):
        """Test beam geometry calculations."""
        # Set up beam endpoints
        start = mock_vector(0, 0, 0)
        end = mock_vector(6000, 0, 0)  # 6m beam
        
        self.mock_obj.StartPoint = start
        self.mock_obj.EndPoint = end
        
        # Test geometry update
        with patch('builtins.hasattr', return_value=True):
            self.beam._update_geometry(self.mock_obj)
            
            # Check length calculation
            expected_length = 6000.0
            assert abs(self.mock_obj.Length - expected_length) < 1e-6
    
    def test_local_coordinate_system(self, mock_vector):
        """Test local coordinate system calculation."""
        # Horizontal beam
        start = mock_vector(0, 0, 0)
        end = mock_vector(1000, 0, 0)
        
        self.mock_obj.StartPoint = start
        self.mock_obj.EndPoint = end
        
        with patch('builtins.hasattr', return_value=True):
            self.beam._update_geometry(self.mock_obj)
            
            # Local X should be along beam (1,0,0)
            local_x = self.mock_obj.LocalXAxis
            assert abs(local_x.x - 1.0) < 1e-6
            assert abs(local_x.y) < 1e-6
            assert abs(local_x.z) < 1e-6
    
    def test_vertical_beam_coordinate_system(self, mock_vector):
        """Test coordinate system for vertical beam."""
        # Vertical beam
        start = mock_vector(0, 0, 0)
        end = mock_vector(0, 0, 3000)  # 3m column
        
        self.mock_obj.StartPoint = start
        self.mock_obj.EndPoint = end
        
        with patch('builtins.hasattr', return_value=True):
            self.beam._update_geometry(self.mock_obj)
            
            # Local X should be vertical (0,0,1)
            local_x = self.mock_obj.LocalXAxis
            assert abs(local_x.x) < 1e-6
            assert abs(local_x.y) < 1e-6
            assert abs(local_x.z - 1.0) < 1e-6
    
    def test_section_property_validation(self):
        """Test section property validation."""
        # Mock section properties
        mock_area = Mock()
        mock_area.getValueAs.return_value = 7740  # mm²
        
        mock_depth = Mock()
        mock_depth.getValueAs.return_value = 311  # mm
        
        mock_width = Mock()
        mock_width.getValueAs.return_value = 165  # mm
        
        self.mock_obj.CrossSectionArea = mock_area
        self.mock_obj.SectionDepth = mock_depth
        self.mock_obj.SectionWidth = mock_width
        
        with patch('builtins.hasattr', return_value=True):
            # Should not generate warnings for reasonable values
            self.beam._validate_section_properties(self.mock_obj)
    
    def test_section_property_mismatch_warning(self):
        """Test warning for section property mismatch."""
        # Set up mismatched properties
        mock_area = Mock()
        mock_area.getValueAs.return_value = 1000  # mm² (too small)
        
        mock_depth = Mock()
        mock_depth.getValueAs.return_value = 311  # mm
        
        mock_width = Mock()
        mock_width.getValueAs.return_value = 165  # mm
        
        self.mock_obj.CrossSectionArea = mock_area
        self.mock_obj.SectionDepth = mock_depth
        self.mock_obj.SectionWidth = mock_width
        
        with patch('builtins.hasattr', return_value=True):
            with patch('StructureTools.objects.StructuralBeam.App.Console') as mock_console:
                self.beam._validate_section_properties(self.mock_obj)
                # Should warn about area mismatch
                mock_console.PrintWarning.assert_called_once()
    
    def test_end_condition_updates(self):
        """Test end condition property updates."""
        # Test pinned condition
        self.mock_obj.StartCondition = "Pinned"
        
        with patch('builtins.hasattr', return_value=True):
            self.beam._update_end_conditions(self.mock_obj)
            
            # Should set moment releases for pinned connection
            assert self.mock_obj.StartMomentReleaseY == True
            assert self.mock_obj.StartMomentReleaseZ == True
        
        # Test fixed condition
        self.mock_obj.StartCondition = "Fixed"
        
        with patch('builtins.hasattr', return_value=True):
            self.beam._update_end_conditions(self.mock_obj)
            
            # Should not have moment releases for fixed connection
            assert self.mock_obj.StartMomentReleaseY == False
            assert self.mock_obj.StartMomentReleaseZ == False
    
    def test_material_property_update(self):
        """Test material property updates."""
        # Mock material object
        mock_material = Mock()
        mock_modulus = Mock()
        mock_modulus.getValueAs.return_value = 200000  # MPa
        mock_material.ModulusElasticity = mock_modulus
        
        self.mock_obj.Material = mock_material
        
        with patch('builtins.hasattr', return_value=True):
            self.beam._update_material_properties(self.mock_obj)
            
            # Should update effective modulus
            assert "200000" in str(self.mock_obj.EffectiveModulus)
    
    def test_load_consistency_validation(self):
        """Test load array consistency validation."""
        # Set up inconsistent load arrays
        self.mock_obj.DistributedLoadY = [1000, 2000]  # 2 load cases
        self.mock_obj.DistributedLoadZ = [500]  # 1 load case
        self.mock_obj.PointLoads = [0, 5000, 10000]  # 3 load cases
        
        with patch('builtins.hasattr', return_value=True):
            with patch('StructureTools.objects.StructuralBeam.App.Console') as mock_console:
                self.beam._validate_load_consistency(self.mock_obj)
                # Should warn about inconsistent load cases
                mock_console.PrintWarning.assert_called_once()


@pytest.mark.unit
class TestStructuralBeamStiffness:
    """Test beam stiffness matrix calculations."""
    
    def setup_method(self):
        """Set up beam for stiffness testing."""
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock()
        self.beam = StructuralBeam(self.mock_obj)
        
        # Set up beam properties
        mock_length = Mock()
        mock_length.getValueAs.return_value = 6000  # mm
        
        mock_modulus = Mock()
        mock_modulus.getValueAs.return_value = 200000  # MPa
        
        mock_area = Mock()
        mock_area.getValueAs.return_value = 7740  # mm²
        
        mock_iy = Mock()
        mock_iy.getValueAs.return_value = 204000000  # mm⁴
        
        mock_iz = Mock()
        mock_iz.getValueAs.return_value = 9200000  # mm⁴
        
        mock_j = Mock()
        mock_j.getValueAs.return_value = 410000  # mm⁴
        
        self.mock_obj.Length = mock_length
        self.mock_obj.EffectiveModulus = mock_modulus
        self.mock_obj.CrossSectionArea = mock_area
        self.mock_obj.MomentInertiaY = mock_iy
        self.mock_obj.MomentInertiaZ = mock_iz
        self.mock_obj.TorsionalConstant = mock_j
    
    def test_stiffness_matrix_size(self):
        """Test stiffness matrix dimensions."""
        with patch('builtins.hasattr', return_value=True):
            k_matrix = self.beam.get_stiffness_matrix(self.mock_obj)
            
            # Should be 12x12 matrix
            assert len(k_matrix) == 12
            assert all(len(row) == 12 for row in k_matrix)
    
    def test_stiffness_matrix_symmetry(self):
        """Test stiffness matrix symmetry."""
        with patch('builtins.hasattr', return_value=True):
            k_matrix = self.beam.get_stiffness_matrix(self.mock_obj)
            
            # Matrix should be symmetric
            for i in range(12):
                for j in range(12):
                    assert abs(k_matrix[i][j] - k_matrix[j][i]) < 1e-10
    
    def test_axial_stiffness(self):
        """Test axial stiffness terms."""
        with patch('builtins.hasattr', return_value=True):
            k_matrix = self.beam.get_stiffness_matrix(self.mock_obj)
            
            # Axial stiffness = EA/L
            E = 200000  # MPa
            A = 7740    # mm²
            L = 6000    # mm
            expected_axial = E * A / L
            
            # Check diagonal terms (nodes 1 and 2, DOF 0 and 6)
            assert abs(k_matrix[0][0] - expected_axial) < 1e-6
            assert abs(k_matrix[6][6] - expected_axial) < 1e-6
            
            # Check off-diagonal coupling
            assert abs(k_matrix[0][6] + expected_axial) < 1e-6
    
    def test_bending_stiffness_strong_axis(self):
        """Test bending stiffness about strong axis."""
        with patch('builtins.hasattr', return_value=True):
            k_matrix = self.beam.get_stiffness_matrix(self.mock_obj)
            
            # Bending stiffness = 12EI/L³
            E = 200000      # MPa
            I = 204000000   # mm⁴ (strong axis)
            L = 6000        # mm
            expected_bending = 12 * E * I / (L**3)
            
            # Check transverse stiffness (DOF 1 and 7)
            assert abs(k_matrix[1][1] - expected_bending) < 1e-3
            assert abs(k_matrix[7][7] - expected_bending) < 1e-3
    
    def test_zero_length_beam(self):
        """Test handling of zero-length beam."""
        mock_length = Mock()
        mock_length.getValueAs.return_value = 0  # Zero length
        self.mock_obj.Length = mock_length
        
        with patch('builtins.hasattr', return_value=True):
            k_matrix = self.beam.get_stiffness_matrix(self.mock_obj)
            
            # Should return zero matrix for zero-length beam
            for i in range(12):
                for j in range(12):
                    assert k_matrix[i][j] == 0.0


@pytest.mark.unit
class TestStructuralBeamLoads:
    """Test beam load handling."""
    
    def setup_method(self):
        """Set up beam for load testing."""
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock()
        self.beam = StructuralBeam(self.mock_obj)
        
        # Set up beam length
        mock_length = Mock()
        mock_length.getValueAs.return_value = 6000  # mm
        self.mock_obj.Length = mock_length
    
    def test_distributed_load_conversion(self):
        """Test conversion of distributed loads to nodal loads."""
        # Set up uniform distributed load
        self.mock_obj.DistributedLoadY = [-10000]  # 10 kN/m downward
        self.mock_obj.DistributedLoadZ = [0]
        
        with patch('builtins.hasattr', return_value=True):
            load_vector = self.beam.get_load_vector(self.mock_obj, 0)
            
            # For uniform load w, equivalent nodal loads are wL/2 at each end
            L = 6000  # mm
            w = -10000  # N/m
            expected_force = w * L / 2
            
            # Check nodal forces (DOF 1 and 7 for Y-direction)
            assert abs(load_vector[1] - expected_force) < 1e-6
            assert abs(load_vector[7] - expected_force) < 1e-6
            
            # Check moments (DOF 5 and 11)
            expected_moment = w * L**2 / 12
            assert abs(load_vector[5] - expected_moment) < 1e-3
            assert abs(load_vector[11] + expected_moment) < 1e-3  # Opposite sign
    
    def test_empty_load_vector(self):
        """Test load vector for beam with no loads."""
        self.mock_obj.DistributedLoadY = []
        self.mock_obj.DistributedLoadZ = []
        
        with patch('builtins.hasattr', return_value=True):
            load_vector = self.beam.get_load_vector(self.mock_obj, 0)
            
            # Should be all zeros
            assert all(abs(f) < 1e-10 for f in load_vector)
            assert len(load_vector) == 12


@pytest.mark.performance
class TestStructuralBeamPerformance:
    """Performance tests for StructuralBeam operations."""
    
    def test_beam_creation_performance(self, benchmark):
        """Benchmark beam object creation time."""
        mock_obj = Mock()
        mock_obj.addProperty = Mock()
        
        def create_beam():
            return StructuralBeam(mock_obj)
        
        result = benchmark(create_beam)
        assert result is not None
    
    def test_stiffness_matrix_performance(self, benchmark):
        """Benchmark stiffness matrix calculation performance."""
        mock_obj = Mock()
        mock_obj.addProperty = Mock()
        beam = StructuralBeam(mock_obj)
        
        # Set up required properties
        mock_length = Mock()
        mock_length.getValueAs.return_value = 6000
        mock_obj.Length = mock_length
        
        with patch('builtins.hasattr', return_value=True):
            def calculate_stiffness():
                return beam.get_stiffness_matrix(mock_obj)
            
            result = benchmark(calculate_stiffness)
            assert len(result) == 12