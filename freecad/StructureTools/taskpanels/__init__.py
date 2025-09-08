# -*- coding: utf-8 -*-
"""
StructureTools Task Panels

This module contains all professional task panels for enhanced user interface
and streamlined structural engineering workflows.
"""

__title__ = "StructureTools Task Panels"
__author__ = "StructureTools Development Team"
__version__ = "2.0.0"

# Import all task panels for easy access (with error handling for dependencies)
try:
    from .PlatePropertiesPanel import PlatePropertiesPanel
except ImportError:
    PlatePropertiesPanel = None

try:
    from .MaterialTaskPanel import MaterialTaskPanel
except ImportError:
    MaterialTaskPanel = None
    
try:
    from .BeamPropertiesPanel import BeamPropertiesPanel
except ImportError:
    BeamPropertiesPanel = None
    
try:
    from .NodePropertiesPanel import NodePropertiesPanel
except ImportError:
    NodePropertiesPanel = None
    
try:
    from .LoadApplicationPanel import LoadApplicationPanel
except ImportError:
    LoadApplicationPanel = None
    
try:
    from .AnalysisSetupPanel import AnalysisSetupPanel
except ImportError:
    AnalysisSetupPanel = None
    
try:
    from .ProfileTaskPanel import ProfileTaskPanel
except ImportError:
    ProfileTaskPanel = None

__all__ = [
    "PlatePropertiesPanel",
    "MaterialTaskPanel",
    "BeamPropertiesPanel", 
    "NodePropertiesPanel",
    "LoadApplicationPanel",
    "AnalysisSetupPanel",
    "ProfileTaskPanel"
]