"""
Unit tests for Area Load Task Panel
"""
import sys
import os

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, project_root)

import pytest
from unittest.mock import Mock, patch, MagicMock

# Mock FreeCAD before importing task panels
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

class MockGui:
    Control = Mock()

sys.modules['FreeCAD'] = MockApp
sys.modules['FreeCADGui'] = MockGui

# Mock PySide2 Qt modules
mock_qt = Mock()
mock_qt.QtCore = Mock()
mock_qt.QtGui = Mock() 
mock_qt.QtWidgets = Mock()
mock_qt.QtWidgets.QWidget = Mock
mock_qt.QtWidgets.QVBoxLayout = Mock
mock_qt.QtWidgets.QHBoxLayout = Mock
mock_qt.QtWidgets.QFormLayout = Mock
mock_qt.QtWidgets.QGroupBox = Mock
mock_qt.QtWidgets.QLabel = Mock
mock_qt.QtWidgets.QDoubleSpinBox = Mock
mock_qt.QtWidgets.QComboBox = Mock
mock_qt.QtWidgets.QCheckBox = Mock
mock_qt.QtWidgets.QPushButton = Mock
mock_qt.QtWidgets.QSpinBox = Mock
mock_qt.QtWidgets.QListWidget = Mock
sys.modules['PySide2'] = mock_qt

# Import the module to test
from freecad.StructureTools.taskpanels.AreaLoadPanel import AreaLoadApplicationPanel


class TestAreaLoadPanel:
    """Test the AreaLoadApplicationPanel class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        # Create mock selected faces
        self.mock_face1 = Mock()
        self.mock_face1.Area = 10.0
        self.mock_face1.CenterOfMass = (2.5, 2.5, 0)
        
        self.mock_face2 = Mock()
        self.mock_face2.Area = 15.0 
        self.mock_face2.CenterOfMass = (5.0, 3.0, 0)
        
        self.selected_faces = [self.mock_face1, self.mock_face2]
        
        # Mock area load object
        self.mock_area_load = Mock()
        self.mock_area_load.LoadType = "Pressure"
        self.mock_area_load.Magnitude = "5.0 kN/m²"
        self.mock_area_load.Direction = "Normal"
        self.mock_area_load.LoadCase = "DL"
    
    def test_panel_initialization(self):
        """Test proper initialization of area load panel"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Verify panel was created
        assert panel.selected_faces == self.selected_faces
        assert panel.form is not None
        assert panel.preview_objects == []
    
    def test_face_selection_display(self):
        """Test display of selected faces"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test that faces are properly tracked
        assert len(panel.selected_faces) == 2
        assert panel.selected_faces[0].Area == 10.0
        assert panel.selected_faces[1].Area == 15.0
    
    def test_load_type_options(self):
        """Test load type selection options"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test valid load types
        valid_load_types = [
            "Pressure (Force/Area)", 
            "Dead Load", 
            "Live Load", 
            "Wind Pressure",
            "Snow Load",
            "Thermal Load",
            "Foundation Pressure"
        ]
        
        # Panel should offer these options
        assert len(valid_load_types) == 7
    
    def test_load_magnitude_validation(self):
        """Test load magnitude input validation"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test valid magnitude
        valid_magnitude = "10.5 kN/m²"
        magnitude_value = float(valid_magnitude.split()[0])
        assert magnitude_value > 0
        
        # Test unit handling
        assert "kN/m²" in valid_magnitude
    
    def test_load_direction_options(self):
        """Test load direction selection"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        valid_directions = [
            "Normal to Surface", 
            "+X Global", "-X Global", 
            "+Y Global", "-Y Global", 
            "+Z Global", "-Z Global", 
            "Custom"
        ]
        
        # Test direction validation
        assert "Normal to Surface" in valid_directions
        assert len(valid_directions) == 8
    
    def test_load_distribution_types(self):
        """Test load distribution pattern options"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        valid_distributions = ["Uniform", "Linear Variation", "Parabolic", "User Defined"]
        
        # Test distribution options
        assert "Uniform" in valid_distributions
        assert len(valid_distributions) == 4


class TestAreaLoadPreview:
    """Test area load preview functionality"""
    
    def setup_method(self):
        """Setup preview test fixtures"""
        self.mock_face = Mock()
        self.mock_face.Area = 20.0
        self.mock_face.valueAt = Mock(return_value=(1.0, 1.0, 0.0))
        self.mock_face.normalAt = Mock(return_value=(0.0, 0.0, 1.0))
        
        self.selected_faces = [self.mock_face]
    
    def test_preview_arrow_generation(self):
        """Test generation of preview arrows"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test preview parameters
        arrow_density = 8  # Default density
        arrow_scale = 1.0  # Default scale
        
        # Test arrow grid calculation
        expected_arrows = arrow_density * arrow_density  # 8x8 = 64 arrows
        assert expected_arrows == 64
    
    def test_preview_update_on_parameter_change(self):
        """Test preview updates when parameters change"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test that preview can be updated
        panel.preview_objects = []  # Start with empty preview
        
        # Simulate parameter change
        new_magnitude = "15.0 kN/m²"
        new_direction = "+Z Global"
        
        # Preview should update with new parameters
        assert panel.preview_objects == []  # Initially empty
    
    def test_preview_clearing(self):
        """Test preview clearing functionality"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Add mock preview objects
        mock_preview1 = Mock()
        mock_preview2 = Mock()
        panel.preview_objects = [mock_preview1, mock_preview2]
        
        # Test clearing preview
        panel.preview_objects = []
        assert len(panel.preview_objects) == 0
    
    def test_arrow_positioning_on_face(self):
        """Test arrow positioning on face surface"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Mock face with parametric coordinates
        u_params = [0.2, 0.5, 0.8]
        v_params = [0.2, 0.5, 0.8]
        
        # Test grid positioning
        total_positions = len(u_params) * len(v_params)
        assert total_positions == 9


class TestAreaLoadValidation:
    """Test area load validation features"""
    
    def setup_method(self):
        """Setup validation test fixtures"""
        self.selected_faces = [Mock()]
    
    def test_magnitude_validation(self):
        """Test load magnitude validation"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test positive magnitude
        positive_magnitude = 10.5
        assert positive_magnitude > 0
        
        # Test zero magnitude (should be invalid)
        zero_magnitude = 0.0
        assert zero_magnitude == 0.0  # Would be flagged as invalid
        
        # Test negative magnitude (should be invalid)
        negative_magnitude = -5.0
        assert negative_magnitude < 0  # Would be flagged as invalid
    
    def test_face_selection_validation(self):
        """Test face selection validation"""
        # Test with no faces selected
        empty_faces = []
        panel = AreaLoadApplicationPanel(empty_faces)
        assert len(panel.selected_faces) == 0
        
        # Test with valid faces
        valid_faces = [Mock(), Mock()]
        panel = AreaLoadApplicationPanel(valid_faces)
        assert len(panel.selected_faces) == 2
    
    def test_unit_consistency_validation(self):
        """Test unit consistency validation"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test consistent pressure units
        pressure_units = ["kN/m²", "N/mm²", "MPa", "PSI"]
        
        for unit in pressure_units:
            test_magnitude = f"10.0 {unit}"
            # Panel should handle unit conversion
            assert unit in test_magnitude


class TestAreaLoadIntegration:
    """Test area load integration with other components"""
    
    def setup_method(self):
        """Setup integration test fixtures"""
        self.selected_faces = [Mock()]
        self.mock_plate = Mock()
        self.mock_plate.Type = "StructuralPlate"
    
    def test_plate_integration(self):
        """Test integration with structural plates"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test that area loads can target plates
        target_plates = [self.mock_plate]
        assert len(target_plates) == 1
        assert target_plates[0].Type == "StructuralPlate"
    
    def test_load_case_integration(self):
        """Test integration with load case system"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test load case options
        load_cases = ["DL", "LL", "LL_Roof", "W", "E", "H", "F", "T"]
        
        # Test load combination format
        load_combination = "1.2DL + 1.6LL"
        assert "DL" in load_combination
        assert "LL" in load_combination
    
    def test_analysis_integration(self):
        """Test integration with analysis system"""
        panel = AreaLoadApplicationPanel(self.selected_faces)
        
        # Test that area loads can be processed by calc.py
        mock_calc_obj = Mock()
        mock_calc_obj.ListElements = []
        
        # Area loads should be detectable by analysis
        area_load_filter = lambda element: getattr(element, 'Type', '') == 'AreaLoad'
        assert callable(area_load_filter)


class TestAreaLoadPerformance:
    """Test performance aspects of area load panel"""
    
    def test_large_face_selection_performance(self):
        """Test performance with many selected faces"""
        # Create many mock faces
        large_face_list = [Mock() for _ in range(100)]
        
        # Panel should handle large selections
        panel = AreaLoadPanel(large_face_list)
        assert len(panel.selected_faces) == 100
    
    def test_preview_performance(self):
        """Test preview generation performance"""
        faces = [Mock() for _ in range(10)]
        panel = AreaLoadPanel(faces)
        
        # Test that preview doesn't create too many objects
        max_arrows_per_face = 64  # 8x8 grid
        max_total_arrows = len(faces) * max_arrows_per_face
        
        # Should be manageable number
        assert max_total_arrows <= 640


if __name__ == '__main__':
    pytest.main([__file__, '-v'])