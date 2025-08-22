# Temporary import check shim for CI-less environments
import types
import sys

# Minimal FreeCAD stub
FreeCAD = types.SimpleNamespace()
App = FreeCAD
Gui = types.SimpleNamespace()
# simple stub for addCommand used in modules
def _addCommand_stub(name, cmd):
    # noop
    return
Gui.addCommand = _addCommand_stub
Part = types.SimpleNamespace()

sys.modules['FreeCAD'] = FreeCAD
sys.modules['App'] = App
sys.modules['FreeCADGui'] = Gui
sys.modules['Part'] = Part

# Provide PySide QtWidgets stub used in calc
class QtWidgetsStub:
    class QMessageBox:
        Critical = 2
        Ok = 0
        def __init__(self):
            pass
        def setIcon(self, x):
            pass
        def setWindowTitle(self, x):
            pass
        def setText(self, x):
            pass
        def setStandardButtons(self, x):
            pass
        def exec_(self):
            pass

sys.modules['PySide'] = types.SimpleNamespace(QtWidgets=QtWidgetsStub)

# Now try importing the calc module
import os
# Ensure workspace root is on sys.path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
freecad_dir = os.path.join(repo_root, 'freecad')
if freecad_dir not in sys.path:
    sys.path.insert(0, freecad_dir)

from StructureTools import calc
print('Imported calc successfully')
