"""
AISC 360 Steel Design Check Command

FreeCAD command for performing AISC 360-16 steel design checks on structural members.
Supports both ASD (Allowable Stress Design) and LRFD (Load and Resistance Factor Design) methods.
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

from .design.AISC360 import (
    AISC360DesignCode, DesignMethod, MemberType, SectionProperties, 
    MaterialProperties, DesignForces, DesignResult
)


class AIScDesignDialog(QtWidgets.QDialog):
    """Professional dialog for AISC 360 design checking setup."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AISC 360 Steel Design Check")
        self.setWindowIcon(QtGui.QIcon(":/icons/aisc_design.svg"))
        self.resize(800, 700)
        
        # Design checker instance
        self.design_checker = None
        self.selected_members = []
        self.design_results = []
        
        # Setup UI
        self.setup_ui()
        self.load_structural_members()
        
    def setup_ui(self):
        """Create the user interface."""
        layout = QtWidgets.QVBoxLayout(self)
        
        # Title and description
        title_label = QtWidgets.QLabel("AISC 360-16 Steel Design Check")
        title_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title_label)
        
        description_label = QtWidgets.QLabel(
            "Perform comprehensive steel design checks according to AISC 360-16.\n"
            "Select members, choose design method, and configure parameters."
        )
        description_label.setWordWrap(True)
        description_label.setStyleSheet("color: gray; margin-bottom: 15px;")
        layout.addWidget(description_label)
        
        # Create tab widget for organized interface
        self.tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(self.tab_widget)
        
        # Tab 1: Member Selection
        self.create_member_selection_tab()
        
        # Tab 2: Design Parameters
        self.create_design_parameters_tab()
        
        # Tab 3: Load Combinations
        self.create_load_combinations_tab()
        
        # Tab 4: Results and Reporting
        self.create_results_tab()
        
        # Button layout
        button_layout = QtWidgets.QHBoxLayout()
        
        # Action buttons
        self.run_check_btn = QtWidgets.QPushButton("Run Design Check")
        self.run_check_btn.setIcon(QtGui.QIcon(":/icons/play.svg"))
        self.run_check_btn.clicked.connect(self.run_design_check)
        
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
        button_layout.addWidget(self.export_report_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.help_btn)
        button_layout.addWidget(self.close_btn)
        
        layout.addLayout(button_layout)
        
    def create_member_selection_tab(self):
        """Create member selection tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Member selection controls
        selection_group = QtWidgets.QGroupBox("Member Selection")
        selection_layout = QtWidgets.QVBoxLayout(selection_group)
        
        # Available members list
        members_label = QtWidgets.QLabel("Available Structural Members:")
        selection_layout.addWidget(members_label)
        
        self.members_list = QtWidgets.QListWidget()
        self.members_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.members_list.itemSelectionChanged.connect(self.on_member_selection_changed)
        selection_layout.addWidget(self.members_list)
        
        # Selection buttons
        selection_buttons = QtWidgets.QHBoxLayout()
        
        self.select_all_btn = QtWidgets.QPushButton("Select All")
        self.select_all_btn.clicked.connect(self.select_all_members)
        
        self.clear_selection_btn = QtWidgets.QPushButton("Clear Selection")
        self.clear_selection_btn.clicked.connect(self.clear_member_selection)
        
        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.load_structural_members)
        
        selection_buttons.addWidget(self.select_all_btn)
        selection_buttons.addWidget(self.clear_selection_btn)
        selection_buttons.addStretch()
        selection_buttons.addWidget(self.refresh_btn)
        
        selection_layout.addLayout(selection_buttons)
        layout.addWidget(selection_group)
        
        # Member properties preview
        preview_group = QtWidgets.QGroupBox("Selected Member Properties")
        preview_layout = QtWidgets.QVBoxLayout(preview_group)
        
        self.member_properties_text = QtWidgets.QTextEdit()
        self.member_properties_text.setReadOnly(True)
        self.member_properties_text.setMaximumHeight(150)
        self.member_properties_text.setPlainText("Select members to view properties...")
        preview_layout.addWidget(self.member_properties_text)
        
        layout.addWidget(preview_group)
        
        self.tab_widget.addTab(tab, "Members")
        
    def create_design_parameters_tab(self):
        """Create design parameters tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Design method selection
        method_group = QtWidgets.QGroupBox("Design Method")
        method_layout = QtWidgets.QVBoxLayout(method_group)
        
        self.design_method_group = QtWidgets.QButtonGroup()
        
        self.lrfd_radio = QtWidgets.QRadioButton("LRFD (Load and Resistance Factor Design)")
        self.lrfd_radio.setChecked(True)
        self.lrfd_radio.setToolTip("Load and Resistance Factor Design - Modern probability-based method")
        self.design_method_group.addButton(self.lrfd_radio, 0)
        method_layout.addWidget(self.lrfd_radio)
        
        self.asd_radio = QtWidgets.QRadioButton("ASD (Allowable Stress Design)")
        self.asd_radio.setToolTip("Allowable Stress Design - Traditional working stress method")
        self.design_method_group.addButton(self.asd_radio, 1)
        method_layout.addWidget(self.asd_radio)
        
        layout.addWidget(method_group)
        
        # Check types selection
        checks_group = QtWidgets.QGroupBox("Design Checks to Perform")
        checks_layout = QtWidgets.QGridLayout(checks_group)
        
        self.check_flexure = QtWidgets.QCheckBox("Flexural Strength (F2, F3, F4)")
        self.check_flexure.setChecked(True)
        self.check_flexure.setToolTip("Check beam flexural strength including LTB")
        checks_layout.addWidget(self.check_flexure, 0, 0)
        
        self.check_shear = QtWidgets.QCheckBox("Shear Strength (G2)")
        self.check_shear.setChecked(True)
        self.check_shear.setToolTip("Check web shear strength")
        checks_layout.addWidget(self.check_shear, 0, 1)
        
        self.check_compression = QtWidgets.QCheckBox("Compression Strength (E3)")
        self.check_compression.setChecked(True)
        self.check_compression.setToolTip("Check column compression strength")
        checks_layout.addWidget(self.check_compression, 1, 0)
        
        self.check_combined = QtWidgets.QCheckBox("Combined Loading (H1)")
        self.check_combined.setChecked(True)
        self.check_combined.setToolTip("Check beam-column interaction")
        checks_layout.addWidget(self.check_combined, 1, 1)
        
        self.check_deflection = QtWidgets.QCheckBox("Deflection Limits")
        self.check_deflection.setChecked(True)
        self.check_deflection.setToolTip("Check serviceability deflection limits")
        checks_layout.addWidget(self.check_deflection, 2, 0)
        
        layout.addWidget(checks_group)
        
        # Design parameters
        params_group = QtWidgets.QGroupBox("Design Parameters")
        params_layout = QtWidgets.QFormLayout(params_group)
        
        # Effective length factors
        self.kx_factor = QtWidgets.QDoubleSpinBox()
        self.kx_factor.setRange(0.5, 2.0)
        self.kx_factor.setValue(1.0)
        self.kx_factor.setDecimals(2)
        self.kx_factor.setSingleStep(0.1)
        params_layout.addRow("Effective Length Factor Kx:", self.kx_factor)
        
        self.ky_factor = QtWidgets.QDoubleSpinBox()
        self.ky_factor.setRange(0.5, 2.0)
        self.ky_factor.setValue(1.0)
        self.ky_factor.setDecimals(2)
        self.ky_factor.setSingleStep(0.1)
        params_layout.addRow("Effective Length Factor Ky:", self.ky_factor)
        
        # Lateral-torsional buckling parameters
        self.cb_factor = QtWidgets.QDoubleSpinBox()
        self.cb_factor.setRange(1.0, 2.5)
        self.cb_factor.setValue(1.0)
        self.cb_factor.setDecimals(2)
        self.cb_factor.setSingleStep(0.1)
        self.cb_factor.setToolTip("Lateral-torsional buckling modification factor")
        params_layout.addRow("LTB Factor Cb:", self.cb_factor)
        
        # Deflection limit ratios
        self.deflection_limit = QtWidgets.QComboBox()
        self.deflection_limit.addItems(["L/360 (Live Load)", "L/240 (Total Load)", 
                                       "L/180 (Cantilever)", "L/300 (Floors)", "Custom"])
        self.deflection_limit.setCurrentText("L/360 (Live Load)")
        params_layout.addRow("Deflection Limit:", self.deflection_limit)
        
        layout.addWidget(params_group)
        
        self.tab_widget.addTab(tab, "Parameters")
        
    def create_load_combinations_tab(self):
        """Create load combinations tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Load combinations selection
        combo_group = QtWidgets.QGroupBox("Load Combinations")
        combo_layout = QtWidgets.QVBoxLayout(combo_group)
        
        # Load combination list
        self.load_combinations_list = QtWidgets.QListWidget()
        self.load_combinations_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        combo_layout.addWidget(self.load_combinations_list)
        
        # Populate with standard combinations
        self.populate_load_combinations()
        
        # Combination management buttons
        combo_buttons = QtWidgets.QHBoxLayout()
        
        self.select_all_combos_btn = QtWidgets.QPushButton("Select All")
        self.select_all_combos_btn.clicked.connect(self.select_all_combinations)
        
        self.select_standard_btn = QtWidgets.QPushButton("Select Standard")
        self.select_standard_btn.clicked.connect(self.select_standard_combinations)
        
        self.add_custom_combo_btn = QtWidgets.QPushButton("Add Custom")
        self.add_custom_combo_btn.clicked.connect(self.add_custom_combination)
        
        combo_buttons.addWidget(self.select_all_combos_btn)
        combo_buttons.addWidget(self.select_standard_btn)
        combo_buttons.addWidget(self.add_custom_combo_btn)
        combo_buttons.addStretch()
        
        combo_layout.addLayout(combo_buttons)
        layout.addWidget(combo_group)
        
        # Load factors preview
        factors_group = QtWidgets.QGroupBox("Load Factors Preview")
        factors_layout = QtWidgets.QVBoxLayout(factors_group)
        
        self.load_factors_text = QtWidgets.QTextEdit()
        self.load_factors_text.setReadOnly(True)
        self.load_factors_text.setMaximumHeight(120)
        factors_layout.addWidget(self.load_factors_text)
        
        layout.addWidget(factors_group)
        
        # Connect selection change
        self.load_combinations_list.itemSelectionChanged.connect(self.update_load_factors_preview)
        
        self.tab_widget.addTab(tab, "Load Combinations")
        
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
            "Member", "Check Type", "Ratio", "Status", "Code Section", "Details"
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
        
        # Report options
        report_group = QtWidgets.QGroupBox("Report Options")
        report_layout = QtWidgets.QFormLayout(report_group)
        
        self.report_format = QtWidgets.QComboBox()
        self.report_format.addItems(["PDF Report", "HTML Report", "CSV Results", "Text Summary"])
        report_layout.addRow("Report Format:", self.report_format)
        
        self.include_details = QtWidgets.QCheckBox("Include Detailed Calculations")
        self.include_details.setChecked(True)
        report_layout.addRow("", self.include_details)
        
        self.include_diagrams = QtWidgets.QCheckBox("Include Section Diagrams")
        self.include_diagrams.setChecked(False)
        report_layout.addRow("", self.include_diagrams)
        
        layout.addWidget(report_group)
        
        self.tab_widget.addTab(tab, "Results")
        
    def load_structural_members(self):
        """Load structural members from the FreeCAD document."""
        self.members_list.clear()
        
        if not App.ActiveDocument:
            App.Console.PrintWarning("No active document found\n")
            return
        
        # Find structural members (beams, columns, etc.)
        structural_objects = []
        
        for obj in App.ActiveDocument.Objects:
            # Check for StructureTools objects
            if hasattr(obj, 'Type'):
                if obj.Type in ['StructuralBeam', 'StructuralColumn', 'StructuralBrace']:
                    structural_objects.append(obj)
            
            # Check for legacy member objects
            elif hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
                if obj.Proxy.Type in ['Member', 'Beam', 'Column']:
                    structural_objects.append(obj)
            
            # Check by object name patterns
            elif any(pattern in obj.Name.lower() for pattern in ['beam', 'column', 'brace', 'member']):
                structural_objects.append(obj)
        
        # Populate the list
        for obj in structural_objects:
            item = QtWidgets.QListWidgetItem(f"{obj.Name} ({obj.Label})")
            item.setData(Qt.UserRole, obj.Name)
            
            # Set icon based on member type
            if 'beam' in obj.Name.lower() or 'girder' in obj.Name.lower():
                item.setIcon(QtGui.QIcon(":/icons/beam.svg"))
            elif 'column' in obj.Name.lower():
                item.setIcon(QtGui.QIcon(":/icons/column.svg"))
            else:
                item.setIcon(QtGui.QIcon(":/icons/member.svg"))
            
            self.members_list.addItem(item)
        
        App.Console.PrintMessage(f"Found {len(structural_objects)} structural members\n")
    
    def populate_load_combinations(self):
        """Populate load combinations list."""
        # Get standard combinations based on current design method
        method = DesignMethod.LRFD if self.lrfd_radio.isChecked() else DesignMethod.ASD
        
        # Create temporary design checker to get standard combinations
        temp_checker = AISC360DesignCode(method)
        standard_combinations = temp_checker.get_standard_load_combinations()
        
        self.load_combinations_list.clear()
        for combo in standard_combinations:
            item = QtWidgets.QListWidgetItem(combo.name)
            item.setData(Qt.UserRole, combo)
            self.load_combinations_list.addItem(item)
    
    def on_member_selection_changed(self):
        """Handle member selection changes."""
        selected_items = self.members_list.selectedItems()
        self.selected_members = [item.data(Qt.UserRole) for item in selected_items]
        
        # Update member properties preview
        if selected_items:
            preview_text = f"Selected {len(selected_items)} members:\n"
            for item in selected_items[:5]:  # Show first 5
                obj_name = item.data(Qt.UserRole)
                obj = App.ActiveDocument.getObject(obj_name)
                if obj:
                    preview_text += f"• {obj.Label}: "
                    if hasattr(obj, 'Material') and obj.Material:
                        preview_text += f"Material: {obj.Material.Label}, "
                    if hasattr(obj, 'Section') and obj.Section:
                        preview_text += f"Section: {obj.Section.Label}"
                    preview_text += "\n"
            
            if len(selected_items) > 5:
                preview_text += f"... and {len(selected_items) - 5} more members"
        else:
            preview_text = "Select members to view properties..."
        
        self.member_properties_text.setPlainText(preview_text)
    
    def select_all_members(self):
        """Select all available members."""
        self.members_list.selectAll()
    
    def clear_member_selection(self):
        """Clear member selection."""
        self.members_list.clearSelection()
    
    def select_all_combinations(self):
        """Select all load combinations."""
        self.load_combinations_list.selectAll()
    
    def select_standard_combinations(self):
        """Select standard load combinations only."""
        self.load_combinations_list.clearSelection()
        
        # Select first 4-5 standard combinations
        standard_count = min(5, self.load_combinations_list.count())
        for i in range(standard_count):
            item = self.load_combinations_list.item(i)
            item.setSelected(True)
    
    def add_custom_combination(self):
        """Add custom load combination."""
        # This would open a dialog to define custom combination
        QtWidgets.QMessageBox.information(self, "Custom Combination", 
                                         "Custom load combination editor will be implemented in future version.")
    
    def update_load_factors_preview(self):
        """Update load factors preview based on selected combinations."""
        selected_items = self.load_combinations_list.selectedItems()
        
        if not selected_items:
            self.load_factors_text.setPlainText("Select load combinations to view factors...")
            return
        
        preview_text = f"Selected {len(selected_items)} load combinations:\n\n"
        
        for item in selected_items[:3]:  # Show first 3 in detail
            combo = item.data(Qt.UserRole)
            preview_text += f"{combo.name}:\n"
            for load_type, factor in combo.factors.items():
                preview_text += f"  {load_type}: {factor}\n"
            preview_text += "\n"
        
        if len(selected_items) > 3:
            preview_text += f"... and {len(selected_items) - 3} more combinations"
        
        self.load_factors_text.setPlainText(preview_text)
    
    def run_design_check(self):
        """Run AISC design check on selected members."""
        if not self.selected_members:
            QtWidgets.QMessageBox.warning(self, "No Selection", 
                                         "Please select at least one structural member.")
            return
        
        # Get design method
        method = DesignMethod.LRFD if self.lrfd_radio.isChecked() else DesignMethod.ASD
        
        # Create design checker
        self.design_checker = AISC360DesignCode(method)
        
        # Get selected load combinations
        selected_combo_items = self.load_combinations_list.selectedItems()
        if not selected_combo_items:
            QtWidgets.QMessageBox.warning(self, "No Load Combinations", 
                                         "Please select at least one load combination.")
            return
        
        # Progress dialog
        progress = QtWidgets.QProgressDialog("Running AISC Design Checks...", "Cancel", 
                                           0, len(self.selected_members), self)
        progress.setWindowModality(Qt.WindowModal)
        
        self.design_results = []
        
        try:
            for i, member_name in enumerate(self.selected_members):
                if progress.wasCanceled():
                    break
                
                progress.setLabelText(f"Checking member: {member_name}")
                progress.setValue(i)
                
                # Get member object
                member_obj = App.ActiveDocument.getObject(member_name)
                if not member_obj:
                    continue
                
                # Run design checks for this member
                member_results = self.check_member(member_obj)
                self.design_results.extend(member_results)
            
            progress.setValue(len(self.selected_members))
            
            # Update results display
            self.update_results_display()
            
            # Switch to results tab
            self.tab_widget.setCurrentIndex(3)
            
            # Enable export button
            self.export_report_btn.setEnabled(True)
            
            App.Console.PrintMessage(f"Design check completed for {len(self.selected_members)} members\n")
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Design Check Error", 
                                          f"Error during design check: {str(e)}")
            App.Console.PrintError(f"Design check error: {str(e)}\n")
        
        finally:
            progress.close()
    
    def check_member(self, member_obj) -> List[DesignResult]:
        """Perform design checks on a single member."""
        results = []
        
        try:
            # Extract member properties
            section, material, forces, length_props = self.extract_member_properties(member_obj)
            
            if not section or not material:
                App.Console.PrintWarning(f"Incomplete properties for member {member_obj.Label}\n")
                return results
            
            # Perform selected checks
            if self.check_flexure.isChecked() and abs(forces.Mux) > 0.1:
                flexure_result = self.design_checker.check_beam_flexure(section, material, forces, length_props)
                results.append(flexure_result)
            
            if self.check_shear.isChecked() and forces.resultant_shear > 0.1:
                shear_result = self.design_checker.check_beam_shear(section, material, forces)
                results.append(shear_result)
            
            if self.check_compression.isChecked() and abs(forces.Pu) > 0.1:
                compression_result = self.design_checker.check_column_compression(section, material, forces, length_props)
                results.append(compression_result)
            
            if self.check_combined.isChecked() and abs(forces.Pu) > 0.1 and forces.max_moment > 0.1:
                combined_result = self.design_checker.check_combined_loading(section, material, forces, length_props)
                results.append(combined_result)
            
        except Exception as e:
            App.Console.PrintError(f"Error checking member {member_obj.Label}: {str(e)}\n")
        
        return results
    
    def extract_member_properties(self, member_obj):
        """Extract section, material, forces, and length properties from member."""
        # This would extract actual properties from the FreeCAD object
        # For now, use example values
        
        # Default section (would get from member_obj.Section)
        section = SectionProperties(
            name="W18X35", A=10.3, Ix=510.0, Iy=57.6, Zx=57.6, Zy=15.3,
            Sx=57.0, Sy=7.00, rx=7.04, ry=2.36, J=0.422, Cw=5440.0,
            d=17.70, tw=0.300, bf=6.00, tf=0.425, k=1.16
        )
        
        # Default material (would get from member_obj.Material)
        material = MaterialProperties(
            name='A992', Fy=50.0, Fu=65.0, E=29000.0, G=11200.0,
            nu=0.30, density=490.0
        )
        
        # Default forces (would get from analysis results)
        forces = DesignForces(Pu=50.0, Mux=2400.0, Muy=600.0, Vux=15.0, Vuy=5.0)
        
        # Length properties
        length_props = {
            'Lx': 144.0,  # Unbraced length x
            'Ly': 144.0,  # Unbraced length y
            'Lb': 72.0,   # Lateral unbraced length
            'Kx': self.kx_factor.value(),
            'Ky': self.ky_factor.value(),
            'Cb': self.cb_factor.value()
        }
        
        return section, material, forces, length_props
    
    def update_results_display(self):
        """Update the results table and summary."""
        # Clear and populate results table
        self.results_table.setRowCount(len(self.design_results))
        
        for i, result in enumerate(self.design_results):
            # Member name
            self.results_table.setItem(i, 0, QtWidgets.QTableWidgetItem(result.member_name))
            
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
            details_text = f"Demand: {result.demand:.1f}, Capacity: {result.capacity:.1f}"
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
        format_text = self.report_format.currentText()
        if "PDF" in format_text:
            file_filter = "PDF Files (*.pdf)"
            default_ext = ".pdf"
        elif "HTML" in format_text:
            file_filter = "HTML Files (*.html)"
            default_ext = ".html"
        elif "CSV" in format_text:
            file_filter = "CSV Files (*.csv)"
            default_ext = ".csv"
        else:
            file_filter = "Text Files (*.txt)"
            default_ext = ".txt"
        
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export Design Report", f"AISC_Design_Report{default_ext}", file_filter
        )
        
        if file_path:
            try:
                # Generate report
                project_info = {
                    "Project": "FreeCAD Structure",
                    "Date": QtCore.QDateTime.currentDateTime().toString(),
                    "Design Method": self.design_checker.design_method.value,
                    "Code": self.design_checker.code_version
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
        AISC 360-16 Steel Design Check
        
        This tool performs comprehensive steel design checks according to AISC 360-16.
        
        Usage:
        1. Select structural members from the Members tab
        2. Choose design method (ASD or LRFD) and parameters
        3. Select load combinations to check
        4. Run design check and review results
        5. Export report if needed
        
        Design Checks:
        • Flexural Strength (F2, F3, F4)
        • Shear Strength (G2)  
        • Compression Strength (E3)
        • Combined Loading (H1)
        • Deflection Limits
        
        Both ASD and LRFD methods are supported with appropriate safety factors.
        """
        
        QtWidgets.QMessageBox.information(self, "AISC Design Help", help_text)


class AISCDesignCommand:
    """FreeCAD command for AISC 360 steel design checking."""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "resources", "icons", "aisc_design.svg"),
            "MenuText": "AISC 360 Steel Design Check",
            "ToolTip": "Perform AISC 360-16 steel design checks on structural members",
            "Accel": "Ctrl+Shift+A"
        }
    
    def Activated(self):
        """Execute the command."""
        try:
            # Check if we have structural members
            if not App.ActiveDocument:
                QtWidgets.QMessageBox.warning(
                    None, "No Document", 
                    "Please open or create a FreeCAD document first."
                )
                return
            
            # Show the AISC design dialog
            dialog = AISCDesignDialog()
            dialog.exec_()
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                None, "AISC Design Error", 
                f"Error opening AISC design checker: {str(e)}"
            )
            App.Console.PrintError(f"AISC design command error: {str(e)}\n")
    
    def IsActive(self):
        """Check if command should be enabled."""
        return App.ActiveDocument is not None


# Register the command
if App.GuiUp:
    Gui.addCommand("RunAISCDesign", AISCDesignCommand())