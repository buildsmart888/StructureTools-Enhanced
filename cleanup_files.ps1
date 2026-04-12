# StructureTools Cleanup Script
# This script removes unnecessary files safely

Write-Host "Starting cleanup process..." -ForegroundColor Green

# Counter for deleted files
$deletedCount = 0

# Phase 1: Delete test output files
Write-Host "`n=== Phase 1: Removing test output files ===" -ForegroundColor Cyan

$testOutputFiles = @(
    "full_pytest.log",
    "full_tests.log",
    "full_tests.xml",
    "node_fail.log",
    "node_partial.log",
    "node_tests.xml",
    "pytest_objects.log",
    "pytest_objects.xml",
    "python_ver.log",
    "teste.json"
)

foreach ($file in $testOutputFiles) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "  ✓ Deleted: $file" -ForegroundColor Green
        $deletedCount++
    } else {
        Write-Host "  - Not found: $file" -ForegroundColor Gray
    }
}

# Phase 2: Delete cache directories
Write-Host "`n=== Phase 2: Removing cache directories ===" -ForegroundColor Cyan

$cacheDirs = @("__pycache__", ".pytest_cache")

foreach ($dir in $cacheDirs) {
    if (Test-Path $dir) {
        Remove-Item $dir -Recurse -Force
        Write-Host "  ✓ Deleted directory: $dir" -ForegroundColor Green
        $deletedCount++
    } else {
        Write-Host "  - Not found: $dir" -ForegroundColor Gray
    }
}

# Phase 3: Delete redundant test scripts in root
Write-Host "`n=== Phase 3: Removing redundant test scripts ===" -ForegroundColor Cyan

$redundantScripts = @(
    "batch_update_global_units.py",
    "check_class.py",
    "check_phase1_completion.py",
    "check_supports.py",
    "comprehensive_test.py",
    "comprehensive_verification.py",
    "demo_thai_units.py",
    "diagram_diagnostic.py",
    "diagram_github.py",
    "final_fix_verification.py",
    "fix_area_load_comprehensive.py",
    "fix_area_load_panel.py",
    "fix_regex_errors.py",
    "freecad_test.py",
    "quick_test.py",
    "quick_verification_test.py",
    "run_all_tests.py",
    "run_tests.py",
    "seismic_user_guide.py",
    "simple_check.py",
    "verify_all_diagram_fixes.py",
    "verify_fixes.py",
    "verify_material_fixes.py",
    "verify_phase_one.py",
    "verify_tests.py"
)

foreach ($file in $redundantScripts) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "  ✓ Deleted: $file" -ForegroundColor Green
        $deletedCount++
    }
}

# Phase 4: Delete test_*.py files from root (they should be in tests/ directory)
Write-Host "`n=== Phase 4: Removing test files from root ===" -ForegroundColor Cyan

$rootTestFiles = Get-ChildItem -Path "." -Filter "test_*.py" -File

foreach ($file in $rootTestFiles) {
    Remove-Item $file.FullName -Force
    Write-Host "  ✓ Deleted: $($file.Name)" -ForegroundColor Green
    $deletedCount++
}

# Phase 5: Delete redundant documentation files
Write-Host "`n=== Phase 5: Removing redundant documentation ===" -ForegroundColor Cyan

$redundantDocs = @(
    "PHASE1_COMPLETION_REPORT.md",
    "PHASE1_PHASE2_FINAL_STATUS.md",
    "PHASE1_PHASE2_INTEGRATION_REPORT.md",
    "PHASE2_COMPLETION_REPORT.py",
    "FINAL_SUMMARY_REPORT.py",
    "DIAGRAM_FIXES_SUMMARY.md",
    "diagram_error_fixes_summary.md",
    "MATERIAL_FIXES_SUMMARY.md",
    "DENSITY_FIX_SUMMARY.md",
    "SHEAR_UNIT_FIX_SUMMARY.md",
    "MOMENT_UNITS_FIX_SUMMARY.md",
    "UNIT_SYSTEM_FIXES_SUMMARY.md",
    "calc_units_enhancement_summary.md",
    "seismic_gui_fix_summary.md",
    "sign_convention_correction_summary.md",
    "simplified_units_system_summary.md",
    "ICON_FIXES_SUMMARY.md",
    "REACTION_TABLE_ENHANCEMENTS.md",
    "REACTION_TABLE_ENHANCEMENT_SUMMARY.md",
    "REACTION_TABLE_FEATURE_SUMMARY.md",
    "TEST_SUMMARY.md"
)

foreach ($file in $redundantDocs) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "  ✓ Deleted: $file" -ForegroundColor Green
        $deletedCount++
    }
}

# Phase 6: Delete obsolete files
Write-Host "`n=== Phase 6: Removing obsolete files ===" -ForegroundColor Cyan

$obsoleteFiles = @(
    "run_test.bat",
    "codeviz-diagram-2025-08-16T03-34-36.drawio"
)

foreach ($file in $obsoleteFiles) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "  ✓ Deleted: $file" -ForegroundColor Green
        $deletedCount++
    }
}

# Summary
Write-Host "`n=== Cleanup Summary ===" -ForegroundColor Yellow
Write-Host "Total files/directories deleted: $deletedCount" -ForegroundColor Green
Write-Host "`nCleanup completed successfully!" -ForegroundColor Green
Write-Host "`nNote: The following were preserved:" -ForegroundColor Cyan
Write-Host "  - Core source code (freecad/ directory)" -ForegroundColor White
Write-Host "  - Essential docs (README.md, DEVELOPMENT.md, LICENSE)" -ForegroundColor White
Write-Host "  - Configuration files" -ForegroundColor White
Write-Host "  - Organized tests (tests/ directory)" -ForegroundColor White
Write-Host "  - Important guides (BIM, MATERIAL, THAI_STANDARDS, etc.)" -ForegroundColor White
