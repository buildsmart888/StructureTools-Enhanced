# -*- coding: utf-8 -*-
"""
Advanced Section Manager GUI with ArchProfile Integration
GUI สำหรับจัดการ Section โดยใช้ ArchProfile และ steelpy database
"""

import FreeCAD as App
import os
import sys
import json
from pathlib import Path

# Safe imports for FreeCAD modules
try:
    import FreeCADGui as Gui
    FREECADGUI_AVAILABLE = True
except ImportError:
    FREECADGUI_AVAILABLE = False

try:
    import Draft
    DRAFT_AVAILABLE = True
except ImportError:
    DRAFT_AVAILABLE = False

try:
    import Arch
    ARCH_AVAILABLE = True
except ImportError:
    ARCH_AVAILABLE = False

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

# Import steelpy integration - use fixed version for stability
try:
    from ..data.SteelPyIntegrationFixed import (
        get_steelpy_manager, get_available_shape_types, 
        get_sections_for_shape, get_section_data, 
        search_steel_sections, STEELPY_AVAILABLE
    )
    STEELPY_INTEGRATION = True
    if STEELPY_AVAILABLE:
        print("[OK] steelpy integration loaded successfully")
    else:
        print("[INFO] steelpy integration loaded, but steelpy not available")
except ImportError:
    STEELPY_INTEGRATION = False
    STEELPY_AVAILABLE = False
    print("[WARNING] steelpy integration not available")

# Import existing core components
try:
    from ..core import get_section_manager
    from ..section import Section, ViewProviderSection
    CORE_AVAILABLE = True
except ImportError:
    CORE_AVAILABLE = False

class SteelPyDatabase:
    """Wrapper for steelpy database integration"""
    
    def __init__(self):
        self.available = STEELPY_AVAILABLE and STEELPY_INTEGRATION
        self.shape_types = {}
        
        if self.available:
            self.load_shape_types()
    
    def load_shape_types(self):
        """Load all available shape types from steelpy using safe integration"""
        try:
            # Use safe integration manager
            shape_types_data = get_available_shape_types()
            
            # Convert to internal format
            self.shape_types = {}
            for shape_key, shape_info in shape_types_data.items():
                # Create dummy collection object for compatibility
                class DummyCollection:
                    pass
                
                dummy_collection = DummyCollection()
                self.shape_types[shape_key] = (shape_info['name'], dummy_collection)
            
            print(f"[OK] Loaded {len(self.shape_types)} shape types via safe integration")
            
        except Exception as e:
            print(f"Error loading steelpy shapes: {e}")
            self.available = False
    
    def get_shape_list(self, shape_type):
        """Get list of available shapes for a type"""
        if not self.available:
            return []
        
        try:
            return get_sections_for_shape(shape_type)
        except Exception as e:
            print(f"Error getting shape list: {e}")
            return []
    
    def get_section_properties(self, shape_type, section_name):
        """Get detailed properties for a specific section using safe integration"""
        if not self.available:
            return None
        
        try:
            # Use the safe integration function
            properties = get_section_data(shape_type, section_name)
            
            if properties:
                # Ensure compatibility with our expected property names
                if 'area' in properties and 'Area' not in properties:
                    properties['Area'] = properties['area']
                if 'weight' in properties and 'Weight' not in properties:
                    properties['Weight'] = properties['weight']
                if 'height' in properties and 'Height' not in properties:
                    properties['Height'] = properties['height']
                if 'width' in properties and 'Width' not in properties:
                    properties['Width'] = properties['width']
                if 'web_thickness' in properties and 'WebThickness' not in properties:
                    properties['WebThickness'] = properties['web_thickness']
                if 'flange_thickness' in properties and 'FlangeThickness' not in properties:
                    properties['FlangeThickness'] = properties['flange_thickness']
                if 'ix' in properties and 'Ix' not in properties:
                    properties['Ix'] = properties['ix']
                if 'iy' in properties and 'Iy' not in properties:
                    properties['Iy'] = properties['iy']
                if 'sx' in properties and 'Sx' not in properties:
                    properties['Sx'] = properties['sx']
                if 'sy' in properties and 'Sy' not in properties:
                    properties['Sy'] = properties['sy']
                if 'zx' in properties and 'Zx' not in properties:
                    properties['Zx'] = properties['zx']
                if 'zy' in properties and 'Zy' not in properties:
                    properties['Zy'] = properties['zy']
                # rx and ry should already be in the correct format from safe integration
                if 'j' in properties and 'J' not in properties:
                    properties['J'] = properties['j']
                
                # Add derived properties for compatibility
                if 'Ix' in properties:
                    properties['MomentInertiaY'] = properties['Ix']
                if 'Iy' in properties:
                    properties['MomentInertiaZ'] = properties['Iy']
                if 'Sx' in properties:
                    properties['SectionModulusY'] = properties['Sx']
                if 'Sy' in properties:
                    properties['SectionModulusZ'] = properties['Sy']
                if 'Zx' in properties:
                    properties['PlasticModulusY'] = properties['Zx']
                if 'Zy' in properties:
                    properties['PlasticModulusZ'] = properties['Zy']
                if 'rx' in properties:
                    properties['RadiusGyrationY'] = properties['rx']
                if 'ry' in properties:
                    properties['RadiusGyrationZ'] = properties['ry']
                if 'J' in properties:
                    properties['TorsionalConstant'] = properties['J']
                
                # Ensure section name and type are set
                if 'SectionName' not in properties:
                    properties['SectionName'] = section_name
                if 'ShapeType' not in properties:
                    properties['ShapeType'] = shape_type
                
            return properties
            
        except Exception as e:
            print(f"Error getting section properties: {e}")
            return None

class ArchProfileIntegration:
    """Integration with FreeCAD's ArchProfile system"""
    
    def __init__(self):
        self.available = ARCH_AVAILABLE
    
    def check_arch_availability(self):
        """Check if Arch module is available"""
        return ARCH_AVAILABLE
    
    def create_arch_profile(self, profile_data):
        """Create ArchProfile object from section data"""
        if not self.available:
            return None
        
        try:
            # Create profile object
            profile_obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", 
                                                       f"Profile_{profile_data['SectionName']}")
            
            # Use Arch.Profile if available
            try:
                import Arch
                Arch.Profile(profile_obj)
            except:
                # Fallback to basic profile creation
                pass
            
            # Set profile properties
            if hasattr(profile_obj, 'Height') and 'Height' in profile_data:
                profile_obj.Height = f"{profile_data['Height']:.2f} mm"
            if hasattr(profile_obj, 'Width') and 'Width' in profile_data:
                profile_obj.Width = f"{profile_data['Width']:.2f} mm"
            
            # Create profile shape based on type
            shape_type = profile_data.get('ShapeType', 'W_shapes')
            
            if 'W_shapes' in shape_type or 'M_shapes' in shape_type or 'S_shapes' in shape_type:
                shape = self.create_i_beam_profile(profile_data)
            elif 'HSS_rect' in shape_type:
                shape = self.create_rectangular_hss_profile(profile_data)
            elif 'HSS_round' in shape_type or 'Pipe' in shape_type:
                shape = self.create_circular_profile(profile_data)
            elif 'L_shapes' in shape_type:
                shape = self.create_angle_profile(profile_data)
            else:
                # Default to I-beam
                shape = self.create_i_beam_profile(profile_data)
            
            if shape:
                profile_obj.Shape = shape
                profile_obj.Label = profile_data['SectionName']
            
            return profile_obj
            
        except Exception as e:
            print(f"Error creating ArchProfile: {e}")
            return None
    
    def create_i_beam_profile(self, data):
        """Create I-beam profile shape"""
        try:
            import Part
            
            # Extract dimensions (convert to FreeCAD units)
            height = data.get('Height', 300)  # mm
            width = data.get('Width', 150)   # mm
            web_thickness = data.get('WebThickness', 8)  # mm
            flange_thickness = data.get('FlangeThickness', 12)  # mm
            
            # Create I-beam profile sketch
            points = [
                # Bottom flange
                (-width/2, -height/2),
                (width/2, -height/2),
                (width/2, -height/2 + flange_thickness),
                (web_thickness/2, -height/2 + flange_thickness),
                # Web
                (web_thickness/2, height/2 - flange_thickness),
                # Top flange
                (width/2, height/2 - flange_thickness),
                (width/2, height/2),
                (-width/2, height/2),
                (-width/2, height/2 - flange_thickness),
                (-web_thickness/2, height/2 - flange_thickness),
                # Web
                (-web_thickness/2, -height/2 + flange_thickness),
                (-width/2, -height/2 + flange_thickness),
                (-width/2, -height/2)  # Close
            ]
            
            # Create wire from points
            edges = []
            for i in range(len(points) - 1):
                p1 = App.Vector(points[i][0], points[i][1], 0)
                p2 = App.Vector(points[i+1][0], points[i+1][1], 0)
                edges.append(Part.makeLine(p1, p2))
            
            # Close the profile
            wire = Part.Wire(edges)
            face = Part.Face(wire)
            
            return face
            
        except Exception as e:
            print(f"Error creating I-beam profile: {e}")
            return None
    
    def create_rectangular_hss_profile(self, data):
        """Create rectangular HSS profile shape"""
        try:
            import Part
            
            height = data.get('Height', 100)  # mm
            width = data.get('Width', 100)   # mm
            thickness = data.get('WebThickness', 6)  # mm (wall thickness)
            
            # Outer rectangle
            outer_rect = Part.makePolygon([
                App.Vector(-width/2, -height/2, 0),
                App.Vector(width/2, -height/2, 0),
                App.Vector(width/2, height/2, 0),
                App.Vector(-width/2, height/2, 0),
                App.Vector(-width/2, -height/2, 0)
            ])
            
            # Inner rectangle (hollow)
            inner_width = width - 2 * thickness
            inner_height = height - 2 * thickness
            
            if inner_width > 0 and inner_height > 0:
                inner_rect = Part.makePolygon([
                    App.Vector(-inner_width/2, -inner_height/2, 0),
                    App.Vector(inner_width/2, -inner_height/2, 0),
                    App.Vector(inner_width/2, inner_height/2, 0),
                    App.Vector(-inner_width/2, inner_height/2, 0),
                    App.Vector(-inner_width/2, -inner_height/2, 0)
                ])
                
                outer_face = Part.Face(outer_rect)
                inner_face = Part.Face(inner_rect)
                
                # Cut inner from outer
                profile_face = outer_face.cut(inner_face)
                return profile_face
            else:
                # Solid rectangle if wall too thick
                return Part.Face(outer_rect)
            
        except Exception as e:
            print(f"Error creating HSS profile: {e}")
            return None
    
    def create_circular_profile(self, data):
        """Create circular profile shape"""
        try:
            import Part
            
            # For pipes, extract outer diameter and wall thickness
            outer_diameter = data.get('Width', 100)  # mm
            thickness = data.get('WebThickness', 6)  # mm (wall thickness)
            
            # Create outer circle
            outer_circle = Part.makeCircle(outer_diameter/2)
            outer_face = Part.Face(outer_circle)
            
            # Create inner circle if hollow
            inner_diameter = outer_diameter - 2 * thickness
            if inner_diameter > 0:
                inner_circle = Part.makeCircle(inner_diameter/2)
                inner_face = Part.Face(inner_circle)
                
                # Cut inner from outer
                profile_face = outer_face.cut(inner_face)
                return profile_face
            else:
                # Solid circle
                return outer_face
            
        except Exception as e:
            print(f"Error creating circular profile: {e}")
            return None
    
    def create_angle_profile(self, data):
        """Create angle profile shape"""
        try:
            import Part
            
            # For L shapes, we need leg dimensions
            height = data.get('Height', 100)  # mm
            width = data.get('Width', 100)   # mm
            thickness = data.get('WebThickness', 10)  # mm
            
            # Create L-shape
            points = [
                (0, 0),
                (width, 0),
                (width, thickness),
                (thickness, thickness),
                (thickness, height),
                (0, height),
                (0, 0)  # Close
            ]
            
            # Create wire from points
            edges = []
            for i in range(len(points) - 1):
                p1 = App.Vector(points[i][0], points[i][1], 0)
                p2 = App.Vector(points[i+1][0], points[i+1][1], 0)
                edges.append(Part.makeLine(p1, p2))
            
            wire = Part.Wire(edges)
            face = Part.Face(wire)
            
            return face
            
        except Exception as e:
            print(f"Error creating angle profile: {e}")
            return None

class SectionManagerGUI(QMainWindow):
    """Advanced Section Manager GUI with steelpy and ArchProfile integration"""
    
    def __init__(self):
        print("[INFO] Initializing SectionManagerGUI...")
        super(SectionManagerGUI, self).__init__()
        
        try:
            print("[INFO] Creating database connections...")
            # Initialize databases
            self.steelpy_db = SteelPyDatabase()
            self.arch_integration = ArchProfileIntegration()
            
            print("[INFO] Initializing UI...")
            # Initialize UI
            self.init_ui()
            
            print("[INFO] Loading section database...")
            # Load initial data
            self.load_section_database()
            
            print("[OK] SectionManagerGUI initialization completed!")
            
        except Exception as e:
            print(f"[ERROR] Failed to initialize SectionManagerGUI: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def init_ui(self):
        """Initialize user interface"""
        try:
            print("[INFO] Setting window properties...")
            self.setWindowTitle("Advanced Section Manager - StructureTools")
            self.setGeometry(100, 100, 1000, 700)
            
            print("[INFO] Creating central widget...")
            # Create central widget and main layout
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            main_layout = QHBoxLayout(central_widget)
            
            print("[INFO] Creating left panel...")
            # Left panel - Section browser
            left_panel = self.create_section_browser()
            main_layout.addWidget(left_panel, 1)
            
            print("[INFO] Creating right panel...")
            # Right panel - Properties and preview
            right_panel = self.create_properties_panel()
            main_layout.addWidget(right_panel, 1)
            
            print("[INFO] Creating status bar...")
            # Status bar
            self.status_bar = QStatusBar()
            self.setStatusBar(self.status_bar)
            
            # Update status
            if self.steelpy_db.available:
                self.status_bar.showMessage("steelpy database loaded successfully")
            else:
                self.status_bar.showMessage("steelpy not available - install with: pip install steelpy")
            
            print("[OK] UI initialization completed!")
            
        except Exception as e:
            print(f"[ERROR] UI initialization failed: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def create_section_browser(self):
        """Create section browser panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Title
        title = QLabel("Steel Section Database")
        title.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px;")
        layout.addWidget(title)
        
        # Database source selection
        source_group = QGroupBox("Database Source")
        source_layout = QVBoxLayout(source_group)
        
        self.source_steelpy = QRadioButton("steelpy (AISC)")
        self.source_steelpy.setChecked(True)
        self.source_steelpy.toggled.connect(self.on_source_changed)
        
        self.source_builtin = QRadioButton("Built-in Database")
        self.source_builtin.toggled.connect(self.on_source_changed)
        
        source_layout.addWidget(self.source_steelpy)
        source_layout.addWidget(self.source_builtin)
        layout.addWidget(source_group)
        
        # Shape type selection
        shape_group = QGroupBox("Shape Type")
        shape_layout = QVBoxLayout(shape_group)
        
        self.shape_type_combo = QComboBox()
        self.shape_type_combo.currentTextChanged.connect(self.on_shape_type_changed)
        shape_layout.addWidget(self.shape_type_combo)
        layout.addWidget(shape_group)
        
        # Section list with search
        section_group = QGroupBox("Available Sections")
        section_layout = QVBoxLayout(section_group)
        
        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search sections...")
        self.search_box.textChanged.connect(self.on_search_changed)
        section_layout.addWidget(self.search_box)
        
        # Section list
        self.section_list = QListWidget()
        self.section_list.itemClicked.connect(self.on_section_selected)
        self.section_list.itemDoubleClicked.connect(self.on_section_double_clicked)
        section_layout.addWidget(self.section_list)
        
        section_group.setLayout(section_layout)
        layout.addWidget(section_group)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        self.create_section_btn = QPushButton("Create Section")
        self.create_section_btn.clicked.connect(self.create_section_object)
        self.create_section_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")
        
        self.create_profile_btn = QPushButton("Create ArchProfile")
        self.create_profile_btn.clicked.connect(self.create_arch_profile)
        self.create_profile_btn.setStyleSheet("QPushButton { background-color: #2196F3; color: white; font-weight: bold; }")
        
        button_layout.addWidget(self.create_section_btn)
        button_layout.addWidget(self.create_profile_btn)
        layout.addLayout(button_layout)
        
        return panel
    
    def create_properties_panel(self):
        """Create properties display panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Title
        title = QLabel("Section Properties")
        title.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px;")
        layout.addWidget(title)
        
        # Properties table
        self.properties_table = QTableWidget()
        self.properties_table.setColumnCount(2)
        self.properties_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.properties_table.horizontalHeader().setStretchLastSection(True)
        self.properties_table.setAlternatingRowColors(True)
        layout.addWidget(self.properties_table)
        
        # Preview area
        preview_group = QGroupBox("Section Preview")
        preview_layout = QVBoxLayout(preview_group)
        
        self.preview_label = QLabel("Select a section to see preview")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setMinimumHeight(200)
        self.preview_label.setStyleSheet("border: 1px solid gray; background-color: #f0f0f0;")
        preview_layout.addWidget(self.preview_label)
        
        layout.addWidget(preview_group)
        
        # Additional info
        info_group = QGroupBox("Additional Information")
        info_layout = QVBoxLayout(info_group)
        
        self.info_text = QTextEdit()
        self.info_text.setMaximumHeight(100)
        self.info_text.setReadOnly(True)
        info_layout.addWidget(self.info_text)
        
        layout.addWidget(info_group)
        
        return panel
    
    def load_section_database(self):
        """Load available shape types"""
        self.shape_type_combo.clear()
        
        if self.source_steelpy.isChecked() and self.steelpy_db.available:
            # Load steelpy shape types
            for shape_key, (shape_name, _) in self.steelpy_db.shape_types.items():
                self.shape_type_combo.addItem(shape_name, shape_key)
        else:
            # Load built-in database
            builtin_shapes = [
                ("Wide Flange Beams", "W_SHAPES"),
                ("Standard I-Beams", "S_SHAPES"),
                ("Channels", "C_SHAPES"),
                ("Angles", "L_SHAPES"),
                ("Rectangular HSS", "HSS_RECT"),
                ("Round HSS", "HSS_ROUND")
            ]
            for name, key in builtin_shapes:
                self.shape_type_combo.addItem(name, key)
    
    def on_source_changed(self):
        """Handle database source change"""
        self.load_section_database()
        self.section_list.clear()
        self.properties_table.setRowCount(0)
    
    def on_shape_type_changed(self):
        """Handle shape type change"""
        self.section_list.clear()
        
        shape_key = self.shape_type_combo.currentData()
        if not shape_key:
            return
        
        if self.source_steelpy.isChecked() and self.steelpy_db.available:
            # Load sections from steelpy
            sections = self.steelpy_db.get_shape_list(shape_key)
            self.section_list.addItems(sections)
        else:
            # Load from built-in database
            sections = self.get_builtin_sections(shape_key)
            self.section_list.addItems(sections)
    
    def on_search_changed(self):
        """Handle search text change"""
        search_text = self.search_box.text().lower()
        
        for i in range(self.section_list.count()):
            item = self.section_list.item(i)
            item.setHidden(search_text not in item.text().lower())
    
    def on_section_selected(self, item):
        """Handle section selection"""
        section_name = item.text()
        shape_key = self.shape_type_combo.currentData()
        
        if self.source_steelpy.isChecked() and self.steelpy_db.available:
            properties = self.steelpy_db.get_section_properties(shape_key, section_name)
        else:
            properties = self.get_builtin_section_properties(shape_key, section_name)
        
        if properties:
            self.display_properties(properties)
            self.update_preview(properties)
    
    def on_section_double_clicked(self, item):
        """Handle section double-click"""
        self.create_section_object()
    
    def display_properties(self, properties):
        """Display section properties in table"""
        # Define property order and display names
        property_order = [
            ('SectionName', 'Section Name'),
            ('Area', 'Cross-sectional Area (mm²)'),
            ('Weight', 'Weight (kg/m)'),
            ('Height', 'Height (mm)'),
            ('Width', 'Width (mm)'),
            ('WebThickness', 'Web Thickness (mm)'),
            ('FlangeThickness', 'Flange Thickness (mm)'),
            ('Ix', 'Moment of Inertia Ix (mm⁴)'),
            ('Iy', 'Moment of Inertia Iy (mm⁴)'),
            ('Sx', 'Section Modulus Sx (mm³)'),
            ('Sy', 'Section Modulus Sy (mm³)'),
            ('Zx', 'Plastic Modulus Zx (mm³)'),
            ('Zy', 'Plastic Modulus Zy (mm³)'),
            ('rx', 'Radius of Gyration rx (mm)'),
            ('ry', 'Radius of Gyration ry (mm)'),
            ('J', 'Torsional Constant J (mm⁴)')
        ]
        
        # Clear table and set row count
        display_props = [(key, name) for key, name in property_order if key in properties]
        self.properties_table.setRowCount(len(display_props))
        
        # Populate table
        for row, (prop_key, prop_name) in enumerate(display_props):
            value = properties[prop_key]
            
            # Format value
            if isinstance(value, (int, float)):
                if prop_key in ['Area', 'Ix', 'Iy', 'J']:
                    formatted_value = f"{value:,.0f}"
                elif prop_key in ['Sx', 'Sy', 'Zx', 'Zy']:
                    formatted_value = f"{value:,.0f}"
                elif prop_key == 'Weight':
                    formatted_value = f"{value:.2f}"
                else:
                    formatted_value = f"{value:.1f}"
            else:
                formatted_value = str(value)
            
            # Set table items
            self.properties_table.setItem(row, 0, QTableWidgetItem(prop_name))
            self.properties_table.setItem(row, 1, QTableWidgetItem(formatted_value))
        
        # Update info text
        info_text = f"Standard: {properties.get('Standard', 'Unknown')}\n"
        info_text += f"Shape Type: {properties.get('ShapeType', 'Unknown')}\n"
        info_text += f"Source: {properties.get('Source', 'Unknown')}"
        self.info_text.setText(info_text)
    
    def update_preview(self, properties):
        """Update section preview"""
        # For now, show text preview
        # TODO: Add 2D section drawing
        shape_type = properties.get('ShapeType', '')
        section_name = properties.get('SectionName', '')
        
        preview_text = f"Section: {section_name}\n\n"
        
        if 'W_shapes' in shape_type:
            preview_text += "Wide Flange (W) Section\n"
        elif 'HSS' in shape_type:
            preview_text += "Hollow Structural Section\n"
        elif 'L_shapes' in shape_type:
            preview_text += "Angle Section\n"
        else:
            preview_text += f"Type: {shape_type}\n"
        
        if 'Height' in properties and 'Width' in properties:
            preview_text += f"\nDimensions:\n"
            preview_text += f"H: {properties['Height']:.1f} mm\n"
            preview_text += f"W: {properties['Width']:.1f} mm"
        
        self.preview_label.setText(preview_text)
    
    def create_section_object(self):
        """Create StructureTools Section object"""
        current_item = self.section_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select a section first.")
            return
        
        section_name = current_item.text()
        shape_key = self.shape_type_combo.currentData()
        
        if not App.ActiveDocument:
            App.newDocument("SectionDocument")
        
        try:
            if self.source_steelpy.isChecked() and self.steelpy_db.available:
                properties = self.steelpy_db.get_section_properties(shape_key, section_name)
            else:
                properties = self.get_builtin_section_properties(shape_key, section_name)
            
            if not properties:
                QMessageBox.critical(self, "Error", "Could not retrieve section properties.")
                return
            
            # Create Section object
            section_obj = App.ActiveDocument.addObject("Part::FeaturePython", f"Section_{section_name.replace('X', 'x')}")
            Section(section_obj, [])
            ViewProviderSection(section_obj.ViewObject)
            
            # Set properties
            section_obj.SectionName = properties['SectionName']
            if 'Area' in properties:
                section_obj.Area = properties['Area']
            if 'MomentInertiaY' in properties:
                section_obj.Iy = properties['MomentInertiaY']
            if 'MomentInertiaZ' in properties:
                section_obj.Iz = properties['MomentInertiaZ']
            if 'TorsionalConstant' in properties:
                section_obj.J = properties['TorsionalConstant']
            if 'SectionModulusY' in properties:
                section_obj.Sy = properties['SectionModulusY']
            if 'SectionModulusZ' in properties:
                section_obj.Sz = properties['SectionModulusZ']
            
            # Set label
            section_obj.Label = f"Section_{section_name.replace('X', 'x')}"
            
            App.ActiveDocument.recompute()
            
            QMessageBox.information(self, "Success", f"Section {section_name} created successfully!")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create section: {str(e)}")
    
    def create_arch_profile(self):
        """Create ArchProfile object"""
        current_item = self.section_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select a section first.")
            return
        
        if not self.arch_integration.available:
            QMessageBox.critical(self, "Error", "Arch module not available.")
            return
        
        section_name = current_item.text()
        shape_key = self.shape_type_combo.currentData()
        
        if not App.ActiveDocument:
            App.newDocument("SectionDocument")
        
        try:
            if self.source_steelpy.isChecked() and self.steelpy_db.available:
                properties = self.steelpy_db.get_section_properties(shape_key, section_name)
            else:
                properties = self.get_builtin_section_properties(shape_key, section_name)
            
            if not properties:
                QMessageBox.critical(self, "Error", "Could not retrieve section properties.")
                return
            
            # Create ArchProfile
            profile_obj = self.arch_integration.create_arch_profile(properties)
            
            if profile_obj:
                App.ActiveDocument.recompute()
                QMessageBox.information(self, "Success", f"ArchProfile {section_name} created successfully!")
            else:
                QMessageBox.critical(self, "Error", "Failed to create ArchProfile.")
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create ArchProfile: {str(e)}")
    
    def get_builtin_sections(self, shape_key):
        """Get sections from built-in database"""
        # Simple built-in sections for fallback
        builtin_sections = {
            'W_SHAPES': ['W8x31', 'W10x49', 'W12x26', 'W14x22', 'W16x31', 'W18x35'],
            'S_SHAPES': ['S8x18.4', 'S10x25.4', 'S12x31.8', 'S15x42.9'],
            'C_SHAPES': ['C8x11.5', 'C10x15.3', 'C12x20.7'],
            'L_SHAPES': ['L3x3x1/4', 'L4x4x1/2', 'L6x6x3/8'],
            'HSS_RECT': ['HSS8x6x1/4', 'HSS10x8x3/8', 'HSS12x8x1/2'],
            'HSS_ROUND': ['HSS6.625x0.280', 'HSS8.625x0.322', 'HSS10.750x0.365']
        }
        
        return builtin_sections.get(shape_key, [])
    
    def get_builtin_section_properties(self, shape_key, section_name):
        """Get properties from built-in database"""
        # Simple properties for demonstration
        # In real implementation, this would come from a comprehensive database
        
        base_properties = {
            'SectionName': section_name,
            'ShapeType': shape_key,
            'Standard': 'AISC (Built-in)',
            'Source': 'Built-in Database',
            'Area': 5000,  # mm²
            'Weight': 25.0,  # kg/m
            'Height': 250,  # mm
            'Width': 150,   # mm
            'WebThickness': 8,  # mm
            'FlangeThickness': 12,  # mm
            'Ix': 50000000,  # mm⁴
            'Iy': 15000000,  # mm⁴
            'Sx': 400000,   # mm³
            'Sy': 200000,   # mm³
            'rx': 100,      # mm
            'ry': 55,       # mm
            'J': 500000     # mm⁴
        }
        
        return base_properties

def show_section_manager_gui():
    """Show Section Manager GUI"""
    if not GUI_AVAILABLE:
        print("GUI not available")
        if FREECADGUI_AVAILABLE:
            try:
                import FreeCADGui as Gui
                Gui.SendMsgToActiveView("StdCmdPython")
                App.Console.PrintError("GUI libraries not available. Install PySide2 or PySide.\n")
            except:
                print("GUI libraries not available. Install PySide2 or PySide.")
        return None
    
    # Show warning if steelpy not available
    if not STEELPY_AVAILABLE:
        if FREECADGUI_AVAILABLE:
            App.Console.PrintWarning("steelpy library not available. Install with: pip install steelpy\n")
            App.Console.PrintMessage("GUI will work with built-in sections only.\n")
        else:
            print("WARNING: steelpy library not available. Install with: pip install steelpy")
            print("GUI will work with built-in sections only.")
    
    try:
        # Get or create QApplication
        app = QApplication.instance()
        if app is None:
            print("[INFO] Creating QApplication instance")
            app = QApplication([])
        
        # Check if already open
        for widget in app.topLevelWidgets():
            if isinstance(widget, SectionManagerGUI):
                print("[INFO] Found existing Section Manager GUI - bringing to front")
                widget.show()
                widget.raise_()
                widget.activateWindow()
                return widget
        
        # Create new instance with detailed logging
        print("[INFO] Creating new Section Manager GUI instance...")
        gui = SectionManagerGUI()
        
        # Keep reference to prevent garbage collection
        if not hasattr(show_section_manager_gui, '_gui_instances'):
            show_section_manager_gui._gui_instances = []
        show_section_manager_gui._gui_instances.append(gui)
        
        print("[INFO] Showing GUI window...")
        gui.show()
        gui.raise_()
        gui.activateWindow()
        
        print("[OK] Advanced Section Manager GUI displayed successfully!")
        return gui
        
    except Exception as e:
        error_msg = f"Failed to open Section Manager GUI: {str(e)}"
        print(f"[ERROR] {error_msg}")
        
        # Print detailed traceback
        import traceback
        traceback.print_exc()
        
        if FREECADGUI_AVAILABLE:
            App.Console.PrintError(error_msg + "\n")
        else:
            print(f"ERROR: {error_msg}")
        return None

# Command integration
class SectionManagerCommand:
    """FreeCAD command for Section Manager"""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), '..', 'resources', 'icons', 'section_manager.svg'),
            'MenuText': 'Advanced Section Manager',
            'ToolTip': 'Open advanced section manager with steelpy database integration'
        }
    
    def Activated(self):
        show_section_manager_gui()
    
    def IsActive(self):
        return True

# Register command
if GUI_AVAILABLE:
    Gui.addCommand('StructureTools_SectionManager', SectionManagerCommand())