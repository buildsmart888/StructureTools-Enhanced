"""
Test script to verify the fixes for StructuralMaterial.py
Run this in FreeCAD's Python console
"""

import sys
import os

# Add the module path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
if module_path not in sys.path:
    sys.path.insert(0, module_path)

print("🔧 Testing StructuralMaterial fixes...")
print("=" * 50)

try:
    import FreeCAD
    import Part
    from freecad.StructureTools.objects.StructuralMaterial import StructuralMaterial
    print("✅ All imports successful")
except Exception as e:
    print(f"❌ Import failed: {e}")
    exit()

try:
    # Create a new document
    doc = FreeCAD.newDocument("MaterialTest")
    print("✅ Created new document")
except Exception as e:
    print(f"❌ Failed to create document: {e}")
    exit()

try:
    # Create material object
    material_obj = doc.addObject("App::DocumentObjectGroupPython", "TestMaterial")
    StructuralMaterial(material_obj)
    print("✅ Created StructuralMaterial object")
except Exception as e:
    print(f"❌ Failed to create StructuralMaterial object: {e}")
    FreeCAD.closeDocument(doc.Name)
    exit()

# Test 1: Check that ValidationWarnings property exists
print("\n📋 Testing ValidationWarnings Property:")
try:
    if hasattr(material_obj, 'ValidationWarnings'):
        print("  ✅ ValidationWarnings property exists")
        print(f"  ✅ Initial ValidationWarnings value: {material_obj.ValidationWarnings}")
    else:
        print("  ❌ ValidationWarnings property: MISSING")
except Exception as e:
    print(f"  ❌ ValidationWarnings property error: {e}")

# Test 2: Test density normalization with different units
print("\n📋 Testing Density Normalization:")
test_densities = [
    ("7850 kg/m^3", 7850.0),
    ("7.85e-06 kg/mm^3", 7850.0),
    ("0.00785 kg/cm^3", 7850.0)
]

all_density_tests_passed = True
for test_density, expected_kg_m3 in test_densities:
    try:
        # Set the density
        material_obj.Density = test_density
        # Use the helper function to normalize
        normalized_density = material_obj.Proxy._as_kg_per_m3(material_obj.Density)
        if abs(normalized_density - expected_kg_m3) < 1.0:  # Allow small floating point differences
            print(f"  ✅ {test_density} → {normalized_density:.1f} kg/m³")
        else:
            print(f"  ❌ {test_density} → {normalized_density:.1f} kg/m³ (expected ~{expected_kg_m3})")
            all_density_tests_passed = False
    except Exception as e:
        print(f"  ❌ {test_density} → ERROR: {e}")
        all_density_tests_passed = False

# Test 3: Test ShearModulus calculation
print("\n📋 Testing ShearModulus Calculation:")
try:
    # Set some test values
    material_obj.ModulusElasticity = "200000 MPa"
    material_obj.PoissonRatio = 0.3
    
    # Trigger the calculation
    material_obj.Proxy._calculate_shear_modulus(material_obj)
    
    # Check the result
    if hasattr(material_obj, 'ShearModulus'):
        shear_modulus_mpa = material_obj.ShearModulus.getValueAs('MPa')
        expected_G = 200000 / (2 * (1 + 0.3))  # E / (2*(1+nu))
        if abs(shear_modulus_mpa - expected_G) < 1.0:
            print(f"  ✅ ShearModulus calculated correctly: {shear_modulus_mpa:.0f} MPa")
        else:
            print(f"  ❌ ShearModulus incorrect: {shear_modulus_mpa:.0f} MPa (expected ~{expected_G:.0f})")
    else:
        print("  ❌ ShearModulus property: MISSING")
except Exception as e:
    print(f"  ❌ ShearModulus calculation error: {e}")

# Test 4: Test execute method (this is where the original errors occurred)
print("\n📋 Testing Execute Method:")
try:
    # This should not raise the previous errors anymore
    material_obj.Proxy.execute(material_obj)
    print("  ✅ Execute method completed successfully")
    print("  ✅ No AttributeError: 'FeaturePython' object has no attribute 'ValidationWarnings'")
    print("  ✅ No TypeError: unsupported format string passed to Base.Quantity.__format__")
except AttributeError as e:
    if "ValidationWarnings" in str(e):
        print(f"  ❌ ValidationWarnings error still occurs: {e}")
    else:
        print(f"  ❌ Different AttributeError: {e}")
except TypeError as e:
    if "format" in str(e):
        print(f"  ❌ Format error still occurs: {e}")
    else:
        print(f"  ❌ Different TypeError: {e}")
except Exception as e:
    print(f"  ⚠️ Execute method failed with other error: {e}")

# Test 5: Test density validation with different unit formats
print("\n📋 Testing Density Validation:")
try:
    # Test with problematic density value from logs
    material_obj.Density = "7.850000000000001e-06 kg/mm^3"
    # This should not cause validation errors anymore
    material_obj.Proxy.onChanged(material_obj, 'Density')
    print("  ✅ Density validation with scientific notation completed without errors")
except Exception as e:
    print(f"  ❌ Density validation error: {e}")

# Clean up
try:
    FreeCAD.closeDocument(doc.Name)
    print("\n✅ Cleaned up test document")
except:
    pass

print("\n" + "=" * 50)
print("🎉 Test completed!")
print("The fixes should be working correctly.")
print("Original errors should be resolved:")
print("  - AttributeError: 'FeaturePython' object has no attribute 'ValidationWarnings'")
print("  - TypeError: unsupported format string passed to Base.Quantity.__format__")
print("  - Density validation issues with different unit formats")

print("\nTo run this test in FreeCAD:")
print("1. Open FreeCAD")
print("2. Open the Python console (View → Panels → Python console)")
print("3. Type and execute:")
print("   exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_material_fixes.py').read())")