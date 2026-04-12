
import FreeCAD
import FreeCADGui
import os

ICONPATH = os.path.join(os.path.dirname(__file__), "..", "resources")

class CommandShowDesign:
    """
    Command to visualize design check results (Pass/Fail) on the 3D model.
    Colors members based on their utilization ratio.
    """
    
    def GetResources(self):
        # Use existing icon temporarily
        icon_path = os.path.join(ICONPATH, "icons/bim_status.svg")
        if not os.path.exists(icon_path):
             icon_path = os.path.join(ICONPATH, "icons/diagram.svg")
             
        return {
            "Pixmap": icon_path, 
            "MenuText": "Show Design Status",
            "ToolTip": "Colorize members based on design utilization ratio (Green=Pass, Red=Fail)",
            "Accel": "Shift+D"
        }

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        if not doc:
            return

        # Open transaction
        doc.openTransaction("Show Design Status")
        
        count = 0
        for obj in doc.Objects:
            # Check if object has design results
            if hasattr(obj, 'DesignRatio') or hasattr(obj, 'MaxUtilization'):
                
                # Get max ratio
                ratio = 0.0
                if hasattr(obj, 'MaxUtilization'):
                    ratio = float(obj.MaxUtilization)
                elif hasattr(obj, 'DesignRatio'):
                    ratio = float(obj.DesignRatio)
                
                # Determine Color
                # Green: < 0.8
                # Yellow: 0.8 - 1.0
                # Red: > 1.0 (Fail)
                # Blue: 0.0 (No calc or pass very safe)
                
                if ratio > 1.0:
                    color = (1.0, 0.0, 0.0) # Red
                elif ratio > 0.8:
                    color = (1.0, 1.0, 0.0) # Yellow
                elif ratio > 0.0:
                    color = (0.0, 1.0, 0.0) # Green
                else:
                    color = (0.7, 0.7, 0.7) # Grey/Default
                
                # Apply Color
                if hasattr(obj, 'ViewObject'):
                    # Save original color if not saved? (Optional enhancement)
                    obj.ViewObject.ShapeColor = color
                    
                    # Also try to update StructuralBeam specific display mode if applicable
                    if hasattr(obj.ViewObject, 'ResultsDisplay'):
                         obj.ViewObject.ResultsDisplay = "Utilization"
                    
                count += 1

        doc.commitTransaction()
        FreeCAD.Console.PrintMessage(f"Updated design visualization for {count} members.\n")
        doc.recompute()

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None

if __name__ == "__main__":
    # For testing in console
    cmd = CommandShowDesign()
    if cmd.IsActive():
        cmd.Activated()

FreeCADGui.addCommand('ShowDesignStatus', CommandShowDesign())
