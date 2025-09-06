#!/usr/bin/env python3
"""
Simple test to verify PlatePropertiesPanel.py can be imported correctly.
"""

import sys
import os
from unittest.mock import Mock

# Add current directory to path
sys.path.insert(0, '.')

# Setup mocks before importing
mock_app = Mock()
mock_gui = Mock()
mock_qt = Mock()
mock_qt.QtCore = Mock()
mock_qt.QtWidgets = Mock()
mock_qt.QtWidgets.QWidget = Mock
mock_qt.QtWidgets.QVBoxLayout = Mock
mock_qt.QtWidgets.QLabel = Mock
mock_qt.QtWidgets.QTabWidget = Mock
mock_qt.QtWidgets.QGroupBox = Mock
mock_qt.QtWidgets.QHBoxLayout = Mock
mock_qt.QtWidgets.QCheckBox = Mock
mock_qt.QtWidgets.QPushButton = Mock
mock_qt.QtWidgets.QFormLayout = Mock
mock_qt.QtWidgets.QListWidget = Mock
mock_qt.QtWidgets.QSpinBox = Mock
mock_qt.QtWidgets.QComboBox = Mock
mock_qt.QtWidgets.QDoubleSpinBox = Mock
mock_qt.QtGui = Mock()

sys.modules['FreeCAD'] = mock_app
sys.modules['FreeCADGui'] = mock_gui
sys.modules['PySide2'] = mock_qt
sys.modules['PySide2.QtCore'] = mock_qt.QtCore
sys.modules['PySide2.QtWidgets'] = mock_qt.QtWidgets
sys.modules['PySide2.QtGui'] = mock_qt.QtGui

print("Testing PlatePropertiesPanel import...")

try:
    # Clear any existing modules to avoid caching issues
    if 'freecad.StructureTools.taskpanels.PlatePropertiesPanel' in sys.modules:
        del sys.modules['freecad.StructureTools.taskpanels.PlatePropertiesPanel']
    
    import freecad.StructureTools.taskpanels.PlatePropertiesPanel as plate_module
    print("✓ Successfully imported PlatePropertiesPanel module")
    
    # Get the class
    PlatePropertiesPanel = getattr(plate_module, 'PlatePropertiesPanel', None)
    if PlatePropertiesPanel:
        print("✓ Successfully found PlatePropertiesPanel class")
        
        # Try to create an instance
        mock_plate = Mock()
        panel = PlatePropertiesPanel(mock_plate)
        print("✓ Successfully created PlatePropertiesPanel instance")
        
        # Check if key methods exist
        methods_to_check = ['createUI', 'createGeometryTab', 'createMaterialTab', 'accept', 'reject']
        for method in methods_to_check:
            if hasattr(panel, method):
                print(f"✓ Method {method} exists")
            else:
                print(f"✗ Method {method} missing")
        
        print("All tests passed!")
    else:
        print("✗ PlatePropertiesPanel class not found in module")
        print("Available attributes:", [attr for attr in dir(plate_module) if not attr.startswith('_')])
        
        # Try to see what went wrong
        print("Module file:", plate_module.__file__ if hasattr(plate_module, '__file__') else 'No file')
        
        # Try alternative access methods
        all_attrs = dir(plate_module)
        print("All attributes (including private):", all_attrs)
    
except Exception as e:
    print(f"✗ Import failed: {e}")
    import traceback
    traceback.print_exc()
