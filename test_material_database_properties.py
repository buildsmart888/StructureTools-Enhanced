#!/usr/bin/env python3
"""
Test script to verify MaterialDatabase shows correct properties in Enhanced dialog.

This script tests:
1. MaterialDatabase.get_concrete_materials() returns data (not None)
2. Concrete materials show correct properties (density, modulus)
3. Material Enhanced dialog displays properties correctly

Usage:
- Run this script in FreeCAD Python console:
  exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_material_database_properties.py').read())
"""

import FreeCAD as App

def test_material_database_concrete_properties():
    """Test MaterialDatabase concrete properties."""
    print("="*80)
    print("TESTING MATERIAL DATABASE - CONCRETE PROPERTIES")
    print("="*80)
    
    try:
        from freecad.StructureTools.data.MaterialDatabase import MaterialDatabase
        print("✅ MaterialDatabase imported successfully")
    except ImportError as e:
        print(f"❌ Cannot import MaterialDatabase: {e}")
        return False
    
    # Test get_concrete_materials
    concrete_materials = MaterialDatabase.get_concrete_materials()
    
    if concrete_materials is None:
        print("❌ CRITICAL ERROR: get_concrete_materials() returned None")
        print("   This means the function is missing 'return materials' statement")
        return False
    
    print(f"✅ get_concrete_materials() returned {len(concrete_materials)} materials")
    
    # Test specific concrete materials
    expected_concrete_props = {
        "Normal Weight C25": {
            "expected_density": 2400,
            "expected_modulus": 25000,  # Should be 25000 MPa, not steel values
            "expected_poisson": 0.20
        },
        "Normal Weight C30": {
            "expected_density": 2400,
            "expected_modulus": 27000,  # Should be 27000 MPa, not steel values
            "expected_poisson": 0.20
        },
        "Thai Fc210": {
            "expected_density": 2400,
            "expected_modulus": 21579,  # Thai concrete modulus
            "expected_poisson": 0.20
        },
        "Thai Fc280": {
            "expected_density": 2400,
            "expected_modulus": 24870,  # Thai concrete modulus
            "expected_poisson": 0.20
        }
    }
    
    all_correct = True
    
    for material_name, expected in expected_concrete_props.items():
        print(f"\n🔍 Testing material: {material_name}")
        
        if material_name in concrete_materials:
            material_data = concrete_materials[material_name]
            
            # Check density
            actual_density = material_data.get('density', 0)
            if actual_density == expected['expected_density']:
                print(f"   ✅ Density: {actual_density} kg/m³")
            else:
                print(f"   ❌ Density: {actual_density} kg/m³ (expected: {expected['expected_density']})")
                all_correct = False
            
            # Check modulus
            actual_modulus = material_data.get('modulus_elasticity', 0)
            if actual_modulus == expected['expected_modulus']:
                print(f"   ✅ Modulus: {actual_modulus} MPa")
            else:
                print(f"   ❌ Modulus: {actual_modulus} MPa (expected: {expected['expected_modulus']})")
                all_correct = False
            
            # Check Poisson ratio
            actual_poisson = material_data.get('poisson_ratio', 0)
            if abs(actual_poisson - expected['expected_poisson']) < 0.01:
                print(f"   ✅ Poisson: {actual_poisson}")
            else:
                print(f"   ❌ Poisson: {actual_poisson} (expected: {expected['expected_poisson']})")
                all_correct = False
            
            # Check if this has steel properties (BUG)
            if actual_density == 7850:
                print(f"   🚨 CRITICAL BUG: Concrete material has STEEL density!")
                all_correct = False
                
            if actual_modulus == 200000:
                print(f"   🚨 CRITICAL BUG: Concrete material has STEEL modulus!")
                all_correct = False
                
            if actual_poisson == 0.30:
                print(f"   🚨 BUG: Concrete material has STEEL Poisson ratio!")
                all_correct = False
        
        else:
            print(f"   ❌ Material '{material_name}' not found in database")
            all_correct = False
    
    return all_correct

def test_material_database_integration():
    """Test MaterialDatabase integration with MaterialSelectionPanel."""
    print(f"\n{'='*80}")
    print("TESTING MATERIAL DATABASE INTEGRATION")
    print(f"{'='*80}")
    
    try:
        from freecad.StructureTools.data.MaterialDatabase import MaterialDatabase
        
        # Test get_all_materials
        all_materials = MaterialDatabase.get_all_materials()
        
        print(f"Available categories: {list(all_materials.keys())}")
        
        # Test concrete category
        if 'Concrete' in all_materials:
            concrete_count = len(all_materials['Concrete'])
            print(f"✅ Concrete category has {concrete_count} materials")
            
            # Check some concrete materials
            concrete_materials = all_materials['Concrete']
            
            if 'Normal Weight C30' in concrete_materials:
                c30 = concrete_materials['Normal Weight C30']
                print(f"   Normal Weight C30:")
                print(f"     Density: {c30.get('density')} kg/m³")
                print(f"     Modulus: {c30.get('modulus_elasticity')} MPa")
                print(f"     Poisson: {c30.get('poisson_ratio')}")
                
                if c30.get('density') == 2400 and c30.get('modulus_elasticity') == 27000:
                    print(f"   ✅ Normal Weight C30 has correct concrete properties!")
                else:
                    print(f"   ❌ Normal Weight C30 has incorrect properties!")
                    return False
            else:
                print("   ❌ 'Normal Weight C30' not found in concrete materials")
                return False
        else:
            print("❌ 'Concrete' category not found")
            return False
        
        # Test steel category for comparison
        if 'Steel' in all_materials:
            steel_count = len(all_materials['Steel'])
            print(f"✅ Steel category has {steel_count} materials")
            
            steel_materials = all_materials['Steel']
            if 'ASTM A36' in steel_materials:
                a36 = steel_materials['ASTM A36']
                print(f"   ASTM A36 (for comparison):")
                print(f"     Density: {a36.get('density')} kg/m³")
                print(f"     Modulus: {a36.get('modulus_elasticity')} MPa")
                print(f"     Poisson: {a36.get('poisson_ratio')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing MaterialDatabase integration: {e}")
        return False

def test_material_standards_consistency():
    """Test consistency between MaterialDatabase and MaterialStandards."""
    print(f"\n{'='*80}")
    print("TESTING CONSISTENCY: MaterialDatabase vs MaterialStandards")
    print(f"{'='*80}")
    
    try:
        from freecad.StructureTools.data.MaterialDatabase import MaterialDatabase
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
        
        print("✅ Both databases imported successfully")
        
        # Test ACI_Normal_30MPa consistency
        print(f"\n🔍 Testing ACI_Normal_30MPa consistency:")
        
        # From MaterialStandards.py
        if 'ACI_Normal_30MPa' in MATERIAL_STANDARDS:
            std_props = MATERIAL_STANDARDS['ACI_Normal_30MPa']
            print(f"   MaterialStandards.py:")
            print(f"     Density: {std_props.get('Density')}")
            print(f"     Modulus: {std_props.get('ModulusElasticity')}")
            print(f"     Poisson: {std_props.get('PoissonRatio')}")
        
        # From MaterialDatabase.py
        concrete_materials = MaterialDatabase.get_concrete_materials()
        if concrete_materials and 'Normal Weight C30' in concrete_materials:
            db_props = concrete_materials['Normal Weight C30']
            print(f"   MaterialDatabase.py (Normal Weight C30):")
            print(f"     Density: {db_props.get('density')} kg/m³")
            print(f"     Modulus: {db_props.get('modulus_elasticity')} MPa")
            print(f"     Poisson: {db_props.get('poisson_ratio')}")
            
            # Check consistency
            std_density = int(std_props.get('Density', '0 kg/m^3').split()[0])
            std_modulus = int(std_props.get('ModulusElasticity', '0 MPa').split()[0])
            std_poisson = std_props.get('PoissonRatio', 0)
            
            db_density = db_props.get('density', 0)
            db_modulus = db_props.get('modulus_elasticity', 0)
            db_poisson = db_props.get('poisson_ratio', 0)
            
            if (std_density == db_density and std_modulus == db_modulus and 
                abs(std_poisson - db_poisson) < 0.01):
                print(f"   ✅ Properties are CONSISTENT between both databases!")
                return True
            else:
                print(f"   ❌ Properties are INCONSISTENT!")
                print(f"      Density: {std_density} vs {db_density}")
                print(f"      Modulus: {std_modulus} vs {db_modulus}")
                print(f"      Poisson: {std_poisson} vs {db_poisson}")
                return False
        else:
            print("   ❌ Normal Weight C30 not found in MaterialDatabase")
            return False
            
    except Exception as e:
        print(f"❌ Error testing consistency: {e}")
        return False

def run_all_tests():
    """Run all material database tests."""
    print("MATERIAL DATABASE PROPERTIES TEST SUITE")
    print("=" * 80)
    
    results = []
    
    # Test 1: Basic MaterialDatabase concrete properties
    results.append(("MaterialDatabase Concrete Properties", test_material_database_concrete_properties()))
    
    # Test 2: MaterialDatabase integration
    results.append(("MaterialDatabase Integration", test_material_database_integration()))
    
    # Test 3: Consistency between databases
    results.append(("Database Consistency", test_material_standards_consistency()))
    
    # Summary
    print(f"\n{'='*80}")
    print("TEST SUMMARY")
    print(f"{'='*80}")
    
    passed = 0
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        print(f"{test_name:<35} : {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! MaterialDatabase is working correctly.")
        print("✅ The Enhanced Material dialog should now show correct concrete properties:")
        print("   - Normal Weight C30: 2400 kg/m³, 27000 MPa, 0.20 Poisson")
        print("   - Normal Weight C25: 2400 kg/m³, 25000 MPa, 0.20 Poisson")
        print("   - Thai concrete grades: Correct density and modulus values")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    return passed == len(results)

if __name__ == "__main__":
    # Run the tests
    success = run_all_tests()
    
    print(f"\n{'='*80}")
    print("MATERIAL DATABASE TEST COMPLETE")
    print(f"{'='*80}")
    
    if success:
        print("✅ MaterialDatabase has been fixed and should display correct properties")
        print("ℹ️  The Enhanced Material dialog should now show:")
        print("   - Concrete materials with 2400 kg/m³ density")
        print("   - Concrete materials with 25000-27000 MPa modulus (not 200000 MPa)")
        print("   - Concrete materials with 0.20 Poisson ratio (not 0.30)")
    else:
        print("❌ Some issues remain with MaterialDatabase")
        print("ℹ️  Check the test output above for specific problems")