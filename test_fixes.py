#!/usr/bin/env python3
"""
Test script to verify that the fixes for plate and area load objects work correctly.
"""

import sys
import os

# Setup repo path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
freecad_dir = os.path.join(repo_root, 'freecad')
if freecad_dir not in sys.path:
    sys.path.insert(0, freecad_dir)

try:
    import FreeCAD as App
    import Part
    from freecad.StructureTools.objects.StructuralPlate import StructuralPlate
    from freecad.StructureTools.objects.AreaLoad import AreaLoad
    print("SUCCESS: All modules imported successfully")
except ImportError as e:
    print(f"ERROR: Failed to import modules: {e}")
    sys.exit(1)

def test_plate_creation():
    """Test that we can create a plate object without errors."""
    try:
        # Create a new document
        doc = App.newDocument("TestPlate")
        
        # Create a simple rectangular face
        rect = Part.makePlane(1000, 500, App.Vector(0, 0, 0))  # 1m x 0.5m plate
        
        # Create a plate object
        plate = doc.addObject("App::FeaturePython", "TestPlate")
        StructuralPlate(plate)
        
        # Set plate properties
        plate.Thickness = "20 mm"
        plate.PlateType = "Thin Plate"
        
        # Recompute the document
        doc.recompute()
        
        print("SUCCESS: Plate creation test passed")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to create plate: {e}")
        return False

def test_area_load_creation():
    """Test that we can create an area load object without errors."""
    try:
        # Create a new document
        doc = App.newDocument("TestAreaLoad")
        
        # Create an area load object
        area_load = doc.addObject("App::FeaturePython", "TestAreaLoad")
        AreaLoad(area_load)
        
        # Set area load properties
        area_load.LoadIntensity = "5.0 kN/m^2"
        area_load.Direction = "-Z Global"
        area_load.LoadDistribution = "TwoWay"
        
        # Recompute the document
        doc.recompute()
        
        print("SUCCESS: Area load creation test passed")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to create area load: {e}")
        return False

def main():
    """Run the tests."""
    print("Testing fixes for plate and area load objects...")
    print("=" * 50)
    
    plate_success = test_plate_creation()
    area_load_success = test_area_load_creation()
    
    if plate_success and area_load_success:
        print("✓ All tests PASSED! The fixes are working correctly.")
        return 0
    else:
        print("✗ Some tests FAILED! Please check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
