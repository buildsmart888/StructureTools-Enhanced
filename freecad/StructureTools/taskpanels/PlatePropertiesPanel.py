import FreeCAD as App
import FreeCADGui as Gui
from PySide2 import QtCore, QtWidgets, QtGui
import os


class PlatePropertiesPanel:
    """
    Professional task panel for editing StructuralPlate properties.
    
    This panel provides comprehensive editing capabilities for plate/shell elements
    with real-time validation and preview functionality.
    """
    
    def __init__(self, plate_object):
        """
        Initialize plate properties panel.
        
        Args:
            plate_object: StructuralPlate object to edit
        """
        self.plate_obj = plate_object
        self.form = self.createUI()
        self.preview_enabled = True
        
        # Connect to object changes
        self.plate_obj.addObserver(self.onObjectChanged)
        
        # Load current values
        self.loadCurrentValues()
    
    def createUI(self):
        """Create the user interface."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Title
        title_label = QtWidgets.QLabel(f"Plate Properties: {self.plate_obj.Label}")
        title_label.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        layout.addWidget(title_label)
        
        # Create tab widget for organized properties
        self.tab_widget = QtWidgets.QTabWidget()
        
        # Geometry tab
        self.geometry_tab = self.createGeometryTab()
        self.tab_widget.addTab(self.geometry_tab, "Geometry")
        
        # Material tab
        self.material_tab = self.createMaterialTab()
        self.tab_widget.addTab(self.material_tab, "Material & Section")
        
        # Analysis tab
        self.analysis_tab = self.createAnalysisTab()
        self.tab_widget.addTab(self.analysis_tab, "Analysis")
        
        # Meshing tab
        self.meshing_tab = self.createMeshingTab()
        self.tab_widget.addTab(self.meshing_tab, "Meshing")
        
        # Loads tab
        self.loads_tab = self.createLoadsTab()
        self.tab_widget.addTab(self.loads_tab, "Loads")
        
        layout.addWidget(self.tab_widget)
        
        # Preview controls
        preview_group = QtWidgets.QGroupBox("Preview")
        preview_layout = QtWidgets.QHBoxLayout()
        
        self.preview_checkbox = QtWidgets.QCheckBox("Real-time Preview")
        self.preview_checkbox.setChecked(self.preview_enabled)
        self.preview_checkbox.toggled.connect(self.togglePreview)
        
        self.update_preview_btn = QtWidgets.QPushButton("Update Preview")
        self.update_preview_btn.clicked.connect(self.updatePreview)
        
        preview_layout.addWidget(self.preview_checkbox)
        preview_layout.addWidget(self.update_preview_btn)
        preview_layout.addStretch()
        preview_group.setLayout(preview_layout)
        layout.addWidget(preview_group)
        
        # Status bar
        self.status_label = QtWidgets.QLabel("Ready")
        self.status_label.setStyleSheet("color: green; font-style: italic;")
        layout.addWidget(self.status_label)
        
        widget.setLayout(layout)
        return widget
    
    def createGeometryTab(self):
        """Create geometry properties tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout()
        
        # Corner nodes selection
        nodes_group = QtWidgets.QGroupBox("Corner Nodes")
        nodes_layout = QtWidgets.QVBoxLayout()
        
        self.nodes_list = QtWidgets.QListWidget()
        self.nodes_list.setMaximumHeight(100)
        nodes_layout.addWidget(self.nodes_list)
        
        nodes_buttons = QtWidgets.QHBoxLayout()
        self.add_node_btn = QtWidgets.QPushButton("Add Node")
        self.add_node_btn.clicked.connect(self.addNode)
        self.remove_node_btn = QtWidgets.QPushButton("Remove Node")
        self.remove_node_btn.clicked.connect(self.removeNode)
        self.clear_nodes_btn = QtWidgets.QPushButton("Clear All")
        self.clear_nodes_btn.clicked.connect(self.clearNodes)
        
        nodes_buttons.addWidget(self.add_node_btn)
        nodes_buttons.addWidget(self.remove_node_btn)
        nodes_buttons.addWidget(self.clear_nodes_btn)
        nodes_layout.addLayout(nodes_buttons)
        nodes_group.setLayout(nodes_layout)
        layout.addRow(nodes_group)
        
        # Plate thickness
        self.thickness_input = QtWidgets.QSpinBox()
        self.thickness_input.setRange(1, 1000)
        self.thickness_input.setSuffix(" mm")
        self.thickness_input.setValue(200)
        self.thickness_input.valueChanged.connect(self.onThicknessChanged)
        layout.addRow("Thickness:", self.thickness_input)
        
        # Plate type
        self.plate_type_combo = QtWidgets.QComboBox()
        self.plate_type_combo.addItems(["Thin Plate", "Thick Plate", "Shell", "Membrane"])
        self.plate_type_combo.currentTextChanged.connect(self.onPlateTypeChanged)
        layout.addRow("Plate Type:", self.plate_type_combo)
        
        # Calculated properties (read-only)
        calc_group = QtWidgets.QGroupBox("Calculated Properties")
        calc_layout = QtWidgets.QFormLayout()
        
        self.area_label = QtWidgets.QLabel("0 mm²")
        self.perimeter_label = QtWidgets.QLabel("0 mm")
        self.aspect_ratio_label = QtWidgets.QLabel("1.0")
        
        calc_layout.addRow("Area:", self.area_label)
        calc_layout.addRow("Perimeter:", self.perimeter_label)
        calc_layout.addRow("Aspect Ratio:", self.aspect_ratio_label)
        calc_group.setLayout(calc_layout)
        layout.addRow(calc_group)
        
        tab.setLayout(layout)
        return tab
    
    def createMaterialTab(self):
        """Create material and section properties tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout()
        
        # Material selection
        material_group = QtWidgets.QGroupBox("Material Assignment")
        material_layout = QtWidgets.QFormLayout()
        
        self.material_combo = QtWidgets.QComboBox()
        self.material_combo.addItem("None")
        self.populateMaterials()
        self.material_combo.currentTextChanged.connect(self.onMaterialChanged)
        material_layout.addRow("Material:", self.material_combo)
        
        self.create_material_btn = QtWidgets.QPushButton("Create New Material")
        self.create_material_btn.clicked.connect(self.createNewMaterial)
        material_layout.addRow(self.create_material_btn)
        
        material_group.setLayout(material_layout)
        layout.addRow(material_group)
        
        # Material properties display (read-only)
        props_group = QtWidgets.QGroupBox("Material Properties")
        props_layout = QtWidgets.QFormLayout()
        
        self.elastic_modulus_label = QtWidgets.QLabel("N/A")
        self.poisson_ratio_label = QtWidgets.QLabel("N/A")
        self.density_label = QtWidgets.QLabel("N/A")
        self.membrane_bending_ratio_label = QtWidgets.QLabel("N/A")
        
        props_layout.addRow("Elastic Modulus:", self.elastic_modulus_label)
        props_layout.addRow("Poisson Ratio:", self.poisson_ratio_label)
        props_layout.addRow("Density:", self.density_label)
        props_layout.addRow("Membrane/Bending Ratio:", self.membrane_bending_ratio_label)
        props_group.setLayout(props_layout)
        layout.addRow(props_group)
        
        tab.setLayout(layout)
        return tab
    
    def createAnalysisTab(self):
        """Create analysis properties tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout()
        
        # Analysis behavior
        behavior_group = QtWidgets.QGroupBox("Analysis Behavior")
        behavior_layout = QtWidgets.QFormLayout()
        
        self.membrane_action_check = QtWidgets.QCheckBox("Include Membrane Action")
        self.membrane_action_check.setChecked(True)
        self.membrane_action_check.toggled.connect(self.onAnalysisBehaviorChanged)
        
        self.bending_action_check = QtWidgets.QCheckBox("Include Bending Action")
        self.bending_action_check.setChecked(True)
        self.bending_action_check.toggled.connect(self.onAnalysisBehaviorChanged)
        
        self.shear_deformation_check = QtWidgets.QCheckBox("Include Shear Deformation")
        self.shear_deformation_check.setChecked(False)
        self.shear_deformation_check.toggled.connect(self.onAnalysisBehaviorChanged)
        
        behavior_layout.addRow(self.membrane_action_check)
        behavior_layout.addRow(self.bending_action_check)
        behavior_layout.addRow(self.shear_deformation_check)
        behavior_group.setLayout(behavior_layout)
        layout.addRow(behavior_group)
        
        # Boundary conditions
        boundary_group = QtWidgets.QGroupBox("Edge Boundary Conditions")
        boundary_layout = QtWidgets.QFormLayout()
        
        edge_conditions = ["Free", "Simply Supported", "Fixed", "Elastic"]
        
        self.edge1_combo = QtWidgets.QComboBox()
        self.edge1_combo.addItems(edge_conditions)
        self.edge1_combo.setCurrentText("Simply Supported")
        boundary_layout.addRow("Edge 1:", self.edge1_combo)
        
        self.edge2_combo = QtWidgets.QComboBox()
        self.edge2_combo.addItems(edge_conditions)
        self.edge2_combo.setCurrentText("Simply Supported")
        boundary_layout.addRow("Edge 2:", self.edge2_combo)
        
        self.edge3_combo = QtWidgets.QComboBox()
        self.edge3_combo.addItems(edge_conditions)
        self.edge3_combo.setCurrentText("Simply Supported")
        boundary_layout.addRow("Edge 3:", self.edge3_combo)
        
        self.edge4_combo = QtWidgets.QComboBox()
        self.edge4_combo.addItems(edge_conditions)
        self.edge4_combo.setCurrentText("Simply Supported")
        boundary_layout.addRow("Edge 4 (if quad):", self.edge4_combo)
        
        boundary_group.setLayout(boundary_layout)
        layout.addRow(boundary_group)
        
        # Nonlinearity options
        nonlinear_group = QtWidgets.QGroupBox("Nonlinearity")
        nonlinear_layout = QtWidgets.QFormLayout()
        
        self.geometric_nonlinear_check = QtWidgets.QCheckBox("Geometric Nonlinearity")
        self.material_nonlinear_check = QtWidgets.QCheckBox("Material Nonlinearity")
        
        nonlinear_layout.addRow(self.geometric_nonlinear_check)
        nonlinear_layout.addRow(self.material_nonlinear_check)
        nonlinear_group.setLayout(nonlinear_layout)
        layout.addRow(nonlinear_group)
        
        tab.setLayout(layout)
        return tab
    
    def createMeshingTab(self):
        """Create meshing properties tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout()
        
        # Mesh generation
        mesh_group = QtWidgets.QGroupBox("Mesh Generation")
        mesh_layout = QtWidgets.QFormLayout()
        
        self.mesh_density_spin = QtWidgets.QSpinBox()
        self.mesh_density_spin.setRange(2, 20)
        self.mesh_density_spin.setValue(4)
        self.mesh_density_spin.valueChanged.connect(self.onMeshParametersChanged)
        mesh_layout.addRow("Mesh Density:", self.mesh_density_spin)
        
        self.mesh_size_spin = QtWidgets.QDoubleSpinBox()
        self.mesh_size_spin.setRange(10.0, 1000.0)
        self.mesh_size_spin.setValue(100.0)
        self.mesh_size_spin.setSuffix(" mm")
        self.mesh_size_spin.valueChanged.connect(self.onMeshParametersChanged)
        mesh_layout.addRow("Element Size:", self.mesh_size_spin)
        
        self.element_type_combo = QtWidgets.QComboBox()
        self.element_type_combo.addItems(["Tri3", "Tri6", "Quad4", "Quad8", "Quad9"])
        self.element_type_combo.setCurrentText("Quad4")
        self.element_type_combo.currentTextChanged.connect(self.onMeshParametersChanged)
        mesh_layout.addRow("Element Type:", self.element_type_combo)
        
        mesh_group.setLayout(mesh_layout)
        layout.addRow(mesh_group)
        
        # Mesh generation controls
        mesh_controls = QtWidgets.QHBoxLayout()
        self.generate_mesh_btn = QtWidgets.QPushButton("Generate Mesh")
        self.generate_mesh_btn.clicked.connect(self.generateMesh)
        self.clear_mesh_btn = QtWidgets.QPushButton("Clear Mesh")
        self.clear_mesh_btn.clicked.connect(self.clearMesh)
        
        mesh_controls.addWidget(self.generate_mesh_btn)
        mesh_controls.addWidget(self.clear_mesh_btn)
        layout.addRow(mesh_controls)
        
        # Mesh quality display
        quality_group = QtWidgets.QGroupBox("Mesh Quality")
        quality_layout = QtWidgets.QFormLayout()
        
        self.num_elements_label = QtWidgets.QLabel("0")
        self.num_nodes_label = QtWidgets.QLabel("0")
        self.min_angle_label = QtWidgets.QLabel("N/A")
        self.max_aspect_ratio_label = QtWidgets.QLabel("N/A")
        self.quality_grade_label = QtWidgets.QLabel("N/A")
        
        quality_layout.addRow("Elements:", self.num_elements_label)
        quality_layout.addRow("Nodes:", self.num_nodes_label)
        quality_layout.addRow("Min Angle:", self.min_angle_label)
        quality_layout.addRow("Max Aspect Ratio:", self.max_aspect_ratio_label)
        quality_layout.addRow("Quality Grade:", self.quality_grade_label)
        
        quality_group.setLayout(quality_layout)
        layout.addRow(quality_group)
        
        tab.setLayout(layout)
        return tab
    
    def createLoadsTab(self):
        """Create loads management tab."""
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Applied loads list
        loads_group = QtWidgets.QGroupBox("Applied Area Loads")
        loads_layout = QtWidgets.QVBoxLayout()
        
        self.loads_list = QtWidgets.QListWidget()
        self.loads_list.setMaximumHeight(150)
        loads_layout.addWidget(self.loads_list)
        
        # Load management buttons
        load_buttons = QtWidgets.QHBoxLayout()
        self.add_load_btn = QtWidgets.QPushButton("Add Load")
        self.add_load_btn.clicked.connect(self.addAreaLoad)
        self.edit_load_btn = QtWidgets.QPushButton("Edit Load")
        self.edit_load_btn.clicked.connect(self.editAreaLoad)
        self.remove_load_btn = QtWidgets.QPushButton("Remove Load")
        self.remove_load_btn.clicked.connect(self.removeAreaLoad)
        
        load_buttons.addWidget(self.add_load_btn)
        load_buttons.addWidget(self.edit_load_btn)
        load_buttons.addWidget(self.remove_load_btn)
        loads_layout.addLayout(load_buttons)
        
        loads_group.setLayout(loads_layout)
        layout.addWidget(loads_group)
        
        # Load summary
        summary_group = QtWidgets.QGroupBox("Load Summary")
        summary_layout = QtWidgets.QFormLayout()
        
        self.total_pressure_label = QtWidgets.QLabel("0 kN/m²")
        self.total_force_label = QtWidgets.QLabel("0 kN")
        self.load_resultant_label = QtWidgets.QLabel("(0, 0, 0)")
        
        summary_layout.addRow("Total Pressure:", self.total_pressure_label)
        summary_layout.addRow("Total Force:", self.total_force_label)
        summary_layout.addRow("Load Resultant:", self.load_resultant_label)
        
        summary_group.setLayout(summary_layout)
        layout.addWidget(summary_group)
        
        tab.setLayout(layout)
        return tab
    
    def populateMaterials(self):
        """Populate material combo box with available materials."""
        self.material_combo.clear()
        self.material_combo.addItem("None")
        
        doc = App.ActiveDocument
        if doc:
            for obj in doc.Objects:
                if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
                    if obj.Proxy.Type == "StructuralMaterial":
                        self.material_combo.addItem(obj.Label)
    
    def loadCurrentValues(self):
        """Load current property values into UI controls."""
        if not self.plate_obj:
            return
        
        try:
            # Geometry tab
            if hasattr(self.plate_obj, 'Thickness'):
                thickness_value = self.plate_obj.Thickness.getValueAs('mm')
                self.thickness_input.setValue(int(thickness_value))
            
            if hasattr(self.plate_obj, 'PlateType'):
                self.plate_type_combo.setCurrentText(self.plate_obj.PlateType)
            
            # Update calculated properties
            self.updateCalculatedProperties()
            
            # Material tab
            if hasattr(self.plate_obj, 'Material') and self.plate_obj.Material:
                self.material_combo.setCurrentText(self.plate_obj.Material.Label)
                self.updateMaterialProperties()
            
            # Analysis tab
            if hasattr(self.plate_obj, 'IncludeMembraneAction'):
                self.membrane_action_check.setChecked(self.plate_obj.IncludeMembraneAction)
            if hasattr(self.plate_obj, 'IncludeBendingAction'):
                self.bending_action_check.setChecked(self.plate_obj.IncludeBendingAction)
            if hasattr(self.plate_obj, 'IncludeShearDeformation'):
                self.shear_deformation_check.setChecked(self.plate_obj.IncludeShearDeformation)
            
            # Meshing tab
            if hasattr(self.plate_obj, 'MeshDensity'):
                self.mesh_density_spin.setValue(self.plate_obj.MeshDensity)
            
            # Update mesh quality if mesh exists
            self.updateMeshQuality()
            
            # Loads tab
            self.updateLoadsList()
            
        except Exception as e:
            App.Console.PrintWarning(f"Error loading current values: {e}\n")
    
    def updateCalculatedProperties(self):
        """Update calculated geometric properties."""
        if not self.plate_obj:
            return
        
        try:
            if hasattr(self.plate_obj, 'Area'):
                self.area_label.setText(str(self.plate_obj.Area))
            if hasattr(self.plate_obj, 'Perimeter'):
                self.perimeter_label.setText(str(self.plate_obj.Perimeter))
            if hasattr(self.plate_obj, 'AspectRatio'):
                self.aspect_ratio_label.setText(f"{self.plate_obj.AspectRatio:.2f}")
        except Exception as e:
            App.Console.PrintWarning(f"Error updating calculated properties: {e}\n")
    
    def updateMaterialProperties(self):
        """Update material properties display."""
        if not self.plate_obj or not hasattr(self.plate_obj, 'Material') or not self.plate_obj.Material:
            self.elastic_modulus_label.setText("N/A")
            self.poisson_ratio_label.setText("N/A")
            self.density_label.setText("N/A")
            self.membrane_bending_ratio_label.setText("N/A")
            return
        
        try:
            material = self.plate_obj.Material
            
            if hasattr(material, 'ModulusElasticity'):
                self.elastic_modulus_label.setText(str(material.ModulusElasticity))
            if hasattr(material, 'PoissonRatio'):
                self.poisson_ratio_label.setText(f"{material.PoissonRatio:.3f}")
            if hasattr(material, 'Density'):
                self.density_label.setText(str(material.Density))
            if hasattr(self.plate_obj, 'MembraneBendingRatio'):
                self.membrane_bending_ratio_label.setText(f"{self.plate_obj.MembraneBendingRatio:.3f}")
                
        except Exception as e:
            App.Console.PrintWarning(f"Error updating material properties: {e}\n")
    
    def updateMeshQuality(self):
        """Update mesh quality display."""
        if not self.plate_obj or not hasattr(self.plate_obj, 'MeshData') or not self.plate_obj.MeshData:
            self.num_elements_label.setText("0")
            self.num_nodes_label.setText("0")
            self.min_angle_label.setText("N/A")
            self.max_aspect_ratio_label.setText("N/A")
            self.quality_grade_label.setText("N/A")
            return
        
        try:
            mesh_data = self.plate_obj.MeshData
            if 'quality' in mesh_data:
                quality = mesh_data['quality']
                
                self.num_elements_label.setText(str(quality.get('num_elements', 0)))
                self.num_nodes_label.setText(str(quality.get('num_nodes', 0)))
                self.min_angle_label.setText(f"{quality.get('min_angle', 0):.1f}°")
                self.max_aspect_ratio_label.setText(f"{quality.get('max_aspect_ratio', 0):.2f}")
                
                grade = quality.get('quality_grade', 'N/A')
                self.quality_grade_label.setText(grade)
                
                # Color code the quality grade
                color_map = {
                    'Excellent': 'green',
                    'Good': 'blue', 
                    'Acceptable': 'orange',
                    'Poor': 'red'
                }
                color = color_map.get(grade, 'black')
                self.quality_grade_label.setStyleSheet(f"color: {color}; font-weight: bold;")
                
        except Exception as e:
            App.Console.PrintWarning(f"Error updating mesh quality: {e}\n")
    
    def updateLoadsList(self):
        """Update the loads list display."""
        self.loads_list.clear()
        
        if not self.plate_obj or not hasattr(self.plate_obj, 'AreaLoads'):
            return
        
        try:
            if self.plate_obj.AreaLoads:
                for load in self.plate_obj.AreaLoads:
                    if hasattr(load, 'Label'):
                        self.loads_list.addItem(load.Label)
        except Exception as e:
            App.Console.PrintWarning(f"Error updating loads list: {e}\n")
    
    # Event handlers
    def onThicknessChanged(self, value):
        """Handle thickness change."""
        if self.plate_obj and hasattr(self.plate_obj, 'Thickness'):
            self.plate_obj.Thickness = f"{value} mm"
            if self.preview_enabled:
                self.updatePreview()
    
    def onPlateTypeChanged(self, plate_type):
        """Handle plate type change."""
        if self.plate_obj and hasattr(self.plate_obj, 'PlateType'):
            self.plate_obj.PlateType = plate_type
            if self.preview_enabled:
                self.updatePreview()
    
    def onMaterialChanged(self, material_label):
        """Handle material change."""
        if not self.plate_obj:
            return
        
        if material_label == "None":
            self.plate_obj.Material = None
        else:
            # Find material by label
            doc = App.ActiveDocument
            for obj in doc.Objects:
                if obj.Label == material_label and hasattr(obj, 'Proxy'):
                    if hasattr(obj.Proxy, 'Type') and obj.Proxy.Type == "StructuralMaterial":
                        self.plate_obj.Material = obj
                        break
        
        self.updateMaterialProperties()
        if self.preview_enabled:
            self.updatePreview()
    
    def onAnalysisBehaviorChanged(self):
        """Handle analysis behavior changes."""
        if not self.plate_obj:
            return
        
        if hasattr(self.plate_obj, 'IncludeMembraneAction'):
            self.plate_obj.IncludeMembraneAction = self.membrane_action_check.isChecked()
        if hasattr(self.plate_obj, 'IncludeBendingAction'):
            self.plate_obj.IncludeBendingAction = self.bending_action_check.isChecked()
        if hasattr(self.plate_obj, 'IncludeShearDeformation'):
            self.plate_obj.IncludeShearDeformation = self.shear_deformation_check.isChecked()
    
    def onMeshParametersChanged(self):
        """Handle mesh parameter changes."""
        if self.preview_enabled:
            self.updatePreview()
    
    def onObjectChanged(self, obj, prop):
        """Handle object property changes."""
        if obj == self.plate_obj:
            # Update UI when object changes externally
            if prop in ['Area', 'Perimeter', 'AspectRatio']:
                self.updateCalculatedProperties()
            elif prop == 'MeshData':
                self.updateMeshQuality()
    
    # Actions
    def togglePreview(self, enabled):
        """Toggle real-time preview."""
        self.preview_enabled = enabled
        if enabled:
            self.updatePreview()
    
    def updatePreview(self):
        """Update the 3D preview."""
        if self.plate_obj:
            self.plate_obj.recompute()
            App.ActiveDocument.recompute()
            self.updateStatus("Preview updated")
    
    def addNode(self):
        """Add a corner node to the plate."""
        # This would open a node selection dialog
        App.Console.PrintMessage("Add node functionality would be implemented here\n")
    
    def removeNode(self):
        """Remove selected corner node."""
        current_item = self.nodes_list.currentItem()
        if current_item:
            # Remove from plate object
            App.Console.PrintMessage(f"Remove node: {current_item.text()}\n")
    
    def clearNodes(self):
        """Clear all corner nodes."""
        if self.plate_obj and hasattr(self.plate_obj, 'CornerNodes'):
            self.plate_obj.CornerNodes = []
            self.nodes_list.clear()
    
    def createNewMaterial(self):
        """Create a new material object."""
        try:
            from ..objects.StructuralMaterial import makeStructuralMaterial
            material = makeStructuralMaterial()
            if material:
                self.populateMaterials()
                self.material_combo.setCurrentText(material.Label)
        except ImportError:
            App.Console.PrintWarning("StructuralMaterial not available\n")
    
    def generateMesh(self):
        """Generate finite element mesh."""
        if not self.plate_obj:
            return
        
        try:
            # Update mesh parameters
            if hasattr(self.plate_obj, 'MeshDensity'):
                self.plate_obj.MeshDensity = self.mesh_density_spin.value()
            
            # Trigger mesh generation
            if hasattr(self.plate_obj.Proxy, 'generateMesh'):
                mesh_data = self.plate_obj.Proxy.generateMesh(self.plate_obj)
                if mesh_data:
                    self.updateMeshQuality()
                    self.updateStatus("Mesh generated successfully")
                else:
                    self.updateStatus("Mesh generation failed", "red")
            
        except Exception as e:
            self.updateStatus(f"Mesh error: {str(e)}", "red")
    
    def clearMesh(self):
        """Clear the finite element mesh."""
        if self.plate_obj and hasattr(self.plate_obj, 'MeshData'):
            self.plate_obj.MeshData = None
            self.updateMeshQuality()
            self.updateStatus("Mesh cleared")
    
    def addAreaLoad(self):
        """Add a new area load to the plate."""
        try:
            from ..objects.AreaLoad import makeAreaLoad
            
            # Create area load with this plate as target
            area_load = makeAreaLoad(target_faces=[self.plate_obj])
            if area_load:
                # Add to plate's load list
                if hasattr(self.plate_obj, 'AreaLoads'):
                    current_loads = list(self.plate_obj.AreaLoads) if self.plate_obj.AreaLoads else []
                    current_loads.append(area_load)
                    self.plate_obj.AreaLoads = current_loads
                
                self.updateLoadsList()
                self.updateStatus(f"Area load {area_load.Label} added")
                
        except ImportError:
            App.Console.PrintWarning("AreaLoad not available\n")
        except Exception as e:
            self.updateStatus(f"Error adding load: {str(e)}", "red")
    
    def editAreaLoad(self):
        """Edit selected area load."""
        current_item = self.loads_list.currentItem()
        if current_item:
            App.Console.PrintMessage(f"Edit load: {current_item.text()}\n")
            # This would open the area load properties panel
    
    def removeAreaLoad(self):
        """Remove selected area load."""
        current_item = self.loads_list.currentItem()
        if current_item and self.plate_obj:
            load_label = current_item.text()
            
            # Find and remove the load
            if hasattr(self.plate_obj, 'AreaLoads') and self.plate_obj.AreaLoads:
                current_loads = list(self.plate_obj.AreaLoads)
                for load in current_loads:
                    if hasattr(load, 'Label') and load.Label == load_label:
                        current_loads.remove(load)
                        break
                
                self.plate_obj.AreaLoads = current_loads
                self.updateLoadsList()
                self.updateStatus(f"Load {load_label} removed")
    
    def updateStatus(self, message, color="green"):
        """Update status message."""
        self.status_label.setText(message)
        self.status_label.setStyleSheet(f"color: {color}; font-style: italic;")
    
    def accept(self):
        """Accept changes and close panel."""
        self.updatePreview()
        self.updateStatus("Changes applied")
        return True
    
    def reject(self):
        """Reject changes and close panel."""
        # Could implement undo functionality here
        return True
    
    def getStandardButtons(self):
        """Return standard dialog buttons."""
        return QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel