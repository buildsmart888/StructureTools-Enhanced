# -*- coding: utf-8 -*-
"""
validation.py - Input validation and model checking utilities

This module provides comprehensive validation functions for structural
engineering inputs and model integrity checking.
"""

import FreeCAD as App
import math
from typing import List, Dict, Tuple, Optional, Any, Union
from .exceptions import ValidationError, ModelError, MaterialError, GeometryError

# Import Global Units System
try:
    from .units_manager import (
        get_units_manager, format_force, format_stress, format_modulus
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e9:.0f} GPa"


class StructuralValidator:
    """
    Comprehensive validation class for structural engineering inputs.
    """
    
    def __init__(self):
        """Initialize validator with engineering limits."""
        
        # Material property limits (SI units)
        self.material_limits = {
            'elastic_modulus': {'min': 1e6, 'max': 1e12, 'unit': 'Pa'},  # 1 MPa to 1 TPa
            'poisson_ratio': {'min': 0.0, 'max': 0.5, 'unit': '-'},
            'density': {'min': 100, 'max': 50000, 'unit': 'kg/m³'},
            'yield_strength': {'min': 1e6, 'max': 5e9, 'unit': 'Pa'},
            'ultimate_strength': {'min': 1e6, 'max': 5e9, 'unit': 'Pa'}
        }
        
        # Geometric limits
        self.geometry_limits = {
            'length': {'min': 0.001, 'max': 10000, 'unit': 'm'},  # 1mm to 10km
            'thickness': {'min': 0.0001, 'max': 10, 'unit': 'm'}, # 0.1mm to 10m
            'area': {'min': 1e-8, 'max': 10000, 'unit': 'm²'},
            'angle': {'min': -360, 'max': 360, 'unit': 'degrees'}
        }
        
        # Load limits
        self.load_limits = {
            'force': {'min': 0.001, 'max': 1e12, 'unit': 'N'},
            'pressure': {'min': 0.001, 'max': 1e9, 'unit': 'Pa'},
            'moment': {'min': 0.001, 'max': 1e15, 'unit': 'N·m'},
            'load_factor': {'min': 0.0, 'max': 10.0, 'unit': '-'}
        }
    
    def validate_material_properties(self, material_obj) -> List[str]:
        """
        Validate material properties for engineering feasibility.
        
        Args:
            material_obj: StructuralMaterial object
            
        Returns:
            List of validation warning/error messages
        """
        warnings = []
        
        try:
            # Elastic modulus validation
            if hasattr(material_obj, 'ModulusElasticity'):
                E = self.get_property_value(material_obj.ModulusElasticity, 'Pa')
                limits = self.material_limits['elastic_modulus']
                if not (limits['min'] <= E <= limits['max']):
                    warnings.append(
                        f"Elastic modulus {E/1e9:.1f} GPa is outside typical range "
                        f"({limits['min']/1e9:.1f}-{limits['max']/1e9:.1f} GPa)"
                    )
            
            # Poisson ratio validation
            if hasattr(material_obj, 'PoissonRatio'):
                nu = material_obj.PoissonRatio
                limits = self.material_limits['poisson_ratio']
                if not (limits['min'] <= nu <= limits['max']):
                    raise ValidationError(
                        f"Poisson ratio must be between {limits['min']} and {limits['max']}",
                        parameter='PoissonRatio',
                        value=nu
                    )
                    
                # Check for auxetic materials (negative Poisson ratio)
                if nu < 0:
                    warnings.append("Negative Poisson ratio detected - auxetic material")
            
            # Density validation
            if hasattr(material_obj, 'Density'):
                rho = self.get_property_value(material_obj.Density, 'kg/m^3')
                limits = self.material_limits['density']
                if not (limits['min'] <= rho <= limits['max']):
                    warnings.append(
                        f"Density {rho:.0f} kg/m³ is outside typical range "
                        f"({limits['min']:.0f}-{limits['max']:.0f} kg/m³)"
                    )
            
            # Strength relationship validation
            if hasattr(material_obj, 'YieldStrength') and hasattr(material_obj, 'UltimateStrength'):
                fy = self.get_property_value(material_obj.YieldStrength, 'Pa')
                fu = self.get_property_value(material_obj.UltimateStrength, 'Pa')
                
                if fy >= fu:
                    raise ValidationError(
                        "Ultimate strength must be greater than yield strength",
                        parameter='Strength relationship',
                        value=f"fy={fy/1e6:.0f} MPa, fu={fu/1e6:.0f} MPa"
                    )
                
                # Check reasonable strength ratios
                strength_ratio = fu / fy if fy > 0 else 0
                if strength_ratio < 1.1:
                    warnings.append("Very low ultimate/yield strength ratio - check values")
                elif strength_ratio > 3.0:
                    warnings.append("Very high ultimate/yield strength ratio - check values")
            
        except ValidationError:
            raise
        except Exception as e:
            warnings.append(f"Error validating material properties: {str(e)}")
        
        return warnings
    
    def validate_geometric_properties(self, geometry_obj) -> List[str]:
        """
        Validate geometric properties for structural elements.
        
        Args:
            geometry_obj: Structural object with geometry
            
        Returns:
            List of validation messages
        """
        warnings = []
        
        try:
            # Length validation for beams/members
            if hasattr(geometry_obj, 'Length'):
                length = self.get_property_value(geometry_obj.Length, 'm')
                limits = self.geometry_limits['length']
                if not (limits['min'] <= length <= limits['max']):
                    warnings.append(
                        f"Member length {length:.3f} m is outside typical range "
                        f"({limits['min']:.3f}-{limits['max']:.0f} m)"
                    )
            
            # Thickness validation for plates
            if hasattr(geometry_obj, 'Thickness'):
                thickness = self.get_property_value(geometry_obj.Thickness, 'm')
                limits = self.geometry_limits['thickness']
                if not (limits['min'] <= thickness <= limits['max']):
                    warnings.append(
                        f"Plate thickness {thickness*1000:.1f} mm is outside typical range "
                        f"({limits['min']*1000:.1f}-{limits['max']*1000:.0f} mm)"
                    )
                    
                # Check for very thin plates (potential buckling issues)
                if hasattr(geometry_obj, 'Area'):
                    area = self.get_property_value(geometry_obj.Area, 'm²')
                    side_length = math.sqrt(area)  # Approximate square
                    slenderness = side_length / thickness
                    
                    if slenderness > 200:
                        warnings.append(
                            f"Very slender plate (L/t = {slenderness:.0f}) - "
                            "consider buckling analysis"
                        )
            
            # Aspect ratio validation
            if hasattr(geometry_obj, 'AspectRatio'):
                aspect_ratio = geometry_obj.AspectRatio
                if aspect_ratio > 10:
                    warnings.append(
                        f"High aspect ratio ({aspect_ratio:.1f}) - "
                        "consider mesh refinement"
                    )
                elif aspect_ratio < 0.1:
                    warnings.append(
                        f"Very low aspect ratio ({aspect_ratio:.1f}) - "
                        "check geometry definition"
                    )
        
        except Exception as e:
            warnings.append(f"Error validating geometry: {str(e)}")
        
        return warnings
    
    def validate_load_application(self, load_obj) -> List[str]:
        """
        Validate load definitions and magnitudes.
        
        Args:
            load_obj: Load object (nodal, distributed, or area)
            
        Returns:
            List of validation messages
        """
        warnings = []
        
        try:
            # Load magnitude validation
            if hasattr(load_obj, 'Magnitude') or hasattr(load_obj, 'LoadMagnitude'):
                magnitude_attr = 'LoadMagnitude' if hasattr(load_obj, 'LoadMagnitude') else 'Magnitude'
                magnitude = getattr(load_obj, magnitude_attr)
                
                # Determine load type for appropriate limits
                if hasattr(load_obj, 'Type'):
                    load_type = load_obj.Type
                    if 'Area' in load_type:
                        # Area/pressure load
                        mag_value = self.get_property_value(magnitude, 'Pa')
                        limits = self.load_limits['pressure']
                        unit_str = "Pa"
                    else:
                        # Force load
                        mag_value = self.get_property_value(magnitude, 'N')
                        limits = self.load_limits['force']
                        unit_str = "N"
                    
                    if not (limits['min'] <= abs(mag_value) <= limits['max']):
                        warnings.append(
                            f"Load magnitude {mag_value:.2e} {unit_str} is outside typical range "
                            f"({limits['min']:.0e}-{limits['max']:.0e} {unit_str})"
                        )
                    
                    # Check for zero loads
                    if abs(mag_value) < limits['min']:
                        warnings.append("Load magnitude is very small - check units")
            
            # Load factor validation
            if hasattr(load_obj, 'LoadFactor'):
                factor = load_obj.LoadFactor
                limits = self.load_limits['load_factor']
                if not (limits['min'] <= factor <= limits['max']):
                    warnings.append(
                        f"Load factor {factor:.2f} is outside typical range "
                        f"({limits['min']:.1f}-{limits['max']:.1f})"
                    )
            
            # Direction validation for vector loads
            if hasattr(load_obj, 'Direction'):
                direction = load_obj.Direction
                if hasattr(direction, 'Length'):
                    if direction.Length < 0.001:
                        raise ValidationError(
                            "Load direction vector has zero or near-zero magnitude",
                            parameter='Direction',
                            value=direction
                        )
        
        except ValidationError:
            raise
        except Exception as e:
            warnings.append(f"Error validating load: {str(e)}")
        
        return warnings
    
    def validate_structural_model(self, calc_obj) -> Dict[str, List[str]]:
        """
        Comprehensive structural model validation.
        
        Args:
            calc_obj: Calc object containing structural model
            
        Returns:
            Dictionary of validation results by category
        """
        validation_results = {
            'errors': [],
            'warnings': [],
            'info': []
        }
        
        try:
            if not hasattr(calc_obj, 'ListElements'):
                validation_results['errors'].append("No structural elements found in model")
                return validation_results
            
            elements = calc_obj.ListElements
            
            # Count different element types
            beams = [e for e in elements if 'Line' in e.Name or 'Wire' in e.Name]
            plates = [e for e in elements if 'Plate' in e.Name]
            loads = [e for e in elements if 'Load' in e.Name]
            supports = [e for e in elements if 'Suport' in e.Name]
            
            validation_results['info'].append(f"Model contains: {len(beams)} beams, "
                                            f"{len(plates)} plates, {len(loads)} loads, "
                                            f"{len(supports)} supports")
            
            # Check for minimum required elements
            if len(beams) == 0 and len(plates) == 0:
                validation_results['errors'].append("No structural elements (beams or plates) found")
            
            if len(supports) == 0:
                validation_results['warnings'].append("No supports defined - structure may be unstable")
            
            if len(loads) == 0:
                validation_results['warnings'].append("No loads applied to structure")
            
            # Check for duplicate elements at same location
            duplicate_warnings = self.check_duplicate_elements(elements)
            validation_results['warnings'].extend(duplicate_warnings)
            
            # Validate element connectivity
            connectivity_warnings = self.check_element_connectivity(beams, plates)
            validation_results['warnings'].extend(connectivity_warnings)
            
            # Check for material assignments
            material_warnings = self.check_material_assignments(beams + plates)
            validation_results['warnings'].extend(material_warnings)
            
        except Exception as e:
            validation_results['errors'].append(f"Error validating structural model: {str(e)}")
        
        return validation_results
    
    def check_duplicate_elements(self, elements) -> List[str]:
        """Check for duplicate elements at same locations."""
        warnings = []
        
        # Group elements by approximate location
        locations = {}
        tolerance = 1.0  # mm
        
        for element in elements:
            try:
                if hasattr(element, 'Shape') and hasattr(element.Shape, 'CenterOfMass'):
                    center = element.Shape.CenterOfMass
                    # Round to tolerance
                    rounded_pos = (
                        round(center.x / tolerance) * tolerance,
                        round(center.y / tolerance) * tolerance,
                        round(center.z / tolerance) * tolerance
                    )
                    
                    if rounded_pos not in locations:
                        locations[rounded_pos] = []
                    locations[rounded_pos].append(element.Name)
            except:
                continue
        
        # Report duplicates
        for pos, elements_at_pos in locations.items():
            if len(elements_at_pos) > 1:
                warnings.append(f"Multiple elements at similar location {pos}: {elements_at_pos}")
        
        return warnings
    
    def check_element_connectivity(self, beams, plates) -> List[str]:
        """Check structural element connectivity."""
        warnings = []
        
        if not beams and not plates:
            return warnings
        
        # For beams, check for disconnected members
        beam_endpoints = []
        tolerance = 1.0  # mm
        
        for beam in beams:
            try:
                if hasattr(beam, 'Shape') and hasattr(beam.Shape, 'Vertexes'):
                    vertices = beam.Shape.Vertexes
                    if len(vertices) >= 2:
                        start = vertices[0].Point
                        end = vertices[-1].Point
                        beam_endpoints.extend([start, end])
            except:
                continue
        
        # Find isolated endpoints (not connected to other members)
        isolated_points = []
        for i, point1 in enumerate(beam_endpoints):
            connections = 0
            for j, point2 in enumerate(beam_endpoints):
                if i != j:
                    distance = point1.distanceToPoint(point2)
                    if distance <= tolerance:
                        connections += 1
            
            if connections < 1:  # Point appears only once (isolated end)
                isolated_points.append(point1)
        
        if isolated_points:
            warnings.append(f"Found {len(isolated_points)} isolated beam endpoints - "
                          "structure may not be properly connected")
        
        return warnings
    
    def check_material_assignments(self, structural_elements) -> List[str]:
        """Check that all structural elements have material assignments."""
        warnings = []
        
        elements_without_material = []
        for element in structural_elements:
            has_material = False
            
            # Check various ways materials might be assigned
            if hasattr(element, 'Material') and element.Material:
                has_material = True
            elif hasattr(element, 'MaterialName') and element.MaterialName:
                has_material = True
            
            if not has_material:
                elements_without_material.append(element.Name)
        
        if elements_without_material:
            warnings.append(f"Elements without material assignment: {elements_without_material}")
        
        return warnings
    
    @staticmethod
    def get_property_value(property_obj, target_unit: str) -> float:
        """
        Extract numeric value from FreeCAD property with unit conversion.
        
        Args:
            property_obj: FreeCAD property (could be Quantity or numeric)
            target_unit: Target unit string
            
        Returns:
            Numeric value in target units
        """
        try:
            # If it's a FreeCAD Quantity with getValueAs method
            if hasattr(property_obj, 'getValueAs'):
                return property_obj.getValueAs(target_unit)
            
            # If it's already a number
            if isinstance(property_obj, (int, float)):
                return float(property_obj)
            
            # Try to convert string
            if isinstance(property_obj, str):
                return float(property_obj)
            
            # Fallback
            return float(property_obj)
            
        except (ValueError, TypeError, AttributeError):
            raise ValidationError(
                f"Could not extract numeric value from {property_obj} for unit {target_unit}",
                parameter='property_value',
                value=property_obj
            )