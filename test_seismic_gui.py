#!/usr/bin/env python3
"""
Test script to verify that the SeismicLoadGUI can be instantiated 
without the 'connect_signals' error.
"""

import sys
import os
import traceback

# Add the module path to sys.path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
sys.path.insert(0, module_path)

def test_seismic_gui_instantiation():
    """Test that SeismicLoadGUI can be instantiated without errors."""
    try:
        # Import the SeismicLoadGUI class
        from commands.command_seismic_load_gui import SeismicLoadGUI
        
        # Try to instantiate the class
        # We're not actually showing the GUI, just testing instantiation
        gui = SeismicLoadGUI()
        print("✅ SeismicLoadGUI instantiated successfully!")
        print("✅ The 'connect_signals' method is properly defined.")
        return True
    except AttributeError as e:
        if "connect_signals" in str(e):
            print(f"❌ FAILED: {e}")
            print("❌ The 'connect_signals' method is still not properly defined.")
            traceback.print_exc()
            return False
        elif "stateChanged" in str(e):
            print(f"❌ FAILED: {e}")
            print("❌ There's still an issue with the QCheckBox mock class.")
            traceback.print_exc()
            return False
        elif "calculate_btn" in str(e):
            print(f"❌ FAILED: {e}")
            print("❌ There's still an issue with the button creation.")
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
    print("Testing SeismicLoadGUI instantiation...")
    success = test_seismic_gui_instantiation()
    if success:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Tests failed!")
        sys.exit(1)