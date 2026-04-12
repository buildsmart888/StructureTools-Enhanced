@echo off
echo Starting cleanup...

REM Delete log files
del /F /Q full_pytest.log 2>nul
del /F /Q full_tests.log 2>nul
del /F /Q full_tests.xml 2>nul
del /F /Q node_fail.log 2>nul
del /F /Q node_partial.log 2>nul
del /F /Q node_tests.xml 2>nul
del /F /Q pytest_objects.log 2>nul
del /F /Q pytest_objects.xml 2>nul
del /F /Q python_ver.log 2>nul
del /F /Q teste.json 2>nul
echo Deleted log files

REM Delete cache directories
rmdir /S /Q __pycache__ 2>nul
rmdir /S /Q .pytest_cache 2>nul
echo Deleted cache directories

REM Delete redundant scripts
del /F /Q batch_update_global_units.py 2>nul
del /F /Q check_class.py 2>nul
del /F /Q check_phase1_completion.py 2>nul
del /F /Q check_supports.py 2>nul
del /F /Q comprehensive_test.py 2>nul
del /F /Q comprehensive_verification.py 2>nul
del /F /Q demo_thai_units.py 2>nul
del /F /Q diagram_diagnostic.py 2>nul
del /F /Q diagram_github.py 2>nul
del /F /Q final_fix_verification.py 2>nul
del /F /Q fix_area_load_comprehensive.py 2>nul
del /F /Q fix_area_load_panel.py 2>nul
del /F /Q fix_regex_errors.py 2>nul
del /F /Q freecad_test.py 2>nul
del /F /Q quick_test.py 2>nul
del /F /Q quick_verification_test.py 2>nul
del /F /Q run_all_tests.py 2>nul
del /F /Q run_tests.py 2>nul
del /F /Q seismic_user_guide.py 2>nul
del /F /Q simple_check.py 2>nul
del /F /Q verify_all_diagram_fixes.py 2>nul
del /F /Q verify_fixes.py 2>nul
del /F /Q verify_material_fixes.py 2>nul
del /F /Q verify_phase_one.py 2>nul
del /F /Q verify_tests.py 2>nul
echo Deleted redundant scripts

REM Delete test files from root
del /F /Q test_*.py 2>nul
echo Deleted test files from root

REM Delete redundant documentation
del /F /Q PHASE1_COMPLETION_REPORT.md 2>nul
del /F /Q PHASE1_PHASE2_FINAL_STATUS.md 2>nul
del /F /Q PHASE1_PHASE2_INTEGRATION_REPORT.md 2>nul
del /F /Q PHASE2_COMPLETION_REPORT.py 2>nul
del /F /Q FINAL_SUMMARY_REPORT.py 2>nul
del /F /Q DIAGRAM_FIXES_SUMMARY.md 2>nul
del /F /Q diagram_error_fixes_summary.md 2>nul
del /F /Q MATERIAL_FIXES_SUMMARY.md 2>nul
del /F /Q DENSITY_FIX_SUMMARY.md 2>nul
del /F /Q SHEAR_UNIT_FIX_SUMMARY.md 2>nul
del /F /Q MOMENT_UNITS_FIX_SUMMARY.md 2>nul
del /F /Q UNIT_SYSTEM_FIXES_SUMMARY.md 2>nul
del /F /Q calc_units_enhancement_summary.md 2>nul
del /F /Q seismic_gui_fix_summary.md 2>nul
del /F /Q sign_convention_correction_summary.md 2>nul
del /F /Q simplified_units_system_summary.md 2>nul
del /F /Q ICON_FIXES_SUMMARY.md 2>nul
del /F /Q REACTION_TABLE_ENHANCEMENTS.md 2>nul
del /F /Q REACTION_TABLE_ENHANCEMENT_SUMMARY.md 2>nul
del /F /Q REACTION_TABLE_FEATURE_SUMMARY.md 2>nul
del /F /Q TEST_SUMMARY.md 2>nul
echo Deleted redundant documentation

REM Delete obsolete files
del /F /Q run_test.bat 2>nul
del /F /Q codeviz-diagram-2025-08-16T03-34-36.drawio 2>nul
echo Deleted obsolete files

echo.
echo Cleanup completed!
pause
