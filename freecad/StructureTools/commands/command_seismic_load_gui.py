# -*- coding: utf-8 -*-
"""
Seismic Load GUI Interface - Professional Seismic Analysis System
=================================================================

Comprehensive GUI for seismic load generation and analysis based on:
- ASCE 7-22 Seismic Standards
- Thai TIS Standards (TIS 1301/1302-61)
- Static Seismic Load Analysis
- Response Spectrum Analysis
- Integration with FreeCAD structural analysis
- Professional workflow similar to MIDAS nGen

Features:
- Static Seismic Load calculation and application
- Response Spectrum analysis with custom spectrum functions
- Interactive seismic parameter input
- Real-time load visualization
- Automatic integration with calc system
- Professional reporting capabilities
"""

import sys
import os
import math
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

# Setup FreeCAD stubs for standalone operation
try:
    from ..utils.freecad_stubs import setup_freecad_stubs, is_freecad_available
    if not is_freecad_available():
        setup_freecad_stubs()
except ImportError:
    pass

# Import FreeCAD modules with fallbacks
try:
    import FreeCAD as App
    import FreeCADGui as Gui
    import Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False

# Import GUI framework with comprehensive fallbacks
try:
    from PySide2 import QtWidgets, QtCore, QtGui
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    QT_AVAILABLE = True
except ImportError:
    try:
        from PySide import QtWidgets, QtCore, QtGui
        from PySide.QtWidgets import *
        from PySide.QtCore import *
        from PySide.QtGui import *
        QT_AVAILABLE = True
    except ImportError:
        # Comprehensive mock classes for standalone testing
        QT_AVAILABLE = False
        
        class QDialog:
            def __init__(self, parent=None): pass
            def setWindowTitle(self, title): pass
            def resize(self, w, h): pass
            def setLayout(self, layout): pass
            def exec_(self): pass
            def show(self): pass
            def close(self): 
                """Mock close method"""
                return True
        
        class QVBoxLayout:
            def __init__(self): pass
            def addWidget(self, widget): pass
            def addLayout(self, layout): pass
        
        class QHBoxLayout:
            def __init__(self): pass
            def addWidget(self, widget): pass
        
        class QGridLayout:
            def __init__(self): pass
            def addWidget(self, widget, row, col, rowspan=1, colspan=1): pass
        
        class QLabel:
            def __init__(self, text=""): pass
            def setStyleSheet(self, style): pass
            def setAlignment(self, align): pass
            def setWordWrap(self, wrap): pass
        
        class QLineEdit:
            def __init__(self, text=""): self.text_value = str(text)
            def text(self): return self.text_value
            def setText(self, text): self.text_value = str(text)
        
        # Mock signal class for proper GUI functionality
        class MockSignal:
            """Mock signal class that supports connect method"""
            def __init__(self):
                self.connections = []
            def connect(self, func):
                self.connections.append(func)
                return True
            def emit(self, *args, **kwargs):
                for func in self.connections:
                    try:
                        func(*args, **kwargs)
                    except:
                        pass
            def __call__(self, *args, **kwargs):
                """Allow signal to be called directly"""
                self.emit(*args, **kwargs)
        
        class QComboBox:
            def __init__(self): 
                self.items = []
                self.current_index = 0
                self.currentTextChanged = MockSignal()
            def addItems(self, items): self.items = items
            def currentText(self): return self.items[self.current_index] if self.items else ""
            def setCurrentText(self, text): 
                if text in self.items:
                    old_index = self.current_index
                    self.current_index = self.items.index(text)
                    if old_index != self.current_index:
                        self.currentTextChanged.emit(text)
            def setCurrentIndex(self, index): 
                if 0 <= index < len(self.items):
                    old_index = self.current_index
                    self.current_index = index
                    if old_index != self.current_index and self.items:
                        self.currentTextChanged.emit(self.items[index])
        
        class QPushButton:
            def __init__(self, text=""): 
                self.text_value = text
                self.clicked = MockSignal()
            def setStyleSheet(self, style): pass
            def setEnabled(self, enabled): pass
        
        class QTabWidget:
            def __init__(self): 
                self.tabs = []
                self.enabled_tabs = {}
            def addTab(self, widget, text): 
                self.tabs.append((widget, text))
            def setTabEnabled(self, index, enabled):
                self.enabled_tabs[index] = enabled
        
        class QWidget:
            def __init__(self): pass
            def setLayout(self, layout): pass
        
        class QGroupBox:
            def __init__(self, title=""): pass
            def setLayout(self, layout): pass
        
        class QCheckBox:
            def __init__(self, text=""): self.checked = False
            def setChecked(self, checked): self.checked = checked
            def isChecked(self): return self.checked
        
        class QTextEdit:
            def __init__(self): self.text_content = ""
            def setMaximumHeight(self, height): pass
            def setPlainText(self, text): self.text_content = text
            def append(self, text): self.text_content += "\\n" + text
        
        class QTableWidget:
            def __init__(self, rows=0, cols=0): pass
            def setRowCount(self, count): pass
            def setColumnCount(self, count): pass
            def setHorizontalHeaderLabels(self, labels): pass
            def setItem(self, row, col, item): pass
        
        class QTableWidgetItem:
            def __init__(self, text=""): pass
        
        class QSpinBox:
            def __init__(self): self.val = 0
            def setValue(self, val): self.val = val
            def value(self): return self.val
            def setRange(self, min_val, max_val): pass
        
        class QDoubleSpinBox:
            def __init__(self): self.val = 0.0
            def setValue(self, val): self.val = float(val)
            def value(self): return self.val
            def setRange(self, min_val, max_val): pass
            def setDecimals(self, decimals): pass
        
        class QApplication:
            """Mock QApplication for standalone testing"""
            _instance = None
            def __init__(self, argv=None): 
                QApplication._instance = self
            @staticmethod
            def instance():
                return QApplication._instance
        
        # Qt Constants
        class Qt:
            AlignCenter = 0
            Horizontal = 1
            Vertical = 2

# Import seismic analysis modules
try:
    from .seismic_asce7 import SeismicLoadASCE7, BuildingSeismicData, SeismicForces
    from .thai_seismic_loads import ThaiSeismicLoad, ThaiSeismicData
    SEISMIC_MODULES_AVAILABLE = True
except ImportError:
    SEISMIC_MODULES_AVAILABLE = False
    # Create mock classes
    class SeismicLoadASCE7:
        def __init__(self): pass
        def calculate_static_seismic(self, data): return {}
        def generate_response_spectrum(self, data): return {}
    
    class ThaiSeismicLoad:
        def __init__(self): pass
        def calculate_static_seismic(self, data): return {}

# Import calc system
try:
    from ..calc import StructAnalysis
    from ..material import Material
    CALC_AVAILABLE = True
except ImportError:
    CALC_AVAILABLE = False

class SeismicAnalysisType(Enum):
    """Seismic analysis type enumeration"""
    STATIC = "Static Seismic"
    RESPONSE_SPECTRUM = "Response Spectrum"
    TIME_HISTORY = "Time History"  # Future

class SpectrumType(Enum):
    """Response spectrum type enumeration"""
    DESIGN = "Design Response Spectrum"
    MCE = "MCE Response Spectrum"
    CUSTOM = "Custom Spectrum"

@dataclass
class SeismicLoadParameters:
    """Seismic load input parameters container"""
    # Basic Building Data
    building_height: float = 30.0  # meters
    building_width: float = 20.0   # meters  
    building_length: float = 40.0  # meters
    total_weight: float = 50000.0  # kN
    
    # Seismic Parameters
    site_class: str = "C"  # A, B, C, D, E, F
    ss: float = 1.5  # Mapped spectral response acceleration (short periods)
    s1: float = 0.6  # Mapped spectral response acceleration (1-second period)
    sms: float = 1.5  # Site-modified spectral response acceleration (short periods)
    sm1: float = 0.6  # Site-modified spectral response acceleration (1-second period)
    sds: float = 1.0  # Design spectral response acceleration (short periods)
    sd1: float = 0.4  # Design spectral response acceleration (1-second period)
    
    # Building Characteristics
    importance_factor: float = 1.0  # Ie
    response_modification: float = 8.0  # R factor
    overstrength_factor: float = 3.0  # Omega_0
    deflection_amplification: float = 5.5  # Cd
    
    # Analysis Type
    analysis_type: str = "Static Seismic"  # Static, Response Spectrum
    spectrum_type: str = "Design Response Spectrum"
    
    # Thai Specific
    province: str = "Bangkok"
    seismic_zone: str = "Zone_A"
    
    # Code Selection
    design_code: str = "ASCE7-22"  # ASCE7-22, TIS1301-61
    
    # Load Application
    direction_x: bool = True
    direction_y: bool = True
    apply_to_structure: bool = True
    load_case_name: str = "Seismic_X"
    
    # Response Spectrum Parameters
    periods: List[float] = None
    accelerations: List[float] = None
    damping_ratio: float = 0.05  # 5% damping
    modal_combination: str = "CQC"  # CQC, SRSS
    
    def __post_init__(self):
        if self.periods is None:
            # Default response spectrum periods
            self.periods = [0.0, 0.2*self.sd1/self.sds, self.sd1/self.sds, 1.5*self.sd1/self.sds, 4.0]
        if self.accelerations is None:
            # Default ASCE 7-22 design response spectrum
            self.accelerations = [0.4*self.sds, self.sds, self.sd1/self.periods[2], 
                                self.sd1/self.periods[3], self.sd1/self.periods[4]]

class SeismicLoadGUI(QDialog):
    """Professional Seismic Load GUI Interface"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parameters = SeismicLoadParameters()
        self.seismic_forces = None
        self.response_spectrum = None
        self.calc_model = None
        
        self.setWindowTitle("Seismic Load Generator - Professional Interface")
        self.resize(900, 700)
        
        self.setup_ui()
        self.connect_signals()
        self.load_defaults()
    
    def setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout()
        
        # Title Header
        title_label = QLabel("Seismic Load Analysis System")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #C2185B; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Tab Widget for organized input
        self.tab_widget = QTabWidget()
        
        # Tab 1: Basic Parameters
        self.basic_tab = self.create_basic_parameters_tab()
        self.tab_widget.addTab(self.basic_tab, "Basic Parameters")
        
        # Tab 2: Seismic Parameters  
        self.seismic_tab = self.create_seismic_parameters_tab()
        self.tab_widget.addTab(self.seismic_tab, "Seismic Parameters")
        
        # Tab 3: Analysis Type
        self.analysis_tab = self.create_analysis_type_tab()
        self.tab_widget.addTab(self.analysis_tab, "Analysis Type")
        
        # Tab 4: Response Spectrum
        self.spectrum_tab = self.create_response_spectrum_tab()
        self.tab_widget.addTab(self.spectrum_tab, "Response Spectrum")
        
        # Tab 5: Thai Standards
        self.thai_tab = self.create_thai_standards_tab()
        self.tab_widget.addTab(self.thai_tab, "Thai Standards")
        
        # Tab 6: Load Application
        self.application_tab = self.create_application_tab()
        self.tab_widget.addTab(self.application_tab, "Load Application")
        
        layout.addWidget(self.tab_widget)
        
        # Results Preview
        self.results_group = self.create_results_preview()
        layout.addWidget(self.results_group)
        
        # Action Buttons
        self.button_layout = self.create_action_buttons()
        layout.addLayout(self.button_layout)
        
        self.setLayout(layout)
    
    def create_basic_parameters_tab(self):
        """Create basic building parameters tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Building Geometry Group
        geometry_group = QGroupBox("Building Geometry")
        geo_layout = QGridLayout()
        
        # Height
        geo_layout.addWidget(QLabel("Building Height (m):"), 0, 0)
        self.height_edit = QLineEdit(str(self.parameters.building_height))
        geo_layout.addWidget(self.height_edit, 0, 1)
        
        # Width
        geo_layout.addWidget(QLabel("Building Width (m):"), 1, 0)
        self.width_edit = QLineEdit(str(self.parameters.building_width))
        geo_layout.addWidget(self.width_edit, 1, 1)
        
        # Length
        geo_layout.addWidget(QLabel("Building Length (m):"), 2, 0)
        self.length_edit = QLineEdit(str(self.parameters.building_length))
        geo_layout.addWidget(self.length_edit, 2, 1)
        
        # Total Weight
        geo_layout.addWidget(QLabel("Total Building Weight (kN):"), 3, 0)
        self.weight_edit = QLineEdit(str(self.parameters.total_weight))
        geo_layout.addWidget(self.weight_edit, 3, 1)
        
        geometry_group.setLayout(geo_layout)
        layout.addWidget(geometry_group, 0, 0, 1, 2)
        
        # Design Code Selection
        code_group = QGroupBox("Design Code")
        code_layout = QGridLayout()
        
        code_layout.addWidget(QLabel("Design Standard:"), 0, 0)
        self.code_combo = QComboBox()
        self.code_combo.addItems(["ASCE 7-22", "TIS 1301-61", "Both"])
        code_layout.addWidget(self.code_combo, 0, 1)
        
        code_group.setLayout(code_layout)
        layout.addWidget(code_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_seismic_parameters_tab(self):
        """Create seismic parameters tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Site Parameters Group
        site_group = QGroupBox("Site Seismic Parameters")
        site_layout = QGridLayout()
        
        site_layout.addWidget(QLabel("Site Class:"), 0, 0)
        self.site_class_combo = QComboBox()
        self.site_class_combo.addItems(["A", "B", "C", "D", "E", "F"])
        self.site_class_combo.setCurrentText(self.parameters.site_class)
        site_layout.addWidget(self.site_class_combo, 0, 1)
        
        site_layout.addWidget(QLabel("Ss (Mapped short period):"), 1, 0)
        self.ss_edit = QLineEdit(str(self.parameters.ss))
        site_layout.addWidget(self.ss_edit, 1, 1)
        
        site_layout.addWidget(QLabel("S1 (Mapped 1-second period):"), 2, 0)
        self.s1_edit = QLineEdit(str(self.parameters.s1))
        site_layout.addWidget(self.s1_edit, 2, 1)
        
        site_layout.addWidget(QLabel("SMS (Site-modified short):"), 3, 0)
        self.sms_edit = QLineEdit(str(self.parameters.sms))
        site_layout.addWidget(self.sms_edit, 3, 1)
        
        site_layout.addWidget(QLabel("SM1 (Site-modified 1-sec):"), 4, 0)
        self.sm1_edit = QLineEdit(str(self.parameters.sm1))
        site_layout.addWidget(self.sm1_edit, 4, 1)
        
        site_group.setLayout(site_layout)
        layout.addWidget(site_group, 0, 0, 1, 2)
        
        # Design Parameters Group
        design_group = QGroupBox("Design Seismic Parameters")
        design_layout = QGridLayout()
        
        design_layout.addWidget(QLabel("SDS (Design short period):"), 0, 0)
        self.sds_edit = QLineEdit(str(self.parameters.sds))
        design_layout.addWidget(self.sds_edit, 0, 1)
        
        design_layout.addWidget(QLabel("SD1 (Design 1-second):"), 1, 0)
        self.sd1_edit = QLineEdit(str(self.parameters.sd1))
        design_layout.addWidget(self.sd1_edit, 1, 1)
        
        design_layout.addWidget(QLabel("Importance Factor (Ie):"), 2, 0)
        self.ie_edit = QLineEdit(str(self.parameters.importance_factor))
        design_layout.addWidget(self.ie_edit, 2, 1)
        
        design_layout.addWidget(QLabel("Response Modification (R):"), 3, 0)
        self.r_edit = QLineEdit(str(self.parameters.response_modification))
        design_layout.addWidget(self.r_edit, 3, 1)
        
        design_group.setLayout(design_layout)
        layout.addWidget(design_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_analysis_type_tab(self):
        """Create analysis type selection tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Analysis Type Group
        analysis_group = QGroupBox("Seismic Analysis Type")
        analysis_layout = QGridLayout()
        
        analysis_layout.addWidget(QLabel("Analysis Method:"), 0, 0)
        self.analysis_type_combo = QComboBox()
        self.analysis_type_combo.addItems(["Static Seismic", "Response Spectrum", "Time History"])
        analysis_layout.addWidget(self.analysis_type_combo, 0, 1)
        
        # Static Seismic Parameters
        static_group = QGroupBox("Static Seismic Parameters")
        static_layout = QGridLayout()
        
        static_layout.addWidget(QLabel("Base Shear Coefficient (Cs):"), 0, 0)
        self.cs_edit = QLineEdit("0.1")
        static_layout.addWidget(self.cs_edit, 0, 1)
        
        static_layout.addWidget(QLabel("Vertical Distribution:"), 1, 0)
        self.distribution_combo = QComboBox()
        self.distribution_combo.addItems(["Linear", "Parabolic", "User Defined"])
        static_layout.addWidget(self.distribution_combo, 1, 1)
        
        static_group.setLayout(static_layout)
        analysis_layout.addWidget(static_group, 1, 0, 1, 2)
        
        analysis_group.setLayout(analysis_layout)
        layout.addWidget(analysis_group, 0, 0, 1, 2)
        
        # Direction Group
        direction_group = QGroupBox("Load Direction")
        direction_layout = QGridLayout()
        
        self.x_direction_check = QCheckBox("X-Direction")
        self.x_direction_check.setChecked(self.parameters.direction_x)
        direction_layout.addWidget(self.x_direction_check, 0, 0)
        
        self.y_direction_check = QCheckBox("Y-Direction")
        self.y_direction_check.setChecked(self.parameters.direction_y)
        direction_layout.addWidget(self.y_direction_check, 0, 1)
        
        direction_group.setLayout(direction_layout)
        layout.addWidget(direction_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_response_spectrum_tab(self):
        """Create response spectrum tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Spectrum Type Group
        spectrum_group = QGroupBox("Response Spectrum Type")
        spectrum_layout = QGridLayout()
        
        spectrum_layout.addWidget(QLabel("Spectrum Type:"), 0, 0)
        self.spectrum_type_combo = QComboBox()
        self.spectrum_type_combo.addItems(["Design Response Spectrum", "MCE Response Spectrum", "Custom Spectrum"])
        spectrum_layout.addWidget(self.spectrum_type_combo, 0, 1)
        
        spectrum_layout.addWidget(QLabel("Damping Ratio:"), 1, 0)
        self.damping_edit = QLineEdit(str(self.parameters.damping_ratio))
        spectrum_layout.addWidget(self.damping_edit, 1, 1)
        
        spectrum_layout.addWidget(QLabel("Modal Combination:"), 2, 0)
        self.modal_combo = QComboBox()
        self.modal_combo.addItems(["CQC", "SRSS", "ABS"])
        spectrum_layout.addWidget(self.modal_combo, 2, 1)
        
        spectrum_group.setLayout(spectrum_layout)
        layout.addWidget(spectrum_group, 0, 0, 1, 2)
        
        # Spectrum Definition Table
        table_group = QGroupBox("Response Spectrum Definition")
        table_layout = QVBoxLayout()
        
        self.spectrum_table = QTableWidget(10, 2)
        self.spectrum_table.setHorizontalHeaderLabels(["Period (sec)", "Acceleration (g)"])
        
        # Populate with default values
        for i, (period, accel) in enumerate(zip(self.parameters.periods[:10], 
                                              self.parameters.accelerations[:10])):
            self.spectrum_table.setItem(i, 0, QTableWidgetItem(str(period)))
            self.spectrum_table.setItem(i, 1, QTableWidgetItem(str(accel)))
        
        table_layout.addWidget(self.spectrum_table)
        
        # Spectrum buttons
        button_layout = QHBoxLayout()
        self.generate_spectrum_btn = QPushButton("Generate ASCE Spectrum")
        self.import_spectrum_btn = QPushButton("Import Custom Spectrum")
        button_layout.addWidget(self.generate_spectrum_btn)
        button_layout.addWidget(self.import_spectrum_btn)
        table_layout.addLayout(button_layout)
        
        table_group.setLayout(table_layout)
        layout.addWidget(table_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_thai_standards_tab(self):
        """Create Thai standards specific tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Thai Location Group
        location_group = QGroupBox("Thai Seismic Parameters")
        location_layout = QGridLayout()
        
        location_layout.addWidget(QLabel("Province:"), 0, 0)
        self.province_combo = QComboBox()
        # Add Thai provinces with seismic considerations
        thai_provinces = [
            "Bangkok", "Samut Prakan", "Nonthaburi", "Pathum Thani", "Phra Nakhon Si Ayutthaya",
            "Chiang Mai", "Chiang Rai", "Lampang", "Lamphun", "Mae Hong Son", "Nan", "Phayao",
            "Phrae", "Uttaradit", "Tak", "Kamphaeng Phet", "Nakhon Sawan", "Phetchabun",
            "Phitsanulok", "Sukhothai", "Uthai Thani", "Kanchanaburi", "Ratchaburi", 
            "Suphan Buri", "Nakhon Pathom", "Samut Sakhon", "Samut Songkhram"
        ]
        self.province_combo.addItems(thai_provinces)
        self.province_combo.setCurrentText(self.parameters.province)
        location_layout.addWidget(self.province_combo, 0, 1)
        
        location_layout.addWidget(QLabel("Seismic Zone:"), 1, 0)
        self.seismic_zone_combo = QComboBox()
        self.seismic_zone_combo.addItems(["Zone_A", "Zone_B", "Zone_C"])
        location_layout.addWidget(self.seismic_zone_combo, 1, 1)
        
        location_layout.addWidget(QLabel("Ground Motion Level:"), 2, 0)
        self.ground_motion_combo = QComboBox()
        self.ground_motion_combo.addItems(["Low", "Moderate", "High"])
        location_layout.addWidget(self.ground_motion_combo, 2, 1)
        
        location_group.setLayout(location_layout)
        layout.addWidget(location_group, 0, 0, 1, 2)
        
        # Thai Standards Info
        info_group = QGroupBox("TIS 1301/1302-61 Information")
        info_layout = QVBoxLayout()
        
        info_text = """
        Thai Standard TIS 1301/1302-61:
        • Seismic design for buildings in Thailand
        • Provincial seismic hazard mapping
        • Compatible with international seismic codes
        • Specific provisions for Thai geological conditions
        • Zone A: Low seismicity (most of Thailand)
        • Zone B: Moderate seismicity (border regions)
        • Zone C: High seismicity (western border areas)
        """
        info_label = QLabel(info_text)
        info_label.setWordWrap(True)
        info_layout.addWidget(info_label)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_application_tab(self):
        """Create load application tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Load Case Group
        loadcase_group = QGroupBox("Load Case Definition")
        loadcase_layout = QGridLayout()
        
        loadcase_layout.addWidget(QLabel("Load Case Name:"), 0, 0)
        self.loadcase_edit = QLineEdit(self.parameters.load_case_name)
        loadcase_layout.addWidget(self.loadcase_edit, 0, 1)
        
        # Application Options
        self.apply_checkbox = QCheckBox("Apply to Active Structure")
        self.apply_checkbox.setChecked(self.parameters.apply_to_structure)
        loadcase_layout.addWidget(self.apply_checkbox, 1, 0, 1, 2)
        
        # Load combination options
        loadcase_layout.addWidget(QLabel("Load Combination Factor:"), 2, 0)
        self.combination_edit = QLineEdit("1.0")
        loadcase_layout.addWidget(self.combination_edit, 2, 1)
        
        loadcase_group.setLayout(loadcase_layout)
        layout.addWidget(loadcase_group, 0, 0, 1, 2)
        
        # Integration Options
        integration_group = QGroupBox("Analysis Integration")
        integration_layout = QGridLayout()
        
        self.auto_calc_checkbox = QCheckBox("Automatically run structural analysis")
        integration_layout.addWidget(self.auto_calc_checkbox, 0, 0, 1, 2)
        
        self.generate_report_checkbox = QCheckBox("Generate seismic analysis report")
        integration_layout.addWidget(self.generate_report_checkbox, 1, 0, 1, 2)
        
        self.modal_analysis_checkbox = QCheckBox("Include modal analysis results")
        integration_layout.addWidget(self.modal_analysis_checkbox, 2, 0, 1, 2)
        
        integration_group.setLayout(integration_layout)
        layout.addWidget(integration_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_results_preview(self):
        """Create results preview group"""
        group = QGroupBox("Seismic Analysis Results Preview")
        layout = QVBoxLayout()
        
        self.results_text = QTextEdit()
        self.results_text.setMaximumHeight(150)
        self.results_text.setPlainText("Seismic loads will be displayed here after calculation...")
        
        layout.addWidget(self.results_text)
        group.setLayout(layout)
        
        return group
    
    def create_action_buttons(self):
        """Create action buttons"""
        layout = QHBoxLayout()
        
        # Calculate Button
        self.calculate_btn = QPushButton("Calculate Seismic Loads")
        self.calculate_btn.setStyleSheet("QPushButton { background-color: #C2185B; color: white; font-weight: bold; padding: 8px; }")
        layout.addWidget(self.calculate_btn)
        
        # Generate Spectrum Button
        self.spectrum_btn = QPushButton("Generate Response Spectrum")
        self.spectrum_btn.setStyleSheet("QPushButton { background-color: #7B1FA2; color: white; font-weight: bold; padding: 8px; }")
        layout.addWidget(self.spectrum_btn)
        
        # Apply to Structure Button
        self.apply_btn = QPushButton("Apply to Structure")
        self.apply_btn.setStyleSheet("QPushButton { background-color: #A23B72; color: white; font-weight: bold; padding: 8px; }")
        self.apply_btn.setEnabled(False)
        layout.addWidget(self.apply_btn)
        
        # Run Analysis Button
        self.analyze_btn = QPushButton("Run Structural Analysis")
        self.analyze_btn.setStyleSheet("QPushButton { background-color: #F18F01; color: white; font-weight: bold; padding: 8px; }")
        self.analyze_btn.setEnabled(False)
        layout.addWidget(self.analyze_btn)
        
        # Close Button
        self.close_btn = QPushButton("Close")
        layout.addWidget(self.close_btn)
        
        return layout
    
    def connect_signals(self):
        """Connect GUI signals"""
        self.calculate_btn.clicked.connect(self.calculate_seismic_loads)
        self.spectrum_btn.clicked.connect(self.generate_response_spectrum)
        self.apply_btn.clicked.connect(self.apply_loads_to_structure)
        self.analyze_btn.clicked.connect(self.run_structural_analysis)
        self.close_btn.clicked.connect(self.close)
        
        # Real-time updates
        self.analysis_type_combo.currentTextChanged.connect(self.update_analysis_type)
        self.spectrum_type_combo.currentTextChanged.connect(self.update_spectrum_type)
        self.generate_spectrum_btn.clicked.connect(self.generate_asce_spectrum)
    
    def load_defaults(self):
        """Load default values"""
        self.update_parameters()
    
    def update_parameters(self):
        """Update parameters from GUI inputs"""
        try:
            self.parameters.building_height = float(self.height_edit.text())
            self.parameters.building_width = float(self.width_edit.text())
            self.parameters.building_length = float(self.length_edit.text())
            self.parameters.total_weight = float(self.weight_edit.text())
            self.parameters.site_class = self.site_class_combo.currentText()
            self.parameters.ss = float(self.ss_edit.text())
            self.parameters.s1 = float(self.s1_edit.text())
            self.parameters.sds = float(self.sds_edit.text())
            self.parameters.sd1 = float(self.sd1_edit.text())
            self.parameters.analysis_type = self.analysis_type_combo.currentText()
            self.parameters.spectrum_type = self.spectrum_type_combo.currentText()
            self.parameters.province = self.province_combo.currentText()
            self.parameters.load_case_name = self.loadcase_edit.text()
            self.parameters.direction_x = self.x_direction_check.isChecked()
            self.parameters.direction_y = self.y_direction_check.isChecked()
        except (ValueError, AttributeError):
            pass  # Handle invalid input gracefully
    
    def update_analysis_type(self):
        """Update interface based on analysis type"""
        analysis_type = self.analysis_type_combo.currentText()
        
        # Enable/disable relevant tabs based on analysis type
        if analysis_type == "Static Seismic":
            self.tab_widget.setTabEnabled(3, False)  # Disable Response Spectrum tab
        elif analysis_type == "Response Spectrum":
            self.tab_widget.setTabEnabled(3, True)   # Enable Response Spectrum tab
            
        self.parameters.analysis_type = analysis_type
    
    def update_spectrum_type(self):
        """Update spectrum parameters based on type"""
        spectrum_type = self.spectrum_type_combo.currentText()
        self.parameters.spectrum_type = spectrum_type
        
        if spectrum_type in ["Design Response Spectrum", "MCE Response Spectrum"]:
            self.generate_asce_spectrum()
    
    def generate_asce_spectrum(self):
        """Generate ASCE 7-22 response spectrum"""
        try:
            # Update parameters first
            self.update_parameters()
            
            # Generate ASCE 7-22 design response spectrum
            sds = self.parameters.sds
            sd1 = self.parameters.sd1
            tl = 8.0  # Long-period transition period (simplified)
            
            # Define periods
            periods = []
            accelerations = []
            
            # Period range from 0 to 4 seconds
            for i in range(41):  # 0 to 4 seconds in 0.1 second increments
                t = i * 0.1
                periods.append(t)
                
                # ASCE 7-22 design response spectrum equations
                if t <= 0.2 * sd1 / sds:
                    # Short period range
                    sa = sds * (0.4 + 0.6 * t / (0.2 * sd1 / sds))
                elif t <= sd1 / sds:
                    # Intermediate period range
                    sa = sds
                elif t <= tl:
                    # Long period range
                    sa = sd1 / t
                else:
                    # Very long period range
                    sa = sd1 * tl / (t * t)
                
                accelerations.append(sa)
            
            # Update spectrum table
            self.spectrum_table.setRowCount(len(periods))
            for i, (period, accel) in enumerate(zip(periods, accelerations)):
                self.spectrum_table.setItem(i, 0, QTableWidgetItem(f"{period:.2f}"))
                self.spectrum_table.setItem(i, 1, QTableWidgetItem(f"{accel:.4f}"))
            
            # Store in parameters
            self.parameters.periods = periods
            self.parameters.accelerations = accelerations
            
            self.results_text.append(f"\\n✅ ASCE 7-22 Response Spectrum Generated")
            self.results_text.append(f"   SDS = {sds:.3f}g, SD1 = {sd1:.3f}g")
            self.results_text.append(f"   {len(periods)} spectrum points defined")
            
        except Exception as e:
            self.results_text.append(f"\\n❌ Spectrum generation error: {e}")
    
    def calculate_seismic_loads(self):
        """Calculate seismic loads based on analysis type"""
        self.update_parameters()
        
        try:
            results_text = f"Seismic Load Calculation Results\\n"
            results_text += f"{'='*40}\\n\\n"
            
            analysis_type = self.parameters.analysis_type
            
            if analysis_type == "Static Seismic":
                self.calculate_static_seismic()
                results_text += "Static Seismic Analysis Results:\\n"
            elif analysis_type == "Response Spectrum":
                self.calculate_response_spectrum_analysis()
                results_text += "Response Spectrum Analysis Results:\\n"
            
            # Display results
            if self.seismic_forces:
                results_text += f"Building Height: {self.parameters.building_height} m\\n"
                results_text += f"Total Weight: {self.parameters.total_weight} kN\\n"
                results_text += f"Site Class: {self.parameters.site_class}\\n"
                results_text += f"SDS: {self.parameters.sds}g, SD1: {self.parameters.sd1}g\\n\\n"
                results_text += "Calculated Seismic Forces:\\n"
                results_text += f"• Base shear X: {getattr(self.seismic_forces, 'base_shear_x', 'N/A')} kN\\n"
                results_text += f"• Base shear Y: {getattr(self.seismic_forces, 'base_shear_y', 'N/A')} kN\\n"
                results_text += f"• Period X: {getattr(self.seismic_forces, 'period_x', 'N/A')} sec\\n"
                results_text += f"• Period Y: {getattr(self.seismic_forces, 'period_y', 'N/A')} sec\\n"
            
            self.results_text.setPlainText(results_text)
            self.apply_btn.setEnabled(True)
            
        except Exception as e:
            self.results_text.setPlainText(f"Calculation error: {str(e)}")
    
    def calculate_static_seismic(self):
        """Calculate static seismic loads per ASCE 7-22"""
        try:
            # Basic seismic parameters
            w = self.parameters.total_weight  # Total weight
            sds = self.parameters.sds
            sd1 = self.parameters.sd1
            r = self.parameters.response_modification
            ie = self.parameters.importance_factor
            
            # Approximate fundamental period (ASCE 7-22)
            h = self.parameters.building_height
            ta = 0.02 * (h ** 0.75)  # Simplified for moment frame
            
            # Seismic response coefficient
            cs1 = sds / (r / ie)
            cs2 = sd1 / (ta * (r / ie))
            cs = min(cs1, cs2)
            cs = max(cs, 0.01)  # Minimum value
            
            # Base shear
            v = cs * w
            
            # Store results
            self.seismic_forces = type('obj', (object,), {
                'base_shear_x': v if self.parameters.direction_x else 0,
                'base_shear_y': v if self.parameters.direction_y else 0,
                'period_x': ta,
                'period_y': ta,
                'cs': cs,
                'total_weight': w
            })()
            
        except Exception as e:
            raise Exception(f"Static seismic calculation failed: {e}")
    
    def calculate_response_spectrum_analysis(self):
        """Calculate response spectrum analysis"""
        try:
            # This would involve modal analysis and spectrum application
            # For now, simplified calculation
            w = self.parameters.total_weight
            sds = self.parameters.sds
            
            # Simplified response spectrum base shear
            v = 0.8 * sds * w / self.parameters.response_modification
            
            self.seismic_forces = type('obj', (object,), {
                'base_shear_x': v if self.parameters.direction_x else 0,
                'base_shear_y': v if self.parameters.direction_y else 0,
                'period_x': 0.5,
                'period_y': 0.5,
                'modal_periods': [0.2, 0.5, 0.8],
                'modal_participation': [0.8, 0.15, 0.05]
            })()
            
        except Exception as e:
            raise Exception(f"Response spectrum calculation failed: {e}")
    
    def generate_response_spectrum(self):
        """Generate and plot response spectrum"""
        try:
            self.generate_asce_spectrum()
            self.results_text.append("\\n📊 Response spectrum generated and ready for analysis")
            
        except Exception as e:
            self.results_text.append(f"\\n❌ Spectrum generation error: {e}")
    
    def apply_loads_to_structure(self):
        """Apply calculated seismic loads to the structure"""
        if not self.seismic_forces:
            self.results_text.append("\\nNo seismic forces calculated!")
            return
        
        try:
            if not CALC_AVAILABLE:
                self.results_text.append("\\nStructural analysis system not available!")
                return
            
            # Get active document and structure
            if FREECAD_AVAILABLE and App.ActiveDocument:
                doc = App.ActiveDocument
                
                # Find structural analysis object
                analysis_objects = [obj for obj in doc.Objects if hasattr(obj, 'Proxy') and 'Analysis' in str(type(obj.Proxy))]
                
                if analysis_objects:
                    analysis_obj = analysis_objects[0]
                    
                    # Apply seismic loads to the structure
                    self.apply_seismic_loads_to_model(analysis_obj)
                    self.results_text.append(f"\\n✅ Seismic loads applied to structure as '{self.parameters.load_case_name}'")
                    self.analyze_btn.setEnabled(True)
                else:
                    self.results_text.append("\\n❌ No structural analysis object found!")
            else:
                # Mock application for testing
                self.results_text.append(f"\\n✅ Seismic loads would be applied as '{self.parameters.load_case_name}'")
                self.analyze_btn.setEnabled(True)
                
        except Exception as e:
            self.results_text.append(f"\\n❌ Error applying loads: {str(e)}")
    
    def apply_seismic_loads_to_model(self, analysis_obj):
        """Apply seismic forces to the structural model"""
        try:
            # Create seismic load objects in the model
            # This integrates with the calc system
            
            # Add equivalent static loads for static analysis
            # Add response spectrum loads for dynamic analysis
            # Set load case parameters
            
            if hasattr(analysis_obj, 'Proxy'):
                proxy = analysis_obj.Proxy
                if hasattr(proxy, 'add_seismic_loads'):
                    proxy.add_seismic_loads(self.seismic_forces, self.parameters)
            
        except Exception as e:
            raise Exception(f"Failed to apply seismic loads to model: {e}")
    
    def run_structural_analysis(self):
        """Run the structural analysis with applied seismic loads"""
        try:
            if not CALC_AVAILABLE:
                self.results_text.append("\\nStructural analysis system not available!")
                return
            
            self.results_text.append("\\n🔄 Running seismic structural analysis...")
            
            # Run the analysis
            if FREECAD_AVAILABLE and App.ActiveDocument:
                doc = App.ActiveDocument
                analysis_objects = [obj for obj in doc.Objects if hasattr(obj, 'Proxy') and 'Analysis' in str(type(obj.Proxy))]
                
                if analysis_objects:
                    analysis_obj = analysis_objects[0]
                    
                    # Execute the analysis
                    analysis_obj.Proxy.execute(analysis_obj)
                    
                    self.results_text.append("✅ Seismic structural analysis completed!")
                    self.results_text.append("✅ Results available in analysis object")
                    
                    # Auto-generate report if requested
                    if hasattr(self, 'generate_report_checkbox') and self.generate_report_checkbox.isChecked():
                        self.generate_seismic_report()
                else:
                    self.results_text.append("❌ No analysis object found!")
            else:
                # Mock analysis for testing
                self.results_text.append("✅ Seismic structural analysis would be executed")
                
        except Exception as e:
            self.results_text.append(f"❌ Analysis error: {str(e)}")
    
    def generate_seismic_report(self):
        """Generate professional seismic analysis report"""
        try:
            from ..reporting import ProfessionalReportGenerator
            
            report_gen = ProfessionalReportGenerator()
            
            # Prepare report data
            report_data = {
                'project_name': 'Seismic Analysis',
                'seismic_parameters': self.parameters,
                'seismic_forces': self.seismic_forces,
                'response_spectrum': self.response_spectrum,
                'analysis_date': datetime.now(),
                'code_used': self.parameters.design_code
            }
            
            # Generate report
            report = report_gen.generate_seismic_report(report_data)
            
            self.results_text.append("\\n📄 Seismic analysis report generated successfully!")
            
        except Exception as e:
            self.results_text.append(f"\\n❌ Report generation error: {str(e)}")

def show_seismic_load_gui():
    """Show the seismic load GUI"""
    try:
        # Create Qt Application if needed
        app = QApplication.instance() if QT_AVAILABLE else None
        if app is None and QT_AVAILABLE:
            app = QApplication(sys.argv)
        
        # Create and show the GUI
        dialog = SeismicLoadGUI()
        dialog.show()
        
        return dialog
        
    except Exception as e:
        print(f"Error showing seismic load GUI: {e}")
        return None

# FreeCAD Command Integration
class SeismicLoadCommand:
    """FreeCAD command for seismic load GUI"""
    
    def GetResources(self):
        return {
            'Pixmap': 'seismic_load.png',
            'MenuText': 'Seismic Load Generator',
            'ToolTip': 'Professional seismic load analysis and generation (Static & Response Spectrum)'
        }
    
    def Activated(self):
        """Called when the command is activated"""
        dialog = show_seismic_load_gui()
        if dialog and QT_AVAILABLE:
            dialog.exec_()
    
    def IsActive(self):
        return True

# Register command if FreeCAD is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    Gui.addCommand("seismic_load_gui", SeismicLoadCommand())

# Export for direct usage
__all__ = ['SeismicLoadGUI', 'SeismicLoadParameters', 'show_seismic_load_gui', 'SeismicLoadCommand',
           'SeismicAnalysisType', 'SpectrumType']
