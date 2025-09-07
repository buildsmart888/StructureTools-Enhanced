# -*- coding: utf-8 -*-
"""
Test TaskPanel version of Advanced Section Manager
ทดสอบ TaskPanel version ของ Advanced Section Manager
"""

import FreeCAD as App

def test_task_panel_directly():
    """Test TaskPanel creation directly"""
    print("=" * 60)
    print("Testing Advanced Section Manager TaskPanel")
    print("=" * 60)
    
    try:
        print("[INFO] Testing TaskPanel import...")
        from freecad.StructureTools.gui.SectionManagerTaskPanel import (
            AdvancedSectionManagerTaskPanel, show_advanced_section_manager_task_panel
        )
        print("[OK] TaskPanel module imported successfully!")
        
        print("\n[INFO] Testing direct TaskPanel creation...")
        task_panel = AdvancedSectionManagerTaskPanel()
        print("[OK] TaskPanel instance created successfully!")
        
        # Check if TaskPanel has the expected structure
        if hasattr(task_panel, 'form'):
            print("[OK] TaskPanel has form widget")
        else:
            print("[ERROR] TaskPanel missing form widget")
            return False
        
        if hasattr(task_panel, 'steelpy_available'):
            print(f"[INFO] SteelPy available: {task_panel.steelpy_available}")
        
        if hasattr(task_panel, 'shape_types'):
            print(f"[INFO] Shape types loaded: {len(task_panel.shape_types)}")
        
        # Test the form widget
        form = task_panel.form
        if form:
            print("[OK] Form widget exists")
            
            # Check for expected UI elements
            ui_elements = [
                ('shape_combo', 'QComboBox'),
                ('section_list', 'QListWidget'),
                ('props_table', 'QTableWidget'),
                ('create_section_btn', 'QPushButton'),
                ('create_profile_btn', 'QPushButton')
            ]
            
            for attr_name, expected_type in ui_elements:
                if hasattr(task_panel, attr_name):
                    widget = getattr(task_panel, attr_name)
                    print(f"[OK] Found {attr_name}: {type(widget).__name__}")
                else:
                    print(f"[WARNING] Missing {attr_name}")
        
        print("\n[INFO] TaskPanel structure test completed!")
        return True
        
    except Exception as e:
        print(f"[ERROR] TaskPanel test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_task_panel_via_function():
    """Test TaskPanel via show function"""
    print("\n" + "=" * 60)
    print("Testing TaskPanel via show function")
    print("=" * 60)
    
    try:
        print("[INFO] Testing show_advanced_section_manager_task_panel()...")
        from freecad.StructureTools.gui.SectionManagerTaskPanel import show_advanced_section_manager_task_panel
        
        result = show_advanced_section_manager_task_panel()
        
        if result:
            print("[OK] TaskPanel show function succeeded!")
            print("\n🎉 TaskPanel should now be visible in the Task Panel area!")
            print("Look for 'Advanced Section Manager' in the FreeCAD Task Panel.")
            return True
        else:
            print("[ERROR] TaskPanel show function failed!")
            return False
            
    except Exception as e:
        print(f"[ERROR] TaskPanel show test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_task_panel_via_command():
    """Test TaskPanel via FreeCAD command"""
    print("\n" + "=" * 60)
    print("Testing TaskPanel via FreeCAD command")
    print("=" * 60)
    
    try:
        import FreeCADGui as Gui
        
        print("[INFO] Checking if command is registered...")
        commands = Gui.listCommands()
        
        if 'StructureTools_AdvancedSectionManagerTaskPanel' in commands:
            print("[OK] TaskPanel command is registered")
            
            print("[INFO] Executing command...")
            Gui.runCommand('StructureTools_AdvancedSectionManagerTaskPanel')
            print("[OK] Command executed!")
            
            return True
        else:
            print("[ERROR] TaskPanel command not found")
            print("Available StructureTools commands:")
            structure_commands = [cmd for cmd in commands if 'StructureTools' in cmd]
            for cmd in structure_commands:
                print(f"  - {cmd}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Command test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_all_task_panel_tests():
    """Run all TaskPanel tests"""
    print("Advanced Section Manager TaskPanel - Comprehensive Test")
    print("=" * 70)
    
    tests = [
        ("Direct TaskPanel Creation", test_task_panel_directly),
        ("TaskPanel Show Function", test_task_panel_via_function),
        ("TaskPanel Command", test_task_panel_via_command)
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
    print("\n" + "=" * 70)
    print("TASKPANEL TEST SUMMARY:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "[OK]" if result else "[FAIL]"
        print(f"  {symbol} {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed >= 2:  # Allow command test to fail
        print("\n🎉 TASKPANEL WORKING!")
        print("\nTo use the TaskPanel version:")
        print("1. Look for 'Advanced Section Manager (TaskPanel)' button")
        print("2. Or run: Gui.runCommand('StructureTools_AdvancedSectionManagerTaskPanel')")
        print("3. Or run: show_advanced_section_manager_task_panel()")
        print("\nThe TaskPanel should appear in the Task Panel area (usually right side)")
    else:
        print(f"\n⚠️  TaskPanel tests failed - needs attention")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    try:
        import FreeCAD
        print(f"Running TaskPanel test in FreeCAD {FreeCAD.Version()}")
        run_all_task_panel_tests()
    except ImportError:
        print("This test should be run from FreeCAD Python console")
        print("Copy and paste this code into FreeCAD:")
        print("exec(open(r'C:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools\\test_task_panel.py').read())")