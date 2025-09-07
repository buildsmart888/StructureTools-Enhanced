# -*- coding: utf-8 -*-
"""
Advanced Section Manager Command
คำสั่งสำหรับเปิด Advanced Section Manager GUI
"""

import FreeCAD as App
import FreeCADGui as Gui
import os

class AdvancedSectionManagerCommand:
    """Command to open Advanced Section Manager"""
    
    def __init__(self):
        pass
    
    def GetResources(self):
        # Use existing section icon as fallback
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'icons', 'advanced_section_manager.svg')
        if not os.path.exists(icon_path):
            icon_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'icons', 'section.svg')
        
        return {
            'Pixmap': icon_path,
            'MenuText': 'Advanced Section Manager',
            'ToolTip': 'Open advanced section manager with steelpy database and ArchProfile integration',
            'Accel': 'Ctrl+Shift+S'
        }
    
    def Activated(self):
        """Execute the command"""
        try:
            from ..gui.SectionManagerGUI import show_section_manager_gui
            gui = show_section_manager_gui()
            
            if gui:
                App.Console.PrintMessage("Advanced Section Manager opened successfully\n")
            else:
                App.Console.PrintWarning("Could not open Advanced Section Manager\n")
                
        except ImportError as e:
            App.Console.PrintError(f"Failed to import Advanced Section Manager: {e}\n")
            App.Console.PrintMessage("Make sure steelpy is installed: pip install steelpy\n")
        except Exception as e:
            App.Console.PrintError(f"Error opening Advanced Section Manager: {e}\n")
    
    def IsActive(self):
        """Check if command should be active"""
        return True

# Register the command
try:
    Gui.addCommand('StructureTools_AdvancedSectionManager', AdvancedSectionManagerCommand())
except Exception as e:
    App.Console.PrintError(f"Failed to register Advanced Section Manager command: {e}\n")