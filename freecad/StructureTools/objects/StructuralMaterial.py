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
    
    def _ensure_property(self, obj, type_name: str, prop_name: str, group: str, doc: str = "", readonly: bool = False) -> None:
        """
        Ensure a property exists on the object, creating it if necessary.
        
        Args:
            obj: The DocumentObject
            type_name: Property type (e.g., "App::PropertyStringList")
            prop_name: Property name
            group: Property group
            doc: Property documentation
            readonly: Whether the property should be read-only
        """
        if not hasattr(obj, prop_name):
            try:
                obj.addProperty(type_name, prop_name, group, doc)
                if readonly:
                    obj.setEditorMode(prop_name, 1)  # 1 = read-only in Property Editor
            except Exception:
                # Property might already exist, continue anyway
                pass
    
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
        obj.MaterialStandard = "ASTM_A992"  # Set a default, will be updated next
        
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
        
        # Initialize ValidationWarnings property to prevent AttributeError
        self._ensure_property(obj, "App::PropertyStringList", "ValidationWarnings", "Validation",
                             "Current validation warnings")
        obj.ValidationWarnings = []
        
        # Update properties based on selected standard
        self._update_standard_properties(obj)
    
    def _as_kg_per_m3(self, val) -> float:
        """
        Helper function to normalize density values to kg/m³.
        
        Args:
            val: Density value (can be Quantity, string, or float)
            
        Returns:
            float: Density in kg/m³
        """
        try:
            # If it's already a FreeCAD Quantity with getValueAs method
            if hasattr(val, 'getValueAs'):
                return float(val.getValueAs('kg/m^3'))
            
            # If it's a string or numeric value, convert via Units.parseQuantity
            from FreeCAD import Units
            # Handle scientific notation and different unit formats properly
            if isinstance(val, str):
                # Use FreeCAD's parseQuantity to handle various unit formats
                q = Units.parseQuantity(val)
                return float(q.getValueAs('kg/m^3'))
            
            # For numeric values, create a Quantity and convert
            q = Units.Quantity(str(val))
            return float(q.getValueAs('kg/m^3'))
        except Exception as e:
            raise Exception(f"Could not convert {val} to kg/m³: {str(e)}")

    def _calculate_shear_modulus(self, obj) -> None:
        """Calculate shear modulus from elastic modulus and Poisson ratio."""
        if not (hasattr(obj, 'ModulusElasticity') and hasattr(obj, 'PoissonRatio')):
            return
        
        try:
            # Get E in MPa and nu as float
            E = obj.ModulusElasticity.getValueAs('MPa')
            nu = obj.PoissonRatio
            G_MPa = float(E) / (2 * (1 + nu))
            
            # Update shear modulus with proper Quantity formatting
            from FreeCAD import Units
            obj.ShearModulus = Units.Quantity(f"{G_MPa:.0f} MPa")
            
        except (AttributeError, ValueError, TypeError) as e:
            App.Console.PrintWarning(f"Could not calculate shear modulus: {e}\n")

    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and dependencies.
        
        Args:
            obj: Material DocumentObject
            prop: Changed property name
        """
        try:
            # Import validation after FreeCAD is available
            from ..utils.validation import StructuralValidator
            from ..utils.exceptions import ValidationError
            
            validator = StructuralValidator()
            
            # Handle MaterialStandard changes
            if prop == 'MaterialStandard':
                App.Console.PrintMessage(f"Material standard changed to {obj.MaterialStandard}\n")
                self._update_standard_properties(obj)
            
            # Validate changed property
            elif prop == 'PoissonRatio':
                if hasattr(obj, 'PoissonRatio'):
                    nu = obj.PoissonRatio
                    if not (0.0 <= nu <= 0.5):
                        App.Console.PrintError(
                            f"Invalid Poisson ratio {nu:.3f}. Must be between 0.0 and 0.5\n"
                        )
                        obj.PoissonRatio = 0.3  # Reset to default
            
            elif prop == 'ModulusElasticity':
                if hasattr(obj, 'ModulusElasticity'):
                    try:
                        E = validator.get_property_value(obj.ModulusElasticity, 'Pa')
                        if E <= 0:
                            App.Console.PrintError("Elastic modulus must be positive\n")
                    except Exception as e:
                        App.Console.PrintError(f"Invalid elastic modulus: {str(e)}\n")
            
            elif prop == 'Density':
                if hasattr(obj, 'Density'):
                    try:
                        # Use the new helper function to normalize density to kg/m³
                        rho_kg_m3 = self._as_kg_per_m3(obj.Density)
                        if rho_kg_m3 <= 0:
                            App.Console.PrintError("Density must be positive\n")
                    except Exception as e:
                        App.Console.PrintError(f"Invalid density: {str(e)}\n")
            
            # Full validation on critical changes
            if prop in ['ModulusElasticity', 'PoissonRatio', 'YieldStrength', 'UltimateStrength']:
                try:
                    warnings = validator.validate_material_properties(obj)
                    if warnings:
                        # Ensure ValidationWarnings property exists
                        self._ensure_property(obj, "App::PropertyStringList", "ValidationWarnings", "Validation",
                                            "Current validation warnings")
                        
                        try:
                            obj.ValidationWarnings = warnings
                        except Exception:
                            # If we can't set the property, just continue
                            pass
                        for warning in warnings:
                            App.Console.PrintWarning(f"Material warning: {warning}\n")
                    else:
                        # Ensure ValidationWarnings property exists
                        self._ensure_property(obj, "App::PropertyStringList", "ValidationWarnings", "Validation",
                                            "Current validation warnings")
                        try:
                            obj.ValidationWarnings = []
                        except Exception:
                            # If we can't set the property, just continue
                            pass
                except ValidationError as e:
                    App.Console.PrintError(f"Material validation error: {str(e)}\n")
                except Exception as e:
                    App.Console.PrintWarning(f"Error during material validation: {str(e)}\n")
        
        except ImportError:
            # Fallback validation without utils
            if prop == 'PoissonRatio' and hasattr(obj, 'PoissonRatio'):
                nu = obj.PoissonRatio
                if not (0.0 <= nu <= 0.5):
                    App.Console.PrintError(f"Invalid Poisson ratio {nu:.3f}\n")
                    obj.PoissonRatio = 0.3
        except Exception as e:
            App.Console.PrintWarning(f"Error in material property validation: {str(e)}\n")
    
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
            
            # Debug the standard and properties
            App.Console.PrintMessage(f"Updating properties for standard: {standard}\n")
            App.Console.PrintMessage(f"Available properties: {list(props.keys())}\n")
            
            # Check for concrete vs steel material type
            if 'CompressiveStrength' in props:
                # Set material type to Concrete for concrete materials
                if hasattr(obj, 'MaterialType'):
                    obj.MaterialType = 'Concrete'
                    App.Console.PrintMessage(f"Setting material type to Concrete\n")
            
            # Update properties from standard
            for prop_name, value in props.items():
                if hasattr(obj, prop_name):
                    App.Console.PrintMessage(f"Setting {prop_name} = {value}\n")
                    setattr(obj, prop_name, value)
            
            # Force update critical properties to ensure they're set correctly
            if 'Density' in props and hasattr(obj, 'Density'):
                obj.Density = props['Density']
                App.Console.PrintMessage(f"Forcing update of Density to {props['Density']}\n")
                
            if 'ModulusElasticity' in props and hasattr(obj, 'ModulusElasticity'):
                obj.ModulusElasticity = props['ModulusElasticity']
                App.Console.PrintMessage(f"Forcing update of ModulusElasticity to {props['ModulusElasticity']}\n")
                
            if 'PoissonRatio' in props and hasattr(obj, 'PoissonRatio'):
                obj.PoissonRatio = props['PoissonRatio']
                App.Console.PrintMessage(f"Forcing update of PoissonRatio to {props['PoissonRatio']}\n")
                
            if 'YieldStrength' in props and hasattr(obj, 'YieldStrength'):
                obj.YieldStrength = props['YieldStrength']
                App.Console.PrintMessage(f"Forcing update of YieldStrength to {props['YieldStrength']}\n")
                
            if 'UltimateStrength' in props and hasattr(obj, 'UltimateStrength'):
                obj.UltimateStrength = props['UltimateStrength']
                App.Console.PrintMessage(f"Forcing update of UltimateStrength to {props['UltimateStrength']}\n")
            
            # Special handling for concrete materials
            if 'CompressiveStrength' in props:
                # For concrete, set YieldStrength and UltimateStrength to CompressiveStrength
                # as these are not typically used for concrete but needed for compatibility
                if hasattr(obj, 'CompressiveStrength') and hasattr(obj, 'YieldStrength'):
                    obj.YieldStrength = props['CompressiveStrength']
                    App.Console.PrintMessage(f"Setting YieldStrength to CompressiveStrength: {props['CompressiveStrength']}\n")
                if hasattr(obj, 'CompressiveStrength') and hasattr(obj, 'UltimateStrength'):
                    obj.UltimateStrength = props['CompressiveStrength']
                    App.Console.PrintMessage(f"Setting UltimateStrength to CompressiveStrength: {props['CompressiveStrength']}\n")
            
            App.Console.PrintMessage(
                f"Updated material properties for standard: {standard}\n"
            )
            self._clear_validation_warnings(obj)
    
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
        # Ensure ValidationWarnings property exists
        self._ensure_property(obj, "App::PropertyStringList", "ValidationWarnings", "Validation",
                            "Current validation warnings")
        # Initialize the property if it doesn't exist
        if not hasattr(obj, "ValidationWarnings"):
            try:
                obj.ValidationWarnings = []
            except Exception:
                pass

        # Ensure ValidationWarnings is a list-like container
        try:
            warnings = list(obj.ValidationWarnings)
        except Exception:
            warnings = []

        if warning not in warnings:
            warnings.append(warning)
            try:
                obj.ValidationWarnings = warnings
            except Exception:
                # If we can't set the property, just continue
                pass
    
    def _remove_validation_warning(self, obj, warning_key: str) -> None:
        """Remove validation warnings containing the key."""
        if not hasattr(obj, 'ValidationWarnings'):
            return
        try:
            existing = list(obj.ValidationWarnings)
        except Exception:
            existing = []

        warnings = [w for w in existing if warning_key not in str(w).lower()]
        obj.ValidationWarnings = warnings
    
    def _clear_validation_warnings(self, obj) -> None:
        """Clear all validation warnings."""
        if hasattr(obj, 'ValidationWarnings'):
            try:
                obj.ValidationWarnings = []
            except Exception:
                # If we can't set the property, just continue
                pass
    
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
            try:
                obj.addProperty("App::PropertyMap", "FreeCADMaterialCard", "Internal",
                               "FreeCAD material card data")
            except Exception:
                # Property might already exist, continue anyway
                pass
            try:
                obj.FreeCADMaterialCard = material_dict
            except Exception:
                # If we can't set the property, just continue
                pass
            
        except Exception as e:
            App.Console.PrintWarning(f"Could not update FreeCAD material: {e}\n")
    
    def get_calc_properties(self, obj, unit_length: str = 'm', unit_force: str = 'kN') -> dict:
        """
        Get material properties formatted for calc integration.
        
        Args:
            obj: Material DocumentObject
            unit_length: Target length unit (m, mm, etc.)
            unit_force: Target force unit (kN, N, etc.)
            
        Returns:
            Dictionary with material properties for FEModel3D
        """
        try:
            # Convert density from kg/m³ to force/volume units
            density_kg_m3 = obj.Density.getValueAs('kg/m^3')
            density_kn_m3 = density_kg_m3 * 9.80665 / 1000  # Convert to kN/m³
            density = density_kn_m3  # Will be converted to target units by calc
            
            # Get elastic properties in target units
            E = obj.ModulusElasticity.getValueAs(f'{unit_force}/{unit_length}^2')
            nu = obj.PoissonRatio
            G = E / (2 * (1 + nu))  # Calculate shear modulus
            
            return {
                'name': obj.Name,
                'E': float(E),
                'G': float(G),
                'nu': float(nu),
                'density': float(density),
                'unit_system': f'{unit_force}-{unit_length}'
            }
            
        except Exception as e:
            App.Console.PrintError(f"Error getting calc properties for material {obj.Name}: {e}\n")
            # Return safe defaults
            return {
                'name': obj.Name if hasattr(obj, 'Name') else 'Material',
                'E': 200000.0,  # MPa
                'G': 77000.0,   # MPa  
                'nu': 0.3,
                'density': 7850.0,  # kg/m³
                'unit_system': f'{unit_force}-{unit_length}'
            }


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