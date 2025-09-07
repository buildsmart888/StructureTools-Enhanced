# -*- coding: utf-8 -*-
"""
Section Drawing System
ระบบวาดหน้าตัดเหล็กจากข้อมูล geometry
"""

import FreeCAD as App
import Part
try:
    import Draft
    DRAFT_AVAILABLE = True
except Exception:
    DRAFT_AVAILABLE = False
    print('[WARNING] Draft module not available; dimension helpers will be limited')
import math
# Optional Arch (BIM) integration for ArchProfile mapping
try:
    import Arch
    ARCH_AVAILABLE = True
except Exception:
    ARCH_AVAILABLE = False

class SectionDrawer:
    """Class for drawing steel sections from geometry data"""
    
    def __init__(self):
        self.scale = 1.0
        self.line_width = 2.0
        self.fill_color = (0.8, 0.8, 0.9)  # Light blue
        self.line_color = (0.2, 0.2, 0.6)  # Dark blue
    
    def draw_section(self, geometry_data, section_name="Section"):
        """Draw section from geometry data"""
        if not geometry_data:
            print("[ERROR] No geometry data provided")
            return None
        
        geometry_type = geometry_data.get('type', geometry_data.get('beam_type', 'UNKNOWN'))
        
        if geometry_type == 'I_BEAM':
            return self.draw_i_beam(geometry_data, section_name)
        elif geometry_type == 'TEE':
            return self.draw_tee_section(geometry_data, section_name)
        elif geometry_type == 'ANGLE':
            return self.draw_angle_section(geometry_data, section_name)
        elif geometry_type == 'CIRCULAR':
            return self.draw_circular_section(geometry_data, section_name)
        elif geometry_type == 'RECTANGULAR':
            return self.draw_rectangular_section(geometry_data, section_name)
        else:
            print(f"[WARNING] Unknown geometry type: {geometry_type}")
            return self.draw_generic_section(geometry_data, section_name)
    
    def draw_i_beam(self, geometry_data, section_name):
        """Draw I-beam section"""
        try:
            # Get dimensions
            height = geometry_data.get('height', 200)
            width = geometry_data.get('width', 100) 
            web_thickness = geometry_data.get('web_thickness', 8)
            flange_thickness = geometry_data.get('flange_thickness', 12)
            
            print(f"[INFO] Drawing I-beam: {section_name}")
            print(f"  H={height}mm, W={width}mm, tw={web_thickness}mm, tf={flange_thickness}mm")
            
            # Use drawing points if available
            if 'drawing_points' in geometry_data and geometry_data['drawing_points']:
                points = geometry_data['drawing_points']
                return self.create_section_from_points(points, section_name)
            
            # Generate I-beam outline points
            points = self.calculate_i_beam_outline(height, width, web_thickness, flange_thickness)
            
            # Create the section
            section_obj = self.create_section_from_points(points, section_name)
            
            # Add dimensions
            self.add_section_dimensions(section_obj, geometry_data)
            
            return section_obj
            
        except Exception as e:
            print(f"[ERROR] Failed to draw I-beam: {e}")
            return None
    
    def draw_tee_section(self, geometry_data, section_name):
        """Draw T-section"""
        try:
            height = geometry_data.get('height', 100)
            width = geometry_data.get('width', 100)
            web_thickness = geometry_data.get('web_thickness', 8)
            flange_thickness = geometry_data.get('flange_thickness', 12)
            
            print(f"[INFO] Drawing T-section: {section_name}")
            
            if 'drawing_points' in geometry_data and geometry_data['drawing_points']:
                points = geometry_data['drawing_points']
            else:
                points = self.calculate_tee_outline(height, width, web_thickness, flange_thickness)
            
            section_obj = self.create_section_from_points(points, section_name)
            self.add_section_dimensions(section_obj, geometry_data)
            
            return section_obj
            
        except Exception as e:
            print(f"[ERROR] Failed to draw T-section: {e}")
            return None
    
    def draw_angle_section(self, geometry_data, section_name):
        """Draw angle section"""
        try:
            leg1 = geometry_data.get('leg1', geometry_data.get('leg1_length', 75))
            leg2 = geometry_data.get('leg2', geometry_data.get('leg2_length', 75))
            thickness = geometry_data.get('thickness', 6)
            
            print(f"[INFO] Drawing Angle: {section_name}")
            print(f"  Leg1={leg1}mm, Leg2={leg2}mm, t={thickness}mm")
            
            if 'drawing_points' in geometry_data and geometry_data['drawing_points']:
                points = geometry_data['drawing_points']
            else:
                points = self.calculate_angle_outline(leg1, leg2, thickness)
            
            section_obj = self.create_section_from_points(points, section_name)
            self.add_section_dimensions(section_obj, geometry_data)
            
            return section_obj
            
        except Exception as e:
            print(f"[ERROR] Failed to draw angle: {e}")
            return None
    
    def draw_circular_section(self, geometry_data, section_name):
        """Draw circular section (pipe/HSS round)"""
        try:
            outer_diameter = geometry_data.get('outer_diameter', 100)
            inner_diameter = geometry_data.get('inner_diameter', 0)
            
            print(f"[INFO] Drawing Circular: {section_name}")
            print(f"  OD={outer_diameter}mm, ID={inner_diameter}mm")
            
            # Create outer circle
            outer_circle = Part.makeCircle(outer_diameter/2)
            outer_face = Part.Face(outer_circle)
            
            # Create inner circle if hollow
            if inner_diameter > 0:
                inner_circle = Part.makeCircle(inner_diameter/2)
                inner_face = Part.Face(inner_circle)
                section_shape = outer_face.cut(inner_face)
            else:
                section_shape = outer_face
            
            # Create FreeCAD object
            section_obj = App.ActiveDocument.addObject("Part::Feature", f"Section_{section_name}")
            section_obj.Shape = section_shape
            section_obj.Label = section_name
            
            # Set visual properties
            section_obj.ViewObject.ShapeColor = self.fill_color
            section_obj.ViewObject.LineColor = self.line_color
            section_obj.ViewObject.LineWidth = self.line_width
            
            App.ActiveDocument.recompute()
            
            return section_obj
            
        except Exception as e:
            print(f"[ERROR] Failed to draw circular section: {e}")
            return None
    
    def draw_rectangular_section(self, geometry_data, section_name):
        """Draw rectangular section (HSS rectangular)"""
        try:
            height = geometry_data.get('height', 100)
            width = geometry_data.get('width', 100)
            thickness = geometry_data.get('thickness', 6)
            
            print(f"[INFO] Drawing Rectangular HSS: {section_name}")
            print(f"  H={height}mm, W={width}mm, t={thickness}mm")
            
            # Create outer rectangle
            outer_points = [
                App.Vector(-width/2, -height/2, 0),
                App.Vector(width/2, -height/2, 0),
                App.Vector(width/2, height/2, 0),
                App.Vector(-width/2, height/2, 0),
                App.Vector(-width/2, -height/2, 0)
            ]
            
            outer_wire = Part.makePolygon(outer_points)
            outer_face = Part.Face(outer_wire)
            
            # Create inner rectangle if wall thickness allows
            inner_width = width - 2*thickness
            inner_height = height - 2*thickness
            
            if inner_width > 0 and inner_height > 0:
                inner_points = [
                    App.Vector(-inner_width/2, -inner_height/2, 0),
                    App.Vector(inner_width/2, -inner_height/2, 0),
                    App.Vector(inner_width/2, inner_height/2, 0),
                    App.Vector(-inner_width/2, inner_height/2, 0),
                    App.Vector(-inner_width/2, -inner_height/2, 0)
                ]
                
                inner_wire = Part.makePolygon(inner_points)
                inner_face = Part.Face(inner_wire)
                section_shape = outer_face.cut(inner_face)
            else:
                section_shape = outer_face
            
            # Create FreeCAD object
            section_obj = App.ActiveDocument.addObject("Part::Feature", f"Section_{section_name}")
            section_obj.Shape = section_shape
            section_obj.Label = section_name
            
            # Set visual properties
            section_obj.ViewObject.ShapeColor = self.fill_color
            section_obj.ViewObject.LineColor = self.line_color
            section_obj.ViewObject.LineWidth = self.line_width
            
            App.ActiveDocument.recompute()
            
            return section_obj
            
        except Exception as e:
            print(f"[ERROR] Failed to draw rectangular section: {e}")
            return None
    
    def create_section_from_points(self, points, section_name):
        """Create section object from outline points"""
        try:
            if not points:
                print("[ERROR] No points provided")
                return None
            
            # Convert points to FreeCAD vectors
            vectors = []
            for point in points:
                if isinstance(point, (list, tuple)) and len(point) >= 2:
                    vectors.append(App.Vector(point[0], point[1], 0))
            
            if len(vectors) < 3:
                print("[ERROR] Not enough points for section")
                return None
            
            # Ensure closed polygon
            if vectors[0] != vectors[-1]:
                vectors.append(vectors[0])
            
            # Create wire and face
            wire = Part.makePolygon(vectors)
            face = Part.Face(wire)

            # Create FreeCAD object (Part feature)
            section_obj = App.ActiveDocument.addObject("Part::Feature", f"Section_{section_name}")
            section_obj.Shape = face
            section_obj.Label = section_name
            
            # Set visual properties
            section_obj.ViewObject.ShapeColor = self.fill_color
            section_obj.ViewObject.LineColor = self.line_color
            section_obj.ViewObject.LineWidth = self.line_width
            
            App.ActiveDocument.recompute()
            
            # If Arch is available, attempt to create an ArchProfile from the face
            if ARCH_AVAILABLE:
                try:
                    # Arch.makeProfile accepts a shape or object and returns a Profile object
                    if hasattr(Arch, 'makeProfile'):
                        profile = Arch.makeProfile(section_obj)
                        # Label the profile clearly
                        try:
                            profile.Label = f"Profile_{section_name}"
                        except Exception:
                            pass
                        App.ActiveDocument.recompute()
                        return profile
                except Exception as e:
                    print(f"[WARNING] Arch profile creation failed: {e}")

            return section_obj
        except Exception as e:
            print(f"[ERROR] Failed to create section from points: {e}")
            return None

    def create_arch_profile_from_points(self, points, section_name):
        """Create an ArchProfile from outline points when Arch module is available.

        This creates a Draft wire if Draft is available (preferred), then calls
        Arch.makeProfile() to produce a Profile object. Falls back to creating a
        Part feature and then attempting Arch.makeProfile on it.
        """
        if not ARCH_AVAILABLE:
            print("[WARNING] Arch module not available; cannot create ArchProfile")
            return None

        try:
            # Convert to FreeCAD vectors
            vectors = []
            for point in points:
                if isinstance(point, (list, tuple)) and len(point) >= 2:
                    vectors.append(App.Vector(point[0], point[1], 0))

            if len(vectors) < 3:
                print("[ERROR] Not enough points to create ArchProfile")
                return None

            # Ensure closed polygon
            if vectors[0] != vectors[-1]:
                vectors.append(vectors[0])

            # Prefer Draft wire when available (cleaner profile input)
            if DRAFT_AVAILABLE:
                try:
                    import Draft
                    wire_obj = Draft.makeWire(vectors, closed=True)
                    App.ActiveDocument.recompute()
                    if hasattr(Arch, 'makeProfile'):
                        profile = Arch.makeProfile(wire_obj)
                        try:
                            profile.Label = f"Profile_{section_name}"
                        except Exception:
                            pass
                        App.ActiveDocument.recompute()
                        return profile
                except Exception as e:
                    print(f"[WARNING] Draft->Arch profile creation failed: {e}")

            # Fallback: create a Part face and then call Arch.makeProfile
            try:
                wire = Part.makePolygon(vectors)
                face = Part.Face(wire)
                section_obj = App.ActiveDocument.addObject("Part::Feature", f"Section_{section_name}")
                section_obj.Shape = face
                section_obj.Label = section_name
                App.ActiveDocument.recompute()

                if hasattr(Arch, 'makeProfile'):
                    profile = Arch.makeProfile(section_obj)
                    try:
                        profile.Label = f"Profile_{section_name}"
                    except Exception:
                        pass
                    App.ActiveDocument.recompute()
                    return profile
                return section_obj
            except Exception as e:
                print(f"[ERROR] Failed to create ArchProfile fallback: {e}")
                return None

        except Exception as e:
            print(f"[ERROR] Arch profile creation failed: {e}")
            return None
    
    def calculate_i_beam_outline(self, height, width, web_thickness, flange_thickness):
        """Calculate I-beam outline points"""
        h = height
        w = width
        tw = web_thickness
        tf = flange_thickness
        
        points = [
            # Top flange
            (-w/2, h/2), (w/2, h/2), (w/2, h/2-tf), (tw/2, h/2-tf),
            # Web to bottom
            (tw/2, -h/2+tf), (w/2, -h/2+tf),
            # Bottom flange
            (w/2, -h/2), (-w/2, -h/2), (-w/2, -h/2+tf), (-tw/2, -h/2+tf),
            # Web back to top
            (-tw/2, h/2-tf), (-w/2, h/2-tf), (-w/2, h/2)
        ]
        
        return points
    
    def calculate_tee_outline(self, height, width, web_thickness, flange_thickness):
        """Calculate T-section outline points"""
        h = height
        w = width
        tw = web_thickness
        tf = flange_thickness
        
        points = [
            # Top flange
            (-w/2, h/2), (w/2, h/2), (w/2, h/2-tf), (tw/2, h/2-tf),
            # Web down
            (tw/2, -h/2), (-tw/2, -h/2),
            # Web back up
            (-tw/2, h/2-tf), (-w/2, h/2-tf), (-w/2, h/2)
        ]
        
        return points
    
    def calculate_angle_outline(self, leg1, leg2, thickness):
        """Calculate angle section outline points"""
        points = [
            (0, 0), (leg2, 0), (leg2, thickness), (thickness, thickness), 
            (thickness, leg1), (0, leg1), (0, 0)
        ]
        
        return points
    
    def add_section_dimensions(self, section_obj, geometry_data):
        """Add dimension annotations to section"""
        try:
            # This would add dimension lines - simplified for now
            # Could be enhanced with Draft.makeDimension()
            
            # Add a simple text label with key dimensions
            if hasattr(section_obj, 'ViewObject'):
                # Get key dimension
                if 'height' in geometry_data and 'width' in geometry_data:
                    height = geometry_data['height']
                    width = geometry_data['width']
                    
                    # Add dimensions as object properties for reference
                    section_obj.addProperty("App::PropertyLength", "Height", "Dimensions", "Section height")
                    section_obj.addProperty("App::PropertyLength", "Width", "Dimensions", "Section width")
                    section_obj.Height = f"{height} mm"
                    section_obj.Width = f"{width} mm"
                    
                    if 'web_thickness' in geometry_data:
                        section_obj.addProperty("App::PropertyLength", "WebThickness", "Dimensions", "Web thickness")
                        section_obj.WebThickness = f"{geometry_data['web_thickness']} mm"
                    
                    if 'flange_thickness' in geometry_data:
                        section_obj.addProperty("App::PropertyLength", "FlangeThickness", "Dimensions", "Flange thickness")
                        section_obj.FlangeThickness = f"{geometry_data['flange_thickness']} mm"
        
        except Exception as e:
            print(f"[WARNING] Failed to add dimensions: {e}")
    
    def draw_generic_section(self, geometry_data, section_name):
        """Draw generic section as fallback"""
        try:
            # Create a simple rectangular placeholder
            width = geometry_data.get('width', 100)
            height = geometry_data.get('height', 200)
            
            points = [
                (-width/2, -height/2), (width/2, -height/2),
                (width/2, height/2), (-width/2, height/2),
                (-width/2, -height/2)
            ]
            
            return self.create_section_from_points(points, section_name)
            
        except Exception as e:
            print(f"[ERROR] Failed to draw generic section: {e}")
            return None

# Section integration with StructureTools
class EnhancedSection:
    """Enhanced section object with drawing capabilities"""
    
    def __init__(self, section_obj, geometry_data=None, properties_data=None):
        self.section_obj = section_obj
        self.geometry_data = geometry_data or {}
        self.properties_data = properties_data or {}
        self.drawer = SectionDrawer()
        self.drawn_section = None
    
    def draw_section_view(self):
        """Draw the section view"""
        if not self.geometry_data:
            print("[WARNING] No geometry data available for drawing")
            return None
        
        section_name = self.section_obj.Label if self.section_obj else "Unknown"
        self.drawn_section = self.drawer.draw_section(self.geometry_data, section_name)
        
        return self.drawn_section
    
    def get_calc_properties(self):
        """Get properties formatted for calc system"""
        if not self.properties_data:
            return {}
        
        # Extract key properties for structural analysis
        calc_props = {}
        
        # Area
        if 'area' in self.properties_data:
            calc_props['Area'] = self.properties_data['area']
        elif 'area' in self.properties_data and isinstance(self.properties_data['area'], dict):
            calc_props['Area'] = self.properties_data['area']['value']
        
        # Moments of inertia
        if 'moment_inertia_x' in self.properties_data:
            if isinstance(self.properties_data['moment_inertia_x'], dict):
                calc_props['Iy'] = self.properties_data['moment_inertia_x']['value']
            else:
                calc_props['Iy'] = self.properties_data['moment_inertia_x']
        elif 'ix' in self.properties_data:
            calc_props['Iy'] = self.properties_data['ix']
        
        if 'moment_inertia_y' in self.properties_data:
            if isinstance(self.properties_data['moment_inertia_y'], dict):
                calc_props['Iz'] = self.properties_data['moment_inertia_y']['value']
            else:
                calc_props['Iz'] = self.properties_data['moment_inertia_y']
        elif 'iy' in self.properties_data:
            calc_props['Iz'] = self.properties_data['iy']
        
        # Torsional constant
        if 'torsional_constant' in self.properties_data:
            if isinstance(self.properties_data['torsional_constant'], dict):
                calc_props['J'] = self.properties_data['torsional_constant']['value']
            else:
                calc_props['J'] = self.properties_data['torsional_constant']
        elif 'j' in self.properties_data:
            calc_props['J'] = self.properties_data['j']
        
        # Section moduli
        if 'section_modulus_x' in self.properties_data:
            if isinstance(self.properties_data['section_modulus_x'], dict):
                calc_props['Sy'] = self.properties_data['section_modulus_x']['value']
            else:
                calc_props['Sy'] = self.properties_data['section_modulus_x']
        elif 'sx' in self.properties_data:
            calc_props['Sy'] = self.properties_data['sx']
        
        if 'section_modulus_y' in self.properties_data:
            if isinstance(self.properties_data['section_modulus_y'], dict):
                calc_props['Sz'] = self.properties_data['section_modulus_y']['value']
            else:
                calc_props['Sz'] = self.properties_data['section_modulus_y']
        elif 'sy' in self.properties_data:
            calc_props['Sz'] = self.properties_data['sy']
        
        return calc_props
    
    def update_section_properties(self):
        """Update StructureTools section object with properties"""
        if not self.section_obj or not self.properties_data:
            return False
        
        try:
            calc_props = self.get_calc_properties()
            
            # Update section object properties
            for prop_name, value in calc_props.items():
                if hasattr(self.section_obj, prop_name):
                    setattr(self.section_obj, prop_name, value)
            
            # Set section name
            if 'name' in self.properties_data:
                self.section_obj.SectionName = self.properties_data['name']
            
            return True
            
        except Exception as e:
            print(f"[ERROR] Failed to update section properties: {e}")
            return False

# Convenience functions
def draw_section_from_data(geometry_data, section_name="Section"):
    """Draw section from geometry data"""
    drawer = SectionDrawer()
    return drawer.draw_section(geometry_data, section_name)

def create_enhanced_section(section_obj, geometry_data, properties_data):
    """Create enhanced section with drawing capabilities"""
    return EnhancedSection(section_obj, geometry_data, properties_data)

# Export main classes
__all__ = [
    'SectionDrawer',
    'EnhancedSection',
    'draw_section_from_data',
    'create_enhanced_section'
]