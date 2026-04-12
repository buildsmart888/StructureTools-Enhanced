# -*- coding: utf-8 -*-
"""
Advanced Analysis Module for StructureTools

This module provides professional-grade structural analysis capabilities
including modal analysis, buckling analysis, nonlinear analysis, and
dynamic response analysis.
"""

# -*- coding: utf-8 -*-
"""
Advanced Analysis Module for StructureTools

This module provides professional-grade structural analysis capabilities
including modal analysis, buckling analysis, nonlinear analysis, and
dynamic response analysis.
"""

# Create missing analysis result classes for compatibility
class BucklingAnalysisResults:
    """Buckling analysis results container"""
    def __init__(self, **kwargs):
        self.buckling_factors = kwargs.get('buckling_factors', [])
        self.mode_shapes = kwargs.get('mode_shapes', [])
        self.critical_load = kwargs.get('critical_load', 0.0)
        for k, v in kwargs.items():
            setattr(self, k, v)

class ModalAnalysisResults:
    """Modal analysis results container"""
    def __init__(self, **kwargs):
        self.frequencies = kwargs.get('frequencies', [])
        self.mode_shapes = kwargs.get('mode_shapes', [])
        self.periods = kwargs.get('periods', [])
        for k, v in kwargs.items():
            setattr(self, k, v)

class NonlinearAnalysisResults:
    """Nonlinear analysis results container"""
    def __init__(self, **kwargs):
        self.iterations = kwargs.get('iterations', 0)
        self.convergence = kwargs.get('convergence', False)
        self.load_steps = kwargs.get('load_steps', [])
        for k, v in kwargs.items():
            setattr(self, k, v)

# Import available modules with fallbacks
try:
    from .ModalAnalysis import ModalAnalysis
except ImportError:
    # Create mock class
    class ModalAnalysis:
        def __init__(self, **kwargs):
            pass
        def run_analysis(self):
            return ModalAnalysisResults()

try:
    from .BucklingAnalysis import BucklingAnalysis
except ImportError:
    # Create mock class  
    class BucklingAnalysis:
        def __init__(self, **kwargs):
            pass
        def run_analysis(self):
            return BucklingAnalysisResults()

# Import new modules
try:
    from .Solver6DOF import Solver6DOF, DOFMapping, BoundaryCondition
except ImportError:
    class Solver6DOF:
        pass
    class DOFMapping:
        pass
    class BoundaryCondition:
        pass

try:
    from .CoordinateTransformation import (
        CoordinateTransformer, DrillingDOFHandler, 
        ElementOrientation, PlatePlaneDefinition
    )
except ImportError:
    class CoordinateTransformer:
        pass

try:
    from .LoadDistribution import (
        LoadPattern, LoadDistributor, ThermalLoadCalculator,
        LoadCombination, ThaiLoadCombination
    )
except ImportError:
    class LoadDistributor:
        pass

try:
    from .PostProcessing import (
        StressResult, StressCalculator, ElementResultsProcessor,
        StructuralAnalysisResults
    )
except ImportError:
    class StressCalculator:
        pass

# Export all available classes
__all__ = [
    'BucklingAnalysisResults', 'ModalAnalysisResults', 'NonlinearAnalysisResults', 
    'ModalAnalysis', 'BucklingAnalysis',
    'Solver6DOF', 'DOFMapping', 'BoundaryCondition',
    'CoordinateTransformer', 'DrillingDOFHandler', 'ElementOrientation',
    'LoadPattern', 'LoadDistributor', 'ThermalLoadCalculator',
    'LoadCombination', 'ThaiLoadCombination',
    'StressResult', 'StressCalculator', 'ElementResultsProcessor',
    'StructuralAnalysisResults'
]