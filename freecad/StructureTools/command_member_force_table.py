"""
Command to open Member Force Summary panel.

Registers the toolbar command for viewing beam force detail summary.
"""

import FreeCAD
import FreeCADGui
import os

# PySide imports
try:
    from .qt_compat import QtWidgets
except ImportError:
    try:
        from PySide import QtWidgets
    except ImportError:
        QtWidgets = None

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")


class CommandMemberForceTable:
    """Command to view member force summary table."""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(ICONPATH, "beam_force.svg"),
            'MenuText': "View Member Force Summary",
            'ToolTip': "View maximum and minimum member forces in a table format"
        }
    
    def Activated(self):
        """Execute when command is activated."""
        try:
            # Find calc object
            calc_obj = self._find_calc_object()
            
            if not calc_obj:
                QtWidgets.QMessageBox.warning(
                    None, "No Calculation Found",
                    "No calculation object found.\n\n"
                    "Please:\n"
                    "1. Create a structural model with members\n"
                    "2. Run the Calc command to analyze\n"
                    "3. Then use this command to view results"
                )
                return
            
            # Check if model has analysis results
            model = None
            if hasattr(calc_obj, 'model') and calc_obj.model:
                model = calc_obj.model
            elif hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                model = calc_obj.FEModel
            elif hasattr(calc_obj, 'Proxy') and hasattr(calc_obj.Proxy, 'model'):
                model = calc_obj.Proxy.model
            
            if not model:
                QtWidgets.QMessageBox.warning(
                    None, "No Analysis Results",
                    "No analysis results found in the calculation object.\n\n"
                    "Please run the Calc command first to analyze the model."
                )
                return
            
            # Open the panel
            from .member_force_panel import MemberForcePanel
            panel = MemberForcePanel(calc_obj)
            FreeCADGui.Control.showDialog(panel)
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error opening member force panel: {str(e)}\n")
            if QtWidgets:
                QtWidgets.QMessageBox.critical(
                    None, "Error", 
                    f"Failed to open member force panel:\n{str(e)}"
                )
    
    def _find_calc_object(self):
        """Find a calc object in the document."""
        if not FreeCAD.ActiveDocument:
            return None
        
        # First check selection
        selection = FreeCADGui.Selection.getSelection()
        for obj in selection:
            if self._is_calc_object(obj):
                return obj
        
        # Then search document
        for obj in FreeCAD.ActiveDocument.Objects:
            if self._is_calc_object(obj):
                return obj
        
        return None
    
    def _is_calc_object(self, obj):
        """Check if object is a Calc object."""
        if hasattr(obj, 'Proxy') and obj.Proxy:
            if hasattr(obj.Proxy, '__class__'):
                class_name = obj.Proxy.__class__.__name__
                if 'Calc' in class_name:
                    return True
        return False
    
    def IsActive(self):
        """Check if command should be active."""
        return FreeCAD.ActiveDocument is not None


# Register the command
if hasattr(FreeCADGui, 'addCommand'):
    FreeCADGui.addCommand('ViewMemberForceSummary', CommandMemberForceTable())
