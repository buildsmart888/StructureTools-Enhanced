"""
Member Force Panel

UI Panel for displaying member force summary table with filtering and export.
"""

import FreeCAD
import FreeCADGui
import os
import csv
from typing import List, Optional, Any

# PySide imports
try:
    from .qt_compat import QtWidgets, QtCore, QtGui
except ImportError:
    try:
        from PySide import QtWidgets, QtCore, QtGui
    except ImportError as e:
        raise ImportError("Neither PySide2 nor PySide could be imported.") from e

from .member_force_summary import MemberForceSummary, create_member_force_summary

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")


class MemberForcePanel:
    """Panel for displaying member force summary table with export functionality."""
    
    # Table column headers
    HEADERS = ['Type', 'Beam', 'L/C', 'd (m)', 'Fx (kN)', 'Fy (kN)', 'Fz (kN)', 
               'Mx (kN·m)', 'My (kN·m)', 'Mz (kN·m)']
    
    def __init__(self, calc_obj):
        """
        Initialize the panel.
        
        Args:
            calc_obj: FreeCAD Calc object with model attribute
        """
        self.calc_obj = calc_obj
        self.summary = create_member_force_summary(calc_obj)
        self.form = self.create_ui()
        self.populate_filters()
        self.populate_table()
    
    def create_ui(self) -> QtWidgets.QWidget:
        """Create the user interface."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Title
        title = QtWidgets.QLabel("Beam Force Detail Summary")
        title.setStyleSheet("font-size: 14pt; font-weight: bold;")
        layout.addWidget(title)
        
        # Sign convention note
        note = QtWidgets.QLabel(
            "Sign convention: positive above line, negative below line except Fx "
            "where positive is compression. Distance d is given from beam end A."
        )
        note.setWordWrap(True)
        note.setStyleSheet("font-style: italic; color: #666;")
        layout.addWidget(note)
        
        # Filters section
        filter_group = QtWidgets.QGroupBox("Filters")
        filter_layout = QtWidgets.QHBoxLayout(filter_group)
        
        # Load Combination filter
        lc_layout = QtWidgets.QVBoxLayout()
        lc_label = QtWidgets.QLabel("Load Combination:")
        self.combo_filter = QtWidgets.QComboBox()
        self.combo_filter.addItem("All Load Combinations", None)
        lc_layout.addWidget(lc_label)
        lc_layout.addWidget(self.combo_filter)
        filter_layout.addLayout(lc_layout)
        
        # Beam filter
        beam_layout = QtWidgets.QVBoxLayout()
        beam_label = QtWidgets.QLabel("Select Beams:")
        self.beam_list = QtWidgets.QListWidget()
        self.beam_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.beam_list.setMaximumHeight(100)
        
        self.select_all_btn = QtWidgets.QPushButton("Select All")
        self.clear_selection_btn = QtWidgets.QPushButton("Clear")
        
        beam_btn_layout = QtWidgets.QHBoxLayout()
        beam_btn_layout.addWidget(self.select_all_btn)
        beam_btn_layout.addWidget(self.clear_selection_btn)
        
        beam_layout.addWidget(beam_label)
        beam_layout.addWidget(self.beam_list)
        beam_layout.addLayout(beam_btn_layout)
        filter_layout.addLayout(beam_layout)
        
        # Apply filter button
        self.apply_btn = QtWidgets.QPushButton("Apply Filter")
        self.apply_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        filter_layout.addWidget(self.apply_btn)
        
        layout.addWidget(filter_group)
        
        # Results table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(len(self.HEADERS))
        self.table.setHorizontalHeaderLabels(self.HEADERS)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        layout.addWidget(self.table)
        
        # Export section
        export_group = QtWidgets.QGroupBox("Export")
        export_layout = QtWidgets.QHBoxLayout(export_group)
        
        self.export_excel_btn = QtWidgets.QPushButton("Export to Excel")
        self.export_csv_btn = QtWidgets.QPushButton("Export to CSV")
        
        export_layout.addWidget(self.export_excel_btn)
        export_layout.addWidget(self.export_csv_btn)
        export_layout.addStretch()
        
        layout.addWidget(export_group)
        
        # Connect signals
        self.setup_connections()
        
        return widget
    
    def setup_connections(self):
        """Connect UI signals to handlers."""
        self.apply_btn.clicked.connect(self.populate_table)
        self.select_all_btn.clicked.connect(self.select_all_beams)
        self.clear_selection_btn.clicked.connect(self.clear_beam_selection)
        self.export_excel_btn.clicked.connect(lambda: self.export_to_format('excel'))
        self.export_csv_btn.clicked.connect(lambda: self.export_to_format('csv'))
    
    def populate_filters(self):
        """Populate filter dropdowns."""
        if not self.summary:
            return
        
        # Load combinations
        combos = self.summary.get_load_combos()
        for combo in combos:
            self.combo_filter.addItem(combo, combo)
        
        # Members
        members = self.summary.get_member_names()
        for member in members:
            item = QtWidgets.QListWidgetItem(member)
            item.setSelected(True)  # Select all by default
            self.beam_list.addItem(item)
    
    def get_selected_combos(self) -> Optional[List[str]]:
        """Get selected load combinations."""
        combo_data = self.combo_filter.currentData()
        if combo_data is None:
            return None  # All combos
        return [combo_data]
    
    def get_selected_members(self) -> Optional[List[str]]:
        """Get selected member names."""
        selected = self.beam_list.selectedItems()
        if not selected or len(selected) == self.beam_list.count():
            return None  # All members
        return [item.text() for item in selected]
    
    def select_all_beams(self):
        """Select all beams in the list."""
        for i in range(self.beam_list.count()):
            self.beam_list.item(i).setSelected(True)
    
    def clear_beam_selection(self):
        """Clear beam selection."""
        self.beam_list.clearSelection()
    
    def populate_table(self):
        """Populate the table with filtered data."""
        self.table.setRowCount(0)
        
        if not self.summary:
            self.show_no_data_message()
            return
        
        combos = self.get_selected_combos()
        members = self.get_selected_members()
        
        try:
            rows = self.summary.get_summary_table_data(combos, members)
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error getting force data: {str(e)}\n")
            self.show_no_data_message()
            return
        
        if not rows:
            self.show_no_data_message()
            return
        
        self.table.setRowCount(len(rows))
        
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                if col_idx == 0:  # Type column
                    item = QtWidgets.QTableWidgetItem(str(value))
                    # Bold the max/min type
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                elif col_idx in [1, 2]:  # Beam, L/C - string columns
                    item = QtWidgets.QTableWidgetItem(str(value))
                else:  # Numeric columns
                    try:
                        num_val = float(value)
                        # Format with 3 decimal places
                        item = QtWidgets.QTableWidgetItem(f"{num_val:.3f}")
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        
                        # Color code: red for negative, black for positive
                        if num_val < 0:
                            item.setForeground(QtGui.QColor(200, 0, 0))
                    except (ValueError, TypeError):
                        item = QtWidgets.QTableWidgetItem(str(value))
                
                self.table.setItem(row_idx, col_idx, item)
        
        # Resize columns to content
        self.table.resizeColumnsToContents()
    
    def show_no_data_message(self):
        """Show message when no data is available."""
        self.table.setRowCount(1)
        self.table.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem("No analysis data found. Please run analysis first.")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(0, 0, item)
        self.table.horizontalHeader().setVisible(False)
    
    def export_to_format(self, format_type: str):
        """Export table data to specified format."""
        if format_type == 'excel':
            file_filter = "Excel Files (*.xlsx)"
            default_name = "BeamForceSummary.xlsx"
        else:
            file_filter = "CSV Files (*.csv)"
            default_name = "BeamForceSummary.csv"
        
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.form, "Export Data", default_name, file_filter
        )
        
        if not file_path:
            return
        
        try:
            if format_type == 'excel':
                self.export_to_excel(file_path)
            else:
                self.export_to_csv(file_path)
            
            QtWidgets.QMessageBox.information(
                self.form, "Export Successful", 
                f"Data exported successfully to:\n{file_path}"
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self.form, "Export Error", 
                f"Failed to export data:\n{str(e)}"
            )
    
    def export_to_csv(self, file_path: str):
        """Export table data to CSV file."""
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write title
            writer.writerow(['Beam Force Detail Summary'])
            writer.writerow([])
            
            # Write headers
            writer.writerow(self.HEADERS)
            
            # Write data
            for row in range(self.table.rowCount()):
                row_data = []
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    row_data.append(item.text() if item else '')
                writer.writerow(row_data)
    
    def export_to_excel(self, file_path: str):
        """Export table data to Excel file."""
        try:
            from openpyxl import Workbook
            from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
        except ImportError:
            # Fallback to CSV if openpyxl not available
            csv_path = file_path.replace('.xlsx', '.csv')
            self.export_to_csv(csv_path)
            raise ImportError(
                f"openpyxl not installed. Data exported as CSV to: {csv_path}"
            )
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Beam Force Summary"
        
        # Title
        ws['A1'] = "Beam Force Detail Summary"
        ws['A1'].font = Font(bold=True, size=14)
        ws.merge_cells('A1:J1')
        
        # Sign convention note
        ws['A2'] = "Sign convention: positive above line, negative below except Fx where positive is compression"
        ws['A2'].font = Font(italic=True)
        ws.merge_cells('A2:J2')
        
        # Headers
        header_font = Font(bold=True)
        header_fill = PatternFill(start_color="DCDCDC", end_color="DCDCDC", fill_type="solid")
        thin_border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )
        
        for col, header in enumerate(self.HEADERS, 1):
            cell = ws.cell(row=4, column=col, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.border = thin_border
            cell.alignment = Alignment(horizontal='center')
        
        # Data
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                cell = ws.cell(row=row + 5, column=col + 1, value=item.text() if item else '')
                cell.border = thin_border
                
                # Right-align numeric columns
                if col >= 3:
                    cell.alignment = Alignment(horizontal='right')
        
        # Adjust column widths
        for col in range(1, len(self.HEADERS) + 1):
            ws.column_dimensions[chr(64 + col)].width = 12
        
        wb.save(file_path)
    
    def accept(self):
        """Accept and close panel."""
        FreeCADGui.Control.closeDialog()
    
    def reject(self):
        """Reject and close panel."""
        FreeCADGui.Control.closeDialog()
    
    def getStandardButtons(self):
        """Return standard buttons."""
        return int(QtWidgets.QDialogButtonBox.Close)
