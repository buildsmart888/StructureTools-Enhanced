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

# Try to import our modified module
try:
    from freecad.StructureTools.load_distributed import LoadDistributed
    print("LoadDistributed class imported successfully")
except ImportError as e:
    print(f"Failed to import LoadDistributed: {e}")

# Test the functionality if FreeCAD is available
if FREECAD_AVAILABLE:
    try:
        # Create a simple line for testing
        doc = App.newDocument()
        
        # Create a line
        line = doc.addObject("Part::Feature", "Line")
        line.Shape = Part.makeLine(App.Vector(0, 0, 0), App.Vector(1000, 0, 0))
        
        # Create a distributed load
        load_obj = doc.addObject("Part::FeaturePython", "TestLoad")
        
        # Create LoadDistributed instance
        load = LoadDistributed(load_obj, (line, "Edge1"))
        
        # Test setting start and end positions
        load_obj.StartPosition = 200.0  # Start 200mm from beginning
        load_obj.EndPosition = 800.0    # End 800mm from beginning
        
        print("Load object created successfully with start/end positions")
        print(f"StartPosition: {load_obj.StartPosition}")
        print(f"EndPosition: {load_obj.EndPosition}")
        
        # Clean up
        App.closeDocument(doc.Name)
        
    except Exception as e:
        print(f"Error testing LoadDistributed: {e}")
        import traceback
        traceback.print_exc()

print("Test completed")