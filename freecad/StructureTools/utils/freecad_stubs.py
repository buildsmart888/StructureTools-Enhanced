# -*- coding: utf-8 -*-
"""
FreeCAD Stubs for Standalone Testing
===================================

This module provides mock implementations of FreeCAD modules for standalone testing
outside of the FreeCAD environment. This allows StructureTools to be imported and
tested without requiring a full FreeCAD installation.
"""

import types
import sys
from typing import Any, Dict, List, Optional, Union


class MockFreeCADApp:
    """Mock FreeCAD App module"""
    
    class Console:
        @staticmethod
        def PrintMessage(msg: str) -> None:
            print(f"FreeCAD: {msg}")
        
        @staticmethod
        def PrintWarning(msg: str) -> None:
            print(f"FreeCAD Warning: {msg}")
        
        @staticmethod
        def PrintError(msg: str) -> None:
            print(f"FreeCAD Error: {msg}")
    
    @staticmethod
    def activeDocument():
        return MockDocument()
    
    @staticmethod
    def newDocument(name: str = "Unnamed"):
        return MockDocument()


class MockDocument:
    """Mock FreeCAD Document"""
    
    def __init__(self):
        self.Objects = []
        self.Name = "MockDocument"
    
    def addObject(self, type_name: str, object_name: str):
        """Add mock object to document"""
        mock_obj = MockDocumentObject()
        mock_obj.Name = object_name
        mock_obj.TypeId = type_name
        self.Objects.append(mock_obj)
        return mock_obj
    
    def removeObject(self, object_name: str):
        """Remove object from document"""
        self.Objects = [obj for obj in self.Objects if obj.Name != object_name]
    
    def recompute(self):
        """Mock recompute"""
        pass


class MockDocumentObject:
    """Mock FreeCAD Document Object"""
    
    def __init__(self):
        self.Name = "MockObject"
        self.Label = "Mock Object"
        self.TypeId = "MockType"
        self.ViewObject = MockViewProvider()
        self._properties = {}
    
    def addProperty(self, prop_type: str, prop_name: str, group: str = "", doc: str = ""):
        """Add property to mock object"""
        # Create mock property with default value
        if "Float" in prop_type:
            default_value = 0.0
        elif "Int" in prop_type:
            default_value = 0
        elif "Bool" in prop_type:
            default_value = False
        elif "String" in prop_type:
            default_value = ""
        elif "Vector" in prop_type:
            default_value = MockVector()
        elif "Link" in prop_type:
            default_value = None
        else:
            default_value = None
        
        setattr(self, prop_name, default_value)
        self._properties[prop_name] = {
            'type': prop_type,
            'group': group,
            'doc': doc,
            'value': default_value
        }
        return getattr(self, prop_name)
    
    def touch(self):
        """Mock touch method"""
        pass


class MockViewProvider:
    """Mock View Provider"""
    
    def __init__(self):
        self.Visibility = True
        self.DisplayMode = "Flat Lines"


class MockVector:
    """Mock FreeCAD Vector"""
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


class MockPart:
    """Mock Part module"""
    
    @staticmethod
    def makeBox(length: float, width: float, height: float):
        """Mock makeBox"""
        return MockShape()
    
    @staticmethod
    def makeCylinder(radius: float, height: float):
        """Mock makeCylinder"""
        return MockShape()


class MockShape:
    """Mock Part Shape"""
    
    def __init__(self):
        self.Volume = 1000.0
        self.Area = 100.0
        self.BoundBox = MockBoundBox()


class MockBoundBox:
    """Mock Bounding Box"""
    
    def __init__(self):
        self.XMin = 0.0
        self.XMax = 10.0
        self.YMin = 0.0
        self.YMax = 10.0
        self.ZMin = 0.0
        self.ZMax = 10.0


class MockGui:
    """Mock FreeCADGui module"""
    
    @staticmethod
    def addCommand(name: str, command):
        """Mock addCommand"""
        pass
    
    @staticmethod
    def activateWorkbench(name: str):
        """Mock activateWorkbench"""
        pass
    
    class Control:
        @staticmethod
        def showTaskPanel(panel):
            """Mock showTaskPanel"""
            pass
        
        @staticmethod
        def closeTaskPanel():
            """Mock closeTaskPanel"""
            pass


class MockPySide:
    """Mock PySide module"""
    
    class QtWidgets:
        class QWidget:
            def __init__(self):
                pass
        
        class QVBoxLayout:
            def __init__(self):
                pass
            
            def addWidget(self, widget):
                pass
        
        class QLabel:
            def __init__(self, text: str = ""):
                self.text = text
        
        class QPushButton:
            def __init__(self, text: str = ""):
                self.text = text
        
        class QLineEdit:
            def __init__(self):
                self.text = ""
            
            def setText(self, text: str):
                self.text = text
            
            def text(self):
                return self.text


def setup_freecad_stubs():
    """Setup FreeCAD stubs in sys.modules if not already present"""
    
    # Only setup if FreeCAD modules are not already available
    if 'FreeCAD' not in sys.modules:
        # Main FreeCAD modules
        sys.modules['FreeCAD'] = MockFreeCADApp()
        sys.modules['App'] = sys.modules['FreeCAD']
        sys.modules['FreeCADGui'] = MockGui()
        sys.modules['Gui'] = sys.modules['FreeCADGui']
        sys.modules['Part'] = MockPart()
        
        # PySide modules
        sys.modules['PySide'] = MockPySide()
        sys.modules['PySide2'] = MockPySide()
        
        return True
    
    return False


def is_freecad_available() -> bool:
    """Check if running in actual FreeCAD environment"""
    try:
        import FreeCAD
        # Check if it's the real FreeCAD by testing for specific attributes
        return hasattr(FreeCAD, 'Version') and hasattr(FreeCAD, 'ConfigGet')
    except ImportError:
        return False


# Auto-setup stubs when module is imported
_stubs_setup = setup_freecad_stubs()

# Export main functions
__all__ = [
    'setup_freecad_stubs',
    'is_freecad_available',
    'MockFreeCADApp',
    'MockDocument', 
    'MockDocumentObject',
    'MockVector',
    'MockPart',
    'MockGui',
    'MockPySide'
]

if __name__ == "__main__":
    print("FreeCAD Stubs Module")
    print(f"Stubs setup: {_stubs_setup}")
    print(f"FreeCAD available: {is_freecad_available()}")
