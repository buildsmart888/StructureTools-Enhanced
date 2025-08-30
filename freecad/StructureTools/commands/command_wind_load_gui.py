# -*- coding: utf-8 -*-
"""
Wind Load GUI Interface - Professional Wind Analysis System
============================================================

Comprehensive GUI for wind load generation and analysis based on:
- ASCE 7-22 Standards
- Thai TIS Standards (TIS 1311-50)
- Integration with FreeCAD structural analysis
- Professional workflow similar to MIDAS nGen

Features:
- Interactive wind load parameter input
- Real-time load visualization
- Automatic integration with calc system
- Professional reporting capabilities
"""

import sys
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime

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

# Define ICONPATH for accessing icons
ICONPATH = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")

# Import GUI framework with fallbacks
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
        # Mock classes for standalone testing
        QT_AVAILABLE = False
        
        class QDialog:
            def __init__(self, parent=None): pass
            def setWindowTitle(self, title): pass
            def setWindowIcon(self, icon): pass
            def resize(self, w, h): pass
            def setLayout(self, layout): pass
            def exec_(self): pass
            def show(self): pass
            def close(self): pass
        
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
            def __init__(self, text=""): self.text_value = text
            def text(self): return self.text_value
            def setText(self, text): self.text_value = text
        
        class QComboBox:
            def __init__(self): 
                self.items = []
                self.current_index = 0
            def addItems(self, items): self.items = items
            def currentText(self): return self.items[self.current_index] if self.items else ""
            def setCurrentText(self, text): 
                if text in self.items:
                    self.current_index = self.items.index(text)
            def setCurrentIndex(self, index): self.current_index = index
            def currentTextChanged(self): pass
        
        class QPushButton:
            def __init__(self, text=""): pass
            def setStyleSheet(self, style): pass
            def setEnabled(self, enabled): pass
            def clicked(self): pass
        
        class QTabWidget:
            def __init__(self): pass
            def addTab(self, widget, text): pass
        
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
            def append(self, text): self.text_content += "\n" + text
        
        class QIcon:
            def __init__(self, path): pass
        
        class QApplication:
            @staticmethod
            def instance(): return None
            def __init__(self, args): pass
        
        # Qt Constants
        class Qt:
            AlignCenter = 0
        
        # Mock signal connection
        class MockSignal:
            def connect(self, slot): pass
        
        # Add signal attributes to mock widgets
        for cls in [QComboBox, QPushButton, QCheckBox]:
            if hasattr(cls, '__init__'):
                original_init = cls.__init__
                def new_init(self, *args, **kwargs):
                    original_init(self, *args, **kwargs)
                    self.clicked = MockSignal()
                    self.currentTextChanged = MockSignal()
                cls.__init__ = new_init

# Import plotting library with fallback
try:
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('Qt5Agg')  # Use Qt5Agg backend for FreeCAD
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    # Create mock classes for plotting
    class Figure:
        def __init__(self): pass
        def add_subplot(self, *args): return MockAxes()
        def tight_layout(self): pass
    
    class FigureCanvas:
        def __init__(self, figure): pass
    
    class MockAxes:
        def __init__(self): pass
        def plot(self, *args, **kwargs): pass
        def set_xlabel(self, label): pass
        def set_ylabel(self, label): pass
        def set_title(self, title): pass
        def grid(self, *args, **kwargs): pass

# Import wind analysis modules
try:
    from .wind_asce7 import WindLoadASCE7, BuildingWindData, WindForces
    from .thai_wind_loads import ThaiWindLoad, ThaiWindData
    WIND_MODULES_AVAILABLE = True
except ImportError:
    WIND_MODULES_AVAILABLE = False
    # Create mock classes
    class WindLoadASCE7:
        def __init__(self): pass
    
    class ThaiWindLoad:
        def __init__(self): pass

# Import calc system
try:
    from ..calc import StructAnalysis
    from ..material import Material
    CALC_AVAILABLE = True
except ImportError:
    CALC_AVAILABLE = False

@dataclass
class WindLoadParameters:
    """Wind load input parameters container"""
    # Basic Building Data
    building_height: float = 30.0  # meters
    building_width: float = 20.0   # meters  
    building_length: float = 40.0  # meters
    
    # Wind Parameters
    basic_wind_speed: float = 45.0  # m/s
    exposure_category: str = "C"    # A, B, C, D
    topographic_factor: float = 1.0
    directionality_factor: float = 0.85
    
    # Thai Specific
    province: str = "Bangkok"
    wind_zone: str = "Zone_1"
    
    # Code Selection
    design_code: str = "ASCE7-22"  # ASCE7-22, TIS1311-50
    
    # Load Application
    apply_to_structure: bool = True
    load_case_name: str = "Wind_Load_X"

class WindLoadGUI(QDialog):
    """Professional Wind Load GUI Interface"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parameters = WindLoadParameters()
        self.wind_forces = None
        self.calc_model = None
        
        self.setWindowTitle("Wind Load Generator - Professional Interface")
        self.setWindowIcon(QIcon(os.path.join(ICONPATH, "wind_load.svg")) if FREECAD_AVAILABLE else None)
        self.resize(900, 700)
        
        self.setup_ui()
        self.connect_signals()
        self.load_defaults()
    
    def setup_ui(self):
        """Setup the user interface"""
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)  # Add more spacing between main sections
        
        # Title Header - reduced padding
        title_label = QLabel("Wind Load Analysis System")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2E86AB; padding: 5px;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Split the UI into top (tabs) and bottom (results) sections
        splitter = QSplitter(Qt.Vertical)
        
        # Top section: Tab Widget for organized input
        top_widget = QWidget()
        top_layout = QVBoxLayout(top_widget)
        top_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins to maximize space
        
        self.tab_widget = QTabWidget()
        
        # Tab 1: Basic Parameters
        self.basic_tab = self.create_basic_parameters_tab()
        self.tab_widget.addTab(self.basic_tab, "Basic Parameters")
        
        # Tab 2: Wind Parameters  
        self.wind_tab = self.create_wind_parameters_tab()
        self.tab_widget.addTab(self.wind_tab, "Wind Parameters")
        
        # Tab 3: Professional Wind Load Function (MIDAS-style)
        self.wind_load_function_tab = self.create_wind_load_tab()
        self.tab_widget.addTab(self.wind_load_function_tab, "Wind Load Function")
        
        # Tab 4: Thai Standards
        self.thai_tab = self.create_thai_standards_tab()
        self.tab_widget.addTab(self.thai_tab, "Thai Standards")
        
        # Tab 5: Load Application
        self.application_tab = self.create_application_tab()
        self.tab_widget.addTab(self.application_tab, "Load Application")
        
        top_layout.addWidget(self.tab_widget)
        
        # Bottom section: Results Preview
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout(bottom_widget)
        bottom_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins to maximize space
        
        self.results_group = self.create_results_preview()
        bottom_layout.addWidget(self.results_group)
        
        # Add widgets to splitter
        splitter.addWidget(top_widget)
        splitter.addWidget(bottom_widget)
        
        # Set initial sizes - give more space to results preview
        splitter.setSizes([600, 400])  
        
        main_layout.addWidget(splitter, 1)  # Give splitter all available space
        
        # Action Buttons
        self.button_layout = self.create_action_buttons()
        main_layout.addLayout(self.button_layout)
        
        self.setLayout(main_layout)
        
    def create_wind_load_tab(self):
        """Create a professional wind load tab similar to MIDAS nGen"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Function settings section
        function_group = QGroupBox("Wind Load Function")
        function_layout = QGridLayout()
        
        # Function Name
        function_layout.addWidget(QLabel("Function Name:"), 0, 0)
        self.wind_function_name_edit = QLineEdit("Wind Load Function-1")
        function_layout.addWidget(self.wind_function_name_edit, 0, 1)
        
        # Design Wind Load
        function_layout.addWidget(QLabel("Design Wind Load:"), 1, 0)
        self.design_wind_combo = QComboBox()
        self.design_wind_combo.addItems(["ASCE 7-22", "TIS 1311-50", "Custom"])
        function_layout.addWidget(self.design_wind_combo, 1, 1)
        
        # Equation section
        equation_group = QGroupBox("Equation")
        equation_layout = QGridLayout()
        
        equation_layout.addWidget(QLabel("From:"), 0, 0)
        self.height_from_edit = QLineEdit("1")
        equation_layout.addWidget(self.height_from_edit, 0, 1)
        
        equation_layout.addWidget(QLabel("To:"), 0, 2)
        self.height_to_edit = QLineEdit("50")
        equation_layout.addWidget(self.height_to_edit, 0, 3)
        
        equation_layout.addWidget(QLabel("Inc:"), 0, 4)
        self.height_inc_edit = QLineEdit("1")
        equation_layout.addWidget(self.height_inc_edit, 0, 5)
        
        equation_layout.addWidget(QLabel("Value:"), 1, 0, 1, 4)
        self.equation_value_edit = QLineEdit()
        equation_layout.addWidget(self.equation_value_edit, 1, 4)
        
        self.calculate_wind_eq_btn = QPushButton("Calculate")
        equation_layout.addWidget(self.calculate_wind_eq_btn, 1, 5)
        
        equation_group.setLayout(equation_layout)
        function_layout.addWidget(equation_group, 2, 0, 1, 2)
        
        function_group.setLayout(function_layout)
        layout.addWidget(function_group, 0, 0, 1, 2)
        
        # Direction tabs - simplified version
        direction_tabs = QTabWidget()
        x_tab = QWidget()
        y_tab = QWidget()
        direction_tabs.addTab(x_tab, "X")
        direction_tabs.addTab(y_tab, "Y")
        
        # Table and plot layout for X direction (we'll implement just this for simplicity)
        x_layout = QHBoxLayout()
        
        # Wind pressure table
        wind_table_group = QGroupBox()
        wind_table_layout = QVBoxLayout()
        
        self.wind_table = QTableWidget(10, 2)
        self.wind_table.setHorizontalHeaderLabels(["Z (m)", "Wind Pressure (N/m²)"])
        
        # Populate with sample values
        heights = [25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0]
        pressures = [1287.0, 1294.5, 1301.8, 1309.2, 1316.4, 1323.6, 1330.6, 1337.6, 1344.5, 1351.3]
        
        for i, (height, pressure) in enumerate(zip(heights, pressures)):
            self.wind_table.setItem(i, 0, QTableWidgetItem(f"{height:.1f}"))
            self.wind_table.setItem(i, 1, QTableWidgetItem(f"{pressure:.2f}"))
        
        wind_table_layout.addWidget(self.wind_table)
        wind_table_group.setLayout(wind_table_layout)
        x_layout.addWidget(wind_table_group)
        
        # Wind pressure plot
        wind_plot_group = QGroupBox()
        wind_plot_layout = QVBoxLayout()
        
        if MATPLOTLIB_AVAILABLE:
            try:
                self.wind_figure = Figure(figsize=(5, 4), dpi=100)
                self.wind_canvas = FigureCanvas(self.wind_figure)
                self.wind_axes = self.wind_figure.add_subplot(111)
                self.wind_axes.set_xlabel('Wind Pressure (N/m²)')
                self.wind_axes.set_ylabel('Z (m)')
                self.wind_axes.grid(True, linestyle='--', alpha=0.7)
                
                # Plot initial data
                self.wind_axes.plot(pressures, heights, 'b-', linewidth=2)
                
                # Add a data point marker with annotation
                marker_idx = 0  # First point
                self.wind_axes.plot(pressures[marker_idx], heights[marker_idx], 'bo', markersize=6)
                self.wind_axes.annotate(
                    f"{pressures[marker_idx]:.2f}",
                    xy=(pressures[marker_idx], heights[marker_idx]),
                    xytext=(10, 0), textcoords='offset points',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.7)
                )
                
                # Configure figure to avoid tight_layout warning
                self.configure_figure_layout(self.wind_figure)  # Apply consistent figure settings
                wind_plot_layout.addWidget(self.wind_canvas)
            except Exception as e:
                fallback_label = QLabel("Plot not available: matplotlib error")
                wind_plot_layout.addWidget(fallback_label)
                print(f"Error creating wind plot: {e}")
        else:
            fallback_label = QLabel("Plot not available: matplotlib required")
            wind_plot_layout.addWidget(fallback_label)
        
        wind_plot_group.setLayout(wind_plot_layout)
        x_layout.addWidget(wind_plot_group)
        
        x_tab.setLayout(x_layout)
        
        # Simple layout for Y tab (placeholder)
        y_tab.setLayout(QVBoxLayout())
        y_tab.layout().addWidget(QLabel("Y direction parameters would be shown here"))
        
        layout.addWidget(direction_tabs, 1, 0, 1, 2)
        
        # Wind type section
        type_group = QGroupBox("Type")
        type_layout = QGridLayout()
        
        # Create a simplified type table
        self.wind_type_table = QTableWidget(5, 2)
        self.wind_type_table.setHorizontalHeaderLabels(["", "Wind Pressure (N/m²)"])
        self.wind_type_table.setVerticalHeaderLabels(["Structure", "External", "Roof", "", "Internal"])
        
        # Add some type data
        types = ["", "Windward", "Leeward", "Side", "Windward", "Leeward", "", ""]
        values = ["", "1378.16", "-984.40", "-1378.16", "-1378.16", "-1378.16", "", "-738.30"]
        
        for i in range(len(types)):
            if i < self.wind_type_table.rowCount()*2:
                row = i // 2
                col = i % 2
                if types[i]:
                    self.wind_type_table.setItem(row, col, QTableWidgetItem(types[i]))
        
        for i, value in enumerate(values):
            if i < self.wind_type_table.rowCount() and value:
                self.wind_type_table.setItem(i, 1, QTableWidgetItem(value))
        
        type_layout.addWidget(self.wind_type_table, 0, 0)
        type_group.setLayout(type_layout)
        layout.addWidget(type_group, 2, 0, 1, 2)
        
        # Description field
        description_group = QGroupBox("Description")
        description_layout = QVBoxLayout()
        self.wind_description_edit = QTextEdit()
        self.wind_description_edit.setMaximumHeight(50)
        description_layout.addWidget(self.wind_description_edit)
        description_group.setLayout(description_layout)
        layout.addWidget(description_group, 3, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
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
        
        geometry_group.setLayout(geo_layout)
        layout.addWidget(geometry_group, 0, 0, 1, 2)
        
        # Design Code Selection - Horizontal layout to save vertical space
        code_group = QGroupBox("Design Code")
        code_layout = QHBoxLayout()
        code_layout.setContentsMargins(10, 5, 10, 5)  # Reduce vertical margins
        
        code_layout.addWidget(QLabel("Design Standard:"))
        self.code_combo = QComboBox()
        self.code_combo.addItems(["ASCE 7-22", "TIS 1311-50", "Both"])
        code_layout.addWidget(self.code_combo)
        
        code_group.setLayout(code_layout)
        code_group.setMaximumHeight(60)  # Limit the height of the design code group
        layout.addWidget(code_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_wind_parameters_tab(self):
        """Create wind parameters tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Use a more compact layout with 2 columns to save vertical space
        main_layout = QGridLayout()
        main_layout.setVerticalSpacing(5)  # Reduce vertical spacing
        
        # Wind Speed Group - more compact
        speed_group = QGroupBox("Wind Speed Parameters")
        speed_layout = QGridLayout()
        speed_layout.setContentsMargins(5, 5, 5, 5)  # Smaller margins
        
        speed_layout.addWidget(QLabel("Basic Wind Speed (m/s):"), 0, 0)
        self.wind_speed_edit = QLineEdit(str(self.parameters.basic_wind_speed))
        speed_layout.addWidget(self.wind_speed_edit, 0, 1)
        
        # Exposure Category
        speed_layout.addWidget(QLabel("Exposure Category:"), 1, 0)
        self.exposure_combo = QComboBox()
        self.exposure_combo.addItems(["A", "B", "C", "D"])
        self.exposure_combo.setCurrentText(self.parameters.exposure_category)
        speed_layout.addWidget(self.exposure_combo, 1, 1)
        
        speed_group.setLayout(speed_layout)
        speed_group.setMaximumHeight(100)  # Limit the height
        main_layout.addWidget(speed_group, 0, 0, 1, 2)
        
        # Factors Group - more compact
        factors_group = QGroupBox("Wind Load Factors")
        factors_layout = QGridLayout()
        factors_layout.setContentsMargins(5, 5, 5, 5)  # Smaller margins
        
        factors_layout.addWidget(QLabel("Topographic Factor (Kzt):"), 0, 0)
        self.topo_edit = QLineEdit(str(self.parameters.topographic_factor))
        factors_layout.addWidget(self.topo_edit, 0, 1)
        
        factors_layout.addWidget(QLabel("Directionality Factor (Kd):"), 1, 0)
        self.direction_edit = QLineEdit(str(self.parameters.directionality_factor))
        factors_layout.addWidget(self.direction_edit, 1, 1)
        
        factors_group.setLayout(factors_layout)
        factors_group.setMaximumHeight(100)  # Limit the height
        main_layout.addWidget(factors_group, 1, 0, 1, 2)
        
        layout.addLayout(main_layout, 0, 0)
        widget.setLayout(layout)
        return widget
    
    def create_thai_standards_tab(self):
        """Create Thai standards specific tab"""
        widget = QWidget()
        layout = QGridLayout()
        layout.setVerticalSpacing(10)  # Add spacing between sections
        
        # Thai Location Group - more compact
        location_group = QGroupBox("Thai Location Parameters")
        location_layout = QHBoxLayout()  # Use horizontal layout to save space
        location_layout.setContentsMargins(5, 5, 5, 5)  # Smaller margins
        
        # First column
        location_col1 = QGridLayout()
        location_col1.addWidget(QLabel("Province:"), 0, 0)
        self.province_combo = QComboBox()
        # Add all 77 Thai provinces
        thai_provinces = [
            "Bangkok", "Samut Prakan", "Nonthaburi", "Pathum Thani", "Phra Nakhon Si Ayutthaya",
            "Ang Thong", "Lopburi", "Sing Buri", "Chai Nat", "Saraburi", "Chonburi", "Rayong",
            "Chanthaburi", "Trat", "Chachoengsao", "Prachinburi", "Nakhon Nayok", "Sa Kaeo",
            "Nakhon Ratchasima", "Buriram", "Surin", "Sisaket", "Ubon Ratchathani", "Yasothon",
            "Chaiyaphum", "Amnat Charoen", "Mukdahan", "Nakhon Phanom", "Sakon Nakhon", 
            "Kalasin", "Khon Kaen", "Udon Thani", "Loei", "Nong Bua Lamphu", "Nong Khai",
            "Beung Kan", "Roi Et", "Maha Sarakham", "Tak", "Kamphaeng Phet", "Sukhothai",
            "Phitsanulok", "Phichit", "Phetchabun", "Uthai Thani", "Nakhon Sawan", "Chainat",
            "Kanchanaburi", "Suphan Buri", "Ratchaburi", "Nakhon Pathom", "Samut Sakhon",
            "Samut Songkhram", "Phetchaburi", "Prachuap Khiri Khan", "Nakhon Si Thammarat",
            "Krabi", "Phang Nga", "Phuket", "Surat Thani", "Ranong", "Chumphon", "Songkhla",
            "Satun", "Trang", "Phatthalung", "Pattani", "Yala", "Narathiwat", "Chiang Mai",
            "Lamphun", "Lampang", "Uttaradit", "Phrae", "Nan", "Phayao", "Chiang Rai",
            "Mae Hong Son"
        ]
        self.province_combo.addItems(thai_provinces)
        self.province_combo.setCurrentText(self.parameters.province)
        location_col1.addWidget(self.province_combo, 0, 1)
        
        # Second column
        location_col2 = QGridLayout()
        location_col2.addWidget(QLabel("Wind Zone:"), 0, 0)
        self.wind_zone_combo = QComboBox()
        self.wind_zone_combo.addItems(["Zone_1", "Zone_2", "Zone_3", "Zone_4"])
        location_col2.addWidget(self.wind_zone_combo, 0, 1)
        
        # Add columns to main layout
        location_layout.addLayout(location_col1, 1)
        location_layout.addLayout(location_col2, 1)
        
        location_group.setLayout(location_layout)
        location_group.setMaximumHeight(80)  # Limit the height
        layout.addWidget(location_group, 0, 0, 1, 2)
        
        # Thai Standards Info - more compact
        info_group = QGroupBox("TIS 1311-50 Information")
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(5, 5, 5, 5)  # Smaller margins
        
        info_text = "Thai Standard TIS 1311-50:\n• Covers wind loads for building design\n• Provincial wind speed mapping\n• Compatible with international standards\n• Specific factors for Thai geography"
        info_label = QLabel(info_text)
        info_label.setWordWrap(True)
        info_layout.addWidget(info_label)
        
        info_group.setLayout(info_layout)
        info_group.setMaximumHeight(100)  # Limit the height
        layout.addWidget(info_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_application_tab(self):
        """Create load application tab"""
        widget = QWidget()
        layout = QVBoxLayout()  # Use vertical layout for better arrangement
        layout.setSpacing(10)  # Add spacing between sections
        
        # Single layout for both groups to make more compact
        form_layout = QFormLayout()  # Use form layout for cleaner look
        form_layout.setContentsMargins(5, 5, 5, 5)  # Smaller margins
        
        # Load Case Name
        self.loadcase_edit = QLineEdit(self.parameters.load_case_name)
        form_layout.addRow("Load Case Name:", self.loadcase_edit)
        
        # Application Options - check boxes in a row to save space
        checkbox_layout = QHBoxLayout()
        
        self.apply_checkbox = QCheckBox("Apply to Active Structure")
        self.apply_checkbox.setChecked(self.parameters.apply_to_structure)
        checkbox_layout.addWidget(self.apply_checkbox)
        
        self.auto_calc_checkbox = QCheckBox("Run Analysis")
        checkbox_layout.addWidget(self.auto_calc_checkbox)
        
        self.generate_report_checkbox = QCheckBox("Generate Report")
        checkbox_layout.addWidget(self.generate_report_checkbox)
        
        layout.addLayout(form_layout)
        layout.addLayout(checkbox_layout)
        
        # Add a spacer to push everything to the top
        layout.addStretch(1)
        
        widget.setLayout(layout)
        return widget
    
    def configure_figure_layout(self, figure):
        """Configure figure margins to avoid tight_layout warnings"""
        # These settings ensure enough space for axis labels, title and tick marks
        figure.subplots_adjust(left=0.15, right=0.95, bottom=0.15, top=0.9)
        return figure
        
    def create_results_preview(self):
        """Create results preview group"""
        group = QGroupBox("Wind Load Results Preview")
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 10, 5, 10)  # Add more vertical space
        
        # Use grid layout for better control of text and visualization areas
        results_layout = QGridLayout()
        results_layout.setVerticalSpacing(10)  # Add spacing between elements
        
        # Results summary text with reduced height
        self.results_text = QTextEdit()
        self.results_text.setMaximumHeight(80)  # Reduce text area height
        self.results_text.setPlainText("Wind loads will be displayed here after calculation...")
        results_layout.addWidget(self.results_text, 0, 0)
        
        # Add plot widget if matplotlib is available with increased size
        if MATPLOTLIB_AVAILABLE:
            try:
                self.wind_figure = Figure(figsize=(6, 4), dpi=100)  # Increased figure size
                self.configure_figure_layout(self.wind_figure)  # Apply consistent figure settings
                self.wind_canvas = FigureCanvas(self.wind_figure)
                self.wind_canvas.setMinimumHeight(150)  # Set minimum height for better visibility
                self.wind_axes = self.wind_figure.add_subplot(111)
                results_layout.addWidget(self.wind_canvas, 1, 0)
            except Exception as e:
                print(f"Error creating wind plot: {e}")
        
        layout.addLayout(results_layout)
        group.setLayout(layout)
        
        # Set minimum height for the entire group
        group.setMinimumHeight(250)
        
        return group
    
    def create_action_buttons(self):
        """Create action buttons"""
        layout = QHBoxLayout()
        
        # Calculate Button
        self.calculate_btn = QPushButton("Calculate Wind Loads")
        self.calculate_btn.setStyleSheet("QPushButton { background-color: #2E86AB; color: white; font-weight: bold; padding: 8px; }")
        layout.addWidget(self.calculate_btn)
        
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
        self.calculate_btn.clicked.connect(self.calculate_wind_loads)
        self.apply_btn.clicked.connect(self.apply_loads_to_structure)
        self.analyze_btn.clicked.connect(self.run_structural_analysis)
        self.close_btn.clicked.connect(self.close)
        
        # Real-time updates
        # self.analysis_type_combo.currentTextChanged.connect(self.update_analysis_type)
        # self.spectrum_type_combo.currentTextChanged.connect(self.update_spectrum_type)
        # self.generate_spectrum_btn.clicked.connect(self.generate_asce_spectrum)
        
        # Wind Load Function tab connections
        if hasattr(self, 'calculate_wind_eq_btn'):
            self.calculate_wind_eq_btn.clicked.connect(self.calculate_wind_equation)
        
        if hasattr(self, 'design_wind_combo'):
            self.design_wind_combo.currentTextChanged.connect(self.update_wind_design_code)

    def update_wind_design_code(self):
        """Update wind design code based on combo selection"""
        if hasattr(self, 'design_wind_combo'):
            design_code = self.design_wind_combo.currentText()
            self.parameters.design_code = design_code
            self.calculate_wind_loads()

    def calculate_wind_equation(self):
        """Calculate wind pressure values based on equation"""
        try:
            # Get height range
            if not hasattr(self, 'height_from_edit') or not hasattr(self, 'height_to_edit') or not hasattr(self, 'height_inc_edit'):
                return
            
            height_from = float(self.height_from_edit.text())
            height_to = float(self.height_to_edit.text())
            height_inc = float(self.height_inc_edit.text())
            
            # Generate heights
            heights = []
            current_height = height_from
            while current_height <= height_to:
                heights.append(current_height)
                current_height += height_inc
            
            # Calculate pressures based on a simplified equation
            # In a real implementation, this would use the proper wind pressure equation based on code
            # For now, we'll use a simple increasing function with height
            base_pressure = 1000.0  # Base pressure in N/m²
            pressures = [base_pressure * (1 + 0.01 * h) for h in heights]
            
            # Update the table
            if hasattr(self, 'wind_table'):
                self.wind_table.setRowCount(len(heights))
                for i, (height, pressure) in enumerate(zip(heights, pressures)):
                    self.wind_table.setItem(i, 0, QTableWidgetItem(f"{height:.1f}"))
                    self.wind_table.setItem(i, 1, QTableWidgetItem(f"{pressure:.2f}"))
            
            # Update the plot
            self.plot_wind_pressure(heights, pressures)
            
            # Store the data for reference
            self.wind_heights = heights
            self.wind_pressures = pressures
            
            # Update results text
            self.results_text.append(f"\n✅ Wind pressure calculated for heights {height_from}m to {height_to}m")
            self.results_text.append(f"   Base pressure: {base_pressure:.2f} N/m², Height increment: {height_inc}m")
            
        except (ValueError, AttributeError) as e:
            self.results_text.append(f"\n❌ Error calculating wind equation: {e}")

    def plot_wind_pressure(self, heights=None, pressures=None):
        """Plot wind pressure distribution with professional styling"""
        try:
            if not MATPLOTLIB_AVAILABLE:
                return
            
            # Check if we have plot widgets
            if not hasattr(self, 'wind_axes') or not hasattr(self, 'wind_figure'):
                return
            
            # Use provided data or default values
            if heights is None or pressures is None:
                # Use stored data if available
                if hasattr(self, 'wind_heights') and hasattr(self, 'wind_pressures'):
                    heights = self.wind_heights
                    pressures = self.wind_pressures
                else:
                    # Default sample data
                    heights = [h for h in range(1, 31)]
                    pressures = [1000 * (1 + 0.01 * h) for h in heights]
            
            # Clear the plot
            self.wind_axes.clear()
            
            # Plot with professional styling
            self.wind_axes.plot(pressures, heights, 'b-', linewidth=2.5)
            
            # Add markers at key points
            marker_indices = [0, len(heights)//4, len(heights)//2, 3*len(heights)//4, -1]  # More markers for better visualization
            marker_indices = [i for i in marker_indices if i < len(heights)]
            
            self.wind_axes.plot([pressures[i] for i in marker_indices], 
                              [heights[i] for i in marker_indices], 
                              'bo', markersize=6)
            
            # Add data point labels for better readability
            # Choose multiple points to label to improve understanding of the plot
            for idx in [0, len(heights)//2, -1]:  # Label first, middle, and last points
                if idx < len(heights):
                    self.wind_axes.annotate(
                        f"{pressures[idx]:.2f}",
                        xy=(pressures[idx], heights[idx]),
                        xytext=(10, 0), textcoords='offset points',
                        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.8)
                    )
            
            # Enhanced labels and grid
            self.wind_axes.set_xlabel('Wind Pressure (N/m²)', fontsize=10, fontweight='bold')
            self.wind_axes.set_ylabel('Height (m)', fontsize=10, fontweight='bold')
            self.wind_axes.set_title('Wind Pressure vs. Height', fontsize=12)
            self.wind_axes.grid(True, linestyle='--', alpha=0.7)
            
            # Update x and y limits to show all data with better padding
            x_min = min(pressures) * 0.9 if min(pressures) > 0 else 0
            x_max = max(pressures) * 1.1
            y_min = min(heights) * 0.9 if min(heights) > 0 else 0
            y_max = max(heights) * 1.1
            
            self.wind_axes.set_xlim(x_min, x_max)
            self.wind_axes.set_ylim(y_min, y_max)
            
            # Add horizontal grid lines at more intervals for better readability
            self.wind_axes.yaxis.set_major_locator(plt.MaxNLocator(10))
            
            # Instead of tight_layout, use the pre-configured figure adjustments
            # This prevents the "tight layout not applied" warning
            # self.wind_figure.tight_layout()  # Commented out to avoid warning
            self.wind_canvas.draw()
            
        except Exception as e:
            print(f"Error plotting wind pressure: {e}")
            import traceback
            traceback.print_exc()

    def calculate_wind_loads(self):
        """Calculate wind loads based on selected code"""
        self.update_parameters()
        
        try:
            if not WIND_MODULES_AVAILABLE:
                self.results_text.setPlainText("Wind analysis modules not available - using mock calculation")
                results_text = "Mock Wind Load Results:\n"
                results_text += "="*40 + "\n\n"
                results_text += f"Basic Wind Speed: {self.parameters.basic_wind_speed} m/s\n"
                results_text += f"Building Height: {self.parameters.building_height} m\n"
                results_text += f"Estimated Wind Pressure: {self.parameters.basic_wind_speed**2 * 0.6:.2f} Pa\n"
                self.results_text.setPlainText(results_text)
                return
            
            results_text = f"Wind Load Calculation Results\n"
            results_text += "="*40 + "\n\n"
            
            # Calculate based on selected code
            if "ASCE" in self.parameters.design_code:
                self.calculate_asce_loads()
                results_text += "ASCE 7-22 Wind Loads:\n"
            
            if "TIS" in self.parameters.design_code:
                self.calculate_thai_loads()
                results_text += "TIS 1311-50 Wind Loads:\n"
            
            if "Both" in self.parameters.design_code:
                self.calculate_asce_loads()
                self.calculate_thai_loads()
                results_text += "Comparative Analysis (ASCE vs TIS):\n"
            
            # Display results
            if self.wind_forces:
                results_text += f"Building Height: {self.parameters.building_height} m\n"
                results_text += f"Wind Speed: {self.parameters.basic_wind_speed} m/s\n"
                results_text += f"Exposure: {self.parameters.exposure_category}\n"
                results_text += f"Province: {self.parameters.province}\n\n"
                results_text += "Calculated Wind Forces:\n"
                results_text += f"• Along-wind force: {getattr(self.wind_forces, 'along_wind', 'N/A')} kN\n"
                results_text += f"• Across-wind force: {getattr(self.wind_forces, 'across_wind', 'N/A')} kN\n"
                results_text += f"• Base moment: {getattr(self.wind_forces, 'base_moment', 'N/A')} kN⋅m\n"
            
            self.results_text.setPlainText(results_text)
            self.apply_btn.setEnabled(True)
            
            # Plot wind pressure distribution if available
            self.plot_wind_pressure()
            
        except Exception as e:
            self.results_text.setPlainText(f"Calculation error: {str(e)}")
    
    def load_defaults(self):
        """Load default values"""
        self.update_parameters()
    
    def update_parameters(self):
        """Update parameters from GUI inputs"""
        try:
            self.parameters.building_height = float(self.height_edit.text())
            self.parameters.building_width = float(self.width_edit.text())
            self.parameters.building_length = float(self.length_edit.text())
            self.parameters.basic_wind_speed = float(self.wind_speed_edit.text())
            self.parameters.exposure_category = self.exposure_combo.currentText()
            self.parameters.topographic_factor = float(self.topo_edit.text())
            self.parameters.directionality_factor = float(self.direction_edit.text())
            self.parameters.design_code = self.code_combo.currentText()
            self.parameters.province = self.province_combo.currentText()
            self.parameters.wind_zone = self.wind_zone_combo.currentText()
            self.parameters.load_case_name = self.loadcase_edit.text()
            self.parameters.apply_to_structure = self.apply_checkbox.isChecked()
        except ValueError:
            pass  # Handle invalid input gracefully
    
    def update_thai_parameters(self):
        """Update Thai-specific parameters"""
        province = self.province_combo.currentText()
        # Auto-update wind zone based on province (simplified mapping)
        province_zones = {
            "Bangkok": "Zone_1", "Samut Prakan": "Zone_1", "Nonthaburi": "Zone_1",
            "Chonburi": "Zone_2", "Rayong": "Zone_2", "Phuket": "Zone_3",
            "Songkhla": "Zone_3", "Chiang Mai": "Zone_1", "Nakhon Ratchasima": "Zone_1"
        }
        if province in province_zones:
            zone_index = ["Zone_1", "Zone_2", "Zone_3", "Zone_4"].index(province_zones[province])
            self.wind_zone_combo.setCurrentIndex(zone_index)
    

    
    def calculate_asce_loads(self):
        """Calculate ASCE 7-22 wind loads"""
        try:
            # Create building data for ASCE analysis
            building_data = {
                'height': self.parameters.building_height,
                'width': self.parameters.building_width,
                'length': self.parameters.building_length,
                'wind_speed': self.parameters.basic_wind_speed,
                'exposure': self.parameters.exposure_category,
                'Kzt': self.parameters.topographic_factor,
                'Kd': self.parameters.directionality_factor
            }
            
            # Initialize ASCE wind calculator
            asce_calc = WindLoadASCE7()
            self.wind_forces = asce_calc.calculate_wind_loads(building_data)
            
        except Exception as e:
            print(f"ASCE calculation error: {e}")
    
    def calculate_thai_loads(self):
        """Calculate TIS 1311-50 wind loads"""
        try:
            # Create building data for Thai analysis
            thai_data = {
                'height': self.parameters.building_height,
                'width': self.parameters.building_width,
                'length': self.parameters.building_length,
                'province': self.parameters.province,
                'wind_zone': self.parameters.wind_zone,
                'exposure': self.parameters.exposure_category
            }
            
            # Initialize Thai wind calculator
            thai_calc = ThaiWindLoad()
            thai_forces = thai_calc.calculate_wind_loads(thai_data)
            
            # Store results (prefer Thai if both calculated)
            if not self.wind_forces:
                self.wind_forces = thai_forces
                
        except Exception as e:
            print(f"Thai calculation error: {e}")
    
    def apply_loads_to_structure(self):
        """Apply calculated wind loads to the structure"""
        if not self.wind_forces:
            self.results_text.append("\nNo wind forces calculated!")
            return
        
        try:
            if not CALC_AVAILABLE:
                self.results_text.append("\nStructural analysis system not available!")
                return
            
            # Get active document and structure
            if FREECAD_AVAILABLE and App.ActiveDocument:
                doc = App.ActiveDocument
                
                # Find structural analysis object
                analysis_objects = [obj for obj in doc.Objects if hasattr(obj, 'Proxy') and 'Analysis' in str(type(obj.Proxy))]
                
                if analysis_objects:
                    analysis_obj = analysis_objects[0]
                    
                    # Apply wind loads to the structure
                    self.apply_wind_loads_to_model(analysis_obj)
                    self.results_text.append(f"\n✅ Wind loads applied to structure as '{self.parameters.load_case_name}'")
                    self.analyze_btn.setEnabled(True)
                else:
                    self.results_text.append("\n❌ No structural analysis object found!")
            else:
                # Mock application for testing
                self.results_text.append(f"\n✅ Wind loads would be applied as '{self.parameters.load_case_name}'")
                self.analyze_btn.setEnabled(True)
                
        except Exception as e:
            self.results_text.append(f"\n❌ Error applying loads: {str(e)}")
    
    def apply_wind_loads_to_model(self, analysis_obj):
        """Apply wind forces to the structural model"""
        try:
            # Create wind load objects in the model
            # This integrates with the calc system
            
            # Add distributed loads representing wind pressure
            # Add point loads for concentrated forces
            # Set load case parameters
            
            # Example integration with calc system
            if hasattr(analysis_obj, 'Proxy'):
                proxy = analysis_obj.Proxy
                if hasattr(proxy, 'add_wind_loads'):
                    proxy.add_wind_loads(self.wind_forces, self.parameters.load_case_name)
            
        except Exception as e:
            raise Exception(f"Failed to apply loads to model: {e}")
    
    def run_structural_analysis(self):
        """Run the structural analysis with applied wind loads"""
        try:
            if not CALC_AVAILABLE:
                self.results_text.append("\nStructural analysis system not available!")
                return
            
            self.results_text.append("\n🔄 Running structural analysis...")
            
            # Run the analysis
            if FREECAD_AVAILABLE and App.ActiveDocument:
                doc = App.ActiveDocument
                analysis_objects = [obj for obj in doc.Objects if hasattr(obj, 'Proxy') and 'Analysis' in str(type(obj.Proxy))]
                
                if analysis_objects:
                    analysis_obj = analysis_objects[0]
                    
                    # Execute the analysis
                    analysis_obj.Proxy.execute(analysis_obj)
                    
                    self.results_text.append("✅ Structural analysis completed!")
                    self.results_text.append("✅ Results available in analysis object")
                    
                    # Auto-generate report if requested
                    if hasattr(self, 'generate_report_checkbox') and self.generate_report_checkbox.isChecked():
                        self.generate_wind_report()
                else:
                    self.results_text.append("❌ No analysis object found!")
            else:
                # Mock analysis for testing
                self.results_text.append("✅ Structural analysis would be executed")
                
        except Exception as e:
            self.results_text.append(f"❌ Analysis error: {str(e)}")
    
    def generate_wind_report(self):
        """Generate professional wind load report"""
        try:
            from ..reporting import ProfessionalReportGenerator
            
            report_gen = ProfessionalReportGenerator()
            
            # Prepare report data
            report_data = {
                'project_name': 'Wind Load Analysis',
                'wind_parameters': self.parameters,
                'wind_forces': self.wind_forces,
                'analysis_date': datetime.now(),
                'code_used': self.parameters.design_code
            }
            
            # Generate report
            report = report_gen.generate_wind_report(report_data)
            
            self.results_text.append("\n📄 Wind load report generated successfully!")
            
        except Exception as e:
            self.results_text.append(f"\n❌ Report generation error: {str(e)}")

def show_wind_load_gui():
    """Show the wind load GUI"""
    try:
        # Create Qt Application if needed
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # Create and show the GUI
        dialog = WindLoadGUI()
        dialog.show()
        
        return dialog
        
    except Exception as e:
        print(f"Error showing wind load GUI: {e}")
        return None

# FreeCAD Command Integration
class WindLoadCommand:
    """FreeCAD command for wind load GUI"""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(ICONPATH, "wind_load.svg"),
            'MenuText': 'Wind Load Generator',
            'ToolTip': 'Professional wind load analysis and generation'
        }
    
    def Activated(self):
        """Called when the command is activated"""
        dialog = show_wind_load_gui()
        if dialog:
            dialog.exec_()
    
    def IsActive(self):
        return True

# Register command - Fixed to ensure proper registration
try:
    import FreeCADGui as Gui
    Gui.addCommand("wind_load_gui", WindLoadCommand())
except Exception as e:
    print(f"Failed to register wind_load_gui command: {e}")

# Export for direct usage
__all__ = ['WindLoadGUI', 'WindLoadParameters', 'show_wind_load_gui', 'WindLoadCommand']
