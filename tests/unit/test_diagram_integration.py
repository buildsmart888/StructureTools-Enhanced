import types
import builtins
import pytest

# ensure FreeCADGui has addCommand so importing diagram (which registers the command)
# does not crash in the headless test environment
import FreeCADGui
if not hasattr(FreeCADGui, 'addCommand'):
    FreeCADGui.addCommand = lambda *a, **k: None

from freecad.StructureTools import diagram


class DummyVertex:
    def __init__(self, x, y, z):
        class P: pass
        self.Point = types.SimpleNamespace(x=x, y=y, z=z)


class DummyEdge:
    def __init__(self, v1, v2):
        self.Vertexes = [v1, v2]


class DummyElement:
    def __init__(self, name, edges):
        self.Name = name
        self.Shape = types.SimpleNamespace(Edges=edges)
        self.RotationSection = types.SimpleNamespace(getValueAs=lambda unit: 0)


class DummyObjCalc:
    def __init__(self):
        self.NumPointsMoment = 3
        self.NumPointsShear = 3
        self.NumPointsTorque = 3
        self.NumPointsAxial = 3
        self.NameMembers = []


class DummyObj:
    def __init__(self):
        self.ObjectBaseCalc = types.SimpleNamespace(MomentZ=[], MomentY=[], ShearY=[], ShearZ=[], Torque=[], AxialForce=[], NumPointsMoment=3, NumPointsShear=3, NumPointsTorque=3, NumPointsAxial=3, NameMembers=[])
        self.ObjectBaseElements = []
        self.Color = (1,0,0)
        self.Transparency = 0
        self.ViewObject = types.SimpleNamespace(LineWidth=1, PointSize=1, LineColor=(0,0,0), PointColor=(0,0,0), ShapeAppearance=None)


@pytest.fixture
def mock_part(monkeypatch):
    calls = {}

    class FakeShape:
        def __init__(self):
            self.Area = 1

    class FakePart:
        @staticmethod
        def LineSegment(a, b):
            calls['line_segment'] = calls.get('line_segment', 0) + 1
            return types.SimpleNamespace(toShape=lambda: 'edge')

        @staticmethod
        def Wire(edges):
            calls['wire'] = calls.get('wire', 0) + 1
            return 'wire'

        @staticmethod
        def Face(wire):
            calls['face'] = calls.get('face', 0) + 1
            return FakeShape()

        @staticmethod
        def makeCompound(items):
            calls['compound'] = calls.get('compound', 0) + 1
            # return a fake element that implements translate/transformGeometry/mirror
            class FakeElement:
                def __init__(self):
                    self.Placement = None

                def translate(self, v):
                    return self

                def transformGeometry(self, mat):
                    return self

                def mirror(self, p, v):
                    return self

            return FakeElement()

        @staticmethod
        def makeWireString(string, font, height):
            calls['makeWireString'] = calls.get('makeWireString', 0) + 1
            return []

    monkeypatch.setattr(diagram, 'Part', FakePart)
    return calls


def test_make_diagram_calls_part(monkeypatch, mock_part):
    # prepare minimal geometry: one element with one edge between two vertices
    v1 = types.SimpleNamespace(Point=types.SimpleNamespace(x=0, y=0, z=0))
    v2 = types.SimpleNamespace(Point=types.SimpleNamespace(x=1, y=0, z=0))
    edge = types.SimpleNamespace(Vertexes=[v1, v2])
    element = types.SimpleNamespace(Name='Line1', Shape=types.SimpleNamespace(Edges=[edge]), RotationSection=types.SimpleNamespace(getValueAs=lambda u: 0))

    objCalc = types.SimpleNamespace(MomentZ=["1,0, -1"], MomentY=[], ShearY=[], ShearZ=[], Torque=[], AxialForce=[], NumPointsMoment=3, NumPointsShear=3, NumPointsTorque=3, NumPointsAxial=3, NameMembers=['Line1_0'])
    obj = types.SimpleNamespace(ObjectBaseCalc=objCalc, ObjectBaseElements=[] , Color=(1,0,0), Transparency=0, ViewObject=types.SimpleNamespace(LineWidth=1, PointSize=1, LineColor=(0,0,0), PointColor=(0,0,0), ShapeAppearance=None))

    # create a minimal fake FreeCAD object with addProperty used by Diagram.__init__
    class FakeObj:
        def __init__(self):
            self.ViewObject = types.SimpleNamespace(LineWidth=1, PointSize=1, LineColor=(0,0,0), PointColor=(0,0,0), ShapeAppearance=None)

        def addProperty(self, *args, **kwargs):
            # create a writable attribute name on self and return self so chained
            # assignments (like .ObjectBaseCalc = ...) work in Diagram.__init__
            # args[1] is usually the property name
            name = args[1] if len(args) > 1 else 'prop'
            setattr(self, name, None)
            return self

    fake_obj = FakeObj()
    # pass a non-empty listSelection to avoid Diagram.getMembers scanning FreeCAD.ActiveDocument
    selection = types.SimpleNamespace(Object=element, SubElementNames=['Edge1'])
    # monkeypatch minimal FreeCAD classes used by diagram.rotate on the diagram module
    class FakeVector:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def normalize(self):
            return None

        def __eq__(self, other):
            return (round(self.x, 6), round(self.y, 6), round(self.z, 6)) == (
                round(other.x, 6), round(other.y, 6), round(other.z, 6)
            )

    class FakeRotation:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class FakePlacement:
        def __init__(self, position, rotation):
            self.position = position
            self.rotation = rotation

        def toMatrix(self):
            return 'matrix'

    diagram.FreeCAD.Vector = FakeVector
    diagram.FreeCAD.Rotation = FakeRotation
    diagram.FreeCAD.Placement = FakePlacement
    diagram.FreeCAD.Material = lambda **kwargs: None

    d = diagram.Diagram(fake_obj, objCalc, [selection])
    # call makeDiagram directly with simplified matrices/nodes/members
    nodes = [[0,0,0], [1,0,0]]
    members = {'Line1_0': {'nodes': ['0','1'], 'RotationSection': 0}}
    orderMembers = [(0, 'Line1_0')]
    # use small matrix: 1 member, 3 points
    matrix = [[1.0, 0.0, -1.0]]

    d.makeDiagram(matrix, nodes, members, orderMembers, 3, 0, 1.0, 10, 2, True)

    # assert key Part methods were called
    assert mock_part.get('line_segment', 0) > 0
    assert mock_part.get('face', 0) > 0
    assert mock_part.get('compound', 0) > 0
    assert mock_part.get('makeWireString', 0) >= 0
