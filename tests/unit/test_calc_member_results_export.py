import types
import sys

# setup minimal fake FreeCAD modules
fake_modules = {}
for name in ('FreeCAD', 'App', 'FreeCADGui', 'Part'):
    fake_modules[name] = types.ModuleType(name)
sys.modules.update(fake_modules)

class _Quantity:
    def __init__(self, value, unit=None):
        try:
            self.value = float(value)
        except Exception:
            self.value = 0.0
    def getValueAs(self, unit):
        return self.value

FreeCAD = sys.modules['FreeCAD']
FreeCAD.Units = types.SimpleNamespace(Quantity=_Quantity)
FreeCAD.Vector = lambda x,y,z: (x,y,z)
FreeCADGui = sys.modules['FreeCADGui']
FreeCADGui.addCommand = lambda *a, **k: None

from freecad.StructureTools.calc import Calc

class DummyMember:
    def __init__(self, name):
        self.name = name
    def moment_array(self, axis, n):
        return (list(range(n)), [1.0]*n)
    def shear_array(self, axis, n):
        return (list(range(n)), [2.0]*n)
    def axial_array(self, n):
        return (list(range(n)), [3.0]*n)
    def torque_array(self, n):
        return (list(range(n)), [4.0]*n)
    def deflection_array(self, axis, n):
        return (list(range(n)), [0.1]*n)
    def min_moment(self, axis): return -1.0
    def max_moment(self, axis): return 1.0
    def min_shear(self, axis): return -2.0
    def max_shear(self, axis): return 2.0
    def min_torque(self): return -3.0
    def max_torque(self): return 3.0
    def min_deflection(self, axis): return -0.5
    def max_deflection(self, axis): return 0.5

class DummyModel:
    def __init__(self):
        self.members = {'A': DummyMember('A')}
        self.plates = {}
        self.quads = {}
    def analyze(self):
        return True

class DummyObj:
    def __init__(self):
        self.ListElements = []
        self.LengthUnit = 'm'
        self.ForceUnit = 'kN'
        self.NumPointsMoment = 3
        self.NumPointsShear = 3
        self.NumPointsAxial = 2
        self.NumPointsTorque = 2
        self.NumPointsDeflection = 2
        self.selfWeight = False
        self.LoadCombination = '100_DL'


def test_export_helpers(monkeypatch):
    dummy = DummyModel()
    monkeypatch.setattr('freecad.StructureTools.calc.FEModel3D', lambda: dummy)
    obj = DummyObj()
    calc = Calc(obj, elements=[])
    calc.execute(obj)
    # JSON
    j = calc.member_results_to_json(obj)
    assert '"name": "A"' in j or '"name":"A"' in j
    # CSV
    csv = calc.member_results_to_csv(obj)
    assert 'name' in csv.splitlines()[0]
    assert 'A' in csv
