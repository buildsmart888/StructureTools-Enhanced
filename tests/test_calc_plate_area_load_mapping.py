import importlib
import types

import pytest

# Import the calc module under test
from freecad.StructureTools import calc

class MockFEModel:
    def __init__(self):
        self.nodes = []
        self.quads = {}
        self.plates = {}
        self.materials = {}
        self.added_quads = []
        self.added_quad_pressures = []

    def add_node(self, name, x, y, z):
        nid = str(len(self.nodes))
        self.nodes.append((nid, (x, y, z)))
        return nid

    def add_material(self, name, E, G, nu, density):
        self.materials[name] = (E, G, nu, density)

    def add_quad(self, name, i, j, m, n, thk, mat_name):
        self.quads[name] = {'nodes': (i, j, m, n), 'thk': thk, 'mat': mat_name, 'pressures': []}
        self.added_quads.append(name)

    def add_quad_surface_pressure(self, quad_name, pressure, case='Case 1'):
        if quad_name in self.quads:
            self.quads[quad_name]['pressures'].append((pressure, case))
        self.added_quad_pressures.append((quad_name, pressure, case))


class FakePlateProxy:
    def to_calc_payload(self, obj, length_unit='mm'):
        # simple single quad mesh with 4 nodes
        return {
            'name': obj.Name,
            'nodes': {
                'n1': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                'n2': {'x': 1000.0, 'y': 0.0, 'z': 0.0},
                'n3': {'x': 1000.0, 'y': 1000.0, 'z': 0.0},
                'n4': {'x': 0.0, 'y': 1000.0, 'z': 0.0},
            },
            'elements': {'e1': {'nodes': ['n1', 'n2', 'n3', 'n4']}},
            'thickness': 10.0,
            'material': 'default',
            'area': 1000000.0,
        }

class FakeAreaLoadProxy:
    def to_solver_loads(self, obj, mesh_payload=None, force_unit='kN', length_unit='mm'):
        # return a per-element pressure entry matching the expected created element name
        # mesh_payload may contain element keys like 'P1_e1'
        if mesh_payload and 'elements' in mesh_payload:
            # take the first key and return a pressure
            first = next(iter(mesh_payload['elements'].keys()))
            return {'entries': [{'element': first, 'pressure': 5.0}], 'total_force': 5.0}
        return {'entries': [], 'total_force': 0.0}

class DummyObj:
    def __init__(self, list_elements, length_unit='mm', force_unit='kN'):
        self.ListElements = list_elements
        self.LengthUnit = length_unit
        self.ForceUnit = force_unit

class SimpleElement:
    def __init__(self, name, type_name, proxy):
        self.Name = name
        self.Type = type_name
        self.Proxy = proxy


def test_plate_mesh_and_area_load_mapping(monkeypatch):
    # Monkeypatch FEModel3D used by calc to use our mock
    monkeypatch.setattr(calc, 'FEModel3D', MockFEModel)

    # Create plate and area-load elements
    plate = SimpleElement('P1', 'StructuralPlate', FakePlateProxy())
    aload = SimpleElement('AL1', 'AreaLoad', FakeAreaLoadProxy())

    # Document-like object passed to Calc.execute
    obj = DummyObj([plate, aload])

    calc_inst = calc.Calc()
    # Execute the calc which should create the model inside calc_inst.model
    calc_inst.execute(obj)

    model = getattr(calc_inst, 'model', None)
    assert model is not None, "Model was not created"

    # Expect a quad named P1_e1 to be created
    assert 'P1_e1' in model.quads
    # Expect pressure applied to that quad
    applied = [p for p in model.added_quad_pressures if p[0] == 'P1_e1']
    assert applied, "No pressure applied to P1_e1"
    assert applied[0][1] == 5.0
*** End Patch
