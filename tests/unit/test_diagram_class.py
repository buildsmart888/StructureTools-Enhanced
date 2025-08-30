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


class TestDiagramClass:
    """Test cases for the Diagram class methods."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Reset mocks
        mock_freecad.reset_mock()
        mock_part.reset_mock()
        mock_freecad_gui.reset_mock()
        
        # Create a mock object for the diagram
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock(return_value=self.mock_obj)
        
        # Create a mock calculation object
        self.mock_obj_calc = Mock()
        self.mock_obj_calc.NameMembers = ['Line1_0', 'Line2_0']
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

    def test_init(self):
        """Test Diagram class initialization."""
        # Create diagram instance
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Verify that addProperty was called with correct parameters
        assert self.mock_obj.addProperty.called
        # Verify that the diagram object was set up with default values
        assert hasattr(diagram, 'separatesOrdinates')
        assert hasattr(diagram, 'generateCoordinates')

    def test_get_matrix(self):
        """Test the getMatrix method."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Test with simple matrix data
        param = ["1.0,2.0,3.0", "4.0,5.0,6.0"]
        result = diagram.getMatrix(param)
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0] == [1.0, 2.0, 3.0]
        assert result[1] == [4.0, 5.0, 6.0]

    def test_map_nodes(self):
        """Test the mapNodes method."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Create mock elements with vertices
        mock_vertex1 = Mock()
        mock_vertex1.Point.x = 0.0
        mock_vertex1.Point.y = 0.0
        mock_vertex1.Point.z = 0.0
        
        mock_vertex2 = Mock()
        mock_vertex2.Point.x = 1.0
        mock_vertex2.Point.y = 0.0
        mock_vertex2.Point.z = 0.0
        
        mock_edge = Mock()
        mock_edge.Vertexes = [mock_vertex1, mock_vertex2]
        
        mock_element = Mock()
        mock_element.Shape.Edges = [mock_edge]
        
        elements = [mock_element]
        nodes = diagram.mapNodes(elements, tol=1e-3)
        
        assert isinstance(nodes, list)
        assert len(nodes) == 2
        assert nodes[0] == [0.0, 0.0, 0.0]
        assert nodes[1] == [1.0, 0.0, 0.0]

    def test_filter_members_selected(self):
        """Test the filterMembersSelected method."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Create mock object with no selected elements
        mock_obj = Mock()
        mock_obj.ObjectBaseElements = []
        mock_obj.ObjectBaseCalc = Mock()
        mock_obj.ObjectBaseCalc.NameMembers = ['Line1_0', 'Line2_0']
        
        result = diagram.filterMembersSelected(mock_obj)
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0] == (0, 'Line1_0')
        assert result[1] == (1, 'Line2_0')

    def test_convert_to_thai_units(self):
        """Test the convertToThaiUnits method."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        diagram.UseThaiUnits = True
        
        # Test force conversion
        values = [1.0, 2.0, 3.0]  # kN values
        result = diagram.convertToThaiUnits(values, "force")
        
        assert isinstance(result, list)
        # Since we're mocking, we can't test actual conversion values
        # but we can test that the method returns a list of the same length
        assert len(result) == len(values)

    def test_get_thai_units_label(self):
        """Test the getThaiUnitsLabel method."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        diagram.UseThaiUnits = True
        diagram.ThaiUnitsDisplay = "Auto"
        
        # Test force label
        result = diagram.getThaiUnitsLabel("force")
        # Should return "kgf" by default
        assert isinstance(result, str)

    def test_separates_ordinates(self):
        """Test the separatesOrdinates method."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Test with values that change sign
        values = [1.0, 0.5, -0.2, -0.5, 0.1]
        result = diagram.separatesOrdinates(values)
        
        assert isinstance(result, list)
        assert len(result) >= 2  # Should split into at least 2 groups

    def test_generate_coordinates(self):
        """Test the generateCoordinates method."""
        diagram = Diagram(self.mock_obj, self.mock_obj_calc, self.mock_selection)
        
        # Test with simple ordinate data
        ordinates = [[1.0, -0.5], [0.2]]
        dist = 1.0
        result = diagram.generateCoordinates(ordinates, dist)
        
        assert isinstance(result, list)
        assert all(isinstance(loop, list) for loop in result)

if __name__ == '__main__':
    pytest.main([__file__])