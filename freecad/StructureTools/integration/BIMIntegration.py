# BIM Integration Module
"""
BIM Workbench Integration for StructureTools

This module provides seamless integration between the BIM Workbench
and StructureTools, allowing:
1. Import BIM objects as structural elements
2. Convert structural analysis results back to BIM
3. Maintain object relationships and properties
4. Synchronize changes between workbenches
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft
import math

class BIMStructuralIntegration:
    """Main class for BIM-Structural integration"""
    
    def __init__(self):
        self.bim_to_structural_map = {}
        self.structural_to_bim_map = {}
        self.imported_objects = []
        
    def import_from_bim(self, selected_objects=None):
        """
        Import BIM objects and convert to structural elements
        
        Args:
            selected_objects: List of BIM objects to convert, if None uses selection
        """
        if selected_objects is None:
            selected_objects = Gui.Selection.getSelection()
        
        if not selected_objects:
            FreeCAD.Console.PrintWarning("No BIM objects selected for import\n")
            return []
        
        imported_structural = []
        
        for bim_obj in selected_objects:
            # Check if object has BIM/IFC properties
            if self.is_bim_object(bim_obj):
                structural_obj = self.convert_bim_to_structural(bim_obj)
                if structural_obj:
                    imported_structural.append(structural_obj)
                    self.bim_to_structural_map[bim_obj] = structural_obj
                    self.structural_to_bim_map[structural_obj] = bim_obj
                    
        FreeCAD.Console.PrintMessage(f"Imported {len(imported_structural)} structural elements from BIM\n")
        App.ActiveDocument.recompute()
        return imported_structural
    
    def is_bim_object(self, obj):
        """Check if object is a BIM object"""
        # Check for BIM/IFC properties
        if hasattr(obj, 'IfcType'):
            return True
        if hasattr(obj, 'Role') and obj.Role in ['Structure', 'Structural']:
            return True
        # Check object name patterns
        if any(pattern in obj.Label.lower() for pattern in ['beam', 'column', 'slab', 'wall', 'foundation']):
            return True
        return False
    
    def convert_bim_to_structural(self, bim_obj):
        """Convert BIM object to appropriate structural element"""
        if not hasattr(bim_obj, 'Shape') or not bim_obj.Shape.isValid():
            FreeCAD.Console.PrintWarning(f"BIM object {bim_obj.Label} has invalid shape\n")
            return None
        
        # Determine structural type from BIM properties
        structural_type = self.determine_structural_type(bim_obj)
        
        if structural_type == 'beam':
            return self.create_structural_beam_from_bim(bim_obj)
        elif structural_type == 'column':
            return self.create_structural_column_from_bim(bim_obj)
        elif structural_type in ['slab', 'wall']:
            return self.create_structural_plate_from_bim(bim_obj)
        else:
            FreeCAD.Console.PrintWarning(f"Unknown structural type for {bim_obj.Label}\n")
            return None
    
    def determine_structural_type(self, bim_obj):
        """Determine structural element type from BIM object"""
        # Check IFC type if available
        if hasattr(bim_obj, 'IfcType'):
            ifc_type = bim_obj.IfcType.lower()
            if 'beam' in ifc_type:
                return 'beam'
            elif 'column' in ifc_type:
                return 'column'
            elif 'slab' in ifc_type:
                return 'slab'
            elif 'wall' in ifc_type:
                return 'wall'
        
        # Check object label
        label = bim_obj.Label.lower()
        if 'beam' in label or 'girder' in label:
            return 'beam'
        elif 'column' in label or 'pillar' in label:
            return 'column'
        elif 'slab' in label or 'floor' in label:
            return 'slab'
        elif 'wall' in label:
            return 'wall'
        
        # Analyze geometry to determine type
        shape = bim_obj.Shape
        if shape.ShapeType == 'Solid':
            # Analyze dimensions to guess element type
            bbox = shape.BoundBox
            length = bbox.XLength
            width = bbox.YLength
            height = bbox.ZLength
            
            # Sort dimensions
            dims = sorted([length, width, height])
            
            # If one dimension is much larger (>3x), likely beam or column
            if dims[2] > 3 * dims[1]:
                # Check if vertical (column) or horizontal (beam)
                if height == dims[2]:
                    return 'column'
                else:
                    return 'beam'
            # If one dimension is much smaller (<0.3x), likely slab/wall
            elif dims[0] < 0.3 * dims[1]:
                return 'slab'
        
        return 'unknown'
    
    def create_structural_beam_from_bim(self, bim_obj):
        """Create structural beam from BIM object"""
        try:
            # Import member module
            from freecad.StructureTools import member
            
            # Extract beam centerline
            centerline = self.extract_beam_centerline(bim_obj)
            if not centerline:
                FreeCAD.Console.PrintWarning(f"Cannot extract centerline from {bim_obj.Label}\n")
                return None
            
            # Create member object
            structural_beam = App.ActiveDocument.addObject("Part::FeaturePython", f"Beam_{bim_obj.Label}")
            member.Member(structural_beam)
            
            # Set base geometry
            structural_beam.Base = centerline
            
            # Extract and set material properties
            if hasattr(bim_obj, 'Material'):
                material_obj = self.convert_bim_material_to_structural(bim_obj.Material)
                if material_obj:
                    structural_beam.MaterialMember = material_obj
            
            # Extract section properties
            section_props = self.extract_bim_section_properties(bim_obj)
            if section_props:
                self.apply_section_properties(structural_beam, section_props)
            
            # Copy additional properties
            structural_beam.Label = f"Beam_{bim_obj.Label}"
            if hasattr(bim_obj, 'Description'):
                structural_beam.Description = bim_obj.Description
            
            FreeCAD.Console.PrintMessage(f"Created structural beam: {structural_beam.Label}\n")
            return structural_beam
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error creating structural beam from {bim_obj.Label}: {str(e)}\n")
            return None
    
    def create_structural_column_from_bim(self, bim_obj):
        """Create structural column from BIM object"""
        # Similar to beam creation but with column-specific handling
        return self.create_structural_beam_from_bim(bim_obj)  # Same process for now
    
    def create_structural_plate_from_bim(self, bim_obj):
        """Create structural plate from BIM slab/wall"""
        try:
            # Check if we have plate creation capability
            try:
                from freecad.StructureTools.objects.StructuralPlate import StructuralPlate
                has_plates = True
            except ImportError:
                has_plates = False
            
            if not has_plates:
                FreeCAD.Console.PrintWarning("Structural plates not yet implemented - creating placeholder\n")
                # Create placeholder Part object for now
                structural_plate = App.ActiveDocument.addObject("Part::Feature", f"Plate_{bim_obj.Label}")
                structural_plate.Shape = bim_obj.Shape
                structural_plate.Label = f"Plate_{bim_obj.Label}"
                return structural_plate
            
            # Extract base face from BIM object
            base_faces = self.extract_structural_faces(bim_obj)
            if not base_faces:
                FreeCAD.Console.PrintWarning(f"Cannot extract structural faces from {bim_obj.Label}\n")
                return None
            
            # Create structural plate
            structural_plate = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", f"Plate_{bim_obj.Label}")
            StructuralPlate(structural_plate)
            
            # Set base face (use first face for now)
            structural_plate.BaseFace = base_faces[0]
            
            # Extract thickness
            thickness = self.extract_plate_thickness(bim_obj)
            if thickness:
                structural_plate.Thickness = f"{thickness} mm"
            
            # Extract material
            if hasattr(bim_obj, 'Material'):
                material_obj = self.convert_bim_material_to_structural(bim_obj.Material)
                if material_obj:
                    structural_plate.Material = material_obj
            
            structural_plate.Label = f"Plate_{bim_obj.Label}"
            FreeCAD.Console.PrintMessage(f"Created structural plate: {structural_plate.Label}\n")
            return structural_plate
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error creating structural plate from {bim_obj.Label}: {str(e)}\n")
            return None
    
    def extract_beam_centerline(self, bim_obj):
        """Extract centerline from BIM beam object"""
        shape = bim_obj.Shape
        
        # Try to find existing centerline
        if hasattr(bim_obj, 'Base') and bim_obj.Base:
            return bim_obj.Base
        
        # For simple cases, create line between centroids of end faces
        if shape.ShapeType == 'Solid':
            # Find the longest edge as approximation
            longest_edge = None
            max_length = 0
            
            for edge in shape.Edges:
                if edge.Length > max_length:
                    max_length = edge.Length
                    longest_edge = edge
            
            if longest_edge:
                # Create wire from edge
                return App.ActiveDocument.addObject("Part::Feature", "temp_centerline")
        
        return None
    
    def extract_bim_section_properties(self, bim_obj):
        """Extract section properties from BIM object"""
        properties = {}
        
        # Try to get cross-sectional area and moments of inertia
        if hasattr(bim_obj, 'Shape') and bim_obj.Shape.isValid():
            # For simplified approach, estimate from bounding box
            bbox = bim_obj.Shape.BoundBox
            
            # Estimate section properties (very basic)
            if hasattr(bim_obj, 'Width') and hasattr(bim_obj, 'Height'):
                width = bim_obj.Width.Value
                height = bim_obj.Height.Value
            else:
                # Guess from bounding box
                dims = [bbox.XLength, bbox.YLength, bbox.ZLength]
                dims.sort()
                width = dims[0]
                height = dims[1]
            
            properties['width'] = width
            properties['height'] = height
            properties['area'] = width * height
            properties['Ixx'] = width * height**3 / 12
            properties['Iyy'] = height * width**3 / 12
        
        return properties
    
    def extract_structural_faces(self, bim_obj):
        """Extract faces suitable for structural plate elements"""
        faces = []
        
        if hasattr(bim_obj, 'Shape') and bim_obj.Shape.isValid():
            for face in bim_obj.Shape.Faces:
                # For slabs, typically want horizontal faces
                # For walls, typically want vertical faces
                faces.append(face)
        
        return faces
    
    def extract_plate_thickness(self, bim_obj):
        """Extract thickness from BIM slab/wall"""
        if hasattr(bim_obj, 'Thickness'):
            return bim_obj.Thickness.Value
        elif hasattr(bim_obj, 'Width'):
            return bim_obj.Width.Value
        elif hasattr(bim_obj, 'Shape'):
            # Estimate from bounding box
            bbox = bim_obj.Shape.BoundBox
            dims = [bbox.XLength, bbox.YLength, bbox.ZLength]
            return min(dims)  # Assume thickness is smallest dimension
        
        return 200  # Default 200mm
    
    def convert_bim_material_to_structural(self, bim_material):
        """Convert BIM material to structural material"""
        if not bim_material:
            return None
        
        try:
            # Import material creation utilities
            from freecad.StructureTools.utils.MaterialHelper import create_material_from_database
            
            # Try to match BIM material to structural database
            material_name = bim_material.Label if hasattr(bim_material, 'Label') else str(bim_material)
            
            # Simple matching - could be enhanced
            if 'steel' in material_name.lower() or 'a992' in material_name.lower():
                return create_material_from_database("ASTM_A992", f"Steel_{material_name}")
            elif 'concrete' in material_name.lower() or 'c25' in material_name.lower():
                return create_material_from_database("ACI_Normal_25MPa", f"Concrete_{material_name}")
            else:
                # Create custom material
                return create_material_from_database("Custom", material_name)
                
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Could not convert BIM material {material_name}: {str(e)}\n")
            return None
    
    def apply_section_properties(self, structural_obj, section_props):
        """Apply section properties to structural object"""
        # This would set section properties - implementation depends on section system
        pass
    
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
            FreeCAD.Console.PrintError(f"Error applying results to BIM object {bim_obj.Label}: {str(e)}\n")
    
    def sync_geometry_changes(self):
        """Synchronize geometry changes between BIM and structural objects"""
        for bim_obj, structural_obj in self.bim_to_structural_map.items():
            if hasattr(bim_obj, 'Shape') and hasattr(structural_obj, 'Shape'):
                # Simple check - could be more sophisticated
                if bim_obj.Shape.isValid() and structural_obj.Shape.isValid():
                    # Update structural object if BIM geometry changed
                    if bim_obj.Shape.BoundBox != structural_obj.Shape.BoundBox:
                        FreeCAD.Console.PrintMessage(f"Updating structural object {structural_obj.Label} from BIM changes\n")
                        # Re-extract geometry and update
                        self.update_structural_from_bim(bim_obj, structural_obj)

# Global instance for integration
bim_integration = BIMStructuralIntegration()
