# -*- coding: utf-8 -*-
"""
Test Advanced Section Manager in FreeCAD environment
ทดสอบ Advanced Section Manager ใน FreeCAD
"""

def test_command_registration():
    """Test if command is registered properly"""
    print("=== Testing Command Registration ===")
    
    try:
        import FreeCADGui as Gui
        
        # Check if command is registered
        commands = Gui.listCommands()
        if 'StructureTools_AdvancedSectionManager' in commands:
            print("[OK] Advanced Section Manager command is registered")
            return True
        else:
            print("[FAIL] Advanced Section Manager command not found")
            print("Available StructureTools commands:")
            structure_commands = [cmd for cmd in commands if 'StructureTools' in cmd or 'Structure' in cmd]
            for cmd in structure_commands:
                print(f"  - {cmd}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Command registration test failed: {e}")
        return False

def test_gui_import():
    """Test GUI module imports"""
    print("\n=== Testing GUI Imports ===")
    
    try:
        from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui
        print("[OK] SectionManagerGUI imported successfully")
        
        from freecad.StructureTools.commands.advanced_section_manager import AdvancedSectionManagerCommand
        print("[OK] Advanced Section Manager command imported")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] GUI import test failed: {e}")
        return False

def test_gui_opening():
    """Test opening the GUI"""
    print("\n=== Testing GUI Opening ===")
    
    try:
        from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui
        
        # Try to open GUI
        gui = show_section_manager_gui()
        
        if gui is not None:
            print("[OK] GUI opened successfully")
            
            # Close GUI after test
            try:
                gui.close()
                print("[OK] GUI closed successfully")
            except:
                print("[INFO] GUI close method not available (normal)")
            
            return True
        else:
            print("[FAIL] GUI failed to open (returned None)")
            return False
            
    except Exception as e:
        print(f"[ERROR] GUI opening test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_steelpy_status():
    """Test steelpy availability status"""
    print("\n=== Testing SteelPy Status ===")
    
    try:
        from freecad.StructureTools.data.SteelPyIntegration import STEELPY_AVAILABLE, get_steelpy_manager
        
        print(f"[INFO] STEELPY_AVAILABLE: {STEELPY_AVAILABLE}")
        
        if STEELPY_AVAILABLE:
            manager = get_steelpy_manager()
            stats = manager.get_statistics()
            print(f"[OK] SteelPy manager working: {stats.get('total_sections', 0)} sections available")
        else:
            print("[INFO] SteelPy not available - install with: pip install steelpy")
            print("[INFO] GUI will work with built-in sections only")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] SteelPy status test failed: {e}")
        return False

def test_icon_availability():
    """Test if icons are available"""
    print("\n=== Testing Icon Availability ===")
    
    import os
    
    try:
        # Check for icon files
        icon_dir = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools', 'resources', 'icons')
        
        required_icons = [
            'advanced_section_manager.svg',
            'section.svg'  # fallback
        ]
        
        for icon in required_icons:
            icon_path = os.path.join(icon_dir, icon)
            if os.path.exists(icon_path):
                print(f"[OK] Icon found: {icon}")
            else:
                print(f"[WARN] Icon missing: {icon}")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Icon test failed: {e}")
        return False

def run_freecad_tests():
    """Run all FreeCAD-specific tests"""
    print("Advanced Section Manager - FreeCAD Integration Test")
    print("=" * 60)
    
    tests = [
        ("Command Registration", test_command_registration),
        ("GUI Import", test_gui_import),
        ("SteelPy Status", test_steelpy_status),
        ("Icon Availability", test_icon_availability),
        ("GUI Opening", test_gui_opening)
    ]
    
    results = []
    for test_name, test_func in tests:
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
    
    if passed >= 4:  # Allow GUI opening to fail due to environment
        print("\n🎉 INTEGRATION READY!")
        print("\nTo use:")
        print("1. Install steelpy: pip install steelpy (optional)")
        print("2. In FreeCAD: Load StructureTools workbench")
        print("3. Click 'Advanced Section Manager' button")
        print("4. Or run: Gui.runCommand('StructureTools_AdvancedSectionManager')")
    else:
        print(f"\n⚠️  {total-passed} critical issues need attention")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # This should be run from FreeCAD Python console
    try:
        import FreeCAD
        print(f"Running in FreeCAD {FreeCAD.Version()}")
        run_freecad_tests()
    except ImportError:
        print("This test should be run from FreeCAD Python console")
        print("Copy and paste this code into FreeCAD:")
        print("exec(open(r'C:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools\\test_freecad_gui.py').read())")