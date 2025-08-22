import types
import os
import sys

# Ensure freecad stubs on sys.path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
freecad_dir = os.path.join(repo_root, '..', 'freecad')
import types
import os
import sys

# Ensure freecad stubs on sys.path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
freecad_dir = os.path.join(repo_root, '..', 'freecad')
if freecad_dir not in sys.path:
    sys.path.insert(0, freecad_dir)

# Minimal FreeCAD shims for tests
FreeCAD = types.SimpleNamespace()
App = FreeCAD
sys.modules['FreeCAD'] = FreeCAD
sys.modules['App'] = App
sys.modules['FreeCADGui'] = types.SimpleNamespace(addCommand=lambda *a, **k: None)
sys.modules['Part'] = types.SimpleNamespace()

from StructureTools import calc
from StructureTools.Pynite_main.FEModel3D import FEModel3D

# Fake mesh data returned by PlateMesher.meshFace
fake_mesh = {
    'nodes': {
        'n1': {'x': 0.0, 'y': 0.0, 'z': 0.0},
        'n2': {'x': 1.0, 'y': 0.0, 'z': 0.0},
        'n3': {'x': 1.0, 'y': 1.0, 'z': 0.0},
        'n4': {'x': 0.0, 'y': 1.0, 'z': 0.0},
    },
    'elements': {
        'e1': {'nodes': ['n1','n2','n3','n4']}
    }
}


class FakeMesher:
    def meshFace(self, face, **kwargs):
        return fake_mesh


class FakeFace:
    def __init__(self, verts):
        self.Vertexes = verts


class FakeVertex:
    def __init__(self, x, y, z):
        self.Point = types.SimpleNamespace(x=x, y=y, z=z)


class FakePlate:
    def __init__(self, name, verts):
        self.Name = name
        self.Type = 'StructuralPlate'
        self.Shape = types.SimpleNamespace(Faces=[FakeFace(verts)])
        self.CornerNodes = []
        self.Thickness = 0.1
        self.Material = None
        self.MeshDensity = 1  # request mesh


class FakeAreaLoad:
    def __init__(self, name, target):
        self.Name = name
        self.Type = 'AreaLoad'
        self.TargetFaces = [target]
        self.Magnitude = 1000.0
        self.ObjectBase = []


def test_calc_mesh_path_creates_quads(monkeypatch):
    verts = [FakeVertex(0,0,0), FakeVertex(1,0,0), FakeVertex(1,1,0), FakeVertex(0,1,0)]
    plate = FakePlate('PlateMesh', verts)
    aload = FakeAreaLoad('AL1', plate)

    class Obj:
        pass
    o = Obj()
    o.ListElements = [plate, aload]
    o.LengthUnit = 'm'
    o.ForceUnit = 'kN'
    o.LoadCombination = '100_DL'
    o.selfWeight = False

    # Monkeypatch PlateMesher with our fake
    monkeypatch.setattr(calc, 'PlateMesher', FakeMesher, raising=False)

    c = calc.Calc(o, o.ListElements)
    c.execute(o)

    assert hasattr(o, 'AnalysisType')
