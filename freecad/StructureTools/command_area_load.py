# -*- coding: utf-8 -*-
"""
command_area_load.py - FreeCAD command to create area loads on surfaces

This module provides commands for creating area loads on structural surfaces
with comprehensive visualization and analysis integration.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtWidgets, QtCore
import os

from .objects.AreaLoad import AreaLoad, ViewProviderAreaLoad
from .taskpanels.AreaLoadPanel import AreaLoadPanel
from .utils.thai_units import get_thai_converter
from .utils.units_manager import get_units_manager, format_force
from .design.thai_design_requirements import get_thai_design_instance


class CreateAreaLoadCommand:
    """FreeCAD command to create area loads on selected surfaces."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'area_load.svg'),
            'MenuText': 'Create Area Load',
            'ToolTip': 'Create area load on selected faces/surfaces'
        }
    
    def IsActive(self):
        """Return True if command should be active."""
        return App.ActiveDocument is not None
    
    def Activated(self):
        """Execute the command."""
        # Get selected faces
        selected_faces = self.get_selected_faces()
        
        if not selected_faces:
            QtWidgets.QMessageBox.information(
                None,
                'Create Area Load',
                'Please select faces or surfaces to apply area loads.\n\n'
                'You can select:\n'
                '• Faces from Part objects\n'
                '• Structural plates\n'
                '• Any surface geometry'
            )
            return
        
        # Create area load
        area_load = self.create_area_load(selected_faces)
        if area_load:
            # Show properties panel
            self.show_area_load_panel(area_load)
        
        App.ActiveDocument.recompute()
        Gui.updateGui()
    
    def get_selected_faces(self):
        """Get list of selected faces."""
        selected_faces = []
        
        try:
            sel_objects = Gui.Selection.getSelectionEx()
            for sel_obj in sel_objects:
                if sel_obj.SubElementNames:
                    # Sub-elements selected (faces)
                    for sub_name in sel_obj.SubElementNames:
                        if 'Face' in sub_name:
                            selected_faces.append({
                                'object': sel_obj.Object,
                                'face_name': sub_name
                            })
                else:
                    # Whole object selected - check if it's a structural plate
                    obj = sel_obj.Object
                    if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
                        if obj.Proxy.Type == "StructuralPlate":
                            selected_faces.append({
                                'object': obj,
                                'face_name': 'Plate'
                            })
                    elif hasattr(obj, 'Shape'):
                        # Add all faces of the shape
                        if hasattr(obj.Shape, 'Faces'):
                            for i, face in enumerate(obj.Shape.Faces):
                                selected_faces.append({
                                    'object': obj,
                                    'face_name': f'Face{i+1}'
                                })
        except Exception as e:
            App.Console.PrintWarning(f"Warning getting selected faces: {str(e)}\n")
        
        return selected_faces
    
    def create_area_load(self, selected_faces):
        """Create AreaLoad object from selected faces."""
        try:
            # Generate unique name
            area_load_name = "AreaLoad"
            counter = 1
            while App.ActiveDocument.getObject(area_load_name):
                area_load_name = f"AreaLoad_{counter:03d}"
                counter += 1
            
            # Create DocumentObject
            area_load_obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", area_load_name)
            
            # Create AreaLoad proxy
            area_load_proxy = AreaLoad(area_load_obj)
            
            # Create ViewProvider
            if App.GuiUp:
                view_provider = ViewProviderAreaLoad(area_load_obj.ViewObject)
            
            # Set target faces
            target_objects = []
            for face_info in selected_faces:
                target_objects.append(face_info['object'])
            
            # Remove duplicates
            unique_targets = []
            for obj in target_objects:
                if obj not in unique_targets:
                    unique_targets.append(obj)
            
            area_load_obj.TargetFaces = unique_targets
            
            # Set default label
            if len(unique_targets) == 1:
                area_load_obj.Label = f"AreaLoad_{unique_targets[0].Label}"
            else:
                area_load_obj.Label = f"AreaLoad_{len(unique_targets)}_faces"
            
            return area_load_obj
            
        except Exception as e:
            App.Console.PrintError(f"Error creating area load: {str(e)}\n")
            return None
    
    def show_area_load_panel(self, area_load_obj):
        """Show area load properties panel."""
        try:
            panel = AreaLoadPanel(area_load_obj)
            Gui.Control.showDialog(panel)
        except Exception as e:
            App.Console.PrintError(f"Error showing area load panel: {str(e)}\n")


class EditAreaLoadCommand:
    """Command to edit existing area load properties."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'edit_area_load.svg'),
            'MenuText': 'Edit Area Load',
            'ToolTip': 'Edit area load properties and settings'
        }
    
    def IsActive(self):
        """Return True if area load is selected."""
        selection = Gui.Selection.getSelection()
        if len(selection) == 1:
            obj = selection[0]
            if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
                return obj.Proxy.Type == "AreaLoad"
        return False
    
    def Activated(self):
        """Execute the command."""
        selection = Gui.Selection.getSelection()
        if selection:
            area_load_obj = selection[0]
            try:
                panel = AreaLoadPanel(area_load_obj)
                Gui.Control.showDialog(panel)
            except Exception as e:
                App.Console.PrintError(f"Error showing area load panel: {str(e)}\n")


# Register commands
if App.GuiUp:
    Gui.addCommand('CreateAreaLoad', CreateAreaLoadCommand())
    Gui.addCommand('EditAreaLoad', EditAreaLoadCommand())