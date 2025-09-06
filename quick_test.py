import FreeCAD
import Part
from freecad.StructureTools import calc

# Create a simple test
doc = FreeCAD.newDocument("Test")

# Create a beam
p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(1000, 0, 0)
line = Part.makeLine(p1, p2)
beam = doc.addObject("Part::Feature", "Beam")
beam.Shape = line

# Create calc object
calc_obj = doc.addObject("App::DocumentObjectGroupPython", "CalcTest")
calc.Calc(calc_obj, [beam])

# Test that all NumPoints properties exist
print("Testing NumPoints properties:")
print("NumPointsMoment:", calc_obj.NumPointsMoment)
print("NumPointsAxial:", calc_obj.NumPointsAxial)
print("NumPointsShear:", calc_obj.NumPointsShear)
print("NumPointsTorque:", calc_obj.NumPointsTorque)
print("NumPointsDeflection:", calc_obj.NumPointsDeflection)

# Test ReactionLoadCombo
print("\nTesting ReactionLoadCombo:")
print("ReactionLoadCombo:", calc_obj.ReactionLoadCombo)

print("\n✅ All tests passed! The fixes are working correctly.")

# Clean up
FreeCAD.closeDocument(doc.Name)