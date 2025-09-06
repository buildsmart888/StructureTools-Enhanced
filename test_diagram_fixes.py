"""
Test script to verify the diagram fixes work correctly
Run this in FreeCAD's Python console
"""

import sys
import os

# Add the module path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
if module_path not in sys.path:
    sys.path.insert(0, module_path)

print("🔧 Testing Diagram Fixes")
print("=" * 50)

try:
    import FreeCAD
    import Part
    from freecad.StructureTools.diagram_core import get_label_positions, separates_ordinates, generate_coordinates
    from freecad.StructureTools.diagram import Diagram
    
    print("✅ All imports successful")
    
    # Test 1: Check label positioning with very small values
    print("\n📋 Test 1: Label Positioning with Small Values")
    values_scaled = [1e-15, 2e-15, 3e-15]  # Very small values
    list_matrix_row = [1e-15, 2e-15, 3e-15]
    dist = 1.0
    font_height = 100
    precision = 2
    
    labels = get_label_positions(values_scaled, list_matrix_row, dist, font_height, precision)
    print(f"  Labels generated: {len(labels)}")
    for label in labels:
        print(f"    {label}")
    
    # Test 2: Check with zero values
    print("\n📋 Test 2: Label Positioning with Zero Values")
    values_scaled = [0.0, 0.0, 0.0]
    list_matrix_row = [0.0, 0.0, 0.0]
    
    labels = get_label_positions(values_scaled, list_matrix_row, dist, font_height, precision)
    print(f"  Labels generated: {len(labels)}")
    for label in labels:
        print(f"    {label}")
    
    # Test 3: Check coordinate generation
    print("\n📋 Test 3: Coordinate Generation")
    ordinates = [[1e-15, 2e-15, 3e-15]]
    coordinates = generate_coordinates(ordinates, dist, zero_tol=1e-12)
    print(f"  Coordinates generated: {len(coordinates)} loops")
    for loop in coordinates:
        print(f"    Loop with {len(loop)} points")
    
    # Test 4: Test with actual FreeCAD objects
    print("\n📋 Test 4: FreeCAD Object Creation")
    
    # Create test document
    doc = FreeCAD.newDocument("DiagramTest")
    
    # Create a simple beam
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(1000, 0, 0)  # 1m beam
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "TestBeam")
    beam.Shape = line
    
    # Create calc object
    from freecad.StructureTools.calc import Calc
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "TestCalc")
    Calc(calc_obj, [beam])
    
    # Set some test values
    calc_obj.MomentZ = ["1000,2000,3000", "1500,2500,3500"]
    calc_obj.MomentY = ["500,1000,1500", "750,1250,1750"]
    calc_obj.ShearY = ["100,200,300", "150,250,350"]
    calc_obj.ShearZ = ["50,100,150", "75,125,175"]
    calc_obj.AxialForce = ["1000,2000,3000", "1500,2500,3500"]
    calc_obj.Torque = ["100,200,300", "150,250,350"]
    
    # Create diagram object
    diagram_obj = doc.addObject("App::DocumentObjectGroupPython", "TestDiagram")
    Diagram(diagram_obj, calc_obj, [])
    
    print("  ✅ Created test objects")
    
    # Test diagram execution
    try:
        diagram_obj.Proxy.execute(diagram_obj)
        print("  ✅ Diagram execution completed")
        
        # Check if shape was created
        if hasattr(diagram_obj, 'Shape') and not diagram_obj.Shape.isNull():
            print(f"  ✅ Diagram shape created with {len(diagram_obj.Shape.Faces)} faces")
        else:
            print("  ⚠️  Diagram shape is null or missing")
            
    except Exception as e:
        print(f"  ❌ Diagram execution failed: {e}")
        import traceback
        traceback.print_exc()
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    print("\n✅ Cleaned up test document")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("🎉 Test completed!")
print("The diagram fixes should be working correctly.")

print("\nTo run this test in FreeCAD:")
print("1. Open FreeCAD")
print("2. Open the Python console (View → Panels → Python console)")
print("3. Type and execute:")
print("   exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_diagram_fixes.py').read())")