# -*- coding: utf-8 -*-
"""
Complete BIM Integration Commands for StructureTools

This module provides comprehensive commands for BIM Workbench integration,
allowing seamless workflow between BIM and structural analysis.
"""

import FreeCAD as App
import FreeCADGui as Gui
import os
from .BIMIntegration import bim_integration

class BIMImportCommand:
    """Command to import BIM objects as structural elements"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "bim_import.svg"),
            "MenuText": "Import from BIM",
            "ToolTip": "Import selected BIM objects as structural elements"
        }
    
    def Activated(self):
        """Execute the BIM import command"""
        try:
            # Get selected objects
            selected_objects = Gui.Selection.getSelection()
            
            if not selected_objects:
                FreeCAD.Console.PrintWarning("Please select BIM objects to import\n")
                return
            
            # Import objects
            imported_objects = bim_integration.import_from_bim(selected_objects)
            
            if imported_objects:
                FreeCAD.Console.PrintMessage(f"Successfully imported {len(imported_objects)} structural elements\n")
                
                # Show simple summary
                summary_msg = f"Imported structural elements:\n"
                for obj in imported_objects[:5]:  # Show first 5
                    summary_msg += f"- {obj.Label}\n"
                if len(imported_objects) > 5:
                    summary_msg += f"... and {len(imported_objects) - 5} more\n"
                
                FreeCAD.Console.PrintMessage(summary_msg)
            else:
                FreeCAD.Console.PrintWarning("No valid BIM objects found for import\n")
                
        except Exception as e:
            FreeCAD.Console.PrintError(f"BIM import failed: {str(e)}\n")
    
    def IsActive(self):
        """Command is active when document exists and objects are selected"""
        return App.ActiveDocument is not None and len(Gui.Selection.getSelection()) > 0

class BIMExportResultsCommand:
    """Command to export structural analysis results back to BIM"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "bim_export.svg"),
            "MenuText": "Export Results to BIM", 
            "ToolTip": "Export structural analysis results back to BIM objects"
        }
    
    def Activated(self):
        """Execute the results export command"""
        try:
            # Find calc objects with results
            calc_objects = self.find_calc_objects_with_results()
            
            if not calc_objects:
                FreeCAD.Console.PrintWarning("No structural analysis results found to export\n")
                return
            
            # Use first calc object for now (could be enhanced with selection dialog)
            selected_calc = calc_objects[0]
            results = self.extract_results_from_calc(selected_calc)
            
            # Get structural objects linked to BIM
            structural_objects = list(bim_integration.structural_to_bim_map.keys())
            
            if structural_objects:
                bim_integration.export_results_to_bim(structural_objects, results)
                FreeCAD.Console.PrintMessage(f"Results exported to {len(structural_objects)} BIM objects\n")
            else:
                FreeCAD.Console.PrintWarning("No linked BIM objects found\n")
                    
        except Exception as e:
            FreeCAD.Console.PrintError(f"BIM export failed: {str(e)}\n")
    
    def find_calc_objects_with_results(self):
        """Find calc objects that have analysis results"""
        calc_objects = []
        
        for obj in App.ActiveDocument.Objects:
            if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
                if obj.Proxy.Type == 'Calc':
                    # Check if it has results
                    if hasattr(obj, 'solved') and obj.solved:
                        calc_objects.append(obj)
        
        return calc_objects
    
    def extract_results_from_calc(self, calc_obj):
        """Extract analysis results from calc object"""
        results = {}
        
        try:
            # Get model from calc
            if hasattr(calc_obj, 'model') and calc_obj.model:
                model = calc_obj.model
                
                # Extract member results
                if hasattr(model, 'Members'):
                    for member_name, member in model.Members.items():
                        try:
                            # Get moment and deflection arrays
                            moments = []
                            deflections = []
                            
                            if hasattr(member, 'moment_array'):
                                moments = [m for m in member.moment_array() if m is not None]
                            if hasattr(member, 'deflection_array'):
                                deflections = [d for d in member.deflection_array() if d is not None]
                            
                            results[member_name] = {
                                'max_moment': max([abs(m) for m in moments]) if moments else 0,
                                'max_deflection': max([abs(d) for d in deflections]) if deflections else 0,
                                'capacity_ratio': 0.75  # Placeholder - would calculate actual ratio
                            }
                        except Exception as e:
                            FreeCAD.Console.PrintWarning(f"Could not extract results for {member_name}: {str(e)}\n")
                            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Could not extract results: {str(e)}\n")
        
        return results
    
    def IsActive(self):
        """Command is active when document exists and there are analysis results"""
        if not App.ActiveDocument:
            return False
        return len(self.find_calc_objects_with_results()) > 0

class BIMSyncCommand:
    """Command to synchronize changes between BIM and structural models"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "bim_sync.svg"),
            "MenuText": "Sync BIM Changes",
            "ToolTip": "Synchronize geometry changes between BIM and structural objects"
        }
    
    def Activated(self):
        """Execute the sync command"""
        try:
            # Check if there are linked objects
            if not bim_integration.bim_to_structural_map:
                FreeCAD.Console.PrintWarning("No BIM-Structural links found to synchronize\n")
                return
            
            # Perform synchronization
            bim_integration.sync_geometry_changes()
            
            FreeCAD.Console.PrintMessage("BIM-Structural synchronization completed\n")
            App.ActiveDocument.recompute()
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"BIM sync failed: {str(e)}\n")
    
    def IsActive(self):
        """Command is active when there are linked BIM-Structural objects"""
        return (App.ActiveDocument is not None and 
                len(bim_integration.bim_to_structural_map) > 0)

class BIMStatusCommand:
    """Command to show BIM integration status and manage links"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "bim_status.svg"),
            "MenuText": "BIM Integration Status",
            "ToolTip": "Show BIM integration status and manage object links"
        }
    
    def Activated(self):
        """Show BIM integration status"""
        try:
            # Print status to console
            num_bim_links = len(bim_integration.bim_to_structural_map)
            num_structural_links = len(bim_integration.structural_to_bim_map)
            
            status_msg = f"BIM Integration Status:\n"
            status_msg += f"- BIM to Structural links: {num_bim_links}\n"
            status_msg += f"- Structural to BIM links: {num_structural_links}\n"
            
            if num_bim_links > 0:
                status_msg += "\nLinked Objects:\n"
                for bim_obj, struct_obj in list(bim_integration.bim_to_structural_map.items())[:5]:
                    status_msg += f"- {bim_obj.Label} -> {struct_obj.Label}\n"
                if num_bim_links > 5:
                    status_msg += f"... and {num_bim_links - 5} more links\n"
            else:
                status_msg += "\nNo BIM-Structural links found.\n"
                status_msg += "Use 'Import from BIM' to create links.\n"
            
            FreeCAD.Console.PrintMessage(status_msg)
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Could not show BIM status: {str(e)}\n")
    
    def IsActive(self):
        """Always active when document exists"""
        return App.ActiveDocument is not None

class CreateStructuralDrawingCommand:
    """Command to create structural drawings in TechDraw"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "structural_drawing.svg"),
            "MenuText": "Create Structural Drawing",
            "ToolTip": "Create structural plan and elevation drawings in TechDraw"
        }
    
    def Activated(self):
        """Create structural drawings"""
        try:
            # Get structural objects
            structural_objects = [obj for obj in App.ActiveDocument.Objects 
                                if hasattr(obj, 'Proxy') and 
                                hasattr(obj.Proxy, 'Type') and 
                                obj.Proxy.Type in ['Member', 'StructuralBeam', 'StructuralColumn']]
            
            if not structural_objects:
                FreeCAD.Console.PrintWarning("No structural elements found for drawing\n")
                return
            
            # Create TechDraw page
            page = App.ActiveDocument.addObject('TechDraw::DrawPage', 'StructuralPlan')
            
            # Create template (basic A4)
            template = App.ActiveDocument.addObject('TechDraw::DrawSVGTemplate', 'Template')
            template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_Landscape.svg"
            page.Template = template
            
            # Create structural plan view
            plan_view = App.ActiveDocument.addObject('TechDraw::DrawViewPart', 'PlanView')
            plan_view.Source = structural_objects
            plan_view.Direction = App.Vector(0, 0, -1)  # Top view
            plan_view.Scale = 0.01  # 1:100 scale
            page.addView(plan_view)
            
            FreeCAD.Console.PrintMessage(f"Created structural drawing with {len(structural_objects)} elements\n")
            App.ActiveDocument.recompute()
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Could not create structural drawing: {str(e)}\n")
    
    def IsActive(self):
        """Active when document exists and has structural elements"""
        if not App.ActiveDocument:
            return False
        return any(hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type') and 
                  obj.Proxy.Type in ['Member', 'StructuralBeam'] 
                  for obj in App.ActiveDocument.Objects)

class ExportToFEMCommand:
    """Command to export structural model to FEM workbench"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "fem_export.svg"),
            "MenuText": "Export to FEM",
            "ToolTip": "Export structural model to FEM workbench for advanced analysis"
        }
    
    def Activated(self):
        """Export to FEM workbench"""
        try:
            # Check if FEM workbench is available
            try:
                import Fem
                has_fem = True
            except ImportError:
                has_fem = False
                FreeCAD.Console.PrintError("FEM workbench not available\n")
                return
            
            # Get structural objects
            structural_objects = [obj for obj in App.ActiveDocument.Objects 
                                if hasattr(obj, 'Proxy') and 
                                hasattr(obj.Proxy, 'Type') and 
                                obj.Proxy.Type in ['Member', 'Calc']]
            
            if not structural_objects:
                FreeCAD.Console.PrintWarning("No structural model found for FEM export\n")
                return
            
            # Create FEM analysis
            analysis = App.ActiveDocument.addObject('Fem::FemAnalysis', 'StructuralFEMAnalysis')
            
            # Export geometry and create mesh
            # This would require more detailed FEM integration
            FreeCAD.Console.PrintMessage("Basic FEM analysis container created\n")
            FreeCAD.Console.PrintMessage("Advanced FEM export requires additional implementation\n")
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"FEM export failed: {str(e)}\n")
    
    def IsActive(self):
        """Active when document exists and has structural model"""
        if not App.ActiveDocument:
            return False
        return any(hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type') and 
                  obj.Proxy.Type in ['Member', 'Calc'] 
                  for obj in App.ActiveDocument.Objects)

# Register all commands
Gui.addCommand("BIM_Import", BIMImportCommand())
Gui.addCommand("BIM_Export", BIMExportResultsCommand())  
Gui.addCommand("BIM_Sync", BIMSyncCommand())
Gui.addCommand("BIM_Status", BIMStatusCommand())
Gui.addCommand("CreateStructuralDrawing", CreateStructuralDrawingCommand())
Gui.addCommand("ExportToFEM", ExportToFEMCommand())
