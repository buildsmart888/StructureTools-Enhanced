
import unittest
import sys
import types
from unittest.mock import MagicMock, patch

# Mock modules for headless environment
fake_modules = {}
# Try to import numpy first
try:
    import numpy
except ImportError:
    # If not available, we will mock it
    pass

for name in ('FreeCAD', 'App', 'FreeCADGui', 'Part', 'PyniteFEA', 'PySide', 'numpy'):
    if name not in sys.modules:
        mod = types.ModuleType(name)
        fake_modules[name] = mod
        sys.modules[name] = mod

# Setup submodules for PySide
if 'PySide' in sys.modules:
    pyside = sys.modules['PySide']
    if not hasattr(pyside, 'QtWidgets'):
        qtwidgets = types.ModuleType('QtWidgets')
        pyside.QtWidgets = qtwidgets
        sys.modules['PySide.QtWidgets'] = qtwidgets

# Setup numpy mock details ONLY if it is a fake module
if 'numpy' in fake_modules:
    np = sys.modules['numpy']
    np.ndarray = list
    # Mock specific functions used by Pynite
    np.array = lambda x: x
    np.zeros = lambda *args, **kwargs: []
    np.matmul = lambda a, b: []
    np.divide = lambda a, b: a
    np.subtract = lambda a, b: a
    np.atleast_2d = lambda x: x
    np.all = lambda x: True
    np.nan = float('nan')
    np.array = lambda x: x
    np.dot = lambda a, b: 0
    np.cross = lambda a, b: [0,0,0]
    np.sin = lambda x: 0
    np.cos = lambda x: 1
    np.linspace = lambda *args: []
    np.vstack = lambda args: args[0]
    np.hstack = lambda args: args[0]
    np.allclose = lambda a, b: True
    np.where = lambda c, a, b: a
    np.add = lambda a, b: a
    
    # ensure attributes are set on the module itself for 'from numpy import add'
    for attr in ['add', 'subtract', 'matmul', 'divide', 'zeros', 'array', 'dot', 'cross', 'sin', 'cos', 'linspace', 'vstack', 'hstack', 'allclose', 'where']:
         val = getattr(np, attr, None) or (lambda *args, **kwargs: None)
         setattr(np, attr, val)
    np.pi = 3.14159
    
    # Mock numpy.linalg
    linalg = types.ModuleType('numpy.linalg')
    linalg.solve = lambda a, b: []
    linalg.norm = lambda x: 0.0
    sys.modules['numpy.linalg'] = linalg
    np.linalg = linalg

import os
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
    
# Setup FreeCAD mocks
FreeCAD = sys.modules['FreeCAD']
FreeCAD.Units = types.SimpleNamespace(Quantity=lambda v, u=None: float(v))
FreeCAD.Vector = lambda x, y, z: (x, y, z)
FreeCADGui = sys.modules['FreeCADGui']
FreeCADGui.addCommand = lambda name, cmd: None

# Ensure freecad package is importable
try:
    import freecad.StructureTools.calc
except ImportError as e:
    print(f"Import failed: {e}")
    # Try adding subdirectory if needed?
    # sys.path.append(os.path.join(os.getcwd(), 'freecad')) 
    pass

# Now import the modules under test
# We need to ensure we can import calc without side effects
try:
    from freecad.StructureTools import calc
    # Reload to ensure we get fresh state if needed, though unneeded for new process
except ImportError:
    # If package structure is complex, might need path adjustment
    pass

class TestResultManagerRefactor(unittest.TestCase):
    
    def setUp(self):
        # Create a dummy Calc object
        self.obj = MagicMock()
        self.obj.ListElements = []
        self.obj.LengthUnit = 'm'
        self.obj.ForceUnit = 'kN'
        
        # Result point config
        self.obj.NumPointsMoment = 3
        self.obj.NumPointsShear = 3
        self.obj.NumPointsAxial = 2
        self.obj.NumPointsTorque = 2
        self.obj.NumPointsDeflection = 2
        
        # Flags
        self.obj.selfWeight = False
        self.obj.LoadCombination = '100_DL'
        
        self.obj.MemberResults = [] # Expected to be populated
        
        
    def test_result_manager_called(self):
        """Verify that ResultManager is used and populates MemberResults"""
        
        # Mock PyniteAdapter and ResultManager inside calc
        # We need to patch where they are imported IN CALC.PY
        
        # Mock PyniteAdapter and ResultManager
        # Since ResultManager is imported from .analysis.result_manager inside execute, we must patch it there
        
        with patch('freecad.StructureTools.analysis.result_manager.ResultManager') as MockResultManager, \
             patch('freecad.StructureTools.calc.PyniteAdapter') as MockAdapter:
                 
            # Setup the MockResultManager instance
            mock_manager_instance = MockResultManager.return_value
            
            # Setup the calc instance
            calc_instance = calc.Calc(self.obj, elements=[])
            
            # Create a rich mock model that passes validation checks
            mock_model = MagicMock()
            mock_node = MagicMock() 
            # Ensure support check passes
            mock_node.support_DX = True
            mock_node.X = 0.0
            mock_node.Y = 0.0
            mock_node.Z = 0.0
            # Also set RxnFX etc for reaction checks
            mock_node.RxnFX = {}
            mock_model.nodes = {'node1': mock_node}
            mock_model.members = {'mem1': MagicMock()}
            
            # We mock the model building parts to avoid complex dependency triggers
            calc_instance.mapNodes = MagicMock(return_value=[])
            calc_instance.mapMembers = MagicMock(return_value={})
            calc_instance.setMaterialAndSections = MagicMock(return_value=mock_model)
            calc_instance.setNodes = MagicMock(return_value=mock_model)
            calc_instance.setMembers = MagicMock(return_value=mock_model)
            calc_instance.setLoads = MagicMock(return_value=mock_model)
            calc_instance.setSuports = MagicMock(return_value=mock_model)

            
            # Assume model.analyze() passes
            calc_instance.model = MagicMock()
            calc_instance.model.analyze.return_value = True
            
            # Execute
            calc_instance.execute(self.obj)
            
            # Verify ResultManager was instantiated
            MockResultManager.assert_called()
            
            # Verify prepare_results_for_object was called
            # It might be called with (obj, load_combo, config)
            mock_manager_instance.prepare_results_for_object.assert_called()
            
            args, _ = mock_manager_instance.prepare_results_for_object.call_args
            self.assertEqual(args[0], self.obj)
            self.assertEqual(args[1], '100_DL') # Active load combo
            
            # Verify PyniteAdapter was instantiated
            MockAdapter.assert_called()

if __name__ == '__main__':
    unittest.main()
