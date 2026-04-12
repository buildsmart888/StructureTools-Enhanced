"""
Qt compatibility shim for FreeCAD addons.
FreeCAD < 1.0  uses PySide2 (Qt5)
FreeCAD >= 1.0 uses PySide6 (Qt6)

Import Qt classes from this module instead of PySide2/PySide6 directly:
    from .qt_compat import QtWidgets, QtCore, QtGui, Qt, Signal, Slot
"""

try:
    from PySide6 import QtWidgets, QtCore, QtGui
    from PySide6.QtCore import Qt, Signal, Slot
    PYSIDE_VERSION = 6
except ImportError:
    try:
        from PySide2 import QtWidgets, QtCore, QtGui
        from PySide2.QtCore import Qt, Signal, Slot
        PYSIDE_VERSION = 2
    except ImportError:
        raise ImportError(
            "StructureTools requires PySide6 (FreeCAD 1.x) or PySide2 (FreeCAD 0.x). "
            "Neither could be imported."
        )

__all__ = ["QtWidgets", "QtCore", "QtGui", "Qt", "Signal", "Slot", "PYSIDE_VERSION"]
