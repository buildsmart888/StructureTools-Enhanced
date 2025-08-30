# -*- coding: utf-8 -*-
"""
Load Application Panel - Professional load definition and application interface

This module provides a comprehensive task panel for structural load
application with load combinations, patterns, and real-time preview.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtGui, QtWidgets
import os
from typing import Optional, Dict, List, Any

# Import Global Units System
try:
    from ..utils.units_manager import (
        get_units_manager, format_force, format_stress
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"


class LoadApplicationPanel:
    """
    Professional task panel for load application and management.
    """
    
    def __init__(self, structure_obj=None):
        """
        Initialize Load Application Panel.
        
        Args:
            structure_obj: Structural object to apply loads to (beam, node, etc.)
        """
        self.structure_obj = structure_obj
        self.load_cases = []
        self.current_load_case = 0
        self.form = self._create_ui()
        self._populate_form()
        self._connect_signals()
    
    def _create_ui(self) -> QtWidgets.QWidget:
        """Create the user interface for load application."""
        
        # Main widget
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title = QtWidgets.QLabel("Load Application")
        title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Load case management
        case_widget = self._create_load_case_widget()
        layout.addWidget(case_widget)
        
        # Tab widget for different load types
        tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(tab_widget)
        
        # Nodal loads tab
        nodal_tab = self._create_nodal_loads_tab()
        tab_widget.addTab(nodal_tab, "Nodal Loads")
        
        # Distributed loads tab
        distributed_tab = self._create_distributed_loads_tab()
        tab_widget.addTab(distributed_tab, "Distributed Loads")
        
        # Point loads tab
        point_tab = self._create_point_loads_tab()
        tab_widget.addTab(point_tab, "Point Loads")
        
        # Surface/Area loads tab
        surface_tab = self._create_surface_loads_tab()
        tab_widget.addTab(surface_tab, "Surface Loads")
        
        # Thermal loads tab  
        thermal_tab = self._create_thermal_loads_tab()
        tab_widget.addTab(thermal_tab, "Thermal Loads")
        
        # Load combinations tab
        combinations_tab = self._create_combinations_tab()
        tab_widget.addTab(combinations_tab, "Combinations")
        
        # Load preview and summary
        preview_widget = self._create_preview_widget()
        layout.addWidget(preview_widget)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        self.apply_button = QtWidgets.QPushButton("Apply Loads")
        self.apply_button.setDefault(True)
        button_layout.addWidget(self.apply_button)
        
        self.preview_button = QtWidgets.QPushButton("Preview")
        button_layout.addWidget(self.preview_button)
        
        self.clear_button = QtWidgets.QPushButton("Clear All")
        button_layout.addWidget(self.clear_button)
        
        cancel_button = QtWidgets.QPushButton("Cancel")
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        # Store references
        self.tab_widget = tab_widget
        self.cancel_button = cancel_button
        
        return widget
    
    def _create_load_case_widget(self) -> QtWidgets.QGroupBox:
        """Create load case management widget."""
        group = QtWidgets.QGroupBox("Load Cases")
        layout = QtWidgets.QHBoxLayout(group)
        
        # Load case selection
        layout.addWidget(QtWidgets.QLabel("Case:"))
        self.case_combo = QtWidgets.QComboBox()
        self.case_combo.setMinimumWidth(150)
        layout.addWidget(self.case_combo)
        
        # Load case management buttons
        self.add_case_button = QtWidgets.QPushButton("Add")
        self.add_case_button.setMaximumWidth(60)
        layout.addWidget(self.add_case_button)
        
        self.delete_case_button = QtWidgets.QPushButton("Delete")
        self.delete_case_button.setMaximumWidth(60)
        layout.addWidget(self.delete_case_button)
        
        self.rename_case_button = QtWidgets.QPushButton("Rename")
        self.rename_case_button.setMaximumWidth(60)
        layout.addWidget(self.rename_case_button)
        
        layout.addStretch()
        
        # Load case properties
        layout.addWidget(QtWidgets.QLabel("Type:"))
        self.case_type_combo = QtWidgets.QComboBox()
        self.case_type_combo.addItems([
            "Dead Load", "Live Load", "Wind Load", "Seismic Load", 
            "Snow Load", "Temperature", "Construction Load", "Other"
        ])
        layout.addWidget(self.case_type_combo)
        
        layout.addWidget(QtWidgets.QLabel("Factor:"))
        self.case_factor_spin = QtWidgets.QDoubleSpinBox()
        self.case_factor_spin.setRange(-10.0, 10.0)
        self.case_factor_spin.setValue(1.0)
        self.case_factor_spin.setSingleStep(0.1)
        self.case_factor_spin.setDecimals(2)
        layout.addWidget(self.case_factor_spin)
        
        return group
    
    def _create_nodal_loads_tab(self) -> QtWidgets.QWidget:
        """Create nodal loads tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Forces group
        forces_group = QtWidgets.QGroupBox("Nodal Forces")
        forces_layout = QtWidgets.QFormLayout(forces_group)
        
        # Force components
        self.fx_spin = QtWidgets.QDoubleSpinBox()
        self.fx_spin.setRange(-1e9, 1e9)
        self.fx_spin.setSuffix(" N")
        forces_layout.addRow("Force X:", self.fx_spin)
        
        self.fy_spin = QtWidgets.QDoubleSpinBox()
        self.fy_spin.setRange(-1e9, 1e9)
        self.fy_spin.setSuffix(" N")
        forces_layout.addRow("Force Y:", self.fy_spin)
        
        self.fz_spin = QtWidgets.QDoubleSpinBox()
        self.fz_spin.setRange(-1e9, 1e9)
        self.fz_spin.setSuffix(" N")
        forces_layout.addRow("Force Z:", self.fz_spin)
        
        layout.addWidget(forces_group)
        
        # Moments group
        moments_group = QtWidgets.QGroupBox("Nodal Moments")
        moments_layout = QtWidgets.QFormLayout(moments_group)
        
        # Moment components
        self.mx_spin = QtWidgets.QDoubleSpinBox()
        self.mx_spin.setRange(-1e9, 1e9)
        self.mx_spin.setSuffix(" N⋅m")
        moments_layout.addRow("Moment X:", self.mx_spin)
        
        self.my_spin = QtWidgets.QDoubleSpinBox()
        self.my_spin.setRange(-1e9, 1e9)
        self.my_spin.setSuffix(" N⋅m")
        moments_layout.addRow("Moment Y:", self.my_spin)
        
        self.mz_spin = QtWidgets.QDoubleSpinBox()
        self.mz_spin.setRange(-1e9, 1e9)
        self.mz_spin.setSuffix(" N⋅m")
        moments_layout.addRow("Moment Z:", self.mz_spin)
        
        layout.addWidget(moments_group)
        
        # Node selection for application
        selection_group = QtWidgets.QGroupBox("Application")
        selection_layout = QtWidgets.QFormLayout(selection_group)
        
        self.node_combo = QtWidgets.QComboBox()
        self.node_combo.addItem("Selected Objects")
        selection_layout.addRow("Apply to:", self.node_combo)
        
        self.coordinate_combo = QtWidgets.QComboBox()
        self.coordinate_combo.addItems(["Global", "Local"])
        selection_layout.addRow("Coordinates:", self.coordinate_combo)
        
        layout.addWidget(selection_group)
        
        layout.addStretch()
        
        return widget
    
    def _create_distributed_loads_tab(self) -> QtWidgets.QWidget:
        """Create distributed loads tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Load type selection
        type_group = QtWidgets.QGroupBox("Load Type")
        type_layout = QtWidgets.QHBoxLayout(type_group)
        
        self.uniform_radio = QtWidgets.QRadioButton("Uniform")
        self.uniform_radio.setChecked(True)
        type_layout.addWidget(self.uniform_radio)
        
        self.linear_radio = QtWidgets.QRadioButton("Linear")
        type_layout.addWidget(self.linear_radio)
        
        self.trapezoidal_radio = QtWidgets.QRadioButton("Trapezoidal")
        type_layout.addWidget(self.trapezoidal_radio)
        
        layout.addWidget(type_group)
        
        # Load magnitude
        magnitude_group = QtWidgets.QGroupBox("Load Magnitude")
        magnitude_layout = QtWidgets.QFormLayout(magnitude_group)
        
        # Start values
        self.w_start_y_spin = QtWidgets.QDoubleSpinBox()
        self.w_start_y_spin.setRange(-1e6, 1e6)
        self.w_start_y_spin.setSuffix(" N/m")
        magnitude_layout.addRow("Start Load Y:", self.w_start_y_spin)
        
        self.w_start_z_spin = QtWidgets.QDoubleSpinBox()
        self.w_start_z_spin.setRange(-1e6, 1e6)
        self.w_start_z_spin.setSuffix(" N/m")
        magnitude_layout.addRow("Start Load Z:", self.w_start_z_spin)
        
        # End values (for non-uniform loads)
        self.w_end_y_spin = QtWidgets.QDoubleSpinBox()
        self.w_end_y_spin.setRange(-1e6, 1e6)
        self.w_end_y_spin.setSuffix(" N/m")
        self.w_end_y_spin.setEnabled(False)
        magnitude_layout.addRow("End Load Y:", self.w_end_y_spin)
        
        self.w_end_z_spin = QtWidgets.QDoubleSpinBox()
        self.w_end_z_spin.setRange(-1e6, 1e6)
        self.w_end_z_spin.setSuffix(" N/m")
        self.w_end_z_spin.setEnabled(False)
        magnitude_layout.addRow("End Load Z:", self.w_end_z_spin)
        
        layout.addWidget(magnitude_group)
        
        # Application range
        range_group = QtWidgets.QGroupBox("Application Range")
        range_layout = QtWidgets.QFormLayout(range_group)
        
        self.start_position_spin = QtWidgets.QDoubleSpinBox()
        self.start_position_spin.setRange(0.0, 1.0)
        self.start_position_spin.setSingleStep(0.1)
        self.start_position_spin.setSuffix(" (relative)")
        range_layout.addRow("Start Position:", self.start_position_spin)
        
        self.end_position_spin = QtWidgets.QDoubleSpinBox()
        self.end_position_spin.setRange(0.0, 1.0)
        self.end_position_spin.setValue(1.0)
        self.end_position_spin.setSingleStep(0.1)
        self.end_position_spin.setSuffix(" (relative)")
        range_layout.addRow("End Position:", self.end_position_spin)
        
        layout.addWidget(range_group)
        
        layout.addStretch()
        
        return widget
    
    def _create_point_loads_tab(self) -> QtWidgets.QWidget:
        """Create point loads tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Point loads table
        self.point_loads_table = QtWidgets.QTableWidget()
        self.point_loads_table.setColumnCount(6)
        self.point_loads_table.setHorizontalHeaderLabels([
            "Position", "Force Y", "Force Z", "Moment X", "Moment Y", "Moment Z"
        ])
        self.point_loads_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.point_loads_table)
        
        # Point load controls
        controls_layout = QtWidgets.QHBoxLayout()
        
        add_point_button = QtWidgets.QPushButton("Add Point Load")
        controls_layout.addWidget(add_point_button)
        
        remove_point_button = QtWidgets.QPushButton("Remove Selected")
        controls_layout.addWidget(remove_point_button)
        
        controls_layout.addStretch()
        
        layout.addLayout(controls_layout)
        
        # Quick input for common loads
        quick_group = QtWidgets.QGroupBox("Quick Input")
        quick_layout = QtWidgets.QFormLayout(quick_group)
        
        self.quick_position_spin = QtWidgets.QDoubleSpinBox()
        self.quick_position_spin.setRange(0.0, 1.0)
        self.quick_position_spin.setValue(0.5)
        self.quick_position_spin.setSingleStep(0.1)
        quick_layout.addRow("Position:", self.quick_position_spin)
        
        self.quick_force_spin = QtWidgets.QDoubleSpinBox()
        self.quick_force_spin.setRange(-1e9, 1e9)
        self.quick_force_spin.setSuffix(" N")
        quick_layout.addRow("Force:", self.quick_force_spin)
        
        quick_add_button = QtWidgets.QPushButton("Add to Table")
        quick_layout.addRow("", quick_add_button)
        
        layout.addWidget(quick_group)
        
        # Store references
        self.add_point_button = add_point_button
        self.remove_point_button = remove_point_button
        self.quick_add_button = quick_add_button
        
        return widget
    
    def _create_combinations_tab(self) -> QtWidgets.QWidget:
        """Create load combinations tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Combinations table
        self.combinations_table = QtWidgets.QTableWidget()
        self.combinations_table.setColumnCount(4)
        self.combinations_table.setHorizontalHeaderLabels([
            "Combination Name", "Load Case", "Factor", "Type"
        ])
        layout.addWidget(self.combinations_table)
        
        # Combination controls
        controls_layout = QtWidgets.QHBoxLayout()
        
        add_combination_button = QtWidgets.QPushButton("Add Combination")
        controls_layout.addWidget(add_combination_button)
        
        remove_combination_button = QtWidgets.QPushButton("Remove Selected")
        controls_layout.addWidget(remove_combination_button)
        
        controls_layout.addStretch()
        
        # Standard combinations
        standard_combo = QtWidgets.QComboBox()
        standard_combo.addItems([
            "Custom", "ASCE 7-22 Basic", "ASCE 7-22 with Live Load", 
            "Eurocode Ultimate", "Eurocode Serviceability"
        ])
        controls_layout.addWidget(QtWidgets.QLabel("Standard:"))
        controls_layout.addWidget(standard_combo)
        
        apply_standard_button = QtWidgets.QPushButton("Apply Standard")
        controls_layout.addWidget(apply_standard_button)
        
        layout.addLayout(controls_layout)
        
        # Store references
        self.add_combination_button = add_combination_button
        self.remove_combination_button = remove_combination_button
        self.standard_combo = standard_combo
        self.apply_standard_button = apply_standard_button
        
        return widget
    
    def _create_preview_widget(self) -> QtWidgets.QGroupBox:
        """Create load preview and summary widget."""
        group = QtWidgets.QGroupBox("Load Summary")
        layout = QtWidgets.QVBoxLayout(group)
        
        # Summary text
        self.summary_text = QtWidgets.QTextEdit()
        self.summary_text.setMaximumHeight(100)
        self.summary_text.setReadOnly(True)
        layout.addWidget(self.summary_text)
        
        # Preview options
        options_layout = QtWidgets.QHBoxLayout()
        
        self.show_arrows_check = QtWidgets.QCheckBox("Show load arrows")
        self.show_arrows_check.setChecked(True)
        options_layout.addWidget(self.show_arrows_check)
        
        self.arrow_scale_spin = QtWidgets.QDoubleSpinBox()
        self.arrow_scale_spin.setRange(0.1, 10.0)
        self.arrow_scale_spin.setValue(1.0)
        self.arrow_scale_spin.setSingleStep(0.1)
        options_layout.addWidget(QtWidgets.QLabel("Scale:"))
        options_layout.addWidget(self.arrow_scale_spin)
        
        options_layout.addStretch()
        
        layout.addLayout(options_layout)
        
        return group
    
    def _populate_form(self) -> None:
        """Populate form with existing load data."""
        # Initialize with default load case
        if not self.load_cases:
            self.load_cases = [{"name": "Dead Load", "type": "Dead Load", "factor": 1.0}]
            self.case_combo.addItem("Dead Load")
        
        # Update load case properties
        self._update_case_properties()
        
        # Populate structure-specific data
        if self.structure_obj:
            self._load_existing_loads()
        
        self._update_summary()
    
    def _connect_signals(self) -> None:
        """Connect UI signals to handlers."""
        
        # Load case management
        self.case_combo.currentIndexChanged.connect(self._on_case_changed)
        self.add_case_button.clicked.connect(self._add_load_case)
        self.delete_case_button.clicked.connect(self._delete_load_case)
        self.rename_case_button.clicked.connect(self._rename_load_case)
        
        # Load case properties
        self.case_type_combo.currentTextChanged.connect(self._update_case_type)
        self.case_factor_spin.valueChanged.connect(self._update_case_factor)
        
        # Load type changes
        self.uniform_radio.toggled.connect(self._on_load_type_changed)
        self.linear_radio.toggled.connect(self._on_load_type_changed)
        self.trapezoidal_radio.toggled.connect(self._on_load_type_changed)
        
        # Point loads
        self.add_point_button.clicked.connect(self._add_point_load_row)
        self.remove_point_button.clicked.connect(self._remove_point_load_row)
        self.quick_add_button.clicked.connect(self._quick_add_point_load)
        
        # Load combinations
        self.add_combination_button.clicked.connect(self._add_combination_row)
        self.remove_combination_button.clicked.connect(self._remove_combination_row)
        self.apply_standard_button.clicked.connect(self._apply_standard_combinations)
        
        # Value changes update summary
        for widget in [self.fx_spin, self.fy_spin, self.fz_spin, 
                      self.w_start_y_spin, self.w_start_z_spin]:
            widget.valueChanged.connect(self._update_summary)
        
        # Preview and apply
        self.preview_button.clicked.connect(self._preview_loads)
        self.apply_button.clicked.connect(self.accept)
        self.clear_button.clicked.connect(self._clear_all_loads)
        self.cancel_button.clicked.connect(self.reject)
    
    def _on_case_changed(self, index: int) -> None:
        """Handle load case selection change."""
        if 0 <= index < len(self.load_cases):
            self.current_load_case = index
            self._update_case_properties()
            self._load_case_data(index)
    
    def _update_case_properties(self) -> None:
        """Update case properties from current selection."""
        if 0 <= self.current_load_case < len(self.load_cases):
            case_data = self.load_cases[self.current_load_case]
            self.case_type_combo.setCurrentText(case_data.get("type", "Dead Load"))
            self.case_factor_spin.setValue(case_data.get("factor", 1.0))
    
    def _add_load_case(self) -> None:
        """Add new load case."""
        name, ok = QtWidgets.QInputDialog.getText(
            self.form, "Add Load Case", "Enter load case name:"
        )
        
        if ok and name:
            case_data = {"name": name, "type": "Dead Load", "factor": 1.0}
            self.load_cases.append(case_data)
            self.case_combo.addItem(name)
            self.case_combo.setCurrentIndex(len(self.load_cases) - 1)
    
    def _update_summary(self) -> None:
        """Update load summary display."""
        summary_lines = []
        
        # Current load case
        if 0 <= self.current_load_case < len(self.load_cases):
            case_name = self.load_cases[self.current_load_case]["name"]
            summary_lines.append(f"Load Case: {case_name}")
        
        # Nodal loads
        forces = [self.fx_spin.value(), self.fy_spin.value(), self.fz_spin.value()]
        if any(f != 0 for f in forces):
            summary_lines.append(f"Nodal Force: ({forces[0]:.0f}, {forces[1]:.0f}, {forces[2]:.0f}) N")
        
        # Distributed loads
        if self.w_start_y_spin.value() != 0 or self.w_start_z_spin.value() != 0:
            summary_lines.append(f"Distributed Load: {self.w_start_y_spin.value():.0f} N/m (Y), {self.w_start_z_spin.value():.0f} N/m (Z)")
        
        # Point loads count
        point_count = self.point_loads_table.rowCount()
        if point_count > 0:
            summary_lines.append(f"Point Loads: {point_count} loads defined")
        
        self.summary_text.setPlainText("\n".join(summary_lines))
    
    def _on_load_type_changed(self) -> None:
        """Handle load type radio button changes."""
        is_uniform = self.uniform_radio.isChecked()
        self.w_end_y_spin.setEnabled(not is_uniform)
        self.w_end_z_spin.setEnabled(not is_uniform)
        
        if is_uniform:
            # Copy start values to end values for uniform loads
            self.w_end_y_spin.setValue(self.w_start_y_spin.value())
            self.w_end_z_spin.setValue(self.w_start_z_spin.value())
    
    def _load_existing_loads(self) -> None:
        """Load existing loads from structure object."""
        # This would load existing loads from the structure object
        # Implementation depends on object type and load storage format
        pass
    
    def _preview_loads(self) -> None:
        """Preview loads in 3D view."""
        # This would create visual representations of loads
        FreeCAD.Console.PrintMessage("Load preview functionality not yet implemented\n")
    
    def _clear_all_loads(self) -> None:
        """Clear all load inputs."""
        # Reset all spin boxes
        for widget in [self.fx_spin, self.fy_spin, self.fz_spin, self.mx_spin, self.my_spin, self.mz_spin,
                      self.w_start_y_spin, self.w_start_z_spin, self.w_end_y_spin, self.w_end_z_spin]:
            widget.setValue(0.0)
        
        # Clear tables
        self.point_loads_table.setRowCount(0)
        self.combinations_table.setRowCount(0)
        
        self._update_summary()
    
    def accept(self) -> None:
        """Apply loads to structure object."""
        if not self.structure_obj:
            FreeCAD.Console.PrintWarning("No structure object selected for load application\n")
            return
        
        try:
            # Apply loads based on object type
            if hasattr(self.structure_obj, 'Type'):
                if self.structure_obj.Type == "StructuralNode":
                    self._apply_nodal_loads()
                elif self.structure_obj.Type == "StructuralBeam":
                    self._apply_beam_loads()
            
            FreeCAD.Console.PrintMessage("Loads applied successfully\n")
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error applying loads: {e}\n")
        
        Gui.Control.closeDialog()
    
    def _apply_nodal_loads(self) -> None:
        """Apply nodal loads to node object."""
        # Apply forces
        forces_x = getattr(self.structure_obj, 'NodalLoadsX', [])
        forces_y = getattr(self.structure_obj, 'NodalLoadsY', [])
        forces_z = getattr(self.structure_obj, 'NodalLoadsZ', [])
        
        # Extend arrays to current load case if needed
        while len(forces_x) <= self.current_load_case:
            forces_x.append(0.0)
            forces_y.append(0.0)
            forces_z.append(0.0)
        
        # Update values
        forces_x[self.current_load_case] = self.fx_spin.value()
        forces_y[self.current_load_case] = self.fy_spin.value()
        forces_z[self.current_load_case] = self.fz_spin.value()
        
        # Set properties
        self.structure_obj.NodalLoadsX = forces_x
        self.structure_obj.NodalLoadsY = forces_y
        self.structure_obj.NodalLoadsZ = forces_z
        
        # Apply moments similarly
        moments_x = getattr(self.structure_obj, 'NodalMomentsX', [])
        moments_y = getattr(self.structure_obj, 'NodalMomentsY', [])
        moments_z = getattr(self.structure_obj, 'NodalMomentsZ', [])
        
        while len(moments_x) <= self.current_load_case:
            moments_x.append(0.0)
            moments_y.append(0.0)
            moments_z.append(0.0)
        
        moments_x[self.current_load_case] = self.mx_spin.value()
        moments_y[self.current_load_case] = self.my_spin.value()
        moments_z[self.current_load_case] = self.mz_spin.value()
        
        self.structure_obj.NodalMomentsX = moments_x
        self.structure_obj.NodalMomentsY = moments_y
        self.structure_obj.NodalMomentsZ = moments_z
    
    def _apply_beam_loads(self) -> None:
        """Apply loads to beam object."""
        # Apply distributed loads
        loads_y = getattr(self.structure_obj, 'DistributedLoadY', [])
        loads_z = getattr(self.structure_obj, 'DistributedLoadZ', [])
        
        while len(loads_y) <= self.current_load_case:
            loads_y.append(0.0)
            loads_z.append(0.0)
        
        loads_y[self.current_load_case] = self.w_start_y_spin.value()
        loads_z[self.current_load_case] = self.w_start_z_spin.value()
        
        self.structure_obj.DistributedLoadY = loads_y
        self.structure_obj.DistributedLoadZ = loads_z
        
        # Apply point loads from table
        point_loads = []
        point_positions = []
        
        for row in range(self.point_loads_table.rowCount()):
            position_item = self.point_loads_table.item(row, 0)
            force_item = self.point_loads_table.item(row, 1)
            
            if position_item and force_item:
                try:
                    position = float(position_item.text())
                    force = float(force_item.text())
                    point_loads.append(force)
                    point_positions.append(position)
                except ValueError:
                    continue
        
        # Store point loads (simplified - would need proper load case handling)
        if hasattr(self.structure_obj, 'PointLoads'):
            self.structure_obj.PointLoads = point_loads
        if hasattr(self.structure_obj, 'PointLoadPositions'):
            self.structure_obj.PointLoadPositions = point_positions
    
    def reject(self) -> None:
        """Cancel load application."""
        Gui.Control.closeDialog()
    
    def getStandardButtons(self) -> int:
        """Return standard buttons for dialog."""
        return 0  # No standard buttons, we have custom ones