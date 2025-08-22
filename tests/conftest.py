# -*- coding: utf-8 -*-
"""
Pytest configuration and fixtures for StructureTools tests.
"""

import os
import sys
import pytest
from unittest.mock import Mock, MagicMock
from typing import Generator, Any

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
    # Mock FreeCAD modules
    monkeypatch.setattr("FreeCAD", freecad_app, raising=False)
    monkeypatch.setattr("FreeCADGui", freecad_gui, raising=False)
    
    # Mock sys.modules entries
    sys.modules["FreeCAD"] = freecad_app
    sys.modules["FreeCADGui"] = freecad_gui
    
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