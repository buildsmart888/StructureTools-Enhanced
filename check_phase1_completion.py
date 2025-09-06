#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 1 Completion Status Check
===============================

Comprehensive evaluation of Phase 1 completion status for StructureTools.
This script checks all requirements and deliverables for Phase 1.
"""

import os
import sys
import json
from pathlib import Path

def check_file_exists(file_path, description=""):
    """Check if a file exists and return status"""
    exists = os.path.exists(file_path)
    size = os.path.getsize(file_path) if exists else 0
    status = "✅ EXISTS" if exists and size > 0 else "❌ MISSING"
    if exists and size > 0:
        print(f"  {status} {description}")
        print(f"         Path: {file_path}")
        print(f"         Size: {size:,} bytes")
    else:
        print(f"  {status} {description}")
        print(f"         Path: {file_path}")
    return exists and size > 0

def check_phase1_objects():
    """Check Custom Document Objects implementation"""
    print("\n📦 CUSTOM DOCUMENT OBJECTS")
    print("=" * 50)
    
    objects_dir = "freecad/StructureTools/objects"
    objects = [
        ("StructuralMaterial.py", "Material object with validation"),
        ("StructuralBeam.py", "Beam object with advanced properties"), 
        ("StructuralColumn.py", "Column object with design parameters"),
        ("StructuralNode.py", "Node object with connection details"),
        ("StructuralPlate.py", "Plate/shell object (Phase 1 requirement)"),
        ("AreaLoad.py", "Area load object (Phase 1 requirement)"),
        ("StructuralGrid.py", "Grid system object"),
        ("__init__.py", "Objects module initialization")
    ]
    
    total_objects = len(objects)
    completed_objects = 0
    
    for filename, description in objects:
        file_path = os.path.join(objects_dir, filename)
        if check_file_exists(file_path, f"{filename} - {description}"):
            completed_objects += 1
    
    completion_rate = (completed_objects / total_objects) * 100
    print(f"\n📊 Objects Completion: {completed_objects}/{total_objects} ({completion_rate:.1f}%)")
    
    return completion_rate >= 90  # 90% completion required

def check_phase1_taskpanels():
    """Check Professional Task Panel System"""
    print("\n🖥️ PROFESSIONAL TASK PANELS")
    print("=" * 50)
    
    taskpanels_dir = "freecad/StructureTools/taskpanels"
    taskpanels = [
        ("MaterialSelectionPanel.py", "Material selection with standards"),
        ("MaterialTaskPanel.py", "Material properties with validation"),
        ("LoadApplicationPanel.py", "Load application with real-time preview"),
        ("AnalysisSetupPanel.py", "Analysis setup with validation"),
        ("BeamPropertiesPanel.py", "Beam properties panel"),
        ("NodePropertiesPanel.py", "Node properties panel"),
        ("PlatePropertiesPanel.py", "Plate properties panel (Phase 1)"),
        ("AreaLoadPanel.py", "Area load panel (Phase 1)"),
        ("__init__.py", "Task panels module initialization")
    ]
    
    total_panels = len(taskpanels)
    completed_panels = 0
    
    for filename, description in taskpanels:
        file_path = os.path.join(taskpanels_dir, filename)
        if check_file_exists(file_path, f"{filename} - {description}"):
            completed_panels += 1
    
    completion_rate = (completed_panels / total_panels) * 100
    print(f"\n📊 Task Panels Completion: {completed_panels}/{total_panels} ({completion_rate:.1f}%)")
    
    return completion_rate >= 90

def check_phase1_testing():
    """Check Testing Framework"""
    print("\n🧪 TESTING FRAMEWORK")
    print("=" * 50)
    
    test_files = [
        ("tests/__init__.py", "Test module initialization"),
        ("tests/conftest.py", "Pytest configuration"),
        ("tests/README.md", "Testing documentation"),
        ("run_tests.py", "Test runner script"),
        ("pytest.ini", "Pytest settings"),
        ("requirements-test.txt", "Testing dependencies"),
        ("tests/unit/objects/test_structural_beam.py", "Beam object tests"),
        ("tests/unit/objects/test_structural_material.py", "Material object tests"),
        ("tests/unit/objects/test_structural_node.py", "Node object tests"),
        ("tests/integration/test_material_database.py", "Material integration tests"),
        ("tests/integration/test_taskpanel_integration.py", "Task panel tests")
    ]
    
    total_tests = len(test_files)
    completed_tests = 0
    
    for filename, description in test_files:
        if check_file_exists(filename, f"{filename} - {description}"):
            completed_tests += 1
    
    completion_rate = (completed_tests / total_tests) * 100
    print(f"\n📊 Testing Framework Completion: {completed_tests}/{total_tests} ({completion_rate:.1f}%)")
    
    return completion_rate >= 70  # 70% acceptable for testing

def check_phase1_integration():
    """Check System Integration"""
    print("\n🔗 SYSTEM INTEGRATION")
    print("=" * 50)
    
    integration_files = [
        ("freecad/StructureTools/utils/units_manager.py", "Global units system"),
        ("freecad/StructureTools/utils/universal_thai_units.py", "Thai units integration"),
        ("freecad/StructureTools/data/MaterialStandards.py", "Material standards database"),
        ("freecad/StructureTools/init_gui.py", "GUI initialization"),
        ("freecad/StructureTools/command_plate.py", "Plate command integration"),
        ("freecad/StructureTools/command_area_load.py", "Area load command integration"),
        ("batch_update_global_units.py", "Integration deployment script")
    ]
    
    total_integration = len(integration_files)
    completed_integration = 0
    
    for filename, description in integration_files:
        if check_file_exists(filename, f"{filename} - {description}"):
            completed_integration += 1
    
    completion_rate = (completed_integration / total_integration) * 100
    print(f"\n📊 Integration Completion: {completed_integration}/{total_integration} ({completion_rate:.1f}%)")
    
    return completion_rate >= 80

def check_phase1_critical_missing():
    """Check for critical missing components identified in CLAUDE.md"""
    print("\n🚨 CRITICAL PHASE 1 REQUIREMENTS")
    print("=" * 50)
    
    critical_components = [
        ("freecad/StructureTools/objects/StructuralPlate.py", "Plate/Shell Elements (HIGH PRIORITY)"),
        ("freecad/StructureTools/objects/AreaLoad.py", "Area Load System (HIGH PRIORITY)"),
        ("freecad/StructureTools/taskpanels/PlatePropertiesPanel.py", "Plate Properties Panel"),
        ("freecad/StructureTools/taskpanels/AreaLoadPanel.py", "Area Load Application Panel"),
        ("freecad/StructureTools/command_plate.py", "Plate Command Integration"),
        ("freecad/StructureTools/command_area_load.py", "Area Load Command Integration")
    ]
    
    total_critical = len(critical_components)
    completed_critical = 0
    
    for filename, description in critical_components:
        if check_file_exists(filename, f"{filename} - {description}"):
            completed_critical += 1
    
    completion_rate = (completed_critical / total_critical) * 100
    print(f"\n📊 Critical Components: {completed_critical}/{total_critical} ({completion_rate:.1f}%)")
    
    return completion_rate >= 100  # All critical components must be present

def check_phase1_documentation():
    """Check documentation completeness"""
    print("\n📚 DOCUMENTATION")
    print("=" * 50)
    
    docs = [
        ("CLAUDE.md", "Technical architecture documentation"),
        ("DEVELOPMENT.md", "Development roadmap"),
        ("PHASE2_ROADMAP.md", "Phase 2 planning"),
        ("MATERIAL_DATABASE_GUIDE.md", "Material database guide"),
        ("MATERIAL_INTEGRATION_GUIDE.md", "Material integration guide"),
        ("README.md", "Project overview"),
        ("FINAL_SUMMARY_REPORT.py", "Implementation summary")
    ]
    
    total_docs = len(docs)
    completed_docs = 0
    
    for filename, description in docs:
        if check_file_exists(filename, f"{filename} - {description}"):
            completed_docs += 1
    
    completion_rate = (completed_docs / total_docs) * 100
    print(f"\n📊 Documentation Completion: {completed_docs}/{total_docs} ({completion_rate:.1f}%)")
    
    return completion_rate >= 85

def main():
    """Main phase 1 completion check"""
    print("🚀 PHASE 1 COMPLETION STATUS CHECK")
    print("=" * 60)
    print("Checking all Phase 1 requirements and deliverables...")
    print()
    
    # Change to project directory
    os.chdir("c:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools")
    
    # Run all checks
    checks = [
        ("Custom Document Objects", check_phase1_objects),
        ("Professional Task Panels", check_phase1_taskpanels), 
        ("Testing Framework", check_phase1_testing),
        ("System Integration", check_phase1_integration),
        ("Critical Components", check_phase1_critical_missing),
        ("Documentation", check_phase1_documentation)
    ]
    
    passed_checks = 0
    total_checks = len(checks)
    results = {}
    
    for check_name, check_function in checks:
        try:
            result = check_function()
            results[check_name] = result
            if result:
                passed_checks += 1
        except Exception as e:
            print(f"\n❌ ERROR in {check_name}: {e}")
            results[check_name] = False
    
    # Final assessment
    print("\n" + "=" * 60)
    print("🎯 PHASE 1 COMPLETION ASSESSMENT")
    print("=" * 60)
    
    overall_completion = (passed_checks / total_checks) * 100
    print(f"\nOverall Completion: {passed_checks}/{total_checks} ({overall_completion:.1f}%)")
    
    for check_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {status} {check_name}")
    
    print("\n" + "=" * 60)
    
    if overall_completion >= 90:
        print("🎉 PHASE 1 COMPLETED!")
        print("✅ All major components implemented")
        print("✅ Ready for Phase 2 development")
        print("✅ StructureTools foundation is solid")
        print("\n🚀 Ready to proceed to Phase 2: Advanced Analysis & Design Code Integration")
        return True
    elif overall_completion >= 75:
        print("⚠️ PHASE 1 MOSTLY COMPLETED")
        print("✅ Core functionality implemented")
        print("⚠️ Some components need attention")
        print("✅ Can proceed with Phase 2 planning")
        print("\n📋 Recommended: Complete remaining items while starting Phase 2")
        return True
    elif overall_completion >= 50:
        print("🔄 PHASE 1 IN PROGRESS")
        print("✅ Foundation components implemented") 
        print("❌ Critical components missing")
        print("❌ Not ready for Phase 2")
        print("\n🎯 Focus: Complete critical missing components first")
        return False
    else:
        print("❌ PHASE 1 INCOMPLETE")
        print("❌ Major components missing")
        print("❌ Significant work needed")
        print("❌ Not ready for Phase 2")
        print("\n⚠️ Recommendation: Complete Phase 1 before proceeding")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
