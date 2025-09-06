# -*- coding: utf-8 -*-
"""
Meshing Module for StructureTools

This module provides meshing functionality for structural analysis,
including 2D plate/shell meshing and 3D solid meshing capabilities.
"""

from .PlateMesher import PlateMesher
from .SurfaceMesh import SurfaceMesh, MeshIntegrationManager

__all__ = ['PlateMesher', 'SurfaceMesh', 'MeshIntegrationManager']