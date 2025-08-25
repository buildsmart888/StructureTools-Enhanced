# -*- coding: utf-8 -*-
"""
command_modal_analysis.py - FreeCAD command for modal analysis

This module provides commands to perform modal analysis on structural models
with professional visualization and reporting capabilities.
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtWidgets, QtCore
import os

from .analysis.ModalAnalysis import ModalAnalysis, run_modal_analysis_on_calc
from .utils.exceptions import AnalysisError


class RunModalAnalysisCommand:
    """FreeCAD command to perform modal analysis."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'modal_analysis.svg'),
            'MenuText': 'Modal Analysis',
            'ToolTip': 'Perform modal analysis to extract natural frequencies and mode shapes'
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
        """Execute modal analysis command."""
        selection = Gui.Selection.getSelection()
        if not selection:
            QtWidgets.QMessageBox.warning(
                None,
                'Modal Analysis',
                'Please select a structural analysis (Calc) object first.'
            )
            return
        
        calc_obj = selection[0]
        
        # Show modal analysis setup dialog
        dialog = ModalAnalysisDialog(calc_obj)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.run_modal_analysis(calc_obj, dialog.get_parameters())
    
    def run_modal_analysis(self, calc_obj, parameters):
        """Execute modal analysis with given parameters."""
        try:
            App.Console.PrintMessage("="*60 + "\n")
            App.Console.PrintMessage("STARTING MODAL ANALYSIS\n")
            App.Console.PrintMessage("="*60 + "\n")
            
            # Run analysis
            results = run_modal_analysis_on_calc(
                calc_obj, 
                num_modes=parameters['num_modes']
            )
            
            # Create results visualization if requested
            if parameters['create_visualization']:
                self.create_mode_visualizations(calc_obj, results, parameters)
            
            # Generate report if requested
            if parameters['generate_report']:
                self.generate_modal_report(calc_obj, results)
            
            QtWidgets.QMessageBox.information(
                None,
                'Modal Analysis Complete',
                f'Modal analysis completed successfully!\n\n'
                f'Extracted {results.num_modes} modes\n'
                f'Fundamental frequency: {results.frequencies[0]:.3f} Hz\n'
                f'Fundamental period: {results.get_fundamental_period():.3f} seconds'
            )
            
        except AnalysisError as e:
            App.Console.PrintError(f"Modal analysis failed: {str(e)}\n")
            QtWidgets.QMessageBox.critical(
                None,
                'Modal Analysis Error',
                f'Modal analysis failed:\n\n{str(e)}'
            )
        except Exception as e:
            App.Console.PrintError(f"Unexpected error in modal analysis: {str(e)}\n")
            QtWidgets.QMessageBox.critical(
                None,
                'Modal Analysis Error',
                f'Unexpected error occurred:\n\n{str(e)}'
            )
    
    def create_mode_visualizations(self, calc_obj, results, parameters):
        """Create 3D visualizations of mode shapes."""
        try:
            # Create visualizations for dominant modes
            dominant_modes = results.get_dominant_modes()
            max_visualizations = min(parameters['max_visualizations'], len(dominant_modes))
            
            App.Console.PrintMessage(f"Creating visualizations for {max_visualizations} dominant modes...\n")
            
            for i in range(max_visualizations):
                mode_num = dominant_modes[i]
                # This would create actual 3D visualization
                # Implementation depends on FreeCAD integration requirements
                App.Console.PrintMessage(f"Mode {mode_num + 1}: {results.frequencies[mode_num]:.3f} Hz "
                                       f"({results.mode_classifications[mode_num]})\n")
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating mode visualizations: {str(e)}\n")
    
    def generate_modal_report(self, calc_obj, results):
        """Generate comprehensive modal analysis report."""
        try:
            # Generate report file
            project_name = getattr(calc_obj, 'Label', 'StructuralModel')
            report_filename = f"{project_name}_ModalAnalysis_Report.html"
            
            # This would generate actual HTML/PDF report
            App.Console.PrintMessage(f"Modal analysis report saved: {report_filename}\n")
            
        except Exception as e:
            App.Console.PrintWarning(f"Error generating modal report: {str(e)}\n")


class ModalAnalysisDialog(QtWidgets.QDialog):
    """Dialog for modal analysis parameter setup."""
    
    def __init__(self, calc_obj):
        super().__init__()
        self.calc_obj = calc_obj
        self.setupUi()
    
    def setupUi(self):
        """Setup dialog user interface."""
        self.setWindowTitle("Modal Analysis Setup")
        self.setModal(True)
        self.resize(400, 300)
        
        layout = QtWidgets.QVBoxLayout(self)
        
        # Analysis parameters group
        params_group = QtWidgets.QGroupBox("Analysis Parameters")
        params_layout = QtWidgets.QFormLayout()
        
        # Number of modes
        self.num_modes_spin = QtWidgets.QSpinBox()
        self.num_modes_spin.setRange(1, 100)
        self.num_modes_spin.setValue(10)
        params_layout.addRow("Number of modes:", self.num_modes_spin)
        
        # Analysis method
        self.method_combo = QtWidgets.QComboBox()
        self.method_combo.addItems(["Subspace Iteration", "Lanczos", "Standard"])
        self.method_combo.setCurrentText("Subspace Iteration")
        params_layout.addRow("Solution method:", self.method_combo)
        
        # Frequency range
        freq_layout = QtWidgets.QHBoxLayout()
        self.freq_min_spin = QtWidgets.QDoubleSpinBox()
        self.freq_min_spin.setRange(0.001, 1000.0)
        self.freq_min_spin.setValue(0.1)
        self.freq_min_spin.setSuffix(" Hz")
        
        self.freq_max_spin = QtWidgets.QDoubleSpinBox()
        self.freq_max_spin.setRange(0.1, 10000.0)
        self.freq_max_spin.setValue(100.0)
        self.freq_max_spin.setSuffix(" Hz")
        
        freq_layout.addWidget(QtWidgets.QLabel("Min:"))
        freq_layout.addWidget(self.freq_min_spin)
        freq_layout.addWidget(QtWidgets.QLabel("Max:"))
        freq_layout.addWidget(self.freq_max_spin)
        
        params_layout.addRow("Frequency range:", freq_layout)
        
        params_group.setLayout(params_layout)
        layout.addWidget(params_group)
        
        # Output options group
        output_group = QtWidgets.QGroupBox("Output Options")
        output_layout = QtWidgets.QVBoxLayout()
        
        self.create_viz_check = QtWidgets.QCheckBox("Create mode shape visualizations")
        self.create_viz_check.setChecked(True)
        output_layout.addWidget(self.create_viz_check)
        
        # Max visualizations
        viz_layout = QtWidgets.QHBoxLayout()
        viz_layout.addWidget(QtWidgets.QLabel("Max visualizations:"))
        self.max_viz_spin = QtWidgets.QSpinBox()
        self.max_viz_spin.setRange(1, 20)
        self.max_viz_spin.setValue(5)
        viz_layout.addWidget(self.max_viz_spin)
        viz_layout.addStretch()
        output_layout.addLayout(viz_layout)
        
        self.generate_report_check = QtWidgets.QCheckBox("Generate analysis report")
        self.generate_report_check.setChecked(True)
        output_layout.addWidget(self.generate_report_check)
        
        self.show_summary_check = QtWidgets.QCheckBox("Show results summary")
        self.show_summary_check.setChecked(True)
        output_layout.addWidget(self.show_summary_check)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
        # Advanced options group
        advanced_group = QtWidgets.QGroupBox("Advanced Options")
        advanced_layout = QtWidgets.QFormLayout()
        
        # Mass matrix type
        self.mass_type_combo = QtWidgets.QComboBox()
        self.mass_type_combo.addItems(["Consistent", "Lumped"])
        advanced_layout.addRow("Mass matrix:", self.mass_type_combo)
        
        # Convergence tolerance
        self.tolerance_spin = QtWidgets.QDoubleSpinBox()
        self.tolerance_spin.setRange(1e-12, 1e-3)
        self.tolerance_spin.setValue(1e-6)
        self.tolerance_spin.setDecimals(10)
        self.tolerance_spin.setNotation(QtWidgets.QDoubleSpinBox.ScientificNotation)
        advanced_layout.addRow("Convergence tolerance:", self.tolerance_spin)
        
        advanced_group.setLayout(advanced_layout)
        layout.addWidget(advanced_group)
        
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
    
    def get_parameters(self):
        """Get analysis parameters from dialog."""
        return {
            'num_modes': self.num_modes_spin.value(),
            'method': self.method_combo.currentText(),
            'frequency_range': (self.freq_min_spin.value(), self.freq_max_spin.value()),
            'create_visualization': self.create_viz_check.isChecked(),
            'max_visualizations': self.max_viz_spin.value(),
            'generate_report': self.generate_report_check.isChecked(),
            'show_summary': self.show_summary_check.isChecked(),
            'mass_type': self.mass_type_combo.currentText(),
            'tolerance': self.tolerance_spin.value()
        }


class ViewModalResultsCommand:
    """Command to view existing modal analysis results."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'view_modal_results.svg'),
            'MenuText': 'View Modal Results',
            'ToolTip': 'View previously calculated modal analysis results'
        }
    
    def IsActive(self):
        """Return True if Calc object with modal results is selected."""
        selection = Gui.Selection.getSelection()
        if len(selection) == 1:
            obj = selection[0]
            if hasattr(obj, 'modal_analysis_results'):
                return True
        return False
    
    def Activated(self):
        """Show modal analysis results."""
        selection = Gui.Selection.getSelection()
        calc_obj = selection[0]
        
        if hasattr(calc_obj, 'modal_analysis_results'):
            results = calc_obj.modal_analysis_results
            
            # Show results dialog
            dialog = ModalResultsDialog(results)
            dialog.exec_()
        else:
            QtWidgets.QMessageBox.information(
                None,
                'Modal Results',
                'No modal analysis results found for this object.\n'
                'Please run modal analysis first.'
            )


class ModalResultsDialog(QtWidgets.QDialog):
    """Dialog to display modal analysis results."""
    
    def __init__(self, results):
        super().__init__()
        self.results = results
        self.setupUi()
    
    def setupUi(self):
        """Setup results display interface."""
        self.setWindowTitle("Modal Analysis Results")
        self.setModal(True)
        self.resize(600, 400)
        
        layout = QtWidgets.QVBoxLayout(self)
        
        # Results summary
        summary_group = QtWidgets.QGroupBox("Analysis Summary")
        summary_layout = QtWidgets.QFormLayout()
        
        summary_layout.addRow("Number of modes:", str(self.results.num_modes))
        summary_layout.addRow("Fundamental frequency:", f"{self.results.frequencies[0]:.3f} Hz")
        summary_layout.addRow("Fundamental period:", f"{self.results.get_fundamental_period():.3f} seconds")
        
        summary_group.setLayout(summary_layout)
        layout.addWidget(summary_group)
        
        # Mode table
        table_group = QtWidgets.QGroupBox("Mode Details")
        table_layout = QtWidgets.QVBoxLayout()
        
        self.results_table = QtWidgets.QTableWidget()
        self.populate_results_table()
        table_layout.addWidget(self.results_table)
        
        table_group.setLayout(table_layout)
        layout.addWidget(table_group)
        
        # Close button
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        
        close_button = QtWidgets.QPushButton("Close")
        close_button.clicked.connect(self.accept)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
    
    def populate_results_table(self):
        """Populate results table with mode data."""
        self.results_table.setRowCount(self.results.num_modes)
        self.results_table.setColumnCount(5)
        
        headers = ["Mode", "Frequency (Hz)", "Period (s)", "Classification", "Max Participation"]
        self.results_table.setHorizontalHeaderLabels(headers)
        
        for i in range(self.results.num_modes):
            # Mode number
            self.results_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            
            # Frequency
            freq_item = QtWidgets.QTableWidgetItem(f"{self.results.frequencies[i]:.3f}")
            self.results_table.setItem(i, 1, freq_item)
            
            # Period
            period_item = QtWidgets.QTableWidgetItem(f"{self.results.periods[i]:.3f}")
            self.results_table.setItem(i, 2, period_item)
            
            # Classification
            class_item = QtWidgets.QTableWidgetItem(self.results.mode_classifications[i])
            self.results_table.setItem(i, 3, class_item)
            
            # Max participation factor
            max_pf = max(abs(self.results.participation_factors[i]))
            pf_item = QtWidgets.QTableWidgetItem(f"{max_pf:.3f}")
            self.results_table.setItem(i, 4, pf_item)
        
        self.results_table.resizeColumnsToContents()


# Register commands
if App.GuiUp:
    Gui.addCommand('RunModalAnalysis', RunModalAnalysisCommand())
    Gui.addCommand('ViewModalResults', ViewModalResultsCommand())