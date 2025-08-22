# Minimal FreeCADGui stub for tests
class Selection:
    @staticmethod
    def getSelection():
        return []

class _Gui:
    pass

ActiveDocument = None

__all__ = ['Selection', 'ActiveDocument']
