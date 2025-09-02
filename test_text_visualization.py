#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test script for text-based reaction visualization feature
"""

import FreeCAD
import FreeCADGui

def test_text_visualization():
    """Test the text-based reaction visualization feature."""
    
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
            print("💡 Tip: Create a reaction results object first using the 'Reaction Results' command")
            return False
        
        print(f"✅ Found {len(reaction_objects)} reaction results objects")
        
        # Test text visualization for each reaction object
        for i, reaction_obj in enumerate(reaction_objects):
            print(f"\n--- Testing Text Visualization for Reaction Object {i+1} ---")
            
            # Check if the method exists
            if hasattr(reaction_obj.Proxy, 'create_text_based_visualization'):
                print("✅ Text visualization method found")
                
                # Try to generate text visualization
                try:
                    reaction_obj.Proxy.create_text_based_visualization(reaction_obj)
                    print("✅ Text visualization generated successfully")
                    print("💡 Check the FreeCAD console for the visualization output")
                except Exception as e:
                    print(f"❌ Error generating text visualization: {e}")
                    return False
            else:
                print("❌ Text visualization method not found in ReactionResults proxy")
                return False
            
            # Also test the public method
            if hasattr(reaction_obj.Proxy, 'showTextVisualization'):
                print("✅ Public showTextVisualization method found")
            else:
                print("❌ Public showTextVisualization method not found")
        
        print("\n🎉 Text visualization feature test completed!")
        print("📝 The visualization output should be visible in the FreeCAD console")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_text_visualization()