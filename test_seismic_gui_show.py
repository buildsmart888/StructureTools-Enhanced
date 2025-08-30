#!/usr/bin/env python3
"""
Test script to verify that the SeismicLoadGUI can be shown without errors.
"""

import sys
import os
import traceback

# Add the module path to sys.path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
sys.path.insert(0, module_path)

def test_seismic_gui_show():
    """Test that SeismicLoadGUI can be shown without errors."""
    try:
        # Import the show_seismic_load_gui function
        from commands.command_seismic_load_gui import show_seismic_load_gui
        
        # Try to show the GUI
        print("Showing SeismicLoadGUI...")
        dialog = show_seismic_load_gui()
        
        if dialog:
            print("✅ SeismicLoadGUI shown successfully!")
            return True
        else:
            print("❌ SeismicLoadGUI failed to show!")
            return False
            
    except AttributeError as e:
        if "connect_signals" in str(e):
            print(f"❌ FAILED with connect_signals error: {e}")
            traceback.print_exc()
            return False
        else:
            print(f"❌ FAILED with different AttributeError: {e}")
            traceback.print_exc()
            return False
    except Exception as e:
        print(f"❌ FAILED with unexpected error: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing SeismicLoadGUI show functionality...")
    success = test_seismic_gui_show()
    if success:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Tests failed!")
        sys.exit(1)