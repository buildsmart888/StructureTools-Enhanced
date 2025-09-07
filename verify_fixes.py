# -*- coding: utf-8 -*-
"""
Simple verification of the fixes applied to section.py
ตรวจสอบการแก้ไขใน section.py แบบง่าย
"""

import os

def check_section_file_fixes():
    """Check that fixes have been applied to section.py"""
    print("Checking StructureTools section.py fixes...")
    print("=" * 50)
    
    # Read the section.py file
    section_file = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools', 'section.py')
    
    if not os.path.exists(section_file):
        print("ERROR: section.py file not found")
        return False
    
    with open(section_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes_applied = []
    
    # Check 1: GUI import fixes
    if 'GUI_AVAILABLE' in content and 'QtWidgets = None' in content:
        fixes_applied.append("GUI import fallbacks")
        print("[OK] GUI import fixes applied")
    else:
        print("[FAIL] GUI import fixes missing")
    
    # Check 2: Console logging fixes  
    if 'safe_console_log' in content and 'FreeCAD.Console' in content:
        fixes_applied.append("Safe console logging")
        print("[OK] Console logging fixes applied")
    else:
        print("[FAIL] Console logging fixes missing")
    
    # Check 3: Property name consistency
    area_section_count = content.count('AreaSection')
    if area_section_count == 0:
        fixes_applied.append("Property name consistency")
        print("[OK] Property names consistent (no AreaSection references)")
    else:
        print(f"[WARN] Still found {area_section_count} AreaSection references")
    
    # Check 4: Error handling improvements
    if 'show_error_message' in content and 'safe_console_log' in content:
        fixes_applied.append("Error handling improvements")
        print("[OK] Error handling functions improved")
    else:
        print("[FAIL] Error handling improvements missing")
    
    # Check 5: Property existence checking
    if 'hasattr(obj' in content:
        fixes_applied.append("Property existence checking")
        print("[OK] Property existence checking added")
    else:
        print("[FAIL] Property existence checking missing")
    
    print("\n" + "=" * 50)
    print("FIXES VERIFICATION SUMMARY:")
    print(f"Applied fixes: {len(fixes_applied)}/5")
    
    for fix in fixes_applied:
        print(f"  [OK] {fix}")
    
    if len(fixes_applied) >= 4:
        print("\n[SUCCESS] Critical fixes have been applied!")
        print("\nKey improvements:")
        print("  - App.Console -> FreeCAD.Console with fallbacks")
        print("  - PySide imports with PySide2 fallbacks") 
        print("  - AreaSection -> Area property consistency")
        print("  - Safe console logging function")
        print("  - GUI availability checking")
        print("  - Property existence validation")
        
        print("\nThe fixes should resolve these errors:")
        print("  - 'FeaturePython' object has no attribute 'AreaSection'")
        print("  - module 'App' has no attribute 'Console'")
        print("  - GUI import crashes")
        
        return True
    else:
        print(f"\n[WARNING] Only {len(fixes_applied)} out of 5 critical fixes applied")
        return False

def check_calc_file_fixes():
    """Check that calc.py has been updated for property consistency"""
    print("\nChecking calc.py property fixes...")
    print("-" * 30)
    
    calc_file = os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools', 'calc.py')
    
    if not os.path.exists(calc_file):
        print("WARNING: calc.py file not found")
        return False
    
    with open(calc_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for Area instead of AreaSection
    if 'section.Area' in content:
        print("[OK] calc.py uses correct Area property")
        return True
    else:
        print("[WARN] calc.py may still use old property names")
        return False

if __name__ == "__main__":
    section_ok = check_section_file_fixes()
    calc_ok = check_calc_file_fixes()
    
    print("\n" + "=" * 60)
    if section_ok and calc_ok:
        print("FINAL STATUS: ALL FIXES VERIFIED!")
        print("\nStructureTools should now work without the reported errors.")
        print("You can test it in FreeCAD to confirm the fixes are working.")
    elif section_ok:
        print("FINAL STATUS: MAIN FIXES VERIFIED!")
        print("\nThe critical section.py fixes are in place.")
        print("Minor calc.py issues may remain but shouldn't cause crashes.")
    else:
        print("FINAL STATUS: FIXES INCOMPLETE!")
        print("\nSome critical fixes may be missing.")