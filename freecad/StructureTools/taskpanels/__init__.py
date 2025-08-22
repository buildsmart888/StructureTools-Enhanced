# -*- coding: utf-8 -*-
"""
StructureTools Task Panels

This module contains all professional task panels for enhanced user interface
and streamlined structural engineering workflows.
"""

__title__ = "StructureTools Task Panels"
__author__ = "StructureTools Development Team"
__version__ = "2.0.0"

# Import all task panels for easy access
from .MaterialTaskPanel import MaterialTaskPanel
from .BeamPropertiesPanel import BeamPropertiesPanel
from .NodePropertiesPanel import NodePropertiesPanel
from .LoadApplicationPanel import LoadApplicationPanel
from .AnalysisSetupPanel import AnalysisSetupPanel

__all__ = [
    "MaterialTaskPanel",
    "BeamPropertiesPanel", 
    "NodePropertiesPanel",
    "LoadApplicationPanel",
    "AnalysisSetupPanel"
]