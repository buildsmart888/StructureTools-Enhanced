import FreeCAD, FreeCADGui
import os

# Prefer PySide2 when available
try:
    from PySide2 import QtWidgets
except ImportError:
    try:
        from PySide import QtWidgets
    except ImportError as e:
        raise ImportError("Neither PySide2 nor PySide could be imported. Please install one of them.") from e

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")


class CommandViewReactionTable:
    """Command to view reaction results for any existing calc object."""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(ICONPATH, "reaction_table.svg"),  # Use existing icon or create one
            'MenuText': "View Reaction Table", 
            'ToolTip': "View reaction forces and moments from existing calculation in a table format"
        }
    
    def Activated(self):
        try:
            # Check if a calculation object is selected
            selection = FreeCADGui.Selection.getSelection()
            calc_obj = None
            
            for obj in selection:
                if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                    if 'Calc' in obj.Proxy.__class__.__name__:
                        calc_obj = obj
                        break
            
            if not calc_obj:
                # Try to find calc object in document
                for obj in FreeCAD.ActiveDocument.Objects:
                    if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                        if 'Calc' in obj.Proxy.__class__.__name__:
                            calc_obj = obj
                            break
            
            if not calc_obj:
                QtWidgets.QMessageBox.warning(None, "Warning", 
                    "Please select a calculation object first.")
                return
            
            # Check if analysis data exists
            model_available = False
            if hasattr(calc_obj, 'model') and calc_obj.model:
                model_available = True
            elif hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                model_available = True
            elif hasattr(calc_obj, 'Proxy') and hasattr(calc_obj.Proxy, 'model') and calc_obj.Proxy.model:
                model_available = True
            
            if not model_available:
                QtWidgets.QMessageBox.warning(None, "Warning", 
                    "No analysis data found in the calculation object.")
                return
                
            # First try to find existing reaction results object
            reaction_obj = None
            for obj in FreeCAD.ActiveDocument.Objects:
                if (hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__') and 
                    'ReactionResults' in obj.Proxy.__class__.__name__):
                    if hasattr(obj, 'ObjectBaseCalc') and obj.ObjectBaseCalc == calc_obj:
                        reaction_obj = obj
                        break
            
            # Create reaction results object if not found
            if not reaction_obj:
                from freecad.StructureTools.reaction_results import ReactionResults, ViewProviderReactionResults
                FreeCAD.Console.PrintMessage("Creating new reaction results object...\n")
                reaction_obj = FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroupPython", "ReactionResults")
                ReactionResults(reaction_obj, calc_obj)
                ViewProviderReactionResults(reaction_obj.ViewObject)
                FreeCAD.ActiveDocument.recompute()
            
            # Open the reaction table panel
            from freecad.StructureTools.reaction_table_panel import ReactionTablePanel
            panel = ReactionTablePanel(reaction_obj)
            FreeCADGui.Control.showDialog(panel)
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error displaying reaction table: {str(e)}\n")
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to display reaction table: {str(e)}")
    
    def IsActive(self):
        return FreeCAD.ActiveDocument is not None


# Register the command
if hasattr(FreeCADGui, 'addCommand'):
    FreeCADGui.addCommand('ViewReactionTable', CommandViewReactionTable())