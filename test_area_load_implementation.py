#!/usr/bin/env python3
"""
Test script for area load implementation validation
"""

import sys
import os
import types

# Setup repo path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
freecad_dir = os.path.join(repo_root, 'freecad')
if freecad_dir not in sys.path:
    sys.path.insert(0, freecad_dir)

# Minimal FreeCAD stubs with Vector class
class FakeVector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return FakeVector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return FakeVector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return FakeVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def normalize(self):
        length = (self.x**2 + self.y**2 + self.z**2)**0.5
        if length > 0:
            return FakeVector(self.x/length, self.y/length, self.z/length)
        return FakeVector(0, 0, 0)

# Enhanced FakeObj with addProperty method
class FakeObj:
    def __init__(self):
        pass
    
    def addProperty(self, prop_type, name, group, desc, default=None):
        setattr(self, name, default)

FreeCAD = types.SimpleNamespace()
FreeCAD.Vector = FakeVector
App = FreeCAD

class QMessageBoxStub:
    Critical = 2
    Ok = 0

class QtWidgetsStub:
    QMessageBox = QMessageBoxStub

# Mock FreeCAD modules
sys.modules['FreeCAD'] = FreeCAD
sys.modules['App'] = App
sys.modules['FreeCADGui'] = types.SimpleNamespace(addCommand=lambda *a, **k: None)
sys.modules['Part'] = types.SimpleNamespace()
sys.modules['PySide'] = types.SimpleNamespace(QtWidgets=QtWidgetsStub)

# Import required modules
try:
    from freecad.StructureTools import calc
    from freecad.StructureTools.Pynite_main.FEModel3D import FEModel3D
    from freecad.StructureTools.objects.AreaLoad import AreaLoad
    print("SUCCESS: All modules imported successfully")
except ImportError as e:
    print(f"ERROR: Failed to import modules: {e}")
    sys.exit(1)

# Create fake FreeCAD objects for testing
class FakeFace:
    def __init__(self, verts):
        self.Vertexes = verts
        self.Area = 1.0
        self.Edges = []
        self.ParameterRange = [0, 1, 0, 1]
        # Create fake edges for testing
        for i in range(len(verts)):
            next_i = (i + 1) % len(verts)
            edge = types.SimpleNamespace()
            edge.Vertexes = [verts[i], verts[next_i]]
            edge.Length = ((verts[next_i].X - verts[i].X)**2 + 
                          (verts[next_i].Y - verts[i].Y)**2 + 
                          (verts[next_i].Z - verts[i].Z)**2)**0.5
            self.Edges.append(edge)
    
    def normalAt(self, u, v):
        # Return a simple upward normal for testing
        return FakeVector(0, 0, 1)
    
    @property
    def CenterOfMass(self):
        return FakeVector(0.5, 0.5, 0)

class FakeVertex:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
        self.Point = FakeVector(x, y, z)

class FakePlate:
    def __init__(self, name, verts):
        self.Name = name
        self.Type = 'StructuralPlate'
        self.Shape = types.SimpleNamespace(Faces=[FakeFace(verts)])
        self.CornerNodes = []
        self.Thickness = 0.1
        self.Material = None
        self.MeshDensity = 0  # no mesh

class FakeAreaLoad:
    def __init__(self, name, target, load_distribution="TwoWay"):
        self.Name = name
        self.Type = 'AreaLoad'
        self.TargetFaces = [target]
        self.LoadIntensity = "5.0 kN/m^2"
        self.Magnitude = 5000.0  # 5 kN/m² in N/mm²
        self.LoadDirection = FakeVector(0, 0, -1)  # Downward
        self.LoadDistribution = load_distribution
        self.LoadCategory = "DL"
        self.OneWayDirection = "X"
        self.CustomDistributionDirection = FakeVector(1, 0, 0)
        self.ObjectBase = []

def test_area_load_creation():
    """Test creation of AreaLoad object"""
    try:
        # Create a fake document object
        obj = FakeObj()
        
        # Create AreaLoad instance
        area_load = AreaLoad(obj)
        
        # Check if required properties exist
        required_properties = [
            'TargetFaces', 'LoadIntensity', 'LoadDirection', 'LoadDistribution',
            'LoadCategory', 'OneWayDirection', 'CustomDistributionDirection'
        ]
        
        for prop in required_properties:
            if not hasattr(obj, prop):
                print(f"ERROR: Missing property {prop}")
                return False
        
        print("SUCCESS: AreaLoad object created with all required properties")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to create AreaLoad object: {e}")
        return False

def test_calc_integration():
    """Test integration of area loads with calc module"""
    try:
        # Create four vertices for a rectangular plate
        verts = [FakeVertex(0,0,0), FakeVertex(1,0,0), FakeVertex(1,1,0), FakeVertex(0,1,0)]
        plate = FakePlate('Plate1', verts)
        
        # Test different load distributions
        load_distributions = ["TwoWay", "OneWay", "OpenStructure"]
        
        for distribution in load_distributions:
            print(f"Testing {distribution} distribution...")
            aload = FakeAreaLoad('AL1', plate, distribution)
            
            # Create a fake Calc object container with ListElements
            class Obj:
                pass
            o = Obj()
            o.ListElements = [plate, aload]
            o.LengthUnit = 'm'
            o.ForceUnit = 'kN'
            o.LoadCombination = '100_DL'
            o.selfWeight = False
            
            # Run calc.execute
            c = calc.Calc(o, o.ListElements)
            c.execute(o)
            
            # Check if analysis was successful
            if not hasattr(o, 'AnalysisType'):
                print(f"ERROR: Analysis failed for {distribution} distribution")
                return False
            
            print(f"SUCCESS: {distribution} distribution processed successfully")
        
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to test calc integration: {e}")
        return False

def test_load_distribution_methods():
    """Test load distribution calculation methods"""
    try:
        # Create a fake document object
        obj = FakeObj()
        
        # Create AreaLoad instance
        area_load = AreaLoad(obj)
        
        # Create a simple face for testing
        verts = [FakeVertex(0,0,0), FakeVertex(1,0,0), FakeVertex(1,1,0), FakeVertex(0,1,0)]
        face = FakeFace(verts)
        
        # Test different distribution methods
        distributions = ["OneWay", "TwoWay", "OpenStructure"]
        
        for distribution in distributions:
            edge_factors = area_load.getEdgeDistributionFactors(obj, face, distribution)
            if len(edge_factors) != 4:
                print(f"ERROR: Wrong number of edge factors for {distribution}")
                return False
            
            # Check that factors sum to approximately 1.0 (with some tolerance)
            factor_sum = sum(edge_factors)
            if abs(factor_sum - 1.0) > 0.01:
                print(f"ERROR: Edge factors for {distribution} don't sum to 1.0: {factor_sum}")
                return False
        
        print("SUCCESS: All load distribution methods working correctly")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to test load distribution methods: {e}")
        return False

def test_effective_pressure_calculation():
    """Test effective pressure calculation"""
    try:
        # Create a fake document object
        obj = FakeObj()
        
        # Create AreaLoad instance
        area_load = AreaLoad(obj)
        
        # Set LoadIntensity after creating the AreaLoad instance
        obj.LoadIntensity = "5.0 kN/m^2"
        
        # Test with a simple face normal
        face_normal = FakeVector(0, 0, 1)  # Upward normal
        load_direction = FakeVector(0, 0, -1)  # Downward load
        
        # Set load direction on object
        obj.LoadDirection = load_direction
        
        # Calculate effective pressure
        effective_pressure = area_load.calculateEffectivePressure(obj, face_normal)
        
        # For perpendicular load and surface, should be equal to magnitude
        # 5.0 kN/m² = 5.0 N/mm² (since 1 kN/m² = 1 N/mm² in our unit system)
        expected_pressure = 5.0  # 5.0 kN/m² in N/mm²
        if abs(effective_pressure - expected_pressure) > 1e-6:
            print(f"ERROR: Wrong effective pressure: {effective_pressure}, expected: {expected_pressure}")
            return False
        
        print("SUCCESS: Effective pressure calculation working correctly")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to test effective pressure calculation: {e}")
        return False

def main():
    """Run all tests"""
    print("Starting area load implementation validation tests...")
    print("=" * 50)
    
    tests = [
        ("AreaLoad Creation", test_area_load_creation),
        ("Load Distribution Methods", test_load_distribution_methods),
        ("Effective Pressure Calculation", test_effective_pressure_calculation),
        ("Calc Integration", test_calc_integration)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name} test...")
        try:
            if test_func():
                print(f"✓ {test_name} PASSED")
                passed += 1
            else:
                print(f"✗ {test_name} FAILED")
                failed += 1
        except Exception as e:
            print(f"✗ {test_name} FAILED with exception: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("All tests PASSED! Area load implementation is working correctly.")
        return 0
    else:
        print("Some tests FAILED! Please check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())