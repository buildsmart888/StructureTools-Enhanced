# Minimal FreeCAD stub for unit tests
import math
from unittest.mock import MagicMock

class Quantity:
    def __init__(self, value=0, unit=None):
        # Accept numeric, string like "200000 MPa", or another Quantity
        if isinstance(value, Quantity):
            self._value = float(value._value)
            self._unit = value._unit
        elif isinstance(value, str):
            parts = value.split()
            try:
                self._value = float(parts[0])
            except Exception:
                # fallback to 0.0
                self._value = 0.0
            self._unit = parts[1] if len(parts) > 1 else ''
        else:
            try:
                self._value = float(value)
            except Exception:
                self._value = 0.0
            self._unit = unit

    def getValueAs(self, unit):
        # Simplified: ignore unit conversion and return stored value
        return self._value

    def __str__(self):
        return f"{self._value} {self._unit or ''}".strip()


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        return iter((self.x, self.y, self.z))


Console = MagicMock()
Console.PrintMessage = MagicMock()
Console.PrintWarning = MagicMock()
Console.PrintError = MagicMock()
ActiveDocument = None

class _App:
    pass

# Expose Units namespace similar to FreeCAD.Units
class _Units:
    Quantity = Quantity

Units = _Units()

# Provide simple helpers used in tests
def newDocument(name=None):
    global ActiveDocument
    ActiveDocument = None
    return None

def closeDocument(name):
    global ActiveDocument
    ActiveDocument = None

# backwards-compat names
App = None

__all__ = ['Quantity', 'Vector', 'Console', 'ActiveDocument', 'newDocument', 'closeDocument', 'Units']
