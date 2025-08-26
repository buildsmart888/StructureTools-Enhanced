# -*- coding: utf-8 -*-
"""
TechDraw Integration for StructureTools
Generate structural drawings and diagrams in TechDraw workbench
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import os
from typing import List, Optional, Any

class TechDrawStructuralIntegration:
    """Generate structural drawings in TechDraw workbench"""
    
    def __init__(self):
        self.templates = {
            'structural_plan': 'StructuralPlan.svg',
            'elevation': 'StructuralElevation.svg', 
            'details': 'StructuralDetails.svg',
            'analysis_results': 'AnalysisResults.svg'
        }
    
    def create_structural_drawing(self, calc_obj, drawing_type='comprehensive'):
        """Create comprehensive structural drawing with analysis results"""
        doc = App.ActiveDocument
        if not doc:
            return None
        
        # Create TechDraw page
        page = doc.addObject('TechDraw::DrawPage', 'StructuralAnalysis')
        
        # Add template
        template = doc.addObject('TechDraw::DrawSVGTemplate', 'Template')
        template_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'templates', 
                                   self.templates.get(drawing_type, 'StructuralPlan.svg'))
        if os.path.exists(template_path):
            template.Template = template_path
        page.Template = template
        
        # Add structural elements
        self.add_structural_views(page, calc_obj)
        
        # Add analysis results
        self.add_analysis_diagrams(page, calc_obj)
        
        # Add annotations
        self.add_analysis_annotations(page, calc_obj)
        
        doc.recompute()
        return page
    
    def add_structural_views(self, page, calc_obj):
        """Add structural element views to the drawing"""
        if not hasattr(calc_obj, 'ListElements'):
            return
        
        # Group elements by type
        beams = [elem for elem in calc_obj.ListElements if 'Line' in elem.Name or 'Wire' in elem.Name]
        
        if beams:
            # Create plan view
            plan_view = App.ActiveDocument.addObject('TechDraw::DrawViewPart', 'StructuralPlan')
            plan_view.Source = beams
            plan_view.Direction = App.Vector(0, 0, -1)  # Top view
            plan_view.Scale = 0.01  # Adjust scale as needed
            page.addView(plan_view)
            plan_view.X = 100
            plan_view.Y = 200
            
            # Create elevation view
            elevation_view = App.ActiveDocument.addObject('TechDraw::DrawViewPart', 'StructuralElevation')
            elevation_view.Source = beams
            elevation_view.Direction = App.Vector(0, 1, 0)  # Front view
            elevation_view.Scale = 0.01
            page.addView(elevation_view)
            elevation_view.X = 100
            elevation_view.Y = 100
    
    def add_analysis_diagrams(self, page, calc_obj):
        """Add moment, shear, and deflection diagrams"""
        if not hasattr(calc_obj, 'NameMembers') or not calc_obj.NameMembers:
            return
        
        y_position = 50
        
        # Create diagrams for each type
        diagram_types = [
            ('Moment', 'MomentZ'),
            ('Shear', 'ShearY'),
            ('Deflection', 'DeflectionY')
        ]
        
        for diagram_name, property_name in diagram_types:
            if hasattr(calc_obj, property_name):
                diagram_geometry = self.create_diagram_geometry(calc_obj, property_name)
                if diagram_geometry:
                    diagram_view = App.ActiveDocument.addObject('TechDraw::DrawViewPart', f'{diagram_name}Diagram')
                    diagram_view.Source = [diagram_geometry]
                    diagram_view.Scale = 0.1
                    page.addView(diagram_view)
                    diagram_view.X = 300
                    diagram_view.Y = y_position
                    y_position += 50
    
    def create_diagram_geometry(self, calc_obj, property_name):
        """Create 3D geometry representing analysis diagrams"""
        try:
            # This is a simplified implementation
            # Real implementation would create proper diagram geometry
            doc = App.ActiveDocument
            
            # Create a simple representation
            lines = []
            
            if hasattr(calc_obj, property_name) and getattr(calc_obj, property_name):
                values = getattr(calc_obj, property_name)
                
                # Create diagram points
                for i, value_str in enumerate(values):
                    if isinstance(value_str, str) and ',' in value_str:
                        # Parse comma-separated values
                        diagram_values = [float(v) for v in value_str.split(',') if v.strip()]
                        
                        # Create line representing the diagram
                        for j, val in enumerate(diagram_values):
                            start_point = App.Vector(j * 10, 0, 0)
                            end_point = App.Vector(j * 10, val * 0.001, 0)  # Scale factor
                            line = Part.makeLine(start_point, end_point)
                            lines.append(line)
            
            if lines:
                compound = Part.makeCompound(lines)
                diagram_obj = doc.addObject('Part::Feature', f'{property_name}Diagram')
                diagram_obj.Shape = compound
                return diagram_obj
                
        except Exception as e:
            App.Console.PrintWarning(f"Failed to create diagram geometry: {e}\n")
        
        return None
    
    def add_analysis_annotations(self, page, calc_obj):
        """Add text annotations with analysis results"""
        # Add title
        title_annotation = App.ActiveDocument.addObject('TechDraw::DrawViewAnnotation', 'Title')
        title_annotation.Text = ['Structural Analysis Results', f'Load Combination: {getattr(calc_obj, "LoadCombination", "N/A")}']
        title_annotation.X = 100
        title_annotation.Y = 280
        page.addView(title_annotation)
        
        # Add summary statistics
        if hasattr(calc_obj, 'MaxMomentZ') and calc_obj.MaxMomentZ:
            max_moment = max(calc_obj.MaxMomentZ) if calc_obj.MaxMomentZ else 0
            summary_text = [
                'Analysis Summary:',
                f'Max Moment: {max_moment:.2f}',
                f'Analysis Type: {getattr(calc_obj, "AnalysisType", "Static")}',
                f'Total Elements: {len(getattr(calc_obj, "NameMembers", []))}'
            ]
            
            summary_annotation = App.ActiveDocument.addObject('TechDraw::DrawViewAnnotation', 'Summary')
            summary_annotation.Text = summary_text
            summary_annotation.X = 350
            summary_annotation.Y = 280
            page.addView(summary_annotation)


class CommandCreateStructuralDrawing:
    """Command to create structural drawing in TechDraw"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "techdraw_struct.svg"),
            "MenuText": "Create Structural Drawing",
            "ToolTip": "Create structural analysis drawing in TechDraw"
        }
    
    def Activated(self):
        doc = App.ActiveDocument
        if not doc:
            App.Console.PrintError("No active document\n")
            return
        
        # Find calc objects
        calc_objects = [obj for obj in doc.Objects if hasattr(obj, 'Proxy') and 
                       hasattr(obj.Proxy, '__class__') and 'Calc' in str(obj.Proxy.__class__)]
        
        if not calc_objects:
            App.Console.PrintMessage("No structural analysis found. Run analysis first.\n")
            return
        
        # Use the first calc object
        calc_obj = calc_objects[0]
        
        # Create TechDraw integration and generate drawing
        techdraw_integration = TechDrawStructuralIntegration()
        page = techdraw_integration.create_structural_drawing(calc_obj)
        
        if page:
            App.Console.PrintMessage(f"Created structural drawing: {page.Label}\n")
            # Switch to TechDraw workbench to view the drawing
            try:
                Gui.activateWorkbench("TechDrawWorkbench")
            except:
                App.Console.PrintWarning("TechDraw workbench not available\n")
        else:
            App.Console.PrintError("Failed to create structural drawing\n")
    
    def IsActive(self):
        return App.ActiveDocument is not None


# Register command
Gui.addCommand("CreateStructuralDrawing", CommandCreateStructuralDrawing())
