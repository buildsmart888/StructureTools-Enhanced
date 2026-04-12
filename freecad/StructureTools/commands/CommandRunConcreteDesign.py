
import FreeCAD
import FreeCADGui
import os

ICONPATH = os.path.join(os.path.dirname(__file__), "..", "resources")

class CommandRunConcreteDesign:
    """
    Command to run Concrete Design Checks (RC) on an existing Analysis result.
    Updates the MemberResults with design ratios.
    Checks only members with defined reinforcement.
    """
    
    def GetResources(self):
        # Use existing icon temporarily
        icon_path = os.path.join(ICONPATH, "icons/aci_design.svg")
        if not os.path.exists(icon_path):
             icon_path = os.path.join(ICONPATH, "icons/calc.svg")
             
        return {
            "Pixmap": icon_path, 
            "MenuText": "Run Concrete Design",
            "ToolTip": "Perform reinforced concrete design checks (ACI 318) on the calculated model",
            "Accel": "Shift+C"
        }

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        if not doc:
            return

        # Find the active Calc object
        selection = FreeCADGui.Selection.getSelection()
        calc_obj = None
        
        if selection:
            for sel in selection:
                if hasattr(sel, 'Proxy') and sel.Proxy.__class__.__name__ == 'Calc':
                    calc_obj = sel
                    break
        
        if not calc_obj:
            for obj in doc.Objects:
                if hasattr(obj, 'Proxy') and obj.Proxy.__class__.__name__ == 'Calc':
                    calc_obj = obj
                    break
                    
        if not calc_obj:
            FreeCAD.Console.PrintError("No Analysis (Calc) object found or selected!\n")
            return

        if not hasattr(calc_obj, 'model') or calc_obj.model is None:
             FreeCAD.Console.PrintError("Analysis model not found. Please run 'Calc' (Analysis) first.\n")
             return
             
        self.run_design(calc_obj)

    def run_design(self, obj):
        import FreeCAD
        from freecad.StructureTools.analysis.concrete_design import ConcreteDesignChecker
        from freecad.StructureTools.analysis.result_manager import ResultManager
        from freecad.StructureTools.analysis.pynite_adapter import PyniteAdapter
        
        FreeCAD.Console.PrintMessage("Starting Reinforced Concrete Design Check...\n")
        
        model = obj.model
        active_load_combination = getattr(obj, 'LoadCombination', '100_DL') 
        
        adapter = PyniteAdapter()
        adapter.model = model
        result_manager = ResultManager(adapter)
        
        checker = ConcreteDesignChecker(model)
        
        doc = FreeCAD.ActiveDocument
        doc.openTransaction("Run Concrete Design")
        
        count = 0
        fc_obj_ratios = {}
        
        try:
            for member_name in model.members:
                # Pre-check: Is this member Concrete?
                # Look up section in model
                mem = model.members[member_name]
                sec_name = mem.section_name
                is_concrete = False
                if sec_name in model.sections:
                    sec = model.sections[sec_name]
                    # Check for Rebar properties
                    # Note: We attached them in ModelBuilder
                    if hasattr(sec, 'RebarAreaBottom') and sec.RebarAreaBottom > 0:
                        is_concrete = True
                    elif hasattr(sec, 'RebarAreaTop') and sec.RebarAreaTop > 0:
                        is_concrete = True
                        
                if not is_concrete:
                    continue

                # Run Check
                forces = result_manager.get_max_member_forces(member_name, active_load_combination)
                ratio, details = checker.check_member(member_name, forces)
                
                # Map to FC Name
                fc_name = None
                if doc.getObject(member_name):
                     fc_name = member_name
                else:
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
                    if not hasattr(el, 'DesignRatio'):
                        el.addProperty("App::PropertyFloat", "DesignRatio", "Design", "Utilization Ratio")
                    if not hasattr(el, 'DesignStatus'):
                        el.addProperty("App::PropertyString", "DesignStatus", "Design", "Design Status")
                    if not hasattr(el, 'MaxUtilization'): 
                        el.addProperty("App::PropertyFloat", "MaxUtilization", "Design", "Max Utilization")

                    el.DesignRatio = val
                    el.MaxUtilization = val
                    
                    if val > 1.0:
                        el.DesignStatus = "Fail"
                    elif val > 0.8:
                        el.DesignStatus = "Warning"
                    else:
                        el.DesignStatus = "Pass"
                        
                    count += 1

            FreeCAD.Console.PrintMessage(f"RC Design Check Complete. Updated {count} objects.\n")
            doc.commitTransaction()
            
            doc.recompute()
            
            if hasattr(FreeCADGui, 'runCommand'):
                 from freecad.StructureTools.commands.CommandShowDesign import CommandShowDesign
                 cmd = CommandShowDesign()
                 if cmd.IsActive():
                     cmd.Activated()
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error during concrete design: {e}\n")
            import traceback
            traceback.print_exc()

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None

FreeCADGui.addCommand('RunConcreteDesign', CommandRunConcreteDesign())

if __name__ == "__main__":
    pass
