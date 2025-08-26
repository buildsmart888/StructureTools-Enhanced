# -*- coding: utf-8 -*-
"""
command_plate.py - FreeCAD command to create structural plate/shell elements

This module provides commands for creating structural plates from selected faces
with comprehensive properties, meshing, and analysis capabilities.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft
from PySide import QtWidgets, QtCore, QtGui
import os

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


from .objects.StructuralPlate import StructuralPlate, ViewProviderStructuralPlate
from .taskpanels.PlatePropertiesPanel import PlatePropertiesPanel


class CreateStructuralPlateCommand:
    """
    FreeCAD command to create structural plate elements from selected faces.
    
    This command allows users to:
    1. Select faces from existing geometry
    2. Create StructuralPlate objects with properties
    3. Apply material and thickness
    4. Define boundary conditions
    5. Apply surface loads
    """
    
    def GetResources(self):
        """Return command resources (icon, menu text, tooltip)."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'structural_plate.svg'),
            'MenuText': 'Create Structural Plate',
            'ToolTip': 'Create structural plate/shell element from selected faces'
        }
    
    def IsActive(self):
        """Return True if command should be active."""
        return App.ActiveDocument is not None
    
    def Activated(self):
        """Execute the command."""
        # Get current selection
        selection = Gui.Selection.getSelection()
        selected_faces = []
        
        # Check for selected faces
        sel_objects = Gui.Selection.getSelectionEx()
        for sel_obj in sel_objects:
            if sel_obj.SubElementNames:
                for sub_name in sel_obj.SubElementNames:
                    if 'Face' in sub_name:
                        # Get the actual face
                        face_index = int(sub_name.replace('Face', '')) - 1
                        if hasattr(sel_obj.Object, 'Shape') and sel_obj.Object.Shape.Faces:
                            if face_index < len(sel_obj.Object.Shape.Faces):
                                selected_faces.append({
                                    'object': sel_obj.Object,
                                    'face': sel_obj.Object.Shape.Faces[face_index],
                                    'face_name': sub_name
                                })
        
        if not selected_faces:
            # No faces selected, show message
            QtWidgets.QMessageBox.information(
                None, 
                'Create Structural Plate',
                'Please select one or more faces to create structural plates.\n\n'
                'You can select faces from existing geometry (Part objects, sketches, etc.)'
            )
            return
        
        # Create plates from selected faces
        created_plates = []
        for face_info in selected_faces:
            plate = self.create_plate_from_face(face_info)
            if plate:
                created_plates.append(plate)
        
        if created_plates:
            # Show properties panel for the first created plate
            if len(created_plates) == 1:
                self.show_plate_properties_panel(created_plates[0])
            else:
                # Multiple plates created
                QtWidgets.QMessageBox.information(
                    None,
                    'Structural Plates Created',
                    f'Successfully created {len(created_plates)} structural plates.\n\n'
                    'Select a plate and use "Edit Plate Properties" to configure settings.'
                )
        
        # Update 3D view
        App.ActiveDocument.recompute()
        Gui.updateGui()
    
    def create_plate_from_face(self, face_info):
        """
        Create a StructuralPlate object from face information.
        
        Args:
            face_info (dict): Dictionary with 'object', 'face', and 'face_name'
            
        Returns:
            StructuralPlate object or None if creation failed
        """
        try:
            # Create the DocumentObject
            face_obj = face_info['object']
            face = face_info['face']
            face_name = face_info['face_name']
            
            # Generate unique name
            plate_name = f"StructuralPlate_{face_obj.Label}_{face_name}"
            plate_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", plate_name)
            
            # Create the StructuralPlate proxy
            plate_proxy = StructuralPlate(plate_obj)
            
            # Create ViewProvider
            if App.GuiUp:
                view_provider = ViewProviderStructuralPlate(plate_obj.ViewObject)
            
            # Set basic properties from face
            self.extract_plate_properties_from_face(plate_obj, face_info)
            
            # Set default values
            plate_obj.Label = f"Plate {face_obj.Label} {face_name}"
            
            return plate_obj
            
        except Exception as e:
            App.Console.PrintError(f"Error creating structural plate: {str(e)}\n")
            return None
    
    def extract_plate_properties_from_face(self, plate_obj, face_info):
        """
        Extract geometric properties from the selected face.
        
        Args:
            plate_obj: StructuralPlate DocumentObject
            face_info (dict): Face information dictionary
        """
        try:
            face = face_info['face']
            
            # Calculate face properties
            area = face.Area
            perimeter = face.Length  # Perimeter length
            
            # Get face center
            center = face.CenterOfMass
            
            # Calculate face normal (local Z-axis)
            # Use face normal at center
            u, v = face.Surface.parameter(center)
            normal = face.normalAt(u, v)
            normal.normalize()
            
            # Calculate local X and Y axes
            # Use the face's U and V parameter directions
            try:
                u_dir = face.Surface.uIso(v).tangent(u)[0]
                u_dir.normalize()
                local_x = u_dir
            except:
                # Fallback: use global X direction projected onto face
                global_x = App.Vector(1, 0, 0)
                local_x = global_x - (global_x.dot(normal) * normal)
                if local_x.Length < 0.001:  # X is parallel to normal
                    global_y = App.Vector(0, 1, 0)
                    local_x = global_y - (global_y.dot(normal) * normal)
                local_x.normalize()
            
            # Local Y = Z × X (right-hand rule)
            local_y = normal.cross(local_x)
            local_y.normalize()
            
            # Set geometric properties
            plate_obj.Area = f"{area:.2f} mm²"
            plate_obj.Perimeter = f"{perimeter:.2f} mm"
            plate_obj.LocalXAxis = local_x
            plate_obj.LocalYAxis = local_y
            plate_obj.LocalZAxis = normal
            
            # Calculate aspect ratio (approximate)
            # Find bounding box in local coordinates
            bbox = face.BoundBox
            length = max(bbox.XLength, bbox.YLength, bbox.ZLength)
            width = min(bbox.XLength, bbox.YLength, bbox.ZLength)
            if width > 0.001:
                aspect_ratio = length / width
            else:
                aspect_ratio = 1.0
            
            plate_obj.AspectRatio = aspect_ratio
            
            # Extract corner nodes if face is planar and has 3-4 vertices
            vertices = face.Vertexes
            if len(vertices) in [3, 4]:
                # Create or find structural nodes at vertices
                corner_nodes = []
                for vertex in vertices:
                    node = self.find_or_create_structural_node(vertex.Point)
                    if node:
                        corner_nodes.append(node)
                
                if corner_nodes:
                    plate_obj.CornerNodes = corner_nodes
            
            # Store reference to source face for meshing
            plate_obj.addProperty("App::PropertyLink", "SourceFace", "Source",
                                 "Source face object for plate geometry")
            plate_obj.addProperty("App::PropertyString", "SourceFaceName", "Source", 
                                 "Source face name")
            plate_obj.SourceFace = face_info['object']
            plate_obj.SourceFaceName = face_info['face_name']
            
        except Exception as e:
            App.Console.PrintWarning(f"Warning extracting plate properties: {str(e)}\n")
    
    def find_or_create_structural_node(self, point, tolerance=1.0):
        """
        Find existing StructuralNode at point or create new one.
        
        Args:
            point (App.Vector): 3D point location
            tolerance (float): Search tolerance in mm
            
        Returns:
            StructuralNode object or None
        """
        try:
            # Search for existing nodes
            for obj in App.ActiveDocument.Objects:
                if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
                    if obj.Proxy.Type == "StructuralNode":
                        if hasattr(obj, 'Position'):
                            existing_point = obj.Position
                            distance = point.distanceToPoint(existing_point)
                            if distance <= tolerance:
                                return obj
            
            # Create new node
            from .objects.StructuralNode import StructuralNode, ViewProviderStructuralNode
            
            node_name = f"Node_{point.x:.0f}_{point.y:.0f}_{point.z:.0f}"
            node_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", node_name)
            node_proxy = StructuralNode(node_obj)
            
            if App.GuiUp:
                view_provider = ViewProviderStructuralNode(node_obj.ViewObject)
            
            # Set position
            node_obj.Position = point
            
            return node_obj
            
        except Exception as e:
            App.Console.PrintWarning(f"Warning creating structural node: {str(e)}\n")
            return None
    
    def show_plate_properties_panel(self, plate_obj):
        """
        Show the plate properties task panel.
        
        Args:
            plate_obj: StructuralPlate DocumentObject
        """
        try:
            panel = PlatePropertiesPanel(plate_obj)
            Gui.Control.showDialog(panel)
        except Exception as e:
            App.Console.PrintError(f"Error showing plate properties panel: {str(e)}\n")


class EditStructuralPlateCommand:
    """
    Command to edit existing structural plate properties.
    """
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'edit_plate.svg'),
            'MenuText': 'Edit Plate Properties',
            'ToolTip': 'Edit structural plate properties and settings'
        }
    
    def IsActive(self):
        """Return True if a structural plate is selected."""
        selection = Gui.Selection.getSelection()
        if len(selection) == 1:
            obj = selection[0]
            if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
                return obj.Proxy.Type == "StructuralPlate"
        return False
    
    def Activated(self):
        """Execute the command."""
        selection = Gui.Selection.getSelection()
        if selection:
            plate_obj = selection[0]
            try:
                panel = PlatePropertiesPanel(plate_obj)
                Gui.Control.showDialog(panel)
            except Exception as e:
                App.Console.PrintError(f"Error showing plate properties panel: {str(e)}\n")


# Register commands
if App.GuiUp:
    Gui.addCommand('CreateStructuralPlate', CreateStructuralPlateCommand())
    Gui.addCommand('EditStructuralPlate', EditStructuralPlateCommand())