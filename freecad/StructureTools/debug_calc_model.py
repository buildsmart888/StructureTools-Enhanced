"""
Debug script to check calc objects and FE models
Run this after running calc command to see what's stored
"""

def debug_calc_objects():
    """Debug all calc objects in the current document"""
    import FreeCAD
    
    print("=== DEBUGGING CALC OBJECTS ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document")
        return False
    
    doc = FreeCAD.ActiveDocument
    calc_objects = []
    
    # Find all calc objects
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
            if 'Calc' in obj.Proxy.__class__.__name__:
                calc_objects.append(obj)
    
    if not calc_objects:
        print("❌ No calc objects found")
        return False
    
    print(f"Found {len(calc_objects)} calc object(s):")
    
    for i, calc_obj in enumerate(calc_objects):
        print(f"\n--- Calc Object {i+1}: {calc_obj.Name} ---")
        
        # Check basic properties
        print("Basic Properties:")
        basic_props = ['LengthUnit', 'ForceUnit', 'selfWeight', 'LoadCombination']
        for prop in basic_props:
            if hasattr(calc_obj, prop):
                value = getattr(calc_obj, prop)
                print(f"  ✅ {prop}: {value}")
            else:
                print(f"  ❌ {prop}: Missing")
        
        # Check diagram properties
        print("Diagram Properties:")
        diagram_props = ['NumPointsMoment', 'NumPointsAxial', 'NumPointsShear']
        for prop in diagram_props:
            if hasattr(calc_obj, prop):
                value = getattr(calc_obj, prop)
                print(f"  ✅ {prop}: {value}")
            else:
                print(f"  ❌ {prop}: Missing")
        
        # Check FE Model
        print("FE Model:")
        if hasattr(calc_obj, 'FEModel'):
            if calc_obj.FEModel:
                model = calc_obj.FEModel
                print(f"  ✅ FEModel exists with:")
                print(f"     - Nodes: {len(model.nodes)}")
                print(f"     - Members: {len(model.members)}")
                
                # Check for supports and reactions
                supported_nodes = 0
                nodes_with_reactions = 0
                
                for node_name, node in model.nodes.items():
                    if (node.support_DX or node.support_DY or node.support_DZ or 
                        node.support_RX or node.support_RY or node.support_RZ):
                        supported_nodes += 1
                        
                        # Check for reactions in current load combination
                        combo = calc_obj.LoadCombination if hasattr(calc_obj, 'LoadCombination') else '100_DL'
                        if (combo in node.RxnFX or combo in node.RxnFY or combo in node.RxnFZ or
                            combo in node.RxnMX or combo in node.RxnMY or combo in node.RxnMZ):
                            nodes_with_reactions += 1
                
                print(f"     - Supported nodes: {supported_nodes}")
                print(f"     - Nodes with reactions: {nodes_with_reactions}")
                
                if nodes_with_reactions > 0:
                    print("  ✅ READY FOR REACTION RESULTS")
                else:
                    print("  ⚠️  No reaction data found - analysis may have failed")
                    
            else:
                print("  ❌ FEModel property exists but is None/empty")
        else:
            print("  ❌ No FEModel property")
        
        # Check old-style model
        if hasattr(calc_obj, 'model'):
            if calc_obj.model:
                print("  ✅ Also has old-style 'model' property")
            else:
                print("  ⚠️  Has 'model' property but it's None")
    
    # Summary and recommendations
    print("\n=== SUMMARY ===")
    
    working_calcs = []
    for calc_obj in calc_objects:
        if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            working_calcs.append(calc_obj)
    
    if working_calcs:
        print(f"✅ {len(working_calcs)} calc object(s) ready for Reaction Results:")
        for calc_obj in working_calcs:
            print(f"   - {calc_obj.Name}")
        print("\nYou can now use the Reaction Results button!")
    else:
        print("❌ No calc objects with FE models found")
        print("\nTroubleshooting:")
        print("1. Make sure your model has:")
        print("   - Beam/member geometry")
        print("   - Materials and sections assigned")
        print("   - Support conditions")
        print("   - Loads applied")
        print("2. Run the calc command")
        print("3. Check for any error messages")
        print("4. Run this debug script again")
    
    return len(working_calcs) > 0

def quick_fix_calc():
    """Quick fix for calc objects missing properties"""
    import FreeCAD
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document")
        return
    
    doc = FreeCAD.ActiveDocument
    fixed_count = 0
    
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
            if 'Calc' in obj.Proxy.__class__.__name__:
                print(f"Fixing {obj.Name}...")
                
                try:
                    # Run ensure_required_properties if available
                    if hasattr(obj.Proxy, 'ensure_required_properties'):
                        obj.Proxy.ensure_required_properties(obj)
                        print(f"  ✅ Properties fixed")
                        
                        # Try to run execute to generate FE model
                        obj.Proxy.execute(obj)
                        print(f"  ✅ Analysis executed")
                        fixed_count += 1
                        
                except Exception as e:
                    print(f"  ❌ Error fixing {obj.Name}: {e}")
    
    if fixed_count > 0:
        doc.recompute()
        print(f"\n✅ Fixed {fixed_count} calc objects")
        print("Now try the Reaction Results button again!")
    else:
        print("❌ No calc objects could be fixed")

if __name__ == "__main__":
    debug_calc_objects()