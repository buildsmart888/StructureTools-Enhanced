#!/usr/bin/env python3
"""
Detailed test script to verify that the SeismicLoadGUI can be instantiated 
and that all signals are properly connected.
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
        print("Creating SeismicLoadGUI instance...")
        gui = SeismicLoadGUI()
        print("✅ SeismicLoadGUI instantiated successfully!")
        
        # Check if connect_signals method exists
        if hasattr(gui, 'connect_signals'):
            print("✅ The 'connect_signals' method is properly defined.")
        else:
            print("❌ The 'connect_signals' method is missing!")
            return False
            
        # Check if all the main action buttons exist
        buttons = ['calculate_btn', 'spectrum_btn', 'apply_btn', 'analyze_btn', 'close_btn']
        for button in buttons:
            if hasattr(gui, button):
                print(f"✅ Button '{button}' exists")
            else:
                print(f"❌ Button '{button}' is missing!")
                return False
                
        # Try to call connect_signals method directly
        try:
            gui.connect_signals()
            print("✅ connect_signals method executed without errors")
        except Exception as e:
            print(f"❌ Error calling connect_signals method: {e}")
            traceback.print_exc()
            return False
            
        return True
    except AttributeError as e:
        print(f"❌ FAILED with AttributeError: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"❌ FAILED with unexpected error: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing SeismicLoadGUI instantiation and signal connections...")
    success = test_seismic_gui_instantiation()
    if success:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Tests failed!")
        sys.exit(1)