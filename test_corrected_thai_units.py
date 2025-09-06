#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrected Thai Units Test - Fixed MPa to ksc conversion
Testing the CORRECT conversion: 1 MPa = 10.19716 ksc
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad'))

def test_corrected_conversion_factors():
    """Test the corrected conversion factors"""
    print("🔧 Testing CORRECTED Thai Units Conversion")
    print("=" * 60)
    
    try:
        from StructureTools.utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        # Test the corrected conversion factor
        print("📋 Conversion Factor Verification:")
        print(f"   MPA_TO_KSC = {converter.MPA_TO_KSC}")
        print(f"   KSC_TO_MPA = {converter.KSC_TO_MPA}")
        print(f"   Expected: 10.19716 and 0.0980665")
        
        # Verify with exact values
        assert abs(converter.MPA_TO_KSC - 10.19716) < 0.001, f"Wrong conversion factor: {converter.MPA_TO_KSC}"
        assert abs(converter.KSC_TO_MPA - 0.0980665) < 0.0001, f"Wrong conversion factor: {converter.KSC_TO_MPA}"
        print("   ✅ Conversion factors are CORRECT!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_thai_steel_conversions():
    """Test Thai steel grade conversions with corrected values"""
    print("\n🔧 Thai Steel Grades (CORRECTED)")
    print("=" * 60)
    
    try:
        from StructureTools.utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        # Thai steel grades with expected values
        steel_grades = [
            ("SD30", 300, 400, 3059.1, 4078.9),   # fy_mpa, fu_mpa, fy_ksc_expected, fu_ksc_expected
            ("SD40", 400, 520, 4078.9, 5302.5),
            ("SS400", 245, 400, 2498.3, 4078.9),
            ("SM490", 325, 490, 3314.1, 4996.6)
        ]
        
        print("Grade    | Yield (MPa → ksc)      | Ultimate (MPa → ksc)")
        print("-" * 60)
        
        all_correct = True
        for grade, fy_mpa, fu_mpa, fy_expected, fu_expected in steel_grades:
            fy_ksc = converter.mpa_to_ksc(fy_mpa)
            fu_ksc = converter.mpa_to_ksc(fu_mpa)
            
            fy_correct = abs(fy_ksc - fy_expected) < 1.0
            fu_correct = abs(fu_ksc - fu_expected) < 1.0
            
            fy_status = "✅" if fy_correct else "❌"
            fu_status = "✅" if fu_correct else "❌"
            
            print(f"{grade:8} | {fy_mpa:3.0f} → {fy_ksc:6.0f} {fy_status} | {fu_mpa:3.0f} → {fu_ksc:6.0f} {fu_status}")
            
            if not (fy_correct and fu_correct):
                all_correct = False
        
        return all_correct
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_thai_concrete_conversions():
    """Test Thai concrete grade conversions with corrected values"""
    print("\n🏗️ Thai Concrete Grades (CORRECTED)")
    print("=" * 60)
    
    try:
        from StructureTools.utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        # Thai concrete grades with expected values
        concrete_grades = [
            ("Fc175", 17.5, 178.5),    # fc_mpa, fc_ksc_expected
            ("Fc210", 21.0, 214.1),
            ("Fc240", 24.0, 244.7),
            ("Fc280", 28.0, 285.5),
            ("Fc350", 35.0, 356.9)
        ]
        
        print("Grade  | fc (MPa → ksc)")
        print("-" * 30)
        
        all_correct = True
        for grade, fc_mpa, fc_expected in concrete_grades:
            fc_ksc = converter.mpa_to_ksc(fc_mpa)
            correct = abs(fc_ksc - fc_expected) < 1.0
            status = "✅" if correct else "❌"
            
            print(f"{grade:6} | {fc_mpa:4.1f} → {fc_ksc:5.0f} {status}")
            
            if not correct:
                all_correct = False
        
        return all_correct
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_elastic_modulus_conversions():
    """Test elastic modulus conversions with corrected values"""
    print("\n📊 Elastic Modulus (CORRECTED)")
    print("=" * 60)
    
    try:
        from StructureTools.utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        # Modulus values with expected results
        modulus_tests = [
            ("Steel", 200000, 2039432),        # E_mpa, E_ksc_expected
            ("Concrete (Fc280)", 30000, 305915),
            ("Aluminum", 70000, 713801)
        ]
        
        print("Material           | E (MPa → ksc)")
        print("-" * 50)
        
        all_correct = True
        for material, e_mpa, e_expected in modulus_tests:
            e_ksc = converter.mpa_to_ksc(e_mpa)
            correct = abs(e_ksc - e_expected) < 1000  # Allow 1000 ksc tolerance
            status = "✅" if correct else "❌"
            
            print(f"{material:18} | {e_mpa/1000:3.0f} GPa → {e_ksc/1000:4.0f}k ksc {status}")
            
            if not correct:
                all_correct = False
        
        return all_correct
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_reverse_conversions():
    """Test reverse conversions ksc → MPa"""
    print("\n🔄 Reverse Conversions (ksc → MPa)")
    print("=" * 60)
    
    try:
        from StructureTools.utils.universal_thai_units import UniversalThaiUnits
        converter = UniversalThaiUnits()
        
        # Test round-trip conversions
        test_values_mpa = [28.0, 300.0, 400.0, 200000.0]
        
        print("Original (MPa) | MPa→ksc→MPa | Accuracy")
        print("-" * 45)
        
        all_correct = True
        for original_mpa in test_values_mpa:
            ksc_value = converter.mpa_to_ksc(original_mpa)
            back_to_mpa = converter.ksc_to_mpa(ksc_value)
            
            error = abs(back_to_mpa - original_mpa)
            accuracy = 100 * (1 - error / original_mpa)
            correct = accuracy > 99.9
            status = "✅" if correct else "❌"
            
            print(f"{original_mpa:11.1f} | {back_to_mpa:11.2f} | {accuracy:6.2f}% {status}")
            
            if not correct:
                all_correct = False
        
        return all_correct
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_units_manager():
    """Test the new units manager system"""
    print("\n⚙️ Testing Units Manager System")
    print("=" * 60)
    
    try:
        from StructureTools.utils.units_manager import get_units_manager, UnitsManager
        
        manager = get_units_manager()
        print(f"✅ Units manager created successfully")
        print(f"   Current system: {manager.get_preferred_units()}")
        print(f"   Thai available: {manager.thai_available}")
        print(f"   Show both units: {manager.show_both_units()}")
        
        # Test formatting functions
        print("\n📋 Testing Formatting Functions:")
        
        # Test stress formatting
        stress_mpa = 400.0
        formatted_stress = manager.format_stress(stress_mpa, "steel")
        print(f"   Steel 400 MPa: {formatted_stress}")
        
        # Test modulus formatting  
        modulus_mpa = 200000.0
        formatted_modulus = manager.format_modulus(modulus_mpa, "steel")
        print(f"   Steel 200 GPa: {formatted_modulus}")
        
        # Test Thai units mode
        print("\n🇹🇭 Testing Thai Units Mode:")
        manager.set_preferred_units(UnitsManager.THAI_UNITS)
        
        formatted_stress_thai = manager.format_stress(stress_mpa, "steel")
        formatted_modulus_thai = manager.format_modulus(modulus_mpa, "steel")
        
        print(f"   Steel 400 MPa: {formatted_stress_thai}")
        print(f"   Steel 200 GPa: {formatted_modulus_thai}")
        
        # Reset to SI
        manager.set_preferred_units(UnitsManager.SI_UNITS)
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🇹🇭 CORRECTED Thai Units Test")
    print("Fixed conversion: 1 MPa = 10.19716 ksc (NOT 1.02 ksc!)")
    print("=" * 70)
    
    # Run all tests
    tests = [
        ("Conversion Factors", test_corrected_conversion_factors),
        ("Thai Steel Grades", test_thai_steel_conversions),
        ("Thai Concrete Grades", test_thai_concrete_conversions),
        ("Elastic Modulus", test_elastic_modulus_conversions),
        ("Reverse Conversions", test_reverse_conversions),
        ("Units Manager", test_units_manager)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 70)
    print("🏆 TEST SUMMARY")
    print("=" * 70)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:20}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 ALL TESTS PASSED!")
        print("🇹🇭 Thai units conversions are now CORRECT!")
        print("   • 1 MPa = 10.19716 ksc ✅")
        print("   • Steel SD40: 400 MPa = 4,079 ksc ✅")  
        print("   • Concrete Fc280: 28 MPa = 286 ksc ✅")
        print("   • Units manager working ✅")
        print("\n💪 StructureTools พร้อมใช้หน่วยไทยที่ถูกต้องแล้ว!")
    else:
        print(f"\n❌ {len(results)-passed} TESTS FAILED")
        print("Need to fix remaining issues")
    
    print("\nกดเพื่อออก...")
    input()
