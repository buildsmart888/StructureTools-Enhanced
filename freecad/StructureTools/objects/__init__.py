# -*- coding: utf-8 -*-
"""
StructureTools Custom Document Objects

This module contains all custom FreeCAD Document Objects for structural engineering.
These objects provide enhanced functionality beyond basic FreeCAD objects with
validation, automation, and professional-grade features.
"""

__title__ = "StructureTools Objects"
__author__ = "StructureTools Development Team"
__version__ = "2.0.0"

# Import all custom objects for easy access
from .StructuralMaterial import StructuralMaterial, ViewProviderStructuralMaterial
from .StructuralNode import StructuralNode, ViewProviderStructuralNode
from .StructuralBeam import StructuralBeam, ViewProviderStructuralBeam
from .StructuralPlate import StructuralPlate, ViewProviderStructuralPlate
from .StructuralProfile import StructuralProfile, ViewProviderStructuralProfile, create_structural_profile

__all__ = [
    "StructuralMaterial",
    "ViewProviderStructuralMaterial", 
    "StructuralBeam",
    "ViewProviderStructuralBeam",
    "StructuralNode", 
    "ViewProviderStructuralNode",
    "StructuralPlate",
    "ViewProviderStructuralPlate",
    "StructuralProfile",
    "ViewProviderStructuralProfile",
    "create_structural_profile"
]