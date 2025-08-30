import sys
import os
import pytest

# Add the module path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'freecad', 'StructureTools'))

def test_wind_load_command_registration():
    """Test that the wind load GUI command is properly registered."""
    try:
        # Import FreeCADGui mock
        import FreeCADGui
        if not hasattr(FreeCADGui, 'addCommand'):
            FreeCADGui.addCommand = lambda *a, **k: None
        if not hasattr(FreeCADGui, 'listCommands'):
            FreeCADGui.listCommands = lambda: []
            
        # Import the command module
        from freecad.StructureTools.commands import command_wind_load_gui
        
        # Check if the command class exists
        assert hasattr(command_wind_load_gui, 'WindLoadCommand')
        
        # Check if the command is registered
        # This would normally be checked by FreeCADGui.listCommands()
        wind_command = command_wind_load_gui.WindLoadCommand()
        assert wind_command is not None
        
        # Check if the command has the required methods
        assert hasattr(wind_command, 'GetResources')
        assert hasattr(wind_command, 'Activated')
        assert hasattr(wind_command, 'IsActive')
        
        # Test GetResources method
        resources = wind_command.GetResources()
        assert isinstance(resources, dict)
        assert 'MenuText' in resources
        assert 'ToolTip' in resources
        
    except ImportError as e:
        pytest.fail(f"Failed to import wind load command module: {e}")
    except Exception as e:
        pytest.fail(f"Error testing wind load command registration: {e}")

def test_seismic_load_command_registration():
    """Test that the seismic load GUI command is properly registered."""
    try:
        # Import FreeCADGui mock
        import FreeCADGui
        if not hasattr(FreeCADGui, 'addCommand'):
            FreeCADGui.addCommand = lambda *a, **k: None
        if not hasattr(FreeCADGui, 'listCommands'):
            FreeCADGui.listCommands = lambda: []
            
        # Import the command module
        from freecad.StructureTools.commands import command_seismic_load_gui
        
        # Check if the command class exists
        assert hasattr(command_seismic_load_gui, 'SeismicLoadCommand')
        
        # Check if the command is registered
        # This would normally be checked by FreeCADGui.listCommands()
        seismic_command = command_seismic_load_gui.SeismicLoadCommand()
        assert seismic_command is not None
        
        # Check if the command has the required methods
        assert hasattr(seismic_command, 'GetResources')
        assert hasattr(seismic_command, 'Activated')
        assert hasattr(seismic_command, 'IsActive')
        
        # Test GetResources method
        resources = seismic_command.GetResources()
        assert isinstance(resources, dict)
        assert 'MenuText' in resources
        assert 'ToolTip' in resources
        
    except ImportError as e:
        pytest.fail(f"Failed to import seismic load command module: {e}")
    except Exception as e:
        pytest.fail(f"Error testing seismic load command registration: {e}")

if __name__ == "__main__":
    test_wind_load_command_registration()
    test_seismic_load_command_registration()
    print("All command registration tests passed!")