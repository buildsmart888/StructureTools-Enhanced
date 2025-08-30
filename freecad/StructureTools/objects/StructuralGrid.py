import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Any
import string
import os


class StructuralGrid:
    """
    Parametric structural grid system for building layout.
    
    This class provides intelligent grid systems with automatic member generation,
    grid labeling, and parametric updates for structural building layouts.
    """
    
    def __init__(self, obj):
        """
        Initialize StructuralGrid object.
        
        Args:
            obj: FreeCAD DocumentObject to be enhanced
        """
        self.Type = "StructuralGrid"
        obj.Proxy = self
        
        # Grid definition
        obj.addProperty("App::PropertyFloatList", "XSpacing", "Grid Layout",
                       "X-direction grid spacing (mm)")
        obj.XSpacing = [6000.0, 6000.0, 6000.0]  # Default 3 bays @ 6m
        
        obj.addProperty("App::PropertyFloatList", "YSpacing", "Grid Layout",
                       "Y-direction grid spacing (mm)")
        obj.YSpacing = [8000.0, 8000.0]  # Default 2 bays @ 8m
        
        obj.addProperty("App::PropertyFloatList", "ZLevels", "Grid Layout",
                       "Floor levels (mm above datum)")
        obj.ZLevels = [0.0, 3500.0, 7000.0]  # Default 3 floors @ 3.5m
        
        obj.addProperty("App::PropertyVector", "GridOrigin", "Grid Layout",
                       "Grid origin point")
        obj.GridOrigin = App.Vector(0, 0, 0)
        
        obj.addProperty("App::PropertyAngle", "GridRotation", "Grid Layout",
                       "Grid rotation about Z-axis")
        obj.GridRotation = "0 deg"
        
        # Grid labeling system
        obj.addProperty("App::PropertyEnumeration", "XLabelingStyle", "Labeling",
                       "X-axis labeling style")
        obj.XLabelingStyle = ["Numbers", "Letters", "Custom"]
        obj.XLabelingStyle = "Numbers"
        
        obj.addProperty("App::PropertyEnumeration", "YLabelingStyle", "Labeling",
                       "Y-axis labeling style")
        obj.YLabelingStyle = ["Letters", "Numbers", "Custom"]
        obj.YLabelingStyle = "Letters"
        
        obj.addProperty("App::PropertyStringList", "XLabels", "Labeling",
                       "X-axis grid labels")
        
        obj.addProperty("App::PropertyStringList", "YLabels", "Labeling",
                       "Y-axis grid labels")
        
        obj.addProperty("App::PropertyStringList", "ZLabels", "Labeling",
                       "Level labels")
        
        obj.addProperty("App::PropertyString", "LabelPrefix", "Labeling",
                       "Prefix for grid labels")
        obj.LabelPrefix = ""
        
        obj.addProperty("App::PropertyString", "LabelSuffix", "Labeling",
                       "Suffix for grid labels")
        obj.LabelSuffix = ""
        
        # Automatic member generation
        obj.addProperty("App::PropertyBool", "AutoGenerateBeams", "Generation",
                       "Automatically generate beam layout")
        obj.AutoGenerateBeams = True
        
        obj.addProperty("App::PropertyBool", "AutoGenerateColumns", "Generation",
                       "Automatically generate column layout")
        obj.AutoGenerateColumns = True
        
        obj.addProperty("App::PropertyBool", "AutoGenerateBracing", "Generation",
                       "Automatically generate bracing layout")
        obj.AutoGenerateBracing = False
        
        obj.addProperty("App::PropertyLink", "DefaultBeamSection", "Generation",
                       "Default beam section for generation")
        
        obj.addProperty("App::PropertyLink", "DefaultColumnSection", "Generation",
                       "Default column section for generation")
        
        obj.addProperty("App::PropertyLink", "DefaultBracingSection", "Generation",
                       "Default bracing section for generation")
        
        obj.addProperty("App::PropertyLink", "DefaultMaterial", "Generation",
                       "Default material for generated members")
        
        # Beam generation options
        obj.addProperty("App::PropertyEnumeration", "BeamLayout", "Beam Options",
                       "Beam layout pattern")
        obj.BeamLayout = ["All Grids", "Perimeter Only", "Interior Only", "Custom Pattern"]
        obj.BeamLayout = "All Grids"
        
        obj.addProperty("App::PropertyBoolList", "BeamXDirections", "Beam Options",
                       "Generate beams in X direction for each Y grid line")
        
        obj.addProperty("App::PropertyBoolList", "BeamYDirections", "Beam Options",
                       "Generate beams in Y direction for each X grid line")
        
        obj.addProperty("App::PropertyFloatList", "BeamElevations", "Beam Options",
                       "Elevations for beam generation")
        
        # Column generation options
        obj.addProperty("App::PropertyEnumeration", "ColumnLayout", "Column Options",
                       "Column layout pattern")
        obj.ColumnLayout = ["All Intersections", "Perimeter Only", "Interior Only", "Custom Pattern"]
        obj.ColumnLayout = "All Intersections"
        
        obj.addProperty("App::PropertyBoolList", "ColumnLocations", "Column Options",
                       "Generate columns at specific grid intersections")
        
        obj.addProperty("App::PropertyFloatList", "ColumnBaseLevels", "Column Options",
                       "Base levels for column generation")
        
        obj.addProperty("App::PropertyFloatList", "ColumnTopLevels", "Column Options",
                       "Top levels for column generation")
        
        # Advanced grid features
        obj.addProperty("App::PropertyBool", "ShowGridLines", "Visualization",
                       "Show grid lines in 3D view")
        obj.ShowGridLines = True
        
        obj.addProperty("App::PropertyBool", "ShowGridLabels", "Visualization",
                       "Show grid labels")
        obj.ShowGridLabels = True
        
        obj.addProperty("App::PropertyBool", "ShowLevelLabels", "Visualization",
                       "Show level labels")
        obj.ShowLevelLabels = True
        
        obj.addProperty("App::PropertyFloat", "GridLineWeight", "Visualization",
                       "Grid line weight")
        obj.GridLineWeight = 1.0
        
        obj.addProperty("App::PropertyColor", "GridLineColor", "Visualization",
                       "Grid line color")
        obj.GridLineColor = (0.5, 0.5, 0.5)  # Gray
        
        obj.addProperty("App::PropertyFloat", "LabelSize", "Visualization",
                       "Grid label text size")
        obj.LabelSize = 100.0  # mm
        
        # Grid zones and areas
        obj.addProperty("App::PropertyStringList", "GridZones", "Zones",
                       "Named grid zones")
        
        obj.addProperty("App::PropertyFloatList", "ZoneBoundaries", "Zones",
                       "Zone boundary definitions")
        
        # Building type templates
        obj.addProperty("App::PropertyEnumeration", "BuildingTemplate", "Templates",
                       "Building type template")
        obj.BuildingTemplate = ["Custom", "Office Building", "Warehouse", "Residential", "Parking Garage"]
        obj.BuildingTemplate = "Custom"
        
        obj.addProperty("App::PropertyFloat", "TypicalBayWidth", "Templates",
                       "Typical bay width for templates")
        obj.TypicalBayWidth = 6000.0  # 6m
        
        obj.addProperty("App::PropertyFloat", "TypicalBayDepth", "Templates",
                       "Typical bay depth for templates")
        obj.TypicalBayDepth = 8000.0  # 8m
        
        obj.addProperty("App::PropertyFloat", "TypicalFloorHeight", "Templates",
                       "Typical floor height for templates")
        obj.TypicalFloorHeight = 3500.0  # 3.5m
        
        # Generated objects tracking
        obj.addProperty("App::PropertyLinkList", "GeneratedBeams", "Generated Objects",
                       "List of generated beam objects")
        
        obj.addProperty("App::PropertyLinkList", "GeneratedColumns", "Generated Objects",
                       "List of generated column objects")
        
        obj.addProperty("App::PropertyLinkList", "GeneratedNodes", "Generated Objects",
                       "List of generated node objects")
        
        obj.addProperty("App::PropertyPythonObject", "GridNodes", "Internal",
                       "Grid intersection nodes data")
        obj.GridNodes = {}
        
        # Statistics
        obj.addProperty("App::PropertyInteger", "NumberOfBays", "Statistics",
                       "Total number of bays")
        
        obj.addProperty("App::PropertyArea", "TotalFloorArea", "Statistics",
                       "Total floor area")
        
        obj.addProperty("App::PropertyInteger", "NumberOfColumns", "Statistics",
                       "Number of columns generated")
        
        obj.addProperty("App::PropertyInteger", "NumberOfBeams", "Statistics",
                       "Number of beams generated")
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        if prop in ["XSpacing", "YSpacing", "ZLevels"]:
            self._update_grid_geometry(obj)
            self._update_labels(obj)
            if obj.AutoGenerateBeams or obj.AutoGenerateColumns:
                self._regenerate_members(obj)
        elif prop in ["XLabelingStyle", "YLabelingStyle"]:
            self._update_labels(obj)
        elif prop == "BuildingTemplate":
            self._apply_building_template(obj)
        elif prop in ["AutoGenerateBeams", "AutoGenerateColumns"]:
            self._regenerate_members(obj)
        elif prop in ["BeamLayout", "ColumnLayout"]:
            self._regenerate_members(obj)
    
    def _update_grid_geometry(self, obj) -> None:
        """Update grid geometry when spacing changes."""
        try:
            # Calculate grid boundaries
            x_coords = self._calculate_grid_coordinates(obj.XSpacing, obj.GridOrigin.x)
            y_coords = self._calculate_grid_coordinates(obj.YSpacing, obj.GridOrigin.y)
            z_coords = [obj.GridOrigin.z + level for level in obj.ZLevels]
            
            # Update grid nodes
            self._update_grid_nodes(obj, x_coords, y_coords, z_coords)
            
            # Update statistics
            obj.NumberOfBays = len(obj.XSpacing) * len(obj.YSpacing)
            
            if obj.XSpacing and obj.YSpacing:
                total_x = sum(obj.XSpacing)
                total_y = sum(obj.YSpacing)
                obj.TotalFloorArea = f"{total_x * total_y / 1000000:.2f} m^2"  # Convert mm² to m²
            
            # Update visualization
            if obj.ShowGridLines:
                self._create_grid_visualization(obj, x_coords, y_coords, z_coords)
            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error updating grid geometry: {e}\n")
    
    def _calculate_grid_coordinates(self, spacing_list: List[float], origin: float) -> List[float]:
        """Calculate grid line coordinates from spacing list."""
        coords = [origin]
        cumulative = origin
        
        for spacing in spacing_list:
            cumulative += spacing
            coords.append(cumulative)
        
        return coords
    
    def _update_grid_nodes(self, obj, x_coords: List[float], y_coords: List[float], z_coords: List[float]) -> None:
        """Update grid intersection nodes."""
        grid_nodes = {}
        
        for i, x in enumerate(x_coords):
            for j, y in enumerate(y_coords):
                for k, z in enumerate(z_coords):
                    node_id = f"{i}_{j}_{k}"
                    grid_nodes[node_id] = {
                        'position': App.Vector(x, y, z),
                        'grid_x': i,
                        'grid_y': j,
                        'level': k,
                        'label': self._get_grid_intersection_label(obj, i, j, k)
                    }
        
        obj.GridNodes = grid_nodes
    
    def _get_grid_intersection_label(self, obj, x_index: int, y_index: int, level_index: int) -> str:
        """Get label for grid intersection."""
        try:
            x_label = obj.XLabels[x_index] if x_index < len(obj.XLabels) else str(x_index + 1)
            y_label = obj.YLabels[y_index] if y_index < len(obj.YLabels) else chr(65 + y_index)
            z_label = obj.ZLabels[level_index] if level_index < len(obj.ZLabels) else f"L{level_index + 1}"
            
            return f"{obj.LabelPrefix}{y_label}{x_label}_{z_label}{obj.LabelSuffix}"
            
        except Exception:
            return f"G{x_index}_{y_index}_{level_index}"
    
    def _update_labels(self, obj) -> None:
        """Update grid labels based on labeling style."""
        try:
            # Update X labels
            x_labels = []
            for i in range(len(obj.XSpacing) + 1):
                if obj.XLabelingStyle == "Numbers":
                    x_labels.append(str(i + 1))
                elif obj.XLabelingStyle == "Letters":
                    x_labels.append(chr(65 + i) if i < 26 else f"A{chr(65 + i - 26)}")
                else:  # Custom
                    x_labels.append(f"X{i + 1}")
            obj.XLabels = x_labels
            
            # Update Y labels  
            y_labels = []
            for i in range(len(obj.YSpacing) + 1):
                if obj.YLabelingStyle == "Letters":
                    y_labels.append(chr(65 + i) if i < 26 else f"A{chr(65 + i - 26)}")
                elif obj.YLabelingStyle == "Numbers":
                    y_labels.append(str(i + 1))
                else:  # Custom
                    y_labels.append(f"Y{i + 1}")
            obj.YLabels = y_labels
            
            # Update Z labels
            z_labels = []
            for i, level in enumerate(obj.ZLevels):
                if level == 0:
                    z_labels.append("GF")  # Ground Floor
                elif i == 0:
                    z_labels.append("B1")  # Basement
                else:
                    z_labels.append(f"L{i}")  # Level
            obj.ZLabels = z_labels
            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error updating labels: {e}\n")
    
    def _apply_building_template(self, obj) -> None:
        """Apply building template to grid."""
        template = obj.BuildingTemplate
        
        if template == "Custom":
            return
        elif template == "Office Building":
            self._apply_office_template(obj)
        elif template == "Warehouse":
            self._apply_warehouse_template(obj)
        elif template == "Residential":
            self._apply_residential_template(obj)
        elif template == "Parking Garage":
            self._apply_parking_template(obj)
    
    def _apply_office_template(self, obj) -> None:
        """Apply office building template."""
        # Typical office building: 6-8m bays, 3.5-4m floor heights
        obj.XSpacing = [6000.0] * 5  # 5 bays @ 6m
        obj.YSpacing = [8000.0] * 3  # 3 bays @ 8m  
        obj.ZLevels = [0.0, 4000.0, 8000.0, 12000.0]  # 4 floors @ 4m
        obj.AutoGenerateBeams = True
        obj.AutoGenerateColumns = True
        obj.BeamLayout = "All Grids"
        obj.ColumnLayout = "All Intersections"
    
    def _apply_warehouse_template(self, obj) -> None:
        """Apply warehouse template."""
        # Typical warehouse: large bays, high ceilings
        obj.XSpacing = [12000.0] * 3  # 3 bays @ 12m
        obj.YSpacing = [20000.0] * 2  # 2 bays @ 20m
        obj.ZLevels = [0.0, 8000.0]  # Ground + roof
        obj.AutoGenerateBeams = True
        obj.AutoGenerateColumns = True
        obj.BeamLayout = "All Grids"
        obj.ColumnLayout = "All Intersections"
    
    def _apply_residential_template(self, obj) -> None:
        """Apply residential template."""
        # Typical residential: smaller bays, standard heights
        obj.XSpacing = [4000.0] * 4  # 4 bays @ 4m
        obj.YSpacing = [5000.0] * 3  # 3 bays @ 5m
        obj.ZLevels = [0.0, 3000.0, 6000.0, 9000.0]  # 4 floors @ 3m
        obj.AutoGenerateBeams = True
        obj.AutoGenerateColumns = True
        obj.BeamLayout = "All Grids"
        obj.ColumnLayout = "All Intersections"
    
    def _apply_parking_template(self, obj) -> None:
        """Apply parking garage template."""
        # Typical parking: 5.5m x 16m bays
        obj.XSpacing = [5500.0] * 6  # 6 bays @ 5.5m
        obj.YSpacing = [16000.0] * 2  # 2 bays @ 16m
        obj.ZLevels = [0.0, 3200.0, 6400.0]  # 3 levels @ 3.2m
        obj.AutoGenerateBeams = True
        obj.AutoGenerateColumns = True
        obj.BeamLayout = "All Grids"
        obj.ColumnLayout = "All Intersections"
    
    def _regenerate_members(self, obj) -> None:
        """Regenerate structural members based on current settings."""
        try:
            # Clear existing generated members
            self._clear_generated_members(obj)
            
            # Generate beams
            if obj.AutoGenerateBeams:
                self._generate_beams(obj)
            
            # Generate columns
            if obj.AutoGenerateColumns:
                self._generate_columns(obj)
            
            # Update statistics
            self._update_statistics(obj)
            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error regenerating members: {e}\n")
    
    def _clear_generated_members(self, obj) -> None:
        """Clear previously generated members."""
        doc = App.ActiveDocument
        
        # Remove generated beams
        if hasattr(obj, 'GeneratedBeams') and obj.GeneratedBeams:
            for beam in obj.GeneratedBeams:
                if hasattr(beam, 'Name') and doc.getObject(beam.Name):
                    doc.removeObject(beam.Name)
        
        # Remove generated columns
        if hasattr(obj, 'GeneratedColumns') and obj.GeneratedColumns:
            for column in obj.GeneratedColumns:
                if hasattr(column, 'Name') and doc.getObject(column.Name):
                    doc.removeObject(column.Name)
        
        # Remove generated nodes
        if hasattr(obj, 'GeneratedNodes') and obj.GeneratedNodes:
            for node in obj.GeneratedNodes:
                if hasattr(node, 'Name') and doc.getObject(node.Name):
                    doc.removeObject(node.Name)
        
        # Clear lists
        obj.GeneratedBeams = []
        obj.GeneratedColumns = []
        obj.GeneratedNodes = []
    
    def _generate_beams(self, obj) -> None:
        """Generate beam layout based on grid."""
        if not obj.GridNodes:
            return
        
        try:
            from .StructuralBeam import makeStructuralBeam
            
            generated_beams = []
            
            # Determine beam elevations
            beam_elevations = obj.BeamElevations if hasattr(obj, 'BeamElevations') and obj.BeamElevations else obj.ZLevels[1:]
            
            for level_idx, elevation in enumerate(beam_elevations):
                level_idx += 1  # Skip ground level for beams
                
                # Generate beams in X direction
                if self._should_generate_x_beams(obj, level_idx):
                    x_beams = self._generate_x_direction_beams(obj, level_idx, elevation)
                    generated_beams.extend(x_beams)
                
                # Generate beams in Y direction
                if self._should_generate_y_beams(obj, level_idx):
                    y_beams = self._generate_y_direction_beams(obj, level_idx, elevation)
                    generated_beams.extend(y_beams)
            
            obj.GeneratedBeams = generated_beams
            
        except ImportError:
            FreeCAD.Console.PrintWarning("StructuralBeam not available for generation\n")
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error generating beams: {e}\n")
    
    def _should_generate_x_beams(self, obj, level_idx: int) -> bool:
        """Check if X-direction beams should be generated."""
        layout = obj.BeamLayout
        
        if layout == "All Grids":
            return True
        elif layout == "Perimeter Only":
            return level_idx == 1 or level_idx == len(obj.ZLevels) - 1
        elif layout == "Interior Only":
            return 1 < level_idx < len(obj.ZLevels) - 1
        else:  # Custom Pattern
            return True  # Would check custom pattern
    
    def _should_generate_y_beams(self, obj, level_idx: int) -> bool:
        """Check if Y-direction beams should be generated."""
        return self._should_generate_x_beams(obj, level_idx)  # Same logic for now
    
    def _generate_x_direction_beams(self, obj, level_idx: int, elevation: float) -> List:
        """Generate beams in X direction."""
        beams = []
        
        try:
            from .StructuralBeam import makeStructuralBeam
            
            x_coords = self._calculate_grid_coordinates(obj.XSpacing, obj.GridOrigin.x)
            y_coords = self._calculate_grid_coordinates(obj.YSpacing, obj.GridOrigin.y)
            
            # For each Y grid line, create beams along X
            for j, y in enumerate(y_coords):
                for i in range(len(x_coords) - 1):
                    start_point = App.Vector(x_coords[i], y, elevation)
                    end_point = App.Vector(x_coords[i + 1], y, elevation)
                    
                    beam_name = f"Beam_{obj.YLabels[j] if j < len(obj.YLabels) else j}_{level_idx}_X"
                    beam = makeStructuralBeam(start_point=start_point, end_point=end_point, name=beam_name)
                    
                    if beam:
                        # Set section and material if available
                        if obj.DefaultBeamSection:
                            beam.Section = obj.DefaultBeamSection
                        if obj.DefaultMaterial:
                            beam.Material = obj.DefaultMaterial
                        
                        beams.append(beam)
                        
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error generating X-direction beams: {e}\n")
        
        return beams
    
    def _generate_y_direction_beams(self, obj, level_idx: int, elevation: float) -> List:
        """Generate beams in Y direction."""
        beams = []
        
        try:
            from .StructuralBeam import makeStructuralBeam
            
            x_coords = self._calculate_grid_coordinates(obj.XSpacing, obj.GridOrigin.x)
            y_coords = self._calculate_grid_coordinates(obj.YSpacing, obj.GridOrigin.y)
            
            # For each X grid line, create beams along Y
            for i, x in enumerate(x_coords):
                for j in range(len(y_coords) - 1):
                    start_point = App.Vector(x, y_coords[j], elevation)
                    end_point = App.Vector(x, y_coords[j + 1], elevation)
                    
                    beam_name = f"Beam_{obj.XLabels[i] if i < len(obj.XLabels) else i}_{level_idx}_Y"
                    beam = makeStructuralBeam(start_point=start_point, end_point=end_point, name=beam_name)
                    
                    if beam:
                        # Set section and material if available
                        if obj.DefaultBeamSection:
                            beam.Section = obj.DefaultBeamSection
                        if obj.DefaultMaterial:
                            beam.Material = obj.DefaultMaterial
                        
                        beams.append(beam)
                        
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error generating Y-direction beams: {e}\n")
        
        return beams
    
    def _generate_columns(self, obj) -> None:
        """Generate column layout based on grid."""
        if not obj.GridNodes:
            return
        
        try:
            from .StructuralColumn import makeStructuralColumn
            
            generated_columns = []
            
            x_coords = self._calculate_grid_coordinates(obj.XSpacing, obj.GridOrigin.x)
            y_coords = self._calculate_grid_coordinates(obj.YSpacing, obj.GridOrigin.y)
            
            # Generate columns at grid intersections
            for i, x in enumerate(x_coords):
                for j, y in enumerate(y_coords):
                    if self._should_generate_column_at(obj, i, j):
                        columns = self._generate_column_stack(obj, i, j, x, y)
                        generated_columns.extend(columns)
            
            obj.GeneratedColumns = generated_columns
            
        except ImportError:
            FreeCAD.Console.PrintWarning("StructuralColumn not available for generation\n")
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error generating columns: {e}\n")
    
    def _should_generate_column_at(self, obj, x_idx: int, y_idx: int) -> bool:
        """Check if column should be generated at grid intersection."""
        layout = obj.ColumnLayout
        
        if layout == "All Intersections":
            return True
        elif layout == "Perimeter Only":
            is_perimeter = (x_idx == 0 or x_idx == len(obj.XSpacing) or 
                          y_idx == 0 or y_idx == len(obj.YSpacing))
            return is_perimeter
        elif layout == "Interior Only":
            is_interior = (0 < x_idx < len(obj.XSpacing) and 
                         0 < y_idx < len(obj.YSpacing))
            return is_interior
        else:  # Custom Pattern
            return True  # Would check custom pattern
    
    def _generate_column_stack(self, obj, x_idx: int, y_idx: int, x: float, y: float) -> List:
        """Generate stack of columns at a grid intersection."""
        columns = []
        
        try:
            from .StructuralColumn import makeStructuralColumn
            
            # Generate columns between each level
            for k in range(len(obj.ZLevels) - 1):
                base_level = obj.ZLevels[k]
                top_level = obj.ZLevels[k + 1]
                
                base_point = App.Vector(x, y, base_level)
                top_point = App.Vector(x, y, top_level)
                
                x_label = obj.XLabels[x_idx] if x_idx < len(obj.XLabels) else str(x_idx)
                y_label = obj.YLabels[y_idx] if y_idx < len(obj.YLabels) else chr(65 + y_idx)
                
                column_name = f"Column_{y_label}{x_label}_{k+1}"
                column = makeStructuralColumn(base_point=base_point, top_point=top_point, name=column_name)
                
                if column:
                    # Set grid location
                    column.GridLocation = f"{y_label}{x_label}"
                    
                    # Set section and material if available
                    if obj.DefaultColumnSection:
                        column.Section = obj.DefaultColumnSection
                    if obj.DefaultMaterial:
                        column.Material = obj.DefaultMaterial
                    
                    columns.append(column)
                    
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error generating column stack: {e}\n")
        
        return columns
    
    def _create_grid_visualization(self, obj, x_coords: List[float], y_coords: List[float], z_coords: List[float]) -> None:
        """Create 3D visualization of grid lines."""
        try:
            # This would create grid line visualization
            # For now, just update the shape with boundary lines
            
            lines = []
            
            # Create X-direction grid lines
            for y in y_coords:
                for z in z_coords:
                    start = App.Vector(x_coords[0], y, z)
                    end = App.Vector(x_coords[-1], y, z)
                    lines.append(Part.makeLine(start, end))
            
            # Create Y-direction grid lines
            for x in x_coords:
                for z in z_coords:
                    start = App.Vector(x, y_coords[0], z)
                    end = App.Vector(x, y_coords[-1], z)
                    lines.append(Part.makeLine(start, end))
            
            # Create level lines (vertical)
            if len(z_coords) > 1:
                for x in x_coords:
                    for y in y_coords:
                        start = App.Vector(x, y, z_coords[0])
                        end = App.Vector(x, y, z_coords[-1])
                        lines.append(Part.makeLine(start, end))
            
            if lines:
                compound = Part.makeCompound(lines)
                obj.Shape = compound
                
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error creating grid visualization: {e}\n")
    
    def _update_statistics(self, obj) -> None:
        """Update grid statistics."""
        try:
            obj.NumberOfColumns = len(obj.GeneratedColumns) if hasattr(obj, 'GeneratedColumns') else 0
            obj.NumberOfBeams = len(obj.GeneratedBeams) if hasattr(obj, 'GeneratedBeams') else 0
            
        except Exception as e:
            FreeCAD.Console.PrintWarning(f"Error updating statistics: {e}\n")
    
    def execute(self, obj) -> None:
        """
        Update grid and regenerate members if needed.
        
        Args:
            obj: The DocumentObject being executed
        """
        # Update grid geometry
        self._update_grid_geometry(obj)
        
        # Update labels
        self._update_labels(obj)
        
        # Regenerate members if auto-generation is enabled
        if obj.AutoGenerateBeams or obj.AutoGenerateColumns:
            self._regenerate_members(obj)


class ViewProviderStructuralGrid:
    """
    ViewProvider for StructuralGrid with enhanced visualization.
    """
    
    def __init__(self, vobj):
        """Initialize ViewProvider."""
        vobj.Proxy = self
        self.Object = vobj.Object
        
        # Visualization properties
        vobj.addProperty("App::PropertyBool", "ShowDimensions", "Display",
                        "Show grid dimensions")
        vobj.ShowDimensions = False
        
        vobj.addProperty("App::PropertyFloat", "GridTransparency", "Display",
                        "Grid line transparency")
        vobj.GridTransparency = 80.0
        
        vobj.addProperty("App::PropertyBool", "ShowBoundingBox", "Display",
                        "Show grid bounding box")
        vobj.ShowBoundingBox = True
    
    def getIcon(self) -> str:
        """Return icon for structural grid."""
        return self._get_icon_path("structural_grid.svg")
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icon_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")
        return os.path.join(icon_dir, icon_name)
    
    def setEdit(self, vobj, mode: int) -> bool:
        """Open grid properties panel."""
        if mode == 0:
            try:
                from ..taskpanels.GridPropertiesPanel import GridPropertiesPanel
                self.panel = GridPropertiesPanel(vobj.Object)
                Gui.Control.showDialog(self.panel)
                return True
            except ImportError:
                FreeCAD.Console.PrintWarning("GridPropertiesPanel not yet implemented\n")
                return False
        return False
    
    def unsetEdit(self, vobj, mode: int) -> bool:
        """Close grid properties panel."""
        if hasattr(self, 'panel'):
            Gui.Control.closeDialog()
        return True
    
    def doubleClicked(self, vobj) -> bool:
        """Handle double-click to open properties."""
        return self.setEdit(vobj, 0)


def makeStructuralGrid(x_spacing=None, y_spacing=None, z_levels=None, name="StructuralGrid"):
    """
    Create a new StructuralGrid object.
    
    Args:
        x_spacing: List of X-direction bay widths
        y_spacing: List of Y-direction bay depths  
        z_levels: List of floor levels
        name: Object name
        
    Returns:
        Created StructuralGrid object
    """
    doc = App.ActiveDocument
    if not doc:
        FreeCAD.Console.PrintError("No active document. Please create or open a document first.\n")
        return None
    
    # Create the object
    obj = doc.addObject("App::DocumentObjectGroupPython", name)
    StructuralGrid(obj)
    
    # Create ViewProvider
    if App.GuiUp:
        ViewProviderStructuralGrid(obj.ViewObject)
    
    # Set properties
    if x_spacing:
        obj.XSpacing = x_spacing
    if y_spacing:
        obj.YSpacing = y_spacing
    if z_levels:
        obj.ZLevels = z_levels
    
    # Recompute to update geometry
    obj.recompute()
    doc.recompute()
    
    FreeCAD.Console.PrintMessage(f"Created StructuralGrid: {obj.Label}\n")
    return obj