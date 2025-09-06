import FreeCADGui
if not hasattr(FreeCADGui, 'addCommand'):
    FreeCADGui.addCommand = lambda *a, **k: None

from freecad.StructureTools import diagram


def test_make_text_from_specs_handles_empty(monkeypatch):
    d = diagram.Diagram.__new__(diagram.Diagram)
    # monkeypatch Part.makeWireString to return an iterable of iterable of mock wires
    class MockWire:
        def rotated(self, *a, **k):
            return self
        def translate(self, v):
            return self

    class FakePart:
        @staticmethod
        def makeWireString(string, font, height):
            return [[MockWire()]]

    monkeypatch.setattr(diagram, 'Part', FakePart)
    labels = [("1.00e+00", 0.0, 0.0), ("-1.00e+00", 1.0, -1.0)]
    wires = diagram.Diagram.makeTextFromSpecs(d, labels, 10)
    assert isinstance(wires, list)
    assert len(wires) >= 1
