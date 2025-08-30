"""
Example script demonstrating the Reaction Table Panel functionality
This script creates a simple structure and shows how to use the reaction table panel
"""

import FreeCAD, FreeCADGui

def create_example_structure():
    """Create a simple example structure to demonstrate reaction results"""
    # Create new document
    doc = FreeCAD.newDocument("ReactionTableExample")
    
    # Import required modules
    import Part
    from freecad.StructureTools import suport, material, member, load_distributed, calc
    
    # Create geometry - a simple beam
    p1 = FreeCAD.Vector(0, 0, 0)
    p2 = FreeCAD.Vector(5000, 0, 0)  # 5m beam
    line = Part.makeLine(p1, p2)
    beam = doc.addObject("Part::Feature", "Beam")
    beam.Shape = line
    
    # Create fixed support at left end
    support1 = doc.addObject("App::DocumentObjectGroupPython", "FixedSupport")
    suport.Suport(support1, [beam], [p1])
    support1.SupportDX = True
    support1.SupportDY = True
    support1.SupportDZ = True
    support1.SupportRX = True
    support1.SupportRY = True
    support1.SupportRZ = True
    
    # Create pinned support at right end
    support2 = doc.addObject("App::DocumentObjectGroupPython", "PinnedSupport")
    suport.Suport(support2, [beam], [p2])
    support2.SupportDY = True
    support2.SupportDZ = True
    
    # Create material (steel)
    mat = doc.addObject("App::DocumentObjectGroupPython", "Steel")
    material.Material(mat)
    mat.Standard = "ASTM-A36"
    
    # Create member
    mem = doc.addObject("App::DocumentObjectGroupPython", "StructuralMember")
    member.Member(mem, [beam])
    mem.Material = mat
    
    # Create distributed load
    load = doc.addObject("App::DocumentObjectGroupPython", "UniformLoad")
    load_distributed.Load_Distributed(load, [beam])
    load.LoadType = 'DL'
    load.Magnitude = 15.0  # 15 kN/m
    
    # Create calculation object
    calc_obj = doc.addObject("App::DocumentObjectGroupPython", "StructuralAnalysis")
    elements = [beam, load, support1, support2, mem, mat]
    calc.Calc(calc_obj, elements)
    
    # Run the analysis
    calc_obj.Proxy.execute(calc_obj)
    
    # Create reaction results visualization
    from freecad.StructureTools.reaction_results import ReactionResults, ViewProviderReactionResults
    reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "ReactionResults")
    ReactionResults(reaction_obj, calc_obj)
    ViewProviderReactionResults(reaction_obj.ViewObject)
    
    # Recompute document
    doc.recompute()
    
    print("Example structure created successfully!")
    print("To view reaction results:")
    print("1. Double-click the 'ReactionResults' object in the tree view")
    print("2. Or use the 'Reaction Results Table' command from the toolbar")
    print("3. Or right-click the 'ReactionResults' object and select 'Open Reaction Table'")
    
    return reaction_obj

# Run the example
if __name__ == "__main__":
    reaction_obj = create_example_structure()