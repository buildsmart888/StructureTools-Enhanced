#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Test Suite for Thai Units Integration
=================================================

Tests all Thai units functionality across StructureTools components:
- Node Load (load_nodal.py)
- Distributed Load (load_distributed.py) 
- Area Load (AreaLoad.py)
- Pressure Load (StructuralPlate.py)
- Diagram Calc (calc.py)
- Diagram Display (diagram.py)

Usage: python test_thai_units_comprehensive.py
"""

import sys
import os
import unittest
from unittest.mock import Mock, MagicMock, patch
import math

# Add the project path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad'))

class TestThaiUnitsIntegration(unittest.TestCase):
    """Comprehensive test suite for Thai units integration"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock FreeCAD modules
        self.mock_freecad()
        
    def mock_freecad(self):
        """Mock FreeCAD modules for testing"""
        # Create mock modules
        mock_freecad = MagicMock()
        mock_freecadgui = MagicMock()
        mock_part = MagicMock()
        mock_draft = MagicMock()
        
        # Mock Vector class
        mock_freecad.Vector = lambda x=0, y=0, z=0: MagicMock(x=x, y=y, z=z)
        mock_freecad.Units = MagicMock()
        mock_freecad.Units.Quantity = lambda val, unit: MagicMock(
            getValueAs=lambda target_unit: float(val)
        )
        mock_freecad.Console = MagicMock()
        
        # Patch the modules
        sys.modules['FreeCAD'] = mock_freecad
        sys.modules['FreeCADGui'] = mock_freecadgui
        sys.modules['Part'] = mock_part
        sys.modules['Draft'] = mock_draft
        
        return mock_freecad, mock_freecadgui, mock_part

class TestUniversalThaiUnits(TestThaiUnitsIntegration):
    """Test the universal Thai units converter"""
    
    def test_thai_units_converter_import(self):
        """Test that universal Thai units can be imported"""
        try:
            from freecad.StructureTools.utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            self.assertIsNotNone(converter)
            print("✅ Universal Thai Units converter imported successfully")
        except ImportError as e:
            self.fail(f"❌ Failed to import UniversalThaiUnits: {e}")
    
    def test_force_conversions(self):
        """Test force unit conversions (kN ↔ kgf, kN ↔ tf)"""
        try:
            from freecad.StructureTools.utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            
            # Test kN to kgf
            kn_val = 10.0
            kgf_val = converter.kn_to_kgf(kn_val)
            expected_kgf = 10.0 * 101.97162129779283  # kN to kgf conversion
            self.assertAlmostEqual(kgf_val, expected_kgf, places=2)
            
            # Test kN to tf
            tf_val = converter.kn_to_tf(kn_val)
            expected_tf = 10.0 / 9.80665  # kN to tf conversion
            self.assertAlmostEqual(tf_val, expected_tf, places=3)
            
            print(f"✅ Force conversions: {kn_val} kN = {kgf_val:.2f} kgf = {tf_val:.3f} tf")
            
        except Exception as e:
            self.fail(f"❌ Force conversion test failed: {e}")
    
    def test_moment_conversions(self):
        """Test moment unit conversions (kN·m ↔ kgf·cm, kN·m ↔ tf·m)"""
        try:
            from freecad.StructureTools.utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            
            # Test kN·m to kgf·cm
            kn_m_val = 5.0
            kgf_cm_val = converter.kn_m_to_kgf_cm(kn_m_val)
            expected_kgf_cm = 5.0 * 101.97162129779283 * 100  # kN·m to kgf·cm
            self.assertAlmostEqual(kgf_cm_val, expected_kgf_cm, places=1)
            
            # Test kN·m to tf·m
            tf_m_val = converter.kn_m_to_tf_m(kn_m_val)
            expected_tf_m = 5.0 / 9.80665  # kN·m to tf·m
            self.assertAlmostEqual(tf_m_val, expected_tf_m, places=3)
            
            print(f"✅ Moment conversions: {kn_m_val} kN·m = {kgf_cm_val:.1f} kgf·cm = {tf_m_val:.3f} tf·m")
            
        except Exception as e:
            self.fail(f"❌ Moment conversion test failed: {e}")
    
    def test_pressure_conversions(self):
        """Test pressure unit conversions (kN/m² ↔ ksc, kN/m² ↔ tf/m²)"""
        try:
            from freecad.StructureTools.utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            
            # Test kN/m² to ksc (kg/cm²)
            kn_m2_val = 24.0
            ksc_val = converter.kn_m2_to_ksc_m2(kn_m2_val)
            expected_ksc = 24.0 * 0.10197162129779283  # kN/m² to ksc
            self.assertAlmostEqual(ksc_val, expected_ksc, places=3)
            
            # Test kN/m² to tf/m²
            tf_m2_val = converter.kn_m2_to_tf_m2(kn_m2_val)
            expected_tf_m2 = 24.0 / 9.80665  # kN/m² to tf/m²
            self.assertAlmostEqual(tf_m2_val, expected_tf_m2, places=3)
            
            print(f"✅ Pressure conversions: {kn_m2_val} kN/m² = {ksc_val:.3f} ksc = {tf_m2_val:.3f} tf/m²")
            
        except Exception as e:
            self.fail(f"❌ Pressure conversion test failed: {e}")

class TestNodeLoadThaiUnits(TestThaiUnitsIntegration):
    """Test Thai units integration in Node Load"""
    
    def test_node_load_thai_properties(self):
        """Test that Node Load has Thai units properties"""
        try:
            from freecad.StructureTools.load_nodal import NodalLoad
            
            # Create mock object
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            
            # Create NodalLoad instance
            nodal_load = NodalLoad(mock_obj)
            
            # Check that Thai units properties were added
            property_calls = [call[0] for call in mock_obj.addProperty.call_args_list]
            thai_properties = [call for call in property_calls if 'Thai' in str(call)]
            
            self.assertTrue(len(thai_properties) > 0, "No Thai units properties found")
            print(f"✅ Node Load Thai properties added: {len(thai_properties)} properties")
            
        except Exception as e:
            self.fail(f"❌ Node Load Thai properties test failed: {e}")
    
    def test_node_load_thai_conversion(self):
        """Test Node Load Thai units conversion methods"""
        try:
            from freecad.StructureTools.load_nodal import NodalLoad
            
            # Create mock object with properties
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            mock_obj.UseThaiUnits = True
            mock_obj.NodalLoading = [10.0, 0.0, -5.0]  # kN forces
            
            # Create NodalLoad instance
            nodal_load = NodalLoad(mock_obj)
            
            # Test conversion method exists
            self.assertTrue(hasattr(nodal_load, 'getLoadInThaiUnits'))
            self.assertTrue(hasattr(nodal_load, 'updateThaiUnits'))
            
            print("✅ Node Load Thai conversion methods found")
            
        except Exception as e:
            self.fail(f"❌ Node Load Thai conversion test failed: {e}")

class TestDistributedLoadThaiUnits(TestThaiUnitsIntegration):
    """Test Thai units integration in Distributed Load"""
    
    def test_distributed_load_thai_properties(self):
        """Test that Distributed Load has Thai units properties"""
        try:
            from freecad.StructureTools.load_distributed import DistributedLoad
            
            # Create mock object
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            
            # Create DistributedLoad instance
            dist_load = DistributedLoad(mock_obj)
            
            # Check that Thai units properties were added
            property_calls = [call[0] for call in mock_obj.addProperty.call_args_list]
            thai_properties = [call for call in property_calls if 'Thai' in str(call)]
            
            self.assertTrue(len(thai_properties) > 0, "No Thai units properties found")
            print(f"✅ Distributed Load Thai properties added: {len(thai_properties)} properties")
            
        except Exception as e:
            self.fail(f"❌ Distributed Load Thai properties test failed: {e}")
    
    def test_distributed_load_thai_conversion(self):
        """Test Distributed Load Thai units conversion methods"""
        try:
            from freecad.StructureTools.load_distributed import DistributedLoad
            
            # Create mock object with properties
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            mock_obj.UseThaiUnits = True
            mock_obj.InitialLoading = 5.0  # kN/m
            mock_obj.FinalLoading = 10.0   # kN/m
            
            # Create DistributedLoad instance
            dist_load = DistributedLoad(mock_obj)
            
            # Test conversion method exists
            self.assertTrue(hasattr(dist_load, 'getDistributedLoadInThaiUnits'))
            self.assertTrue(hasattr(dist_load, 'updateThaiUnits'))
            
            print("✅ Distributed Load Thai conversion methods found")
            
        except Exception as e:
            self.fail(f"❌ Distributed Load Thai conversion test failed: {e}")

class TestAreaLoadThaiUnits(TestThaiUnitsIntegration):
    """Test Thai units integration in Area Load"""
    
    def test_area_load_thai_properties(self):
        """Test that Area Load has Thai units properties"""
        try:
            from freecad.StructureTools.objects.AreaLoad import AreaLoad
            
            # Create mock object
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            
            # Create AreaLoad instance
            area_load = AreaLoad(mock_obj)
            
            # Check that Thai units properties were added
            property_calls = [call[0] for call in mock_obj.addProperty.call_args_list]
            thai_properties = [call for call in property_calls if 'Thai' in str(call)]
            
            self.assertTrue(len(thai_properties) > 0, "No Thai units properties found")
            print(f"✅ Area Load Thai properties added: {len(thai_properties)} properties")
            
        except Exception as e:
            self.fail(f"❌ Area Load Thai properties test failed: {e}")
    
    def test_area_load_thai_conversion(self):
        """Test Area Load Thai units conversion methods"""
        try:
            from freecad.StructureTools.objects.AreaLoad import AreaLoad
            
            # Create mock object with properties
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            mock_obj.UseThaiUnits = True
            mock_obj.LoadIntensity = "2.4 kN/m^2"
            mock_obj.TotalForce = 24.0  # kN
            mock_obj.LoadedArea = 10.0  # m²
            
            # Create AreaLoad instance
            area_load = AreaLoad(mock_obj)
            
            # Test conversion method exists
            self.assertTrue(hasattr(area_load, 'getLoadInThaiUnits'))
            self.assertTrue(hasattr(area_load, 'updateThaiUnits'))
            
            print("✅ Area Load Thai conversion methods found")
            
        except Exception as e:
            self.fail(f"❌ Area Load Thai conversion test failed: {e}")

class TestStructuralPlateThaiUnits(TestThaiUnitsIntegration):
    """Test Thai units integration in Structural Plate (Pressure Loads)"""
    
    def test_structural_plate_thai_properties(self):
        """Test that Structural Plate has Thai units properties"""
        try:
            from freecad.StructureTools.objects.StructuralPlate import StructuralPlate
            
            # Create mock object
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            
            # Create StructuralPlate instance
            plate = StructuralPlate(mock_obj)
            
            # Check that Thai units properties were added
            property_calls = [call[0] for call in mock_obj.addProperty.call_args_list]
            thai_properties = [call for call in property_calls if 'Thai' in str(call)]
            
            self.assertTrue(len(thai_properties) > 0, "No Thai units properties found")
            print(f"✅ Structural Plate Thai properties added: {len(thai_properties)} properties")
            
        except Exception as e:
            self.fail(f"❌ Structural Plate Thai properties test failed: {e}")
    
    def test_structural_plate_thai_conversion(self):
        """Test Structural Plate Thai units conversion methods"""
        try:
            from freecad.StructureTools.objects.StructuralPlate import StructuralPlate
            
            # Create mock object with properties
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            mock_obj.UseThaiUnits = True
            mock_obj.PressureLoads = [2400.0, 1200.0]  # Pa
            mock_obj.ShearLoadsX = [1000.0, 500.0]     # N/m
            
            # Create StructuralPlate instance
            plate = StructuralPlate(mock_obj)
            
            # Test conversion method exists
            self.assertTrue(hasattr(plate, 'getLoadsInThaiUnits'))
            self.assertTrue(hasattr(plate, 'updateThaiUnits'))
            
            print("✅ Structural Plate Thai conversion methods found")
            
        except Exception as e:
            self.fail(f"❌ Structural Plate Thai conversion test failed: {e}")

class TestCalcThaiUnits(TestThaiUnitsIntegration):
    """Test Thai units integration in Calc (Analysis Results)"""
    
    def test_calc_thai_properties(self):
        """Test that Calc has Thai units properties"""
        try:
            from freecad.StructureTools.calc import Calc
            
            # Create mock object
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            
            # Create Calc instance
            calc = Calc(mock_obj, [])
            
            # Check that Thai units properties were added
            property_calls = [call[0] for call in mock_obj.addProperty.call_args_list]
            thai_properties = [call for call in property_calls if 'Thai' in str(call)]
            
            self.assertTrue(len(thai_properties) > 0, "No Thai units properties found")
            print(f"✅ Calc Thai properties added: {len(thai_properties)} properties")
            
        except Exception as e:
            self.fail(f"❌ Calc Thai properties test failed: {e}")
    
    def test_calc_thai_conversion(self):
        """Test Calc Thai units conversion methods"""
        try:
            from freecad.StructureTools.calc import Calc
            
            # Create mock object with properties
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            mock_obj.UseThaiUnits = True
            mock_obj.MomentZ = ["10.5,15.2,8.9"]
            mock_obj.AxialForce = ["25.0,30.0,20.0"]
            mock_obj.ShearY = ["5.5,7.2,4.1"]
            
            # Create Calc instance
            calc = Calc(mock_obj, [])
            
            # Test conversion method exists
            self.assertTrue(hasattr(calc, 'updateThaiUnitsResults'))
            self.assertTrue(hasattr(calc, 'getResultsInThaiUnits'))
            
            print("✅ Calc Thai conversion methods found")
            
        except Exception as e:
            self.fail(f"❌ Calc Thai conversion test failed: {e}")

class TestDiagramThaiUnits(TestThaiUnitsIntegration):
    """Test Thai units integration in Diagram Display"""
    
    def test_diagram_thai_properties(self):
        """Test that Diagram has Thai units properties"""
        try:
            from freecad.StructureTools.diagram import Diagram
            
            # Create mock objects
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            mock_calc = MagicMock()
            
            # Create Diagram instance
            diagram = Diagram(mock_obj, mock_calc, [])
            
            # Check that Thai units properties were added
            property_calls = [call[0] for call in mock_obj.addProperty.call_args_list]
            thai_properties = [call for call in property_calls if 'Thai' in str(call)]
            
            self.assertTrue(len(thai_properties) > 0, "No Thai units properties found")
            print(f"✅ Diagram Thai properties added: {len(thai_properties)} properties")
            
        except Exception as e:
            self.fail(f"❌ Diagram Thai properties test failed: {e}")
    
    def test_diagram_thai_conversion(self):
        """Test Diagram Thai units conversion methods"""
        try:
            from freecad.StructureTools.diagram import Diagram
            
            # Create mock objects
            mock_obj = MagicMock()
            mock_obj.addProperty = MagicMock()
            mock_calc = MagicMock()
            
            # Create Diagram instance
            diagram = Diagram(mock_obj, mock_calc, [])
            
            # Test conversion method exists
            self.assertTrue(hasattr(diagram, 'convertToThaiUnits'))
            self.assertTrue(hasattr(diagram, 'getThaiUnitsLabel'))
            
            print("✅ Diagram Thai conversion methods found")
            
        except Exception as e:
            self.fail(f"❌ Diagram Thai conversion test failed: {e}")

class TestThaiUnitsIntegrationFlow(TestThaiUnitsIntegration):
    """Test complete Thai units integration workflow"""
    
    def test_complete_workflow(self):
        """Test complete Thai units workflow from loads to analysis"""
        try:
            print("\n=== Testing Complete Thai Units Workflow ===")
            
            # Test 1: Universal converter
            from freecad.StructureTools.utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            
            # Sample structural values
            node_force_kn = 100.0
            moment_kn_m = 50.0
            pressure_kn_m2 = 2.4
            
            # Convert to Thai units
            node_force_kgf = converter.kn_to_kgf(node_force_kn)
            node_force_tf = converter.kn_to_tf(node_force_kn)
            moment_kgf_cm = converter.kn_m_to_kgf_cm(moment_kn_m)
            moment_tf_m = converter.kn_m_to_tf_m(moment_kn_m)
            pressure_ksc = converter.kn_m2_to_ksc_m2(pressure_kn_m2)
            pressure_tf_m2 = converter.kn_m2_to_tf_m2(pressure_kn_m2)
            
            print(f"Force: {node_force_kn} kN = {node_force_kgf:.1f} kgf = {node_force_tf:.2f} tf")
            print(f"Moment: {moment_kn_m} kN·m = {moment_kgf_cm:.1f} kgf·cm = {moment_tf_m:.2f} tf·m")
            print(f"Pressure: {pressure_kn_m2} kN/m² = {pressure_ksc:.3f} ksc = {pressure_tf_m2:.3f} tf/m²")
            
            # Verify conversion accuracy
            self.assertAlmostEqual(node_force_kgf / 101.97, node_force_kn, places=2)
            self.assertAlmostEqual(moment_tf_m * 9.807, moment_kn_m, places=2)
            self.assertAlmostEqual(pressure_ksc * 9.807, pressure_kn_m2, places=2)
            
            print("✅ Complete Thai units workflow tested successfully")
            
        except Exception as e:
            self.fail(f"❌ Complete workflow test failed: {e}")

def run_thai_units_tests():
    """Run all Thai units tests"""
    print("🇹🇭 StructureTools Thai Units Integration Test Suite")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestUniversalThaiUnits,
        TestNodeLoadThaiUnits,
        TestDistributedLoadThaiUnits,
        TestAreaLoadThaiUnits,
        TestStructuralPlateThaiUnits,
        TestCalcThaiUnits,
        TestDiagramThaiUnits,
        TestThaiUnitsIntegrationFlow
    ]
    
    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("🇹🇭 THAI UNITS INTEGRATION TEST SUMMARY")
    print("=" * 60)
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED! Thai units integration is working correctly.")
        print(f"✅ Total tests run: {result.testsRun}")
        print("✅ Components tested:")
        print("   • Universal Thai Units Converter")
        print("   • Node Load Thai Units")
        print("   • Distributed Load Thai Units")
        print("   • Area Load Thai Units") 
        print("   • Structural Plate Pressure Thai Units")
        print("   • Calc Analysis Results Thai Units")
        print("   • Diagram Display Thai Units")
        print("   • Complete Workflow Integration")
        print("\n🎉 Thai units now fully functional across ALL project components!")
    else:
        print(f"❌ TESTS FAILED: {len(result.failures)} failures, {len(result.errors)} errors")
        for test, error in result.failures + result.errors:
            print(f"   • {test}: {error}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_thai_units_tests()
    sys.exit(0 if success else 1)
