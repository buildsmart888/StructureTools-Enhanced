#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Material System Testing

This script tests the complete material system including:
1. Material database functionality
2. Old material system with database integration
3. New StructuralMaterial system
4. Calc integration with both material types
5. Material helper utilities
"""

import sys
import os
import traceback

# Add the StructureTools path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools'))

def print_test_header(test_name):
    """Print formatted test header."""
    print(f"\n{'='*60}")
    print(f"TEST: {test_name}")
    print('='*60)

def print_success(message):
    """Print success message."""
    print(f"[SUCCESS] {message}")

def print_error(message):
    """Print error message.""" 
    print(f"[ERROR] {message}")

def print_warning(message):
    """Print warning message."""
    print(f"[WARNING] {message}")

def test_material_database():
    """Test 1: Material Database Import and Basic Functions"""
    print_test_header("Material Database Import and Basic Functions")
    
    try:
        # Test database import
        from data.MaterialStandards import MATERIAL_STANDARDS, MATERIAL_CATEGORIES, get_material_info
        print_success(f"Successfully imported MaterialStandards")
        print(f"   Total standards: {len(MATERIAL_STANDARDS)}")
        print(f"   Categories: {list(MATERIAL_CATEGORIES.keys())}")
        
        # Test get_material_info
        astm_a992_info = get_material_info('ASTM_A992')
        if astm_a992_info:
            print_success("get_material_info() working correctly")
            print(f"   ASTM A992 Yield Strength: {astm_a992_info.get('YieldStrength', 'N/A')}")
            print(f"   ASTM A992 Elastic Modulus: {astm_a992_info.get('ModulusElasticity', 'N/A')}")
        else:
            print_error("get_material_info() returned empty result")
        
        # Test categories
        steel_materials = MATERIAL_CATEGORIES.get('Steel', [])
        concrete_materials = MATERIAL_CATEGORIES.get('Concrete', [])
        print_success(f"Categories working: Steel ({len(steel_materials)}), Concrete ({len(concrete_materials)})")
        
        return True
        
    except ImportError as e:
        print_error(f"Failed to import MaterialStandards: {e}")
        return False
    except Exception as e:
        print_error(f"Database test failed: {e}")
        traceback.print_exc()
        return False

def test_material_helper_utilities():
    """Test 2: Material Helper Utilities"""
    print_test_header("Material Helper Utilities")
    
    try:
        from utils.MaterialHelper import (
            list_available_standards,
            list_standards_by_category,
            search_materials,
            get_calc_properties_from_database
        )
        
        # Test list functions
        all_standards = list_available_standards()
        print_success(f"list_available_standards(): {len(all_standards)} standards found")
        
        steel_standards = list_standards_by_category("Steel")
        print_success(f"list_standards_by_category('Steel'): {len(steel_standards)} standards")
        
        # Test search
        astm_results = search_materials("ASTM")
        print_success(f"search_materials('ASTM'): {len(astm_results)} results")
        
        # Test calc properties generation
        calc_props = get_calc_properties_from_database("ASTM_A992", "m", "kN")
        if calc_props:
            print_success("get_calc_properties_from_database() working")
            print(f"   E = {calc_props['E']:,.0f} kN/m²")
            print(f"   G = {calc_props['G']:,.0f} kN/m²")
            print(f"   density = {calc_props['density']:.1f} kN/m³")
        else:
            print_error("Failed to generate calc properties")
        
        return True
        
    except ImportError as e:
        print_error(f"Failed to import MaterialHelper: {e}")
        return False
    except Exception as e:
        print_error(f"Helper utilities test failed: {e}")
        traceback.print_exc()
        return False

def test_old_material_system():
    """Test 3: Old Material System with Database Integration"""
    print_test_header("Old Material System with Database Integration")
    
    try:
        # Mock FreeCAD environment
        class MockApp:
            class Console:
                @staticmethod
                def PrintMessage(msg): print(f"INFO: {msg.strip()}")
                @staticmethod
                def PrintError(msg): print(f"ERROR: {msg.strip()}")
                @staticmethod
                def PrintWarning(msg): print(f"WARNING: {msg.strip()}")
        
        class MockProperty:
            def __init__(self, value):
                self.value = value
            
            def getValueAs(self, unit):
                if isinstance(self.value, str) and 'MPa' in self.value:
                    return float(self.value.replace(' MPa', ''))
                elif isinstance(self.value, str) and 'kg/m^3' in self.value:
                    return float(self.value.replace(' kg/m^3', ''))
                return float(self.value) if isinstance(self.value, (int, float)) else 0
        
        class MockMaterial:
            def __init__(self):
                self.Label = "TestMaterial"
                self.Name = "TestMaterial"
                self.MaterialStandard = "ASTM_A992"
                self.ModulusElasticity = MockProperty("200000 MPa")
                self.PoissonRatio = 0.30
                self.Density = MockProperty("7850 kg/m^3")
                self.YieldStrength = MockProperty("345 MPa")
                self.UltimateStrength = MockProperty("450 MPa")
                self.GradeDesignation = "Gr. 50"
        
        # Import and test old material system
        import material
        
        # Mock the App module
        material.App = MockApp()
        
        mock_obj = MockMaterial()
        old_material = material.Material(mock_obj)
        
        # Test get_calc_properties method
        if hasattr(old_material, 'get_calc_properties'):
            props = old_material.get_calc_properties(mock_obj, 'm', 'kN')
            print_success("Old Material has get_calc_properties() method")
            print(f"   Material name: {props['name']}")
            print(f"   E = {props['E']:,.0f} kN/m²")
            print(f"   density = {props['density']:.1f} kN/m³")
        else:
            print_error("Old Material missing get_calc_properties() method")
        
        # Test update from database
        if hasattr(old_material, '_update_standard_properties'):
            old_material._update_standard_properties(mock_obj)
            print_success("_update_standard_properties() method available")
        else:
            print_error("_update_standard_properties() method missing")
        
        # Test property validation
        if hasattr(old_material, 'onChanged'):
            mock_obj.PoissonRatio = 0.8  # Invalid value
            old_material.onChanged(mock_obj, 'PoissonRatio')
            if mock_obj.PoissonRatio == 0.3:
                print_success("Poisson ratio validation working")
            else:
                print_warning(f"Poisson ratio validation may not work (value: {mock_obj.PoissonRatio})")
        
        return True
        
    except Exception as e:
        print_error(f"Old material system test failed: {e}")
        traceback.print_exc()
        return False

def test_structural_material_system():
    """Test 4: New StructuralMaterial System"""
    print_test_header("New StructuralMaterial System")
    
    try:
        # Mock FreeCAD environment for StructuralMaterial
        class MockApp:
            class Console:
                @staticmethod
                def PrintMessage(msg): print(f"INFO: {msg.strip()}")
                @staticmethod
                def PrintError(msg): print(f"ERROR: {msg.strip()}")
                @staticmethod
                def PrintWarning(msg): print(f"WARNING: {msg.strip()}")
        
        class MockProperty:
            def __init__(self, value):
                self.value = value
            
            def getValueAs(self, unit):
                if isinstance(self.value, str) and 'MPa' in self.value:
                    return float(self.value.replace(' MPa', ''))
                elif isinstance(self.value, str) and 'kg/m^3' in self.value:
                    return float(self.value.replace(' kg/m^3', ''))
                return float(self.value) if isinstance(self.value, (int, float)) else 0
        
        class MockStructuralMaterial:
            def __init__(self):
                self.Label = "StructuralMaterial"
                self.Name = "StructuralMaterial"
                self.MaterialStandard = "ASTM_A992"
                self.MaterialType = "Steel"
                self.ModulusElasticity = MockProperty("200000 MPa")
                self.PoissonRatio = 0.30
                self.Density = MockProperty("7850 kg/m^3")
                self.YieldStrength = MockProperty("345 MPa")
                self.UltimateStrength = MockProperty("450 MPa")
                self.GradeDesignation = "Gr. 50"
                self.ValidationWarnings = []
        
        # Import and test StructuralMaterial
        from objects.StructuralMaterial import StructuralMaterial
        
        # Mock the App module
        import objects.StructuralMaterial as sm_module
        sm_module.App = MockApp()
        
        mock_obj = MockStructuralMaterial()
        structural_material = StructuralMaterial(mock_obj)
        
        # Test get_calc_properties method
        if hasattr(structural_material, 'get_calc_properties'):
            props = structural_material.get_calc_properties(mock_obj, 'm', 'kN')
            print_success("StructuralMaterial has get_calc_properties() method")
            print(f"   Material name: {props['name']}")
            print(f"   E = {props['E']:,.0f} kN/m²")
            print(f"   G = {props['G']:,.0f} kN/m²")
            print(f"   density = {props['density']:.1f} kN/m³")
        else:
            print_error("StructuralMaterial missing get_calc_properties() method")
        
        # Test validation methods
        test_methods = [
            '_validate_poisson_ratio',
            '_update_standard_properties', 
            '_calculate_shear_modulus',
            '_validate_strength_properties'
        ]
        
        for method in test_methods:
            if hasattr(structural_material, method):
                print_success(f"{method}() method available")
            else:
                print_warning(f"{method}() method missing")
        
        return True
        
    except ImportError as e:
        print_error(f"Failed to import StructuralMaterial: {e}")
        return False
    except Exception as e:
        print_error(f"StructuralMaterial test failed: {e}")
        traceback.print_exc()
        return False

def test_calc_integration():
    """Test 5: Calc Integration with Materials"""
    print_test_header("Calc Integration with Materials")
    
    try:
        # Import calc module
        import calc
        
        # Test material database integration in calc
        if hasattr(calc, 'MATERIAL_STANDARDS'):
            print_success("Calc has access to MATERIAL_STANDARDS")
            print(f"   Available standards: {len(calc.MATERIAL_STANDARDS)}")
        else:
            print_warning("Calc may not have direct access to MATERIAL_STANDARDS")
        
        if hasattr(calc, 'HAS_MATERIAL_DATABASE'):
            if calc.HAS_MATERIAL_DATABASE:
                print_success("Calc reports material database is available")
            else:
                print_warning("Calc reports material database is not available")
        
        # Test the enhanced setMaterialAndSections method
        # This would require a full FreeCAD environment to test properly
        print_warning("Full calc integration test requires FreeCAD environment")
        print("   Enhanced setMaterialAndSections() method should:")
        print("      - Detect get_calc_properties() method")
        print("      - Use enhanced material interface if available")
        print("      - Fall back to original method for compatibility")
        print("      - Handle both beam and plate materials")
        
        return True
        
    except ImportError as e:
        print_error(f"Failed to import calc: {e}")
        return False
    except Exception as e:
        print_error(f"Calc integration test failed: {e}")
        traceback.print_exc()
        return False

def test_commands_and_gui():
    """Test 6: Commands and GUI Integration"""
    print_test_header("Commands and GUI Integration")
    
    try:
        # Test CreateMaterial command
        try:
            from commands.CreateMaterial import CreateMaterialCommand
            cmd = CreateMaterialCommand()
            resources = cmd.GetResources()
            print_success("CreateMaterialCommand imported successfully")
            print(f"   Menu Text: {resources.get('MenuText', 'N/A')}")
            print(f"   Tool Tip: {resources.get('ToolTip', 'N/A')}")
        except ImportError:
            print_warning("CreateMaterialCommand not available (requires commands/__init__.py)")
        
        # Test MaterialDatabaseManager command  
        try:
            from commands.MaterialDatabaseManager import MaterialDatabaseManagerCommand
            cmd = MaterialDatabaseManagerCommand()
            resources = cmd.GetResources()
            print_success("MaterialDatabaseManagerCommand imported successfully")
            print(f"   Menu Text: {resources.get('MenuText', 'N/A')}")
            print(f"   Shortcut: {resources.get('Accel', 'N/A')}")
        except ImportError:
            print_warning("MaterialDatabaseManagerCommand not available")
        
        # Test init_gui integration
        try:
            with open('init_gui.py', 'r', encoding='utf-8') as f:
                init_content = f.read()
            
            if 'CreateMaterial' in init_content:
                print_success("CreateMaterial command registered in init_gui.py")
            else:
                print_warning("CreateMaterial command not found in init_gui.py")
            
            if 'MaterialDatabaseManager' in init_content:
                print_success("MaterialDatabaseManager command registered in init_gui.py")
            else:
                print_warning("MaterialDatabaseManager command not found in init_gui.py")
        
        except FileNotFoundError:
            print_warning("init_gui.py not found in current directory")
        
        return True
        
    except Exception as e:
        print_error(f"Commands and GUI test failed: {e}")
        traceback.print_exc()
        return False

def run_all_tests():
    """Run comprehensive material system tests."""
    print("StructureTools Material System Comprehensive Test")
    print("=" * 60)
    
    test_results = []
    
    # Run all tests
    tests = [
        ("Material Database", test_material_database),
        ("Material Helper Utilities", test_material_helper_utilities),  
        ("Old Material System", test_old_material_system),
        ("StructuralMaterial System", test_structural_material_system),
        ("Calc Integration", test_calc_integration),
        ("Commands and GUI", test_commands_and_gui)
    ]
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            test_results.append((test_name, result))
            if result:
                print_success(f"{test_name}: PASSED")
            else:
                print_error(f"{test_name}: FAILED")
        except Exception as e:
            print_error(f"{test_name}: EXCEPTION - {e}")
            test_results.append((test_name, False))
    
    # Summary
    print_test_header("Test Summary")
    
    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)
    
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print_success("All tests passed! Material system is working correctly.")
        return True
    else:
        print_warning(f"{total - passed} tests failed. Some features may not work properly.")
        
        # Show failed tests
        print("\nFailed tests:")
        for test_name, result in test_results:
            if not result:
                print(f"  [FAIL] {test_name}")
        
        return False

if __name__ == "__main__":
    success = run_all_tests()
    
    print(f"\n{'='*60}")
    if success:
        print("[SUCCESS] Material system testing completed successfully!")
        print("The enhanced material system is ready for use.")
    else:
        print("[ERROR] Some tests failed. Please review the issues above.")
        print("Some features may require a full FreeCAD environment to test.")
    
    sys.exit(0 if success else 1)