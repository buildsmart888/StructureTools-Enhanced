#!/usr/bin/env python3
"""
Test script to simulate the original error scenario.
"""

import sys
import os
import traceback

# Add the module path to sys.path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
sys.path.insert(0, module_path)

def test_connect_signals_without_buttons():
    """Test calling connect_signals when buttons don't exist."""
    try:
        # Import the SeismicLoadGUI class
        from commands.command_seismic_load_gui import SeismicLoadGUI
        
        # Create a GUI instance
        gui = SeismicLoadGUI()
        
        # Remove one of the buttons to simulate an error condition
        if hasattr(gui, 'calculate_btn'):
            delattr(gui, 'calculate_btn')
        
        # Try to call connect_signals - this should not fail with our fix
        gui.connect_signals()
        print("✅ connect_signals handled missing button gracefully")
        return True
        
    except AttributeError as e:
        if "connect_signals" in str(e):
            print(f"❌ FAILED: connect_signals method missing: {e}")
            return False
        else:
            print(f"❌ FAILED with AttributeError: {e}")
            traceback.print_exc()
            return False
    except Exception as e:
        print(f"❌ FAILED with unexpected error: {e}")
        traceback.print_exc()
        return False

def test_original_error_scenario():
    """Test the original error scenario by creating a partial GUI."""
    try:
        # Import necessary classes
        from commands.command_seismic_load_gui import SeismicLoadGUI
        
        # Create an instance and manually call parts of the initialization
        # to simulate the error condition
        gui = SeismicLoadGUI()
        
        # Simulate a scenario where setup_ui fails partway through
        # Remove some buttons but not others
        if hasattr(gui, 'calculate_btn'):
            delattr(gui, 'calculate_btn')
            
        # Now try to call connect_signals - with our fix, this should not fail
        gui.connect_signals()
        print("✅ connect_signals handled partial button creation gracefully")
        return True
        
    except Exception as e:
        print(f"❌ FAILED with error: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing error scenarios...")
    
    print("\n1. Testing connect_signals with missing buttons...")
    success1 = test_connect_signals_without_buttons()
    
    print("\n2. Testing original error scenario...")
    success2 = test_original_error_scenario()
    
    if success1 and success2:
        print("\n🎉 All error scenario tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Some tests failed!")
        sys.exit(1)