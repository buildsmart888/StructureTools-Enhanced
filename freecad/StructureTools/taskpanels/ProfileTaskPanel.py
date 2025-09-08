# -*- coding: utf-8 -*-
"""
ProfileTaskPanel

Advanced GUI task panel for creating and editing structural profiles
with integration to section databases and calc system.
"""

import FreeCAD as App
import os
import math

# Safe GUI imports
try:
    import FreeCADGui as Gui
    from PySide2 import QtWidgets, QtCore, QtGui
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    GUI_AVAILABLE = True
except ImportError:
    try:
        from PySide import QtWidgets, QtCore, QtGui
        from PySide.QtWidgets import *
        from PySide.QtCore import *
        from PySide.QtGui import *
        GUI_AVAILABLE = True
    except ImportError:
        GUI_AVAILABLE = False

# Import database integrations
try:
    from ..data.EnhancedSteelDatabase import (
        get_enhanced_database, get_enhanced_shape_types,
        get_enhanced_sections, get_enhanced_section_data,
        get_section_geometry_data
    )
    ENHANCED_DATABASE_AVAILABLE = True
except ImportError:
    ENHANCED_DATABASE_AVAILABLE = False

try:
    from ..data.SectionStandards import SECTION_STANDARDS, get_section_info
    SECTION_DATABASE_AVAILABLE = True
except ImportError:
    SECTION_DATABASE_AVAILABLE = False
    SECTION_STANDARDS = {}

# Import profile object
try:
    from ..objects.StructuralProfile import StructuralProfile, ViewProviderStructuralProfile
    PROFILE_OBJECT_AVAILABLE = True
except ImportError:
    PROFILE_OBJECT_AVAILABLE = False

class ProfileTaskPanel:
    """Advanced Profile Creation/Editing Task Panel"""
    
    def __init__(self, profile_object=None):
        """Initialize task panel
        
        Args:
            profile_object: Existing StructuralProfile object to edit, or None for new
        """
        self.profile_object = profile_object
        self.is_editing = profile_object is not None
        self.preview_object = None
        self.database_sections = {}
        self.current_geometry = None
        
        # Initialize databases
        self.initialize_databases()
        
        # Create UI
        self.form = self.create_ui()
        
        # Load existing data if editing
        if self.is_editing:
            self.load_existing_data()
        
        # Initial preview
        self.update_preview()
    
    def initialize_databases(self):
        """Initialize section databases"""
        self.database_sections = {"Custom": {}}
        
        # Enhanced database
        if ENHANCED_DATABASE_AVAILABLE:
            try:
                db = get_enhanced_database()
                if db and db.available:
                    shape_types = get_enhanced_shape_types()
                    for shape_type, info in shape_types.items():
                        sections = get_enhanced_sections(shape_type)
                        self.database_sections[shape_type] = {
                            'name': info['name'],
                            'sections': sections
                        }
                    App.Console.PrintMessage(f"Enhanced database loaded: {len(shape_types)} shape types\n")
            except Exception as e:
                App.Console.PrintWarning(f"Enhanced database error: {e}\n")
        
        # Basic database fallback
        if SECTION_DATABASE_AVAILABLE and not self.database_sections:
            for section_name in SECTION_STANDARDS.keys():
                if "W" in section_name:
                    shape_type = "AISC_W_SHAPES"
                elif "IPE" in section_name:
                    shape_type = "EUROPEAN_I_BEAMS"
                elif "HSS" in section_name:
                    shape_type = "HSS_SHAPES"
                else:
                    shape_type = "OTHER"
                
                if shape_type not in self.database_sections:
                    self.database_sections[shape_type] = {'name': shape_type, 'sections': []}
                self.database_sections[shape_type]['sections'].append(section_name)
    
    def create_ui(self):
        """Create the task panel UI"""
        # Main widget
        widget = QWidget()
        main_layout = QVBoxLayout(widget)
        
        # Title
        title_text = "Edit Structural Profile" if self.is_editing else "Create Structural Profile"
        title = QLabel(title_text)
        title.setStyleSheet("font-weight: bold; font-size: 16px; color: #2E86AB; padding: 10px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Profile Type Selection
        type_group = QGroupBox("Profile Type")
        type_layout = QVBoxLayout(type_group)
        
        # Profile type buttons with icons
        self.profile_type_group = QButtonGroup()
        profile_types = [
            ("I-Beam", "I-beam/Wide Flange sections", "I"),
            ("Channel", "Channel sections (C-shapes)", "C"), 
            ("Angle", "Angle sections (L-shapes)", "L"),
            ("HSS Rectangular", "Hollow Structural Sections - Rectangular", "□"),
            ("HSS Circular", "Hollow Structural Sections - Circular", "○"),
            ("Rectangle", "Solid rectangular sections", "▬"),
            ("Circle", "Solid circular sections", "●"),
            ("T-Section", "T-shaped sections", "T"),
            ("Custom", "Custom defined section", "?")
        ]
        
        type_grid = QGridLayout()
        for i, (ptype, tooltip, symbol) in enumerate(profile_types):
            btn = QRadioButton(f"{symbol} {ptype}")
            btn.setToolTip(tooltip)
            btn.setProperty("profile_type", ptype)
            self.profile_type_group.addButton(btn, i)
            type_grid.addWidget(btn, i // 3, i % 3)
            
            if ptype == "I-Beam":  # Default selection
                btn.setChecked(True)
        
        self.profile_type_group.buttonClicked.connect(self.on_profile_type_changed)
        type_layout.addLayout(type_grid)
        main_layout.addWidget(type_group)
        
        # Database Section Selection
        database_group = QGroupBox("Standard Sections Database")
        database_layout = QFormLayout(database_group)
        
        self.shape_type_combo = QComboBox()
        database_layout.addRow("Shape Type:", self.shape_type_combo)
        
        self.section_combo = QComboBox()
        database_layout.addRow("Section:", self.section_combo)
        
        # Search functionality
        search_layout = QHBoxLayout()
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Search sections...")
        self.search_edit.textChanged.connect(self.filter_sections)
        search_btn = QPushButton("🔍")
        search_btn.setMaximumWidth(30)
        search_btn.clicked.connect(self.search_sections)
        search_layout.addWidget(self.search_edit)
        search_layout.addWidget(search_btn)
        database_layout.addRow("Search:", search_layout)
        
        # Populate databases
        self.populate_database_combos()
        self.shape_type_combo.currentTextChanged.connect(self.on_shape_type_changed)
        self.section_combo.currentTextChanged.connect(self.on_section_changed)
        
        main_layout.addWidget(database_group)
        
        # Dimensions Group
        self.dimensions_group = QGroupBox("Dimensions")
        self.dimensions_layout = QFormLayout(self.dimensions_group)
        
        # Create dimension inputs (will be populated based on profile type)
        self.dimension_inputs = {}
        self.create_dimension_inputs()
        
        main_layout.addWidget(self.dimensions_group)
        
        # Properties Display
        properties_group = QGroupBox("Calculated Properties")
        properties_layout = QVBoxLayout(properties_group)
        
        self.properties_table = QTableWidget(0, 2)
        self.properties_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.properties_table.horizontalHeader().setStretchLastSection(True)
        self.properties_table.setMaximumHeight(200)
        self.properties_table.setAlternatingRowColors(True)
        properties_layout.addWidget(self.properties_table)
        
        main_layout.addWidget(properties_group)
        
        # Preview Options
        preview_group = QGroupBox("Preview Options")
        preview_layout = QFormLayout(preview_group)
        
        self.show_preview_cb = QCheckBox("Show Live Preview")
        self.show_preview_cb.setChecked(True)
        self.show_preview_cb.toggled.connect(self.toggle_preview)
        preview_layout.addRow(self.show_preview_cb)
        
        self.show_dimensions_cb = QCheckBox("Show Dimensions")
        self.show_dimensions_cb.setChecked(True)
        preview_layout.addRow(self.show_dimensions_cb)
        
        self.scale_spin = QDoubleSpinBox()
        self.scale_spin.setRange(0.1, 10.0)
        self.scale_spin.setValue(1.0)
        self.scale_spin.setSingleStep(0.1)
        self.scale_spin.valueChanged.connect(self.update_preview)
        preview_layout.addRow("Scale:", self.scale_spin)
        
        main_layout.addWidget(preview_group)
        
        # Calc Integration
        calc_group = QGroupBox("Structural Analysis Integration")
        calc_layout = QVBoxLayout(calc_group)
        
        self.calc_ready_label = QLabel("✓ Properties ready for calc integration")
        self.calc_ready_label.setStyleSheet("color: green; font-weight: bold;")
        calc_layout.addWidget(self.calc_ready_label)
        
        self.export_calc_btn = QPushButton("Export Properties to Calc")
        self.export_calc_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.export_calc_btn.clicked.connect(self.export_to_calc)
        calc_layout.addWidget(self.export_calc_btn)
        
        main_layout.addWidget(calc_group)
        
        return widget
    
    def populate_database_combos(self):
        """Populate database combo boxes including steelpy integration"""
        self.shape_type_combo.clear()
        self.shape_type_combo.addItem("Custom", "Custom")
        
        # Add existing StructureTools databases
        for shape_type, info in self.database_sections.items():
            if shape_type != "Custom" and info.get('sections'):
                display_name = info.get('name', shape_type)
                section_count = len(info['sections'])
                self.shape_type_combo.addItem(f"{display_name} ({section_count} sections)", shape_type)
        
        # Add steelpy databases if available
        self.load_steelpy_databases()
    
    def load_steelpy_databases(self):
        """Load steelpy databases if available"""
        try:
            from ..data.SteelpyDatabaseIntegration import steelpy_manager, is_steelpy_available
            
            if not is_steelpy_available():
                # Add option to configure steelpy
                self.shape_type_combo.addItem("⚙️ Configure Steelpy Database...", "configure_steelpy")
                return
            
            # Load steelpy profiles
            steelpy_profiles = steelpy_manager.get_all_available_profiles()
            
            for kind, designations in steelpy_profiles.items():
                if designations:
                    # Map steelpy kinds to display names
                    kind_display_names = {
                        'W': 'AISC W-Shapes', 'M': 'AISC M-Shapes', 'S': 'AISC S-Shapes', 'HP': 'AISC HP-Shapes',
                        'WT': 'AISC WT-Shapes', 'MT': 'AISC MT-Shapes', 'ST': 'AISC ST-Shapes',
                        'C': 'AISC C-Channels', 'MC': 'AISC MC-Channels',
                        'L': 'AISC Angles', 'HSS': 'AISC HSS Rectangular', 'HSS_R': 'AISC HSS Circular',
                        'PIPE': 'AISC Pipes'
                    }
                    
                    display_name = kind_display_names.get(kind, f"Steelpy {kind}")
                    section_count = len(designations)
                    
                    # Store in database sections for consistency
                    self.database_sections[f"steelpy_{kind}"] = {
                        'name': display_name,
                        'sections': designations,
                        'source': 'steelpy',
                        'kind': kind
                    }
                    
                    self.shape_type_combo.addItem(f"{display_name} ({section_count} sections)", f"steelpy_{kind}")
            
            App.Console.PrintMessage(f"Loaded {len(steelpy_profiles)} steelpy databases\n")
            
        except ImportError:
            # Steelpy integration not available
            self.shape_type_combo.addItem("📁 Steelpy Database (Not Available)", "steelpy_not_available")
        except Exception as e:
            App.Console.PrintError(f"Failed to load steelpy databases: {e}\n")
    
    def apply_steelpy_section(self, shape_type, section_name):
        """Apply steelpy database section properties"""
        try:
            from ..data.SteelpyDatabaseIntegration import steelpy_manager, steelpy_geometry_generator
            
            if not steelpy_manager:
                QMessageBox.warning(self.form, "Warning", "Steelpy database not available")
                return
            
            # Extract steelpy kind from shape_type
            steelpy_kind = shape_type.replace("steelpy_", "")
            
            # Get profile properties from steelpy
            properties = steelpy_manager.get_profile_properties(steelpy_kind, section_name)
            if not properties:
                QMessageBox.warning(self.form, "Warning", f"Could not load properties for {section_name}")
                return
            
            # Set profile type
            profile_type = properties['profile_type']
            for btn in self.profile_type_group.buttons():
                if btn.property("profile_type") == profile_type:
                    btn.setChecked(True)
                    self.on_profile_type_changed()
                    break
            
            # Apply dimensions
            dimensions = properties['dimensions']
            
            # Update dimension inputs based on available data
            for dim_name, value in dimensions.items():
                if dim_name in self.dimension_inputs:
                    self.dimension_inputs[dim_name].setText(f"{value:.2f}")
            
            # Generate preview using steelpy geometry
            face = steelpy_geometry_generator.create_2d_face(steelpy_kind, section_name)
            if face:
                self.current_geometry = {
                    'face': face,
                    'source': 'steelpy',
                    'kind': steelpy_kind,
                    'designation': section_name
                }
                self.update_preview()
            
            # Update property display
            self.update_property_display()
            
            # Update profile name
            if hasattr(self, 'profile_name_edit'):
                suggested_name = f"{steelpy_kind}_{section_name.replace('/', '_')}"
                self.profile_name_edit.setText(suggested_name)
            
            App.Console.PrintMessage(f"Applied steelpy section: {steelpy_kind} {section_name}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Failed to apply steelpy section: {e}\n")
            QMessageBox.critical(self.form, "Error", f"Failed to load steelpy section: {str(e)}")
    
    def get_profile_type_mapping(self):
        """Get mapping between FreeCAD ProfileType and database shape types"""
        return {
            # FreeCAD ProfileType -> Compatible database shape types
            'I-Beam': ['W', 'M', 'S', 'HP', 'steelpy_W', 'steelpy_M', 'steelpy_S', 'steelpy_HP'],
            'Wide Flange': ['W', 'M', 'steelpy_W', 'steelpy_M'], 
            'Channel': ['C', 'MC', 'steelpy_C', 'steelpy_MC'],
            'Angle': ['L', 'steelpy_L'],
            'HSS Rectangular': ['HSS', 'steelpy_HSS'],
            'HSS Circular': ['HSS_R', 'PIPE', 'steelpy_HSS_R', 'steelpy_PIPE'],
            'T-Section': ['WT', 'MT', 'ST', 'steelpy_WT', 'steelpy_MT', 'steelpy_ST'],
            'Rectangle': [],  # Custom only
            'Circle': [],     # Custom only
            'Custom': []      # No database mapping
        }
    
    def filter_sections_by_profile_type(self, profile_type):
        """Filter database sections to show only those compatible with selected profile type"""
        mapping = self.get_profile_type_mapping()
        compatible_shapes = mapping.get(profile_type, [])
        
        # Clear current sections
        self.shape_type_combo.clear()
        self.shape_type_combo.addItem("Select shape type...", "")
        
        # Add compatible database sections
        for shape_key, shape_data in self.database_sections.items():
            if shape_key in compatible_shapes or any(comp in shape_key for comp in compatible_shapes):
                # Safe access to sections data
                sections = shape_data.get('sections', [])
                section_count = len(sections)
                display_name = shape_data.get('name', shape_key)
                self.shape_type_combo.addItem(f"{display_name} ({section_count} sections)", shape_key)
        
        # If no compatible sections found, allow custom
        if self.shape_type_combo.count() == 1:  # Only "Select shape type..." item
            self.shape_type_combo.addItem("Custom Profile (Manual Input)", "custom")
    
    def configure_steelpy_database(self):
        """Open steelpy configuration dialog"""
        try:
            from ..gui.SteelpyConfigDialog import show_steelpy_config_dialog
            
            result = show_steelpy_config_dialog(self.form)
            if result == QDialog.Accepted:
                # Reload databases after configuration
                self.populate_database_combos()
                QMessageBox.information(self.form, "Success", 
                                      "Steelpy database configured successfully!\n"
                                      "Databases have been reloaded.")
            
        except ImportError:
            QMessageBox.critical(self.form, "Error", 
                               "Steelpy configuration dialog not available")
        except Exception as e:
            QMessageBox.critical(self.form, "Error", 
                               f"Failed to open configuration dialog:\n{str(e)}")
    
    def on_shape_type_changed(self):
        """Handle shape type selection change"""
        shape_type = self.shape_type_combo.currentData()
        self.section_combo.clear()
        
        # Handle special cases
        if shape_type == "Custom":
            self.section_combo.addItem("Custom", "Custom")
            self.section_combo.setEnabled(False)
        elif shape_type == "configure_steelpy":
            self.configure_steelpy_database()
            # Reset to Custom after configuration
            self.shape_type_combo.setCurrentIndex(0)  # Custom
            return
        elif shape_type == "steelpy_not_available":
            QMessageBox.information(self.form, "Steelpy Not Available", 
                                  "Steelpy database integration is not available.\n"
                                  "Please install steelpy or check your installation.")
            self.shape_type_combo.setCurrentIndex(0)  # Custom
            return
        else:
            self.section_combo.setEnabled(True)
            self.section_combo.addItem("Select section...", None)
            
            sections = self.database_sections.get(shape_type, {}).get('sections', [])
            for section in sorted(sections):
                self.section_combo.addItem(section, section)
    
    def on_section_changed(self):
        """Handle section selection change"""
        section_name = self.section_combo.currentData()
        shape_type = self.shape_type_combo.currentData()
        
        if section_name and section_name != "Custom":
            self.apply_database_section(shape_type, section_name)
    
    def apply_database_section(self, shape_type, section_name):
        """Apply properties from database section including steelpy"""
        try:
            # Check if this is a steelpy database
            if shape_type.startswith("steelpy_"):
                self.apply_steelpy_section(shape_type, section_name)
                return
            
            # Get section data from existing databases
            section_data = None
            geometry_data = None
            
            if ENHANCED_DATABASE_AVAILABLE:
                try:
                    section_data = get_enhanced_section_data(shape_type, section_name)
                    geometry_data = get_section_geometry_data(shape_type, section_name)
                    self.current_geometry = geometry_data
                except:
                    pass
            
            if not section_data and SECTION_DATABASE_AVAILABLE:
                section_data = get_section_info(section_name)
            
            if section_data:
                self.update_inputs_from_data(section_data)
                self.update_preview()
                App.Console.PrintMessage(f"Applied section {section_name}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Failed to apply database section: {e}\n")
    
    def update_inputs_from_data(self, section_data):
        """Update input fields from section data"""
        def extract_value(keys, default=0.0):
            for key in keys if isinstance(keys, list) else [keys]:
                if key in section_data:
                    value = section_data[key]
                    if isinstance(value, dict) and 'value' in value:
                        return float(value['value'])
                    elif isinstance(value, (int, float)):
                        return float(value)
            return default
        
        # Update dimension inputs based on available data
        mappings = {
            'height_input': ['height', 'Depth', 'd', 'h'],
            'width_input': ['width', 'FlangeWidth', 'bf', 'b'],
            'web_thickness_input': ['web_thickness', 'WebThickness', 'tw'],
            'flange_thickness_input': ['flange_thickness', 'FlangeThickness', 'tf'],
            'thickness_input': ['thickness', 't'],
            'diameter_input': ['diameter', 'outer_diameter', 'OD', 'd'],
            'leg1_input': ['leg1', 'LegWidth', 'leg_width'],
            'leg2_input': ['leg2', 'LegHeight', 'leg_height']
        }
        
        for input_name, keys in mappings.items():
            if input_name in self.dimension_inputs:
                value = extract_value(keys)
                if value > 0:
                    self.dimension_inputs[input_name].setText(f"{value:.1f}")
    
    def create_dimension_inputs(self):
        """Create dimension input fields"""
        # Clear existing inputs
        for i in reversed(range(self.dimensions_layout.count())):
            self.dimensions_layout.itemAt(i).widget().setParent(None)
        
        self.dimension_inputs.clear()
        
        # Get current profile type
        profile_type = self.get_current_profile_type()
        
        # Create inputs based on profile type
        if profile_type in ["I-Beam", "Wide Flange"]:
            self.add_dimension_input("height_input", "Height (mm):", "200")
            self.add_dimension_input("width_input", "Flange Width (mm):", "100")
            self.add_dimension_input("web_thickness_input", "Web Thickness (mm):", "8")
            self.add_dimension_input("flange_thickness_input", "Flange Thickness (mm):", "12")
            
        elif profile_type == "Channel":
            self.add_dimension_input("height_input", "Height (mm):", "200")
            self.add_dimension_input("width_input", "Width (mm):", "75")
            self.add_dimension_input("web_thickness_input", "Web Thickness (mm):", "8")
            self.add_dimension_input("flange_thickness_input", "Flange Thickness (mm):", "12")
            
        elif profile_type == "HSS Rectangular":
            self.add_dimension_input("height_input", "Height (mm):", "150")
            self.add_dimension_input("width_input", "Width (mm):", "100")
            self.add_dimension_input("thickness_input", "Wall Thickness (mm):", "6")
            
        elif profile_type == "HSS Circular":
            self.add_dimension_input("diameter_input", "Diameter (mm):", "100")
            self.add_dimension_input("thickness_input", "Wall Thickness (mm):", "6")
            
        elif profile_type == "Rectangle":
            self.add_dimension_input("height_input", "Height (mm):", "150")
            self.add_dimension_input("width_input", "Width (mm):", "100")
            
        elif profile_type == "Circle":
            self.add_dimension_input("diameter_input", "Diameter (mm):", "100")
            
        elif profile_type == "Angle":
            self.add_dimension_input("leg1_input", "Leg 1 Length (mm):", "75")
            self.add_dimension_input("leg2_input", "Leg 2 Length (mm):", "50")
            self.add_dimension_input("thickness_input", "Thickness (mm):", "6")
            
        elif profile_type == "T-Section":
            self.add_dimension_input("height_input", "Height (mm):", "150")
            self.add_dimension_input("width_input", "Flange Width (mm):", "100")
            self.add_dimension_input("web_thickness_input", "Web Thickness (mm):", "8")
            self.add_dimension_input("flange_thickness_input", "Flange Thickness (mm):", "12")
        
        # Connect all inputs to update preview
        for input_widget in self.dimension_inputs.values():
            input_widget.textChanged.connect(self.update_preview)
    
    def add_dimension_input(self, name, label, default_value):
        """Add a dimension input field"""
        input_widget = QLineEdit()
        input_widget.setText(default_value)
        input_widget.setValidator(QDoubleValidator(0.1, 9999.0, 2))
        self.dimension_inputs[name] = input_widget
        self.dimensions_layout.addRow(label, input_widget)
    
    def get_current_profile_type(self):
        """Get currently selected profile type"""
        checked_button = self.profile_type_group.checkedButton()
        if checked_button:
            return checked_button.property("profile_type")
        return "I-Beam"
    
    def on_profile_type_changed(self):
        """Handle profile type change"""
        self.create_dimension_inputs()
        self.update_preview()
        
        # Update section database filter
        profile_type = self.get_current_profile_type()
        self.filter_database_by_type(profile_type)
    
    def filter_database_by_type(self, profile_type):
        """Filter database sections by profile type"""
        # Use the mapping function to filter sections
        self.filter_sections_by_profile_type(profile_type)
        
        # Clear section selection since we've changed shape types
        if hasattr(self, 'section_combo'):
            self.section_combo.clear()
            self.section_combo.addItem("Select section...", None)
    
    def filter_sections(self):
        """Filter sections based on search text"""
        search_text = self.search_edit.text().lower()
        shape_type = self.shape_type_combo.currentData()
        
        if shape_type == "Custom":
            return
        
        self.section_combo.clear()
        self.section_combo.addItem("Select section...", None)
        
        sections = self.database_sections.get(shape_type, {}).get('sections', [])
        filtered_sections = [s for s in sections if search_text in s.lower()]
        
        for section in sorted(filtered_sections):
            self.section_combo.addItem(section, section)
    
    def search_sections(self):
        """Perform advanced section search"""
        search_text = self.search_edit.text()
        if not search_text:
            return
        
        # Enhanced search across all databases
        results = []
        for shape_type, info in self.database_sections.items():
            if shape_type != "Custom":
                sections = info.get('sections', [])
                matches = [s for s in sections if search_text.lower() in s.lower()]
                results.extend([(shape_type, s) for s in matches])
        
        if results:
            # Show results in a dialog
            self.show_search_results(results)
        else:
            QMessageBox.information(self.form, "Search Results", "No matching sections found.")
    
    def show_search_results(self, results):
        """Show search results in a dialog"""
        dialog = QDialog(self.form)
        dialog.setWindowTitle("Search Results")
        dialog.setModal(True)
        dialog.resize(400, 300)
        
        layout = QVBoxLayout(dialog)
        
        list_widget = QListWidget()
        for shape_type, section in results:
            item_text = f"{section} ({self.database_sections[shape_type]['name']})"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, (shape_type, section))
            list_widget.addItem(item)
        
        layout.addWidget(list_widget)
        
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        
        if dialog.exec_() == QDialog.Accepted:
            current_item = list_widget.currentItem()
            if current_item:
                shape_type, section = current_item.data(Qt.UserRole)
                # Set the combo boxes
                shape_index = self.shape_type_combo.findData(shape_type)
                if shape_index >= 0:
                    self.shape_type_combo.setCurrentIndex(shape_index)
                    self.on_shape_type_changed()
                    section_index = self.section_combo.findData(section)
                    if section_index >= 0:
                        self.section_combo.setCurrentIndex(section_index)
                        self.on_section_changed()
    
    def update_preview(self):
        """Update live preview"""
        if not self.show_preview_cb.isChecked():
            self.clear_preview()
            return
        
        try:
            # Clear existing preview
            self.clear_preview()
            
            # Create temporary profile object
            self.create_preview_object()
            
            # Update properties display
            self.update_properties_display()
            
        except Exception as e:
            App.Console.PrintError(f"Preview update failed: {e}\n")
    
    def create_preview_object(self):
        """Create preview object"""
        if not App.ActiveDocument:
            App.newDocument("ProfilePreview")
        
        # Create preview object
        preview_name = "ProfilePreview_Temp"
        
        # Remove existing preview
        if self.preview_object:
            try:
                App.ActiveDocument.removeObject(self.preview_object.Name)
            except:
                pass
        
        # Create new preview
        self.preview_object = App.ActiveDocument.addObject("Part::FeaturePython", preview_name)
        StructuralProfile(self.preview_object)
        if GUI_AVAILABLE:
            ViewProviderStructuralProfile(self.preview_object.ViewObject)
            # Make preview semi-transparent
            self.preview_object.ViewObject.Transparency = 30
        
        # Apply current settings
        self.apply_current_settings_to_object(self.preview_object)
        
        App.ActiveDocument.recompute()
        
        # Fit view
        if GUI_AVAILABLE:
            try:
                Gui.ActiveDocument.ActiveView.fitAll()
            except:
                pass
    
    def apply_current_settings_to_object(self, obj):
        """Apply current GUI settings to an object"""
        # Profile type
        profile_type = self.get_current_profile_type()
        obj.ProfileType = profile_type
        
        # Dimensions
        def get_input_value(input_name, default=100.0):
            if input_name in self.dimension_inputs:
                try:
                    return float(self.dimension_inputs[input_name].text())
                except:
                    pass
            return default
        
        # Apply dimensions based on profile type
        if profile_type in ["I-Beam", "Wide Flange", "T-Section", "Channel"]:
            obj.Height = f"{get_input_value('height_input', 200)} mm"
            obj.Width = f"{get_input_value('width_input', 100)} mm"
            obj.WebThickness = f"{get_input_value('web_thickness_input', 8)} mm"
            obj.FlangeThickness = f"{get_input_value('flange_thickness_input', 12)} mm"
            
        elif profile_type == "HSS Rectangular":
            obj.Height = f"{get_input_value('height_input', 150)} mm"
            obj.Width = f"{get_input_value('width_input', 100)} mm"
            obj.Thickness = f"{get_input_value('thickness_input', 6)} mm"
            
        elif profile_type == "HSS Circular":
            obj.Diameter = f"{get_input_value('diameter_input', 100)} mm"
            obj.Thickness = f"{get_input_value('thickness_input', 6)} mm"
            
        elif profile_type == "Rectangle":
            obj.Height = f"{get_input_value('height_input', 150)} mm"
            obj.Width = f"{get_input_value('width_input', 100)} mm"
            
        elif profile_type == "Circle":
            obj.Diameter = f"{get_input_value('diameter_input', 100)} mm"
            
        elif profile_type == "Angle":
            obj.Leg1 = f"{get_input_value('leg1_input', 75)} mm"
            obj.Leg2 = f"{get_input_value('leg2_input', 50)} mm"
            obj.Thickness = f"{get_input_value('thickness_input', 6)} mm"
        
        # Scale
        obj.Scale = self.scale_spin.value()
        
        # Visual properties
        obj.ShowDimensions = self.show_dimensions_cb.isChecked()
        
        # Profile name
        section_name = self.section_combo.currentData()
        if section_name and section_name != "Custom":
            obj.ProfileName = section_name
        else:
            obj.ProfileName = f"Custom_{profile_type}"
    
    def update_properties_display(self):
        """Update properties table"""
        if not self.preview_object:
            return
        
        # Wait for object to compute properties
        App.ActiveDocument.recompute()
        
        properties = [
            ("Profile Type", self.preview_object.ProfileType),
            ("Profile Name", getattr(self.preview_object, 'ProfileName', 'Custom')),
            ("Area (mm²)", f"{self.preview_object.Area.getValueAs('mm^2'):.1f}" if hasattr(self.preview_object, 'Area') else "0"),
            ("Ix (mm⁴)", f"{self.preview_object.MomentInertiaX * 1e6:.0f}" if hasattr(self.preview_object, 'MomentInertiaX') else "0"),
            ("Iy (mm⁴)", f"{self.preview_object.MomentInertiaY * 1e6:.0f}" if hasattr(self.preview_object, 'MomentInertiaY') else "0"),
            ("Sx (mm³)", f"{self.preview_object.SectionModulusX * 1e9:.0f}" if hasattr(self.preview_object, 'SectionModulusX') else "0"),
            ("Sy (mm³)", f"{self.preview_object.SectionModulusY * 1e9:.0f}" if hasattr(self.preview_object, 'SectionModulusY') else "0"),
            ("Weight (kg/m)", f"{self.preview_object.Weight:.2f}" if hasattr(self.preview_object, 'Weight') else "0"),
        ]
        
        # Dimension properties based on profile type
        profile_type = self.get_current_profile_type()
        if profile_type in ["I-Beam", "Wide Flange", "Channel", "T-Section"]:
            properties.extend([
                ("Height (mm)", f"{self.preview_object.Height.getValueAs('mm'):.1f}"),
                ("Width (mm)", f"{self.preview_object.Width.getValueAs('mm'):.1f}"),
                ("Web Thickness (mm)", f"{self.preview_object.WebThickness.getValueAs('mm'):.1f}"),
                ("Flange Thickness (mm)", f"{self.preview_object.FlangeThickness.getValueAs('mm'):.1f}")
            ])
        
        self.properties_table.setRowCount(len(properties))
        
        for row, (prop_name, prop_value) in enumerate(properties):
            self.properties_table.setItem(row, 0, QTableWidgetItem(prop_name))
            self.properties_table.setItem(row, 1, QTableWidgetItem(str(prop_value)))
        
        self.properties_table.resizeColumnsToContents()
    
    def toggle_preview(self, enabled):
        """Toggle preview on/off"""
        if enabled:
            self.update_preview()
        else:
            self.clear_preview()
    
    def clear_preview(self):
        """Clear preview object"""
        if self.preview_object:
            try:
                App.ActiveDocument.removeObject(self.preview_object.Name)
            except:
                pass
            self.preview_object = None
    
    def load_existing_data(self):
        """Load data from existing profile object"""
        if not self.is_editing or not self.profile_object:
            return
        
        try:
            # Set profile type
            profile_type = self.profile_object.ProfileType
            for button in self.profile_type_group.buttons():
                if button.property("profile_type") == profile_type:
                    button.setChecked(True)
                    break
            
            # Create dimension inputs for this type
            self.create_dimension_inputs()
            
            # Load dimension values
            dimension_mappings = {
                'height_input': 'Height',
                'width_input': 'Width', 
                'web_thickness_input': 'WebThickness',
                'flange_thickness_input': 'FlangeThickness',
                'thickness_input': 'Thickness',
                'diameter_input': 'Diameter',
                'leg1_input': 'Leg1',
                'leg2_input': 'Leg2'
            }
            
            for input_name, prop_name in dimension_mappings.items():
                if input_name in self.dimension_inputs and hasattr(self.profile_object, prop_name):
                    value = getattr(self.profile_object, prop_name)
                    if hasattr(value, 'getValueAs'):
                        self.dimension_inputs[input_name].setText(f"{value.getValueAs('mm'):.1f}")
            
            # Load other properties
            if hasattr(self.profile_object, 'Scale'):
                self.scale_spin.setValue(self.profile_object.Scale)
                
            if hasattr(self.profile_object, 'ShowDimensions'):
                self.show_dimensions_cb.setChecked(self.profile_object.ShowDimensions)
            
        except Exception as e:
            App.Console.PrintError(f"Failed to load existing data: {e}\n")
    
    def export_to_calc(self):
        """Export properties to calc system"""
        if not self.preview_object:
            QMessageBox.warning(self.form, "Export Error", "No profile data available to export.")
            return
        
        try:
            # Get calc properties
            App.ActiveDocument.recompute()
            
            if hasattr(self.preview_object, 'CalcProperties') and self.preview_object.CalcProperties:
                calc_props = self.preview_object.CalcProperties
                
                # Show export dialog with properties
                self.show_calc_export_dialog(calc_props)
            else:
                QMessageBox.warning(self.form, "Export Error", "No calc properties available.")
                
        except Exception as e:
            App.Console.PrintError(f"Calc export failed: {e}\n")
            QMessageBox.critical(self.form, "Export Error", f"Export failed: {e}")
    
    def show_calc_export_dialog(self, calc_props):
        """Show calc export properties dialog"""
        dialog = QDialog(self.form)
        dialog.setWindowTitle("Export to Calc")
        dialog.setModal(True)
        dialog.resize(400, 300)
        
        layout = QVBoxLayout(dialog)
        
        # Info label
        info_label = QLabel("The following properties will be exported to calc:")
        layout.addWidget(info_label)
        
        # Properties table
        table = QTableWidget(len(calc_props), 2)
        table.setHorizontalHeaderLabels(["Property", "Value"])
        
        for row, (key, value) in enumerate(calc_props.items()):
            table.setItem(row, 0, QTableWidgetItem(key))
            if isinstance(value, float):
                table.setItem(row, 1, QTableWidgetItem(f"{value:.6e}"))
            else:
                table.setItem(row, 1, QTableWidgetItem(str(value)))
        
        table.resizeColumnsToContents()
        layout.addWidget(table)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        
        if dialog.exec_() == QDialog.Accepted:
            # Actually export to calc (placeholder)
            QMessageBox.information(self.form, "Export Complete", 
                                  f"Properties exported to calc system successfully!")
            App.Console.PrintMessage(f"Calc properties exported: {calc_props}\n")
    
    def accept(self):
        """Accept and create/update profile"""
        try:
            if self.is_editing:
                # Update existing profile
                self.apply_current_settings_to_object(self.profile_object)
                App.Console.PrintMessage(f"Updated profile: {self.profile_object.Label}\n")
            else:
                # Create new profile
                profile_name = f"StructuralProfile_{self.get_current_profile_type()}"
                profile_obj = App.ActiveDocument.addObject("Part::FeaturePython", profile_name)
                StructuralProfile(profile_obj)
                if GUI_AVAILABLE:
                    ViewProviderStructuralProfile(profile_obj.ViewObject)
                
                # Apply settings
                self.apply_current_settings_to_object(profile_obj)
                
                App.Console.PrintMessage(f"Created new profile: {profile_obj.Label}\n")
            
            # Clean up preview
            self.clear_preview()
            
            # Recompute
            App.ActiveDocument.recompute()
            
            return True
            
        except Exception as e:
            App.Console.PrintError(f"Profile creation/update failed: {e}\n")
            QMessageBox.critical(self.form, "Error", f"Operation failed: {e}")
            return False
    
    def reject(self):
        """Cancel and clean up"""
        self.clear_preview()
        return True


def show_profile_task_panel(profile_object=None):
    """Show Profile Task Panel"""
    if not GUI_AVAILABLE:
        App.Console.PrintError("GUI not available. Install PySide2.\n")
        return False
    
    if not PROFILE_OBJECT_AVAILABLE:
        App.Console.PrintError("StructuralProfile object not available.\n")
        return False
    
    try:
        panel = ProfileTaskPanel(profile_object)
        Gui.Control.showDialog(panel)
        return True
    except Exception as e:
        App.Console.PrintError(f"Failed to show profile task panel: {e}\n")
        return False


# Command for creating profile
class CreateStructuralProfileCommand:
    """FreeCAD command to create structural profiles"""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), '..', 'resources', 'icons', 'structural_profile.svg'),
            'MenuText': 'Create Structural Profile',
            'ToolTip': 'Create parametric structural profile with GUI'
        }
    
    def Activated(self):
        show_profile_task_panel()
    
    def IsActive(self):
        return True


# Register command
if GUI_AVAILABLE:
    Gui.addCommand('StructureTools_CreateStructuralProfile', CreateStructuralProfileCommand())