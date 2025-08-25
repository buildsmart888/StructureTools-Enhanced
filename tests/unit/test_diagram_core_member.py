from freecad.StructureTools.diagram_core import make_member_diagram_coords


def test_make_member_diagram_coords_basic():
    values = [0.5, -0.2, 0.1]
    dist = 1.0
    scale = 2.0
    coords, scaled = make_member_diagram_coords(values, dist, scale)
    assert isinstance(coords, list) and isinstance(scaled, list)
    assert all(isinstance(loop, list) for loop in coords)
    assert scaled == [v * scale for v in values]
        # Removed trailing footer to make the file valid Python
