"""BIM Workbench Integration (concise, import-safe)

Provides a lightweight bridge to convert Profile objects into structural
members and to attach standardized/enhanced properties.
"""

from typing import List
import FreeCAD as App

try:
    import FreeCADGui as Gui
    FREECADGUI = True
except Exception:
    Gui = None
    FREECADGUI = False


def _console(msg: str):
    try:
        App.Console.PrintMessage(msg + "\n")
    except Exception:
        print(msg)


def _console_warn(msg: str):
    try:
        App.Console.PrintWarning(msg + "\n")
    except Exception:
        print("WARNING:", msg)


def _console_error(msg: str):
    try:
        App.Console.PrintError(msg + "\n")
    except Exception:
        print("ERROR:", msg)


class BIMStructuralIntegration:
    """Minimal, robust BIM -> Structural bridge."""

    def __init__(self):
        self.bim_to_structural = {}
        self.structural_to_bim = {}

    def import_from_bim(self, objects: List = None) -> List:
        if objects is None and FREECADGUI:
            try:
                objects = Gui.Selection.getSelection()
            except Exception:
                objects = []
        objects = objects or []
        if not objects:
            _console_warn("No objects selected to import")
            return []

        created = []
        for obj in objects:
            if self.is_profile_object(obj):
                s = self.create_structural_beam_from_profile(obj)
                if s:
                    created.append(s)
                    self.bim_to_structural[obj] = s
                    self.structural_to_bim[s] = obj
            elif self.is_bim_object(obj):
                s = self.create_structural_from_bim(obj)
                if s:
                    created.append(s)
                    self.bim_to_structural[obj] = s
                    self.structural_to_bim[s] = obj

        _console(f"Imported {len(created)} structural elements")
        try:
            App.ActiveDocument.recompute()
        except Exception:
            pass
        return created

    def is_profile_object(self, obj) -> bool:
        try:
            if hasattr(obj, 'StandardizedProperties') or hasattr(obj, 'EnhancedProperties'):
                return True
            lbl = getattr(obj, 'Label', '')
            return isinstance(lbl, str) and (lbl.startswith('Profile_') or lbl.startswith('Section_'))
        except Exception:
            return False

    def is_bim_object(self, obj) -> bool:
        # lightweight heuristic
        try:
            lbl = getattr(obj, 'Label', '')
            return isinstance(lbl, str) and any(k in lbl.lower() for k in ('beam', 'column', 'slab', 'wall'))
        except Exception:
            return False

    def create_structural_from_bim(self, bim_obj):
        # fallback: if a BIM object contains a referenced profile, try to use it
        try:
            if hasattr(bim_obj, 'Profile'):
                return self.create_structural_beam_from_profile(bim_obj.Profile)
            _console_warn(f"create_structural_from_bim: no profile found on {getattr(bim_obj, 'Label', '')}")
        except Exception as e:
            _console_error(f"create_structural_from_bim error: {e}")
        return None

    def create_structural_beam_from_profile(self, profile_obj):
        try:
            # lazy import to avoid top-level dependency
            from freecad.StructureTools import member

            doc = App.ActiveDocument
            if doc is None:
                _console_warn("No active document to create structural member")
                return None

            beam = doc.addObject('Part::FeaturePython', f"Beam_{getattr(profile_obj, 'Label', 'Profile')}")
            member.Member(beam)

            # attach section reference if possible
            try:
                beam.Section = profile_obj
            except Exception:
                try:
                    beam.Section = getattr(profile_obj, 'Shape', None)
                except Exception:
                    pass

            # copy standardized properties if present
            try:
                if hasattr(profile_obj, 'StandardizedProperties'):
                    beam.StandardizedProperties = profile_obj.StandardizedProperties
                    self.apply_section_properties(beam, profile_obj.StandardizedProperties)
                elif hasattr(profile_obj, 'EnhancedProperties'):
                    beam.EnhancedProperties = profile_obj.EnhancedProperties
                    self.apply_section_properties(beam, profile_obj.EnhancedProperties)
            except Exception:
                pass

            beam.Label = f"Beam_{getattr(profile_obj, 'Label', 'Profile')}"
            _console(f"Created structural beam: {beam.Label}")
            return beam
        except Exception as e:
            _console_error(f"create_structural_beam_from_profile error: {e}")
            return None

    def apply_section_properties(self, structural_obj, props):
        try:
            if not props:
                return
            # unwrap if standardized mapping stores original
            if isinstance(props, dict) and 'original' in props:
                data = props['original']
            else:
                data = props

            try:
                if not hasattr(structural_obj, 'SectionProperties'):
                    structural_obj.addProperty('App::PropertyPythonObject', 'SectionProperties', 'Section', 'Standardized section properties')
                structural_obj.SectionProperties = data
            except Exception:
                try:
                    structural_obj.SectionProperties = data
                except Exception:
                    pass

            if isinstance(data, dict):
                for src, dst in (('area_mm2', 'Area'), ('Ix_mm4', 'Ix'), ('Iy_mm4', 'Iy')):
                    if src in data:
                        try:
                            setattr(structural_obj, dst, float(data[src]))
                        except Exception:
                            pass
        except Exception as e:
            _console_error(f"apply_section_properties error: {e}")


# singleton instance
bim_integration = BIMStructuralIntegration()
"""BIM Workbench Integration for StructureTools

Lightweight bridge that converts Profiles/Sections into structural members.
Designed to be import-safe in headless/test environments (guards FreeCAD GUI calls).
"""

import math
import FreeCAD as App

try:
    import FreeCADGui as Gui
    FREECADGUI_AVAILABLE = True
except Exception:
    Gui = None
    FREECADGUI_AVAILABLE = False

try:
    import Part
    PART_AVAILABLE = True
except Exception:
    Part = None
    PART_AVAILABLE = False

try:
    import Draft
    DRAFT_AVAILABLE = True
except Exception:
    Draft = None
    DRAFT_AVAILABLE = False


def _console_print(msg):
    try:
        App.Console.PrintMessage(msg + "\n")
    except Exception:
        print(msg)


def _console_warn(msg):
    try:
        App.Console.PrintWarning(msg + "\n")
    except Exception:
        print("WARNING:", msg)


def _console_error(msg):
    try:
        App.Console.PrintError(msg + "\n")
    except Exception:
        print("ERROR:", msg)


class BIMStructuralIntegration:
    """Bridge between BIM and Structural workbenches"""

    def __init__(self):
        self.bim_to_structural_map = {}
        self.structural_to_bim_map = {}
        self.imported_objects = []

    def import_from_bim(self, selected_objects=None):
        """Import BIM objects or Profile objects and convert to structural elements.

        Accepts a list of FreeCAD objects (BIM elements or Profile objects).
        If selected_objects is None and GUI is available, uses current selection.
        Returns a list of created structural objects.
        """
        try:
            if selected_objects is None and FREECADGUI_AVAILABLE:
                selected_objects = Gui.Selection.getSelection()
        except Exception:
            selected_objects = selected_objects or []

        if not selected_objects:
            _console_warn("No BIM objects selected for import")
            return []

        imported_structural = []

        for bim_obj in selected_objects:
            # Profiles created by SectionDrawing or ArchProfile
            if self.is_profile_object(bim_obj):
                structural_obj = self.create_structural_beam_from_profile(bim_obj)
                if structural_obj:
                    imported_structural.append(structural_obj)
                    self.bim_to_structural_map[bim_obj] = structural_obj
                    self.structural_to_bim_map[structural_obj] = bim_obj
                continue

            # BIM objects
            if self.is_bim_object(bim_obj):
                structural_obj = self.convert_bim_to_structural(bim_obj)
                if structural_obj:
                    imported_structural.append(structural_obj)
                    self.bim_to_structural_map[bim_obj] = structural_obj
                    self.structural_to_bim_map[structural_obj] = bim_obj

        _console_print(f"Imported {len(imported_structural)} structural elements from BIM")
        try:
            App.ActiveDocument.recompute()
        except Exception:
            pass
        return imported_structural

    def is_bim_object(self, obj):
        """Heuristic to detect BIM objects (IFC-like)"""
        try:
            if hasattr(obj, 'IfcType'):
                return True
            if hasattr(obj, 'Role') and obj.Role in ['Structure', 'Structural']:
                return True
            label = getattr(obj, 'Label', '')
            if isinstance(label, str) and any(p in label.lower() for p in ['beam', 'column', 'slab', 'wall', 'foundation']):
                return True
        except Exception:
            return False
        return False

    def is_profile_object(self, obj):
        """Detect profile/section objects produced by SectionDrawing/ArchProfile"""
        try:
            if hasattr(obj, 'StandardizedProperties') or hasattr(obj, 'EnhancedProperties'):
                return True
            label = getattr(obj, 'Label', '')
            if isinstance(label, str) and (label.startswith('Profile_') or label.startswith('Section_')):
                return True
        except Exception:
            pass
        return False

    def convert_bim_to_structural(self, bim_obj):
        """Convert BIM object to a structural element (beam/column/plate).

        Conservative conversion that attempts to extract geometry and section
        properties and create a structural member object in the active document.
        """
        try:
            if not hasattr(bim_obj, 'Shape') or not bim_obj.Shape.isValid():
                _console_warn(f"BIM object {getattr(bim_obj, 'Label', '<no label>')} has invalid shape")
                return None

            structural_type = self.determine_structural_type(bim_obj)
            if structural_type == 'beam':
                return self.create_structural_beam_from_bim(bim_obj)
            elif structural_type == 'column':
                return self.create_structural_column_from_bim(bim_obj)
            elif structural_type in ['slab', 'wall']:
                return self.create_structural_plate_from_bim(bim_obj)
            else:
                _console_warn(f"Unknown structural type for {getattr(bim_obj, 'Label', '<no label>')}")
                return None

        except Exception as e:
            _console_error(f"convert_bim_to_structural error: {e}")
            return None

    def determine_structural_type(self, bim_obj):
        try:
            if hasattr(bim_obj, 'IfcType'):
                ifc_type = bim_obj.IfcType.lower()
                if 'beam' in ifc_type:
                    return 'beam'
                if 'column' in ifc_type:
                    return 'column'
                if 'slab' in ifc_type:
                    return 'slab'
                if 'wall' in ifc_type:
                    return 'wall'

            label = getattr(bim_obj, 'Label', '').lower()
            if 'beam' in label or 'girder' in label:
                return 'beam'
            if 'column' in label:
                return 'column'
            if 'slab' in label or 'floor' in label:
                return 'slab'
            if 'wall' in label:
                return 'wall'

            # fallback: inspect bounding box geometry heuristics
            try:
                shape = bim_obj.Shape
                if getattr(shape, 'ShapeType', '') == 'Solid':
                    bbox = shape.BoundBox
                    dims = sorted([bbox.XLength, bbox.YLength, bbox.ZLength])
                    if dims[2] > 3 * dims[1]:
                        if bbox.ZLength == dims[2]:
                            return 'column'
                        return 'beam'
                    if dims[0] < 0.3 * dims[1]:
                        return 'slab'
            except Exception:
                pass

            return 'unknown'

        except Exception:
            return 'unknown'

    def create_structural_beam_from_bim(self, bim_obj):
        try:
            from freecad.StructureTools import member

            centerline = self.extract_beam_centerline(bim_obj)
            if not centerline:
                _console_warn(f"Cannot extract centerline from {getattr(bim_obj, 'Label', '')}")
                return None

            structural_beam = App.ActiveDocument.addObject("Part::FeaturePython", f"Beam_{bim_obj.Label}")
            member.Member(structural_beam)
            structural_beam.Base = centerline

            if hasattr(bim_obj, 'Material'):
                material_obj = self.convert_bim_material_to_structural(bim_obj.Material)
                if material_obj:
                    try:
                        structural_beam.MaterialMember = material_obj
                    except Exception:
                        pass

            section_props = self.extract_bim_section_properties(bim_obj)
            if section_props:
                self.apply_section_properties(structural_beam, section_props)

            structural_beam.Label = f"Beam_{bim_obj.Label}"
            _console_print(f"Created structural beam: {structural_beam.Label}")
            return structural_beam

        except Exception as e:
            _console_error(f"Error creating structural beam from {getattr(bim_obj, 'Label', '')}: {e}")
            return None

    def create_structural_column_from_bim(self, bim_obj):
        return self.create_structural_beam_from_bim(bim_obj)

    def create_structural_beam_from_profile(self, profile_obj):
        """Create structural element from in-document Profile/Section object."""
        try:
            from freecad.StructureTools import member

            structural_beam = App.ActiveDocument.addObject("Part::FeaturePython", f"Beam_{getattr(profile_obj, 'Label', 'Profile')}")
            member.Member(structural_beam)

            # Attempt to set Section reference
            try:
                structural_beam.Section = profile_obj
            except Exception:
                try:
                    structural_beam.Section = getattr(profile_obj, 'Shape', None)
                except Exception:
                    pass

            # Copy props
            try:
                if hasattr(profile_obj, 'StandardizedProperties'):
                    std = profile_obj.StandardizedProperties
                    self.apply_section_properties(structural_beam, std)
                    structural_beam.StandardizedProperties = std
                elif hasattr(profile_obj, 'EnhancedProperties'):
                    enh = profile_obj.EnhancedProperties
                    self.apply_section_properties(structural_beam, enh)
                    structural_beam.EnhancedProperties = enh
            except Exception:
                pass

            structural_beam.Label = f"Beam_{getattr(profile_obj, 'Label', 'Profile')}"
            _console_print(f"Created structural beam from profile: {structural_beam.Label}")
            return structural_beam

        except Exception as e:
            _console_error(f"Error creating structural beam from profile {getattr(profile_obj, 'Label', '')}: {e}")
            return None

    def create_structural_plate_from_bim(self, bim_obj):
        try:
            try:
                from freecad.StructureTools.objects.StructuralPlate import StructuralPlate
                has_plates = True
            except Exception:
                has_plates = False

            if not has_plates:
                _console_warn("Structural plates not yet implemented - creating placeholder")
                structural_plate = App.ActiveDocument.addObject("Part::Feature", f"Plate_{bim_obj.Label}")
                try:
                    structural_plate.Shape = bim_obj.Shape
                except Exception:
                    pass
                structural_plate.Label = f"Plate_{bim_obj.Label}"
                return structural_plate

            base_faces = self.extract_structural_faces(bim_obj)
            if not base_faces:
                _console_warn(f"Cannot extract structural faces from {getattr(bim_obj, 'Label', '')}")
                return None

            structural_plate = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", f"Plate_{bim_obj.Label}")
            StructuralPlate(structural_plate)
            structural_plate.BaseFace = base_faces[0]

            thickness = self.extract_plate_thickness(bim_obj)
            if thickness:
                structural_plate.Thickness = f"{thickness} mm"

            if hasattr(bim_obj, 'Material'):
                material_obj = self.convert_bim_material_to_structural(bim_obj.Material)
                if material_obj:
                    structural_plate.Material = material_obj

            structural_plate.Label = f"Plate_{bim_obj.Label}"
            _console_print(f"Created structural plate: {structural_plate.Label}")
            return structural_plate

        except Exception as e:
            _console_error(f"Error creating structural plate from {getattr(bim_obj, 'Label', '')}: {e}")
            return None

    def extract_beam_centerline(self, bim_obj):
        try:
            shape = getattr(bim_obj, 'Shape', None)
            if hasattr(bim_obj, 'Base') and getattr(bim_obj, 'Base', None):
                return bim_obj.Base

            if shape is not None and getattr(shape, 'ShapeType', '') == 'Solid':
                longest_edge = None
                max_length = 0
                for edge in getattr(shape, 'Edges', []):
                    try:
                        if edge.Length > max_length:
                            max_length = edge.Length
                            longest_edge = edge
                    except Exception:
                        continue
                if longest_edge:
                    # create a simple placeholder centerline object
                    return App.ActiveDocument.addObject("Part::Feature", "temp_centerline")
        except Exception:
            return None
        return None

    def extract_bim_section_properties(self, bim_obj):
        properties = {}
        try:
            if hasattr(bim_obj, 'Shape') and bim_obj.Shape.isValid():
                bbox = bim_obj.Shape.BoundBox
                if hasattr(bim_obj, 'Width') and hasattr(bim_obj, 'Height'):
                    width = getattr(bim_obj.Width, 'Value', None)
                    height = getattr(bim_obj.Height, 'Value', None)
                else:
                    dims = [bbox.XLength, bbox.YLength, bbox.ZLength]
                    dims.sort()
                    width = dims[0]
                    height = dims[1]
                properties['width'] = width
                properties['height'] = height
                try:
                    properties['area'] = width * height
                    properties['Ixx'] = width * height**3 / 12
                    properties['Iyy'] = height * width**3 / 12
                except Exception:
                    pass
        except Exception:
            pass
        return properties

    def extract_structural_faces(self, bim_obj):
        faces = []
        try:
            if hasattr(bim_obj, 'Shape') and bim_obj.Shape.isValid():
                for face in getattr(bim_obj.Shape, 'Faces', []):
                    faces.append(face)
        except Exception:
            pass
        return faces

    def extract_plate_thickness(self, bim_obj):
        try:
            if hasattr(bim_obj, 'Thickness'):
                return getattr(bim_obj.Thickness, 'Value', None)
            if hasattr(bim_obj, 'Width'):
                return getattr(bim_obj.Width, 'Value', None)
            if hasattr(bim_obj, 'Shape'):
                bbox = bim_obj.Shape.BoundBox
                dims = [bbox.XLength, bbox.YLength, bbox.ZLength]
                return min(dims)
        except Exception:
            pass
        return 200

    def convert_bim_material_to_structural(self, bim_material):
        if not bim_material:
            return None
        try:
            from freecad.StructureTools.utils.MaterialHelper import create_material_from_database
            material_name = getattr(bim_material, 'Label', None) or str(bim_material)
            if 'steel' in material_name.lower() or 'a992' in material_name.lower():
                return create_material_from_database("ASTM_A992", f"Steel_{material_name}")
            if 'concrete' in material_name.lower() or 'c25' in material_name.lower():
                return create_material_from_database("ACI_Normal_25MPa", f"Concrete_{material_name}")
            return create_material_from_database("Custom", material_name)
        except Exception as e:
            _console_warn(f"Could not convert BIM material {getattr(bim_material, 'Label', str(bim_material))}: {e}")
            return None

    def apply_section_properties(self, structural_obj, section_props):
        """Apply standardized or enhanced properties into the structural object."""
        try:
            if not section_props:
                return

            props = section_props.get('original', section_props) if isinstance(section_props, dict) else section_props

            try:
                if not hasattr(structural_obj, 'SectionProperties'):
                    structural_obj.addProperty("App::PropertyPythonObject", "SectionProperties", "Section", "Standardized section properties")
                structural_obj.SectionProperties = props
            except Exception:
                try:
                    structural_obj.SectionProperties = props
                except Exception:
                    pass

            if isinstance(section_props, dict):
                for src_key, dest_key in [('area_mm2', 'Area'), ('Ix_mm4', 'Ix'), ('Iy_mm4', 'Iy'), ('J_mm4', 'J')]:
                    if src_key in section_props:
                        try:
                            val = float(section_props[src_key])
                            setattr(structural_obj, dest_key, val)
                        except Exception:
                            pass

        except Exception as e:
            _console_error(f"Error applying section properties: {e}")

    def export_results_to_bim(self, structural_objects, analysis_results):
        for structural_obj in structural_objects:
            if structural_obj in self.structural_to_bim_map:
                bim_obj = self.structural_to_bim_map[structural_obj]
                self.apply_results_to_bim_object(bim_obj, structural_obj, analysis_results)

    def apply_results_to_bim_object(self, bim_obj, structural_obj, results):
        try:
            if not hasattr(bim_obj, 'StructuralResults'):
                bim_obj.addProperty("App::PropertyString", "StructuralResults", "Analysis", "Structural analysis results")

            if structural_obj.Label in results:
                obj_results = results[structural_obj.Label]
                result_summary = f"Max Moment: {obj_results.get('max_moment', 'N/A')}\n"
                result_summary += f"Max Deflection: {obj_results.get('max_deflection', 'N/A')}\n"
                result_summary += f"Capacity Ratio: {obj_results.get('capacity_ratio', 'N/A')}"
                bim_obj.StructuralResults = result_summary

                if 'capacity_ratio' in obj_results:
                    try:
                        ratio = float(obj_results['capacity_ratio'])
                        if ratio > 1.0:
                            try:
                                bim_obj.ViewObject.ShapeColor = (1.0, 0.0, 0.0)
                            except Exception:
                                pass
                        elif ratio > 0.8:
                            try:
                                bim_obj.ViewObject.ShapeColor = (1.0, 1.0, 0.0)
                            except Exception:
                                pass
                        else:
                            try:
                                bim_obj.ViewObject.ShapeColor = (0.0, 1.0, 0.0)
                            except Exception:
                                pass
                    except Exception:
                        pass
        except Exception as e:
            _console_error(f"Error applying results to BIM object {getattr(bim_obj, 'Label', '')}: {e}")

    def sync_geometry_changes(self):
        for bim_obj, structural_obj in self.bim_to_structural_map.items():
            try:
                if hasattr(bim_obj, 'Shape') and hasattr(structural_obj, 'Shape'):
                    if bim_obj.Shape.isValid() and structural_obj.Shape.isValid():
                        if bim_obj.Shape.BoundBox != structural_obj.Shape.BoundBox:
                            _console_print(f"Updating structural object {structural_obj.Label} from BIM changes")
                            try:
                                self.update_structural_from_bim(bim_obj, structural_obj)
                            except Exception:
                                pass
            except Exception:
                pass


# Global instance for integration
    def apply_section_properties(self, structural_obj, section_props):
        """Apply section properties to structural object"""
        try:
            if not section_props:
                return

            # If section_props contains a 'original' key (standardized mapping), unwrap
            props = section_props.get('original', section_props) if isinstance(section_props, dict) else section_props

            # Attach a SectionProperties container for downstream tools
            try:
                if not hasattr(structural_obj, 'SectionProperties'):
                    structural_obj.addProperty("App::PropertyPythonObject", "SectionProperties", "Section", "Standardized section properties")
                structural_obj.SectionProperties = props
            except Exception:
                # best-effort: set attribute directly
                try:
                    structural_obj.SectionProperties = props
                except Exception:
                    pass

            # If standardized keys exist, try to populate simple numeric properties
            if isinstance(section_props, dict):
                # common keys
                for src_key, dest_key in [('area_mm2', 'Area'), ('Ix_mm4', 'Ix'), ('Iy_mm4', 'Iy'), ('J_mm4', 'J')]:
                    if src_key in section_props:
                        try:
                            val = float(section_props[src_key])
                            setattr(structural_obj, dest_key, val)
                        except Exception:
                            pass

        except Exception as e:
                _console_error(f"Error applying section properties: {str(e)}")
    
    def export_results_to_bim(self, structural_objects, analysis_results):
        """Export structural analysis results back to BIM objects"""
        for structural_obj in structural_objects:
            if structural_obj in self.structural_to_bim_map:
                bim_obj = self.structural_to_bim_map[structural_obj]
                self.apply_results_to_bim_object(bim_obj, structural_obj, analysis_results)
    
    def apply_results_to_bim_object(self, bim_obj, structural_obj, results):
        """Apply analysis results to BIM object properties"""
        try:
            # Add custom properties to store analysis results
            if not hasattr(bim_obj, 'StructuralResults'):
                bim_obj.addProperty("App::PropertyString", "StructuralResults", "Analysis", "Structural analysis results")
            
            # Format results summary
            if structural_obj.Label in results:
                obj_results = results[structural_obj.Label]
                result_summary = f"Max Moment: {obj_results.get('max_moment', 'N/A')}\n"
                result_summary += f"Max Deflection: {obj_results.get('max_deflection', 'N/A')}\n"
                result_summary += f"Capacity Ratio: {obj_results.get('capacity_ratio', 'N/A')}"
                
                bim_obj.StructuralResults = result_summary
                
                # Color code based on capacity ratio
                if 'capacity_ratio' in obj_results:
                    ratio = float(obj_results['capacity_ratio'])
                    if ratio > 1.0:
                        bim_obj.ViewObject.ShapeColor = (1.0, 0.0, 0.0)  # Red for overstressed
                    elif ratio > 0.8:
                        bim_obj.ViewObject.ShapeColor = (1.0, 1.0, 0.0)  # Yellow for high utilization
                    else:
                        bim_obj.ViewObject.ShapeColor = (0.0, 1.0, 0.0)  # Green for safe
                        
        except Exception as e:
                _console_error(f"Error applying results to BIM object {getattr(bim_obj, 'Label', '')}: {str(e)}")
    
    def sync_geometry_changes(self):
        """Synchronize geometry changes between BIM and structural objects"""
        for bim_obj, structural_obj in self.bim_to_structural_map.items():
            if hasattr(bim_obj, 'Shape') and hasattr(structural_obj, 'Shape'):
                # Simple check - could be more sophisticated
                if bim_obj.Shape.isValid() and structural_obj.Shape.isValid():
                    # Update structural object if BIM geometry changed
                    if bim_obj.Shape.BoundBox != structural_obj.Shape.BoundBox:
                            _console_print(f"Updating structural object {structural_obj.Label} from BIM changes")
                        # Re-extract geometry and update
                        self.update_structural_from_bim(bim_obj, structural_obj)

# Global instance for integration
bim_integration = BIMStructuralIntegration()
