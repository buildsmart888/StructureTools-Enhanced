# -*- coding: utf-8 -*-
"""
ACI 318-19 Design Module Initialization for StructureTools Phase 2
=================================================================

This module provides the public interface for ACI 318-19 concrete design
capabilities in StructureTools Phase 2.

Key Features:
- Complete flexural design (beams, slabs)
- Comprehensive shear design 
- Column design with interaction diagrams
- Foundation design (footings, piles)
- Development length calculations
- Professional reporting and code compliance

Usage:
    from freecad.StructureTools.design.aci import ACI318Designer, ConcreteGrade, RebarGrade
    
    # Create designer instance
    designer = ACI318Designer()
    
    # Design beam
    result = designer.design_beam(section, concrete_grade, rebar_grade, forces)
    
    # Generate report
    report = designer.generate_report([result])
"""

from typing import Dict, List, Tuple, Optional, Any, Union

from .ACI318 import (
    ACI318,
    ConcreteGrade,
    RebarGrade, 
    ConcreteMaterialProperties,
    RebarMaterialProperties,
    ConcreteSection,
    ConcreteDesignForces,
    ConcreteDesignResults
)

from .ACI318_Extended import (
    ACIFoundations,
    ACISlabs,
    ACIDevelopment,
    FootingSection,
    SlabSection
)

# Import Phase 1 foundation if available
try:
    from ...utils.units_manager import get_units_manager
    from ...material import Material
    STRUCTURETOOLS_AVAILABLE = True
except ImportError:
    STRUCTURETOOLS_AVAILABLE = False


class ACI318Designer:
    """
    Main designer class providing simplified interface to ACI 318-19 design.
    
    This class acts as a facade to the detailed ACI 318-19 implementation,
    providing easy-to-use methods for common design tasks.
    """
    
    def __init__(self):
        """Initialize ACI 318-19 designer with all capabilities."""
        self.aci = ACI318()
        self.foundations = ACIFoundations()
        self.slabs = ACISlabs()
        self.development = ACIDevelopment()
        
        # Default materials
        self.default_concrete = ConcreteGrade.NORMAL_4000
        self.default_rebar = RebarGrade.GRADE_60
    
    def design_beam(self, width: float, height: float, span: float,
                   moment: float, shear: float = 0,
                   concrete_grade: ConcreteGrade = None,
                   rebar_grade: RebarGrade = None,
                   name: str = "Beam") -> ConcreteDesignResults:
        """
        Design concrete beam with flexural and shear reinforcement.
        
        Args:
            width: Beam width (in)
            height: Beam height (in)  
            span: Beam span (in)
            moment: Design moment (lb-in)
            shear: Design shear (lb)
            concrete_grade: Concrete grade (default: 4000 psi)
            rebar_grade: Rebar grade (default: Grade 60)
            name: Beam identifier
            
        Returns:
            ConcreteDesignResults with complete beam design
        """
        # Use defaults if not specified
        if concrete_grade is None:
            concrete_grade = self.default_concrete
        if rebar_grade is None:
            rebar_grade = self.default_rebar
        
        # Create section and materials
        section = ConcreteSection(
            name=name,
            b=width,
            h=height,
            d=height - 2.5,  # Assume 2.5" to centroid
            cover=1.5
        )
        
        concrete = self.aci.CONCRETE_PROPERTIES[concrete_grade]
        rebar = self.aci.REBAR_PROPERTIES[rebar_grade]
        
        # Design flexural reinforcement
        flexural_result = self.aci.design_flexural_member(section, concrete, rebar, moment)
        
        # Design shear reinforcement if shear provided
        if shear > 0:
            shear_result = self.aci.design_shear_reinforcement(section, concrete, rebar, shear)
            
            # Combine results
            flexural_result.capacity_checks.update(shear_result.capacity_checks)
            flexural_result.design_strengths.update(shear_result.design_strengths)
            flexural_result.reinforcement.update(shear_result.reinforcement)
            
            # Update overall status
            max_ratio = max(flexural_result.demand_capacity_ratio, shear_result.demand_capacity_ratio)
            flexural_result.demand_capacity_ratio = max_ratio
            flexural_result.passed = flexural_result.passed and shear_result.passed
            
            if shear_result.demand_capacity_ratio > flexural_result.demand_capacity_ratio:
                flexural_result.controlling_check = "shear"
            
            # Combine recommendations
            flexural_result.recommendations.extend(shear_result.recommendations)
        
        return flexural_result
    
    def design_column(self, width: float, height: float, length: float,
                     axial_load: float, moment: float = 0,
                     concrete_grade: ConcreteGrade = None,
                     rebar_grade: RebarGrade = None,
                     name: str = "Column") -> ConcreteDesignResults:
        """
        Design concrete column for axial load and moment.
        
        Args:
            width: Column width (in)
            height: Column height (in)
            length: Unsupported length (in)  
            axial_load: Design axial load (lb, compression positive)
            moment: Design moment (lb-in)
            concrete_grade: Concrete grade (default: 4000 psi)
            rebar_grade: Rebar grade (default: Grade 60)
            name: Column identifier
            
        Returns:
            ConcreteDesignResults with column design
        """
        # Use defaults if not specified
        if concrete_grade is None:
            concrete_grade = self.default_concrete
        if rebar_grade is None:
            rebar_grade = self.default_rebar
        
        # Create section and materials
        section = ConcreteSection(
            name=name,
            b=width,
            h=height,
            d=height - 2.5,  # Assume 2.5" to centroid
            cover=1.5
        )
        
        concrete = self.aci.CONCRETE_PROPERTIES[concrete_grade]
        rebar = self.aci.REBAR_PROPERTIES[rebar_grade]
        
        # Create design forces
        forces = ConcreteDesignForces(Pu=axial_load, Mux=moment)
        
        # Design column
        result = self.aci.design_column(section, concrete, rebar, forces, length)
        
        return result
    
    def design_footing(self, length: float, width: float, thickness: float,
                      column_size: Tuple[float, float], column_load: float,
                      soil_bearing: float,
                      concrete_grade: ConcreteGrade = None,
                      rebar_grade: RebarGrade = None,
                      name: str = "Footing") -> ConcreteDesignResults:
        """
        Design isolated spread footing.
        
        Args:
            length: Footing length (in)
            width: Footing width (in)
            thickness: Footing thickness (in)
            column_size: (length, width) of column (in)
            column_load: Column axial load (lb)
            soil_bearing: Allowable soil bearing pressure (psf)
            concrete_grade: Concrete grade (default: 3000 psi)
            rebar_grade: Rebar grade (default: Grade 60)
            name: Footing identifier
            
        Returns:
            ConcreteDesignResults with footing design
        """
        # Use defaults if not specified (lower strength for footings)
        if concrete_grade is None:
            concrete_grade = ConcreteGrade.NORMAL_3000
        if rebar_grade is None:
            rebar_grade = self.default_rebar
        
        # Create footing section and materials
        footing = FootingSection(
            name=name,
            L=length,
            W=width,
            t=thickness,
            column_L=column_size[0],
            column_W=column_size[1],
            cover=3.0,  # Increased cover for footings
            bar_diameter=0.75  # Default #6 bars
        )
        
        concrete = self.foundations.CONCRETE_PROPERTIES[concrete_grade]
        rebar = self.foundations.REBAR_PROPERTIES[rebar_grade]
        
        # Create design forces
        forces = ConcreteDesignForces(Pu=column_load)
        
        # Design footing
        result = self.foundations.design_isolated_footing(
            footing, concrete, rebar, forces, soil_bearing
        )
        
        return result
    
    def design_slab(self, length: float, width: float, thickness: float,
                   dead_load: float, live_load: float,
                   slab_type: str = "two_way",
                   concrete_grade: ConcreteGrade = None,
                   rebar_grade: RebarGrade = None,
                   name: str = "Slab") -> ConcreteDesignResults:
        """
        Design concrete slab (one-way or two-way).
        
        Args:
            length: Slab length/span (in)
            width: Slab width (in)
            thickness: Slab thickness (in)
            dead_load: Dead load (psf)
            live_load: Live load (psf)
            slab_type: "one_way" or "two_way"
            concrete_grade: Concrete grade (default: 4000 psi)
            rebar_grade: Rebar grade (default: Grade 60)
            name: Slab identifier
            
        Returns:
            ConcreteDesignResults with slab design
        """
        # Use defaults if not specified
        if concrete_grade is None:
            concrete_grade = self.default_concrete
        if rebar_grade is None:
            rebar_grade = self.default_rebar
        
        # Create slab section and materials
        slab = SlabSection(
            name=name,
            Lx=min(length, width),  # Short span
            Ly=max(length, width),  # Long span
            t=thickness,
            cover=0.75,  # Standard slab cover
            bar_diameter=0.5  # Default #4 bars
        )
        
        concrete = self.slabs.CONCRETE_PROPERTIES[concrete_grade]
        rebar = self.slabs.REBAR_PROPERTIES[rebar_grade]
        
        # Design based on type
        if slab_type.lower() == "one_way":
            result = self.slabs.design_one_way_slab(slab, concrete, rebar, dead_load, live_load)
        else:
            result = self.slabs.design_two_way_slab(slab, concrete, rebar, dead_load, live_load)
        
        return result
    
    def calculate_development_length(self, bar_size: int,
                                   concrete_grade: ConcreteGrade = None,
                                   rebar_grade: RebarGrade = None,
                                   tension: bool = True,
                                   top_bar: bool = False) -> float:
        """
        Calculate development length for reinforcing bars.
        
        Args:
            bar_size: Bar size number (3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18)
            concrete_grade: Concrete grade (default: 4000 psi)
            rebar_grade: Rebar grade (default: Grade 60)
            tension: True for tension, False for compression
            top_bar: True if top bar (requires increased development length)
            
        Returns:
            Development length (in)
        """
        # Use defaults if not specified
        if concrete_grade is None:
            concrete_grade = self.default_concrete
        if rebar_grade is None:
            rebar_grade = self.default_rebar
        
        # Convert bar size to diameter
        bar_diameter = bar_size / 8.0  # Bar size in eighths of inch
        
        concrete = self.development.CONCRETE_PROPERTIES[concrete_grade]
        rebar = self.development.REBAR_PROPERTIES[rebar_grade]
        
        if tension:
            # Modification factors
            modification_factors = {}
            if top_bar:
                modification_factors['top_bar_factor'] = 1.3
            if bar_size <= 6:
                modification_factors['size_factor'] = 0.8
            
            ld = self.development.calculate_development_length_tension(
                bar_diameter, concrete, rebar, modification_factors
            )
        else:
            ld = self.development.calculate_development_length_compression(
                bar_diameter, concrete, rebar
            )
        
        return ld
    
    def generate_design_report(self, results: List[ConcreteDesignResults],
                             project_name: str = "ACI 318-19 Design",
                             filepath: str = None) -> str:
        """
        Generate comprehensive design report for multiple members.
        
        Args:
            results: List of design results
            project_name: Project name for report header
            filepath: Optional file path to save report
            
        Returns:
            Report content as string
        """
        # Use the ACI report generator
        report = self.aci.generate_design_report(results, filepath)
        
        # Add project header
        header = f"""
{project_name}
ACI 318-19 CONCRETE DESIGN REPORT
Generated by StructureTools Phase 2
{"=" * 60}

"""
        
        full_report = header + report
        
        # Save to file if requested
        if filepath:
            with open(filepath, 'w') as f:
                f.write(full_report)
            print(f"Design report saved to: {filepath}")
        
        return full_report


# Convenience functions for quick design
def quick_beam_design(width: float, height: float, moment: float,
                     concrete_psi: float = 4000, rebar_fy: float = 60000) -> Dict:
    """Quick beam design with simplified inputs."""
    designer = ACI318Designer()
    
    # Map to standard grades
    concrete_grade = ConcreteGrade.NORMAL_4000 if concrete_psi <= 4000 else ConcreteGrade.NORMAL_5000
    rebar_grade = RebarGrade.GRADE_60 if rebar_fy <= 60000 else RebarGrade.GRADE_75
    
    result = designer.design_beam(width, height, 0, moment, 0, concrete_grade, rebar_grade)
    
    return {
        'passed': result.passed,
        'As_required': result.reinforcement.get('As_required', 0),
        'dc_ratio': result.demand_capacity_ratio,
        'recommendations': result.recommendations
    }


def quick_column_design(width: float, height: float, axial_load: float,
                       concrete_psi: float = 4000, rebar_fy: float = 60000) -> Dict:
    """Quick column design with simplified inputs."""
    designer = ACI318Designer()
    
    # Map to standard grades  
    concrete_grade = ConcreteGrade.NORMAL_4000 if concrete_psi <= 4000 else ConcreteGrade.NORMAL_5000
    rebar_grade = RebarGrade.GRADE_60 if rebar_fy <= 60000 else RebarGrade.GRADE_75
    
    result = designer.design_column(width, height, height*12, axial_load, 0, concrete_grade, rebar_grade)
    
    return {
        'passed': result.passed,
        'As_required': result.reinforcement.get('As_required', 0),
        'dc_ratio': result.demand_capacity_ratio,
        'recommendations': result.recommendations
    }


# Export main classes and functions
__all__ = [
    'ACI318Designer',
    'ACI318',
    'ACIFoundations', 
    'ACISlabs',
    'ACIDevelopment',
    'ConcreteGrade',
    'RebarGrade',
    'ConcreteMaterialProperties',
    'RebarMaterialProperties', 
    'ConcreteSection',
    'FootingSection',
    'SlabSection',
    'ConcreteDesignForces',
    'ConcreteDesignResults',
    'quick_beam_design',
    'quick_column_design'
]


# Module information
__version__ = "2.0.0"
__author__ = "StructureTools Phase 2 Development Team"
__description__ = "Professional ACI 318-19 concrete design implementation for StructureTools"


# Example usage
if __name__ == "__main__":
    print("ACI 318-19 Design Module for StructureTools Phase 2")
    print("=" * 55)
    print("")
    
    # Example beam design
    print("Example: Design 12x24 beam for 150 kip-in moment")
    beam_result = quick_beam_design(12, 24, 150000)
    print(f"Result: {'PASS' if beam_result['passed'] else 'FAIL'}")
    print(f"Required As: {beam_result['As_required']:.2f} in²")
    print(f"D/C Ratio: {beam_result['dc_ratio']:.3f}")
    print("")
    
    # Example column design
    print("Example: Design 16x16 column for 200 kip axial load")
    column_result = quick_column_design(16, 16, 200000)
    print(f"Result: {'PASS' if column_result['passed'] else 'FAIL'}")
    print(f"Required As: {column_result['As_required']:.2f} in²")
    print(f"D/C Ratio: {column_result['dc_ratio']:.3f}")
    print("")
    
    print("ACI 318-19 module ready for StructureTools integration!")
