# -*- coding: utf-8 -*-
"""
Steel Profile Selector Interface
Interface สำหรับเลือก steel profiles จาก steelpy database
"""

import FreeCAD as App
import os
import json

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

# Import steelpy integration
try:
    from ..data.SteelPyIntegration import (
        get_steelpy_manager, 
        get_available_shape_types,
        get_sections_for_shape,
        get_section_data,
        search_steel_sections,
        filter_steel_sections,
        STEELPY_AVAILABLE
    )
    INTEGRATION_AVAILABLE = True
except ImportError:
    INTEGRATION_AVAILABLE = False

class SteelProfileModel(QAbstractTableModel):
    """Table model for steel profile data"""
    
    def __init__(self):
        super().__init__()
        self.sections_data = []
        self.headers = ['Section', 'Type', 'Area (mm²)', 'Weight (kg/m)', 'Height (mm)', 'Width (mm)']
        
    def set_sections_data(self, sections_data):
        """Set sections data"""
        self.beginResetModel()
        self.sections_data = sections_data
        self.endResetModel()
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.sections_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return None
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self.sections_data):
            return None
        
        section_info = self.sections_data[index.row()]
        column = index.column()
        
        if role == Qt.DisplayRole:
            if column == 0:  # Section name
                return section_info['name']
            elif column == 1:  # Type
                return section_info.get('shape_name', '')
            elif column == 2:  # Area
                props = section_info.get('properties', {})
                area = props.get('area', 0)
                return f"{area:,.0f}" if area else "-"
            elif column == 3:  # Weight
                props = section_info.get('properties', {})
                weight = props.get('weight', 0)
                return f"{weight:.2f}" if weight else "-"
            elif column == 4:  # Height
                props = section_info.get('properties', {})
                height = props.get('height', 0)
                return f"{height:.1f}" if height else "-"
            elif column == 5:  # Width
                props = section_info.get('properties', {})
                width = props.get('width', 0)
                return f"{width:.1f}" if width else "-"
        
        elif role == Qt.TextAlignmentRole:
            if column > 1:  # Numbers
                return Qt.AlignRight | Qt.AlignVCenter
            return Qt.AlignLeft | Qt.AlignVCenter
        
        elif role == Qt.UserRole:
            return section_info
        
        return None

class PropertyFilterWidget(QWidget):
    """Widget for filtering properties"""
    
    filterChanged = Signal()
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Property Filters")
        title.setStyleSheet("font-weight: bold; margin-bottom: 5px;")
        layout.addWidget(title)
        
        # Scroll area for filters
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMaximumHeight(300)
        
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # Area filter
        self.area_group = self.create_range_filter("Cross-sectional Area (mm²)", "area")
        scroll_layout.addWidget(self.area_group)
        
        # Weight filter
        self.weight_group = self.create_range_filter("Weight (kg/m)", "weight")
        scroll_layout.addWidget(self.weight_group)
        
        # Height filter
        self.height_group = self.create_range_filter("Height (mm)", "height")
        scroll_layout.addWidget(self.height_group)
        
        # Width filter
        self.width_group = self.create_range_filter("Width (mm)", "width")
        scroll_layout.addWidget(self.width_group)
        
        # Moment of inertia filters
        self.ix_group = self.create_range_filter("Moment of Inertia Ix (mm⁴)", "ix")
        scroll_layout.addWidget(self.ix_group)
        
        self.iy_group = self.create_range_filter("Moment of Inertia Iy (mm⁴)", "iy")
        scroll_layout.addWidget(self.iy_group)
        
        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)
        
        # Control buttons
        button_layout = QHBoxLayout()
        
        self.apply_btn = QPushButton("Apply Filters")
        self.apply_btn.clicked.connect(self.apply_filters)
        
        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(self.clear_filters)
        
        button_layout.addWidget(self.apply_btn)
        button_layout.addWidget(self.clear_btn)
        layout.addLayout(button_layout)
    
    def create_range_filter(self, label, property_name):
        """Create range filter group"""
        group = QGroupBox(label)
        layout = QGridLayout(group)
        
        # Enable checkbox
        enable_check = QCheckBox("Enable")
        enable_check.setObjectName(f"{property_name}_enable")
        layout.addWidget(enable_check, 0, 0, 1, 2)
        
        # Min value
        layout.addWidget(QLabel("Min:"), 1, 0)
        min_spin = QDoubleSpinBox()
        min_spin.setObjectName(f"{property_name}_min")
        min_spin.setRange(0, 999999999)
        min_spin.setEnabled(False)
        layout.addWidget(min_spin, 1, 1)
        
        # Max value
        layout.addWidget(QLabel("Max:"), 2, 0)
        max_spin = QDoubleSpinBox()
        max_spin.setObjectName(f"{property_name}_max")
        max_spin.setRange(0, 999999999)
        max_spin.setValue(999999999)
        max_spin.setEnabled(False)
        layout.addWidget(max_spin, 2, 1)
        
        # Connect enable checkbox
        enable_check.toggled.connect(min_spin.setEnabled)
        enable_check.toggled.connect(max_spin.setEnabled)
        enable_check.toggled.connect(self.filterChanged)
        min_spin.valueChanged.connect(self.filterChanged)
        max_spin.valueChanged.connect(self.filterChanged)
        
        return group
    
    def apply_filters(self):
        """Apply current filters"""
        self.filterChanged.emit()
    
    def clear_filters(self):
        """Clear all filters"""
        for group in [self.area_group, self.weight_group, self.height_group, 
                      self.width_group, self.ix_group, self.iy_group]:
            for child in group.findChildren(QCheckBox):
                child.setChecked(False)
            for child in group.findChildren(QDoubleSpinBox):
                if "min" in child.objectName():
                    child.setValue(0)
                else:
                    child.setValue(999999999)
        
        self.filterChanged.emit()
    
    def get_active_filters(self):
        """Get currently active filters"""
        filters = {}
        
        property_names = ['area', 'weight', 'height', 'width', 'ix', 'iy']
        
        for prop in property_names:
            enable_check = self.findChild(QCheckBox, f"{prop}_enable")
            if enable_check and enable_check.isChecked():
                min_spin = self.findChild(QDoubleSpinBox, f"{prop}_min")
                max_spin = self.findChild(QDoubleSpinBox, f"{prop}_max")
                
                if min_spin and max_spin:
                    min_val = min_spin.value()
                    max_val = max_spin.value()
                    
                    if min_val > 0 or max_val < 999999999:
                        filters[prop] = {}
                        if min_val > 0:
                            filters[prop]['min'] = min_val
                        if max_val < 999999999:
                            filters[prop]['max'] = max_val
        
        return filters

class SectionComparisonWidget(QWidget):
    """Widget for comparing multiple sections"""
    
    def __init__(self):
        super().__init__()
        self.sections_to_compare = []
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Section Comparison")
        title.setStyleSheet("font-weight: bold; font-size: 12px;")
        layout.addWidget(title)
        
        # Comparison table
        self.comparison_table = QTableWidget()
        self.comparison_table.setMaximumHeight(200)
        layout.addWidget(self.comparison_table)
        
        # Control buttons
        button_layout = QHBoxLayout()
        
        self.add_btn = QPushButton("Add Selected")
        self.add_btn.clicked.connect(self.add_current_selection)
        
        self.remove_btn = QPushButton("Remove Selected")
        self.remove_btn.clicked.connect(self.remove_selected)
        
        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(self.clear_comparison)
        
        self.export_btn = QPushButton("Export Comparison")
        self.export_btn.clicked.connect(self.export_comparison)
        
        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.remove_btn)
        button_layout.addWidget(self.clear_btn)
        button_layout.addWidget(self.export_btn)
        layout.addLayout(button_layout)
    
    def add_section(self, section_data):
        """Add section to comparison"""
        if section_data not in self.sections_to_compare:
            self.sections_to_compare.append(section_data)
            self.update_comparison_table()
    
    def remove_selected(self):
        """Remove selected sections from comparison"""
        selected_rows = set()
        for item in self.comparison_table.selectedItems():
            selected_rows.add(item.row())
        
        for row in sorted(selected_rows, reverse=True):
            if 0 <= row < len(self.sections_to_compare):
                del self.sections_to_compare[row]
        
        self.update_comparison_table()
    
    def clear_comparison(self):
        """Clear all sections from comparison"""
        self.sections_to_compare.clear()
        self.update_comparison_table()
    
    def update_comparison_table(self):
        """Update comparison table display"""
        if not self.sections_to_compare:
            self.comparison_table.setRowCount(0)
            self.comparison_table.setColumnCount(0)
            return
        
        # Set table dimensions
        self.comparison_table.setRowCount(len(self.sections_to_compare))
        
        # Define columns to compare
        columns = [
            ('name', 'Section'),
            ('area', 'Area (mm²)'),
            ('weight', 'Weight (kg/m)'),
            ('height', 'Height (mm)'),
            ('width', 'Width (mm)'),
            ('ix', 'Ix (mm⁴)'),
            ('iy', 'Iy (mm⁴)')
        ]
        
        self.comparison_table.setColumnCount(len(columns))
        self.comparison_table.setHorizontalHeaderLabels([col[1] for col in columns])
        
        # Fill table data
        for row, section_data in enumerate(self.sections_to_compare):
            properties = section_data.get('properties', {})
            
            for col, (prop_key, _) in enumerate(columns):
                if prop_key == 'name':
                    value = section_data.get('name', '')
                    item = QTableWidgetItem(str(value))
                else:
                    value = properties.get(prop_key, 0)
                    if isinstance(value, (int, float)) and value > 0:
                        if prop_key in ['area', 'ix', 'iy']:
                            formatted = f"{value:,.0f}"
                        elif prop_key == 'weight':
                            formatted = f"{value:.2f}"
                        else:
                            formatted = f"{value:.1f}"
                    else:
                        formatted = "-"
                    
                    item = QTableWidgetItem(formatted)
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                
                self.comparison_table.setItem(row, col, item)
        
        # Resize columns
        self.comparison_table.resizeColumnsToContents()
    
    def export_comparison(self):
        """Export comparison to file"""
        if not self.sections_to_compare:
            QMessageBox.information(self, "Info", "No sections to export.")
            return
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Export Comparison", "section_comparison.csv", 
            "CSV Files (*.csv);;JSON Files (*.json)"
        )
        
        if filename:
            try:
                if filename.endswith('.json'):
                    with open(filename, 'w') as f:
                        json.dump(self.sections_to_compare, f, indent=2)
                else:
                    # CSV export
                    import csv
                    with open(filename, 'w', newline='') as f:
                        writer = csv.writer(f)
                        
                        # Headers
                        headers = ['Section', 'Shape Type', 'Area (mm²)', 'Weight (kg/m)', 
                                 'Height (mm)', 'Width (mm)', 'Ix (mm⁴)', 'Iy (mm⁴)']
                        writer.writerow(headers)
                        
                        # Data
                        for section_data in self.sections_to_compare:
                            properties = section_data.get('properties', {})
                            row = [
                                section_data.get('name', ''),
                                section_data.get('shape_name', ''),
                                properties.get('area', 0),
                                properties.get('weight', 0),
                                properties.get('height', 0),
                                properties.get('width', 0),
                                properties.get('ix', 0),
                                properties.get('iy', 0)
                            ]
                            writer.writerow(row)
                
                QMessageBox.information(self, "Success", f"Comparison exported to {filename}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export: {str(e)}")

class SteelProfileSelector(QMainWindow):
    """Main steel profile selector interface"""
    
    sectionSelected = Signal(dict)  # Emitted when section is selected
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize data
        self.current_sections = []
        self.current_shape_type = None
        
        # Initialize UI
        self.init_ui()
        
        # Load initial data
        self.load_shape_types()
    
    def init_ui(self):
        """Initialize user interface"""
        self.setWindowTitle("Steel Profile Selector - StructureTools")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Left panel - Selection and filters
        left_panel = self.create_selection_panel()
        main_layout.addWidget(left_panel, 2)
        
        # Right panel - Details and comparison
        right_panel = self.create_details_panel()
        main_layout.addWidget(right_panel, 1)
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.update_status()
    
    def create_selection_panel(self):
        """Create selection panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Shape type selection
        shape_group = QGroupBox("Shape Type")
        shape_layout = QVBoxLayout(shape_group)
        
        self.shape_type_combo = QComboBox()
        self.shape_type_combo.currentTextChanged.connect(self.on_shape_type_changed)
        shape_layout.addWidget(self.shape_type_combo)
        layout.addWidget(shape_group)
        
        # Search and filters
        search_group = QGroupBox("Search & Filters")
        search_layout = QVBoxLayout(search_group)
        
        # Search box
        search_box_layout = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search sections (e.g., W12, HSS8x6)...")
        self.search_box.textChanged.connect(self.on_search_changed)
        
        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self.perform_search)
        
        search_box_layout.addWidget(self.search_box)
        search_box_layout.addWidget(self.search_btn)
        search_layout.addLayout(search_box_layout)
        
        # Property filters (collapsible)
        self.filter_widget = PropertyFilterWidget()
        self.filter_widget.filterChanged.connect(self.apply_property_filters)
        
        filter_collapsible = self.create_collapsible_widget("Advanced Filters", self.filter_widget)
        search_layout.addWidget(filter_collapsible)
        
        search_group.setLayout(search_layout)
        layout.addWidget(search_group)
        
        # Results table
        results_group = QGroupBox("Search Results")
        results_layout = QVBoxLayout(results_group)
        
        # Results info
        self.results_info = QLabel("Select a shape type to see available sections")
        results_layout.addWidget(self.results_info)
        
        # Table
        self.results_table = QTableView()
        self.results_model = SteelProfileModel()
        self.results_table.setModel(self.results_model)
        self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.results_table.selectionModel().currentRowChanged.connect(self.on_section_selected)
        self.results_table.doubleClicked.connect(self.on_section_double_clicked)
        results_layout.addWidget(self.results_table)
        
        results_group.setLayout(results_layout)
        layout.addWidget(results_group)
        
        return panel
    
    def create_details_panel(self):
        """Create details panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Section details
        details_group = QGroupBox("Section Details")
        details_layout = QVBoxLayout(details_group)
        
        self.details_text = QTextEdit()
        self.details_text.setMaximumHeight(250)
        self.details_text.setReadOnly(True)
        details_layout.addWidget(self.details_text)
        
        details_group.setLayout(details_layout)
        layout.addWidget(details_group)
        
        # Comparison widget
        self.comparison_widget = SectionComparisonWidget()
        layout.addWidget(self.comparison_widget)
        
        # Action buttons
        action_group = QGroupBox("Actions")
        action_layout = QVBoxLayout(action_group)
        
        self.select_btn = QPushButton("Select Section")
        self.select_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 8px; }")
        self.select_btn.clicked.connect(self.select_current_section)
        self.select_btn.setEnabled(False)
        
        self.add_compare_btn = QPushButton("Add to Comparison")
        self.add_compare_btn.clicked.connect(self.add_to_comparison)
        self.add_compare_btn.setEnabled(False)
        
        action_layout.addWidget(self.select_btn)
        action_layout.addWidget(self.add_compare_btn)
        action_group.setLayout(action_layout)
        layout.addWidget(action_group)
        
        return panel
    
    def create_collapsible_widget(self, title, widget):
        """Create collapsible widget"""
        collapsible = QGroupBox(title)
        collapsible.setCheckable(True)
        collapsible.setChecked(False)
        
        layout = QVBoxLayout(collapsible)
        layout.addWidget(widget)
        
        # Hide/show content based on checkbox
        collapsible.toggled.connect(widget.setVisible)
        widget.setVisible(False)
        
        return collapsible
    
    def load_shape_types(self):
        """Load available shape types"""
        self.shape_type_combo.clear()
        
        if not INTEGRATION_AVAILABLE or not STEELPY_AVAILABLE:
            self.shape_type_combo.addItem("steelpy not available")
            return
        
        try:
            shape_types = get_available_shape_types()
            
            for shape_key, shape_info in shape_types.items():
                display_text = f"{shape_info['name']} ({shape_info['count']} sections)"
                self.shape_type_combo.addItem(display_text, shape_key)
            
        except Exception as e:
            self.status_bar.showMessage(f"Error loading shape types: {e}")
    
    def on_shape_type_changed(self):
        """Handle shape type change"""
        shape_key = self.shape_type_combo.currentData()
        if not shape_key or shape_key == "steelpy not available":
            return
        
        self.current_shape_type = shape_key
        self.load_sections_for_shape(shape_key)
    
    def load_sections_for_shape(self, shape_key):
        """Load sections for selected shape type"""
        try:
            # Get all sections for this shape
            section_names = get_sections_for_shape(shape_key)
            
            # Convert to full section data
            sections_data = []
            shape_types = get_available_shape_types()
            shape_name = shape_types.get(shape_key, {}).get('name', shape_key)
            
            for section_name in section_names:
                properties = get_section_data(shape_key, section_name)
                if properties:
                    sections_data.append({
                        'name': section_name,
                        'shape_type': shape_key,
                        'shape_name': shape_name,
                        'properties': properties
                    })
            
            self.current_sections = sections_data
            self.results_model.set_sections_data(sections_data)
            
            # Update results info
            self.results_info.setText(f"Found {len(sections_data)} sections")
            
        except Exception as e:
            self.status_bar.showMessage(f"Error loading sections: {e}")
    
    def on_search_changed(self):
        """Handle search text change"""
        # Auto-search as user types (with delay)
        if hasattr(self, 'search_timer'):
            self.search_timer.stop()
        
        self.search_timer = QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.perform_search)
        self.search_timer.start(500)  # 500ms delay
    
    def perform_search(self):
        """Perform search based on current criteria"""
        search_text = self.search_box.text().strip()
        
        if not search_text:
            # Show all sections for current shape type
            if self.current_shape_type:
                self.load_sections_for_shape(self.current_shape_type)
            return
        
        try:
            # Search sections
            results = search_steel_sections(search_text, self.current_shape_type)
            
            self.current_sections = results
            self.results_model.set_sections_data(results)
            
            # Update results info
            self.results_info.setText(f"Search results: {len(results)} sections found")
            
        except Exception as e:
            self.status_bar.showMessage(f"Search error: {e}")
    
    def apply_property_filters(self):
        """Apply property-based filters"""
        filters = self.filter_widget.get_active_filters()
        
        if not filters:
            # No filters, show current sections
            if self.current_shape_type:
                self.load_sections_for_shape(self.current_shape_type)
            return
        
        try:
            # Apply filters
            results = filter_steel_sections(filters, self.current_shape_type)
            
            self.current_sections = results
            self.results_model.set_sections_data(results)
            
            # Update results info
            filter_count = len(filters)
            self.results_info.setText(f"Filtered results ({filter_count} filters): {len(results)} sections")
            
        except Exception as e:
            self.status_bar.showMessage(f"Filter error: {e}")
    
    def on_section_selected(self, current, previous):
        """Handle section selection"""
        if not current.isValid():
            self.select_btn.setEnabled(False)
            self.add_compare_btn.setEnabled(False)
            self.details_text.clear()
            return
        
        # Get section data
        section_data = self.results_model.data(current, Qt.UserRole)
        if not section_data:
            return
        
        # Enable buttons
        self.select_btn.setEnabled(True)
        self.add_compare_btn.setEnabled(True)
        
        # Update details
        self.update_section_details(section_data)
        
        # Store current selection
        self.current_selection = section_data
    
    def on_section_double_clicked(self, index):
        """Handle section double-click"""
        self.select_current_section()
    
    def update_section_details(self, section_data):
        """Update section details display"""
        properties = section_data.get('properties', {})
        
        details = f"Section: {section_data.get('name', 'Unknown')}\n"
        details += f"Type: {section_data.get('shape_name', 'Unknown')}\n"
        details += f"Standard: {properties.get('standard', 'AISC')}\n"
        details += f"Source: {properties.get('source', 'steelpy')}\n\n"
        
        details += "Geometric Properties:\n"
        if 'area' in properties:
            details += f"  Cross-sectional Area: {properties['area']:,.0f} mm²\n"
        if 'weight' in properties:
            details += f"  Weight: {properties['weight']:.2f} kg/m\n"
        if 'height' in properties:
            details += f"  Height: {properties['height']:.1f} mm\n"
        if 'width' in properties:
            details += f"  Width: {properties['width']:.1f} mm\n"
        if 'web_thickness' in properties:
            details += f"  Web Thickness: {properties['web_thickness']:.1f} mm\n"
        if 'flange_thickness' in properties:
            details += f"  Flange Thickness: {properties['flange_thickness']:.1f} mm\n"
        
        details += "\nSection Properties:\n"
        if 'ix' in properties:
            details += f"  Moment of Inertia Ix: {properties['ix']:,.0f} mm⁴\n"
        if 'iy' in properties:
            details += f"  Moment of Inertia Iy: {properties['iy']:,.0f} mm⁴\n"
        if 'sx' in properties:
            details += f"  Section Modulus Sx: {properties['sx']:,.0f} mm³\n"
        if 'sy' in properties:
            details += f"  Section Modulus Sy: {properties['sy']:,.0f} mm³\n"
        if 'zx' in properties:
            details += f"  Plastic Modulus Zx: {properties['zx']:,.0f} mm³\n"
        if 'zy' in properties:
            details += f"  Plastic Modulus Zy: {properties['zy']:,.0f} mm³\n"
        if 'rx' in properties:
            details += f"  Radius of Gyration rx: {properties['rx']:.1f} mm\n"
        if 'ry' in properties:
            details += f"  Radius of Gyration ry: {properties['ry']:.1f} mm\n"
        if 'j' in properties:
            details += f"  Torsional Constant J: {properties['j']:,.0f} mm⁴\n"
        
        self.details_text.setText(details)
    
    def select_current_section(self):
        """Select current section and emit signal"""
        if hasattr(self, 'current_selection'):
            self.sectionSelected.emit(self.current_selection)
            self.status_bar.showMessage(f"Selected: {self.current_selection['name']}")
    
    def add_to_comparison(self):
        """Add current section to comparison"""
        if hasattr(self, 'current_selection'):
            self.comparison_widget.add_section(self.current_selection)
            self.status_bar.showMessage(f"Added {self.current_selection['name']} to comparison")
    
    def update_status(self):
        """Update status bar"""
        if not INTEGRATION_AVAILABLE:
            self.status_bar.showMessage("steelpy integration not available")
        elif not STEELPY_AVAILABLE:
            self.status_bar.showMessage("steelpy not installed - pip install steelpy")
        else:
            try:
                manager = get_steelpy_manager()
                stats = manager.get_statistics()
                total = stats.get('total_sections', 0)
                types = stats.get('shape_types', 0)
                self.status_bar.showMessage(f"steelpy database: {total} sections in {types} shape types")
            except:
                self.status_bar.showMessage("steelpy database loaded")

# Standalone function to show selector
def show_steel_profile_selector(parent=None):
    """Show steel profile selector dialog"""
    if not GUI_AVAILABLE:
        print("GUI not available")
        return None
    
    selector = SteelProfileSelector(parent)
    selector.show()
    return selector

# Export main classes
__all__ = [
    'SteelProfileSelector',
    'SteelProfileModel', 
    'PropertyFilterWidget',
    'SectionComparisonWidget',
    'show_steel_profile_selector'
]