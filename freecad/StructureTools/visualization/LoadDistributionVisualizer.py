# -*- coding: utf-8 -*-
"""
LoadDistributionVisualizer.py - Visualize load transfer patterns for slabs

Creates 3D visualization of:
- Two-Way slab yield line patterns (star pattern / triangular areas)
- One-Way slab strip patterns (parallel strips)
- Distributed loads on supporting beams (triangular/trapezoidal/uniform)
"""

import FreeCAD as App
import Part
import math
from typing import List, Tuple, Optional, Dict


class LoadDistributionVisualizer:
    """
    Creates visual representations of load distribution patterns.
    
    Supports:
    - Two-Way (Yield Line): Star pattern with 45° yield lines from corners
    - One-Way: Parallel strips perpendicular to short span
    - Distributed loads on beams: Triangular, trapezoidal, or uniform
    """
    
    def __init__(self, doc=None):
        """Initialize visualizer with optional document."""
        self.doc = doc or App.ActiveDocument
        self.visualization_objects = []
        self.line_width = 2.0
        self.arrow_scale = 50.0  # mm per kN/m
        
        # Colors
        self.yield_line_color = (1.0, 0.5, 0.0)  # Orange for yield lines
        self.one_way_color = (0.0, 0.5, 1.0)     # Blue for one-way strips
        self.load_arrow_color = (1.0, 0.0, 0.5)  # Magenta for load arrows
        self.tributary_color = (1.0, 0.8, 0.6)   # Light orange for tributary areas
    
    def clear_visualization(self):
        """Remove all visualization objects."""
        for obj in self.visualization_objects:
            try:
                if self.doc.getObject(obj.Name):
                    self.doc.removeObject(obj.Name)
            except Exception:
                pass
        self.visualization_objects = []
    
    def visualize_two_way_yield_line(self, corners: List[App.Vector], 
                                      load_intensity: float = 10.0,
                                      name_prefix: str = "TwoWay") -> List:
        """
        Create yield line pattern for two-way slab.
        
        Args:
            corners: List of 4 corner points [A, B, C, D] counterclockwise
            load_intensity: Load in kN/m²
            name_prefix: Prefix for object names
            
        Returns:
            List of created visualization objects
        """
        if len(corners) < 4:
            App.Console.PrintWarning("Need 4 corners for two-way visualization\n")
            return []
        
        A, B, C, D = corners[:4]
        
        # Calculate spans
        span_AB = (B - A).Length  # mm
        span_BC = (C - B).Length  # mm
        
        # Determine short and long spans
        if span_AB <= span_BC:
            short_span = span_AB
            long_span = span_BC
        else:
            short_span = span_BC
            long_span = span_AB
        
        # Calculate center point (intersection of yield lines)
        center = (A + B + C + D) * 0.25
        
        # For rectangular slab, yield lines go at 45° from corners
        # but only extend to the centerline of the short span
        half_short = short_span / 2
        
        created_objects = []
        
        # Create yield line edges from each corner toward center
        # Triangular areas for short edges, trapezoidal for long edges
        
        # Create the star pattern lines
        yield_lines = []
        
        # Calculate yield line intersection points
        # For a 4-edge supported slab, lines from corners meet along centerline
        if span_AB <= span_BC:
            # AB and CD are short spans (triangular loads)
            # BC and DA are long spans (trapezoidal loads)
            # Yield lines from A and B meet at center of AB edge region
            mid_AB_left = A + (D - A).normalize() * half_short
            mid_AB_right = B + (C - B).normalize() * half_short
            mid_CD_left = D + (A - D).normalize() * half_short
            mid_CD_right = C + (B - C).normalize() * half_short
            
            yield_lines = [
                (A, mid_AB_left), (A, mid_AB_right - (mid_AB_right - mid_AB_left)),
                (B, mid_AB_right), 
                (C, mid_CD_right),
                (D, mid_CD_left),
            ]
            
            # Simplified: draw diagonal lines from corners to center region
            yield_lines = [
                (A, center), (B, center), (C, center), (D, center)
            ]
        else:
            yield_lines = [
                (A, center), (B, center), (C, center), (D, center)
            ]
        
        # Create yield line geometry
        for i, (start, end) in enumerate(yield_lines):
            line = Part.makeLine(start, end)
            line_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_YieldLine_{i}")
            line_obj.Shape = line
            
            if hasattr(line_obj, 'ViewObject'):
                line_obj.ViewObject.LineColor = self.yield_line_color
                line_obj.ViewObject.LineWidth = self.line_width * 2
                line_obj.ViewObject.DrawStyle = "Dashed"
            
            created_objects.append(line_obj)
            self.visualization_objects.append(line_obj)
        
        # Create slab boundary
        boundary = Part.makePolygon([A, B, C, D, A])
        boundary_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Boundary")
        boundary_obj.Shape = boundary
        
        if hasattr(boundary_obj, 'ViewObject'):
            boundary_obj.ViewObject.LineColor = (0.0, 0.0, 0.0)
            boundary_obj.ViewObject.LineWidth = self.line_width
        
        created_objects.append(boundary_obj)
        self.visualization_objects.append(boundary_obj)
        
        # Create tributary area shading
        self._create_tributary_areas_two_way(corners, center, name_prefix, created_objects)
        
        # Create load magnitude label
        label_pos = center + App.Vector(0, 0, 100)
        self._create_load_label(label_pos, load_intensity, name_prefix, created_objects)
        
        return created_objects
    
    def _create_load_label(self, position: App.Vector, 
                            load_intensity: float,
                            name_prefix: str,
                            created_objects: List):
        """Create text label showing load intensity."""
        try:
            # Create text object for load label
            text_obj = self.doc.addObject("App::Annotation", f"{name_prefix}_LoadLabel")
            text_obj.LabelText = [f"{load_intensity:.1f} kN/m²"]
            text_obj.Position = position
            
            created_objects.append(text_obj)
            self.visualization_objects.append(text_obj)
        except Exception as e:
            App.Console.PrintWarning(f"Could not create load label: {e}\n")
    
    def _create_tributary_areas_two_way(self, corners: List[App.Vector], 
                                         center: App.Vector,
                                         name_prefix: str,
                                         created_objects: List):
        """Create semi-transparent tributary area faces for two-way slab."""
        A, B, C, D = corners[:4]
        
        try:
            # Create triangular/trapezoidal faces
            triangles = [
                [A, B, center],  # Triangle to edge AB
                [B, C, center],  # Triangle to edge BC
                [C, D, center],  # Triangle to edge CD
                [D, A, center],  # Triangle to edge DA
            ]
            
            for i, pts in enumerate(triangles):
                wire = Part.makePolygon(pts + [pts[0]])
                face = Part.Face(wire)
                face_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Area_{i}")
                face_obj.Shape = face
                
                if hasattr(face_obj, 'ViewObject'):
                    # Alternate colors
                    if i % 2 == 0:
                        face_obj.ViewObject.ShapeColor = (1.0, 0.9, 0.7)
                    else:
                        face_obj.ViewObject.ShapeColor = (0.7, 0.9, 1.0)
                    face_obj.ViewObject.Transparency = 50
                
                created_objects.append(face_obj)
                self.visualization_objects.append(face_obj)
                
        except Exception as e:
            App.Console.PrintWarning(f"Error creating tributary areas: {e}\n")
    
    def visualize_one_way_distribution(self, corners: List[App.Vector],
                                        span_direction: str = "short",
                                        load_intensity: float = 10.0,
                                        name_prefix: str = "OneWay") -> List:
        """
        Create one-way slab load distribution visualization.
        
        Args:
            corners: List of 4 corner points [A, B, C, D]
            span_direction: "short" (perpendicular to short span) or "long"
            load_intensity: Load in kN/m²
            name_prefix: Prefix for object names
            
        Returns:
            List of created visualization objects
        """
        if len(corners) < 4:
            return []
        
        A, B, C, D = corners[:4]
        
        # Determine spans
        span_AB = (B - A).Length
        span_BC = (C - B).Length
        
        created_objects = []
        
        # Create boundary
        boundary = Part.makePolygon([A, B, C, D, A])
        boundary_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Boundary")
        boundary_obj.Shape = boundary
        
        if hasattr(boundary_obj, 'ViewObject'):
            boundary_obj.ViewObject.LineColor = (0.0, 0.0, 0.0)
            boundary_obj.ViewObject.LineWidth = self.line_width
        
        created_objects.append(boundary_obj)
        self.visualization_objects.append(boundary_obj)
        
        # Create parallel strip lines
        num_strips = 5
        
        if (span_direction == "short" and span_AB <= span_BC) or \
           (span_direction == "long" and span_AB > span_BC):
            # Strips parallel to AB (perpendicular to BC)
            for i in range(1, num_strips):
                t = i / num_strips
                start = A + (D - A) * t
                end = B + (C - B) * t
                line = Part.makeLine(start, end)
                line_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Strip_{i}")
                line_obj.Shape = line
                
                if hasattr(line_obj, 'ViewObject'):
                    line_obj.ViewObject.LineColor = self.one_way_color
                    line_obj.ViewObject.LineWidth = 1.0
                    line_obj.ViewObject.DrawStyle = "Dashed"
                
                created_objects.append(line_obj)
                self.visualization_objects.append(line_obj)
        else:
            # Strips parallel to AD (perpendicular to AB)
            for i in range(1, num_strips):
                t = i / num_strips
                start = A + (B - A) * t
                end = D + (C - D) * t
                line = Part.makeLine(start, end)
                line_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Strip_{i}")
                line_obj.Shape = line
                
                if hasattr(line_obj, 'ViewObject'):
                    line_obj.ViewObject.LineColor = self.one_way_color
                    line_obj.ViewObject.LineWidth = 1.0
                    line_obj.ViewObject.DrawStyle = "Dashed"
                
                created_objects.append(line_obj)
                self.visualization_objects.append(line_obj)
        
        # Create slab face with shading
        try:
            wire = Part.makePolygon([A, B, C, D, A])
            face = Part.Face(wire)
            face_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Face")
            face_obj.Shape = face
            
            if hasattr(face_obj, 'ViewObject'):
                face_obj.ViewObject.ShapeColor = (0.8, 0.9, 1.0)
                face_obj.ViewObject.Transparency = 50
            
            created_objects.append(face_obj)
            self.visualization_objects.append(face_obj)
        except Exception:
            pass
        
        # Add load label
        center = (A + B + C + D) * 0.25
        label_pos = center + App.Vector(0, 0, 100)
        self._create_load_label(label_pos, load_intensity, name_prefix, created_objects)
        
        return created_objects
    
    def visualize_beam_distributed_load(self, start: App.Vector, 
                                         end: App.Vector,
                                         load_type: str = "uniform",
                                         w1: float = 10.0,
                                         w2: float = 10.0,
                                         name_prefix: str = "BeamLoad") -> List:
        """
        Visualize distributed load on a beam.
        
        Args:
            start: Start point of beam
            end: End point of beam
            load_type: "uniform", "triangular", or "trapezoidal"
            w1: Load at start (kN/m)
            w2: Load at end (kN/m)
            name_prefix: Prefix for object names
            
        Returns:
            List of created visualization objects
        """
        created_objects = []
        
        beam_vec = end - start
        beam_length = beam_vec.Length
        beam_dir = beam_vec.normalize()
        
        # Perpendicular direction (typically up for floor beams)
        up_dir = App.Vector(0, 0, 1)
        if abs(beam_dir.dot(up_dir)) > 0.9:
            up_dir = App.Vector(1, 0, 0)
        
        # Number of arrows
        num_arrows = max(5, int(beam_length / 200))
        
        for i in range(num_arrows + 1):
            t = i / num_arrows
            pos = start + beam_dir * (beam_length * t)
            
            # Calculate load magnitude at this point
            if load_type == "uniform":
                w = w1
            elif load_type == "triangular":
                w = w1 * (1 - t)  # Decreasing from start
            else:  # trapezoidal
                w = w1 + (w2 - w1) * t
            
            # Arrow length proportional to load
            arrow_length = w * self.arrow_scale / 10
            
            if arrow_length > 1:
                # Create arrow
                arrow_end = pos - up_dir * arrow_length
                
                # Arrow shaft
                shaft = Part.makeLine(pos, arrow_end)
                shaft_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Arrow_{i}")
                shaft_obj.Shape = shaft
                
                if hasattr(shaft_obj, 'ViewObject'):
                    shaft_obj.ViewObject.LineColor = self.load_arrow_color
                    shaft_obj.ViewObject.LineWidth = 1.5
                
                created_objects.append(shaft_obj)
                self.visualization_objects.append(shaft_obj)
        
        # Create load envelope line
        envelope_pts = []
        for i in range(num_arrows + 1):
            t = i / num_arrows
            pos = start + beam_dir * (beam_length * t)
            
            if load_type == "uniform":
                w = w1
            elif load_type == "triangular":
                w = w1 * (1 - t)
            else:
                w = w1 + (w2 - w1) * t
            
            arrow_length = w * self.arrow_scale / 10
            envelope_pts.append(pos - up_dir * arrow_length)
        
        if len(envelope_pts) > 1:
            envelope = Part.makePolygon(envelope_pts)
            envelope_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Envelope")
            envelope_obj.Shape = envelope
            
            if hasattr(envelope_obj, 'ViewObject'):
                envelope_obj.ViewObject.LineColor = self.load_arrow_color
                envelope_obj.ViewObject.LineWidth = 2.0
            
            created_objects.append(envelope_obj)
            self.visualization_objects.append(envelope_obj)
        
        # Create beam line
        beam_line = Part.makeLine(start, end)
        beam_obj = self.doc.addObject("Part::Feature", f"{name_prefix}_Beam")
        beam_obj.Shape = beam_line
        
        if hasattr(beam_obj, 'ViewObject'):
            beam_obj.ViewObject.LineColor = (0.3, 0.3, 0.3)
            beam_obj.ViewObject.LineWidth = 3.0
        
        created_objects.append(beam_obj)
        self.visualization_objects.append(beam_obj)
        
        return created_objects


class SlabLoadCalculator:
    """
    Calculate distributed loads on beams from slab area loads.
    
    Supports:
    - Two-Way (Yield Line): Triangular for short edges, trapezoidal for long edges
    - One-Way: Uniform load to supporting beams
    """
    
    def __init__(self):
        pass
    
    def calculate_two_way_beam_loads(self, 
                                      slab_corners: List[App.Vector],
                                      load_intensity: float,
                                      edge_beams: Dict[str, Tuple[App.Vector, App.Vector]] = None) -> Dict:
        """
        Calculate distributed loads on beams for two-way slab (yield line method).
        
        Args:
            slab_corners: [A, B, C, D] counterclockwise
            load_intensity: Load in kN/m²
            edge_beams: Optional dict {"AB": (start, end), "BC": ...}
            
        Returns:
            Dict with load data for each edge beam:
            {
                "AB": {"load_type": "triangular", "w_max": value, "length": value},
                "BC": {"load_type": "trapezoidal", "w1": value, "w2": value, "length": value},
                ...
            }
        """
        if len(slab_corners) < 4:
            return {}
        
        A, B, C, D = slab_corners[:4]
        
        # Calculate spans (in mm)
        Lx = (B - A).Length / 1000  # m
        Ly = (C - B).Length / 1000  # m
        
        # Determine short and long spans
        short_span = min(Lx, Ly)
        long_span = max(Lx, Ly)
        
        # Yield line coefficient (for 4-edge supported slab)
        # Load distribution based on 45° yield lines from corners
        
        results = {}
        
        if Lx <= Ly:
            # X direction is short span: AB and CD get triangular loads
            # Y direction is long span: BC and DA get trapezoidal loads
            
            # Triangular load on short span beams
            w_max_short = load_intensity * short_span / 2  # kN/m at peak
            
            # Trapezoidal load on long span beams
            # Width at ends = short_span / 2, uniform in middle
            trap_end_width = short_span / 2
            if long_span > short_span:
                trap_uniform_length = long_span - short_span
            else:
                trap_uniform_length = 0
            
            w_trap = load_intensity * trap_end_width  # kN/m
            
            results["AB"] = {
                "load_type": "triangular",
                "w_max": w_max_short,
                "w1": 0, "w2": w_max_short,  # Peak at center
                "length": Lx,
                "total_force": load_intensity * Lx * short_span / 4  # kN
            }
            results["CD"] = {
                "load_type": "triangular",
                "w_max": w_max_short,
                "w1": 0, "w2": w_max_short,
                "length": Lx,
                "total_force": load_intensity * Lx * short_span / 4
            }
            results["BC"] = {
                "load_type": "trapezoidal",
                "w1": 0, 
                "w2": w_trap,  # At quarter point
                "w_uniform": w_trap,
                "uniform_length": trap_uniform_length,
                "length": Ly,
                "total_force": load_intensity * Ly * short_span / 4 + load_intensity * trap_uniform_length * trap_end_width
            }
            results["DA"] = {
                "load_type": "trapezoidal",
                "w1": 0,
                "w2": w_trap,
                "w_uniform": w_trap,
                "uniform_length": trap_uniform_length,
                "length": Ly,
                "total_force": load_intensity * Ly * short_span / 4 + load_intensity * trap_uniform_length * trap_end_width
            }
        else:
            # Y direction is short span: BC and DA get triangular loads
            # X direction is long span: AB and CD get trapezoidal loads
            w_max_short = load_intensity * short_span / 2
            trap_end_width = short_span / 2
            trap_uniform_length = long_span - short_span if long_span > short_span else 0
            w_trap = load_intensity * trap_end_width
            
            results["BC"] = {
                "load_type": "triangular",
                "w_max": w_max_short,
                "w1": 0, "w2": w_max_short,
                "length": Ly,
                "total_force": load_intensity * Ly * short_span / 4
            }
            results["DA"] = {
                "load_type": "triangular",
                "w_max": w_max_short,
                "w1": 0, "w2": w_max_short,
                "length": Ly,
                "total_force": load_intensity * Ly * short_span / 4
            }
            results["AB"] = {
                "load_type": "trapezoidal",
                "w1": 0,
                "w2": w_trap,
                "w_uniform": w_trap,
                "uniform_length": trap_uniform_length,
                "length": Lx,
                "total_force": load_intensity * Lx * short_span / 4 + load_intensity * trap_uniform_length * trap_end_width
            }
            results["CD"] = {
                "load_type": "trapezoidal",
                "w1": 0,
                "w2": w_trap,
                "w_uniform": trap_uniform_length,
                "length": Lx,
                "total_force": load_intensity * Lx * short_span / 4 + load_intensity * trap_uniform_length * trap_end_width
            }
        
        return results
    
    def calculate_one_way_beam_loads(self,
                                      slab_corners: List[App.Vector],
                                      load_intensity: float,
                                      span_direction: str = "short") -> Dict:
        """
        Calculate distributed loads on beams for one-way slab.
        
        Args:
            slab_corners: [A, B, C, D] counterclockwise
            load_intensity: Load in kN/m²
            span_direction: "short" or "long" - direction load spans
            
        Returns:
            Dict with load data for supporting beams (uniform load)
        """
        if len(slab_corners) < 4:
            return {}
        
        A, B, C, D = slab_corners[:4]
        
        Lx = (B - A).Length / 1000  # m
        Ly = (C - B).Length / 1000  # m
        
        results = {}
        
        if (span_direction == "short" and Lx <= Ly) or \
           (span_direction == "long" and Lx > Ly):
            # Load spans along X (AB), supports on BC and DA
            w_uniform = load_intensity * Lx / 2  # kN/m
            
            results["BC"] = {
                "load_type": "uniform",
                "w": w_uniform,
                "length": Ly,
                "total_force": w_uniform * Ly
            }
            results["DA"] = {
                "load_type": "uniform",
                "w": w_uniform,
                "length": Ly,
                "total_force": w_uniform * Ly
            }
        else:
            # Load spans along Y (BC), supports on AB and CD
            w_uniform = load_intensity * Ly / 2  # kN/m
            
            results["AB"] = {
                "load_type": "uniform",
                "w": w_uniform,
                "length": Lx,
                "total_force": w_uniform * Lx
            }
            results["CD"] = {
                "load_type": "uniform",
                "w": w_uniform,
                "length": Lx,
                "total_force": w_uniform * Lx
            }
        
        return results
    
    def print_beam_loads(self, results: Dict):
        """Print beam load summary to console."""
        App.Console.PrintMessage("\n=== Beam Load Distribution ===\n")
        for edge, data in results.items():
            load_type = data.get("load_type", "unknown")
            length = data.get("length", 0)
            
            if load_type == "uniform":
                w = data.get("w", 0)
                App.Console.PrintMessage(f"Edge {edge}: Uniform w = {w:.2f} kN/m, L = {length:.2f} m\n")
            elif load_type == "triangular":
                w_max = data.get("w_max", 0)
                App.Console.PrintMessage(f"Edge {edge}: Triangular w_max = {w_max:.2f} kN/m, L = {length:.2f} m\n")
            elif load_type == "trapezoidal":
                w_uniform = data.get("w_uniform", 0)
                App.Console.PrintMessage(f"Edge {edge}: Trapezoidal w = {w_uniform:.2f} kN/m, L = {length:.2f} m\n")
            
            total = data.get("total_force", 0)
            App.Console.PrintMessage(f"         Total Force: {total:.2f} kN\n")
        App.Console.PrintMessage("==============================\n")


# Add method to LoadDistributionVisualizer
def visualize_slab_with_beam_loads(self, corners: List[App.Vector], 
                                    load_intensity: float = 10.0,
                                    distribution_type: str = "two_way",
                                    name_prefix: str = "SlabLoad") -> List:
    """
    Visualize slab with load distribution and beam loads.
    
    Args:
        corners: [A, B, C, D] counterclockwise
        load_intensity: Load in kN/m²
        distribution_type: "two_way" or "one_way"
        name_prefix: Prefix for object names
    """
    created_objects = []
    calc = SlabLoadCalculator()
    
    if len(corners) < 4:
        return []
    
    A, B, C, D = corners[:4]
    
    if distribution_type == "two_way":
        # Visualize slab
        self.visualize_two_way_yield_line(corners, load_intensity, name_prefix)
        
        # Calculate beam loads
        beam_loads = calc.calculate_two_way_beam_loads(corners, load_intensity)
    else:
        self.visualize_one_way_distribution(corners, "short", load_intensity, name_prefix)
        beam_loads = calc.calculate_one_way_beam_loads(corners, load_intensity, "short")
    
    # Print results
    calc.print_beam_loads(beam_loads)
    
    # Visualize beam loads
    edge_points = {
        "AB": (A, B),
        "BC": (B, C),
        "CD": (C, D),
        "DA": (D, A)
    }
    
    for edge, data in beam_loads.items():
        if edge in edge_points:
            start, end = edge_points[edge]
            # Offset beam slightly for visibility
            offset = App.Vector(0, 0, -500)
            
            load_type = data.get("load_type", "uniform")
            if load_type == "triangular":
                self.visualize_beam_distributed_load(
                    start + offset, end + offset,
                    load_type="triangular",
                    w1=data.get("w_max", 10), w2=0,
                    name_prefix=f"{name_prefix}_{edge}"
                )
            elif load_type == "trapezoidal":
                self.visualize_beam_distributed_load(
                    start + offset, end + offset,
                    load_type="trapezoidal",
                    w1=0, w2=data.get("w_uniform", 10),
                    name_prefix=f"{name_prefix}_{edge}"
                )
            else:  # uniform
                self.visualize_beam_distributed_load(
                    start + offset, end + offset,
                    load_type="uniform",
                    w1=data.get("w", 10), w2=data.get("w", 10),
                    name_prefix=f"{name_prefix}_{edge}"
                )
    
    return created_objects


# Monkey-patch the method
LoadDistributionVisualizer.visualize_slab_with_beam_loads = visualize_slab_with_beam_loads


def create_example_visualization():
    """Create example visualization for testing."""
    doc = App.ActiveDocument
    if not doc:
        doc = App.newDocument("LoadVisualization")
    
    viz = LoadDistributionVisualizer(doc)
    
    # Example 1: Two-Way slab 6m x 5m with beam loads
    App.Console.PrintMessage("\n=== Two-Way Slab (6m x 5m, 10 kN/m²) ===\n")
    corners_two_way = [
        App.Vector(0, 0, 0),
        App.Vector(6000, 0, 0),
        App.Vector(6000, 5000, 0),
        App.Vector(0, 5000, 0)
    ]
    viz.visualize_slab_with_beam_loads(corners_two_way, load_intensity=10.0, 
                                        distribution_type="two_way", 
                                        name_prefix="TwoWaySlab")
    
    # Example 2: One-Way slab 7m x 2.5m (high aspect ratio)
    App.Console.PrintMessage("\n=== One-Way Slab (7m x 2.5m, 10 kN/m²) ===\n")
    corners_one_way = [
        App.Vector(10000, 0, 0),
        App.Vector(17000, 0, 0),
        App.Vector(17000, 2500, 0),
        App.Vector(10000, 2500, 0)
    ]
    viz.visualize_slab_with_beam_loads(corners_one_way, load_intensity=10.0,
                                        distribution_type="one_way",
                                        name_prefix="OneWaySlab")
    
    doc.recompute()
    App.Console.PrintMessage("\n=== Visualization Complete ===\n")
    return viz


def calculate_and_print_example():
    """Calculate beam loads without visualization (for console use)."""
    calc = SlabLoadCalculator()
    
    # Example from structville: 6m x 5m slab, 10 kN/m²
    corners = [
        App.Vector(0, 0, 0),
        App.Vector(6000, 0, 0),
        App.Vector(6000, 5000, 0),
        App.Vector(0, 5000, 0)
    ]
    
    App.Console.PrintMessage("\n*** Two-Way Slab Load Distribution ***\n")
    App.Console.PrintMessage("Slab: 6.0m x 5.0m, Load: 10 kN/m²\n")
    App.Console.PrintMessage("Short span (Lx) = 5.0m, Long span (Ly) = 6.0m\n")
    App.Console.PrintMessage("Aspect ratio k = 6.0/5.0 = 1.2\n")
    
    results = calc.calculate_two_way_beam_loads(corners, load_intensity=10.0)
    calc.print_beam_loads(results)
    
    # Verify: Total load = 10 * 6 * 5 = 300 kN
    total = sum(d.get("total_force", 0) for d in results.values())
    App.Console.PrintMessage(f"\nTotal slab load: 10 × 6 × 5 = 300 kN\n")
    App.Console.PrintMessage(f"Sum of beam reactions: {total:.2f} kN\n")
    
    return results


# Register as a FreeCAD module
if App.GuiUp:
    App.Console.PrintMessage("LoadDistributionVisualizer loaded\n")
