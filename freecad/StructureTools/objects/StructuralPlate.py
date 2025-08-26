# -*- coding: utf-8 -*-
"""
StructuralPlate - Professional plate/shell element object with advanced capabilities

This module provides a comprehensive plate/shell object for structural engineering
with surface loads, membrane and bending properties, and buckling analysis.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft
from typing import List, Dict, Tuple, Optional, Any
import math
import os


class StructuralPlate:
    """
    Custom Document Object for structural plates and shells with enhanced functionality.
    
    This class provides professional-grade plate/shell objects for structural analysis
    with surface loads, membrane forces, bending moments, and stability checks.
    """
    
    def __init__(self, obj):
        """
        Initialize StructuralPlate object.
        
        Args:
            obj: FreeCAD DocumentObject to be enhanced
        """
        self.Type = "StructuralPlate"
        obj.Proxy = self
        
        # Geometric properties
        obj.addProperty("App::PropertyLinkList", "CornerNodes", "Geometry",
                       "Corner nodes defining the plate (3 or 4 nodes)")
        
        obj.addProperty("App::PropertyVector", "LocalXAxis", "Geometry",
                       "Local X-axis direction (in-plane)")
        
        obj.addProperty("App::PropertyVector", "LocalYAxis", "Geometry", 
                       "Local Y-axis direction (in-plane)")
        
        obj.addProperty("App::PropertyVector", "LocalZAxis", "Geometry",
                       "Local Z-axis direction (normal to plate)")
        
        obj.addProperty("App::PropertyArea", "Area", "Geometry",
                       "Plate area (calculated)")
        
        obj.addProperty("App::PropertyLength", "Perimeter", "Geometry",
                       "Plate perimeter (calculated)")
        
        # Plate properties
        obj.addProperty("App::PropertyLength", "Thickness", "Plate",
                       "Plate thickness")
        obj.Thickness = "200 mm"  # Default 200mm
        
        obj.addProperty("App::PropertyEnumeration", "PlateType", "Plate",
                       "Type of plate element")
        obj.PlateType = ["Thin Plate", "Thick Plate", "Shell", "Membrane"]
        obj.PlateType = "Thin Plate"
        
        obj.addProperty("App::PropertyBool", "IncludeMembraneAction", "Plate",
                       "Include membrane forces in analysis")
        obj.IncludeMembraneAction = True
        
        obj.addProperty("App::PropertyBool", "IncludeBendingAction", "Plate",
                       "Include bending moments in analysis")
        obj.IncludeBendingAction = True
        
        obj.addProperty("App::PropertyBool", "IncludeShearDeformation", "Plate",
                       "Include transverse shear deformation (thick plate)")
        obj.IncludeShearDeformation = False
        
        # Material reference
        obj.addProperty("App::PropertyLink", "Material", "Material",
                       "Reference to StructuralMaterial object")
        
        # Section properties (calculated from thickness and material)
        obj.addProperty("App::PropertyFloat", "MembraneBendingRatio", "Properties",
                       "Ratio of membrane to bending stiffness")
        
        obj.addProperty("App::PropertyFloat", "AspectRatio", "Properties",
                       "Plate aspect ratio (length/width)")
        
        # Surface loading properties
        obj.addProperty("App::PropertyFloatList", "PressureLoads", "Loads",
                       "Pressure loads normal to surface by load case (Pa)")
        
        obj.addProperty("App::PropertyFloatList", "ShearLoadsX", "Loads",
                       "In-plane shear loads in local X direction by load case")
        
        obj.addProperty("App::PropertyFloatList", "ShearLoadsY", "Loads",
                       "In-plane shear loads in local Y direction by load case")
        
        obj.addProperty("App::PropertyFloatList", "ThermalLoads", "Loads",
                       "Temperature loads by load case (°C)")
        
        # Thai Units Support
        obj.addProperty("App::PropertyBool", "UseThaiUnits", "Thai Units",
                       "Enable Thai units for plate load calculations")
        obj.UseThaiUnits = False
        
        obj.addProperty("App::PropertyFloatList", "PressureLoadsKsc", "Thai Units",
                       "Pressure loads in ksc/m² (Thai units)")
        
        obj.addProperty("App::PropertyFloatList", "PressureLoadsTfM2", "Thai Units",
                       "Pressure loads in tf/m² (Thai units)")
        
        obj.addProperty("App::PropertyFloatList", "ShearLoadsKgfM", "Thai Units",
                       "In-plane shear loads in kgf/m (Thai units)")
        
        obj.addProperty("App::PropertyFloatList", "TemperatureGradient", "Loads",
                       "Temperature gradient through thickness by load case (°C/mm)")
        
        # Load distribution patterns
        obj.addProperty("App::PropertyEnumeration", "LoadPattern", "Loads",
                       "Load distribution pattern over plate surface")
        obj.LoadPattern = ["Uniform", "Linear X", "Linear Y", "Bilinear", "Point", "Custom"]
        obj.LoadPattern = "Uniform"
        
        obj.addProperty("App::PropertyFloatList", "LoadFactors", "Loads",
                       "Load factors for pattern distribution")
        
        # Boundary conditions
        obj.addProperty("App::PropertyEnumeration", "EdgeCondition1", "Boundary",
                       "Boundary condition for edge 1")
        obj.EdgeCondition1 = ["Free", "Simply Supported", "Fixed", "Elastic"]
        obj.EdgeCondition1 = "Simply Supported"
        
        obj.addProperty("App::PropertyEnumeration", "EdgeCondition2", "Boundary",
                       "Boundary condition for edge 2")
        obj.EdgeCondition2 = ["Free", "Simply Supported", "Fixed", "Elastic"]
        obj.EdgeCondition2 = "Simply Supported"
        
        obj.addProperty("App::PropertyEnumeration", "EdgeCondition3", "Boundary",
                       "Boundary condition for edge 3")
        obj.EdgeCondition3 = ["Free", "Simply Supported", "Fixed", "Elastic"]
        obj.EdgeCondition3 = "Simply Supported"
        
        obj.addProperty("App::PropertyEnumeration", "EdgeCondition4", "Boundary",
                       "Boundary condition for edge 4 (if quad)")
        obj.EdgeCondition4 = ["Free", "Simply Supported", "Fixed", "Elastic"]
        obj.EdgeCondition4 = "Simply Supported"
        
        # Edge spring properties
        obj.addProperty("App::PropertyFloatList", "EdgeSprings", "Boundary",
                       "Spring stiffness for elastic edge supports")
        
        # Analysis results
        obj.addProperty("App::PropertyFloatList", "DisplacementsZ", "Results",
                       "Out-of-plane displacements by load combination")
        
        obj.addProperty("App::PropertyFloatList", "DisplacementsX", "Results",
                       "In-plane displacements X by load combination")
        
        obj.addProperty("App::PropertyFloatList", "DisplacementsY", "Results",
                       "In-plane displacements Y by load combination")
        
        # Membrane forces (per unit width)
        obj.addProperty("App::PropertyFloatList", "MembraneForceX", "Results",
                       "Membrane force Nx by load combination")
        
        obj.addProperty("App::PropertyFloatList", "MembraneForceY", "Results",
                       "Membrane force Ny by load combination")
        
        obj.addProperty("App::PropertyFloatList", "MembraneShearXY", "Results",
                       "Membrane shear force Nxy by load combination")
        
        # Bending moments (per unit width)
        obj.addProperty("App::PropertyFloatList", "BendingMomentX", "Results",
                       "Bending moment Mx by load combination")
        
        obj.addProperty("App::PropertyFloatList", "BendingMomentY", "Results",
                       "Bending moment My by load combination")
        
        obj.addProperty("App::PropertyFloatList", "TwistingMoment", "Results",
                       "Twisting moment Mxy by load combination")
        
        # Transverse shear forces (per unit width)
        obj.addProperty("App::PropertyFloatList", "ShearForceX", "Results",
                       "Transverse shear force Qx by load combination")
        
        obj.addProperty("App::PropertyFloatList", "ShearForceY", "Results",
                       "Transverse shear force Qy by load combination")
        
        # Stress results
        obj.addProperty("App::PropertyFloatList", "MaxStress", "Results",
                       "Maximum stress by load combination")
        
        obj.addProperty("App::PropertyFloatList", "MinStress", "Results",
                       "Minimum stress by load combination")
        
        obj.addProperty("App::PropertyFloatList", "VonMisesStress", "Results",
                       "Von Mises stress by load combination")
        
        # Buckling analysis
        obj.addProperty("App::PropertyFloatList", "BucklingFactors", "Stability",
                       "Critical buckling load factors")
        
        obj.addProperty("App::PropertyFloatList", "BucklingModes", "Stability",
                       "Buckling mode shapes")
        
        # Meshing properties
        obj.addProperty("App::PropertyInteger", "MeshDivisionsX", "Mesh",
                       "Number of mesh divisions in X direction")
        obj.MeshDivisionsX = 4
        
        obj.addProperty("App::PropertyInteger", "MeshDivisionsY", "Mesh",
                       "Number of mesh divisions in Y direction")
        obj.MeshDivisionsY = 4
        
        obj.addProperty("App::PropertyEnumeration", "ElementType", "Mesh",
                       "Type of finite element for analysis")
        obj.ElementType = ["Quad4", "Quad8", "Quad9", "Tri3", "Tri6"]
        obj.ElementType = "Quad4"
        
        obj.addProperty("App::PropertyBool", "AutoMesh", "Mesh",
                       "Automatically generate mesh")
        obj.AutoMesh = True
        
        # Visualization properties
        obj.addProperty("App::PropertyBool", "ShowLocalAxes", "Display",
                       "Show local coordinate axes")
        obj.ShowLocalAxes = False
        
        obj.addProperty("App::PropertyBool", "ShowLoads", "Display",
                       "Show surface loads")
        obj.ShowLoads = True
        
        obj.addProperty("App::PropertyBool", "ShowResults", "Display",
                       "Show analysis results")
        obj.ShowResults = False
        
        obj.addProperty("App::PropertyEnumeration", "ResultsType", "Display",
                       "Type of results to display")
        obj.ResultsType = ["Displacement", "Stress", "Membrane Force", "Bending Moment"]
        obj.ResultsType = "Displacement"
        
        # Initialize calculations
        self.calculatePlateProperties(obj)
    
    def calculatePlateProperties(self, obj):
        """Calculate basic plate properties."""
        try:
            if not obj.CornerNodes:
                return
            
            # Calculate area and perimeter
            self.updateGeometry(obj)
            
            # Calculate aspect ratio
            if hasattr(obj, 'Area') and obj.Area > 0:
                # Simplified aspect ratio calculation
                obj.AspectRatio = math.sqrt(obj.Area.Value / 1000000)  # Basic estimate
                
        except Exception as e:
            App.Console.PrintError(f"Error calculating plate properties: {e}\n")
    
    def updateGeometry(self, obj):
        """Update plate geometry based on corner nodes."""
        if not obj.CornerNodes or len(obj.CornerNodes) < 3:
            return
        
        try:
            # Get node positions
            points = []
            for node in obj.CornerNodes:
                if hasattr(node, 'Position'):
                    points.append(node.Position)
                else:
                    App.Console.PrintWarning("Node missing Position property\n")
                    return
            
            # Create plate surface
            if len(points) == 3:
                # Triangular plate
                face = Part.Face(Part.makePolygon(points + [points[0]]))
            elif len(points) == 4:
                # Quadrilateral plate
                face = Part.Face(Part.makePolygon(points + [points[0]]))
            else:
                App.Console.PrintError("Plate must have 3 or 4 corner nodes\n")
                return
                
            # Update properties
            obj.Area = face.Area
            obj.Perimeter = face.Perimeter
            
            # Calculate local axes
            self.calculateLocalAxes(obj, points)
            
        except Exception as e:
            App.Console.PrintError(f"Error updating plate geometry: {e}\n")
    
    def calculateLocalAxes(self, obj, points):
        """Calculate local coordinate system for the plate."""
        try:
            if len(points) < 3:
                return
                
            # Local X-axis: from node 1 to node 2
            x_vec = points[1] - points[0]
            x_vec.normalize()
            obj.LocalXAxis = x_vec
            
            # Local Z-axis: normal to plane (cross product)
            if len(points) >= 3:
                y_temp = points[2] - points[0]
                z_vec = x_vec.cross(y_temp)
                z_vec.normalize()
                obj.LocalZAxis = z_vec
                
                # Local Y-axis: complete right-handed system
                y_vec = z_vec.cross(x_vec)
                y_vec.normalize()
                obj.LocalYAxis = y_vec
                
        except Exception as e:
            App.Console.PrintError(f"Error calculating local axes: {e}\n")
        obj.addProperty("App::PropertyInteger", "InternalID", "Internal",
                       "Internal numbering for analysis")
        
        obj.addProperty("App::PropertyBool", "IsActive", "Internal",
                       "Plate is active in current analysis")
        obj.IsActive = True
    
    def getLoadsInThaiUnits(self, obj):
        """Get plate loads in Thai units"""
        if not hasattr(obj, 'UseThaiUnits') or not obj.UseThaiUnits:
            return None
            
        try:
            # Import Thai units converter
            from ..utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            
            thai_results = {
                'pressure_loads_ksc': [],
                'pressure_loads_tf_m2': [],
                'shear_loads_kgf_m': []
            }
            
            # Convert pressure loads
            if hasattr(obj, 'PressureLoads') and obj.PressureLoads:
                for pressure_pa in obj.PressureLoads:
                    # Convert Pa to kN/m² first, then to Thai units
                    pressure_kn_m2 = pressure_pa / 1000.0  # Pa to kN/m²
                    ksc_value = converter.kn_m2_to_ksc_m2(pressure_kn_m2)
                    tf_value = converter.kn_m2_to_tf_m2(pressure_kn_m2)
                    thai_results['pressure_loads_ksc'].append(ksc_value)
                    thai_results['pressure_loads_tf_m2'].append(tf_value)
            
            # Convert shear loads
            if hasattr(obj, 'ShearLoadsX') and obj.ShearLoadsX:
                for shear_n_m in obj.ShearLoadsX:
                    # Convert N/m to kN/m first, then to kgf/m
                    shear_kn_m = shear_n_m / 1000.0  # N/m to kN/m
                    kgf_value = converter.kn_to_kgf(shear_kn_m)
                    thai_results['shear_loads_kgf_m'].append(kgf_value)
            
            # Update Thai unit properties
            obj.PressureLoadsKsc = thai_results['pressure_loads_ksc']
            obj.PressureLoadsTfM2 = thai_results['pressure_loads_tf_m2']
            obj.ShearLoadsKgfM = thai_results['shear_loads_kgf_m']
            
            return thai_results
            
        except Exception as e:
            App.Console.PrintError(f"Error converting plate loads to Thai units: {e}\n")
            return None
    
    def updateThaiUnits(self, obj):
        """Update Thai units when properties change"""
        if hasattr(obj, 'UseThaiUnits') and obj.UseThaiUnits:
            self.getLoadsInThaiUnits(obj)
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        if prop == "CornerNodes":
            self._update_geometry(obj)
        elif prop == "Material":
            self._update_material_properties(obj)
        elif prop == "Thickness":
            self._update_section_properties(obj)
        elif prop == "PlateType":
            self._update_plate_behavior(obj)
        elif prop in ["EdgeCondition1", "EdgeCondition2", "EdgeCondition3", "EdgeCondition4"]:
            self._update_boundary_conditions(obj)
        elif prop in ["PressureLoads", "ShearLoadsX", "ShearLoadsY"]:
            # Update Thai units when loads change
            if hasattr(obj, 'UseThaiUnits') and obj.UseThaiUnits:
                self.updateThaiUnits(obj)
    
    def _update_geometry(self, obj) -> None:
        """Update geometric properties when corner nodes change."""
        if not hasattr(obj, 'CornerNodes') or len(obj.CornerNodes) < 3:
            return
        
        try:
            # Get node positions
            nodes = obj.CornerNodes
            if len(nodes) < 3:
                return
            
            # Create plate surface
            if len(nodes) == 3:
                # Triangular plate
                points = [node.Position for node in nodes]
                wire = Part.makePolygon(points + [points[0]])
                face = Part.Face(wire)
            elif len(nodes) == 4:
                # Quadrilateral plate
                points = [node.Position for node in nodes]
                wire = Part.makePolygon(points + [points[0]])
                face = Part.Face(wire)
            else:
                App.Console.PrintWarning("Plate supports 3 or 4 corner nodes only\n")
                return
            
            # Calculate geometric properties
            obj.Area = f"{face.Area} mm^2"
            obj.Perimeter = f"{wire.Length} mm"
            
            # Calculate local coordinate system
            self._calculate_local_coordinates(obj, points)
            
            # Update visual representation
            self._update_visual_representation(obj, face)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating plate geometry: {e}\n")
    
    def _calculate_local_coordinates(self, obj, points: List) -> None:
        """Calculate local coordinate system for the plate."""
        if len(points) < 3:
            return
        
        try:
            # Local X-axis (from point 1 to point 2)
            local_x = (points[1] - points[0]).normalize()
            obj.LocalXAxis = local_x
            
            # Local Z-axis (normal to plate surface)
            vec1 = points[1] - points[0]
            vec2 = points[2] - points[0]
            local_z = vec1.cross(vec2).normalize()
            obj.LocalZAxis = local_z
            
            # Local Y-axis (perpendicular to X and Z)
            local_y = local_z.cross(local_x)
            obj.LocalYAxis = local_y
            
            # Calculate aspect ratio
            if len(points) == 4:
                length1 = points[0].distanceToPoint(points[1])
                length2 = points[1].distanceToPoint(points[2])
                obj.AspectRatio = max(length1, length2) / min(length1, length2)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating local coordinates: {e}\n")
    
    def _update_material_properties(self, obj) -> None:
        """Update properties when material changes."""
        if not hasattr(obj, 'Material') or not obj.Material:
            return
        
        material = obj.Material
        if hasattr(material, 'ModulusElasticity') and hasattr(material, 'PoissonRatio'):
            try:
                # Calculate membrane/bending stiffness ratio
                E = material.ModulusElasticity.getValueAs('MPa')
                nu = material.PoissonRatio
                t = obj.Thickness.getValueAs('mm') if hasattr(obj, 'Thickness') else 200
                
                # Membrane stiffness per unit width
                A = E * t / (1 - nu**2)
                
                # Bending stiffness per unit width
                D = E * t**3 / (12 * (1 - nu**2))
                
                # Ratio
                obj.MembraneBendingRatio = A * t**2 / (12 * D) if D > 0 else 0
                
            except Exception as e:
                App.Console.PrintWarning(f"Error updating material properties: {e}\n")
    
    def _update_section_properties(self, obj) -> None:
        """Update section properties when thickness changes."""
        # Recalculate material-dependent properties
        self._update_material_properties(obj)
    
    def _update_plate_behavior(self, obj) -> None:
        """Update analysis behavior based on plate type."""
        if not hasattr(obj, 'PlateType'):
            return
        
        plate_type = obj.PlateType
        
        if plate_type == "Thin Plate":
            obj.IncludeMembraneAction = False
            obj.IncludeBendingAction = True
            obj.IncludeShearDeformation = False
        elif plate_type == "Thick Plate":
            obj.IncludeMembraneAction = True
            obj.IncludeBendingAction = True
            obj.IncludeShearDeformation = True
        elif plate_type == "Shell":
            obj.IncludeMembraneAction = True
            obj.IncludeBendingAction = True
            obj.IncludeShearDeformation = False
        elif plate_type == "Membrane":
            obj.IncludeMembraneAction = True
            obj.IncludeBendingAction = False
            obj.IncludeShearDeformation = False
    
    def _update_boundary_conditions(self, obj) -> None:
        """Update boundary condition properties."""
        # This would update analysis properties based on edge conditions
        pass
    
    def _update_visual_representation(self, obj, face) -> None:
        """Update the 3D visual representation of the plate."""
        try:
            if hasattr(obj, 'Thickness'):
                thickness = obj.Thickness.getValueAs('mm')
                
                # Create solid by extruding face
                extrusion_vector = obj.LocalZAxis * thickness
                solid = face.extrude(extrusion_vector)
                obj.Shape = solid
            else:
                # Just show the surface
                obj.Shape = face
                
        except Exception as e:
            App.Console.PrintWarning(f"Error updating plate visualization: {e}\n")
            obj.Shape = face
    
    def execute(self, obj) -> None:
        """
        Update plate geometry and validate properties.
        
        Args:
            obj: The DocumentObject being executed
        """
        # Update geometry
        self._update_geometry(obj)
        
        # Validate material assignment
        if not hasattr(obj, 'Material') or not obj.Material:
            App.Console.PrintWarning(f"Plate {obj.Label}: No material assigned\n")
        
        # Validate load consistency
        self._validate_load_consistency(obj)
        
        # Update derived properties
        self._update_material_properties(obj)
    
    def _validate_load_consistency(self, obj) -> None:
        """Validate load arrays have consistent lengths."""
        load_properties = [
            'PressureLoads', 'ShearLoadsX', 'ShearLoadsY', 'ThermalLoads'
        ]
        
        lengths = []
        for prop in load_properties:
            if hasattr(obj, prop):
                lengths.append(len(getattr(obj, prop, [])))
        
        if lengths and len(set(lengths)) > 1:
            App.Console.PrintWarning(
                f"Plate {obj.Label}: Inconsistent load case count across load types\n"
            )
    
    def get_stiffness_matrix(self, obj) -> List[List[float]]:
        """
        Calculate local stiffness matrix for the plate element.
        
        Args:
            obj: The DocumentObject
            
        Returns:
            Stiffness matrix for plate element
        """
        if not hasattr(obj, 'Material') or not obj.Material:
            return []
        
        try:
            # Material properties
            E = obj.Material.ModulusElasticity.getValueAs('MPa')
            nu = obj.Material.PoissonRatio
            t = obj.Thickness.getValueAs('mm')
            
            # Membrane stiffness matrix
            membrane_factor = E * t / (1 - nu**2)
            
            # Bending stiffness matrix  
            bending_factor = E * t**3 / (12 * (1 - nu**2))
            
            # This is simplified - actual implementation would depend on 
            # element formulation (triangular vs quadrilateral)
            # and would return proper DOF arrangement
            
            return self._calculate_element_stiffness(membrane_factor, bending_factor, nu)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating plate stiffness: {e}\n")
            return []
    
    def _calculate_element_stiffness(self, A_factor: float, D_factor: float, nu: float) -> List[List[float]]:
        """Calculate element stiffness matrix (simplified)."""
        # This is a placeholder - actual implementation would use 
        # finite element formulation for plate elements
        # Returns 6x6 matrix for triangular element or 8x8 for quad
        
        size = 6  # Simplified for triangular element
        k_matrix = [[0.0] * size for _ in range(size)]
        
        # Placeholder values - actual implementation would use
        # shape functions and numerical integration
        diagonal_value = A_factor + D_factor
        for i in range(size):
            k_matrix[i][i] = diagonal_value
        
        return k_matrix
    
    def get_equivalent_nodal_loads(self, obj, load_case: int = 0) -> List[float]:
        """
        Get equivalent nodal loads for surface loads.
        
        Args:
            obj: The DocumentObject
            load_case: Load case index
            
        Returns:
            Equivalent nodal load vector
        """
        loads = []
        
        if not (hasattr(obj, 'Area') and hasattr(obj, 'CornerNodes')):
            return loads
        
        try:
            area = obj.Area.getValueAs('mm^2')
            num_nodes = len(obj.CornerNodes)
            
            # Get pressure load for this load case
            pressure = 0.0
            if hasattr(obj, 'PressureLoads') and len(obj.PressureLoads) > load_case:
                pressure = obj.PressureLoads[load_case]
            
            # Distribute pressure load to corner nodes
            # For uniform pressure, each node gets 1/n of total load
            total_load = pressure * area
            nodal_load = total_load / num_nodes
            
            # Create load vector (simplified - actual would depend on DOF arrangement)
            loads = [0.0] * (num_nodes * 3)  # 3 DOF per node (simplified)
            
            # Apply vertical loads (in local Z direction)
            for i in range(num_nodes):
                loads[i * 3 + 2] = nodal_load  # Z-direction load
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating equivalent loads: {e}\n")
        
        return loads


class ViewProviderStructuralPlate:
    """
    ViewProvider for StructuralPlate with enhanced visualization and editing.
    """
    
    def __init__(self, vobj):
        """Initialize ViewProvider."""
        vobj.Proxy = self
        self.Object = vobj.Object
        
        # Visualization properties
        vobj.addProperty("App::PropertyBool", "ShowLocalAxes", "Display",
                        "Show local coordinate system")
        vobj.ShowLocalAxes = False
        
        vobj.addProperty("App::PropertyBool", "ShowLoads", "Display",
                        "Show applied surface loads") 
        vobj.ShowLoads = True
        
        vobj.addProperty("App::PropertyBool", "ShowBoundaryConditions", "Display",
                        "Show boundary conditions")
        vobj.ShowBoundaryConditions = True
        
        vobj.addProperty("App::PropertyEnumeration", "ResultsDisplay", "Results",
                        "Type of results to display")
        vobj.ResultsDisplay = ["None", "Displacements", "Membrane Forces", "Bending Moments", "Stresses"]
        vobj.ResultsDisplay = "None"
        
        vobj.addProperty("App::PropertyFloat", "ResultScale", "Results",
                        "Result display scale factor")
        vobj.ResultScale = 1.0
        
        vobj.addProperty("App::PropertyColor", "PlateColor", "Display",
                        "Plate color")
        vobj.PlateColor = (0.8, 0.8, 0.9)  # Light blue-gray
        
        vobj.addProperty("App::PropertyFloat", "Transparency", "Display",
                        "Plate transparency (0-100)")
        vobj.Transparency = 20.0
    
    def getIcon(self) -> str:
        """
        Return icon based on plate type and status.
        
        Returns:
            Path to appropriate icon file
        """
        if not hasattr(self.Object, 'PlateType'):
            return self._get_icon_path("plate_generic.svg")
        
        plate_type = getattr(self.Object, 'PlateType', 'Thin Plate').lower()
        
        # Check for analysis results
        has_results = (hasattr(self.Object, 'UtilizationRatios') and 
                      len(self.Object.UtilizationRatios) > 0)
        
        if has_results:
            max_util = max(self.Object.UtilizationRatios) if self.Object.UtilizationRatios else 0
            if max_util > 1.0:
                return self._get_icon_path("plate_overstressed.svg")
            elif max_util > 0.8:
                return self._get_icon_path("plate_warning.svg")
            else:
                return self._get_icon_path("plate_ok.svg")
        
        # Icon based on type
        if "shell" in plate_type:
            return self._get_icon_path("shell_generic.svg")
        elif "membrane" in plate_type:
            return self._get_icon_path("membrane_generic.svg")
        else:
            return self._get_icon_path("plate_generic.svg")
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icon_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")
        return os.path.join(icon_dir, icon_name)
    
    def setEdit(self, vobj, mode: int) -> bool:
        """
        Open custom task panel for plate editing.
        
        Args:
            vobj: ViewObject being edited
            mode: Edit mode
            
        Returns:
            True if edit mode started successfully
        """
        if mode == 0:
            from ..taskpanels.PlatePropertiesPanel import PlatePropertiesPanel
            self.panel = PlatePropertiesPanel(vobj.Object)
            Gui.Control.showDialog(self.panel)
            return True
        return False
    
    def unsetEdit(self, vobj, mode: int) -> bool:
        """Close plate editing panel."""
        Gui.Control.closeDialog()
        return True
    
    def doubleClicked(self, vobj) -> bool:
        """Handle double-click to open properties panel."""
        return self.setEdit(vobj, 0)
    
    def updateData(self, obj, prop: str) -> None:
        """Update visualization when object data changes."""
        if prop in ["CornerNodes", "Thickness", "PressureLoads"]:
            # Trigger visual update
            pass
    
    def getDisplayModes(self, vobj) -> list:
        """Return available display modes."""
        return ["Flat Lines", "Shaded", "Wireframe", "Points"]
    
    def getDefaultDisplayMode(self) -> str:
        """Return default display mode."""
        return "Shaded"
    
    def setDisplayMode(self, mode: str) -> str:
        """Set display mode."""
        return mode