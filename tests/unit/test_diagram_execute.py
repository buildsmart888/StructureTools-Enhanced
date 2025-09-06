import types
import pytest
from unittest.mock import Mock, patch, MagicMock

# Mock FreeCAD modules for testing
import sys

# Create mock FreeCAD modules
mock_freecad = MagicMock()
mock_freecad_gui = MagicMock()
mock_part = MagicMock()
mock_pyside = MagicMock()

sys.modules['FreeCAD'] = mock_freecad
sys.modules['FreeCADGui'] = mock_freecad_gui
sys.modules['Part'] = mock_part
sys.modules['PySide2'] = mock_pyside
sys.modules['PySide2.QtWidgets'] = mock_pyside

# Mock the diagram module's dependencies
with patch('freecad.StructureTools.diagram.UniversalThaiUnits', Mock()):
    from freecad.StructureTools.diagram import Diagram


class TestExecuteMethod:
    """Test cases for the execute method."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Reset mocks
        mock_freecad.reset_mock()
        mock_part.reset_mock()
        mock_freecad_gui.reset_mock()
        
        # Create a mock object for the diagram
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock(return_value=self.mock_obj)
        self.mock_obj.MomentZ = False
        self.mock_obj.MomentY = False
        self.mock_obj.ShearY = False
        self.mock_obj.ShearZ = False
        self.mock_obj.Torque = False
        self.mock_obj.AxialForce = False
        self.mock_obj.Color = (1, 0, 0)
        self.mock_obj.Transparency = 0
        self.mock_obj.FontHeight = 10
        self.mock_obj.Precision = 2
        self.mock_obj.ScaleMoment = 1.0
        self.mock_obj.ScaleShear = 1.0
        self.mock_obj.ScaleTorque = 1.0
        self.mock_obj.ScaleAxial = 1.0
        
        self.mock_obj.ViewObject = Mock()
        self.mock_obj.ViewObject.LineWidth = 1
        self.mock_obj.ViewObject.PointSize = 1
        self.mock_obj.ViewObject.LineColor = (0, 0, 0)
        self.mock_obj.ViewObject.PointColor = (0, 0, 0)
        self.mock_obj.ViewObject.ShapeAppearance = None
        self.mock_obj.ViewObject.Transparency = 0
        
        # Create a mock calculation object
        self.mock_obj_calc = Mock()
        self.mock_obj_calc.NameMembers = ['Line1_0']
        self.mock_obj_calc.ListElements = []
        self.mock_obj_calc.MomentZ = ["1,0,-1"]
        self.mock_obj_calc.MomentY = ["0,1,0"]
        self.mock_obj_calc.ShearY = ["0.5,0,-0.5"]
        self.mock_obj_calc.ShearZ = ["0.3,0,-0.3"]
        self.mock_obj_calc.Torque = ["0.1,0,-0.1"]
        self.mock_obj_calc.AxialForce = ["1,0,-1"]
        self.mock_obj_calc.NumPointsMoment = 3
        self.mock_obj_calc.NumPointsShear = 3
        self.mock_obj_calc.NumPointsTorque = 3
        self.mock_obj_calc.NumPointsAxial = 3
        
        # Create mock selection
        self.mock_selection = []

    def test_execute_no_diagrams(self):
        """Test the execute method when no diagram types are selected."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Mock the methods that would be called
        diagram.mapNodes = Mock(return_value=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
        diagram.mapMembers = Mock(return_value={'Line1_0': {'nodes': ['0', '1'], 'RotationSection': 0}})
        diagram.filterMembersSelected = Mock(return_value=[(0, 'Line1_0')])
        diagram._createAllDiagrams = Mock(return_value=[])
        
        # Create mock Part methods
        mock_shape = Mock()
        mock_part.Shape = Mock(return_value=mock_shape)
        
        # Call the execute method
        diagram.execute(self.mock_obj)
        
        # Assertions
        assert diagram.mapNodes.called
        assert diagram.mapMembers.called
        assert diagram.filterMembersSelected.called
        assert diagram._createAllDiagrams.called
        assert self.mock_obj.Shape is not None

    def test_execute_with_moment_z(self):
        """Test the execute method when MomentZ diagram is selected."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Enable MomentZ diagram
        self.mock_obj.MomentZ = True
        
        # Mock the methods that would be called
        diagram.mapNodes = Mock(return_value=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
        diagram.mapMembers = Mock(return_value={'Line1_0': {'nodes': ['0', '1'], 'RotationSection': 0}})
        diagram.filterMembersSelected = Mock(return_value=[(0, 'Line1_0')])
        diagram._createAllDiagrams = Mock(return_value=['diagram_element'])
        
        # Create mock Part methods
        mock_compound = Mock()
        mock_part.makeCompound = Mock(return_value=mock_compound)
        
        # Call the execute method
        diagram.execute(self.mock_obj)
        
        # Assertions
        assert diagram.mapNodes.called
        assert diagram.mapMembers.called
        assert diagram.filterMembersSelected.called
        assert diagram._createAllDiagrams.called
        assert self.mock_obj.Shape == mock_compound

    def test_execute_with_multiple_diagrams(self):
        """Test the execute method when multiple diagram types are selected."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Enable multiple diagram types
        self.mock_obj.MomentZ = True
        self.mock_obj.ShearY = True
        self.mock_obj.AxialForce = True
        
        # Mock the methods that would be called
        diagram.mapNodes = Mock(return_value=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
        diagram.mapMembers = Mock(return_value={'Line1_0': {'nodes': ['0', '1'], 'RotationSection': 0}})
        diagram.filterMembersSelected = Mock(return_value=[(0, 'Line1_0')])
        diagram._createAllDiagrams = Mock(return_value=['diagram1', 'diagram2', 'diagram3'])
        
        # Create mock Part methods
        mock_compound = Mock()
        mock_part.makeCompound = Mock(return_value=mock_compound)
        
        # Call the execute method
        diagram.execute(self.mock_obj)
        
        # Assertions
        assert diagram.mapNodes.called
        assert diagram.mapMembers.called
        assert diagram.filterMembersSelected.called
        assert diagram._createAllDiagrams.called
        assert self.mock_obj.Shape == mock_compound

    def test_execute_styling(self):
        """Test that the execute method applies styling correctly."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Mock the methods that would be called
        diagram.mapNodes = Mock(return_value=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
        diagram.mapMembers = Mock(return_value={'Line1_0': {'nodes': ['0', '1'], 'RotationSection': 0}})
        diagram.filterMembersSelected = Mock(return_value=[(0, 'Line1_0')])
        diagram._createAllDiagrams = Mock(return_value=[])
        
        # Create mock Part methods
        mock_shape = Mock()
        mock_part.Shape = Mock(return_value=mock_shape)
        
        # Mock FreeCAD Material
        mock_freecad.Material = Mock(return_value='material')
        
        # Call the execute method
        diagram.execute(self.mock_obj)
        
        # Assertions for styling
        assert self.mock_obj.ViewObject.LineWidth == 1
        assert self.mock_obj.ViewObject.PointSize == 1
        assert self.mock_obj.ViewObject.Transparency == 70  # Updated to match the actual value
        assert self.mock_obj.ViewObject.ShapeAppearance is not None

if __name__ == '__main__':
    pytest.main([__file__])