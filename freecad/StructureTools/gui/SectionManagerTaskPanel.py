# -*- coding: utf-8 -*-
"""
Advanced Section Manager Task Panel
Task Panel version สำหรับความเสถียรใน FreeCAD
"""

import FreeCAD as App
import os
import sys

# Safe imports for FreeCAD modules
try:
    import FreeCADGui as Gui
    FREECADGUI_AVAILABLE = True
except ImportError:
    FREECADGUI_AVAILABLE = False

# Safe GUI imports
try:
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

# Import enhanced database for complete section information
try:
    from ..data.EnhancedSteelDatabase import (
        get_enhanced_database, get_enhanced_shape_types,
        get_enhanced_sections, get_enhanced_section_data,
        get_section_geometry_data, search_enhanced_sections
    )
    ENHANCED_DB_INTEGRATION = True
    print("[OK] Enhanced steel database integration loaded for TaskPanel")
except ImportError:
    ENHANCED_DB_INTEGRATION = False
    print("[WARNING] Enhanced database integration not available for TaskPanel")

# Fallback to basic steelpy integration
try:
    from ..data.SteelPyIntegrationFixed import (
        get_steelpy_manager, get_available_shape_types, 
        get_sections_for_shape, get_section_data, 
        search_steel_sections, STEELPY_AVAILABLE
    )
    STEELPY_INTEGRATION = True
    if STEELPY_AVAILABLE:
        print("[OK] steelpy integration loaded successfully for TaskPanel")
    else:
        print("[INFO] steelpy integration loaded, but steelpy not available")
except ImportError:
    STEELPY_INTEGRATION = False
    STEELPY_AVAILABLE = False
    print("[WARNING] steelpy integration not available for TaskPanel")

# Import existing core components
try:
    from ..core import get_section_manager
    from ..section import Section, ViewProviderSection
    CORE_AVAILABLE = True
except ImportError:
    CORE_AVAILABLE = False

# Property mapper
try:
    from ..utils.enhanced_property_mapper import standardize_section_properties
    PROPERTY_MAPPER_AVAILABLE = True
except Exception:
    PROPERTY_MAPPER_AVAILABLE = False

class AdvancedSectionManagerTaskPanel:
    """Advanced Section Manager as FreeCAD Task Panel"""
    
    def __init__(self):
        print("[INFO] Initializing AdvancedSectionManagerTaskPanel...")
        
        # Initialize variables
        self.enhanced_db_available = ENHANCED_DB_INTEGRATION
        self.steelpy_available = STEELPY_AVAILABLE and STEELPY_INTEGRATION
        self.current_shape_type = None
        self.current_section = None
        self.shape_types = {}
        self.enhanced_database = None
        
        # Initialize database
        self.initialize_database()
        
        # Create UI
        self.form = self.create_task_panel()
        
        print("[OK] AdvancedSectionManagerTaskPanel initialized!")
    
    def initialize_database(self):
        """Initialize enhanced database or fallback to basic"""
        try:
            if self.enhanced_db_available:
                print("[INFO] Initializing Enhanced Steel Database...")
                self.enhanced_database = get_enhanced_database()
                if self.enhanced_database.available:
                    self.shape_types = get_enhanced_shape_types()
                    print(f"[OK] Enhanced database loaded: {len(self.shape_types)} shape types")
                    return
                else:
                    print("[WARNING] Enhanced database not available, falling back...")
                    self.enhanced_db_available = False
            
            # Fallback to basic steelpy
            if self.steelpy_available:
                print("[INFO] Using basic steelpy integration...")
                self.shape_types = get_available_shape_types()
                print(f"[OK] Basic steelpy loaded: {len(self.shape_types)} shape types")
            else:
                print("[WARNING] No database available, using built-in sections")
                
        except Exception as e:
            print(f"[ERROR] Database initialization failed: {e}")
            self.enhanced_db_available = False
            self.steelpy_available = False
    
    def create_task_panel(self):
        """Create the task panel UI"""
        print("[INFO] Creating TaskPanel UI...")

        # Main widget
        widget = QWidget()
        main_layout = QVBoxLayout(widget)

        # Title
        title = QLabel("Advanced Section Manager")
        title.setStyleSheet("font-weight: bold; font-size: 16px; color: #2E86AB; padding: 5px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Database status
        status_group = QGroupBox("Database Status")
        status_layout = QVBoxLayout(status_group)

        if self.enhanced_db_available:
            total_sections = self.enhanced_database.get_statistics()['total_sections'] if self.enhanced_database else 0
            status_text = f"✓ Enhanced Steel Database ({len(self.shape_types)} shape types, {total_sections} sections)"
            status_color = "green"
        elif self.steelpy_available:
            status_text = f"✓ Basic steelpy database ({len(self.shape_types)} shape types available)"
            status_color = "blue"
        else:
            status_text = "⚠ No steel database - using built-in sections"
            status_color = "orange"

        self.status_label = QLabel(status_text)
        self.status_label.setStyleSheet(f"color: {status_color}; padding: 5px;")
        status_layout.addWidget(self.status_label)
        main_layout.addWidget(status_group)

        # Shape type selection
        shape_group = QGroupBox("Steel Section Type")
        shape_layout = QFormLayout(shape_group)

        self.shape_combo = QComboBox()
        shape_layout.addRow("Type:", self.shape_combo)

        # Populate shape types
        if self.enhanced_db_available or self.steelpy_available:
            for key, info in self.shape_types.items():
                if self.enhanced_db_available:
                    # Enhanced database includes category information
                    category = info.get('category', 'Unknown')
                    display_text = f"{info['name']} ({info['count']} sections, {category})"
                else:
                    # Basic steelpy
                    display_text = f"{info['name']} ({info['count']} sections)"
                self.shape_combo.addItem(display_text, key)
        else:
            # Built-in options
            builtin_shapes = [
                ("Wide Flange Beams (W)", "W_SHAPES"),
                ("Standard I-Beams (S)", "S_SHAPES"),
                ("Channels (C)", "C_SHAPES"),
                ("Angles (L)", "L_SHAPES")
            ]
            for name, key in builtin_shapes:
                self.shape_combo.addItem(name, key)

        # Connect after population to avoid on_shape_changed firing before UI ready
        self.shape_combo.currentTextChanged.connect(self.on_shape_changed)

        main_layout.addWidget(shape_group)

        # Section selection
        section_group = QGroupBox("Available Sections")
        section_layout = QVBoxLayout(section_group)

        # Search box
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search:"))
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Filter sections...")
        self.search_edit.textChanged.connect(self.filter_sections)
        # Pressing Enter after typing will select the first matching section
        self.search_edit.returnPressed.connect(self.select_first_matching)
        search_layout.addWidget(self.search_edit)
        section_layout.addLayout(search_layout)

        # Section list
        self.section_list = QListWidget()
        self.section_list.itemClicked.connect(self.on_section_selected)
        section_layout.addWidget(self.section_list)

        main_layout.addWidget(section_group)

        # Properties display
        props_group = QGroupBox("Section Properties")
        props_layout = QVBoxLayout(props_group)

        self.props_table = QTableWidget(0, 2)
        self.props_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.props_table.horizontalHeader().setStretchLastSection(True)
        self.props_table.setMaximumHeight(200)
        props_layout.addWidget(self.props_table)

        main_layout.addWidget(props_group)

        # Action buttons
        button_layout = QHBoxLayout()

        self.create_section_btn = QPushButton("Create StructureTools Section")
        self.create_section_btn.setStyleSheet("""
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
        self.create_section_btn.clicked.connect(self.create_section)
        self.create_section_btn.setEnabled(False)

        self.create_profile_btn = QPushButton("Create ArchProfile")
        self.create_profile_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.create_profile_btn.clicked.connect(self.create_arch_profile)
        self.create_profile_btn.setEnabled(False)

        # Add Draw Section button
        self.draw_section_btn = QPushButton("Draw Section View")
        self.draw_section_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        self.draw_section_btn.clicked.connect(self.draw_section)
        self.draw_section_btn.setEnabled(False)

        button_layout.addWidget(self.create_section_btn)
        button_layout.addWidget(self.create_profile_btn)
        button_layout.addWidget(self.draw_section_btn)
        # Import profiles button
        self.import_profiles_btn = QPushButton("Import Profiles (JSON)")
        self.import_profiles_btn.setStyleSheet("""
            QPushButton {
                background-color: #6A1B9A;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #5E35B1;
            }
        """)
        self.import_profiles_btn.clicked.connect(self.import_profiles_json)
        button_layout.addWidget(self.import_profiles_btn)
        # Send to BIM GenericTools button
        self.send_bim_btn = QPushButton("Send to BIM GenericTools")
        self.send_bim_btn.setStyleSheet("""
            QPushButton {
                background-color: #8E24AA;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #6A1B9A;
            }
        """)
        self.send_bim_btn.clicked.connect(self.send_to_bim_generictools)
        self.send_bim_btn.setEnabled(False)
        button_layout.addWidget(self.send_bim_btn)
        main_layout.addLayout(button_layout)

        # Load initial sections
        if self.shape_combo.count() > 0:
            self.on_shape_changed()

        print("[OK] TaskPanel UI created successfully!")
        return widget

    def import_profiles_json(self):
        """Open file dialog to import profiles JSON and merge into enhanced DB"""
        try:
            # Use Qt file dialog if available
            if GUI_AVAILABLE:
                from PySide2.QtWidgets import QFileDialog
                dlg = QFileDialog()
                dlg.setFileMode(QFileDialog.ExistingFile)
                dlg.setNameFilter("JSON files (*.json)")
                if dlg.exec_():
                    files = dlg.selectedFiles()
                    if files:
                        file_path = files[0]
                    else:
                        return
                else:
                    return
            else:
                # Fallback: ask for path via input
                file_path = input('Path to profiles JSON: ')

            # Importer
            from ..data.ImportedProfilesImporter import import_profiles_json as importer
            from ..data.EnhancedSteelDatabase import get_enhanced_database

            db = get_enhanced_database()
            ok = importer(file_path, db)
            if ok:
                # Refresh state
                self.enhanced_db_available = True
                self.enhanced_database = db
                self.shape_types = get_enhanced_shape_types()
                # Rebuild shape combo
                self.shape_combo.clear()
                for key, info in self.shape_types.items():
                    category = info.get('category', 'Unknown')
                    display_text = f"{info['name']} ({info['count']} sections, {category})"
                    self.shape_combo.addItem(display_text, key)

                # Auto-select IMPORTED shape_type if present
                imported_index = None
                for i in range(self.shape_combo.count()):
                    if self.shape_combo.itemData(i) == 'IMPORTED':
                        imported_index = i
                        break
                if imported_index is not None:
                    self.shape_combo.setCurrentIndex(imported_index)
                    # Trigger loading of sections
                    self.on_shape_changed()

                self.status_label.setText(f"✓ Enhanced Steel Database (imported {len(self.shape_types)} shape types)")
                if FREECADGUI_AVAILABLE:
                    App.Console.PrintMessage(f"Imported profiles from {file_path}\n")
            else:
                if FREECADGUI_AVAILABLE:
                    App.Console.PrintError(f"Failed to import profiles from {file_path}\n")

        except Exception as e:
            print(f"[ERROR] Import profiles failed: {e}")
            if FREECADGUI_AVAILABLE:
                App.Console.PrintError(f"Import profiles failed: {e}\n")
    
    def on_shape_changed(self):
        """Handle shape type change"""
        shape_key = self.shape_combo.currentData()
        if not shape_key:
            return
        
        print(f"[INFO] Loading sections for shape type: {shape_key}")
        self.current_shape_type = shape_key
        self.section_list.clear()
        
        try:
            if self.enhanced_db_available:
                sections = get_enhanced_sections(shape_key)
            elif self.steelpy_available:
                sections = get_sections_for_shape(shape_key)
            else:
                sections = self.get_builtin_sections(shape_key)
            
            self.section_list.addItems(sections)
            print(f"[OK] Loaded {len(sections)} sections")
            
        except Exception as e:
            print(f"[ERROR] Failed to load sections: {e}")
    
    def filter_sections(self):
        """Filter sections based on search text"""
        search_text = self.search_edit.text().lower()
        
        for i in range(self.section_list.count()):
            item = self.section_list.item(i)
            item.setHidden(search_text not in item.text().lower())

    def select_first_matching(self):
        """Select the first visible item after search return pressed"""
        for i in range(self.section_list.count()):
            item = self.section_list.item(i)
            if not item.isHidden():
                self.section_list.setCurrentItem(item)
                # Trigger selection handler
                self.on_section_selected(item)
                return
    
    def on_section_selected(self, item):
        """Handle section selection"""
        section_name = item.text()
        self.current_section = section_name
        
        print(f"[INFO] Selected section: {section_name}")
        
        try:
            if self.enhanced_db_available:
                properties = get_enhanced_section_data(self.current_shape_type, section_name)
                geometry = get_section_geometry_data(self.current_shape_type, section_name)
                self.current_geometry = geometry
            elif self.steelpy_available:
                properties = get_section_data(self.current_shape_type, section_name)
                self.current_geometry = None
            else:
                properties = self.get_builtin_properties(self.current_shape_type, section_name)
                self.current_geometry = None
            
            if properties:
                self.display_properties(properties)
                self.create_section_btn.setEnabled(True)
                self.create_profile_btn.setEnabled(True)
                # Enable send to BIM when enhanced geometry or ArchProfile is possible
                try:
                    self.send_bim_btn.setEnabled(bool(self.current_geometry or self.enhanced_db_available))
                except Exception:
                    pass
                # Enable Draw Section button if geometry is available
                if hasattr(self, 'draw_section_btn'):
                    self.draw_section_btn.setEnabled(bool(self.current_geometry))
                    if self.current_geometry:
                        print(f"[INFO] Geometry data available for section drawing")
            
        except Exception as e:
            print(f"[ERROR] Failed to get section properties: {e}")
    
    def display_properties(self, properties):
        """Display section properties in table"""
        # Property order - enhanced for complete data
        if self.enhanced_db_available:
            # Enhanced database properties with units
            prop_order = [
                ('name', 'Section Name'),
                ('area', 'Cross-sectional Area'),
                ('weight', 'Weight per Unit Length'),
                ('height', 'Overall Height'),
                ('width', 'Overall Width'),
                ('web_thickness', 'Web Thickness'),
                ('flange_thickness', 'Flange Thickness'),
                ('moment_inertia_x', 'Moment of Inertia Ix'),
                ('moment_inertia_y', 'Moment of Inertia Iy'),
                ('section_modulus_x', 'Section Modulus Sx'),
                ('section_modulus_y', 'Section Modulus Sy'),
                ('plastic_modulus_x', 'Plastic Modulus Zx'),
                ('plastic_modulus_y', 'Plastic Modulus Zy'),
                ('radius_gyration_x', 'Radius of Gyration rx'),
                ('radius_gyration_y', 'Radius of Gyration ry'),
                ('torsional_constant', 'Torsional Constant J')
            ]
        else:
            # Basic properties
            prop_order = [
                ('name', 'Section Name'),
                ('area', 'Area (mm²)'),
                ('weight', 'Weight (kg/m)'),
                ('height', 'Height (mm)'),
                ('width', 'Width (mm)'),
                ('web_thickness', 'Web Thickness (mm)'),
                ('flange_thickness', 'Flange Thickness (mm)'),
                ('ix', 'Ix (mm⁴)'),
                ('iy', 'Iy (mm⁴)'),
                ('sx', 'Sx (mm³)'),
                ('sy', 'Sy (mm³)')
            ]
        
        # Filter available properties
        available_props = [(key, name) for key, name in prop_order if key in properties]
        self.props_table.setRowCount(len(available_props))
        
        for row, (prop_key, prop_name) in enumerate(available_props):
            value = properties[prop_key]
            
            # Format value based on database type
            if self.enhanced_db_available and isinstance(value, dict) and 'value' in value:
                # Enhanced database with units
                formatted_value = f"{value['value']:,.1f} {value.get('unit', '')}"
                if value['value'] >= 1000000:
                    # Scientific notation for very large numbers
                    formatted_value = f"{value['value']:.2e} {value.get('unit', '')}"
            elif isinstance(value, (int, float)):
                # Basic values
                if prop_key in ['area', 'ix', 'iy', 'moment_inertia_x', 'moment_inertia_y']:
                    if value >= 1000000:
                        formatted_value = f"{value:.2e}"
                    else:
                        formatted_value = f"{value:,.0f}"
                elif prop_key in ['sx', 'sy', 'section_modulus_x', 'section_modulus_y']:
                    if value >= 1000000:
                        formatted_value = f"{value:.2e}"
                    else:
                        formatted_value = f"{value:,.0f}"
                elif prop_key in ['weight']:
                    formatted_value = f"{value:.2f}"
                else:
                    formatted_value = f"{value:.1f}"
            else:
                formatted_value = str(value)
            
            # Set table items
            self.props_table.setItem(row, 0, QTableWidgetItem(prop_name))
            self.props_table.setItem(row, 1, QTableWidgetItem(formatted_value))
    
    def create_section(self):
        """Create StructureTools Section object"""
        if not self.current_section or not self.current_shape_type:
            return
        
        if not App.ActiveDocument:
            App.newDocument("SectionDocument")
        
        try:
            # Get properties and geometry
            if self.enhanced_db_available:
                properties = get_enhanced_section_data(self.current_shape_type, self.current_section)
                geometry = get_section_geometry_data(self.current_shape_type, self.current_section)
            elif self.steelpy_available:
                properties = get_section_data(self.current_shape_type, self.current_section)
                geometry = None
            else:
                properties = self.get_builtin_properties(self.current_shape_type, self.current_section)
                geometry = None
            
            if not properties:
                return
            
            # Create Section object
            section_obj = App.ActiveDocument.addObject("Part::FeaturePython", 
                                                       f"Section_{self.current_section.replace('X', 'x')}")
            Section(section_obj, [])
            ViewProviderSection(section_obj.ViewObject)
            
            # Set properties - handle both enhanced and basic formats
            section_obj.SectionName = properties.get('name', self.current_section)
            
            # Area
            area_val = self.extract_property_value(properties, ['area'])
            if area_val:
                section_obj.Area = area_val
            
            # Moments of inertia
            ix_val = self.extract_property_value(properties, ['moment_inertia_x', 'ix'])
            if ix_val:
                section_obj.Iy = ix_val  # Major axis in StructureTools
            
            iy_val = self.extract_property_value(properties, ['moment_inertia_y', 'iy'])  
            if iy_val:
                section_obj.Iz = iy_val  # Minor axis in StructureTools
            
            # Torsional constant
            j_val = self.extract_property_value(properties, ['torsional_constant', 'j'])
            if j_val:
                section_obj.J = j_val
            
            # Section moduli
            sx_val = self.extract_property_value(properties, ['section_modulus_x', 'sx'])
            if sx_val:
                section_obj.Sy = sx_val
                
            sy_val = self.extract_property_value(properties, ['section_modulus_y', 'sy'])
            if sy_val:
                section_obj.Sz = sy_val
            
            section_obj.Label = f"Section_{self.current_section.replace('X', 'x')}"
            
            # Store enhanced data if available
            if self.enhanced_db_available and geometry:
                # Add custom properties for enhanced data
                section_obj.addProperty("App::PropertyPythonObject", "EnhancedProperties", 
                                       "Enhanced", "Complete section properties")
                section_obj.addProperty("App::PropertyPythonObject", "GeometryData", 
                                       "Enhanced", "Section geometry for drawing")
                section_obj.EnhancedProperties = properties
                section_obj.GeometryData = geometry
                # Also attach standardized mapping for calc consumers
                try:
                    if PROPERTY_MAPPER_AVAILABLE:
                        standardized = standardize_section_properties(properties)
                        section_obj.addProperty("App::PropertyPythonObject", "StandardizedProperties", 
                                               "Enhanced", "Standardized section properties")
                        section_obj.StandardizedProperties = standardized
                except Exception:
                    pass
            elif self.enhanced_db_available:
                # Attach minimal enhanced properties even if geometry missing
                try:
                    section_obj.addProperty("App::PropertyPythonObject", "EnhancedProperties", 
                                           "Enhanced", "Complete section properties")
                    section_obj.EnhancedProperties = properties
                    try:
                        if PROPERTY_MAPPER_AVAILABLE:
                            standardized = standardize_section_properties(properties)
                            section_obj.addProperty("App::PropertyPythonObject", "StandardizedProperties", 
                                                   "Enhanced", "Standardized section properties")
                            section_obj.StandardizedProperties = standardized
                    except Exception:
                        pass
                except Exception:
                    pass
            
            App.ActiveDocument.recompute()
            
            print(f"[OK] Section {self.current_section} created successfully!")
            
            # Show message
            if FREECADGUI_AVAILABLE:
                App.Console.PrintMessage(f"Section {self.current_section} created successfully!\n")
                if geometry:
                    App.Console.PrintMessage("Section includes geometry data for drawing.\n")
            
        except Exception as e:
            print(f"[ERROR] Failed to create section: {e}")
            if FREECADGUI_AVAILABLE:
                App.Console.PrintError(f"Failed to create section: {e}\n")
    
    def extract_property_value(self, properties, prop_names):
        """Extract property value from enhanced or basic format"""
        for prop_name in prop_names:
            if prop_name in properties:
                value = properties[prop_name]
                if isinstance(value, dict) and 'value' in value:
                    return value['value']  # Enhanced format
                elif isinstance(value, (int, float)):
                    return value  # Basic format
        return None
    
    def draw_section(self):
        """Draw section view using geometry data"""
        if not self.current_section or not self.current_shape_type:
            print("[WARNING] No section selected for drawing")
            return
        
        if not self.enhanced_db_available or not hasattr(self, 'current_geometry') or not self.current_geometry:
            print("[WARNING] No geometry data available for drawing")
            if FREECADGUI_AVAILABLE:
                App.Console.PrintMessage("Geometry data not available. Install steelpy and use enhanced database.\n")
            return
        
        if not App.ActiveDocument:
            App.newDocument("SectionDrawing")
        
        try:
            print(f"[INFO] Drawing section view for: {self.current_section}")
            
            # Import drawing system
            from ..geometry.SectionDrawing import draw_section_from_data
            
            # Draw the section
            section_drawing = draw_section_from_data(self.current_geometry, self.current_section)
            
            if section_drawing:
                print(f"[OK] Section drawing created: {section_drawing.Label}")
                if FREECADGUI_AVAILABLE:
                    App.Console.PrintMessage(f"Section drawing created: {section_drawing.Label}\n")
                
                # Fit view to show the drawing
                try:
                    import FreeCADGui as Gui
                    Gui.activeDocument().activeView().fitAll()
                except:
                    pass
            else:
                print("[ERROR] Failed to create section drawing")
                if FREECADGUI_AVAILABLE:
                    App.Console.PrintError("Failed to create section drawing\n")
        
        except Exception as e:
            print(f"[ERROR] Drawing failed: {e}")
            if FREECADGUI_AVAILABLE:
                App.Console.PrintError(f"Drawing failed: {e}\n")
            import traceback
            traceback.print_exc()
    
    def create_arch_profile(self):
        """Create ArchProfile object (simplified version)"""
        if not self.current_section or not self.current_shape_type:
            return

        try:
            from ..geometry.SectionDrawing import SectionDrawer
            # Try to get geometry for the current section
            geometry = None
            if self.enhanced_db_available:
                geometry = get_section_geometry_data(self.current_shape_type, self.current_section)

            drawer = SectionDrawer()

            # If geometry contains drawing_points, create ArchProfile from them
            if geometry and 'drawing_points' in geometry and geometry['drawing_points']:
                profile = drawer.create_arch_profile_from_points(geometry['drawing_points'], self.current_section)
                if profile:
                    print(f"[OK] ArchProfile created: {getattr(profile, 'Label', self.current_section)}")
                    if FREECADGUI_AVAILABLE:
                        App.Console.PrintMessage(f"ArchProfile created: {getattr(profile, 'Label', self.current_section)}\n")
                    # Enable Send to BIM button when profile available
                    try:
                        self.send_bim_btn.setEnabled(True)
                    except Exception:
                        pass
                    return profile

            # Fallback: if geometry describes circular params, create simple approximated polygon
            if geometry and geometry.get('beam_type') == 'CIRCULAR' and ('outer_diameter' in geometry):
                od = geometry.get('outer_diameter')
                # approximate circle with 32 points
                pts = []
                import math
                for i in range(32):
                    theta = 2*math.pi*(i/32.0)
                    pts.append([ (od/2.0)*math.cos(theta), (od/2.0)*math.sin(theta) ])
                profile = drawer.create_arch_profile_from_points(pts, self.current_section)
                if profile:
                    print(f"[OK] ArchProfile created (circular approx): {getattr(profile, 'Label', self.current_section)}")
                    if FREECADGUI_AVAILABLE:
                        App.Console.PrintMessage(f"ArchProfile created: {getattr(profile, 'Label', self.current_section)}\n")
                    try:
                        self.send_bim_btn.setEnabled(True)
                    except Exception:
                        pass
                    return profile
                    return

            print(f"[WARNING] No suitable geometry available for ArchProfile creation for {self.current_section}")
            return None

        except Exception as e:
            print(f"[ERROR] ArchProfile creation failed: {e}")
            if FREECADGUI_AVAILABLE:
                App.Console.PrintError(f"ArchProfile creation failed: {e}\n")
            return None

    def send_to_bim_generictools(self):
        """Send the created ArchProfile or section data to BIM GenericTools bridge if available"""
        if not self.current_section:
            return

        try:
            # Try to import a BIM GenericTools bridge module (project-provided or FreeCAD BIM GenericTools)
            try:
                from ..integration.BIMIntegration import BIMStructuralIntegration
                bridge = BIMStructuralIntegration()
            except Exception:
                # Try importing FreeCAD's GenericTools if available
                try:
                    import GenericTools as GT
                    bridge = None
                except Exception:
                    bridge = None

            # Get the current ArchProfile or create it
            profile_obj = None
            if self.enhanced_db_available:
                geometry = get_section_geometry_data(self.current_shape_type, self.current_section)
            else:
                geometry = None

            # If a profile exists in document, prefer it
            if FREECADGUI_AVAILABLE and App.ActiveDocument:
                # try to find Profile by label
                for obj in App.ActiveDocument.Objects:
                    if getattr(obj, 'Label', '') == f"Profile_{self.current_section}" or getattr(obj, 'Label', '') == self.current_section:
                        profile_obj = obj
                        break

            # If not found, attempt to create one
            if not profile_obj:
                profile_obj = self.create_arch_profile()

            if not profile_obj:
                print(f"[WARNING] No ArchProfile available to send to BIM for {self.current_section}")
                return False

            # Attach enhanced properties (if available)
            if self.enhanced_db_available:
                props = get_enhanced_section_data(self.current_shape_type, self.current_section)
                # Attach minimal properties to profile for BIM consumption
                try:
                    if hasattr(profile_obj, 'addProperty'):
                        profile_obj.addProperty('App::PropertyPythonObject', 'EnhancedProperties', 'BIM', 'Enhanced section properties')
                        profile_obj.EnhancedProperties = props
                except Exception:
                    pass

            # Attempt to call bridge API if available
            if 'bridge' in locals() and bridge:
                try:
                    bridge.import_from_bim([profile_obj])
                    print(f"[OK] Sent profile {self.current_section} to BIMStructuralIntegration bridge")
                    if FREECADGUI_AVAILABLE:
                        App.Console.PrintMessage(f"Sent profile {self.current_section} to BIM bridge\n")
                    return True
                except Exception as e:
                    print(f"[WARNING] BIM bridge call failed: {e}")

            # Fallback: try to call GenericTools if available
            try:
                import GenericTools as GT
                if hasattr(GT, 'import_profile'):
                    GT.import_profile(profile_obj)
                    print(f"[OK] Sent profile {self.current_section} to GenericTools.import_profile")
                    return True
            except Exception:
                pass

            print("[WARNING] No BIM GenericTools bridge available to receive the profile")
            return False

        except Exception as e:
            print(f"[ERROR] Failed to send to BIM GenericTools: {e}")
            if FREECADGUI_AVAILABLE:
                App.Console.PrintError(f"Failed to send to BIM GenericTools: {e}\n")
            return False
    
    def get_builtin_sections(self, shape_key):
        """Get built-in sections for fallback"""
        builtin_sections = {
            'W_SHAPES': ['W8x31', 'W10x49', 'W12x26', 'W14x22', 'W16x31'],
            'S_SHAPES': ['S8x18.4', 'S10x25.4', 'S12x31.8'],
            'C_SHAPES': ['C8x11.5', 'C10x15.3', 'C12x20.7'],
            'L_SHAPES': ['L3x3x1/4', 'L4x4x1/2', 'L6x6x3/8']
        }
        return builtin_sections.get(shape_key, [])
    
    def get_builtin_properties(self, shape_key, section_name):
        """Get built-in properties for fallback"""
        return {
            'name': section_name,
            'area': 5000,  # mm²
            'weight': 25.0,  # kg/m
            'height': 250,  # mm
            'width': 150,   # mm
            'web_thickness': 8,  # mm
            'flange_thickness': 12,  # mm
            'ix': 50000000,  # mm⁴
            'iy': 15000000,  # mm⁴
            'sx': 400000,   # mm³
            'sy': 200000,   # mm³
            'j': 500000     # mm⁴
        }
    
    def accept(self):
        """Accept and close task panel"""
        print("[INFO] Task Panel accepted - closing...")
        return True
    
    def reject(self):
        """Reject and close task panel"""
        print("[INFO] Task Panel rejected - closing...")
        return True

def show_advanced_section_manager_task_panel():
    """Show Advanced Section Manager as Task Panel"""
    if not GUI_AVAILABLE:
        print("[ERROR] GUI not available - install PySide2")
        if FREECADGUI_AVAILABLE:
            App.Console.PrintError("GUI libraries not available. Install PySide2.\n")
        return False
    
    if not FREECADGUI_AVAILABLE:
        print("[ERROR] FreeCADGui not available - run from FreeCAD")
        return False
    
    try:
        # Create and show task panel
        panel = AdvancedSectionManagerTaskPanel()
        Gui.Control.showDialog(panel)
        
        print("[OK] Advanced Section Manager Task Panel opened!")
        return True
        
    except Exception as e:
        error_msg = f"Failed to show task panel: {str(e)}"
        print(f"[ERROR] {error_msg}")
        App.Console.PrintError(error_msg + "\n")
        import traceback
        traceback.print_exc()
        return False

# Alternative command for TaskPanel version
class AdvancedSectionManagerTaskPanelCommand:
    """FreeCAD command for TaskPanel version"""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), '..', 'resources', 'icons', 'advanced_section_manager.svg'),
            'MenuText': 'Advanced Section Manager (TaskPanel)',
            'ToolTip': 'Open advanced section manager as task panel'
        }
    
    def Activated(self):
        show_advanced_section_manager_task_panel()
    
    def IsActive(self):
        return True

# Register TaskPanel command
if GUI_AVAILABLE and FREECADGUI_AVAILABLE:
    Gui.addCommand('StructureTools_AdvancedSectionManagerTaskPanel', 
                   AdvancedSectionManagerTaskPanelCommand())