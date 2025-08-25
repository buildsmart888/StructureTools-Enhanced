# -*- coding: utf-8 -*-
"""
Advanced Analysis Module for StructureTools

This module provides professional-grade structural analysis capabilities
including modal analysis, buckling analysis, nonlinear analysis, and
dynamic response analysis.
"""

from .ModalAnalysis import ModalAnalysis, ModalAnalysisResults

__all__ = [
    'ModalAnalysis',
    'ModalAnalysisResults'
]

# Future imports will be added as modules are implemented
# from .BucklingAnalysis import BucklingAnalysis, BucklingResults
# from .NonlinearAnalysis import NonlinearAnalysis, NonlinearResults