import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtWidgets, QtGui
import math
import numpy as np
import os


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
        title_label.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 5px;")
        layout.addWidget(title_label)
        
        instruction_label = QtWidgets.QLabel("Select surfaces and define load properties below:")
        instruction_label.setStyleSheet("color: gray; font-style: italic; margin-bottom: 10px;")
        layout.addWidget(instruction_label)
        
        # Create tabbed interface
        self.tab_widget = QtWidgets.QTabWidget()
        
        # Target surfaces tab
        self.surfaces_tab = self.createSurfacesTab()
        self.tab_widget.addTab(self.surfaces_tab, "Target Surfaces")
        
        # Load definition tab
        self.load_tab = self.createLoadDefinitionTab()
        self.tab_widget.addTab(self.load_tab, "Load Definition")
        
        # Distribution tab
        self.distribution_tab = self.createDistributionTab()
        self.tab_widget.addTab(self.distribution_tab, "Distribution")
        
        # Preview tab
        self.preview_tab = self.createPreviewTab()
        self.tab_widget.addTab(self.preview_tab, "Preview & Settings")
        
        layout.addWidget(self.tab_widget)
        
        # Load summary
        summary_group = self.createLoadSummary()
        layout.addWidget(summary_group)
        
        # Status bar
        self.status_label = QtWidgets.QLabel("Ready - Select surfaces to apply loads")
        self.status_label.setStyleSheet("color: blue; font-style: italic; margin-top: 5px;")
        layout.addWidget(self.status_label)
        
        widget.setLayout(layout)
        return widget
    
    def createSurfacesTab(self):
        """Create surfaces selection tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Selected faces display
        selection_group = QtWidgets.QGroupBox("Selected Surfaces")
        selection_layout = QtWidgets.QVBoxLayout()
        
        self.face_list = QtWidgets.QListWidget()
        self.face_list.setMaximumHeight(120)
        self.face_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        selection_layout.addWidget(self.face_list)
        
        # Face selection buttons
        face_button_layout = QtWidgets.QGridLayout()
        
        self.add_faces_btn = QtWidgets.QPushButton("Add Faces")
        self.add_faces_btn.setToolTip("Select additional faces in 3D view")
        self.add_faces_btn.clicked.connect(self.addFaces)
        
        self.add_from_selection_btn = QtWidgets.QPushButton("Add from Selection")
        self.add_from_selection_btn.setToolTip("Add currently selected faces")
        self.add_from_selection_btn.clicked.connect(self.addFromSelection)
        
        self.remove_faces_btn = QtWidgets.QPushButton("Remove Selected")
        self.remove_faces_btn.clicked.connect(self.removeSelectedFaces)
        
        self.clear_all_btn = QtWidgets.QPushButton("Clear All")
        self.clear_all_btn.clicked.connect(self.clearAllFaces)
        
        face_button_layout.addWidget(self.add_faces_btn, 0, 0)
        face_button_layout.addWidget(self.add_from_selection_btn, 0, 1)
        face_button_layout.addWidget(self.remove_faces_btn, 1, 0)
        face_button_layout.addWidget(self.clear_all_btn, 1, 1)
        
        selection_layout.addLayout(face_button_layout)
        selection_group.setLayout(selection_layout)
        layout.addWidget(selection_group)
        
        # Surface properties (read-only)
        properties_group = QtWidgets.QGroupBox("Surface Properties")
        properties_layout = QtWidgets.QFormLayout()
        
        self.total_area_label = QtWidgets.QLabel("0 m²")
        self.num_faces_label = QtWidgets.QLabel("0")
        self.area_range_label = QtWidgets.QLabel("N/A")
        
        properties_layout.addRow("Total Area:", self.total_area_label)
        properties_layout.addRow("Number of Faces:", self.num_faces_label)
        properties_layout.addRow("Area Range:", self.area_range_label)
        
        properties_group.setLayout(properties_layout)
        layout.addWidget(properties_group)
        
        # Selection filters
        filter_group = QtWidgets.QGroupBox("Selection Filters")
        filter_layout = QtWidgets.QFormLayout()
        
        self.face_type_filter = QtWidgets.QComboBox()
        self.face_type_filter.addItems(["All Types", "Planar", "Cylindrical", "Spherical", "Other"])
        self.face_type_filter.currentTextChanged.connect(self.applySelectionFilter)
        
        self.min_area_filter = QtWidgets.QDoubleSpinBox()
        self.min_area_filter.setRange(0.0, 1000000.0)
        self.min_area_filter.setValue(0.0)
        self.min_area_filter.setSuffix(" m²")
        self.min_area_filter.valueChanged.connect(self.applySelectionFilter)
        
        filter_layout.addRow("Face Type:", self.face_type_filter)
        filter_layout.addRow("Min Area:", self.min_area_filter)
        filter_group.setLayout(filter_layout)
        layout.addWidget(filter_group)
        
        tab.setLayout(layout)
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
        self.load_type_combo.addItems(load_types)
        self.load_type_combo.currentTextChanged.connect(self.onLoadTypeChanged)
        type_layout.addRow("Load Type:", self.load_type_combo)
        
        self.load_category_combo = QtWidgets.QComboBox()
        self.load_category_combo.addItems(["DL", "LL", "LL_Roof", "W", "E", "H", "F", "T", "CUSTOM"])
        type_layout.addRow("Category:", self.load_category_combo)
        
        type_group.setLayout(type_layout)
        layout.addWidget(type_group)
        
        # Load magnitude
        magnitude_group = QtWidgets.QGroupBox("Load Magnitude")
        magnitude_layout = QtWidgets.QFormLayout()
        
        self.magnitude_input = QtWidgets.QDoubleSpinBox()
        self.magnitude_input.setRange(-1000.0, 1000.0)
        self.magnitude_input.setValue(5.0)
        self.magnitude_input.setDecimals(3)
        self.magnitude_input.setSuffix(" kN/m²")
        self.magnitude_input.valueChanged.connect(self.onMagnitudeChanged)
        magnitude_layout.addRow("Magnitude:", self.magnitude_input)
        
        self.magnitude_unit_combo = QtWidgets.QComboBox()
        self.magnitude_unit_combo.addItems(["kN/m²", "N/m²", "kPa", "MPa", "psf", "psi"])
        self.magnitude_unit_combo.currentTextChanged.connect(self.onUnitChanged)
        magnitude_layout.addRow("Unit:", self.magnitude_unit_combo)
        
        magnitude_group.setLayout(magnitude_layout)
        layout.addWidget(magnitude_group)
        
        # Load direction
        direction_group = QtWidgets.QGroupBox("Load Direction")
        direction_layout = QtWidgets.QFormLayout()
        
        self.direction_combo = QtWidgets.QComboBox()
        directions = ["Normal to Surface", "+X Global", "-X Global", 
                     "+Y Global", "-Y Global", "+Z Global", "-Z Global", "Custom"]
        self.direction_combo.addItems(directions)
        self.direction_combo.currentTextChanged.connect(self.onDirectionChanged)
        direction_layout.addRow("Direction:", self.direction_combo)
        
        # Custom direction input
        custom_layout = QtWidgets.QHBoxLayout()
        self.custom_x = QtWidgets.QDoubleSpinBox()
        self.custom_x.setRange(-1.0, 1.0)
        self.custom_x.setDecimals(3)
        self.custom_x.setValue(0.0)
        
        self.custom_y = QtWidgets.QDoubleSpinBox()
        self.custom_y.setRange(-1.0, 1.0)
        self.custom_y.setDecimals(3)
        self.custom_y.setValue(0.0)
        
        self.custom_z = QtWidgets.QDoubleSpinBox()
        self.custom_z.setRange(-1.0, 1.0)
        self.custom_z.setDecimals(3)
        self.custom_z.setValue(-1.0)
        
        custom_layout.addWidget(QtWidgets.QLabel("X:"))
        custom_layout.addWidget(self.custom_x)
        custom_layout.addWidget(QtWidgets.QLabel("Y:"))
        custom_layout.addWidget(self.custom_y)
        custom_layout.addWidget(QtWidgets.QLabel("Z:"))
        custom_layout.addWidget(self.custom_z)
        
        self.normalize_btn = QtWidgets.QPushButton("Normalize")
        self.normalize_btn.clicked.connect(self.normalizeCustomDirection)
        custom_layout.addWidget(self.normalize_btn)
        
        direction_layout.addRow("Custom Vector:", custom_layout)
        direction_group.setLayout(direction_layout)
        layout.addWidget(direction_group)
        
        # Load case information
        case_group = QtWidgets.QGroupBox("Load Case Information")
        case_layout = QtWidgets.QFormLayout()
        
        self.load_case_input = QtWidgets.QLineEdit()
        self.load_case_input.setText("DL1")
        self.load_case_input.textChanged.connect(self.onLoadCaseChanged)
        case_layout.addRow("Load Case Name:", self.load_case_input)
        
        self.load_factor_input = QtWidgets.QDoubleSpinBox()
        self.load_factor_input.setRange(0.0, 10.0)
        self.load_factor_input.setValue(1.0)
        self.load_factor_input.setDecimals(2)
        case_layout.addRow("Load Factor:", self.load_factor_input)
        
        self.description_input = QtWidgets.QLineEdit()
        self.description_input.setPlaceholderText("Optional load description")
        case_layout.addRow("Description:", self.description_input)
        
        case_group.setLayout(case_layout)
        layout.addWidget(case_group)
        
        tab.setLayout(layout)
        return tab
    
    def createDistributionTab(self):
        """Create load distribution tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Distribution pattern
        pattern_group = QtWidgets.QGroupBox("Distribution Pattern")
        pattern_layout = QtWidgets.QFormLayout()
        
        self.distribution_combo = QtWidgets.QComboBox()
        distributions = ["Uniform", "Linear X", "Linear Y", "Bilinear", "Parabolic", "Point Load", "User Defined"]
        self.distribution_combo.addItems(distributions)
        self.distribution_combo.currentTextChanged.connect(self.onDistributionChanged)
        pattern_layout.addRow("Pattern:", self.distribution_combo)
        
        pattern_group.setLayout(pattern_layout)
        layout.addWidget(pattern_group)
        
        # Distribution parameters (varies by pattern)
        self.params_group = QtWidgets.QGroupBox("Distribution Parameters")
        self.params_layout = QtWidgets.QFormLayout()
        self.params_group.setLayout(self.params_layout)
        layout.addWidget(self.params_group)
        
        # Spatial variation
        spatial_group = QtWidgets.QGroupBox("Spatial Variation")
        spatial_layout = QtWidgets.QFormLayout()
        
        # Variation center
        center_layout = QtWidgets.QHBoxLayout()
        self.center_x = QtWidgets.QDoubleSpinBox()
        self.center_x.setRange(-10000.0, 10000.0)
        self.center_x.setValue(0.0)
        self.center_x.setSuffix(" mm")
        
        self.center_y = QtWidgets.QDoubleSpinBox()
        self.center_y.setRange(-10000.0, 10000.0)
        self.center_y.setValue(0.0)
        self.center_y.setSuffix(" mm")
        
        self.center_z = QtWidgets.QDoubleSpinBox()
        self.center_z.setRange(-10000.0, 10000.0)
        self.center_z.setValue(0.0)
        self.center_z.setSuffix(" mm")
        
        self.pick_center_btn = QtWidgets.QPushButton("Pick")
        self.pick_center_btn.setToolTip("Pick center point from 3D view")
        self.pick_center_btn.clicked.connect(self.pickVariationCenter)
        
        center_layout.addWidget(self.center_x)
        center_layout.addWidget(self.center_y)
        center_layout.addWidget(self.center_z)
        center_layout.addWidget(self.pick_center_btn)
        spatial_layout.addRow("Variation Center:", center_layout)
        
        self.variation_radius = QtWidgets.QDoubleSpinBox()
        self.variation_radius.setRange(1.0, 100000.0)
        self.variation_radius.setValue(1000.0)
        self.variation_radius.setSuffix(" mm")
        spatial_layout.addRow("Variation Radius:", self.variation_radius)
        
        spatial_group.setLayout(spatial_layout)
        layout.addWidget(spatial_group)
        
        # Custom function
        custom_group = QtWidgets.QGroupBox("Custom Distribution Function")
        custom_layout = QtWidgets.QVBoxLayout()
        
        function_label = QtWidgets.QLabel("Python expression (use x, y, z coordinates):")
        custom_layout.addWidget(function_label)
        
        self.custom_function_input = QtWidgets.QTextEdit()
        self.custom_function_input.setMaximumHeight(60)
        self.custom_function_input.setText("1.0")
        self.custom_function_input.setPlaceholderText("Example: 1.0 + 0.5*sin(x/1000)")
        custom_layout.addWidget(self.custom_function_input)
        
        function_buttons = QtWidgets.QHBoxLayout()
        self.validate_function_btn = QtWidgets.QPushButton("Validate Function")
        self.validate_function_btn.clicked.connect(self.validateCustomFunction)
        self.example_functions_btn = QtWidgets.QPushButton("Examples...")
        self.example_functions_btn.clicked.connect(self.showExampleFunctions)
        
        function_buttons.addWidget(self.validate_function_btn)
        function_buttons.addWidget(self.example_functions_btn)
        custom_layout.addLayout(function_buttons)
        
        custom_group.setLayout(custom_layout)
        layout.addWidget(custom_group)
        
        # Initialize distribution parameters
        self.updateDistributionParameters()
        
        tab.setLayout(layout)
        return tab
    
    def createPreviewTab(self):
        """Create preview and settings tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Preview controls
        preview_group = QtWidgets.QGroupBox("Preview Controls")
        preview_layout = QtWidgets.QFormLayout()
        
        self.show_preview_check = QtWidgets.QCheckBox("Show Load Preview")
        self.show_preview_check.setChecked(True)
        self.show_preview_check.toggled.connect(self.togglePreview)
        preview_layout.addRow(self.show_preview_check)
        
        self.arrow_scale_spin = QtWidgets.QDoubleSpinBox()
        self.arrow_scale_spin.setRange(0.1, 10.0)
        self.arrow_scale_spin.setValue(1.0)
        self.arrow_scale_spin.setDecimals(2)
        self.arrow_scale_spin.valueChanged.connect(self.updatePreviewSettings)
        preview_layout.addRow("Arrow Scale:", self.arrow_scale_spin)
        
        self.arrow_density_spin = QtWidgets.QSpinBox()
        self.arrow_density_spin.setRange(2, 20)
        self.arrow_density_spin.setValue(5)
        self.arrow_density_spin.valueChanged.connect(self.updatePreviewSettings)
        preview_layout.addRow("Arrow Density:", self.arrow_density_spin)
        
        self.auto_update_check = QtWidgets.QCheckBox("Auto Update Preview")
        self.auto_update_check.setChecked(True)
        self.auto_update_check.toggled.connect(self.toggleAutoUpdate)
        preview_layout.addRow(self.auto_update_check)
        
        preview_group.setLayout(preview_layout)
        layout.addWidget(preview_group)
        
        # Manual update button
        self.manual_update_btn = QtWidgets.QPushButton("Update Preview Now")
        self.manual_update_btn.clicked.connect(self.updatePreview)
        layout.addWidget(self.manual_update_btn)
        
        # Color settings
        color_group = QtWidgets.QGroupBox("Visualization Colors")
        color_layout = QtWidgets.QFormLayout()
        
        self.load_color_btn = QtWidgets.QPushButton()
        self.load_color_btn.setStyleSheet("background-color: red; min-height: 20px;")
        self.load_color_btn.clicked.connect(self.chooseLoadColor)
        color_layout.addRow("Load Color:", self.load_color_btn)
        
        self.arrow_transparency_spin = QtWidgets.QSpinBox()
        self.arrow_transparency_spin.setRange(0, 90)
        self.arrow_transparency_spin.setValue(20)
        self.arrow_transparency_spin.setSuffix("%")
        color_layout.addRow("Transparency:", self.arrow_transparency_spin)
        
        color_group.setLayout(color_layout)
        layout.addWidget(color_group)
        
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
        
        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)
        
        tab.setLayout(layout)
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
        
        summary_group.setLayout(summary_layout)
        return summary_group
    
    def populateSelectedFaces(self):
        """Populate the selected faces list."""
        self.face_list.clear()
        
        for i, face in enumerate(self.selected_faces):
            if hasattr(face, 'Label'):
                item_text = f"{face.Label} - Face {i+1}"
            else:
                item_text = f"Face {i+1}"
            
            self.face_list.addItem(item_text)
        
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
            self.min_factor_spin.setRange(0.0, 10.0)
            self.min_factor_spin.setValue(0.5)
            self.min_factor_spin.setDecimals(2)
            
            self.max_factor_spin = QtWidgets.QDoubleSpinBox()
            self.max_factor_spin.setRange(0.0, 10.0)
            self.max_factor_spin.setValue(1.5)
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
                factor_spin.setRange(0.0, 10.0)
                factor_spin.setValue(1.0)
                factor_spin.setDecimals(2)
                self.corner_factors.append(factor_spin)
                self.params_layout.addRow(f"Factor at {corner}:", factor_spin)
                
        elif distribution == "Parabolic":
            self.vertex_factor_spin = QtWidgets.QDoubleSpinBox()
            self.vertex_factor_spin.setRange(0.0, 10.0)
            self.vertex_factor_spin.setValue(2.0)
            self.vertex_factor_spin.setDecimals(2)
            
            self.edge_factor_spin = QtWidgets.QDoubleSpinBox()
            self.edge_factor_spin.setRange(0.0, 10.0)
            self.edge_factor_spin.setValue(0.5)
            self.edge_factor_spin.setDecimals(2)
            
            self.params_layout.addRow("Center Factor:", self.vertex_factor_spin)
            self.params_layout.addRow("Edge Factor:", self.edge_factor_spin)
            
        elif distribution == "Point Load":
            point_layout = QtWidgets.QHBoxLayout()
            
            self.point_u = QtWidgets.QDoubleSpinBox()
            self.point_u.setRange(0.0, 1.0)
            self.point_u.setValue(0.5)
            self.point_u.setDecimals(3)
            
            self.point_v = QtWidgets.QDoubleSpinBox()
            self.point_v.setRange(0.0, 1.0)
            self.point_v.setValue(0.5)
            self.point_v.setDecimals(3)
            
            point_layout.addWidget(QtWidgets.QLabel("U:"))
            point_layout.addWidget(self.point_u)
            point_layout.addWidget(QtWidgets.QLabel("V:"))
            point_layout.addWidget(self.point_v)
            
            self.params_layout.addRow("Point Location:", point_layout)
            
        elif distribution == "User Defined":
            note_label = QtWidgets.QLabel("Define custom function in 'Custom Distribution Function' section")
            note_label.setStyleSheet("color: blue; font-style: italic;")
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
            self.custom_x.setValue(x / length)
            self.custom_y.setValue(y / length)
            self.custom_z.setValue(z / length)
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
            self.load_color_btn.setStyleSheet(f"background-color: {color.name()}; min-height: 20px;")
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
            
            # Create line for arrow shaft
            arrow_line = Part.makeLine(point, end_point)
            arrow_obj.Shape = arrow_line
            
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
        self.status_label.setStyleSheet(f"color: {color}; font-style: italic; margin-top: 5px;")
    
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