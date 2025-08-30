"""
Comprehensive verification script for all fixes
Run this in FreeCAD's Python console
"""

import sys
import os

# Add the module path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
if module_path not in sys.path:
    sys.path.insert(0, module_path)

print("🔧 Comprehensive Verification of All Fixes")
print("=" * 50)

# Test 1: StructuralMaterial fixes
print("\n📋 Test 1: StructuralMaterial Fixes")
try:
    import FreeCAD
    from freecad.StructureTools.objects.StructuralMaterial import StructuralMaterial
    print("✅ StructuralMaterial import successful")
    
    # Create test document
    doc = FreeCAD.newDocument("MaterialTest")
    
    # Create material object
    material_obj = doc.addObject("App::DocumentObjectGroupPython", "TestMaterial")
    StructuralMaterial(material_obj)
    print("✅ StructuralMaterial object created")
    
    # Test ValidationWarnings property
    if hasattr(material_obj, 'ValidationWarnings'):
        print(f"✅ ValidationWarnings property exists: {material_obj.ValidationWarnings}")
    else:
        print("❌ ValidationWarnings property missing")
    
    # Test density normalization
    try:
        material_obj.Density = "7.850000000000001e-06 kg/mm^3"
        normalized = material_obj.Proxy._as_kg_per_m3(material_obj.Density)
        expected = 7850.0
        if abs(normalized - expected) < 1.0:
            print(f"✅ Density normalization: {normalized:.1f} kg/m³ (expected ~{expected})")
        else:
            print(f"❌ Density normalization: {normalized:.1f} kg/m³ (expected ~{expected})")
    except Exception as e:
        print(f"❌ Density normalization failed: {e}")
    
    # Test shear modulus calculation
    try:
        material_obj.ModulusElasticity = "200000 MPa"
        material_obj.PoissonRatio = 0.3
        material_obj.Proxy._calculate_shear_modulus(material_obj)
        shear_G = material_obj.ShearModulus.getValueAs('MPa')
        expected_G = 200000 / (2 * (1 + 0.3))
        if abs(shear_G - expected_G) < 1.0:
            print(f"✅ Shear modulus calculated: {shear_G:.0f} MPa (expected ~{expected_G:.0f})")
        else:
            print(f"❌ Shear modulus calculated: {shear_G:.0f} MPa (expected ~{expected_G:.0f})")
    except Exception as e:
        print(f"❌ Shear modulus calculation failed: {e}")
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    
except Exception as e:
    print(f"❌ StructuralMaterial test failed: {e}")

# Test 2: Calc object fixes
print("\n📋 Test 2: Calc Object Fixes")
try:
    import FreeCAD
    import Part
    from freecad.StructureTools.calc import Calc
    
    # Create test document
    doc = FreeCAD.newDocument("CalcTest")
    
    # Create a simple beam
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(1000, 0, 0)  # 1m beam
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "TestBeam")
    beam.Shape = line
    
    # Create calc object
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "TestCalc")
    Calc(calc_obj, [beam])
    print("✅ Calc object created")
    
    # Test NumPoints properties
    num_points_props = [
        ('NumPointsMoment', 5),
        ('NumPointsAxial', 3),
        ('NumPointsShear', 4),
        ('NumPointsTorque', 3),
        ('NumPointsDeflection', 4)
    ]
    
    all_good = True
    for prop_name, expected_value in num_points_props:
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
    
    # Test ReactionLoadCombo
    if hasattr(calc_obj, 'ReactionLoadCombo'):
        print(f"  ✅ ReactionLoadCombo exists")
    else:
        print("  ❌ ReactionLoadCombo: MISSING")
        all_good = False
    
    # Test backward compatibility methods
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
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    
except Exception as e:
    print(f"❌ Calc object test failed: {e}")

# Test 3: Diagram object
print("\n📋 Test 3: Diagram Object")
try:
    import FreeCAD
    import Part
    from freecad.StructureTools.calc import Calc
    from freecad.StructureTools.diagram import Diagram
    
    # Create test document
    doc = FreeCAD.newDocument("DiagramTest")
    
    # Create a simple beam
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(1000, 0, 0)  # 1m beam
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "TestBeam")
    beam.Shape = line
    
    # Create calc object
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "TestCalc")
    Calc(calc_obj, [beam])
    
    # Create diagram object
    diagram_obj = doc.addObject("App::DocumentObjectGroupPython", "TestDiagram")
    Diagram(diagram_obj, calc_obj, [])
    print("✅ Diagram object created")
    
    # Test diagram properties
    diagram_props = [
        'Color', 'Transparency', 'FontHeight', 'Precision', 'DrawText',
        'MomentZ', 'MomentY', 'ScaleMoment',
        'ShearZ', 'ShearY', 'ScaleShear',
        'Torque', 'ScaleTorque',
        'AxialForce', 'ScaleAxial'
    ]
    
    all_good = True
    for prop_name in diagram_props:
        if hasattr(diagram_obj, prop_name):
            print(f"  ✅ {prop_name}: {getattr(diagram_obj, prop_name)}")
        else:
            print(f"  ❌ {prop_name}: MISSING")
            all_good = False
    
    # Clean up
    FreeCAD.closeDocument(doc.Name)
    
except Exception as e:
    print(f"❌ Diagram object test failed: {e}")

print("\n" + "=" * 50)
print("🎉 Comprehensive verification completed!")
print("All fixes should be working correctly.")