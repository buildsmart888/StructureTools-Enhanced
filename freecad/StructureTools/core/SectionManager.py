# -*- coding: utf-8 -*-
"""
Section Manager - Central Management for Section Operations

This module provides centralized management for section operations,
separating business logic from UI and FreeCAD-specific code.
"""

from typing import Dict, List, Optional, Tuple, Any
import logging

# Setup logging
logger = logging.getLogger(__name__)

class SectionManager:
    """
    Central manager for section operations.
    Handles business logic separate from FreeCAD integration.
    """
    
    def __init__(self):
        self.database_available = False
        self.section_standards = {}
        self.validators = {}
        self.geometry_generators = {}
        self._initialize_components()
    
    def _initialize_components(self):
        """Initialize manager components."""
        try:
            # Import database
            from ..data.SectionStandards import SECTION_STANDARDS, get_section_info
            self.section_standards = SECTION_STANDARDS
            self.get_section_info = get_section_info
            self.database_available = True
            logger.info(f"Section database initialized with {len(SECTION_STANDARDS)} sections")
            
            # Import validators
            from ..data.SectionValidator import validate_section_for_design_code, calculate_section_classification
            self.validate_section = validate_section_for_design_code
            self.classify_section = calculate_section_classification
            
        except ImportError as e:
            logger.error(f"Failed to initialize section components: {str(e)}")
            self.database_available = False
    
    def detect_section_from_name(self, name: str) -> str:
        """
        Intelligent section detection from object name.
        
        Args:
            name: Object name or label
            
        Returns:
            Detected section name or "Custom"
        """
        if not self.database_available:
            return "Custom"
        
        try:
            name_upper = name.upper()
            
            # Direct match patterns
            section_patterns = {
                'W': ['W12X26', 'W14X22', 'W16X31', 'W18X35'],
                'IPE': ['IPE100', 'IPE120', 'IPE160', 'IPE200', 'IPE240', 'IPE300'],
                'HEB': ['HEB100', 'HEB120', 'HEB160', 'HEB200'],
                'HSS': ['HSS6X4X1/4', 'HSS8X6X1/4', 'HSS4.000X0.250', 'HSS6.625X0.280']
            }
            
            # Look for exact matches first
            for section_name in self.section_standards.keys():
                if section_name.upper() in name_upper or name_upper in section_name.upper():
                    logger.debug(f"Detected section '{section_name}' from name '{name}'")
                    return section_name
            
            # Look for pattern matches
            for pattern_prefix, sections in section_patterns.items():
                if pattern_prefix in name_upper:
                    for section in sections:
                        if section in self.section_standards:
                            logger.debug(f"Pattern-detected section '{section}' from name '{name}'")
                            return section
            
            logger.debug(f"No section detected from name '{name}', defaulting to Custom")
            return "Custom"
            
        except Exception as e:
            logger.error(f"Error detecting section from name '{name}': {str(e)}")
            return "Custom"
    
    def get_section_properties(self, section_name: str) -> Optional[Dict]:
        """
        Get comprehensive section properties.
        
        Args:
            section_name: Section standard name
            
        Returns:
            Section properties dictionary or None
        """
        if not self.database_available or section_name == "Custom":
            return None
        
        try:
            properties = self.get_section_info(section_name)
            if properties:
                # Add derived properties
                properties = self._calculate_derived_properties(properties)
                logger.debug(f"Retrieved properties for section '{section_name}'")
            else:
                logger.warning(f"No properties found for section '{section_name}'")
            
            return properties
            
        except Exception as e:
            logger.error(f"Error retrieving properties for section '{section_name}': {str(e)}")
            return None
    
    def _calculate_derived_properties(self, properties: Dict) -> Dict:
        """Calculate additional derived properties."""
        try:
            # Calculate plastic moduli if not present
            if "Zx" not in properties and "Ix" in properties and "Depth" in properties:
                # Rough approximation for plastic modulus
                ix = properties["Ix"]
                depth = properties["Depth"]
                properties["Zx_calculated"] = (ix * 2.5) / depth  # Approximation
            
            # Calculate shape factors
            if "Zx" in properties and "Sx" in properties:
                properties["ShapeFactorX"] = properties["Zx"] / properties["Sx"]
            
            # Calculate section efficiency metrics
            if "Area" in properties and "Weight" in properties:
                properties["AreaPerWeight"] = properties["Area"] / properties["Weight"]
            
            return properties
            
        except Exception as e:
            logger.error(f"Error calculating derived properties: {str(e)}")
            return properties
    
    def validate_section_properties(self, properties: Dict, design_code: str = "AISC_360") -> Tuple[bool, List[str], List[str]]:
        """
        Validate section properties against design requirements.
        
        Args:
            properties: Section properties dictionary
            design_code: Design code for validation
            
        Returns:
            Tuple of (is_valid, errors, warnings)
        """
        try:
            if hasattr(self, 'validate_section'):
                return self.validate_section(properties, design_code)
            else:
                logger.warning("Section validation not available")
                return True, [], ["Validation not available"]
                
        except Exception as e:
            logger.error(f"Error validating section: {str(e)}")
            return False, [f"Validation error: {str(e)}"], []
    
    def classify_section_for_design(self, properties: Dict, material_grade: str = "A992") -> str:
        """
        Classify section for structural design.
        
        Args:
            properties: Section properties dictionary
            material_grade: Material grade
            
        Returns:
            Section classification (Compact, Non-compact, Slender)
        """
        try:
            if hasattr(self, 'classify_section'):
                classification = self.classify_section(properties, material_grade)
                logger.debug(f"Section classified as: {classification}")
                return classification
            else:
                logger.warning("Section classification not available")
                return "Unknown"
                
        except Exception as e:
            logger.error(f"Error classifying section: {str(e)}")
            return "Error"
    
    def get_available_sections(self, filter_criteria: Optional[Dict] = None) -> List[str]:
        """
        Get list of available sections with optional filtering.
        
        Args:
            filter_criteria: Optional filtering criteria
            
        Returns:
            List of section names
        """
        if not self.database_available:
            return []
        
        try:
            sections = list(self.section_standards.keys())
            
            if filter_criteria:
                sections = self._apply_section_filters(sections, filter_criteria)
            
            logger.debug(f"Retrieved {len(sections)} sections")
            return sections
            
        except Exception as e:
            logger.error(f"Error retrieving available sections: {str(e)}")
            return []
    
    def _apply_section_filters(self, sections: List[str], criteria: Dict) -> List[str]:
        """Apply filtering criteria to section list."""
        filtered_sections = []
        
        try:
            for section_name in sections:
                properties = self.get_section_info(section_name)
                if not properties:
                    continue
                
                # Apply filters
                include_section = True
                
                if "min_depth" in criteria:
                    if properties.get("Depth", 0) < criteria["min_depth"]:
                        include_section = False
                
                if "max_depth" in criteria:
                    if properties.get("Depth", float('inf')) > criteria["max_depth"]:
                        include_section = False
                
                if "max_weight" in criteria:
                    if properties.get("Weight", float('inf')) > criteria["max_weight"]:
                        include_section = False
                
                if "section_type" in criteria:
                    if properties.get("Type", "") != criteria["section_type"]:
                        include_section = False
                
                if include_section:
                    filtered_sections.append(section_name)
            
            return filtered_sections
            
        except Exception as e:
            logger.error(f"Error applying section filters: {str(e)}")
            return sections

class SectionGeometryFactory:
    """
    Factory for creating section geometry.
    Separates geometry creation from main section logic.
    """
    
    def __init__(self):
        self.generators = {}
        self._register_generators()
    
    def _register_generators(self):
        """Register available geometry generators."""
        try:
            # Import geometry generators
            from .geometry_generators import (
                IBeamGenerator, RectangularHSSGenerator, 
                CircularHSSGenerator, AngleGenerator, ChannelGenerator
            )
            
            self.generators = {
                "Wide Flange": IBeamGenerator(),
                "I-Beam": IBeamGenerator(),
                "H-Beam": IBeamGenerator(),
                "Rectangular HSS": RectangularHSSGenerator(),
                "Circular HSS": CircularHSSGenerator(),
                "Equal Angle": AngleGenerator(),
                "Unequal Angle": AngleGenerator(),
                "Channel": ChannelGenerator()
            }
            
            logger.info(f"Registered {len(self.generators)} geometry generators")
            
        except ImportError:
            logger.warning("Geometry generators not available - will use legacy methods")
    
    def generate_geometry(self, section_properties: Dict):
        """
        Generate section geometry from properties.
        
        Args:
            section_properties: Section properties dictionary
            
        Returns:
            Generated geometry or None
        """
        try:
            section_type = section_properties.get("Type", "")
            
            if section_type in self.generators:
                generator = self.generators[section_type]
                geometry = generator.generate(section_properties)
                logger.debug(f"Generated geometry for section type: {section_type}")
                return geometry
            else:
                logger.warning(f"No generator available for section type: {section_type}")
                return None
                
        except Exception as e:
            logger.error(f"Error generating section geometry: {str(e)}")
            return None

class SectionPropertyCalculator:
    """
    Calculator for section properties from geometry.
    Handles both database and calculated properties.
    """
    
    @staticmethod
    def calculate_properties_from_face(face) -> Dict:
        """
        Calculate section properties from FreeCAD face.
        
        Args:
            face: FreeCAD face object
            
        Returns:
            Dictionary of calculated properties
        """
        try:
            properties = {}
            
            if not face or not hasattr(face, 'Area'):
                return properties
            
            # Basic geometric properties
            properties["Area"] = face.Area
            properties["CenterOfMass"] = face.CenterOfMass
            
            # Moments of inertia
            if hasattr(face, 'MatrixOfInertia'):
                matrix = face.MatrixOfInertia
                if hasattr(matrix, 'A') and len(matrix.A) >= 6:
                    cx, cy, cz = face.CenterOfMass
                    A = face.Area
                    
                    # Extract and adjust moments of inertia
                    Iy = matrix.A[5] + A * cx**2  # Apply parallel axis theorem
                    Iz = matrix.A[0] + A * cy**2
                    Iyz = matrix.A[1] + A * cx * cy
                    
                    properties["Iy"] = Iy
                    properties["Iz"] = Iz
                    properties["Iyz"] = Iyz
                    properties["J"] = Iy + Iz  # Polar moment (approximation)
            
            # Bounding box dimensions
            if hasattr(face, 'BoundBox'):
                bbox = face.BoundBox
                properties["Depth"] = bbox.YMax - bbox.YMin
                properties["Width"] = bbox.XMax - bbox.XMin
            
            # Calculate section moduli (rough estimates)
            if "Iy" in properties and "Depth" in properties:
                properties["Sx"] = (2 * properties["Iy"]) / properties["Depth"]
            
            if "Iz" in properties and "Width" in properties:
                properties["Sy"] = (2 * properties["Iz"]) / properties["Width"]
            
            # Calculate radii of gyration
            if "Area" in properties and properties["Area"] > 0:
                A = properties["Area"]
                if "Iy" in properties:
                    properties["ry"] = (properties["Iy"] / A) ** 0.5
                if "Iz" in properties:
                    properties["rz"] = (properties["Iz"] / A) ** 0.5
            
            logger.debug("Calculated section properties from face geometry")
            return properties
            
        except Exception as e:
            logger.error(f"Error calculating properties from face: {str(e)}")
            return {}
    
    @staticmethod
    def validate_calculated_properties(properties: Dict) -> Tuple[List[str], List[str]]:
        """
        Validate calculated properties for engineering reasonableness.
        
        Args:
            properties: Calculated properties dictionary
            
        Returns:
            Tuple of (errors, warnings)
        """
        errors = []
        warnings = []
        
        try:
            # Check area
            area = properties.get("Area", 0)
            if area <= 0:
                errors.append("Section area must be positive")
            elif area < 100:  # mm²
                warnings.append(f"Very small section area: {area:.1f} mm²")
            elif area > 1000000:  # mm²  
                warnings.append(f"Very large section area: {area:.1f} mm²")
            
            # Check moments of inertia
            for prop in ["Iy", "Iz"]:
                value = properties.get(prop, 0)
                if value < 0:
                    errors.append(f"{prop} cannot be negative")
                elif value == 0 and area > 0:
                    warnings.append(f"{prop} is zero - may indicate calculation error")
            
            # Check dimensions
            depth = properties.get("Depth", 0)
            width = properties.get("Width", 0)
            
            if depth <= 0:
                errors.append("Section depth must be positive")
            elif depth < 10:  # mm
                warnings.append(f"Very small depth: {depth:.1f} mm")
            elif depth > 2000:  # mm
                warnings.append(f"Very large depth: {depth:.1f} mm")
            
            if width <= 0:
                errors.append("Section width must be positive")
            elif width < 10:  # mm
                warnings.append(f"Very small width: {width:.1f} mm")
            elif width > 1000:  # mm
                warnings.append(f"Very large width: {width:.1f} mm")
            
            return errors, warnings
            
        except Exception as e:
            return [f"Validation error: {str(e)}"], []