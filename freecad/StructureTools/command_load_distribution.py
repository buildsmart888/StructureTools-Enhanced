# -*- coding: utf-8 -*-
"""
command_load_distribution.py - Commands for load distribution visualization

Provides commands for visualizing load distribution patterns on slabs:
- Two-Way (Yield Line) distribution
- One-Way distribution
- Beam load calculations and export
"""

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtWidgets, QtCore
import os

from .visualization.LoadDistributionVisualizer import LoadDistributionVisualizer, SlabLoadCalculator
from .objects.AreaLoad import AreaLoad


class VisualizeLoadDistributionCommand:
    """Command to visualize load distribution patterns for selected area loads."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'load_distribution.svg'),
            'MenuText': 'Visualize Load Distribution',
            'ToolTip': 'Visualize load distribution pattern (Two-Way/One-Way) and beam loads'
        }
    
    def IsActive(self):
        """Return True if an AreaLoad is selected."""
        if not App.ActiveDocument:
            return False
        
        selection = Gui.Selection.getSelection()
        if len(selection) == 1:
            obj = selection[0]
            if hasattr(obj, 'Proxy'):
                if hasattr(obj.Proxy, 'Type') and 'AreaLoad' in str(obj.Proxy.Type):
                    return True
        return False
    
    def Activated(self):
        """Execute the command."""
        selection = Gui.Selection.getSelection()
        if not selection:
            return
        
        area_load_obj = selection[0]
        
        # Show dialog to choose distribution type
        dialog = LoadDistributionDialog(area_load_obj)
        result = dialog.exec_()
        
        if result == QtWidgets.QDialog.Accepted:
            dist_type = dialog.get_distribution_type()
            load_intensity = dialog.get_load_intensity()
            show_beam_loads = dialog.get_show_beam_loads()
            
            # Create visualization
            self.create_visualization(area_load_obj, dist_type, load_intensity, show_beam_loads)
        
        App.ActiveDocument.recompute()
        Gui.updateGui()
    
    def create_visualization(self, area_load_obj, dist_type, load_intensity, show_beam_loads):
        """Create load distribution visualization."""
        try:
            # Extract corners from area load faces
            corners = self.extract_corners(area_load_obj)
            if len(corners) < 4:
                QtWidgets.QMessageBox.warning(
                    None,
                    'Load Distribution',
                    'Unable to extract slab corners. Please ensure the area load is applied to a rectangular surface.'
                )
                return
            
            # Create visualizer
            doc = App.ActiveDocument
            viz = LoadDistributionVisualizer(doc)
            viz.clear_visualization()
            
            # Create visualization based on type
            if dist_type == "Two-Way (Yield Line)":
                viz.visualize_slab_with_beam_loads(
                    corners, 
                    load_intensity=load_intensity,
                    distribution_type="two_way",
                    name_prefix=f"{area_load_obj.Name}_TwoWay"
                )
            elif dist_type == "One-Way (Short Span)":
                viz.visualize_slab_with_beam_loads(
                    corners,
                    load_intensity=load_intensity,
                    distribution_type="one_way",
                    name_prefix=f"{area_load_obj.Name}_OneWay"
                )
            
            # Calculate and display beam loads
            if show_beam_loads:
                self.show_beam_load_summary(corners, load_intensity, dist_type)
            
            App.Console.PrintMessage(f"✓ Load distribution visualization created for {area_load_obj.Label}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error creating load distribution: {str(e)}\n")
            QtWidgets.QMessageBox.critical(
                None,
                'Error',
                f'Error creating visualization:\n{str(e)}'
            )
    
    def extract_corners(self, area_load_obj):
        """Extract corner vertices from area load target faces."""
        corners = []
        try:
            if hasattr(area_load_obj, 'TargetFaces') and area_load_obj.TargetFaces:
                for face_obj in area_load_obj.TargetFaces:
                    if hasattr(face_obj, 'Shape'):
                        shape = face_obj.Shape
                        if hasattr(shape, 'Vertexes'):
                            for v in shape.Vertexes:
                                corners.append(v.Point)
                        elif hasattr(shape, 'Faces') and len(shape.Faces) > 0:
                            for v in shape.Faces[0].Vertexes:
                                corners.append(v.Point)
        except Exception as e:
            App.Console.PrintWarning(f"Error extracting corners: {e}\n")
        
        # Return first 4 unique corners
        unique = []
        for c in corners:
            is_dup = False
            for u in unique:
                if (c - u).Length < 1.0:  # 1mm tolerance
                    is_dup = True
                    break
            if not is_dup:
                unique.append(c)
        
        return unique[:4]
    
    def show_beam_load_summary(self, corners, load_intensity, dist_type):
        """Calculate and display beam load summary."""
        calc = SlabLoadCalculator()
        
        if "Two-Way" in dist_type:
            beam_loads = calc.calculate_two_way_beam_loads(corners, load_intensity)
        else:
            beam_loads = calc.calculate_one_way_beam_loads(corners, load_intensity, "short")
        
        calc.print_beam_loads(beam_loads)


class LoadDistributionDialog(QtWidgets.QDialog):
    """Dialog for configuring load distribution visualization."""
    
    def __init__(self, area_load_obj, parent=None):
        super(LoadDistributionDialog, self).__init__(parent)
        self.area_load_obj = area_load_obj
        self.setup_ui()
    
    def setup_ui(self):
        """Setup dialog UI."""
        self.setWindowTitle("Load Distribution Visualization")
        self.setMinimumWidth(400)
        
        layout = QtWidgets.QVBoxLayout()
        
        # Header
        header = QtWidgets.QLabel(f"<b>Visualize:</b> {self.area_load_obj.Label}")
        layout.addWidget(header)
        
        # Distribution type
        dist_group = QtWidgets.QGroupBox("Distribution Type")
        dist_layout = QtWidgets.QVBoxLayout()
        
        self.radio_two_way = QtWidgets.QRadioButton("Two-Way (Yield Line)")
        self.radio_two_way.setChecked(True)
        self.radio_two_way.setToolTip("For slabs with Lx/Ly < 2.0 - creates star pattern with yield lines")
        
        self.radio_one_way = QtWidgets.QRadioButton("One-Way (Short Span)")
        self.radio_one_way.setToolTip("For slabs with Lx/Ly ≥ 2.0 - creates parallel strip pattern")
        
        dist_layout.addWidget(self.radio_two_way)
        dist_layout.addWidget(self.radio_one_way)
        dist_group.setLayout(dist_layout)
        layout.addWidget(dist_group)
        
        # Load intensity
        load_group = QtWidgets.QGroupBox("Load Parameters")
        load_layout = QtWidgets.QFormLayout()
        
        self.spin_intensity = QtWidgets.QDoubleSpinBox()
        self.spin_intensity.setRange(0.1, 1000.0)
        self.spin_intensity.setValue(10.0)
        self.spin_intensity.setSuffix(" kN/m²")
        self.spin_intensity.setDecimals(2)
        
        # Try to get load from area load object
        if hasattr(self.area_load_obj, 'LoadIntensity'):
            try:
                intensity_str = str(self.area_load_obj.LoadIntensity)
                intensity_val = float(intensity_str.split()[0])
                self.spin_intensity.setValue(intensity_val)
            except:
                pass
        
        load_layout.addRow("Load Intensity:", self.spin_intensity)
        load_group.setLayout(load_layout)
        layout.addWidget(load_group)
        
        # Options
        options_group = QtWidgets.QGroupBox("Visualization Options")
        options_layout = QtWidgets.QVBoxLayout()
        
        self.check_beam_loads = QtWidgets.QCheckBox("Show beam loads in console")
        self.check_beam_loads.setChecked(True)
        self.check_beam_loads.setToolTip("Print calculated beam loads to FreeCAD console")
        
        options_layout.addWidget(self.check_beam_loads)
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)
        
        # Info text
        info_text = QtWidgets.QLabel(
            "<i>This will create a 3D visualization showing:<br>"
            "• Load distribution pattern (yield lines or strips)<br>"
            "• Tributary areas with color coding<br>"
            "• Distributed loads on supporting beams</i>"
        )
        info_text.setWordWrap(True)
        layout.addWidget(info_text)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        btn_ok = QtWidgets.QPushButton("Create Visualization")
        btn_ok.clicked.connect(self.accept)
        
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_cancel.clicked.connect(self.reject)
        
        button_layout.addWidget(btn_ok)
        button_layout.addWidget(btn_cancel)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def get_distribution_type(self):
        """Get selected distribution type."""
        if self.radio_two_way.isChecked():
            return "Two-Way (Yield Line)"
        else:
            return "One-Way (Short Span)"
    
    def get_load_intensity(self):
        """Get load intensity value."""
        return self.spin_intensity.value()
    
    def get_show_beam_loads(self):
        """Get whether to show beam loads."""
        return self.check_beam_loads.isChecked()


class ClearLoadDistributionCommand:
    """Command to clear load distribution visualizations."""
    
    def GetResources(self):
        """Return command resources."""
        return {
            'Pixmap': os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'clear_distribution.svg'),
            'MenuText': 'Clear Load Distribution',
            'ToolTip': 'Clear all load distribution visualization objects'
        }
    
    def IsActive(self):
        """Return True if document is active."""
        return App.ActiveDocument is not None
    
    def Activated(self):
        """Execute the command."""
        doc = App.ActiveDocument
        if not doc:
            return
        
        # Find and remove all visualization objects
        removed_count = 0
        for obj in doc.Objects:
            if any(keyword in obj.Name for keyword in 
                   ['TwoWay', 'OneWay', 'YieldLine', 'Strip', 'BeamLoad', 'SlabLoad']):
                try:
                    doc.removeObject(obj.Name)
                    removed_count += 1
                except:
                    pass
        
        if removed_count > 0:
            App.Console.PrintMessage(f"✓ Removed {removed_count} load distribution visualization objects\n")
        else:
            App.Console.PrintMessage("No load distribution visualizations found\n")
        
        doc.recompute()
        Gui.updateGui()


# Register commands
if App.GuiUp:
    Gui.addCommand('VisualizeLoadDistribution', VisualizeLoadDistributionCommand())
    Gui.addCommand('ClearLoadDistribution', ClearLoadDistributionCommand())
