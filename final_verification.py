#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Final verification script for StructureTools Point Load Implementation
This script verifies that all components of the point load feature have been correctly implemented.
"""

import sys
import os

# Add the StructureTools path to sys.path
structure_tools_path = r"c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools"
if structure_tools_path not in sys.path:
    sys.path.append(structure_tools_path)

def check_file_exists(filepath, description):
    """Check if a file exists and print the result."""
    if os.path.exists(filepath):
        print(f"✓ {description} - FOUND")
        return True
    else:
        print(f"✗ {description} - NOT FOUND")
        return False

def check_import(module_path, class_name, description):
    """Check if a class can be imported from a module."""
    try:
        module = __import__(module_path, fromlist=[class_name])
        cls = getattr(module, class_name)
        print(f"✓ {description} - SUCCESS")
        return True
    except Exception as e:
        print(f"✗ {description} - FAILED ({str(e)})")
        return False

def check_string_in_file(filepath, search_string, description):
    """Check if a string exists in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if search_string in content:
            print(f"✓ {description} - FOUND")
            return True
        else:
            print(f"✗ {description} - NOT FOUND")
            return False
    except Exception as e:
        print(f"✗ {description} - ERROR ({str(e)})")
        return False

def main():
    print("StructureTools Point Load Implementation - Final Verification")
    print("=" * 70)
    
    # 1. Check if load_point.py file exists
    load_point_file = os.path.join(structure_tools_path, "freecad", "StructureTools", "load_point.py")
    check_file_exists(load_point_file, "Load point module file")
    
    # 2. Check if LoadPoint class can be imported
    check_import("freecad.StructureTools.load_point", "LoadPoint", "LoadPoint class import")
    
    # 3. Check if icon file exists
    icon_file = os.path.join(structure_tools_path, "freecad", "StructureTools", "resources", "icons", "load_point.svg")
    check_file_exists(icon_file, "Load point icon file")
    
    # 4. Check if calc.py has been modified correctly
    calc_file = os.path.join(structure_tools_path, "freecad", "StructureTools", "calc.py")
    check_string_in_file(calc_file, "elif 'Edge' in load.ObjectBase[0][1][0] and hasattr(load, 'PointLoading'):", 
                        "Point load processing in calc.py")
    
    # 5. Check if init_gui.py imports load_point
    init_gui_file = os.path.join(structure_tools_path, "freecad", "StructureTools", "init_gui.py")
    check_string_in_file(init_gui_file, "from freecad.StructureTools import load_point", 
                        "Load point import in init_gui.py")
    
    # 6. Check if load_point command is registered in toolbar
    check_string_in_file(init_gui_file, '"load_point"', "Load point command registration")
    
    # 7. Check if GlobalDirection includes moment options
    check_string_in_file(load_point_file, "'+My','-My', '+Mz','-Mz', '+Mx','-Mx'", 
                        "Moment direction options in LoadPoint")
    
    # 8. Check if RelativePosition property exists
    check_string_in_file(load_point_file, "RelativePosition", "RelativePosition property")
    
    print("=" * 70)
    print("Verification completed!")

if __name__ == "__main__":
    main()