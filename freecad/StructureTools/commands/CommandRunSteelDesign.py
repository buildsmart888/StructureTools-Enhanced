
import FreeCAD
import FreeCADGui
import os

ICONPATH = os.path.join(os.path.dirname(__file__), "..", "resources")

class CommandRunSteelDesign:
    """
    Command to run Steel Design Checks on an existing Analysis result.
    Updates the MemberResults with design ratios.
    """
    
    def GetResources(self):
        # Use existing icon temporarily
        icon_path = os.path.join(ICONPATH, "icons/aisc_design.svg")
        if not os.path.exists(icon_path):
             icon_path = os.path.join(ICONPATH, "icons/calc.svg")
             
        return {
            "Pixmap": icon_path, 
            "MenuText": "Run Steel Design",
            "ToolTip": "Perform steel design checks (ASD) on the calculated model",
            "Accel": "Shift+S"
        }

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        if not doc:
            return

        # Find the active Calc object (Analysis)
        # Strategy: Look for selected Calc object, or finding the first one in the doc
        selection = FreeCADGui.Selection.getSelection()
        calc_obj = None
        
        if selection:
            for sel in selection:
                if hasattr(sel, 'Proxy') and sel.Proxy.__class__.__name__ == 'Calc':
                    calc_obj = sel
                    break
        
        if not calc_obj:
            # Try to find any Calc object in document
            for obj in doc.Objects:
                if hasattr(obj, 'Proxy') and obj.Proxy.__class__.__name__ == 'Calc':
                    calc_obj = obj
                    break
                    
        if not calc_obj:
            FreeCAD.Console.PrintError("No Analysis (Calc) object found or selected!\n")
            return

        # Check if model exists
        if not hasattr(calc_obj, 'model') or calc_obj.model is None:
             FreeCAD.Console.PrintError("Analysis model not found. Please run 'Calc' (Analysis) first.\n")
             return
             
        # Run Design
        self.run_design(calc_obj)

    def run_design(self, obj):
        import FreeCAD
        from freecad.StructureTools.analysis.steel_design import SteelDesignChecker
        from freecad.StructureTools.analysis.result_manager import ResultManager
        from freecad.StructureTools.analysis.pynite_adapter import PyniteAdapter
        
        FreeCAD.Console.PrintMessage("Starting Steel Design Check...\n")
        
        model = obj.model
        active_load_combination = getattr(obj, 'LoadCombination', '100_DL') # Default fallback
        
        # Setup helpers
        # Hack to reuse ResultManager with existing model
        adapter = PyniteAdapter()
        adapter.model = model
        result_manager = ResultManager(adapter)
        
        checker = SteelDesignChecker(model)
        
        doc = FreeCAD.ActiveDocument
        doc.openTransaction("Run Steel Design")
        
        count = 0
        changed_objs = []
        
        try:
            for member_name in model.members:
                # Get max forces
                forces = result_manager.get_max_member_forces(member_name, active_load_combination)
                
                # Check Member
                # Ideally check if member material is Steel before checking?
                # SteelDesignChecker could return 0.0 or skip if properties missing?
                # For now, we try checking all members.
                
                ratio, details = checker.check_member(member_name, forces)
                
                # Update FreeCAD Object
                found_obj = None
                
                # Lookup object logic
                # Try exact name first
                found_obj = doc.getObject(member_name)
                
                # If not found, search in ListElements for prefix match (lines used in calc)
                if not found_obj and hasattr(obj, 'ListElements'):
                     for el in obj.ListElements:
                        if member_name.startswith(el.Name):
                            found_obj = el
                            break
                            
                if found_obj:
                    # Verify material (optional optimization)
                    # For now just apply result.
                    
                    if not hasattr(found_obj, 'DesignRatio'):
                        found_obj.addProperty("App::PropertyFloat", "DesignRatio", "Design", "Utilization Ratio")
                    if not hasattr(found_obj, 'DesignStatus'):
                        found_obj.addProperty("App::PropertyString", "DesignStatus", "Design", "Design Status")
                    if not hasattr(found_obj, 'MaxUtilization'): 
                        found_obj.addProperty("App::PropertyFloat", "MaxUtilization", "Design", "Max Utilization")
                        
                    # Update
                    # Taking max if multiple segments map to one object
                    current_max = getattr(found_obj, 'DesignRatio', 0.0)
                    
                    # Reset if this is the first time in this run? 
                    # Difficult to know if we are iterating the same object multiple times without tracking.
                    # A better way: Collect all ratios for an object ID, then apply MAX at the end.
                    # But assuming one-to-one or suffix mapping for simple cases:
                    
                    # Logic: If we just started, we should probably reset?
                    # But we are iterating Pynite members.
                    # Let's just use max(current, ratio) but we need to know if 'current' is old data.
                    # Pynite members are usually unique per span. 
                    # If multiple Pynite members map to one FC object (e.g. subdivided), we want the critical ratio.
                    
                    new_max = max(current_max, ratio)
                    
                    # Wait! 'current_max' keeps the value from previous runs if we don't reset it!
                    # We should really reset all relevant objects first.
                    # But iterating doc objects is slow.
                    # Strategy: Use a dictionary to track max ratios for fc objects in this run.
                    
                    # See optimized approach below
                    
                    pass 

            # Optimized Update Loop
            fc_obj_ratios = {} # {obj_name: max_ratio}
            
            for member_name in model.members:
                 forces = result_manager.get_max_member_forces(member_name, active_load_combination)
                 ratio, details = checker.check_member(member_name, forces)
                 
                 # Map to FC Name
                 fc_name = None
                 # Try exact
                 if doc.getObject(member_name):
                     fc_name = member_name
                 else:
                     # Suffix match
                     # Assumes format Name_NodeA_NodeB or Name_i
                     # Simple heuristics: split by '_' and take first part? 
                     # Risk: user named object "Beam_1".
                     # Robust: Match against obj.ListElements
                     if hasattr(obj, 'ListElements'):
                         for el in obj.ListElements:
                             if member_name.startswith(el.Name):
                                 fc_name = el.Name
                                 break
                 
                 if fc_name:
                     if fc_name not in fc_obj_ratios:
                         fc_obj_ratios[fc_name] = ratio
                     else:
                         fc_obj_ratios[fc_name] = max(fc_obj_ratios[fc_name], ratio)
            
            # Apply to objects
            for fc_name, val in fc_obj_ratios.items():
                el = doc.getObject(fc_name)
                if el:
                    # Add props
                    if not hasattr(el, 'DesignRatio'):
                        el.addProperty("App::PropertyFloat", "DesignRatio", "Design", "Utilization Ratio")
                        el.DesignRatio = 0.0 # Init
                    if not hasattr(el, 'DesignStatus'):
                        el.addProperty("App::PropertyString", "DesignStatus", "Design", "Design Status")
                    if not hasattr(el, 'MaxUtilization'): 
                        el.addProperty("App::PropertyFloat", "MaxUtilization", "Design", "Max Utilization")
                        el.MaxUtilization = 0.0

                    el.DesignRatio = val
                    el.MaxUtilization = val
                    
                    if val > 1.0:
                        el.DesignStatus = "Fail"
                    elif val > 0.8:
                        el.DesignStatus = "Warning"
                    else:
                        el.DesignStatus = "Pass"
                        
                    count += 1

            FreeCAD.Console.PrintMessage(f"Design Check Complete. Updated {count} objects.\n")
            doc.commitTransaction()
            
            # Auto-trigger visualization?
            # Let's do it.
            doc.recompute()
            
            # Run ShowDesignStatus logic specifically to update colors
            # Because recompute might not trigger ViewProvider colormap updates if purely python
            if hasattr(FreeCADGui, 'runCommand'):
                 # We can invoke the command visually or just replicate logic
                 from freecad.StructureTools.commands.CommandShowDesign import CommandShowDesign
                 cmd = CommandShowDesign()
                 if cmd.IsActive():
                     cmd.Activated()
            
        except ImportError:
            FreeCAD.Console.PrintError("Steel Design Module not found.\n")
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error during steel design: {e}\n")
            import traceback
            traceback.print_exc()

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None

FreeCADGui.addCommand('RunSteelDesign', CommandRunSteelDesign())

if __name__ == "__main__":
    pass
