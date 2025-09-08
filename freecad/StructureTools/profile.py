# -*- coding: utf-8 -*-
"""
Structural Profile Command

Main command interface for creating parametric structural profiles
with advanced GUI integration and calc system support.
"""

import FreeCAD as App
import os

# Safe GUI imports
try:
    import FreeCADGui as Gui
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

# Import core components
try:
    from .objects.StructuralProfile import create_structural_profile
    from .taskpanels.ProfileTaskPanel import show_profile_task_panel
    PROFILE_SYSTEM_AVAILABLE = True
except ImportError:
    PROFILE_SYSTEM_AVAILABLE = False
    App.Console.PrintError("StructuralProfile system not available\n")

class StructuralProfileCommand:
    """Create Structural Profile command"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "resources", "icons", "profile.svg"),
            "Accel": "Ctrl+Shift+P",
            "MenuText": "Create Structural Profile",
            "ToolTip": "Create parametric 2D structural profile with section properties"
        }
    
    def Activated(self):
        """Activate command"""
        if not PROFILE_SYSTEM_AVAILABLE:
            App.Console.PrintError("StructuralProfile system not available\n")
            return
        
        # Show task panel for profile creation
        if GUI_AVAILABLE:
            success = show_profile_task_panel()
            if success:
                App.Console.PrintMessage("Profile creation panel opened\n")
            else:
                App.Console.PrintError("Failed to open profile panel\n")
        else:
            # Non-GUI fallback: create default I-beam profile
            App.Console.PrintMessage("Creating default I-beam profile...\n")
            try:
                profile = create_structural_profile("StructuralProfile_I_Beam", "I-Beam", "Custom")
                App.Console.PrintMessage(f"Created profile: {profile.Label}\n")
            except Exception as e:
                App.Console.PrintError(f"Failed to create profile: {e}\n")
    
    def IsActive(self):
        """Check if command should be active"""
        return True


class EditStructuralProfileCommand:
    """Edit existing Structural Profile command"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "resources", "icons", "profile_edit.svg"),
            "MenuText": "Edit Structural Profile",
            "ToolTip": "Edit selected structural profile"
        }
    
    def Activated(self):
        """Activate command"""
        if not PROFILE_SYSTEM_AVAILABLE or not GUI_AVAILABLE:
            App.Console.PrintError("Profile editing system not available\n")
            return
        
        # Get selected profile object
        selection = Gui.Selection.getSelection()
        if not selection:
            App.Console.PrintError("Please select a StructuralProfile to edit\n")
            return
        
        profile_obj = selection[0]
        
        # Check if it's a StructuralProfile
        if not hasattr(profile_obj, 'Proxy') or not hasattr(profile_obj.Proxy, 'Type'):
            App.Console.PrintError("Selected object is not a StructuralProfile\n")
            return
        
        if profile_obj.Proxy.Type != "StructuralProfile":
            App.Console.PrintError("Selected object is not a StructuralProfile\n")
            return
        
        # Open edit panel
        success = show_profile_task_panel(profile_obj)
        if success:
            App.Console.PrintMessage(f"Editing profile: {profile_obj.Label}\n")
        else:
            App.Console.PrintError("Failed to open profile edit panel\n")
    
    def IsActive(self):
        """Check if command should be active"""
        if not GUI_AVAILABLE:
            return False
        
        selection = Gui.Selection.getSelection()
        if len(selection) != 1:
            return False
        
        obj = selection[0]
        return (hasattr(obj, 'Proxy') and 
                hasattr(obj.Proxy, 'Type') and 
                obj.Proxy.Type == "StructuralProfile")


# Register commands
if GUI_AVAILABLE:
    Gui.addCommand('StructureTools_CreateStructuralProfile', StructuralProfileCommand())
    Gui.addCommand('StructureTools_EditProfile', EditStructuralProfileCommand())


def create_profile_from_parameters(profile_type, dimensions, name=None):
    """API function to create profile from parameters
    
    Args:
        profile_type: Type of profile ('I-Beam', 'Channel', etc.)
        dimensions: Dictionary of dimensional parameters
        name: Optional profile name
    
    Returns:
        StructuralProfile object
    """
    if not PROFILE_SYSTEM_AVAILABLE:
        raise ImportError("StructuralProfile system not available")
    
    # Create profile object
    if not name:
        name = f"StructuralProfile_{profile_type}"
    
    profile = create_structural_profile(name, profile_type, "Custom")
    
    # Apply dimensions
    for dim_name, value in dimensions.items():
        if dim_name.lower() == 'height' and hasattr(profile, 'Height'):
            profile.Height = f"{value} mm"
        elif dim_name.lower() == 'width' and hasattr(profile, 'Width'):
            profile.Width = f"{value} mm"
        elif dim_name.lower() == 'web_thickness' and hasattr(profile, 'WebThickness'):
            profile.WebThickness = f"{value} mm"
        elif dim_name.lower() == 'flange_thickness' and hasattr(profile, 'FlangeThickness'):
            profile.FlangeThickness = f"{value} mm"
        elif dim_name.lower() == 'thickness' and hasattr(profile, 'Thickness'):
            profile.Thickness = f"{value} mm"
        elif dim_name.lower() == 'diameter' and hasattr(profile, 'Diameter'):
            profile.Diameter = f"{value} mm"
        elif dim_name.lower() == 'leg1' and hasattr(profile, 'Leg1'):
            profile.Leg1 = f"{value} mm"
        elif dim_name.lower() == 'leg2' and hasattr(profile, 'Leg2'):
            profile.Leg2 = f"{value} mm"
    
    # Recompute to update properties
    App.ActiveDocument.recompute()
    
    return profile


def get_profile_properties(profile_obj):
    """Get calc-ready properties from a StructuralProfile object
    
    Args:
        profile_obj: StructuralProfile object
        
    Returns:
        Dictionary of properties for calc integration
    """
    if not hasattr(profile_obj, 'CalcProperties'):
        App.Console.PrintError("Profile object missing CalcProperties\n")
        return {}
    
    return profile_obj.CalcProperties


# Example usage and testing functions
def create_example_profiles():
    """Create example profiles for demonstration"""
    if not PROFILE_SYSTEM_AVAILABLE:
        App.Console.PrintError("StructuralProfile system not available\n")
        return
    
    if not App.ActiveDocument:
        App.newDocument("StructuralProfiles_Examples")
    
    examples = [
        {
            'name': 'W12x26_Example',
            'type': 'I-Beam',
            'dimensions': {
                'height': 311.15,  # mm
                'width': 165.1,
                'web_thickness': 6.86,
                'flange_thickness': 9.91
            }
        },
        {
            'name': 'HSS6x4x1/4_Example', 
            'type': 'HSS Rectangular',
            'dimensions': {
                'height': 152.4,  # mm
                'width': 101.6,
                'thickness': 6.35
            }
        },
        {
            'name': 'HSS4.000x0.250_Example',
            'type': 'HSS Circular',
            'dimensions': {
                'diameter': 101.6,  # mm
                'thickness': 6.35
            }
        },
        {
            'name': 'C8x11.5_Example',
            'type': 'Channel',
            'dimensions': {
                'height': 203.2,  # mm
                'width': 58.7,
                'web_thickness': 6.35,
                'flange_thickness': 9.65
            }
        },
        {
            'name': 'L4x4x1/2_Example',
            'type': 'Angle',
            'dimensions': {
                'leg1': 101.6,  # mm
                'leg2': 101.6,
                'thickness': 12.7
            }
        }
    ]
    
    created_profiles = []
    
    for example in examples:
        try:
            profile = create_profile_from_parameters(
                example['type'], 
                example['dimensions'], 
                example['name']
            )
            created_profiles.append(profile)
            App.Console.PrintMessage(f"Created example: {profile.Label}\n")
            
            # Print calc properties for verification
            calc_props = get_profile_properties(profile)
            if calc_props:
                App.Console.PrintMessage(f"  Area: {calc_props.get('Area', 0):.6f} m²\n")
                App.Console.PrintMessage(f"  Iy: {calc_props.get('Iy', 0):.9f} m⁴\n")
                App.Console.PrintMessage(f"  Weight: {calc_props.get('Weight', 0):.2f} kg/m\n")
            
        except Exception as e:
            App.Console.PrintError(f"Failed to create {example['name']}: {e}\n")
    
    # Arrange profiles in a grid for better visualization
    if GUI_AVAILABLE and created_profiles:
        try:
            spacing = 500  # mm spacing between profiles
            for i, profile in enumerate(created_profiles):
                x_pos = (i % 3) * spacing
                y_pos = (i // 3) * spacing
                profile.Placement.Base = App.Vector(x_pos, y_pos, 0)
            
            App.ActiveDocument.recompute()
            Gui.SendMsgToActiveView("ViewFit")
            
            App.Console.PrintMessage(f"Created {len(created_profiles)} example profiles\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error arranging profiles: {e}\n")
    
    return created_profiles


if __name__ == "__main__":
    # Test profile creation when run directly
    App.Console.PrintMessage("Testing StructuralProfile system...\n")
    create_example_profiles()