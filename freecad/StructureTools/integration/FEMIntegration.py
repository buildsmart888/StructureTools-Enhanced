# -*- coding: utf-8 -*-
"""
FEM Workbench Integration for StructureTools
Bridge between StructureTools and FEM workbench for advanced analysis
"""

import FreeCAD as App
import FreeCADGui as Gui
import os
from typing import List, Optional, Any

class FEMStructuralBridge:
    """Bridge to FEM Workbench for advanced analysis"""
    
    def __init__(self):
        self.fem_analysis = None
        self.mesh_object = None
        self.structural_objects = []
    
    def export_to_fem(self, structural_objects):
        """Export structural model to FEM workbench"""
        doc = App.ActiveDocument
        if not doc:
            return None
        
        # Check if FEM workbench is available
        try:
            import Fem
            import femtools.femutils as femutils
        except ImportError:
            App.Console.PrintError("FEM workbench not available\n")
            return None
        
        # Create FEM analysis container
        self.fem_analysis = doc.addObject("Fem::FemAnalysisPython", "StructuralFEMAnalysis")
        
        # Create mesh object
        self.create_fem_mesh(structural_objects)
        
        # Convert materials
        self.convert_materials_to_fem(structural_objects)
        
        # Convert loads and constraints
        self.convert_loads_to_fem(structural_objects)
        self.convert_constraints_to_fem(structural_objects)
        
        # Add solver
        self.add_fem_solver()
        
        doc.recompute()
        return self.fem_analysis
    
    def create_fem_mesh(self, structural_objects):
        """Create FEM mesh from structural objects"""
        try:
            import Fem
            import MeshPart
            
            # Combine all structural geometry
            shapes = []
            for obj in structural_objects:
                if hasattr(obj, 'Shape') and not obj.Shape.isNull():
                    shapes.append(obj.Shape)
            
            if not shapes:
                return None
            
            # Create compound shape
            import Part
            compound = Part.makeCompound(shapes)
            
            # Create mesh object
            mesh_obj = App.ActiveDocument.addObject("Fem::FemMeshGmsh", "StructuralMesh")
            mesh_obj.Part = compound
            
            # Set mesh parameters
            mesh_obj.CharacteristicLengthMax = 1000.0  # mm
            mesh_obj.CharacteristicLengthMin = 100.0   # mm
            mesh_obj.ElementOrder = 'Linear'
            
            # Add to analysis
            self.fem_analysis.addObject(mesh_obj)
            self.mesh_object = mesh_obj
            
            return mesh_obj
            
        except Exception as e:
            App.Console.PrintError(f"Failed to create FEM mesh: {e}\n")
            return None
    
    def convert_materials_to_fem(self, structural_objects):
        """Convert structural materials to FEM materials"""
        try:
            import Fem
            
            # Collect unique materials
            materials = {}
            
            for obj in structural_objects:
                if hasattr(obj, 'MaterialMember') and obj.MaterialMember:
                    material = obj.MaterialMember
                    if material.Label not in materials:
                        materials[material.Label] = material
            
            # Create FEM materials
            for mat_name, material in materials.items():
                fem_material = App.ActiveDocument.addObject("Fem::Material", f"FEM_{mat_name}")
                
                # Extract properties
                try:
                    E = float(material.ModulusElasticity.getValueAs('Pa'))
                    nu = float(material.PoissonRatio)
                    density = float(material.Density.getValueAs('kg/m^3'))
                except:
                    # Fallback values
                    E = 200e9  # Pa
                    nu = 0.3
                    density = 7850  # kg/m^3
                
                # Set FEM material properties
                fem_material.Material = {
                    'Name': mat_name,
                    'YoungsModulus': f"{E} Pa",
                    'PoissonRatio': str(nu),
                    'Density': f"{density} kg/m^3"
                }
                
                self.fem_analysis.addObject(fem_material)
                
        except Exception as e:
            App.Console.PrintError(f"Failed to convert materials to FEM: {e}\n")
    
    def convert_loads_to_fem(self, structural_objects):
        """Convert structural loads to FEM loads"""
        doc = App.ActiveDocument
        
        # Find load objects
        load_objects = [obj for obj in doc.Objects if 'Load' in obj.Name]
        
        for load_obj in load_objects:
            try:
                self.convert_single_load_to_fem(load_obj)
            except Exception as e:
                App.Console.PrintWarning(f"Failed to convert load {load_obj.Label}: {e}\n")
    
    def convert_single_load_to_fem(self, load_obj):
        """Convert a single load object to FEM load"""
        try:
            import Fem
            
            if hasattr(load_obj, 'LoadType'):
                if load_obj.LoadType == 'Nodal':
                    # Create FEM force constraint
                    fem_force = App.ActiveDocument.addObject("Fem::ConstraintForce", f"FEM_{load_obj.Label}")
                    
                    # Set force values
                    if hasattr(load_obj, 'ForceX'):
                        fem_force.Force = load_obj.ForceX * 1000  # Convert to N
                    fem_force.Direction = (1.0, 0.0, 0.0)  # Default direction
                    
                    self.fem_analysis.addObject(fem_force)
                    
                elif load_obj.LoadType == 'Distributed':
                    # Create FEM pressure constraint
                    fem_pressure = App.ActiveDocument.addObject("Fem::ConstraintPressure", f"FEM_{load_obj.Label}")
                    
                    if hasattr(load_obj, 'LoadValue'):
                        fem_pressure.Pressure = load_obj.LoadValue * 1000  # Convert to Pa
                    
                    self.fem_analysis.addObject(fem_pressure)
                    
        except Exception as e:
            App.Console.PrintError(f"Failed to create FEM load: {e}\n")
    
    def convert_constraints_to_fem(self, structural_objects):
        """Convert structural supports to FEM constraints"""
        doc = App.ActiveDocument
        
        # Find support objects
        support_objects = [obj for obj in doc.Objects if 'Suport' in obj.Name]
        
        for support_obj in support_objects:
            try:
                self.convert_single_constraint_to_fem(support_obj)
            except Exception as e:
                App.Console.PrintWarning(f"Failed to convert support {support_obj.Label}: {e}\n")
    
    def convert_single_constraint_to_fem(self, support_obj):
        """Convert a single support to FEM constraint"""
        try:
            import Fem
            
            # Create FEM fixed constraint
            fem_fixed = App.ActiveDocument.addObject("Fem::ConstraintFixed", f"FEM_{support_obj.Label}")
            
            # Set constraint conditions based on support properties
            if hasattr(support_obj, 'FixTranslationX'):
                fem_fixed.NameX = support_obj.FixTranslationX
            if hasattr(support_obj, 'FixTranslationY'):
                fem_fixed.NameY = support_obj.FixTranslationY
            if hasattr(support_obj, 'FixTranslationZ'):
                fem_fixed.NameZ = support_obj.FixTranslationZ
            
            self.fem_analysis.addObject(fem_fixed)
            
        except Exception as e:
            App.Console.PrintError(f"Failed to create FEM constraint: {e}\n")
    
    def add_fem_solver(self):
        """Add FEM solver to the analysis"""
        try:
            import Fem
            
            # Add CalculiX solver (most common)
            solver = App.ActiveDocument.addObject("Fem::SolverCalculix", "CalculiXSolver")
            
            # Set solver parameters
            solver.AnalysisType = 'static'
            solver.GeometricalNonlinearity = 'linear'
            solver.IterationsControlParameterTimeUse = False
            
            self.fem_analysis.addObject(solver)
            
        except Exception as e:
            App.Console.PrintError(f"Failed to add FEM solver: {e}\n")
    
    def run_fem_analysis(self):
        """Run FEM analysis"""
        if not self.fem_analysis:
            App.Console.PrintError("No FEM analysis to run\n")
            return False
        
        try:
            import femtools.femutils as femutils
            
            # Generate mesh if needed
            if self.mesh_object and not self.mesh_object.FemMesh:
                self.mesh_object.Proxy.execute(self.mesh_object)
            
            # Run analysis
            femutils.run_analysis(self.fem_analysis)
            
            App.Console.PrintMessage("FEM analysis completed successfully\n")
            return True
            
        except Exception as e:
            App.Console.PrintError(f"FEM analysis failed: {e}\n")
            return False
    
    def import_fem_results(self):
        """Import FEM results back to StructureTools"""
        if not self.fem_analysis:
            return
        
        try:
            # Find result objects
            result_objects = [obj for obj in self.fem_analysis.Group if 'Result' in obj.Name]
            
            for result_obj in result_objects:
                App.Console.PrintMessage(f"FEM Result available: {result_obj.Label}\n")
                # Here you would extract specific results and update StructureTools objects
                
        except Exception as e:
            App.Console.PrintError(f"Failed to import FEM results: {e}\n")


class CommandExportToFEM:
    """Command to export structural model to FEM workbench"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "..", "resources", "icons", "fem_export.svg"),
            "MenuText": "Export to FEM",
            "ToolTip": "Export structural model to FEM workbench for advanced analysis"
        }
    
    def Activated(self):
        doc = App.ActiveDocument
        if not doc:
            App.Console.PrintError("No active document\n")
            return
        
        # Find structural objects
        structural_objects = []
        for obj in doc.Objects:
            if (hasattr(obj, 'MaterialMember') or hasattr(obj, 'SectionMember') or 
                'Line' in obj.Name or 'Wire' in obj.Name):
                structural_objects.append(obj)
        
        if not structural_objects:
            App.Console.PrintMessage("No structural objects found\n")
            return
        
        # Create FEM bridge and export
        fem_bridge = FEMStructuralBridge()
        analysis = fem_bridge.export_to_fem(structural_objects)
        
        if analysis:
            App.Console.PrintMessage(f"Exported to FEM analysis: {analysis.Label}\n")
            
            # Ask user if they want to switch to FEM workbench
            try:
                from PySide import QtWidgets
                reply = QtWidgets.QMessageBox.question(None, "Switch Workbench", 
                                                     "Export complete. Switch to FEM workbench?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                
                if reply == QtWidgets.QMessageBox.Yes:
                    Gui.activateWorkbench("FemWorkbench")
            except:
                App.Console.PrintMessage("Switch to FEM workbench manually to continue\n")
        else:
            App.Console.PrintError("Failed to export to FEM\n")
    
    def IsActive(self):
        return App.ActiveDocument is not None


# Register command
Gui.addCommand("ExportToFEM", CommandExportToFEM())
