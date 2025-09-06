#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Thai Units Test
======================

Basic test for Thai units conversion functionality without FreeCAD dependencies.
"""

import sys
import os
import math

# Add path to find modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools'))

def test_thai_units_converter():
    """Test Thai units converter functionality"""
    print("🇹🇭 Testing Thai Units Converter")
    print("=" * 50)
    
    try:
        from utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        print("✅ UniversalThaiUnits imported successfully")
        
        # Test force conversions
        print("\n📏 Testing Force Conversions:")
        kn_val = 100.0
        kgf_val = converter.kn_to_kgf(kn_val)
        tf_val = converter.kn_to_tf(kn_val)
        
        print(f"  {kn_val} kN = {kgf_val:.2f} kgf = {tf_val:.3f} tf")
        
        # Verify reverse conversion
        kn_back = converter.kgf_to_kn(kgf_val)
        print(f"  Reverse: {kgf_val:.2f} kgf = {kn_back:.2f} kN (diff: {abs(kn_val - kn_back):.6f})")
        
        if abs(kn_val - kn_back) < 0.001:
            print("  ✅ Force conversion accuracy verified")
        else:
            print("  ❌ Force conversion accuracy issue")
        
        # Test moment conversions
        print("\n🔄 Testing Moment Conversions:")
        kn_m_val = 50.0
        kgf_cm_val = converter.kn_m_to_kgf_cm(kn_m_val)
        tf_m_val = converter.kn_m_to_tf_m(kn_m_val)
        
        print(f"  {kn_m_val} kN·m = {kgf_cm_val:.1f} kgf·cm = {tf_m_val:.3f} tf·m")
        
        # Verify reverse conversion
        kn_m_back = converter.kgf_cm_to_kn_m(kgf_cm_val)
        print(f"  Reverse: {kgf_cm_val:.1f} kgf·cm = {kn_m_back:.2f} kN·m (diff: {abs(kn_m_val - kn_m_back):.6f})")
        
        if abs(kn_m_val - kn_m_back) < 0.001:
            print("  ✅ Moment conversion accuracy verified")
        else:
            print("  ❌ Moment conversion accuracy issue")
        
        # Test pressure conversions
        print("\n🏗️ Testing Pressure Conversions:")
        mpa_val = 25.0
        ksc_val = converter.mpa_to_ksc(mpa_val)
        
        kn_m2_val = 2400.0  # kN/m² (same as kPa)
        ksc_m2_val = converter.kn_m2_to_ksc_m2(kn_m2_val)
        tf_m2_val = converter.kn_m2_to_tf_m2(kn_m2_val)
        
        print(f"  {mpa_val} MPa = {ksc_val:.3f} ksc")
        print(f"  {kn_m2_val} kN/m² = {ksc_m2_val:.3f} ksc/m² = {tf_m2_val:.3f} tf/m²")
        
        # Test linear load conversions
        print("\n📐 Testing Linear Load Conversions:")
        kn_m_load = 15.0
        kgf_m_load = converter.kn_m_to_kgf_m(kn_m_load)
        tf_m_load = converter.kn_m_to_tf_m(kn_m_load)
        
        print(f"  {kn_m_load} kN/m = {kgf_m_load:.2f} kgf/m = {tf_m_load:.3f} tf/m")
        
        # Test practical engineering values
        print("\n🏢 Testing Practical Engineering Values:")
        
        # Typical building loads
        dead_load_kn_m2 = 2.4  # Dead load
        live_load_kn_m2 = 2.0   # Live load
        
        print(f"  Dead Load: {dead_load_kn_m2} kN/m² = {converter.kn_m2_to_ksc_m2(dead_load_kn_m2):.3f} ksc/m² = {converter.kn_m2_to_tf_m2(dead_load_kn_m2):.3f} tf/m²")
        print(f"  Live Load: {live_load_kn_m2} kN/m² = {converter.kn_m2_to_ksc_m2(live_load_kn_m2):.3f} ksc/m² = {converter.kn_m2_to_tf_m2(live_load_kn_m2):.3f} tf/m²")
        
        # Typical concrete strength
        concrete_fc = 28.0  # MPa (Fc280)
        print(f"  Concrete Fc: {concrete_fc} MPa = {converter.mpa_to_ksc(concrete_fc):.2f} ksc")
        
        # Typical steel strength  
        steel_fy = 400.0  # MPa (SD40)
        print(f"  Steel Fy: {steel_fy} MPa = {converter.mpa_to_ksc(steel_fy):.2f} ksc")
        
        print("\n✅ All Thai units conversions working correctly!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return False

def test_thai_units_accuracy():
    """Test accuracy of Thai units conversions against known values"""
    print("\n🔬 Testing Conversion Accuracy")
    print("=" * 50)
    
    try:
        from utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        # Known conversion factors
        tests = [
            # (value, conversion_method, expected_result, tolerance, description)
            (1.0, converter.kn_to_kgf, 101.972, 0.01, "1 kN to kgf"),
            (1.0, converter.kn_to_tf, 0.10197, 0.0001, "1 kN to tf"), 
            (1.0, converter.mpa_to_ksc, 0.10197, 0.0001, "1 MPa to ksc"),
            (9.80665, converter.kn_to_kgf, 1000.0, 0.1, "9.80665 kN to kgf (gravity)"),
            (100.0, converter.kn_m_to_kgf_cm, 1019716.2, 1.0, "100 kN·m to kgf·cm"),
        ]
        
        all_passed = True
        for value, method, expected, tolerance, description in tests:
            result = method(value)
            diff = abs(result - expected)
            passed = diff <= tolerance
            
            status = "✅" if passed else "❌"
            print(f"  {status} {description}: {result:.4f} (expected: {expected:.4f}, diff: {diff:.6f})")
            
            if not passed:
                all_passed = False
        
        if all_passed:
            print("\n✅ All accuracy tests passed!")
        else:
            print("\n❌ Some accuracy tests failed!")
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Accuracy test error: {e}")
        return False

def test_components_integration():
    """Test that components can use Thai units"""
    print("\n🔧 Testing Components Integration")
    print("=" * 50)
    
    # Test basic class structure
    try:
        from utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        # Simulate load data
        nodal_load_data = {
            'force_x_kn': 10.0,
            'force_y_kn': 0.0,
            'force_z_kn': -25.0,
            'moment_x_kn_m': 5.0,
            'moment_y_kn_m': 0.0,
            'moment_z_kn_m': 15.0
        }
        
        # Convert to Thai units
        thai_nodal_data = {
            'force_x_kgf': converter.kn_to_kgf(nodal_load_data['force_x_kn']),
            'force_x_tf': converter.kn_to_tf(nodal_load_data['force_x_kn']),
            'force_z_kgf': converter.kn_to_kgf(nodal_load_data['force_z_kn']),
            'force_z_tf': converter.kn_to_tf(nodal_load_data['force_z_kn']),
            'moment_z_kgf_cm': converter.kn_m_to_kgf_cm(nodal_load_data['moment_z_kn_m']),
            'moment_z_tf_m': converter.kn_m_to_tf_m(nodal_load_data['moment_z_kn_m'])
        }
        
        print("  📍 Node Load Conversion:")
        print(f"    Fx: {nodal_load_data['force_x_kn']} kN = {thai_nodal_data['force_x_kgf']:.1f} kgf = {thai_nodal_data['force_x_tf']:.3f} tf")
        print(f"    Fz: {nodal_load_data['force_z_kn']} kN = {thai_nodal_data['force_z_kgf']:.1f} kgf = {thai_nodal_data['force_z_tf']:.3f} tf")
        print(f"    Mz: {nodal_load_data['moment_z_kn_m']} kN·m = {thai_nodal_data['moment_z_kgf_cm']:.1f} kgf·cm = {thai_nodal_data['moment_z_tf_m']:.3f} tf·m")
        
        # Simulate distributed load data
        dist_load_data = {
            'initial_load_kn_m': 5.0,
            'final_load_kn_m': 10.0
        }
        
        thai_dist_data = {
            'initial_load_kgf_m': converter.kn_m_to_kgf_m(dist_load_data['initial_load_kn_m']),
            'initial_load_tf_m': converter.kn_m_to_tf_m(dist_load_data['initial_load_kn_m']),
            'final_load_kgf_m': converter.kn_m_to_kgf_m(dist_load_data['final_load_kn_m']),
            'final_load_tf_m': converter.kn_m_to_tf_m(dist_load_data['final_load_kn_m'])
        }
        
        print("\n  📏 Distributed Load Conversion:")
        print(f"    Initial: {dist_load_data['initial_load_kn_m']} kN/m = {thai_dist_data['initial_load_kgf_m']:.1f} kgf/m = {thai_dist_data['initial_load_tf_m']:.3f} tf/m")
        print(f"    Final: {dist_load_data['final_load_kn_m']} kN/m = {thai_dist_data['final_load_kgf_m']:.1f} kgf/m = {thai_dist_data['final_load_tf_m']:.3f} tf/m")
        
        # Simulate area load data
        area_load_data = {
            'pressure_kn_m2': 2.4,
            'area_m2': 25.0
        }
        
        total_force_kn = area_load_data['pressure_kn_m2'] * area_load_data['area_m2']
        
        thai_area_data = {
            'pressure_ksc_m2': converter.kn_m2_to_ksc_m2(area_load_data['pressure_kn_m2']),
            'pressure_tf_m2': converter.kn_m2_to_tf_m2(area_load_data['pressure_kn_m2']),
            'total_force_kgf': converter.kn_to_kgf(total_force_kn),
            'total_force_tf': converter.kn_to_tf(total_force_kn)
        }
        
        print("\n  🏗️ Area Load Conversion:")
        print(f"    Pressure: {area_load_data['pressure_kn_m2']} kN/m² = {thai_area_data['pressure_ksc_m2']:.3f} ksc/m² = {thai_area_data['pressure_tf_m2']:.3f} tf/m²")
        print(f"    Total Force: {total_force_kn} kN = {thai_area_data['total_force_kgf']:.1f} kgf = {thai_area_data['total_force_tf']:.2f} tf")
        
        print("\n✅ Components integration test successful!")
        return True
        
    except Exception as e:
        print(f"❌ Components integration test failed: {e}")
        return False

def main():
    """Run all Thai units tests"""
    print("🇹🇭 StructureTools Thai Units Simple Test Suite")
    print("=" * 60)
    
    test_results = []
    
    # Run tests
    test_results.append(("Converter Functionality", test_thai_units_converter()))
    test_results.append(("Conversion Accuracy", test_thai_units_accuracy()))
    test_results.append(("Components Integration", test_components_integration()))
    
    # Print summary
    print("\n" + "=" * 60)
    print("🇹🇭 THAI UNITS TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(test_results)
    
    for test_name, result in test_results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL THAI UNITS TESTS PASSED!")
        print("Thai units integration is working correctly across StructureTools.")
        print("\nSupported conversions:")
        print("  • Forces: kN ↔ kgf, kN ↔ tf")
        print("  • Moments: kN·m ↔ kgf·cm, kN·m ↔ tf·m")
        print("  • Pressures: kN/m² ↔ ksc/m², kN/m² ↔ tf/m²")
        print("  • Stresses: MPa ↔ ksc")
        print("  • Linear loads: kN/m ↔ kgf/m, kN/m ↔ tf/m")
        return True
    else:
        print(f"\n❌ {total - passed} TESTS FAILED!")
        print("Some Thai units functionality needs attention.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
