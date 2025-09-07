"""ProfileGeometryGenerator

Generate simple outline geometry for common steel sections from tabular properties.

This generator produces a minimal geometry_data dict suitable for
`SectionDrawing.SectionDrawer` consumption. It is intentionally simple and
creates rectangular/flange+web outlines for typical W/I sections, angle
sections and rectangular HSS. The resulting geometry contains a `type` and
dimension keys (height, width, web_thickness, flange_thickness, thickness)
and a fallback `drawing_points` polyline when possible.
"""
from __future__ import annotations

from typing import Dict, Any, List, Optional


def _to_float(v) -> Optional[float]:
    try:
        return float(v)
    except Exception:
        return None


def generate_geometry_from_properties(props: Dict[str, Any], name: str = "") -> Dict[str, Any]:
    """Return a geometry_data dict inferred from properties.

    Heuristics:
    - If keys d, bf, tf, tw present -> I_BEAM
    - If keys leg1/leg2/t or A/t -> ANGLE
    - If keys outer_diameter or OD -> CIRCULAR
    - If keys d,bf but no tw/tf -> RECTANGULAR HSS (use t if present)
    - Otherwise return empty dict
    """
    g: Dict[str, Any] = {}

    # Normalize keys lowercased
    lp = {k.lower(): v for k, v in (props.items() if isinstance(props, dict) else [])}

    # Try I-beam (W shapes)
    d = _to_float(lp.get('d') or lp.get('height') or lp.get('h'))
    bf = _to_float(lp.get('bf') or lp.get('b') or lp.get('width'))
    tf = _to_float(lp.get('tf') or lp.get('ft') or lp.get('flange_thickness'))
    tw = _to_float(lp.get('tw') or lp.get('wt') or lp.get('web_thickness'))

    if d and bf and tf and tw:
        g['type'] = 'I_BEAM'
        g['height'] = d
        g['width'] = bf
        g['flange_thickness'] = tf
        g['web_thickness'] = tw
        # Also generate drawing_points using SectionDrawer.calculate_i_beam_outline
        # Use same rectangle outline coordinates as SectionDrawer expects
        h = d
        w = bf
        pts: List[List[float]] = [
            [-w/2, h/2], [w/2, h/2], [w/2, h/2-tf], [tw/2, h/2-tf],
            [tw/2, -h/2+tf], [w/2, -h/2+tf], [w/2, -h/2], [-w/2, -h/2],
            [-w/2, -h/2+tf], [-tw/2, -h/2+tf], [-tw/2, h/2-tf], [-w/2, h/2-tf],
            [-w/2, h/2]
        ]
        g['drawing_points'] = pts
        return g

    # Angle
    leg1 = _to_float(lp.get('leg1') or lp.get('l1') or lp.get('a'))
    leg2 = _to_float(lp.get('leg2') or lp.get('l2') or lp.get('b'))
    t = _to_float(lp.get('t') or lp.get('thickness'))
    if leg1 and leg2 and t:
        g['type'] = 'ANGLE'
        g['leg1'] = leg1
        g['leg2'] = leg2
        g['thickness'] = t
        g['drawing_points'] = [[0, 0], [leg2, 0], [leg2, t], [t, t], [t, leg1], [0, leg1], [0, 0]]
        return g

    # Circular (pipe)
    od = _to_float(lp.get('outer_diameter') or lp.get('od') or lp.get('d'))
    idv = _to_float(lp.get('inner_diameter') or lp.get('id') or lp.get('ri') or 0)
    if od:
        g['type'] = 'CIRCULAR'
        g['outer_diameter'] = od
        g['inner_diameter'] = idv or 0
        return g

    # Rectangular HSS (use d,bf and t)
    if d and bf and t:
        g['type'] = 'RECTANGULAR'
        g['height'] = d
        g['width'] = bf
        g['thickness'] = t
        return g

    # Fallback: if we have numeric width & height -> generic rectangle
    h = d or _to_float(lp.get('height'))
    w = bf or _to_float(lp.get('width'))
    if h and w:
        g['type'] = 'RECTANGULAR'
        g['height'] = h
        g['width'] = w
        return g

    return {}
