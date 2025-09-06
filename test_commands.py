"""
Test script to verify command registration in FreeCAD.
This script should be run from within FreeCAD's Python console.
"""

import sys
import os

# Add the module path
mod_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "FreeCAD", "Mod", "StructureTools")
if mod_path not in sys.path:
    sys.path.append(mod_path)

def test_command_registration():
    """Test that the wind and seismic load commands are properly registered."""
    try:
        import FreeCADGui as Gui
        
        # List all available commands
        commands = Gui.listCommands()
        
        # Check if our commands are registered
        wind_command_found = "wind_load_gui" in commands
        seismic_command_found = "seismic_load_gui" in commands
        
        print("Command Registration Test Results:")
        print(f"Wind Load GUI Command: {'✅ FOUND' if wind_command_found else '❌ NOT FOUND'}")
        print(f"Seismic Load GUI Command: {'✅ FOUND' if seismic_command_found else '❌ NOT FOUND'}")
        
        if wind_command_found:
            print("\nWind Load GUI Command Resources:")
            try:
                cmd = Gui.Command.get("wind_load_gui")
                resources = cmd.GetResources()
                print(f"  Pixmap: {resources.get('Pixmap', 'Not set')}")
                print(f"  MenuText: {resources.get('MenuText', 'Not set')}")
                print(f"  ToolTip: {resources.get('ToolTip', 'Not set')}")
            except Exception as e:
                print(f"  Error getting resources: {e}")
        
        if seismic_command_found:
            print("\nSeismic Load GUI Command Resources:")
            try:
                cmd = Gui.Command.get("seismic_load_gui")
                resources = cmd.GetResources()
                print(f"  Pixmap: {resources.get('Pixmap', 'Not set')}")
                print(f"  MenuText: {resources.get('MenuText', 'Not set')}")
                print(f"  ToolTip: {resources.get('ToolTip', 'Not set')}")
            except Exception as e:
                print(f"  Error getting resources: {e}")
        
        return wind_command_found and seismic_command_found
        
    except Exception as e:
        print(f"Error during command registration test: {e}")
        return False

def test_icon_paths():
    """Test that the icon paths are correct."""
    try:
        from freecad.StructureTools.commands import command_wind_load_gui, command_seismic_load_gui
        
        # Get the icon paths from the commands
        wind_resources = command_wind_load_gui.WindLoadCommand().GetResources()
        seismic_resources = command_seismic_load_gui.SeismicLoadCommand().GetResources()
        
        wind_icon_path = wind_resources.get('Pixmap', '')
        seismic_icon_path = seismic_resources.get('Pixmap', '')
        
        print("\nIcon Path Test Results:")
        print(f"Wind Load Icon Path: {wind_icon_path}")
        print(f"Seismic Load Icon Path: {seismic_icon_path}")
        
        # Check if files exist
        wind_icon_exists = os.path.exists(wind_icon_path) if wind_icon_path else False
        seismic_icon_exists = os.path.exists(seismic_icon_path) if seismic_icon_path else False
        
        print(f"Wind Load Icon File: {'✅ EXISTS' if wind_icon_exists else '❌ NOT FOUND'}")
        print(f"Seismic Load Icon File: {'✅ EXISTS' if seismic_icon_exists else '❌ NOT FOUND'}")
        
        return wind_icon_exists and seismic_icon_exists
        
    except Exception as e:
        print(f"Error during icon path test: {e}")
        return False

if __name__ == "__main__":
    print("Running StructureTools Command Tests...\n")
    
    # Test command registration
    commands_ok = test_command_registration()
    
    # Test icon paths
    icons_ok = test_icon_paths()
    
    print("\n" + "="*50)
    print("TEST SUMMARY:")
    print(f"Command Registration: {'✅ PASS' if commands_ok else '❌ FAIL'}")
    print(f"Icon Paths: {'✅ PASS' if icons_ok else '❌ FAIL'}")
    print(f"Overall: {'✅ ALL TESTS PASS' if commands_ok and icons_ok else '❌ SOME TESTS FAIL'}")
    print("="*50)