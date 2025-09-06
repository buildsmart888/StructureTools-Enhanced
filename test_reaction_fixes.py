#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test script to verify reaction visualization fixes
"""

import FreeCAD
import FreeCADGui

def test_reaction_visualization_fixes():
    """Test that our reaction visualization fixes work correctly."""
    
    try:
        # Get the active document
        doc = FreeCAD.ActiveDocument
        if not doc:
            print("❌ No active document found")
            return False
        
        # Find reaction results objects
        reaction_objects = []
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                if 'ReactionResults' in obj.Proxy.__class__.__name__:
                    reaction_objects.append(obj)
        
        if not reaction_objects:
            print("❌ No reaction results objects found in document")
            return False
        
        print(f"✅ Found {len(reaction_objects)} reaction results objects")
        
        # Test each reaction object
        for i, reaction_obj in enumerate(reaction_objects):
            print(f"\n--- Testing Reaction Object {i+1} ---")
            
            # Check scale factors
            if hasattr(reaction_obj, 'ScaleReactionForces'):
                print(f"✅ Force scale factor: {reaction_obj.ScaleReactionForces}")
            else:
                print("❌ ScaleReactionForces property not found")
                
            if hasattr(reaction_obj, 'ScaleReactionMoments'):
                print(f"✅ Moment scale factor: {reaction_obj.ScaleReactionMoments}")
            else:
                print("❌ ScaleReactionMoments property not found")
            
            # Check if multiple load combinations are available
            if hasattr(reaction_obj, 'ObjectBaseCalc') and reaction_obj.ObjectBaseCalc:
                calc_obj = reaction_obj.ObjectBaseCalc
                
                # Try to get load combinations
                load_combos = []
                if hasattr(calc_obj, 'LoadCombination'):
                    load_combos = calc_obj.LoadCombination
                    if isinstance(load_combos, str):
                        load_combos = [load_combos]
                    print(f"✅ Available load combinations: {load_combos}")
                else:
                    print("ℹ️ No LoadCombination property found")
            
            # Recompute the reaction object to test visualization
            try:
                reaction_obj.Proxy.execute(reaction_obj)
                print("✅ Reaction visualization updated successfully")
            except Exception as e:
                print(f"❌ Error updating reaction visualization: {e}")
        
        print("\n🎉 All tests completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False

if __name__ == "__main__":
    test_reaction_visualization_fixes()