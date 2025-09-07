#!/usr/bin/env python3
"""
Fix Existing Material Objects in FreeCAD Document

This script fixes material objects that are already created in FreeCAD documents
but are showing incorrect properties in the Model Data property panel.

The problem: Existing material objects may have incorrect properties that were
set before the MaterialDatabase and MaterialStandards fixes.

Usage:
1. Open your FreeCAD document with problematic materials
2. Run this script in FreeCAD Python console:
   exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\fix_existing_material_objects.py').read())
"""

import FreeCAD as App

def find_all_material_objects():
    """Find all material objects in active document."""
    if not App.ActiveDocument:
        print("❌ No active document. Please open a document first.")
        return []
    
    materials = []
    
    for obj in App.ActiveDocument.Objects:
        is_material = False
        
        # Check if it has material-like properties
        if (hasattr(obj, 'Density') and hasattr(obj, 'ModulusElasticity') and 
            hasattr(obj, 'PoissonRatio')):
            is_material = True
        
        # Check by object name/label
        if ('material' in obj.Name.lower() or 'material' in obj.Label.lower()):
            is_material = True
        
        # Check by proxy type
        if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
            class_name = obj.Proxy.__class__.__name__
            if 'Material' in class_name:
                is_material = True
        
        if is_material:
            materials.append(obj)
    
    return materials

def analyze_material_object(material_obj):
    """Analyze a material object and determine if it needs fixing."""
    print(f"\n🔍 Analyzing: {material_obj.Label} ({material_obj.Name})")
    
    issues = []
    material_type = "unknown"
    
    # Determine material type from name/label
    name_lower = (material_obj.Label + " " + material_obj.Name).lower()
    
    if any(term in name_lower for term in ['concrete', 'คอนกรีต', 'fc', 'aci_normal', 'c25', 'c30']):
        material_type = "concrete"
    elif any(term in name_lower for term in ['steel', 'เหล็ก', 'astm', 'sd40', 'sd50']):
        material_type = "steel"
    
    print(f"   Detected type: {material_type}")
    
    # Check current properties
    current_props = {}
    
    if hasattr(material_obj, 'Density'):
        density_str = str(material_obj.Density)
        if 'kg/m' in density_str:
            current_props['density'] = float(density_str.split()[0])
        else:
            current_props['density'] = float(density_str)
        print(f"   Current Density: {current_props['density']} kg/m³")
    
    if hasattr(material_obj, 'ModulusElasticity'):
        modulus_str = str(material_obj.ModulusElasticity)
        if 'MPa' in modulus_str:
            current_props['modulus'] = float(modulus_str.split()[0])
        elif 'GPa' in modulus_str:
            current_props['modulus'] = float(modulus_str.split()[0]) * 1000
        else:
            current_props['modulus'] = float(modulus_str)
        print(f"   Current Modulus: {current_props['modulus']} MPa")
    
    if hasattr(material_obj, 'PoissonRatio'):
        current_props['poisson'] = material_obj.PoissonRatio
        print(f"   Current Poisson: {current_props['poisson']}")
    
    # Check for issues based on material type
    if material_type == "concrete":
        # Concrete should have: 2400 kg/m³, 25000-35000 MPa, 0.20
        if current_props.get('density', 0) == 7850:
            issues.append("density_steel_instead_concrete")
            print(f"   ❌ ISSUE: Concrete has steel density (7850 kg/m³)")
        elif current_props.get('density', 0) not in range(2000, 2600):
            issues.append("density_wrong")
            print(f"   ⚠️  Warning: Unusual concrete density")
        
        if current_props.get('modulus', 0) == 200000:
            issues.append("modulus_steel_instead_concrete")
            print(f"   ❌ ISSUE: Concrete has steel modulus (200000 MPa)")
        elif current_props.get('modulus', 0) not in range(15000, 50000):
            issues.append("modulus_wrong")
            print(f"   ⚠️  Warning: Unusual concrete modulus")
        
        if abs(current_props.get('poisson', 0) - 0.30) < 0.01:
            issues.append("poisson_steel_instead_concrete")
            print(f"   ❌ ISSUE: Concrete has steel Poisson ratio (0.30)")
        elif abs(current_props.get('poisson', 0) - 0.20) > 0.05:
            issues.append("poisson_wrong")
            print(f"   ⚠️  Warning: Unusual concrete Poisson ratio")
    
    elif material_type == "steel":
        # Steel should have: 7850 kg/m³, 200000 MPa, 0.30
        if current_props.get('density', 0) == 2400:
            issues.append("density_concrete_instead_steel")
            print(f"   ❌ ISSUE: Steel has concrete density (2400 kg/m³)")
        
        if current_props.get('modulus', 0) in range(25000, 35000):
            issues.append("modulus_concrete_instead_steel")
            print(f"   ❌ ISSUE: Steel has concrete modulus ({current_props['modulus']} MPa)")
        
        if abs(current_props.get('poisson', 0) - 0.20) < 0.01:
            issues.append("poisson_concrete_instead_steel")
            print(f"   ❌ ISSUE: Steel has concrete Poisson ratio (0.20)")
    
    if not issues:
        print(f"   ✅ No issues found")
    
    return {
        'object': material_obj,
        'type': material_type,
        'current_props': current_props,
        'issues': issues
    }

def fix_material_object(analysis_result):
    """Fix a material object based on analysis."""
    obj = analysis_result['object']
    material_type = analysis_result['type']
    issues = analysis_result['issues']
    
    if not issues:
        return False  # No fixes needed
    
    print(f"\n🔧 Fixing: {obj.Label}")
    
    fixes_applied = 0
    
    if material_type == "concrete":
        # Apply correct concrete properties
        correct_props = {
            'density': 2400,  # kg/m³
            'modulus': 27000,  # MPa (default for C30)
            'poisson': 0.20
        }
        
        # Try to determine specific concrete grade
        name_lower = (obj.Label + " " + obj.Name).lower()
        if '25' in name_lower or 'c25' in name_lower:
            correct_props['modulus'] = 25000
        elif '30' in name_lower or 'c30' in name_lower:
            correct_props['modulus'] = 27000
        elif '280' in name_lower or 'fc280' in name_lower:
            correct_props['modulus'] = 24870
        elif '210' in name_lower or 'fc210' in name_lower:
            correct_props['modulus'] = 21579
        
        # Apply fixes
        if any(issue.startswith('density_') for issue in issues):
            try:
                obj.Density = f"{correct_props['density']} kg/m^3"
                print(f"   ✅ Fixed Density: {correct_props['density']} kg/m³")
                fixes_applied += 1
            except Exception as e:
                print(f"   ❌ Error fixing density: {e}")
        
        if any(issue.startswith('modulus_') for issue in issues):
            try:
                obj.ModulusElasticity = f"{correct_props['modulus']} MPa"
                print(f"   ✅ Fixed Modulus: {correct_props['modulus']} MPa")
                fixes_applied += 1
            except Exception as e:
                print(f"   ❌ Error fixing modulus: {e}")
        
        if any(issue.startswith('poisson_') for issue in issues):
            try:
                obj.PoissonRatio = correct_props['poisson']
                print(f"   ✅ Fixed Poisson: {correct_props['poisson']}")
                fixes_applied += 1
            except Exception as e:
                print(f"   ❌ Error fixing Poisson ratio: {e}")
    
    elif material_type == "steel":
        # Apply correct steel properties
        correct_props = {
            'density': 7850,  # kg/m³
            'modulus': 200000,  # MPa
            'poisson': 0.30
        }
        
        # Apply fixes
        if any(issue.startswith('density_') for issue in issues):
            try:
                obj.Density = f"{correct_props['density']} kg/m^3"
                print(f"   ✅ Fixed Density: {correct_props['density']} kg/m³")
                fixes_applied += 1
            except Exception as e:
                print(f"   ❌ Error fixing density: {e}")
        
        if any(issue.startswith('modulus_') for issue in issues):
            try:
                obj.ModulusElasticity = f"{correct_props['modulus']} MPa"
                print(f"   ✅ Fixed Modulus: {correct_props['modulus']} MPa")
                fixes_applied += 1
            except Exception as e:
                print(f"   ❌ Error fixing modulus: {e}")
        
        if any(issue.startswith('poisson_') for issue in issues):
            try:
                obj.PoissonRatio = correct_props['poisson']
                print(f"   ✅ Fixed Poisson: {correct_props['poisson']}")
                fixes_applied += 1
            except Exception as e:
                print(f"   ❌ Error fixing Poisson ratio: {e}")
    
    return fixes_applied > 0

def update_material_standards():
    """Update MaterialStandard property if it exists."""
    print(f"\n📋 Updating MaterialStandard properties...")
    
    try:
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
        standards_available = True
    except ImportError:
        print("❌ MaterialStandards not available")
        standards_available = False
    
    if not standards_available:
        return
    
    materials = find_all_material_objects()
    updated_count = 0
    
    for obj in materials:
        if hasattr(obj, 'MaterialStandard'):
            name_lower = (obj.Label + " " + obj.Name).lower()
            
            # Try to map to correct standard
            new_standard = None
            
            if any(term in name_lower for term in ['concrete', 'คอนกรีต', 'fc']):
                if '30' in name_lower or 'c30' in name_lower:
                    new_standard = "ACI_Normal_30MPa"
                elif '25' in name_lower or 'c25' in name_lower:
                    new_standard = "ACI_Normal_25MPa"
                elif 'fc280' in name_lower:
                    new_standard = "ACI_Normal_30MPa"  # Closest match
                elif 'fc210' in name_lower:
                    new_standard = "ACI_Normal_25MPa"  # Closest match
            elif any(term in name_lower for term in ['steel', 'เหล็ก', 'astm']):
                if 'a36' in name_lower:
                    new_standard = "ASTM_A36"
                elif 'a992' in name_lower or 'a572' in name_lower:
                    new_standard = "ASTM_A992"
                else:
                    new_standard = "ASTM_A36"  # Default
            
            if new_standard and new_standard in MATERIAL_STANDARDS:
                try:
                    old_standard = obj.MaterialStandard
                    obj.MaterialStandard = new_standard
                    print(f"   ✅ Updated {obj.Label}: {old_standard} → {new_standard}")
                    updated_count += 1
                except Exception as e:
                    print(f"   ❌ Error updating MaterialStandard for {obj.Label}: {e}")
    
    print(f"   Updated MaterialStandard for {updated_count} objects")

def run_material_object_fix():
    """Main function to fix all material objects."""
    print("EXISTING MATERIAL OBJECTS FIX")
    print("=" * 80)
    
    if not App.ActiveDocument:
        print("❌ No active document. Please open a document first.")
        return
    
    print(f"Active Document: {App.ActiveDocument.Name}")
    
    # Find all material objects
    materials = find_all_material_objects()
    
    if not materials:
        print("❌ No material objects found in the document")
        return
    
    print(f"✅ Found {len(materials)} material objects")
    
    # Analyze each material
    analyses = []
    problematic_materials = []
    
    for material in materials:
        analysis = analyze_material_object(material)
        analyses.append(analysis)
        
        if analysis['issues']:
            problematic_materials.append(analysis)
    
    # Summary
    print(f"\n{'='*60}")
    print("ANALYSIS SUMMARY")
    print(f"{'='*60}")
    print(f"Total materials analyzed: {len(analyses)}")
    print(f"Materials with issues: {len(problematic_materials)}")
    
    if problematic_materials:
        print(f"\nProblematic materials:")
        for analysis in problematic_materials:
            obj = analysis['object']
            issues = analysis['issues']
            print(f"  - {obj.Label}: {', '.join(issues)}")
    
    # Offer to fix issues
    if problematic_materials:
        print(f"\n🤔 Fix all problematic materials? This will update their properties.")
        response = input("Continue with fixes? (y/N): ").lower().strip()
        
        if response in ['y', 'yes']:
            fixed_count = 0
            for analysis in problematic_materials:
                if fix_material_object(analysis):
                    fixed_count += 1
            
            # Update MaterialStandard properties
            update_material_standards()
            
            # Recompute document
            try:
                App.ActiveDocument.recompute()
                print(f"\n✅ Document recomputed successfully")
            except Exception as e:
                print(f"\n❌ Error recomputing document: {e}")
            
            print(f"\n{'='*80}")
            print("FIX COMPLETE")
            print(f"{'='*80}")
            print(f"✅ Fixed {fixed_count} material objects")
            print("ℹ️  Check the Model Data property panel - it should now show correct values!")
            print("ℹ️  Properties should be:")
            print("   - Concrete: 2400 kg/m³, 25000-27000 MPa, 0.20 Poisson")  
            print("   - Steel: 7850 kg/m³, 200000 MPa, 0.30 Poisson")
        else:
            print("❌ No fixes applied")
    else:
        print("✅ All material objects have correct properties!")

if __name__ == "__main__":
    run_material_object_fix()