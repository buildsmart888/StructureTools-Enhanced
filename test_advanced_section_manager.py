# -*- coding: utf-8 -*-
"""
Test script for Advanced Section Manager
สคริปต์ทดสอบ Advanced Section Manager
"""

import FreeCAD as App

def test_safe_steelpy_integration():
    """Test the safe steelpy integration"""
    print("Testing Safe SteelPy Integration:")
    print("=" * 50)
    
    try:
        from freecad.StructureTools.data.SteelPyIntegrationFixed import (
            get_steelpy_manager, get_available_shape_types, 
            get_sections_for_shape, get_section_data, 
            search_steel_sections, test_steelpy_integration
        )
        
        # Run the built-in test
        success = test_steelpy_integration()
        
        if success:
            print("\n[OK] Safe steelpy integration is working!")
            
            # Test specific functions
            manager = get_steelpy_manager()
            print(f"Manager available: {manager.available}")
            
            if manager.available:
                # Test shape types
                shape_types = get_available_shape_types()
                print(f"Available shape types: {len(shape_types)}")
                for key, info in list(shape_types.items())[:3]:
                    print(f"  {key}: {info['name']} ({info['count']} sections)")
                
                # Test section search
                if shape_types:
                    first_shape = list(shape_types.keys())[0]
                    sections = get_sections_for_shape(first_shape)
                    print(f"Sections in {first_shape}: {len(sections)}")
                    
                    if sections:
                        # Test section properties
                        sample_section = sections[0]
                        properties = get_section_data(first_shape, sample_section)
                        if properties:
                            print(f"Sample section {sample_section} properties:")
                            for key, value in list(properties.items())[:5]:
                                print(f"  {key}: {value}")
        else:
            print("\n[ERROR] Safe steelpy integration failed!")
            
    except Exception as e:
        print(f"[ERROR] Failed to test steelpy integration: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return success

def test_advanced_section_manager_gui():
    """Test the Advanced Section Manager GUI"""
    print("\nTesting Advanced Section Manager GUI:")
    print("=" * 50)
    
    try:
        from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui
        
        # Try to open the GUI
        gui = show_section_manager_gui()
        
        if gui:
            print("[OK] Advanced Section Manager GUI opened successfully!")
            
            # Test database connection
            if hasattr(gui, 'steelpy_db'):
                print(f"SteelPy database available: {gui.steelpy_db.available}")
                if gui.steelpy_db.available:
                    print(f"Shape types loaded: {len(gui.steelpy_db.shape_types)}")
            
            # Test ArchProfile integration
            if hasattr(gui, 'arch_integration'):
                print(f"Arch integration available: {gui.arch_integration.available}")
            
            return True
        else:
            print("[ERROR] Failed to open Advanced Section Manager GUI!")
            return False
            
    except Exception as e:
        print(f"[ERROR] GUI test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_command_registration():
    """Test command registration"""
    print("\nTesting Command Registration:")
    print("=" * 50)
    
    try:
        import FreeCADGui as Gui
        
        # Check if command is registered
        commands = Gui.listCommands()
        
        if 'StructureTools_AdvancedSectionManager' in commands:
            print("[OK] Advanced Section Manager command is registered")
            
            # Try to run the command
            try:
                Gui.runCommand('StructureTools_AdvancedSectionManager')
                print("[OK] Command executed successfully")
                return True
            except Exception as e:
                print(f"[ERROR] Command execution failed: {e}")
                return False
        else:
            print("[ERROR] Advanced Section Manager command not found")
            print("Available StructureTools commands:")
            structure_commands = [cmd for cmd in commands if 'StructureTools' in cmd or 'Structure' in cmd]
            for cmd in structure_commands:
                print(f"  - {cmd}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Command registration test failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("Advanced Section Manager - Comprehensive Test")
    print("=" * 60)
    
    tests = [
        ("Safe SteelPy Integration", test_safe_steelpy_integration),
        ("Advanced Section Manager GUI", test_advanced_section_manager_gui), 
        ("Command Registration", test_command_registration)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"[ERROR] {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "[OK]" if result else "[FAIL]"
        print(f"  {symbol} {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("\nAdvanced Section Manager is ready to use:")
        print("1. Click the 'Advanced Section Manager' button in StructureTools toolbar")
        print("2. Or run: Gui.runCommand('StructureTools_AdvancedSectionManager')")
        print("3. Select sections from steelpy database and create StructureTools objects")
    else:
        print(f"\n⚠️  {total-passed} test(s) failed - needs attention")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # This should be run from FreeCAD Python console
    try:
        import FreeCAD
        print(f"Running in FreeCAD {FreeCAD.Version()}")
        run_all_tests()
    except ImportError:
        print("This test should be run from FreeCAD Python console")
        print("Copy and paste this code into FreeCAD:")
        print("exec(open(r'C:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools\\test_advanced_section_manager.py').read())")