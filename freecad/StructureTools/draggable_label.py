import FreeCAD, FreeCADGui, Part, Draft
from typing import Optional
import logging

# Prefer PySide2 when available
try:
    from PySide2 import QtCore
except ImportError:
    try:
        from PySide import QtCore
    except ImportError as e:
        raise ImportError("Neither PySide2 nor PySide could be imported. Please install one of them.") from e

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class DraggableReactionLabel:
    """A draggable label for reaction values that can be repositioned by the user."""
    
    def __init__(self, obj):
        """Initialize the draggable label object."""
        obj.Proxy = self
        
        # Text properties
        obj.addProperty("App::PropertyString", "LabelText", "Text", "The text to display")
        obj.addProperty("App::PropertyInteger", "FontSize", "Text", "Font size for the label").FontSize = 8
        obj.addProperty("App::PropertyColor", "TextColor", "Text", "Color of the text").TextColor = (0.0, 0.0, 0.0, 0.0)
        
        # Position properties
        obj.addProperty("App::PropertyVector", "Position", "Position", "Label position")
        obj.addProperty("App::PropertyVector", "OriginalPosition", "Position", "Original position before dragging")
        
        # Connection properties
        obj.addProperty("App::PropertyVector", "ConnectedPoint", "Connection", "Point this label is connected to")
        obj.addProperty("App::PropertyBool", "ShowConnectionLine", "Connection", "Show line connecting label to point").ShowConnectionLine = True
        obj.addProperty("App::PropertyColor", "ConnectionLineColor", "Connection", "Color of connection line").ConnectionLineColor = (0.5, 0.5, 0.5, 0.0)
        
        # Dragging state
        obj.addProperty("App::PropertyBool", "IsDragging", "Internal", "Internal dragging state").IsDragging = False
        obj.addProperty("App::PropertyBool", "HasBeenMoved", "Internal", "Whether label has been moved from original position").HasBeenMoved = False
        
        # Visual elements storage
        self.text_object = None
        self.connection_line = None
        self.label_background = None
    
    def execute(self, obj):
        """Update the label visualization."""
        try:
            self.update_label_geometry(obj)
        except Exception as e:
            logger.error(f"Error in DraggableReactionLabel.execute: {str(e)}")
    
    def update_label_geometry(self, obj):
        """Update the 3D geometry of the label."""
        # Clear existing objects
        self.clear_geometry()
        
        if not obj.LabelText or not obj.Position:
            return
        
        # Create text annotation
        try:
            self.text_object = FreeCAD.ActiveDocument.addObject("App::Annotation", f"Text_{obj.Name}")
            self.text_object.LabelText = obj.LabelText
            self.text_object.Position = obj.Position
            
            # Set text properties
            if hasattr(self.text_object, 'ViewObject'):
                self.text_object.ViewObject.FontSize = obj.FontSize
                if hasattr(self.text_object.ViewObject, 'TextColor'):
                    self.text_object.ViewObject.TextColor = obj.TextColor[:3]
                
                # Make text always face camera
                if hasattr(self.text_object.ViewObject, 'DisplayMode'):
                    self.text_object.ViewObject.DisplayMode = "Screen"
        except Exception as e:
            logger.error(f"Error creating text object: {str(e)}")
        
        # Create connection line if enabled
        if obj.ShowConnectionLine and obj.ConnectedPoint:
            try:
                self.connection_line = FreeCAD.ActiveDocument.addObject("Part::Feature", f"Connection_{obj.Name}")
                line_shape = Part.makeLine(obj.ConnectedPoint, obj.Position)
                self.connection_line.Shape = line_shape
                
                # Set line properties
                if hasattr(self.connection_line, 'ViewObject'):
                    self.connection_line.ViewObject.LineColor = obj.ConnectionLineColor[:3]
                    self.connection_line.ViewObject.LineWidth = 1.0
                    self.connection_line.ViewObject.DrawStyle = "Dashed"
            except Exception as e:
                logger.error(f"Error creating connection line: {str(e)}")
        
        # Create label background (optional visual enhancement)
        try:
            if obj.LabelText:
                self.create_label_background(obj)
        except Exception as e:
            logger.error(f"Error creating label background: {str(e)}")
    
    def create_label_background(self, obj):
        """Create a subtle background for the label to improve readability."""
        try:
            # Estimate text dimensions (rough approximation)
            text_width = len(obj.LabelText) * obj.FontSize * 0.6
            text_height = obj.FontSize * 1.2
            
            # Create a small rectangle behind the text
            corner1 = obj.Position + FreeCAD.Vector(-text_width/2, -text_height/2, 0)
            corner2 = obj.Position + FreeCAD.Vector(text_width/2, text_height/2, 0)
            
            # Create rectangle (simplified as a line frame)
            self.label_background = FreeCAD.ActiveDocument.addObject("Part::Feature", f"Background_{obj.Name}")
            
            lines = [
                Part.makeLine(corner1, FreeCAD.Vector(corner2.x, corner1.y, corner1.z)),
                Part.makeLine(FreeCAD.Vector(corner2.x, corner1.y, corner1.z), corner2),
                Part.makeLine(corner2, FreeCAD.Vector(corner1.x, corner2.y, corner2.z)),
                Part.makeLine(FreeCAD.Vector(corner1.x, corner2.y, corner2.z), corner1)
            ]
            
            self.label_background.Shape = Part.makeCompound(lines)
            
            if hasattr(self.label_background, 'ViewObject'):
                self.label_background.ViewObject.LineColor = (0.9, 0.9, 0.9)
                self.label_background.ViewObject.LineWidth = 0.5
                self.label_background.ViewObject.Transparency = 50
                
        except Exception as e:
            logger.error(f"Error creating label background: {str(e)}")
    
    def clear_geometry(self):
        """Clear existing geometry objects."""
        objects_to_remove = [self.text_object, self.connection_line, self.label_background]
        
        for obj in objects_to_remove:
            if obj and hasattr(obj, 'Document') and obj.Document:
                try:
                    obj.Document.removeObject(obj.Name)
                except:
                    pass
        
        self.text_object = None
        self.connection_line = None
        self.label_background = None
    
    def reset_position(self, obj):
        """Reset label to its original position."""
        if hasattr(obj, 'OriginalPosition') and obj.OriginalPosition:
            obj.Position = obj.OriginalPosition
            obj.HasBeenMoved = False
            self.execute(obj)
    
    def set_text(self, obj, text: str):
        """Update the label text."""
        obj.LabelText = text
        self.execute(obj)
    
    def set_position(self, obj, position: FreeCAD.Vector):
        """Update the label position."""
        obj.Position = position
        if not obj.HasBeenMoved:
            obj.OriginalPosition = position
        obj.HasBeenMoved = True
        self.execute(obj)
    
    def set_connected_point(self, obj, point: FreeCAD.Vector):
        """Set the point this label is connected to."""
        obj.ConnectedPoint = point
        self.execute(obj)


class ViewProviderDraggableReactionLabel:
    """View provider for draggable reaction labels with mouse interaction."""
    
    def __init__(self, vobj):
        vobj.Proxy = self
        self.is_dragging = False
        self.drag_start_pos = None
        self.original_label_pos = None
    
    def attach(self, vobj):
        """Attach view provider to object."""
        self.ViewObject = vobj
        self.Object = vobj.Object
    
    def updateData(self, obj, prop):
        """Handle property changes."""
        if prop in ["Position", "LabelText", "ShowConnectionLine", "ConnectedPoint"]:
            if hasattr(obj, 'Proxy') and obj.Proxy:
                obj.Proxy.execute(obj)
    
    def onChanged(self, vobj, prop):
        """Handle view property changes."""
        pass
    
    def getIcon(self):
        """Return icon for the label."""
        return ":/icons/label.svg"
    
    def claimChildren(self):
        """Claim child objects (text, line, background)."""
        children = []
        if hasattr(self.Object, 'Proxy') and self.Object.Proxy:
            proxy = self.Object.Proxy
            if proxy.text_object:
                children.append(proxy.text_object)
            if proxy.connection_line:
                children.append(proxy.connection_line)
            if proxy.label_background:
                children.append(proxy.label_background)
        return children
    
    def setEdit(self, vobj, mode):
        """Enter edit mode for dragging."""
        if mode == 0:
            # Enable dragging mode
            self.start_drag_mode()
            return True
        return False
    
    def unsetEdit(self, vobj, mode):
        """Exit edit mode."""
        self.stop_drag_mode()
        return True
    
    def start_drag_mode(self):
        """Start drag interaction mode."""
        try:
            # Install event filter for mouse events
            self.event_callback = FreeCADGui.addDocumentObserver(DragEventHandler(self))
            FreeCAD.Console.PrintMessage("Label drag mode enabled. Click and drag to reposition.\n")
        except Exception as e:
            logger.error(f"Error starting drag mode: {str(e)}")
    
    def stop_drag_mode(self):
        """Stop drag interaction mode."""
        try:
            if hasattr(self, 'event_callback'):
                FreeCADGui.removeDocumentObserver(self.event_callback)
            FreeCAD.Console.PrintMessage("Label drag mode disabled.\n")
        except Exception as e:
            logger.error(f"Error stopping drag mode: {str(e)}")
    
    def handle_mouse_press(self, pos):
        """Handle mouse press for starting drag."""
        try:
            # Check if click is near the label
            if self.is_near_label(pos):
                self.is_dragging = True
                self.drag_start_pos = pos
                self.original_label_pos = self.Object.Position
                return True
        except Exception as e:
            logger.error(f"Error handling mouse press: {str(e)}")
        return False
    
    def handle_mouse_move(self, pos):
        """Handle mouse move during drag."""
        if not self.is_dragging or not self.drag_start_pos:
            return False
        
        try:
            # Calculate new position based on mouse movement
            delta = pos - self.drag_start_pos
            new_position = self.original_label_pos + FreeCAD.Vector(delta.x, delta.y, 0)
            
            # Update label position
            if hasattr(self.Object, 'Proxy') and self.Object.Proxy:
                self.Object.Proxy.set_position(self.Object, new_position)
            
            return True
            
        except Exception as e:
            logger.error(f"Error handling mouse move: {str(e)}")
        return False
    
    def handle_mouse_release(self, pos):
        """Handle mouse release to end drag."""
        if self.is_dragging:
            self.is_dragging = False
            self.drag_start_pos = None
            self.original_label_pos = None
            FreeCAD.ActiveDocument.recompute()
            return True
        return False
    
    def is_near_label(self, pos) -> bool:
        """Check if mouse position is near the label."""
        try:
            label_pos = self.Object.Position
            # Simple distance check (can be improved with proper screen projection)
            distance = (pos - label_pos).Length
            return distance < 50  # 50 units threshold
        except:
            return False


class DragEventHandler:
    """Event handler for label dragging operations."""
    
    def __init__(self, view_provider):
        self.view_provider = view_provider
    
    def slotCreatedObject(self, obj):
        """Handle object creation events."""
        pass
    
    def slotDeletedObject(self, obj):
        """Handle object deletion events."""
        pass
    
    def slotChangedObject(self, obj, prop):
        """Handle object property changes."""
        pass
    
    def slotActivateDocument(self, doc):
        """Handle document activation."""
        pass
    
    def slotRelabelDocument(self, doc):
        """Handle document relabel."""
        pass


def create_draggable_reaction_label(text: str, position: FreeCAD.Vector, 
                                  connected_point: Optional[FreeCAD.Vector] = None,
                                  font_size: int = 8,
                                  text_color: tuple = (0.0, 0.0, 0.0, 0.0)) -> FreeCAD.DocumentObject:
    """Convenience function to create a draggable reaction label."""
    try:
        # Create the label object
        label_obj = FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroupPython", "ReactionLabel")
        
        # Initialize with proxy classes
        DraggableReactionLabel(label_obj)
        ViewProviderDraggableReactionLabel(label_obj.ViewObject)
        
        # Set properties
        label_obj.LabelText = text
        label_obj.Position = position
        label_obj.OriginalPosition = position
        label_obj.FontSize = font_size
        label_obj.TextColor = text_color
        
        if connected_point:
            label_obj.ConnectedPoint = connected_point
            label_obj.ShowConnectionLine = True
        else:
            label_obj.ShowConnectionLine = False
        
        # Execute to create initial geometry
        label_obj.Proxy.execute(label_obj)
        
        return label_obj
        
    except Exception as e:
        logger.error(f"Error creating draggable reaction label: {str(e)}")
        return None


def reset_all_reaction_labels():
    """Reset all reaction labels in the document to their original positions."""
    try:
        count = 0
        for obj in FreeCAD.ActiveDocument.Objects:
            if (hasattr(obj, 'Proxy') and 
                hasattr(obj.Proxy, '__class__') and 
                'DraggableReactionLabel' in obj.Proxy.__class__.__name__):
                
                obj.Proxy.reset_position(obj)
                count += 1
        
        FreeCAD.Console.PrintMessage(f"Reset {count} reaction label positions.\n")
        FreeCAD.ActiveDocument.recompute()
        
    except Exception as e:
        logger.error(f"Error resetting reaction labels: {str(e)}")