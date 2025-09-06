#!/usr/bin/env python3
"""
Script to systematically fix AreaLoadPanel for mock compatibility.
"""
import re

def fix_area_load_panel():
    """Fix all mock compatibility issues in AreaLoadPanel.py"""
    
    # Read the file
    with open('freecad/StructureTools/taskpanels/AreaLoadPanel.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace setLayout calls
    content = re.sub(r'(\w+)\.setLayout\(([^)]+)\)', r'_safe_set_layout(\1, \2)', content)
    
    # 2. Replace addWidget calls 
    content = re.sub(r'(\w+)\.addWidget\(([^)]+)\)', r'_safe_add_widget(\1, \2)', content)
    
    # 3. Replace setToolTip calls
    content = re.sub(r'(\w+)\.setToolTip\(([^)]+)\)', r'_safe_call_method(\1, "setToolTip", \2)', content)
    
    # 4. Replace setStyleSheet calls
    content = re.sub(r'(\w+)\.setStyleSheet\(([^)]+)\)', r'_safe_call_method(\1, "setStyleSheet", \2)', content)
    
    # 5. Replace signal connections
    content = re.sub(r'(\w+)\.(\w+)\.connect\(([^)]+)\)', r'_safe_connect(getattr(\1, "\2", None), \3)', content)
    
    # 6. Fix common method calls that might fail on mocks
    methods_to_fix = [
        'setMaximumHeight', 'setSelectionMode', 'setRange', 'setSuffix', 
        'setValue', 'addItems', 'setChecked', 'addItem', 'addTab'
    ]
    
    for method in methods_to_fix:
        pattern = rf'(\w+)\.{method}\(([^)]*)\)'
        replacement = rf'_safe_call_method(\1, "{method}", \2)'
        content = re.sub(pattern, replacement, content)
    
    # Write back
    with open('freecad/StructureTools/taskpanels/AreaLoadPanel.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Applied comprehensive mock compatibility fixes to AreaLoadPanel.py")

if __name__ == '__main__':
    fix_area_load_panel()
