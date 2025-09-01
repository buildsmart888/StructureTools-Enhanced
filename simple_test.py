#!/usr/bin/env python3
"""
Simple test script to verify that the AreaLoad and StructuralPlate classes can be imported without syntax errors.
"""

import sys
import os

# Setup repo path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
freecad_dir = os.path.join(repo_root, 'freecad')
if freecad_dir not in sys.path:
    sys.path.insert(0, freecad_dir)

def test_imports():
    """Test that we can import the classes without syntax errors."""
    try:
        # Try to import the classes
        from freecad.StructureTools.objects.StructuralPlate import StructuralPlate
        from freecad.StructureTools.objects.AreaLoad import AreaLoad
        print("SUCCESS: All classes imported successfully")
        return True
    except Exception as e:
        print(f"ERROR: Failed to import classes: {e}")
        return False

def main():
    """Run the tests."""
    print("Testing imports for StructuralPlate and AreaLoad classes...")
    print("=" * 60)
    
    success = test_imports()
    
    if success:
        print("✓ Import test PASSED! No syntax errors found.")
        return 0
    else:
        print("✗ Import test FAILED! Please check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())