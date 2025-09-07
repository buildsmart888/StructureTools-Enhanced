# -*- coding: utf-8 -*-
"""
Simple script to open Advanced Section Manager
สคริปต์เปิด Advanced Section Manager
"""

import FreeCAD as App

def open_section_manager():
    """Open Advanced Section Manager GUI"""
    print("Opening Advanced Section Manager...")
    
    try:
        # Method 1: Try using the command
        try:
            import FreeCADGui as Gui
            Gui.runCommand('StructureTools_AdvancedSectionManager')
            print("[OK] Opened using FreeCAD command")
            return True
        except Exception as e:
            print(f"[INFO] Command method failed: {e}")
        
        # Method 2: Try direct import
        try:
            from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui
            gui = show_section_manager_gui()
            
            if gui:
                print("[OK] Opened using direct import")
                return True
            else:
                print("[WARN] GUI returned None")
        except Exception as e:
            print(f"[ERROR] Direct import failed: {e}")
            import traceback
            traceback.print_exc()
        
        # Method 3: Try alternative approach
        try:
            print("[INFO] Trying alternative approach...")
            
            # Check if steelpy is available
            try:
                import steelpy
                print("[OK] steelpy is available")
                steelpy_available = True
            except ImportError:
                print("[WARN] steelpy not available - install with: pip install steelpy")
                steelpy_available = False
            
            # Check GUI libraries
            try:
                from PySide2 import QtWidgets
                print("[OK] PySide2 available")
                gui_available = True
            except ImportError:
                try:
                    from PySide import QtWidgets
                    print("[OK] PySide available")
                    gui_available = True
                except ImportError:
                    print("[ERROR] No GUI libraries available")
                    gui_available = False
            
            if not gui_available:
                print("\nSOLUTION: Install GUI libraries:")
                print("pip install PySide2")
                return False
            
            # Try to import and show
            from freecad.StructureTools.gui.SectionManagerGUI import SectionManagerGUI
            
            app = QtWidgets.QApplication.instance()
            if app is None:
                print("[INFO] Creating QApplication instance")
                app = QtWidgets.QApplication([])
            
            gui = SectionManagerGUI()
            gui.show()
            
            print("[OK] GUI created and shown")
            return True
            
        except Exception as e:
            print(f"[ERROR] Alternative approach failed: {e}")
            import traceback
            traceback.print_exc()
        
        return False
        
    except Exception as e:
        print(f"[ERROR] Failed to open Section Manager: {e}")
        return False

def diagnose_issues():
    """Diagnose common issues"""
    print("\n=== Diagnosing Issues ===")
    
    issues = []
    solutions = []
    
    # Check steelpy
    try:
        import steelpy
        print("[OK] steelpy available")
    except ImportError:
        issues.append("steelpy not installed")
        solutions.append("pip install steelpy")
    
    # Check GUI libraries
    gui_available = False
    try:
        from PySide2 import QtWidgets
        print("[OK] PySide2 available")
        gui_available = True
    except ImportError:
        try:
            from PySide import QtWidgets
            print("[OK] PySide available") 
            gui_available = True
        except ImportError:
            issues.append("No GUI libraries available")
            solutions.append("pip install PySide2")
    
    # Check FreeCAD modules
    try:
        import FreeCADGui
        print("[OK] FreeCADGui available")
    except ImportError:
        issues.append("FreeCADGui not available")
        solutions.append("Run from FreeCAD environment")
    
    # Check command registration
    try:
        import FreeCADGui as Gui
        commands = Gui.listCommands()
        if 'StructureTools_AdvancedSectionManager' in commands:
            print("[OK] Command registered")
        else:
            issues.append("Command not registered")
            solutions.append("Restart FreeCAD or reload StructureTools workbench")
    except:
        pass
    
    if issues:
        print(f"\n⚠️  Found {len(issues)} issue(s):")
        for i, (issue, solution) in enumerate(zip(issues, solutions), 1):
            print(f"  {i}. {issue}")
            print(f"     Solution: {solution}")
    else:
        print("\n✅ No obvious issues found")
    
    return len(issues) == 0

# Main execution
if __name__ == "__main__":
    print("Advanced Section Manager - Quick Opener")
    print("=" * 50)
    
    # Diagnose first
    diagnosis_ok = diagnose_issues()
    
    # Try to open
    if diagnosis_ok or True:  # Try even if issues found
        success = open_section_manager()
        
        if success:
            print("\n🎉 SUCCESS: Advanced Section Manager opened!")
        else:
            print("\n❌ FAILED: Could not open Advanced Section Manager")
            print("\nTroubleshooting steps:")
            print("1. Ensure you're running this in FreeCAD")
            print("2. Install steelpy: pip install steelpy")
            print("3. Install PySide2: pip install PySide2") 
            print("4. Reload StructureTools workbench")
            print("5. Check FreeCAD console for error messages")
    
    print("\n" + "=" * 50)

# Also create a simple function for FreeCAD macro
def quick_open():
    """Quick function for FreeCAD macro"""
    from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui
    return show_section_manager_gui()

# Instructions for user
print("USAGE:")
print("1. Copy this file to FreeCAD and run with exec()")
print("2. Or run: open_section_manager()")
print("3. Or run: quick_open()")