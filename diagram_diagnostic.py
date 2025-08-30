"""
Diagnostic script to identify why diagram values are zero
Run this in FreeCAD's Python console
"""

import sys
import os

# Add the module path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
if module_path not in sys.path:
    sys.path.insert(0, module_path)

print("🔧 Diagram Diagnostic Tool")
print("=" * 50)

try:
    import FreeCAD
    import Part
    from freecad.StructureTools.calc import Calc
    
    # Create a test model with a simple beam and load
    doc = FreeCAD.newDocument("DiagnosticTest")
    
    # Create a horizontal beam (1m long)
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(1000, 0, 0)  # 1m beam in mm
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "TestBeam")
    beam.Shape = line
    
    # Create a support at the left end
    support = doc.addObject("App::DocumentObjectGroupPython", "LeftSupport")
    # We'll simulate a simple support object
    support.Placement = FreeCAD.Placement(p1, FreeCAD.Rotation())
    
    # Create a point load at the right end
    load = doc.addObject("App::DocumentObjectGroupPython", "PointLoad")
    load.Placement = FreeCAD.Placement(p2, FreeCAD.Rotation())
    
    # Create calc object with the beam
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "CalcTest")
    Calc(calc_obj, [beam])
    
    print("✅ Created test structure")
    
    # Check if the calc object has the required properties
    print("\n📋 Checking Calc Object Properties:")
    required_props = [
        'NumPointsMoment', 'NumPointsAxial', 'NumPointsShear', 
        'NumPointsTorque', 'NumPointsDeflection'
    ]
    
    for prop in required_props:
        if hasattr(calc_obj, prop):
            value = getattr(calc_obj, prop)
            print(f"  ✅ {prop}: {value}")
        else:
            print(f"  ❌ {prop}: MISSING")
    
    # Check if there are any loads or supports in the document
    print("\n📋 Checking Document Objects:")
    objects = doc.Objects
    loads = [obj for obj in objects if 'Load' in obj.Name]
    supports = [obj for obj in objects if 'Support' in obj.Name or 'Suport' in obj.Name]
    
    print(f"  Loads found: {len(loads)}")
    print(f"  Supports found: {len(supports)}")
    
    # Try to execute the calculation
    print("\n📋 Executing Calculation:")
    try:
        calc_obj.Proxy.execute(calc_obj)
        print("  ✅ Calculation executed successfully")
    except Exception as e:
        print(f"  ❌ Calculation failed: {e}")
    
    # Check the results
    print("\n📋 Checking Results:")
    result_props = [
        'MomentZ', 'MomentY', 'ShearY', 'ShearZ', 
        'AxialForce', 'Torque', 'DeflectionY', 'DeflectionZ'
    ]
    
    for prop in result_props:
        if hasattr(calc_obj, prop):
            values = getattr(calc_obj, prop)
            if values:
                # Check if all values are essentially zero
                all_zero = True
                for val_str in values[:3]:  # Check first 3 members
                    try:
                        val_list = [float(x) for x in val_str.split(',')]
                        if any(abs(v) > 1e-10 for v in val_list):
                            all_zero = False
                            break
                    except:
                        pass
                if all_zero:
                    print(f"  ⚠️  {prop}: All values are zero")
                else:
                    print(f"  ✅ {prop}: Contains non-zero values")
            else:
                print(f"  ⚠️  {prop}: Empty result list")
        else:
            print(f"  ❌ {prop}: MISSING")
    
    # Check load summary
    if hasattr(calc_obj, 'LoadSummary'):
        load_summary = calc_obj.LoadSummary
        print(f"\n📋 Load Summary: {len(load_summary)} loads")
        for load in load_summary:
            print(f"  - {load}")
    else:
        print("\n📋 Load Summary: MISSING")
    
    # Check reaction forces
    if hasattr(calc_obj, 'ReactionNodes'):
        reaction_nodes = calc_obj.ReactionNodes
        print(f"\n📋 Reaction Nodes: {len(reaction_nodes)} nodes")
        if reaction_nodes:
            rx = getattr(calc_obj, 'ReactionX', [])
            ry = getattr(calc_obj, 'ReactionY', [])
            rz = getattr(calc_obj, 'ReactionZ', [])
            for i, node in enumerate(reaction_nodes[:3]):  # Show first 3
                fx = rx[i] if i < len(rx) else 0
                fy = ry[i] if i < len(ry) else 0
                fz = rz[i] if i < len(rz) else 0
                print(f"  Node {node}: FX={fx:.2e}, FY={fy:.2e}, FZ={fz:.2e}")
    else:
        print("\n📋 Reaction Nodes: MISSING")
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    print("\n✅ Diagnostic completed!")
    
except Exception as e:
    print(f"❌ Diagnostic failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("💡 Troubleshooting Tips:")
print("1. Ensure you have applied loads to your structure")
print("2. Make sure supports are properly defined")
print("3. Check that materials and sections are assigned to members")
print("4. Verify that the LoadCase or LoadCombination is set correctly")
print("5. Confirm that the structure is stable (not a mechanism)")