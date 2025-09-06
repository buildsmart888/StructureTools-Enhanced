# -*- coding: utf-8 -*-
"""
exceptions.py - Custom exceptions for StructureTools

This module defines custom exception classes for proper error handling
and user feedback throughout the StructureTools workbench.
"""

class StructureToolsError(Exception):
    """Base exception for all StructureTools errors."""
    pass


class ValidationError(StructureToolsError):
    """Raised when input validation fails."""
    
    def __init__(self, message, parameter=None, value=None):
        super().__init__(message)
        self.parameter = parameter
        self.value = value
        
    def __str__(self):
        if self.parameter and self.value:
            return f"Validation Error for {self.parameter}={self.value}: {super().__str__()}"
        return super().__str__()


class ModelError(StructureToolsError):
    """Raised when structural model has issues."""
    
    def __init__(self, message, model_object=None, issue_type=None):
        super().__init__(message)
        self.model_object = model_object
        self.issue_type = issue_type


class AnalysisError(StructureToolsError):
    """Raised when analysis fails."""
    
    def __init__(self, message, analysis_type=None, convergence_info=None):
        super().__init__(message)
        self.analysis_type = analysis_type
        self.convergence_info = convergence_info


class GeometryError(StructureToolsError):
    """Raised when geometry operations fail."""
    
    def __init__(self, message, geometry_object=None):
        super().__init__(message)
        self.geometry_object = geometry_object


class MaterialError(StructureToolsError):
    """Raised when material properties are invalid."""
    
    def __init__(self, message, material_name=None, property_name=None):
        super().__init__(message)
        self.material_name = material_name
        self.property_name = property_name


class MeshingError(StructureToolsError):
    """Raised when meshing operations fail."""
    
    def __init__(self, message, mesh_quality=None, element_count=None):
        super().__init__(message)
        self.mesh_quality = mesh_quality
        self.element_count = element_count


class LoadError(StructureToolsError):
    """Raised when load application fails."""
    
    def __init__(self, message, load_type=None, load_magnitude=None):
        super().__init__(message)
        self.load_type = load_type
        self.load_magnitude = load_magnitude


class ConfigurationError(StructureToolsError):
    """Raised when configuration is invalid."""
    
    def __init__(self, message, config_parameter=None):
        super().__init__(message)
        self.config_parameter = config_parameter