#!/usr/bin/env python3
"""Quick cleanup script to remove unnecessary files"""
import os
import shutil
from pathlib import Path

def main():
    base_dir = Path(__file__).parent
    deleted_count = 0
    
    print("Starting cleanup...")
    
    # Test output files
    test_outputs = [
        "full_pytest.log", "full_tests.log", "full_tests.xml",
        "node_fail.log", "node_partial.log", "node_tests.xml",
        "pytest_objects.log", "pytest_objects.xml", "python_ver.log",
        "teste.json"
    ]
    
    for file in test_outputs:
        filepath = base_dir / file
        if filepath.exists():
            filepath.unlink()
            print(f"✓ Deleted: {file}")
            deleted_count += 1
    
    # Cache directories
    cache_dirs = ["__pycache__", ".pytest_cache"]
    for dir_name in cache_dirs:
        dirpath = base_dir / dir_name
        if dirpath.exists():
            shutil.rmtree(dirpath)
            print(f"✓ Deleted directory: {dir_name}")
            deleted_count += 1
    
    # Redundant scripts
    redundant = [
        "batch_update_global_units.py", "check_class.py", "check_phase1_completion.py",
        "check_supports.py", "comprehensive_test.py", "comprehensive_verification.py",
        "demo_thai_units.py", "diagram_diagnostic.py", "diagram_github.py",
        "final_fix_verification.py", "fix_area_load_comprehensive.py", "fix_area_load_panel.py",
        "fix_regex_errors.py", "freecad_test.py", "quick_test.py", "quick_verification_test.py",
        "run_all_tests.py", "run_tests.py", "seismic_user_guide.py", "simple_check.py",
        "verify_all_diagram_fixes.py", "verify_fixes.py", "verify_material_fixes.py",
        "verify_phase_one.py", "verify_tests.py"
    ]
    
    for file in redundant:
        filepath = base_dir / file
        if filepath.exists():
            filepath.unlink()
            print(f"✓ Deleted: {file}")
            deleted_count += 1
    
    # Test files in root
    for file in base_dir.glob("test_*.py"):
        file.unlink()
        print(f"✓ Deleted: {file.name}")
        deleted_count += 1
    
    # Redundant docs
    redundant_docs = [
        "PHASE1_COMPLETION_REPORT.md", "PHASE1_PHASE2_FINAL_STATUS.md",
        "PHASE1_PHASE2_INTEGRATION_REPORT.md", "PHASE2_COMPLETION_REPORT.py",
        "FINAL_SUMMARY_REPORT.py", "DIAGRAM_FIXES_SUMMARY.md",
        "diagram_error_fixes_summary.md", "MATERIAL_FIXES_SUMMARY.md",
        "DENSITY_FIX_SUMMARY.md", "SHEAR_UNIT_FIX_SUMMARY.md",
        "MOMENT_UNITS_FIX_SUMMARY.md", "UNIT_SYSTEM_FIXES_SUMMARY.md",
        "calc_units_enhancement_summary.md", "seismic_gui_fix_summary.md",
        "sign_convention_correction_summary.md", "simplified_units_system_summary.md",
        "ICON_FIXES_SUMMARY.md", "REACTION_TABLE_ENHANCEMENTS.md",
        "REACTION_TABLE_ENHANCEMENT_SUMMARY.md", "REACTION_TABLE_FEATURE_SUMMARY.md",
        "TEST_SUMMARY.md"
    ]
    
    for file in redundant_docs:
        filepath = base_dir / file
        if filepath.exists():
            filepath.unlink()
            print(f"✓ Deleted: {file}")
            deleted_count += 1
    
    # Obsolete files
    obsolete = ["run_test.bat", "codeviz-diagram-2025-08-16T03-34-36.drawio"]
    for file in obsolete:
        filepath = base_dir / file
        if filepath.exists():
            filepath.unlink()
            print(f"✓ Deleted: {file}")
            deleted_count += 1
    
    print(f"\n✅ Cleanup complete! Deleted {deleted_count} items.")

if __name__ == "__main__":
    main()
