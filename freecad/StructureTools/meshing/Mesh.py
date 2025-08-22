"""Minimal Mesh compatibility shim for PlateMesher imports during tests.

The real FreeCAD `Mesh` module is not available in headless tests. Provide a
tiny stub so PlateMesher can be imported. This stub intentionally does not
implement real meshing functionality.
"""

class Mesh:
    def __init__(self):
        pass

def meshFromShape(shape):
    # Return an empty mesh-like object
    return Mesh()

def createMesh(*args, **kwargs):
    return Mesh()
