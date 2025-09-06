import FreeCAD, FreeCADGui
import os
from typing import List, Any

# Prefer PySide2 when available
try:
    from PySide2 import QtWidgets, QtCore, QtGui
except ImportError:
    try:
        from PySide import QtWidgets, QtCore, QtGui
    except ImportError as e:
        raise ImportError("Neither PySide2 nor PySide could be imported. Please install one of them.") from e

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")


class CommandTextVisualization:
    """Command to show text-based visualization of reaction forces and moments."""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(ICONPATH, "reaction.svg"),
            'MenuText': "Text Visualization", 
            'ToolTip': "Display reaction forces and moments as text-based visualization"
        }
    
    def Activated(self):
        try:
            # Check if a reaction results object is selected
            selection = FreeCADGui.Selection.getSelection()
            reaction_obj = None
            
            # First, try to find a reaction results object in selection
            for obj in selection:
                if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                    if 'ReactionResults' in obj.Proxy.__class__.__name__:
                        reaction_obj = obj
                        break
            
            # If no reaction object found in selection, try to find one in document
            if not reaction_obj:
                for obj in FreeCAD.ActiveDocument.Objects:
                    if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                        if 'ReactionResults' in obj.Proxy.__class__.__name__:
                            reaction_obj = obj
                            break
            
            if not reaction_obj:
                QtWidgets.QMessageBox.warning(None, "Warning", 
                    "Please select or create a reaction results object first.")
                return
            
            # Show text-based visualization
            if hasattr(reaction_obj, 'Proxy') and reaction_obj.Proxy:
                reaction_obj.Proxy.create_text_based_visualization(reaction_obj)
                FreeCAD.Console.PrintMessage("Text-based visualization displayed in FreeCAD console.\n")
            else:
                FreeCAD.Console.PrintError("ReactionResults proxy not found\n")
                
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error showing text visualization: {str(e)}\n")
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to show text visualization: {str(e)}")
    
    def IsActive(self):
        return FreeCAD.ActiveDocument is not None


# Register the command
if hasattr(FreeCADGui, 'addCommand'):
    FreeCADGui.addCommand('TextVisualization', CommandTextVisualization())