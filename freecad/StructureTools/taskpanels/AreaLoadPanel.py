import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtWidgets, QtGui
import math
import os
import sys

# Import Global Units System
try:
    from ..utils.units_manager import (
        get_units_manager, set_units_system, 
        format_force, format_stress, format_modulus
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN/m²"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"

# Handle numpy import gracefully
try:
    import numpy as np
except ImportError:
    # Mock numpy for basic operations if not available
    class MockNumpy:
        def linspace(self, start, stop, num):
            """Simple linspace implementation"""
            if num <= 1:
                return [start]
            step = (stop - start) / (num - 1)
            return [start + i * step for i in range(num)]
    np = MockNumpy()

# Defensive programming functions for Mock object compatibility
def _safe_set_style(widget, style):
    """Safely set widget stylesheet, tolerant to mocked widgets."""
    try:
        if hasattr(widget, 'setStyleSheet') and callable(getattr(widget, 'setStyleSheet')):
            _safe_call_method(widget, "setStyleSheet", style)
    except Exception:
        pass

def _safe_set_layout(container, layout):
    """Safely set layout on container, tolerant to mocked widgets."""
    try:
        if hasattr(container, 'setLayout') and callable(getattr(container, 'setLayout')):
            container.setLayout(layout)
    except Exception:
        pass

def _safe_add_widget(container, widget, *args, **kwargs):
    """Safely add widget to container, tolerant to mocked widgets."""
    try:
        if hasattr(container, 'addWidget') and callable(getattr(container, 'addWidget')):
            container.addWidget(widget, *args, **kwargs)
    except Exception:
        pass

def _safe_call_method(obj, method_name, *args, **kwargs):
    """Safely call method on object, tolerant to mocked objects."""
    try:
        if hasattr(obj, method_name):
            method = getattr(obj, method_name)
            if callable(method):
                return method(*args, **kwargs)
    except Exception:
        pass
    return None

def _safe_connect(signal_obj, callback):
    """Safely connect signal to callback, tolerant to mocked signals."""
    try:
        if signal_obj is None:
            return
        if hasattr(signal_obj, 'connect') and callable(getattr(signal_obj, 'connect')):
            signal_obj.connect(callback)
        elif callable(signal_obj):
            try:
                signal_obj(callback)
            except Exception:
                pass
    except Exception:
        pass


class AreaLoadApplicationPanel:
    """
    Professional task panel for applying area loads on structural surfaces.
    
    This panel provides comprehensive area load application with real-time preview,
    multiple distribution patterns, and integration with design codes.
    """
    
    def __init__(self, selected_faces=None):
        """
        Initialize area load application panel.
        
        Args:
            selected_faces: List of pre-selected faces to apply loads to
        """
        self.selected_faces = selected_faces or []
        self.preview_objects = []
        self.current_load_object = None
        self.form = self.createUI()
        
        # Load application settings
        self.load_settings = {
            'show_preview': True,
            'arrow_scale': 1.0,
            'arrow_density': 5,
            'auto_update': True
        }
        
        # Populate initial face list
        self.populateSelectedFaces()
        
        # Setup preview if faces are already selected
        if self.selected_faces and self.load_settings['show_preview']:
            self.updatePreview()
    
    def createUI(self):
        """Create the user interface."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Title and instructions
        title_label = QtWidgets.QLabel("Apply Area Load on Surfaces")
        _safe_call_method(title_label, 'setStyleSheet', "font-weight: bold; font-size: 14px; margin-bottom: 5px;")
        _safe_add_widget(layout, title_label)
        
        instruction_label = QtWidgets.QLabel("Select surfaces and define load properties below:")
        _safe_call_method(instruction_label, 'setStyleSheet', "color: gray; font-style: italic; margin-bottom: 10px;")
        _safe_add_widget(layout, instruction_label)
        
        # Create tabbed interface
        self.tab_widget = QtWidgets.QTabWidget()
        
        # Target surfaces tab
        self.surfaces_tab = self.createSurfacesTab()
        _safe_call_method(self.tab_widget, "addTab", self.surfaces_tab, "Target Surfaces")
        
        # Load definition tab
        self.load_tab = self.createLoadDefinitionTab()
        _safe_call_method(self.tab_widget, "addTab", self.load_tab, "Load Definition")
        
        # Distribution tab
        self.distribution_tab = self.createDistributionTab()
        try:
            self.tab_widget.addTab(self.distribution_tab, "Distribution")
        except Exception as e:
            App.Console.PrintWarning(f"Error adding Distribution tab: {e}\n")
            _safe_call_method(self.tab_widget, "addTab", self.distribution_tab, "Distribution")
        
        # Preview tab
        self.preview_tab = self.createPreviewTab()
        _safe_call_method(self.tab_widget, "addTab", self.preview_tab, "Preview & Settings")
        
        _safe_add_widget(layout, self.tab_widget)
        
        # Load summary
        summary_group = self.createLoadSummary()
        _safe_add_widget(layout, summary_group)
        
        # Status bar
        self.status_label = QtWidgets.QLabel("Ready - Select surfaces to apply loads")
        _safe_call_method(self.status_label, "setStyleSheet", "color: blue; font-style: italic; margin-top: 5px;")
        _safe_add_widget(layout, self.status_label)
        
        _safe_set_layout(widget, layout)
        return widget
    
    def createSurfacesTab(self):
        """Create surfaces selection tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Selected faces display
        selection_group = QtWidgets.QGroupBox("Selected Surfaces")
        selection_layout = QtWidgets.QVBoxLayout()
        
        self.face_list = QtWidgets.QListWidget()
        _safe_call_method(self.face_list, "setMaximumHeight", 120)
        _safe_call_method(self.face_list, "setSelectionMode", QtWidgets.QAbstractItemView.ExtendedSelection)
        _safe_add_widget(selection_layout, self.face_list)
        
        # Face selection buttons
        face_button_layout = QtWidgets.QGridLayout()
        
        self.add_faces_btn = QtWidgets.QPushButton("Add Faces")
        _safe_call_method(self.add_faces_btn, 'setToolTip', "Select additional faces in 3D view")
        _safe_connect(getattr(self.add_faces_btn, 'clicked', None), self.addFaces)
        
        self.add_from_selection_btn = QtWidgets.QPushButton("Add from Selection")
        _safe_call_method(self.add_from_selection_btn, 'setToolTip', "Add currently selected faces")
        _safe_connect(getattr(self.add_from_selection_btn, 'clicked', None), self.addFromSelection)
        
        self.remove_faces_btn = QtWidgets.QPushButton("Remove Selected")
        _safe_connect(getattr(self.remove_faces_btn, 'clicked', None), self.removeSelectedFaces)
        
        self.clear_all_btn = QtWidgets.QPushButton("Clear All")
        _safe_connect(getattr(self.clear_all_btn, 'clicked', None), self.clearAllFaces)
        
        face_button_layout.addWidget(self.add_faces_btn, 0, 0)
        face_button_layout.addWidget(self.add_from_selection_btn, 0, 1)
        face_button_layout.addWidget(self.remove_faces_btn, 1, 0)
        face_button_layout.addWidget(self.clear_all_btn, 1, 1)
        
        selection_layout.addLayout(face_button_layout)
        _safe_set_layout(selection_group, selection_layout)
        _safe_add_widget(layout, selection_group)
        
        # Surface properties (read-only)
        properties_group = QtWidgets.QGroupBox("Surface Properties")
        properties_layout = QtWidgets.QFormLayout()
        
        self.total_area_label = QtWidgets.QLabel("0 m²")
        self.num_faces_label = QtWidgets.QLabel("0")
        self.area_range_label = QtWidgets.QLabel("N/A")
        
        properties_layout.addRow("Total Area:", self.total_area_label)
        properties_layout.addRow("Number of Faces:", self.num_faces_label)
        properties_layout.addRow("Area Range:", self.area_range_label)
        
        _safe_set_layout(properties_group, properties_layout)
        _safe_add_widget(layout, properties_group)
        
        # Selection filters
        filter_group = QtWidgets.QGroupBox("Selection Filters")
        filter_layout = QtWidgets.QFormLayout()
        
        self.face_type_filter = QtWidgets.QComboBox()
        _safe_call_method(self.face_type_filter, "addItems", ["All Types", "Planar", "Cylindrical", "Spherical", "Other"])
        _safe_connect(getattr(self.face_type_filter, "currentTextChanged", None), self.applySelectionFilter)
        
        self.min_area_filter = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.min_area_filter, "setRange", 0.0, 1000000.0)
        _safe_call_method(self.min_area_filter, "setValue", 0.0)
        _safe_call_method(self.min_area_filter, "setSuffix", " m²")
        _safe_connect(getattr(self.min_area_filter, "valueChanged", None), self.applySelectionFilter)
        
        filter_layout.addRow("Face Type:", self.face_type_filter)
        filter_layout.addRow("Min Area:", self.min_area_filter)
        _safe_set_layout(filter_group, filter_layout)
        _safe_add_widget(layout, filter_group)
        
        _safe_set_layout(tab, layout)
        return tab
    
    def createLoadDefinitionTab(self):
        """Create load definition tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Load type and category
        type_group = QtWidgets.QGroupBox("Load Type & Category")
        type_layout = QtWidgets.QFormLayout()
        
        self.load_type_combo = QtWidgets.QComboBox()
        load_types = [
            "Dead Load (DL)", "Live Load (LL)", "Live Load Roof (LL_Roof)",
            "Wind Load (W)", "Earthquake (E)", "Earth Pressure (H)",
            "Fluid Pressure (F)", "Thermal (T)", "Custom Pressure"
        ]
        _safe_call_method(self.load_type_combo, "addItems", load_types)
        _safe_connect(getattr(self.load_type_combo, "currentTextChanged", None), self.onLoadTypeChanged)
        type_layout.addRow("Load Type:", self.load_type_combo)
        
        self.load_category_combo = QtWidgets.QComboBox()
        _safe_call_method(self.load_category_combo, "addItems", ["DL", "LL", "LL_Roof", "W", "E", "H", "F", "T", "CUSTOM"])
        type_layout.addRow("Category:", self.load_category_combo)
        
        _safe_set_layout(type_group, type_layout)
        _safe_add_widget(layout, type_group)
        
        # Load magnitude
        magnitude_group = QtWidgets.QGroupBox("Load Magnitude")
        magnitude_layout = QtWidgets.QFormLayout()
        
        self.magnitude_input = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.magnitude_input, "setRange", -1000.0, 1000.0)
        _safe_call_method(self.magnitude_input, "setValue", 5.0)
        self.magnitude_input.setDecimals(3)
        _safe_call_method(self.magnitude_input, "setSuffix", " kN/m²")
        _safe_connect(getattr(self.magnitude_input, "valueChanged", None), self.onMagnitudeChanged)
        magnitude_layout.addRow("Magnitude:", self.magnitude_input)
        
        self.magnitude_unit_combo = QtWidgets.QComboBox()
        _safe_call_method(self.magnitude_unit_combo, "addItems", ["kN/m²", "N/m²", "kPa", "MPa", "psf", "psi"])
        _safe_connect(getattr(self.magnitude_unit_combo, "currentTextChanged", None), self.onUnitChanged)
        magnitude_layout.addRow("Unit:", self.magnitude_unit_combo)
        
        _safe_set_layout(magnitude_group, magnitude_layout)
        _safe_add_widget(layout, magnitude_group)
        
        # Load direction
        direction_group = QtWidgets.QGroupBox("Load Direction")
        direction_layout = QtWidgets.QFormLayout()
        
        self.direction_combo = QtWidgets.QComboBox()
        directions = ["Normal to Surface", "+X Global", "-X Global", 
                     "+Y Global", "-Y Global", "+Z Global", "-Z Global", "Custom"]
        _safe_call_method(self.direction_combo, "addItems", directions)
        _safe_connect(getattr(self.direction_combo, "currentTextChanged", None), self.onDirectionChanged)
        direction_layout.addRow("Direction:", self.direction_combo)
        
        # Custom direction input
        custom_layout = QtWidgets.QHBoxLayout()
        self.custom_x = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.custom_x, "setRange", -1.0, 1.0)
        self.custom_x.setDecimals(3)
        _safe_call_method(self.custom_x, "setValue", 0.0)
        
        self.custom_y = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.custom_y, "setRange", -1.0, 1.0)
        self.custom_y.setDecimals(3)
        _safe_call_method(self.custom_y, "setValue", 0.0)
        
        self.custom_z = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.custom_z, "setRange", -1.0, 1.0)
        self.custom_z.setDecimals(3)
        _safe_call_method(self.custom_z, "setValue", -1.0)
        
        _safe_add_widget(custom_layout, QtWidgets.QLabel("X:"))
        _safe_add_widget(custom_layout, self.custom_x)
        _safe_add_widget(custom_layout, QtWidgets.QLabel("Y:"))
        _safe_add_widget(custom_layout, self.custom_y)
        _safe_add_widget(custom_layout, QtWidgets.QLabel("Z:"))
        _safe_add_widget(custom_layout, self.custom_z)
        
        self.normalize_btn = QtWidgets.QPushButton("Normalize")
        _safe_connect(getattr(self.normalize_btn, "clicked", None), self.normalizeCustomDirection)
        _safe_add_widget(custom_layout, self.normalize_btn)
        
        direction_layout.addRow("Custom Vector:", custom_layout)
        _safe_set_layout(direction_group, direction_layout)
        _safe_add_widget(layout, direction_group)
        
        # Load case information
        case_group = QtWidgets.QGroupBox("Load Case Information")
        case_layout = QtWidgets.QFormLayout()
        
        self.load_case_input = QtWidgets.QLineEdit()
        self.load_case_input.setText("DL1")
        _safe_connect(getattr(self.load_case_input, "textChanged", None), self.onLoadCaseChanged)
        case_layout.addRow("Load Case Name:", self.load_case_input)
        
        self.load_factor_input = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.load_factor_input, "setRange", 0.0, 10.0)
        _safe_call_method(self.load_factor_input, "setValue", 1.0)
        self.load_factor_input.setDecimals(2)
        case_layout.addRow("Load Factor:", self.load_factor_input)
        
        self.description_input = QtWidgets.QLineEdit()
        self.description_input.setPlaceholderText("Optional load description")
        case_layout.addRow("Description:", self.description_input)
        
        _safe_set_layout(case_group, case_layout)
        _safe_add_widget(layout, case_group)
        
        _safe_set_layout(tab, layout)
        return tab
    
    def createDistributionTab(self):
        """Create load distribution tab."""
        App.Console.PrintMessage("Creating Distribution tab with OneWay/TwoWay options...\n")
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Distribution pattern
        pattern_group = QtWidgets.QGroupBox("Distribution Pattern")
        pattern_layout = QtWidgets.QFormLayout()
        
        self.distribution_combo = QtWidgets.QComboBox()
        distributions = ["Uniform", "Linear X", "Linear Y", "Bilinear", "Parabolic", "Point Load", "User Defined"]
        _safe_call_method(self.distribution_combo, "addItems", distributions)
        _safe_connect(getattr(self.distribution_combo, "currentTextChanged", None), self.onDistributionChanged)
        pattern_layout.addRow("Pattern:", self.distribution_combo)
        
        _safe_set_layout(pattern_group, pattern_layout)
        _safe_add_widget(layout, pattern_group)
        
        # Load transfer method group
        transfer_group = QtWidgets.QGroupBox("Load Transfer Method")
        transfer_layout = QtWidgets.QFormLayout()
        
        App.Console.PrintMessage("Adding OneWay/TwoWay distribution options...\n")
        
        # Load distribution method (OneWay vs TwoWay)
        self.load_distribution_combo = QtWidgets.QComboBox()
        distribution_methods = ["TwoWay", "OneWay", "OpenStructure"]
        try:
            self.load_distribution_combo.addItems(distribution_methods)
            App.Console.PrintMessage(f"Added distribution methods: {distribution_methods}\n")
        except Exception as e:
            App.Console.PrintWarning(f"Error adding distribution methods: {e}\n")
            _safe_call_method(self.load_distribution_combo, "addItems", distribution_methods)
        _safe_connect(getattr(self.load_distribution_combo, "currentTextChanged", None), self.onLoadDistributionChanged)
        transfer_layout.addRow("Distribution Method:", self.load_distribution_combo)
        
        # OneWay direction (enabled only for OneWay method)
        self.oneway_direction_combo = QtWidgets.QComboBox()
        oneway_directions = ["X", "Y", "Custom"]
        _safe_call_method(self.oneway_direction_combo, "addItems", oneway_directions)
        _safe_connect(getattr(self.oneway_direction_combo, "currentTextChanged", None), self.onOneWayDirectionChanged)
        transfer_layout.addRow("OneWay Direction:", self.oneway_direction_combo)
        
        # Custom direction input (enabled only for Custom OneWay)
        self.custom_direction_layout = QtWidgets.QHBoxLayout()
        self.custom_x_input = QtWidgets.QDoubleSpinBox()
        self.custom_x_input.setRange(-1.0, 1.0)
        self.custom_x_input.setSingleStep(0.1)
        self.custom_x_input.setValue(1.0)
        self.custom_y_input = QtWidgets.QDoubleSpinBox()
        self.custom_y_input.setRange(-1.0, 1.0)
        self.custom_y_input.setSingleStep(0.1)
        self.custom_y_input.setValue(0.0)
        self.custom_z_input = QtWidgets.QDoubleSpinBox()
        self.custom_z_input.setRange(-1.0, 1.0)
        self.custom_z_input.setSingleStep(0.1)
        self.custom_z_input.setValue(0.0)
        
        self.custom_direction_layout.addWidget(QtWidgets.QLabel("X:"))
        self.custom_direction_layout.addWidget(self.custom_x_input)
        self.custom_direction_layout.addWidget(QtWidgets.QLabel("Y:"))
        self.custom_direction_layout.addWidget(self.custom_y_input)
        self.custom_direction_layout.addWidget(QtWidgets.QLabel("Z:"))
        self.custom_direction_layout.addWidget(self.custom_z_input)
        
        custom_widget = QtWidgets.QWidget()
        custom_widget.setLayout(self.custom_direction_layout)
        transfer_layout.addRow("Custom Direction:", custom_widget)
        
        # Distribution factors
        self.distribution_factors_input = QtWidgets.QLineEdit()
        self.distribution_factors_input.setText("1.0, 1.0, 1.0, 1.0")
        self.distribution_factors_input.setToolTip("Distribution factors for load edges (comma-separated)")
        transfer_layout.addRow("Distribution Factors:", self.distribution_factors_input)
        
        _safe_set_layout(transfer_group, transfer_layout)
        _safe_add_widget(layout, transfer_group)
        
        # Initialize transfer method controls
        self.updateLoadTransferControls()
        
        # Distribution parameters (varies by pattern)
        self.params_group = QtWidgets.QGroupBox("Distribution Parameters")
        self.params_layout = QtWidgets.QFormLayout()
        _safe_set_layout(self.params_group, self.params_layout)
        _safe_add_widget(layout, self.params_group)
        
        # Spatial variation
        spatial_group = QtWidgets.QGroupBox("Spatial Variation")
        spatial_layout = QtWidgets.QFormLayout()
        
        # Variation center
        center_layout = QtWidgets.QHBoxLayout()
        self.center_x = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.center_x, "setRange", -10000.0, 10000.0)
        _safe_call_method(self.center_x, "setValue", 0.0)
        _safe_call_method(self.center_x, "setSuffix", " mm")
        
        self.center_y = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.center_y, "setRange", -10000.0, 10000.0)
        _safe_call_method(self.center_y, "setValue", 0.0)
        _safe_call_method(self.center_y, "setSuffix", " mm")
        
        self.center_z = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.center_z, "setRange", -10000.0, 10000.0)
        _safe_call_method(self.center_z, "setValue", 0.0)
        _safe_call_method(self.center_z, "setSuffix", " mm")
        
        self.pick_center_btn = QtWidgets.QPushButton("Pick")
        _safe_call_method(self.pick_center_btn, "setToolTip", "Pick center point from 3D view")
        _safe_connect(getattr(self.pick_center_btn, "clicked", None), self.pickVariationCenter)
        
        _safe_add_widget(center_layout, self.center_x)
        _safe_add_widget(center_layout, self.center_y)
        _safe_add_widget(center_layout, self.center_z)
        _safe_add_widget(center_layout, self.pick_center_btn)
        spatial_layout.addRow("Variation Center:", center_layout)
        
        self.variation_radius = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.variation_radius, "setRange", 1.0, 100000.0)
        _safe_call_method(self.variation_radius, "setValue", 1000.0)
        _safe_call_method(self.variation_radius, "setSuffix", " mm")
        spatial_layout.addRow("Variation Radius:", self.variation_radius)
        
        _safe_set_layout(spatial_group, spatial_layout)
        _safe_add_widget(layout, spatial_group)
        
        # Custom function
        custom_group = QtWidgets.QGroupBox("Custom Distribution Function")
        custom_layout = QtWidgets.QVBoxLayout()
        
        function_label = QtWidgets.QLabel("Python expression (use x, y, z coordinates):")
        _safe_add_widget(custom_layout, function_label)
        
        self.custom_function_input = QtWidgets.QTextEdit()
        _safe_call_method(self.custom_function_input, "setMaximumHeight", 60)
        self.custom_function_input.setText("1.0")
        self.custom_function_input.setPlaceholderText("Example: 1.0 + 0.5*sin(x/1000)")
        _safe_add_widget(custom_layout, self.custom_function_input)
        
        function_buttons = QtWidgets.QHBoxLayout()
        self.validate_function_btn = QtWidgets.QPushButton("Validate Function")
        _safe_connect(getattr(self.validate_function_btn, "clicked", None), self.validateCustomFunction)
        self.example_functions_btn = QtWidgets.QPushButton("Examples...")
        _safe_connect(getattr(self.example_functions_btn, "clicked", None), self.showExampleFunctions)
        
        _safe_add_widget(function_buttons, self.validate_function_btn)
        _safe_add_widget(function_buttons, self.example_functions_btn)
        custom_layout.addLayout(function_buttons)
        
        _safe_set_layout(custom_group, custom_layout)
        _safe_add_widget(layout, custom_group)
        
        # Initialize distribution parameters
        self.updateDistributionParameters()
        
        _safe_set_layout(tab, layout)
        return tab
    
    def createPreviewTab(self):
        """Create preview and settings tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Preview controls
        preview_group = QtWidgets.QGroupBox("Preview Controls")
        preview_layout = QtWidgets.QFormLayout()
        
        self.show_preview_check = QtWidgets.QCheckBox("Show Load Preview")
        _safe_call_method(self.show_preview_check, "setChecked", True)
        _safe_connect(getattr(self.show_preview_check, "toggled", None), self.togglePreview)
        preview_layout.addRow(self.show_preview_check)
        
        self.arrow_scale_spin = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.arrow_scale_spin, "setRange", 0.1, 10.0)
        _safe_call_method(self.arrow_scale_spin, "setValue", 1.0)
        self.arrow_scale_spin.setDecimals(2)
        _safe_connect(getattr(self.arrow_scale_spin, "valueChanged", None), self.updatePreviewSettings)
        preview_layout.addRow("Arrow Scale:", self.arrow_scale_spin)
        
        self.arrow_density_spin = QtWidgets.QSpinBox()
        _safe_call_method(self.arrow_density_spin, "setRange", 2, 20)
        _safe_call_method(self.arrow_density_spin, "setValue", 5)
        _safe_connect(getattr(self.arrow_density_spin, "valueChanged", None), self.updatePreviewSettings)
        preview_layout.addRow("Arrow Density:", self.arrow_density_spin)
        
        self.auto_update_check = QtWidgets.QCheckBox("Auto Update Preview")
        _safe_call_method(self.auto_update_check, "setChecked", True)
        _safe_connect(getattr(self.auto_update_check, "toggled", None), self.toggleAutoUpdate)
        preview_layout.addRow(self.auto_update_check)
        
        _safe_set_layout(preview_group, preview_layout)
        _safe_add_widget(layout, preview_group)
        
        # Manual update button
        self.manual_update_btn = QtWidgets.QPushButton("Update Preview Now")
        _safe_connect(getattr(self.manual_update_btn, "clicked", None), self.updatePreview)
        _safe_add_widget(layout, self.manual_update_btn)
        
        # Color settings
        color_group = QtWidgets.QGroupBox("Visualization Colors")
        color_layout = QtWidgets.QFormLayout()
        
        self.load_color_btn = QtWidgets.QPushButton()
        _safe_call_method(self.load_color_btn, "setStyleSheet", "background-color: red; min-height: 20px;")
        _safe_connect(getattr(self.load_color_btn, "clicked", None), self.chooseLoadColor)
        color_layout.addRow("Load Color:", self.load_color_btn)
        
        self.arrow_transparency_spin = QtWidgets.QSpinBox()
        _safe_call_method(self.arrow_transparency_spin, "setRange", 0, 90)
        _safe_call_method(self.arrow_transparency_spin, "setValue", 20)
        _safe_call_method(self.arrow_transparency_spin, "setSuffix", "%")
        color_layout.addRow("Transparency:", self.arrow_transparency_spin)
        
        _safe_set_layout(color_group, color_layout)
        _safe_add_widget(layout, color_group)
        
        # Preview statistics
        stats_group = QtWidgets.QGroupBox("Preview Statistics")
        stats_layout = QtWidgets.QFormLayout()
        
        self.num_arrows_label = QtWidgets.QLabel("0")
        self.total_force_label = QtWidgets.QLabel("0 kN")
        self.resultant_label = QtWidgets.QLabel("(0, 0, 0)")
        self.load_center_label = QtWidgets.QLabel("(0, 0, 0)")
        
        stats_layout.addRow("Number of Arrows:", self.num_arrows_label)
        stats_layout.addRow("Total Force:", self.total_force_label)
        stats_layout.addRow("Resultant Vector:", self.resultant_label)
        stats_layout.addRow("Load Center:", self.load_center_label)
        
        _safe_set_layout(stats_group, stats_layout)
        _safe_add_widget(layout, stats_group)
        
        _safe_set_layout(tab, layout)
        return tab
    
    def createLoadSummary(self):
        """Create load summary group."""
        summary_group = QtWidgets.QGroupBox("Load Summary")
        summary_layout = QtWidgets.QFormLayout()
        
        self.summary_magnitude_label = QtWidgets.QLabel("0 kN/m²")
        self.summary_total_force_label = QtWidgets.QLabel("0 kN")
        self.summary_area_label = QtWidgets.QLabel("0 m²")
        self.summary_direction_label = QtWidgets.QLabel("Normal")
        
        summary_layout.addRow("Magnitude:", self.summary_magnitude_label)
        summary_layout.addRow("Total Area:", self.summary_area_label)
        summary_layout.addRow("Total Force:", self.summary_total_force_label)
        summary_layout.addRow("Direction:", self.summary_direction_label)
        
        _safe_set_layout(summary_group, summary_layout)
        return summary_group
    
    def updateLoadTransferControls(self):
        """Update load transfer control visibility based on selected method."""
        try:
            if not hasattr(self, 'load_distribution_combo'):
                return
                
            method = self.load_distribution_combo.currentText()
            
            # Enable/disable OneWay direction controls
            is_oneway = (method == "OneWay")
            if hasattr(self, 'oneway_direction_combo'):
                self.oneway_direction_combo.setEnabled(is_oneway)
            
            # Enable/disable custom direction inputs
            is_custom = False
            if is_oneway and hasattr(self, 'oneway_direction_combo'):
                is_custom = (self.oneway_direction_combo.currentText() == "Custom")
            
            if hasattr(self, 'custom_x_input'):
                self.custom_x_input.setEnabled(is_custom)
                self.custom_y_input.setEnabled(is_custom)  
                self.custom_z_input.setEnabled(is_custom)
            
            # Update preview if available
            if hasattr(self, 'updatePreview'):
                self.updatePreview()
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating load transfer controls: {e}\n")
    
    def onLoadDistributionChanged(self):
        """Handle load distribution method change."""
        self.updateLoadTransferControls()
    
    def onOneWayDirectionChanged(self):
        """Handle OneWay direction change."""
        self.updateLoadTransferControls()
    
    def populateSelectedFaces(self):
        """Populate the selected faces list."""
        self.face_list.clear()
        
        for i, face in enumerate(self.selected_faces):
            if hasattr(face, 'Label'):
                item_text = f"{face.Label} - Face {i+1}"
            else:
                item_text = f"Face {i+1}"
            
            _safe_call_method(self.face_list, "addItem", item_text)
        
        self.updateSurfaceProperties()
    
    def updateSurfaceProperties(self):
        """Update surface properties display."""
        if not self.selected_faces:
            self.total_area_label.setText("0 m²")
            self.num_faces_label.setText("0")
            self.area_range_label.setText("N/A")
            return
        
        try:
            total_area = 0.0
            areas = []
            
            for face in self.selected_faces:
                if hasattr(face, 'Shape'):
                    shape = face.Shape
                    if hasattr(shape, 'Faces'):
                        for f in shape.Faces:
                            area = f.Area / 1000000.0  # Convert mm² to m²
                            areas.append(area)
                            total_area += area
                    elif hasattr(shape, 'Area'):
                        area = shape.Area / 1000000.0
                        areas.append(area)
                        total_area += area
            
            self.total_area_label.setText(f"{total_area:.3f} m²")
            self.num_faces_label.setText(str(len(self.selected_faces)))
            
            if areas:
                min_area = min(areas)
                max_area = max(areas)
                self.area_range_label.setText(f"{min_area:.3f} - {max_area:.3f} m²")
            else:
                self.area_range_label.setText("N/A")
            
            self.updateLoadSummary()
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating surface properties: {e}\n")
    
    def updateDistributionParameters(self):
        """Update distribution parameters based on selected pattern."""
        # Clear existing parameters
        for i in reversed(range(self.params_layout.count())):
            child = self.params_layout.itemAt(i).widget()
            if child:
                child.setParent(None)
        
        distribution = self.distribution_combo.currentText()
        
        if distribution == "Uniform":
            # No additional parameters needed
            label = QtWidgets.QLabel("No additional parameters required")
            self.params_layout.addRow(label)
            
        elif distribution in ["Linear X", "Linear Y"]:
            self.min_factor_spin = QtWidgets.QDoubleSpinBox()
            _safe_call_method(self.min_factor_spin, "setRange", 0.0, 10.0)
            _safe_call_method(self.min_factor_spin, "setValue", 0.5)
            self.min_factor_spin.setDecimals(2)
            
            self.max_factor_spin = QtWidgets.QDoubleSpinBox()
            _safe_call_method(self.max_factor_spin, "setRange", 0.0, 10.0)
            _safe_call_method(self.max_factor_spin, "setValue", 1.5)
            self.max_factor_spin.setDecimals(2)
            
            direction = "X" if "X" in distribution else "Y"
            self.params_layout.addRow(f"Min Factor ({direction}=0):", self.min_factor_spin)
            self.params_layout.addRow(f"Max Factor ({direction}=1):", self.max_factor_spin)
            
        elif distribution == "Bilinear":
            # Four corner factors
            self.corner_factors = []
            corners = ["(0,0)", "(1,0)", "(1,1)", "(0,1)"]
            
            for i, corner in enumerate(corners):
                factor_spin = QtWidgets.QDoubleSpinBox()
                _safe_call_method(factor_spin, "setRange", 0.0, 10.0)
                _safe_call_method(factor_spin, "setValue", 1.0)
                factor_spin.setDecimals(2)
                self.corner_factors.append(factor_spin)
                self.params_layout.addRow(f"Factor at {corner}:", factor_spin)
                
        elif distribution == "Parabolic":
            self.vertex_factor_spin = QtWidgets.QDoubleSpinBox()
            _safe_call_method(self.vertex_factor_spin, "setRange", 0.0, 10.0)
            _safe_call_method(self.vertex_factor_spin, "setValue", 2.0)
            self.vertex_factor_spin.setDecimals(2)
            
            self.edge_factor_spin = QtWidgets.QDoubleSpinBox()
            _safe_call_method(self.edge_factor_spin, "setRange", 0.0, 10.0)
            _safe_call_method(self.edge_factor_spin, "setValue", 0.5)
            self.edge_factor_spin.setDecimals(2)
            
            self.params_layout.addRow("Center Factor:", self.vertex_factor_spin)
            self.params_layout.addRow("Edge Factor:", self.edge_factor_spin)
            
        elif distribution == "Point Load":
            point_layout = QtWidgets.QHBoxLayout()
            
            self.point_u = QtWidgets.QDoubleSpinBox()
            _safe_call_method(self.point_u, "setRange", 0.0, 1.0)
            _safe_call_method(self.point_u, "setValue", 0.5)
            self.point_u.setDecimals(3)
            
            self.point_v = QtWidgets.QDoubleSpinBox()
            _safe_call_method(self.point_v, "setRange", 0.0, 1.0)
            _safe_call_method(self.point_v, "setValue", 0.5)
            self.point_v.setDecimals(3)
            
            _safe_add_widget(point_layout, QtWidgets.QLabel("U:"))
            _safe_add_widget(point_layout, self.point_u)
            _safe_add_widget(point_layout, QtWidgets.QLabel("V:"))
            _safe_add_widget(point_layout, self.point_v)
            
            self.params_layout.addRow("Point Location:", point_layout)
            
        elif distribution == "User Defined":
            note_label = QtWidgets.QLabel("Define custom function in 'Custom Distribution Function' section")
            _safe_call_method(note_label, "setStyleSheet", "color: blue; font-style: italic;")
            self.params_layout.addRow(note_label)
    
    def updateLoadSummary(self):
        """Update load summary display."""
        try:
            # Get magnitude
            magnitude = self.magnitude_input.value()
            unit = self.magnitude_unit_combo.currentText()
            
            # Convert to kN/m² for display
            magnitude_kn_m2 = self.convertToKnM2(magnitude, unit)
            
            # Get total area
            total_area_text = self.total_area_label.text()
            if total_area_text != "0 m²":
                total_area = float(total_area_text.split()[0])
                total_force = magnitude_kn_m2 * total_area
            else:
                total_area = 0.0
                total_force = 0.0
            
            # Update summary labels
            self.summary_magnitude_label.setText(f"{magnitude_kn_m2:.3f} kN/m²")
            self.summary_area_label.setText(f"{total_area:.3f} m²")
            self.summary_total_force_label.setText(f"{total_force:.2f} kN")
            self.summary_direction_label.setText(self.direction_combo.currentText())
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating load summary: {e}\n")
    
    def convertToKnM2(self, value, unit):
        """Convert magnitude to kN/m² for display."""
        conversion_factors = {
            "kN/m²": 1.0,
            "N/m²": 0.001,
            "kPa": 1.0,
            "MPa": 1000.0,
            "psf": 0.0479,  # pounds per square foot
            "psi": 6.895    # pounds per square inch
        }
        return value * conversion_factors.get(unit, 1.0)
    
    # Event handlers
    def onLoadTypeChanged(self, load_type):
        """Handle load type change."""
        # Auto-update load category
        category_map = {
            "Dead Load (DL)": "DL",
            "Live Load (LL)": "LL", 
            "Live Load Roof (LL_Roof)": "LL_Roof",
            "Wind Load (W)": "W",
            "Earthquake (E)": "E",
            "Earth Pressure (H)": "H",
            "Fluid Pressure (F)": "F",
            "Thermal (T)": "T",
            "Custom Pressure": "CUSTOM"
        }
        
        if load_type in category_map:
            self.load_category_combo.setCurrentText(category_map[load_type])
        
        self.updateStatus(f"Load type changed to {load_type}")
        if self.load_settings['auto_update']:
            self.updatePreview()
    
    def onMagnitudeChanged(self, value):
        """Handle magnitude change."""
        self.updateLoadSummary()
        if self.load_settings['auto_update']:
            self.updatePreview()
    
    def onUnitChanged(self, unit):
        """Handle unit change."""
        self.updateLoadSummary()
        if self.load_settings['auto_update']:
            self.updatePreview()
    
    def onDirectionChanged(self, direction):
        """Handle direction change."""
        # Enable/disable custom direction inputs
        is_custom = (direction == "Custom")
        self.custom_x.setEnabled(is_custom)
        self.custom_y.setEnabled(is_custom)
        self.custom_z.setEnabled(is_custom)
        self.normalize_btn.setEnabled(is_custom)
        
        self.updateLoadSummary()
        if self.load_settings['auto_update']:
            self.updatePreview()
    
    def onDistributionChanged(self, distribution):
        """Handle distribution pattern change."""
        self.updateDistributionParameters()
        if self.load_settings['auto_update']:
            self.updatePreview()
    
    def onLoadCaseChanged(self, case_name):
        """Handle load case name change."""
        if self.load_settings['auto_update']:
            self.updatePreview()
    
    # Actions
    def addFaces(self):
        """Add faces using interactive selection."""
        self.updateStatus("Select faces in 3D view, then click 'Add from Selection'")
    
    def addFromSelection(self):
        """Add currently selected faces."""
        selection = Gui.Selection.getSelection()
        added_count = 0
        
        for obj in selection:
            if hasattr(obj, 'Shape') and obj not in self.selected_faces:
                self.selected_faces.append(obj)
                added_count += 1
        
        if added_count > 0:
            self.populateSelectedFaces()
            self.updateStatus(f"Added {added_count} face(s)")
            if self.load_settings['auto_update']:
                self.updatePreview()
        else:
            self.updateStatus("No new faces to add")
    
    def removeSelectedFaces(self):
        """Remove selected faces from list."""
        selected_items = self.face_list.selectedItems()
        if not selected_items:
            self.updateStatus("No faces selected for removal")
            return
        
        # Get indices of selected items
        indices = [self.face_list.row(item) for item in selected_items]
        indices.sort(reverse=True)  # Remove from end to avoid index shifting
        
        # Remove from selected_faces list
        for index in indices:
            if 0 <= index < len(self.selected_faces):
                del self.selected_faces[index]
        
        self.populateSelectedFaces()
        self.clearPreview()
        self.updateStatus(f"Removed {len(indices)} face(s)")
    
    def clearAllFaces(self):
        """Clear all selected faces."""
        self.selected_faces.clear()
        self.populateSelectedFaces()
        self.clearPreview()
        self.updateStatus("All faces cleared")
    
    def applySelectionFilter(self):
        """Apply selection filters."""
        # This would filter the face list based on criteria
        self.updateStatus("Selection filter applied")
    
    def normalizeCustomDirection(self):
        """Normalize custom direction vector."""
        x = self.custom_x.value()
        y = self.custom_y.value()
        z = self.custom_z.value()
        
        length = math.sqrt(x*x + y*y + z*z)
        if length > 0:
            _safe_call_method(self.custom_x, "setValue", x / length)
            _safe_call_method(self.custom_y, "setValue", y / length)
            _safe_call_method(self.custom_z, "setValue", z / length)
            self.updateStatus("Direction vector normalized")
        else:
            self.updateStatus("Cannot normalize zero vector", "red")
    
    def pickVariationCenter(self):
        """Pick variation center from 3D view."""
        self.updateStatus("Pick center point functionality would be implemented here")
    
    def validateCustomFunction(self):
        """Validate custom distribution function."""
        function_text = self.custom_function_input.toPlainText()
        
        try:
            # Test the function with sample coordinates
            x, y, z = 100.0, 200.0, 0.0
            result = eval(function_text)
            
            if isinstance(result, (int, float)):
                self.updateStatus(f"Function valid. Test result: {result:.3f}")
            else:
                self.updateStatus("Function must return a number", "red")
                
        except Exception as e:
            self.updateStatus(f"Function error: {str(e)}", "red")
    
    def showExampleFunctions(self):
        """Show example distribution functions."""
        examples = [
            "1.0  # Uniform",
            "1.0 + 0.5*sin(x/1000)  # Sinusoidal in X",
            "1.0 + 0.3*cos(y/500)   # Cosine in Y",
            "1.0 - 0.2*(x**2 + y**2)/1000000  # Parabolic",
            "1.0 if abs(x) < 500 else 0.5  # Step function"
        ]
        
        example_text = "\n".join(examples)
        QtWidgets.QMessageBox.information(self, "Example Functions", example_text)
    
    def togglePreview(self, enabled):
        """Toggle preview display."""
        self.load_settings['show_preview'] = enabled
        if enabled:
            self.updatePreview()
        else:
            self.clearPreview()
    
    def toggleAutoUpdate(self, enabled):
        """Toggle auto-update preview."""
        self.load_settings['auto_update'] = enabled
        self.manual_update_btn.setEnabled(not enabled)
    
    def updatePreviewSettings(self):
        """Update preview settings."""
        self.load_settings['arrow_scale'] = self.arrow_scale_spin.value()
        self.load_settings['arrow_density'] = self.arrow_density_spin.value()
        
        if self.load_settings['auto_update']:
            self.updatePreview()
    
    def chooseLoadColor(self):
        """Choose load arrow color."""
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            _safe_call_method(self.load_color_btn, "setStyleSheet", f"background-color: {color.name()}; min-height: 20px;")
            if self.load_settings['auto_update']:
                self.updatePreview()
    
    def updatePreview(self):
        """Update load preview visualization."""
        if not self.load_settings['show_preview'] or not self.selected_faces:
            return
        
        try:
            self.clearPreview()
            
            # Create preview arrows for each face
            arrow_count = 0
            for face in self.selected_faces:
                arrows = self.createPreviewArrows(face)
                self.preview_objects.extend(arrows)
                arrow_count += len(arrows)
            
            # Update statistics
            self.num_arrows_label.setText(str(arrow_count))
            self.updatePreviewStatistics()
            
            # Refresh 3D view
            Gui.updateGui()
            
            self.updateStatus(f"Preview updated with {arrow_count} arrows")
            
        except Exception as e:
            self.updateStatus(f"Preview error: {str(e)}", "red")
    
    def createPreviewArrows(self, face):
        """Create preview arrows for a face."""
        arrows = []
        
        if not hasattr(face, 'Shape'):
            return arrows
        
        try:
            # Get face geometry
            shape = face.Shape
            if hasattr(shape, 'Faces'):
                faces_to_process = shape.Faces
            else:
                faces_to_process = [shape] if hasattr(shape, 'Area') else []
            
            density = self.load_settings['arrow_density']
            scale = self.load_settings['arrow_scale']
            
            for f in faces_to_process:
                # Create grid of arrows
                u_params = np.linspace(0.1, 0.9, density)
                v_params = np.linspace(0.1, 0.9, density)
                
                for u in u_params:
                    for v in v_params:
                        try:
                            point = f.valueAt(u, v)
                            arrow = self.createSingleArrow(point, f, scale)
                            if arrow:
                                arrows.append(arrow)
                        except:
                            continue
                            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating preview arrows: {e}\n")
        
        return arrows
    
    def createSingleArrow(self, point, face, scale):
        """Create a single preview arrow."""
        try:
            # Get load direction
            direction = self.getLoadDirection(face, point)
            
            # Get load magnitude
            magnitude = self.magnitude_input.value()
            
            # Calculate arrow geometry
            arrow_length = magnitude * scale * 10  # Scale factor
            if arrow_length < 5:
                arrow_length = 5
            
            end_point = point + (direction * arrow_length)
            
            # Create arrow (simplified - in practice would create proper arrow geometry)
            doc = App.ActiveDocument
            arrow_obj = doc.addObject("Part::Feature", "LoadArrow")
            
            # Create line for arrow shaft - import Part module
            try:
                import Part
                arrow_line = Part.makeLine(point, end_point)
                arrow_obj.Shape = arrow_line
            except ImportError:
                # Fallback for testing without Part module
                pass
            
            # Set visual properties
            if App.GuiUp:
                arrow_obj.ViewObject.LineColor = (1.0, 0.0, 0.0)  # Red
                arrow_obj.ViewObject.LineWidth = 2
            
            return arrow_obj
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating arrow: {e}\n")
            return None
    
    def getLoadDirection(self, face, point):
        """Get load direction vector at a point."""
        direction_type = self.direction_combo.currentText()
        
        if direction_type == "Normal to Surface":
            try:
                # Get surface normal at point
                normal = face.normalAt(0.5, 0.5)  # Simplified
                return normal.normalize()
            except:
                return App.Vector(0, 0, -1)
        elif direction_type == "+X Global":
            return App.Vector(1, 0, 0)
        elif direction_type == "-X Global":
            return App.Vector(-1, 0, 0)
        elif direction_type == "+Y Global":
            return App.Vector(0, 1, 0)
        elif direction_type == "-Y Global":
            return App.Vector(0, -1, 0)
        elif direction_type == "+Z Global":
            return App.Vector(0, 0, 1)
        elif direction_type == "-Z Global":
            return App.Vector(0, 0, -1)
        elif direction_type == "Custom":
            x = self.custom_x.value()
            y = self.custom_y.value()
            z = self.custom_z.value()
            return App.Vector(x, y, z).normalize()
        
        return App.Vector(0, 0, -1)
    
    def clearPreview(self):
        """Clear preview objects."""
        doc = App.ActiveDocument
        if doc:
            for obj in self.preview_objects:
                try:
                    if hasattr(obj, 'Name') and doc.getObject(obj.Name):
                        doc.removeObject(obj.Name)
                except:
                    pass
        
        self.preview_objects.clear()
        self.num_arrows_label.setText("0")
    
    def updatePreviewStatistics(self):
        """Update preview statistics display."""
        try:
            # Calculate total force and resultant
            magnitude = self.magnitude_input.value()
            unit = self.magnitude_unit_combo.currentText()
            magnitude_kn_m2 = self.convertToKnM2(magnitude, unit)
            
            total_area_text = self.total_area_label.text()
            if total_area_text != "0 m²":
                total_area = float(total_area_text.split()[0])
                total_force = magnitude_kn_m2 * total_area
            else:
                total_force = 0.0
            
            self.total_force_label.setText(f"{total_force:.2f} kN")
            
            # Calculate resultant direction
            direction = self.getLoadDirection(None, App.Vector(0, 0, 0))
            resultant = direction * total_force
            
            self.resultant_label.setText(f"({resultant.x:.1f}, {resultant.y:.1f}, {resultant.z:.1f})")
            
            # Calculate approximate load center (simplified)
            if self.selected_faces:
                center = App.Vector(0, 0, 0)
                count = 0
                for face in self.selected_faces:
                    if hasattr(face, 'Shape') and hasattr(face.Shape, 'CenterOfMass'):
                        center += face.Shape.CenterOfMass
                        count += 1
                
                if count > 0:
                    center = center * (1.0 / count)
                    self.load_center_label.setText(f"({center.x:.1f}, {center.y:.1f}, {center.z:.1f})")
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating statistics: {e}\n")
    
    def updateStatus(self, message, color="blue"):
        """Update status message."""
        self.status_label.setText(message)
        _safe_call_method(self.status_label, "setStyleSheet", f"color: {color}; font-style: italic; margin-top: 5px;")
    
    def accept(self):
        """Accept and create area load object."""
        if not self.selected_faces:
            QtWidgets.QMessageBox.warning(None, "Warning", "No faces selected for load application")
            return False
        
        try:
            # Create area load object
            from ..objects.AreaLoad import makeAreaLoad
            
            magnitude_text = f"{self.magnitude_input.value()} {self.magnitude_unit_combo.currentText()}"
            load_type = self.load_type_combo.currentText()
            
            area_load = makeAreaLoad(
                target_faces=self.selected_faces,
                magnitude=magnitude_text,
                load_type=load_type
            )
            
            if area_load:
                # Set additional properties
                area_load.LoadCaseName = self.load_case_input.text()
                area_load.LoadFactor = self.load_factor_input.value()
                area_load.Description = self.description_input.text()
                area_load.Direction = self.direction_combo.currentText()
                
                # Apply load distribution settings
                if hasattr(self, 'load_distribution_combo'):
                    # Set load distribution method
                    if hasattr(area_load, 'LoadDistribution'):
                        area_load.LoadDistribution = self.load_distribution_combo.currentText()
                    
                    # Set OneWay direction if applicable
                    if (hasattr(area_load, 'OneWayDirection') and hasattr(self, 'oneway_direction_combo')):
                        area_load.OneWayDirection = self.oneway_direction_combo.currentText()
                    
                    # Set custom direction if applicable
                    if (hasattr(area_load, 'CustomDistributionDirection') and 
                        hasattr(self, 'custom_x_input') and 
                        hasattr(self, 'oneway_direction_combo') and
                        self.oneway_direction_combo.currentText() == "Custom"):
                        custom_dir = App.Vector(
                            self.custom_x_input.value(),
                            self.custom_y_input.value(), 
                            self.custom_z_input.value()
                        )
                        area_load.CustomDistributionDirection = custom_dir
                    
                    # Set distribution factors
                    if hasattr(area_load, 'EdgeDistributionFactors') and hasattr(self, 'distribution_factors_input'):
                        try:
                            factors_text = self.distribution_factors_input.text()
                            factors = [float(f.strip()) for f in factors_text.split(',')]
                            area_load.EdgeDistributionFactors = factors
                        except:
                            # Use default factors if parsing fails
                            area_load.EdgeDistributionFactors = [1.0, 1.0, 1.0, 1.0]
                
                if self.direction_combo.currentText() == "Custom":
                    area_load.CustomDirection = App.Vector(
                        self.custom_x.value(),
                        self.custom_y.value(), 
                        self.custom_z.value()
                    )
                
                area_load.Distribution = self.distribution_combo.currentText()
                
                # Store distribution parameters
                self.setDistributionParameters(area_load)
                
                # Set visualization properties
                area_load.ShowLoadArrows = self.show_preview_check.isChecked()
                area_load.ArrowScale = self.arrow_scale_spin.value()
                area_load.ArrowDensity = self.arrow_density_spin.value()
                
                area_load.recompute()
                App.ActiveDocument.recompute()
                
                self.clearPreview()
                self.updateStatus(f"Area load {area_load.Label} created successfully", "green")
                return True
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to create area load: {str(e)}")
            return False
    
    def setDistributionParameters(self, area_load):
        """Set distribution parameters on area load object."""
        distribution = self.distribution_combo.currentText()
        
        if distribution == "Uniform":
            area_load.DistributionParameters = [1.0]
        elif distribution in ["Linear X", "Linear Y"]:
            area_load.DistributionParameters = [
                self.min_factor_spin.value(),
                self.max_factor_spin.value()
            ]
        elif distribution == "Bilinear":
            area_load.DistributionParameters = [factor.value() for factor in self.corner_factors]
        elif distribution == "Parabolic":
            area_load.DistributionParameters = [
                self.vertex_factor_spin.value(),
                self.edge_factor_spin.value()
            ]
        elif distribution == "Point Load":
            area_load.DistributionParameters = [
                self.point_u.value(),
                self.point_v.value()
            ]
        elif distribution == "User Defined":
            area_load.DistributionFunction = self.custom_function_input.toPlainText()
    
    def reject(self):
        """Reject and close panel."""
        self.clearPreview()
        return True
    
    def getStandardButtons(self):
        """Return standard dialog buttons."""
        return QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel


class AreaLoadPanel:
    """
    Task panel wrapper for area load application.
    
    This class provides the interface between FreeCAD's task panel system
    and the AreaLoadApplicationPanel implementation.
    """
    
    def __init__(self, area_load_object=None):
        """
        Initialize the area load panel.
        
        Args:
            area_load_object: Existing AreaLoad object to edit, or None to create new
        """
        self.area_load_object = area_load_object
        
        if area_load_object:
            # Edit existing area load
            self.panel = AreaLoadEditPanel(area_load_object)
        else:
            # Create new area load from selection
            selected_faces = self.get_selected_faces_from_gui()
            self.panel = AreaLoadApplicationPanel(selected_faces)
        
        self.form = self.panel.form
    
    def get_selected_faces_from_gui(self):
        """Get selected faces from FreeCAD GUI."""
        selected_faces = []
        
        try:
            sel_objects = Gui.Selection.getSelectionEx()
            for sel_obj in sel_objects:
                if sel_obj.SubElementNames:
                    # Sub-elements selected (faces)
                    for sub_name in sel_obj.SubElementNames:
                        if 'Face' in sub_name:
                            selected_faces.append(sel_obj.Object)
                else:
                    # Whole object selected
                    obj = sel_obj.Object
                    if hasattr(obj, 'Shape'):
                        selected_faces.append(obj)
        except Exception as e:
            App.Console.PrintWarning(f"Warning getting selected faces: {str(e)}\n")
        
        # Remove duplicates while preserving order
        unique_faces = []
        for face in selected_faces:
            if face not in unique_faces:
                unique_faces.append(face)
        
        return unique_faces
    
    def accept(self):
        """Accept the panel and create/update area load."""
        return self.panel.accept()
    
    def reject(self):
        """Reject the panel and clean up."""
        return self.panel.reject()
    
    def getStandardButtons(self):
        """Return standard dialog buttons."""
        return self.panel.getStandardButtons()


class AreaLoadEditPanel:
    """
    Panel for editing existing area load objects.
    
    This provides a simplified interface for modifying existing area loads
    without recreating the load visualization.
    """
    
    def __init__(self, area_load_object):
        """
        Initialize edit panel for existing area load.
        
        Args:
            area_load_object: Existing AreaLoad object to edit
        """
        self.area_load_object = area_load_object
        self.form = self.createUI()
        self.populateFromObject()
    
    def createUI(self):
        """Create simplified UI for editing existing area load."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Title
        title_label = QtWidgets.QLabel(f"Edit Area Load: {self.area_load_object.Label}")
        _safe_call_method(title_label, 'setStyleSheet', "font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        _safe_add_widget(layout, title_label)
        
        # Basic properties group
        props_group = QtWidgets.QGroupBox("Load Properties")
        props_layout = QtWidgets.QFormLayout()
        
        # Magnitude
        self.magnitude_input = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.magnitude_input, "setRange", -1000.0, 1000.0)
        self.magnitude_input.setDecimals(3)
        _safe_call_method(self.magnitude_input, "setSuffix", " kN/m²")
        props_layout.addRow("Magnitude:", self.magnitude_input)
        
        # Load type
        self.load_type_combo = QtWidgets.QComboBox()
        load_types = [
            "Dead Load (DL)", "Live Load (LL)", "Live Load Roof (LL_Roof)",
            "Wind Load (W)", "Earthquake (E)", "Earth Pressure (H)",
            "Fluid Pressure (F)", "Thermal (T)", "Custom Pressure"
        ]
        _safe_call_method(self.load_type_combo, "addItems", load_types)
        props_layout.addRow("Load Type:", self.load_type_combo)
        
        # Direction
        self.direction_combo = QtWidgets.QComboBox()
        directions = ["Normal to Surface", "+X Global", "-X Global", 
                     "+Y Global", "-Y Global", "+Z Global", "-Z Global", "Custom"]
        _safe_call_method(self.direction_combo, "addItems", directions)
        props_layout.addRow("Direction:", self.direction_combo)
        
        # Load case
        self.load_case_input = QtWidgets.QLineEdit()
        props_layout.addRow("Load Case:", self.load_case_input)
        
        # Load factor
        self.load_factor_input = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.load_factor_input, "setRange", 0.0, 10.0)
        self.load_factor_input.setDecimals(2)
        _safe_call_method(self.load_factor_input, "setValue", 1.0)
        props_layout.addRow("Load Factor:", self.load_factor_input)
        
        # Description
        self.description_input = QtWidgets.QLineEdit()
        self.description_input.setPlaceholderText("Optional description")
        props_layout.addRow("Description:", self.description_input)
        
        _safe_set_layout(props_group, props_layout)
        _safe_add_widget(layout, props_group)
        
        # Visualization group
        viz_group = QtWidgets.QGroupBox("Visualization")
        viz_layout = QtWidgets.QFormLayout()
        
        self.show_arrows_check = QtWidgets.QCheckBox()
        _safe_call_method(self.show_arrows_check, "setChecked", True)
        viz_layout.addRow("Show Load Arrows:", self.show_arrows_check)
        
        self.arrow_scale_spin = QtWidgets.QDoubleSpinBox()
        _safe_call_method(self.arrow_scale_spin, "setRange", 0.1, 10.0)
        _safe_call_method(self.arrow_scale_spin, "setValue", 1.0)
        self.arrow_scale_spin.setDecimals(2)
        viz_layout.addRow("Arrow Scale:", self.arrow_scale_spin)
        
        self.arrow_density_spin = QtWidgets.QSpinBox()
        _safe_call_method(self.arrow_density_spin, "setRange", 2, 20)
        _safe_call_method(self.arrow_density_spin, "setValue", 5)
        viz_layout.addRow("Arrow Density:", self.arrow_density_spin)
        
        _safe_set_layout(viz_group, viz_layout)
        _safe_add_widget(layout, viz_group)
        
        # Target surfaces info (read-only)
        surfaces_group = QtWidgets.QGroupBox("Target Surfaces (Read-Only)")
        surfaces_layout = QtWidgets.QVBoxLayout()
        
        self.surfaces_list = QtWidgets.QListWidget()
        _safe_call_method(self.surfaces_list, "setMaximumHeight", 100)
        _safe_call_method(self.surfaces_list, "setSelectionMode", QtWidgets.QAbstractItemView.NoSelection)
        _safe_add_widget(surfaces_layout, self.surfaces_list)
        
        note_label = QtWidgets.QLabel("Note: To change target surfaces, delete this load and create a new one.")
        _safe_call_method(note_label, "setStyleSheet", "color: gray; font-style: italic;")
        _safe_add_widget(surfaces_layout, note_label)
        
        _safe_set_layout(surfaces_group, surfaces_layout)
        _safe_add_widget(layout, surfaces_group)
        
        _safe_set_layout(widget, layout)
        return widget
    
    def populateFromObject(self):
        """Populate UI from existing area load object."""
        try:
            obj = self.area_load_object
            
            # Basic properties
            if hasattr(obj, 'Magnitude'):
                magnitude_str = str(obj.Magnitude)
                # Extract numeric value
                try:
                    magnitude_val = float(magnitude_str.split()[0])
                    _safe_call_method(self.magnitude_input, "setValue", magnitude_val)
                except:
                    _safe_call_method(self.magnitude_input, "setValue", 5.0)
            
            if hasattr(obj, 'LoadType'):
                load_type = str(obj.LoadType)
                for i in range(self.load_type_combo.count()):
                    if load_type in self.load_type_combo.itemText(i):
                        self.load_type_combo.setCurrentIndex(i)
                        break
            
            if hasattr(obj, 'Direction'):
                direction = str(obj.Direction)
                for i in range(self.direction_combo.count()):
                    if direction == self.direction_combo.itemText(i):
                        self.direction_combo.setCurrentIndex(i)
                        break
            
            if hasattr(obj, 'LoadCaseName'):
                self.load_case_input.setText(str(obj.LoadCaseName))
            
            if hasattr(obj, 'LoadFactor'):
                _safe_call_method(self.load_factor_input, "setValue", float(obj.LoadFactor))
            
            if hasattr(obj, 'Description'):
                self.description_input.setText(str(obj.Description))
            
            # Visualization
            if hasattr(obj, 'ShowLoadArrows'):
                _safe_call_method(self.show_arrows_check, "setChecked", bool(obj.ShowLoadArrows))
            
            if hasattr(obj, 'ArrowScale'):
                _safe_call_method(self.arrow_scale_spin, "setValue", float(obj.ArrowScale))
            
            if hasattr(obj, 'ArrowDensity'):
                _safe_call_method(self.arrow_density_spin, "setValue", int(obj.ArrowDensity))
            
            # Target surfaces
            if hasattr(obj, 'TargetFaces'):
                for target in obj.TargetFaces:
                    if hasattr(target, 'Label'):
                        _safe_call_method(self.surfaces_list, "addItem", target.Label)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error populating from object: {e}\n")
    
    def accept(self):
        """Accept changes and update the area load object."""
        try:
            obj = self.area_load_object
            
            # Update properties
            if hasattr(obj, 'Magnitude'):
                magnitude_val = self.magnitude_input.value()
                obj.Magnitude = f"{magnitude_val} kN/m²"
            
            if hasattr(obj, 'LoadType'):
                obj.LoadType = self.load_type_combo.currentText()
            
            if hasattr(obj, 'Direction'):
                obj.Direction = self.direction_combo.currentText()
            
            if hasattr(obj, 'LoadCaseName'):
                obj.LoadCaseName = self.load_case_input.text()
            
            if hasattr(obj, 'LoadFactor'):
                obj.LoadFactor = self.load_factor_input.value()
            
            if hasattr(obj, 'Description'):
                obj.Description = self.description_input.text()
            
            # Visualization
            if hasattr(obj, 'ShowLoadArrows'):
                obj.ShowLoadArrows = self.show_arrows_check.isChecked()
            
            if hasattr(obj, 'ArrowScale'):
                obj.ArrowScale = self.arrow_scale_spin.value()
            
            if hasattr(obj, 'ArrowDensity'):
                obj.ArrowDensity = self.arrow_density_spin.value()
            
            # Recompute object
            obj.recompute()
            App.ActiveDocument.recompute()
            
            App.Console.PrintMessage(f"Area load {obj.Label} updated successfully.\n")
            return True
            
        except Exception as e:
            App.Console.PrintError(f"Error updating area load: {str(e)}\n")
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to update area load: {str(e)}")
            return False
    
    def reject(self):
        """Reject changes and close panel."""
        return True
    
    def getStandardButtons(self):
        """Return standard dialog buttons."""
        return QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel