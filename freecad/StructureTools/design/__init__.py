# -*- coding: utf-8 -*-
"""
StructureTools Phase 2 - Design Code Integration Module
=======================================================

This module provides comprehensive design code integration for StructureTools Phase 2,
implementing professional structural design capabilities per multiple international codes:

- AISC 360-16: Steel design per American Institute of Steel Construction
- ACI 318-19: Concrete design per American Concrete Institute  
- Eurocode 2: Design of concrete structures (planned)
- Eurocode 3: Design of steel structures (planned)

Key Features:
- Professional member design and analysis
- Code compliance checking and reporting
- Unified design interface across multiple codes
- Integration with Phase 1 structural models
- Comprehensive design reports

Usage:
    from freecad.StructureTools.design import SteelDesigner, ConcreteDesigner
    
    # Steel design
    steel_designer = SteelDesigner()
    result = steel_designer.design_beam(section, forces, code='AISC360')
    
    # Concrete design  
    concrete_designer = ConcreteDesigner()
    result = concrete_designer.design_beam(section, forces, code='ACI318')
"""

# Import Phase 1 foundation if available
try:
    from ..utils.units_manager import get_units_manager
    from ..material import Material
    STRUCTURETOOLS_AVAILABLE = True
except ImportError:
    STRUCTURETOOLS_AVAILABLE = False

# Add missing enums for design results
class DesignRatio:
    """Design ratio enumeration for code compliance"""
    PASS = "PASS"
    FAIL = "FAIL" 
    WARNING = "WARNING"

class LoadCombinationType:
    """Load combination types per various codes"""
    STRENGTH = "STRENGTH"
    SERVICE = "SERVICE"
    FACTORED = "FACTORED"
    SEISMIC = "SEISMIC"

class MemberType:
    """Structural member type classification"""
    BEAM = "BEAM"
    COLUMN = "COLUMN"
    BRACE = "BRACE"
    PLATE = "PLATE"

# Import design code implementations with graceful degradation
try:
    from .aisc import (
        AISC360, SteelMaterialProperties, SectionProperties, 
        SteelDesignForces, SteelDesignResults
    )
    AISC_AVAILABLE = True
except ImportError:
    AISC_AVAILABLE = False
    # Mock classes for graceful degradation

# Try importing from individual AISC360.py file
try:
    from .AISC360 import AISC360DesignCode
    # Create alias for compatibility
    AISC360_Calculator = AISC360DesignCode
    AISC360_AVAILABLE_DIRECT = True
except ImportError:
    AISC360_AVAILABLE_DIRECT = False
    # Create mock class
    class AISC360_Calculator:
        def __init__(self, **kwargs):
            pass
        def design_beam(self, *args, **kwargs):
            return {"status": "mock", "message": "AISC360 not available"}
        def design_column(self, *args, **kwargs):
            return {"status": "mock", "message": "AISC360 not available"}

if not AISC_AVAILABLE:
    # Mock classes for graceful degradation
    class AISC360:
        def __init__(self):
            pass
    
    class SteelMaterialProperties:
        def __init__(self):
            self.Fy = 50000  # psi
            self.Fu = 65000  # psi
    
    class SectionProperties:
        def __init__(self):
            self.A = 1.0
            self.Ix = 1.0
            self.Sx = 1.0
    
    class SteelDesignForces:
        def __init__(self):
            self.Pu = 0.0
            self.Mux = 0.0
    
    class SteelDesignResults:
        def __init__(self):
            self.DCR = 1.0

try:
    from .aci import (
        ACI318Designer, ConcreteMaterialProperties,
        RebarMaterialProperties, ConcreteSection, ConcreteDesignForces,
        ConcreteDesignResults, quick_beam_design, quick_column_design
    )
    ACI_AVAILABLE = True
except ImportError:
    ACI_AVAILABLE = False
    # Mock classes for graceful degradation
    class ACI318Designer:
        def __init__(self):
            pass
    
    class ConcreteMaterialProperties:
        def __init__(self):
            self.fc = 4000  # psi
    
    class RebarMaterialProperties:
        def __init__(self):
            self.fy = 60000  # psi
    
    class ConcreteSection:
        def __init__(self):
            self.width = 12.0
            self.height = 24.0
    
    class ConcreteDesignForces:
        def __init__(self):
            self.Pu = 0.0
            self.Mux = 0.0
    
    class ConcreteDesignResults:
        def __init__(self):
            self.DCR = 1.0
    
    def quick_beam_design(*args, **kwargs):
        return ConcreteDesignResults()
    
    def quick_column_design(*args, **kwargs):
        return ConcreteDesignResults()

from typing import Dict, List, Tuple, Optional, Any, Union
from enum import Enum
from dataclasses import dataclass


class DesignCode(Enum):
    """Supported design codes"""
    AISC_360_16 = "AISC_360_16"
    ACI_318_19 = "ACI_318_19"
    EUROCODE_2 = "EUROCODE_2"  # Future
    EUROCODE_3 = "EUROCODE_3"  # Future


class SteelGrade(Enum):
    """Steel material grades for fallback"""
    A992 = "A992"
    A36 = "A36"
    A572_50 = "A572_50"


class ConcreteGrade(Enum):
    """Concrete grades for fallback"""
    NORMAL_3000 = "3000_psi"
    NORMAL_4000 = "4000_psi"
    NORMAL_5000 = "5000_psi"


class RebarGrade(Enum):
    """Rebar grades for fallback"""
    GRADE_40 = "Grade_40"
    GRADE_60 = "Grade_60"


@dataclass
class UnifiedDesignForces:
    """Unified design forces for both steel and concrete"""
    # Axial forces
    Pu: float = 0.0          # Factored axial load (lb, compression positive)
    Pr: float = 0.0          # Required axial strength
    
    # Moments
    Mux: float = 0.0         # Factored moment about x-axis (lb-in)
    Muy: float = 0.0         # Factored moment about y-axis (lb-in)
    Mrx: float = 0.0         # Required moment strength about x-axis
    Mry: float = 0.0         # Required moment strength about y-axis
    
    # Shear
    Vux: float = 0.0         # Factored shear about x-axis (lb)
    Vuy: float = 0.0         # Factored shear about y-axis (lb)
    Vrx: float = 0.0         # Required shear strength about x-axis
    Vry: float = 0.0         # Required shear strength about y-axis
    
    # Torsion
    Tu: float = 0.0          # Factored torsion (lb-in)
    Tr: float = 0.0          # Required torsional strength


@dataclass
class UnifiedDesignResults:
    """Unified design results format"""
    member_id: str
    design_code: DesignCode
    member_type: str         # beam, column, brace, slab, footing, etc.
    passed: bool
    controlling_check: str
    demand_capacity_ratio: float
    capacity_checks: Dict[str, float]
    design_strengths: Dict[str, float]
    material_properties: Dict[str, Any]
    section_properties: Dict[str, Any]
    recommendations: List[str]
    code_references: List[str]


class SteelDesigner:
    """
    Unified steel design interface supporting multiple steel design codes.
    
    Currently implements:
    - AISC 360-16 (complete)
    
    Planned:
    - Eurocode 3 (Phase 2 extension)
    """
    
    def __init__(self, design_code: DesignCode = DesignCode.AISC_360_16):
        """Initialize steel designer with specified code."""
        self.design_code = design_code
        
        if design_code == DesignCode.AISC_360_16:
            self.engine = AISC360()
        else:
            raise NotImplementedError(f"Design code {design_code} not yet implemented")
    
    def design_beam(self, section_name: str, forces: UnifiedDesignForces,
                   material_grade: SteelGrade = SteelGrade.A992,
                   member_id: str = "Steel_Beam") -> UnifiedDesignResults:
        """
        Design steel beam per selected design code.
        
        Args:
            section_name: Section designation (e.g., "W18X50")
            forces: Design forces
            material_grade: Steel material grade
            member_id: Member identifier
            
        Returns:
            UnifiedDesignResults with beam design results
        """
        # Convert to AISC format
        aisc_forces = SteelDesignForces(
            Pr=forces.Pr or forces.Pu,
            Mrx=forces.Mrx or forces.Mux,
            Mry=forces.Mry or forces.Muy,
            Vrx=forces.Vrx or forces.Vux,
            Vry=forces.Vry or forces.Vuy,
            Tr=forces.Tr or forces.Tu
        )
        
        # Get section properties
        section_props = self.engine.get_section_properties(section_name)
        if not section_props:
            # Create empty result for unknown section
            return UnifiedDesignResults(
                member_id=member_id,
                design_code=self.design_code,
                member_type="beam",
                passed=False,
                controlling_check="section_not_found",
                demand_capacity_ratio=float('inf'),
                capacity_checks={},
                design_strengths={},
                material_properties={},
                section_properties={},
                recommendations=[f"Section {section_name} not found in database"],
                code_references=[]
            )
        
        # Get material properties
        material_props = self.engine.STEEL_PROPERTIES[material_grade]
        
        # Perform design
        aisc_result = self.engine.design_member(section_props, material_props, aisc_forces)
        
        # Convert to unified format
        unified_result = self._convert_aisc_to_unified(aisc_result, "beam")
        return unified_result
    
    def design_column(self, section_name: str, forces: UnifiedDesignForces,
                     unbraced_length: float,
                     material_grade: SteelGrade = SteelGrade.A992,
                     member_id: str = "Steel_Column") -> UnifiedDesignResults:
        """
        Design steel column per selected design code.
        
        Args:
            section_name: Section designation (e.g., "W14X82")
            forces: Design forces
            unbraced_length: Unbraced length (in)
            material_grade: Steel material grade
            member_id: Member identifier
            
        Returns:
            UnifiedDesignResults with column design results
        """
        # Convert to AISC format
        aisc_forces = SteelDesignForces(
            Pr=forces.Pr or forces.Pu,
            Mrx=forces.Mrx or forces.Mux,
            Mry=forces.Mry or forces.Muy
        )
        
        # Get section and material properties
        section_props = self.engine.get_section_properties(section_name)
        material_props = self.engine.STEEL_PROPERTIES[material_grade]
        
        # Set unbraced length
        if section_props:
            section_props.Lb = unbraced_length
        
        # Perform design
        aisc_result = self.engine.design_member(section_props, material_props, aisc_forces)
        
        # Convert to unified format
        unified_result = self._convert_aisc_to_unified(aisc_result, "column")
        return unified_result
    
    def _convert_aisc_to_unified(self, aisc_result: SteelDesignResults,
                                member_type: str) -> UnifiedDesignResults:
        """Convert AISC results to unified format."""
        return UnifiedDesignResults(
            member_id=aisc_result.member_id,
            design_code=self.design_code,
            member_type=member_type,
            passed=aisc_result.passed,
            controlling_check=aisc_result.controlling_check,
            demand_capacity_ratio=aisc_result.demand_capacity_ratio,
            capacity_checks=aisc_result.capacity_checks,
            design_strengths=aisc_result.design_strengths,
            material_properties=aisc_result.material_properties,
            section_properties=aisc_result.section_properties,
            recommendations=aisc_result.recommendations,
            code_references=aisc_result.code_references
        )


class ConcreteDesigner:
    """
    Unified concrete design interface supporting multiple concrete design codes.
    
    Currently implements:
    - ACI 318-19 (complete)
    
    Planned:
    - Eurocode 2 (Phase 2 extension)
    """
    
    def __init__(self, design_code: DesignCode = DesignCode.ACI_318_19):
        """Initialize concrete designer with specified code."""
        self.design_code = design_code
        
        if design_code == DesignCode.ACI_318_19:
            self.engine = ACI318Designer()
        else:
            raise NotImplementedError(f"Design code {design_code} not yet implemented")
    
    def design_beam(self, width: float, height: float, forces: UnifiedDesignForces,
                   concrete_grade: ConcreteGrade = ConcreteGrade.NORMAL_4000,
                   rebar_grade: RebarGrade = RebarGrade.GRADE_60,
                   member_id: str = "Concrete_Beam") -> UnifiedDesignResults:
        """
        Design concrete beam per selected design code.
        
        Args:
            width: Beam width (in)
            height: Beam height (in)
            forces: Design forces
            concrete_grade: Concrete grade
            rebar_grade: Rebar grade
            member_id: Member identifier
            
        Returns:
            UnifiedDesignResults with beam design results
        """
        # Extract moment and shear
        moment = forces.Mux or forces.Mrx
        shear = forces.Vux or forces.Vrx
        
        # Perform design
        aci_result = self.engine.design_beam(
            width, height, 0, moment, shear, 
            concrete_grade, rebar_grade, member_id
        )
        
        # Convert to unified format
        unified_result = self._convert_aci_to_unified(aci_result, "beam")
        return unified_result
    
    def design_column(self, width: float, height: float, forces: UnifiedDesignForces,
                     unbraced_length: float,
                     concrete_grade: ConcreteGrade = ConcreteGrade.NORMAL_4000,
                     rebar_grade: RebarGrade = RebarGrade.GRADE_60,
                     member_id: str = "Concrete_Column") -> UnifiedDesignResults:
        """
        Design concrete column per selected design code.
        
        Args:
            width: Column width (in)
            height: Column height (in)
            forces: Design forces
            unbraced_length: Unbraced length (in)
            concrete_grade: Concrete grade
            rebar_grade: Rebar grade
            member_id: Member identifier
            
        Returns:
            UnifiedDesignResults with column design results
        """
        # Extract axial load and moment
        axial_load = forces.Pu or forces.Pr
        moment = forces.Mux or forces.Mrx
        
        # Perform design
        aci_result = self.engine.design_column(
            width, height, unbraced_length, axial_load, moment,
            concrete_grade, rebar_grade, member_id
        )
        
        # Convert to unified format
        unified_result = self._convert_aci_to_unified(aci_result, "column")
        return unified_result
    
    def design_footing(self, length: float, width: float, thickness: float,
                      column_size: Tuple[float, float], forces: UnifiedDesignForces,
                      soil_bearing: float,
                      concrete_grade: ConcreteGrade = ConcreteGrade.NORMAL_3000,
                      rebar_grade: RebarGrade = RebarGrade.GRADE_60,
                      member_id: str = "Footing") -> UnifiedDesignResults:
        """
        Design concrete footing per selected design code.
        
        Args:
            length: Footing length (in)
            width: Footing width (in)
            thickness: Footing thickness (in)
            column_size: (length, width) of column (in)
            forces: Design forces
            soil_bearing: Allowable soil bearing pressure (psf)
            concrete_grade: Concrete grade
            rebar_grade: Rebar grade
            member_id: Member identifier
            
        Returns:
            UnifiedDesignResults with footing design results
        """
        # Extract column load
        column_load = forces.Pu or forces.Pr
        
        # Perform design
        aci_result = self.engine.design_footing(
            length, width, thickness, column_size, column_load, soil_bearing,
            concrete_grade, rebar_grade, member_id
        )
        
        # Convert to unified format
        unified_result = self._convert_aci_to_unified(aci_result, "footing")
        return unified_result
    
    def _convert_aci_to_unified(self, aci_result: ConcreteDesignResults,
                               member_type: str) -> UnifiedDesignResults:
        """Convert ACI results to unified format."""
        return UnifiedDesignResults(
            member_id=aci_result.member_id,
            design_code=self.design_code,
            member_type=member_type,
            passed=aci_result.passed,
            controlling_check=aci_result.controlling_check,
            demand_capacity_ratio=aci_result.demand_capacity_ratio,
            capacity_checks=aci_result.capacity_checks,
            design_strengths=aci_result.design_strengths,
            material_properties={},  # Would be populated from concrete/rebar properties
            section_properties=aci_result.reinforcement,
            recommendations=aci_result.recommendations,
            code_references=[]  # Would be populated with ACI section references
        )


class UnifiedDesigner:
    """
    Master design interface supporting both steel and concrete design
    with automatic material detection and code selection.
    """
    
    def __init__(self):
        """Initialize unified designer with default codes."""
        self.steel_designer = SteelDesigner(DesignCode.AISC_360_16)
        self.concrete_designer = ConcreteDesigner(DesignCode.ACI_318_19)
    
    def design_member(self, member_type: str, material_type: str,
                     **kwargs) -> UnifiedDesignResults:
        """
        Design member with automatic code selection based on material.
        
        Args:
            member_type: "beam", "column", "brace", "footing", etc.
            material_type: "steel" or "concrete"
            **kwargs: Design parameters specific to member and material type
            
        Returns:
            UnifiedDesignResults with design results
        """
        if material_type.lower() == "steel":
            if member_type.lower() == "beam":
                return self.steel_designer.design_beam(**kwargs)
            elif member_type.lower() == "column":
                return self.steel_designer.design_column(**kwargs)
            else:
                raise ValueError(f"Steel {member_type} design not implemented")
                
        elif material_type.lower() == "concrete":
            if member_type.lower() == "beam":
                return self.concrete_designer.design_beam(**kwargs)
            elif member_type.lower() == "column":
                return self.concrete_designer.design_column(**kwargs)
            elif member_type.lower() == "footing":
                return self.concrete_designer.design_footing(**kwargs)
            else:
                raise ValueError(f"Concrete {member_type} design not implemented")
                
        else:
            raise ValueError(f"Material type {material_type} not supported")
    
    def generate_unified_report(self, results: List[UnifiedDesignResults],
                               project_name: str = "StructureTools Design Report",
                               filepath: str = None) -> str:
        """
        Generate comprehensive design report for multiple members and codes.
        
        Args:
            results: List of unified design results
            project_name: Project name
            filepath: Optional file path to save report
            
        Returns:
            Report content as string
        """
        report_lines = [
            f"{project_name}",
            "STRUCTURAL DESIGN REPORT - StructureTools Phase 2",
            "=" * 70,
            "",
            f"Design Codes Used:",
        ]
        
        # List unique codes used
        codes_used = set(result.design_code.value for result in results)
        for code in sorted(codes_used):
            report_lines.append(f"  - {code}")
        
        report_lines.extend([
            "",
            f"Number of Members Analyzed: {len(results)}",
            "",
            "DESIGN SUMMARY",
            "-" * 50,
            f"{'Member':<15} {'Type':<10} {'Material':<10} {'Code':<12} {'Status':<8} {'D/C':<8} {'Control':<15}",
            "-" * 88
        ])
        
        # Add member summary
        for result in results:
            status = "PASS" if result.passed else "FAIL"
            material = "Steel" if "AISC" in result.design_code.value else "Concrete"
            code = result.design_code.value.replace("_", " ")
            
            report_lines.append(
                f"{result.member_id:<15} {result.member_type:<10} {material:<10} "
                f"{code:<12} {status:<8} {result.demand_capacity_ratio:<8.3f} {result.controlling_check:<15}"
            )
        
        # Add detailed results
        report_lines.extend([
            "",
            "DETAILED DESIGN RESULTS",
            "-" * 30
        ])
        
        for result in results:
            report_lines.extend([
                "",
                f"Member: {result.member_id}",
                f"Type: {result.member_type.title()}",
                f"Design Code: {result.design_code.value.replace('_', ' ')}",
                f"Status: {'PASS' if result.passed else 'FAIL'}",
                f"Controlling Check: {result.controlling_check}",
                f"Overall D/C Ratio: {result.demand_capacity_ratio:.3f}",
                ""
            ])
            
            # Add capacity checks
            if result.capacity_checks:
                report_lines.append("Capacity Checks:")
                for check, ratio in result.capacity_checks.items():
                    report_lines.append(f"  {check}: {ratio:.3f}")
                report_lines.append("")
            
            # Add recommendations
            if result.recommendations:
                report_lines.append("Recommendations:")
                for rec in result.recommendations:
                    report_lines.append(f"  - {rec}")
                report_lines.append("")
        
        report_content = "\n".join(report_lines)
        
        # Save to file if requested
        if filepath:
            with open(filepath, 'w') as f:
                f.write(report_content)
            print(f"Unified design report saved to: {filepath}")
        
        return report_content


# Export main classes and functions
__all__ = [
    'SteelDesigner',
    'ConcreteDesigner', 
    'UnifiedDesigner',
    'DesignCode',
    'UnifiedDesignForces',
    'UnifiedDesignResults',
    # Steel design exports
    'AISC360',
    'AISC360_Calculator',  # Added for compatibility
    'AISC360DesignCode',   # Direct import from AISC360.py
    'SteelGrade',
    'SteelMaterialProperties',
    'SectionProperties',
    'SteelDesignForces',
    'SteelDesignResults',
    # Design enums and types
    'DesignRatio',
    'LoadCombinationType',
    'MemberType',
    # Concrete design exports
    'ACI318Designer',
    'ConcreteGrade',
    'RebarGrade',
    'ConcreteMaterialProperties',
    'RebarMaterialProperties',
    'ConcreteSection',
    'ConcreteDesignForces',
    'ConcreteDesignResults',
    'quick_beam_design',
    'quick_column_design'
]


# Module information
__version__ = "2.0.0"
__author__ = "StructureTools Phase 2 Development Team"
__description__ = "Comprehensive design code integration for professional structural design"


# Example usage
if __name__ == "__main__":
    print("StructureTools Phase 2 - Design Code Integration Module")
    print("=" * 60)
    print("")
    
    # Create unified designer
    designer = UnifiedDesigner()
    
    # Example steel beam design
    print("Example 1: Steel beam design (W18X50, AISC 360-16)")
    steel_forces = UnifiedDesignForces(Mux=3000000)  # 3000 kip-in
    steel_result = designer.design_member(
        "beam", "steel",
        section_name="W18X50",
        forces=steel_forces,
        member_id="B1"
    )
    print(f"Result: {'PASS' if steel_result.passed else 'FAIL'}")
    print(f"D/C Ratio: {steel_result.demand_capacity_ratio:.3f}")
    print("")
    
    # Example concrete beam design
    print("Example 2: Concrete beam design (12x24, ACI 318-19)")
    concrete_forces = UnifiedDesignForces(Mux=150000)  # 150 kip-in
    concrete_result = designer.design_member(
        "beam", "concrete",
        width=12, height=24,
        forces=concrete_forces,
        member_id="CB1"
    )
    print(f"Result: {'PASS' if concrete_result.passed else 'FAIL'}")
    print(f"D/C Ratio: {concrete_result.demand_capacity_ratio:.3f}")
    print("")
    
    # Generate unified report
    results = [steel_result, concrete_result]
    report = designer.generate_unified_report(results, "Phase 2 Example Design")
    print("Unified design report generated successfully!")
    print("")
    print("Design Code Integration Module ready for StructureTools Phase 2!")
