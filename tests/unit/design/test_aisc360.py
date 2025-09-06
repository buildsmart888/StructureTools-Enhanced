"""
Unit tests for AISC 360-16 Design Code Implementation
"""
import sys
import os
import numpy as np

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, project_root)

import pytest
from unittest.mock import Mock, patch

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

sys.modules['FreeCAD'] = MockApp

from freecad.StructureTools.design.AISC360 import (
    AISC360DesignCode, DesignMethod, MemberType, FailureMode,
    SectionProperties, MaterialProperties, DesignForces, DesignResult,
    SteelDesignUtilities
)


class TestSectionProperties:
    """Test SectionProperties dataclass."""
    
    def test_section_properties_initialization(self):
        """Test proper initialization of section properties."""
        section = SectionProperties(
            name='W18X35', A=10.3, Ix=510.0, Iy=57.6, Zx=57.6, Zy=15.3,
            Sx=57.0, Sy=7.00, rx=7.04, ry=2.36, J=0.422, Cw=5440.0,
            d=17.70, tw=0.300, bf=6.00, tf=0.425, k=1.16
        )
        
        assert section.name == 'W18X35'
        assert section.A == 10.3
        assert section.Ix == 510.0
        assert section.d == 17.70
    
    def test_properties_dict(self):
        """Test properties dictionary conversion."""
        section = SectionProperties(
            name='W14X22', A=6.49, Ix=199.0, Iy=29.0, Zx=29.0, Zy=9.77,
            Sx=28.4, Sy=4.14, rx=5.54, ry=2.11, J=0.239, Cw=2360.0,
            d=13.74, tw=0.230, bf=5.00, tf=0.335, k=0.859
        )
        
        props_dict = section.properties_dict
        assert isinstance(props_dict, dict)
        assert props_dict['name'] == 'W14X22'
        assert props_dict['A'] == 6.49
        assert len(props_dict) == 17  # All properties


class TestMaterialProperties:
    """Test MaterialProperties dataclass."""
    
    def test_material_properties_initialization(self):
        """Test proper initialization of material properties."""
        material = MaterialProperties(
            name='A992', Fy=50.0, Fu=65.0, E=29000.0, G=11200.0,
            nu=0.30, density=490.0
        )
        
        assert material.name == 'A992'
        assert material.Fy == 50.0
        assert material.E == 29000.0
    
    def test_material_validation(self):
        """Test material property validation."""
        # Valid material
        valid_material = MaterialProperties(
            name='A36', Fy=36.0, Fu=58.0, E=29000.0, G=11200.0,
            nu=0.30, density=490.0
        )
        assert valid_material.is_valid == True
        
        # Invalid material (Fu < Fy)
        invalid_material = MaterialProperties(
            name='Invalid', Fy=50.0, Fu=40.0, E=29000.0, G=11200.0,
            nu=0.30, density=490.0
        )
        assert invalid_material.is_valid == False


class TestDesignForces:
    """Test DesignForces dataclass."""
    
    def test_design_forces_initialization(self):
        """Test proper initialization of design forces."""
        forces = DesignForces(Pu=100.0, Mux=2400.0, Muy=600.0, Vux=15.0, Vuy=5.0)
        
        assert forces.Pu == 100.0
        assert forces.Mux == 2400.0
        assert forces.max_moment == 2400.0  # Max of Mux and Muy
        assert forces.resultant_shear == pytest.approx(15.81, rel=1e-2)  # sqrt(15^2 + 5^2)
    
    def test_force_calculations(self):
        """Test derived force calculations."""
        forces = DesignForces(Mux=1200.0, Muy=1600.0, Vux=8.0, Vuy=6.0)
        
        assert forces.max_moment == 1600.0  # Max of the two moments
        assert forces.resultant_shear == 10.0  # 3-4-5 triangle


class TestAISC360DesignCode:
    """Test AISC360DesignCode class."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.lrfd_checker = AISC360DesignCode(DesignMethod.LRFD)
        self.asd_checker = AISC360DesignCode(DesignMethod.ASD)
        
        # Standard test section and material
        self.test_section = SectionProperties(
            name='W18X35', A=10.3, Ix=510.0, Iy=57.6, Zx=57.6, Zy=15.3,
            Sx=57.0, Sy=7.00, rx=7.04, ry=2.36, J=0.422, Cw=5440.0,
            d=17.70, tw=0.300, bf=6.00, tf=0.425, k=1.16
        )
        
        self.test_material = MaterialProperties(
            name='A992', Fy=50.0, Fu=65.0, E=29000.0, G=11200.0,
            nu=0.30, density=490.0
        )
    
    def test_design_code_initialization(self):
        """Test proper initialization of design code checker."""
        # LRFD initialization
        assert self.lrfd_checker.design_method == DesignMethod.LRFD
        assert self.lrfd_checker.code_version == "AISC 360-16"
        assert hasattr(self.lrfd_checker, 'resistance_factors')
        
        # ASD initialization
        assert self.asd_checker.design_method == DesignMethod.ASD
        assert hasattr(self.asd_checker, 'safety_factors')
    
    def test_database_loading(self):
        """Test steel section and material database loading."""
        # Check section database
        assert 'W18X35' in self.lrfd_checker.steel_database
        assert 'W14X22' in self.lrfd_checker.steel_database
        
        # Check material database
        assert 'A992' in self.lrfd_checker.material_database
        assert 'A36' in self.lrfd_checker.material_database
        
        # Verify section properties
        w18x35 = self.lrfd_checker.steel_database['W18X35']
        assert w18x35.A == 10.3
        assert w18x35.Ix == 510.0
    
    def test_resistance_factors(self):
        """Test resistance factors for LRFD."""
        factors = self.lrfd_checker.resistance_factors
        
        # Standard AISC resistance factors
        assert factors['flexure'] == 0.90
        assert factors['shear'] == 0.90
        assert factors['compression'] == 0.90
        assert factors['tension'] == 0.90
    
    def test_safety_factors(self):
        """Test safety factors for ASD."""
        factors = self.asd_checker.safety_factors
        
        # Standard AISC safety factors
        assert factors['flexure'] == 1.67
        assert factors['shear'] == 1.67
        assert factors['compression'] == 1.67
        assert factors['tension'] == 1.67
    
    def test_beam_flexure_check_basic(self):
        """Test basic beam flexural strength check."""
        # Test forces with moment only
        forces = DesignForces(Mux=2400.0)  # 2400 kip-in moment
        
        # Length properties
        length_props = {'Lb': 72.0, 'Kx': 1.0, 'Ky': 1.0, 'Cb': 1.0}
        
        # Run flexure check
        result = self.lrfd_checker.check_beam_flexure(
            self.test_section, self.test_material, forces, length_props
        )
        
        # Verify result structure
        assert isinstance(result, DesignResult)
        assert result.member_name == 'W18X35'
        assert result.design_method == DesignMethod.LRFD
        assert result.failure_mode in [FailureMode.FLEXURAL_YIELDING, FailureMode.LATERAL_TORSIONAL_BUCKLING]
        assert result.demand > 0
        assert result.capacity > 0
        assert result.ratio > 0
        assert result.code_section in ["F2.1", "F2.2"]
    
    def test_beam_flexure_check_zero_moment(self):
        """Test flexure check with zero moment."""
        forces = DesignForces(Mux=0.0)
        length_props = {'Lb': 72.0}
        
        result = self.lrfd_checker.check_beam_flexure(
            self.test_section, self.test_material, forces, length_props
        )
        
        assert result.demand == 0.0
        assert result.capacity == float('inf')
        assert result.ratio == 0.0
        assert result.status == "OK"
    
    def test_beam_shear_check(self):
        """Test beam shear strength check."""
        forces = DesignForces(Vux=15.0, Vuy=5.0)  # Resultant = ~15.8 kips
        
        result = self.lrfd_checker.check_beam_shear(
            self.test_section, self.test_material, forces
        )
        
        # Verify result
        assert isinstance(result, DesignResult)
        assert result.failure_mode == FailureMode.SHEAR_YIELDING
        assert result.code_section == "G2.1"
        assert result.demand > 0
        assert result.capacity > 0
        
        # Check details
        assert 'web_area' in result.details
        assert 'h_tw_ratio' in result.details
        assert 'shear_coefficient' in result.details
    
    def test_column_compression_check(self):
        """Test column compression strength check."""
        forces = DesignForces(Pu=200.0)  # 200 kip compression
        
        # Length properties with effective lengths
        length_props = {
            'Lx': 144.0,  # 12 ft
            'Ly': 144.0,  # 12 ft
            'Kx': 1.0,
            'Ky': 1.0
        }
        
        result = self.lrfd_checker.check_column_compression(
            self.test_section, self.test_material, forces, length_props
        )
        
        # Verify result
        assert isinstance(result, DesignResult)
        assert result.failure_mode in [FailureMode.COMPRESSION_YIELDING, FailureMode.COMPRESSION_BUCKLING]
        assert result.code_section == "E3"
        assert result.demand > 0
        assert result.capacity > 0
        
        # Check details
        assert 'slenderness_max' in result.details
        assert 'critical_stress' in result.details
        assert 'lambda_c' in result.details
    
    def test_combined_loading_check(self):
        """Test combined axial and flexural loading check."""
        forces = DesignForces(Pu=50.0, Mux=1200.0, Muy=300.0)
        
        length_props = {
            'Lx': 144.0, 'Ly': 144.0, 'Lb': 72.0,
            'Kx': 1.0, 'Ky': 1.0, 'Cb': 1.0
        }
        
        result = self.lrfd_checker.check_combined_loading(
            self.test_section, self.test_material, forces, length_props
        )
        
        # Verify result
        assert isinstance(result, DesignResult)
        assert result.failure_mode == FailureMode.COMBINED_LOADING
        assert result.code_section == "H1.1"
        assert result.capacity == 1.0  # Interaction equation limit
        
        # Check details
        assert 'axial_ratio' in result.details
        assert 'interaction_equation' in result.details
        assert result.details['interaction_equation'] in ['H1-1a', 'H1-1b']
    
    def test_deflection_check(self):
        """Test deflection limit check."""
        deflections = {'live': 0.5}  # 0.5 inch deflection
        length = 240.0  # 20 ft span
        
        result = self.lrfd_checker.check_deflection(
            self.test_section, self.test_material, deflections, length, 'live'
        )
        
        # Verify result
        assert isinstance(result, DesignResult)
        assert result.failure_mode == FailureMode.DEFLECTION_LIMIT
        assert result.code_section == "Serviceability"
        
        # L/360 limit for live load
        expected_limit = length / 360.0
        assert abs(result.capacity - expected_limit) < 1e-6
    
    def test_asd_vs_lrfd_comparison(self):
        """Test that ASD and LRFD give different but reasonable results."""
        forces = DesignForces(Mux=2000.0)
        length_props = {'Lb': 72.0, 'Cb': 1.0}
        
        # LRFD check
        lrfd_result = self.lrfd_checker.check_beam_flexure(
            self.test_section, self.test_material, forces, length_props
        )
        
        # ASD check
        asd_result = self.asd_checker.check_beam_flexure(
            self.test_section, self.test_material, forces, length_props
        )
        
        # Both should be valid results
        assert isinstance(lrfd_result, DesignResult)
        assert isinstance(asd_result, DesignResult)
        
        # Results should be different (different factors)
        assert lrfd_result.capacity != asd_result.capacity
        
        # Both should have reasonable ratios
        assert 0.0 <= lrfd_result.ratio <= 10.0
        assert 0.0 <= asd_result.ratio <= 10.0


class TestLoadCombinations:
    """Test load combination functionality."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.lrfd_checker = AISC360DesignCode(DesignMethod.LRFD)
        self.asd_checker = AISC360DesignCode(DesignMethod.ASD)
    
    def test_standard_load_combinations_lrfd(self):
        """Test standard LRFD load combinations."""
        combinations = self.lrfd_checker.get_standard_load_combinations()
        
        # Should have multiple combinations
        assert len(combinations) > 5
        
        # Check specific combinations
        combo_names = [combo.name for combo in combinations]
        assert "1.4D" in combo_names
        assert "1.2D + 1.6L" in combo_names
        assert "0.9D + 1.0W" in combo_names
        
        # Check factors
        for combo in combinations:
            assert combo.method == DesignMethod.LRFD
            assert isinstance(combo.factors, dict)
            assert len(combo.factors) > 0
    
    def test_standard_load_combinations_asd(self):
        """Test standard ASD load combinations."""
        combinations = self.asd_checker.get_standard_load_combinations()
        
        # Should have multiple combinations
        assert len(combinations) > 5
        
        # Check specific combinations
        combo_names = [combo.name for combo in combinations]
        assert "D" in combo_names
        assert "D + L" in combo_names
        assert "0.6D + 0.6W" in combo_names
        
        # Check factors
        for combo in combinations:
            assert combo.method == DesignMethod.ASD
            assert isinstance(combo.factors, dict)
    
    def test_factored_force_calculation(self):
        """Test factored force calculation from load combination."""
        from freecad.StructureTools.design.AISC360 import LoadCombination
        
        combo = LoadCombination("1.2D + 1.6L", DesignMethod.LRFD, {"D": 1.2, "L": 1.6})
        
        forces = {"D": 50.0, "L": 30.0}
        factored = combo.get_factored_force(forces)
        
        expected = 1.2 * 50.0 + 1.6 * 30.0  # 108.0
        assert factored == expected


class TestSteelDesignUtilities:
    """Test utility functions."""
    
    def test_effective_length_factor_calculation(self):
        """Test effective length factor calculation."""
        # Pinned-pinned
        k = SteelDesignUtilities.calculate_effective_length_factor('pinned', 'pinned')
        assert k == 1.0
        
        # Fixed-fixed
        k = SteelDesignUtilities.calculate_effective_length_factor('fixed', 'fixed')
        assert k == 0.5
        
        # Fixed-pinned
        k = SteelDesignUtilities.calculate_effective_length_factor('fixed', 'pinned')
        assert k == 0.7
        
        # Fixed-free (cantilever)
        k = SteelDesignUtilities.calculate_effective_length_factor('fixed', 'free')
        assert k == 2.0
    
    def test_unit_conversion(self):
        """Test unit conversion functionality."""
        # Length conversions
        assert SteelDesignUtilities.convert_units(12.0, 'in', 'ft') == 1.0
        assert SteelDesignUtilities.convert_units(1.0, 'ft', 'in') == 12.0
        
        # Force conversions
        assert SteelDesignUtilities.convert_units(1.0, 'kip', 'lbf') == 1000.0
        assert SteelDesignUtilities.convert_units(1000.0, 'lbf', 'kip') == 1.0
        
        # Stress conversions
        assert SteelDesignUtilities.convert_units(1.0, 'ksi', 'psi') == 1000.0
        
        # Invalid units should raise error
        with pytest.raises(ValueError):
            SteelDesignUtilities.convert_units(1.0, 'invalid', 'in')


class TestDesignReporting:
    """Test design report generation."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.design_checker = AISC360DesignCode(DesignMethod.LRFD)
        
        # Create sample results
        self.sample_results = [
            DesignResult(
                member_name="W18X35",
                design_method=DesignMethod.LRFD,
                failure_mode=FailureMode.FLEXURAL_YIELDING,
                demand=2000.0,
                capacity=2880.0,
                ratio=0.694,
                status="OK",
                details={'Mp': 2880.0, 'applied_moment': 2000.0},
                code_section="F2.1"
            ),
            DesignResult(
                member_name="W14X22",
                design_method=DesignMethod.LRFD,
                failure_mode=FailureMode.SHEAR_YIELDING,
                demand=15.0,
                capacity=45.6,
                ratio=0.329,
                status="OK",
                details={'Vn': 50.7, 'applied_shear': 15.0},
                code_section="G2.1"
            )
        ]
    
    def test_design_report_generation(self):
        """Test comprehensive design report generation."""
        project_info = {
            "Project Name": "Test Structure",
            "Engineer": "Test Engineer",
            "Date": "2024-01-01"
        }
        
        report = self.design_checker.generate_design_report(self.sample_results, project_info)
        
        # Check report structure
        assert isinstance(report, str)
        assert len(report) > 100  # Should be substantial
        
        # Check content
        assert "AISC 360-16 STEEL DESIGN REPORT" in report
        assert "LRFD" in report
        assert "Test Structure" in report
        assert "W18X35" in report
        assert "W14X22" in report
        
        # Check summary
        assert "Total Members Checked: 2" in report
        assert "Passing Members: 2" in report
        assert "Success Rate: 100.0%" in report
    
    def test_design_result_summary(self):
        """Test individual design result summary."""
        result = self.sample_results[0]
        summary = result.get_summary()
        
        assert "W18X35" in summary
        assert "Flexural Yielding" in summary
        assert "0.694" in summary
        assert "OK" in summary
    
    def test_design_result_acceptability(self):
        """Test design result acceptability check."""
        # Passing result
        passing_result = self.sample_results[0]
        assert passing_result.is_acceptable == True
        
        # Failing result
        failing_result = DesignResult(
            member_name="Test",
            design_method=DesignMethod.LRFD,
            failure_mode=FailureMode.FLEXURAL_YIELDING,
            demand=3000.0,
            capacity=2000.0,
            ratio=1.5,
            status="FAIL",
            details={},
            code_section="F2.1"
        )
        assert failing_result.is_acceptable == False


class TestAdvancedFeatures:
    """Test advanced design features."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.design_checker = AISC360DesignCode(DesignMethod.LRFD)
        
        self.test_section = SectionProperties(
            name='W24X55', A=16.2, Ix=1350.0, Iy=134.0, Zx=114.0, Zy=29.1,
            Sx=112.0, Sy=13.3, rx=9.11, ry=2.87, J=0.742, Cw=14600.0,
            d=23.57, tw=0.395, bf=7.01, tf=0.505, k=1.34
        )
        
        self.test_material = MaterialProperties(
            name='A992', Fy=50.0, Fu=65.0, E=29000.0, G=11200.0,
            nu=0.30, density=490.0
        )
    
    def test_section_classification(self):
        """Test section classification for flexure."""
        classification = self.design_checker._classify_section_flexure(
            self.test_section, self.test_material
        )
        
        assert classification in ["compact", "noncompact", "slender"]
    
    def test_lateral_torsional_buckling_calculation(self):
        """Test lateral-torsional buckling strength calculation."""
        length_props = {'Lb': 120.0, 'Cb': 1.0}  # 10 ft unbraced length
        
        ltb_strength = self.design_checker._calculate_ltb_strength(
            self.test_section, self.test_material, length_props
        )
        
        assert ltb_strength > 0
        assert ltb_strength <= self.test_material.Fy * self.test_section.Zx
    
    def test_compression_buckling_modes(self):
        """Test compression buckling for different slenderness ratios."""
        # Short column (yielding)
        short_props = {'Lx': 50.0, 'Ly': 50.0, 'Kx': 1.0, 'Ky': 1.0}
        forces = DesignForces(Pu=300.0)
        
        short_result = self.design_checker.check_column_compression(
            self.test_section, self.test_material, forces, short_props
        )
        
        # Long column (buckling)
        long_props = {'Lx': 300.0, 'Ly': 300.0, 'Kx': 1.0, 'Ky': 1.0}
        
        long_result = self.design_checker.check_column_compression(
            self.test_section, self.test_material, forces, long_props
        )
        
        # Short column should have higher capacity
        assert short_result.capacity > long_result.capacity
        
        # Check failure modes
        assert short_result.details['lambda_c'] < long_result.details['lambda_c']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])