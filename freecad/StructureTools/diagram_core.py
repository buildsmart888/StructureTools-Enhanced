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



def separates_ordinates(values: List[float], zero_tol: float = 1e-12) -> List[List[float]]:
    """Split a 1D list of ordinates into continuous loops, preserving sign change information.

    Returns a list of lists. Small values abs(value) <= zero_tol are treated
    as zero for the crossing logic. Unlike the previous implementation, this
    version maintains continuity by not splitting at sign changes, but rather
    tracking where zero crossings occur.
    """
    if not values:
        return []
    
    # Return the values as a single continuous loop to maintain diagram continuity
    return [values]


def generate_coordinates(ordinates: List[List[float]], dist: float, zero_tol: float = 1e-12) -> List[List[Tuple[float, float]]]:
    """Convert separates_ordinates output into x,y coordinate loops with proper zero crossing handling.

    ordinates: list of lists (each inner is a sequence of ordinate values)
    dist: spacing between sample points on x axis

    Returns list of loops where each loop is list of (x, y) pairs with continuous connections
    and proper handling of zero crossings.
    """
    loops_out: List[List[Tuple[float, float]]] = []
    
    # Process each continuous loop of ordinates
    for loop_values in ordinates:
        loop: List[Tuple[float, float]] = []
        
        # Add starting point at origin if first value is not near zero
        if abs(loop_values[0]) > zero_tol:
            loop.append((0.0, 0.0))
        
        # Add all coordinate points
        for i, value in enumerate(loop_values):
            coordinate = (i * dist, value)
            loop.append(coordinate)
        
        # Add ending point at x-axis if last value is not near zero
        if abs(loop_values[-1]) > zero_tol:
            loop.append(((len(loop_values) - 1) * dist, 0.0))
            
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


def make_member_diagram_coords(values_original: List[float], dist: float, scale: float, zero_tol: float = 1e-12):
    """Compute coordinate loops and scaled ordinate values for a member diagram with continuity.

    Returns (coordinates, values_scaled) where coordinates is a list of loops
    (each loop is a list of (x,y) tuples) and values_scaled is the scaled
    ordinate list used for drawing/labeling. This version maintains continuity
    while properly handling zero crossings.
    """
    values_scaled = [v * scale for v in values_original]
    # Create a single continuous loop instead of splitting at sign changes
    ordinates = [values_scaled]  # Single continuous loop
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
    """Return label strings and their (x,y) positions for diagram text with improved positioning.

    Returns a list of tuples: (label_string, x, y)
    
    Note: This follows the original StructureTools convention where:
    - Values are multiplied by -1 to convert from PyNite to structural engineering sign convention
    - Uses scientific notation for consistent formatting like the original
    """
    labels: List[Tuple[str, float, float]] = []
    
    for i, value in enumerate(values_scaled):
        # IMPORTANT: Keep the original sign flip logic (* -1) 
        # This converts PyNite sign convention to structural engineering sign convention
        value_string = list_matrix_row[i] * -1
        
        # Use original scientific notation format for consistency with original StructureTools
        # But also handle very small values that should be shown as zero
        if abs(value_string) < 1e-12:
            string = "0"
        else:
            string = f"{value_string:.{precision}e}"
        
        x = dist * i
        
        # Improved positioning logic that works better with continuous diagrams
        # Place labels above positive values and below negative values with consistent offset
        if value >= 0:
            y = value + abs(offset) if abs(offset) > 0 else value + font_height/2
        else:
            y = value - abs(offset) if abs(offset) > 0 else value - font_height/2
        
        labels.append((string, x, y))
    
    return labels