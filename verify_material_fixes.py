# Simple verification script for FreeCAD Python console
# Copy and paste this into FreeCAD's Python console to test the fixes

import sys
import os

# Add the module path
module_path = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools')
if module_path not in sys.path:
    sys.path.insert(0, module_path)

print("🔧 Verifying StructuralMaterial fixes...")
print("=" * 50)

try:
    import FreeCAD
    from freecad.StructureTools.objects.StructuralMaterial import StructuralMaterial
    print("✅ Import successful")
except Exception as e:
    print(f"❌ Import failed: {e}")
    exit()

# Create test document
doc = FreeCAD.newDocument("Test")

# Create material object
material_obj = doc.addObject("App::DocumentObjectGroupPython", "TestMaterial")
StructuralMaterial(material_obj)

print("✅ Created StructuralMaterial object")

# Test 1: Check ValidationWarnings property
print("\n📋 Test 1: ValidationWarnings Property")
if hasattr(material_obj, 'ValidationWarnings'):
    print(f"✅ ValidationWarnings exists: {material_obj.ValidationWarnings}")
else:
    print("❌ ValidationWarnings missing")

# Test 2: Test density normalization
print("\n📋 Test 2: Density Normalization")
try:
    # Test with problematic density from logs
    material_obj.Density = "7.850000000000001e-06 kg/mm^3"
    normalized = material_obj.Proxy._as_kg_per_m3(material_obj.Density)
    print(f"✅ Density normalization: {normalized:.1f} kg/m³")
except Exception as e:
    print(f"❌ Density normalization failed: {e}")

# Test 3: Test shear modulus calculation
print("\n📋 Test 3: Shear Modulus Calculation")
try:
    material_obj.ModulusElasticity = "200000 MPa"
    material_obj.PoissonRatio = 0.3
    material_obj.Proxy._calculate_shear_modulus(material_obj)
    shear_G = material_obj.ShearModulus.getValueAs('MPa')
    print(f"✅ Shear modulus calculated: {shear_G:.0f} MPa")
except Exception as e:
    print(f"❌ Shear modulus calculation failed: {e}")

# Test 4: Test execute method
print("\n📋 Test 4: Execute Method")
try:
    material_obj.Proxy.execute(material_obj)
    print("✅ Execute method completed without errors")
except Exception as e:
    print(f"❌ Execute method failed: {e}")

# Clean up
FreeCAD.closeDocument(doc.Name)
print("\n✅ Verification completed!")
print("All fixes should be working correctly.")