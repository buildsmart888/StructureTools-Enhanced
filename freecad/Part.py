"""Minimal Part stub for tests"""

class Shape:
    def __init__(self):
        self.Vertexes = []
        self.Edges = []
        self.Faces = []

class Vertex:
    def __init__(self, point):
        self.Point = point

class Edge:
    def __init__(self, vertexes=None):
        self.Vertexes = vertexes or []

class Face:
    def __init__(self, vertexes=None):
        self.Vertexes = vertexes or []

def makeLine(a, b):
    return None

def makeSphere(r):
    return None

__all__ = ['Shape', 'Vertex', 'Edge', 'Face', 'makeLine', 'makeSphere']
