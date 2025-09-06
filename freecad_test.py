"""
Simple test script to verify the fixes in FreeCAD
Run this in FreeCAD's Python console
"""

import sys
import os

# Add the module path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
if module_path not in sys.path:
    sys.path.insert(0, module_path)

print("🔧 Testing StructureTools fixes...")
print("=" * 50)

try:
    import FreeCAD
    import Part
    from freecad.StructureTools import calc
    print("✅ All imports successful")
except Exception as e:
    print(f"❌ Import failed: {e}")
    exit()

try:
    # Create a new document
    doc = FreeCAD.newDocument("Test")
    print("✅ Created new document")
except Exception as e:
    print(f"❌ Failed to create document: {e}")
    exit()

try:
    # Create a simple beam
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(1000, 0, 0)  # 1m beam
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "TestBeam")
    beam.Shape = line
    print("✅ Created test beam")
except Exception as e:
    print(f"❌ Failed to create beam: {e}")
    FreeCAD.closeDocument(doc.Name)
    exit()

try:
    # Create calc object
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "TestCalc")
    calc.Calc(calc_obj, [beam])
    print("✅ Created calc object")
except Exception as e:
    print(f"❌ Failed to create calc object: {e}")
    FreeCAD.closeDocument(doc.Name)
    exit()

# Test NumPoints properties
print("\n📋 Testing NumPoints Properties:")
num_points_props = [
    ('NumPointsMoment', 5),
    ('NumPointsAxial', 3),
    ('NumPointsShear', 4),
    ('NumPointsTorque', 3),
    ('NumPointsDeflection', 4)
]

all_good = True
for prop_name, expected_value in num_points_props:
    try:
        if hasattr(calc_obj, prop_name):
            actual_value = getattr(calc_obj, prop_name)
            if actual_value == expected_value:
                print(f"  ✅ {prop_name}: {actual_value}")
            else:
                print(f"  ❌ {prop_name}: {actual_value} (expected {expected_value})")
                all_good = False
        else:
            print(f"  ❌ {prop_name}: MISSING")
            all_good = False
    except Exception as e:
        print(f"  ❌ {prop_name}: ERROR - {e}")
        all_good = False

# Test ReactionLoadCombo
print("\n📋 Testing ReactionLoadCombo:")
try:
    if hasattr(calc_obj, 'ReactionLoadCombo'):
        # Try to access the property
        current_value = calc_obj.ReactionLoadCombo
        print(f"  ✅ ReactionLoadCombo exists - Current value: {current_value}")
    else:
        print("  ❌ ReactionLoadCombo: MISSING")
        all_good = False
except Exception as e:
    print(f"  ❌ ReactionLoadCombo: ERROR - {e}")
    all_good = False

# Test backward compatibility methods
print("\n📋 Testing Backward Compatibility Methods:")
try:
    if hasattr(calc_obj.Proxy, '_addPropIfMissing'):
        print("  ✅ _addPropIfMissing method exists")
    else:
        print("  ❌ _addPropIfMissing method: MISSING")
        all_good = False
        
    if hasattr(calc_obj.Proxy, 'ensure_required_properties'):
        print("  ✅ ensure_required_properties method exists")
    else:
        print("  ❌ ensure_required_properties method: MISSING")
        all_good = False
except Exception as e:
    print(f"  ❌ Backward compatibility methods: ERROR - {e}")
    all_good = False

# Clean up
try:
    FreeCAD.closeDocument(doc.Name)
    print("\n✅ Cleaned up test document")
except:
    pass

print("\n" + "=" * 50)
if all_good:
    print("🎉 ALL TESTS PASSED!")
    print("The fixes should be working correctly.")
else:
    print("💥 SOME TESTS FAILED!")
    print("There may still be issues to resolve.")

print("\nTo run this test in FreeCAD:")
print("1. Open FreeCAD")
print("2. Open the Python console (View → Panels → Python console)")
print("3. Type and execute:")
print("   exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/freecad_test.py').read())")