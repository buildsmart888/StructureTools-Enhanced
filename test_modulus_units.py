#!/usr/bin/env python3
"""
Test Modulus Elasticity Units in Calc

This script tests and demonstrates how modulus elasticity units are converted
from FreeCAD material properties to Pynite engine in calc.py.

Key Question: Does Pynite expect modulus in GPa or in the calc units (kN/m²)?

Usage:
- Run this script in FreeCAD Python console:
  exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_modulus_units.py').read())
"""

import FreeCAD as App

def test_material_property_units():
    """Test how material properties are stored and converted."""
    print("="*80)
    print("MATERIAL PROPERTY UNITS TEST")
    print("="*80)
    
    if not App.ActiveDocument:
        print("❌ No active document. Please create a document first.")
        return
    
    # Create test materials
    materials_to_test = [
        ("Steel_Test", "200000 MPa", "7850 kg/m^3", 0.30, "Steel"),
        ("Concrete_Test", "27000 MPa", "2400 kg/m^3", 0.20, "Concrete")
    ]
    
    created_materials = []
    
    for name, modulus_str, density_str, poisson, mat_type in materials_to_test:
        try:
            # Create basic material object
            mat_obj = App.ActiveDocument.addObject("Part::FeaturePython", name)
            
            # Add material properties
            mat_obj.addProperty("App::PropertyPressure", "ModulusElasticity", "Material", "Elastic Modulus")
            mat_obj.addProperty("App::PropertyDensity", "Density", "Material", "Material Density")  
            mat_obj.addProperty("App::PropertyFloat", "PoissonRatio", "Material", "Poisson Ratio")
            mat_obj.addProperty("App::PropertyString", "MaterialType", "Material", "Material Type")
            
            # Set values
            mat_obj.ModulusElasticity = modulus_str
            mat_obj.Density = density_str
            mat_obj.PoissonRatio = poisson
            mat_obj.MaterialType = mat_type
            
            created_materials.append(mat_obj)
            print(f"✅ Created test material: {name}")
            
        except Exception as e:
            print(f"❌ Error creating {name}: {e}")
    
    App.ActiveDocument.recompute()
    return created_materials

def test_unit_conversion_logic(materials):
    """Test the unit conversion logic used in calc.py."""
    print(f"\n{'='*60}")
    print("UNIT CONVERSION TESTING")
    print(f"{'='*60}")
    
    # Test different unit combinations that calc.py might use
    unit_combinations = [
        ("kN", "m"),      # Default calc units
        ("N", "m"),       # SI units
        ("kN", "mm"),     # Mixed units
        ("MN", "m"),      # Large force units
    ]
    
    for force_unit, length_unit in unit_combinations:
        print(f"\n🔧 Testing with ForceUnit='{force_unit}', LengthUnit='{length_unit}':")
        stress_unit = f"{force_unit}/{length_unit}^2"
        
        for material in materials:
            name = material.Name
            mat_type = material.MaterialType
            
            print(f"\n   📊 Material: {name} ({mat_type})")
            
            # Get original property values
            modulus_original = str(material.ModulusElasticity)
            density_original = str(material.Density)
            
            print(f"      Original Modulus: {modulus_original}")
            print(f"      Original Density: {density_original}")
            
            try:
                # Test modulus conversion (same logic as calc.py)
                modulus_converted = float(material.ModulusElasticity.getValueAs(stress_unit))
                
                print(f"      Converted Modulus: {modulus_converted:.1f} {stress_unit}")
                
                # Compare with expected values for different scenarios
                if force_unit == "kN" and length_unit == "m":
                    # This is the default calc units
                    if mat_type == "Steel":
                        expected_gpa = 200  # GPa
                        expected_kn_m2 = expected_gpa * 1000000  # Convert GPa to kN/m²
                        print(f"      Expected (Steel): {expected_kn_m2:.0f} kN/m² ({expected_gpa} GPa)")
                    elif mat_type == "Concrete":
                        expected_gpa = 27  # GPa
                        expected_kn_m2 = expected_gpa * 1000000  # Convert GPa to kN/m²
                        print(f"      Expected (Concrete): {expected_kn_m2:.0f} kN/m² ({expected_gpa} GPa)")
                    
                    # Check if conversion is correct
                    if mat_type == "Steel" and abs(modulus_converted - 200000000) < 1000:
                        print(f"      ✅ Steel modulus conversion correct!")
                    elif mat_type == "Concrete" and abs(modulus_converted - 27000000) < 1000:
                        print(f"      ✅ Concrete modulus conversion correct!")
                    else:
                        print(f"      ⚠️  Conversion may not match expected values")
                
                # Test density conversion
                density_unit = f"{force_unit}/{length_unit}^3"
                
                # Calc.py logic: kg/m³ → t/m³ → kN/m³ → target units
                try:
                    density_kg_m3 = App.Units.Quantity(material.Density).getValueAs('kg/m^3')
                    density_t_m3 = density_kg_m3 / 1000  # kg/m³ to t/m³
                    density_kn_m3 = density_t_m3 * 9.81  # t/m³ to kN/m³ (multiply by g)
                    density_converted = float(App.Units.Quantity(density_kn_m3, 'kN/m^3').getValueAs(density_unit))
                    
                    print(f"      Converted Density: {density_converted:.3f} {density_unit}")
                    print(f"        (Steps: {density_kg_m3:.0f} kg/m³ → {density_t_m3:.3f} t/m³ → {density_kn_m3:.2f} kN/m³)")
                    
                except Exception as e:
                    print(f"      ❌ Density conversion error: {e}")
                
            except Exception as e:
                print(f"      ❌ Conversion error: {e}")

def demonstrate_pynite_usage():
    """Demonstrate what units Pynite actually receives."""
    print(f"\n{'='*60}")
    print("PYNITE USAGE DEMONSTRATION")
    print(f"{'='*60}")
    
    # Show what typical Pynite add_material calls look like
    print("\n🏗️  Typical Pynite add_material() calls:")
    print("   Steel:")
    print("     model.add_material('Steel', E=200000000, G=76923077, nu=0.30, rho=78.5)")
    print("     (E = 200 GPa = 200,000,000 kN/m²)")
    print()
    print("   Concrete:")
    print("     model.add_material('Concrete', E=27000000, G=11250000, nu=0.20, rho=23.5)")
    print("     (E = 27 GPa = 27,000,000 kN/m²)")
    print()
    
    print("📐 Unit Analysis:")
    print("   Default Calc Units: ForceUnit='kN', LengthUnit='m'")
    print("   Stress Units: kN/m²")
    print("   1 GPa = 1,000 MPa = 1,000,000 kN/m²")
    print()
    print("   Steel (200 GPa):")
    print("     200 GPa = 200,000 MPa = 200,000,000 kN/m²")
    print()
    print("   Concrete (27 GPa):")
    print("     27 GPa = 27,000 MPa = 27,000,000 kN/m²")

def check_existing_calc_object():
    """Check existing Calc objects and their unit settings."""
    print(f"\n{'='*60}")
    print("EXISTING CALC OBJECT ANALYSIS")
    print(f"{'='*60}")
    
    calc_objects = []
    for obj in App.ActiveDocument.Objects:
        if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
            if 'Calc' in obj.Proxy.__class__.__name__:
                calc_objects.append(obj)
    
    if not calc_objects:
        print("❌ No Calc objects found in document")
        return
    
    for calc_obj in calc_objects:
        print(f"\n📊 Calc Object: {calc_obj.Name}")
        
        # Check unit settings
        force_unit = getattr(calc_obj, 'ForceUnit', 'Not set')
        length_unit = getattr(calc_obj, 'LengthUnit', 'Not set')
        
        print(f"   ForceUnit: {force_unit}")
        print(f"   LengthUnit: {length_unit}")
        print(f"   Stress Units: {force_unit}/{length_unit}²")
        
        if force_unit == 'kN' and length_unit == 'm':
            print(f"   ✅ Using standard units (stress in kN/m²)")
            print(f"   📐 Material modulus conversion:")
            print(f"      Steel 200 GPa → 200,000,000 kN/m²")
            print(f"      Concrete 27 GPa → 27,000,000 kN/m²")
        else:
            print(f"   ⚠️  Using non-standard units - check conversions carefully")

def run_modulus_units_test():
    """Run complete modulus units test."""
    print("MODULUS ELASTICITY UNITS TEST")
    print("=" * 80)
    print("This test examines how FreeCAD material properties are converted")
    print("for use in Pynite finite element analysis engine.")
    print()
    
    # Create test materials
    print("1️⃣ Creating test materials...")
    materials = test_material_property_units()
    
    if materials:
        # Test unit conversions
        print("\n2️⃣ Testing unit conversions...")
        test_unit_conversion_logic(materials)
    
    # Demonstrate Pynite usage
    print("\n3️⃣ Demonstrating Pynite usage...")
    demonstrate_pynite_usage()
    
    # Check existing calc objects
    print("\n4️⃣ Checking existing Calc objects...")
    check_existing_calc_object()
    
    # Summary and conclusions
    print(f"\n{'='*80}")
    print("CONCLUSIONS")
    print(f"{'='*80}")
    print("✅ MODULUS UNITS IN CALC/PYNITE:")
    print()
    print("🔹 FreeCAD Materials store modulus in: MPa (default display)")
    print("🔹 Calc converts modulus to: kN/m² (when using default kN,m units)")  
    print("🔹 Pynite receives modulus in: kN/m² (same as calc units)")
    print()
    print("📊 CONVERSION EXAMPLES:")
    print("   Steel (200 GPa):")
    print("     FreeCAD: 200000 MPa")
    print("     Calc converts: 200000 MPa → 200,000,000 kN/m²")
    print("     Pynite receives: 200,000,000 kN/m²")
    print()
    print("   Concrete (27 GPa):")
    print("     FreeCAD: 27000 MPa")
    print("     Calc converts: 27000 MPa → 27,000,000 kN/m²")
    print("     Pynite receives: 27,000,000 kN/m²")
    print()
    print("✅ ANSWER: Pynite expects modulus in CALC UNITS (kN/m²), not GPa!")
    print("   The conversion from MPa to kN/m² is handled automatically by")
    print("   FreeCAD's getValueAs() method in calc.py")
    
    # Clean up test materials
    if materials:
        response = input(f"\n🗑️  Delete {len(materials)} test materials? (y/N): ").lower().strip()
        if response in ['y', 'yes']:
            for mat in materials:
                App.ActiveDocument.removeObject(mat.Name)
            App.ActiveDocument.recompute()
            print("✅ Test materials deleted")

if __name__ == "__main__":
    run_modulus_units_test()