# Simple check to verify the fixes
# Run in FreeCAD Python console:
# exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/simple_check.py').read())

import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')

try:
    import FreeCAD
    import Part
    from freecad.StructureTools import calc
    
    # Create test objects
    doc = FreeCAD.newDocument("Test")
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(1000, 0, 0)
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "Beam")
    beam.Shape = line
    
    # Create calc object
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "CalcTest")
    calc.Calc(calc_obj, [beam])
    
    # Check properties
    print("✅ NumPointsMoment:", calc_obj.NumPointsMoment)
    print("✅ NumPointsShear:", calc_obj.NumPointsShear)
    print("✅ NumPointsDeflection:", calc_obj.NumPointsDeflection)
    print("✅ ReactionLoadCombo:", calc_obj.ReactionLoadCombo)
    
    # Test execute method
    try:
        calc_obj.Proxy.execute(calc_obj)
        print("✅ Execute method completed without AttributeError")
    except AttributeError as e:
        if "NumPointsMoment" in str(e):
            print("❌ Still getting NumPointsMoment error:", e)
        else:
            print("⚠️ Different AttributeError:", e)
    except Exception as e:
        print("⚠️ Execute failed with other error:", e)
    
    FreeCAD.closeDocument(doc.Name)
    print("✅ Simple check completed!")
    
except Exception as e:
    print("❌ Error:", e)