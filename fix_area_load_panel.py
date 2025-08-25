#!/usr/bin/env python3
"""
Script to fix AreaLoadPanel for mock compatibility in testing.
"""
import re

def fix_area_load_panel():
    """Fix all mock compatibility issues in AreaLoadPanel.py"""
    
    # Read the file
    with open('freecad/StructureTools/taskpanels/AreaLoadPanel.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace signal connections like obj.signal.connect(slot) with _safe_connect(getattr(obj, 'signal', None), slot)
    content = re.sub(r'(\w+)\.(\w+)\.connect\(([^)]+)\)', r'_safe_connect(getattr(\1, "\2", None), \3)', content)
    
    # Write back
    with open('freecad/StructureTools/taskpanels/AreaLoadPanel.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed AreaLoadPanel.py signal connections")

if __name__ == '__main__':
    fix_area_load_panel()
