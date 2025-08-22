import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Any
import os


class StructuralColumn:
    """
    Professional structural column object with advanced analysis capabilities.
    
    This class provides specialized column functionality including buckling analysis,
    P-M interaction, biaxial bending, and design code checking.
    """
    
    def __init__(self, obj):
        """
        Initialize StructuralColumn object.
        
        Args:
            obj: FreeCAD DocumentObject to be enhanced
        """
        self.Type = "StructuralColumn"
        obj.Proxy = self
        
        # Geometric properties
        obj.addProperty("App::PropertyVector", "BasePoint", "Geometry",
                       "Base point of column (bottom)")
        obj.BasePoint = App.Vector(0, 0, 0)
        
        obj.addProperty("App::PropertyVector", "TopPoint", "Geometry",
                       "Top point of column")
        obj.TopPoint = App.Vector(0, 0, 3000)  # Default 3m column
        
        obj.addProperty("App::PropertyLength", "Height", "Geometry",
                       "Column height (calculated)")
        
        obj.addProperty("App::PropertyAngle", "Inclination", "Geometry",
                       "Column inclination from vertical")
        obj.Inclination = "0 deg"
        
        obj.addProperty("App::PropertyVector", "LocalXAxis", "Geometry",
                       "Local X-axis direction (strong axis)")
        
        obj.addProperty("App::PropertyVector", "LocalYAxis", "Geometry",
                       "Local Y-axis direction (weak axis)")
        
        obj.addProperty("App::PropertyVector", "LocalZAxis", "Geometry",
                       "Local Z-axis direction (column axis)")
        
        # Section properties
        obj.addProperty("App::PropertyLink", "Section", "Section",
                       "Reference to section object")
        
        obj.addProperty("App::PropertyString", "SectionType", "Section",
                       "Section type (W, HSS, Pipe, etc.)")
        obj.SectionType = "W"
        
        obj.addProperty("App::PropertyString", "SectionDesignation", "Section",
                       "Section designation (e.g., W14x90)")
        obj.SectionDesignation = "W14x90"
        
        # Column-specific section properties
        obj.addProperty("App::PropertyArea", "GrossArea", "Section",
                       "Gross cross-sectional area Ag")
        
        obj.addProperty("App::PropertyLength", "RadiusOfGyrationX", "Section",
                       "Radius of gyration about X-axis rx")
        
        obj.addProperty("App::PropertyLength", "RadiusOfGyrationY", "Section",
                       "Radius of gyration about Y-axis ry")
        
        obj.addProperty("App::PropertyLength", "RadiusOfGyrationZ", "Section",
                       "Polar radius of gyration rz")
        
        obj.addProperty("App::PropertyFloat", "ShapeFactorX", "Section",
                       "Shape factor for X-axis")
        obj.ShapeFactorX = 1.12
        
        obj.addProperty("App::PropertyFloat", "ShapeFactorY", "Section",
                       "Shape factor for Y-axis")
        obj.ShapeFactorY = 1.12
        
        # Material properties
        obj.addProperty("App::PropertyLink", "Material", "Material",
                       "Reference to StructuralMaterial object")
        
        # Column-specific design properties
        obj.addProperty("App::PropertyEnumeration", "ColumnType", "Design",
                       "Column behavior type")
        obj.ColumnType = ["Compression", "Beam-Column", "Tension", "Combined"]
        obj.ColumnType = "Compression"
        
        obj.addProperty("App::PropertyFloat", "EffectiveLengthFactorX", "Design",
                       "Effective length factor for X-axis buckling Kx")
        obj.EffectiveLengthFactorX = 1.0
        
        obj.addProperty("App::PropertyFloat", "EffectiveLengthFactorY", "Design",
                       "Effective length factor for Y-axis buckling Ky")
        obj.EffectiveLengthFactorY = 1.0
        
        obj.addProperty("App::PropertyFloat", "EffectiveLengthFactorZ", "Design",
                       "Effective length factor for torsional buckling Kz")
        obj.EffectiveLengthFactorZ = 1.0
        
        obj.addProperty("App::PropertyLength", "UnbracedLengthX", "Design",
                       "Unbraced length for X-axis buckling Lx")
        
        obj.addProperty("App::PropertyLength", "UnbracedLengthY", "Design",
                       "Unbraced length for Y-axis buckling Ly")
        
        obj.addProperty("App::PropertyLength", "UnbracedLengthZ", "Design",
                       "Unbraced length for torsional buckling Lt")
        
        # End conditions and restraints
        obj.addProperty("App::PropertyEnumeration", "BaseConnection", "Connections",
                       "Base connection type")
        obj.BaseConnection = ["Fixed", "Pinned", "Semi-Rigid", "Free"]
        obj.BaseConnection = "Fixed"
        
        obj.addProperty("App::PropertyEnumeration", "TopConnection", "Connections",
                       "Top connection type")
        obj.TopConnection = ["Fixed", "Pinned", "Semi-Rigid", "Free"]
        obj.TopConnection = "Pinned"
        
        obj.addProperty("App::PropertyFloatList", "IntermediateRestraints", "Connections",
                       "Intermediate restraint locations (ratios from base)")
        
        obj.addProperty("App::PropertyFloat", "BaseRotationalStiffness", "Connections",
                       "Base rotational stiffness (kN⋅m/rad)")
        obj.BaseRotationalStiffness = 0.0
        
        obj.addProperty("App::PropertyFloat", "TopRotationalStiffness", "Connections",
                       "Top rotational stiffness (kN⋅m/rad)")
        obj.TopRotationalStiffness = 0.0
        
        # Loading properties
        obj.addProperty("App::PropertyFloatList", "AxialLoads", "Loading",
                       "Applied axial loads by load case (compression +ve)")
        
        obj.addProperty("App::PropertyFloatList", "MomentsX", "Loading",
                       "Applied moments about X-axis by load case")
        
        obj.addProperty("App::PropertyFloatList", "MomentsY", "Loading",
                       "Applied moments about Y-axis by load case")
        
        obj.addProperty("App::PropertyFloatList", "TorsionalMoments", "Loading",
                       "Applied torsional moments by load case")
        
        obj.addProperty("App::PropertyFloatList", "LateralLoadsX", "Loading",
                       "Lateral loads in X direction by load case")
        
        obj.addProperty("App::PropertyFloatList", "LateralLoadsY", "Loading",
                       "Lateral loads in Y direction by load case")
        
        # Column stability analysis
        obj.addProperty("App::PropertyFloat", "ElasticBucklingLoadX", "Stability",
                       "Elastic buckling load for X-axis Pe,x")
        
        obj.addProperty("App::PropertyFloat", "ElasticBucklingLoadY", "Stability",
                       "Elastic buckling load for Y-axis Pe,y")
        
        obj.addProperty("App::PropertyFloat", "ElasticBucklingLoadZ", "Stability",
                       "Elastic torsional buckling load Pe,z")
        
        obj.addProperty("App::PropertyFloat", "CriticalBucklingLoad", "Stability",
                       "Critical buckling load (minimum of Pe,x, Pe,y, Pe,z)")
        
        obj.addProperty("App::PropertyFloat", "SlendernessRatioX", "Stability",
                       "Slenderness ratio for X-axis (KL/r)x")
        
        obj.addProperty("App::PropertyFloat", "SlendernessRatioY", "Stability",
                       "Slenderness ratio for Y-axis (KL/r)y")
        
        obj.addProperty("App::PropertyFloat", "SlendernessRatioZ", "Stability",
                       "Slenderness ratio for torsion (KL/r)z")
        
        # Design capacities (AISC 360)
        obj.addProperty("App::PropertyFloat", "NominalCompressiveStrength", "Capacity",
                       "Nominal compressive strength Pn")
        
        obj.addProperty("App::PropertyFloat", "DesignCompressiveStrength", "Capacity",
                       "Design compressive strength φPn")
        
        obj.addProperty("App::PropertyFloat", "NominalFlexuralStrengthX", "Capacity",
                       "Nominal flexural strength about X-axis Mnx")
        
        obj.addProperty("App::PropertyFloat", "NominalFlexuralStrengthY", "Capacity",
                       "Nominal flexural strength about Y-axis Mny")
        
        obj.addProperty("App::PropertyFloat", "DesignFlexuralStrengthX", "Capacity",
                       "Design flexural strength about X-axis φMnx")
        
        obj.addProperty("App::PropertyFloat", "DesignFlexuralStrengthY", "Capacity",
                       "Design flexural strength about Y-axis φMny")
        
        # Interaction equations
        obj.addProperty("App::PropertyFloatList", "PMInteractionRatios", "Interaction",
                       "P-M interaction ratios by load combination")
        
        obj.addProperty("App::PropertyFloatList", "BiaxialInteractionRatios", "Interaction",
                       "Biaxial bending interaction ratios")
        
        obj.addProperty("App::PropertyString", "ControllingCombination", "Interaction",
                       "Controlling load combination")
        
        obj.addProperty("App::PropertyFloat", "MaxInteractionRatio", "Interaction",
                       "Maximum interaction ratio")
        
        # Design parameters
        obj.addProperty("App::PropertyEnumeration", "DesignCode", "Code",
                       "Design code for checking")
        obj.DesignCode = ["AISC 360-16", "AISC 360-10", "Eurocode 3", "AS 4100", "CSA S16"]
        obj.DesignCode = "AISC 360-16"
        
        obj.addProperty("App::PropertyFloat", "SafetyFactor", "Code",
                       "Safety factor for design")
        obj.SafetyFactor = 2.0
        
        obj.addProperty("App::PropertyBool", "CheckBuckling", "Code",
                       "Include buckling check in design")
        obj.CheckBuckling = True
        
        obj.addProperty("App::PropertyBool", "CheckDeflection", "Code",
                       "Include deflection check")
        obj.CheckDeflection = True
        
        obj.addProperty("App::PropertyFloat", "DeflectionLimit", "Code",
                       "Deflection limit (L/ratio)")
        obj.DeflectionLimit = 300.0  # L/300
        
        # Analysis results
        obj.addProperty("App::PropertyFloatList", "AxialForces", "Results",
                       "Axial forces by load combination")
        
        obj.addProperty("App::PropertyFloatList", "ShearForcesX", "Results",
                       "Shear forces in X direction")
        
        obj.addProperty("App::PropertyFloatList", "ShearForcesY", "Results",
                       "Shear forces in Y direction")
        
        obj.addProperty("App::PropertyFloatList", "BendingMomentsX", "Results",
                       "Bending moments about X-axis")
        
        obj.addProperty("App::PropertyFloatList", "BendingMomentsY", "Results",
                       "Bending moments about Y-axis")
        
        obj.addProperty("App::PropertyFloatList", "TorsionalMomentsResult", "Results",
                       "Torsional moments")
        
        obj.addProperty("App::PropertyFloatList", "DeflectionsX", "Results",
                       "Lateral deflections in X direction")
        
        obj.addProperty("App::PropertyFloatList", "DeflectionsY", "Results",
                       "Lateral deflections in Y direction")
        
        obj.addProperty("App::PropertyFloatList", "AxialDeformations", "Results",
                       "Axial deformations")
        
        # Status and identification
        obj.addProperty("App::PropertyString", "ColumnID", "Identification",
                       "Unique column identifier")
        
        obj.addProperty("App::PropertyString", "GridLocation", "Identification",
                       "Grid location (e.g., A1, B3)")
        
        obj.addProperty("App::PropertyString", "ColumnGroup", "Identification",
                       "Column group for similar members")
        
        obj.addProperty("App::PropertyString", "Description", "Identification",
                       "Column description or notes")
        
        obj.addProperty("App::PropertyBool", "IsActive", "Status",
                       "Column is active in analysis")
        obj.IsActive = True
        
        obj.addProperty("App::PropertyBool", "DesignPassed", "Status",
                       "Column passes design checks")
        obj.DesignPassed = False
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        if prop in ["BasePoint", "TopPoint"]:
            self._update_geometry(obj)
        elif prop == "Material":
            self._update_material_properties(obj)
        elif prop == "Section":
            self._update_section_properties(obj)
        elif prop in ["EffectiveLengthFactorX", "EffectiveLengthFactorY", "EffectiveLengthFactorZ"]:
            self._update_buckling_properties(obj)
        elif prop in ["AxialLoads", "MomentsX", "MomentsY"]:
            self._update_design_checks(obj)
    
    def _update_geometry(self, obj) -> None:
        """Update geometric properties when endpoints change."""
        if not (hasattr(obj, 'BasePoint') and hasattr(obj, 'TopPoint')):
            return
        
        try:
            # Calculate height
            base = obj.BasePoint
            top = obj.TopPoint
            height_vector = top - base
            height = height_vector.Length
            obj.Height = f"{height} mm"
            
            # Calculate inclination
            vertical = App.Vector(0, 0, 1)
            inclination = math.degrees(height_vector.getAngle(vertical))
            obj.Inclination = f"{inclination} deg"
            
            # Calculate local coordinate system
            self._calculate_local_coordinates(obj, height_vector)
            
            # Update visual representation
            self._update_visual_representation(obj)
            
            # Update unbraced lengths if not set
            if not hasattr(obj, 'UnbracedLengthX') or obj.UnbracedLengthX == 0:
                obj.UnbracedLengthX = obj.Height
            if not hasattr(obj, 'UnbracedLengthY') or obj.UnbracedLengthY == 0:
                obj.UnbracedLengthY = obj.Height
            if not hasattr(obj, 'UnbracedLengthZ') or obj.UnbracedLengthZ == 0:
                obj.UnbracedLengthZ = obj.Height
                
        except Exception as e:
            App.Console.PrintWarning(f"Error updating column geometry: {e}\n")
    
    def _calculate_local_coordinates(self, obj, height_vector: App.Vector) -> None:
        """Calculate local coordinate system for the column."""
        try:
            # Local Z-axis is along column height
            local_z = height_vector.normalize()
            obj.LocalZAxis = local_z
            
            # Local X-axis (strong axis) - perpendicular to Z in XY plane
            if abs(local_z.z) < 0.999:  # Not vertical
                local_x = App.Vector(local_z.y, -local_z.x, 0).normalize()
            else:  # Vertical column
                local_x = App.Vector(1, 0, 0)
            obj.LocalXAxis = local_x
            
            # Local Y-axis (weak axis) - perpendicular to both X and Z
            local_y = local_z.cross(local_x)
            obj.LocalYAxis = local_y
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating local coordinates: {e}\n")
    
    def _update_material_properties(self, obj) -> None:
        """Update properties when material changes."""
        if not (hasattr(obj, 'Material') and obj.Material):
            return
        
        try:
            material = obj.Material
            
            # Update buckling calculations when material changes
            self._update_buckling_properties(obj)
            self._update_design_checks(obj)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating material properties: {e}\n")
    
    def _update_section_properties(self, obj) -> None:
        """Update section properties when section changes."""
        if not (hasattr(obj, 'Section') and obj.Section):
            return
        
        try:
            section = obj.Section
            
            # Copy section properties to column
            if hasattr(section, 'Area'):
                obj.GrossArea = section.Area
            if hasattr(section, 'RadiusOfGyrationX'):
                obj.RadiusOfGyrationX = section.RadiusOfGyrationX
            if hasattr(section, 'RadiusOfGyrationY'):
                obj.RadiusOfGyrationY = section.RadiusOfGyrationY
            
            # Update buckling and design calculations
            self._update_buckling_properties(obj)
            self._update_design_checks(obj)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating section properties: {e}\n")
    
    def _update_buckling_properties(self, obj) -> None:
        """Update buckling analysis properties."""
        if not self._has_required_properties_for_buckling(obj):
            return
        
        try:
            # Get material and geometric properties
            E = self._get_elastic_modulus(obj)
            if E <= 0:
                return
            
            height = obj.Height.getValueAs('mm')
            rx = obj.RadiusOfGyrationX.getValueAs('mm') if hasattr(obj, 'RadiusOfGyrationX') else 50.0
            ry = obj.RadiusOfGyrationY.getValueAs('mm') if hasattr(obj, 'RadiusOfGyrationY') else 50.0
            
            Kx = obj.EffectiveLengthFactorX
            Ky = obj.EffectiveLengthFactorY
            Kz = obj.EffectiveLengthFactorZ
            
            # Calculate slenderness ratios
            obj.SlendernessRatioX = (Kx * height) / rx if rx > 0 else 0
            obj.SlendernessRatioY = (Ky * height) / ry if ry > 0 else 0
            obj.SlendernessRatioZ = (Kz * height) / min(rx, ry) if min(rx, ry) > 0 else 0
            
            # Calculate elastic buckling loads (Euler buckling)
            I_x = rx * rx * obj.GrossArea.getValueAs('mm^2') if hasattr(obj, 'GrossArea') else 1000000
            I_y = ry * ry * obj.GrossArea.getValueAs('mm^2') if hasattr(obj, 'GrossArea') else 1000000
            
            # Pe = π²EI/(KL)²
            obj.ElasticBucklingLoadX = (math.pi**2 * E * I_x) / ((Kx * height)**2) / 1000  # Convert to kN
            obj.ElasticBucklingLoadY = (math.pi**2 * E * I_y) / ((Ky * height)**2) / 1000  # Convert to kN
            
            # Torsional buckling (simplified)
            J = 1000000  # Placeholder torsional constant
            obj.ElasticBucklingLoadZ = (math.pi**2 * E * J) / ((Kz * height)**2) / 1000
            
            # Critical buckling load is minimum
            obj.CriticalBucklingLoad = min(obj.ElasticBucklingLoadX, 
                                         obj.ElasticBucklingLoadY, 
                                         obj.ElasticBucklingLoadZ)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating buckling properties: {e}\n")
    
    def _update_design_checks(self, obj) -> None:
        """Update design capacity and interaction checks."""
        if not self._has_required_properties_for_design(obj):
            return
        
        try:
            # Calculate nominal compressive strength (AISC 360)
            self._calculate_compressive_strength(obj)
            
            # Calculate flexural strengths
            self._calculate_flexural_strengths(obj)
            
            # Calculate interaction ratios
            self._calculate_interaction_ratios(obj)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating design checks: {e}\n")
    
    def _calculate_compressive_strength(self, obj) -> None:
        """Calculate nominal compressive strength per AISC 360."""
        try:
            # Get material properties
            Fy = self._get_yield_strength(obj)
            E = self._get_elastic_modulus(obj)
            
            if Fy <= 0 or E <= 0:
                return
            
            # Get section properties
            Ag = obj.GrossArea.getValueAs('mm^2') if hasattr(obj, 'GrossArea') else 0
            if Ag <= 0:
                return
            
            # Calculate effective slenderness ratios
            KL_r_x = obj.SlendernessRatioX if hasattr(obj, 'SlendernessRatioX') else 50
            KL_r_y = obj.SlendernessRatioY if hasattr(obj, 'SlendernessRatioY') else 50
            KL_r = max(KL_r_x, KL_r_y)  # Governing slenderness ratio
            
            # Calculate elastic buckling stress
            Fe = (math.pi**2 * E) / (KL_r**2) if KL_r > 0 else E
            
            # Calculate critical stress based on AISC 360
            lambda_c = math.sqrt(Fy / Fe)
            
            if lambda_c <= 1.5:
                # Inelastic buckling
                Fcr = (0.658**(lambda_c**2)) * Fy
            else:
                # Elastic buckling
                Fcr = 0.877 * Fe
            
            # Nominal compressive strength
            obj.NominalCompressiveStrength = Fcr * Ag / 1000  # Convert to kN
            
            # Design compressive strength (φ = 0.90 for compression)
            obj.DesignCompressiveStrength = 0.90 * obj.NominalCompressiveStrength
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating compressive strength: {e}\n")
    
    def _calculate_flexural_strengths(self, obj) -> None:
        """Calculate nominal flexural strengths."""
        try:
            # This is simplified - actual implementation would consider
            # lateral-torsional buckling, local buckling, etc.
            
            Fy = self._get_yield_strength(obj)
            if Fy <= 0:
                return
            
            # Placeholder section moduli (would come from section object)
            Sx = 1000000  # mm³
            Sy = 500000   # mm³
            
            # Nominal flexural strengths (simplified)
            obj.NominalFlexuralStrengthX = Fy * Sx / 1000000  # Convert to kN⋅m
            obj.NominalFlexuralStrengthY = Fy * Sy / 1000000  # Convert to kN⋅m
            
            # Design flexural strengths (φ = 0.90 for flexure)
            obj.DesignFlexuralStrengthX = 0.90 * obj.NominalFlexuralStrengthX
            obj.DesignFlexuralStrengthY = 0.90 * obj.NominalFlexuralStrengthY
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating flexural strengths: {e}\n")
    
    def _calculate_interaction_ratios(self, obj) -> None:
        """Calculate P-M interaction ratios for all load combinations."""
        if not (hasattr(obj, 'AxialLoads') and hasattr(obj, 'MomentsX') and hasattr(obj, 'MomentsY')):
            return
        
        try:
            interaction_ratios = []
            max_ratio = 0.0
            controlling_combo = ""
            
            # Get design capacities
            Pc = obj.DesignCompressiveStrength if hasattr(obj, 'DesignCompressiveStrength') else 1000
            Mcx = obj.DesignFlexuralStrengthX if hasattr(obj, 'DesignFlexuralStrengthX') else 100
            Mcy = obj.DesignFlexuralStrengthY if hasattr(obj, 'DesignFlexuralStrengthY') else 100
            
            if Pc <= 0 or Mcx <= 0 or Mcy <= 0:
                return
            
            # Calculate interaction for each load combination
            num_combos = max(len(obj.AxialLoads), len(obj.MomentsX), len(obj.MomentsY))
            
            for i in range(num_combos):
                P = obj.AxialLoads[i] if i < len(obj.AxialLoads) else 0
                Mx = obj.MomentsX[i] if i < len(obj.MomentsX) else 0
                My = obj.MomentsY[i] if i < len(obj.MomentsY) else 0
                
                # AISC 360 interaction equations
                if P / Pc >= 0.2:
                    # High axial load case
                    ratio = (P / Pc) + (8.0/9.0) * ((Mx / Mcx) + (My / Mcy))
                else:
                    # Low axial load case
                    ratio = (P / (2.0 * Pc)) + ((Mx / Mcx) + (My / Mcy))
                
                interaction_ratios.append(ratio)
                
                if ratio > max_ratio:
                    max_ratio = ratio
                    controlling_combo = f"LC{i+1}"
            
            obj.PMInteractionRatios = interaction_ratios
            obj.MaxInteractionRatio = max_ratio
            obj.ControllingCombination = controlling_combo
            obj.DesignPassed = (max_ratio <= 1.0)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating interaction ratios: {e}\n")
    
    def _has_required_properties_for_buckling(self, obj) -> bool:
        """Check if required properties are available for buckling analysis."""
        return (hasattr(obj, 'Height') and hasattr(obj, 'Material') and 
                hasattr(obj, 'EffectiveLengthFactorX') and hasattr(obj, 'EffectiveLengthFactorY'))
    
    def _has_required_properties_for_design(self, obj) -> bool:
        """Check if required properties are available for design checks."""
        return (hasattr(obj, 'Material') and hasattr(obj, 'GrossArea') and
                hasattr(obj, 'NominalCompressiveStrength'))
    
    def _get_elastic_modulus(self, obj) -> float:
        """Get elastic modulus from material."""
        if hasattr(obj, 'Material') and obj.Material:
            if hasattr(obj.Material, 'ModulusElasticity'):
                return obj.Material.ModulusElasticity.getValueAs('MPa')
        return 200000.0  # Default steel E = 200 GPa
    
    def _get_yield_strength(self, obj) -> float:
        """Get yield strength from material."""
        if hasattr(obj, 'Material') and obj.Material:
            if hasattr(obj.Material, 'YieldStrength'):
                return obj.Material.YieldStrength.getValueAs('MPa')
        return 345.0  # Default steel Fy = 345 MPa (50 ksi)
    
    def _update_visual_representation(self, obj) -> None:
        """Update 3D visual representation of the column."""
        try:
            if not (hasattr(obj, 'BasePoint') and hasattr(obj, 'TopPoint')):
                return
            
            # Create column centerline
            base = obj.BasePoint
            top = obj.TopPoint
            centerline = Part.makeLine(base, top)
            
            # Create column solid if section is available
            if hasattr(obj, 'Section') and obj.Section:
                # Get section shape and extrude along column length
                # This would be implemented based on section type
                column_solid = self._create_column_solid(obj, centerline)
                if column_solid:
                    obj.Shape = column_solid
                    return
            
            # Fallback: show centerline
            obj.Shape = centerline
            
        except Exception as e:
            App.Console.PrintWarning(f"Error updating column visualization: {e}\n")
    
    def _create_column_solid(self, obj, centerline) -> Optional[Part.Shape]:
        """Create 3D column solid based on section."""
        try:
            # Placeholder implementation
            # Real implementation would use section geometry
            
            # Create a simple rectangular section for visualization
            width = 200  # mm
            depth = 200  # mm
            
            # Create rectangle at base
            base_point = obj.BasePoint
            rect = Part.makePolygon([
                base_point + App.Vector(-width/2, -depth/2, 0),
                base_point + App.Vector(width/2, -depth/2, 0),
                base_point + App.Vector(width/2, depth/2, 0),
                base_point + App.Vector(-width/2, depth/2, 0),
                base_point + App.Vector(-width/2, -depth/2, 0)
            ])
            
            face = Part.Face(rect)
            height_vector = obj.TopPoint - obj.BasePoint
            solid = face.extrude(height_vector)
            
            return solid
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating column solid: {e}\n")
            return None
    
    def execute(self, obj) -> None:
        """
        Update column geometry and perform design checks.
        
        Args:
            obj: The DocumentObject being executed
        """
        # Update geometry
        self._update_geometry(obj)
        
        # Update buckling properties
        self._update_buckling_properties(obj)
        
        # Update design checks
        self._update_design_checks(obj)
        
        # Validate column design
        self._validate_design(obj)
    
    def _validate_design(self, obj) -> None:
        """Validate column design and provide warnings."""
        warnings = []
        
        # Check slenderness ratios
        if hasattr(obj, 'SlendernessRatioX') and obj.SlendernessRatioX > 200:
            warnings.append(f"High slenderness ratio in X direction: {obj.SlendernessRatioX:.1f}")
        
        if hasattr(obj, 'SlendernessRatioY') and obj.SlendernessRatioY > 200:
            warnings.append(f"High slenderness ratio in Y direction: {obj.SlendernessRatioY:.1f}")
        
        # Check interaction ratios
        if hasattr(obj, 'MaxInteractionRatio') and obj.MaxInteractionRatio > 1.0:
            warnings.append(f"Column overstressed: interaction ratio = {obj.MaxInteractionRatio:.2f}")
        
        # Check material assignment
        if not hasattr(obj, 'Material') or not obj.Material:
            warnings.append("No material assigned")
        
        # Log warnings
        if warnings:
            App.Console.PrintWarning(f"Column {obj.Label} warnings: {'; '.join(warnings)}\n")


class ViewProviderStructuralColumn:
    """
    ViewProvider for StructuralColumn with enhanced visualization.
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
                        "Show applied loads")
        vobj.ShowLoads = True
        
        vobj.addProperty("App::PropertyBool", "ShowDeflections", "Display",
                        "Show deformed shape")
        vobj.ShowDeflections = False
        
        vobj.addProperty("App::PropertyEnumeration", "ResultsDisplay", "Results",
                        "Type of results to display")
        vobj.ResultsDisplay = ["None", "Axial Force", "Moments", "Deflections", "Utilization"]
        vobj.ResultsDisplay = "None"
        
        vobj.addProperty("App::PropertyFloat", "ResultScale", "Results",
                        "Result display scale factor")
        vobj.ResultScale = 1.0
        
        vobj.addProperty("App::PropertyColor", "ColumnColor", "Display",
                        "Column color")
        vobj.ColumnColor = (0.7, 0.7, 0.9)  # Light blue
    
    def getIcon(self) -> str:
        """Return icon based on column status."""
        if not hasattr(self.Object, 'DesignPassed'):
            return self._get_icon_path("column_generic.svg")
        
        if self.Object.DesignPassed:
            return self._get_icon_path("column_ok.svg")
        else:
            return self._get_icon_path("column_overstressed.svg")
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icon_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")
        return os.path.join(icon_dir, icon_name)
    
    def setEdit(self, vobj, mode: int) -> bool:
        """Open column properties panel."""
        if mode == 0:
            try:
                from ..taskpanels.ColumnPropertiesPanel import ColumnPropertiesPanel
                self.panel = ColumnPropertiesPanel(vobj.Object)
                Gui.Control.showDialog(self.panel)
                return True
            except ImportError:
                App.Console.PrintWarning("ColumnPropertiesPanel not yet implemented\n")
                return False
        return False
    
    def unsetEdit(self, vobj, mode: int) -> bool:
        """Close column properties panel."""
        if hasattr(self, 'panel'):
            Gui.Control.closeDialog()
        return True
    
    def doubleClicked(self, vobj) -> bool:
        """Handle double-click to open properties."""
        return self.setEdit(vobj, 0)


def makeStructuralColumn(base_point=None, top_point=None, section_type="W", section_size="W14x90", name="StructuralColumn"):
    """
    Create a new StructuralColumn object.
    
    Args:
        base_point: Base point of column
        top_point: Top point of column
        section_type: Section type
        section_size: Section designation
        name: Object name
        
    Returns:
        Created StructuralColumn object
    """
    doc = App.ActiveDocument
    if not doc:
        App.Console.PrintError("No active document. Please create or open a document first.\n")
        return None
    
    # Create the object
    obj = doc.addObject("App::DocumentObjectGroupPython", name)
    StructuralColumn(obj)
    
    # Create ViewProvider
    if App.GuiUp:
        ViewProviderStructuralColumn(obj.ViewObject)
    
    # Set properties
    if base_point:
        obj.BasePoint = base_point
    if top_point:
        obj.TopPoint = top_point
    
    obj.SectionType = section_type
    obj.SectionDesignation = section_size
    
    # Generate unique ID
    column_count = len([o for o in doc.Objects if hasattr(o, 'Proxy') and hasattr(o.Proxy, 'Type') and o.Proxy.Type == "StructuralColumn"])
    obj.ColumnID = f"C{column_count + 1:03d}"
    
    # Recompute to update geometry
    obj.recompute()
    doc.recompute()
    
    App.Console.PrintMessage(f"Created StructuralColumn: {obj.Label} with ID: {obj.ColumnID}\n")
    return obj