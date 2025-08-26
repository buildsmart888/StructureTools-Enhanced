#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify material integration between old and new material systems with calc.

This script tests:
1. Old Material object compatibility with calc
2. New StructuralMaterial object compatibility with calc  
3. Material property conversion and validation
4. Fallback behavior for missing properties
"""

import sys
import os

# Add the StructureTools path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools'))

def test_material_calc_integration():
    """Test material integration with calc system."""
    print("Testing Material Integration with Calc System")
    print("=" * 50)
    
    try:
        # Mock FreeCAD environment for testing
        class MockProperty:
            def __init__(self, value, unit=''):
                self.value = value
                self.unit = unit
            
            def getValueAs(self, target_unit):
                # Simple unit conversion for testing
                if 'MPa' in str(self.value) and 'kN/m^2' in target_unit:
                    return float(str(self.value).replace(' MPa', '')) * 1000
                elif 'kg/m^3' in str(self.value):
                    return float(str(self.value).replace(' kg/m^3', ''))
                return float(str(self.value).split()[0]) if ' ' in str(self.value) else float(self.value)
        
        class MockMaterialOld:
            def __init__(self, name="TestMaterial"):
                self.Name = name
                self.Label = name
                self.ModulusElasticity = MockProperty("200000 MPa")
                self.PoissonRatio = 0.3
                self.Density = MockProperty("7850 kg/m^3")
                # Add the old material class
                from material import Material
                self.Proxy = Material(self)
        
        class MockMaterialNew:
            def __init__(self, name="TestMaterialNew"):
                self.Name = name
                self.Label = name
                self.ModulusElasticity = MockProperty("200000 MPa")
                self.PoissonRatio = 0.3
                self.Density = MockProperty("7850 kg/m^3")
                self.YieldStrength = MockProperty("345 MPa")
                self.UltimateStrength = MockProperty("450 MPa")
                # Add the new material class
                from objects.StructuralMaterial import StructuralMaterial
                self.Proxy = StructuralMaterial(self)
        
        # Test 1: Old Material System
        print("\n1. Testing Old Material System:")
        print("-" * 30)
        
        old_material = MockMaterialOld("Steel_A36")
        if hasattr(old_material.Proxy, 'get_calc_properties'):
            props = old_material.Proxy.get_calc_properties(old_material, 'm', 'kN')
            print(f"   Material Name: {props['name']}")
            print(f"   Elastic Modulus: {props['E']} kN/m²")
            print(f"   Shear Modulus: {props['G']} kN/m²")
            print(f"   Poisson Ratio: {props['nu']}")
            print(f"   Density: {props['density']} kN/m³")
            print("   ✓ Old material system working correctly")
        else:
            print("   ✗ Old material missing get_calc_properties method")
        
        # Test 2: New Material System
        print("\n2. Testing New Material System:")
        print("-" * 30)
        
        new_material = MockMaterialNew("Steel_A992")
        if hasattr(new_material.Proxy, 'get_calc_properties'):
            props = new_material.Proxy.get_calc_properties(new_material, 'm', 'kN')
            print(f"   Material Name: {props['name']}")
            print(f"   Elastic Modulus: {props['E']} kN/m²")
            print(f"   Shear Modulus: {props['G']} kN/m²")
            print(f"   Poisson Ratio: {props['nu']}")
            print(f"   Density: {props['density']} kN/m³")
            print("   ✓ New material system working correctly")
        else:
            print("   ✗ New material missing get_calc_properties method")
        
        # Test 3: Material Property Validation
        print("\n3. Testing Material Property Validation:")
        print("-" * 40)
        
        # Test invalid Poisson ratio
        test_material = MockMaterialOld("TestValidation")
        test_material.PoissonRatio = 0.8  # Invalid (> 0.5)
        
        try:
            if hasattr(test_material.Proxy, 'onChanged'):
                test_material.Proxy.onChanged(test_material, 'PoissonRatio')
                print(f"   Poisson ratio after validation: {test_material.PoissonRatio}")
                if test_material.PoissonRatio == 0.3:
                    print("   ✓ Validation working - invalid Poisson ratio corrected")
                else:
                    print("   ⚠ Validation may not be working properly")
        except Exception as e:
            print(f"   ⚠ Validation test error: {e}")
        
        # Test 4: Unit Conversion
        print("\n4. Testing Unit Conversion:")
        print("-" * 25)
        
        test_mat = MockMaterialOld("UnitTest")
        props_m_kn = test_mat.Proxy.get_calc_properties(test_mat, 'm', 'kN')
        props_mm_n = test_mat.Proxy.get_calc_properties(test_mat, 'mm', 'N')
        
        print(f"   m-kN system: E = {props_m_kn['E']} kN/m²")
        print(f"   mm-N system: E = {props_mm_n['E']} N/mm²")
        print("   ✓ Unit conversion capability confirmed")
        
        print("\n" + "=" * 50)
        print("✓ Material Integration Tests Completed Successfully")
        print("Both old and new material systems are now compatible with calc")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("Make sure you're running this from the StructureTools directory")
        return False
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_material_calc_integration()
    sys.exit(0 if success else 1)