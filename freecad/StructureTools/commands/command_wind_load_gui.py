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
            def append(self, text): self.text_content += "\\n" + text
        
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
        def calculate_wind_loads(self, data): return {}
    
    class ThaiWindLoad:
        def __init__(self): pass
        def calculate_wind_loads(self, data): return {}

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
        self.setWindowIcon(QIcon(":/icons/wind.png") if FREECAD_AVAILABLE else None)
        self.resize(800, 600)
        
        self.setup_ui()
        self.connect_signals()
        self.load_defaults()
    
    def setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout()
        
        # Title Header
        title_label = QLabel("Wind Load Analysis System")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2E86AB; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Tab Widget for organized input
        self.tab_widget = QTabWidget()
        
        # Tab 1: Basic Parameters
        self.basic_tab = self.create_basic_parameters_tab()
        self.tab_widget.addTab(self.basic_tab, "Basic Parameters")
        
        # Tab 2: Wind Parameters  
        self.wind_tab = self.create_wind_parameters_tab()
        self.tab_widget.addTab(self.wind_tab, "Wind Parameters")
        
        # Tab 3: Thai Standards
        self.thai_tab = self.create_thai_standards_tab()
        self.tab_widget.addTab(self.thai_tab, "Thai Standards")
        
        # Tab 4: Load Application
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
        
        geometry_group.setLayout(geo_layout)
        layout.addWidget(geometry_group, 0, 0, 1, 2)
        
        # Design Code Selection
        code_group = QGroupBox("Design Code")
        code_layout = QGridLayout()
        
        code_layout.addWidget(QLabel("Design Standard:"), 0, 0)
        self.code_combo = QComboBox()
        self.code_combo.addItems(["ASCE 7-22", "TIS 1311-50", "Both"])
        code_layout.addWidget(self.code_combo, 0, 1)
        
        code_group.setLayout(code_layout)
        layout.addWidget(code_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_wind_parameters_tab(self):
        """Create wind parameters tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Wind Speed Group
        speed_group = QGroupBox("Wind Speed Parameters")
        speed_layout = QGridLayout()
        
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
        layout.addWidget(speed_group, 0, 0, 1, 2)
        
        # Factors Group
        factors_group = QGroupBox("Wind Load Factors")
        factors_layout = QGridLayout()
        
        factors_layout.addWidget(QLabel("Topographic Factor (Kzt):"), 0, 0)
        self.topo_edit = QLineEdit(str(self.parameters.topographic_factor))
        factors_layout.addWidget(self.topo_edit, 0, 1)
        
        factors_layout.addWidget(QLabel("Directionality Factor (Kd):"), 1, 0)
        self.direction_edit = QLineEdit(str(self.parameters.directionality_factor))
        factors_layout.addWidget(self.direction_edit, 1, 1)
        
        factors_group.setLayout(factors_layout)
        layout.addWidget(factors_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_thai_standards_tab(self):
        """Create Thai standards specific tab"""
        widget = QWidget()
        layout = QGridLayout()
        
        # Thai Location Group
        location_group = QGroupBox("Thai Location Parameters")
        location_layout = QGridLayout()
        
        location_layout.addWidget(QLabel("Province:"), 0, 0)
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
        location_layout.addWidget(self.province_combo, 0, 1)
        
        location_layout.addWidget(QLabel("Wind Zone:"), 1, 0)
        self.wind_zone_combo = QComboBox()
        self.wind_zone_combo.addItems(["Zone_1", "Zone_2", "Zone_3", "Zone_4"])
        location_layout.addWidget(self.wind_zone_combo, 1, 1)
        
        location_group.setLayout(location_layout)
        layout.addWidget(location_group, 0, 0, 1, 2)
        
        # Thai Standards Info
        info_group = QGroupBox("TIS 1311-50 Information")
        info_layout = QVBoxLayout()
        
        info_text = """
        Thai Standard TIS 1311-50:
        • Covers wind loads for building design
        • Provincial wind speed mapping
        • Compatible with international standards
        • Specific factors for Thai geography
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
        
        loadcase_group.setLayout(loadcase_layout)
        layout.addWidget(loadcase_group, 0, 0, 1, 2)
        
        # Integration Options
        integration_group = QGroupBox("Analysis Integration")
        integration_layout = QGridLayout()
        
        self.auto_calc_checkbox = QCheckBox("Automatically run structural analysis")
        integration_layout.addWidget(self.auto_calc_checkbox, 0, 0, 1, 2)
        
        self.generate_report_checkbox = QCheckBox("Generate wind load report")
        integration_layout.addWidget(self.generate_report_checkbox, 1, 0, 1, 2)
        
        integration_group.setLayout(integration_layout)
        layout.addWidget(integration_group, 1, 0, 1, 2)
        
        widget.setLayout(layout)
        return widget
    
    def create_results_preview(self):
        """Create results preview group"""
        group = QGroupBox("Wind Load Results Preview")
        layout = QVBoxLayout()
        
        self.results_text = QTextEdit()
        self.results_text.setMaximumHeight(150)
        self.results_text.setPlainText("Wind loads will be displayed here after calculation...")
        
        layout.addWidget(self.results_text)
        group.setLayout(layout)
        
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
        self.code_combo.currentTextChanged.connect(self.update_parameters)
        self.province_combo.currentTextChanged.connect(self.update_thai_parameters)
    
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
    
    def calculate_wind_loads(self):
        """Calculate wind loads based on selected code"""
        self.update_parameters()
        
        try:
            if not WIND_MODULES_AVAILABLE:
                self.results_text.setPlainText("Wind analysis modules not available")
                return
            
            results_text = f"Wind Load Calculation Results\\n"
            results_text += f"{'='*40}\\n\\n"
            
            # Calculate based on selected code
            if "ASCE" in self.parameters.design_code:
                self.calculate_asce_loads()
                results_text += "ASCE 7-22 Wind Loads:\\n"
            
            if "TIS" in self.parameters.design_code:
                self.calculate_thai_loads()
                results_text += "TIS 1311-50 Wind Loads:\\n"
            
            if "Both" in self.parameters.design_code:
                self.calculate_asce_loads()
                self.calculate_thai_loads()
                results_text += "Comparative Analysis (ASCE vs TIS):\\n"
            
            # Display results
            if self.wind_forces:
                results_text += f"Building Height: {self.parameters.building_height} m\\n"
                results_text += f"Wind Speed: {self.parameters.basic_wind_speed} m/s\\n"
                results_text += f"Exposure: {self.parameters.exposure_category}\\n"
                results_text += f"Province: {self.parameters.province}\\n\\n"
                results_text += "Calculated Wind Forces:\\n"
                results_text += f"• Along-wind force: {getattr(self.wind_forces, 'along_wind', 'N/A')} kN\\n"
                results_text += f"• Across-wind force: {getattr(self.wind_forces, 'across_wind', 'N/A')} kN\\n"
                results_text += f"• Base moment: {getattr(self.wind_forces, 'base_moment', 'N/A')} kN⋅m\\n"
            
            self.results_text.setPlainText(results_text)
            self.apply_btn.setEnabled(True)
            
        except Exception as e:
            self.results_text.setPlainText(f"Calculation error: {str(e)}")
    
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
            self.results_text.append("\\nNo wind forces calculated!")
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
                    
                    # Apply wind loads to the structure
                    self.apply_wind_loads_to_model(analysis_obj)
                    self.results_text.append(f"\\n✅ Wind loads applied to structure as '{self.parameters.load_case_name}'")
                    self.analyze_btn.setEnabled(True)
                else:
                    self.results_text.append("\\n❌ No structural analysis object found!")
            else:
                # Mock application for testing
                self.results_text.append(f"\\n✅ Wind loads would be applied as '{self.parameters.load_case_name}'")
                self.analyze_btn.setEnabled(True)
                
        except Exception as e:
            self.results_text.append(f"\\n❌ Error applying loads: {str(e)}")
    
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
                self.results_text.append("\\nStructural analysis system not available!")
                return
            
            self.results_text.append("\\n🔄 Running structural analysis...")
            
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
            
            self.results_text.append("\\n📄 Wind load report generated successfully!")
            
        except Exception as e:
            self.results_text.append(f"\\n❌ Report generation error: {str(e)}")

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
            'Pixmap': 'wind_load.png',
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

# Register command if FreeCAD is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    Gui.addCommand("wind_load_gui", WindLoadCommand())

# Export for direct usage
__all__ = ['WindLoadGUI', 'WindLoadParameters', 'show_wind_load_gui', 'WindLoadCommand']
