"""
Test script for the new ViewReactionTable command and enhancements
"""

import FreeCAD, FreeCADGui
import os

def test_view_reaction_table_command():
    """Test if ViewReactionTable command is properly registered"""
    print("Testing ViewReactionTable command registration...")
    
    try:
        # Try to import the command module
        import freecad.StructureTools.command_reaction_table
        print("✓ Successfully imported command_reaction_table module")
        
        # Check if CommandViewReactionTable class exists
        if hasattr(freecad.StructureTools.command_reaction_table, 'CommandViewReactionTable'):
            print("✓ CommandViewReactionTable class found")
            
            # Check if it has the required methods
            cmd_class = freecad.StructureTools.command_reaction_table.CommandViewReactionTable
            if hasattr(cmd_class, 'GetResources') and hasattr(cmd_class, 'Activated'):
                print("✓ CommandViewReactionTable has required methods")
                
                # Try to instantiate the command
                try:
                    cmd = cmd_class()
                    resources = cmd.GetResources()
                    print(f"✓ Command resources: {resources}")
                    return True
                except Exception as e:
                    print(f"✗ Failed to instantiate command: {e}")
                    return False
            else:
                print("✗ CommandViewReactionTable missing required methods")
                return False
        else:
            print("✗ CommandViewReactionTable class not found")
            return False
            
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_reaction_object_creation():
    """Test creating reaction results from existing calc object"""
    print("Testing reaction results creation from existing calc...")
    
    try:
        # Check for calc object in active document
        if not FreeCAD.ActiveDocument:
            print("✗ No active document")
            return False
            
        calc_obj = None
        for obj in FreeCAD.ActiveDocument.Objects:
            if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                if 'Calc' in obj.Proxy.__class__.__name__:
                    calc_obj = obj
                    break
                    
        if not calc_obj:
            print("✗ No calc object found in document")
            return False
            
        print(f"✓ Found existing calc object: {calc_obj.Name}")
        
        # Create reaction results
        from freecad.StructureTools.reaction_results import ReactionResults, ViewProviderReactionResults
        
        reaction_obj = FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroupPython", "TestReactionResults")
        ReactionResults(reaction_obj, calc_obj)
        ViewProviderReactionResults(reaction_obj.ViewObject)
        
        print("✓ Successfully created reaction results object")
        
        # Test if model is accessible
        model = None
        if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            model = calc_obj.FEModel
            print("✓ Found model in FEModel attribute")
        elif hasattr(calc_obj, 'model') and calc_obj.model:
            model = calc_obj.model
            print("✓ Found model in model attribute")
        elif hasattr(calc_obj, 'Proxy') and hasattr(calc_obj.Proxy, 'model') and calc_obj.Proxy.model:
            model = calc_obj.Proxy.model
            print("✓ Found model in Proxy.model attribute")
        else:
            print("✗ No model found in calc object")
            return False
            
        if hasattr(model, 'nodes') and model.nodes:
            print(f"✓ Model has {len(model.nodes)} nodes")
        else:
            print("✗ No nodes found in model")
            return False
            
        # Get load combinations
        if hasattr(model, 'LoadCombos') and model.LoadCombos:
            print(f"✓ Found {len(model.LoadCombos)} load combinations")
            print(f"  Load combinations: {list(model.LoadCombos.keys())}")
        else:
            print("✗ No load combinations found")
            
        return True
        
    except Exception as e:
        print(f"✗ Error in test_reaction_object_creation: {e}")
        return False

def run_tests():
    print("=" * 50)
    print("TESTING REACTION TABLE ENHANCEMENTS")
    print("=" * 50)
    
    test_results = []
    
    # Test 1: Command registration
    print("Test 1: Command registration")
    test_results.append(("Command registration", test_view_reaction_table_command()))
    
    # Test 2: Reaction object creation
    print("\nTest 2: Reaction object creation")
    test_results.append(("Reaction object creation", test_reaction_object_creation()))
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST RESULTS:")
    all_passed = True
    for name, result in test_results:
        status = "✓ PASSED" if result else "✗ FAILED"
        if not result:
            all_passed = False
        print(f"{name}: {status}")
    
    if all_passed:
        print("\nAll tests PASSED! The reaction table enhancements are working properly.")
    else:
        print("\nSome tests FAILED. Please review the output above.")
    
    print("=" * 50)
    
    return all_passed

if __name__ == "__main__":
    run_tests()