#!/usr/bin/env python3
"""
Diagnose Property Panel Material Issues

This script specifically diagnoses why material properties show incorrect values
in FreeCAD's Model Data property panel even after database fixes.

The issue: Material objects in FreeCAD document may have:
1. Incorrect stored property values
2. Missing or wrong MaterialStandard references
3. Properties not updating when MaterialStandard changes
4. Caching issues in FreeCAD GUI

Usage:
1. Select a material object in FreeCAD Tree View
2. Run this script in FreeCAD Python console:
   exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\diagnose_property_panel_issue.py').read())
"""

import FreeCAD as App
import FreeCADGui as Gui

def diagnose_selected_material():
    """Diagnose the currently selected material object."""
    selection = Gui.Selection.getSelection()
    
    if not selection:
        print("❌ No object selected. Please select a material object first.")
        return None
    
    obj = selection[0]
    
    # Check if it's a material object
    if not (hasattr(obj, 'Density') or hasattr(obj, 'ModulusElasticity')):
        print(f"❌ Selected object '{obj.Label}' does not appear to be a material object.")
        print("   Material objects should have Density and ModulusElasticity properties.")
        return None
    
    print(f"🔍 DIAGNOSING MATERIAL: {obj.Label} ({obj.Name})")
    print(f"{'='*70}")
    
    return obj

def analyze_material_properties(obj):
    """Analyze all properties of a material object."""
    print(f"\n📊 PROPERTY ANALYSIS:")
    print(f"{'Property':<20} {'Current Value':<25} {'Type':<15} {'Status'}")
    print(f"{'-'*75}")
    
    properties = {}
    
    # Core material properties
    core_props = ['Density', 'ModulusElasticity', 'PoissonRatio', 'YieldStrength', 'UltimateStrength']
    
    for prop_name in core_props:
        if hasattr(obj, prop_name):
            try:
                value = getattr(obj, prop_name)
                value_str = str(value)
                value_type = type(value).__name__
                
                # Check for problematic values
                status = "✅ OK"
                if prop_name == 'Density' and '7850' in value_str and 'concrete' in obj.Label.lower():
                    status = "❌ CONCRETE HAS STEEL DENSITY"
                elif prop_name == 'Density' and '2400' in value_str and 'steel' in obj.Label.lower():
                    status = "❌ STEEL HAS CONCRETE DENSITY"
                elif prop_name == 'ModulusElasticity' and '200000' in value_str and 'concrete' in obj.Label.lower():
                    status = "❌ CONCRETE HAS STEEL MODULUS"
                elif prop_name == 'ModulusElasticity' and ('25000' in value_str or '27000' in value_str) and 'steel' in obj.Label.lower():
                    status = "❌ STEEL HAS CONCRETE MODULUS"
                elif prop_name == 'PoissonRatio' and abs(float(value) - 0.30) < 0.01 and 'concrete' in obj.Label.lower():
                    status = "❌ CONCRETE HAS STEEL POISSON"
                elif prop_name == 'PoissonRatio' and abs(float(value) - 0.20) < 0.01 and 'steel' in obj.Label.lower():
                    status = "❌ STEEL HAS CONCRETE POISSON"
                
                properties[prop_name] = {
                    'value': value,
                    'value_str': value_str,
                    'type': value_type,
                    'status': status
                }
                
                print(f"{prop_name:<20} {value_str:<25} {value_type:<15} {status}")
                
            except Exception as e:
                print(f"{prop_name:<20} {'ERROR: ' + str(e):<25} {'Error':<15} {'❌ ERROR'}")
                properties[prop_name] = {'error': str(e)}
    
    return properties

def check_material_standard_integration(obj):
    """Check MaterialStandard property and integration."""
    print(f"\n🏛️ MATERIAL STANDARD ANALYSIS:")
    
    if not hasattr(obj, 'MaterialStandard'):
        print("❌ Object does not have MaterialStandard property")
        print("   This means it's using the old Material system, not StructuralMaterial")
        return False
    
    current_standard = obj.MaterialStandard
    print(f"Current MaterialStandard: '{current_standard}'")
    
    # Check if standard exists in database
    try:
        from freecad.StructureTools.data.MaterialStandards import MATERIAL_STANDARDS
        
        if current_standard in MATERIAL_STANDARDS:
            print(f"✅ Standard '{current_standard}' found in database")
            
            # Compare current properties with database
            db_props = MATERIAL_STANDARDS[current_standard]
            print(f"\nDatabase properties for '{current_standard}':")
            for prop_name, db_value in db_props.items():
                print(f"   {prop_name}: {db_value}")
            
            # Check if current object properties match database
            print(f"\nProperty Comparison:")
            matches = True
            
            for prop_name in ['Density', 'ModulusElasticity', 'PoissonRatio']:
                if prop_name in db_props and hasattr(obj, prop_name):
                    current_value_str = str(getattr(obj, prop_name))
                    db_value_str = str(db_props[prop_name])
                    
                    if current_value_str == db_value_str:
                        print(f"   ✅ {prop_name}: {current_value_str} (matches)")
                    else:
                        print(f"   ❌ {prop_name}: {current_value_str} != {db_value_str}")
                        matches = False
            
            return matches
        
        else:
            print(f"❌ Standard '{current_standard}' NOT found in database")
            print(f"Available standards: {list(MATERIAL_STANDARDS.keys())}")
            return False
            
    except ImportError:
        print("❌ Cannot import MaterialStandards database")
        return False

def check_object_proxy_type(obj):
    """Check what type of object this is."""
    print(f"\n🏗️ OBJECT TYPE ANALYSIS:")
    
    print(f"Object TypeId: {obj.TypeId}")
    
    if hasattr(obj, 'Proxy') and obj.Proxy:
        proxy_class = obj.Proxy.__class__.__name__
        print(f"Proxy Class: {proxy_class}")
        
        if proxy_class == "StructuralMaterial":
            print("✅ This is a StructuralMaterial object (Enhanced Material)")
            return "StructuralMaterial"
        elif "Material" in proxy_class:
            print("⚠️  This is a basic Material object (Legacy)")
            return "BasicMaterial"
        else:
            print(f"⚠️  Unknown proxy type: {proxy_class}")
            return "Unknown"
    else:
        print("❌ Object has no proxy - may be corrupted or very old")
        return "NoProxy"

def force_property_update(obj):
    """Force update of material properties."""
    print(f"\n🔄 FORCING PROPERTY UPDATE:")
    
    object_type = check_object_proxy_type(obj)
    
    if object_type == "StructuralMaterial":
        # Try to trigger property update
        if hasattr(obj, 'MaterialStandard'):
            current_standard = obj.MaterialStandard
            print(f"Attempting to refresh MaterialStandard: {current_standard}")
            
            try:
                # Force trigger onChanged event
                obj.MaterialStandard = current_standard
                print("✅ Triggered MaterialStandard refresh")
                
                # Force recompute
                obj.recompute()
                App.ActiveDocument.recompute()
                print("✅ Forced document recompute")
                
                return True
                
            except Exception as e:
                print(f"❌ Error forcing update: {e}")
                return False
    
    elif object_type == "BasicMaterial":
        print("⚠️  This is a basic Material object - cannot auto-update from MaterialStandard")
        print("   Consider recreating this material using the Enhanced Material dialog")
        return False
    
    return False

def suggest_fix_actions(obj, properties_analysis, standard_matches):
    """Suggest specific actions to fix the material."""
    print(f"\n💡 SUGGESTED FIX ACTIONS:")
    
    # Check if properties are wrong
    has_property_issues = False
    for prop_name, prop_data in properties_analysis.items():
        if isinstance(prop_data, dict) and '❌' in prop_data.get('status', ''):
            has_property_issues = True
            break
    
    if has_property_issues:
        print("1. 🔧 PROPERTY CORRECTION NEEDED:")
        print("   - Material properties do not match the material type")
        print("   - Run the fix script to correct property values")
        print("   - Command: exec(open(r'..\\fix_existing_material_objects.py').read())")
    
    if not standard_matches and hasattr(obj, 'MaterialStandard'):
        print("2. 🏛️ MATERIAL STANDARD MISMATCH:")
        print("   - Object properties don't match the MaterialStandard database")
        print("   - Try refreshing the MaterialStandard property")
        print("   - Or update to a correct MaterialStandard value")
    
    if not hasattr(obj, 'MaterialStandard'):
        print("3. 🆙 UPGRADE TO STRUCTURAL MATERIAL:")
        print("   - This object uses the old Material system")
        print("   - Consider recreating with Enhanced Material dialog")
        print("   - This will provide MaterialStandard integration")
    
    print("4. 🔄 IMMEDIATE ACTIONS TO TRY:")
    print("   - Select the object and press Ctrl+Shift+R to force recompute")
    print("   - Or run: obj.recompute(); App.ActiveDocument.recompute()")
    if hasattr(obj, 'MaterialStandard'):
        print(f"   - Or run: obj.MaterialStandard = '{obj.MaterialStandard}'; obj.recompute()")

def run_diagnosis():
    """Run complete diagnosis of selected material."""
    print("PROPERTY PANEL MATERIAL ISSUE DIAGNOSIS")
    print("=" * 80)
    
    # Get selected object
    obj = diagnose_selected_material()
    if not obj:
        return
    
    # Analyze properties
    properties_analysis = analyze_material_properties(obj)
    
    # Check MaterialStandard integration
    standard_matches = check_material_standard_integration(obj)
    
    # Check object type
    object_type = check_object_proxy_type(obj)
    
    # Suggest fixes
    suggest_fix_actions(obj, properties_analysis, standard_matches)
    
    # Offer to attempt automatic fix
    print(f"\n{'='*80}")
    print("AUTOMATIC FIX ATTEMPT")
    print(f"{'='*80}")
    
    response = input("🤔 Attempt automatic property refresh? (y/N): ").lower().strip()
    
    if response in ['y', 'yes']:
        success = force_property_update(obj)
        if success:
            print("✅ Property refresh completed - check the Property Panel now!")
            
            # Re-analyze to see if it worked
            print("\n📊 POST-FIX ANALYSIS:")
            analyze_material_properties(obj)
        else:
            print("❌ Automatic fix failed - manual intervention required")
    
    print(f"\n{'='*80}")
    print("DIAGNOSIS COMPLETE")
    print(f"{'='*80}")
    print("ℹ️  Check the FreeCAD Property Panel (Model Data tab) for the selected material")
    print("ℹ️  If values are still incorrect, run the fix_existing_material_objects.py script")

if __name__ == "__main__":
    run_diagnosis()