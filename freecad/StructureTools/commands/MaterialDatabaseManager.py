# -*- coding: utf-8 -*-
"""
MaterialDatabaseManager - Command for managing material database

This command provides a comprehensive interface for managing the material
standards database, including browsing, searching, and creating materials.
"""

import FreeCAD as App
import FreeCADGui as Gui
import os
from typing import List, Dict, Optional

# Import Qt modules
try:
    from PySide2 import QtWidgets, QtCore, QtGui
except ImportError:
    try:
        from PySide import QtWidgets, QtCore
        from PySide import QtGui
    except ImportError:
        try:
            from PyQt5 import QtWidgets, QtCore, QtGui
        except ImportError:
            try:
                from PyQt4 import QtGui as QtWidgets, QtCore
                from PyQt4 import QtGui
            except ImportError:
                # Fallback - create a minimal stub
                import types
                QtWidgets = types.SimpleNamespace()
                QtCore = types.SimpleNamespace()
                QtGui = types.SimpleNamespace()
                
                # Create essential classes as stubs
                class QWidget: pass
                class QDialog: pass
                class QTreeWidgetItem: 
                    def __init__(self, items): self.items = items
                    
                QtWidgets.QWidget = QWidget
                QtWidgets.QDialog = QDialog  
                QtWidgets.QTreeWidgetItem = QTreeWidgetItem

# Icon path
ICONPATH = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")

# Import material utilities
try:
    from ..utils.MaterialHelper import (
        list_available_standards,
        list_standards_by_category,
        search_materials,
        create_material_from_database,
        get_calc_properties_from_database
    )
    from ..data.MaterialStandards import MATERIAL_CATEGORIES, get_material_info
    HAS_DATABASE = True
except ImportError:
    HAS_DATABASE = False
    MATERIAL_CATEGORIES = {}
    def list_available_standards():
        return []
    def get_material_info(name):
        return {}


class MaterialDatabaseManagerCommand:
    """Command for managing material database."""
    
    def GetResources(self) -> dict:
        """Return command resources."""
        return {
            "Pixmap": os.path.join(ICONPATH, "material_database.svg"),
            "Accel": "Ctrl+Shift+M",
            "MenuText": "Material Database Manager",
            "ToolTip": "Browse and manage material standards database"
        }
    
    def Activated(self) -> None:
        """Execute the command."""
        if not HAS_DATABASE:
            from PySide import QtWidgets
            QtWidgets.QMessageBox.warning(
                None, 
                "Database Not Available", 
                "Material standards database is not available.\nPlease check your installation."
            )
            return
        
        # Show material database manager dialog
        self.show_database_manager_dialog()
    
    def show_database_manager_dialog(self):
        """Show comprehensive material database manager."""
        # Create main dialog
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Material Standards Database Manager")
        dialog.setMinimumWidth(800)
        dialog.setMinimumHeight(600)
        
        layout = QtWidgets.QHBoxLayout()
        
        # Left panel - Category tree and search
        left_panel = QtWidgets.QVBoxLayout()
        
        # Search box
        search_group = QtWidgets.QGroupBox("Search Materials")
        search_layout = QtWidgets.QVBoxLayout()
        
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText("Enter search term...")
        search_layout.addWidget(self.search_input)
        
        search_button = QtWidgets.QPushButton("Search")
        search_layout.addWidget(search_button)
        
        search_group.setLayout(search_layout)
        left_panel.addWidget(search_group)
        
        # Category tree
        category_group = QtWidgets.QGroupBox("Material Categories")
        category_layout = QtWidgets.QVBoxLayout()
        
        self.category_tree = QtWidgets.QTreeWidget()
        self.category_tree.setHeaderLabels(["Material Standards"])
        category_layout.addWidget(self.category_tree)
        
        category_group.setLayout(category_layout)
        left_panel.addWidget(category_group)
        
        # Right panel - Material details and actions
        right_panel = QtWidgets.QVBoxLayout()
        
        # Material details
        details_group = QtWidgets.QGroupBox("Material Properties")
        details_layout = QtWidgets.QVBoxLayout()
        
        self.details_table = QtWidgets.QTableWidget()
        self.details_table.setColumnCount(2)
        self.details_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.details_table.horizontalHeader().setStretchLastSection(True)
        details_layout.addWidget(self.details_table)
        
        details_group.setLayout(details_layout)
        right_panel.addWidget(details_group)
        
        # Calc compatibility preview
        calc_group = QtWidgets.QGroupBox("Calc Properties Preview")
        calc_layout = QtWidgets.QVBoxLayout()
        
        self.calc_preview = QtWidgets.QTextEdit()
        self.calc_preview.setMaximumHeight(150)
        self.calc_preview.setReadOnly(True)
        calc_layout.addWidget(self.calc_preview)
        
        calc_group.setLayout(calc_layout)
        right_panel.addWidget(calc_group)
        
        # Action buttons
        action_group = QtWidgets.QGroupBox("Actions")
        action_layout = QtWidgets.QVBoxLayout()
        
        create_button = QtWidgets.QPushButton("Create Material Object")
        create_enhanced_button = QtWidgets.QPushButton("Create Enhanced Material")
        export_button = QtWidgets.QPushButton("Export Database")
        
        action_layout.addWidget(create_button)
        action_layout.addWidget(create_enhanced_button)
        action_layout.addWidget(export_button)
        
        action_group.setLayout(action_layout)
        right_panel.addWidget(action_group)
        
        # Layout assembly
        left_widget = QtWidgets.QWidget()
        left_widget.setLayout(left_panel)
        left_widget.setMaximumWidth(300)
        
        right_widget = QtWidgets.QWidget()
        right_widget.setLayout(right_panel)
        
        layout.addWidget(left_widget)
        layout.addWidget(right_widget)
        
        # Bottom buttons
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(layout)
        
        button_layout = QtWidgets.QHBoxLayout()
        close_button = QtWidgets.QPushButton("Close")
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        main_layout.addLayout(button_layout)
        
        dialog.setLayout(main_layout)
        
        # Initialize data
        self.populate_category_tree()
        self.current_material = None
        
        # Connect signals
        search_button.clicked.connect(self.perform_search)
        self.search_input.returnPressed.connect(self.perform_search)
        self.category_tree.itemClicked.connect(self.on_material_selected)
        create_button.clicked.connect(self.create_basic_material)
        create_enhanced_button.clicked.connect(self.create_enhanced_material)
        export_button.clicked.connect(self.export_database)
        close_button.clicked.connect(dialog.close)
        
        # Show dialog
        dialog.exec_()
    
    def populate_category_tree(self):
        """Populate the category tree with materials."""
        self.category_tree.clear()
        
        for category, materials in MATERIAL_CATEGORIES.items():
            category_item = QtWidgets.QTreeWidgetItem([category])
            
            for material in materials:
                material_item = QtWidgets.QTreeWidgetItem([material])
                material_item.setData(0, QtCore.Qt.UserRole, material)
                category_item.addChild(material_item)
            
            self.category_tree.addTopLevelItem(category_item)
        
        # Expand all categories
        self.category_tree.expandAll()
    
    def perform_search(self):
        """Perform search and update tree."""
        search_term = self.search_input.text().strip()
        if not search_term:
            self.populate_category_tree()
            return
        
        matches = search_materials(search_term)
        
        # Clear and populate with search results
        self.category_tree.clear()
        
        if matches:
            search_item = QtWidgets.QTreeWidgetItem([f"Search Results ({len(matches)})"])
            
            for material in matches:
                material_item = QtWidgets.QTreeWidgetItem([material])
                material_item.setData(0, QtCore.Qt.UserRole, material)
                search_item.addChild(material_item)
            
            self.category_tree.addTopLevelItem(search_item)
            self.category_tree.expandAll()
        else:
            no_results_item = QtWidgets.QTreeWidgetItem(["No results found"])
            self.category_tree.addTopLevelItem(no_results_item)
    
    def on_material_selected(self, item, column):
        """Handle material selection."""
        material_name = item.data(0, QtCore.Qt.UserRole)
        if not material_name:
            return
        
        self.current_material = material_name
        self.update_material_details(material_name)
        self.update_calc_preview(material_name)
    
    def update_material_details(self, material_name):
        """Update material details table."""
        props = get_material_info(material_name)
        
        self.details_table.setRowCount(len(props))
        
        for row, (key, value) in enumerate(props.items()):
            property_item = QtWidgets.QTableWidgetItem(key)
            value_item = QtWidgets.QTableWidgetItem(str(value))
            
            self.details_table.setItem(row, 0, property_item)
            self.details_table.setItem(row, 1, value_item)
        
        self.details_table.resizeColumnsToContents()
    
    def update_calc_preview(self, material_name):
        """Update calc compatibility preview."""
        calc_props = get_calc_properties_from_database(material_name, 'm', 'kN')
        
        if calc_props:
            preview_text = "Calc Properties (m-kN system):\n"
            preview_text += f"Name: {calc_props['name']}\n"
            preview_text += f"Elastic Modulus: {calc_props['E']:,.0f} kN/m²\n"
            preview_text += f"Shear Modulus: {calc_props['G']:,.0f} kN/m²\n"
            preview_text += f"Poisson Ratio: {calc_props['nu']:.3f}\n"
            preview_text += f"Density: {calc_props['density']:.1f} kN/m³\n"
            preview_text += f"Unit System: {calc_props['unit_system']}\n"
            preview_text += "\n✓ Compatible with calc analysis"
        else:
            preview_text = "Error: Could not generate calc properties"
        
        self.calc_preview.setText(preview_text)
    
    def create_basic_material(self):
        """Create basic material from selected standard."""
        if not self.current_material:
            from PySide import QtWidgets
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select a material standard")
            return
        
        try:
            from ..utils.MaterialHelper import create_material_from_database
            material = create_material_from_database(self.current_material)
            if material:
                App.Console.PrintMessage(f"Created material: {material.Label}\n")
            else:
                App.Console.PrintError("Failed to create material\n")
        except Exception as e:
            App.Console.PrintError(f"Error creating material: {e}\n")
    
    def create_enhanced_material(self):
        """Create enhanced StructuralMaterial from selected standard."""
        if not self.current_material:
            from PySide import QtWidgets
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select a material standard")
            return
        
        try:
            from ..commands.CreateMaterial import create_steel_material
            material = create_steel_material(f"Steel_{self.current_material}", self.current_material)
            if material:
                App.Console.PrintMessage(f"Created enhanced material: {material.Label}\n")
            else:
                App.Console.PrintError("Failed to create enhanced material\n")
        except Exception as e:
            App.Console.PrintError(f"Error creating enhanced material: {e}\n")
    
    def export_database(self):
        """Export material database to file."""
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Export Material Database",
            "material_database.json",
            "JSON Files (*.json);;All Files (*)"
        )
        
        if file_path:
            try:
                from ..utils.MaterialHelper import export_material_database
                success = export_material_database(file_path)
                if success:
                    QtWidgets.QMessageBox.information(
                        None, 
                        "Export Successful", 
                        f"Database exported to:\n{file_path}"
                    )
                else:
                    QtWidgets.QMessageBox.warning(
                        None, 
                        "Export Failed", 
                        "Failed to export database"
                    )
            except Exception as e:
                QtWidgets.QMessageBox.critical(
                    None, 
                    "Export Error", 
                    f"Error during export:\n{str(e)}"
                )
    
    def IsActive(self) -> bool:
        """Return True if command can be activated."""
        return App.ActiveDocument is not None


# Register the command
Gui.addCommand("MaterialDatabaseManager", MaterialDatabaseManagerCommand())