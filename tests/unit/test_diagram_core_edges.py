from freecad.StructureTools.diagram_core import (
    separates_ordinates,
    generate_coordinates,
    normalize_loop_for_face,
    compose_face_loops,
    make_member_diagram_coords,
)


def test_separates_empty():
    assert separates_ordinates([]) == []


def test_separates_all_zeros():
    vals = [0.0, 0.0, 0.0]
    loops = separates_ordinates(vals, zero_tol=1e-3)
    assert loops == [[0.0, 0.0, 0.0]]


def test_separates_alternating_tiny_values_treated_as_zero():
    vals = [1e-4, -1e-4, 1e-4]
    # with zero_tol larger than values, no splitting should occur
    loops = separates_ordinates(vals, zero_tol=1e-3)
    assert len(loops) == 1


def test_generate_coordinates_zero_dist():
    ordinates = [[1.0, -1.0]]
    coords = generate_coordinates(ordinates, dist=0.0)
    # x coordinates should all be zero when dist == 0
    assert all(x == 0.0 for loop in coords for x, y in loop)


def test_normalize_loop_for_face_empty():
    assert normalize_loop_for_face([]) == []


def test_compose_face_loops_filters_degenerate():
    # loop with only 2 distinct points (closed will have duplicate) should be filtered
    loops = [[(0, 0), (1, 0)], [(0, 0), (1, 0), (1, 1), (0, 0)]]
    out = compose_face_loops(loops)
    assert len(out) == 1


def test_make_member_diagram_coords_scale_zero():
    values = [1.0, -0.5, 0.25]
    coords, scaled = make_member_diagram_coords(values, dist=1.0, scale=0.0)
    assert scaled == [0.0, 0.0, 0.0]
    assert isinstance(coords, list)
