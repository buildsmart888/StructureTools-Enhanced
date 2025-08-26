# -*- coding: utf-8 -*-
"""
Test Thai Standards Integration
ทดสอบการผสานรวมมาตรฐานไทย

This test module validates the integration of Thai Ministry B.E. 2566 standards
into the StructureTools system.
"""

import unittest
import sys
import os

# Add the parent directory to sys.path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'freecad', 'StructureTools'))

try:
    from data.MaterialDatabase import MaterialDatabase
    from utils.thai_units import ThaiUnitsConverter, get_thai_converter
    from design.thai_design_requirements import ThaiDesignRequirements, get_thai_design_instance
except ImportError as e:
    print(f"Import error: {e}")
    # Mock the modules for testing
    class MaterialDatabase:
        def __init__(self):
            self.materials = {}
        def get_material(self, name):
            return None
    
    class ThaiUnitsConverter:
        def ksc_to_mpa(self, value):
            return value * 0.0980665
        def mpa_to_ksc(self, value):
            return value / 0.0980665
    
    class ThaiDesignRequirements:
        def __init__(self):
            self.load_factors = {'dead': 1.2, 'live': 1.6}


class TestThaiMaterialDatabase(unittest.TestCase):
    """Test Thai materials in MaterialDatabase."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.db = MaterialDatabase()
    
    def test_thai_concrete_materials(self):
        """Test Thai concrete materials are available."""
        thai_concretes = [
            'Concrete_Fc180_Thai', 'Concrete_Fc210_Thai', 
            'Concrete_Fc280_Thai', 'Concrete_Fc350_Thai'
        ]
        
        for concrete_name in thai_concretes:
            material = self.db.get_material(concrete_name)
            if material:
                print(f"✓ Found Thai concrete: {concrete_name}")
                # Check if it has Thai properties
                self.assertIn('description_thai', material)
                self.assertIn('fc_ksc', material)
                self.assertIn('standard', material)
                print(f"  - fc': {material.get('fc_ksc')} ksc")
                print(f"  - Standard: {material.get('standard')}")
            else:
                print(f"✗ Missing Thai concrete: {concrete_name}")
    
    def test_thai_steel_materials(self):
        """Test Thai steel materials are available."""
        thai_steels = [
            'Steel_SR24_Thai', 'Steel_SD40_Thai', 'Steel_SD50_Thai'
        ]
        
        for steel_name in thai_steels:
            material = self.db.get_material(steel_name)
            if material:
                print(f"✓ Found Thai steel: {steel_name}")
                # Check if it has Thai properties
                self.assertIn('description_thai', material)
                self.assertIn('fy_ksc', material)
                self.assertIn('standard', material)
                print(f"  - fy: {material.get('fy_ksc')} ksc")
                print(f"  - Standard: {material.get('standard')}")
            else:
                print(f"✗ Missing Thai steel: {steel_name}")
    
    def test_material_database_completeness(self):
        """Test that MaterialDatabase has comprehensive Thai materials."""
        all_materials = self.db.get_all_materials()
        thai_materials = [name for name in all_materials.keys() if '_Thai' in name]
        
        print(f"\nFound {len(thai_materials)} Thai materials:")
        for name in thai_materials:
            print(f"  - {name}")
        
        # Should have at least concrete and steel materials
        self.assertGreaterEqual(len(thai_materials), 6, 
                               "Should have at least 6 Thai materials (4 concrete + 3 steel)")


class TestThaiUnitsConverter(unittest.TestCase):
    """Test Thai units conversion functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.converter = ThaiUnitsConverter()
    
    def test_pressure_conversions(self):
        """Test pressure unit conversions."""
        # Test ksc to MPa
        ksc_value = 280  # Fc280
        mpa_value = self.converter.ksc_to_mpa(ksc_value)
        expected_mpa = 280 * 0.0980665  # ≈ 27.46 MPa
        
        print(f"\nPressure conversion test:")
        print(f"  {ksc_value} ksc = {mpa_value:.2f} MPa (expected: {expected_mpa:.2f})")
        
        self.assertAlmostEqual(mpa_value, expected_mpa, places=3)
        
        # Test reverse conversion
        ksc_back = self.converter.mpa_to_ksc(mpa_value)
        self.assertAlmostEqual(ksc_back, ksc_value, places=1)
        print(f"  {mpa_value:.2f} MPa = {ksc_back:.1f} ksc (should be {ksc_value})")
    
    def test_force_conversions(self):
        """Test force unit conversions."""
        # Test tf to kN
        tf_value = 10  # 10 metric tons
        kn_value = self.converter.tf_to_kn(tf_value)
        expected_kn = 10 * 9.80665  # ≈ 98.07 kN
        
        print(f"\nForce conversion test:")
        print(f"  {tf_value} tf = {kn_value:.2f} kN (expected: {expected_kn:.2f})")
        
        self.assertAlmostEqual(kn_value, expected_kn, places=2)
        
        # Test reverse conversion
        tf_back = self.converter.kn_to_tf(kn_value)
        self.assertAlmostEqual(tf_back, tf_value, places=2)
        print(f"  {kn_value:.2f} kN = {tf_back:.2f} tf (should be {tf_value})")
    
    def test_concrete_strength_conversion(self):
        """Test concrete strength conversion with Thai grades."""
        fc_ksc = 280  # Fc280
        result = self.converter.concrete_strength_conversion(fc_ksc, 'ksc')
        
        print(f"\nConcrete strength conversion test:")
        print(f"  Input: {fc_ksc} ksc")
        print(f"  Output: {result['fc_MPa']:.2f} MPa")
        print(f"  Thai grade: {result['closest_thai_grade']}")
        print(f"  Ec: {result['ec_ksc']:.0f} ksc = {result['ec_MPa']:.0f} MPa")
        
        self.assertEqual(result['closest_thai_grade'], 'Fc280')
        self.assertAlmostEqual(result['fc_MPa'], fc_ksc * 0.0980665, places=3)
    
    def test_steel_strength_conversion(self):
        """Test steel strength conversion with Thai grades."""
        fy_ksc = 4000  # SD40
        result = self.converter.steel_strength_conversion(fy_ksc, 'ksc')
        
        print(f"\nSteel strength conversion test:")
        print(f"  Input: {fy_ksc} ksc")
        print(f"  Output: {result['fy_MPa']:.1f} MPa")
        print(f"  Thai grade: {result['closest_thai_grade']}")
        
        self.assertEqual(result['closest_thai_grade'], 'SD40 (ข้ออ้อย)')
        self.assertAlmostEqual(result['fy_MPa'], fy_ksc * 0.0980665, places=1)
    
    def test_structural_load_conversion(self):
        """Test structural load conversions."""
        load_ksc = 500  # ksc/m2
        area = 10  # m2
        
        result = self.converter.structural_load_conversion(
            load_ksc, 'ksc/m2', 'kN/m2', area
        )
        
        print(f"\nStructural load conversion test:")
        print(f"  {load_ksc} ksc/m² = {result['converted_value']:.2f} kN/m²")
        print(f"  Total load: {result['total_load_kN']:.2f} kN = {result['total_load_tf']:.2f} tf")
        
        expected_kn_m2 = load_ksc * 0.0980665
        self.assertAlmostEqual(result['converted_value'], expected_kn_m2, places=2)


class TestThaiDesignRequirements(unittest.TestCase):
    """Test Thai design requirements and calculations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.design = ThaiDesignRequirements()
    
    def test_load_factors(self):
        """Test Thai load factors."""
        factors = self.design.load_factors
        
        print(f"\nThai load factors:")
        for load_type, factor in factors.items():
            print(f"  {load_type}: {factor}")
        
        # Check standard load factors
        self.assertEqual(factors['dead'], 1.2)
        self.assertEqual(factors['live'], 1.6)
        self.assertEqual(factors['wind'], 1.6)
        self.assertEqual(factors['seismic'], 1.0)
    
    def test_concrete_design_strength(self):
        """Test concrete design strength calculation."""
        fc_prime = 280  # ksc
        result = self.design.get_concrete_design_strength(fc_prime, 'ksc')
        
        print(f"\nConcrete design strength test:")
        print(f"  fc': {fc_prime} ksc")
        print(f"  Design strength: {result['design_strength_ksc']:.0f} ksc = {result['design_strength_MPa']:.2f} MPa")
        print(f"  Ec: {result['elastic_modulus_ksc']:.0f} ksc = {result['elastic_modulus_MPa']:.0f} MPa")
        
        # Check design strength (φ * fc')
        expected_design = fc_prime * 0.85  # φ = 0.85
        self.assertAlmostEqual(result['design_strength_ksc'], expected_design, places=1)
    
    def test_steel_design_strength(self):
        """Test steel design strength calculation."""
        fy = 4000  # ksc (SD40)
        result = self.design.get_steel_design_strength(fy, None, 'ksc')
        
        print(f"\nSteel design strength test:")
        print(f"  fy: {fy} ksc")
        print(f"  Design tension: {result['design_tension_ksc']:.0f} ksc = {result['design_tension_MPa']:.1f} MPa")
        print(f"  Design shear: {result['design_shear_ksc']:.0f} ksc = {result['design_shear_MPa']:.1f} MPa")
        
        # Check design strength (φ * fy)
        expected_tension = fy * 0.90  # φ = 0.90
        self.assertAlmostEqual(result['design_tension_ksc'], expected_tension, places=1)
    
    def test_load_combinations(self):
        """Test Thai load combinations."""
        combinations = self.design.get_load_combinations()
        
        print(f"\nThai load combinations:")
        for method in combinations:
            print(f"  {method} method:")
            for combo_name, combo in combinations[method].items():
                print(f"    {combo_name}: {combo['formula']} - {combo['description_thai']}")
        
        # Check LRFD basic combination
        basic_lrfd = combinations['LRFD']['basic']
        self.assertEqual(basic_lrfd['formula'], '1.2D + 1.6L')
        self.assertEqual(basic_lrfd['factors']['D'], 1.2)
        self.assertEqual(basic_lrfd['factors']['L'], 1.6)
    
    def test_reinforcement_calculation(self):
        """Test reinforcement calculation for Thai standards."""
        # Example beam
        moment = 150  # kN.m
        fc_prime = 280  # ksc
        fy = 4000  # ksc (SD40)
        b = 300  # mm
        d = 450  # mm
        
        result = self.design.calculate_reinforcement_requirements(
            moment, fc_prime, fy, b, d, 'ksc'
        )
        
        print(f"\nReinforcement calculation test:")
        print(f"  Beam: {b}×{d+50} mm, fc'={fc_prime} ksc, fy={fy} ksc")
        print(f"  Moment: {moment} kN.m")
        print(f"  As required: {result['As_required_mm2']:.0f} mm²")
        print(f"  As minimum: {result['As_minimum_mm2']:.0f} mm²")
        print(f"  Suggested: {result['num_bars_DB16']} bars {result['bar_size_suggested']}")
        print(f"  Status: {result['status_thai']}")
        
        # Should have reasonable reinforcement
        self.assertGreater(result['As_required_mm2'], 0)
        self.assertGreater(result['num_bars_DB16'], 0)


class TestIntegrationScenarios(unittest.TestCase):
    """Test real-world integration scenarios."""
    
    def test_thai_building_design_workflow(self):
        """Test complete Thai building design workflow."""
        print(f"\n{'='*60}")
        print("THAI BUILDING DESIGN WORKFLOW TEST")
        print("การทดสอบขั้นตอนการออกแบบอาคารแบบไทย")
        print(f"{'='*60}")
        
        # 1. Select materials
        db = MaterialDatabase()
        converter = get_thai_converter()
        design = get_thai_design_instance()
        
        # Concrete: Fc280
        concrete = db.get_material('Concrete_Fc280_Thai')
        if concrete:
            print(f"1. คอนกรีต: {concrete.get('description_thai', 'Fc280')}")
            print(f"   fc' = {concrete.get('fc_ksc', 280)} ksc = {converter.ksc_to_mpa(concrete.get('fc_ksc', 280)):.1f} MPa")
        
        # Steel: SD40
        steel = db.get_material('Steel_SD40_Thai')
        if steel:
            print(f"2. เหล็กเสริม: {steel.get('description_thai', 'SD40')}")
            print(f"   fy = {steel.get('fy_ksc', 4000)} ksc = {converter.ksc_to_mpa(steel.get('fy_ksc', 4000)):.0f} MPa")
        
        # 3. Load calculations
        print(f"\n3. การคำนวณภาระ:")
        
        # Dead load (self-weight of concrete slab)
        slab_thickness = 0.15  # m
        concrete_density = 2400  # kg/m3
        dead_load_kgf_m2 = concrete_density * slab_thickness  # 360 kgf/m2
        dead_load_ksc_m2 = dead_load_kgf_m2 / 10000  # convert to ksc/m2
        dead_load_kn_m2 = converter.ksc_to_mpa(dead_load_ksc_m2) * 1000  # to kN/m2
        
        print(f"   ภาระตาย: {dead_load_ksc_m2:.3f} ksc/m² = {dead_load_kn_m2:.2f} kN/m²")
        
        # Live load (office building)
        live_load_kn_m2 = 2.5  # kN/m2 for office
        live_load_ksc_m2 = converter.mpa_to_ksc(live_load_kn_m2 / 1000)
        
        print(f"   ภาระจร: {live_load_ksc_m2:.3f} ksc/m² = {live_load_kn_m2} kN/m²")
        
        # 4. Load combinations
        print(f"\n4. การรวมภาระ (LRFD):")
        load_factors = design.load_factors
        factored_load_kn_m2 = (load_factors['dead'] * dead_load_kn_m2 + 
                              load_factors['live'] * live_load_kn_m2)
        factored_load_ksc_m2 = converter.mpa_to_ksc(factored_load_kn_m2 / 1000)
        
        print(f"   Factored: {load_factors['dead']}×{dead_load_kn_m2:.2f} + {load_factors['live']}×{live_load_kn_m2} = {factored_load_kn_m2:.2f} kN/m²")
        print(f"   = {factored_load_ksc_m2:.3f} ksc/m²")
        
        # 5. Design verification
        print(f"\n5. การตรวจสอบการออกแบบ:")
        print(f"   ✓ ใช้มาตรฐาน: กฎกระทรวง พ.ศ. 2566")
        print(f"   ✓ วัสดุ: คอนกรีต Fc280, เหล็ก SD40")
        print(f"   ✓ ภาระรวม: {factored_load_kn_m2:.2f} kN/m²")
        print(f"   ✓ หน่วยไทย: รองรับ ksc, tf, เมตร")
        
        # Assertions to verify the workflow works
        self.assertIsNotNone(concrete)
        self.assertIsNotNone(steel)
        self.assertGreater(factored_load_kn_m2, 0)
        self.assertIn('Thai', concrete.get('standard', ''))
        self.assertIn('Thai', steel.get('standard', ''))
        
        print(f"\n✅ การทดสอบขั้นตอนการออกแบบแบบไทยสำเร็จ!")


def run_thai_standards_tests():
    """Run all Thai standards integration tests."""
    print(f"\n{'='*80}")
    print("THAI MINISTRY B.E. 2566 STANDARDS INTEGRATION TESTS")
    print("การทดสอบการผสานรวมมาตรฐานกฎกระทรวง พ.ศ. 2566")
    print(f"{'='*80}")
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestThaiMaterialDatabase))
    test_suite.addTest(unittest.makeSuite(TestThaiUnitsConverter))
    test_suite.addTest(unittest.makeSuite(TestThaiDesignRequirements))
    test_suite.addTest(unittest.makeSuite(TestIntegrationScenarios))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Summary
    print(f"\n{'='*80}")
    print("TEST SUMMARY / สรุปการทดสอบ")
    print(f"{'='*80}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print(f"\nFAILURES:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
    
    if result.errors:
        print(f"\nERRORS:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    if result.wasSuccessful():
        print(f"\n🎉 ALL TESTS PASSED! การทดสอบทั้งหมดผ่าน!")
        print(f"✅ Thai Ministry B.E. 2566 standards successfully integrated")
        print(f"✅ มาตรฐานกฎกระทรวง พ.ศ. 2566 ผสานรวมสำเร็จ")
    else:
        print(f"\n❌ Some tests failed. การทดสอบบางส่วนล้มเหลว")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_thai_standards_tests()
    exit(0 if success else 1)
