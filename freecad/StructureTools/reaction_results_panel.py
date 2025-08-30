import FreeCAD, FreeCADGui
import os
from typing import Optional

# Prefer PySide2 when available
try:
    from PySide2 import QtWidgets, QtCore, QtGui
except ImportError:
    try:
        from PySide import QtWidgets, QtCore, QtGui
    except ImportError as e:
        raise ImportError("Neither PySide2 nor PySide could be imported. Please install one of them.") from e

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")


class ReactionResultsPanel:
    """Control panel for reaction results visualization with S3D-style interface."""
    
    def __init__(self, reaction_obj):
        self.reaction_obj = reaction_obj
        self.form = self.create_ui()
        self.setup_connections()
        self.update_ui_from_object()
    
    def create_ui(self):
        """Create the user interface similar to S3D reaction results panel."""
        # Main widget
        widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title_label = QtWidgets.QLabel("Reaction Results")
        title_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #2c3e50;")
        main_layout.addWidget(title_label)
        
        # Load combination selection
        combo_group = QtWidgets.QGroupBox("Load Combination")
        combo_layout = QtWidgets.QVBoxLayout()
        
        self.load_combo_dropdown = QtWidgets.QComboBox()
        self.load_combo_dropdown.setMinimumWidth(200)
        self.populate_load_combinations()
        combo_layout.addWidget(self.load_combo_dropdown)
        
        combo_group.setLayout(combo_layout)
        main_layout.addWidget(combo_group)
        
        # Reaction Forces Group
        forces_group = QtWidgets.QGroupBox("Reaction Forces")
        forces_layout = QtWidgets.QVBoxLayout()
        
        # Create checkboxes for force components
        self.fx_checkbox = QtWidgets.QCheckBox("Fx (X-Direction Forces)")
        self.fx_checkbox.setChecked(True)
        self.fx_checkbox.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "force_x.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "force_x.svg")) else QtGui.QIcon())
        
        self.fy_checkbox = QtWidgets.QCheckBox("Fy (Y-Direction Forces)")
        self.fy_checkbox.setChecked(True)
        self.fy_checkbox.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "force_y.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "force_y.svg")) else QtGui.QIcon())
        
        self.fz_checkbox = QtWidgets.QCheckBox("Fz (Z-Direction Forces)")
        self.fz_checkbox.setChecked(True)
        self.fz_checkbox.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "force_z.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "force_z.svg")) else QtGui.QIcon())
        
        forces_layout.addWidget(self.fx_checkbox)
        forces_layout.addWidget(self.fy_checkbox)
        forces_layout.addWidget(self.fz_checkbox)
        
        # Force scale control
        force_scale_layout = QtWidgets.QHBoxLayout()
        force_scale_layout.addWidget(QtWidgets.QLabel("Scale:"))
        self.force_scale_spinbox = QtWidgets.QDoubleSpinBox()
        self.force_scale_spinbox.setRange(0.1, 10.0)
        self.force_scale_spinbox.setValue(1.0)
        self.force_scale_spinbox.setSingleStep(0.1)
        self.force_scale_spinbox.setDecimals(1)
        force_scale_layout.addWidget(self.force_scale_spinbox)
        force_scale_layout.addStretch()
        forces_layout.addLayout(force_scale_layout)
        
        forces_group.setLayout(forces_layout)
        main_layout.addWidget(forces_group)
        
        # Reaction Moments Group
        moments_group = QtWidgets.QGroupBox("Reaction Moments")
        moments_layout = QtWidgets.QVBoxLayout()
        
        # Create checkboxes for moment components
        self.mx_checkbox = QtWidgets.QCheckBox("Mx (X-Axis Moments)")
        self.mx_checkbox.setChecked(True)
        self.mx_checkbox.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "moment_x.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "moment_x.svg")) else QtGui.QIcon())
        
        self.my_checkbox = QtWidgets.QCheckBox("My (Y-Axis Moments)")
        self.my_checkbox.setChecked(True)
        self.my_checkbox.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "moment_y.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "moment_y.svg")) else QtGui.QIcon())
        
        self.mz_checkbox = QtWidgets.QCheckBox("Mz (Z-Axis Moments)")
        self.mz_checkbox.setChecked(True)
        self.mz_checkbox.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "moment_z.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "moment_z.svg")) else QtGui.QIcon())
        
        moments_layout.addWidget(self.mx_checkbox)
        moments_layout.addWidget(self.my_checkbox)
        moments_layout.addWidget(self.mz_checkbox)
        
        # Moment scale control
        moment_scale_layout = QtWidgets.QHBoxLayout()
        moment_scale_layout.addWidget(QtWidgets.QLabel("Scale:"))
        self.moment_scale_spinbox = QtWidgets.QDoubleSpinBox()
        self.moment_scale_spinbox.setRange(0.1, 10.0)
        self.moment_scale_spinbox.setValue(1.0)
        self.moment_scale_spinbox.setSingleStep(0.1)
        self.moment_scale_spinbox.setDecimals(1)
        moment_scale_layout.addWidget(self.moment_scale_spinbox)
        moment_scale_layout.addStretch()
        moments_layout.addLayout(moment_scale_layout)
        
        moments_group.setLayout(moments_layout)
        main_layout.addWidget(moments_group)
        
        # Display Options Group
        display_group = QtWidgets.QGroupBox("Display Options")
        display_layout = QtWidgets.QGridLayout()
        
        # Show labels checkbox
        self.labels_checkbox = QtWidgets.QCheckBox("Show Values")
        self.labels_checkbox.setChecked(True)
        display_layout.addWidget(self.labels_checkbox, 0, 0, 1, 2)
        
        # Precision control
        display_layout.addWidget(QtWidgets.QLabel("Precision:"), 1, 0)
        self.precision_spinbox = QtWidgets.QSpinBox()
        self.precision_spinbox.setRange(0, 6)
        self.precision_spinbox.setValue(2)
        display_layout.addWidget(self.precision_spinbox, 1, 1)
        
        # Font size control
        display_layout.addWidget(QtWidgets.QLabel("Font Size:"), 2, 0)
        self.font_size_spinbox = QtWidgets.QSpinBox()
        self.font_size_spinbox.setRange(6, 24)
        self.font_size_spinbox.setValue(8)
        display_layout.addWidget(self.font_size_spinbox, 2, 1)
        
        # Arrow thickness control
        display_layout.addWidget(QtWidgets.QLabel("Arrow Thickness:"), 3, 0)
        self.thickness_spinbox = QtWidgets.QDoubleSpinBox()
        self.thickness_spinbox.setRange(0.5, 10.0)
        self.thickness_spinbox.setValue(2.0)
        self.thickness_spinbox.setSingleStep(0.5)
        self.thickness_spinbox.setDecimals(1)
        display_layout.addWidget(self.thickness_spinbox, 3, 1)
        
        display_group.setLayout(display_layout)
        main_layout.addWidget(display_group)
        
        # Color Selection Group
        color_group = QtWidgets.QGroupBox("Colors")
        color_layout = QtWidgets.QGridLayout()
        
        # Force color
        color_layout.addWidget(QtWidgets.QLabel("Force Color:"), 0, 0)
        self.force_color_button = QtWidgets.QPushButton()
        self.force_color_button.setMaximumSize(50, 25)
        self.force_color_button.setStyleSheet("background-color: red; border: 1px solid gray;")
        color_layout.addWidget(self.force_color_button, 0, 1)
        
        # Moment color
        color_layout.addWidget(QtWidgets.QLabel("Moment Color:"), 1, 0)
        self.moment_color_button = QtWidgets.QPushButton()
        self.moment_color_button.setMaximumSize(50, 25)
        self.moment_color_button.setStyleSheet("background-color: blue; border: 1px solid gray;")
        color_layout.addWidget(self.moment_color_button, 1, 1)
        
        color_group.setLayout(color_layout)
        main_layout.addWidget(color_group)
        
        # Control buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        self.refresh_button = QtWidgets.QPushButton("Refresh Display")
        self.refresh_button.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "refresh.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "refresh.svg")) else QtGui.QIcon())
        
        self.reset_labels_button = QtWidgets.QPushButton("Reset Label Positions")
        self.reset_labels_button.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "reset.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "reset.svg")) else QtGui.QIcon())
        
        self.export_button = QtWidgets.QPushButton("Export to CSV")
        self.export_button.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "export.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "export.svg")) else QtGui.QIcon())
        
        self.table_view_button = QtWidgets.QPushButton("Table View")
        self.table_view_button.setIcon(QtGui.QIcon(os.path.join(ICONPATH, "icons", "table.svg")) if os.path.exists(os.path.join(ICONPATH, "icons", "table.svg")) else QtGui.QIcon())
        
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.reset_labels_button)
        button_layout.addWidget(self.export_button)
        button_layout.addWidget(self.table_view_button)
        
        main_layout.addLayout(button_layout)
        
        # Summary information
        self.info_label = QtWidgets.QLabel("Ready to display reactions")
        self.info_label.setStyleSheet("color: #7f8c8d; font-style: italic;")
        main_layout.addWidget(self.info_label)
        
        main_layout.addStretch()
        return widget

    def setup_connections(self):
        """Connect UI elements to their handlers."""
        # Load combination change
        self.load_combo_dropdown.currentTextChanged.connect(self.on_load_combination_changed)
        
        # Force checkboxes
        self.fx_checkbox.toggled.connect(self.on_force_checkbox_changed)
        self.fy_checkbox.toggled.connect(self.on_force_checkbox_changed)
        self.fz_checkbox.toggled.connect(self.on_force_checkbox_changed)
        
        # Moment checkboxes
        self.mx_checkbox.toggled.connect(self.on_moment_checkbox_changed)
        self.my_checkbox.toggled.connect(self.on_moment_checkbox_changed)
        self.mz_checkbox.toggled.connect(self.on_moment_checkbox_changed)
        
        # Scale controls
        self.force_scale_spinbox.valueChanged.connect(self.on_force_scale_changed)
        self.moment_scale_spinbox.valueChanged.connect(self.on_moment_scale_changed)
        
        # Display options
        self.labels_checkbox.toggled.connect(self.on_display_option_changed)
        self.precision_spinbox.valueChanged.connect(self.on_display_option_changed)
        self.font_size_spinbox.valueChanged.connect(self.on_display_option_changed)
        self.thickness_spinbox.valueChanged.connect(self.on_display_option_changed)
        
        # Color buttons
        self.force_color_button.clicked.connect(self.on_force_color_clicked)
        self.moment_color_button.clicked.connect(self.on_moment_color_clicked)
        
        # Control buttons
        self.refresh_button.clicked.connect(self.on_refresh_clicked)
        self.reset_labels_button.clicked.connect(self.on_reset_labels_clicked)
        self.export_button.clicked.connect(self.on_export_clicked)
        self.table_view_button.clicked.connect(self.on_table_view_clicked)
    
    def populate_load_combinations(self):
        """Populate the load combination dropdown."""
        if not self.reaction_obj or not self.reaction_obj.ObjectBaseCalc:
            return
        
        try:
            # Get available load combinations from calc object
            calc_obj = self.reaction_obj.ObjectBaseCalc
            if hasattr(calc_obj, 'LoadCombination'):
                # Get all available load combinations from calc object
                if hasattr(calc_obj, 'LoadCombination'):
                    available_combos = calc_obj.LoadCombination
                    self.load_combo_dropdown.clear()
                    
                    if isinstance(available_combos, list):
                        self.load_combo_dropdown.addItems(available_combos)
                    else:
                        self.load_combo_dropdown.addItem(str(available_combos))
                    
                    # Set current selection to match object property
                    if hasattr(self.reaction_obj, 'ActiveLoadCombination'):
                        current_combo = self.reaction_obj.ActiveLoadCombination
                        index = self.load_combo_dropdown.findText(current_combo)
                        if index >= 0:
                            self.load_combo_dropdown.setCurrentIndex(index)
                            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Warning: Could not populate load combinations: {str(e)}\n")
            # Add default combination
            self.load_combo_dropdown.addItem("100_DL")
    
    def update_ui_from_object(self):
        """Update UI controls to match object properties."""
        if not self.reaction_obj:
            return
        
        try:
            # Update checkboxes
            if hasattr(self.reaction_obj, 'ShowReactionFX'):
                self.fx_checkbox.setChecked(self.reaction_obj.ShowReactionFX)
            if hasattr(self.reaction_obj, 'ShowReactionFY'):
                self.fy_checkbox.setChecked(self.reaction_obj.ShowReactionFY)
            if hasattr(self.reaction_obj, 'ShowReactionFZ'):
                self.fz_checkbox.setChecked(self.reaction_obj.ShowReactionFZ)
                
            if hasattr(self.reaction_obj, 'ShowReactionMX'):
                self.mx_checkbox.setChecked(self.reaction_obj.ShowReactionMX)
            if hasattr(self.reaction_obj, 'ShowReactionMY'):
                self.my_checkbox.setChecked(self.reaction_obj.ShowReactionMY)
            if hasattr(self.reaction_obj, 'ShowReactionMZ'):
                self.mz_checkbox.setChecked(self.reaction_obj.ShowReactionMZ)
            
            # Update scale controls
            if hasattr(self.reaction_obj, 'ScaleReactionForces'):
                self.force_scale_spinbox.setValue(self.reaction_obj.ScaleReactionForces)
            if hasattr(self.reaction_obj, 'ScaleReactionMoments'):
                self.moment_scale_spinbox.setValue(self.reaction_obj.ScaleReactionMoments)
            
            # Update display options
            if hasattr(self.reaction_obj, 'ShowLabels'):
                self.labels_checkbox.setChecked(self.reaction_obj.ShowLabels)
            if hasattr(self.reaction_obj, 'Precision'):
                self.precision_spinbox.setValue(self.reaction_obj.Precision)
            if hasattr(self.reaction_obj, 'LabelFontSize'):
                self.font_size_spinbox.setValue(self.reaction_obj.LabelFontSize)
            if hasattr(self.reaction_obj, 'ArrowThickness'):
                self.thickness_spinbox.setValue(self.reaction_obj.ArrowThickness)
                
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Warning: Could not update UI from object: {str(e)}\n")
    
    def on_load_combination_changed(self, combo_name):
        """Handle load combination selection change."""
        if self.reaction_obj:
            self.reaction_obj.ActiveLoadCombination = combo_name
            self.update_display()
            self.update_info_label()
    
    def on_force_checkbox_changed(self):
        """Handle force checkbox changes."""
        if not self.reaction_obj:
            return
        
        self.reaction_obj.ShowReactionFX = self.fx_checkbox.isChecked()
        self.reaction_obj.ShowReactionFY = self.fy_checkbox.isChecked()
        self.reaction_obj.ShowReactionFZ = self.fz_checkbox.isChecked()
        self.update_display()
    
    def on_moment_checkbox_changed(self):
        """Handle moment checkbox changes."""
        if not self.reaction_obj:
            return
        
        self.reaction_obj.ShowReactionMX = self.mx_checkbox.isChecked()
        self.reaction_obj.ShowReactionMY = self.my_checkbox.isChecked()
        self.reaction_obj.ShowReactionMZ = self.mz_checkbox.isChecked()
        self.update_display()
    
    def on_force_scale_changed(self, value):
        """Handle force scale change."""
        if self.reaction_obj:
            self.reaction_obj.ScaleReactionForces = value
            self.update_display()
    
    def on_moment_scale_changed(self, value):
        """Handle moment scale change."""
        if self.reaction_obj:
            self.reaction_obj.ScaleReactionMoments = value
            self.update_display()
    
    def on_display_option_changed(self):
        """Handle display option changes."""
        if not self.reaction_obj:
            return
        
        self.reaction_obj.ShowLabels = self.labels_checkbox.isChecked()
        self.reaction_obj.Precision = self.precision_spinbox.value()
        self.reaction_obj.LabelFontSize = self.font_size_spinbox.value()
        self.reaction_obj.ArrowThickness = self.thickness_spinbox.value()
        self.update_display()
    
    def on_force_color_clicked(self):
        """Handle force color button click."""
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.red, self.form, "Select Force Color")
        if color.isValid():
            rgb = color.getRgbF()
            self.reaction_obj.ForceArrowColor = (rgb[0], rgb[1], rgb[2], 0.0)
            self.force_color_button.setStyleSheet(f"background-color: {color.name()}; border: 1px solid gray;")
            self.update_display()
    
    def on_moment_color_clicked(self):
        """Handle moment color button click."""
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.blue, self.form, "Select Moment Color")
        if color.isValid():
            rgb = color.getRgbF()
            self.reaction_obj.MomentArrowColor = (rgb[0], rgb[1], rgb[2], 0.0)
            self.moment_color_button.setStyleSheet(f"background-color: {color.name()}; border: 1px solid gray;")
            self.update_display()
    
    def on_refresh_clicked(self):
        """Handle refresh button click."""
        self.update_display()
        self.update_info_label()
    
    def on_reset_labels_clicked(self):
        """Handle reset label positions button click."""
        try:
            # Reset all draggable reaction labels to their original positions
            from .draggable_label import reset_all_reaction_labels
            reset_all_reaction_labels()
            
            # Update display
            self.update_display()
            self.info_label.setText("Label positions reset to original locations")
            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Could not reset label positions: {str(e)}\n")
            self.info_label.setText("Error resetting label positions")
    
    def update_display(self):
        """Update the reaction visualization display."""
        if self.reaction_obj and hasattr(self.reaction_obj, 'Proxy'):
            try:
                self.reaction_obj.Proxy.execute(self.reaction_obj)
                FreeCAD.ActiveDocument.recompute()
                FreeCADGui.updateGui()
            except Exception as e:
                FreeCAD.Console.PrintError(f"Error updating reaction display: {str(e)}\n")
    
    def update_info_label(self):
        """Update the information label with current status."""
        try:
            if not self.reaction_obj or not self.reaction_obj.ObjectBaseCalc:
                self.info_label.setText("No calculation object linked")
                return
            
            calc_obj = self.reaction_obj.ObjectBaseCalc
            
            # Try different ways to get the FE model
            model = None
            if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                model = calc_obj.FEModel
            elif hasattr(calc_obj, 'model') and calc_obj.model:
                model = calc_obj.model
                
            if not model:
                self.info_label.setText("Analysis not completed - please run calculation")
                return
            
            # Count supported nodes
            supported_nodes = 0
            total_reactions = 0
            
            for node in model.nodes.values():
                if (node.support_DX or node.support_DY or node.support_DZ or 
                    node.support_RX or node.support_RY or node.support_RZ):
                    supported_nodes += 1
                    
                    # Count non-zero reactions for current load combination
                    combo = self.reaction_obj.ActiveLoadCombination
                    if combo in node.RxnFX and abs(node.RxnFX[combo]) > 1e-6:
                        total_reactions += 1
                    if combo in node.RxnFY and abs(node.RxnFY[combo]) > 1e-6:
                        total_reactions += 1
                    if combo in node.RxnFZ and abs(node.RxnFZ[combo]) > 1e-6:
                        total_reactions += 1
                    if combo in node.RxnMX and abs(node.RxnMX[combo]) > 1e-6:
                        total_reactions += 1
                    if combo in node.RxnMY and abs(node.RxnMY[combo]) > 1e-6:
                        total_reactions += 1
                    if combo in node.RxnMZ and abs(node.RxnMZ[combo]) > 1e-6:
                        total_reactions += 1
            
            self.info_label.setText(f"Displaying {total_reactions} reactions at {supported_nodes} support nodes")
            
        except Exception as e:
            self.info_label.setText(f"Error: {str(e)}")
    
    def accept(self):
        """Accept changes and close panel."""
        FreeCADGui.Control.closeDialog()
    
    def reject(self):
        """Reject changes and close panel."""
        FreeCADGui.Control.closeDialog()
    
    def getStandardButtons(self):
        """Return standard buttons for the panel."""
        return int(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
    
    def on_export_clicked(self):
        """Handle export to CSV button click."""
        try:
            # Get file path from user
            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self.form, 
                "Export Reaction Results", 
                "", 
                "CSV Files (*.csv);;All Files (*)"
            )
            
            if not file_path:
                return
                
            # Ensure file has .csv extension
            if not file_path.lower().endswith('.csv'):
                file_path += '.csv'
            
            # Export reaction results
            success = self.export_reaction_results_to_csv(file_path)
            
            if success:
                self.info_label.setText(f"Reaction results exported to: {file_path}")
                QtWidgets.QMessageBox.information(
                    self.form, 
                    "Export Successful", 
                    f"Reaction results successfully exported to:\n{file_path}"
                )
            else:
                self.info_label.setText("Error exporting reaction results")
                QtWidgets.QMessageBox.critical(
                    self.form, 
                    "Export Failed", 
                    "Failed to export reaction results. Check FreeCAD console for details."
                )
                
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error exporting reaction results: {str(e)}\n")
            self.info_label.setText(f"Error: {str(e)}")
    
    def on_table_view_clicked(self):
        """Handle table view button click."""
        try:
            # Close current dialog and open table view
            FreeCADGui.Control.closeDialog()
            
            # Open the reaction table panel
            from .reaction_table_panel import ReactionTablePanel
            panel = ReactionTablePanel(self.reaction_obj)
            FreeCADGui.Control.showDialog(panel)
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error opening reaction table panel: {str(e)}\n")
            self.info_label.setText(f"Error: {str(e)}")
    
    def export_reaction_results_to_csv(self, file_path):
        """Export reaction results to CSV file."""
        try:
            if not self.reaction_obj or not self.reaction_obj.ObjectBaseCalc:
                return False
                
            calc_obj = self.reaction_obj.ObjectBaseCalc
            model = None
            
            # Try different ways to get the FE model
            if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                model = calc_obj.FEModel
            elif hasattr(calc_obj, 'model') and calc_obj.model:
                model = calc_obj.model
                
            if not model:
                return False
            
            # Get active load combination
            load_combo = self.reaction_obj.ActiveLoadCombination
            
            # Import units manager for formatting
            try:
                from .utils.units_manager import format_force, format_moment
                units_available = True
            except ImportError:
                units_available = False
                format_force = lambda x: f"{x:.3f}"
                format_moment = lambda x: f"{x:.3f}"
            
            # Open file for writing
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                import csv
                writer = csv.writer(csvfile)
                
                # Write header with units information
                unit_system_info = "SI (kN, kN·m, m)"  # Default
                if units_available:
                    from .utils.units_manager import get_units_manager
                    manager = get_units_manager()
                    force_unit = manager.get_base_unit("force")
                    moment_unit = manager.get_base_unit("moment")
                    length_unit = manager.get_base_unit("length")
                    unit_system_info = f"{force_unit}, {moment_unit}, {length_unit}"
                
                writer.writerow([f"Reaction Results - Load Combination: {load_combo}"])
                writer.writerow([f"Units: {unit_system_info}"])
                writer.writerow([f"Sign Convention: +X=Right, +Y=Up, +Z=Out of screen"])
                writer.writerow([])  # Empty row
                
                # Column headers
                writer.writerow([
                    "Node ID", "DOF", 
                    "Rx (Force X)", "Ry (Force Y)", "Rz (Force Z)", 
                    "Mx (Moment X)", "My (Moment Y)", "Mz (Moment Z)",
                    "X (Position)", "Y (Position)", "Z (Position)"
                ])
                
                # Write data for each supported node
                supported_nodes = 0
                for node_name, node in model.nodes.items():
                    if self.is_node_supported(node):
                        supported_nodes += 1
                        
                        # Get reaction values for current load combination
                        rx = node.RxnFX.get(load_combo, 0.0) if load_combo in node.RxnFX else 0.0
                        ry = node.RxnFY.get(load_combo, 0.0) if load_combo in node.RxnFY else 0.0
                        rz = node.RxnFZ.get(load_combo, 0.0) if load_combo in node.RxnFZ else 0.0
                        mx = node.RxnMX.get(load_combo, 0.0) if load_combo in node.RxnMX else 0.0
                        my = node.RxnMY.get(load_combo, 0.0) if load_combo in node.RxnMY else 0.0
                        mz = node.RxnMZ.get(load_combo, 0.0) if load_combo in node.RxnMZ else 0.0
                        
                        # Format values with units
                        rx_formatted = format_force(rx) if units_available else f"{rx:.3f}"
                        ry_formatted = format_force(ry) if units_available else f"{ry:.3f}"
                        rz_formatted = format_force(rz) if units_available else f"{rz:.3f}"
                        mx_formatted = format_moment(mx) if units_available else f"{mx:.3f}"
                        my_formatted = format_moment(my) if units_available else f"{my:.3f}"
                        mz_formatted = format_moment(mz) if units_available else f"{mz:.3f}"
                        
                        # Node coordinates (in meters)
                        x_pos = f"{node.X:.3f}"
                        y_pos = f"{node.Y:.3f}"
                        z_pos = f"{node.Z:.3f}"
                        
                        # Write row for each non-zero reaction component
                        reactions_found = False
                        
                        if abs(rx) > 1e-6:
                            writer.writerow([node_name, "FX", rx_formatted, "", "", "", "", "", x_pos, y_pos, z_pos])
                            reactions_found = True
                            
                        if abs(ry) > 1e-6:
                            writer.writerow([node_name, "FY", "", ry_formatted, "", "", "", "", x_pos, y_pos, z_pos])
                            reactions_found = True
                            
                        if abs(rz) > 1e-6:
                            writer.writerow([node_name, "FZ", "", "", rz_formatted, "", "", "", x_pos, y_pos, z_pos])
                            reactions_found = True
                            
                        if abs(mx) > 1e-6:
                            writer.writerow([node_name, "MX", "", "", "", mx_formatted, "", "", x_pos, y_pos, z_pos])
                            reactions_found = True
                            
                        if abs(my) > 1e-6:
                            writer.writerow([node_name, "MY", "", "", "", "", my_formatted, "", x_pos, y_pos, z_pos])
                            reactions_found = True
                            
                        if abs(mz) > 1e-6:
                            writer.writerow([node_name, "MZ", "", "", "", "", "", mz_formatted, x_pos, y_pos, z_pos])
                            reactions_found = True
                        
                        # If no reactions but node is supported, show zero values
                        if not reactions_found:
                            writer.writerow([node_name, "All", rx_formatted, ry_formatted, rz_formatted, 
                                           mx_formatted, my_formatted, mz_formatted, x_pos, y_pos, z_pos])
                
                # Write summary
                writer.writerow([])
                writer.writerow([f"Total Supported Nodes: {supported_nodes}"])
                
                # Calculate total reactions for sanity check
                total_fx = total_fy = total_fz = 0.0
                total_mx = total_my = total_mz = 0.0
                
                for node in model.nodes.values():
                    if self.is_node_supported(node):
                        total_fx += node.RxnFX.get(load_combo, 0.0) if load_combo in node.RxnFX else 0.0
                        total_fy += node.RxnFY.get(load_combo, 0.0) if load_combo in node.RxnFY else 0.0
                        total_fz += node.RxnFZ.get(load_combo, 0.0) if load_combo in node.RxnFZ else 0.0
                        total_mx += node.RxnMX.get(load_combo, 0.0) if load_combo in node.RxnMX else 0.0
                        total_my += node.RxnMY.get(load_combo, 0.0) if load_combo in node.RxnMY else 0.0
                        total_mz += node.RxnMZ.get(load_combo, 0.0) if load_combo in node.RxnMZ else 0.0
                
                writer.writerow([f"Sum Reactions: FX={format_force(total_fx) if units_available else total_fx:.3f}, FY={format_force(total_fy) if units_available else total_fy:.3f}, FZ={format_force(total_fz) if units_available else total_fz:.3f}"])
                writer.writerow([f"Sum Moments: MX={format_moment(total_mx) if units_available else total_mx:.3f}, MY={format_moment(total_my) if units_available else total_my:.3f}, MZ={format_moment(total_mz) if units_available else total_mz:.3f}"])
            
            return True
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error exporting reaction results to CSV: {str(e)}\n")
            return False
    
    def is_node_supported(self, node) -> bool:
        """Check if a node has any support conditions."""
        return (node.support_DX or node.support_DY or node.support_DZ or 
                node.support_RX or node.support_RY or node.support_RZ)
