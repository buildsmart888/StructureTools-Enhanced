#!/usr/bin/env python3
"""
Test script to verify ReactionResults command registration
"""

import sys
import os

# Add the StructureTools path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'freecad', 'StructureTools'))

def test_reaction_command():
    """Test if ReactionResults command is properly registered"""
    print("Testing ReactionResults command registration...")
    
    try:
        # Try to import the reaction_results module
        import reaction_results
        print("✓ Successfully imported reaction_results module")
        
        # Check if CommandReactionResults class exists
        if hasattr(reaction_results, 'CommandReactionResults'):
            print("✓ CommandReactionResults class found")
            
            # Check if it has the required methods
            cmd_class = reaction_results.CommandReactionResults
            if hasattr(cmd_class, 'GetResources') and hasattr(cmd_class, 'Activated'):
                print("✓ CommandReactionResults has required methods")
                
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
                print("✗ CommandReactionResults missing required methods")
                return False
        else:
            print("✗ CommandReactionResults class not found")
            return False
            
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

if __name__ == "__main__":
    print("StructureTools ReactionResults Command Test")
    print("=" * 50)
    
    success = test_reaction_command()
    
    print("\n" + "=" * 50)
    if success:
        print("✓ ReactionResults command test passed!")
    else:
        print("✗ ReactionResults command test failed!")
        sys.exit(1)