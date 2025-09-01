import sys
import os

# Add the StructureTools path to sys.path
structure_tools_path = r"c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools"
if structure_tools_path not in sys.path:
    sys.path.append(structure_tools_path)

# Try to import FreeCAD modules
try:
    import FreeCAD as App
    import FreeCADGui
    import Part
    FREECAD_AVAILABLE = True
    print("FreeCAD modules imported successfully")
except ImportError as e:
    print(f"Failed to import FreeCAD modules: {e}")
    FREECAD_AVAILABLE = False

# Try to import our new module
try:
    from freecad.StructureTools.load_point import LoadPoint
    print("LoadPoint class imported successfully")
except ImportError as e:
    print(f"Failed to import LoadPoint: {e}")

# Test the functionality if FreeCAD is available
if FREECAD_AVAILABLE:
    try:
        # Create a simple line for testing
        doc = App.newDocument()
        
        # Create a line
        line = doc.addObject("Part::Feature", "Line")
        line.Shape = Part.makeLine(App.Vector(0, 0, 0), App.Vector(1000, 0, 0))
        
        # Create a point load
        load_obj = doc.addObject("Part::FeaturePython", "TestPointLoad")
        
        # Create LoadPoint instance
        load = LoadPoint(load_obj, (line, "Edge1"))
        
        # Test setting position
        load_obj.RelativePosition = 0.3  # 30% along the member
        load_obj.PointLoading = 5000000  # 5000 kN
        
        print("Point load object created successfully with position and force")
        print(f"RelativePosition: {load_obj.RelativePosition}")
        print(f"PointLoading: {load_obj.PointLoading}")
        
        # Clean up
        App.closeDocument(doc.Name)
        
    except Exception as e:
        print(f"Error testing LoadPoint: {e}")
        import traceback
        traceback.print_exc()

print("Point load test completed")