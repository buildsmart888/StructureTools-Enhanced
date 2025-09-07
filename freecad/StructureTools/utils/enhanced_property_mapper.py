"""Standardize enhanced/steelpy section properties into a stable mapping

This helper converts both enhanced-database dict formats and simple numeric
dicts into a predictable dictionary with SI units (mm, mm^2, mm^4, mm^3).
"""
from typing import Dict, Any

def _get_value(v):
    if isinstance(v, dict) and 'value' in v:
        return v['value']
    return v

def standardize_section_properties(properties: Dict[str, Any]) -> Dict[str, Any]:
    """Return a standardized mapping of commonly used section properties.

    Keys returned (best-effort):
      - name
      - area_mm2
      - weight_kgpm
      - height_mm, width_mm
      - web_thickness_mm, flange_thickness_mm
      - Ix_mm4, Iy_mm4
      - Sx_mm3, Sy_mm3
      - J_mm4
      - rx_mm, ry_mm
      - original: original properties dict (for reference)

    The function is intentionally conservative and uses common alternate keys.
    """
    if not properties:
        return {}

    p = properties
    get = lambda *keys: next((_get_value(p[k]) for k in keys if k in p), None)

    mapping = {
        'name': p.get('name') or p.get('label') or p.get('section_name'),
        'area_mm2': get('area', 'A'),
        'weight_kgpm': get('weight', 'w'),
        'height_mm': get('height', 'd', 'h'),
        'width_mm': get('width', 'bf', 'b'),
        'web_thickness_mm': get('web_thickness', 'tw'),
        'flange_thickness_mm': get('flange_thickness', 'tf'),
        'Ix_mm4': get('moment_inertia_x', 'ix', 'Ixx', 'Ix'),
        'Iy_mm4': get('moment_inertia_y', 'iy', 'Iyy', 'Iy'),
        'Sx_mm3': get('section_modulus_x', 'sx', 'Sx'),
        'Sy_mm3': get('section_modulus_y', 'sy', 'Sy'),
        'J_mm4': get('torsional_constant', 'j', 'J'),
        'rx_mm': get('radius_gyration_x', 'rx'),
        'ry_mm': get('radius_gyration_y', 'ry'),
        'original': properties
    }

    # Ensure numeric normalization where possible (leave None if missing)
    for k in ['area_mm2','weight_kgpm','height_mm','width_mm','web_thickness_mm','flange_thickness_mm',
              'Ix_mm4','Iy_mm4','Sx_mm3','Sy_mm3','J_mm4','rx_mm','ry_mm']:
        v = mapping.get(k)
        try:
            if v is not None:
                mapping[k] = float(v)
        except Exception:
            # keep original value if conversion fails
            pass

    return mapping
