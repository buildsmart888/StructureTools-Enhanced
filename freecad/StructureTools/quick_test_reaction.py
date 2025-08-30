"""
Quick test script for Reaction Results - Run in FreeCAD Python Console
"""

def quick_test():
    import FreeCAD, FreeCADGui
    print("=== Quick Reaction Results Test ===")
    
    # Test 1: Check if calc command works
    print("1. Testing calc command...")
    try:
        from freecad.StructureTools.calc import CommandCalc
        cmd = CommandCalc()
        print("   ✅ Calc command imported successfully")
    except Exception as e:
        print(f"   ❌ Calc command failed: {e}")
        return False
    
    # Test 2: Check reaction results import  
    print("2. Testing reaction results import...")
    try:
        from freecad.StructureTools import reaction_results
        print("   ✅ Reaction results imported successfully")
    except Exception as e:
        print(f"   ❌ Reaction results import failed: {e}")
        return False
    
    # Test 3: Check if reaction command exists
    print("3. Testing reaction command...")
    try:
        from freecad.StructureTools.reaction_results import CommandReactionResults
        cmd = CommandReactionResults()
        if hasattr(cmd, 'GetResources'):
            resources = cmd.GetResources()
            print(f"   ✅ Command resources: {resources['MenuText']}")
        else:
            print("   ❌ No GetResources method")
    except Exception as e:
        print(f"   ❌ Command test failed: {e}")
        
    # Test 4: Check if we have any calc objects in document
    print("4. Checking for existing calc objects...")
    if FreeCAD.ActiveDocument:
        calc_objects = []
        for obj in FreeCAD.ActiveDocument.Objects:
            if hasattr(obj, 'Proxy') and obj.Proxy and 'Calc' in str(type(obj.Proxy)):
                calc_objects.append(obj)
        
        if calc_objects:
            print(f"   ✅ Found {len(calc_objects)} calc objects")
            
            # Check if any has FE model
            for calc_obj in calc_objects:
                if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                    print(f"   ✅ {calc_obj.Name} has FE model with {len(calc_obj.FEModel.nodes)} nodes")
                    
                    # Test creating reaction results
                    try:
                        reaction_obj = FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroupPython", "TestReactionResults")
                        reaction_results.ReactionResults(reaction_obj, calc_obj)
                        reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
                        FreeCAD.ActiveDocument.recompute()
                        print("   ✅ Reaction results object created successfully")
                        return True
                    except Exception as e:
                        print(f"   ❌ Failed to create reaction results: {e}")
                        
                else:
                    print(f"   ⚠️ {calc_obj.Name} has no FE model - run analysis first")
        else:
            print("   ⚠️ No calc objects found - create and run analysis first")
    else:
        print("   ⚠️ No active document")
    
    print("\n=== Test Instructions ===")
    print("To test Reaction Results:")
    print("1. Create a simple beam structure")
    print("2. Add supports and loads")
    print("3. Run calc command (analysis)")  
    print("4. Click 'Reaction Results' button in StructureResults toolbar")
    print("5. Or run: exec(open(r'{}').read())".format(__file__.replace('\\', '/')))
    
    return True

if __name__ == "__main__":
    quick_test()