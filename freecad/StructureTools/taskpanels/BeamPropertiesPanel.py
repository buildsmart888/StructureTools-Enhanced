# -*- coding: utf-8 -*-
"""
Beam Properties Panel - Professional beam configuration interface

This module provides a comprehensive task panel for structural beam
properties with section selection, material assignment, and connection details.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtGui, QtWidgets
from typing import Optional

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


class BeamPropertiesPanel:
    """Professional task panel for beam properties."""
    
    def __init__(self, beam_obj):
        """Initialize Beam Properties Panel."""
        self.beam_obj = beam_obj
        self.form = self._create_ui()
        self._populate_form()
        self._connect_signals()
    
    def _create_ui(self) -> QtWidgets.QWidget:
        """Create the user interface."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title = QtWidgets.QLabel("Beam Properties")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        # Tab widget
        tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(tab_widget)
        
        # Geometry tab
        geometry_tab = self._create_geometry_tab()
        tab_widget.addTab(geometry_tab, "Geometry")
        
        # Section tab
        section_tab = self._create_section_tab()
        tab_widget.addTab(section_tab, "Section")
        
        # Material tab
        material_tab = self._create_material_tab()
        tab_widget.addTab(material_tab, "Material")
        
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
    
    def _create_geometry_tab(self) -> QtWidgets.QWidget:
        """Create geometry properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Start point
        start_layout = QtWidgets.QHBoxLayout()
        self.start_x = QtWidgets.QDoubleSpinBox()
        self.start_x.setRange(-1e6, 1e6)
        self.start_x.setSuffix(" mm")
        self.start_y = QtWidgets.QDoubleSpinBox()
        self.start_y.setRange(-1e6, 1e6)
        self.start_y.setSuffix(" mm")
        self.start_z = QtWidgets.QDoubleSpinBox()
        self.start_z.setRange(-1e6, 1e6)
        self.start_z.setSuffix(" mm")
        start_layout.addWidget(self.start_x)
        start_layout.addWidget(self.start_y)
        start_layout.addWidget(self.start_z)
        layout.addRow("Start Point (X,Y,Z):", start_layout)
        
        # End point
        end_layout = QtWidgets.QHBoxLayout()
        self.end_x = QtWidgets.QDoubleSpinBox()
        self.end_x.setRange(-1e6, 1e6)
        self.end_x.setSuffix(" mm")
        self.end_y = QtWidgets.QDoubleSpinBox()
        self.end_y.setRange(-1e6, 1e6)
        self.end_y.setSuffix(" mm")
        self.end_z = QtWidgets.QDoubleSpinBox()
        self.end_z.setRange(-1e6, 1e6)
        self.end_z.setSuffix(" mm")
        end_layout.addWidget(self.end_x)
        end_layout.addWidget(self.end_y)
        end_layout.addWidget(self.end_z)
        layout.addRow("End Point (X,Y,Z):", end_layout)
        
        # Length (read-only)
        self.length_label = QtWidgets.QLabel("0 mm")
        layout.addRow("Length:", self.length_label)
        
        # Member ID and type
        self.member_id_edit = QtWidgets.QLineEdit()
        layout.addRow("Member ID:", self.member_id_edit)
        
        self.member_type_combo = QtWidgets.QComboBox()
        self.member_type_combo.addItems(["Beam", "Column", "Brace", "Joist", "Girder"])
        layout.addRow("Member Type:", self.member_type_combo)
        
        return widget
    
    def _create_section_tab(self) -> QtWidgets.QWidget:
        """Create section properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Section type and size
        self.section_type_combo = QtWidgets.QComboBox()
        self.section_type_combo.addItems(["W", "C", "L", "HSS", "Pipe", "Plate", "Custom"])
        layout.addRow("Section Type:", self.section_type_combo)
        
        self.section_size_edit = QtWidgets.QLineEdit()
        layout.addRow("Section Size:", self.section_size_edit)
        
        # Section properties
        self.area_edit = QtWidgets.QLineEdit()
        self.area_edit.setSuffix(" mm²")
        layout.addRow("Area (A):", self.area_edit)
        
        self.iy_edit = QtWidgets.QLineEdit()
        self.iy_edit.setSuffix(" mm⁴")
        layout.addRow("Moment of Inertia Iy:", self.iy_edit)
        
        self.iz_edit = QtWidgets.QLineEdit()
        self.iz_edit.setSuffix(" mm⁴")
        layout.addRow("Moment of Inertia Iz:", self.iz_edit)
        
        self.j_edit = QtWidgets.QLineEdit()
        self.j_edit.setSuffix(" mm⁴")
        layout.addRow("Torsional Constant J:", self.j_edit)
        
        # Section dimensions
        self.depth_edit = QtWidgets.QLineEdit()
        self.depth_edit.setSuffix(" mm")
        layout.addRow("Depth:", self.depth_edit)
        
        self.width_edit = QtWidgets.QLineEdit()
        self.width_edit.setSuffix(" mm")
        layout.addRow("Width:", self.width_edit)
        
        return widget
    
    def _create_material_tab(self) -> QtWidgets.QWidget:
        """Create material assignment tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Material selection
        material_layout = QtWidgets.QHBoxLayout()
        self.material_combo = QtWidgets.QComboBox()
        self.material_combo.addItem("Select Material...")
        material_layout.addWidget(self.material_combo)
        
        self.material_browse_button = QtWidgets.QPushButton("Browse...")
        material_layout.addWidget(self.material_browse_button)
        
        layout.addRow("Material:", material_layout)
        
        # Effective properties (read-only)
        self.effective_modulus_label = QtWidgets.QLabel("200000 MPa")
        layout.addRow("Effective Modulus:", self.effective_modulus_label)
        
        self.material_density_label = QtWidgets.QLabel("7850 kg/m³")
        layout.addRow("Density:", self.material_density_label)
        
        return widget
    
    def _create_connections_tab(self) -> QtWidgets.QWidget:
        """Create connection properties tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Start connection
        self.start_condition_combo = QtWidgets.QComboBox()
        self.start_condition_combo.addItems(["Fixed", "Pinned", "Roller", "Free", "Spring"])
        layout.addRow("Start Condition:", self.start_condition_combo)
        
        # Start releases
        start_releases_layout = QtWidgets.QHBoxLayout()
        self.start_my_release = QtWidgets.QCheckBox("My")
        self.start_mz_release = QtWidgets.QCheckBox("Mz")
        start_releases_layout.addWidget(self.start_my_release)
        start_releases_layout.addWidget(self.start_mz_release)
        layout.addRow("Start Releases:", start_releases_layout)
        
        # End connection
        self.end_condition_combo = QtWidgets.QComboBox()
        self.end_condition_combo.addItems(["Fixed", "Pinned", "Roller", "Free", "Spring"])
        layout.addRow("End Condition:", self.end_condition_combo)
        
        # End releases
        end_releases_layout = QtWidgets.QHBoxLayout()
        self.end_my_release = QtWidgets.QCheckBox("My")
        self.end_mz_release = QtWidgets.QCheckBox("Mz")
        end_releases_layout.addWidget(self.end_my_release)
        end_releases_layout.addWidget(self.end_mz_release)
        layout.addRow("End Releases:", end_releases_layout)
        
        return widget
    
    def _populate_form(self) -> None:
        """Populate form with beam properties."""
        if not self.beam_obj:
            return
        
        try:
            # Geometry
            if hasattr(self.beam_obj, 'StartPoint'):
                start = self.beam_obj.StartPoint
                self.start_x.setValue(start.x)
                self.start_y.setValue(start.y)
                self.start_z.setValue(start.z)
            
            if hasattr(self.beam_obj, 'EndPoint'):
                end = self.beam_obj.EndPoint
                self.end_x.setValue(end.x)
                self.end_y.setValue(end.y)
                self.end_z.setValue(end.z)
            
            # Update length
            self._update_length()
            
            # Section properties
            if hasattr(self.beam_obj, 'SectionType'):
                self.section_type_combo.setCurrentText(self.beam_obj.SectionType)
            
            if hasattr(self.beam_obj, 'SectionSize'):
                self.section_size_edit.setText(self.beam_obj.SectionSize)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error populating beam form: {e}\n")
    
    def _connect_signals(self) -> None:
        """Connect UI signals."""
        # Geometry updates
        for coord in [self.start_x, self.start_y, self.start_z, self.end_x, self.end_y, self.end_z]:
            coord.valueChanged.connect(self._update_length)
        
        # Buttons
        self.apply_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # Material browse
        self.material_browse_button.clicked.connect(self._browse_material)
    
    def _update_length(self) -> None:
        """Update beam length display."""
        try:
            start = App.Vector(self.start_x.value(), self.start_y.value(), self.start_z.value())
            end = App.Vector(self.end_x.value(), self.end_y.value(), self.end_z.value())
            length = start.distanceToPoint(end)
            self.length_label.setText(f"{length:.1f} mm")
        except:
            self.length_label.setText("0 mm")
    
    def _browse_material(self) -> None:
        """Browse for material object."""
        # This would open material selection dialog
        App.Console.PrintMessage("Material browser not yet implemented\n")
    
    def accept(self) -> None:
        """Apply changes."""
        if not self.beam_obj:
            return
        
        try:
            # Update geometry
            start = App.Vector(self.start_x.value(), self.start_y.value(), self.start_z.value())
            end = App.Vector(self.end_x.value(), self.end_y.value(), self.end_z.value())
            
            self.beam_obj.StartPoint = start
            self.beam_obj.EndPoint = end
            
            # Update section
            self.beam_obj.SectionType = self.section_type_combo.currentText()
            self.beam_obj.SectionSize = self.section_size_edit.text()
            
            # Update connections
            self.beam_obj.StartCondition = self.start_condition_combo.currentText()
            self.beam_obj.EndCondition = self.end_condition_combo.currentText()
            
            # Update releases
            self.beam_obj.StartMomentReleaseY = self.start_my_release.isChecked()
            self.beam_obj.StartMomentReleaseZ = self.start_mz_release.isChecked()
            self.beam_obj.EndMomentReleaseY = self.end_my_release.isChecked()
            self.beam_obj.EndMomentReleaseZ = self.end_mz_release.isChecked()
            
            self.beam_obj.touch()
            App.ActiveDocument.recompute()
            
        except Exception as e:
            App.Console.PrintError(f"Error updating beam: {e}\n")
        
        Gui.Control.closeDialog()
    
    def reject(self) -> None:
        """Cancel changes."""
        Gui.Control.closeDialog()
    
    def getStandardButtons(self) -> int:
        """Return standard buttons."""
        return 0