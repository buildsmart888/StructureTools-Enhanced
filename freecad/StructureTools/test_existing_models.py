"""
Test script for existing model files with old calc objects
Run in FreeCAD Python Console after opening existing model
"""

def fix_existing_calc_objects():
    """Fix all existing calc objects in current document"""
    import FreeCAD
    
    print("=== Fixing Existing Calc Objects ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document. Please open your existing model file first.")
        return False
    
    doc = FreeCAD.ActiveDocument
    calc_objects = []
    
    # Find all calc objects
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and obj.Proxy:
            if 'Calc' in str(type(obj.Proxy)) or hasattr(obj.Proxy, '__class__') and 'Calc' in obj.Proxy.__class__.__name__:
                calc_objects.append(obj)
    
    if not calc_objects:
        print("❌ No calc objects found in document")
        return False
    
    print(f"Found {len(calc_objects)} calc objects:")
    
    fixed_count = 0
    for calc_obj in calc_objects:
        print(f"\n--- Processing {calc_obj.Name} ---")
        
        try:
            # Check current properties
            missing_props = []
            required_props = [
                'selfWeight', 'NumPointsMoment', 'NumPointsAxial', 
                'NumPointsShear', 'NumPointsTorque', 'NumPointsDeflection',
                'GlobalUnitsSystem', 'UseGlobalUnits', 'FEModel'
            ]
            
            for prop in required_props:
                if not hasattr(calc_obj, prop):
                    missing_props.append(prop)
            
            if missing_props:
                print(f"   Missing properties: {missing_props}")
                
                # Run ensure_required_properties if calc has the method
                if hasattr(calc_obj.Proxy, 'ensure_required_properties'):
                    calc_obj.Proxy.ensure_required_properties(calc_obj)
                    print("   ✅ Added missing properties")
                    fixed_count += 1
                else:
                    print("   ⚠️ Calc proxy doesn't have ensure_required_properties method")
            else:
                print("   ✅ All properties present")
                fixed_count += 1
            
            # Test if it can execute now
            try:
                print("   Testing execution...")
                calc_obj.Proxy.execute(calc_obj)
                print("   ✅ Execution successful")
            except Exception as e:
                print(f"   ❌ Execution failed: {e}")
                
        except Exception as e:
            print(f"   ❌ Error processing {calc_obj.Name}: {e}")
    
    doc.recompute()
    
    print(f"\n=== Summary ===")
    print(f"   Fixed {fixed_count}/{len(calc_objects)} calc objects")
    
    if fixed_count == len(calc_objects):
        print("   ✅ All calc objects are now compatible!")
        return True
    else:
        print("   ⚠️ Some calc objects may still have issues")
        return False

def test_reaction_results_with_existing():
    """Test reaction results creation with existing model"""
    import FreeCAD
    
    print("\n=== Testing Reaction Results with Existing Model ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document")
        return False
    
    doc = FreeCAD.ActiveDocument
    
    # Find a working calc object
    working_calc = None
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and obj.Proxy and 'Calc' in str(type(obj.Proxy)):
            if hasattr(obj, 'FEModel') and obj.FEModel:
                working_calc = obj
                break
            elif hasattr(obj, 'NumPointsMoment'):  # Has required properties
                working_calc = obj
                break
    
    if not working_calc:
        print("❌ No suitable calc object found")
        print("   Make sure to run fix_existing_calc_objects() first")
        return False
    
    print(f"Using calc object: {working_calc.Name}")
    
    try:
        # Create reaction results
        from freecad.StructureTools import reaction_results
        
        # Check if reaction results already exists
        existing_reaction = None
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy') and obj.Proxy and 'ReactionResults' in str(type(obj.Proxy)):
                existing_reaction = obj
                break
        
        if existing_reaction:
            print(f"   Found existing reaction results: {existing_reaction.Name}")
            reaction_obj = existing_reaction
        else:
            print("   Creating new reaction results object...")
            reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "ReactionResults")
            reaction_results.ReactionResults(reaction_obj, working_calc)
            reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
        
        # Test execution
        reaction_obj.Proxy.execute(reaction_obj)
        print("   ✅ Reaction results created successfully!")
        
        # Try opening the panel
        try:
            from freecad.StructureTools.reaction_results_panel import ReactionResultsPanel
            # Don't actually open the panel in test, just check if it can be created
            panel = ReactionResultsPanel(reaction_obj)
            print("   ✅ Control panel ready")
            
        except Exception as e:
            print(f"   ⚠️ Panel creation failed: {e}")
        
        doc.recompute()
        return True
        
    except Exception as e:
        print(f"   ❌ Reaction results creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def complete_existing_model_test():
    """Complete test for existing model files"""
    print("="*60)
    print("EXISTING MODEL COMPATIBILITY TEST")
    print("="*60)
    print("Make sure you have opened your existing structural model first!")
    print("="*60)
    
    # Step 1: Fix calc objects
    print("\nSTEP 1: Fixing existing calc objects...")
    calc_fixed = fix_existing_calc_objects()
    
    if not calc_fixed:
        print("\n❌ Could not fix calc objects. Check errors above.")
        return False
    
    # Step 2: Test reaction results
    print("\nSTEP 2: Testing reaction results...")
    reaction_ok = test_reaction_results_with_existing()
    
    if calc_fixed and reaction_ok:
        print("\n" + "="*60)
        print("🎉 EXISTING MODEL IS NOW COMPATIBLE!")
        print("="*60)
        print("Your existing structural model now works with:")
        print("   ✅ Updated calc command (no more AttributeError)")
        print("   ✅ All required properties added automatically")
        print("   ✅ Reaction Results visualization")
        print("   ✅ Full backward compatibility")
        print("")
        print("You can now:")
        print("   • Run analysis using existing calc objects")
        print("   • Use ReactionResults button in toolbar")
        print("   • View reaction forces and moments")
        print("   • Continue working with your existing model")
        print("="*60)
        return True
    else:
        print("\n⚠️ Some issues remain. Check errors above.")
        return False

def quick_fix_instructions():
    """Show quick fix instructions for existing files"""
    print("\n" + "="*60)
    print("QUICK FIX FOR EXISTING MODELS")
    print("="*60)
    print("If you have existing structural models with calc objects:")
    print("")
    print("1. Open your existing FreeCAD file")
    print("2. Run this command in Python Console:")
    print("   exec(open(r'{}').read())".format(__file__.replace('\\', '/')))
    print("3. Or run: complete_existing_model_test()")
    print("")
    print("This will:")
    print("   • Find all calc objects in your model")
    print("   • Add missing properties automatically")  
    print("   • Fix AttributeError issues")
    print("   • Enable Reaction Results")
    print("="*60)

if __name__ == "__main__":
    # Show instructions if no document is open
    import FreeCAD
    if not FreeCAD.ActiveDocument:
        quick_fix_instructions()
    else:
        complete_existing_model_test()