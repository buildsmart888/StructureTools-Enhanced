# -*- coding: utf-8 -*-
"""
StructureTools Core Module

This module contains the core business logic and architecture for StructureTools,
separated from FreeCAD-specific implementations.
"""

from .SectionManager import SectionManager, SectionGeometryFactory, SectionPropertyCalculator
from .geometry_generators import (
    SectionGeometryGenerator, IBeamGenerator, RectangularHSSGenerator, 
    CircularHSSGenerator, AngleGenerator, ChannelGenerator, create_geometry_generator
)

# Version info
__version__ = "2.1.0"
__author__ = "StructureTools Development Team"

# Main factory instances
_section_manager = None
_geometry_factory = None

def get_section_manager() -> SectionManager:
    """Get singleton instance of SectionManager."""
    global _section_manager
    if _section_manager is None:
        _section_manager = SectionManager()
    return _section_manager

def get_geometry_factory() -> SectionGeometryFactory:
    """Get singleton instance of SectionGeometryFactory."""
    global _geometry_factory
    if _geometry_factory is None:
        _geometry_factory = SectionGeometryFactory()
    return _geometry_factory

# Convenience functions
def detect_section_from_name(name: str) -> str:
    """Convenience function for section detection."""
    manager = get_section_manager()
    return manager.detect_section_from_name(name)

def get_section_properties(section_name: str) -> dict:
    """Convenience function to get section properties."""
    manager = get_section_manager()
    return manager.get_section_properties(section_name)

def generate_section_geometry(section_properties: dict):
    """Convenience function to generate section geometry."""
    factory = get_geometry_factory()
    return factory.generate_geometry(section_properties)

def calculate_properties_from_face(face) -> dict:
    """Convenience function to calculate properties from face."""
    return SectionPropertyCalculator.calculate_properties_from_face(face)

__all__ = [
    'SectionManager', 'SectionGeometryFactory', 'SectionPropertyCalculator',
    'SectionGeometryGenerator', 'IBeamGenerator', 'RectangularHSSGenerator',
    'CircularHSSGenerator', 'AngleGenerator', 'ChannelGenerator',
    'get_section_manager', 'get_geometry_factory',
    'detect_section_from_name', 'get_section_properties', 
    'generate_section_geometry', 'calculate_properties_from_face',
    'create_geometry_generator'
]