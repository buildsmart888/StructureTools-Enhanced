"""ProfileGeometryGenerator

Advanced geometry generation and section property calculation for structural profiles.
Supports comprehensive section property calculations including area, moments of inertia,
section moduli, radii of gyration, and other structural properties.

This generator produces detailed geometry_data suitable for:
- SectionDrawing.SectionDrawer consumption  
- StructuralProfile object property calculation
- Calc system integration with complete structural properties
- Advanced structural analysis workflows
- Precise 2D Face generation for FreeCAD integration

Enhanced to support:
- Complete structural property calculations (A, Ix, Iy, J, Sx, Sy, rx, ry)
- Advanced section types (I-beams, channels, angles, HSS, T-sections)  
- Integration with FreeCAD StructuralProfile objects
- Calc system property export
- Precise 2D geometry generation using boolean operations
"""
from __future__ import annotations

import math
from typing import Dict, Any, List, Optional, Tuple, Union

# FreeCAD imports for advanced geometry generation
try:
    import FreeCAD as App
    import Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False
    App = None
    Part = None


def _to_float(v) -> Optional[float]:
    try:
        return float(v)
    except Exception:
        return None


class AdvancedSectionCalculator:
    """Advanced section property calculator for structural profiles"""
    
    def __init__(self):
        self.steel_density = 7850.0  # kg/m³
    
    def calculate_i_beam_properties(self, height: float, width: float, 
                                  web_thickness: float, flange_thickness: float) -> Dict[str, Any]:
        """Calculate complete I-beam section properties"""
        h, b, tw, tf = height, width, web_thickness, flange_thickness
        
        # Area calculation
        area = 2 * b * tf + (h - 2 * tf) * tw  # mm²
        
        # Moment of inertia about major axis (X) - strong axis
        ix = (b * h**3 - (b - tw) * (h - 2*tf)**3) / 12  # mm⁴
        
        # Moment of inertia about minor axis (Y) - weak axis  
        iy = (2 * tf * b**3 + (h - 2*tf) * tw**3) / 12  # mm⁴
        
        # Torsional constant (simplified for I-sections)
        j = (2 * b * tf**3 + (h - 2*tf) * tw**3) / 3  # mm⁴
        
        # Section moduli
        sx = ix / (h/2) if h > 0 else 0  # mm³
        sy = iy / (b/2) if b > 0 else 0  # mm³
        
        # Plastic section moduli (simplified)
        zx = sx * 1.12 if sx > 0 else 0  # mm³ (approximation)
        zy = sy * 1.15 if sy > 0 else 0  # mm³ (approximation)
        
        # Radii of gyration
        rx = math.sqrt(ix / area) if area > 0 else 0  # mm
        ry = math.sqrt(iy / area) if area > 0 else 0  # mm
        
        # Weight per unit length
        weight = area * self.steel_density * 1e-9  # kg/m
        
        # Warping constant (simplified)
        cw = (h - tf)**2 * b**3 * tf / 24 if b > 0 and tf > 0 else 0  # mm⁶
        
        return {
            'area': area,
            'ix': ix, 'iy': iy, 'j': j,
            'sx': sx, 'sy': sy,
            'zx': zx, 'zy': zy,
            'rx': rx, 'ry': ry,
            'weight': weight,
            'cw': cw,
            'section_type': 'I_BEAM'
        }
    
    def calculate_rectangular_hss_properties(self, height: float, width: float, 
                                           thickness: float) -> Dict[str, Any]:
        """Calculate rectangular HSS section properties"""
        h, b, t = height, width, thickness
        
        # Area calculation
        area = 2 * (h * t + b * t) - 4 * t * t  # mm²
        
        # Moments of inertia (hollow rectangular section)
        ix = (b * h**3 - (b - 2*t) * (h - 2*t)**3) / 12  # mm⁴
        iy = (h * b**3 - (h - 2*t) * (b - 2*t)**3) / 12  # mm⁴
        
        # Torsional constant for rectangular HSS
        a, b_tor = max(h-2*t, b-2*t), min(h-2*t, b-2*t)
        if a > 0 and b_tor > 0:
            # Thin-walled rectangular section
            j = 2 * t * (h - t)**2 * (b - t)**2 / (h + b - 2*t)
        else:
            j = 0
        
        # Section moduli
        sx = ix / (h/2) if h > 0 else 0
        sy = iy / (b/2) if b > 0 else 0
        
        # Plastic section moduli (simplified)
        zx = sx * 1.27 if sx > 0 else 0
        zy = sy * 1.27 if sy > 0 else 0
        
        # Radii of gyration
        rx = math.sqrt(ix / area) if area > 0 else 0
        ry = math.sqrt(iy / area) if area > 0 else 0
        
        # Weight
        weight = area * self.steel_density * 1e-9
        
        return {
            'area': area,
            'ix': ix, 'iy': iy, 'j': j,
            'sx': sx, 'sy': sy,
            'zx': zx, 'zy': zy,
            'rx': rx, 'ry': ry,
            'weight': weight,
            'section_type': 'RECTANGULAR_HSS'
        }
    
    def calculate_circular_hss_properties(self, diameter: float, thickness: float) -> Dict[str, Any]:
        """Calculate circular HSS section properties"""
        d, t = diameter, thickness
        
        # Area calculation
        area = math.pi * (d * t - t * t)  # mm²
        
        # Moments of inertia (hollow circular section)
        ix = iy = math.pi * (d**4 - (d - 2*t)**4) / 64  # mm⁴
        
        # Torsional constant (polar moment for circular sections)
        j = 2 * ix  # mm⁴
        
        # Section moduli
        sx = sy = ix / (d/2) if d > 0 else 0  # mm³
        
        # Plastic section moduli for circular sections
        zx = zy = sx * 4/3 if sx > 0 else 0  # mm³
        
        # Radii of gyration
        rx = ry = math.sqrt(ix / area) if area > 0 else 0  # mm
        
        # Weight
        weight = area * self.steel_density * 1e-9
        
        return {
            'area': area,
            'ix': ix, 'iy': iy, 'j': j,
            'sx': sx, 'sy': sy,
            'zx': zx, 'zy': zy,
            'rx': rx, 'ry': ry,
            'weight': weight,
            'section_type': 'CIRCULAR_HSS'
        }
    
    def calculate_channel_properties(self, height: float, width: float,
                                   web_thickness: float, flange_thickness: float) -> Dict[str, Any]:
        """Calculate channel section properties"""
        h, b, tw, tf = height, width, web_thickness, flange_thickness
        
        # Area calculation
        area = 2 * b * tf + (h - 2 * tf) * tw  # mm²
        
        # Centroidal calculations for unsymmetric section
        # Distance from web to centroid
        y_bar = (2 * b * tf * (b/2) + (h - 2*tf) * tw * 0) / area if area > 0 else 0
        
        # Moment of inertia about major axis
        ix = (tw * h**3 + 2 * b * tf * (h - tf)**2) / 12  # mm⁴ (simplified)
        
        # Moment of inertia about minor axis (considering centroidal shift)
        iy_gross = (2 * tf * b**3 + (h - 2*tf) * tw**3) / 12
        iy = iy_gross + area * y_bar**2 if area > 0 else 0  # mm⁴
        
        # Torsional constant (simplified)
        j = (2 * b * tf**3 + (h - 2*tf) * tw**3) / 3  # mm⁴
        
        # Section moduli
        sx = ix / (h/2) if h > 0 else 0
        sy = iy / max(y_bar, b - y_bar) if y_bar > 0 else 0
        
        # Plastic section moduli (simplified)
        zx = sx * 1.12 if sx > 0 else 0
        zy = sy * 1.15 if sy > 0 else 0
        
        # Radii of gyration
        rx = math.sqrt(ix / area) if area > 0 else 0
        ry = math.sqrt(iy / area) if area > 0 else 0
        
        # Weight
        weight = area * self.steel_density * 1e-9
        
        return {
            'area': area,
            'ix': ix, 'iy': iy, 'j': j,
            'sx': sx, 'sy': sy,
            'zx': zx, 'zy': zy,
            'rx': rx, 'ry': ry,
            'weight': weight,
            'centroidal_distance': y_bar,
            'section_type': 'CHANNEL'
        }
    
    def calculate_angle_properties(self, leg1: float, leg2: float, thickness: float) -> Dict[str, Any]:
        """Calculate angle section properties"""
        a, b, t = leg1, leg2, thickness
        
        # Area calculation
        area = (a + b - t) * t  # mm²
        
        # Centroidal distances for unequal angles
        x_bar = (a**2 * t + b * t * (t/2)) / area if area > 0 else 0
        y_bar = (b**2 * t + a * t * (t/2)) / area if area > 0 else 0
        
        # Moments of inertia about centroidal axes (simplified)
        # These are approximations for angle sections
        ix_approx = (a * t**3 / 3) + t * a**3 / 3
        iy_approx = (b * t**3 / 3) + t * b**3 / 3
        
        # Apply parallel axis theorem
        ix = ix_approx - area * y_bar**2 if area > 0 else 0
        iy = iy_approx - area * x_bar**2 if area > 0 else 0
        
        # Torsional constant (simplified)
        j = (a + b - t) * t**3 / 3  # mm⁴
        
        # Section moduli (simplified)
        sx = ix / max(y_bar, a - y_bar) if y_bar > 0 else 0
        sy = iy / max(x_bar, b - x_bar) if x_bar > 0 else 0
        
        # Radii of gyration
        rx = math.sqrt(ix / area) if area > 0 else 0
        ry = math.sqrt(iy / area) if area > 0 else 0
        
        # Weight
        weight = area * self.steel_density * 1e-9
        
        return {
            'area': area,
            'ix': ix, 'iy': iy, 'j': j,
            'sx': sx, 'sy': sy,
            'rx': rx, 'ry': ry,
            'weight': weight,
            'centroidal_x': x_bar,
            'centroidal_y': y_bar,
            'section_type': 'ANGLE'
        }
    
    def calculate_rectangle_properties(self, height: float, width: float) -> Dict[str, Any]:
        """Calculate solid rectangular section properties"""
        h, b = height, width
        
        # Area
        area = b * h
        
        # Moments of inertia
        ix = b * h**3 / 12
        iy = h * b**3 / 12
        
        # Torsional constant for rectangle
        if b > h:
            a, b_tor = b, h
        else:
            a, b_tor = h, b
        
        j = a * b_tor**3 * (1/3 - 0.21 * (b_tor/a) * (1 - b_tor**4/(12*a**4)))
        
        # Section moduli
        sx = ix / (h/2) if h > 0 else 0
        sy = iy / (b/2) if b > 0 else 0
        
        # Plastic section moduli
        zx = b * h**2 / 4
        zy = h * b**2 / 4
        
        # Radii of gyration
        rx = math.sqrt(ix / area) if area > 0 else 0
        ry = math.sqrt(iy / area) if area > 0 else 0
        
        # Weight
        weight = area * self.steel_density * 1e-9
        
        return {
            'area': area,
            'ix': ix, 'iy': iy, 'j': j,
            'sx': sx, 'sy': sy,
            'zx': zx, 'zy': zy,
            'rx': rx, 'ry': ry,
            'weight': weight,
            'section_type': 'RECTANGLE'
        }
    
    def calculate_circle_properties(self, diameter: float) -> Dict[str, Any]:
        """Calculate solid circular section properties"""
        d = diameter
        r = d / 2
        
        # Area
        area = math.pi * r**2
        
        # Moments of inertia
        ix = iy = math.pi * r**4 / 4
        
        # Torsional constant (polar moment)
        j = math.pi * r**4 / 2
        
        # Section moduli
        sx = sy = ix / r if r > 0 else 0
        
        # Plastic section moduli
        zx = zy = d**3 / 6
        
        # Radii of gyration
        rx = ry = math.sqrt(ix / area) if area > 0 else 0
        
        # Weight
        weight = area * self.steel_density * 1e-9
        
        return {
            'area': area,
            'ix': ix, 'iy': iy, 'j': j,
            'sx': sx, 'sy': sy,
            'zx': zx, 'zy': zy,
            'rx': rx, 'ry': ry,
            'weight': weight,
            'section_type': 'CIRCLE'
        }

# Create global calculator instance
_section_calculator = AdvancedSectionCalculator()


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


def calculate_section_properties_from_dimensions(profile_type: str, dimensions: Dict[str, float]) -> Dict[str, Any]:
    """Calculate complete section properties from profile type and dimensions
    
    Args:
        profile_type: Type of profile ('I_BEAM', 'RECTANGULAR_HSS', 'CIRCULAR_HSS', etc.)
        dimensions: Dictionary of dimensional parameters
        
    Returns:
        Dictionary with complete structural properties
    """
    try:
        if profile_type.upper() in ['I_BEAM', 'WIDE_FLANGE']:
            return _section_calculator.calculate_i_beam_properties(
                dimensions.get('height', 200),
                dimensions.get('width', 100), 
                dimensions.get('web_thickness', 8),
                dimensions.get('flange_thickness', 12)
            )
        
        elif profile_type.upper() == 'RECTANGULAR_HSS':
            return _section_calculator.calculate_rectangular_hss_properties(
                dimensions.get('height', 150),
                dimensions.get('width', 100),
                dimensions.get('thickness', 6)
            )
        
        elif profile_type.upper() == 'CIRCULAR_HSS':
            return _section_calculator.calculate_circular_hss_properties(
                dimensions.get('diameter', 100),
                dimensions.get('thickness', 6)
            )
        
        elif profile_type.upper() == 'CHANNEL':
            return _section_calculator.calculate_channel_properties(
                dimensions.get('height', 200),
                dimensions.get('width', 75),
                dimensions.get('web_thickness', 8),
                dimensions.get('flange_thickness', 12)
            )
        
        elif profile_type.upper() == 'ANGLE':
            return _section_calculator.calculate_angle_properties(
                dimensions.get('leg1', 75),
                dimensions.get('leg2', 50),
                dimensions.get('thickness', 6)
            )
        
        elif profile_type.upper() == 'RECTANGLE':
            return _section_calculator.calculate_rectangle_properties(
                dimensions.get('height', 150),
                dimensions.get('width', 100)
            )
        
        elif profile_type.upper() == 'CIRCLE':
            return _section_calculator.calculate_circle_properties(
                dimensions.get('diameter', 100)
            )
        
        else:
            return {'error': f'Unsupported profile type: {profile_type}'}
            
    except Exception as e:
        return {'error': f'Calculation failed: {str(e)}'}


def generate_calc_properties(section_properties: Dict[str, Any]) -> Dict[str, Any]:
    """Convert section properties to calc-compatible format
    
    Args:
        section_properties: Section properties from calculate_section_properties_from_dimensions
        
    Returns:
        Dictionary formatted for calc system integration
    """
    if 'error' in section_properties:
        return section_properties
    
    try:
        # Convert from mm units to meter units for calc
        calc_props = {
            'Area': section_properties.get('area', 0) / 1e6,      # mm² to m²
            'Iy': section_properties.get('ix', 0) / 1e12,         # mm⁴ to m⁴ (major axis)
            'Iz': section_properties.get('iy', 0) / 1e12,         # mm⁴ to m⁴ (minor axis)
            'J': section_properties.get('j', 0) / 1e12,           # mm⁴ to m⁴
            'Sy': section_properties.get('sx', 0) / 1e9,          # mm³ to m³ (major axis)
            'Sz': section_properties.get('sy', 0) / 1e9,          # mm³ to m³ (minor axis)
            'ry': section_properties.get('rx', 0) / 1000,         # mm to m (major axis)
            'rz': section_properties.get('ry', 0) / 1000,         # mm to m (minor axis)
            'Weight': section_properties.get('weight', 0),        # kg/m (already correct)
            'SectionType': section_properties.get('section_type', 'UNKNOWN')
        }
        
        # Add plastic moduli if available
        if 'zx' in section_properties:
            calc_props['Zy'] = section_properties['zx'] / 1e9    # mm³ to m³
        if 'zy' in section_properties:
            calc_props['Zz'] = section_properties['zy'] / 1e9    # mm³ to m³
        
        # Add warping constant if available
        if 'cw' in section_properties:
            calc_props['Cw'] = section_properties['cw'] / 1e18   # mm⁶ to m⁶
        
        # Add centroidal information for unsymmetric sections
        if 'centroidal_distance' in section_properties:
            calc_props['CentroidalDistance'] = section_properties['centroidal_distance'] / 1000  # mm to m
        
        if 'centroidal_x' in section_properties:
            calc_props['CentroidalX'] = section_properties['centroidal_x'] / 1000  # mm to m
        if 'centroidal_y' in section_properties:
            calc_props['CentroidalY'] = section_properties['centroidal_y'] / 1000  # mm to m
        
        return calc_props
        
    except Exception as e:
        return {'error': f'Calc property conversion failed: {str(e)}'}


def create_profile_geometry_data(profile_type: str, dimensions: Dict[str, float]) -> Dict[str, Any]:
    """Create complete geometry data for profile including drawing points and properties
    
    Args:
        profile_type: Type of profile
        dimensions: Dimensional parameters
        
    Returns:
        Complete geometry data dictionary
    """
    try:
        # Generate basic geometry data using existing function
        basic_props = {k.lower(): v for k, v in dimensions.items()}  # Normalize keys
        basic_geometry = generate_geometry_from_properties(basic_props)
        
        # Calculate advanced properties
        advanced_properties = calculate_section_properties_from_dimensions(profile_type, dimensions)
        
        # Generate calc properties
        calc_properties = generate_calc_properties(advanced_properties)
        
        # Combine all data
        complete_geometry = {
            # Basic geometry information
            'type': basic_geometry.get('type', profile_type.upper()),
            'profile_type': profile_type,
            'dimensions': dimensions,
            
            # Drawing data
            'drawing_points': basic_geometry.get('drawing_points', []),
            
            # Complete structural properties
            'properties': advanced_properties,
            
            # Calc-ready properties
            'calc_properties': calc_properties,
            
            # Metadata
            'units': {
                'length': 'mm',
                'area': 'mm²', 
                'moment_inertia': 'mm⁴',
                'section_modulus': 'mm³',
                'weight': 'kg/m'
            },
            'generated_by': 'StructureTools_ProfileGeometryGenerator'
        }
        
        return complete_geometry
        
    except Exception as e:
        return {'error': f'Geometry data creation failed: {str(e)}'}


def get_supported_profile_types() -> List[str]:
    """Get list of supported profile types"""
    return [
        'I_BEAM',
        'WIDE_FLANGE', 
        'CHANNEL',
        'ANGLE',
        'RECTANGULAR_HSS',
        'CIRCULAR_HSS', 
        'RECTANGLE',
        'CIRCLE',
        'T_SECTION'
    ]


def get_required_dimensions(profile_type: str) -> List[str]:
    """Get required dimensions for a profile type"""
    requirements = {
        'I_BEAM': ['height', 'width', 'web_thickness', 'flange_thickness'],
        'WIDE_FLANGE': ['height', 'width', 'web_thickness', 'flange_thickness'],
        'CHANNEL': ['height', 'width', 'web_thickness', 'flange_thickness'],
        'RECTANGULAR_HSS': ['height', 'width', 'thickness'],
        'CIRCULAR_HSS': ['diameter', 'thickness'],
        'RECTANGLE': ['height', 'width'],
        'CIRCLE': ['diameter'],
        'ANGLE': ['leg1', 'leg2', 'thickness'],
        'T_SECTION': ['height', 'width', 'web_thickness', 'flange_thickness']
    }
    
    return requirements.get(profile_type.upper(), [])


# ================================================================================================
# ADVANCED GEOMETRY GENERATOR - Precise 2D Face Generation
# ================================================================================================

class AdvancedGeometryGenerator:
    """
    Advanced 2D geometry generator using precise boolean operations
    Inspired by professional steel profile modeling techniques
    """
    
    def __init__(self):
        self.unit_factor = 1.0  # Default: mm
        
    def mm(self, val):
        """Convert value to working units (future flexibility)"""
        return float(val) * self.unit_factor
    
    def make_face_from_points(self, points) -> 'Part.Face':
        """Create Part.Face from list of (x,y) points with automatic closure"""
        if not FREECAD_AVAILABLE:
            raise ImportError("FreeCAD not available for geometry generation")
            
        pts = [App.Vector(x, y, 0) for (x, y) in points]
        if pts[0].distanceToPoint(pts[-1]) > 1e-9:
            pts.append(pts[0])  # Close polygon automatically
        wire = Part.makePolygon(pts)
        return Part.Face(wire)
    
    def diff_face(self, outer: 'Part.Face', inner: 'Part.Face') -> 'Part.Face':
        """Boolean subtraction: outer - inner (for hollow sections)"""
        return outer.cut(inner)
    
    def create_i_beam_face(self, d: float, bf: float, tw: float, tf: float) -> 'Part.Face':
        """
        Create precise I/W-beam 2D face using boolean operations
        
        Args:
            d: Overall depth (height)
            bf: Flange width  
            tw: Web thickness
            tf: Flange thickness
            
        Returns:
            Part.Face representing I-beam cross-section
        """
        d, bf, tw, tf = map(self.mm, (d, bf, tw, tf))
        
        # Create outer rectangular boundary
        outer = self.make_face_from_points([
            (-bf/2, -d/2), (bf/2, -d/2), (bf/2, d/2), (-bf/2, d/2)
        ])
        
        # Calculate clear web height between flanges
        clear_web_y = (d - 2*tf) / 2.0
        half_web = tw / 2.0
        
        # Create cutout regions
        # Top cutout (above upper flange)
        inner_top = self.make_face_from_points([
            (-bf/2,  tf/2 + clear_web_y), (bf/2,  tf/2 + clear_web_y),
            (bf/2,  d/2), (-bf/2,  d/2)
        ])
        
        # Bottom cutout (below lower flange) 
        inner_bot = self.make_face_from_points([
            (-bf/2, -d/2), (bf/2, -d/2),
            (bf/2, -tf/2 - clear_web_y), (-bf/2, -tf/2 - clear_web_y)
        ])
        
        # Left side cutout (beside web in flange region)
        inner_left = self.make_face_from_points([
            (-bf/2, -tf/2), (-half_web, -tf/2), 
            (-half_web, tf/2), (-bf/2, tf/2)
        ])
        
        # Right side cutout (beside web in flange region)
        inner_right = self.make_face_from_points([
            (half_web, -tf/2), (bf/2, -tf/2),
            (bf/2, tf/2), (half_web, tf/2)
        ])
        
        # Perform boolean operations
        face = outer.cut(inner_top).cut(inner_bot).cut(inner_left).cut(inner_right)
        return face
    
    def create_channel_face(self, d: float, bf: float, tw: float, tf: float) -> 'Part.Face':
        """
        Create C-channel 2D face (opening to the right)
        Reference axis through web centerline
        """
        d, bf, tw, tf = map(self.mm, (d, bf, tw, tf))
        
        # Outer boundary
        outer = self.make_face_from_points([
            (0, -d/2), (bf, -d/2), (bf, d/2), (0, d/2)
        ])
        
        # Inner cutout (leaving flanges and web)
        inner = self.make_face_from_points([
            (tw, -d/2 + tf), (bf, -d/2 + tf), 
            (bf, d/2 - tf), (tw, d/2 - tf)
        ])
        
        return self.diff_face(outer, inner)
    
    def create_angle_face(self, b: float, d: float, t: float) -> 'Part.Face':
        """
        Create L-angle 2D face
        Corner at origin (0,0), extending to +x and +y
        """
        b, d, t = map(self.mm, (b, d, t))
        
        # L-shape outline (no cutouts needed)
        points = [
            (0, 0), (b, 0), (b, t), (t, t), (t, d), (0, d)
        ]
        
        return self.make_face_from_points(points)
    
    def create_hss_rect_face(self, H: float, B: float, t: float) -> 'Part.Face':
        """
        Create rectangular HSS (hollow structural section) 2D face
        Centered at origin
        """
        H, B, t = map(self.mm, (H, B, t))
        
        # Outer rectangle
        outer = self.make_face_from_points([
            (-B/2, -H/2), (B/2, -H/2), (B/2, H/2), (-B/2, H/2)
        ])
        
        # Inner rectangle (hollow center)
        inner = self.make_face_from_points([
            (-(B/2 - t), -(H/2 - t)), ((B/2 - t), -(H/2 - t)),
            ((B/2 - t), (H/2 - t)), (-(B/2 - t), (H/2 - t))
        ])
        
        return self.diff_face(outer, inner)
    
    def create_pipe_face(self, Do: float, t: float) -> 'Part.Face':
        """
        Create circular pipe/HSS 2D face
        
        Args:
            Do: Outside diameter
            t: Wall thickness
        """
        if not FREECAD_AVAILABLE:
            raise ImportError("FreeCAD not available for circular geometry")
            
        Do, t = map(self.mm, (Do, t))
        Ro = Do / 2.0
        Ri = Ro - t
        
        # Create outer and inner circles
        outer = Part.Face(Part.Wire(Part.makeCircle(Ro, App.Vector(0, 0, 0))))
        inner = Part.Face(Part.Wire(Part.makeCircle(Ri, App.Vector(0, 0, 0))))
        
        return self.diff_face(outer, inner)
    
    def create_solid_circle_face(self, D: float) -> 'Part.Face':
        """Create solid circular face (round bar)"""
        if not FREECAD_AVAILABLE:
            raise ImportError("FreeCAD not available for circular geometry")
            
        R = self.mm(D) / 2.0
        return Part.Face(Part.Wire(Part.makeCircle(R, App.Vector(0, 0, 0))))
    
    def create_t_section_face(self, d: float, bf: float, tw: float, tf: float) -> 'Part.Face':
        """
        Create T-section 2D face (half of I-beam, web extends downward)
        """
        d, bf, tw, tf = map(self.mm, (d, bf, tw, tf))
        
        # Create as modified rectangle with T-shape cutouts
        outer = self.make_face_from_points([
            (-bf/2, 0), (bf/2, 0), (bf/2, tf), 
            (tw/2, tf), (tw/2, d), (-tw/2, d), 
            (-tw/2, tf), (-bf/2, tf)
        ])
        
        return outer
    
    def create_profile_face(self, profile_type: str, dimensions: Dict[str, float]) -> Optional['Part.Face']:
        """
        Create 2D face for any supported profile type
        
        Args:
            profile_type: Type of profile ('I-Beam', 'Channel', etc.)
            dimensions: Dictionary of dimensional parameters
            
        Returns:
            Part.Face object or None if failed
        """
        if not FREECAD_AVAILABLE:
            return None
            
        try:
            profile_type = profile_type.upper().replace('-', '_').replace(' ', '_')
            
            if profile_type in ['I_BEAM', 'WIDE_FLANGE']:
                return self.create_i_beam_face(
                    dimensions['height'], dimensions['width'],
                    dimensions['web_thickness'], dimensions['flange_thickness']
                )
                
            elif profile_type == 'CHANNEL':
                return self.create_channel_face(
                    dimensions['height'], dimensions['width'],
                    dimensions['web_thickness'], dimensions['flange_thickness']  
                )
                
            elif profile_type == 'ANGLE':
                return self.create_angle_face(
                    dimensions.get('leg1', dimensions.get('width', 0)),
                    dimensions.get('leg2', dimensions.get('height', 0)),
                    dimensions['thickness']
                )
                
            elif profile_type in ['HSS_RECTANGULAR', 'RECTANGULAR_HSS']:
                return self.create_hss_rect_face(
                    dimensions['height'], dimensions['width'], dimensions['thickness']
                )
                
            elif profile_type in ['HSS_CIRCULAR', 'CIRCULAR_HSS', 'PIPE']:
                return self.create_pipe_face(
                    dimensions['diameter'], dimensions['thickness']
                )
                
            elif profile_type == 'CIRCLE':
                return self.create_solid_circle_face(dimensions['diameter'])
                
            elif profile_type == 'T_SECTION':
                return self.create_t_section_face(
                    dimensions['height'], dimensions['width'],
                    dimensions['web_thickness'], dimensions['flange_thickness']
                )
                
            else:
                return None
                
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"Profile face creation failed: {e}\n")
            return None


# Global instance for easy access
advanced_geometry_generator = AdvancedGeometryGenerator()


# ================================================================================================
# CSV DATABASE INTEGRATION - Enhanced Profile Database Loading
# ================================================================================================

def read_csv_profile(csv_path: str, designation: str, 
                    headers_candidates: List[str] = None) -> Optional[Dict[str, str]]:
    """
    Read profile data from CSV database file
    
    Args:
        csv_path: Path to CSV database file
        designation: Profile designation to find (e.g., "W12X26", "HSS6X4X3/8")
        headers_candidates: List of possible header names for designation column
        
    Returns:
        Dictionary of profile properties or None if not found
    """
    import csv
    import os
    
    if not os.path.exists(csv_path):
        return None
        
    if headers_candidates is None:
        headers_candidates = ["Designation", "AISC_Manual_Label", "Label", "Shape", "Profile"]
    
    try:
        with open(csv_path, newline='', encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            
            # Find designation column
            header_design = None
            for h in headers_candidates:
                if h in reader.fieldnames:
                    header_design = h
                    break
                    
            if header_design is None:
                return None
                
            # Search for matching designation
            for row in reader:
                if row[header_design].strip() == designation.strip():
                    return row
                    
    except Exception:
        return None
        
    return None


def create_profile_from_csv_database(csv_path: str, designation: str, 
                                   profile_type: str = None) -> Optional['Part.Face']:
    """
    Create profile geometry directly from CSV database
    
    Args:
        csv_path: Path to CSV database file
        designation: Profile designation (e.g., "W12X26")
        profile_type: Profile type override (auto-detect if None)
        
    Returns:
        Part.Face geometry or None if failed
    """
    if not FREECAD_AVAILABLE:
        return None
        
    # Read profile data from CSV
    row = read_csv_profile(csv_path, designation)
    if not row:
        return None
    
    # Auto-detect profile type from filename if not provided
    if profile_type is None:
        import os
        fname = os.path.basename(csv_path).lower()
        if fname.startswith(("w_", "hp_", "s_", "m_")):
            profile_type = "I-Beam"
        elif fname.startswith(("wt_", "mt_")):
            profile_type = "T-Section" 
        elif fname.startswith(("c_", "mc_")):
            profile_type = "Channel"
        elif fname.startswith(("hss_r", "pipe")):
            profile_type = "HSS Circular"
        elif fname.startswith(("hss_", "rhs_")):
            profile_type = "HSS Rectangular"
        elif fname.startswith(("l_", "dbl_l", "ll_")):
            profile_type = "Angle"
        else:
            return None
    
    # Extract dimensions using flexible column mapping
    def get_value(keys: List[str], default: float = 0.0) -> float:
        for k in keys:
            if k in row and row[k].strip() != "":
                try:
                    return float(row[k])
                except:
                    continue
        return default
    
    # Build dimensions dictionary based on profile type
    dimensions = {}
    
    if profile_type in ["I-Beam", "Wide Flange"]:
        dimensions = {
            'height': get_value(["d", "Depth", "h", "OD"]),
            'width': get_value(["bf", "FlangeWidth", "b"]),
            'web_thickness': get_value(["tw", "WebThickness", "tw_web"]),
            'flange_thickness': get_value(["tf", "FlangeThickness", "tf_flange"])
        }
        
    elif profile_type == "T-Section":
        dimensions = {
            'height': get_value(["d", "Depth", "h"]),
            'width': get_value(["bf", "FlangeWidth", "b"]),
            'web_thickness': get_value(["tw", "WebThickness"]),
            'flange_thickness': get_value(["tf", "FlangeThickness"])
        }
        
    elif profile_type == "Channel":
        dimensions = {
            'height': get_value(["d", "Depth", "h"]),
            'width': get_value(["bf", "FlangeWidth", "b"]),
            'web_thickness': get_value(["tw", "WebThickness"]),
            'flange_thickness': get_value(["tf", "FlangeThickness"])
        }
        
    elif profile_type == "Angle":
        dimensions = {
            'leg1': get_value(["b", "Leg1", "bf", "Width"]),
            'leg2': get_value(["d", "Leg2", "Depth", "h"]),
            'thickness': get_value(["t", "Thickness", "tw", "tf"])
        }
        
    elif profile_type == "HSS Rectangular":
        dimensions = {
            'height': get_value(["H", "h", "Depth", "d", "ODh"]),
            'width': get_value(["B", "b", "Width", "bf", "ODb"]),
            'thickness': get_value(["t", "Thickness", "tw"])
        }
        
    elif profile_type in ["HSS Circular", "Pipe"]:
        dimensions = {
            'diameter': get_value(["Do", "OD", "OutsideDiameter", "d", "Depth"]),
            'thickness': get_value(["t", "Thickness"])
        }
        
    else:
        return None
    
    # Create geometry using advanced generator
    return advanced_geometry_generator.create_profile_face(profile_type, dimensions)


def get_available_profiles_from_csv(csv_path: str, 
                                   headers_candidates: List[str] = None) -> List[str]:
    """
    Get list of available profile designations from CSV database
    
    Args:
        csv_path: Path to CSV database file
        headers_candidates: List of possible header names
        
    Returns:
        List of profile designations
    """
    import csv
    import os
    
    if not os.path.exists(csv_path):
        return []
        
    if headers_candidates is None:
        headers_candidates = ["Designation", "AISC_Manual_Label", "Label", "Shape", "Profile"]
    
    profiles = []
    
    try:
        with open(csv_path, newline='', encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            
            # Find designation column
            header_design = None
            for h in headers_candidates:
                if h in reader.fieldnames:
                    header_design = h
                    break
                    
            if header_design is None:
                return []
                
            # Extract all designations
            for row in reader:
                designation = row[header_design].strip()
                if designation:
                    profiles.append(designation)
                    
    except Exception:
        return []
        
    return profiles


# Legacy compatibility class
class ProfileGeometryGenerator(AdvancedSectionCalculator):
    """
    Legacy compatibility class for ProfileGeometryGenerator
    
    This class provides backward compatibility while using the new 
    AdvancedSectionCalculator as the base implementation.
    """
    
    def __init__(self):
        super().__init__()
        self.advanced_generator = AdvancedGeometryGenerator() if FREECAD_AVAILABLE else None
    
    def generate_i_beam_geometry(self, height: float, width: float, 
                               web_thickness: float, flange_thickness: float, 
                               name: str = "I-Beam") -> Optional[Dict[str, Any]]:
        """Generate I-beam geometry and properties"""
        try:
            # Calculate section properties
            properties = self.calculate_i_beam_properties(
                height, width, web_thickness, flange_thickness
            )
            
            # Create geometry data dictionary
            geometry_data = {
                'name': name,
                'profile_type': 'I-Beam',
                'dimensions': {
                    'height': height,
                    'width': width, 
                    'web_thickness': web_thickness,
                    'flange_thickness': flange_thickness
                }
            }
            
            # Add calculated properties
            geometry_data.update(properties)
            
            # Generate face geometry if FreeCAD available
            if self.advanced_generator:
                face = self.advanced_generator.face_w_like(
                    d=height, bf=width, tw=web_thickness, tf=flange_thickness
                )
                geometry_data['face'] = face
            
            return geometry_data
            
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"I-beam geometry generation failed: {e}\n")
            return None
    
    def generate_rectangle_geometry(self, width: float, height: float, 
                                  name: str = "Rectangle") -> Optional[Dict[str, Any]]:
        """Generate rectangular section geometry and properties"""
        try:
            # Calculate section properties
            properties = self.calculate_rectangular_properties(width, height)
            
            geometry_data = {
                'name': name,
                'profile_type': 'Rectangle',
                'dimensions': {'width': width, 'height': height}
            }
            
            geometry_data.update(properties)
            
            # Generate face geometry if FreeCAD available
            if self.advanced_generator:
                face = self.advanced_generator.face_rectangular_like(width, height)
                geometry_data['face'] = face
            
            return geometry_data
            
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"Rectangle geometry generation failed: {e}\n")
            return None
    
    def generate_circle_geometry(self, diameter: float, 
                               name: str = "Circle") -> Optional[Dict[str, Any]]:
        """Generate circular section geometry and properties"""
        try:
            # Calculate section properties
            properties = self.calculate_circular_properties(diameter)
            
            geometry_data = {
                'name': name,
                'profile_type': 'Circle',
                'dimensions': {'diameter': diameter}
            }
            
            geometry_data.update(properties)
            
            # Generate face geometry if FreeCAD available  
            if self.advanced_generator:
                face = self.advanced_generator.face_circular_like(diameter)
                geometry_data['face'] = face
            
            return geometry_data
            
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"Circle geometry generation failed: {e}\n")
            return None
    
    def generate_hss_geometry(self, height: float, width: float, thickness: float,
                            name: str = "HSS") -> Optional[Dict[str, Any]]:
        """Generate HSS (hollow structural section) geometry and properties"""
        try:
            # Calculate section properties
            properties = self.calculate_hss_properties(height, width, thickness)
            
            geometry_data = {
                'name': name,
                'profile_type': 'HSS',
                'dimensions': {
                    'height': height,
                    'width': width,
                    'thickness': thickness
                }
            }
            
            geometry_data.update(properties)
            
            # Generate face geometry if FreeCAD available
            if self.advanced_generator:
                face = self.advanced_generator.face_hss_like(height, width, thickness)
                geometry_data['face'] = face
            
            return geometry_data
            
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"HSS geometry generation failed: {e}\n")
            return None
    
    def generate_channel_geometry(self, height: float, width: float, 
                                web_thickness: float, flange_thickness: float,
                                name: str = "Channel") -> Optional[Dict[str, Any]]:
        """Generate channel section geometry and properties"""
        try:
            # Calculate section properties
            properties = self.calculate_channel_properties(
                height, width, web_thickness, flange_thickness
            )
            
            geometry_data = {
                'name': name,
                'profile_type': 'Channel',
                'dimensions': {
                    'height': height,
                    'width': width,
                    'web_thickness': web_thickness,
                    'flange_thickness': flange_thickness
                }
            }
            
            geometry_data.update(properties)
            
            # Generate face geometry if FreeCAD available
            if self.advanced_generator:
                face = self.advanced_generator.face_c_like(
                    d=height, bf=width, tw=web_thickness, tf=flange_thickness
                )
                geometry_data['face'] = face
            
            return geometry_data
            
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"Channel geometry generation failed: {e}\n")
            return None
    
    def generate_angle_geometry(self, leg1: float, leg2: float, thickness: float,
                              name: str = "Angle") -> Optional[Dict[str, Any]]:
        """Generate angle section geometry and properties"""
        try:
            # Calculate section properties
            properties = self.calculate_angle_properties(leg1, leg2, thickness)
            
            geometry_data = {
                'name': name,
                'profile_type': 'Angle',
                'dimensions': {
                    'leg1': leg1,
                    'leg2': leg2,
                    'thickness': thickness
                }
            }
            
            geometry_data.update(properties)
            
            # Generate face geometry if FreeCAD available
            if self.advanced_generator:
                face = self.advanced_generator.face_l_like(leg1, leg2, thickness)
                geometry_data['face'] = face
            
            return geometry_data
            
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"Angle geometry generation failed: {e}\n")
            return None
