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

# Mock FreeCAD modules
sys.modules['FreeCAD'] = FreeCAD
sys.modules['App'] = App
sys.modules['FreeCADGui'] = types.SimpleNamespace(addCommand=lambda *a, **k: None)
sys.modules['Part'] = types.SimpleNamespace()
sys.modules['PySide'] = types.SimpleNamespace()

# Import AreaLoad
from freecad.StructureTools.objects.AreaLoad import AreaLoad

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

print("LoadIntensity:", obj.LoadIntensity)
print("Parsed LoadIntensity:", area_load.parseLoadIntensity(obj.LoadIntensity))

# Calculate effective pressure
effective_pressure = area_load.calculateEffectivePressure(obj, face_normal)

print("Face normal:", face_normal.x, face_normal.y, face_normal.z)
print("Load direction:", load_direction.x, load_direction.y, load_direction.z)

# Manually calculate dot product
dot_product = (load_direction.x * face_normal.x + 
              load_direction.y * face_normal.y + 
              load_direction.z * face_normal.z)
print("Dot product:", dot_product)
print("Absolute dot product:", abs(dot_product))

pressure_magnitude = area_load._getPressureMagnitude(obj)
print("Pressure magnitude:", pressure_magnitude)

print("Effective pressure:", effective_pressure)
print("Expected pressure: 5.0")