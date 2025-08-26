"""
ACI 318 Concrete Design Check Command

FreeCAD command for performing ACI 318-19 concrete design checks on structural elements.
Supports reinforced concrete beams, columns, slabs, and foundations.
"""

import os
from typing import List, Dict, Optional

# Import Global Units System
try:
    from .utils.units_manager import (
        get_units_manager, format_force, format_stress, format_modulus
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e9:.0f} GPa"

try:
    import FreeCAD as App
    import FreeCADGui as Gui
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2.QtCore import Qt
except ImportError:
    # For testing without FreeCAD
    class MockApp:
        class Console:
            @staticmethod
            def PrintMessage(msg): print(f"INFO: {msg}")
            @staticmethod
            def PrintWarning(msg): print(f"WARNING: {msg}")
            @staticmethod
            def PrintError(msg): print(f"ERROR: {msg}")
    App = MockApp()

from .design.ACI318 import (
    ACI318DesignCode, ConcreteStrengthMethod, ConcreteElementType,
    ConcreteSection, ConcreteProperties, ReinforcementProperties,
    ConcreteDesignForces, ConcreteDesignResult, RebarSize
)


class ACIDesignDialog(QtWidgets.QDialog):
    """Professional dialog for ACI 318 concrete design checking setup."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ACI 318 Concrete Design Check")
        self.setWindowIcon(QtGui.QIcon(":/icons/aci_design.svg"))
        self.resize(900, 750)
        
        # Design checker instance
        self.design_checker = None
        self.selected_elements = []
        self.design_results = []
        
        # Setup UI
        self.setup_ui()
        self.load_concrete_elements()
        
    def setup_ui(self):
        """Create the user interface."""
        layout = QtWidgets.QVBoxLayout(self)
        
        # Title and description
        title_label = QtWidgets.QLabel("ACI 318-19 Concrete Design Check")
        title_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title_label)
        
        description_label = QtWidgets.QLabel(
            "Perform comprehensive concrete design checks according to ACI 318-19.\n"
            "Design reinforced concrete beams, columns, slabs, and foundations."
        )
        description_label.setWordWrap(True)
        description_label.setStyleSheet("color: gray; margin-bottom: 15px;")
        layout.addWidget(description_label)
        
        # Create tab widget for organized interface
        self.tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(self.tab_widget)
        
        # Tab 1: Element Selection
        self.create_element_selection_tab()
        
        # Tab 2: Material Properties
        self.create_material_properties_tab()
        
        # Tab 3: Reinforcement Design
        self.create_reinforcement_tab()
        
        # Tab 4: Design Checks
        self.create_design_checks_tab()
        
        # Tab 5: Results and Reporting
        self.create_results_tab()
        
        # Button layout
        button_layout = QtWidgets.QHBoxLayout()
        
        # Action buttons
        self.run_check_btn = QtWidgets.QPushButton("Run Design Check")
        self.run_check_btn.setIcon(QtGui.QIcon(":/icons/play.svg"))
        self.run_check_btn.clicked.connect(self.run_design_check)
        
        self.design_reinforcement_btn = QtWidgets.QPushButton("Design Reinforcement")
        self.design_reinforcement_btn.setIcon(QtGui.QIcon(":/icons/rebar.svg"))
        self.design_reinforcement_btn.clicked.connect(self.design_reinforcement)
        
        self.export_report_btn = QtWidgets.QPushButton("Export Report")
        self.export_report_btn.setIcon(QtGui.QIcon(":/icons/export.svg"))
        self.export_report_btn.clicked.connect(self.export_report)
        self.export_report_btn.setEnabled(False)
        
        # Standard buttons
        self.help_btn = QtWidgets.QPushButton("Help")
        self.help_btn.setIcon(QtGui.QIcon(":/icons/help.svg"))
        self.help_btn.clicked.connect(self.show_help)
        
        self.close_btn = QtWidgets.QPushButton("Close")
        self.close_btn.setIcon(QtGui.QIcon(":/icons/close.svg"))
        self.close_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(self.run_check_btn)
        button_layout.addWidget(self.design_reinforcement_btn)
        button_layout.addWidget(self.export_report_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.help_btn)
        button_layout.addWidget(self.close_btn)
        
        layout.addLayout(button_layout)
        
    def create_element_selection_tab(self):
        """Create element selection tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Element selection controls
        selection_group = QtWidgets.QGroupBox("Concrete Element Selection")
        selection_layout = QtWidgets.QVBoxLayout(selection_group)
        
        # Available elements list
        elements_label = QtWidgets.QLabel("Available Concrete Elements:")
        selection_layout.addWidget(elements_label)
        
        self.elements_list = QtWidgets.QListWidget()
        self.elements_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.elements_list.itemSelectionChanged.connect(self.on_element_selection_changed)
        selection_layout.addWidget(self.elements_list)
        
        # Selection buttons
        selection_buttons = QtWidgets.QHBoxLayout()
        
        self.select_all_btn = QtWidgets.QPushButton("Select All")
        self.select_all_btn.clicked.connect(self.select_all_elements)
        
        self.clear_selection_btn = QtWidgets.QPushButton("Clear Selection")
        self.clear_selection_btn.clicked.connect(self.clear_element_selection)
        
        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.load_concrete_elements)
        
        selection_buttons.addWidget(self.select_all_btn)
        selection_buttons.addWidget(self.clear_selection_btn)
        selection_buttons.addStretch()
        selection_buttons.addWidget(self.refresh_btn)
        
        selection_layout.addLayout(selection_buttons)
        layout.addWidget(selection_group)
        
        # Element type filter
        filter_group = QtWidgets.QGroupBox("Element Type Filter")
        filter_layout = QtWidgets.QHBoxLayout(filter_group)
        
        self.filter_beams = QtWidgets.QCheckBox("Beams")
        self.filter_beams.setChecked(True)
        self.filter_beams.toggled.connect(self.apply_element_filter)
        
        self.filter_columns = QtWidgets.QCheckBox("Columns")
        self.filter_columns.setChecked(True)
        self.filter_columns.toggled.connect(self.apply_element_filter)
        
        self.filter_slabs = QtWidgets.QCheckBox("Slabs")
        self.filter_slabs.setChecked(True)
        self.filter_slabs.toggled.connect(self.apply_element_filter)
        
        self.filter_foundations = QtWidgets.QCheckBox("Foundations")
        self.filter_foundations.setChecked(True)
        self.filter_foundations.toggled.connect(self.apply_element_filter)
        
        filter_layout.addWidget(self.filter_beams)
        filter_layout.addWidget(self.filter_columns)
        filter_layout.addWidget(self.filter_slabs)
        filter_layout.addWidget(self.filter_foundations)
        
        layout.addWidget(filter_group)
        
        # Element properties preview
        preview_group = QtWidgets.QGroupBox("Selected Element Properties")
        preview_layout = QtWidgets.QVBoxLayout(preview_group)
        
        self.element_properties_text = QtWidgets.QTextEdit()
        self.element_properties_text.setReadOnly(True)
        self.element_properties_text.setMaximumHeight(150)
        self.element_properties_text.setPlainText("Select elements to view properties...")
        preview_layout.addWidget(self.element_properties_text)
        
        layout.addWidget(preview_group)
        
        self.tab_widget.addTab(tab, "Elements")
        
    def create_material_properties_tab(self):
        """Create material properties tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Concrete properties
        concrete_group = QtWidgets.QGroupBox("Concrete Properties")
        concrete_layout = QtWidgets.QFormLayout(concrete_group)
        
        self.concrete_grade = QtWidgets.QComboBox()
        self.concrete_grade.addItems(["3000psi", "4000psi", "5000psi", "6000psi", "8000psi", "Custom"])
        self.concrete_grade.setCurrentText("4000psi")
        self.concrete_grade.currentTextChanged.connect(self.update_concrete_properties)
        concrete_layout.addRow("Concrete Grade:", self.concrete_grade)
        
        self.fc_value = QtWidgets.QSpinBox()
        self.fc_value.setRange(2500, 15000)
        self.fc_value.setSuffix(" psi")
        self.fc_value.setValue(4000)
        self.fc_value.setEnabled(False)
        concrete_layout.addRow("f'c:", self.fc_value)
        
        self.concrete_density = QtWidgets.QSpinBox()
        self.concrete_density.setRange(90, 160)
        self.concrete_density.setSuffix(" pcf")
        self.concrete_density.setValue(150)
        concrete_layout.addRow("Density:", self.concrete_density)
        
        self.concrete_Ec = QtWidgets.QSpinBox()
        self.concrete_Ec.setRange(2000000, 8000000)
        self.concrete_Ec.setSuffix(" psi")
        self.concrete_Ec.setValue(3644000)  # For 4000 psi concrete
        self.concrete_Ec.setEnabled(False)
        concrete_layout.addRow("Ec (calculated):", self.concrete_Ec)
        
        layout.addWidget(concrete_group)
        
        # Reinforcement properties
        rebar_group = QtWidgets.QGroupBox("Reinforcement Properties")
        rebar_layout = QtWidgets.QFormLayout(rebar_group)
        
        self.rebar_grade = QtWidgets.QComboBox()
        self.rebar_grade.addItems(["Grade60", "Grade75", "Grade80", "Custom"])
        self.rebar_grade.setCurrentText("Grade60")
        self.rebar_grade.currentTextChanged.connect(self.update_rebar_properties)
        rebar_layout.addRow("Steel Grade:", self.rebar_grade)
        
        self.fy_value = QtWidgets.QSpinBox()
        self.fy_value.setRange(40000, 100000)
        self.fy_value.setSuffix(" psi")
        self.fy_value.setValue(60000)
        self.fy_value.setEnabled(False)
        rebar_layout.addRow("fy:", self.fy_value)
        
        self.fu_value = QtWidgets.QSpinBox()
        self.fu_value.setRange(60000, 150000)
        self.fu_value.setSuffix(" psi")
        self.fu_value.setValue(90000)
        self.fu_value.setEnabled(False)
        rebar_layout.addRow("fu:", self.fu_value)
        
        self.Es_value = QtWidgets.QSpinBox()
        self.Es_value.setRange(25000000, 35000000)
        self.Es_value.setSuffix(" psi")
        self.Es_value.setValue(29000000)
        self.Es_value.setEnabled(False)
        rebar_layout.addRow("Es:", self.Es_value)
        
        layout.addWidget(rebar_group)
        
        # Design factors
        factors_group = QtWidgets.QGroupBox("Design Factors")
        factors_layout = QtWidgets.QFormLayout(factors_group)
        
        self.phi_flexure = QtWidgets.QDoubleSpinBox()
        self.phi_flexure.setRange(0.65, 0.95)
        self.phi_flexure.setDecimals(2)
        self.phi_flexure.setSingleStep(0.05)
        self.phi_flexure.setValue(0.90)
        self.phi_flexure.setToolTip("Strength reduction factor for flexure (tension controlled)")
        factors_layout.addRow("φ (Flexure):", self.phi_flexure)
        
        self.phi_shear = QtWidgets.QDoubleSpinBox()
        self.phi_shear.setRange(0.65, 0.85)
        self.phi_shear.setDecimals(2)
        self.phi_shear.setSingleStep(0.05)
        self.phi_shear.setValue(0.75)
        factors_layout.addRow("φ (Shear):", self.phi_shear)
        
        self.phi_compression = QtWidgets.QDoubleSpinBox()
        self.phi_compression.setRange(0.60, 0.80)
        self.phi_compression.setDecimals(2)
        self.phi_compression.setSingleStep(0.05)
        self.phi_compression.setValue(0.65)
        self.phi_compression.setToolTip("Strength reduction factor for compression (tied columns)")
        factors_layout.addRow("φ (Compression):", self.phi_compression)
        
        layout.addWidget(factors_group)
        
        self.tab_widget.addTab(tab, "Materials")
        
    def create_reinforcement_tab(self):
        """Create reinforcement design tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Flexural reinforcement
        flexural_group = QtWidgets.QGroupBox("Flexural Reinforcement")
        flexural_layout = QtWidgets.QFormLayout(flexural_group)
        
        # Tension reinforcement
        self.tension_bar_size = QtWidgets.QComboBox()
        self.tension_bar_size.addItems(["#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11"])
        self.tension_bar_size.setCurrentText("#8")
        flexural_layout.addRow("Tension Bar Size:", self.tension_bar_size)
        
        self.tension_bar_count = QtWidgets.QSpinBox()
        self.tension_bar_count.setRange(2, 20)
        self.tension_bar_count.setValue(4)
        self.tension_bar_count.valueChanged.connect(self.update_reinforcement_preview)
        flexural_layout.addRow("Number of Bars:", self.tension_bar_count)
        
        # Compression reinforcement
        self.compression_bar_size = QtWidgets.QComboBox()
        self.compression_bar_size.addItems(["None", "#4", "#5", "#6", "#7", "#8"])
        self.compression_bar_size.setCurrentText("#6")
        flexural_layout.addRow("Compression Bar Size:", self.compression_bar_size)
        
        self.compression_bar_count = QtWidgets.QSpinBox()
        self.compression_bar_count.setRange(0, 10)
        self.compression_bar_count.setValue(2)
        self.compression_bar_count.valueChanged.connect(self.update_reinforcement_preview)
        flexural_layout.addRow("Number of Compression Bars:", self.compression_bar_count)
        
        layout.addWidget(flexural_group)
        
        # Shear reinforcement
        shear_group = QtWidgets.QGroupBox("Shear Reinforcement")
        shear_layout = QtWidgets.QFormLayout(shear_group)
        
        self.stirrup_size = QtWidgets.QComboBox()
        self.stirrup_size.addItems(["#3", "#4", "#5"])
        self.stirrup_size.setCurrentText("#4")
        shear_layout.addRow("Stirrup Size:", self.stirrup_size)
        
        self.stirrup_spacing = QtWidgets.QDoubleSpinBox()
        self.stirrup_spacing.setRange(2.0, 24.0)
        self.stirrup_spacing.setSuffix(' in.')
        self.stirrup_spacing.setValue(8.0)
        self.stirrup_spacing.valueChanged.connect(self.update_reinforcement_preview)
        shear_layout.addRow("Stirrup Spacing:", self.stirrup_spacing)
        
        layout.addWidget(shear_group)
        
        # Section geometry
        geometry_group = QtWidgets.QGroupBox("Section Geometry")
        geometry_layout = QtWidgets.QFormLayout(geometry_group)
        
        self.section_width = QtWidgets.QDoubleSpinBox()
        self.section_width.setRange(8.0, 48.0)
        self.section_width.setSuffix(' in.')
        self.section_width.setValue(12.0)
        self.section_width.valueChanged.connect(self.update_reinforcement_preview)
        geometry_layout.addRow("Width:", self.section_width)
        
        self.section_height = QtWidgets.QDoubleSpinBox()
        self.section_height.setRange(10.0, 72.0)
        self.section_height.setSuffix(' in.')
        self.section_height.setValue(24.0)
        self.section_height.valueChanged.connect(self.update_reinforcement_preview)
        geometry_layout.addRow("Height:", self.section_height)
        
        self.concrete_cover = QtWidgets.QDoubleSpinBox()
        self.concrete_cover.setRange(0.75, 4.0)
        self.concrete_cover.setSuffix(' in.')
        self.concrete_cover.setValue(1.5)
        self.concrete_cover.valueChanged.connect(self.update_reinforcement_preview)
        geometry_layout.addRow("Cover:", self.concrete_cover)
        
        layout.addWidget(geometry_group)
        
        # Reinforcement preview
        preview_group = QtWidgets.QGroupBox("Reinforcement Summary")
        preview_layout = QtWidgets.QVBoxLayout(preview_group)
        
        self.reinforcement_summary = QtWidgets.QTextEdit()
        self.reinforcement_summary.setReadOnly(True)
        self.reinforcement_summary.setMaximumHeight(120)
        preview_layout.addWidget(self.reinforcement_summary)
        
        layout.addWidget(preview_group)
        
        # Update initial preview
        self.update_reinforcement_preview()
        
        self.tab_widget.addTab(tab, "Reinforcement")
        
    def create_design_checks_tab(self):
        """Create design checks tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Design checks selection
        checks_group = QtWidgets.QGroupBox("Design Checks to Perform")
        checks_layout = QtWidgets.QGridLayout(checks_group)
        
        self.check_flexure = QtWidgets.QCheckBox("Flexural Strength (ACI 22.2)")
        self.check_flexure.setChecked(True)
        self.check_flexure.setToolTip("Check beam/slab flexural capacity")
        checks_layout.addWidget(self.check_flexure, 0, 0)
        
        self.check_shear = QtWidgets.QCheckBox("Shear Strength (ACI 22.5)")
        self.check_shear.setChecked(True)
        self.check_shear.setToolTip("Check shear capacity and stirrup requirements")
        checks_layout.addWidget(self.check_shear, 0, 1)
        
        self.check_compression = QtWidgets.QCheckBox("Compression Strength (ACI 22.4)")
        self.check_compression.setChecked(True)
        self.check_compression.setToolTip("Check column compression capacity")
        checks_layout.addWidget(self.check_compression, 1, 0)
        
        self.check_development = QtWidgets.QCheckBox("Development Length (ACI 25.4)")
        self.check_development.setChecked(True)
        self.check_development.setToolTip("Check reinforcement development lengths")
        checks_layout.addWidget(self.check_development, 1, 1)
        
        self.check_deflection = QtWidgets.QCheckBox("Deflection Limits (ACI 24.2)")
        self.check_deflection.setChecked(True)
        self.check_deflection.setToolTip("Check serviceability deflection limits")
        checks_layout.addWidget(self.check_deflection, 2, 0)
        
        layout.addWidget(checks_group)
        
        # Design forces input
        forces_group = QtWidgets.QGroupBox("Design Forces")
        forces_layout = QtWidgets.QFormLayout(forces_group)
        
        self.factored_moment = QtWidgets.QDoubleSpinBox()
        self.factored_moment.setRange(0, 10000000)
        self.factored_moment.setSuffix(' in-lb')
        self.factored_moment.setValue(3000000)  # 250 kip-ft
        self.factored_moment.setToolTip("Factored moment Mu")
        forces_layout.addRow("Moment Mu:", self.factored_moment)
        
        self.factored_shear = QtWidgets.QDoubleSpinBox()
        self.factored_shear.setRange(0, 500000)
        self.factored_shear.setSuffix(' lb')
        self.factored_shear.setValue(25000)
        self.factored_shear.setToolTip("Factored shear Vu")
        forces_layout.addRow("Shear Vu:", self.factored_shear)
        
        self.factored_axial = QtWidgets.QDoubleSpinBox()
        self.factored_axial.setRange(0, 5000000)
        self.factored_axial.setSuffix(' lb')
        self.factored_axial.setValue(200000)
        self.factored_axial.setToolTip("Factored axial force Pu (compression positive)")
        forces_layout.addRow("Axial Pu:", self.factored_axial)
        
        layout.addWidget(forces_group)
        
        # Length properties
        length_group = QtWidgets.QGroupBox("Length Properties")
        length_layout = QtWidgets.QFormLayout(length_group)
        
        self.element_length = QtWidgets.QDoubleSpinBox()
        self.element_length.setRange(48, 600)  # 4 ft to 50 ft
        self.element_length.setSuffix(' in.')
        self.element_length.setValue(240)  # 20 ft
        length_layout.addRow("Element Length:", self.element_length)
        
        self.effective_length_x = QtWidgets.QDoubleSpinBox()
        self.effective_length_x.setRange(48, 600)
        self.effective_length_x.setSuffix(' in.')
        self.effective_length_x.setValue(240)
        self.effective_length_x.setToolTip("Effective length for buckling about x-axis")
        length_layout.addRow("Effective Length (x):", self.effective_length_x)
        
        self.effective_length_y = QtWidgets.QDoubleSpinBox()
        self.effective_length_y.setRange(48, 600)
        self.effective_length_y.setSuffix(' in.')
        self.effective_length_y.setValue(240)
        self.effective_length_y.setToolTip("Effective length for buckling about y-axis")
        length_layout.addRow("Effective Length (y):", self.effective_length_y)
        
        layout.addWidget(length_group)
        
        self.tab_widget.addTab(tab, "Design Checks")
        
    def create_results_tab(self):
        """Create results and reporting tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Results table
        results_group = QtWidgets.QGroupBox("Design Check Results")
        results_layout = QtWidgets.QVBoxLayout(results_group)
        
        self.results_table = QtWidgets.QTableWidget()
        self.results_table.setColumnCount(6)
        self.results_table.setHorizontalHeaderLabels([
            "Element", "Check Type", "Ratio", "Status", "Code Section", "Details"
        ])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.setAlternatingRowColors(True)
        self.results_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        results_layout.addWidget(self.results_table)
        
        layout.addWidget(results_group)
        
        # Summary information
        summary_group = QtWidgets.QGroupBox("Design Summary")
        summary_layout = QtWidgets.QVBoxLayout(summary_group)
        
        self.summary_text = QtWidgets.QTextEdit()
        self.summary_text.setReadOnly(True)
        self.summary_text.setMaximumHeight(100)
        self.summary_text.setPlainText("Run design check to see summary...")
        summary_layout.addWidget(self.summary_text)
        
        layout.addWidget(summary_group)
        
        # Reinforcement requirements
        rebar_req_group = QtWidgets.QGroupBox("Reinforcement Requirements")
        rebar_req_layout = QtWidgets.QVBoxLayout(rebar_req_group)
        
        self.reinforcement_requirements = QtWidgets.QTextEdit()
        self.reinforcement_requirements.setReadOnly(True)
        self.reinforcement_requirements.setMaximumHeight(120)
        self.reinforcement_requirements.setPlainText("Design reinforcement to see requirements...")
        rebar_req_layout.addWidget(self.reinforcement_requirements)
        
        layout.addWidget(rebar_req_group)
        
        self.tab_widget.addTab(tab, "Results")
        
    def load_concrete_elements(self):
        """Load concrete elements from the FreeCAD document."""
        self.elements_list.clear()
        
        if not App.ActiveDocument:
            App.Console.PrintWarning("No active document found\n")
            return
        
        # Find concrete elements
        concrete_objects = []
        
        for obj in App.ActiveDocument.Objects:
            # Check for StructureTools concrete objects
            if hasattr(obj, 'Type'):
                if obj.Type in ['ConcreteBeam', 'ConcreteColumn', 'ConcreteSlab', 'ConcreteFoundation']:
                    concrete_objects.append(obj)
            
            # Check for structural plates (slabs)
            elif hasattr(obj, 'Type') and obj.Type == 'StructuralPlate':
                concrete_objects.append(obj)
                
            # Check by object name patterns
            elif any(pattern in obj.Name.lower() for pattern in ['concrete', 'beam', 'column', 'slab', 'foundation']):
                concrete_objects.append(obj)
        
        # Populate the list
        for obj in concrete_objects:
            item = QtWidgets.QListWidgetItem(f"{obj.Name} ({obj.Label})")
            item.setData(Qt.UserRole, obj.Name)
            
            # Set icon based on element type
            if any(pattern in obj.Name.lower() for pattern in ['beam', 'girder']):
                item.setIcon(QtGui.QIcon(":/icons/concrete_beam.svg"))
            elif 'column' in obj.Name.lower():
                item.setIcon(QtGui.QIcon(":/icons/concrete_column.svg"))
            elif any(pattern in obj.Name.lower() for pattern in ['slab', 'plate']):
                item.setIcon(QtGui.QIcon(":/icons/concrete_slab.svg"))
            elif 'foundation' in obj.Name.lower():
                item.setIcon(QtGui.QIcon(":/icons/foundation.svg"))
            else:
                item.setIcon(QtGui.QIcon(":/icons/concrete.svg"))
            
            self.elements_list.addItem(item)
        
        App.Console.PrintMessage(f"Found {len(concrete_objects)} concrete elements\n")
    
    def apply_element_filter(self):
        """Apply element type filter to the list."""
        # This would filter the elements list based on selected checkboxes
        # For now, just refresh the list
        self.load_concrete_elements()
    
    def on_element_selection_changed(self):
        """Handle element selection changes."""
        selected_items = self.elements_list.selectedItems()
        self.selected_elements = [item.data(Qt.UserRole) for item in selected_items]
        
        # Update element properties preview
        if selected_items:
            preview_text = f"Selected {len(selected_items)} elements:\n"
            for item in selected_items[:3]:  # Show first 3
                obj_name = item.data(Qt.UserRole)
                obj = App.ActiveDocument.getObject(obj_name)
                if obj:
                    preview_text += f"• {obj.Label}: "
                    if hasattr(obj, 'Shape'):
                        preview_text += f"Dimensions: {obj.Shape.BoundBox.XLength:.1f} x {obj.Shape.BoundBox.YLength:.1f} x {obj.Shape.BoundBox.ZLength:.1f}\n"
                    else:
                        preview_text += "Concrete element\n"
            
            if len(selected_items) > 3:
                preview_text += f"... and {len(selected_items) - 3} more elements"
        else:
            preview_text = "Select elements to view properties..."
        
        self.element_properties_text.setPlainText(preview_text)
    
    def select_all_elements(self):
        """Select all available elements."""
        self.elements_list.selectAll()
    
    def clear_element_selection(self):
        """Clear element selection."""
        self.elements_list.clearSelection()
    
    def update_concrete_properties(self):
        """Update concrete properties based on grade selection."""
        grade = self.concrete_grade.currentText()
        
        if grade == "Custom":
            self.fc_value.setEnabled(True)
            self.concrete_Ec.setEnabled(True)
        else:
            self.fc_value.setEnabled(False)
            self.concrete_Ec.setEnabled(False)
            
            # Update values based on grade
            if grade == "3000psi":
                self.fc_value.setValue(3000)
                self.concrete_Ec.setValue(3122000)
            elif grade == "4000psi":
                self.fc_value.setValue(4000)
                self.concrete_Ec.setValue(3605000)
            elif grade == "5000psi":
                self.fc_value.setValue(5000)
                self.concrete_Ec.setValue(4031000)
            elif grade == "6000psi":
                self.fc_value.setValue(6000)
                self.concrete_Ec.setValue(4415000)
            elif grade == "8000psi":
                self.fc_value.setValue(8000)
                self.concrete_Ec.setValue(5099000)
    
    def update_rebar_properties(self):
        """Update rebar properties based on grade selection."""
        grade = self.rebar_grade.currentText()
        
        if grade == "Custom":
            self.fy_value.setEnabled(True)
            self.fu_value.setEnabled(True)
            self.Es_value.setEnabled(True)
        else:
            self.fy_value.setEnabled(False)
            self.fu_value.setEnabled(False)
            self.Es_value.setEnabled(False)
            
            # Update values based on grade
            if grade == "Grade60":
                self.fy_value.setValue(60000)
                self.fu_value.setValue(90000)
            elif grade == "Grade75":
                self.fy_value.setValue(75000)
                self.fu_value.setValue(100000)
            elif grade == "Grade80":
                self.fy_value.setValue(80000)
                self.fu_value.setValue(120000)
    
    def update_reinforcement_preview(self):
        """Update reinforcement summary preview."""
        try:
            # Get current values
            tension_bar = self.tension_bar_size.currentText()
            tension_count = self.tension_bar_count.value()
            comp_bar = self.compression_bar_size.currentText()
            comp_count = self.compression_bar_count.value()
            stirrup = self.stirrup_size.currentText()
            spacing = self.stirrup_spacing.value()
            
            width = self.section_width.value()
            height = self.section_height.value()
            cover = self.concrete_cover.value()
            
            # Calculate areas
            tension_area = RebarSize.get_bar_properties(tension_bar).area * tension_count
            
            comp_area = 0
            if comp_bar != "None":
                comp_area = RebarSize.get_bar_properties(comp_bar).area * comp_count
            
            effective_depth = height - cover - 0.5
            rho = tension_area / (width * effective_depth) if effective_depth > 0 else 0
            
            # Create summary
            summary = f"Section: {width:.1f}\" x {height:.1f}\" (d = {effective_depth:.1f}\")\n"
            summary += f"Tension: {tension_count} {tension_bar} bars (As = {tension_area:.2f} in²)\n"
            
            if comp_area > 0:
                summary += f"Compression: {comp_count} {comp_bar} bars (As' = {comp_area:.2f} in²)\n"
            else:
                summary += f"Compression: None\n"
            
            summary += f"Stirrups: {stirrup} @ {spacing:.1f}\" spacing\n"
            summary += f"Reinforcement ratio ρ = {rho:.4f}"
            
            self.reinforcement_summary.setPlainText(summary)
            
        except Exception as e:
            self.reinforcement_summary.setPlainText(f"Error updating preview: {str(e)}")
    
    def run_design_check(self):
        """Run ACI 318 design check on selected elements."""
        if not self.selected_elements:
            QtWidgets.QMessageBox.warning(self, "No Selection", 
                                         "Please select at least one concrete element.")
            return
        
        # Create design checker
        self.design_checker = ACI318DesignCode(ConcreteStrengthMethod.USD)
        
        # Update strength reduction factors
        self.design_checker.phi_factors['tension_controlled'] = self.phi_flexure.value()
        self.design_checker.phi_factors['shear'] = self.phi_shear.value()
        self.design_checker.phi_factors['compression_controlled'] = self.phi_compression.value()
        
        # Progress dialog
        progress = QtWidgets.QProgressDialog("Running ACI Design Checks...", "Cancel", 
                                           0, len(self.selected_elements), self)
        progress.setWindowModality(Qt.WindowModal)
        
        self.design_results = []
        
        try:
            for i, element_name in enumerate(self.selected_elements):
                if progress.wasCanceled():
                    break
                
                progress.setLabelText(f"Checking element: {element_name}")
                progress.setValue(i)
                
                # Get element object
                element_obj = App.ActiveDocument.getObject(element_name)
                if not element_obj:
                    continue
                
                # Run design checks for this element
                element_results = self.check_element(element_obj)
                self.design_results.extend(element_results)
            
            progress.setValue(len(self.selected_elements))
            
            # Update results display
            self.update_results_display()
            
            # Switch to results tab
            self.tab_widget.setCurrentIndex(4)
            
            # Enable export button
            self.export_report_btn.setEnabled(True)
            
            App.Console.PrintMessage(f"Design check completed for {len(self.selected_elements)} elements\n")
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Design Check Error", 
                                          f"Error during design check: {str(e)}")
            App.Console.PrintError(f"Design check error: {str(e)}\n")
        
        finally:
            progress.close()
    
    def check_element(self, element_obj) -> List[ConcreteDesignResult]:
        """Perform design checks on a single element."""
        results = []
        
        try:
            # Extract element properties
            section, concrete, rebar, forces, length_props = self.extract_element_properties(element_obj)
            
            if not section or not concrete or not rebar:
                App.Console.PrintWarning(f"Incomplete properties for element {element_obj.Label}\n")
                return results
            
            # Perform selected checks
            if self.check_flexure.isChecked() and abs(forces.Mu) > 100:
                flexure_result = self.design_checker.check_beam_flexure(section, concrete, rebar, forces)
                results.append(flexure_result)
            
            if self.check_shear.isChecked() and abs(forces.Vu) > 100:
                shear_result = self.design_checker.check_beam_shear(section, concrete, rebar, forces)
                results.append(shear_result)
            
            if self.check_compression.isChecked() and abs(forces.Pu) > 1000:
                compression_result = self.design_checker.check_column_compression(
                    section, concrete, rebar, forces, length_props
                )
                results.append(compression_result)
            
            if self.check_development.isChecked():
                dev_result = self.design_checker.check_development_length(
                    section, concrete, rebar, self.tension_bar_size.currentText(), "tension"
                )
                results.append(dev_result)
                
        except Exception as e:
            App.Console.PrintError(f"Error checking element {element_obj.Label}: {str(e)}\n")
        
        return results
    
    def extract_element_properties(self, element_obj):
        """Extract section, materials, forces, and length properties from element."""
        # Create section from GUI inputs
        tension_bars = [(self.tension_bar_size.currentText(), self.tension_bar_count.value())]
        compression_bars = []
        if self.compression_bar_size.currentText() != "None":
            compression_bars = [(self.compression_bar_size.currentText(), self.compression_bar_count.value())]
        
        section = ConcreteSection(
            name=element_obj.Label,
            width=self.section_width.value(),
            height=self.section_height.value(),
            cover=self.concrete_cover.value(),
            tension_bars=tension_bars,
            compression_bars=compression_bars,
            stirrups=self.stirrup_size.currentText(),
            stirrup_spacing=self.stirrup_spacing.value()
        )
        
        # Create concrete properties from GUI
        concrete = ConcreteProperties(
            name=self.concrete_grade.currentText(),
            fc=self.fc_value.value(),
            density=self.concrete_density.value(),
            Ec=self.concrete_Ec.value(),
            fr=0,
            beta1=0
        )
        
        # Create rebar properties from GUI
        rebar = ReinforcementProperties(
            name=self.rebar_grade.currentText(),
            fy=self.fy_value.value(),
            fu=self.fu_value.value(),
            Es=self.Es_value.value(),
            bar_sizes=[]
        )
        
        # Get forces from GUI
        forces = ConcreteDesignForces(
            Mu=self.factored_moment.value(),
            Vu=self.factored_shear.value(),
            Pu=self.factored_axial.value()
        )
        
        # Length properties
        length_props = {
            'klu_x': self.effective_length_x.value(),
            'klu_y': self.effective_length_y.value(),
            'span': self.element_length.value()
        }
        
        return section, concrete, rebar, forces, length_props
    
    def design_reinforcement(self):
        """Design reinforcement for selected elements."""
        if not self.selected_elements:
            QtWidgets.QMessageBox.warning(self, "No Selection", 
                                         "Please select at least one concrete element.")
            return
        
        try:
            # Create design checker
            design_checker = ACI318DesignCode(ConcreteStrengthMethod.USD)
            
            # Get materials
            concrete = ConcreteProperties(
                name=self.concrete_grade.currentText(),
                fc=self.fc_value.value(),
                density=self.concrete_density.value(),
                Ec=self.concrete_Ec.value(),
                fr=0, beta1=0
            )
            
            rebar = ReinforcementProperties(
                name=self.rebar_grade.currentText(),
                fy=self.fy_value.value(),
                fu=self.fu_value.value(),
                Es=self.Es_value.value(),
                bar_sizes=[]
            )
            
            # Design reinforcement
            requirements_text = "REINFORCEMENT DESIGN RESULTS:\n"
            requirements_text += "=" * 40 + "\n\n"
            
            for element_name in self.selected_elements[:3]:  # Limit to first 3
                element_obj = App.ActiveDocument.getObject(element_name)
                if not element_obj:
                    continue
                
                # Create section geometry
                section = ConcreteSection(
                    name=element_obj.Label,
                    width=self.section_width.value(),
                    height=self.section_height.value(),
                    cover=self.concrete_cover.value(),
                    tension_bars=[],  # Will be designed
                    compression_bars=[],
                    stirrups="#4",
                    stirrup_spacing=8
                )
                
                # Design for applied moment
                Mu = self.factored_moment.value()
                
                reinforcement_design = design_checker.design_beam_reinforcement(
                    section, concrete, rebar, Mu
                )
                
                requirements_text += f"Element: {element_obj.Label}\n"
                requirements_text += f"Required As: {reinforcement_design['As_required']:.2f} in²\n"
                requirements_text += f"Reinforcement Ratio: {reinforcement_design['rho_provided']:.4f}\n"
                
                if 'bar_arrangement' in reinforcement_design:
                    arrangement = reinforcement_design['bar_arrangement']
                    requirements_text += f"Suggested: {arrangement['number']} {arrangement['bar_size']} bars\n"
                    requirements_text += f"Area Provided: {arrangement['area_provided']:.2f} in²\n"
                
                requirements_text += "\n"
            
            self.reinforcement_requirements.setPlainText(requirements_text)
            
            # Switch to results tab
            self.tab_widget.setCurrentIndex(4)
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Design Error", 
                                          f"Error during reinforcement design: {str(e)}")
    
    def update_results_display(self):
        """Update the results table and summary."""
        # Clear and populate results table
        self.results_table.setRowCount(len(self.design_results))
        
        for i, result in enumerate(self.design_results):
            # Element name
            self.results_table.setItem(i, 0, QtWidgets.QTableWidgetItem(result.element_name))
            
            # Check type
            self.results_table.setItem(i, 1, QtWidgets.QTableWidgetItem(result.failure_mode.value))
            
            # Ratio
            ratio_item = QtWidgets.QTableWidgetItem(f"{result.ratio:.3f}")
            if result.ratio > 1.0:
                ratio_item.setBackground(QtGui.QColor(255, 200, 200))  # Light red
            elif result.ratio > 0.9:
                ratio_item.setBackground(QtGui.QColor(255, 255, 200))  # Light yellow
            else:
                ratio_item.setBackground(QtGui.QColor(200, 255, 200))  # Light green
            self.results_table.setItem(i, 2, ratio_item)
            
            # Status
            status_item = QtWidgets.QTableWidgetItem(result.status)
            if result.status == "FAIL":
                status_item.setForeground(QtGui.QColor(200, 0, 0))  # Red
            else:
                status_item.setForeground(QtGui.QColor(0, 150, 0))  # Green
            self.results_table.setItem(i, 3, status_item)
            
            # Code section
            self.results_table.setItem(i, 4, QtWidgets.QTableWidgetItem(result.code_section))
            
            # Details
            details_text = f"Demand: {result.demand:.0f}, Capacity: {result.capacity:.0f}"
            self.results_table.setItem(i, 5, QtWidgets.QTableWidgetItem(details_text))
        
        # Auto-resize columns
        self.results_table.resizeColumnsToContents()
        
        # Update summary
        total_checks = len(self.design_results)
        passing_checks = sum(1 for r in self.design_results if r.status == "OK")
        failing_checks = total_checks - passing_checks
        
        summary = f"Total Checks: {total_checks}\n"
        summary += f"Passing: {passing_checks}\n"
        summary += f"Failing: {failing_checks}\n"
        if total_checks > 0:
            summary += f"Success Rate: {passing_checks/total_checks*100:.1f}%"
        
        self.summary_text.setPlainText(summary)
    
    def export_report(self):
        """Export design report."""
        if not self.design_results:
            QtWidgets.QMessageBox.warning(self, "No Results", 
                                         "No design results to export. Run design check first.")
            return
        
        # Get export file path
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export Design Report", "ACI_Design_Report.txt", "Text Files (*.txt)"
        )
        
        if file_path:
            try:
                # Generate report
                project_info = {
                    "Project": "FreeCAD Concrete Structure",
                    "Date": QtCore.QDateTime.currentDateTime().toString(),
                    "Design Method": "USD (Ultimate Strength Design)",
                    "Code": "ACI 318-19"
                }
                
                report_content = self.design_checker.generate_design_report(self.design_results, project_info)
                
                # Write to file
                with open(file_path, 'w') as f:
                    f.write(report_content)
                
                QtWidgets.QMessageBox.information(self, "Export Complete", 
                                                 f"Design report exported to:\n{file_path}")
                
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Export Error", 
                                              f"Error exporting report: {str(e)}")
    
    def show_help(self):
        """Show help information."""
        help_text = """
        ACI 318-19 Concrete Design Check
        
        This tool performs comprehensive concrete design checks according to ACI 318-19.
        
        Usage:
        1. Select concrete elements from the Elements tab
        2. Configure concrete and reinforcement materials
        3. Define reinforcement layout and section geometry
        4. Set design forces and run design checks
        5. Review results and export report if needed
        
        Design Checks:
        • Flexural Strength (ACI 22.2)
        • Shear Strength (ACI 22.5)  
        • Compression Strength (ACI 22.4)
        • Development Length (ACI 25.4)
        • Deflection Limits (ACI 24.2)
        
        Ultimate Strength Design method is used with appropriate φ factors.
        """
        
        QtWidgets.QMessageBox.information(self, "ACI Design Help", help_text)


class ACIDesignCommand:
    """FreeCAD command for ACI 318 concrete design checking."""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "resources", "icons", "aci_design.svg"),
            "MenuText": "ACI 318 Concrete Design Check",
            "ToolTip": "Perform ACI 318-19 concrete design checks on structural elements",
            "Accel": "Ctrl+Shift+C"
        }
    
    def Activated(self):
        """Execute the command."""
        try:
            # Check if we have a document
            if not App.ActiveDocument:
                QtWidgets.QMessageBox.warning(
                    None, "No Document", 
                    "Please open or create a FreeCAD document first."
                )
                return
            
            # Show the ACI design dialog
            dialog = ACIDesignDialog()
            dialog.exec_()
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                None, "ACI Design Error", 
                f"Error opening ACI design checker: {str(e)}"
            )
            App.Console.PrintError(f"ACI design command error: {str(e)}\n")
    
    def IsActive(self):
        """Check if command should be enabled."""
        return App.ActiveDocument is not None


# Register the command
if App.GuiUp:
    Gui.addCommand("RunACIDesign", ACIDesignCommand())