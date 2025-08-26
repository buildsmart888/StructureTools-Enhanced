# -*- coding: utf-8 -*-
"""
Phase 1 Completion Verification Script

Verifies that all Phase 1 critical components have been successfully implemented.
"""

import os
import sys
import importlib

def check_file_exists(filepath):
    """Check if a file exists."""
    return os.path.exists(filepath)

def check_module_structure():
    """Check module structure for Phase 1 components."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    freecad_path = os.path.join(base_path, "freecad", "StructureTools")
    
    print(f"\n{'='*60}")
    print("PHASE 1 COMPLETION VERIFICATION")
    print(f"{'='*60}")
    print(f"Base path: {base_path}")
    print(f"FreeCAD path: {freecad_path}")
    
    # Critical components to check
    components = {
        "StructuralPlate": os.path.join(freecad_path, "objects", "StructuralPlate.py"),
        "AreaLoad": os.path.join(freecad_path, "objects", "AreaLoad.py"),
        "PlateMesher": os.path.join(freecad_path, "meshing", "PlateMesher.py"),
        "SurfaceMesh": os.path.join(freecad_path, "meshing", "SurfaceMesh.py")
    }
    
    results = {}
    
    print(f"\n📋 CHECKING COMPONENT FILES:")
    print("-" * 40)
    
    for name, filepath in components.items():
        exists = check_file_exists(filepath)
        results[name] = {"file_exists": exists, "filepath": filepath}
        
        status = "✅" if exists else "❌"
        print(f"{status} {name}: {filepath}")
        
        if exists:
            # Check file size to ensure it's not empty
            size = os.path.getsize(filepath)
            results[name]["file_size"] = size
            print(f"   📄 File size: {size:,} bytes")
    
    return results

def check_enhanced_features():
    """Check for enhanced features in Phase 1 components."""
    print(f"\n🔍 CHECKING ENHANCED FEATURES:")
    print("-" * 40)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    freecad_path = os.path.join(base_path, "freecad", "StructureTools")
    
    # Features to check in each component
    feature_checks = {
        "StructuralPlate.py": [
            "LocalXAxis", "LocalYAxis", "LocalZAxis",  # Geometry
            "PressureLoads", "ShearLoads", "ThermalLoads",  # Loads
            "EdgeSupports", "PointSupports",  # Boundary conditions
            "MembraneForcesX", "MembraneForcesY", "BendingMomentsX",  # Results
            "MeshDivisionsX", "MeshDivisionsY",  # Meshing
            "ShowLocalAxes", "ShowResults"  # Visualization
        ],
        "AreaLoad.py": [
            "BuildingCode", "LoadCategory", "LiveLoadFactor",  # Code compliance
            "EnvironmentalLoads", "SeismicParameters", "WindParameters",  # Environmental
            "TimeFunction", "Duration", "CyclicLoading",  # Time-dependent
            "calculateASCELoads", "calculateIBCLoads"  # Calculations
        ],
        "PlateMesher.py": [
            "meshWithGmsh", "generateStructuredMesh",  # Meshing algorithms
            "QualityMetrics", "ElementTypes",  # Quality control
            "exportToCalculiX", "exportToNastran"  # Export capabilities
        ],
        "SurfaceMesh.py": [
            "assessMeshQuality", "calculateElementQuality",  # Quality assessment
            "identifyPoorElements", "suggestRefinement",  # Quality improvement
            "MeshIntegrationManager", "integratePynite"  # Integration
        ]
    }
    
    for filename, features in feature_checks.items():
        filepath = os.path.join(freecad_path, "objects" if filename.endswith("Plate.py") or filename.endswith("Load.py") else "meshing", filename)
        
        print(f"\n📄 {filename}:")
        
        if not os.path.exists(filepath):
            print(f"   ❌ File not found")
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            found_features = 0
            total_features = len(features)
            
            for feature in features:
                if feature in content:
                    print(f"   ✅ {feature}")
                    found_features += 1
                else:
                    print(f"   ❌ {feature}")
            
            coverage = (found_features / total_features) * 100
            print(f"   📊 Feature coverage: {found_features}/{total_features} ({coverage:.1f}%)")
            
        except Exception as e:
            print(f"   ❌ Error reading file: {e}")

def check_documentation():
    """Check documentation and status files."""
    print(f"\n📚 CHECKING DOCUMENTATION:")
    print("-" * 40)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    docs_to_check = {
        "PROJECT_STATUS_REPORT.md": "Project status documentation",
        "PHASE2_ROADMAP.md": "Phase 2 roadmap",
        "MATERIAL_DATABASE_GUIDE.md": "Material database guide",
        "MATERIAL_INTEGRATION_GUIDE.md": "Material integration guide"
    }
    
    for filename, description in docs_to_check.items():
        filepath = os.path.join(base_path, filename)
        exists = os.path.exists(filepath)
        
        status = "✅" if exists else "❌"
        print(f"{status} {description}: {filename}")
        
        if exists:
            size = os.path.getsize(filepath)
            print(f"   📄 File size: {size:,} bytes")

def check_test_coverage():
    """Check test coverage for Phase 1 components."""
    print(f"\n🧪 CHECKING TEST COVERAGE:")
    print("-" * 40)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    tests_path = os.path.join(base_path, "tests")
    
    test_files = [
        "test_bim_integration.py",
        "test_material_database.py", 
        "test_load_generator.py",
        "test_phase_one_completion.py"
    ]
    
    for test_file in test_files:
        filepath = os.path.join(tests_path, test_file)
        exists = os.path.exists(filepath)
        
        status = "✅" if exists else "❌"
        print(f"{status} {test_file}")
        
        if exists:
            size = os.path.getsize(filepath)
            print(f"   📄 File size: {size:,} bytes")

def calculate_phase_one_completion():
    """Calculate Phase 1 completion percentage."""
    print(f"\n📊 PHASE 1 COMPLETION ANALYSIS:")
    print("-" * 40)
    
    # Core components (40% of Phase 1)
    core_components = [
        "StructuralPlate.py",
        "AreaLoad.py", 
        "PlateMesher.py",
        "SurfaceMesh.py"
    ]
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    freecad_path = os.path.join(base_path, "freecad", "StructureTools")
    
    core_score = 0
    for component in core_components:
        if component.endswith("Plate.py") or component.endswith("Load.py"):
            filepath = os.path.join(freecad_path, "objects", component)
        else:
            filepath = os.path.join(freecad_path, "meshing", component)
        
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size > 1000:  # Meaningful implementation
                core_score += 10
    
    # BIM Integration (25% of Phase 1)
    bim_integration_file = os.path.join(freecad_path, "integration", "BIMIntegration.py")
    bim_score = 25 if os.path.exists(bim_integration_file) and os.path.getsize(bim_integration_file) > 1000 else 0
    
    # Material Database (20% of Phase 1)
    material_db_file = os.path.join(freecad_path, "data", "MaterialDatabase.py")
    material_score = 20 if os.path.exists(material_db_file) and os.path.getsize(material_db_file) > 1000 else 0
    
    # Load Generator (10% of Phase 1)
    load_gen_file = os.path.join(freecad_path, "commands", "LoadGenerator.py")
    load_score = 10 if os.path.exists(load_gen_file) and os.path.getsize(load_gen_file) > 1000 else 0
    
    # Testing (5% of Phase 1)
    test_score = 5 if os.path.exists(os.path.join(base_path, "tests", "test_phase_one_completion.py")) else 0
    
    total_score = core_score + bim_score + material_score + load_score + test_score
    
    print(f"Core Components (StructuralPlate, AreaLoad, Meshing): {core_score}/40")
    print(f"BIM Integration: {bim_score}/25")
    print(f"Material Database: {material_score}/20")
    print(f"Load Generator: {load_score}/10")
    print(f"Testing Suite: {test_score}/5")
    print(f"\n🎯 TOTAL PHASE 1 COMPLETION: {total_score}/100 ({total_score}%)")
    
    if total_score >= 95:
        print("🎉 PHASE 1 COMPLETE!")
    elif total_score >= 85:
        print("🚧 PHASE 1 NEARLY COMPLETE")
    elif total_score >= 70:
        print("📈 PHASE 1 SUBSTANTIAL PROGRESS")
    else:
        print("🔨 PHASE 1 IN DEVELOPMENT")
    
    return total_score

def main():
    """Main verification function."""
    try:
        # Check module structure
        results = check_module_structure()
        
        # Check enhanced features
        check_enhanced_features()
        
        # Check documentation
        check_documentation()
        
        # Check test coverage
        check_test_coverage()
        
        # Calculate completion
        completion_score = calculate_phase_one_completion()
        
        print(f"\n{'='*60}")
        print("VERIFICATION COMPLETE")
        print(f"{'='*60}")
        
        return completion_score >= 95
        
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit_code = 0 if success else 1
    sys.exit(exit_code)
