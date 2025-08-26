"""Pure-python numeric helpers for Diagram generation.

These helpers contain the pure numeric logic extracted from diagram.py so
they can be unit tested without FreeCAD dependencies.
"""
from typing import List, Tuple

# Import Global Units System
try:
    from .utils.units_manager import (
        get_units_manager, format_force, format_stress, format_modulus
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e9:.0f} GPa"



def separates_ordinates(values: List[float], zero_tol: float = 1e-2) -> List[List[float]]:
    """Split a 1D list of ordinates into loops each time sign changes.

    Returns a list of lists. Small values abs(value) <= zero_tol are treated
    as zero for the crossing logic.
    """
    if not values:
        return []
    loops: List[List[float]] = []
    loop: List[float] = [values[0]]
    for i in range(1, len(values)):
        a = values[i-1]
        b = values[i]
        # treat near-zero as zero
        a_z = abs(a) <= zero_tol
        b_z = abs(b) <= zero_tol
        if (a * b) < 0 and not b_z:
            loops.append(loop)
            loop = [b]
        else:
            loop.append(b)

    loops.append(loop)
    return loops


def generate_coordinates(ordinates: List[List[float]], dist: float, zero_tol: float = 1e-2) -> List[List[Tuple[float, float]]]:
    """Convert separates_ordinates output into x,y coordinate loops.

    ordinates: list of lists (each inner is a sequence of ordinate values)
    dist: spacing between sample points on x axis

    Returns list of loops where each loop is list of (x, y) pairs.
    """
    loops_out: List[List[Tuple[float, float]]] = []
    cont = 0
    for i in range(len(ordinates)):
        loop: List[Tuple[float, float]] = []
        for j in range(len(ordinates[i])):
            if j == 0 and abs(ordinates[i][j]) > zero_tol and len(loop) == 0:
                loop.append((0.0, 0.0))

            coordinate = (cont * dist, ordinates[i][j])
            loop.append(coordinate)
            cont += 1

        # last point handling / intersection calculations
        if i == len(ordinates) - 1:
            if abs(loop[-1][1]) > zero_tol:
                loop.append(((cont - 1) * dist, 0.0))
        else:
            o = loop[-1][0]
            a = abs(loop[-1][1])
            b = abs(ordinates[i+1][0])
            if (a + b) != 0:
                x = (a * dist) / (a + b)
            else:
                x = 0.0
            loop.append((o + x, 0.0))
            # the next loop should start with this intersection point
        loops_out.append(loop)

    return loops_out


def normalize_loop_for_face(loop: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Return a closed loop suitable for face creation without mutating input.

    Ensures the first point is appended at the end.
    """
    if not loop:
        return []
    out = list(loop)
    if out[0] != out[-1]:
        out = out + [out[0]]
    return out


def make_member_diagram_coords(values_original: List[float], dist: float, scale: float, zero_tol: float = 1e-2):
    """Compute coordinate loops and scaled ordinate values for a member diagram.

    Returns (coordinates, values_scaled) where coordinates is a list of loops
    (each loop is a list of (x,y) tuples) and values_scaled is the scaled
    ordinate list used for drawing/labeling.
    """
    values_scaled = [v * scale for v in values_original]
    ordinates = separates_ordinates(values_scaled, zero_tol=zero_tol)
    coordinates = generate_coordinates(ordinates, dist, zero_tol=zero_tol)
    return coordinates, values_scaled


def compose_face_loops(loops: List[List[Tuple[float, float]]]) -> List[List[Tuple[float, float]]]:
    """Return normalized, closed loops suitable for face creation.

    This function is numeric-only and will normalize each loop (close it)
    and filter out degenerate loops (less than 3 distinct points).
    """
    out: List[List[Tuple[float, float]]] = []
    for loop in loops:
        norm = normalize_loop_for_face(loop)
        # filter degenerate loops
        # consider unique points after closing
        unique_pts = []
        for p in norm:
            if not unique_pts or p != unique_pts[-1]:
                unique_pts.append(p)
        if len(unique_pts) >= 4:  # closed loop has first==last => at least 4 points
            out.append(norm)
    return out


def get_label_positions(values_scaled: List[float], list_matrix_row: List[float], dist: float, font_height: float, precision: int, offset: float = 0.0) -> List[Tuple[str, float, float]]:
    """Return label strings and their (x,y) positions for diagram text.

    Returns a list of tuples: (label_string, x, y)
    """
    labels: List[Tuple[str, float, float]] = []
    for i, value in enumerate(values_scaled):
        value_string = list_matrix_row[i] * -1
        string = f"{value_string:.{precision}e}"
        x = dist * i
        y = value + offset if value > 0 else value - offset
        labels.append((string, x, y))
    return labels

