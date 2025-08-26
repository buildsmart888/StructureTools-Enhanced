# -*- coding: utf-8 -*-
"""
Node Properties Panel - Professional node configuration interface

This module provides a comprehensive task panel for structural node
properties with restraints, boundary conditions, and connection details.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtGui, QtWidgets
from typing import Optional

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


class NodePropertiesPanel:
    """Professional task panel for node properties."""
    
    def __init__(self, node_obj):
        """Initialize Node Properties Panel."""
        self.node_obj = node_obj
        self.form = self._create_ui()
        self._populate_form()
        self._connect_signals()
    
    def _create_ui(self) -> QtWidgets.QWidget:
        """Create the user interface."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title = QtWidgets.QLabel("Node Properties")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        # Tab widget
        tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(tab_widget)
        
        # Position tab
        position_tab = self._create_position_tab()
        tab_widget.addTab(position_tab, "Position")
        
        # Restraints tab
        restraints_tab = self._create_restraints_tab()
        tab_widget.addTab(restraints_tab, "Restraints")
        
        # Springs tab
        springs_tab = self._create_springs_tab()
        tab_widget.addTab(springs_tab, "Springs")
        
        # Connections tab
        connections_tab = self._create_connections_tab()
        tab_widget.addTab(connections_tab, "Connections")
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        self.apply_button = QtWidgets.QPushButton("Apply")
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        return widget
    
    def _create_position_tab(self) -> QtWidgets.QWidget:
        """Create position properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Position coordinates
        position_layout = QtWidgets.QHBoxLayout()
        self.pos_x = QtWidgets.QDoubleSpinBox()
        self.pos_x.setRange(-1e6, 1e6)
        self.pos_x.setSuffix(" mm")
        self.pos_y = QtWidgets.QDoubleSpinBox()
        self.pos_y.setRange(-1e6, 1e6)
        self.pos_y.setSuffix(" mm")
        self.pos_z = QtWidgets.QDoubleSpinBox()
        self.pos_z.setRange(-1e6, 1e6)
        self.pos_z.setSuffix(" mm")
        position_layout.addWidget(self.pos_x)
        position_layout.addWidget(self.pos_y)
        position_layout.addWidget(self.pos_z)
        layout.addRow("Position (X,Y,Z):", position_layout)
        
        # Node identification
        self.node_id_edit = QtWidgets.QLineEdit()
        layout.addRow("Node ID:", self.node_id_edit)
        
        self.description_edit = QtWidgets.QTextEdit()
        self.description_edit.setMaximumHeight(80)
        layout.addRow("Description:", self.description_edit)
        
        # Tolerance
        self.tolerance_spin = QtWidgets.QDoubleSpinBox()
        self.tolerance_spin.setRange(0.1, 100.0)
        self.tolerance_spin.setValue(1.0)
        self.tolerance_spin.setSuffix(" mm")
        layout.addRow("Tolerance:", self.tolerance_spin)
        
        return widget
    
    def _create_restraints_tab(self) -> QtWidgets.QWidget:
        """Create restraints properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Quick restraint presets
        presets_group = QtWidgets.QGroupBox("Quick Presets")
        presets_layout = QtWidgets.QHBoxLayout(presets_group)
        
        self.fixed_button = QtWidgets.QPushButton("Fixed")
        self.pinned_button = QtWidgets.QPushButton("Pinned")
        self.roller_button = QtWidgets.QPushButton("Roller")
        self.free_button = QtWidgets.QPushButton("Free")
        
        presets_layout.addWidget(self.fixed_button)
        presets_layout.addWidget(self.pinned_button)
        presets_layout.addWidget(self.roller_button)
        presets_layout.addWidget(self.free_button)
        
        layout.addWidget(presets_group)
        
        # Individual restraints
        restraints_group = QtWidgets.QGroupBox("Individual Restraints")
        restraints_layout = QtWidgets.QGridLayout(restraints_group)
        
        # Translation restraints
        restraints_layout.addWidget(QtWidgets.QLabel("Translations:"), 0, 0)
        self.restraint_x = QtWidgets.QCheckBox("X")
        self.restraint_y = QtWidgets.QCheckBox("Y")
        self.restraint_z = QtWidgets.QCheckBox("Z")
        restraints_layout.addWidget(self.restraint_x, 0, 1)
        restraints_layout.addWidget(self.restraint_y, 0, 2)
        restraints_layout.addWidget(self.restraint_z, 0, 3)
        
        # Rotation restraints
        restraints_layout.addWidget(QtWidgets.QLabel("Rotations:"), 1, 0)
        self.restraint_rx = QtWidgets.QCheckBox("RX")
        self.restraint_ry = QtWidgets.QCheckBox("RY")
        self.restraint_rz = QtWidgets.QCheckBox("RZ")
        restraints_layout.addWidget(self.restraint_rx, 1, 1)
        restraints_layout.addWidget(self.restraint_ry, 1, 2)
        restraints_layout.addWidget(self.restraint_rz, 1, 3)
        
        layout.addWidget(restraints_group)
        
        # Restraint code display
        self.restraint_code_label = QtWidgets.QLabel("000000")
        self.restraint_code_label.setStyleSheet("font-family: monospace; font-size: 12px; color: blue;")
        layout.addWidget(QtWidgets.QLabel("Restraint Code (XYZZRXRYRZ):"))
        layout.addWidget(self.restraint_code_label)
        
        layout.addStretch()
        
        return widget
    
    def _create_springs_tab(self) -> QtWidgets.QWidget:
        """Create spring supports tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Translation springs
        layout.addWidget(QtWidgets.QLabel("Translation Springs:"))
        
        self.spring_x = QtWidgets.QDoubleSpinBox()
        self.spring_x.setRange(0.0, 1e12)
        self.spring_x.setSuffix(" N/mm")
        layout.addRow("Spring X:", self.spring_x)
        
        self.spring_y = QtWidgets.QDoubleSpinBox()
        self.spring_y.setRange(0.0, 1e12)
        self.spring_y.setSuffix(" N/mm")
        layout.addRow("Spring Y:", self.spring_y)
        
        self.spring_z = QtWidgets.QDoubleSpinBox()
        self.spring_z.setRange(0.0, 1e12)
        self.spring_z.setSuffix(" N/mm")
        layout.addRow("Spring Z:", self.spring_z)
        
        # Rotational springs
        layout.addWidget(QtWidgets.QLabel("Rotational Springs:"))
        
        self.spring_rx = QtWidgets.QDoubleSpinBox()
        self.spring_rx.setRange(0.0, 1e12)
        self.spring_rx.setSuffix(" N⋅mm/rad")
        layout.addRow("Spring RX:", self.spring_rx)
        
        self.spring_ry = QtWidgets.QDoubleSpinBox()
        self.spring_ry.setRange(0.0, 1e12)
        self.spring_ry.setSuffix(" N⋅mm/rad")
        layout.addRow("Spring RY:", self.spring_ry)
        
        self.spring_rz = QtWidgets.QDoubleSpinBox()
        self.spring_rz.setRange(0.0, 1e12)
        self.spring_rz.setSuffix(" N⋅mm/rad")
        layout.addRow("Spring RZ:", self.spring_rz)
        
        return widget
    
    def _create_connections_tab(self) -> QtWidgets.QWidget:
        """Create connection details tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Connection type
        self.connection_type_combo = QtWidgets.QComboBox()
        self.connection_type_combo.addItems(["Rigid", "Pinned", "Semi-Rigid", "Special"])
        layout.addRow("Connection Type:", self.connection_type_combo)
        
        # Connection stiffness (for semi-rigid)
        self.connection_stiffness = QtWidgets.QDoubleSpinBox()
        self.connection_stiffness.setRange(0.0, 1e12)
        self.connection_stiffness.setSuffix(" N⋅mm/rad")
        self.connection_stiffness.setEnabled(False)
        layout.addRow("Connection Stiffness:", self.connection_stiffness)
        
        # Connected members (read-only list)
        self.connected_members_list = QtWidgets.QListWidget()
        self.connected_members_list.setMaximumHeight(120)
        layout.addRow("Connected Members:", self.connected_members_list)
        
        return widget
    
    def _populate_form(self) -> None:
        """Populate form with node properties."""
        if not self.node_obj:
            return
        
        try:
            # Position
            if hasattr(self.node_obj, 'Position'):
                pos = self.node_obj.Position
                self.pos_x.setValue(pos.x)
                self.pos_y.setValue(pos.y)
                self.pos_z.setValue(pos.z)
            
            # Node ID
            if hasattr(self.node_obj, 'NodeID'):
                self.node_id_edit.setText(self.node_obj.NodeID)
            
            # Description
            if hasattr(self.node_obj, 'Description'):
                self.description_edit.setPlainText(self.node_obj.Description)
            
            # Restraints
            self.restraint_x.setChecked(getattr(self.node_obj, 'RestraintX', False))
            self.restraint_y.setChecked(getattr(self.node_obj, 'RestraintY', False))
            self.restraint_z.setChecked(getattr(self.node_obj, 'RestraintZ', False))
            self.restraint_rx.setChecked(getattr(self.node_obj, 'RestraintRX', False))
            self.restraint_ry.setChecked(getattr(self.node_obj, 'RestraintRY', False))
            self.restraint_rz.setChecked(getattr(self.node_obj, 'RestraintRZ', False))
            
            # Springs
            self.spring_x.setValue(getattr(self.node_obj, 'SpringX', 0.0))
            self.spring_y.setValue(getattr(self.node_obj, 'SpringY', 0.0))
            self.spring_z.setValue(getattr(self.node_obj, 'SpringZ', 0.0))
            self.spring_rx.setValue(getattr(self.node_obj, 'SpringRX', 0.0))
            self.spring_ry.setValue(getattr(self.node_obj, 'SpringRY', 0.0))
            self.spring_rz.setValue(getattr(self.node_obj, 'SpringRZ', 0.0))
            
            # Connection type
            if hasattr(self.node_obj, 'ConnectionType'):
                self.connection_type_combo.setCurrentText(self.node_obj.ConnectionType)
            
            # Update displays
            self._update_restraint_code()
            self._update_connection_stiffness()
            
        except Exception as e:
            App.Console.PrintWarning(f"Error populating node form: {e}\n")
    
    def _connect_signals(self) -> None:
        """Connect UI signals."""
        
        # Preset buttons
        self.fixed_button.clicked.connect(lambda: self._apply_preset("fixed"))
        self.pinned_button.clicked.connect(lambda: self._apply_preset("pinned"))
        self.roller_button.clicked.connect(lambda: self._apply_preset("roller"))
        self.free_button.clicked.connect(lambda: self._apply_preset("free"))
        
        # Restraint changes
        for restraint in [self.restraint_x, self.restraint_y, self.restraint_z,
                         self.restraint_rx, self.restraint_ry, self.restraint_rz]:
            restraint.toggled.connect(self._update_restraint_code)
        
        # Connection type
        self.connection_type_combo.currentTextChanged.connect(self._update_connection_stiffness)
        
        # Buttons
        self.apply_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
    
    def _apply_preset(self, preset_type: str) -> None:
        """Apply restraint preset."""
        if preset_type == "fixed":
            # All restraints
            self.restraint_x.setChecked(True)
            self.restraint_y.setChecked(True)
            self.restraint_z.setChecked(True)
            self.restraint_rx.setChecked(True)
            self.restraint_ry.setChecked(True)
            self.restraint_rz.setChecked(True)
        elif preset_type == "pinned":
            # Translation restraints only
            self.restraint_x.setChecked(True)
            self.restraint_y.setChecked(True)
            self.restraint_z.setChecked(True)
            self.restraint_rx.setChecked(False)
            self.restraint_ry.setChecked(False)
            self.restraint_rz.setChecked(False)
        elif preset_type == "roller":
            # Vertical support only
            self.restraint_x.setChecked(False)
            self.restraint_y.setChecked(False)
            self.restraint_z.setChecked(True)
            self.restraint_rx.setChecked(False)
            self.restraint_ry.setChecked(False)
            self.restraint_rz.setChecked(False)
        elif preset_type == "free":
            # No restraints
            self.restraint_x.setChecked(False)
            self.restraint_y.setChecked(False)
            self.restraint_z.setChecked(False)
            self.restraint_rx.setChecked(False)
            self.restraint_ry.setChecked(False)
            self.restraint_rz.setChecked(False)
        
        self._update_restraint_code()
    
    def _update_restraint_code(self) -> None:
        """Update restraint code display."""
        restraints = [
            self.restraint_x.isChecked(),
            self.restraint_y.isChecked(),
            self.restraint_z.isChecked(),
            self.restraint_rx.isChecked(),
            self.restraint_ry.isChecked(),
            self.restraint_rz.isChecked()
        ]
        
        code = ''.join('1' if r else '0' for r in restraints)
        self.restraint_code_label.setText(code)
        
        # Update color based on support type
        if code == "111111":
            self.restraint_code_label.setStyleSheet("font-family: monospace; font-size: 12px; color: red; font-weight: bold;")
        elif code == "111000":
            self.restraint_code_label.setStyleSheet("font-family: monospace; font-size: 12px; color: green; font-weight: bold;")
        elif code == "001000":
            self.restraint_code_label.setStyleSheet("font-family: monospace; font-size: 12px; color: orange; font-weight: bold;")
        else:
            self.restraint_code_label.setStyleSheet("font-family: monospace; font-size: 12px; color: blue;")
    
    def _update_connection_stiffness(self) -> None:
        """Update connection stiffness availability."""
        is_semi_rigid = self.connection_type_combo.currentText() == "Semi-Rigid"
        self.connection_stiffness.setEnabled(is_semi_rigid)
    
    def accept(self) -> None:
        """Apply changes."""
        if not self.node_obj:
            return
        
        try:
            # Update position
            pos = App.Vector(self.pos_x.value(), self.pos_y.value(), self.pos_z.value())
            self.node_obj.Position = pos
            
            # Update identification
            self.node_obj.NodeID = self.node_id_edit.text()
            self.node_obj.Description = self.description_edit.toPlainText()
            
            # Update restraints
            self.node_obj.RestraintX = self.restraint_x.isChecked()
            self.node_obj.RestraintY = self.restraint_y.isChecked()
            self.node_obj.RestraintZ = self.restraint_z.isChecked()
            self.node_obj.RestraintRX = self.restraint_rx.isChecked()
            self.node_obj.RestraintRY = self.restraint_ry.isChecked()
            self.node_obj.RestraintRZ = self.restraint_rz.isChecked()
            
            # Update springs
            self.node_obj.SpringX = self.spring_x.value()
            self.node_obj.SpringY = self.spring_y.value()
            self.node_obj.SpringZ = self.spring_z.value()
            self.node_obj.SpringRX = self.spring_rx.value()
            self.node_obj.SpringRY = self.spring_ry.value()
            self.node_obj.SpringRZ = self.spring_rz.value()
            
            # Update connection
            self.node_obj.ConnectionType = self.connection_type_combo.currentText()
            if self.connection_stiffness.isEnabled():
                self.node_obj.ConnectionStiffness = self.connection_stiffness.value()
            
            self.node_obj.touch()
            App.ActiveDocument.recompute()
            
        except Exception as e:
            App.Console.PrintError(f"Error updating node: {e}\n")
        
        Gui.Control.closeDialog()
    
    def reject(self) -> None:
        """Cancel changes."""
        Gui.Control.closeDialog()
    
    def getStandardButtons(self) -> int:
        """Return standard buttons."""
        return 0