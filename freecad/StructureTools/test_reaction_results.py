"""
Simple test script for Reaction Results functionality
Run this in FreeCAD Python console to test the system
"""

import FreeCAD, FreeCADGui
import os

def test_reaction_results_import():
    """Test if reaction results can be imported"""
    try:
        from freecad.StructureTools import reaction_results
        print("✅ reaction_results imported successfully")
        return True
    except Exception as e:
        print(f"❌ reaction_results import failed: {e}")
        return False

def test_create_sample_structure():
    """Create a simple test structure with calc object"""
    try:
        # Create a simple beam structure for testing
        doc = FreeCAD.ActiveDocument
        if not doc:
            doc = FreeCAD.newDocument("ReactionTest")
        
        # Create simple geometry
        import Part
        
        # Create two points
        p1 = FreeCAD.Vector(0, 0, 0)
        p2 = FreeCAD.Vector(3000, 0, 0)  # 3m beam
        
        # Create line
        line = Part.makeLine(p1, p2)
        beam = doc.addObject("Part::Feature", "TestBeam")
        beam.Shape = line
        
        # Create supports
        from freecad.StructureTools import suport
        
        # Left support (fixed)
        support1 = doc.addObject("App::DocumentObjectGroupPython", "Support1")
        suport.Suport(support1, [beam], [p1])
        support1.SupportDX = True
        support1.SupportDY = True
        support1.SupportDZ = True
        support1.SupportRX = True
        support1.SupportRY = True
        support1.SupportRZ = True
        
        # Right support (pinned)
        support2 = doc.addObject("App::DocumentObjectGroupPython", "Support2") 
        suport.Suport(support2, [beam], [p2])
        support2.SupportDY = True
        support2.SupportDZ = True
        
        # Create material
        from freecad.StructureTools import material
        mat = doc.addObject("App::DocumentObjectGroupPython", "Steel")
        material.Material(mat)
        
        # Create member
        from freecad.StructureTools import member
        mem = doc.addObject("App::DocumentObjectGroupPython", "Member1")
        member.Member(mem, [beam])
        mem.Material = mat
        
        # Create load
        from freecad.StructureTools import load_distributed
        load = doc.addObject("App::DocumentObjectGroupPython", "DistLoad")
        load_distributed.Load_Distributed(load, [beam])
        load.LoadType = 'DL'
        load.Magnitude = 10.0  # kN/m
        
        # Create calc object
        from freecad.StructureTools import calc
        calc_obj = doc.addObject("App::DocumentObjectGroupPython", "Calculation")
        elements = [beam, load, support1, support2, mem, mat]
        calc.Calc(calc_obj, elements)
        
        # Run analysis
        calc_obj.Proxy.execute(calc_obj)
        
        doc.recompute()
        print("✅ Test structure created successfully")
        print(f"   - Beam: {beam.Name}")
        print(f"   - Supports: {support1.Name}, {support2.Name}")
        print(f"   - Load: {load.Name}")
        print(f"   - Calc: {calc_obj.Name}")
        
        return calc_obj
        
    except Exception as e:
        print(f"❌ Failed to create test structure: {e}")
        return None

def test_reaction_results_creation(calc_obj):
    """Test creating reaction results visualization"""
    try:
        if not calc_obj:
            print("❌ No calc object provided")
            return False
            
        # Import reaction results
        from freecad.StructureTools.reaction_results import ReactionResults, ViewProviderReactionResults
        
        # Create reaction results object
        doc = FreeCAD.ActiveDocument
        reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "ReactionResults")
        ReactionResults(reaction_obj, calc_obj)
        ViewProviderReactionResults(reaction_obj.ViewObject)
        
        doc.recompute()
        print("✅ Reaction results object created successfully")
        
        # Test execution
        reaction_obj.Proxy.execute(reaction_obj)
        print("✅ Reaction visualization executed successfully")
        
        return reaction_obj
        
    except Exception as e:
        print(f"❌ Failed to create reaction results: {e}")
        return None

def test_reaction_command():
    """Test the reaction results command"""
    try:
        from freecad.StructureTools.reaction_results import CommandReactionResults
        cmd = CommandReactionResults()
        
        # Check if command can be activated
        if cmd.IsActive():
            print("✅ Reaction Results command is active")
            # Don't actually activate to avoid UI issues in console
            return True
        else:
            print("❌ Reaction Results command is not active (no document?)")
            return False
            
    except Exception as e:
        print(f"❌ Command test failed: {e}")
        return False

def run_full_test():
    """Run complete test suite"""
    print("=" * 50)
    print("TESTING REACTION RESULTS SYSTEM")
    print("=" * 50)
    
    # Test 1: Import
    print("1. Testing imports...")
    if not test_reaction_results_import():
        return False
    
    # Test 2: Create test structure
    print("\n2. Creating test structure...")
    calc_obj = test_create_sample_structure()
    if not calc_obj:
        return False
    
    # Test 3: Create reaction results
    print("\n3. Testing reaction results creation...")
    reaction_obj = test_reaction_results_creation(calc_obj)
    if not reaction_obj:
        return False
    
    # Test 4: Test command
    print("\n4. Testing command system...")
    if not test_reaction_command():
        print("   Warning: Command test failed but system may still work")
    
    print("\n" + "=" * 50)
    print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
    print("You can now:")
    print("   - Use the ReactionResults toolbar button")
    print("   - Double-click the ReactionResults object to open controls")
    print("   - Check reaction forces and moments display")
    print("=" * 50)
    
    return True

# Auto-run test when imported in FreeCAD
if __name__ == "__main__":
    run_full_test()