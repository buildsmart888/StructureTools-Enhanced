# -*- coding: utf-8 -*-
"""
Core architecture test package.
Tests for the modular core architecture components.
"""

# Core test modules
from .test_section_manager import TestSectionManager, TestSectionGeometryFactory, TestSectionPropertyCalculator
from .test_geometry_generators import (
    TestSectionGeometryGenerator, TestIBeamGenerator, TestRectangularHSSGenerator,
    TestCircularHSSGenerator, TestAngleGenerator, TestChannelGenerator,
    TestCreateGeometryGenerator
)
from .test_core_integration import TestCoreIntegration

__all__ = [
    # Section Manager Tests
    'TestSectionManager',
    'TestSectionGeometryFactory', 
    'TestSectionPropertyCalculator',
    
    # Geometry Generator Tests
    'TestSectionGeometryGenerator',
    'TestIBeamGenerator',
    'TestRectangularHSSGenerator',
    'TestCircularHSSGenerator',
    'TestAngleGenerator',
    'TestChannelGenerator',
    'TestCreateGeometryGenerator',
    
    # Integration Tests
    'TestCoreIntegration'
]