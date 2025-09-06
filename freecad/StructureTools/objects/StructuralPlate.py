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
        
        # Ensure we're starting with a clean object
        self._ensure_property_exists = self._create_property_adder(obj)
        
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
        
        # Visualization properties
        obj.addProperty("App::PropertyBool", "ShowMesh", "Display",
                       "Show finite element mesh")
        obj.ShowMesh = True
        
        obj.addProperty("App::PropertyColor", "MeshColor", "Display",
                       "Color of finite element mesh")
        obj.MeshColor = (0.5, 0.5, 0.5)  # Gray
        
        obj.addProperty("App::PropertyFloat", "MeshLineWidth", "Display",
                       "Line width for mesh display")
        obj.MeshLineWidth = 1.0
        
        obj.addProperty("App::PropertyEnumeration", "DisplayStyle", "Display",
                       "Plate display style")
        obj.DisplayStyle = ["Solid", "Wireframe", "Points"]
        obj.DisplayStyle = "Solid"
        
        # Identification properties
        obj.addProperty("App::PropertyString", "PlateID", "Identification",
                       "Unique plate identifier")
        
        obj.addProperty("App::PropertyString", "Description", "Identification",
                       "Plate description or notes")
        
        # Status properties
        obj.addProperty("App::PropertyBool", "IsValid", "Status",
                       "Whether the plate definition is valid")
        obj.IsValid = True
        
        obj.addProperty("App::PropertyBool", "IsAnalysisReady", "Status",
                       "Whether the plate is ready for analysis")
        obj.IsAnalysisReady = False
    
    def _create_property_adder(self, obj):
        """
        Create a helper function to safely add properties with error handling.
        
        Args:
            obj: The DocumentObject to add properties to
            
        Returns:
            A function that can be used to add properties to the object
        """
        def ensure_property_exists(prop_type, prop_name, prop_group, prop_doc, default=None):
            try:
                if not hasattr(obj, prop_name):
                    obj.addProperty(prop_type, prop_name, prop_group, prop_doc)
                    if default is not None:
                        setattr(obj, prop_name, default)
                return True
            except Exception as e:
                App.Console.PrintWarning(f"Error creating property {prop_name}: {e}\n")
                return False
        return ensure_property_exists
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        # Ensure critical properties exist
        if not hasattr(obj, 'IncludeMembraneAction'):
            self._ensure_property_exists("App::PropertyBool", "IncludeMembraneAction", "Plate",
                       "Include membrane forces in analysis", True)
        
        if not hasattr(obj, 'IncludeBendingAction'):
            self._ensure_property_exists("App::PropertyBool", "IncludeBendingAction", "Plate",
                       "Include bending moments in analysis", True)
        
        if not hasattr(obj, 'IncludeShearDeformation'):
            self._ensure_property_exists("App::PropertyBool", "IncludeShearDeformation", "Plate",
                       "Include transverse shear deformation (thick plate)", False)
        
        # Handle property changes
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
            if hasattr(obj, 'IncludeMembraneAction'):
                obj.IncludeMembraneAction = False
            if hasattr(obj, 'IncludeBendingAction'):
                obj.IncludeBendingAction = True
            if hasattr(obj, 'IncludeShearDeformation'):
                obj.IncludeShearDeformation = False
        elif plate_type == "Thick Plate":
            if hasattr(obj, 'IncludeMembraneAction'):
                obj.IncludeMembraneAction = True
            if hasattr(obj, 'IncludeBendingAction'):
                obj.IncludeBendingAction = True
            if hasattr(obj, 'IncludeShearDeformation'):
                obj.IncludeShearDeformation = True
        elif plate_type == "Shell":
            if hasattr(obj, 'IncludeMembraneAction'):
                obj.IncludeMembraneAction = True
            if hasattr(obj, 'IncludeBendingAction'):
                obj.IncludeBendingAction = True
            if hasattr(obj, 'IncludeShearDeformation'):
                obj.IncludeShearDeformation = False
        elif plate_type == "Membrane":
            if hasattr(obj, 'IncludeMembraneAction'):
                obj.IncludeMembraneAction = True
            if hasattr(obj, 'IncludeBendingAction'):
                obj.IncludeBendingAction = False
            if hasattr(obj, 'IncludeShearDeformation'):
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
        except Exception as e:
            App.Console.PrintWarning(f"Error updating visual representation: {e}\n")
    
    def execute(self, obj) -> None:
        """Update plate when properties change."""
        # Update geometry if needed
        if hasattr(obj, 'CornerNodes') and obj.CornerNodes:
            self._update_geometry(obj)
    
    def getLoadsInThaiUnits(self, obj):
        """Get plate load values in Thai units."""
        if not hasattr(obj, 'UseThaiUnits') or not obj.UseThaiUnits:
            return None
            
        try:
            # Import Thai units converter
            from ..utils.universal_thai_units import UniversalThaiUnits
            converter = UniversalThaiUnits()
            
            # Get load values in SI units
            pressure_loads = obj.PressureLoads if hasattr(obj, 'PressureLoads') else []
            shear_loads_x = obj.ShearLoadsX if hasattr(obj, 'ShearLoadsX') else []
            shear_loads_y = obj.ShearLoadsY if hasattr(obj, 'ShearLoadsY') else []
            
            # Convert to Thai units
            pressure_loads_ksc = [converter.kn_m2_to_ksc_m2(load) for load in pressure_loads]
            pressure_loads_tf_m2 = [converter.kn_m2_to_tf_m2(load) for load in pressure_loads]
            shear_loads_kgf_m = [converter.kn_m_to_kgf_m(load) for load in shear_loads_x + shear_loads_y]
            
            # Update Thai unit properties
            obj.PressureLoadsKsc = pressure_loads_ksc
            obj.PressureLoadsTfM2 = pressure_loads_tf_m2
            obj.ShearLoadsKgfM = shear_loads_kgf_m
            
            thai_results = {
                'pressure_loads_ksc': pressure_loads_ksc,
                'pressure_loads_tf_m2': pressure_loads_tf_m2,
                'shear_loads_kgf_m': shear_loads_kgf_m
            }
            
            return thai_results
            
        except Exception as e:
            App.Console.PrintError(f"Error converting plate loads to Thai units: {e}\n")
            return None
    
    def updateThaiUnits(self, obj):
        """Update Thai units when properties change."""
        if hasattr(obj, 'UseThaiUnits') and obj.UseThaiUnits:
            self.getLoadsInThaiUnits(obj)

class ViewProviderStructuralPlate:
    """
    ViewProvider for StructuralPlate with enhanced visualization.
    """
    
    def __init__(self, vobj):
        """Initialize ViewProvider."""
        vobj.Proxy = self
        self.Object = vobj.Object
    
    def getIcon(self):
        """Return the icon for this object."""
        return ":/icons/Part_Face.svg"
    
    def attach(self, vobj):
        """Setup the scene sub-graph of the view provider."""
        self.Object = vobj.Object
        return
    
    def updateData(self, obj, prop):
        """Update visualization when object data changes."""
        return
    
    def onChanged(self, vobj, prop):
        """Handle view provider property changes."""
        return
    
    def setEdit(self, vobj, mode):
        """Edit the object."""
        return False
    
    def unsetEdit(self, vobj, mode):
        """Finish editing the object."""
        return
    
    def doubleClicked(self, vobj):
        """Handle double-click."""
        return self.setEdit(vobj, 0)
    
    def __getstate__(self):
        """Save the state."""
        return None

    def __setstate__(self, state):
        """Restore the state."""
        return None

def makeStructuralPlate(nodes=None, thickness="200 mm", plate_type="Thin Plate", name="StructuralPlate"):
    """
    Create a new StructuralPlate object.
    
    Args:
        nodes: List of corner nodes
        thickness: Plate thickness
        plate_type: Type of plate element
        name: Object name
        
    Returns:
        Created StructuralPlate object
    """
    doc = App.ActiveDocument
    if not doc:
        App.Console.PrintError("No active document. Please create or open a document first.\n")
        return None
    
    # Create the object
    obj = doc.addObject("App::DocumentObjectGroupPython", name)
    StructuralPlate(obj)
    
    # Create ViewProvider
    if App.GuiUp:
        ViewProviderStructuralPlate(obj.ViewObject)
    
    # Set properties
    if nodes:
        obj.CornerNodes = nodes if isinstance(nodes, list) else [nodes]
    obj.Thickness = thickness
    obj.PlateType = plate_type
    
    # Generate unique ID
    plate_count = len([o for o in doc.Objects if hasattr(o, 'Proxy') and hasattr(o.Proxy, 'Type') and o.Proxy.Type == "StructuralPlate"])
    obj.PlateID = f"PL{plate_count + 1:03d}"
    
    # Recompute to update properties
    obj.recompute()
    doc.recompute()
    
    App.Console.PrintMessage(f"Created StructuralPlate: {obj.Label} with ID: {obj.PlateID}\n")
    return obj
