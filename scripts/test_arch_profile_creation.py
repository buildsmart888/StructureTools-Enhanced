# Small test harness to exercise ArchProfile creation path
# This script creates lightweight mocks for FreeCAD/Part/Draft/Arch when run
# in CI or headless test so SectionDrawing.create_arch_profile_from_points
# can be exercised without a real FreeCAD GUI.

import sys
from pathlib import Path
repo_root = Path(__file__).parents[1]
sys.path.insert(0, str(repo_root))

# Simple mocks
class MockDoc:
    def __init__(self):
        self.objects = []
    def addObject(self, type_name, label):
        obj = type('Obj', (), {})()
        obj.Label = label
        self.objects.append(obj)
        return obj
    def recompute(self):
        pass

import types

MockFreeCAD = types.ModuleType('FreeCAD')
MockFreeCAD.ActiveDocument = MockDoc()
def _vec(x, y, z=0):
    return (x, y, z)
MockFreeCAD.Vector = _vec
sys.modules['FreeCAD'] = MockFreeCAD
sys.modules['Part'] = type('M', (), {'makePolygon': lambda pts: None, 'Face': lambda w: None})

# Mock Draft
class MockDraft:
    @staticmethod
    def makeWire(vectors, closed=True):
        return type('Wire', (), {'Label': 'WireObj'})()

sys.modules['Draft'] = MockDraft

# Mock Arch
class MockArch:
    @staticmethod
    def makeProfile(obj):
        p = type('Profile', (), {})()
        p.Label = f"MockProfile_{getattr(obj, 'Label', 'unknown')}"
        return p

sys.modules['Arch'] = MockArch

# Now import and run the creation with a simple square
from freecad.StructureTools.geometry.SectionDrawing import SectionDrawer

drawer = SectionDrawer()
points = [[-50,-50], [50,-50], [50,50], [-50,50], [-50,-50]]
profile = drawer.create_arch_profile_from_points(points, 'TEST_PROFILE')

if profile:
    print('Mock ArchProfile created:', getattr(profile, 'Label', '<no label>'))
    sys.exit(0)
else:
    print('ArchProfile creation failed')
    sys.exit(2)
