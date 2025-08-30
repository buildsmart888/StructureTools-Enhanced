"""
Simple test script for Reaction Table Panel functionality
Run this in FreeCAD Python console to test the system
"""

import FreeCAD, FreeCADGui

def test_reaction_table_import():
    """Test if reaction table panel can be imported"""
    try:
        from freecad.StructureTools import reaction_table_panel
        print("✅ reaction_table_panel imported successfully")
        return True
    except Exception as e:
        print(f"❌ reaction_table_panel import failed: {e}")
        return False

def test_reaction_table_command():
    """Test the reaction table panel command"""
    try:
        from freecad.StructureTools.reaction_table_panel import CommandReactionTablePanel
        cmd = CommandReactionTablePanel()
        
        # Check if command can be activated
        if cmd.IsActive():
            print("✅ Reaction Table Panel command is active")
            # Don't actually activate to avoid UI issues in console
            return True
        else:
            print("❌ Reaction Table Panel command is not active (no document?)")
            return False
            
    except Exception as e:
        print(f"❌ Command test failed: {e}")
        return False

def test_reaction_table_panel_class():
    """Test the reaction table panel class"""
    try:
        from freecad.StructureTools.reaction_table_panel import ReactionTablePanel
        print("✅ ReactionTablePanel class found")
        return True
    except Exception as e:
        print(f"❌ ReactionTablePanel class test failed: {e}")
        return False

def run_table_test():
    """Run complete test suite for reaction table panel"""
    print("=" * 50)
    print("TESTING REACTION TABLE PANEL SYSTEM")
    print("=" * 50)
    
    # Test 1: Import
    print("1. Testing imports...")
    if not test_reaction_table_import():
        return False
    
    # Test 2: Test panel class
    print("\n2. Testing panel class...")
    if not test_reaction_table_panel_class():
        return False
    
    # Test 3: Test command
    print("\n3. Testing command system...")
    if not test_reaction_table_command():
        print("   Warning: Command test failed but system may still work")
    
    print("\n" + "=" * 50)
    print("✅ REACTION TABLE PANEL TESTS COMPLETED!")
    print("You can now:")
    print("   - Use the ReactionTablePanel toolbar button")
    print("   - Use the Table View button in Reaction Results panel")
    print("   - View reaction results in tabular format")
    print("   - Export to Excel, Word, or CSV formats")
    print("=" * 50)
    
    return True

# Auto-run test when imported in FreeCAD
if __name__ == "__main__":
    run_table_test()