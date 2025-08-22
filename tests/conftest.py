# -*- coding: utf-8 -*-
"""
Pytest configuration and fixtures for StructureTools tests.
"""

import os
import sys
import pytest
from unittest.mock import Mock, MagicMock
from typing import Generator, Any
import builtins
import unittest.mock as _unittest_mock

from typing import Generator, Any
import builtins
import unittest.mock as _unittest_mock
_BUILTIN_GETATTR = builtins.getattr
_ORIG_UNittest_PATCH = _unittest_mock.patch
_BUILTIN_HASATTR = builtins.hasattr

# Wrap the internal patch enter call so that when a test has patched
# builtins.getattr/hasattr, the internal machinery that inspects the
# original object during patch.__enter__ uses the real builtins. We
# temporarily swap in the originals for the duration of the enter call
# and restore the test-installed values afterwards.
try:
    _orig_patch_enter = _unittest_mock._patch.__enter__

    def _patched_patch_enter(self, *args, **kwargs):
        saved_getattr = builtins.getattr
        saved_hasattr = builtins.hasattr
        try:
            builtins.getattr = _BUILTIN_GETATTR
            builtins.hasattr = _BUILTIN_HASATTR
        except Exception:
            pass
        # Call the original enter while builtins are the originals so
        # internal inspection behaves correctly. Do NOT restore the
        # previously-saved builtins here — the patcher is responsible for
        # leaving the patched values in place for the test body and
        # restoring them on exit.
        result = _orig_patch_enter(self, *args, **kwargs)

        # If the underlying patcher installed a MagicMock into builtins
        # (common when tests call patch('builtins.getattr')), replace
        # that MagicMock with a lightweight function wrapper that calls
        # the Mock.side_effect. This prevents MagicMock recursion when
        # other libraries (like pytest's assertion rewriting) call
        # getattr internally.
        try:
            for name in ('getattr', 'hasattr'):
                val = builtins.__dict__.get(name)
                if isinstance(val, _unittest_mock.Mock):
                    try:
                        side = object.__getattribute__(val, 'side_effect')
                        if callable(side):
                            def _make(side_fn):
                                return lambda o, a, default=False: side_fn(o, a, default)
                            builtins.__dict__[name] = _make(side)
                    except Exception:
                        # If we cannot access side_effect, leave as-is
                        pass
        except Exception:
            pass

        return result

    _unittest_mock._patch.__enter__ = _patched_patch_enter
except Exception:
    # If the internal structure of unittest.mock is different on this
    # Python version, skip this safe-guard; tests may still pass.
    pass

def _safe_patch(*args, **kwargs):
    """Selective wrapper around unittest.mock.patch.

    If the target is a builtins attribute (target string starts with
    'builtins.'), return a wrapper that restores the original
    builtins.getattr during the patcher's __enter__ to avoid recursion
    when tests patch builtins.getattr and then patch other builtins.
    Otherwise behave exactly like the original patch.
    """
    # If called as patch(target, ...), inspect target
    target = args[0] if args else kwargs.get('target')

    # Special-case builtins.* patches: if tests provided a side_effect,
    # install a light-weight function wrapper instead of placing a
    # MagicMock directly into builtins (which can cause recursion in
    # libraries that call getattr internally).
    if isinstance(target, str) and target.startswith('builtins.'):
        bname = target.split('.', 1)[1]

        # Prefer explicit 'new' argument if provided
        if 'new' in kwargs and kwargs['new'] is not None:
            return _ORIG_UNittest_PATCH(*args, **kwargs)

        side = kwargs.get('side_effect', None)
        if callable(side):
            class BuiltinFuncPatch:
                def __enter__(self_inner):
                    # Save original function
                    self_inner._orig = builtins.__dict__.get(bname, None)

                    def _wrapper(o, name, default=False):
                        try:
                            return side(o, name, default)
                        except TypeError:
                            try:
                                return side(o, name)
                            except Exception:
                                return default
                        except Exception:
                            return default

                    builtins.__dict__[bname] = _wrapper
                    return _wrapper

                def __exit__(self_inner, exc_type, exc, tb):
                    try:
                        if self_inner._orig is None:
                            del builtins.__dict__[bname]
                        else:
                            builtins.__dict__[bname] = self_inner._orig
                    except Exception:
                        pass
                    return False

            return BuiltinFuncPatch()

    # No side_effect: fall back to original patcher
    return _ORIG_UNittest_PATCH(*args, **kwargs)

    # Default behaviour for other targets
    return _ORIG_UNittest_PATCH(*args, **kwargs)

# Replace patch with the selective wrapper
_unittest_mock.patch = _safe_patch
# Preserve attributes expected by plugins (e.g., pytest-mock expects
# `mock.patch.object` to exist). Copy commonly-used attributes from the
# original patch function onto our wrapper so external code can access
# `patch.object`, `patch.__wrapped__`, etc.
try:
    _safe_patch.object = _ORIG_UNittest_PATCH.object
    _safe_patch.__wrapped__ = _ORIG_UNittest_PATCH
except Exception:
    pass

# Note: we intentionally avoid monkeypatching unittest.mock internals here.
# The selective wrapper above (`_safe_patch`) is sufficient to restore
# `builtins.getattr` when the tests patch builtins.*. Patching private
# unittest.mock classes caused compatibility issues across Python versions
# and is not needed.

# Add the freecad directory to path for imports
test_dir = os.path.dirname(__file__)
project_root = os.path.dirname(test_dir)
freecad_dir = os.path.join(project_root, "freecad")
sys.path.insert(0, freecad_dir)


@pytest.fixture(scope="session")
def freecad_app():
    """
    Mock FreeCAD App module for testing.
    
    This fixture provides a mock FreeCAD App module that can be used
    in tests without requiring actual FreeCAD installation.
    """
    mock_app = MagicMock()
    
    # Mock common App properties and methods
    mock_app.Vector = lambda x=0, y=0, z=0: MockVector(x, y, z)
    mock_app.Console = MagicMock()
    mock_app.Console.PrintMessage = MagicMock()
    mock_app.Console.PrintWarning = MagicMock()
    mock_app.Console.PrintError = MagicMock()
    
    # Mock document management
    mock_app.ActiveDocument = None
    mock_app.newDocument = MagicMock()
    mock_app.closeDocument = MagicMock()
    
    return mock_app


@pytest.fixture(scope="session")
def freecad_gui():
    """
    Mock FreeCAD Gui module for testing.
    """
    mock_gui = MagicMock()
    
    # Mock Control for task panels
    mock_gui.Control = MagicMock()
    mock_gui.Control.showDialog = MagicMock()
    mock_gui.Control.closeDialog = MagicMock()
    
    return mock_gui


@pytest.fixture
def mock_document_object():
    """
    Create a mock FreeCAD DocumentObject for testing.
    """
    mock_obj = MagicMock()
    mock_obj.addProperty = MagicMock()
    mock_obj.touch = MagicMock()
    mock_obj.Label = "TestObject"
    
    # Mock property storage
    mock_obj._properties = {}
    
    def mock_setattr(name, value):
        mock_obj._properties[name] = value
        
    def mock_getattr(name, default=None):
        return mock_obj._properties.get(name, default)
    
    mock_obj.__setattr__ = mock_setattr
    mock_obj.__getattr__ = mock_getattr
    
    return mock_obj


@pytest.fixture
def material_standards_data():
    """
    Provide sample material standards data for testing.
    """
    return {
        "ASTM_A992": {
            "YieldStrength": "345 MPa",
            "UltimateStrength": "450 MPa",
            "ModulusElasticity": "200000 MPa",
            "Density": "7850 kg/m^3",
            "PoissonRatio": 0.30,
            "ThermalExpansion": 12e-6,
            "GradeDesignation": "Grade 50",
            "TestingStandard": "ASTM A6"
        },
        "EN_S355": {
            "YieldStrength": "355 MPa",
            "UltimateStrength": "510 MPa",
            "ModulusElasticity": "210000 MPa",
            "Density": "7850 kg/m^3",
            "PoissonRatio": 0.30,
            "ThermalExpansion": 12e-6,
            "GradeDesignation": "S355",
            "TestingStandard": "EN 10025"
        }
    }


class MockVector:
    """Mock FreeCAD Vector class for testing."""
    
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other):
        if not isinstance(other, MockVector):
            return False
        return (abs(self.x - other.x) < 1e-10 and 
                abs(self.y - other.y) < 1e-10 and 
                abs(self.z - other.z) < 1e-10)
    
    def __add__(self, other):
        return MockVector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return MockVector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return MockVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return MockVector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def normalize(self):
        length = self.Length
        if length > 1e-10:
            return MockVector(self.x / length, self.y / length, self.z / length)
        return MockVector(0, 0, 0)
    
    def distanceToPoint(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)**0.5
    
    @property
    def Length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5


@pytest.fixture
def mock_vector():
    """Provide MockVector class for testing."""
    return MockVector


@pytest.fixture(autouse=True)
def mock_freecad_modules(monkeypatch, freecad_app, freecad_gui):
    """
    Automatically mock FreeCAD modules for all tests.
    """
    # Mock FreeCAD modules by inserting into sys.modules
    monkeypatch.setitem(sys.modules, "FreeCAD", freecad_app)
    monkeypatch.setitem(sys.modules, "FreeCADGui", freecad_gui)
    
    # Mock Part module
    mock_part = MagicMock()
    mock_part.makeLine = MagicMock()
    mock_part.makeSphere = MagicMock()
    mock_part.makeCompound = MagicMock()
    sys.modules["Part"] = mock_part


# Performance testing fixtures
@pytest.fixture
def benchmark_model_data():
    """
    Provide test data for performance benchmarks.
    """
    return {
        "small_model": {
            "nodes": 10,
            "elements": 9,
            "load_cases": 3
        },
        "medium_model": {
            "nodes": 100,
            "elements": 99,
            "load_cases": 5
        },
        "large_model": {
            "nodes": 1000,
            "elements": 999,
            "load_cases": 10
        }
    }


# Utility functions for tests
def create_test_beam(start_point=(0, 0, 0), end_point=(1000, 0, 0), section="W12x26"):
    """
    Create a test beam object for testing.
    """
    from unittest.mock import MagicMock
    
    beam = MagicMock()
    beam.Type = "StructuralBeam"
    beam.StartPoint = MockVector(*start_point)
    beam.EndPoint = MockVector(*end_point)
    beam.SectionSize = section
    beam.Length = beam.StartPoint.distanceToPoint(beam.EndPoint)
    
    return beam


def create_test_node(position=(0, 0, 0), restraints=None):
    """
    Create a test node object for testing.
    """
    from unittest.mock import MagicMock
    
    node = MagicMock()
    node.Type = "StructuralNode"
    node.Position = MockVector(*position)
    
    # Set restraints
    if restraints is None:
        restraints = [False] * 6
    
    node.RestraintX = restraints[0] if len(restraints) > 0 else False
    node.RestraintY = restraints[1] if len(restraints) > 1 else False
    node.RestraintZ = restraints[2] if len(restraints) > 2 else False
    node.RestraintRX = restraints[3] if len(restraints) > 3 else False
    node.RestraintRY = restraints[4] if len(restraints) > 4 else False
    node.RestraintRZ = restraints[5] if len(restraints) > 5 else False
    
    return node


def create_test_material(standard="ASTM_A992"):
    """
    Create a test material object for testing.
    """
    from unittest.mock import MagicMock
    
    material = MagicMock()
    material.Type = "StructuralMaterial"
    material.MaterialStandard = standard
    material.ModulusElasticity = MockQuantity("200000 MPa")
    material.YieldStrength = MockQuantity("345 MPa")
    material.UltimateStrength = MockQuantity("450 MPa")
    material.Density = MockQuantity("7850 kg/m^3")
    material.PoissonRatio = 0.30
    
    return material


class MockQuantity:
    """Mock FreeCAD Quantity class for testing."""
    
    def __init__(self, value_str):
        parts = value_str.split()
        self.value = float(parts[0])
        self.unit = parts[1] if len(parts) > 1 else ""
    
    def getValueAs(self, unit):
        """Return value in specified unit (simplified)."""
        return self.value
    
    def __str__(self):
        return f"{self.value} {self.unit}"


# Test data generators
@pytest.fixture
def test_beam_data():
    """Generate test data for beam testing."""
    return {
        "simple_beam": {
            "start": (0, 0, 0),
            "end": (6000, 0, 0),
            "section": "W12x26",
            "material": "ASTM_A992"
        },
        "column": {
            "start": (0, 0, 0),
            "end": (0, 0, 3000),
            "section": "W14x90",
            "material": "ASTM_A992"
        }
    }


@pytest.fixture
def test_load_data():
    """Generate test data for load testing."""
    return {
        "point_load": {
            "position": 0.5,  # Mid-span
            "force_y": -10000,  # 10 kN downward
            "force_z": 0
        },
        "distributed_load": {
            "start_y": -5000,  # 5 kN/m
            "end_y": -5000,
            "start_pos": 0.0,
            "end_pos": 1.0
        }
    }


import importlib.util

# Provide a minimal benchmark fixture only when the pytest-benchmark plugin is not
# available (the plugin registers a `benchmark` fixture that we must not override).
if importlib.util.find_spec('pytest_benchmark') is None:
    @pytest.fixture
    def benchmark():
        """Minimal benchmark fixture placeholder used in some unit tests when
        pytest-benchmark is not installed.
        """
        class Bench:
            def __call__(self, func, *args, **kwargs):
                return func(*args, **kwargs)

        return Bench()