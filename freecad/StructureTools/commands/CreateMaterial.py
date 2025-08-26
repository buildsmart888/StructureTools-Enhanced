# -*- coding: utf-8 -*-
"""
CreateMaterial - Command to create material objects compatible with calc

This command provides options to create both old-style and new-style materials
that work seamlessly with the calc object for structural analysis.
"""

import FreeCAD as App
import FreeCADGui as Gui
import os
from typing import Optional

# Icon path
ICONPATH = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")


class CreateMaterialCommand:
    """Command to create structural materials compatible with calc."""
    
    def GetResources(self) -> dict:
        """Return command resources."""
        return {
            "Pixmap": os.path.join(ICONPATH, "material.svg"),
            "Accel": "Shift+M",
            "MenuText": "Create Material",
            "ToolTip": "Create a structural material object for analysis"
        }
    
    def Activated(self) -> None:
        """Execute the command."""
        doc = App.ActiveDocument
        if not doc:
            App.Console.PrintError("No active document. Create or open a document first.\n")
            return
        
        # Show material creation dialog
        try:
            from ..taskpanels.MaterialCreationPanel import MaterialCreationPanel
            panel = MaterialCreationPanel()
            Gui.Control.showDialog(panel)
        except ImportError:
            # Fallback: Create new StructuralMaterial directly
            self.create_structural_material()
    
    def create_structural_material(self, material_name: Optional[str] = None) -> object:
        """
        Create a new StructuralMaterial object.
        
        Args:
            material_name: Optional name for the material
            
        Returns:
            The created material object
        """
        doc = App.ActiveDocument
        if not doc:
            return None
        
        try:
            # Try to create new StructuralMaterial
            from ..objects.StructuralMaterial import StructuralMaterial, ViewProviderStructuralMaterial
            
            name = material_name or "StructuralMaterial"
            obj = doc.addObject("App::DocumentObjectGroupPython", name)
            
            StructuralMaterial(obj)
            ViewProviderStructuralMaterial(obj.ViewObject)
            
            # Set default properties for structural steel
            obj.MaterialStandard = "ASTM_A992"
            obj.GradeDesignation = "Gr. 50"
            obj.ModulusElasticity = "200000 MPa"
            obj.PoissonRatio = 0.30
            obj.Density = "7850 kg/m^3"
            obj.YieldStrength = "345 MPa"
            obj.UltimateStrength = "450 MPa"
            
            App.Console.PrintMessage(f"Created StructuralMaterial: {obj.Label}\n")
            
            doc.recompute()
            return obj
            
        except ImportError:
            App.Console.PrintWarning("StructuralMaterial not available. Creating basic Material.\n")
            return self.create_basic_material(material_name)
    
    def create_basic_material(self, material_name: Optional[str] = None) -> object:
        """
        Create a basic Material object (fallback).
        
        Args:
            material_name: Optional name for the material
            
        Returns:
            The created material object
        """
        doc = App.ActiveDocument
        if not doc:
            return None
        
        try:
            from ..material import Material, ViewProviderMaterial
            
            name = material_name or "Material"
            obj = doc.addObject("Part::FeaturePython", name)
            
            Material(obj)
            ViewProviderMaterial(obj.ViewObject)
            
            # Set default properties for structural steel
            obj.ModulusElasticity = "200000 MPa"
            obj.PoissonRatio = 0.30
            obj.Density = "7850 kg/m^3"
            
            App.Console.PrintMessage(f"Created Material: {obj.Label}\n")
            
            doc.recompute()
            return obj
            
        except Exception as e:
            App.Console.PrintError(f"Failed to create material: {e}\n")
            return None
    
    def IsActive(self) -> bool:
        """Return True if command can be activated."""
        return App.ActiveDocument is not None


# Register the command
Gui.addCommand("CreateMaterial", CreateMaterialCommand())


# Utility functions for programmatic material creation
def create_steel_material(name: str = "Steel", standard: str = "ASTM_A992") -> object:
    """
    Create a predefined steel material.
    
    Args:
        name: Material name
        standard: Material standard (ASTM_A992, ASTM_A36, etc.)
        
    Returns:
        The created material object
    """
    cmd = CreateMaterialCommand()
    material = cmd.create_structural_material(name)
    
    if material and hasattr(material, 'MaterialStandard'):
        material.MaterialStandard = standard
        
        # Set properties based on standard
        if standard == "ASTM_A992":
            material.YieldStrength = "345 MPa"
            material.UltimateStrength = "450 MPa"
        elif standard == "ASTM_A36":
            material.YieldStrength = "250 MPa"
            material.UltimateStrength = "400 MPa"
        elif standard == "EN_S355":
            material.YieldStrength = "355 MPa"
            material.UltimateStrength = "510 MPa"
        
        App.ActiveDocument.recompute()
    
    return material


def create_concrete_material(name: str = "Concrete", fc: float = 25.0) -> object:
    """
    Create a predefined concrete material.
    
    Args:
        name: Material name
        fc: Compressive strength in MPa
        
    Returns:
        The created material object
    """
    cmd = CreateMaterialCommand()
    material = cmd.create_structural_material(name)
    
    if material:
        material.MaterialType = "Concrete"
        material.ModulusElasticity = f"{4700 * (fc ** 0.5):.0f} MPa"  # ACI 318 formula
        material.PoissonRatio = 0.20
        material.Density = "2400 kg/m^3"
        material.CompressiveStrength = f"{fc} MPa"
        
        App.ActiveDocument.recompute()
    
    return material


def validate_material_for_calc(material_obj) -> bool:
    """
    Validate that a material object is compatible with calc.
    
    Args:
        material_obj: Material object to validate
        
    Returns:
        True if compatible, False otherwise
    """
    if not material_obj:
        return False
    
    # Check for required properties
    required_props = ['ModulusElasticity', 'PoissonRatio', 'Density', 'Name']
    
    for prop in required_props:
        if not hasattr(material_obj, prop):
            App.Console.PrintWarning(f"Material {material_obj.Label} missing property: {prop}\n")
            return False
    
    # Check if material has calc compatibility method
    if hasattr(material_obj, 'Proxy') and hasattr(material_obj.Proxy, 'get_calc_properties'):
        try:
            props = material_obj.Proxy.get_calc_properties(material_obj)
            App.Console.PrintMessage(f"Material {material_obj.Label} is calc-compatible\n")
            return True
        except Exception as e:
            App.Console.PrintWarning(f"Material {material_obj.Label} calc integration error: {e}\n")
            return False
    else:
        App.Console.PrintWarning(f"Material {material_obj.Label} lacks calc integration method\n")
        return False