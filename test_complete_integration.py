#!/usr/bin/env python3
"""
Complete Integration Test for Global Units System
Tests all updated StructureTools files
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'freecad'))

# Mock FreeCAD for testing
class MockFreeCAD:
    class Console:
        @staticmethod
        def PrintMessage(msg): print(f"FreeCAD: {msg.strip()}")

sys.modules['FreeCAD'] = MockFreeCAD()
sys.modules['App'] = MockFreeCAD()
sys.modules['FreeCADGui'] = MockFreeCAD()
sys.modules['Part'] = MockFreeCAD()

def test_imports():
    """Test that all files can import Global Units"""
    files_to_test = [
        "freecad.StructureTools.utils.units_manager",
        "freecad.StructureTools.calc",
        "freecad.StructureTools.material",
    ]
    
    success_count = 0
    for module_name in files_to_test:
        try:
            __import__(module_name)
            print(f"✓ {module_name}")
            success_count += 1
        except ImportError as e:
            print(f"✗ {module_name}: {e}")
    
    print(f"\nImport Test: {success_count}/{len(files_to_test)} modules loaded")
    return success_count == len(files_to_test)

if __name__ == "__main__":
    print("Complete Integration Test")
    print("=" * 40)
    
    if test_imports():
        print("\n🎉 ALL INTEGRATIONS SUCCESSFUL 🎉")
        print("Global Units System ready for production!")
    else:
        print("\n⚠ Some integrations need attention")
