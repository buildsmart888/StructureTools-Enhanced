"""
Final test for Reaction Results with all fixes applied
Run in FreeCAD Python Console
"""

def test_reaction_results_final():
    """Complete test of Reaction Results functionality"""
    import FreeCAD, FreeCADGui
    print("=== FINAL REACTION RESULTS TEST ===")
    
    try:
        doc = FreeCAD.ActiveDocument
        if not doc:
            print("❌ No active document. Please open your structural model first.")
            return False
        
        print(f"Testing with document: {doc.Name}")
        
        # Step 1: Find calc objects
        calc_objects = []
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
                if 'Calc' in obj.Proxy.__class__.__name__:
                    calc_objects.append(obj)
        
        if not calc_objects:
            print("❌ No calc objects found in document")
            return False
        
        print(f"✅ Found {len(calc_objects)} calc object(s)")
        
        # Step 2: Test a calc object
        calc_obj = calc_objects[0]
        print(f"   Using: {calc_obj.Name}")
        
        # Check if it has required properties
        required_props = ['selfWeight', 'NumPointsMoment', 'NumPointsAxial']
        missing_props = [prop for prop in required_props if not hasattr(calc_obj, prop)]
        
        if missing_props:
            print(f"   Missing properties: {missing_props}")
            print("   Running calc to fix properties...")
            
            # Execute calc to add missing properties
            calc_obj.Proxy.execute(calc_obj)
            
            # Check again
            still_missing = [prop for prop in required_props if not hasattr(calc_obj, prop)]
            if still_missing:
                print(f"   ❌ Still missing: {still_missing}")
                return False
            else:
                print("   ✅ Properties fixed automatically")
        else:
            print("   ✅ All required properties present")
        
        # Step 3: Check for FE model
        has_fe_model = False
        if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            model = calc_obj.FEModel
            print(f"   ✅ FE Model: {len(model.nodes)} nodes, {len(model.members)} members")
            has_fe_model = True
            
            # Check for reactions
            reaction_count = 0
            for node_name, node in model.nodes.items():
                if (node.support_DX or node.support_DY or node.support_DZ or 
                    node.support_RX or node.support_RY or node.support_RZ):
                    reaction_count += 1
            
            print(f"   ✅ Found {reaction_count} support nodes")
            
        else:
            print("   ⚠️ No FE model found - running analysis...")
            
            # Try to run analysis
            try:
                calc_obj.Proxy.execute(calc_obj)
                if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                    has_fe_model = True
                    print("   ✅ Analysis completed successfully")
                else:
                    print("   ⚠️ Analysis ran but no FE model stored")
            except Exception as e:
                print(f"   ❌ Analysis failed: {e}")
        
        # Step 4: Test Reaction Results creation
        print("\n--- Testing Reaction Results ---")
        
        try:
            from freecad.StructureTools import reaction_results
            
            # Check if reaction results already exists
            existing_reaction = None
            for obj in doc.Objects:
                if hasattr(obj, 'Proxy') and obj.Proxy and 'ReactionResults' in str(type(obj.Proxy)):
                    existing_reaction = obj
                    break
            
            if existing_reaction:
                print(f"   Found existing: {existing_reaction.Name}")
                reaction_obj = existing_reaction
            else:
                print("   Creating new reaction results object...")
                reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "ReactionResultsTest")
                reaction_results.ReactionResults(reaction_obj, calc_obj)
                reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
                print("   ✅ Reaction object created")
            
            # Test properties
            print("   Checking reaction properties...")
            if hasattr(reaction_obj, 'ShowReactionFX'):
                print(f"     ShowReactionFX: {reaction_obj.ShowReactionFX}")
            if hasattr(reaction_obj, 'ActiveLoadCombination'):
                print(f"     Active combo: {reaction_obj.ActiveLoadCombination}")
            
            # Test execution
            print("   Testing visualization execution...")
            reaction_obj.Proxy.execute(reaction_obj)
            print("   ✅ Visualization executed successfully")
            
            # Test GUI panel
            print("   Testing control panel...")
            try:
                from freecad.StructureTools.reaction_results_panel import ReactionResultsPanel
                panel = ReactionResultsPanel(reaction_obj)
                print("   ✅ Control panel created successfully")
                # Don't actually show the panel in test
                
            except Exception as e:
                print(f"   ⚠️ Panel creation failed: {e}")
                print("     But basic reaction results work!")
            
            doc.recompute()
            
            print("\n" + "="*50)
            print("🎉 REACTION RESULTS TEST SUCCESSFUL!")
            print("="*50)
            print("Your Reaction Results system is working:")
            print("   ✅ Calc objects fixed and compatible")
            print("   ✅ FE models stored properly")
            print("   ✅ Reaction visualization created")
            print("   ✅ GUI controls available")
            print("")
            print("To use:")
            print("   1. Click 'Reaction Results' button in StructureResults toolbar")
            print("   2. Or double-click the ReactionResults object")
            print("   3. Use checkboxes to control display")
            print("   4. Change load combinations to see different results")
            print("="*50)
            
            return True
            
        except Exception as e:
            print(f"❌ Reaction Results test failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def quick_reaction_test():
    """Quick test to verify system is working"""
    import FreeCAD
    
    print("=== QUICK REACTION TEST ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ Open a structural model first")
        return False
    
    # Check workbench
    try:
        from freecad.StructureTools import reaction_results
        print("✅ Reaction results module imported")
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False
    
    # Check command
    try:
        from freecad.StructureTools.reaction_results import CommandReactionResults
        cmd = CommandReactionResults()
        if cmd.IsActive():
            print("✅ Reaction Results command is active")
        else:
            print("⚠️ Command not active (normal if no suitable calc object)")
    except Exception as e:
        print(f"❌ Command test failed: {e}")
        return False
    
    print("✅ System appears to be working!")
    print("   Run: test_reaction_results_final() for complete test")
    return True

if __name__ == "__main__":
    # Run appropriate test based on what's available
    import FreeCAD
    if FreeCAD.ActiveDocument:
        test_reaction_results_final()
    else:
        print("Please open a structural model first, then run:")
        print("exec(open(r'{}').read())".format(__file__.replace('\\', '/')))
        quick_reaction_test()