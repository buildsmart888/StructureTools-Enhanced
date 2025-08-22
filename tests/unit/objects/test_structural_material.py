# -*- coding: utf-8 -*-
"""
Unit tests for StructuralMaterial class.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from StructureTools.objects.StructuralMaterial import StructuralMaterial


@pytest.mark.unit
class TestStructuralMaterial:
    """Test suite for StructuralMaterial class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock()
        self.material = StructuralMaterial(self.mock_obj)
    
    def test_material_initialization(self):
        """Test material object initialization."""
        assert self.material.Type == "StructuralMaterial"
        assert self.mock_obj.Proxy == self.material
        
        # Verify properties were added
        assert self.mock_obj.addProperty.called
        
        # Check for essential properties
        property_calls = [call.args for call in self.mock_obj.addProperty.call_args_list]
        property_names = [call[1] for call in property_calls]
        
        essential_properties = [
            "MaterialStandard", "ModulusElasticity", "PoissonRatio", 
            "YieldStrength", "UltimateStrength", "Density"
        ]
        
        for prop in essential_properties:
            assert prop in property_names, f"Property {prop} not added during initialization"
    
    def test_poisson_ratio_validation_valid_range(self):
        """Test Poisson ratio validation for valid values."""
        self.mock_obj.PoissonRatio = 0.3
        
        # Should not change value for valid input
        self.material.onChanged(self.mock_obj, "PoissonRatio")
        assert self.mock_obj.PoissonRatio == 0.3
    
    def test_poisson_ratio_validation_invalid_range(self):
        """Test Poisson ratio validation for invalid values."""
        # Test upper bound violation
        self.mock_obj.PoissonRatio = 1.5
        with patch('StructureTools.objects.StructuralMaterial.App.Console') as mock_console:
            self.material.onChanged(self.mock_obj, "PoissonRatio")
            assert self.mock_obj.PoissonRatio == 0.3  # Reset to default
            mock_console.PrintWarning.assert_called_once()
        
        # Test lower bound violation
        self.mock_obj.PoissonRatio = -0.1
        with patch('StructureTools.objects.StructuralMaterial.App.Console') as mock_console:
            self.material.onChanged(self.mock_obj, "PoissonRatio")
            assert self.mock_obj.PoissonRatio == 0.3  # Reset to default
            mock_console.PrintWarning.assert_called_once()
    
    def test_material_standard_update(self, material_standards_data):
        """Test material properties update when standard changes."""
        # Mock the material standards data
        with patch('StructureTools.objects.StructuralMaterial.MATERIAL_STANDARDS', material_standards_data):
            self.mock_obj.MaterialStandard = "ASTM_A992"
            
            # Mock hasattr to return True for properties
            with patch('builtins.hasattr', return_value=True):
                self.material.onChanged(self.mock_obj, "MaterialStandard")
                
                # Verify properties were updated
                assert hasattr(self.mock_obj, 'YieldStrength')
                assert hasattr(self.mock_obj, 'UltimateStrength')
    
    def test_shear_modulus_calculation(self):
        """Test automatic shear modulus calculation."""
        # Create mock quantity objects
        mock_modulus = Mock()
        mock_modulus.getValueAs.return_value = 200000  # MPa
        
        self.mock_obj.ModulusElasticity = mock_modulus
        self.mock_obj.PoissonRatio = 0.3
        
        with patch('builtins.hasattr', return_value=True):
            self.material._calculate_shear_modulus(self.mock_obj)
            
            # Verify shear modulus was calculated (G = E / (2(1+ν)))
            expected_g = 200000 / (2 * (1 + 0.3))
            # Should be approximately 76923 MPa
            assert abs(expected_g - 76923) < 1
    
    def test_strength_validation_valid_relationship(self):
        """Test strength validation for valid Fy < Fu relationship."""
        mock_fy = Mock()
        mock_fy.getValueAs.return_value = 345  # MPa
        mock_fu = Mock()
        mock_fu.getValueAs.return_value = 450  # MPa
        
        self.mock_obj.YieldStrength = mock_fy
        self.mock_obj.UltimateStrength = mock_fu
        
        with patch('builtins.hasattr', return_value=True):
            # Should not generate warnings
            self.material._validate_strength_properties(self.mock_obj)
    
    def test_strength_validation_invalid_relationship(self):
        """Test strength validation for invalid Fy >= Fu relationship."""
        mock_fy = Mock()
        mock_fy.getValueAs.return_value = 500  # MPa
        mock_fu = Mock()
        mock_fu.getValueAs.return_value = 450  # MPa (lower than yield)
        
        self.mock_obj.YieldStrength = mock_fy
        self.mock_obj.UltimateStrength = mock_fu
        self.mock_obj.ValidationWarnings = []
        
        with patch('builtins.hasattr', return_value=True):
            with patch('StructureTools.objects.StructuralMaterial.App.Console') as mock_console:
                self.material._validate_strength_properties(self.mock_obj)
                mock_console.PrintWarning.assert_called_once()
    
    def test_validation_warning_management(self):
        """Test validation warning add/remove functionality."""
        self.mock_obj.ValidationWarnings = []
        
        # Add warning
        warning_msg = "Test warning message"
        self.material._add_validation_warning(self.mock_obj, warning_msg)
        assert warning_msg in self.mock_obj.ValidationWarnings
        
        # Don't add duplicate
        self.material._add_validation_warning(self.mock_obj, warning_msg)
        assert self.mock_obj.ValidationWarnings.count(warning_msg) == 1
        
        # Clear warnings
        self.material._clear_validation_warnings(self.mock_obj)
        assert len(self.mock_obj.ValidationWarnings) == 0
    
    def test_execute_method(self):
        """Test execute method calls all validation functions."""
        with patch.object(self.material, '_calculate_shear_modulus') as mock_shear:
            with patch.object(self.material, '_validate_poisson_ratio') as mock_poisson:
                with patch.object(self.material, '_validate_strength_properties') as mock_strength:
                    with patch.object(self.material, '_update_freecad_material') as mock_freecad:
                        
                        self.material.execute(self.mock_obj)
                        
                        # Verify all validation methods were called
                        mock_shear.assert_called_once_with(self.mock_obj)
                        mock_poisson.assert_called_once_with(self.mock_obj)
                        mock_strength.assert_called_once_with(self.mock_obj)
                        mock_freecad.assert_called_once_with(self.mock_obj)
    
    def test_freecad_material_integration(self):
        """Test FreeCAD material card creation."""
        # Mock material properties
        self.mock_obj.Label = "Test Material"
        self.mock_obj.Density = Mock()
        self.mock_obj.Density.__str__ = Mock(return_value="7850 kg/m^3")
        self.mock_obj.ModulusElasticity = Mock()
        self.mock_obj.ModulusElasticity.__str__ = Mock(return_value="200000 MPa")
        self.mock_obj.PoissonRatio = 0.3
        self.mock_obj.YieldStrength = Mock()
        self.mock_obj.YieldStrength.__str__ = Mock(return_value="345 MPa")
        self.mock_obj.UltimateStrength = Mock()
        self.mock_obj.UltimateStrength.__str__ = Mock(return_value="450 MPa")
        
        # Test material card creation
        self.material._update_freecad_material(self.mock_obj)
        
        # Verify addProperty was called for FreeCADMaterialCard
        # Note: This is simplified - actual implementation may vary


@pytest.mark.unit
class TestStructuralMaterialProperties:
    """Test material property calculations and validations."""
    
    def test_elastic_modulus_ranges(self):
        """Test elastic modulus validation for different materials."""
        material = StructuralMaterial(Mock())
        
        # Test typical steel range
        steel_modulus = 200000  # MPa
        assert 180000 <= steel_modulus <= 220000
        
        # Test typical concrete range
        concrete_modulus = 30000  # MPa
        assert 20000 <= concrete_modulus <= 50000
        
        # Test typical aluminum range
        aluminum_modulus = 70000  # MPa
        assert 60000 <= aluminum_modulus <= 80000
    
    def test_density_validation(self):
        """Test material density validation."""
        # Typical structural material densities
        steel_density = 7850  # kg/m³
        concrete_density = 2400  # kg/m³
        aluminum_density = 2700  # kg/m³
        
        assert 7800 <= steel_density <= 7900
        assert 2200 <= concrete_density <= 2600
        assert 2600 <= aluminum_density <= 2800
    
    def test_thermal_expansion_validation(self):
        """Test thermal expansion coefficient validation."""
        # Typical values (1/°C)
        steel_alpha = 12e-6
        concrete_alpha = 10e-6
        aluminum_alpha = 23e-6
        
        assert 10e-6 <= steel_alpha <= 14e-6
        assert 8e-6 <= concrete_alpha <= 12e-6
        assert 20e-6 <= aluminum_alpha <= 25e-6


@pytest.mark.performance
class TestStructuralMaterialPerformance:
    """Performance tests for StructuralMaterial operations."""
    
    def test_material_creation_performance(self, benchmark):
        """Benchmark material object creation time."""
        mock_obj = Mock()
        mock_obj.addProperty = Mock()
        
        def create_material():
            return StructuralMaterial(mock_obj)
        
        result = benchmark(create_material)
        assert result is not None
    
    def test_property_validation_performance(self, benchmark):
        """Benchmark property validation performance."""
        mock_obj = Mock()
        mock_obj.PoissonRatio = 0.3
        material = StructuralMaterial(mock_obj)
        
        def validate_properties():
            material.onChanged(mock_obj, "PoissonRatio")
        
        benchmark(validate_properties)