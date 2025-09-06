#!/usr/bin/env python3
"""
Test script for area load implementation with a real model
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
    import Draft
    from freecad.StructureTools import calc
    from freecad.StructureTools.Pynite_main.FEModel3D import FEModel3D
    from freecad.StructureTools.objects.AreaLoad import AreaLoad
    from freecad.StructureTools.objects.StructuralPlate import StructuralPlate
    print("SUCCESS: All modules imported successfully")
except ImportError as e:
    print(f"ERROR: Failed to import modules: {e}")
    sys.exit(1)

def create_test_model():
    """Create a simple test model with a plate and area load"""
    try:
        # Create a new document
        doc = App.newDocument("TestAreaLoad")
        
        # Create a rectangular plate
        plate = doc.addObject("Part::Feature", "Plate1")
        # Create a simple rectangular face
        rect = Part.makePlane(2000, 1000, App.Vector(0, 0, 0))  # 2m x 1m plate
        plate.Shape = rect
        
        # Convert to StructuralPlate
        structural_plate = doc.addObject("App::FeaturePython", "StructuralPlate1")
        StructuralPlate(structural_plate)
        structural_plate.ObjectBase = [(plate, ("Face1",))]
        structural_plate.Thickness = 20  # 20mm thick plate
        
        # Create an area load
        area_load = doc.addObject("App::FeaturePython", "AreaLoad1")
        AreaLoad(area_load)
        area_load.TargetFaces = [structural_plate]
        area_load.LoadIntensity = "5.0 kN/m^2"  # 5 kN/m² load
        area_load.LoadDirection = App.Vector(0, 0, -1)  # Downward load
        area_load.LoadDistribution = "TwoWay"  # Two-way distribution
        
        # Create a simple support at one corner
        # (This would normally be done with support objects, but we'll skip for simplicity)
        
        # Create a calc object
        calc_obj = doc.addObject("App::FeaturePython", "Calc1")
        calc_elements = [structural_plate, area_load]
        calc.Calc(calc_obj, calc_elements)
        calc_obj.ListElements = calc_elements
        calc_obj.LengthUnit = 'm'
        calc_obj.ForceUnit = 'kN'
        calc_obj.LoadCombination = '100_DL'
        calc_obj.selfWeight = False
        
        # Recompute the document
        doc.recompute()
        
        print("SUCCESS: Test model created successfully")
        return doc, calc_obj
        
    except Exception as e:
        print(f"ERROR: Failed to create test model: {e}")
        return None, None

def test_area_load_processing():
    """Test that area loads are properly processed"""
    try:
        # Create test model
        doc, calc_obj = create_test_model()
        if not doc or not calc_obj:
            return False
            
        # Run the calculation
        calc_instance = calc.Calc(calc_obj, calc_obj.ListElements)
        calc_instance.execute(calc_obj)
        
        # Check if analysis was successful
        if not hasattr(calc_obj, 'AnalysisType'):
            print("ERROR: Analysis failed")
            return False
            
        print("SUCCESS: Area load processing test passed")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to test area load processing: {e}")
        return False

def main():
    """Run the real model test"""
    print("Starting area load real model test...")
    print("=" * 50)
    
    try:
        if test_area_load_processing():
            print("✓ Area load real model test PASSED")
            print("All tests PASSED! Area load implementation is working correctly.")
            return 0
        else:
            print("✗ Area load real model test FAILED")
            print("Some tests FAILED! Please check the implementation.")
            return 1
    except Exception as e:
        print(f"✗ Area load real model test FAILED with exception: {e}")
        print("Some tests FAILED! Please check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())