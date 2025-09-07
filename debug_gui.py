# -*- coding: utf-8 -*-
"""
Debug script for Advanced Section Manager GUI
สคริปต์ดีบัก GUI สำหรับ Advanced Section Manager
"""

import FreeCAD as App
import sys
import os

def test_gui_step_by_step():
    """Test GUI creation step by step to isolate the problem"""
    print("=" * 60)
    print("Advanced Section Manager GUI - Step by Step Debug")
    print("=" * 60)
    
    # Test 1: Check PySide availability
    print("\n[TEST 1] Checking PySide availability...")
    try:
        from PySide2 import QtWidgets, QtCore, QtGui
        from PySide2.QtWidgets import *
        from PySide2.QtCore import *
        from PySide2.QtGui import *
        print("[OK] PySide2 is available")
        pyside_available = True
    except ImportError:
        try:
            from PySide import QtWidgets, QtCore, QtGui
            from PySide.QtWidgets import *
            from PySide.QtCore import *
            from PySide.QtGui import *
            print("[OK] PySide is available")
            pyside_available = True
        except ImportError:
            print("[ERROR] No PySide libraries available")
            return False
    
    # Test 2: Check QApplication
    print("\n[TEST 2] Checking QApplication...")
    try:
        app = QApplication.instance()
        if app is None:
            print("[INFO] Creating new QApplication...")
            app = QApplication([])
        print(f"[OK] QApplication ready: {app}")
    except Exception as e:
        print(f"[ERROR] QApplication failed: {e}")
        return False
    
    # Test 3: Test basic window creation
    print("\n[TEST 3] Testing basic window creation...")
    try:
        class TestWindow(QMainWindow):
            def __init__(self):
                super(TestWindow, self).__init__()
                self.setWindowTitle("Test Window")
                self.setGeometry(100, 100, 400, 300)
                
                central = QWidget()
                self.setCentralWidget(central)
                layout = QVBoxLayout(central)
                
                label = QLabel("Test GUI - If you see this, basic Qt works!")
                layout.addWidget(label)
        
        test_window = TestWindow()
        test_window.show()
        print("[OK] Basic window creation works!")
        
        # Keep window open briefly
        import time
        time.sleep(1)
        test_window.close()
        
    except Exception as e:
        print(f"[ERROR] Basic window creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 4: Check steelpy integration imports
    print("\n[TEST 4] Testing steelpy integration imports...")
    try:
        from freecad.StructureTools.data.SteelPyIntegrationFixed import (
            get_steelpy_manager, get_available_shape_types, 
            get_sections_for_shape, get_section_data, 
            search_steel_sections, STEELPY_AVAILABLE
        )
        print(f"[OK] SteelPy integration imported, available: {STEELPY_AVAILABLE}")
    except Exception as e:
        print(f"[ERROR] SteelPy integration import failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 5: Test GUI components import
    print("\n[TEST 5] Testing GUI components import...")
    try:
        from freecad.StructureTools.gui.SectionManagerGUI import (
            SteelPyDatabase, ArchProfileIntegration, SectionManagerGUI
        )
        print("[OK] GUI components imported successfully")
    except Exception as e:
        print(f"[ERROR] GUI components import failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 6: Test database creation
    print("\n[TEST 6] Testing database creation...")
    try:
        steelpy_db = SteelPyDatabase()
        print(f"[OK] SteelPy database created, available: {steelpy_db.available}")
        print(f"Shape types loaded: {len(steelpy_db.shape_types)}")
        
        arch_integration = ArchProfileIntegration()
        print(f"[OK] Arch integration created, available: {arch_integration.available}")
        
    except Exception as e:
        print(f"[ERROR] Database creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 7: Try creating the full GUI
    print("\n[TEST 7] Testing full GUI creation...")
    try:
        print("Creating SectionManagerGUI...")
        gui = SectionManagerGUI()
        
        print("Showing GUI...")
        gui.show()
        gui.raise_()
        gui.activateWindow()
        
        print("[OK] Full GUI created and shown!")
        
        # Check if window is visible
        if gui.isVisible():
            print("[OK] Window is visible!")
        else:
            print("[WARNING] Window is not visible!")
        
        # Keep reference
        if not hasattr(test_gui_step_by_step, '_gui_ref'):
            test_gui_step_by_step._gui_ref = []
        test_gui_step_by_step._gui_ref.append(gui)
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Full GUI creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def simple_gui_test():
    """Simple GUI test without full SectionManagerGUI"""
    print("\n[SIMPLE TEST] Testing minimal GUI...")
    
    try:
        from PySide2.QtWidgets import *
        from PySide2.QtCore import *
        from PySide2.QtGui import *
    except ImportError:
        try:
            from PySide.QtWidgets import *
            from PySide.QtCore import *
            from PySide.QtGui import *
        except ImportError:
            print("[ERROR] No Qt available")
            return False
    
    try:
        app = QApplication.instance() or QApplication([])
        
        # Create simple dialog
        dialog = QDialog()
        dialog.setWindowTitle("Advanced Section Manager - Test")
        dialog.setGeometry(200, 200, 600, 400)
        
        layout = QVBoxLayout(dialog)
        
        # Add some content
        title = QLabel("Advanced Section Manager")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        info = QLabel("This is a test dialog to verify Qt functionality.")
        layout.addWidget(info)
        
        # Add steelpy status
        try:
            from freecad.StructureTools.data.SteelPyIntegrationFixed import STEELPY_AVAILABLE
            if STEELPY_AVAILABLE:
                status_text = "✓ steelpy is available and working"
                status_color = "green"
            else:
                status_text = "⚠ steelpy is not available (install with: pip install steelpy)"
                status_color = "orange"
        except:
            status_text = "✗ steelpy integration has problems"
            status_color = "red"
        
        status = QLabel(status_text)
        status.setStyleSheet(f"color: {status_color}; padding: 10px;")
        layout.addWidget(status)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)
        
        # Show dialog
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()
        
        # Keep reference
        if not hasattr(simple_gui_test, '_dialog_ref'):
            simple_gui_test._dialog_ref = []
        simple_gui_test._dialog_ref.append(dialog)
        
        print("[OK] Simple dialog created and shown!")
        return True
        
    except Exception as e:
        print(f"[ERROR] Simple GUI test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_debug():
    """Run comprehensive debug"""
    print("Starting comprehensive GUI debug...")
    
    # Try simple test first
    simple_success = simple_gui_test()
    
    if simple_success:
        print("\n" + "=" * 60)
        print("Simple GUI test PASSED - Qt is working")
        print("Proceeding to full GUI test...")
        print("=" * 60)
        
        # Try full test
        full_success = test_gui_step_by_step()
        
        if full_success:
            print("\n🎉 SUCCESS: Advanced Section Manager GUI is working!")
            print("\nThe GUI should now be visible.")
            print("If it disappeared, there might be a focus issue.")
            print("\nTry running:")
            print("Gui.runCommand('StructureTools_AdvancedSectionManager')")
        else:
            print("\n❌ FAILED: Full GUI test failed")
            print("But simple GUI works, so Qt is available.")
            print("The issue is in SectionManagerGUI implementation.")
    else:
        print("\n❌ FAILED: Even simple GUI test failed")
        print("Qt/PySide has fundamental problems.")
        print("Check PySide2 installation: pip install PySide2")

if __name__ == "__main__":
    try:
        import FreeCAD
        print(f"Running debug in FreeCAD {FreeCAD.Version()}")
        run_debug()
    except ImportError:
        print("This debug script should be run from FreeCAD Python console")
        print("Copy and paste this code into FreeCAD:")
        print("exec(open(r'C:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools\\debug_gui.py').read())")