# -*- coding: utf-8 -*-
"""
StructureTools utilities package.

This package provides utility functions and classes for error handling,
validation, logging, and other common operations.
"""

from .exceptions import (
    StructureToolsError,
    ValidationError, 
    ModelError,
    AnalysisError,
    GeometryError,
    MaterialError,
    MeshingError,
    LoadError,
    ConfigurationError
)

from .validation import StructuralValidator

__all__ = [
    'StructureToolsError',
    'ValidationError',
    'ModelError', 
    'AnalysisError',
    'GeometryError',
    'MaterialError',
    'MeshingError',
    'LoadError',
    'ConfigurationError',
    'StructuralValidator'
]