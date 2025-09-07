#!/usr/bin/env python3
"""
Test All Material Objects

This script finds and tests all material objects in the current document
to identify any that may be showing incorrect properties (steel instead of concrete).

Usage:
1. Open your FreeCAD document containing material objects
2. Run this script in FreeCAD Python console:
   exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_all_material_objects.py').read())
"""

import FreeCAD as App

def find_all_material_objects():
    """Find all material objects in the current document."""
    if not App.ActiveDocument:
        print("❌ No active document. Please open the document first.")
        return []
    
    material_objects = []
    
    for obj in App.ActiveDocument.Objects:
        # Check if object has material properties
        if (hasattr(obj, 'Density') and 
            hasattr(obj, 'ModulusElasticity') and 
            hasattr(obj, 'PoissonRatio')):
            material_objects.append(obj)
    
    print(f"✅ Found {len(material_objects)} material objects")
    return material_objects

def analyze_material_object(obj):
    """Analyze a material object to detect potential issues."""
    print(f"\n📊 Analyzing: {obj.Label} ({obj.Name})")
    
    issues = []
    properties = {}
    
    # Get current properties
    if hasattr(obj, 'Density'):
        density_str = str(obj.Density)
        properties['density'] = density_str
        print(f"   Density: {density_str}")
        
        # Check for steel density (wrong for concrete)
        if '7850' in density_str:
            issues.append("Steel density detected (7850 kg/m³) - may be incorrect for concrete")
    
    if hasattr(obj, 'ModulusElasticity'):
        modulus_str = str(obj.ModulusElasticity)
        properties['modulus'] = modulus_str
        print(f"   Modulus: {modulus_str}")
        
        # Check for steel modulus (wrong for concrete)
        if '200000' in modulus_str or '200.00 GPa' in modulus_str:
            issues.append("Steel modulus detected (200 GPa) - may be incorrect for concrete")
    
    if hasattr(obj, 'PoissonRatio'):
        poisson = obj.PoissonRatio
        properties['poisson'] = poisson
        print(f"   Poisson: {poisson}")
        
        # Check for steel Poisson ratio (wrong for concrete)
        if abs(poisson - 0.30) < 0.01:
            issues.append("Steel Poisson ratio detected (0.30) - may be incorrect for concrete")
    
    if hasattr(obj, 'MaterialStandard'):
        standard = obj.MaterialStandard
        properties['standard'] = standard
        print(f"   Standard: {standard}")
        
        # Check for concrete standard with steel properties
        if 'concrete' in standard.lower() or 'aci' in standard.lower():
            if issues:
                issues.append(f"Concrete standard '{standard}' but showing steel properties!")
    else:
        properties['standard'] = None
        print("   Standard: Not set (old Material system)")
    
    # Determine material classification
    if issues:
        classification = "❌ PROBLEMATIC"
        print(f"   🚨 Issues found: {len(issues)}")
        for issue in issues:
            print(f"      - {issue}")
    else:
        classification = "✅ OK"
        print(f"   ✅ No issues detected")
    
    return {
        'object': obj,
        'properties': properties,
        'issues': issues,
        'classification': classification
    }

def fix_problematic_object(obj):
    """Fix a problematic material object using the MaterialStandard mechanism."""
    print(f"\n🔧 Attempting to fix: {obj.Label}")
    
    if not hasattr(obj, 'MaterialStandard'):
        print("   ❌ Cannot fix: No MaterialStandard property (old system)")
        return False
    
    try:
        # Get current MaterialStandard
        current_standard = obj.MaterialStandard
        print(f"   📋 Current MaterialStandard: {current_standard}")
        
        if not current_standard or current_standard == "":
            print("   ❌ Cannot fix: MaterialStandard is empty")
            return False
        
        # Force property refresh by temporarily changing MaterialStandard
        print("   🔄 Triggering property refresh...")
        
        # Clear and restore to trigger onChanged
        obj.MaterialStandard = ""
        obj.MaterialStandard = current_standard
        
        # Force recompute
        obj.recompute()
        App.ActiveDocument.recompute()
        
        print("   ✅ Fix applied - properties should be updated from database")
        return True
        
    except Exception as e:
        print(f"   ❌ Error during fix: {e}")
        return False

def run_material_objects_test():
    """Run complete test of all material objects."""
    print("MATERIAL OBJECTS TEST")
    print("=" * 80)
    print("Testing all material objects for property consistency...")
    print()
    
    # Find all material objects
    material_objects = find_all_material_objects()
    
    if not material_objects:
        print("❌ No material objects found in document")
        return
    
    # Analyze each object
    results = []
    problematic_objects = []
    
    for obj in material_objects:
        result = analyze_material_object(obj)
        results.append(result)
        
        if result['issues']:
            problematic_objects.append(obj)
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total material objects: {len(material_objects)}")
    print(f"Objects with issues: {len(problematic_objects)}")
    print(f"Objects OK: {len(material_objects) - len(problematic_objects)}")
    
    if problematic_objects:
        print(f"\n🚨 PROBLEMATIC OBJECTS:")
        for obj in problematic_objects:
            print(f"   - {obj.Label} ({obj.Name})")
        
        # Ask user if they want to fix all problematic objects
        print(f"\n⚠️  Found {len(problematic_objects)} objects with potential issues.")
        response = input("Fix all problematic objects automatically? (y/N): ").lower().strip()
        
        if response in ['y', 'yes']:
            print(f"\n🔧 Fixing {len(problematic_objects)} objects...")
            
            fixed_count = 0
            failed_count = 0
            
            for obj in problematic_objects:
                if fix_problematic_object(obj):
                    fixed_count += 1
                else:
                    failed_count += 1
            
            print(f"\n📊 FIX RESULTS:")
            print(f"   ✅ Successfully fixed: {fixed_count}")
            print(f"   ❌ Failed to fix: {failed_count}")
            
            if fixed_count > 0:
                print(f"\n🎉 {fixed_count} objects have been fixed!")
                print("Please check the Model Data property panel to verify correct values.")
        else:
            print("❌ Fix cancelled by user")
    else:
        print("\n🎉 All material objects appear to have correct properties!")
    
    # Detailed results
    if len(material_objects) <= 10:  # Only show details if not too many objects
        print(f"\n{'='*60}")
        print("DETAILED RESULTS")
        print(f"{'='*60}")
        
        for result in results:
            obj = result['object']
            classification = result['classification']
            issues = result['issues']
            
            print(f"\n{classification} {obj.Label}")
            if issues:
                for issue in issues:
                    print(f"   🚨 {issue}")

if __name__ == "__main__":
    run_material_objects_test()