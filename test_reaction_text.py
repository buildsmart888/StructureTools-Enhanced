#!/usr/bin/env python3
"""
Test script to demonstrate ShowReactionText functionality
Run this in FreeCAD Python Console after running a structural analysis
"""

import FreeCAD as App

def test_show_reaction_text():
    """Test the ShowReactionText functionality"""
    print("Testing ShowReactionText functionality...")
    
    # Get active document
    doc = App.ActiveDocument
    if not doc:
        print("ERROR: No active document found. Please open a FreeCAD document.")
        return False
    
    # Find Calc object
    calc_obj = None
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
            if getattr(obj.Proxy, 'Type', None) == 'Calc':
                calc_obj = obj
                break
    
    if not calc_obj:
        print("ERROR: No Calc object found. Please create a Calc object first.")
        return False
    
    print(f"Found Calc object: {calc_obj.Label}")
    
    # Check if analysis has been run
    if not hasattr(calc_obj, 'model') or calc_obj.model is None:
        print("ERROR: No analysis model found. Please run structural analysis first.")
        return False
    
    print(f"Analysis model found with {len(calc_obj.model.Nodes)} nodes")
    
    # Check for support nodes
    support_nodes = []
    for node_name, node in calc_obj.model.Nodes.items():
        has_support = any([
            node.support_DX, node.support_DY, node.support_DZ,
            node.support_RX, node.support_RY, node.support_RZ
        ])
        if has_support:
            support_nodes.append(node_name)
    
    if not support_nodes:
        print("WARNING: No support nodes found in the model.")
        return False
    
    print(f"Found {len(support_nodes)} support nodes: {support_nodes}")
    
    # Test ShowReactionText properties
    print(f"ShowReactionText: {getattr(calc_obj, 'ShowReactionText', 'Not set')}")
    print(f"ReactionPrecision: {getattr(calc_obj, 'ReactionPrecision', 'Not set')}")
    print(f"ReactionTextOffset: {getattr(calc_obj, 'ReactionTextOffset', 'Not set')}")
    print(f"ReactionFontSize: {getattr(calc_obj, 'ReactionFontSize', 'Not set')}")
    print(f"LoadCombination: {getattr(calc_obj, 'LoadCombination', 'Not set')}")
    
    # Enable ShowReactionText
    print("\n--- Enabling ShowReactionText ---")
    calc_obj.ShowReactionText = True
    
    # Trigger manual update if ViewProvider doesn't auto-update
    if hasattr(calc_obj.ViewObject, 'Proxy'):
        vp = calc_obj.ViewObject.Proxy
        if hasattr(vp, 'updateReactionTextDisplay'):
            print("Manually triggering reaction text display...")
            vp.updateReactionTextDisplay()
    
    # Check if text objects were created
    text_objects = []
    for obj in doc.Objects:
        if obj.Label.startswith("Reactions_"):
            text_objects.append(obj.Label)
    
    if text_objects:
        print(f"SUCCESS: Created {len(text_objects)} reaction text objects:")
        for text_obj in text_objects:
            print(f"  - {text_obj}")
    else:
        print("WARNING: No reaction text objects created. Check the implementation.")
    
    # Test different load combinations
    print("\n--- Testing Load Combination Changes ---")
    available_combinations = getattr(calc_obj, 'load_combinations_list', ['100_DL'])
    if len(available_combinations) > 1:
        original_combo = calc_obj.LoadCombination
        test_combo = available_combinations[1] if available_combinations[1] != original_combo else available_combinations[0]
        
        print(f"Changing from {original_combo} to {test_combo}")
        calc_obj.LoadCombination = test_combo
        
        print("Reaction text should update automatically...")
        
        # Change back
        calc_obj.LoadCombination = original_combo
        print(f"Changed back to {original_combo}")
    else:
        print(f"Only one load combination available: {available_combinations}")
    
    print("\n--- Test Complete ---")
    print("To disable reaction text: calc_obj.ShowReactionText = False")
    
    return True

def show_reaction_values():
    """Display actual reaction values for debugging"""
    doc = App.ActiveDocument
    if not doc:
        return
    
    calc_obj = None
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
            if getattr(obj.Proxy, 'Type', None) == 'Calc':
                calc_obj = obj
                break
    
    if not calc_obj or not hasattr(calc_obj, 'model'):
        print("No calc object or analysis model found")
        return
    
    combo = getattr(calc_obj, 'LoadCombination', '100_DL')
    print(f"\nReaction values for combination '{combo}':")
    print("-" * 50)
    
    for node_name, node in calc_obj.model.Nodes.items():
        has_support = any([
            node.support_DX, node.support_DY, node.support_DZ,
            node.support_RX, node.support_RY, node.support_RZ
        ])
        
        if has_support:
            print(f"\nNode {node_name}:")
            print(f"  Position: ({node.X:.1f}, {node.Y:.1f}, {node.Z:.1f})")
            print(f"  Supports: DX={node.support_DX}, DY={node.support_DY}, DZ={node.support_DZ}")
            print(f"           RX={node.support_RX}, RY={node.support_RY}, RZ={node.support_RZ}")
            
            # Check reaction values
            reactions = {}
            for attr, component in [('RxnFX', 'FX'), ('RxnFY', 'FY'), ('RxnFZ', 'FZ'),
                                   ('RxnMX', 'MX'), ('RxnMY', 'MY'), ('RxnMZ', 'MZ')]:
                if hasattr(node, attr) and combo in getattr(node, attr):
                    value = getattr(node, attr)[combo]
                    if abs(value) > 1e-6:
                        reactions[component] = value
            
            if reactions:
                print("  Reactions:")
                for comp, val in reactions.items():
                    unit = "kN·m" if comp.startswith('M') else "kN"
                    print(f"    {comp}: {val:.2f} {unit}")
            else:
                print("  Reactions: None or negligible")

if __name__ == "__main__":
    print("ShowReactionText Test Script")
    print("Run in FreeCAD Python Console:")
    print("exec(open(r'C:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools\\test_reaction_text.py').read())")
    print("test_show_reaction_text()")
    print("show_reaction_values()")