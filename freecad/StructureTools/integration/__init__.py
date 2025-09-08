# -*- coding: utf-8 -*-
"""
Integration module for StructureTools workbench
Provides bridges to other FreeCAD workbenches (BIM, FEM, TechDraw)
"""

# Import integration modules when available
try:
    from .BIMIntegration import BIMStructuralIntegration, CommandBIMIntegration
    from .BIMCommands import CommandBIMExport, CommandBIMSync
    BIM_AVAILABLE = True
except ImportError:
    BIM_AVAILABLE = False

try:
    from .TechDrawIntegration import TechDrawStructuralIntegration, CommandCreateStructuralDrawing
    TECHDRAW_AVAILABLE = True
except ImportError:
    TECHDRAW_AVAILABLE = False

try:
    from .FEMIntegration import FEMStructuralBridge, CommandExportToFEM
    FEM_AVAILABLE = True
except ImportError:
    FEM_AVAILABLE = False

try:
    from .ProfileCalcIntegration import ProfileCalcIntegrator
    from .ProfileCalcIntegration import apply_profile_to_member, create_calc_section_from_profile, get_profile_calc_properties
    PROFILE_CALC_AVAILABLE = True
except ImportError:
    PROFILE_CALC_AVAILABLE = False

__all__ = [
    'BIMStructuralIntegration', 'CommandBIMIntegration', 'CommandBIMExport', 'CommandBIMSync',
    'TechDrawStructuralIntegration', 'CommandCreateStructuralDrawing',
    'FEMStructuralBridge', 'CommandExportToFEM',
    'ProfileCalcIntegrator', 'apply_profile_to_member', 'create_calc_section_from_profile', 'get_profile_calc_properties',
    'BIM_AVAILABLE', 'TECHDRAW_AVAILABLE', 'FEM_AVAILABLE', 'PROFILE_CALC_AVAILABLE'
]