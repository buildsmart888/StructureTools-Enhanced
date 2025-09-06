import types
import sys

# Provide minimal fake FreeCAD/App/FreeCADGui/Part modules for headless tests
fake_modules = {}
for name in ('FreeCAD', 'App', 'FreeCADGui', 'Part'):
    mod = types.ModuleType(name)
    fake_modules[name] = mod
sys.modules.update(fake_modules)

# Minimal FreeCAD.Units.Quantity and Vector implementations used by calc
class _Quantity:
    def __init__(self, value, unit=None):
        # accept numeric or string-like; store numeric if possible
        try:
            self.value = float(value)
        except Exception:
            self.value = 0.0

    def getValueAs(self, unit):
        return self.value

FreeCAD = sys.modules['FreeCAD']
FreeCAD.Units = types.SimpleNamespace(Quantity=_Quantity)
FreeCAD.Vector = lambda x, y, z: (x, y, z)
FreeCADGui = sys.modules['FreeCADGui']
def _noop_add_command(name, cmd):
    return None
FreeCADGui.addCommand = _noop_add_command

from freecad.StructureTools.calc import Calc


class DummyMember:
    def __init__(self, name):
        self.name = name

    def moment_array(self, axis, n):
        # return (x_positions, values)
        return (list(range(n)), [i * 1.0 for i in range(n)])

    def shear_array(self, axis, n):
        return (list(range(n)), [i * 2.0 for i in range(n)])

    def axial_array(self, n):
        return (list(range(n)), [i * 3.0 for i in range(n)])

    def torque_array(self, n):
        return (list(range(n)), [i * 4.0 for i in range(n)])

    def deflection_array(self, axis, n):
        return (list(range(n)), [i * 0.1 for i in range(n)])

    def min_moment(self, axis):
        return -1.0

    def max_moment(self, axis):
        return 1.0

    def min_shear(self, axis):
        return -2.0

    def max_shear(self, axis):
        return 2.0

    def min_torque(self):
        return -3.0

    def max_torque(self):
        return 3.0

    def min_deflection(self, axis):
        return -0.5

    def max_deflection(self, axis):
        return 0.5


class DummyModel:
    def __init__(self):
        self.members = {
            'M1': DummyMember('M1'),
            'M2': DummyMember('M2')
        }
        self.plates = {}
        self.quads = {}

    def analyze(self):
        return True


class DummyObj:
    def __init__(self):
        # minimal attributes the calc.execute expects
        self.ListElements = []
        self.LengthUnit = 'm'
        self.ForceUnit = 'kN'
        self.NumPointsMoment = 4
        self.NumPointsShear = 4
        self.NumPointsAxial = 3
        self.NumPointsTorque = 3
        self.NumPointsDeflection = 3

        # optional attributes used by execute
        self.selfWeight = False
        self.LoadCombination = '100_DL'
        self.LoadSummary = []
        self.TotalLoads = 0


def test_member_results_structure(monkeypatch):
    dummy_model = DummyModel()

    # monkeypatch FEModel3D constructor to return our dummy model
    def fake_FEModel3D():
        return dummy_model

    monkeypatch.setattr('freecad.StructureTools.calc.FEModel3D', fake_FEModel3D)

    obj = DummyObj()
    calc = Calc(obj, elements=[])

    # execute should populate MemberResults
    calc.execute(obj)

    assert hasattr(obj, 'MemberResults')
    assert isinstance(obj.MemberResults, list)
    assert len(obj.MemberResults) == 2

    first = obj.MemberResults[0]
    assert first['name'] in ('M1', 'M2')
    assert 'momentY' in first and isinstance(first['momentY'], list)
    assert 'momentZ' in first and isinstance(first['momentZ'], list)
    assert 'shearY' in first and isinstance(first['shearY'], list)
    assert 'axial' in first and isinstance(first['axial'], list)
    assert 'deflectionY' in first and isinstance(first['deflectionY'], list)
    assert first['minMomentY'] == -1.0
    assert first['maxTorque'] == 3.0
