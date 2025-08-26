# -*- coding: utf-8 -*-
"""
Material Task Panel - Professional material selection and validation interface

This module provides a comprehensive task panel for structural material
management with standards compliance and automated validation.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtGui, QtWidgets
import os
from typing import Optional, Dict, Any

# Import Global Units System
try:
    from ..utils.units_manager import (
        get_units_manager, format_force, format_stress, format_modulus
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e9:.0f} GPa"

# Import material standards
from ..data.MaterialStandards import MATERIAL_STANDARDS, MATERIAL_CATEGORIES, get_materials_by_category


class MaterialTaskPanel:
    """
    Professional task panel for material properties with standards integration.
    """
    
    def __init__(self, material_obj):
        """
        Initialize Material Task Panel.
        
        Args:
            material_obj: StructuralMaterial object to edit
        """
        self.material_obj = material_obj
        self.form = self._create_ui()
        self._populate_form()
        self._connect_signals()
    
    def _create_ui(self) -> QtWidgets.QWidget:
        """Create the user interface for material properties."""
        
        # Main widget
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title = QtWidgets.QLabel("Material Properties")
        title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Tab widget for organized properties
        tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(tab_widget)
        
        # General tab
        general_tab = self._create_general_tab()
        tab_widget.addTab(general_tab, "General")
        
        # Mechanical tab
        mechanical_tab = self._create_mechanical_tab()
        tab_widget.addTab(mechanical_tab, "Mechanical")
        
        # Strength tab
        strength_tab = self._create_strength_tab()
        tab_widget.addTab(strength_tab, "Strength")
        
        # Advanced tab
        advanced_tab = self._create_advanced_tab()
        tab_widget.addTab(advanced_tab, "Advanced")
        
        # Validation status
        self.validation_widget = self._create_validation_widget()
        layout.addWidget(self.validation_widget)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        self.apply_button = QtWidgets.QPushButton("Apply")
        self.apply_button.setDefault(True)
        button_layout.addWidget(self.apply_button)
        
        self.reset_button = QtWidgets.QPushButton("Reset")
        button_layout.addWidget(self.reset_button)
        
        cancel_button = QtWidgets.QPushButton("Cancel")
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        # Store references to important widgets
        self.tab_widget = tab_widget
        self.cancel_button = cancel_button
        
        return widget
    
    def _create_general_tab(self) -> QtWidgets.QWidget:
        """Create general properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Material standard selection
        self.standard_combo = QtWidgets.QComboBox()
        self.standard_combo.addItems(list(MATERIAL_STANDARDS.keys()))
        layout.addRow("Material Standard:", self.standard_combo)
        
        # Category selection
        self.category_combo = QtWidgets.QComboBox()
        self.category_combo.addItems(list(MATERIAL_CATEGORIES.keys()))
        layout.addRow("Category:", self.category_combo)
        
        # Grade designation
        self.grade_edit = QtWidgets.QLineEdit()
        layout.addRow("Grade Designation:", self.grade_edit)
        
        # Material type
        self.type_edit = QtWidgets.QLineEdit()
        layout.addRow("Material Type:", self.type_edit)
        
        # Description
        self.description_edit = QtWidgets.QTextEdit()
        self.description_edit.setMaximumHeight(80)
        layout.addRow("Description:", self.description_edit)
        
        return widget
    
    def _create_mechanical_tab(self) -> QtWidgets.QWidget:
        """Create mechanical properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Elastic modulus
        modulus_layout = QtWidgets.QHBoxLayout()
        self.modulus_edit = QtWidgets.QLineEdit()
        self.modulus_unit = QtWidgets.QLabel("MPa")
        modulus_layout.addWidget(self.modulus_edit)
        modulus_layout.addWidget(self.modulus_unit)
        layout.addRow("Elastic Modulus (E):", modulus_layout)
        
        # Shear modulus
        shear_layout = QtWidgets.QHBoxLayout()
        self.shear_edit = QtWidgets.QLineEdit()
        self.shear_edit.setReadOnly(True)
        self.shear_unit = QtWidgets.QLabel("MPa (calculated)")
        shear_layout.addWidget(self.shear_edit)
        shear_layout.addWidget(self.shear_unit)
        layout.addRow("Shear Modulus (G):", shear_layout)
        
        # Poisson's ratio
        self.poisson_edit = QtWidgets.QDoubleSpinBox()
        self.poisson_edit.setDecimals(3)
        self.poisson_edit.setRange(0.0, 0.5)
        self.poisson_edit.setSingleStep(0.01)
        layout.addRow("Poisson's Ratio (ν):", self.poisson_edit)
        
        # Density
        density_layout = QtWidgets.QHBoxLayout()
        self.density_edit = QtWidgets.QLineEdit()
        self.density_unit = QtWidgets.QLabel("kg/m³")
        density_layout.addWidget(self.density_edit)
        density_layout.addWidget(self.density_unit)
        layout.addRow("Density (ρ):", density_layout)
        
        # Thermal expansion
        thermal_layout = QtWidgets.QHBoxLayout()
        self.thermal_edit = QtWidgets.QDoubleSpinBox()
        self.thermal_edit.setDecimals(8)
        self.thermal_edit.setRange(0.0, 100e-6)
        self.thermal_edit.setSuffix("e-6")
        self.thermal_unit = QtWidgets.QLabel("1/°C")
        thermal_layout.addWidget(self.thermal_edit)
        thermal_layout.addWidget(self.thermal_unit)
        layout.addRow("Thermal Expansion (α):", thermal_layout)
        
        return widget
    
    def _create_strength_tab(self) -> QtWidgets.QWidget:
        """Create strength properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Yield strength
        yield_layout = QtWidgets.QHBoxLayout()
        self.yield_edit = QtWidgets.QLineEdit()
        self.yield_unit = QtWidgets.QLabel("MPa")
        yield_layout.addWidget(self.yield_edit)
        yield_layout.addWidget(self.yield_unit)
        layout.addRow("Yield Strength (Fy):", yield_layout)
        
        # Ultimate strength
        ultimate_layout = QtWidgets.QHBoxLayout()
        self.ultimate_edit = QtWidgets.QLineEdit()
        self.ultimate_unit = QtWidgets.QLabel("MPa")
        ultimate_layout.addWidget(self.ultimate_edit)
        ultimate_layout.addWidget(self.ultimate_unit)
        layout.addRow("Ultimate Strength (Fu):", ultimate_layout)
        
        # Compressive strength (for concrete)
        compressive_layout = QtWidgets.QHBoxLayout()
        self.compressive_edit = QtWidgets.QLineEdit()
        self.compressive_unit = QtWidgets.QLabel("MPa")
        compressive_layout.addWidget(self.compressive_edit)
        compressive_layout.addWidget(self.compressive_unit)
        layout.addRow("Compressive Strength (fc'):", compressive_layout)
        
        # Strength ratio indicator
        self.ratio_label = QtWidgets.QLabel()
        self.ratio_label.setStyleSheet("color: gray; font-style: italic;")
        layout.addRow("Fu/Fy Ratio:", self.ratio_label)
        
        return widget
    
    def _create_advanced_tab(self) -> QtWidgets.QWidget:
        """Create advanced properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Testing standard
        self.testing_edit = QtWidgets.QLineEdit()
        layout.addRow("Testing Standard:", self.testing_edit)
        
        # Certification level
        self.certification_combo = QtWidgets.QComboBox()
        self.certification_combo.addItems([
            "Mill Certified", "Test Certified", "Special Inspection", "Custom"
        ])
        layout.addRow("Certification:", self.certification_combo)
        
        # Fatigue category
        self.fatigue_combo = QtWidgets.QComboBox()
        self.fatigue_combo.addItems(["A", "B", "C", "D", "E", "E'"])
        layout.addRow("Fatigue Category:", self.fatigue_combo)
        
        # Temperature dependent
        self.temp_dependent_check = QtWidgets.QCheckBox("Enable temperature effects")
        layout.addRow("Temperature:", self.temp_dependent_check)
        
        # Nonlinear behavior
        self.nonlinear_check = QtWidgets.QCheckBox("Enable nonlinear behavior")
        layout.addRow("Nonlinearity:", self.nonlinear_check)
        
        # Cost and sustainability
        cost_layout = QtWidgets.QHBoxLayout()
        self.cost_edit = QtWidgets.QLineEdit()
        self.cost_unit = QtWidgets.QLabel("per unit")
        cost_layout.addWidget(self.cost_edit)
        cost_layout.addWidget(self.cost_unit)
        layout.addRow("Unit Cost:", cost_layout)
        
        carbon_layout = QtWidgets.QHBoxLayout()
        self.carbon_edit = QtWidgets.QLineEdit()
        self.carbon_unit = QtWidgets.QLabel("kg CO2 eq")
        carbon_layout.addWidget(self.carbon_edit)
        carbon_layout.addWidget(self.carbon_unit)
        layout.addRow("Carbon Footprint:", carbon_layout)
        
        return widget
    
    def _create_validation_widget(self) -> QtWidgets.QWidget:
        """Create validation status widget."""
        widget = QtWidgets.QGroupBox("Validation Status")
        layout = QtWidgets.QVBoxLayout(widget)
        
        self.validation_label = QtWidgets.QLabel("All properties valid")
        self.validation_label.setStyleSheet("color: green;")
        layout.addWidget(self.validation_label)
        
        self.warnings_list = QtWidgets.QListWidget()
        self.warnings_list.setMaximumHeight(60)
        self.warnings_list.hide()
        layout.addWidget(self.warnings_list)
        
        return widget
    
    def _populate_form(self) -> None:
        """Populate form with current material properties."""
        if not self.material_obj:
            return
        
        try:
            # General properties
            if hasattr(self.material_obj, 'MaterialStandard'):
                self.standard_combo.setCurrentText(self.material_obj.MaterialStandard)
            
            if hasattr(self.material_obj, 'GradeDesignation'):
                self.grade_edit.setText(self.material_obj.GradeDesignation)
            
            if hasattr(self.material_obj, 'MaterialType'):
                self.type_edit.setText(self.material_obj.MaterialType)
            
            # Mechanical properties
            if hasattr(self.material_obj, 'ModulusElasticity'):
                value = self.material_obj.ModulusElasticity.getValueAs('MPa')
                self.modulus_edit.setText(f"{value:.0f}")
            
            if hasattr(self.material_obj, 'PoissonRatio'):
                self.poisson_edit.setValue(self.material_obj.PoissonRatio)
            
            if hasattr(self.material_obj, 'Density'):
                value = self.material_obj.Density.getValueAs('kg/m^3')
                self.density_edit.setText(f"{value:.0f}")
            
            if hasattr(self.material_obj, 'ThermalExpansion'):
                self.thermal_edit.setValue(self.material_obj.ThermalExpansion * 1e6)
            
            # Strength properties
            if hasattr(self.material_obj, 'YieldStrength'):
                value = self.material_obj.YieldStrength.getValueAs('MPa')
                self.yield_edit.setText(f"{value:.0f}")
            
            if hasattr(self.material_obj, 'UltimateStrength'):
                value = self.material_obj.UltimateStrength.getValueAs('MPa')
                self.ultimate_edit.setText(f"{value:.0f}")
            
            # Update calculated values
            self._update_calculated_values()
            self._update_validation_status()
            
        except Exception as e:
            App.Console.PrintWarning(f"Error populating material form: {e}\n")
    
    def _connect_signals(self) -> None:
        """Connect UI signals to handlers."""
        
        # Standard selection updates all properties
        self.standard_combo.currentTextChanged.connect(self._on_standard_changed)
        
        # Mechanical property updates
        self.modulus_edit.textChanged.connect(self._update_calculated_values)
        self.poisson_edit.valueChanged.connect(self._update_calculated_values)
        
        # Strength property updates
        self.yield_edit.textChanged.connect(self._update_strength_ratio)
        self.ultimate_edit.textChanged.connect(self._update_strength_ratio)
        
        # Validation triggers
        for widget in [self.modulus_edit, self.yield_edit, self.ultimate_edit]:
            widget.textChanged.connect(self._update_validation_status)
        
        self.poisson_edit.valueChanged.connect(self._update_validation_status)
        
        # Button connections
        self.apply_button.clicked.connect(self.accept)
        self.reset_button.clicked.connect(self._populate_form)
        self.cancel_button.clicked.connect(self.reject)
    
    def _on_standard_changed(self, standard_name: str) -> None:
        """Handle material standard selection change."""
        if not standard_name or standard_name not in MATERIAL_STANDARDS:
            return
        
        props = MATERIAL_STANDARDS[standard_name]
        
        try:
            # Update grade designation
            if 'GradeDesignation' in props:
                self.grade_edit.setText(props['GradeDesignation'])
            
            # Update mechanical properties
            if 'ModulusElasticity' in props:
                value = float(props['ModulusElasticity'].split()[0])
                self.modulus_edit.setText(f"{value:.0f}")
            
            if 'PoissonRatio' in props:
                self.poisson_edit.setValue(props['PoissonRatio'])
            
            if 'Density' in props:
                value = float(props['Density'].split()[0])
                self.density_edit.setText(f"{value:.0f}")
            
            if 'ThermalExpansion' in props:
                self.thermal_edit.setValue(props['ThermalExpansion'] * 1e6)
            
            # Update strength properties
            if 'YieldStrength' in props:
                value = float(props['YieldStrength'].split()[0])
                self.yield_edit.setText(f"{value:.0f}")
            
            if 'UltimateStrength' in props:
                value = float(props['UltimateStrength'].split()[0])
                self.ultimate_edit.setText(f"{value:.0f}")
            
            # Update testing standard
            if 'TestingStandard' in props:
                self.testing_edit.setText(props['TestingStandard'])
            
            self._update_calculated_values()
            self._update_strength_ratio()
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating from standard: {e}\n")
    
    def _update_calculated_values(self) -> None:
        """Update calculated values like shear modulus."""
        try:
            E_text = self.modulus_edit.text()
            nu = self.poisson_edit.value()
            
            if E_text and nu > 0:
                E = float(E_text)
                G = E / (2 * (1 + nu))
                self.shear_edit.setText(f"{G:.0f}")
            else:
                self.shear_edit.setText("")
        except:
            self.shear_edit.setText("")
    
    def _update_strength_ratio(self) -> None:
        """Update strength ratio indicator."""
        try:
            fy_text = self.yield_edit.text()
            fu_text = self.ultimate_edit.text()
            
            if fy_text and fu_text:
                fy = float(fy_text)
                fu = float(fu_text)
                
                if fy > 0:
                    ratio = fu / fy
                    self.ratio_label.setText(f"{ratio:.2f}")
                    
                    if ratio < 1.1 or ratio > 2.0:
                        self.ratio_label.setStyleSheet("color: red; font-weight: bold;")
                    else:
                        self.ratio_label.setStyleSheet("color: green;")
                else:
                    self.ratio_label.setText("Invalid")
            else:
                self.ratio_label.setText("")
                self.ratio_label.setStyleSheet("color: gray; font-style: italic;")
        except:
            self.ratio_label.setText("Error")
            self.ratio_label.setStyleSheet("color: red;")
    
    def _update_validation_status(self) -> None:
        """Update validation status display."""
        warnings = []
        
        try:
            # Validate Poisson ratio
            nu = self.poisson_edit.value()
            if nu < 0.0 or nu > 0.5:
                warnings.append("Poisson ratio must be between 0.0 and 0.5")
            
            # Validate strength relationship
            fy_text = self.yield_edit.text()
            fu_text = self.ultimate_edit.text()
            
            if fy_text and fu_text:
                fy = float(fy_text)
                fu = float(fu_text)
                
                if fy >= fu:
                    warnings.append("Ultimate strength must be greater than yield strength")
                
                ratio = fu / fy if fy > 0 else 0
                if ratio < 1.1 or ratio > 2.0:
                    warnings.append("Unusual strength ratio (typical range: 1.1-2.0)")
            
            # Validate modulus
            E_text = self.modulus_edit.text()
            if E_text:
                E = float(E_text)
                if E < 1000 or E > 1000000:
                    warnings.append("Elastic modulus outside typical range")
        
        except ValueError:
            warnings.append("Invalid numerical values")
        
        # Update display
        if warnings:
            self.validation_label.setText(f"{len(warnings)} validation issue(s)")
            self.validation_label.setStyleSheet("color: red; font-weight: bold;")
            
            self.warnings_list.clear()
            self.warnings_list.addItems(warnings)
            self.warnings_list.show()
        else:
            self.validation_label.setText("All properties valid")
            self.validation_label.setStyleSheet("color: green;")
            self.warnings_list.hide()
    
    def accept(self) -> None:
        """Apply changes to material object."""
        if not self.material_obj:
            return
        
        try:
            # Update general properties
            if hasattr(self.material_obj, 'MaterialStandard'):
                self.material_obj.MaterialStandard = self.standard_combo.currentText()
            
            if hasattr(self.material_obj, 'GradeDesignation'):
                self.material_obj.GradeDesignation = self.grade_edit.text()
            
            if hasattr(self.material_obj, 'MaterialType'):
                self.material_obj.MaterialType = self.type_edit.text()
            
            # Update mechanical properties
            if hasattr(self.material_obj, 'ModulusElasticity'):
                value = self.modulus_edit.text()
                if value:
                    self.material_obj.ModulusElasticity = f"{value} MPa"
            
            if hasattr(self.material_obj, 'PoissonRatio'):
                self.material_obj.PoissonRatio = self.poisson_edit.value()
            
            if hasattr(self.material_obj, 'Density'):
                value = self.density_edit.text()
                if value:
                    self.material_obj.Density = f"{value} kg/m^3"
            
            if hasattr(self.material_obj, 'ThermalExpansion'):
                self.material_obj.ThermalExpansion = self.thermal_edit.value() * 1e-6
            
            # Update strength properties
            if hasattr(self.material_obj, 'YieldStrength'):
                value = self.yield_edit.text()
                if value:
                    self.material_obj.YieldStrength = f"{value} MPa"
            
            if hasattr(self.material_obj, 'UltimateStrength'):
                value = self.ultimate_edit.text()
                if value:
                    self.material_obj.UltimateStrength = f"{value} MPa"
            
            # Update advanced properties
            if hasattr(self.material_obj, 'TestingStandard'):
                self.material_obj.TestingStandard = self.testing_edit.text()
            
            if hasattr(self.material_obj, 'CertificationLevel'):
                self.material_obj.CertificationLevel = self.certification_combo.currentText()
            
            # Trigger object update
            self.material_obj.touch()
            App.ActiveDocument.recompute()
            
            App.Console.PrintMessage(f"Material {self.material_obj.Label} updated successfully\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error updating material: {e}\n")
        
        # Close dialog
        Gui.Control.closeDialog()
    
    def reject(self) -> None:
        """Cancel changes and close dialog."""
        Gui.Control.closeDialog()
    
    def getStandardButtons(self) -> int:
        """Return standard buttons for dialog."""
        return 0  # No standard buttons, we have custom ones