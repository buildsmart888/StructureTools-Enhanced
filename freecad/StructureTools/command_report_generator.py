# -*- coding: utf-8 -*-

import os
import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtGui, QtWidgets
from datetime import datetime
import tempfile
import webbrowser

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
    from .reporting.ReportGenerator import (
        StructuralReportGenerator, ReportFormat, 
        ReportConfiguration, AnalysisType
    )
    REPORTING_AVAILABLE = True
except ImportError:
    REPORTING_AVAILABLE = False
    print("Warning: Reporting dependencies not available. Using mock implementation.")
    
    # Mock implementations for development
    class ReportFormat:
        PDF = "PDF"
        HTML = "HTML"
        EXCEL = "EXCEL"
    
    class AnalysisType:
        STATIC = "Static"
        MODAL = "Modal"
        BUCKLING = "Buckling"
    
    class ReportConfiguration:
        def __init__(self):
            self.company_name = ""
            self.project_name = ""
            self.engineer_name = ""


class ReportGeneratorDialog(QtWidgets.QDialog):
    """Professional report generation dialog with comprehensive options"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Comprehensive Report Generator")
        self.setWindowIcon(QtGui.QIcon(":/icons/report_generator.svg"))
        self.resize(900, 700)
        self.setModal(True)
        
        # Initialize data
        self.structural_objects = []
        self.analysis_results = {}
        self.report_config = ReportConfiguration() if REPORTING_AVAILABLE else type('obj', (object,), {})()
        
        # Scan for structural objects
        self.scan_structural_objects()
        
        # Create UI
        self.create_ui()
        self.populate_default_values()
        
        # Connect signals
        self.connect_signals()
    
    def create_ui(self):
        """Create comprehensive report generation interface"""
        layout = QtWidgets.QVBoxLayout(self)
        
        # Create tab widget
        self.tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(self.tab_widget)
        
        # Create tabs
        self.create_project_info_tab()
        self.create_report_content_tab()
        self.create_format_options_tab()
        self.create_advanced_options_tab()
        self.create_preview_tab()
        
        # Button box
        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )
        button_box.accepted.connect(self.generate_report)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
    
    def create_project_info_tab(self):
        """Project information and header settings"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Project Information Group
        project_group = QtWidgets.QGroupBox("Project Information")
        project_layout = QtWidgets.QFormLayout(project_group)
        
        self.project_name_input = QtWidgets.QLineEdit()
        self.project_name_input.setPlaceholderText("Enter project name")
        project_layout.addRow("Project Name:", self.project_name_input)
        
        self.project_number_input = QtWidgets.QLineEdit()
        self.project_number_input.setPlaceholderText("Project reference number")
        project_layout.addRow("Project Number:", self.project_number_input)
        
        self.project_location_input = QtWidgets.QLineEdit()
        self.project_location_input.setPlaceholderText("Project location/address")
        project_layout.addRow("Location:", self.project_location_input)
        
        self.client_name_input = QtWidgets.QLineEdit()
        self.client_name_input.setPlaceholderText("Client organization")
        project_layout.addRow("Client:", self.client_name_input)
        
        layout.addWidget(project_group)
        
        # Engineer Information Group
        engineer_group = QtWidgets.QGroupBox("Engineer Information")
        engineer_layout = QtWidgets.QFormLayout(engineer_group)
        
        self.engineer_name_input = QtWidgets.QLineEdit()
        self.engineer_name_input.setPlaceholderText("Responsible engineer")
        engineer_layout.addRow("Engineer Name:", self.engineer_name_input)
        
        self.engineer_license_input = QtWidgets.QLineEdit()
        self.engineer_license_input.setPlaceholderText("Professional license number")
        engineer_layout.addRow("License Number:", self.engineer_license_input)
        
        self.company_name_input = QtWidgets.QLineEdit()
        self.company_name_input.setPlaceholderText("Engineering firm name")
        engineer_layout.addRow("Company:", self.company_name_input)
        
        self.company_address_input = QtWidgets.QTextEdit()
        self.company_address_input.setMaximumHeight(60)
        self.company_address_input.setPlaceholderText("Company address")
        engineer_layout.addRow("Address:", self.company_address_input)
        
        layout.addWidget(engineer_group)
        
        # Report Settings Group
        settings_group = QtWidgets.QGroupBox("Report Settings")
        settings_layout = QtWidgets.QFormLayout(settings_group)
        
        self.report_title_input = QtWidgets.QLineEdit()
        self.report_title_input.setText("Structural Analysis Report")
        settings_layout.addRow("Report Title:", self.report_title_input)
        
        self.report_date_input = QtWidgets.QDateEdit()
        self.report_date_input.setDate(QtCore.QDate.currentDate())
        self.report_date_input.setCalendarPopup(True)
        settings_layout.addRow("Report Date:", self.report_date_input)
        
        self.revision_input = QtWidgets.QLineEdit()
        self.revision_input.setText("Rev. 0")
        settings_layout.addRow("Revision:", self.revision_input)
        
        layout.addWidget(settings_group)
        
        self.tab_widget.addTab(tab, "Project Info")
    
    def create_report_content_tab(self):
        """Report content selection and structure"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Content Selection Group
        content_group = QtWidgets.QGroupBox("Report Content Selection")
        content_layout = QtWidgets.QVBoxLayout(content_group)
        
        # Section checkboxes in two columns
        sections_layout = QtWidgets.QGridLayout()
        
        # Standard sections
        self.sections = {
            'executive_summary': QtWidgets.QCheckBox("Executive Summary"),
            'project_description': QtWidgets.QCheckBox("Project Description"),
            'design_criteria': QtWidgets.QCheckBox("Design Criteria & Codes"),
            'structural_model': QtWidgets.QCheckBox("Structural Model Description"),
            'load_analysis': QtWidgets.QCheckBox("Load Analysis & Combinations"),
            'analysis_methods': QtWidgets.QCheckBox("Analysis Methods"),
            'analysis_results': QtWidgets.QCheckBox("Analysis Results"),
            'member_design': QtWidgets.QCheckBox("Member Design Checks"),
            'connection_design': QtWidgets.QCheckBox("Connection Design"),
            'serviceability': QtWidgets.QCheckBox("Serviceability Checks"),
            'foundations': QtWidgets.QCheckBox("Foundation Design"),
            'recommendations': QtWidgets.QCheckBox("Recommendations"),
            'references': QtWidgets.QCheckBox("References & Standards"),
            'appendices': QtWidgets.QCheckBox("Appendices & Calculations")
        }
        
        # Add checkboxes to grid
        for i, (key, checkbox) in enumerate(self.sections.items()):
            checkbox.setChecked(True)  # Default all checked
            sections_layout.addWidget(checkbox, i // 2, i % 2)
        
        content_layout.addLayout(sections_layout)
        
        # Quick selection buttons
        quick_buttons_layout = QtWidgets.QHBoxLayout()
        
        self.select_all_btn = QtWidgets.QPushButton("Select All")
        self.select_all_btn.clicked.connect(self.select_all_sections)
        quick_buttons_layout.addWidget(self.select_all_btn)
        
        self.select_none_btn = QtWidgets.QPushButton("Select None")
        self.select_none_btn.clicked.connect(self.select_no_sections)
        quick_buttons_layout.addWidget(self.select_none_btn)
        
        self.select_standard_btn = QtWidgets.QPushButton("Standard Report")
        self.select_standard_btn.clicked.connect(self.select_standard_sections)
        quick_buttons_layout.addWidget(self.select_standard_btn)
        
        self.select_preliminary_btn = QtWidgets.QPushButton("Preliminary Report")
        self.select_preliminary_btn.clicked.connect(self.select_preliminary_sections)
        quick_buttons_layout.addWidget(self.select_preliminary_btn)
        
        content_layout.addLayout(quick_buttons_layout)
        layout.addWidget(content_group)
        
        # Analysis Results Selection
        results_group = QtWidgets.QGroupBox("Analysis Results to Include")
        results_layout = QtWidgets.QVBoxLayout(results_group)
        
        self.results_selection = {
            'displacement_diagrams': QtWidgets.QCheckBox("Displacement Diagrams"),
            'moment_diagrams': QtWidgets.QCheckBox("Moment Diagrams"),
            'shear_diagrams': QtWidgets.QCheckBox("Shear Force Diagrams"),
            'axial_diagrams': QtWidgets.QCheckBox("Axial Force Diagrams"),
            'stress_contours': QtWidgets.QCheckBox("Stress Contour Plots"),
            'reaction_summary': QtWidgets.QCheckBox("Reaction Summary Tables"),
            'member_forces': QtWidgets.QCheckBox("Member Force Tables"),
            'design_ratios': QtWidgets.QCheckBox("Design Ratio Summary"),
            'modal_results': QtWidgets.QCheckBox("Modal Analysis Results"),
            'buckling_results': QtWidgets.QCheckBox("Buckling Analysis Results")
        }
        
        results_grid = QtWidgets.QGridLayout()
        for i, (key, checkbox) in enumerate(self.results_selection.items()):
            checkbox.setChecked(True)
            results_grid.addWidget(checkbox, i // 2, i % 2)
        
        results_layout.addLayout(results_grid)
        layout.addWidget(results_group)
        
        # Structural Objects Selection
        objects_group = QtWidgets.QGroupBox("Structural Objects to Include")
        objects_layout = QtWidgets.QVBoxLayout(objects_group)
        
        self.objects_list = QtWidgets.QListWidget()
        self.objects_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.populate_structural_objects()
        objects_layout.addWidget(self.objects_list)
        
        objects_buttons = QtWidgets.QHBoxLayout()
        self.select_all_objects_btn = QtWidgets.QPushButton("Select All Objects")
        self.select_all_objects_btn.clicked.connect(self.select_all_objects)
        objects_buttons.addWidget(self.select_all_objects_btn)
        
        self.select_analyzed_only_btn = QtWidgets.QPushButton("Analyzed Objects Only")
        self.select_analyzed_only_btn.clicked.connect(self.select_analyzed_objects)
        objects_buttons.addWidget(self.select_analyzed_only_btn)
        
        objects_layout.addLayout(objects_buttons)
        layout.addWidget(objects_group)
        
        self.tab_widget.addTab(tab, "Content")
    
    def create_format_options_tab(self):
        """Report format and output options"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Output Format Group
        format_group = QtWidgets.QGroupBox("Output Format")
        format_layout = QtWidgets.QVBoxLayout(format_group)
        
        self.format_buttons = QtWidgets.QButtonGroup()
        
        self.pdf_radio = QtWidgets.QRadioButton("PDF Report (Recommended)")
        self.pdf_radio.setChecked(True)
        self.pdf_radio.setToolTip("Professional PDF report with high-quality diagrams")
        format_layout.addWidget(self.pdf_radio)
        self.format_buttons.addButton(self.pdf_radio, 0)
        
        self.html_radio = QtWidgets.QRadioButton("Interactive HTML Report")
        self.html_radio.setToolTip("Web-based report with interactive charts and navigation")
        format_layout.addWidget(self.html_radio)
        self.format_buttons.addButton(self.html_radio, 1)
        
        self.excel_radio = QtWidgets.QRadioButton("Excel Workbook")
        self.excel_radio.setToolTip("Spreadsheet format with calculation tables")
        format_layout.addWidget(self.excel_radio)
        self.format_buttons.addButton(self.excel_radio, 2)
        
        self.multi_format_radio = QtWidgets.QRadioButton("Multiple Formats")
        self.multi_format_radio.setToolTip("Generate all formats simultaneously")
        format_layout.addWidget(self.multi_format_radio)
        self.format_buttons.addButton(self.multi_format_radio, 3)
        
        layout.addWidget(format_group)
        
        # PDF Specific Options
        self.pdf_options_group = QtWidgets.QGroupBox("PDF Options")
        pdf_options_layout = QtWidgets.QFormLayout(self.pdf_options_group)
        
        self.paper_size_combo = QtWidgets.QComboBox()
        self.paper_size_combo.addItems(["Letter (8.5×11\")", "A4 (210×297mm)", "Legal (8.5×14\")", "Tabloid (11×17\")"])
        pdf_options_layout.addRow("Paper Size:", self.paper_size_combo)
        
        self.page_orientation_combo = QtWidgets.QComboBox()
        self.page_orientation_combo.addItems(["Portrait", "Landscape"])
        pdf_options_layout.addRow("Orientation:", self.page_orientation_combo)
        
        self.diagram_quality_combo = QtWidgets.QComboBox()
        self.diagram_quality_combo.addItems(["Standard (150 DPI)", "High Quality (300 DPI)", "Print Quality (600 DPI)"])
        self.diagram_quality_combo.setCurrentIndex(1)
        pdf_options_layout.addRow("Diagram Quality:", self.diagram_quality_combo)
        
        self.include_toc_check = QtWidgets.QCheckBox("Include Table of Contents")
        self.include_toc_check.setChecked(True)
        pdf_options_layout.addRow("", self.include_toc_check)
        
        self.include_bookmarks_check = QtWidgets.QCheckBox("Include PDF Bookmarks")
        self.include_bookmarks_check.setChecked(True)
        pdf_options_layout.addRow("", self.include_bookmarks_check)
        
        layout.addWidget(self.pdf_options_group)
        
        # HTML Specific Options
        self.html_options_group = QtWidgets.QGroupBox("HTML Options")
        html_options_layout = QtWidgets.QFormLayout(self.html_options_group)
        
        self.html_theme_combo = QtWidgets.QComboBox()
        self.html_theme_combo.addItems(["Professional", "Modern", "Classic", "Minimalist"])
        html_options_layout.addRow("Theme:", self.html_theme_combo)
        
        self.include_interactive_charts = QtWidgets.QCheckBox("Interactive Charts (Chart.js)")
        self.include_interactive_charts.setChecked(True)
        html_options_layout.addRow("", self.include_interactive_charts)
        
        self.include_3d_viewer = QtWidgets.QCheckBox("3D Model Viewer (Three.js)")
        self.include_3d_viewer.setChecked(False)
        html_options_layout.addRow("", self.include_3d_viewer)
        
        self.responsive_design = QtWidgets.QCheckBox("Responsive Design (Mobile-friendly)")
        self.responsive_design.setChecked(True)
        html_options_layout.addRow("", self.responsive_design)
        
        layout.addWidget(self.html_options_group)
        
        # Output Location Group
        output_group = QtWidgets.QGroupBox("Output Location")
        output_layout = QtWidgets.QFormLayout(output_group)
        
        output_path_layout = QtWidgets.QHBoxLayout()
        self.output_path_input = QtWidgets.QLineEdit()
        self.output_path_input.setPlaceholderText("Select output directory...")
        output_path_layout.addWidget(self.output_path_input)
        
        self.browse_output_btn = QtWidgets.QPushButton("Browse...")
        self.browse_output_btn.clicked.connect(self.browse_output_directory)
        output_path_layout.addWidget(self.browse_output_btn)
        
        output_layout.addRow("Output Directory:", output_path_layout)
        
        self.filename_input = QtWidgets.QLineEdit()
        self.filename_input.setText("StructuralAnalysisReport")
        self.filename_input.setPlaceholderText("Report filename (without extension)")
        output_layout.addRow("Filename:", self.filename_input)
        
        self.open_after_generation = QtWidgets.QCheckBox("Open report after generation")
        self.open_after_generation.setChecked(True)
        output_layout.addRow("", self.open_after_generation)
        
        layout.addWidget(output_group)
        
        self.tab_widget.addTab(tab, "Format & Output")
    
    def create_advanced_options_tab(self):
        """Advanced report generation options"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Calculation Details Group
        calc_group = QtWidgets.QGroupBox("Calculation Detail Level")
        calc_layout = QtWidgets.QVBoxLayout(calc_group)
        
        self.detail_level_group = QtWidgets.QButtonGroup()
        
        self.summary_only_radio = QtWidgets.QRadioButton("Summary Only")
        self.summary_only_radio.setToolTip("High-level results and conclusions")
        calc_layout.addWidget(self.summary_only_radio)
        self.detail_level_group.addButton(self.summary_only_radio, 0)
        
        self.standard_detail_radio = QtWidgets.QRadioButton("Standard Detail")
        self.standard_detail_radio.setChecked(True)
        self.standard_detail_radio.setToolTip("Typical engineering report detail")
        calc_layout.addWidget(self.standard_detail_radio)
        self.detail_level_group.addButton(self.standard_detail_radio, 1)
        
        self.full_detail_radio = QtWidgets.QRadioButton("Full Detail")
        self.full_detail_radio.setToolTip("Comprehensive calculations and intermediate steps")
        calc_layout.addWidget(self.full_detail_radio)
        self.detail_level_group.addButton(self.full_detail_radio, 2)
        
        layout.addWidget(calc_group)
        
        # Units and Precision Group
        units_group = QtWidgets.QGroupBox("Units and Precision")
        units_layout = QtWidgets.QFormLayout(units_group)
        
        self.unit_system_combo = QtWidgets.QComboBox()
        self.unit_system_combo.addItems(["Imperial (US)", "Metric (SI)", "Mixed (Imperial forces, Metric dimensions)"])
        units_layout.addRow("Unit System:", self.unit_system_combo)
        
        self.force_precision_spin = QtWidgets.QSpinBox()
        self.force_precision_spin.setRange(0, 6)
        self.force_precision_spin.setValue(2)
        units_layout.addRow("Force Precision (decimals):", self.force_precision_spin)
        
        self.moment_precision_spin = QtWidgets.QSpinBox()
        self.moment_precision_spin.setRange(0, 6)
        self.moment_precision_spin.setValue(2)
        units_layout.addRow("Moment Precision (decimals):", self.moment_precision_spin)
        
        self.displacement_precision_spin = QtWidgets.QSpinBox()
        self.displacement_precision_spin.setRange(0, 8)
        self.displacement_precision_spin.setValue(4)
        units_layout.addRow("Displacement Precision:", self.displacement_precision_spin)
        
        layout.addWidget(units_group)
        
        # Design Code Options Group
        code_group = QtWidgets.QGroupBox("Design Code References")
        code_layout = QtWidgets.QVBoxLayout(code_group)
        
        self.design_codes = {
            'aisc_360': QtWidgets.QCheckBox("AISC 360 (Steel Design)"),
            'aci_318': QtWidgets.QCheckBox("ACI 318 (Concrete Design)"),
            'asce_7': QtWidgets.QCheckBox("ASCE 7 (Loads)"),
            'ibc': QtWidgets.QCheckBox("International Building Code"),
            'eurocode': QtWidgets.QCheckBox("Eurocode Standards"),
            'csa': QtWidgets.QCheckBox("CSA Standards (Canada)")
        }
        
        codes_grid = QtWidgets.QGridLayout()
        for i, (key, checkbox) in enumerate(self.design_codes.items()):
            codes_grid.addWidget(checkbox, i // 2, i % 2)
        
        code_layout.addLayout(codes_grid)
        layout.addWidget(code_group)
        
        # Custom Template Group
        template_group = QtWidgets.QGroupBox("Custom Template Options")
        template_layout = QtWidgets.QFormLayout(template_group)
        
        self.use_custom_template = QtWidgets.QCheckBox("Use Custom Template")
        template_layout.addRow("", self.use_custom_template)
        
        template_path_layout = QtWidgets.QHBoxLayout()
        self.template_path_input = QtWidgets.QLineEdit()
        self.template_path_input.setEnabled(False)
        self.template_path_input.setPlaceholderText("Select custom template file...")
        template_path_layout.addWidget(self.template_path_input)
        
        self.browse_template_btn = QtWidgets.QPushButton("Browse...")
        self.browse_template_btn.setEnabled(False)
        self.browse_template_btn.clicked.connect(self.browse_template_file)
        template_path_layout.addWidget(self.browse_template_btn)
        
        template_layout.addRow("Template File:", template_path_layout)
        
        # Connect template checkbox
        self.use_custom_template.toggled.connect(self.template_path_input.setEnabled)
        self.use_custom_template.toggled.connect(self.browse_template_btn.setEnabled)
        
        layout.addWidget(template_group)
        
        # Logo and Branding Group
        branding_group = QtWidgets.QGroupBox("Logo and Branding")
        branding_layout = QtWidgets.QFormLayout(branding_group)
        
        self.include_company_logo = QtWidgets.QCheckBox("Include Company Logo")
        branding_layout.addRow("", self.include_company_logo)
        
        logo_path_layout = QtWidgets.QHBoxLayout()
        self.logo_path_input = QtWidgets.QLineEdit()
        self.logo_path_input.setEnabled(False)
        self.logo_path_input.setPlaceholderText("Select company logo file...")
        logo_path_layout.addWidget(self.logo_path_input)
        
        self.browse_logo_btn = QtWidgets.QPushButton("Browse...")
        self.browse_logo_btn.setEnabled(False)
        self.browse_logo_btn.clicked.connect(self.browse_logo_file)
        logo_path_layout.addWidget(self.browse_logo_btn)
        
        branding_layout.addRow("Logo File:", logo_path_layout)
        
        # Connect logo checkbox
        self.include_company_logo.toggled.connect(self.logo_path_input.setEnabled)
        self.include_company_logo.toggled.connect(self.browse_logo_btn.setEnabled)
        
        layout.addWidget(branding_group)
        
        self.tab_widget.addTab(tab, "Advanced")
    
    def create_preview_tab(self):
        """Report preview and generation status"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Preview Text Group
        preview_group = QtWidgets.QGroupBox("Report Structure Preview")
        preview_layout = QtWidgets.QVBoxLayout(preview_group)
        
        self.preview_text = QtWidgets.QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setMaximumHeight(200)
        preview_layout.addWidget(self.preview_text)
        
        self.update_preview_btn = QtWidgets.QPushButton("Update Preview")
        self.update_preview_btn.clicked.connect(self.update_preview)
        preview_layout.addWidget(self.update_preview_btn)
        
        layout.addWidget(preview_group)
        
        # Generation Status Group
        status_group = QtWidgets.QGroupBox("Generation Status")
        status_layout = QtWidgets.QVBoxLayout(status_group)
        
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setVisible(False)
        status_layout.addWidget(self.progress_bar)
        
        self.status_text = QtWidgets.QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setMaximumHeight(150)
        self.status_text.setPlainText("Ready to generate report...")
        status_layout.addWidget(self.status_text)
        
        layout.addWidget(status_group)
        
        # Quick Actions Group
        actions_group = QtWidgets.QGroupBox("Quick Actions")
        actions_layout = QtWidgets.QHBoxLayout(actions_group)
        
        self.validate_btn = QtWidgets.QPushButton("Validate Settings")
        self.validate_btn.clicked.connect(self.validate_settings)
        actions_layout.addWidget(self.validate_btn)
        
        self.estimate_size_btn = QtWidgets.QPushButton("Estimate File Size")
        self.estimate_size_btn.clicked.connect(self.estimate_file_size)
        actions_layout.addWidget(self.estimate_size_btn)
        
        self.test_generation_btn = QtWidgets.QPushButton("Test Generation")
        self.test_generation_btn.clicked.connect(self.test_report_generation)
        actions_layout.addWidget(self.test_generation_btn)
        
        layout.addWidget(actions_group)
        
        self.tab_widget.addTab(tab, "Preview & Status")
    
    def scan_structural_objects(self):
        """Scan document for structural objects"""
        self.structural_objects = []
        
        if not App.ActiveDocument:
            return
        
        for obj in App.ActiveDocument.Objects:
            # Check for structural object types
            if hasattr(obj, 'Proxy') and obj.Proxy:
                proxy_type = getattr(obj.Proxy, 'Type', '')
                if any(struct_type in proxy_type for struct_type in 
                      ['StructuralBeam', 'StructuralColumn', 'StructuralPlate', 'StructuralMaterial']):
                    self.structural_objects.append(obj)
            
            # Check for FEM objects
            if obj.TypeId.startswith('Fem::'):
                self.structural_objects.append(obj)
            
            # Check for calc objects (from StructureTools)
            if hasattr(obj, 'Type') and 'Calc' in getattr(obj, 'Type', ''):
                self.analysis_results[obj.Label] = obj
    
    def populate_default_values(self):
        """Populate default values from FreeCAD document"""
        if App.ActiveDocument:
            self.project_name_input.setText(App.ActiveDocument.Name)
            
        # Set default output path
        if App.ActiveDocument:
            doc_path = App.ActiveDocument.FileName
            if doc_path:
                import os
                output_dir = os.path.dirname(doc_path)
                self.output_path_input.setText(output_dir)
        else:
            self.output_path_input.setText(os.path.expanduser("~/Documents"))
    
    def populate_structural_objects(self):
        """Populate structural objects list"""
        self.objects_list.clear()
        
        for obj in self.structural_objects:
            item = QtWidgets.QListWidgetItem(f"{obj.Label} ({obj.TypeId})")
            item.setData(QtCore.Qt.UserRole, obj)
            item.setSelected(True)  # Default all selected
            self.objects_list.addItem(item)
    
    def connect_signals(self):
        """Connect UI signals"""
        # Format radio buttons
        self.format_buttons.buttonClicked.connect(self.on_format_changed)
        
        # Tab change updates preview
        self.tab_widget.currentChanged.connect(self.update_preview)
    
    def on_format_changed(self, button):
        """Handle format selection change"""
        format_id = self.format_buttons.id(button)
        
        # Show/hide format-specific options
        self.pdf_options_group.setVisible(format_id in [0, 3])
        self.html_options_group.setVisible(format_id in [1, 3])
    
    def select_all_sections(self):
        """Select all report sections"""
        for checkbox in self.sections.values():
            checkbox.setChecked(True)
    
    def select_no_sections(self):
        """Deselect all report sections"""
        for checkbox in self.sections.values():
            checkbox.setChecked(False)
    
    def select_standard_sections(self):
        """Select standard report sections"""
        standard_sections = [
            'executive_summary', 'project_description', 'design_criteria',
            'structural_model', 'load_analysis', 'analysis_results',
            'member_design', 'recommendations', 'references'
        ]
        
        for key, checkbox in self.sections.items():
            checkbox.setChecked(key in standard_sections)
    
    def select_preliminary_sections(self):
        """Select preliminary report sections"""
        preliminary_sections = [
            'executive_summary', 'project_description', 'structural_model',
            'analysis_results', 'recommendations'
        ]
        
        for key, checkbox in self.sections.items():
            checkbox.setChecked(key in preliminary_sections)
    
    def select_all_objects(self):
        """Select all structural objects"""
        for i in range(self.objects_list.count()):
            item = self.objects_list.item(i)
            item.setSelected(True)
    
    def select_analyzed_objects(self):
        """Select only analyzed objects"""
        for i in range(self.objects_list.count()):
            item = self.objects_list.item(i)
            obj = item.data(QtCore.Qt.UserRole)
            
            # Check if object has analysis results
            has_results = (hasattr(obj, 'AnalysisResults') and obj.AnalysisResults) or \
                         any(calc_obj for calc_obj in self.analysis_results.values())
            
            item.setSelected(has_results)
    
    def browse_output_directory(self):
        """Browse for output directory"""
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Output Directory", self.output_path_input.text()
        )
        if directory:
            self.output_path_input.setText(directory)
    
    def browse_template_file(self):
        """Browse for custom template file"""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Template File", "", 
            "Template Files (*.html *.jinja2 *.template);;All Files (*)"
        )
        if file_path:
            self.template_path_input.setText(file_path)
    
    def browse_logo_file(self):
        """Browse for logo file"""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Logo File", "", 
            "Image Files (*.png *.jpg *.jpeg *.svg *.bmp);;All Files (*)"
        )
        if file_path:
            self.logo_path_input.setText(file_path)
    
    def update_preview(self):
        """Update report structure preview"""
        preview_text = "REPORT STRUCTURE PREVIEW\n" + "="*50 + "\n\n"
        
        # Add header information
        preview_text += f"Project: {self.project_name_input.text()}\n"
        preview_text += f"Engineer: {self.engineer_name_input.text()}\n"
        preview_text += f"Date: {self.report_date_input.date().toString()}\n\n"
        
        # Add selected sections
        preview_text += "REPORT SECTIONS:\n" + "-"*20 + "\n"
        section_names = {
            'executive_summary': '1. Executive Summary',
            'project_description': '2. Project Description',
            'design_criteria': '3. Design Criteria & Codes',
            'structural_model': '4. Structural Model',
            'load_analysis': '5. Load Analysis',
            'analysis_methods': '6. Analysis Methods',
            'analysis_results': '7. Analysis Results',
            'member_design': '8. Member Design',
            'connection_design': '9. Connection Design',
            'serviceability': '10. Serviceability Checks',
            'foundations': '11. Foundation Design',
            'recommendations': '12. Recommendations',
            'references': '13. References',
            'appendices': '14. Appendices'
        }
        
        for key, checkbox in self.sections.items():
            if checkbox.isChecked():
                preview_text += f"✓ {section_names.get(key, key.title())}\n"
        
        # Add format information
        preview_text += f"\nOUTPUT FORMAT: {self.get_selected_format()}\n"
        preview_text += f"OUTPUT LOCATION: {self.output_path_input.text()}/{self.filename_input.text()}\n"
        
        # Add object count
        selected_objects = len([item for item in range(self.objects_list.count()) 
                              if self.objects_list.item(item).isSelected()])
        preview_text += f"STRUCTURAL OBJECTS: {selected_objects} selected\n"
        
        self.preview_text.setPlainText(preview_text)
    
    def validate_settings(self):
        """Validate report generation settings"""
        errors = []
        warnings = []
        
        # Check required fields
        if not self.project_name_input.text().strip():
            errors.append("Project name is required")
        
        if not self.engineer_name_input.text().strip():
            warnings.append("Engineer name is recommended")
        
        if not self.output_path_input.text().strip():
            errors.append("Output directory must be specified")
        elif not os.path.exists(self.output_path_input.text()):
            errors.append("Output directory does not exist")
        
        if not self.filename_input.text().strip():
            errors.append("Filename is required")
        
        # Check if any sections are selected
        if not any(cb.isChecked() for cb in self.sections.values()):
            errors.append("At least one report section must be selected")
        
        # Check if any objects are selected
        selected_objects = [item for item in range(self.objects_list.count()) 
                          if self.objects_list.item(item).isSelected()]
        if not selected_objects:
            warnings.append("No structural objects selected")
        
        # Display validation results
        status_text = "VALIDATION RESULTS\n" + "="*30 + "\n"
        
        if errors:
            status_text += "\nERRORS:\n"
            for error in errors:
                status_text += f"❌ {error}\n"
        
        if warnings:
            status_text += "\nWARNINGS:\n"
            for warning in warnings:
                status_text += f"⚠️ {warning}\n"
        
        if not errors and not warnings:
            status_text += "\n✅ All settings are valid. Ready to generate report."
        elif not errors:
            status_text += "\n⚠️ Settings are valid with warnings."
        else:
            status_text += "\n❌ Please fix errors before generating report."
        
        self.status_text.setPlainText(status_text)
    
    def estimate_file_size(self):
        """Estimate output file size"""
        # Simple estimation based on content
        base_size = 500  # KB for basic report
        
        # Add size for each section
        selected_sections = sum(1 for cb in self.sections.values() if cb.isChecked())
        base_size += selected_sections * 50
        
        # Add size for diagrams
        selected_results = sum(1 for cb in self.results_selection.values() if cb.isChecked())
        base_size += selected_results * 200
        
        # Add size for objects
        selected_objects = len([item for item in range(self.objects_list.count()) 
                              if self.objects_list.item(item).isSelected()])
        base_size += selected_objects * 10
        
        # Format multiplier
        format_multipliers = {'PDF': 1.0, 'HTML': 0.3, 'Excel': 0.5, 'Multiple': 1.8}
        multiplier = format_multipliers.get(self.get_selected_format(), 1.0)
        
        estimated_size = int(base_size * multiplier)
        
        if estimated_size < 1024:
            size_text = f"{estimated_size} KB"
        else:
            size_text = f"{estimated_size/1024:.1f} MB"
        
        self.status_text.setPlainText(f"Estimated file size: {size_text}\n\n"
                                    f"Calculation based on:\n"
                                    f"- {selected_sections} report sections\n"
                                    f"- {selected_results} result types\n"
                                    f"- {selected_objects} structural objects\n"
                                    f"- {self.get_selected_format()} format")
    
    def test_report_generation(self):
        """Test report generation with minimal content"""
        self.status_text.setPlainText("Testing report generation capabilities...\n")
        
        try:
            if REPORTING_AVAILABLE:
                # Test with actual report generator
                generator = StructuralReportGenerator()
                test_result = "✅ Report generator initialized successfully\n"
                test_result += "✅ All dependencies available\n"
                test_result += "✅ Ready for full report generation"
            else:
                test_result = "⚠️ Using mock report generator\n"
                test_result += "⚠️ Install reporting dependencies for full functionality\n"
                test_result += "⚠️ Basic report structure will be generated"
            
            self.status_text.append(test_result)
            
        except Exception as e:
            self.status_text.append(f"❌ Test failed: {str(e)}")
    
    def get_selected_format(self):
        """Get selected output format"""
        if self.pdf_radio.isChecked():
            return "PDF"
        elif self.html_radio.isChecked():
            return "HTML"
        elif self.excel_radio.isChecked():
            return "Excel"
        elif self.multi_format_radio.isChecked():
            return "Multiple"
        return "PDF"
    
    def generate_report(self):
        """Generate the structural report"""
        # Validate settings first
        self.validate_settings()
        
        # Check for errors in validation
        validation_text = self.status_text.toPlainText()
        if "❌" in validation_text and "Please fix errors" in validation_text:
            QtWidgets.QMessageBox.warning(
                self, "Validation Errors", 
                "Please fix validation errors before generating the report."
            )
            return
        
        # Show progress
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.status_text.append("\n" + "="*50)
        self.status_text.append("STARTING REPORT GENERATION...")
        
        try:
            # Initialize report generator
            self.progress_bar.setValue(10)
            self.status_text.append("Initializing report generator...")
            
            if REPORTING_AVAILABLE:
                generator = StructuralReportGenerator()
            else:
                # Use mock implementation
                generator = type('MockGenerator', (), {
                    'generate_analysis_report': lambda self, path, fmt: self.generate_mock_report(path)
                })()
            
            # Configure report
            self.progress_bar.setValue(20)
            self.status_text.append("Configuring report settings...")
            
            config = self.create_report_configuration()
            
            # Collect structural data
            self.progress_bar.setValue(30)
            self.status_text.append("Collecting structural data...")
            
            selected_objects = self.get_selected_objects()
            
            # Generate report based on format
            self.progress_bar.setValue(50)
            format_type = self.get_selected_format()
            
            output_dir = self.output_path_input.text()
            filename = self.filename_input.text()
            
            if format_type == "PDF":
                output_path = os.path.join(output_dir, f"{filename}.pdf")
                self.status_text.append(f"Generating PDF report: {output_path}")
                success = self.generate_pdf_report(generator, output_path, config, selected_objects)
                
            elif format_type == "HTML":
                output_path = os.path.join(output_dir, f"{filename}.html")
                self.status_text.append(f"Generating HTML report: {output_path}")
                success = self.generate_html_report(generator, output_path, config, selected_objects)
                
            elif format_type == "Excel":
                output_path = os.path.join(output_dir, f"{filename}.xlsx")
                self.status_text.append(f"Generating Excel report: {output_path}")
                success = self.generate_excel_report(generator, output_path, config, selected_objects)
                
            elif format_type == "Multiple":
                self.status_text.append("Generating multiple formats...")
                success = True
                for fmt, ext in [("PDF", ".pdf"), ("HTML", ".html"), ("Excel", ".xlsx")]:
                    output_path = os.path.join(output_dir, f"{filename}{ext}")
                    self.status_text.append(f"  Generating {fmt}: {output_path}")
                    if fmt == "PDF":
                        success &= self.generate_pdf_report(generator, output_path, config, selected_objects)
                    elif fmt == "HTML":
                        success &= self.generate_html_report(generator, output_path, config, selected_objects)
                    elif fmt == "Excel":
                        success &= self.generate_excel_report(generator, output_path, config, selected_objects)
            
            # Finalize
            self.progress_bar.setValue(100)
            
            if success:
                self.status_text.append("✅ Report generated successfully!")
                
                if self.open_after_generation.isChecked():
                    self.open_generated_report(output_path if format_type != "Multiple" else 
                                             os.path.join(output_dir, f"{filename}.pdf"))
                
                QtWidgets.QMessageBox.information(
                    self, "Success", 
                    f"Report generated successfully!\n\nLocation: {output_dir}"
                )
                
                self.accept()  # Close dialog
            else:
                self.status_text.append("❌ Report generation failed!")
                QtWidgets.QMessageBox.critical(
                    self, "Generation Failed", 
                    "Report generation failed. Check the status log for details."
                )
            
        except Exception as e:
            self.progress_bar.setValue(0)
            self.status_text.append(f"❌ Error during generation: {str(e)}")
            App.Console.PrintError(f"Report generation error: {str(e)}\n")
            
            QtWidgets.QMessageBox.critical(
                self, "Error", 
                f"An error occurred during report generation:\n{str(e)}"
            )
        
        finally:
            self.progress_bar.setVisible(False)
    
    def create_report_configuration(self):
        """Create report configuration from UI settings"""
        config = ReportConfiguration() if REPORTING_AVAILABLE else type('Config', (), {})()
        
        # Project information
        config.project_name = self.project_name_input.text()
        config.project_number = self.project_number_input.text()
        config.project_location = self.project_location_input.text()
        config.client_name = self.client_name_input.text()
        
        # Engineer information
        config.engineer_name = self.engineer_name_input.text()
        config.engineer_license = self.engineer_license_input.text()
        config.company_name = self.company_name_input.text()
        config.company_address = self.company_address_input.toPlainText()
        
        # Report settings
        config.report_title = self.report_title_input.text()
        config.report_date = self.report_date_input.date().toPython()
        config.revision = self.revision_input.text()
        
        # Selected sections
        config.selected_sections = {key: cb.isChecked() for key, cb in self.sections.items()}
        
        # Selected results
        config.selected_results = {key: cb.isChecked() for key, cb in self.results_selection.items()}
        
        return config
    
    def get_selected_objects(self):
        """Get list of selected structural objects"""
        selected_objects = []
        for i in range(self.objects_list.count()):
            item = self.objects_list.item(i)
            if item.isSelected():
                obj = item.data(QtCore.Qt.UserRole)
                selected_objects.append(obj)
        return selected_objects
    
    def generate_pdf_report(self, generator, output_path, config, objects):
        """Generate PDF report"""
        try:
            if REPORTING_AVAILABLE:
                return generator.generate_analysis_report(output_path, ReportFormat.PDF)
            else:
                # Mock PDF generation
                with open(output_path, 'w') as f:
                    f.write("Mock PDF Report\n")
                    f.write(f"Project: {config.project_name}\n")
                    f.write(f"Engineer: {config.engineer_name}\n")
                    f.write(f"Objects: {len(objects)}\n")
                return True
        except Exception as e:
            self.status_text.append(f"PDF generation error: {str(e)}")
            return False
    
    def generate_html_report(self, generator, output_path, config, objects):
        """Generate HTML report"""
        try:
            if REPORTING_AVAILABLE:
                return generator.generate_analysis_report(output_path, ReportFormat.HTML)
            else:
                # Mock HTML generation
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head><title>{config.project_name} - Structural Report</title></head>
                <body>
                    <h1>{config.project_name}</h1>
                    <p>Engineer: {config.engineer_name}</p>
                    <p>Objects: {len(objects)}</p>
                    <p>This is a mock HTML report.</p>
                </body>
                </html>
                """
                with open(output_path, 'w') as f:
                    f.write(html_content)
                return True
        except Exception as e:
            self.status_text.append(f"HTML generation error: {str(e)}")
            return False
    
    def generate_excel_report(self, generator, output_path, config, objects):
        """Generate Excel report"""
        try:
            if REPORTING_AVAILABLE:
                return generator.generate_analysis_report(output_path, ReportFormat.EXCEL)
            else:
                # Mock Excel generation (CSV)
                csv_content = f"Project,{config.project_name}\n"
                csv_content += f"Engineer,{config.engineer_name}\n"
                csv_content += f"Objects,{len(objects)}\n"
                csv_content += "Mock Excel Report\n"
                with open(output_path.replace('.xlsx', '.csv'), 'w') as f:
                    f.write(csv_content)
                return True
        except Exception as e:
            self.status_text.append(f"Excel generation error: {str(e)}")
            return False
    
    def open_generated_report(self, output_path):
        """Open the generated report"""
        try:
            if os.path.exists(output_path):
                if sys.platform.startswith('darwin'):  # macOS
                    os.system(f'open "{output_path}"')
                elif os.name == 'nt':  # Windows
                    os.startfile(output_path)
                else:  # Linux and others
                    os.system(f'xdg-open "{output_path}"')
            else:
                # For mock CSV files
                csv_path = output_path.replace('.xlsx', '.csv')
                if os.path.exists(csv_path):
                    webbrowser.open(f'file://{os.path.abspath(csv_path)}')
        except Exception as e:
            App.Console.PrintWarning(f"Could not open report: {str(e)}\n")


class GenerateReportCommand:
    """Command to generate comprehensive structural reports"""
    
    def GetResources(self):
        return {
            "Pixmap": os.path.join(os.path.dirname(__file__), "resources", "icons", "report_generator.svg"),
            "MenuText": "Generate Report",
            "Accel": "Ctrl+Shift+R",
            "ToolTip": "Generate comprehensive structural analysis report",
            "CmdType": "ForEdit"
        }
    
    def Activated(self):
        """Execute the report generation command"""
        try:
            # Check if document exists
            if not App.ActiveDocument:
                QtWidgets.QMessageBox.warning(
                    None, "No Document", 
                    "Please open or create a FreeCAD document before generating a report."
                )
                return
            
            # Show report generation dialog
            dialog = ReportGeneratorDialog(Gui.getMainWindow())
            dialog.show()
            
        except Exception as e:
            App.Console.PrintError(f"Error launching report generator: {str(e)}\n")
            QtWidgets.QMessageBox.critical(
                None, "Error", 
                f"Failed to launch report generator:\n{str(e)}"
            )
    
    def IsActive(self):
        """Check if command should be active"""
        return App.ActiveDocument is not None


# Register the command
Gui.addCommand("GenerateStructuralReport", GenerateReportCommand())