# -*- coding: utf-8 -*-
"""
Geometry Generators for Section Shapes

Modular geometry generation system for different section types.
Each generator is responsible for creating specific section geometries.
"""

import math
from typing import Dict, Optional
from abc import ABC, abstractmethod

# Try to import FreeCAD, with fallback for testing
try:
    import FreeCAD
    import Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False
    # Mock FreeCAD objects for testing
    class MockVector:
        def __init__(self, x, y, z):
            self.x, self.y, self.z = x, y, z
    
    class MockPart:
        @staticmethod
        def makePolygon(points):
            return MockShape()
        @staticmethod
        def Face(wire):
            return MockShape()
        @staticmethod
        def makeCircle(radius, center):
            return MockShape()
    
    class MockShape:
        def cut(self, other):
            return MockShape()
    
    FreeCAD = type('FreeCAD', (), {'Vector': MockVector})()
    Part = MockPart()

class SectionGeometryGenerator(ABC):
    """Base class for section geometry generators."""
    
    @abstractmethod
    def generate(self, section_properties: Dict):
        """Generate section geometry from properties."""
        pass
    
    @abstractmethod
    def validate_properties(self, properties: Dict) -> bool:
        """Validate required properties for this generator."""
        pass

class IBeamGenerator(SectionGeometryGenerator):
    """Generator for I-beam sections (W, IPE, HEB)."""
    
    def validate_properties(self, properties: Dict) -> bool:
        """Validate required properties for I-beam generation."""
        required = ["Depth", "FlangeWidth", "WebThickness", "FlangeThickness"]
        return all(prop in properties for prop in required)
    
    def generate(self, section_properties: Dict):
        """Generate I-beam geometry."""
        if not FREECAD_AVAILABLE:
            return None
        
        try:
            if not self.validate_properties(section_properties):
                raise ValueError("Missing required properties for I-beam generation")
            
            # Extract dimensions
            d = float(section_properties["Depth"])
            bf = float(section_properties["FlangeWidth"])
            tw = float(section_properties["WebThickness"])
            tf = float(section_properties["FlangeThickness"])
            
            # Engineering validation
            self._validate_i_beam_dimensions(d, bf, tw, tf)
            
            # Generate optimized I-beam profile
            return self._create_i_beam_profile(d, bf, tw, tf)
            
        except Exception as e:
            raise RuntimeError(f"Error generating I-beam geometry: {str(e)}")
    
    def _validate_i_beam_dimensions(self, d: float, bf: float, tw: float, tf: float):
        """Validate I-beam dimensions for engineering reasonableness."""
        if d <= 0 or bf <= 0 or tw <= 0 or tf <= 0:
            raise ValueError("All I-beam dimensions must be positive")
        
        if tw >= bf:
            raise ValueError(f"Web thickness ({tw}) cannot exceed flange width ({bf})")
        
        if 2*tf >= d:
            raise ValueError(f"Total flange thickness ({2*tf}) cannot exceed depth ({d})")
        
        # Engineering limits
        if d/bf > 10:
            raise ValueError(f"Excessive depth/width ratio: {d/bf:.2f}")
        
        if bf/tw > 100:
            raise ValueError(f"Excessive flange width/web thickness ratio: {bf/tw:.1f}")
    
    def _create_i_beam_profile(self, d: float, bf: float, tw: float, tf: float):
        """Create optimized I-beam profile with rounded corners."""
        try:
            # Option for rounded corners (more realistic)
            use_rounded_corners = True
            corner_radius = min(tf/4, tw/4, 3.0)  # Typical corner radius
            
            if use_rounded_corners and corner_radius > 0.5:
                return self._create_rounded_i_beam(d, bf, tw, tf, corner_radius)
            else:
                return self._create_sharp_i_beam(d, bf, tw, tf)
                
        except Exception as e:
            # Fallback to sharp corners if rounded fails
            return self._create_sharp_i_beam(d, bf, tw, tf)
    
    def _create_sharp_i_beam(self, d: float, bf: float, tw: float, tf: float):
        """Create I-beam with sharp corners."""
        points = [
            FreeCAD.Vector(-bf/2, -d/2, 0),         # 1. Bottom left outer
            FreeCAD.Vector(bf/2, -d/2, 0),          # 2. Bottom right outer
            FreeCAD.Vector(bf/2, -d/2+tf, 0),       # 3. Bottom right inner
            FreeCAD.Vector(tw/2, -d/2+tf, 0),       # 4. Web bottom right
            FreeCAD.Vector(tw/2, d/2-tf, 0),        # 5. Web top right
            FreeCAD.Vector(bf/2, d/2-tf, 0),        # 6. Top right inner
            FreeCAD.Vector(bf/2, d/2, 0),           # 7. Top right outer
            FreeCAD.Vector(-bf/2, d/2, 0),          # 8. Top left outer
            FreeCAD.Vector(-bf/2, d/2-tf, 0),       # 9. Top left inner
            FreeCAD.Vector(-tw/2, d/2-tf, 0),       # 10. Web top left
            FreeCAD.Vector(-tw/2, -d/2+tf, 0),      # 11. Web bottom left
            FreeCAD.Vector(-bf/2, -d/2+tf, 0),      # 12. Bottom left inner
            FreeCAD.Vector(-bf/2, -d/2, 0)          # 13. Close polygon
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)
    
    def _create_rounded_i_beam(self, d: float, bf: float, tw: float, tf: float, r: float):
        """Create I-beam with rounded fillets (more complex but realistic)."""
        # This is a simplified version - actual implementation would use proper fillets
        # For now, return sharp version
        return self._create_sharp_i_beam(d, bf, tw, tf)

class RectangularHSSGenerator(SectionGeometryGenerator):
    """Generator for rectangular HSS sections."""
    
    def validate_properties(self, properties: Dict) -> bool:
        """Validate required properties."""
        required = ["Depth", "Width", "WallThickness"]
        return all(prop in properties for prop in required)
    
    def generate(self, section_properties: Dict):
        """Generate rectangular HSS geometry."""
        if not FREECAD_AVAILABLE:
            return None
        
        try:
            if not self.validate_properties(section_properties):
                raise ValueError("Missing required properties for rectangular HSS")
            
            h = float(section_properties["Depth"])
            b = float(section_properties["Width"])
            t = float(section_properties["WallThickness"])
            
            # Validation
            self._validate_rectangular_hss(h, b, t)
            
            return self._create_rectangular_hss_profile(h, b, t)
            
        except Exception as e:
            raise RuntimeError(f"Error generating rectangular HSS: {str(e)}")
    
    def _validate_rectangular_hss(self, h: float, b: float, t: float):
        """Validate rectangular HSS dimensions."""
        if h <= 0 or b <= 0 or t <= 0:
            raise ValueError("All HSS dimensions must be positive")
        
        if 2*t >= h or 2*t >= b:
            raise ValueError(f"Wall thickness ({t}) too large for section ({h}x{b})")
        
        # Check reasonable proportions
        if h/t > 100 or b/t > 100:
            raise ValueError(f"Excessive slenderness: h/t={h/t:.1f}, b/t={b/t:.1f}")
    
    def _create_rectangular_hss_profile(self, h: float, b: float, t: float):
        """Create rectangular HSS profile with proper corner treatment."""
        try:
            # Option for rounded corners (more realistic for HSS)
            use_rounded_corners = True
            corner_radius = min(2*t, min(h, b)/8)  # Typical HSS corner radius
            
            if use_rounded_corners and corner_radius > 0.5:
                return self._create_rounded_rectangular_hss(h, b, t, corner_radius)
            else:
                return self._create_sharp_rectangular_hss(h, b, t)
                
        except Exception:
            # Fallback to sharp corners
            return self._create_sharp_rectangular_hss(h, b, t)
    
    def _create_sharp_rectangular_hss(self, h: float, b: float, t: float):
        """Create rectangular HSS with sharp corners."""
        # Outer rectangle
        outer_points = [
            FreeCAD.Vector(-b/2, -h/2, 0),
            FreeCAD.Vector(b/2, -h/2, 0),
            FreeCAD.Vector(b/2, h/2, 0),
            FreeCAD.Vector(-b/2, h/2, 0),
            FreeCAD.Vector(-b/2, -h/2, 0)
        ]
        
        # Inner rectangle (hole)
        inner_points = [
            FreeCAD.Vector(-(b/2-t), -(h/2-t), 0),
            FreeCAD.Vector((b/2-t), -(h/2-t), 0),
            FreeCAD.Vector((b/2-t), (h/2-t), 0),
            FreeCAD.Vector(-(b/2-t), (h/2-t), 0),
            FreeCAD.Vector(-(b/2-t), -(h/2-t), 0)
        ]
        
        outer_wire = Part.makePolygon(outer_points)
        inner_wire = Part.makePolygon(inner_points)
        
        outer_face = Part.Face(outer_wire)
        inner_face = Part.Face(inner_wire)
        
        return outer_face.cut(inner_face)
    
    def _create_rounded_rectangular_hss(self, h: float, b: float, t: float, r: float):
        """Create rectangular HSS with rounded corners."""
        # Simplified version - return sharp for now
        return self._create_sharp_rectangular_hss(h, b, t)

class CircularHSSGenerator(SectionGeometryGenerator):
    """Generator for circular HSS sections."""
    
    def validate_properties(self, properties: Dict) -> bool:
        """Validate required properties."""
        required = ["Diameter", "WallThickness"]
        return all(prop in properties for prop in required)
    
    def generate(self, section_properties: Dict):
        """Generate circular HSS geometry."""
        if not FREECAD_AVAILABLE:
            return None
        
        try:
            if not self.validate_properties(section_properties):
                raise ValueError("Missing required properties for circular HSS")
            
            d = float(section_properties["Diameter"])
            t = float(section_properties["WallThickness"])
            
            # Validation
            if d <= 0 or t <= 0:
                raise ValueError("Diameter and wall thickness must be positive")
            if t >= d/2:
                raise ValueError(f"Wall thickness ({t}) cannot exceed radius ({d/2})")
            if d/t > 200:
                raise ValueError(f"Excessive slenderness: D/t = {d/t:.1f}")
            
            # Create circular HSS
            outer_circle = Part.makeCircle(d/2, FreeCAD.Vector(0, 0, 0))
            inner_circle = Part.makeCircle(d/2-t, FreeCAD.Vector(0, 0, 0))
            
            outer_face = Part.Face(outer_circle)
            inner_face = Part.Face(inner_circle)
            
            return outer_face.cut(inner_face)
            
        except Exception as e:
            raise RuntimeError(f"Error generating circular HSS: {str(e)}")

class AngleGenerator(SectionGeometryGenerator):
    """Generator for angle sections (L-shapes)."""
    
    def validate_properties(self, properties: Dict) -> bool:
        """Validate required properties."""
        # Can have either equal or unequal legs
        has_equal_legs = "LegWidth" in properties and "Thickness" in properties
        has_unequal_legs = all(prop in properties for prop in ["LegWidth", "LegHeight", "Thickness"])
        
        return has_equal_legs or has_unequal_legs
    
    def generate(self, section_properties: Dict):
        """Generate angle section geometry."""
        if not FREECAD_AVAILABLE:
            return None
        
        try:
            if not self.validate_properties(section_properties):
                raise ValueError("Missing required properties for angle section")
            
            # Handle both equal and unequal angles
            leg_width = float(section_properties.get("LegWidth", 0))
            leg_height = float(section_properties.get("LegHeight", leg_width))  # Default to equal
            thickness = float(section_properties["Thickness"])
            
            # Validation
            if leg_width <= 0 or leg_height <= 0 or thickness <= 0:
                raise ValueError("All angle dimensions must be positive")
            if thickness >= min(leg_width, leg_height):
                raise ValueError("Thickness too large for leg dimensions")
            
            return self._create_angle_profile(leg_width, leg_height, thickness)
            
        except Exception as e:
            raise RuntimeError(f"Error generating angle geometry: {str(e)}")
    
    def _create_angle_profile(self, leg_width: float, leg_height: float, thickness: float):
        """Create L-shaped angle profile."""
        points = [
            FreeCAD.Vector(0, 0, 0),                    # 1. Origin
            FreeCAD.Vector(leg_width, 0, 0),            # 2. End of horizontal leg
            FreeCAD.Vector(leg_width, thickness, 0),     # 3. Inner corner horizontal
            FreeCAD.Vector(thickness, thickness, 0),     # 4. Inner corner
            FreeCAD.Vector(thickness, leg_height, 0),    # 5. Inner corner vertical
            FreeCAD.Vector(0, leg_height, 0),           # 6. End of vertical leg
            FreeCAD.Vector(0, 0, 0)                     # 7. Close polygon
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)

class ChannelGenerator(SectionGeometryGenerator):
    """Generator for channel sections (C-shapes)."""
    
    def validate_properties(self, properties: Dict) -> bool:
        """Validate required properties."""
        required = ["Depth", "FlangeWidth", "WebThickness", "FlangeThickness"]
        return all(prop in properties for prop in required)
    
    def generate(self, section_properties: Dict):
        """Generate channel section geometry."""
        if not FREECAD_AVAILABLE:
            return None
        
        try:
            if not self.validate_properties(section_properties):
                raise ValueError("Missing required properties for channel section")
            
            depth = float(section_properties["Depth"])
            flange_width = float(section_properties["FlangeWidth"])
            web_thickness = float(section_properties["WebThickness"])
            flange_thickness = float(section_properties["FlangeThickness"])
            
            # Validation
            if any(dim <= 0 for dim in [depth, flange_width, web_thickness, flange_thickness]):
                raise ValueError("All channel dimensions must be positive")
            
            if 2*flange_thickness >= depth:
                raise ValueError("Total flange thickness exceeds depth")
            
            if web_thickness >= flange_width:
                raise ValueError("Web thickness exceeds flange width")
            
            return self._create_channel_profile(depth, flange_width, web_thickness, flange_thickness)
            
        except Exception as e:
            raise RuntimeError(f"Error generating channel geometry: {str(e)}")
    
    def _create_channel_profile(self, depth: float, flange_width: float, web_thickness: float, flange_thickness: float):
        """Create C-shaped channel profile."""
        points = [
            FreeCAD.Vector(0, -depth/2, 0),                                    # 1. Bottom left of web
            FreeCAD.Vector(flange_width, -depth/2, 0),                         # 2. Bottom right of bottom flange
            FreeCAD.Vector(flange_width, -depth/2 + flange_thickness, 0),       # 3. Inner corner of bottom flange
            FreeCAD.Vector(web_thickness, -depth/2 + flange_thickness, 0),      # 4. Bottom of web inner face
            FreeCAD.Vector(web_thickness, depth/2 - flange_thickness, 0),       # 5. Top of web inner face
            FreeCAD.Vector(flange_width, depth/2 - flange_thickness, 0),        # 6. Inner corner of top flange
            FreeCAD.Vector(flange_width, depth/2, 0),                          # 7. Top right of top flange
            FreeCAD.Vector(0, depth/2, 0),                                     # 8. Top left of web
            FreeCAD.Vector(0, -depth/2, 0)                                     # 9. Close polygon
        ]
        
        wire = Part.makePolygon(points)
        return Part.Face(wire)

# Factory function for easy access
def create_geometry_generator(section_type: str) -> Optional[SectionGeometryGenerator]:
    """
    Create appropriate geometry generator for section type.
    
    Args:
        section_type: Section type string
        
    Returns:
        Geometry generator instance or None
    """
    generators = {
        "Wide Flange": IBeamGenerator,
        "I-Beam": IBeamGenerator,
        "H-Beam": IBeamGenerator,
        "Rectangular HSS": RectangularHSSGenerator,
        "Circular HSS": CircularHSSGenerator,
        "Equal Angle": AngleGenerator,
        "Unequal Angle": AngleGenerator,
        "Channel": ChannelGenerator
    }
    
    generator_class = generators.get(section_type)
    if generator_class:
        return generator_class()
    else:
        return None