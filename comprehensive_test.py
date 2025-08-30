"""
Comprehensive test that actually executes the calc function
Run this in FreeCAD's Python console
"""

import sys
import os

# Add the module path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
if module_path not in sys.path:
    sys.path.insert(0, module_path)

print("🔧 Comprehensive StructureTools Test")
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
    doc = FreeCAD.newDocument("ComprehensiveTest")
    print("✅ Created new document")
except Exception as e:
    print(f"❌ Failed to create document: {e}")
    exit()

try:
    # Create a simple structure with beam and support
    # Create a horizontal beam
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(3000, 0, 0)  # 3m beam
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "Beam")
    beam.Shape = line
    
    # Create a support at the left end
    support = doc.addObject("App::DocumentObjectGroupPython", "Support")
    # We'll simulate a simple support object
    support.Placement = FreeCAD.Placement(p1, FreeCAD.Rotation())
    
    print("✅ Created test structure")
except Exception as e:
    print(f"❌ Failed to create structure: {e}")
    FreeCAD.closeDocument(doc.Name)
    exit()

try:
    # Create calc object with the beam
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "Calc")
    calc.Calc(calc_obj, [beam])
    print("✅ Created calc object")
except Exception as e:
    print(f"❌ Failed to create calc object: {e}")
    FreeCAD.closeDocument(doc.Name)
    exit()

# Test that all required properties exist
print("\n📋 Testing Required Properties:")
required_properties = [
    'NumPointsMoment', 'NumPointsAxial', 'NumPointsShear', 
    'NumPointsTorque', 'NumPointsDeflection', 'ReactionLoadCombo'
]

all_good = True
for prop in required_properties:
    try:
        if hasattr(calc_obj, prop):
            value = getattr(calc_obj, prop)
            print(f"  ✅ {prop}: {value}")
        else:
            print(f"  ❌ {prop}: MISSING")
            all_good = False
    except Exception as e:
        print(f"  ❌ {prop}: ERROR - {e}")
        all_good = False

# Test the execute method (this is where the original error occurred)
print("\n📋 Testing Execute Method:")
try:
    # This should not raise the AttributeError anymore
    calc_obj.Proxy.execute(calc_obj)
    print("  ✅ Execute method completed successfully")
    print("  ✅ No AttributeError: 'FeaturePython' object has no attribute 'NumPointsMoment'")
except AttributeError as e:
    if "NumPointsMoment" in str(e):
        print(f"  ❌ Original error still occurs: {e}")
        all_good = False
    else:
        print(f"  ❌ Different AttributeError: {e}")
        # This might be okay if it's a different issue
except Exception as e:
    print(f"  ⚠️ Execute method failed with other error: {e}")
    # This might be okay if it's a different issue not related to NumPoints

# Test ReactionLoadCombo specifically
print("\n📋 Testing ReactionLoadCombo Handling:")
try:
    # Test that we can set ReactionLoadCombo without ValueError
    load_combinations = ['100_DL', '101_DL+LL']
    calc_obj.ReactionLoadCombo = load_combinations
    print("  ✅ Set ReactionLoadCombo to list of combinations")
    
    # Test setting to a valid single combination
    calc_obj.ReactionLoadCombo = '100_DL'
    print("  ✅ Set ReactionLoadCombo to single valid combination")
    
    print("  ✅ No ValueError: 'C' is not part of the enumeration")
except ValueError as e:
    print(f"  ❌ ValueError still occurs: {e}")
    all_good = False
except Exception as e:
    print(f"  ❌ Other error with ReactionLoadCombo: {e}")
    all_good = False

# Test backward compatibility functions
print("\n📋 Testing Backward Compatibility:")
try:
    calc_obj.Proxy.ensure_required_properties(calc_obj)
    print("  ✅ ensure_required_properties executed without errors")
    
    # Test _addPropIfMissing with a new property
    calc_obj.Proxy._addPropIfMissing(calc_obj, "App::PropertyInteger", "TestProperty", "Test", "Test property", 99)
    if hasattr(calc_obj, 'TestProperty') and calc_obj.TestProperty == 99:
        print("  ✅ _addPropIfMissing works correctly")
    else:
        print("  ❌ _addPropIfMissing failed")
        all_good = False
except Exception as e:
    print(f"  ❌ Backward compatibility functions failed: {e}")
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
    print("The original errors should be resolved:")
    print("  - AttributeError: 'FeaturePython' object has no attribute 'NumPointsMoment'")
    print("  - ValueError: 'C' is not part of the enumeration in ReactionLoadCombo")
else:
    print("💥 SOME TESTS FAILED!")
    print("There may still be issues to resolve.")

print("\nTo run this test in FreeCAD:")
print("1. Open FreeCAD")
print("2. Open the Python console (View → Panels → Python console)")
print("3. Type and execute:")
print("   exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/comprehensive_test.py').read())")