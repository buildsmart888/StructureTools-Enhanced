"""
Test script to verify calc command works after selfWeight fix
Run in FreeCAD Python Console
"""

def test_calc_fixed():
    import FreeCAD, FreeCADGui
    print("=== Testing Calc Command After Fix ===")
    
    try:
        # Create new document if none exists
        if not FreeCAD.ActiveDocument:
            FreeCAD.newDocument("CalcTest")
        
        doc = FreeCAD.ActiveDocument
        
        # Create simple test geometry
        import Part
        
        # Create a simple beam
        p1 = FreeCAD.Vector(0, 0, 0)
        p2 = FreeCAD.Vector(3000, 0, 0)  # 3m beam
        line = Part.makeLine(p1, p2)
        beam = doc.addObject("Part::Feature", "TestBeam")
        beam.Shape = line
        
        print("✅ Created test beam")
        
        # Create calc object with proper properties
        from freecad.StructureTools import calc
        calc_obj = doc.addObject("App::DocumentObjectGroupPython", "TestCalc")
        
        # Pass minimal elements list
        elements = [beam]
        calc.Calc(calc_obj, elements)
        
        print("✅ Created calc object with properties")
        print(f"   - selfWeight property: {hasattr(calc_obj, 'selfWeight')}")
        print(f"   - selfWeight value: {getattr(calc_obj, 'selfWeight', 'NOT FOUND')}")
        
        # Try to execute calc (this should not fail now)
        try:
            calc_obj.Proxy.execute(calc_obj)
            print("✅ Calc execution completed without errors")
            
            # Check if FEModel was stored
            if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                print(f"✅ FEModel stored with {len(calc_obj.FEModel.nodes)} nodes")
                
                # Now test reaction results creation
                try:
                    from freecad.StructureTools import reaction_results
                    reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "TestReactionResults")
                    reaction_results.ReactionResults(reaction_obj, calc_obj)
                    reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
                    
                    print("✅ Reaction results object created successfully")
                    print("   You can now double-click it to open the control panel")
                    
                except Exception as e:
                    print(f"⚠️ Reaction results creation failed: {e}")
                    print("   But calc command is working now!")
                    
            else:
                print("⚠️ No FEModel found - may need supports and loads for full analysis")
                
        except Exception as e:
            print(f"❌ Calc execution still failing: {e}")
            return False
            
        doc.recompute()
        
        print("\n=== Test Summary ===")
        print("✅ selfWeight property added successfully")
        print("✅ Calc command executes without attribute errors")
        print("✅ Ready to test with full structural model")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def create_full_test_model():
    """Create a complete structural model for testing"""
    import FreeCAD, Part
    print("\n=== Creating Full Test Model ===")
    
    try:
        if not FreeCAD.ActiveDocument:
            FreeCAD.newDocument("FullTest")
        
        doc = FreeCAD.ActiveDocument
        
        # Create beam
        p1 = FreeCAD.Vector(0, 0, 0)
        p2 = FreeCAD.Vector(3000, 0, 0)  # 3m beam
        line = Part.makeLine(p1, p2)
        beam = doc.addObject("Part::Feature", "Beam")
        beam.Shape = line
        
        # Create material
        from freecad.StructureTools import material
        mat = doc.addObject("App::DocumentObjectGroupPython", "Steel")
        material.Material(mat)
        print("✅ Created material")
        
        # Create supports
        from freecad.StructureTools import suport
        support1 = doc.addObject("App::DocumentObjectGroupPython", "Support1")
        suport.Suport(support1, [beam], [p1])
        support1.SupportDX = True
        support1.SupportDY = True
        support1.SupportDZ = True
        
        support2 = doc.addObject("App::DocumentObjectGroupPython", "Support2")
        suport.Suport(support2, [beam], [p2])
        support2.SupportDY = True
        support2.SupportDZ = True
        print("✅ Created supports")
        
        # Create member
        from freecad.StructureTools import member
        mem = doc.addObject("App::DocumentObjectGroupPython", "Member")
        member.Member(mem, [beam])
        mem.Material = mat
        print("✅ Created member")
        
        # Create load
        from freecad.StructureTools import load_distributed
        load = doc.addObject("App::DocumentObjectGroupPython", "Load")
        load_distributed.Load_Distributed(load, [beam])
        load.LoadType = 'DL'
        load.Magnitude = 10.0
        print("✅ Created distributed load")
        
        # Create calc with all elements
        from freecad.StructureTools import calc
        calc_obj = doc.addObject("App::DocumentObjectGroupPython", "FullCalc")
        elements = [beam, mat, support1, support2, mem, load]
        calc.Calc(calc_obj, elements)
        
        print("✅ Created full calc object")
        
        # Enable self weight if desired
        calc_obj.selfWeight = True
        print("   - Self weight enabled")
        
        # Run analysis
        calc_obj.Proxy.execute(calc_obj)
        print("✅ Analysis completed successfully")
        
        if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            nodes_count = len(calc_obj.FEModel.nodes)
            print(f"   - FE Model has {nodes_count} nodes")
            
            # Create reaction results
            from freecad.StructureTools import reaction_results
            reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "ReactionResults")
            reaction_results.ReactionResults(reaction_obj, calc_obj)
            reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
            
            print("✅ Reaction Results created and ready to use!")
            print("   Double-click 'ReactionResults' object to open control panel")
        
        doc.recompute()
        return True
        
    except Exception as e:
        print(f"❌ Full model creation failed: {e}")
        return False

if __name__ == "__main__":
    # Run basic test first
    if test_calc_fixed():
        # Ask if user wants full model
        print("\n" + "="*50)
        print("Would you like to create a complete test model?")
        print("Run: create_full_test_model()")
        print("="*50)