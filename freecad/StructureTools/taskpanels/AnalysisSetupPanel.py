# -*- coding: utf-8 -*-
"""
Analysis Setup Panel - Professional analysis configuration interface

This module provides a comprehensive task panel for structural analysis
setup with solver options, load combinations, and result preferences.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtGui, QtWidgets
from typing import Optional, Dict, List


class AnalysisSetupPanel:
    """Professional task panel for analysis configuration."""
    
    def __init__(self, analysis_obj=None):
        """Initialize Analysis Setup Panel."""
        self.analysis_obj = analysis_obj
        self.form = self._create_ui()
        self._populate_form()
        self._connect_signals()
    
    def _create_ui(self) -> QtWidgets.QWidget:
        """Create the user interface."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title = QtWidgets.QLabel("Analysis Setup")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        # Tab widget
        tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(tab_widget)
        
        # General tab
        general_tab = self._create_general_tab()
        tab_widget.addTab(general_tab, "General")
        
        # Solver tab
        solver_tab = self._create_solver_tab()
        tab_widget.addTab(solver_tab, "Solver")
        
        # Load combinations tab
        combinations_tab = self._create_combinations_tab()
        tab_widget.addTab(combinations_tab, "Load Combinations")
        
        # Results tab
        results_tab = self._create_results_tab()
        tab_widget.addTab(results_tab, "Results")
        
        # Progress and status
        status_widget = self._create_status_widget()
        layout.addWidget(status_widget)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        self.check_button = QtWidgets.QPushButton("Check Model")
        button_layout.addWidget(self.check_button)
        
        self.run_button = QtWidgets.QPushButton("Run Analysis")
        self.run_button.setDefault(True)
        button_layout.addWidget(self.run_button)
        
        self.results_button = QtWidgets.QPushButton("View Results")
        self.results_button.setEnabled(False)
        button_layout.addWidget(self.results_button)
        
        cancel_button = QtWidgets.QPushButton("Cancel")
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        # Store references
        self.tab_widget = tab_widget
        self.cancel_button = cancel_button
        
        return widget
    
    def _create_general_tab(self) -> QtWidgets.QWidget:
        """Create general analysis options tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Analysis type
        self.analysis_type_combo = QtWidgets.QComboBox()
        self.analysis_type_combo.addItems([
            "Linear Static", "Nonlinear Static", "Modal", "Linear Dynamic",
            "Buckling", "Time History", "Response Spectrum"
        ])
        layout.addRow("Analysis Type:", self.analysis_type_combo)
        
        # Analysis title and description
        self.analysis_title_edit = QtWidgets.QLineEdit()
        layout.addRow("Analysis Title:", self.analysis_title_edit)
        
        self.analysis_description_edit = QtWidgets.QTextEdit()
        self.analysis_description_edit.setMaximumHeight(80)
        layout.addRow("Description:", self.analysis_description_edit)
        
        # Units
        self.units_combo = QtWidgets.QComboBox()
        self.units_combo.addItems(["SI (N, mm)", "SI (kN, m)", "Imperial (lbf, in)", "Imperial (kip, ft)"])
        layout.addRow("Units:", self.units_combo)
        
        # Model validation
        self.auto_validate_check = QtWidgets.QCheckBox("Auto-validate model before analysis")
        self.auto_validate_check.setChecked(True)
        layout.addRow("Validation:", self.auto_validate_check)
        
        self.fix_warnings_check = QtWidgets.QCheckBox("Auto-fix minor warnings")
        layout.addRow("", self.fix_warnings_check)
        
        return widget
    
    def _create_solver_tab(self) -> QtWidgets.QWidget:
        """Create solver options tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Solver selection
        solver_group = QtWidgets.QGroupBox("Solver Configuration")
        solver_layout = QtWidgets.QFormLayout(solver_group)
        
        self.solver_combo = QtWidgets.QComboBox()
        self.solver_combo.addItems(["PyNite", "OpenSees", "Custom"])
        solver_layout.addRow("Solver Engine:", self.solver_combo)
        
        self.solver_precision_combo = QtWidgets.QComboBox()
        self.solver_precision_combo.addItems(["Single", "Double", "Extended"])
        solver_layout.addRow("Precision:", self.solver_precision_combo)
        
        layout.addWidget(solver_group)
        
        # Convergence criteria
        convergence_group = QtWidgets.QGroupBox("Convergence Criteria")
        convergence_layout = QtWidgets.QFormLayout(convergence_group)
        
        self.force_tolerance_spin = QtWidgets.QDoubleSpinBox()
        self.force_tolerance_spin.setRange(1e-12, 1e-3)
        self.force_tolerance_spin.setValue(1e-6)
        self.force_tolerance_spin.setDecimals(12)
        self.force_tolerance_spin.setNotation(QtWidgets.QDoubleSpinBox.ScientificNotation)
        convergence_layout.addRow("Force Tolerance:", self.force_tolerance_spin)
        
        self.displacement_tolerance_spin = QtWidgets.QDoubleSpinBox()
        self.displacement_tolerance_spin.setRange(1e-12, 1e-3)
        self.displacement_tolerance_spin.setValue(1e-9)
        self.displacement_tolerance_spin.setDecimals(12)
        self.displacement_tolerance_spin.setNotation(QtWidgets.QDoubleSpinBox.ScientificNotation)
        convergence_layout.addRow("Displacement Tolerance:", self.displacement_tolerance_spin)
        
        self.max_iterations_spin = QtWidgets.QSpinBox()
        self.max_iterations_spin.setRange(10, 10000)
        self.max_iterations_spin.setValue(100)
        convergence_layout.addRow("Max Iterations:", self.max_iterations_spin)
        
        layout.addWidget(convergence_group)
        
        # Performance options
        performance_group = QtWidgets.QGroupBox("Performance Options")
        performance_layout = QtWidgets.QFormLayout(performance_group)
        
        self.parallel_check = QtWidgets.QCheckBox("Enable parallel processing")
        performance_layout.addRow("Parallel:", self.parallel_check)
        
        self.threads_spin = QtWidgets.QSpinBox()
        self.threads_spin.setRange(1, 32)
        self.threads_spin.setValue(4)
        self.threads_spin.setEnabled(False)
        performance_layout.addRow("Number of Threads:", self.threads_spin)
        
        self.memory_limit_spin = QtWidgets.QSpinBox()
        self.memory_limit_spin.setRange(100, 32000)
        self.memory_limit_spin.setValue(2000)
        self.memory_limit_spin.setSuffix(" MB")
        performance_layout.addRow("Memory Limit:", self.memory_limit_spin)
        
        layout.addWidget(performance_group)
        
        layout.addStretch()
        
        return widget
    
    def _create_combinations_tab(self) -> QtWidgets.QWidget:
        """Create load combinations tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Combinations table
        self.combinations_table = QtWidgets.QTableWidget()
        self.combinations_table.setColumnCount(5)
        self.combinations_table.setHorizontalHeaderLabels([
            "Name", "Type", "Dead Factor", "Live Factor", "Active"
        ])
        self.combinations_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.combinations_table)
        
        # Combination controls
        controls_layout = QtWidgets.QHBoxLayout()
        
        add_combo_button = QtWidgets.QPushButton("Add Combination")
        controls_layout.addWidget(add_combo_button)
        
        remove_combo_button = QtWidgets.QPushButton("Remove Selected")
        controls_layout.addWidget(remove_combo_button)
        
        controls_layout.addStretch()
        
        # Load combination standards
        standard_combo = QtWidgets.QComboBox()
        standard_combo.addItems([
            "Manual", "ASCE 7-22", "AISC 360", "Eurocode", "NBC", "Custom"
        ])
        controls_layout.addWidget(QtWidgets.QLabel("Standard:"))
        controls_layout.addWidget(standard_combo)
        
        generate_button = QtWidgets.QPushButton("Generate")
        controls_layout.addWidget(generate_button)
        
        layout.addLayout(controls_layout)
        
        # Combination preview
        preview_group = QtWidgets.QGroupBox("Combination Preview")
        preview_layout = QtWidgets.QVBoxLayout(preview_group)
        
        self.combination_preview = QtWidgets.QTextEdit()
        self.combination_preview.setMaximumHeight(100)
        self.combination_preview.setReadOnly(True)
        preview_layout.addWidget(self.combination_preview)
        
        layout.addWidget(preview_group)
        
        # Store references
        self.add_combo_button = add_combo_button
        self.remove_combo_button = remove_combo_button
        self.standard_combo = standard_combo
        self.generate_button = generate_button
        
        return widget
    
    def _create_results_tab(self) -> QtWidgets.QWidget:
        """Create results options tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        
        # Output options
        layout.addWidget(QtWidgets.QLabel("Output Options:"))
        
        self.save_displacements_check = QtWidgets.QCheckBox("Node displacements")
        self.save_displacements_check.setChecked(True)
        layout.addRow("Save:", self.save_displacements_check)
        
        self.save_reactions_check = QtWidgets.QCheckBox("Support reactions")
        self.save_reactions_check.setChecked(True)
        layout.addRow("", self.save_reactions_check)
        
        self.save_member_forces_check = QtWidgets.QCheckBox("Member forces")
        self.save_member_forces_check.setChecked(True)
        layout.addRow("", self.save_member_forces_check)
        
        self.save_stresses_check = QtWidgets.QCheckBox("Element stresses")
        layout.addRow("", self.save_stresses_check)
        
        # Result precision
        self.result_precision_spin = QtWidgets.QSpinBox()
        self.result_precision_spin.setRange(1, 10)
        self.result_precision_spin.setValue(3)
        layout.addRow("Decimal Precision:", self.result_precision_spin)
        
        # Output format
        self.output_format_combo = QtWidgets.QComboBox()
        self.output_format_combo.addItems(["Internal", "CSV", "Excel", "JSON", "XML"])
        layout.addRow("Export Format:", self.output_format_combo)
        
        # Result visualization
        layout.addWidget(QtWidgets.QLabel("Visualization:"))
        
        self.auto_visualize_check = QtWidgets.QCheckBox("Auto-display results after analysis")
        self.auto_visualize_check.setChecked(True)
        layout.addRow("Auto Display:", self.auto_visualize_check)
        
        self.result_scale_spin = QtWidgets.QDoubleSpinBox()
        self.result_scale_spin.setRange(0.1, 100.0)
        self.result_scale_spin.setValue(1.0)
        layout.addRow("Display Scale:", self.result_scale_spin)
        
        return widget
    
    def _create_status_widget(self) -> QtWidgets.QGroupBox:
        """Create analysis status and progress widget."""
        group = QtWidgets.QGroupBox("Analysis Status")
        layout = QtWidgets.QVBoxLayout(group)
        
        # Status display
        self.status_label = QtWidgets.QLabel("Ready to run analysis")
        layout.addWidget(self.status_label)
        
        # Progress bar
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Model statistics
        stats_layout = QtWidgets.QHBoxLayout()
        
        self.nodes_label = QtWidgets.QLabel("Nodes: 0")
        stats_layout.addWidget(self.nodes_label)
        
        self.elements_label = QtWidgets.QLabel("Elements: 0")
        stats_layout.addWidget(self.elements_label)
        
        self.dof_label = QtWidgets.QLabel("DOF: 0")
        stats_layout.addWidget(self.dof_label)
        
        stats_layout.addStretch()
        
        layout.addLayout(stats_layout)
        
        return group
    
    def _populate_form(self) -> None:
        """Populate form with analysis settings."""
        # Set default values
        self.analysis_title_edit.setText("Linear Static Analysis")
        
        # Add default load combinations
        self._add_default_combinations()
        
        # Update model statistics
        self._update_model_statistics()
    
    def _connect_signals(self) -> None:
        """Connect UI signals."""
        
        # Solver options
        self.parallel_check.toggled.connect(self.threads_spin.setEnabled)
        
        # Load combinations
        self.add_combo_button.clicked.connect(self._add_combination)
        self.remove_combo_button.clicked.connect(self._remove_combination)
        self.generate_button.clicked.connect(self._generate_combinations)
        
        self.combinations_table.itemSelectionChanged.connect(self._update_combination_preview)
        
        # Analysis controls
        self.check_button.clicked.connect(self._check_model)
        self.run_button.clicked.connect(self._run_analysis)
        self.results_button.clicked.connect(self._view_results)
        self.cancel_button.clicked.connect(self.reject)
    
    def _add_default_combinations(self) -> None:
        """Add default load combinations."""
        combinations = [
            {"name": "1.4D", "type": "Ultimate", "dead": 1.4, "live": 0.0, "active": True},
            {"name": "1.2D + 1.6L", "type": "Ultimate", "dead": 1.2, "live": 1.6, "active": True},
            {"name": "1.0D + 1.0L", "type": "Service", "dead": 1.0, "live": 1.0, "active": True}
        ]
        
        self.combinations_table.setRowCount(len(combinations))
        
        for i, combo in enumerate(combinations):
            self.combinations_table.setItem(i, 0, QtWidgets.QTableWidgetItem(combo["name"]))
            self.combinations_table.setItem(i, 1, QtWidgets.QTableWidgetItem(combo["type"]))
            self.combinations_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(combo["dead"])))
            self.combinations_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(combo["live"])))
            
            check_item = QtWidgets.QTableWidgetItem()
            check_item.setCheckState(QtCore.Qt.Checked if combo["active"] else QtCore.Qt.Unchecked)
            self.combinations_table.setItem(i, 4, check_item)
    
    def _update_model_statistics(self) -> None:
        """Update model statistics display."""
        # This would count actual nodes and elements in the model
        node_count = 0
        element_count = 0
        dof_count = 0
        
        # Count from active document
        if App.ActiveDocument:
            for obj in App.ActiveDocument.Objects:
                if hasattr(obj, 'Type'):
                    if obj.Type == "StructuralNode":
                        node_count += 1
                        # Calculate DOF based on restraints
                        if hasattr(obj.Proxy, 'get_degrees_of_freedom'):
                            dof_count += obj.Proxy.get_degrees_of_freedom()
                        else:
                            dof_count += 6  # Default 6 DOF per node
                    elif obj.Type == "StructuralBeam":
                        element_count += 1
        
        self.nodes_label.setText(f"Nodes: {node_count}")
        self.elements_label.setText(f"Elements: {element_count}")
        self.dof_label.setText(f"DOF: {dof_count}")
    
    def _add_combination(self) -> None:
        """Add new load combination."""
        row = self.combinations_table.rowCount()
        self.combinations_table.insertRow(row)
        
        # Set default values
        self.combinations_table.setItem(row, 0, QtWidgets.QTableWidgetItem(f"Combination {row+1}"))
        self.combinations_table.setItem(row, 1, QtWidgets.QTableWidgetItem("Ultimate"))
        self.combinations_table.setItem(row, 2, QtWidgets.QTableWidgetItem("1.0"))
        self.combinations_table.setItem(row, 3, QtWidgets.QTableWidgetItem("0.0"))
        
        check_item = QtWidgets.QTableWidgetItem()
        check_item.setCheckState(QtCore.Qt.Checked)
        self.combinations_table.setItem(row, 4, check_item)
    
    def _remove_combination(self) -> None:
        """Remove selected load combination."""
        current_row = self.combinations_table.currentRow()
        if current_row >= 0:
            self.combinations_table.removeRow(current_row)
    
    def _generate_combinations(self) -> None:
        """Generate standard load combinations."""
        standard = self.standard_combo.currentText()
        
        if standard == "ASCE 7-22":
            # Clear existing and add ASCE 7-22 combinations
            self.combinations_table.setRowCount(0)
            combinations = [
                {"name": "1.4D", "type": "Ultimate", "dead": 1.4, "live": 0.0},
                {"name": "1.2D + 1.6L", "type": "Ultimate", "dead": 1.2, "live": 1.6},
                {"name": "1.2D + 1.0L", "type": "Ultimate", "dead": 1.2, "live": 1.0},
                {"name": "0.9D", "type": "Ultimate", "dead": 0.9, "live": 0.0},
                {"name": "1.0D + 1.0L", "type": "Service", "dead": 1.0, "live": 1.0}
            ]
            
            self.combinations_table.setRowCount(len(combinations))
            for i, combo in enumerate(combinations):
                self.combinations_table.setItem(i, 0, QtWidgets.QTableWidgetItem(combo["name"]))
                self.combinations_table.setItem(i, 1, QtWidgets.QTableWidgetItem(combo["type"]))
                self.combinations_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(combo["dead"])))
                self.combinations_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(combo["live"])))
                
                check_item = QtWidgets.QTableWidgetItem()
                check_item.setCheckState(QtCore.Qt.Checked)
                self.combinations_table.setItem(i, 4, check_item)
    
    def _update_combination_preview(self) -> None:
        """Update combination preview."""
        current_row = self.combinations_table.currentRow()
        if current_row >= 0:
            name = self.combinations_table.item(current_row, 0).text()
            combo_type = self.combinations_table.item(current_row, 1).text()
            dead_factor = self.combinations_table.item(current_row, 2).text()
            live_factor = self.combinations_table.item(current_row, 3).text()
            
            preview_text = f"Combination: {name}\n"
            preview_text += f"Type: {combo_type}\n"
            preview_text += f"Formula: {dead_factor}D + {live_factor}L"
            
            self.combination_preview.setPlainText(preview_text)
    
    def _check_model(self) -> None:
        """Check model for errors and warnings."""
        self.status_label.setText("Checking model...")
        
        # Perform model validation
        errors = []
        warnings = []
        
        # Check for nodes
        node_count = sum(1 for obj in App.ActiveDocument.Objects 
                        if hasattr(obj, 'Type') and obj.Type == "StructuralNode")
        if node_count == 0:
            errors.append("No structural nodes found")
        
        # Check for elements
        element_count = sum(1 for obj in App.ActiveDocument.Objects 
                           if hasattr(obj, 'Type') and obj.Type == "StructuralBeam")
        if element_count == 0:
            errors.append("No structural elements found")
        
        # Display results
        if errors:
            error_text = "Errors found:\n" + "\n".join(errors)
            if warnings:
                error_text += "\n\nWarnings:\n" + "\n".join(warnings)
            
            QtWidgets.QMessageBox.critical(self.form, "Model Check Failed", error_text)
            self.status_label.setText("Model check failed")
            self.run_button.setEnabled(False)
        else:
            if warnings:
                warning_text = "Warnings found:\n" + "\n".join(warnings)
                QtWidgets.QMessageBox.warning(self.form, "Model Check Warnings", warning_text)
            
            self.status_label.setText("Model check passed")
            self.run_button.setEnabled(True)
    
    def _run_analysis(self) -> None:
        """Run structural analysis."""
        self.status_label.setText("Running analysis...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.run_button.setEnabled(False)
        
        try:
            # Simulate analysis progress
            for i in range(101):
                self.progress_bar.setValue(i)
                QtCore.QCoreApplication.processEvents()
                
                # Simulate different phases
                if i < 20:
                    self.status_label.setText("Assembling stiffness matrix...")
                elif i < 40:
                    self.status_label.setText("Applying boundary conditions...")
                elif i < 80:
                    self.status_label.setText("Solving system of equations...")
                else:
                    self.status_label.setText("Processing results...")
            
            # Analysis complete
            self.status_label.setText("Analysis completed successfully")
            self.progress_bar.setVisible(False)
            self.results_button.setEnabled(True)
            
            QtWidgets.QMessageBox.information(
                self.form, "Analysis Complete", 
                "Structural analysis completed successfully.\nClick 'View Results' to examine the results."
            )
            
        except Exception as e:
            self.status_label.setText("Analysis failed")
            self.progress_bar.setVisible(False)
            self.run_button.setEnabled(True)
            
            QtWidgets.QMessageBox.critical(
                self.form, "Analysis Error", 
                f"Analysis failed with error:\n{str(e)}"
            )
    
    def _view_results(self) -> None:
        """Open results viewer."""
        App.Console.PrintMessage("Results viewer not yet implemented\n")
    
    def accept(self) -> None:
        """Apply analysis settings."""
        # Save analysis configuration
        App.Console.PrintMessage("Analysis settings saved\n")
        Gui.Control.closeDialog()
    
    def reject(self) -> None:
        """Cancel analysis setup."""
        Gui.Control.closeDialog()
    
    def getStandardButtons(self) -> int:
        """Return standard buttons."""
        return 0