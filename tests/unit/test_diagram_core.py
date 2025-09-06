import pytest
from freecad.StructureTools.diagram_core import (
    separates_ordinates,
    generate_coordinates,
    normalize_loop_for_face,
)


def test_separates_ordinates_simple():
    vals = [1.0, 0.5, -0.2, -0.5, 0.1]
    loops = separates_ordinates(vals, zero_tol=1e-3)
    assert isinstance(loops, list)
    assert len(loops) >= 2


def test_generate_coordinates_and_normalize():
    ordinates = [[1.0, -0.5], [0.2]]
    dist = 1.0
    coords = generate_coordinates(ordinates, dist)
    assert isinstance(coords, list)
    assert all(isinstance(loop, list) for loop in coords)
    # normalize one loop
    loop = coords[0]
    closed = normalize_loop_for_face(loop)
    assert closed[0] == closed[-1]

