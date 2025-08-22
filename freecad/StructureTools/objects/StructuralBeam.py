# -*- coding: utf-8 -*-
"""
StructuralBeam - Professional beam/member object with advanced analysis capabilities

This module provides a comprehensive beam object for structural engineering
with section properties, connectivity, load handling, and results visualization.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import DraftVecUtils
from typing import List, Dict, Tuple, Optional, Any
import math
import os


class StructuralBeam:
    """
    Custom Document Object for structural beams with enhanced functionality.
    
    This class provides professional-grade beam objects for structural analysis
    with section properties, member forces, deflections, and design checks.
    """
    
    def __init__(self, obj):
        """
        Initialize StructuralBeam object.
        
        Args:
            obj: FreeCAD DocumentObject to be enhanced
        """
        self.Type = "StructuralBeam"
        obj.Proxy = self
        
        # Geometric properties
        obj.addProperty("App::PropertyVector", "StartPoint", "Geometry", 
                       "Start point of beam in global coordinates")
        obj.StartPoint = App.Vector(0, 0, 0)
        
        obj.addProperty("App::PropertyVector", "EndPoint", "Geometry",
                       "End point of beam in global coordinates")
        obj.EndPoint = App.Vector(1000, 0, 0)  # Default 1m beam
        
        obj.addProperty("App::PropertyLength", "Length", "Geometry",
                       "Beam length (calculated from endpoints)")
        
        obj.addProperty("App::PropertyVector", "LocalXAxis", "Geometry",
                       "Local X-axis direction (along beam)")
        
        obj.addProperty("App::PropertyVector", "LocalYAxis", "Geometry", 
                       "Local Y-axis direction (strong axis)")
        
        obj.addProperty("App::PropertyVector", "LocalZAxis", "Geometry",
                       "Local Z-axis direction (weak axis)")
        
        # Section properties
        obj.addProperty("App::PropertyString", "SectionType", "Section",
                       "Section type (W, C, L, HSS, etc.)")
        obj.SectionType = "W"
        
        obj.addProperty("App::PropertyString", "SectionSize", "Section",
                       "Section size designation (e.g., W12x26)")
        obj.SectionSize = "W12x26"
        
        obj.addProperty("App::PropertyArea", "CrossSectionArea", "Section",
                       "Cross-sectional area A")
        obj.CrossSectionArea = "7740 mm^2"
        
        obj.addProperty("App::PropertyLength", "MomentInertiaY", "Section",
                       "Moment of inertia about strong axis Iy")
        obj.MomentInertiaY = "204000000 mm^4"
        
        obj.addProperty("App::PropertyLength", "MomentInertiaZ", "Section",
                       "Moment of inertia about weak axis Iz")
        obj.MomentInertiaZ = "9200000 mm^4"
        
        obj.addProperty("App::PropertyLength", "TorsionalConstant", "Section",
                       "Torsional constant J")
        obj.TorsionalConstant = "410000 mm^4"
        
        obj.addProperty("App::PropertyLength", "SectionDepth", "Section",
                       "Section depth (height)")
        obj.SectionDepth = "311 mm"
        
        obj.addProperty("App::PropertyLength", "SectionWidth", "Section",
                       "Section width")
        obj.SectionWidth = "165 mm"
        
        obj.addProperty("App::PropertyLength", "WebThickness", "Section",
                       "Web thickness")
        obj.WebThickness = "7.5 mm"
        
        obj.addProperty("App::PropertyLength", "FlangeThickness", "Section",
                       "Flange thickness")
        obj.FlangeThickness = "13.0 mm"
        
        # Material reference
        obj.addProperty("App::PropertyLink", "Material", "Material",
                       "Reference to StructuralMaterial object")
        
        obj.addProperty("App::PropertyPressure", "EffectiveModulus", "Material",
                       "Effective modulus for analysis")
        obj.EffectiveModulus = "200000 MPa"
        
        # Connection properties
        obj.addProperty("App::PropertyLink", "StartNode", "Connectivity",
                       "Start node connection")
        
        obj.addProperty("App::PropertyLink", "EndNode", "Connectivity",
                       "End node connection")
        
        obj.addProperty("App::PropertyEnumeration", "StartCondition", "Connectivity",
                       "End condition at start (Fixed, Pinned, Roller)")
        obj.StartCondition = ["Fixed", "Pinned", "Roller", "Free", "Spring"]
        obj.StartCondition = "Pinned"
        
        obj.addProperty("App::PropertyEnumeration", "EndCondition", "Connectivity",
                       "End condition at end (Fixed, Pinned, Roller)")
        obj.EndCondition = ["Fixed", "Pinned", "Roller", "Free", "Spring"]
        obj.EndCondition = "Pinned"
        
        # Member releases (for moment and shear releases)
        obj.addProperty("App::PropertyBool", "StartMomentReleaseY", "Releases",
                       "Moment release about Y at start")
        obj.addProperty("App::PropertyBool", "StartMomentReleaseZ", "Releases",
                       "Moment release about Z at start") 
        obj.addProperty("App::PropertyBool", "EndMomentReleaseY", "Releases",
                       "Moment release about Y at end")
        obj.addProperty("App::PropertyBool", "EndMomentReleaseZ", "Releases",
                       "Moment release about Z at end")
        
        # Loading properties
        obj.addProperty("App::PropertyFloatList", "DistributedLoadY", "Loads",
                       "Distributed load in local Y direction by load case")
        obj.addProperty("App::PropertyFloatList", "DistributedLoadZ", "Loads",
                       "Distributed load in local Z direction by load case")
        
        obj.addProperty("App::PropertyFloatList", "PointLoads", "Loads",
                       "Point loads along beam by load case")
        obj.addProperty("App::PropertyFloatList", "PointLoadPositions", "Loads",
                       "Positions of point loads (0.0 to 1.0)")
        
        obj.addProperty("App::PropertyFloatList", "AppliedMoments", "Loads",
                       "Applied moments along beam by load case")
        obj.addProperty("App::PropertyFloatList", "MomentPositions", "Loads",
                       "Positions of applied moments (0.0 to 1.0)")
        
        # Analysis results
        obj.addProperty("App::PropertyFloatList", "AxialForces", "Results",
                       "Axial forces by position and load combination")
        obj.addProperty("App::PropertyFloatList", "ShearForcesY", "Results",
                       "Shear forces in Y by position and load combination")
        obj.addProperty("App::PropertyFloatList", "ShearForcesZ", "Results", 
                       "Shear forces in Z by position and load combination")
        
        obj.addProperty("App::PropertyFloatList", "MomentsY", "Results",
                       "Bending moments about Y by position and load combination")
        obj.addProperty("App::PropertyFloatList", "MomentsZ", "Results",
                       "Bending moments about Z by position and load combination")
        obj.addProperty("App::PropertyFloatList", "TorsionalMoments", "Results",
                       "Torsional moments by position and load combination")
        
        obj.addProperty("App::PropertyFloatList", "DisplacementsX", "Results",
                       "Axial displacements by position and load combination")
        obj.addProperty("App::PropertyFloatList", "DisplacementsY", "Results",
                       "Transverse displacements Y by position and load combination")
        obj.addProperty("App::PropertyFloatList", "DisplacementsZ", "Results",
                       "Transverse displacements Z by position and load combination")
        
        obj.addProperty("App::PropertyFloatList", "RotationsY", "Results",
                       "Rotations about Y by position and load combination")
        obj.addProperty("App::PropertyFloatList", "RotationsZ", "Results",
                       "Rotations about Z by position and load combination")
        
        # Design check results
        obj.addProperty("App::PropertyFloatList", "UtilizationRatios", "Design",
                       "Utilization ratios by load combination")
        obj.addProperty("App::PropertyFloatList", "CapacityRatios", "Design",
                       "Capacity ratios by load combination")
        
        obj.addProperty("App::PropertyString", "ControllingCase", "Design",
                       "Controlling load combination")
        obj.addProperty("App::PropertyFloat", "MaxUtilization", "Design",
                       "Maximum utilization ratio")
        
        # Advanced properties
        obj.addProperty("App::PropertyInteger", "AnalysisSegments", "Advanced",
                       "Number of segments for analysis")
        obj.AnalysisSegments = 10
        
        obj.addProperty("App::PropertyBool", "IncludeShearDeformation", "Advanced",
                       "Include shear deformation effects")
        obj.IncludeShearDeformation = False
        
        obj.addProperty("App::PropertyBool", "IncludeGeometricNonlinearity", "Advanced",
                       "Include P-Delta effects")
        obj.IncludeGeometricNonlinearity = False
        
        # Identification and organization
        obj.addProperty("App::PropertyString", "MemberID", "Identification",
                       "Unique member identifier")
        obj.addProperty("App::PropertyString", "MemberType", "Identification",
                       "Member type (Beam, Column, Brace, etc.)")
        obj.MemberType = "Beam"
        
        obj.addProperty("App::PropertyString", "Description", "Identification",
                       "Member description or notes")
        
        # Internal properties
        obj.addProperty("App::PropertyInteger", "InternalID", "Internal",
                       "Internal numbering for analysis")
        obj.addProperty("App::PropertyBool", "IsActive", "Internal",
                       "Member is active in current analysis")
        obj.IsActive = True
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        if prop in ["StartPoint", "EndPoint"]:
            self._update_geometry(obj)
        elif prop == "Material":
            self._update_material_properties(obj)
        elif prop in ["SectionType", "SectionSize"]:
            self._update_section_properties(obj)
        elif prop in ["StartCondition", "EndCondition"]:
            self._update_end_conditions(obj)
    
    def _update_geometry(self, obj) -> None:
        """Update geometric properties when endpoints change."""
        if not (hasattr(obj, 'StartPoint') and hasattr(obj, 'EndPoint')):
            return
        
        # Calculate length and direction
        start = obj.StartPoint
        end = obj.EndPoint
        vector = end.sub(start)
        
        obj.Length = vector.Length
        
        # Update local coordinate system
        if vector.Length > 1e-6:  # Avoid division by zero
            # Local X-axis along beam
            local_x = vector.normalize()
            obj.LocalXAxis = local_x
            
            # Local Z-axis (weak axis) - try to keep vertical when possible
            global_z = App.Vector(0, 0, 1)
            if abs(local_x.dot(global_z)) < 0.9:  # Not nearly vertical
                local_z = local_x.cross(global_z).normalize()
            else:  # Nearly vertical - use different reference
                local_z = local_x.cross(App.Vector(1, 0, 0)).normalize()
            
            obj.LocalZAxis = local_z
            
            # Local Y-axis (strong axis)
            local_y = local_z.cross(local_x)
            obj.LocalYAxis = local_y
        
        # Update visual representation
        self._update_visual_representation(obj)
    
    def _update_material_properties(self, obj) -> None:
        """Update properties when material changes."""
        if not hasattr(obj, 'Material') or not obj.Material:
            return
        
        material = obj.Material
        if hasattr(material, 'ModulusElasticity'):
            try:
                modulus = material.ModulusElasticity.getValueAs('MPa')
                obj.EffectiveModulus = f"{modulus} MPa"
            except:
                pass
    
    def _update_section_properties(self, obj) -> None:
        """Update section properties based on section type and size."""
        if not (hasattr(obj, 'SectionType') and hasattr(obj, 'SectionSize')):
            return
        
        # This would integrate with section database
        # For now, provide sample values based on common sections
        section_type = obj.SectionType
        section_size = obj.SectionSize
        
        # Sample W-section properties (W12x26)
        if section_type == "W" and "12x26" in section_size:
            obj.CrossSectionArea = "7740 mm^2"
            obj.MomentInertiaY = "204000000 mm^4"
            obj.MomentInertiaZ = "9200000 mm^4"
            obj.SectionDepth = "311 mm"
            obj.SectionWidth = "165 mm"
            obj.WebThickness = "7.5 mm"
            obj.FlangeThickness = "13.0 mm"
    
    def _update_end_conditions(self, obj) -> None:
        """Update end releases based on connection conditions."""
        if hasattr(obj, 'StartCondition'):
            if obj.StartCondition == "Pinned":
                obj.StartMomentReleaseY = True
                obj.StartMomentReleaseZ = True
            elif obj.StartCondition == "Fixed":
                obj.StartMomentReleaseY = False
                obj.StartMomentReleaseZ = False
        
        if hasattr(obj, 'EndCondition'):
            if obj.EndCondition == "Pinned":
                obj.EndMomentReleaseY = True
                obj.EndMomentReleaseZ = True
            elif obj.EndCondition == "Fixed":
                obj.EndMomentReleaseY = False
                obj.EndMomentReleaseZ = False
    
    def _update_visual_representation(self, obj) -> None:
        """Update the 3D visual representation of the beam."""
        if not (hasattr(obj, 'StartPoint') and hasattr(obj, 'EndPoint')):
            return
        
        start = obj.StartPoint
        end = obj.EndPoint
        
        if start.distanceToPoint(end) < 1e-6:
            return
        
        # Create beam centerline
        line = Part.makeLine(start, end)
        
        # Create section representation (simplified as rectangle)
        if hasattr(obj, 'SectionDepth') and hasattr(obj, 'SectionWidth'):
            try:
                depth = obj.SectionDepth.getValueAs('mm')
                width = obj.SectionWidth.getValueAs('mm')
                
                # Create rectangular cross-section at start
                section_points = [
                    App.Vector(-width/2, -depth/2, 0),
                    App.Vector(width/2, -depth/2, 0),
                    App.Vector(width/2, depth/2, 0),
                    App.Vector(-width/2, depth/2, 0),
                    App.Vector(-width/2, -depth/2, 0)
                ]
                
                section_wire = Part.makePolygon(section_points)
                section_face = Part.Face(section_wire)
                
                # Create beam as sweep
                beam_vector = end.sub(start)
                beam_solid = section_face.extrude(beam_vector)
                
                # Position at start point
                beam_solid.translate(start)
                
                # Align with beam orientation
                if hasattr(obj, 'LocalYAxis') and hasattr(obj, 'LocalZAxis'):
                    # This would require proper rotation matrix implementation
                    pass
                
                obj.Shape = beam_solid
                
            except:
                # Fallback to line representation
                obj.Shape = line
        else:
            obj.Shape = line
    
    def execute(self, obj) -> None:
        """
        Update beam geometry and validate properties.
        
        Args:
            obj: The DocumentObject being executed
        """
        # Update geometry
        self._update_geometry(obj)
        
        # Validate section properties
        self._validate_section_properties(obj)
        
        # Update material integration
        self._update_material_properties(obj)
        
        # Validate load consistency
        self._validate_load_consistency(obj)
    
    def _validate_section_properties(self, obj) -> None:
        """Validate section property relationships."""
        try:
            if hasattr(obj, 'CrossSectionArea') and hasattr(obj, 'SectionDepth') and hasattr(obj, 'SectionWidth'):
                area_calc = obj.SectionDepth.getValueAs('mm') * obj.SectionWidth.getValueAs('mm')
                area_prop = obj.CrossSectionArea.getValueAs('mm^2')
                
                # Check if calculated area is reasonable compared to property
                if abs(area_calc - area_prop) / area_prop > 0.5:  # 50% difference
                    App.Console.PrintWarning(
                        f"Section area mismatch: calculated {area_calc:.0f} mm², "
                        f"property {area_prop:.0f} mm²\n"
                    )
        except:
            pass
    
    def _validate_load_consistency(self, obj) -> None:
        """Validate load arrays have consistent lengths."""
        load_properties = [
            'DistributedLoadY', 'DistributedLoadZ', 'PointLoads', 'AppliedMoments'
        ]
        
        lengths = []
        for prop in load_properties:
            if hasattr(obj, prop):
                lengths.append(len(getattr(obj, prop, [])))
        
        if lengths and len(set(lengths)) > 1:
            App.Console.PrintWarning(
                f"Beam {obj.Label}: Inconsistent load case count across load types\n"
            )
    
    def get_stiffness_matrix(self, obj) -> List[List[float]]:
        """
        Calculate local stiffness matrix for the beam.
        
        Args:
            obj: The DocumentObject
            
        Returns:
            12x12 stiffness matrix in local coordinates
        """
        if not hasattr(obj, 'Length') or obj.Length <= 0:
            return [[0.0] * 12 for _ in range(12)]
        
        try:
            # Material and section properties
            E = obj.EffectiveModulus.getValueAs('MPa') if hasattr(obj, 'EffectiveModulus') else 200000
            A = obj.CrossSectionArea.getValueAs('mm^2') if hasattr(obj, 'CrossSectionArea') else 1000
            Iy = obj.MomentInertiaY.getValueAs('mm^4') if hasattr(obj, 'MomentInertiaY') else 1e6
            Iz = obj.MomentInertiaZ.getValueAs('mm^4') if hasattr(obj, 'MomentInertiaZ') else 1e6
            J = obj.TorsionalConstant.getValueAs('mm^4') if hasattr(obj, 'TorsionalConstant') else 1e6
            L = obj.Length.getValueAs('mm')
            
            # Shear modulus (approximate)
            G = E / 2.6  # Typical for steel
            
            # Initialize 12x12 matrix
            k = [[0.0] * 12 for _ in range(12)]
            
            # Axial stiffness
            k[0][0] = k[6][6] = E * A / L
            k[0][6] = k[6][0] = -E * A / L
            
            # Bending stiffness (Y-direction)
            k[1][1] = k[7][7] = 12 * E * Iz / (L**3)
            k[1][5] = k[5][1] = k[7][11] = k[11][7] = 6 * E * Iz / (L**2)
            k[1][7] = k[7][1] = -12 * E * Iz / (L**3)
            k[1][11] = k[11][1] = k[5][7] = k[7][5] = -6 * E * Iz / (L**2)
            k[5][5] = k[11][11] = 4 * E * Iz / L
            k[5][11] = k[11][5] = 2 * E * Iz / L
            
            # Bending stiffness (Z-direction)
            k[2][2] = k[8][8] = 12 * E * Iy / (L**3)
            k[2][4] = k[4][2] = k[8][10] = k[10][8] = -6 * E * Iy / (L**2)
            k[2][8] = k[8][2] = -12 * E * Iy / (L**3)
            k[2][10] = k[10][2] = k[4][8] = k[8][4] = 6 * E * Iy / (L**2)
            k[4][4] = k[10][10] = 4 * E * Iy / L
            k[4][10] = k[10][4] = 2 * E * Iy / L
            
            # Torsional stiffness
            k[3][3] = k[9][9] = G * J / L
            k[3][9] = k[9][3] = -G * J / L
            
            return k
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating stiffness matrix: {e}\n")
            return [[0.0] * 12 for _ in range(12)]
    
    def get_load_vector(self, obj, load_case: int = 0) -> List[float]:
        """
        Get equivalent nodal load vector for distributed loads.
        
        Args:
            obj: The DocumentObject
            load_case: Load case index
            
        Returns:
            12-element load vector in local coordinates
        """
        loads = [0.0] * 12
        
        if not hasattr(obj, 'Length') or obj.Length <= 0:
            return loads
        
        try:
            L = obj.Length.getValueAs('mm')
            
            # Distributed loads
            if hasattr(obj, 'DistributedLoadY') and len(obj.DistributedLoadY) > load_case:
                wy = obj.DistributedLoadY[load_case]
                # Convert to equivalent nodal loads
                loads[1] = loads[7] = wy * L / 2  # Shear forces
                loads[5] = wy * L**2 / 12  # Moment at start
                loads[11] = -wy * L**2 / 12  # Moment at end
            
            if hasattr(obj, 'DistributedLoadZ') and len(obj.DistributedLoadZ) > load_case:
                wz = obj.DistributedLoadZ[load_case]
                loads[2] = loads[8] = wz * L / 2  # Shear forces
                loads[4] = -wz * L**2 / 12  # Moment at start
                loads[10] = wz * L**2 / 12  # Moment at end
            
            # Point loads would be handled separately in analysis
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating load vector: {e}\n")
        
        return loads


class ViewProviderStructuralBeam:
    """
    ViewProvider for StructuralBeam with enhanced visualization and editing.
    """
    
    def __init__(self, vobj):
        """Initialize ViewProvider."""
        vobj.Proxy = self
        self.Object = vobj.Object
        
        # Visualization properties
        vobj.addProperty("App::PropertyBool", "ShowSectionOutline", "Display",
                        "Show section outline at beam ends")
        vobj.ShowSectionOutline = True
        
        vobj.addProperty("App::PropertyBool", "ShowLocalAxes", "Display",
                        "Show local coordinate system")
        vobj.ShowLocalAxes = False
        
        vobj.addProperty("App::PropertyBool", "ShowLoads", "Display", 
                        "Show applied loads")
        vobj.ShowLoads = True
        
        vobj.addProperty("App::PropertyEnumeration", "ResultsDisplay", "Results",
                        "Type of results to display")
        vobj.ResultsDisplay = ["None", "Moments", "Shear", "Deflection", "Utilization"]
        vobj.ResultsDisplay = "None"
        
        vobj.addProperty("App::PropertyFloat", "LoadScale", "Display",
                        "Load arrow scale factor")
        vobj.LoadScale = 1.0
        
        vobj.addProperty("App::PropertyColor", "BeamColor", "Display",
                        "Beam color")
        vobj.BeamColor = (0.7, 0.7, 0.7)  # Gray
        
        vobj.addProperty("App::PropertyColor", "LoadColor", "Display", 
                        "Load arrow color")
        vobj.LoadColor = (1.0, 0.0, 0.0)  # Red
    
    def getIcon(self) -> str:
        """
        Return icon based on beam type and status.
        
        Returns:
            Path to appropriate icon file
        """
        if not hasattr(self.Object, 'MemberType'):
            return self._get_icon_path("beam_generic.svg")
        
        member_type = getattr(self.Object, 'MemberType', 'Beam').lower()
        
        # Check for design status
        has_results = (hasattr(self.Object, 'MaxUtilization') and 
                      self.Object.MaxUtilization > 0)
        
        if has_results:
            utilization = getattr(self.Object, 'MaxUtilization', 0)
            if utilization > 1.0:
                return self._get_icon_path(f"{member_type}_overstressed.svg")
            elif utilization > 0.8:
                return self._get_icon_path(f"{member_type}_warning.svg")
            else:
                return self._get_icon_path(f"{member_type}_ok.svg")
        else:
            return self._get_icon_path(f"{member_type}_generic.svg")
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icon_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")
        return os.path.join(icon_dir, icon_name)
    
    def setEdit(self, vobj, mode: int) -> bool:
        """
        Open custom task panel for beam editing.
        
        Args:
            vobj: ViewObject being edited
            mode: Edit mode
            
        Returns:
            True if edit mode started successfully
        """
        if mode == 0:
            from ..taskpanels.BeamPropertiesPanel import BeamPropertiesPanel
            self.panel = BeamPropertiesPanel(vobj.Object)
            Gui.Control.showDialog(self.panel)
            return True
        return False
    
    def unsetEdit(self, vobj, mode: int) -> bool:
        """Close beam editing panel."""
        Gui.Control.closeDialog()
        return True
    
    def doubleClicked(self, vobj) -> bool:
        """Handle double-click to open properties panel."""
        return self.setEdit(vobj, 0)
    
    def updateData(self, obj, prop: str) -> None:
        """Update visualization when object data changes."""
        if prop in ["StartPoint", "EndPoint", "SectionDepth", "SectionWidth"]:
            # Trigger visual update
            pass
    
    def getDisplayModes(self, vobj) -> list:
        """Return available display modes."""
        return ["Standard", "Wireframe", "Section"]
    
    def getDefaultDisplayMode(self) -> str:
        """Return default display mode."""
        return "Standard"
    
    def setDisplayMode(self, mode: str) -> str:
        """Set display mode."""
        return mode