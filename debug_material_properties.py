#!/usr/bin/env python3
"""
Debug script to verify material properties and fix incorrect assignments.

This script:
1. Lists all material objects in the document
2. Checks their properties against the database
3. Fixes incorrect property assignments
4. Provides detailed diagnostic information

Usage:
- Run this script in FreeCAD console
- Check the output for material property issues
"""

import FreeCAD as App

def find_material_objects():
    """Find all material objects in active document."""
    if not App.ActiveDocument:
        print("❌ No active document")
        return []
    
    materials = []
    for obj in App.ActiveDocument.Objects:
        # Check for StructuralMaterial objects
        if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
            class_name = obj.Proxy.__class__.__name__
            if 'Material' in class_name:
                materials.append(obj)
        # Also check for objects with material-like properties
        elif (hasattr(obj, 'Density') and hasattr(obj, 'ModulusElasticity') and 
              hasattr(obj, 'PoissonRatio')):
            materials.append(obj)
    
    return materials

def debug_material_properties(material_obj):
    """Debug material properties and compare with database."""
    print(f"\n{'='*60}")
    print(f"DEBUGGING MATERIAL: {material_obj.Label}")
    print(f"{'='*60}")
    
    # Basic info
    print(f"Object Name: {material_obj.Name}")
    print(f"Object Label: {material_obj.Label}")
    print(f"Object Type: {material_obj.TypeId}")
    
    if hasattr(material_obj, 'Proxy') and material_obj.Proxy:
        print(f"Proxy Class: {material_obj.Proxy.__class__.__name__}")
    
    # Material Standard
    if hasattr(material_obj, 'MaterialStandard'):
        print(f"Material Standard: {material_obj.MaterialStandard}")
        standard = material_obj.MaterialStandard
        
        # Check if standard exists in database
        try:
            from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
            
            if standard in MATERIAL_STANDARDS:
                print("✅ Standard found in database")
                db_props = MATERIAL_STANDARDS[standard]
                print(f"Database properties: {list(db_props.keys())}")
                
                # Compare properties
                print(f"\n📊 PROPERTY COMPARISON:")
                print(f"{'Property':<20} {'Current':<20} {'Database':<20} {'Status'}")
                print(f"{'-'*80}")
                
                # Density
                if hasattr(material_obj, 'Density'):
                    current_density = str(material_obj.Density)
                    db_density = db_props.get('Density', 'N/A')
                    status = "✅ OK" if current_density == db_density else "❌ MISMATCH"
                    print(f"{'Density':<20} {current_density:<20} {db_density:<20} {status}")
                
                # Modulus of Elasticity
                if hasattr(material_obj, 'ModulusElasticity'):
                    current_E = str(material_obj.ModulusElasticity)
                    db_E = db_props.get('ModulusElasticity', 'N/A')
                    status = "✅ OK" if current_E == db_E else "❌ MISMATCH"
                    print(f"{'ModulusElasticity':<20} {current_E:<20} {db_E:<20} {status}")
                
                # Poisson Ratio
                if hasattr(material_obj, 'PoissonRatio'):
                    current_nu = material_obj.PoissonRatio
                    db_nu = db_props.get('PoissonRatio', 'N/A')
                    status = "✅ OK" if abs(current_nu - db_nu) < 0.01 else "❌ MISMATCH"
                    print(f"{'PoissonRatio':<20} {current_nu:<20} {db_nu:<20} {status}")
                
                # Yield Strength
                if hasattr(material_obj, 'YieldStrength'):
                    current_fy = str(material_obj.YieldStrength)
                    db_fy = db_props.get('YieldStrength', 'N/A')
                    status = "✅ OK" if current_fy == db_fy else "❌ MISMATCH"
                    print(f"{'YieldStrength':<20} {current_fy:<20} {db_fy:<20} {status}")
                
                # Ultimate Strength
                if hasattr(material_obj, 'UltimateStrength'):
                    current_fu = str(material_obj.UltimateStrength)
                    db_fu = db_props.get('UltimateStrength', 'N/A')
                    status = "✅ OK" if current_fu == db_fu else "❌ MISMATCH"
                    print(f"{'UltimateStrength':<20} {current_fu:<20} {db_fu:<20} {status}")
                
                return True, db_props
            else:
                print(f"❌ Standard '{standard}' NOT found in database")
                print("Available standards:")
                for available_std in sorted(MATERIAL_STANDARDS.keys()):
                    if 'ACI' in available_std or 'Concrete' in available_std:
                        print(f"  - {available_std}")
                return False, {}
                
        except ImportError as e:
            print(f"❌ Cannot import material database: {e}")
            return False, {}
    else:
        print("❌ No MaterialStandard property found")
        return False, {}

def fix_material_properties(material_obj, db_props):
    """Fix material properties based on database values."""
    print(f"\n🔧 FIXING MATERIAL PROPERTIES...")
    
    fixed_count = 0
    
    # Fix each property
    for prop_name, db_value in db_props.items():
        if hasattr(material_obj, prop_name):
            try:
                current_value = getattr(material_obj, prop_name)
                if str(current_value) != str(db_value):
                    setattr(material_obj, prop_name, db_value)
                    print(f"  ✅ Fixed {prop_name}: {current_value} → {db_value}")
                    fixed_count += 1
                else:
                    print(f"  ✓ {prop_name} already correct")
            except Exception as e:
                print(f"  ❌ Error fixing {prop_name}: {e}")
    
    if fixed_count > 0:
        try:
            App.ActiveDocument.recompute()
            print(f"\n✅ Fixed {fixed_count} properties and recomputed document")
        except Exception as e:
            print(f"\n❌ Error recomputing document: {e}")
    else:
        print("\n✅ No fixes needed - all properties correct")

def check_material_naming():
    """Check for materials with incorrect naming."""
    print(f"\n{'='*60}")
    print("CHECKING MATERIAL NAMING PATTERNS")
    print(f"{'='*60}")
    
    materials = find_material_objects()
    
    naming_issues = []
    for material in materials:
        name = material.Label
        if 'ACI_Normal_30MPA' in name:  # Incorrect capitalization
            correct_name = name.replace('MPA', 'MPa')
            naming_issues.append((material, name, correct_name))
            print(f"❌ Incorrect naming: {name}")
            print(f"   Should be: {correct_name}")
    
    return naming_issues

def fix_material_naming(naming_issues):
    """Fix material naming issues."""
    if not naming_issues:
        print("✅ No naming issues found")
        return
    
    print(f"\n🔧 FIXING MATERIAL NAMES...")
    for material, old_name, new_name in naming_issues:
        try:
            material.Label = new_name
            print(f"  ✅ Renamed: {old_name} → {new_name}")
        except Exception as e:
            print(f"  ❌ Error renaming {old_name}: {e}")
    
    try:
        App.ActiveDocument.recompute()
        print("\n✅ All naming fixes applied")
    except Exception as e:
        print(f"\n❌ Error recomputing after renaming: {e}")

def run_material_diagnostics():
    """Run complete material diagnostics."""
    print("MATERIAL PROPERTIES DIAGNOSTIC TOOL")
    print("="*80)
    
    if not App.ActiveDocument:
        print("❌ No active document. Please open a document first.")
        return
    
    materials = find_material_objects()
    
    if not materials:
        print("❌ No material objects found in the document")
        return
    
    print(f"✅ Found {len(materials)} material objects")
    
    # Check naming issues first
    naming_issues = check_material_naming()
    if naming_issues:
        response = input("\n🤔 Fix naming issues? (y/N): ").lower().strip()
        if response in ['y', 'yes']:
            fix_material_naming(naming_issues)
    
    # Debug each material
    materials_with_issues = []
    
    for material in materials:
        has_database, db_props = debug_material_properties(material)
        
        if has_database and db_props:
            # Check if any properties are wrong
            has_issues = False
            
            # Quick check for common issues
            if hasattr(material, 'Density'):
                current_density = str(material.Density)
                db_density = db_props.get('Density', '')
                if current_density != db_density:
                    has_issues = True
            
            if hasattr(material, 'ModulusElasticity'):
                current_E = str(material.ModulusElasticity)
                db_E = db_props.get('ModulusElasticity', '')
                if current_E != db_E:
                    has_issues = True
            
            if has_issues:
                materials_with_issues.append((material, db_props))
    
    # Offer to fix issues
    if materials_with_issues:
        print(f"\n⚠️  Found {len(materials_with_issues)} materials with property issues")
        response = input("🤔 Fix all property issues? (y/N): ").lower().strip()
        if response in ['y', 'yes']:
            for material, db_props in materials_with_issues:
                fix_material_properties(material, db_props)
    
    # Final summary
    print(f"\n{'='*80}")
    print("DIAGNOSTIC COMPLETE")
    print(f"{'='*80}")
    print(f"Total materials checked: {len(materials)}")
    print(f"Materials with naming issues: {len(naming_issues)}")
    print(f"Materials with property issues: {len(materials_with_issues)}")

def create_test_concrete_material():
    """Create a test concrete material to verify the fix."""
    print(f"\n{'='*60}")
    print("CREATING TEST CONCRETE MATERIAL")
    print(f"{'='*60}")
    
    try:
        from freecad.StructureTools.utils.MaterialHelper import create_concrete_30mpa
        
        # Create concrete material
        concrete = create_concrete_30mpa("Test_Concrete_30MPa")
        
        if concrete:
            print("✅ Test concrete material created successfully")
            debug_material_properties(concrete)
            return concrete
        else:
            print("❌ Failed to create test concrete material")
            return None
    
    except Exception as e:
        print(f"❌ Error creating test concrete material: {e}")
        return None

if __name__ == "__main__":
    # Run diagnostics
    run_material_diagnostics()
    
    # Create test material
    print("\n" + "="*80)
    create_test_concrete_material()