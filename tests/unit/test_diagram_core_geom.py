from freecad.StructureTools.diagram_core import compose_face_loops, get_label_positions


def test_compose_face_loops_and_labels():
    loops = [ [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,1),(0,0)] ]
    out = compose_face_loops(loops)
    assert isinstance(out, list)
    labels = get_label_positions([0.1, -0.2], [0.1, -0.2], 1.0, 10, 2)
    assert isinstance(labels, list)
