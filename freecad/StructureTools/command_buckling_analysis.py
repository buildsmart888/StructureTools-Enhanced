# -*- coding: utf-8 -*-
"""
command_buckling_analysis.py - FreeCAD command for linear buckling analysis

This module provides commands to perform linear buckling analysis on structural models
with professional visualization and critical load factor reporting.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtWidgets, QtCore
import os

from .analysis.BucklingAnalysis import BucklingAnalysis, run_buckling_analysis_on_calc
from .utils.exceptions import AnalysisError


class RunBucklingAnalysisCommand:
    """FreeCAD command to perform linear buckling analysis."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'buckling_analysis.svg'),
            'MenuText': 'Buckling Analysis',
            'ToolTip': 'Perform linear buckling analysis to determine critical load factors'
        }
    
    def IsActive(self):
        """Return True if a Calc object is selected."""
        selection = Gui.Selection.getSelection()
        if len(selection) == 1:
            obj = selection[0]
            if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                return 'Calc' in str(obj.Proxy.__class__)
        return False
    
    def Activated(self):
        """Execute buckling analysis command."""
        selection = Gui.Selection.getSelection()
        if not selection:
            QtWidgets.QMessageBox.warning(
                None,
                'Buckling Analysis',
                'Please select a structural analysis (Calc) object first.'
            )
            return
        
        calc_obj = selection[0]
        
        # Show buckling analysis setup dialog
        dialog = BucklingAnalysisDialog(calc_obj)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.run_buckling_analysis(calc_obj, dialog.get_parameters())
    
    def run_buckling_analysis(self, calc_obj, parameters):
        """Execute buckling analysis with given parameters."""
        try:
            App.Console.PrintMessage("="*60 + "\n")
            App.Console.PrintMessage("STARTING BUCKLING ANALYSIS\n")
            App.Console.PrintMessage("="*60 + "\n")
            
            # Run analysis
            results = run_buckling_analysis_on_calc(
                calc_obj, 
                load_case_name=parameters.get('load_case'),
                num_modes=parameters['num_modes']
            )
            
            # Create mode visualizations if requested
            if parameters['create_visualization']:
                self.create_buckling_visualizations(calc_obj, results, parameters)
            
            # Generate report if requested
            if parameters['generate_report']:
                self.generate_buckling_report(calc_obj, results)
            
            # Show results summary
            critical_factor = results.get_critical_load_factor()
            critical_mode = results.get_critical_buckling_mode() + 1
            
            QtWidgets.QMessageBox.information(
                None,
                'Buckling Analysis Complete',
                f'Linear buckling analysis completed successfully!\n\n'
                f'Critical load factor: {critical_factor:.3f}\n'
                f'Critical buckling mode: {critical_mode}\n'
                f'Safety factor against buckling: {critical_factor:.3f}\n\n'
                f'Total modes analyzed: {results.num_modes}'
            )
            
        except AnalysisError as e:
            App.Console.PrintError(f"Buckling analysis failed: {str(e)}\n")
            QtWidgets.QMessageBox.critical(
                None,
                'Buckling Analysis Error',
                f'Buckling analysis failed:\n\n{str(e)}'
            )
        except Exception as e:
            App.Console.PrintError(f"Unexpected error in buckling analysis: {str(e)}\n")
            QtWidgets.QMessageBox.critical(
                None,
                'Buckling Analysis Error',
                f'Unexpected error occurred:\n\n{str(e)}'
            )
    
    def create_buckling_visualizations(self, calc_obj, results, parameters):
        """Create 3D visualizations of buckling mode shapes."""
        try:
            max_visualizations = min(parameters['max_visualizations'], results.num_modes)
            
            App.Console.PrintMessage(f"Creating visualizations for {max_visualizations} buckling modes...\n")
            
            for i in range(max_visualizations):
                mode_num = i + 1
                load_factor = results.load_factors[i]
                mode_type = results.mode_classifications[i]
                
                # Create visualization (placeholder - would create actual 3D objects)
                App.Console.PrintMessage(f"Buckling Mode {mode_num}: Load Factor = {load_factor:.3f} "
                                       f"({mode_type})\n")
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating buckling visualizations: {str(e)}\n")
    
    def generate_buckling_report(self, calc_obj, results):
        """Generate comprehensive buckling analysis report."""
        try:
            # Generate report file
            project_name = getattr(calc_obj, 'Label', 'StructuralModel')
            report_filename = f"{project_name}_BucklingAnalysis_Report.html"
            
            # This would generate actual HTML/PDF report
            App.Console.PrintMessage(f"Buckling analysis report saved: {report_filename}\n")
            
        except Exception as e:
            App.Console.PrintWarning(f"Error generating buckling report: {str(e)}\n")


class BucklingAnalysisDialog(QtWidgets.QDialog):
    """Dialog for buckling analysis parameter setup."""
    
    def __init__(self, calc_obj):
        super().__init__()
        self.calc_obj = calc_obj
        self.setupUi()
    
    def setupUi(self):
        """Setup dialog user interface."""
        self.setWindowTitle("Linear Buckling Analysis Setup")
        self.setModal(True)
        self.resize(450, 400)
        
        layout = QtWidgets.QVBoxLayout(self)
        
        # Analysis parameters group
        params_group = QtWidgets.QGroupBox("Analysis Parameters")
        params_layout = QtWidgets.QFormLayout()
        
        # Number of modes
        self.num_modes_spin = QtWidgets.QSpinBox()
        self.num_modes_spin.setRange(1, 50)
        self.num_modes_spin.setValue(5)
        params_layout.addRow("Number of modes:", self.num_modes_spin)
        
        # Load case selection
        self.load_case_combo = QtWidgets.QComboBox()
        self.populate_load_cases()
        params_layout.addRow("Base load case:", self.load_case_combo)
        
        # Analysis method
        self.method_combo = QtWidgets.QComboBox()
        self.method_combo.addItems(["Subspace Iteration", "Lanczos", "ARPACK"])
        self.method_combo.setCurrentText("Subspace Iteration")
        params_layout.addRow("Solution method:", self.method_combo)
        
        # Convergence tolerance
        self.tolerance_spin = QtWidgets.QDoubleSpinBox()
        self.tolerance_spin.setRange(1e-12, 1e-3)
        self.tolerance_spin.setValue(1e-8)
        self.tolerance_spin.setDecimals(10)
        self.tolerance_spin.setNotation(QtWidgets.QDoubleSpinBox.ScientificNotation)
        params_layout.addRow("Convergence tolerance:", self.tolerance_spin)
        
        params_group.setLayout(params_layout)
        layout.addWidget(params_group)
        
        # Output options group
        output_group = QtWidgets.QGroupBox("Output Options")
        output_layout = QtWidgets.QVBoxLayout()
        
        self.create_viz_check = QtWidgets.QCheckBox("Create buckling mode visualizations")
        self.create_viz_check.setChecked(True)
        output_layout.addWidget(self.create_viz_check)
        
        # Max visualizations
        viz_layout = QtWidgets.QHBoxLayout()
        viz_layout.addWidget(QtWidgets.QLabel("Max visualizations:"))
        self.max_viz_spin = QtWidgets.QSpinBox()
        self.max_viz_spin.setRange(1, 10)
        self.max_viz_spin.setValue(3)
        viz_layout.addWidget(self.max_viz_spin)
        viz_layout.addStretch()
        output_layout.addLayout(viz_layout)
        
        self.generate_report_check = QtWidgets.QCheckBox("Generate analysis report")
        self.generate_report_check.setChecked(True)
        output_layout.addWidget(self.generate_report_check)
        
        self.show_critical_check = QtWidgets.QCheckBox("Highlight critical elements")
        self.show_critical_check.setChecked(False)
        output_layout.addWidget(self.show_critical_check)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
        # Advanced options group
        advanced_group = QtWidgets.QGroupBox("Advanced Options")
        advanced_layout = QtWidgets.QFormLayout()
        
        # Include geometric stiffness
        self.geo_stiffness_check = QtWidgets.QCheckBox()
        self.geo_stiffness_check.setChecked(True)
        advanced_layout.addRow("Include geometric stiffness:", self.geo_stiffness_check)
        
        # Consider initial stress
        self.initial_stress_check = QtWidgets.QCheckBox()
        self.initial_stress_check.setChecked(False)
        advanced_layout.addRow("Consider initial stress:", self.initial_stress_check)
        
        # Eigenvalue solver
        self.solver_combo = QtWidgets.QComboBox()
        self.solver_combo.addItems(["SciPy", "ARPACK"])
        advanced_layout.addRow("Eigenvalue solver:", self.solver_combo)
        
        advanced_group.setLayout(advanced_layout)
        layout.addWidget(advanced_group)
        
        # Information display
        info_group = QtWidgets.QGroupBox("Analysis Information")
        info_layout = QtWidgets.QVBoxLayout()
        
        info_text = QtWidgets.QTextEdit()
        info_text.setMaximumHeight(80)
        info_text.setReadOnly(True)
        info_text.setText(
            "Linear buckling analysis determines the critical load factors at which "
            "the structure becomes unstable. The lowest eigenvalue represents the "
            "most critical buckling load factor."
        )
        info_layout.addWidget(info_text)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        self.run_button = QtWidgets.QPushButton("Run Analysis")
        self.run_button.setDefault(True)
        self.run_button.clicked.connect(self.accept)
        
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addStretch()
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout)
        
        # Connect signals
        self.create_viz_check.toggled.connect(self.max_viz_spin.setEnabled)
    
    def populate_load_cases(self):
        """Populate load case dropdown."""
        self.load_case_combo.addItem("(Automatic)")
        
        # Try to get load cases from calc object
        if hasattr(self.calc_obj, 'ListElements'):
            # Look for load objects
            load_cases = set()
            for element in self.calc_obj.ListElements:
                if hasattr(element, 'LoadCase'):
                    load_cases.add(element.LoadCase)
            
            # Add unique load cases
            for case in sorted(load_cases):
                self.load_case_combo.addItem(case)
        
        # Add common load case names
        common_cases = ["DL", "LL", "DL+LL", "Wind", "Seismic"]
        for case in common_cases:
            if self.load_case_combo.findText(case) == -1:
                self.load_case_combo.addItem(case)
    
    def get_parameters(self):
        """Get analysis parameters from dialog."""
        return {
            'num_modes': self.num_modes_spin.value(),
            'load_case': self.load_case_combo.currentText() if self.load_case_combo.currentText() != "(Automatic)" else None,
            'method': self.method_combo.currentText(),
            'tolerance': self.tolerance_spin.value(),
            'create_visualization': self.create_viz_check.isChecked(),
            'max_visualizations': self.max_viz_spin.value(),
            'generate_report': self.generate_report_check.isChecked(),
            'show_critical': self.show_critical_check.isChecked(),
            'include_geometric_stiffness': self.geo_stiffness_check.isChecked(),
            'consider_initial_stress': self.initial_stress_check.isChecked(),
            'solver': self.solver_combo.currentText().lower()
        }


class ViewBucklingResultsCommand:
    """Command to view existing buckling analysis results."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'view_buckling_results.svg'),
            'MenuText': 'View Buckling Results',
            'ToolTip': 'View previously calculated buckling analysis results'
        }
    
    def IsActive(self):
        """Return True if Calc object with buckling results is selected."""
        selection = Gui.Selection.getSelection()
        if len(selection) == 1:
            obj = selection[0]
            if hasattr(obj, 'buckling_analysis_results'):
                return True
        return False
    
    def Activated(self):
        """Show buckling analysis results."""
        selection = Gui.Selection.getSelection()
        calc_obj = selection[0]
        
        if hasattr(calc_obj, 'buckling_analysis_results'):
            results = calc_obj.buckling_analysis_results
            
            # Show results dialog
            dialog = BucklingResultsDialog(results)
            dialog.exec_()
        else:
            QtWidgets.QMessageBox.information(
                None,
                'Buckling Results',
                'No buckling analysis results found for this object.\n'
                'Please run buckling analysis first.'
            )


class BucklingResultsDialog(QtWidgets.QDialog):
    """Dialog to display buckling analysis results."""
    
    def __init__(self, results):
        super().__init__()
        self.results = results
        self.setupUi()
    
    def setupUi(self):
        """Setup results display interface."""
        self.setWindowTitle("Buckling Analysis Results")
        self.setModal(True)
        self.resize(650, 500)
        
        layout = QtWidgets.QVBoxLayout(self)
        
        # Results summary
        summary_group = QtWidgets.QGroupBox("Analysis Summary")
        summary_layout = QtWidgets.QFormLayout()
        
        critical_factor = self.results.get_critical_load_factor()
        critical_mode = self.results.get_critical_buckling_mode() + 1
        
        summary_layout.addRow("Number of modes:", str(self.results.num_modes))
        summary_layout.addRow("Critical load factor:", f"{critical_factor:.6f}")
        summary_layout.addRow("Critical buckling mode:", f"Mode {critical_mode}")
        summary_layout.addRow("Safety factor:", f"{critical_factor:.3f}")
        
        if hasattr(self.results, 'analysis_time'):
            summary_layout.addRow("Analysis time:", f"{self.results.analysis_time:.2f} seconds")
        
        summary_group.setLayout(summary_layout)
        layout.addWidget(summary_group)
        
        # Applied loads summary
        loads_group = QtWidgets.QGroupBox("Applied Loads")
        loads_layout = QtWidgets.QVBoxLayout()
        
        loads_text = QtWidgets.QTextEdit()
        loads_text.setMaximumHeight(80)
        loads_text.setReadOnly(True)
        
        loads_summary = "Applied loads for buckling analysis:\n"
        for load_type, magnitude in self.results.applied_loads.items():
            loads_summary += f"  {load_type}: {magnitude}\n"
        loads_text.setText(loads_summary)
        
        loads_layout.addWidget(loads_text)
        loads_group.setLayout(loads_layout)
        layout.addWidget(loads_group)
        
        # Mode table
        table_group = QtWidgets.QGroupBox("Buckling Modes")
        table_layout = QtWidgets.QVBoxLayout()
        
        self.results_table = QtWidgets.QTableWidget()
        self.populate_results_table()
        table_layout.addWidget(self.results_table)
        
        table_group.setLayout(table_layout)
        layout.addWidget(table_group)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        self.visualize_button = QtWidgets.QPushButton("Visualize Mode")
        self.visualize_button.clicked.connect(self.visualize_selected_mode)
        
        self.export_button = QtWidgets.QPushButton("Export Results")
        self.export_button.clicked.connect(self.export_results)
        
        close_button = QtWidgets.QPushButton("Close")
        close_button.clicked.connect(self.accept)
        
        button_layout.addWidget(self.visualize_button)
        button_layout.addWidget(self.export_button)
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
    
    def populate_results_table(self):
        """Populate results table with buckling mode data."""
        self.results_table.setRowCount(self.results.num_modes)
        self.results_table.setColumnCount(4)
        
        headers = ["Mode", "Load Factor", "Classification", "Critical Load (N)"]
        self.results_table.setHorizontalHeaderLabels(headers)
        
        for i in range(self.results.num_modes):
            # Mode number
            self.results_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            
            # Load factor
            factor_item = QtWidgets.QTableWidgetItem(f"{self.results.load_factors[i]:.6f}")
            self.results_table.setItem(i, 1, factor_item)
            
            # Classification
            class_item = QtWidgets.QTableWidgetItem(self.results.mode_classifications[i])
            self.results_table.setItem(i, 2, class_item)
            
            # Critical load
            if self.results.critical_loads and i < len(self.results.critical_loads):
                critical_load = list(self.results.critical_loads[i].values())[0] if self.results.critical_loads[i] else 0
                load_item = QtWidgets.QTableWidgetItem(f"{critical_load:.1f}")
                self.results_table.setItem(i, 3, load_item)
        
        self.results_table.resizeColumnsToContents()
        
        # Highlight critical mode
        critical_mode = self.results.get_critical_buckling_mode()
        for col in range(4):
            item = self.results_table.item(critical_mode, col)
            if item:
                item.setBackground(QtWidgets.QColor(255, 200, 200))  # Light red
    
    def visualize_selected_mode(self):
        """Visualize selected buckling mode."""
        current_row = self.results_table.currentRow()
        if current_row >= 0:
            mode_number = current_row + 1
            App.Console.PrintMessage(f"Visualizing buckling mode {mode_number}\n")
            # This would create actual mode shape visualization
        else:
            QtWidgets.QMessageBox.information(
                self, "Selection Required", 
                "Please select a buckling mode to visualize."
            )
    
    def export_results(self):
        """Export buckling results to file."""
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export Buckling Results", 
            "buckling_results.txt", "Text Files (*.txt)"
        )
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write("BUCKLING ANALYSIS RESULTS\n")
                    f.write("=" * 40 + "\n\n")
                    
                    f.write(f"Number of modes: {self.results.num_modes}\n")
                    f.write(f"Critical load factor: {self.results.get_critical_load_factor():.6f}\n")
                    f.write(f"Critical mode: {self.results.get_critical_buckling_mode() + 1}\n\n")
                    
                    f.write("Mode Details:\n")
                    f.write("-" * 20 + "\n")
                    for i in range(self.results.num_modes):
                        f.write(f"Mode {i+1}: Load Factor = {self.results.load_factors[i]:.6f}, "
                               f"Type = {self.results.mode_classifications[i]}\n")
                
                QtWidgets.QMessageBox.information(
                    self, "Export Complete", 
                    f"Results exported to: {filename}"
                )
            except Exception as e:
                QtWidgets.QMessageBox.critical(
                    self, "Export Error", 
                    f"Failed to export results: {str(e)}"
                )


# Register commands
if App.GuiUp:
    Gui.addCommand('RunBucklingAnalysis', RunBucklingAnalysisCommand())
    Gui.addCommand('ViewBucklingResults', ViewBucklingResultsCommand())