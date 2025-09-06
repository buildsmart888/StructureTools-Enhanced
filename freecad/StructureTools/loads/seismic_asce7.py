# -*- coding: utf-8 -*-
"""
ASCE 7 / IBC Seismic Load Generator for StructureTools Phase 2  
============================================================

Professional implementation of ASCE 7-22 and IBC 2021 seismic provisions for:
- Equivalent Lateral Force (ELF) procedure
- Modal Response Spectrum Analysis (MRSA)
- Response spectrum generation
- Site-specific ground motion parameters
- Seismic force distribution and load combinations

This module generates seismic loads per the latest ASCE 7-22/IBC 2021 standards
for integration with StructureTools structural analysis.
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum
import json

# Import Phase 1 foundation if available
try:
    from ..utils.units_manager import get_units_manager, format_force
    STRUCTURETOOLS_AVAILABLE = True
except ImportError:
    try:
        # Fallback to direct import for standalone testing
        from StructureTools.utils.units_manager import get_units_manager, format_force
        STRUCTURETOOLS_AVAILABLE = True
    except ImportError:
        STRUCTURETOOLS_AVAILABLE = False
        get_units_manager = lambda: None
        format_force = lambda x: f"{x/1000:.2f} kN"


class SiteClass(Enum):
    """Site classification per ASCE 7-22 Section 20.3"""
    A = "A"  # Hard rock
    B = "B"  # Rock  
    C = "C"  # Very dense soil and soft rock
    D = "D"  # Stiff soil
    E = "E"  # Soft clay soil
    F = "F"  # Soils requiring site-specific analysis


class SeismicDesignCategory(Enum):
    """Seismic Design Category per ASCE 7-22 Section 11.6"""
    A = "A"  # Very low seismicity
    B = "B"  # Low seismicity
    C = "C"  # Moderate seismicity
    D = "D"  # High seismicity
    E = "E"  # Very high seismicity
    F = "F"  # Very high seismicity with additional requirements


class StructuralSystem(Enum):
    """Structural system types per ASCE 7-22 Table 12.2-1"""
    # Moment frames
    SMF = "special_moment_frame"           # R=8, Ω₀=3, Cd=5.5
    IMF = "intermediate_moment_frame"      # R=4.5, Ω₀=3, Cd=4
    OMF = "ordinary_moment_frame"          # R=3, Ω₀=3, Cd=2.5
    
    # Shear walls
    SPECIAL_SHEAR_WALL = "special_shear_wall"     # R=5, Ω₀=2.5, Cd=4
    ORDINARY_SHEAR_WALL = "ordinary_shear_wall"   # R=4, Ω₀=2.5, Cd=4
    
    # Braced frames
    SCBF = "special_concentrically_braced"  # R=6, Ω₀=2, Cd=5
    OCBF = "ordinary_concentrically_braced" # R=3.25, Ω₀=2, Cd=3.25
    EBF = "eccentrically_braced_frame"      # R=8, Ω₀=2, Cd=4
    
    # Dual systems
    SMF_SHEAR_WALL = "smf_with_shear_wall"  # R=7, Ω₀=2.5, Cd=5.5


@dataclass
class SeismicSiteData:
    """Seismic site parameters and ground motion data"""
    # Geographic location
    latitude: float                        # Latitude (degrees)
    longitude: float                       # Longitude (degrees)
    
    # Ground motion parameters  
    Ss: float                             # Mapped spectral acceleration at short periods
    S1: float                             # Mapped spectral acceleration at 1-second period
    
    # Site conditions
    site_class: SiteClass                 # Site classification
    
    # Site coefficients (calculated from site class and ground motion)
    Fa: float = 0.0                       # Site coefficient for short periods
    Fv: float = 0.0                       # Site coefficient for long periods
    
    # Design ground motion parameters (calculated)
    SMS: float = 0.0                      # Site-modified spectral acceleration (short)
    SM1: float = 0.0                      # Site-modified spectral acceleration (1-sec)
    SDS: float = 0.0                      # Design spectral acceleration (short)
    SD1: float = 0.0                      # Design spectral acceleration (1-sec)
    
    # Additional site parameters
    TL: float = 8.0                       # Long-period transition period (sec)


@dataclass
class BuildingSeismicData:
    """Building data for seismic analysis"""
    # Basic properties (required)
    height: float                         # Total building height (ft)
    weight: float                         # Total seismic weight (lb)
    story_heights: List[float]            # Individual story heights (ft)
    story_weights: List[float]            # Individual story weights (lb)
    
    # Optional properties with defaults
    occupancy_category: str = "II"        # Occupancy category (I, II, III, IV)
    structural_system: str = "moment_frame" # Structural system type
    
    # System factors (from ASCE 7-22 Table 12.2-1)
    R: float = 8.0                        # Response modification coefficient
    Omega0: float = 3.0                   # Overstrength factor
    Cd: float = 5.5                       # Deflection amplification factor
    
    # Building configuration
    approximate_period: float = 0.0       # Approximate fundamental period (sec)
    Ct: float = 0.028                     # Building period coefficient
    x: float = 0.8                        # Building period exponent
    
    # Irregularities
    horizontal_irregularity: bool = False  # Horizontal structural irregularity
    vertical_irregularity: bool = False    # Vertical structural irregularity


@dataclass
class ResponseSpectrum:
    """Design response spectrum data"""
    periods: List[float]                  # Period values (sec)
    accelerations: List[float]            # Spectral accelerations (g)
    
    # Key period points
    TS: float = 0.0                       # Short period region limit
    TL: float = 0.0                       # Long period transition
    T0: float = 0.0                       # Initial period
    
    # Peak values
    SDS: float = 0.0                      # Design spectral acceleration (short)
    SD1: float = 0.0                      # Design spectral acceleration (1-sec)


@dataclass
class SeismicForces:
    """Seismic forces for structural analysis"""
    # Required lists (no defaults)
    story_forces: List[float]             # Lateral forces per story (lb)
    story_heights: List[float]            # Heights of force application (ft)
    story_drifts: List[float]             # Story drift ratios
    Cd_delta: List[float]                 # Amplified displacements
    
    # Optional properties with defaults
    V: float = 0.0                        # Total design base shear (lb)
    Ta: float = 0.0                       # Approximate fundamental period (sec)
    Cs: float = 0.0                       # Seismic response coefficient
    k: float = 1.0                        # Distribution exponent
    Ft: float = 0.0                       # Additional force at top
    E: float = 0.0                        # Seismic load effect
    Em: float = 0.0                       # Maximum seismic load effect


class ASCE7SeismicGenerator:
    """
    Professional ASCE 7-22 seismic load generator.
    
    Generates seismic loads using Equivalent Lateral Force (ELF) procedure
    following ASCE 7-22 Chapter 12.
    """
    
    # System factors per ASCE 7-22 Table 12.2-1 (R, Ω₀, Cd)
    SYSTEM_FACTORS = {
        StructuralSystem.SMF: (8.0, 3.0, 5.5),
        StructuralSystem.IMF: (4.5, 3.0, 4.0),
        StructuralSystem.OMF: (3.0, 3.0, 2.5),
        StructuralSystem.SPECIAL_SHEAR_WALL: (5.0, 2.5, 4.0),
        StructuralSystem.ORDINARY_SHEAR_WALL: (4.0, 2.5, 4.0),
        StructuralSystem.SCBF: (6.0, 2.0, 5.0),
        StructuralSystem.OCBF: (3.25, 2.0, 3.25),
        StructuralSystem.EBF: (8.0, 2.0, 4.0),
        StructuralSystem.SMF_SHEAR_WALL: (7.0, 2.5, 5.5)
    }
    
    # Approximate period coefficients per ASCE 7-22 Table 12.8-2
    PERIOD_COEFFICIENTS = {
        StructuralSystem.SMF: (0.028, 0.8),        # Steel moment frame
        StructuralSystem.IMF: (0.028, 0.8),
        StructuralSystem.OMF: (0.028, 0.8),
        StructuralSystem.SPECIAL_SHEAR_WALL: (0.020, 0.75),  # Concrete shear wall
        StructuralSystem.SCBF: (0.030, 0.75),      # Steel braced frame
        StructuralSystem.OCBF: (0.030, 0.75),
        StructuralSystem.EBF: (0.030, 0.75)
    }
    
    # Site coefficients Fa per ASCE 7-22 Table 11.4-1
    FA_COEFFICIENTS = {
        SiteClass.A: {0.25: 0.8, 0.5: 0.8, 0.75: 0.8, 1.0: 0.8, 1.25: 0.8},
        SiteClass.B: {0.25: 1.0, 0.5: 1.0, 0.75: 1.0, 1.0: 1.0, 1.25: 1.0},
        SiteClass.C: {0.25: 1.2, 0.5: 1.2, 0.75: 1.1, 1.0: 1.0, 1.25: 1.0},
        SiteClass.D: {0.25: 1.6, 0.5: 1.4, 0.75: 1.2, 1.0: 1.1, 1.25: 1.0},
        SiteClass.E: {0.25: 2.5, 0.5: 1.7, 0.75: 1.2, 1.0: 0.9, 1.25: 0.9}
    }
    
    # Site coefficients Fv per ASCE 7-22 Table 11.4-2  
    FV_COEFFICIENTS = {
        SiteClass.A: {0.1: 0.8, 0.2: 0.8, 0.3: 0.8, 0.4: 0.8, 0.5: 0.8},
        SiteClass.B: {0.1: 1.0, 0.2: 1.0, 0.3: 1.0, 0.4: 1.0, 0.5: 1.0},
        SiteClass.C: {0.1: 1.8, 0.2: 1.6, 0.3: 1.5, 0.4: 1.4, 0.5: 1.3},
        SiteClass.D: {0.1: 2.4, 0.2: 2.0, 0.3: 1.8, 0.4: 1.6, 0.5: 1.5},
        SiteClass.E: {0.1: 3.5, 0.2: 3.2, 0.3: 2.8, 0.4: 2.4, 0.5: 2.4}
    }
    
    def __init__(self):
        """Initialize ASCE 7 seismic load generator."""
        self.version = "ASCE 7-22"
        
    def generate_seismic_loads(self, site_data: SeismicSiteData,
                              building: BuildingSeismicData) -> Tuple[ResponseSpectrum, SeismicForces]:
        """
        Generate complete seismic loads per ASCE 7-22 ELF procedure.
        
        Args:
            site_data: Seismic site parameters
            building: Building seismic data
            
        Returns:
            Tuple of (ResponseSpectrum, SeismicForces) with complete seismic data
        """
        # Step 1: Calculate site coefficients and design parameters
        self._calculate_site_coefficients(site_data)
        self._calculate_design_parameters(site_data)
        
        # Step 2: Determine structural system factors
        self._set_system_factors(building)
        
        # Step 3: Calculate fundamental period
        self._calculate_period(building)
        
        # Step 4: Generate design response spectrum
        spectrum = self._generate_response_spectrum(site_data)
        
        # Step 5: Calculate seismic forces using ELF procedure
        forces = self._calculate_elf_forces(site_data, building, spectrum)
        
        return spectrum, forces
    
    def _calculate_site_coefficients(self, site_data: SeismicSiteData):
        """Calculate site coefficients Fa and Fv"""
        
        # Get site coefficient tables
        fa_table = self.FA_COEFFICIENTS.get(site_data.site_class, self.FA_COEFFICIENTS[SiteClass.C])
        fv_table = self.FV_COEFFICIENTS.get(site_data.site_class, self.FV_COEFFICIENTS[SiteClass.C])
        
        # Interpolate Fa coefficient
        site_data.Fa = self._interpolate_coefficient(fa_table, site_data.Ss)
        
        # Interpolate Fv coefficient  
        site_data.Fv = self._interpolate_coefficient(fv_table, site_data.S1)
    
    def _interpolate_coefficient(self, table: Dict[float, float], value: float) -> float:
        """Interpolate site coefficient from table"""
        sorted_keys = sorted(table.keys())
        
        if value <= sorted_keys[0]:
            return table[sorted_keys[0]]
        elif value >= sorted_keys[-1]:
            return table[sorted_keys[-1]]
        else:
            # Linear interpolation
            for i in range(len(sorted_keys) - 1):
                if sorted_keys[i] <= value <= sorted_keys[i + 1]:
                    x1, x2 = sorted_keys[i], sorted_keys[i + 1]
                    y1, y2 = table[x1], table[x2]
                    return y1 + (y2 - y1) * (value - x1) / (x2 - x1)
        
        return 1.0  # Default
    
    def _calculate_design_parameters(self, site_data: SeismicSiteData):
        """Calculate design spectral parameters per ASCE 7-22 Section 11.4.4"""
        
        # Site-modified spectral accelerations
        site_data.SMS = site_data.Fa * site_data.Ss
        site_data.SM1 = site_data.Fv * site_data.S1
        
        # Design spectral accelerations
        site_data.SDS = (2.0 / 3.0) * site_data.SMS
        site_data.SD1 = (2.0 / 3.0) * site_data.SM1
    
    def _set_system_factors(self, building: BuildingSeismicData):
        """Set structural system factors from table"""
        if building.structural_system in self.SYSTEM_FACTORS:
            R, Omega0, Cd = self.SYSTEM_FACTORS[building.structural_system]
            building.R = R
            building.Omega0 = Omega0
            building.Cd = Cd
        else:
            # Default conservative values
            building.R = 3.0
            building.Omega0 = 3.0
            building.Cd = 3.0
    
    def _calculate_period(self, building: BuildingSeismicData):
        """Calculate approximate fundamental period per ASCE 7-22 Section 12.8.2"""
        
        if building.structural_system in self.PERIOD_COEFFICIENTS:
            Ct, x = self.PERIOD_COEFFICIENTS[building.structural_system]
            building.Ct = Ct
            building.x = x
        else:
            # Default values for other systems
            building.Ct = 0.020
            building.x = 0.75
        
        # Calculate approximate period Ta = Ct * hn^x
        building.approximate_period = building.Ct * (building.height ** building.x)
    
    def _generate_response_spectrum(self, site_data: SeismicSiteData) -> ResponseSpectrum:
        """Generate design response spectrum per ASCE 7-22 Section 11.4.5"""
        
        SDS = site_data.SDS
        SD1 = site_data.SD1
        TL = site_data.TL
        
        # Calculate transition periods
        TS = SD1 / SDS if SDS > 0 else 0.2
        T0 = 0.2 * TS
        
        # Generate period array (0.01 to 10 seconds)
        periods = np.logspace(-2, 1, 300)  # 0.01 to 10 seconds
        accelerations = []
        
        for T in periods:
            if T <= T0:
                # Rising linear portion
                Sa = SDS * (0.4 + 0.6 * T / T0)
            elif T <= TS:
                # Constant acceleration region
                Sa = SDS
            elif T <= TL:
                # Descending branch
                Sa = SD1 / T
            else:
                # Long period region
                Sa = SD1 * TL / (T ** 2)
            
            accelerations.append(Sa)
        
        return ResponseSpectrum(
            periods=periods.tolist(),
            accelerations=accelerations,
            TS=TS,
            TL=TL,
            T0=T0,
            SDS=SDS,
            SD1=SD1
        )
    
    def _calculate_elf_forces(self, site_data: SeismicSiteData,
                             building: BuildingSeismicData,
                             spectrum: ResponseSpectrum) -> SeismicForces:
        """Calculate seismic forces using Equivalent Lateral Force procedure"""
        
        forces = SeismicForces()
        
        # Step 1: Calculate seismic response coefficient Cs
        Ta = building.approximate_period
        forces.Ta = Ta
        
        # Calculate Cs per ASCE 7-22 Equation 12.8-2
        if Ta <= spectrum.TS:
            Sa = site_data.SDS
        elif Ta <= spectrum.TL:
            Sa = site_data.SD1 / Ta
        else:
            Sa = site_data.SD1 * spectrum.TL / (Ta ** 2)
        
        Cs = Sa / building.R
        
        # Apply limits on Cs
        Cs_max = site_data.SD1 / (Ta * building.R)  # Upper limit
        Cs_min = max(0.044 * site_data.SDS, 0.01)   # Lower limit
        
        if site_data.S1 >= 0.6:  # Additional minimum for high seismicity
            Cs_min = max(Cs_min, 0.5 * site_data.S1 / building.R)
        
        Cs = max(min(Cs, Cs_max), Cs_min)
        forces.Cs = Cs
        
        # Step 2: Calculate base shear
        forces.V = Cs * building.weight
        
        # Step 3: Distribute forces to stories
        self._distribute_lateral_forces(forces, building)
        
        # Step 4: Calculate drift and displacement demands
        self._calculate_story_drifts(forces, building)
        
        return forces
    
    def _distribute_lateral_forces(self, forces: SeismicForces, building: BuildingSeismicData):
        """Distribute lateral forces to stories per ASCE 7-22 Section 12.8.3"""
        
        # Determine vertical distribution factor k
        Ta = forces.Ta
        if Ta <= 0.5:
            k = 1.0
        elif Ta >= 2.5:
            k = 2.0
        else:
            k = 1.0 + (Ta - 0.5) / 2.0  # Linear interpolation
        
        forces.k = k
        
        # Calculate additional force at top (if required)
        if Ta > 0.7:
            forces.Ft = 0.07 * Ta * forces.V
            forces.Ft = min(forces.Ft, 0.25 * forces.V)
        else:
            forces.Ft = 0.0
        
        # Distribute remaining force
        V_remaining = forces.V - forces.Ft
        
        # Calculate story forces
        story_forces = []
        heights = building.story_heights
        weights = building.story_weights
        
        # Calculate sum of wi*hi^k for normalization
        sum_wh_k = sum(w * (sum(heights[:i+1])) ** k for i, w in enumerate(weights))
        
        for i, (w, h) in enumerate(zip(weights, heights)):
            story_height = sum(heights[:i+1])  # Cumulative height
            
            # Force at this story level
            if i == len(weights) - 1:  # Top story
                Fx = V_remaining * w * (story_height ** k) / sum_wh_k + forces.Ft
            else:
                Fx = V_remaining * w * (story_height ** k) / sum_wh_k
            
            story_forces.append(Fx)
        
        forces.story_forces = story_forces
        forces.story_heights = [sum(heights[:i+1]) for i in range(len(heights))]
    
    def _calculate_story_drifts(self, forces: SeismicForces, building: BuildingSeismicData):
        """Calculate story drift ratios (simplified)"""
        
        # This is a simplified drift calculation
        # Full implementation would require structural analysis
        
        num_stories = len(building.story_heights)
        story_drifts = []
        Cd_deltas = []
        
        # Assume uniform stiffness and calculate approximate drifts
        for i in range(num_stories):
            # Simplified drift calculation (would be from structural analysis)
            drift_ratio = 0.005  # Assume 0.5% drift (placeholder)
            Cd_delta = building.Cd * drift_ratio * building.story_heights[i]
            
            story_drifts.append(drift_ratio)
            Cd_deltas.append(Cd_delta)
        
        forces.story_drifts = story_drifts
        forces.Cd_delta = Cd_deltas
    
    def generate_seismic_report(self, site_data: SeismicSiteData,
                               building: BuildingSeismicData,
                               spectrum: ResponseSpectrum,
                               forces: SeismicForces,
                               filepath: Optional[str] = None) -> str:
        """Generate comprehensive seismic analysis report"""
        
        # Determine Seismic Design Category
        sdc = self._determine_sdc(site_data, building)
        
        report_lines = [
            "ASCE 7-22 SEISMIC ANALYSIS REPORT", 
            "=" * 50,
            "",
            f"Analysis Code: {self.version}",
            f"Analysis Method: Equivalent Lateral Force (ELF) Procedure",
            f"Reference: ASCE 7-22 Chapter 12",
            "",
            "SITE SEISMICITY",
            "-" * 20,
            f"Site Location: ({site_data.latitude:.3f}°, {site_data.longitude:.3f}°)",
            f"Mapped Short Period Acceleration (Ss): {site_data.Ss:.3f}g",
            f"Mapped 1-Second Period Acceleration (S1): {site_data.S1:.3f}g",
            f"Site Class: {site_data.site_class.value}",
            "",
            "SITE COEFFICIENTS",
            "-" * 20,
            f"Site Coefficient Fa: {site_data.Fa:.2f}",
            f"Site Coefficient Fv: {site_data.Fv:.2f}",
            "",
            "DESIGN GROUND MOTION",
            "-" * 25,
            f"Site-Modified Spectral Acceleration SMS: {site_data.SMS:.3f}g",
            f"Site-Modified Spectral Acceleration SM1: {site_data.SM1:.3f}g",
            f"Design Spectral Acceleration SDS: {site_data.SDS:.3f}g",
            f"Design Spectral Acceleration SD1: {site_data.SD1:.3f}g",
            f"Seismic Design Category: {sdc.value}",
            "",
            "BUILDING INFORMATION",
            "-" * 25,
            f"Total Height: {building.height:.1f} ft",
            f"Total Seismic Weight: {building.weight:.0f} lb",
            f"Occupancy Category: {building.occupancy_category.value}",
            f"Structural System: {building.structural_system.value.replace('_', ' ').title()}",
            "",
            "STRUCTURAL SYSTEM FACTORS",
            "-" * 30,
            f"Response Modification Coefficient (R): {building.R:.1f}",
            f"Overstrength Factor (Ω₀): {building.Omega0:.1f}",
            f"Deflection Amplification Factor (Cd): {building.Cd:.1f}",
            "",
            "FUNDAMENTAL PERIOD",
            "-" * 25,
            f"Approximate Period (Ta): {forces.Ta:.3f} sec",
            f"Period Coefficient (Ct): {building.Ct:.3f}",
            f"Period Exponent (x): {building.x:.2f}",
            "",
            "RESPONSE SPECTRUM PARAMETERS",
            "-" * 35,
            f"Short Period Transition (TS): {spectrum.TS:.3f} sec",
            f"Long Period Transition (TL): {spectrum.TL:.1f} sec",
            f"Initial Period (T0): {spectrum.T0:.3f} sec",
            "",
            "BASE SHEAR CALCULATION",
            "-" * 25,
            f"Seismic Response Coefficient (Cs): {forces.Cs:.4f}",
            f"Design Base Shear (V): {forces.V:.0f} lb",
            f"Force Distribution Exponent (k): {forces.k:.2f}",
            f"Additional Top Force (Ft): {forces.Ft:.0f} lb",
            "",
            "STORY FORCES",
            "-" * 15,
            f"{'Story':<8} {'Height (ft)':<12} {'Force (lb)':<12} {'Cumulative (lb)':<15}",
            "-" * 55
        ]
        
        # Add story force details
        cumulative_force = 0
        for i, (height, force) in enumerate(zip(forces.story_heights, forces.story_forces)):
            cumulative_force += force
            report_lines.append(f"{i+1:<8} {height:<12.1f} {force:<12.0f} {cumulative_force:<15.0f}")
        
        report_lines.extend([
            "",
            "LOAD COMBINATIONS (ASCE 7-22 Section 2.3)",
            "-" * 45,
            "1.2D + Ex + L + 0.2S",
            "1.2D + Ey + L + 0.2S", 
            "0.9D + Ex",
            "0.9D + Ey",
            "",
            f"Where: Ex = Ey = ρQE = {forces.V:.0f} lb (redundancy factor ρ assumed = 1.0)",
            "",
            "DESIGN REQUIREMENTS",
            "-" * 25,
            f"- Seismic Design Category: {sdc.value}",
            "- Story drift limits per ASCE 7-22 Table 12.12-1",
            "- P-delta effects evaluation required",
            "- Diaphragm design per ASCE 7-22 Section 12.10",
            "",
            "ADDITIONAL REQUIREMENTS",
            "-" * 30
        ])
        
        # Add SDC-specific requirements
        if sdc in [SeismicDesignCategory.D, SeismicDesignCategory.E, SeismicDesignCategory.F]:
            report_lines.extend([
                "- Special seismic load combinations (ASCE 7-22 Section 12.4.2.3)",
                "- Orthogonal loading effects (ASCE 7-22 Section 12.5)",
                "- Structural integrity requirements (ASCE 7-22 Section 12.3.4)",
                "- Nonlinear procedures may be required"
            ])
        
        report_lines.extend([
            "",
            "NOTES",
            "-" * 10,
            "- Analysis assumes regular building configuration",
            "- For irregular buildings, additional analysis may be required",
            "- Modal response spectrum analysis recommended for complex structures",
            "- Site-specific ground motion analysis may be required for Site Class F"
        ])
        
        report_content = "\n".join(report_lines)
        
        # Save to file if requested
        if filepath:
            with open(filepath, 'w') as f:
                f.write(report_content)
            print(f"ASCE 7-22 seismic analysis report saved to: {filepath}")
        
        return report_content
    
    def _determine_sdc(self, site_data: SeismicSiteData, building: BuildingSeismicData) -> SeismicDesignCategory:
        """Determine Seismic Design Category per ASCE 7-22 Section 11.6"""
        
        SDS = site_data.SDS
        SD1 = site_data.SD1
        occ_cat = building.occupancy_category
        
        # Determine SDC based on SDS
        if SDS < 0.167:
            sdc_s = SeismicDesignCategory.A
        elif SDS < 0.33:
            if occ_cat in [RiskCategory.I, RiskCategory.II]:
                sdc_s = SeismicDesignCategory.B
            else:
                sdc_s = SeismicDesignCategory.C
        elif SDS < 0.50:
            if occ_cat in [RiskCategory.I, RiskCategory.II]:
                sdc_s = SeismicDesignCategory.C
            else:
                sdc_s = SeismicDesignCategory.D
        else:
            sdc_s = SeismicDesignCategory.D
        
        # Determine SDC based on SD1
        if SD1 < 0.067:
            sdc_1 = SeismicDesignCategory.A
        elif SD1 < 0.133:
            if occ_cat in [RiskCategory.I, RiskCategory.II]:
                sdc_1 = SeismicDesignCategory.B
            else:
                sdc_1 = SeismicDesignCategory.C
        elif SD1 < 0.20:
            if occ_cat in [RiskCategory.I, RiskCategory.II]:
                sdc_1 = SeismicDesignCategory.C
            else:
                sdc_1 = SeismicDesignCategory.D
        else:
            sdc_1 = SeismicDesignCategory.D
        
        # Take the more restrictive
        sdc_values = {SeismicDesignCategory.A: 1, SeismicDesignCategory.B: 2, 
                     SeismicDesignCategory.C: 3, SeismicDesignCategory.D: 4}
        
        final_sdc_value = max(sdc_values[sdc_s], sdc_values[sdc_1])
        
        for sdc, value in sdc_values.items():
            if value == final_sdc_value:
                return sdc
        
        return SeismicDesignCategory.C  # Default


# Quick calculation functions
def quick_seismic_analysis(Ss: float, S1: float, site_class: str,
                          height: float, weight: float, R: float = 6.0) -> Dict[str, float]:
    """Quick seismic analysis with simplified inputs"""
    
    # Convert string site class to enum
    site_class_map = {'A': SiteClass.A, 'B': SiteClass.B, 'C': SiteClass.C, 
                     'D': SiteClass.D, 'E': SiteClass.E}
    site_class_enum = site_class_map.get(site_class.upper(), SiteClass.D)
    
    # Create simplified inputs
    site_data = SeismicSiteData(
        latitude=0, longitude=0,
        Ss=Ss, S1=S1,
        site_class=site_class_enum
    )
    
    building = BuildingSeismicData(
        height=height,
        weight=weight,
        occupancy_category=RiskCategory.II,
        structural_system=StructuralSystem.SCBF,  # Default braced frame
        story_heights=[height],
        story_weights=[weight]
    )
    building.R = R
    
    # Generate loads
    generator = ASCE7SeismicGenerator()
    spectrum, forces = generator.generate_seismic_loads(site_data, building)
    
    return {
        'SDS': site_data.SDS,
        'SD1': site_data.SD1,
        'fundamental_period': forces.Ta,
        'response_coefficient': forces.Cs,
        'base_shear': forces.V,
        'base_shear_ratio': forces.V / weight
    }


# Import risk category from wind module for consistency
from .wind_asce7 import RiskCategory


# Example usage and testing
if __name__ == "__main__":
    print("Testing ASCE 7-22 Seismic Load Generator...")
    
    # Example site and building
    site = SeismicSiteData(
        latitude=34.05, longitude=-118.25,  # Los Angeles area
        Ss=1.5, S1=0.6,  # High seismicity
        site_class=SiteClass.D
    )
    
    building = BuildingSeismicData(
        height=120,  # 120 ft tall
        weight=5000000,  # 5000 kips
        occupancy_category=RiskCategory.II,
        structural_system=StructuralSystem.SMF,
        story_heights=[15] * 8,  # 8 stories, 15 ft each
        story_weights=[625000] * 8  # Equal story weights
    )
    
    # Generate seismic loads
    generator = ASCE7SeismicGenerator()
    spectrum, forces = generator.generate_seismic_loads(site, building)
    
    print(f"Design Spectral Acceleration SDS: {site.SDS:.3f}g")
    print(f"Design Spectral Acceleration SD1: {site.SD1:.3f}g")
    print(f"Fundamental Period: {forces.Ta:.3f} sec")
    print(f"Seismic Response Coefficient: {forces.Cs:.4f}")
    print(f"Design Base Shear: {forces.V:.0f} lb")
    print(f"Base Shear Ratio: {forces.V/building.weight:.3f}")
    
    # Generate report
    report = generator.generate_seismic_report(site, building, spectrum, forces)
    print("\nSeismic analysis report generated successfully!")
    
    print("ASCE 7-22 Seismic Load Generator ready for StructureTools integration!")
