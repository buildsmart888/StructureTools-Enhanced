# -*- coding: utf-8 -*-
"""
Global Units Settings for StructureTools

Provides a unified system for switching between SI units and Thai units
across all StructureTools functionality.
"""

import FreeCAD as App
import os
import json

class UnitsManager:
    """Global units manager for StructureTools"""
    
    # Units systems
    SI_UNITS = "SI"  # kN-m-MPa (Metric engineering)
    US_UNITS = "US"  # kip-ft-ksi (US Customary)
    THAI_UNITS = "THAI"  # kgf-cm-ksc (Thai Traditional)
    
    # Default settings with 3-level structure
    DEFAULT_SETTINGS = {
        "unit_system": SI_UNITS,
        
        # Base units (Level 2: Category override)
        "base_units": {
            "length": "m",
            "force": "kN", 
            "stress": "MPa",
            "moment": "kN·m",
            "area": "m²",
            "volume": "m³",
            "unit_weight": "kN/m³",
            "density": "kg/m³"
        },
        
        # Report units (Level 3: Report override)
        "report_units": {
            "length": "m",
            "force": "kN",
            "stress": "MPa", 
            "moment": "kN·m",
            "area": "m²",
            "volume": "m³",
            "unit_weight": "kN/m³",
            "density": "kg/m³"
        },
        
        # Display options
        "show_both_units": True,
        "auto_detect_material": True,
        "mixed_unit_mode": False,
        
        # Precision settings
        "precision": {
            "length": 3,
            "force": 2,
            "stress": 1,
            "moment": 2,
            "area": 4,
            "volume": 6,
            "unit_weight": 1,
            "density": 0
        }
    }
    
    # Unit system presets
    UNIT_PRESETS = {
        SI_UNITS: {
            "name": "SI (Metric Engineering)",
            "description": "kN-m-MPa system for international use",
            "base_units": {
                "length": "m",
                "force": "kN",
                "stress": "MPa", 
                "moment": "kN·m",
                "area": "m²",
                "volume": "m³",
                "unit_weight": "kN/m³",
                "density": "kg/m³"
            }
        },
        US_UNITS: {
            "name": "US Customary (Imperial)",
            "description": "kip-ft-ksi system for ACI 318-19",
            "base_units": {
                "length": "ft",
                "force": "kip",
                "stress": "ksi",
                "moment": "kip·ft", 
                "area": "ft²",
                "volume": "ft³",
                "unit_weight": "pcf",
                "density": "pcf"
            }
        },
        THAI_UNITS: {
            "name": "Thai Traditional",
            "description": "kgf-cm-ksc system for Thai engineering",
            "base_units": {
                "length": "cm",
                "force": "kgf",
                "stress": "ksc",
                "moment": "kgf·cm",
                "area": "cm²", 
                "volume": "cm³",
                "unit_weight": "kgf/cm³",
            }
        }
    }
    
    # Conversion factors (to SI base units)
    CONVERSION_FACTORS = {
        # Length conversions (to meters)
        "length": {
            "mm": 0.001,
            "cm": 0.01, 
            "m": 1.0,
            "in": 0.0254,
            "ft": 0.3048
        },
        
        # Force conversions (to Newtons)
        "force": {
            "N": 1.0,
            "kN": 1000.0,
            "kgf": 9.80665,
            "tf": 9806.65,
            "lb": 4.44822,
            "kip": 4448.22
        },
        
        # Stress conversions (to Pascals) 
        "stress": {
            "Pa": 1.0,
            "kPa": 1000.0,
            "MPa": 1000000.0,
            "ksc": 98066.5,  # 1 ksc = 98066.5 Pa
            "psi": 6894.76,
            "ksi": 6894760.0
        },
        
        # Unit weight conversions (to N/m³)
        "unit_weight": {
            "N/m³": 1.0,
            "kN/m³": 1000.0,
            "kgf/m³": 9.80665,
            "pcf": 157.087  # pounds per cubic foot
        },
        
        # Density conversions (to kg/m³)
        "density": {
            "kg/m³": 1.0,
            "g/cm³": 1000.0,
            "pcf": 16.0185  # pounds per cubic foot to kg/m³
        }
    }
    
    # Engineering material constants
    ENGINEERING_CONSTANTS = {
        "concrete": {
            "SI": {
                "fc_normal": [21, 28, 35, 42],  # MPa
                "unit_weight": 24.0,  # kN/m³
                "modulus_factor": 4700  # E = 4700*sqrt(fc) in MPa
            },
            "US": {
                "fc_normal": [3000, 4000, 5000, 6000],  # psi
                "unit_weight": 150.0,  # pcf
                "modulus_factor": 57000  # E = 57000*sqrt(fc) in psi
            },
            "THAI": {
                "fc_normal": [175, 210, 240, 280, 350],  # ksc (Fc175, Fc210, etc.)
                "unit_weight": 2400.0,  # kg/m³
                "modulus_factor": 478.7  # E = 478.7*sqrt(fc) in ksc
            }
        },
        
        "steel": {
            "SI": {
                "fy_grades": [250, 300, 400, 460],  # MPa (SD30, SD40, etc.)
                "modulus": 200000,  # MPa
                "unit_weight": 78.5  # kN/m³
            },
            "US": {
                "fy_grades": [36, 50, 60, 65],  # ksi (Grade 36, 50, etc.)
                "modulus": 29000,  # ksi
                "unit_weight": 490  # pcf
            },
            "THAI": {
                "fy_grades": [2550, 3060, 4080, 4690],  # ksc (SD30=3060, SD40=4080)
                "modulus": 2039000,  # ksc (200 GPa)
                "unit_weight": 7850  # kg/m³
            }
        }
    }
    
    def __init__(self):
        """Initialize units manager"""
        self.settings_file = os.path.join(
            os.path.dirname(__file__), 
            "..", "..", "..", "structuretools_units_settings.json"
        )
        self.settings = self.load_settings()
        
        # Import Thai converter
        try:
            from .universal_thai_units import UniversalThaiUnits
            self.thai_converter = UniversalThaiUnits()
            self.thai_available = True
        except ImportError:
            self.thai_converter = None
            self.thai_available = False
    
    def load_settings(self):
        """Load units settings from file"""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                # Merge with defaults
                merged = self.DEFAULT_SETTINGS.copy()
                merged.update(settings)
                return merged
        except Exception as e:
            App.Console.PrintWarning(f"Warning loading units settings: {e}\n")
        
        return self.DEFAULT_SETTINGS.copy()
    
    def save_settings(self):
        """Save units settings to file"""
        try:
            os.makedirs(os.path.dirname(self.settings_file), exist_ok=True)
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            App.Console.PrintWarning(f"Warning saving units settings: {e}\n")
    
    def get_unit_system(self):
        """Get current unit system"""
        return self.settings.get("unit_system", self.SI_UNITS)
    
    def set_unit_system(self, system):
        """Set unit system and apply preset"""
        if system in self.UNIT_PRESETS:
            self.settings["unit_system"] = system
            # Apply preset base units
            preset = self.UNIT_PRESETS[system]
            self.settings["base_units"].update(preset["base_units"])
            self.save_settings()
            App.Console.PrintMessage(f"Unit system set to: {preset['name']}\n")
        else:
            App.Console.PrintError(f"Invalid unit system: {system}\n")
    
    def get_base_unit(self, unit_type):
        """Get base unit for a specific type"""
        return self.settings["base_units"].get(unit_type, "")
    
    def get_report_unit(self, unit_type):
        """Get report unit for a specific type"""
        return self.settings["report_units"].get(unit_type, self.get_base_unit(unit_type))
    
    def set_base_unit(self, unit_type, unit):
        """Set base unit for a specific type (Level 2 override)"""
        self.settings["base_units"][unit_type] = unit
        self.save_settings()
    
    def set_report_unit(self, unit_type, unit):
        """Set report unit for a specific type (Level 3 override)"""
        self.settings["report_units"][unit_type] = unit
        self.save_settings()
    
    def set_category_override(self, category, system):
        """Set category-level override using preset system"""
        if system in self.UNIT_PRESETS and category in self.UNIT_PRESETS[system]["base_units"]:
            unit = self.UNIT_PRESETS[system]["base_units"][category]
            self.set_base_unit(category, unit)
        else:
            raise ValueError(f"Invalid category '{category}' or system '{system}'")
    
    def set_report_override(self, category, system):
        """Set report-level override using preset system"""
        if system in self.UNIT_PRESETS and category in self.UNIT_PRESETS[system]["base_units"]:
            unit = self.UNIT_PRESETS[system]["base_units"][category]
            self.set_report_unit(category, unit)
        else:
            raise ValueError(f"Invalid category '{category}' or system '{system}'")
    
    def clear_category_overrides(self):
        """Clear all category overrides (reset to system defaults)"""
        system = self.get_unit_system()
        if system in self.UNIT_PRESETS:
            preset = self.UNIT_PRESETS[system]
            self.settings["base_units"] = preset["base_units"].copy()
            self.save_settings()
    
    def clear_report_overrides(self):
        """Clear all report overrides"""
        self.settings["report_units"] = {}
        self.save_settings()
    
    def is_thai_units(self):
        """Check if Thai units system is active"""
        return self.get_unit_system() == self.THAI_UNITS
    
    def is_si_units(self):
        """Check if SI units system is active"""
        return self.get_unit_system() == self.SI_UNITS
    
    def is_us_units(self):
        """Check if US units system is active"""
        return self.get_unit_system() == self.US_UNITS
    
    def show_both_units(self):
        """Check if both units should be shown"""
        return self.settings.get("show_both_units", True)
    
    def convert_value(self, value, from_unit, to_unit, unit_type):
        """Universal unit conversion"""
        if from_unit == to_unit:
            return value
        
        # Get conversion factors for this unit type
        factors = self.CONVERSION_FACTORS.get(unit_type, {})
        
        if from_unit not in factors or to_unit not in factors:
            App.Console.PrintWarning(f"Unknown units: {from_unit} or {to_unit} for {unit_type}\n")
            return value
        
        # Convert: value -> SI base -> target unit
        si_value = value * factors[from_unit]
        target_value = si_value / factors[to_unit]
        
        return target_value
    
    def convert_to_base_units(self, value, from_unit, unit_type):
        """Convert value to current base units"""
        base_unit = self.get_base_unit(unit_type)
        return self.convert_value(value, from_unit, base_unit, unit_type)
    
    def convert_to_report_units(self, value, from_unit, unit_type):
        """Convert value to report units"""
        report_unit = self.get_report_unit(unit_type)
        return self.convert_value(value, from_unit, report_unit, unit_type)
    
    def get_precision(self, unit_type):
        """Get precision for unit type"""
        return self.settings["precision"].get(unit_type, 2)
    
    def format_force(self, value_n, material_type=None, use_report_units=False):
        """Format force value according to current units"""
        if not value_n:
            return "0"
        
        target_unit = self.get_report_unit("force") if use_report_units else self.get_base_unit("force")
        converted_value = self.convert_value(value_n, "N", target_unit, "force")
        precision = self.get_precision("force")
        
        # Format large values nicely
        if abs(converted_value) >= 1000:
            if target_unit in ["kN", "kip"]:
                display_value = converted_value
            else:
                display_value = converted_value / 1000
                if target_unit == "kgf":
                    target_unit = "tf"
                elif target_unit == "lb":
                    target_unit = "kip" 
        else:
            display_value = converted_value
        
        formatted = f"{display_value:.{precision}f} {target_unit}"
        
        # Show both units if enabled
        if self.show_both_units() and not use_report_units:
            si_unit = "kN"
            si_value = self.convert_value(value_n, "N", si_unit, "force")
            if target_unit != si_unit:
                formatted += f" ({si_value:.{precision}f} {si_unit})"
        
        return formatted
    
    def format_stress(self, value_pa, material_type=None, use_report_units=False):
        """Format stress/pressure value according to current units"""
        if not value_pa:
            return "0"
        
        target_unit = self.get_report_unit("stress") if use_report_units else self.get_base_unit("stress")
        converted_value = self.convert_value(value_pa, "Pa", target_unit, "stress")
        precision = self.get_precision("stress")
        
        formatted = f"{converted_value:.{precision}f} {target_unit}"
        
        # Show both units if enabled
        if self.show_both_units() and not use_report_units:
            si_unit = "MPa"
            si_value = self.convert_value(value_pa, "Pa", si_unit, "stress")
            if target_unit != si_unit:
                formatted += f" ({si_value:.{precision}f} {si_unit})"
        
        return formatted
    
    def format_modulus(self, value_pa, material_type=None, use_report_units=False):
        """Format elastic modulus according to current units"""
        if not value_pa:
            return "0"
        
        target_unit = self.get_report_unit("stress") if use_report_units else self.get_base_unit("stress")
        converted_value = self.convert_value(value_pa, "Pa", target_unit, "stress")
        
        # Format in appropriate scale (GPa, ksi, etc.)
        if target_unit == "MPa" and converted_value >= 1000:
            display_value = converted_value / 1000
            display_unit = "GPa"
        elif target_unit == "ksc" and converted_value >= 1000:
            display_value = converted_value / 1000
            display_unit = "k ksc"
        elif target_unit == "ksi" and converted_value >= 1000:
            display_value = converted_value / 1000  
            display_unit = "Msi"
        else:
            display_value = converted_value
            display_unit = target_unit
        
        precision = 0 if display_value >= 1000 else 1
        formatted = f"{display_value:.{precision}f} {display_unit}"
        
        # Show both units if enabled
        if self.show_both_units() and not use_report_units:
            si_value = self.convert_value(value_pa, "Pa", "MPa", "stress")
            if si_value >= 1000:
                si_display = f"{si_value/1000:.0f} GPa"
            else:
                si_display = f"{si_value:.0f} MPa"
            
            if target_unit not in ["MPa", "Pa"]:
                formatted += f" ({si_display})"
        
        return formatted
    
    def format_length(self, value_m, use_report_units=False):
        """Format length value according to current units"""
        if not value_m:
            return "0"
        
        target_unit = self.get_report_unit("length") if use_report_units else self.get_base_unit("length")
        converted_value = self.convert_value(value_m, "m", target_unit, "length")
        precision = self.get_precision("length")
        
        formatted = f"{converted_value:.{precision}f} {target_unit}"
        
        if self.show_both_units() and not use_report_units and target_unit != "m":
            formatted += f" ({value_m:.{precision}f} m)"
        
        return formatted
    
    def get_units_suffix(self, value_type, material_type=None):
        """Get units suffix for input fields"""
        base_unit = self.get_base_unit(value_type)
        
        if value_type == "force":
            suffix = f" {base_unit}"
        elif value_type in ["stress", "modulus"]:
            suffix = f" {base_unit}"
        else:
            suffix = f" {base_unit}"
        
        # Add system indicator
        system = self.get_unit_system()
        if system == self.THAI_UNITS:
            suffix += " (🇹🇭)"
        elif system == self.US_UNITS:
            suffix += " (🇺🇸)"
        
        return suffix
    
    def convert_input_to_si(self, value, value_type, material_type=None):
        """Convert input value to SI units for internal use"""
        base_unit = self.get_base_unit(value_type)
        
        if value_type == "force":
            return self.convert_value(value, base_unit, "N", "force")
        elif value_type in ["stress", "modulus"]:
            return self.convert_value(value, base_unit, "Pa", "stress")
        elif value_type == "length":
            return self.convert_value(value, base_unit, "m", "length")
        elif value_type == "density":
            return self.convert_value(value, base_unit, "kg/m³", "density")
        else:
            return value
    
    def get_material_recommendations(self):
        """Get material value recommendations based on current units"""
        system = self.get_unit_system()
        constants = self.ENGINEERING_CONSTANTS
        
        steel_data = constants["steel"][system]
        concrete_data = constants["concrete"][system]
        
        stress_unit = self.get_base_unit("stress")
        
        return {
            "steel_modulus": (steel_data["modulus"], stress_unit),
            "concrete_modulus": (concrete_data["modulus_factor"] * (concrete_data["fc_normal"][1] ** 0.5), stress_unit),
            "steel_yield_sd30": (steel_data["fy_grades"][1], stress_unit),  # Grade 300/SD30
            "steel_yield_sd40": (steel_data["fy_grades"][2], stress_unit),  # Grade 400/SD40
            "concrete_fc280": (concrete_data["fc_normal"][1], stress_unit)  # fc' = 28 MPa / 280 ksc
        }
    
    def create_units_selector_widget(self):
        """Create comprehensive units selector widget for UI"""
        try:
            from PySide2 import QtWidgets, QtCore
            
            widget = QtWidgets.QWidget()
            layout = QtWidgets.QVBoxLayout(widget)
            
            # Title
            title = QtWidgets.QLabel("🌐 Global Units Settings")
            title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 5px;")
            layout.addWidget(title)
            
            # Level 1: Unit System Selection
            system_layout = QtWidgets.QHBoxLayout()
            system_layout.addWidget(QtWidgets.QLabel("System:"))
            
            self.system_combo = QtWidgets.QComboBox()
            for system_id, preset in self.UNIT_PRESETS.items():
                self.system_combo.addItem(f"{preset['name']}", system_id)
            
            # Set current selection
            current_system = self.get_unit_system()
            for i in range(self.system_combo.count()):
                if self.system_combo.itemData(i) == current_system:
                    self.system_combo.setCurrentIndex(i)
                    break
            
            self.system_combo.currentIndexChanged.connect(self._on_system_changed)
            system_layout.addWidget(self.system_combo)
            system_layout.addStretch()
            layout.addLayout(system_layout)
            
            # Level 2: Category Overrides (collapsible)
            self.category_group = QtWidgets.QGroupBox("📋 Category Overrides (Optional)")
            self.category_group.setCheckable(True)
            self.category_group.setChecked(False)
            category_layout = QtWidgets.QGridLayout(self.category_group)
            
            # Create unit selectors for each category
            self.unit_combos = {}
            categories = ["force", "stress", "length", "unit_weight"]
            
            for i, category in enumerate(categories):
                label = QtWidgets.QLabel(f"{category.title()}:")
                combo = QtWidgets.QComboBox()
                
                # Populate with available units
                if category in self.CONVERSION_FACTORS:
                    for unit in self.CONVERSION_FACTORS[category].keys():
                        combo.addItem(unit)
                
                # Set current value
                current_unit = self.get_base_unit(category)
                index = combo.findText(current_unit)
                if index >= 0:
                    combo.setCurrentIndex(index)
                
                combo.currentTextChanged.connect(
                    lambda text, cat=category: self.set_base_unit(cat, text)
                )
                
                self.unit_combos[category] = combo
                category_layout.addWidget(label, i // 2, (i % 2) * 2)
                category_layout.addWidget(combo, i // 2, (i % 2) * 2 + 1)
            
            layout.addWidget(self.category_group)
            
            # Display options
            options_layout = QtWidgets.QHBoxLayout()
            
            self.both_units_check = QtWidgets.QCheckBox("Show both units")
            self.both_units_check.setChecked(self.show_both_units())
            self.both_units_check.toggled.connect(self._on_both_units_changed)
            options_layout.addWidget(self.both_units_check)
            
            self.mixed_mode_check = QtWidgets.QCheckBox("Mixed unit mode")
            self.mixed_mode_check.setChecked(self.settings.get("mixed_unit_mode", False))
            self.mixed_mode_check.toggled.connect(self._on_mixed_mode_changed)
            options_layout.addWidget(self.mixed_mode_check)
            
            options_layout.addStretch()
            layout.addLayout(options_layout)
            
            return widget
            
        except ImportError:
            return None
    
    def _on_system_changed(self, index):
        """Handle unit system change"""
        if hasattr(self, 'system_combo'):
            system_id = self.system_combo.itemData(index)
            self.set_unit_system(system_id)
            # Update category combos
            self._update_category_combos()
    
    def _update_category_combos(self):
        """Update category combo boxes after system change"""
        if hasattr(self, 'unit_combos'):
            for category, combo in self.unit_combos.items():
                current_unit = self.get_base_unit(category)
                index = combo.findText(current_unit)
                if index >= 0:
                    combo.setCurrentIndex(index)
    
    def _on_both_units_changed(self, checked):
        """Handle both units display change"""
        self.settings["show_both_units"] = checked
        self.save_settings()
    
    def _on_mixed_mode_changed(self, checked):
        """Handle mixed unit mode change"""
        self.settings["mixed_unit_mode"] = checked
        self.save_settings()
    
    def get_material_recommendations(self):
        """Get material value recommendations based on current units"""
        system = self.get_unit_system()
        constants = self.ENGINEERING_CONSTANTS
        
        steel_data = constants["steel"][system]
        concrete_data = constants["concrete"][system]
        
        stress_unit = self.get_base_unit("stress")
        
        return {
            "steel_modulus": (steel_data["modulus"], stress_unit),
            "concrete_modulus": (int(concrete_data["modulus_factor"] * (concrete_data["fc_normal"][1] ** 0.5)), stress_unit),
            "steel_yield_sd30": (steel_data["fy_grades"][1], stress_unit),  # Grade 300/SD30
            "steel_yield_sd40": (steel_data["fy_grades"][2], stress_unit),  # Grade 400/SD40
            "concrete_fc280": (concrete_data["fc_normal"][1] if system != "THAI" else 280, stress_unit)  # fc' = 28 MPa / 280 ksc
        }

# Global instance
_units_manager = None

def get_units_manager():
    """Get global units manager instance"""
    global _units_manager
    if _units_manager is None:
        _units_manager = UnitsManager()
    return _units_manager

def set_units_system(units_system):
    """Set global units system"""
    manager = get_units_manager()
    manager.set_unit_system(units_system)

def get_current_units():
    """Get current units system"""
    manager = get_units_manager()
    return manager.get_unit_system()

def is_thai_units():
    """Check if Thai units are active globally"""
    manager = get_units_manager()
    return manager.is_thai_units()

def is_si_units():
    """Check if SI units are active globally"""
    manager = get_units_manager()
    return manager.is_si_units()

def is_us_units():
    """Check if US units are active globally"""
    manager = get_units_manager()
    return manager.is_us_units()

def format_force(value_n, material_type=None, use_report_units=False):
    """Global force formatting"""
    manager = get_units_manager()
    return manager.format_force(value_n, material_type, use_report_units)

def format_stress(value_pa, material_type=None, use_report_units=False):
    """Global stress formatting"""
    manager = get_units_manager()
    return manager.format_stress(value_pa, material_type, use_report_units)

def format_modulus(value_pa, material_type=None, use_report_units=False):
    """Global modulus formatting"""
    manager = get_units_manager()
    return manager.format_modulus(value_pa, material_type, use_report_units)

def format_length(value_m, use_report_units=False):
    """Global length formatting"""
    manager = get_units_manager()
    return manager.format_length(value_m, use_report_units)

def convert_value(value, from_unit, to_unit, unit_type):
    """Global unit conversion"""
    manager = get_units_manager()
    return manager.convert_value(value, from_unit, to_unit, unit_type)
