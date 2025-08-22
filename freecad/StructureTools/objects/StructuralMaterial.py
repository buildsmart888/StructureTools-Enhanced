# -*- coding: utf-8 -*-
"""
StructuralMaterial - Professional material object with validation and standards

This module provides a comprehensive material object for structural engineering
with built-in validation, material standards, and integration with design codes.
"""

import FreeCAD as App
import FreeCADGui as Gui
from typing import Dict, Any, Optional
import os

# Import material standards data
from ..data.MaterialStandards import MATERIAL_STANDARDS


class StructuralMaterial:
    """
    Custom Document Object for structural materials with validation and standards compliance.
    
    This class provides enhanced material properties beyond basic FreeCAD materials,
    including design code integration, temperature effects, and automated validation.
    """
    
    def __init__(self, obj):
        """
        Initialize StructuralMaterial object.
        
        Args:
            obj: FreeCAD DocumentObject to be enhanced
        """
        self.Type = "StructuralMaterial"
        obj.Proxy = self
        
        # Basic identification
        obj.addProperty("App::PropertyString", "MaterialType", "Identification", 
                       "Material type classification").MaterialType = "Steel"
        
        # Material standards and codes
        obj.addProperty("App::PropertyEnumeration", "MaterialStandard", "Standard", 
                       "Material standard (ASTM, EN, etc.)")
        obj.MaterialStandard = list(MATERIAL_STANDARDS.keys())
        obj.MaterialStandard = "ASTM_A992"
        
        obj.addProperty("App::PropertyString", "GradeDesignation", "Standard",
                       "Material grade designation").GradeDesignation = "Gr. 50"
        
        # Mechanical properties with validation
        obj.addProperty("App::PropertyPressure", "ModulusElasticity", "Mechanical", 
                       "Young's modulus E")
        obj.ModulusElasticity = "200000 MPa"
        
        obj.addProperty("App::PropertyPressure", "ShearModulus", "Mechanical",
                       "Shear modulus G (calculated or specified)")
        
        obj.addProperty("App::PropertyFloat", "PoissonRatio", "Mechanical", 
                       "Poisson's ratio (0.0-0.5)")
        obj.PoissonRatio = 0.30
        
        obj.addProperty("App::PropertyDensity", "Density", "Physical", 
                       "Material density")
        obj.Density = "7850 kg/m^3"
        
        # Strength properties for design
        obj.addProperty("App::PropertyPressure", "YieldStrength", "Strength", 
                       "Yield strength Fy")
        obj.YieldStrength = "345 MPa"
        
        obj.addProperty("App::PropertyPressure", "UltimateStrength", "Strength", 
                       "Ultimate tensile strength Fu")
        obj.UltimateStrength = "450 MPa"
        
        obj.addProperty("App::PropertyPressure", "CompressiveStrength", "Strength",
                       "Compressive strength (for concrete)")
        
        # Temperature-dependent properties
        obj.addProperty("App::PropertyFloat", "ThermalExpansion", "Thermal", 
                       "Coefficient of thermal expansion (1/°C)")
        obj.ThermalExpansion = 12e-6
        
        obj.addProperty("App::PropertyFloat", "ReferenceTemperature", "Thermal",
                       "Reference temperature (°C)")
        obj.ReferenceTemperature = 20.0
        
        # Fatigue and durability
        obj.addProperty("App::PropertyPressure", "FatigueLimit", "Fatigue", 
                       "Endurance limit for fatigue analysis")
        
        obj.addProperty("App::PropertyInteger", "FatigueCategory", "Fatigue",
                       "AISC fatigue category (A=1, B=2, C=3, etc.)")
        obj.FatigueCategory = 2  # Category B
        
        # Quality and certification
        obj.addProperty("App::PropertyString", "CertificationLevel", "Quality",
                       "Material certification level")
        obj.CertificationLevel = "Mill Certified"
        
        obj.addProperty("App::PropertyString", "TestingStandard", "Quality", 
                       "Testing standard reference")
        obj.TestingStandard = "ASTM A6"
        
        # Cost and sustainability
        obj.addProperty("App::PropertyFloat", "UnitCost", "Economics",
                       "Cost per unit weight or volume")
        
        obj.addProperty("App::PropertyFloat", "CarbonFootprint", "Sustainability",
                       "Carbon footprint (kg CO2 equivalent)")
        
        # Advanced properties for analysis
        obj.addProperty("App::PropertyBool", "IsTemperatureDependent", "Advanced",
                       "Enable temperature-dependent properties")
        obj.IsTemperatureDependent = False
        
        obj.addProperty("App::PropertyBool", "IsNonlinear", "Advanced", 
                       "Enable nonlinear material behavior")
        obj.IsNonlinear = False
        
        # Internal tracking
        obj.addProperty("App::PropertyString", "LastValidated", "Internal",
                       "Last validation timestamp")
        
        obj.addProperty("App::PropertyStringList", "ValidationWarnings", "Internal",
                       "Current validation warnings")
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and dependencies.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        if prop == "PoissonRatio":
            self._validate_poisson_ratio(obj)
        elif prop == "MaterialStandard":
            self._update_standard_properties(obj)
        elif prop == "ModulusElasticity" or prop == "PoissonRatio":
            self._calculate_shear_modulus(obj)
        elif prop in ["YieldStrength", "UltimateStrength"]:
            self._validate_strength_properties(obj)
    
    def _validate_poisson_ratio(self, obj) -> None:
        """Validate Poisson ratio is within physical bounds."""
        if not hasattr(obj, 'PoissonRatio'):
            return
            
        if obj.PoissonRatio < 0.0 or obj.PoissonRatio > 0.5:
            App.Console.PrintWarning(
                f"Invalid Poisson ratio ({obj.PoissonRatio}): must be 0.0-0.5. "
                f"Resetting to 0.30\n"
            )
            obj.PoissonRatio = 0.30
            self._add_validation_warning(obj, "Poisson ratio out of range - reset to 0.30")
    
    def _update_standard_properties(self, obj) -> None:
        """Auto-populate properties based on material standard."""
        if not hasattr(obj, 'MaterialStandard'):
            return
        
        standard = obj.MaterialStandard
        if standard in MATERIAL_STANDARDS:
            props = MATERIAL_STANDARDS[standard]
            
            # Update properties from standard
            for prop_name, value in props.items():
                if hasattr(obj, prop_name):
                    setattr(obj, prop_name, value)
            
            App.Console.PrintMessage(
                f"Updated material properties for standard: {standard}\n"
            )
            self._clear_validation_warnings(obj)
    
    def _calculate_shear_modulus(self, obj) -> None:
        """Calculate shear modulus from elastic modulus and Poisson ratio."""
        if not (hasattr(obj, 'ModulusElasticity') and hasattr(obj, 'PoissonRatio')):
            return
        
        try:
            E = obj.ModulusElasticity.getValueAs('MPa')
            nu = obj.PoissonRatio
            G = E / (2 * (1 + nu))
            
            # Update shear modulus
            obj.ShearModulus = f"{G:.0f} MPa"
            
        except (AttributeError, ValueError) as e:
            App.Console.PrintWarning(f"Could not calculate shear modulus: {e}\n")
    
    def _validate_strength_properties(self, obj) -> None:
        """Validate strength property relationships."""
        if not (hasattr(obj, 'YieldStrength') and hasattr(obj, 'UltimateStrength')):
            return
        
        try:
            Fy = obj.YieldStrength.getValueAs('MPa')
            Fu = obj.UltimateStrength.getValueAs('MPa')
            
            if Fy >= Fu:
                warning = f"Yield strength ({Fy} MPa) should be less than ultimate strength ({Fu} MPa)"
                self._add_validation_warning(obj, warning)
                App.Console.PrintWarning(warning + "\n")
            else:
                self._remove_validation_warning(obj, "strength_relationship")
                
        except (AttributeError, ValueError) as e:
            App.Console.PrintWarning(f"Could not validate strength properties: {e}\n")
    
    def _add_validation_warning(self, obj, warning: str) -> None:
        """Add a validation warning to the object."""
        if not hasattr(obj, 'ValidationWarnings'):
            obj.ValidationWarnings = []
        
        warnings = list(obj.ValidationWarnings)
        if warning not in warnings:
            warnings.append(warning)
            obj.ValidationWarnings = warnings
    
    def _remove_validation_warning(self, obj, warning_key: str) -> None:
        """Remove validation warnings containing the key."""
        if not hasattr(obj, 'ValidationWarnings'):
            return
        
        warnings = [w for w in obj.ValidationWarnings if warning_key not in w.lower()]
        obj.ValidationWarnings = warnings
    
    def _clear_validation_warnings(self, obj) -> None:
        """Clear all validation warnings."""
        if hasattr(obj, 'ValidationWarnings'):
            obj.ValidationWarnings = []
    
    def execute(self, obj) -> None:
        """
        Update material properties and validate consistency.
        
        Args:
            obj: The DocumentObject being executed
        """
        # Update derived properties
        self._calculate_shear_modulus(obj)
        
        # Validate all properties
        self._validate_poisson_ratio(obj)
        self._validate_strength_properties(obj)
        
        # Update material database integration
        self._update_freecad_material(obj)
        
        # Update timestamp
        from datetime import datetime
        obj.LastValidated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _update_freecad_material(self, obj) -> None:
        """Sync with FreeCAD material system."""
        try:
            # Create or update FreeCAD material card
            material_dict = {
                'Name': obj.Label,
                'Density': str(obj.Density),
                'YoungsModulus': str(obj.ModulusElasticity),
                'PoissonRatio': str(obj.PoissonRatio),
                'YieldStrength': str(obj.YieldStrength),
                'UltimateStrength': str(obj.UltimateStrength)
            }
            
            # Store for use by other workbenches
            obj.addProperty("App::PropertyMap", "FreeCADMaterialCard", "Internal",
                           "FreeCAD material card data")
            obj.FreeCADMaterialCard = material_dict
            
        except Exception as e:
            App.Console.PrintWarning(f"Could not update FreeCAD material: {e}\n")


class ViewProviderStructuralMaterial:
    """
    ViewProvider for StructuralMaterial with enhanced visualization and editing.
    """
    
    def __init__(self, vobj):
        """Initialize ViewProvider."""
        vobj.Proxy = self
        self.Object = vobj.Object
        
        # Visualization properties
        vobj.addProperty("App::PropertyBool", "ShowValidationStatus", "Display",
                        "Show validation status in tree")
        vobj.ShowValidationStatus = True
    
    def getIcon(self) -> str:
        """
        Return dynamic icon based on material type and validation status.
        
        Returns:
            Path to appropriate icon file
        """
        if not hasattr(self.Object, 'MaterialStandard'):
            return self._get_icon_path("material_unknown.svg")
        
        # Check validation status
        has_warnings = (hasattr(self.Object, 'ValidationWarnings') and 
                       len(self.Object.ValidationWarnings) > 0)
        
        material_standard = getattr(self.Object, 'MaterialStandard', 'Custom')
        
        if has_warnings:
            return self._get_icon_path("material_warning.svg")
        elif 'ASTM' in material_standard:
            return self._get_icon_path("material_steel_astm.svg")
        elif 'EN' in material_standard:
            return self._get_icon_path("material_steel_en.svg")
        elif 'Concrete' in getattr(self.Object, 'MaterialType', ''):
            return self._get_icon_path("material_concrete.svg")
        else:
            return self._get_icon_path("material_custom.svg")
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icon_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")
        return os.path.join(icon_dir, icon_name)
    
    def setEdit(self, vobj, mode: int) -> bool:
        """
        Open custom task panel for material editing.
        
        Args:
            vobj: ViewObject being edited
            mode: Edit mode
            
        Returns:
            True if edit mode started successfully
        """
        if mode == 0:
            from ..taskpanels.MaterialTaskPanel import MaterialTaskPanel
            self.panel = MaterialTaskPanel(vobj.Object)
            Gui.Control.showDialog(self.panel)
            return True
        return False
    
    def unsetEdit(self, vobj, mode: int) -> bool:
        """
        Close material editing panel.
        
        Args:
            vobj: ViewObject being edited
            mode: Edit mode
            
        Returns:
            True if edit mode ended successfully
        """
        Gui.Control.closeDialog()
        return True
    
    def doubleClicked(self, vobj) -> bool:
        """Handle double-click to open properties panel."""
        return self.setEdit(vobj, 0)
    
    def getDisplayModes(self, vobj) -> list:
        """Return available display modes."""
        return ["Standard"]
    
    def getDefaultDisplayMode(self) -> str:
        """Return default display mode."""
        return "Standard"
    
    def setDisplayMode(self, mode: str) -> str:
        """Set display mode."""
        return mode