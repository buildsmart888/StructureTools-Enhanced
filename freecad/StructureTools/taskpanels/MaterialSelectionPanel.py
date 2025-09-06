# -*- coding: utf-8 -*-
"""
Material Selection Task Panel for StructureTools

Provides a professional interface for selecting materials from standard databases
including ASTM, EN, ACI, JIS and other international standards.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtWidgets, QtGui
import os

try:
    from ..data.MaterialDatabase import MaterialDatabase
except ImportError:
    # Fallback for testing
    class MaterialDatabase:
        @staticmethod
        def get_all_materials():
            return {"Steel": {"ASTM A36": {"name": "Test Material"}}}

# Import Thai units converter and global units manager
try:
    from ..utils.universal_thai_units import UniversalThaiUnits
    from ..utils.units_manager import get_units_manager, format_stress, format_modulus
    THAI_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    UniversalThaiUnits = None
    get_units_manager = lambda: None
    format_stress = lambda x, y=None: f"{x:.0f} MPa"
    format_modulus = lambda x, y=None: f"{x/1000:.0f} GPa"


class MaterialSelectionPanel:
    """Professional material selection panel with database integration"""
    
    def __init__(self, material_object=None):
        """
        Initialize material selection panel
        
        Args:
            material_object: Existing Material object to edit, or None for new
        """
        self.material_object = material_object
        self.selected_material_data = None
        self.all_materials = MaterialDatabase.get_all_materials()
        
        # Initialize units manager and Thai converter
        self.units_manager = get_units_manager()
        self.thai_converter = UniversalThaiUnits() if THAI_UNITS_AVAILABLE else None
        
        self.form = self.createUI()
        
        # Initialize the interface
        self.populate_categories()
        
        # If editing existing material, populate from object
        if material_object:
            self.populate_from_object()
    
    def format_strength_with_thai_units(self, mpa_value, is_concrete=False):
        """Format strength values according to global units settings"""
        if not mpa_value or mpa_value == 0:
            return "N/A"
        
        material_type = "concrete" if is_concrete else "steel"
        if self.units_manager:
            return format_stress(mpa_value, material_type)
        else:
            return f"{mpa_value:.0f} MPa"
    
    def format_modulus_with_thai_units(self, mpa_value, is_concrete=False):
        """Format elastic modulus according to global units settings"""
        if not mpa_value or mpa_value == 0:
            return "N/A"
        
        material_type = "concrete" if is_concrete else "steel"
        if self.units_manager:
            return format_modulus(mpa_value, material_type)
        else:
            gpa_value = mpa_value / 1000.0
            return f"{gpa_value:.0f} GPa"
    
    def createUI(self):
        """Create the user interface"""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title_label = QtWidgets.QLabel("Material Selection")
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; margin-bottom: 10px;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Add units selector
        if self.units_manager and hasattr(self.units_manager, 'create_units_selector_widget'):
            units_widget = self.units_manager.create_units_selector_widget()
            if units_widget:
                layout.addWidget(units_widget)
        
        # Create tab widget for different selection methods
        self.tab_widget = QtWidgets.QTabWidget()
        
        # Standard Materials tab
        self.standard_tab = self.create_standard_materials_tab()
        self.tab_widget.addTab(self.standard_tab, "Standard Materials")
        
        # Custom Material tab
        self.custom_tab = self.create_custom_material_tab()
        self.tab_widget.addTab(self.custom_tab, "Custom Material")
        
        # Search tab
        self.search_tab = self.create_search_tab()
        self.tab_widget.addTab(self.search_tab, "Search")
        
        layout.addWidget(self.tab_widget)
        
        # Material properties preview
        self.properties_group = self.create_properties_preview()
        layout.addWidget(self.properties_group)
        
        # Status bar
        self.status_label = QtWidgets.QLabel("Select a material from the database or enter custom values")
        self.status_label.setStyleSheet("color: blue; font-style: italic; margin-top: 10px;")
        layout.addWidget(self.status_label)
        
        return widget
    
    def create_standard_materials_tab(self):
        """Create standard materials selection tab"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Category selection
        category_layout = QtWidgets.QHBoxLayout()
        category_layout.addWidget(QtWidgets.QLabel("Category:"))
        
        self.category_combo = QtWidgets.QComboBox()
        self.category_combo.currentTextChanged.connect(self.on_category_changed)
        category_layout.addWidget(self.category_combo)
        
        category_layout.addStretch()
        layout.addLayout(category_layout)
        
        # Material list
        list_layout = QtWidgets.QHBoxLayout()
        
        # Left side - Material list
        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(QtWidgets.QLabel("Available Materials:"))
        
        self.material_list = QtWidgets.QListWidget()
        self.material_list.currentItemChanged.connect(self.on_material_selected)
        left_layout.addWidget(self.material_list)
        
        list_layout.addLayout(left_layout)
        
        # Right side - Material details
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(QtWidgets.QLabel("Material Details:"))
        
        self.details_text = QtWidgets.QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setMaximumHeight(200)
        right_layout.addWidget(self.details_text)
        
        # Quick filter buttons
        filter_layout = QtWidgets.QGridLayout()
        
        self.astm_btn = QtWidgets.QPushButton("ASTM Standards")
        self.astm_btn.clicked.connect(lambda: self.filter_by_standard("ASTM"))
        filter_layout.addWidget(self.astm_btn, 0, 0)
        
        self.en_btn = QtWidgets.QPushButton("EN Standards")
        self.en_btn.clicked.connect(lambda: self.filter_by_standard("EN"))
        filter_layout.addWidget(self.en_btn, 0, 1)
        
        self.aci_btn = QtWidgets.QPushButton("ACI Standards")
        self.aci_btn.clicked.connect(lambda: self.filter_by_standard("ACI"))
        filter_layout.addWidget(self.aci_btn, 1, 0)
        
        self.jis_btn = QtWidgets.QPushButton("JIS Standards")
        self.jis_btn.clicked.connect(lambda: self.filter_by_standard("JIS"))
        filter_layout.addWidget(self.jis_btn, 1, 1)
        
        right_layout.addLayout(filter_layout)
        
        list_layout.addLayout(right_layout)
        layout.addLayout(list_layout)
        
        return tab
    
    def create_custom_material_tab(self):
        """Create custom material input tab"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Basic properties group
        basic_group = QtWidgets.QGroupBox("Basic Properties")
        basic_layout = QtWidgets.QFormLayout(basic_group)
        
        self.name_input = QtWidgets.QLineEdit()
        self.name_input.setPlaceholderText("Enter material name")
        basic_layout.addRow("Material Name:", self.name_input)
        
        self.type_combo = QtWidgets.QComboBox()
        self.type_combo.addItems([
            "Carbon Steel", "Stainless Steel", "High Strength Steel",
            "Normal Weight Concrete", "High Strength Concrete", "Lightweight Concrete",
            "Aluminum Alloy", "Structural Timber", "Masonry", "Other"
        ])
        basic_layout.addRow("Material Type:", self.type_combo)
        
        self.standard_input = QtWidgets.QLineEdit()
        self.standard_input.setPlaceholderText("e.g., ASTM A36, EN 10025, ACI 318")
        basic_layout.addRow("Standard:", self.standard_input)
        
        layout.addWidget(basic_group)
        
        # Mechanical properties group
        mechanical_group = QtWidgets.QGroupBox("Mechanical Properties")
        mechanical_layout = QtWidgets.QFormLayout(mechanical_group)
        
        # Elastic modulus
        modulus_layout = QtWidgets.QHBoxLayout()
        self.modulus_input = QtWidgets.QDoubleSpinBox()
        self.modulus_input.setRange(1.0, 500000.0)
        self.modulus_input.setValue(200000.0)
        self.modulus_input.setDecimals(0)
        if self.units_manager:
            suffix = self.units_manager.get_units_suffix("modulus")
            self.modulus_input.setSuffix(suffix)
            self.modulus_input.setToolTip("Elastic Modulus\nUnits adapt to current selection")
        else:
            self.modulus_input.setSuffix(" MPa")
        modulus_layout.addWidget(self.modulus_input)
        
        # Common values buttons with dynamic units
        if self.units_manager and self.units_manager.is_thai_units():
            recommendations = self.units_manager.get_material_recommendations()
            steel_mod_val, steel_unit = recommendations["steel_modulus"]
            concrete_mod_val, concrete_unit = recommendations["concrete_modulus"]
            
            self.steel_modulus_btn = QtWidgets.QPushButton(f"Steel ({steel_mod_val/1000:.0f}k {steel_unit})")
            self.steel_modulus_btn.clicked.connect(lambda: self.modulus_input.setValue(steel_mod_val))
            
            self.concrete_modulus_btn = QtWidgets.QPushButton(f"Concrete ({concrete_mod_val/1000:.0f}k {concrete_unit})")
            self.concrete_modulus_btn.clicked.connect(lambda: self.concrete_modulus_btn.setValue(concrete_mod_val))
        else:
            self.steel_modulus_btn = QtWidgets.QPushButton("Steel (200 GPa)")
            self.steel_modulus_btn.clicked.connect(lambda: self.modulus_input.setValue(200000))
            
            self.concrete_modulus_btn = QtWidgets.QPushButton("Concrete (30 GPa)")
            self.concrete_modulus_btn.clicked.connect(lambda: self.modulus_input.setValue(30000))
        
        modulus_layout.addWidget(self.steel_modulus_btn)
        modulus_layout.addWidget(self.concrete_modulus_btn)
        
        mechanical_layout.addRow("Elastic Modulus:", modulus_layout)
        
        # Poisson's ratio
        self.poisson_input = QtWidgets.QDoubleSpinBox()
        self.poisson_input.setRange(0.0, 0.5)
        self.poisson_input.setValue(0.30)
        self.poisson_input.setDecimals(2)
        mechanical_layout.addRow("Poisson's Ratio:", self.poisson_input)
        
        # Density
        density_layout = QtWidgets.QHBoxLayout()
        self.density_input = QtWidgets.QDoubleSpinBox()
        self.density_input.setRange(100.0, 20000.0)
        self.density_input.setValue(7850.0)
        self.density_input.setDecimals(0)
        self.density_input.setSuffix(" kg/m³")
        density_layout.addWidget(self.density_input)
        
        # Common density buttons
        self.steel_density_btn = QtWidgets.QPushButton("Steel (7850)")
        self.steel_density_btn.clicked.connect(lambda: self.density_input.setValue(7850))
        density_layout.addWidget(self.steel_density_btn)
        
        self.concrete_density_btn = QtWidgets.QPushButton("Concrete (2400)")
        self.concrete_density_btn.clicked.connect(lambda: self.density_input.setValue(2400))
        density_layout.addWidget(self.concrete_density_btn)
        
        mechanical_layout.addRow("Density:", density_layout)
        
        layout.addWidget(mechanical_group)
        
        # Strength properties group
        strength_group = QtWidgets.QGroupBox("Strength Properties - กำลังวัสดุ (Optional)")
        strength_layout = QtWidgets.QFormLayout(strength_group)
        
        # Yield strength
        yield_layout = QtWidgets.QHBoxLayout()
        self.yield_strength_input = QtWidgets.QDoubleSpinBox()
        self.yield_strength_input.setRange(0.0, 10000.0)  # Increased range for Thai units
        
        # Set default value based on current units
        if self.units_manager and self.units_manager.is_thai_units():
            recommendations = self.units_manager.get_material_recommendations()
            default_val, unit = recommendations["steel_yield_sd40"]
            self.yield_strength_input.setValue(default_val)
            suffix = self.units_manager.get_units_suffix("stress")
            tooltip = "Yield Strength in ksc\nThai: จุดครากเอี้ยว"
        else:
            self.yield_strength_input.setValue(250.0)
            suffix = " MPa"
            tooltip = "Yield Strength in MPa"
        
        self.yield_strength_input.setSuffix(suffix)
        self.yield_strength_input.setToolTip(tooltip)
        yield_layout.addWidget(self.yield_strength_input)
        
        # Live conversion label
        if self.units_manager and self.units_manager.show_both_units():
            self.yield_thai_label = QtWidgets.QLabel()
            self.yield_thai_label.setStyleSheet("color: #007700; font-weight: bold;")
            self.yield_strength_input.valueChanged.connect(self.update_yield_thai_label)
            yield_layout.addWidget(self.yield_thai_label)
            # Initialize label
            self.update_yield_thai_label(self.yield_strength_input.value())
        
        strength_layout.addRow("Yield Strength:", yield_layout)
        
        # Ultimate strength
        ultimate_layout = QtWidgets.QHBoxLayout()
        self.ultimate_strength_input = QtWidgets.QDoubleSpinBox()
        self.ultimate_strength_input.setRange(0.0, 10000.0)  # Increased range for Thai units
        
        # Set default value based on current units
        if self.units_manager and self.units_manager.is_thai_units():
            recommendations = self.units_manager.get_material_recommendations()
            default_val = recommendations["steel_yield_sd40"][0] * 1.6  # ~Ultimate = 1.6 * Yield
            self.ultimate_strength_input.setValue(default_val)
            suffix = self.units_manager.get_units_suffix("stress")
            tooltip = "Ultimate Strength in ksc\nThai: กำลังแรงดึงสูงสุด"
        else:
            self.ultimate_strength_input.setValue(400.0)
            suffix = " MPa"
            tooltip = "Ultimate Strength in MPa"
        
        self.ultimate_strength_input.setSuffix(suffix)
        self.ultimate_strength_input.setToolTip(tooltip)
        ultimate_layout.addWidget(self.ultimate_strength_input)
        
        # Live conversion label
        if self.units_manager and self.units_manager.show_both_units():
            self.ultimate_thai_label = QtWidgets.QLabel()
            self.ultimate_thai_label.setStyleSheet("color: #007700; font-weight: bold;")
            self.ultimate_strength_input.valueChanged.connect(self.update_ultimate_thai_label)
            ultimate_layout.addWidget(self.ultimate_thai_label)
            # Initialize label
            self.update_ultimate_thai_label(self.ultimate_strength_input.value())
        
        strength_layout.addRow("Ultimate Strength:", ultimate_layout)
        
        layout.addWidget(strength_group)
        
        # Thermal properties group
        thermal_group = QtWidgets.QGroupBox("Thermal Properties (Optional)")
        thermal_layout = QtWidgets.QFormLayout(thermal_group)
        
        self.thermal_expansion_input = QtWidgets.QDoubleSpinBox()
        self.thermal_expansion_input.setRange(0.0, 50.0)
        self.thermal_expansion_input.setValue(12.0)
        self.thermal_expansion_input.setDecimals(1)
        self.thermal_expansion_input.setSuffix(" × 10⁻⁶ /°C")
        thermal_layout.addRow("Thermal Expansion:", self.thermal_expansion_input)
        
        layout.addWidget(thermal_group)
        
        # Connect signals for live updates of custom material preview
        self.name_input.textChanged.connect(self.update_custom_preview)
        self.type_combo.currentTextChanged.connect(self.update_custom_preview)
        self.standard_input.textChanged.connect(self.update_custom_preview)
        self.modulus_input.valueChanged.connect(self.update_custom_preview)
        self.poisson_input.valueChanged.connect(self.update_custom_preview)
        self.density_input.valueChanged.connect(self.update_custom_preview)
        self.yield_strength_input.valueChanged.connect(self.update_custom_preview)
        self.ultimate_strength_input.valueChanged.connect(self.update_custom_preview)
        self.thermal_expansion_input.valueChanged.connect(self.update_custom_preview)
        
        # Initialize Thai labels with default values
        if THAI_UNITS_AVAILABLE:
            self.update_yield_thai_label(self.yield_strength_input.value())
            self.update_ultimate_thai_label(self.ultimate_strength_input.value())
        
        return tab
    
    def create_search_tab(self):
        """Create material search tab"""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(tab)
        
        # Search input
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(QtWidgets.QLabel("Search:"))
        
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText("Enter material name, standard, or property...")
        self.search_input.textChanged.connect(self.perform_search)
        search_layout.addWidget(self.search_input)
        
        self.search_btn = QtWidgets.QPushButton("Search")
        self.search_btn.clicked.connect(self.perform_search)
        search_layout.addWidget(self.search_btn)
        
        layout.addLayout(search_layout)
        
        # Search filters
        filter_group = QtWidgets.QGroupBox("Search Filters")
        filter_layout = QtWidgets.QGridLayout(filter_group)
        
        self.search_name_check = QtWidgets.QCheckBox("Material Name")
        self.search_name_check.setChecked(True)
        filter_layout.addWidget(self.search_name_check, 0, 0)
        
        self.search_standard_check = QtWidgets.QCheckBox("Standard")
        self.search_standard_check.setChecked(True)
        filter_layout.addWidget(self.search_standard_check, 0, 1)
        
        self.search_type_check = QtWidgets.QCheckBox("Material Type")
        self.search_type_check.setChecked(True)
        filter_layout.addWidget(self.search_type_check, 1, 0)
        
        self.search_description_check = QtWidgets.QCheckBox("Description")
        self.search_description_check.setChecked(False)
        filter_layout.addWidget(self.search_description_check, 1, 1)
        
        layout.addWidget(filter_group)
        
        # Search results
        layout.addWidget(QtWidgets.QLabel("Search Results:"))
        
        self.search_results = QtWidgets.QTreeWidget()
        self.search_results.setHeaderLabels(["Category", "Material Name", "Standard", "Type"])
        self.search_results.currentItemChanged.connect(self.on_search_result_selected)
        layout.addWidget(self.search_results)
        
        return tab
    
    def create_properties_preview(self):
        """Create material properties preview group"""
        group = QtWidgets.QGroupBox("Selected Material Properties")
        layout = QtWidgets.QFormLayout(group)
        
        # Read-only property displays
        self.preview_name = QtWidgets.QLineEdit()
        self.preview_name.setReadOnly(True)
        layout.addRow("Name:", self.preview_name)
        
        self.preview_standard = QtWidgets.QLineEdit()
        self.preview_standard.setReadOnly(True)
        layout.addRow("Standard:", self.preview_standard)
        
        self.preview_type = QtWidgets.QLineEdit()
        self.preview_type.setReadOnly(True)
        layout.addRow("Type:", self.preview_type)
        
        self.preview_modulus = QtWidgets.QLineEdit()
        self.preview_modulus.setReadOnly(True)
        layout.addRow("Elastic Modulus:", self.preview_modulus)
        
        self.preview_poisson = QtWidgets.QLineEdit()
        self.preview_poisson.setReadOnly(True)
        layout.addRow("Poisson's Ratio:", self.preview_poisson)
        
        self.preview_density = QtWidgets.QLineEdit()
        self.preview_density.setReadOnly(True)
        layout.addRow("Density:", self.preview_density)
        
        # Apply button
        self.apply_btn = QtWidgets.QPushButton("Apply Selected Material")
        self.apply_btn.setStyleSheet("font-weight: bold; background-color: #4CAF50; color: white; padding: 8px;")
        self.apply_btn.clicked.connect(self.apply_material)
        self.apply_btn.setEnabled(False)
        layout.addRow(self.apply_btn)
        
        return group
    
    def populate_categories(self):
        """Populate the category combo box"""
        categories = list(self.all_materials.keys())
        self.category_combo.clear()
        self.category_combo.addItems(categories)
    
    def on_category_changed(self, category):
        """Handle category selection change"""
        if not category or category not in self.all_materials:
            return
        
        self.material_list.clear()
        materials = self.all_materials[category]
        
        for material_name in sorted(materials.keys()):
            item = QtWidgets.QListWidgetItem(material_name)
            item.setData(QtCore.Qt.UserRole, materials[material_name])
            self.material_list.addItem(item)
        
        self.status_label.setText(f"Showing {len(materials)} materials in {category} category")
    
    def on_material_selected(self, current, previous):
        """Handle material selection from list"""
        if not current:
            return
        
        material_data = current.data(QtCore.Qt.UserRole)
        if not material_data:
            return
        
        self.selected_material_data = material_data
        self.update_material_details(material_data)
        self.update_properties_preview(material_data)
        self.apply_btn.setEnabled(True)
        
        self.status_label.setText(f"Selected: {material_data['name']}")
    
    def update_material_details(self, material_data):
        """Update the material details text"""
        # Determine if material is concrete based on type/name
        is_concrete = any(term in material_data.get('type', '').lower() + material_data.get('name', '').lower() 
                         for term in ['concrete', 'คอนกรีต', 'fc'])
        
        # Format modulus with Thai units
        modulus_mpa = material_data.get('modulus_elasticity', 0)
        modulus_text = self.format_modulus_with_thai_units(modulus_mpa, is_concrete)
        
        # Format yield strength with Thai units
        yield_strength = material_data.get('yield_strength')
        if yield_strength and str(yield_strength).replace('.', '').isdigit():
            yield_text = self.format_strength_with_thai_units(float(yield_strength), is_concrete)
        else:
            yield_text = str(yield_strength) if yield_strength else 'N/A'
        
        # Format ultimate strength with Thai units
        ultimate_strength = material_data.get('ultimate_strength')
        if ultimate_strength and str(ultimate_strength).replace('.', '').isdigit():
            ultimate_text = self.format_strength_with_thai_units(float(ultimate_strength), is_concrete)
        else:
            ultimate_text = str(ultimate_strength) if ultimate_strength else 'N/A'
        
        details = f"""
<b>{material_data['name']}</b>

<b>Standard:</b> {material_data.get('standard', 'Not specified')}
<b>Type:</b> {material_data.get('type', 'Not specified')}

<b>Mechanical Properties:</b>
• Elastic Modulus: {modulus_text}
• Poisson's Ratio: {material_data.get('poisson_ratio', 0):.2f}  
• Density: {material_data.get('density', 0):,.0f} kg/m³

<b>Strength Properties (🇹🇭 Thai Units):</b>
• Yield Strength: {yield_text}
• Ultimate Strength: {ultimate_text}

<b>Thermal Properties:</b>
• Thermal Expansion: {material_data.get('thermal_expansion', 'N/A')} × 10⁻⁶ /°C

<b>Description:</b>
{material_data.get('description', 'No description available')}
        """.strip()
        
        self.details_text.setHtml(details)
    
    def update_properties_preview(self, material_data):
        """Update the properties preview section"""
        # Determine if material is concrete
        is_concrete = any(term in material_data.get('type', '').lower() + material_data.get('name', '').lower() 
                         for term in ['concrete', 'คอนกรีต', 'fc'])
        
        self.preview_name.setText(material_data.get('name', ''))
        self.preview_standard.setText(material_data.get('standard', ''))
        self.preview_type.setText(material_data.get('type', ''))
        
        # Format modulus with Thai units
        modulus_mpa = material_data.get('modulus_elasticity', 0)
        modulus_text = self.format_modulus_with_thai_units(modulus_mpa, is_concrete)
        self.preview_modulus.setText(modulus_text)
        
        self.preview_poisson.setText(f"{material_data.get('poisson_ratio', 0):.3f}")
        self.preview_density.setText(f"{material_data.get('density', 0):,.0f} kg/m³")
    
    def update_yield_thai_label(self, value):
        """Update Thai units label for yield strength"""
        if hasattr(self, 'yield_thai_label') and self.units_manager:
            if self.units_manager.is_thai_units():
                # Input is in ksc, show MPa equivalent
                mpa_value = self.units_manager.convert_input_to_si(value, "stress")
                self.yield_thai_label.setText(f"= {mpa_value:.1f} MPa")
            else:
                # Input is in MPa, show ksc equivalent  
                ksc_value = self.thai_converter.mpa_to_ksc(value) if self.thai_converter else 0
                self.yield_thai_label.setText(f"= {ksc_value:.0f} ksc")
    
    def update_ultimate_thai_label(self, value):
        """Update Thai units label for ultimate strength"""
        if hasattr(self, 'ultimate_thai_label') and self.units_manager:
            if self.units_manager.is_thai_units():
                # Input is in ksc, show MPa equivalent
                mpa_value = self.units_manager.convert_input_to_si(value, "stress")
                self.ultimate_thai_label.setText(f"= {mpa_value:.1f} MPa")
            else:
                # Input is in MPa, show ksc equivalent
                ksc_value = self.thai_converter.mpa_to_ksc(value) if self.thai_converter else 0
                self.ultimate_thai_label.setText(f"= {ksc_value:.0f} ksc")
    
    def filter_by_standard(self, standard):
        """Filter materials by standard"""
        results = MaterialDatabase.search_materials_by_standard(standard)
        
        # Clear and repopulate the list
        self.material_list.clear()
        
        for category, materials in results.items():
            for material_name, material_data in materials.items():
                item = QtWidgets.QListWidgetItem(f"[{category}] {material_name}")
                item.setData(QtCore.Qt.UserRole, material_data)
                self.material_list.addItem(item)
        
        total_found = sum(len(materials) for materials in results.values())
        self.status_label.setText(f"Found {total_found} materials matching {standard} standard")
    
    def perform_search(self):
        """Perform material search"""
        search_text = self.search_input.text().strip().lower()
        if not search_text:
            self.search_results.clear()
            return
        
        self.search_results.clear()
        
        for category, materials in self.all_materials.items():
            category_item = None
            
            for material_name, material_data in materials.items():
                # Check search criteria
                matches = False
                
                if self.search_name_check.isChecked():
                    if search_text in material_name.lower() or search_text in material_data.get('name', '').lower():
                        matches = True
                
                if self.search_standard_check.isChecked():
                    if search_text in material_data.get('standard', '').lower():
                        matches = True
                
                if self.search_type_check.isChecked():
                    if search_text in material_data.get('type', '').lower():
                        matches = True
                
                if self.search_description_check.isChecked():
                    if search_text in material_data.get('description', '').lower():
                        matches = True
                
                if matches:
                    if not category_item:
                        category_item = QtWidgets.QTreeWidgetItem([category, "", "", ""])
                        category_item.setExpanded(True)
                        self.search_results.addTopLevelItem(category_item)
                    
                    material_item = QtWidgets.QTreeWidgetItem([
                        "",
                        material_data.get('name', material_name),
                        material_data.get('standard', ''),
                        material_data.get('type', '')
                    ])
                    material_item.setData(0, QtCore.Qt.UserRole, material_data)
                    category_item.addChild(material_item)
        
        # Count results
        total_results = 0
        for i in range(self.search_results.topLevelItemCount()):
            total_results += self.search_results.topLevelItem(i).childCount()
        
        self.status_label.setText(f"Search found {total_results} matching materials")
    
    def on_search_result_selected(self, current, previous):
        """Handle search result selection"""
        if not current or not current.parent():  # Skip category items
            return
        
        material_data = current.data(0, QtCore.Qt.UserRole)
        if material_data:
            self.selected_material_data = material_data
            self.update_properties_preview(material_data)
            self.apply_btn.setEnabled(True)
    
    def populate_from_object(self):
        """Populate interface from existing material object"""
        if not self.material_object:
            return
        
        try:
            # Switch to custom tab and populate values
            self.tab_widget.setCurrentIndex(1)  # Custom material tab
            
            # Try to get properties from object
            if hasattr(self.material_object, 'Label'):
                self.name_input.setText(self.material_object.Label)
            
            if hasattr(self.material_object, 'ModulusElasticity'):
                modulus_val = float(str(self.material_object.ModulusElasticity).split()[0])
                self.modulus_input.setValue(modulus_val)
            
            if hasattr(self.material_object, 'PoissonRatio'):
                self.poisson_input.setValue(float(self.material_object.PoissonRatio))
            
            if hasattr(self.material_object, 'Density'):
                density_val = float(str(self.material_object.Density).split()[0])
                self.density_input.setValue(density_val)
            
            # Update preview
            self.update_custom_preview()
            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Warning populating from object: {e}\n")
    
    def update_custom_preview(self):
        """Update preview from custom inputs"""
        custom_data = {
            'name': self.name_input.text() or "Custom Material",
            'standard': self.standard_input.text() or "Custom",
            'type': self.type_combo.currentText(),
            'modulus_elasticity': self.modulus_input.value(),
            'poisson_ratio': self.poisson_input.value(),
            'density': self.density_input.value(),
            'yield_strength': self.yield_strength_input.value() if self.yield_strength_input.value() > 0 else None,
            'ultimate_strength': self.ultimate_strength_input.value() if self.ultimate_strength_input.value() > 0 else None
        }
        
        self.selected_material_data = custom_data
        self.update_properties_preview(custom_data)
        self.apply_btn.setEnabled(True)
    
    def apply_material(self):
        """Apply the selected material properties"""
        if not self.selected_material_data:
            return
        
        # If editing existing material, update it
        if self.material_object:
            self.update_existing_material()
        else:
            self.create_new_material()
    
    def update_existing_material(self):
        """Update existing material object"""
        try:
            obj = self.material_object
            data = self.selected_material_data
            
            # Update label
            obj.Label = data.get('name', 'Material')
            
            # Check if this is a StructuralMaterial object
            if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type') and obj.Proxy.Type == "StructuralMaterial":
                # For StructuralMaterial objects, set the standard if possible
                standard_name = self.find_matching_standard(data)
                if standard_name and hasattr(obj, 'MaterialStandard'):
                    obj.MaterialStandard = standard_name
                    # The _update_standard_properties method will be called automatically
                else:
                    # Set custom properties
                    modulus_mpa = data.get('modulus_elasticity', 200000)
                    obj.ModulusElasticity = f"{modulus_mpa} MPa"
                    
                    obj.PoissonRatio = data.get('poisson_ratio', 0.30)
                    
                    density_kg_m3 = data.get('density', 7850)
                    obj.Density = f"{density_kg_m3} kg/m^3"
                    
                    # Determine material type based on data
                    material_type = "Steel"  # Default
                    if any(term in data.get('type', '').lower() + data.get('name', '').lower() 
                          for term in ['concrete', 'คอนกรีต', 'fc']):
                        material_type = "Concrete"
                    
                    if hasattr(obj, 'MaterialType'):
                        obj.MaterialType = material_type
                    
                    if 'yield_strength' in data and data['yield_strength']:
                        obj.YieldStrength = f"{data['yield_strength']} MPa"
                    
                    if 'ultimate_strength' in data and data['ultimate_strength']:
                        obj.UltimateStrength = f"{data['ultimate_strength']} MPa"
            else:
                # For basic Material objects or other types
                # Update properties
                modulus_mpa = data.get('modulus_elasticity', 200000)
                obj.ModulusElasticity = f"{modulus_mpa} MPa"
                
                obj.PoissonRatio = data.get('poisson_ratio', 0.30)
                
                density_kg_m3 = data.get('density', 7850)
                obj.Density = f"{density_kg_m3} kg/m^3"
                
                # Add additional properties if they exist
                if hasattr(obj, 'MaterialType'):
                    material_type = "Steel"  # Default
                    if any(term in data.get('type', '').lower() + data.get('name', '').lower() 
                          for term in ['concrete', 'คอนกรีต', 'fc']):
                        material_type = "Concrete"
                    obj.MaterialType = material_type
                else:
                    material_type = "Steel"  # Default
                    if any(term in data.get('type', '').lower() + data.get('name', '').lower() 
                          for term in ['concrete', 'คอนกรีต', 'fc']):
                        material_type = "Concrete"
                    obj.addProperty("App::PropertyString", "MaterialType", "Material", "Material classification")
                    obj.MaterialType = material_type
                
                if hasattr(obj, 'Standard'):
                    obj.Standard = data.get('standard', 'Custom')
                else:
                    obj.addProperty("App::PropertyString", "Standard", "Material", "Material standard")
                    obj.Standard = data.get('standard', 'Custom')
                
                # Add strength properties if available
                if 'yield_strength' in data and data['yield_strength']:
                    if not hasattr(obj, 'YieldStrength'):
                        obj.addProperty("App::PropertyPressure", "YieldStrength", "Strength", "Yield strength")
                    obj.YieldStrength = f"{data['yield_strength']} MPa"
                
                if 'ultimate_strength' in data and data['ultimate_strength']:
                    if not hasattr(obj, 'UltimateStrength'):
                        obj.addProperty("App::PropertyPressure", "UltimateStrength", "Strength", "Ultimate strength")
                    obj.UltimateStrength = f"{data['ultimate_strength']} MPa"
            
            obj.recompute()
            App.ActiveDocument.recompute()
            
            App.Console.PrintMessage(f"Material '{obj.Label}' updated successfully.\n")
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error updating material: {str(e)}\n")

    def find_matching_standard(self, data):
        """Find matching database standard for material data"""
        if not HAS_DATABASE:
            return None
        
        # Try to match by name patterns
        name_lower = data.get('name', '').lower()
        type_lower = data.get('type', '').lower()
        standard_lower = data.get('standard', '').lower()
        
        # Check for concrete materials
        concrete_keywords = ['concrete', 'คอนกรีต', 'fc', 'aci_normal', 'en_c']
        for keyword in concrete_keywords:
            if keyword in name_lower or keyword in type_lower or keyword in standard_lower:
                # Look for matching concrete standards
                for standard_name in MATERIAL_STANDARDS:
                    if 'Concrete' in standard_name or 'ACI_Normal' in standard_name or 'EN_C' in standard_name:
                        # Try to match compressive strength if available
                        if 'yield_strength' in data and data['yield_strength']:
                            try:
                                fc = float(data['yield_strength'])
                                if standard_name in MATERIAL_STANDARDS:
                                    std_props = MATERIAL_STANDARDS[standard_name]
                                    if 'CompressiveStrength' in std_props:
                                        std_fc = float(std_props['CompressiveStrength'].split()[0])
                                        if abs(fc - std_fc) < 5:  # Within 5 MPa tolerance
                                            return standard_name
                            except:
                                pass
                        # If no strength match, return first concrete standard found
                        return standard_name
        
        # Check for steel materials
        steel_keywords = ['steel', 'stainless', 'astm', 'en_s', 'jis']
        for keyword in steel_keywords:
            if keyword in name_lower or keyword in type_lower or keyword in standard_lower:
                # Look for matching steel standards
                for standard_name in MATERIAL_STANDARDS:
                    if 'ASTM' in standard_name or 'EN_S' in standard_name or 'JIS' in standard_name:
                        return standard_name
        
        return None

    def create_new_material(self):
        """Create new material object"""
        try:
            data = self.selected_material_data
            
            # Create new material object
            doc = App.ActiveDocument
            if not doc:
                App.Console.PrintError("No active document. Please create or open a document.\n")
                return
            
            # Try to create StructuralMaterial first (enhanced material with standards support)
            try:
                from ..objects.StructuralMaterial import StructuralMaterial, ViewProviderStructuralMaterial
                
                obj = doc.addObject("App::DocumentObjectGroupPython", "StructuralMaterial")
                
                StructuralMaterial(obj)
                ViewProviderStructuralMaterial(obj.ViewObject)
                
                # Set properties
                obj.Label = data.get('name', 'Material')
                
                # Determine material type based on data
                material_type = "Steel"  # Default
                if any(term in data.get('type', '').lower() + data.get('name', '').lower() 
                      for term in ['concrete', 'คอนกรีต', 'fc']):
                    material_type = "Concrete"
                
                obj.MaterialType = material_type
                
                # Set standard if it matches a database standard
                standard_name = self.find_matching_standard(data)
                if standard_name:
                    obj.MaterialStandard = standard_name
                else:
                    # Set custom properties
                    modulus_mpa = data.get('modulus_elasticity', 200000)
                    obj.ModulusElasticity = f"{modulus_mpa} MPa"
                    
                    obj.PoissonRatio = data.get('poisson_ratio', 0.30)
                    
                    density_kg_m3 = data.get('density', 7850)
                    obj.Density = f"{density_kg_m3} kg/m^3"
                    
                    if 'yield_strength' in data and data['yield_strength']:
                        obj.YieldStrength = f"{data['yield_strength']} MPa"
                    
                    if 'ultimate_strength' in data and data['ultimate_strength']:
                        obj.UltimateStrength = f"{data['ultimate_strength']} MPa"
                
                doc.recompute()
                
                App.Console.PrintMessage(f"StructuralMaterial '{obj.Label}' created successfully.\n")
                return
                
            except ImportError:
                # Fallback to basic Material
                obj = doc.addObject("Part::FeaturePython", "Material")
                
                # Import and create material
                from ..material import Material, ViewProviderMaterial
                Material(obj)
                ViewProviderMaterial(obj.ViewObject)
                
                # Set properties
                obj.Label = data.get('name', 'Material')
                
                modulus_mpa = data.get('modulus_elasticity', 200000)
                obj.ModulusElasticity = f"{modulus_mpa} MPa"
                
                obj.PoissonRatio = data.get('poisson_ratio', 0.30)
                
                density_kg_m3 = data.get('density', 7850)
                obj.Density = f"{density_kg_m3} kg/m^3"
                
                # Add additional properties
                obj.addProperty("App::PropertyString", "MaterialType", "Material", "Material classification")
                obj.MaterialType = data.get('type', 'Structural Steel')
                
                obj.addProperty("App::PropertyString", "Standard", "Material", "Material standard")
                obj.Standard = data.get('standard', 'Custom')
                
                if 'yield_strength' in data and data['yield_strength']:
                    obj.addProperty("App::PropertyPressure", "YieldStrength", "Strength", "Yield strength")
                    obj.YieldStrength = f"{data['yield_strength']} MPa"
                
                if 'ultimate_strength' in data and data['ultimate_strength']:
                    obj.addProperty("App::PropertyPressure", "UltimateStrength", "Strength", "Ultimate strength")
                    obj.UltimateStrength = f"{data['ultimate_strength']} MPa"
                
                doc.recompute()
                
                App.Console.PrintMessage(f"Material '{obj.Label}' created successfully.\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error creating material: {str(e)}\n")
    
    def accept(self):
        """Accept and apply material"""
        if self.tab_widget.currentIndex() == 1:  # Custom material tab
            self.update_custom_preview()
        
        self.apply_material()
        return True
    
    def reject(self):
        """Reject and close panel"""
        return True
    
    def getStandardButtons(self):
        """Return standard dialog buttons"""
        return QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel