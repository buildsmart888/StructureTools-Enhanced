"""
Simple verification script to check that test files were created correctly
"""

import os

def verify_test_files():
    """Verify that all test files were created"""
    base_path = r"c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools"
    
    required_files = [
        "test_calc_comprehensive.py",
        "test_diagram_comprehensive.py", 
        "test_structuretools_full.py",
        "test_num_points_fix_verification.py",
        "run_all_tests.py",
        "COMPREHENSIVE_TESTS_README.md",
        "TEST_SUMMARY.md"
    ]
    
    print("🔍 Verifying test files...")
    print("=" * 50)
    
    all_found = True
    for filename in required_files:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            # Get file size
            size = os.path.getsize(filepath)
            print(f"✅ {filename} - Found ({size} bytes)")
        else:
            print(f"❌ {filename} - Missing")
            all_found = False
    
    print("=" * 50)
    if all_found:
        print("🎉 All test files were created successfully!")
        print("\nTo run the tests in FreeCAD:")
        print("1. Open FreeCAD")
        print("2. Open the Python console")
        print("3. Run the commands from COMPREHENSIVE_TESTS_README.md")
        return True
    else:
        print("💥 Some test files are missing!")
        return False

if __name__ == "__main__":
    verify_test_files()