# -*- coding: utf-8 -*-
"""
ASCE 7-22 Seismic Load Analysis Module
=====================================

Professional seismic load calculation based on ASCE 7-22 Minimum Design Loads 
and Associated Criteria for Buildings and Other Structures.

Features:
- Static seismic force calculation
- Response spectrum analysis 
- Design response spectrum generation
- MCE response spectrum generation
- Site-modified seismic parameters
- Multi-directional seismic analysis
- Professional building classification

Standards Compliance:
- ASCE 7-22 (American Society of Civil Engineers)
- IBC 2021 (International Building Code)
- FEMA P-750 (NEHRP Guidelines)
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum

class SiteClass(Enum):
    """Site classification per ASCE 7-22"""
    A = "Hard Rock"
    B = "Rock" 
    C = "Very Dense Soil and Soft Rock"
    D = "Stiff Soil"
    E = "Soft Clay Soil"
    F = "Soils Requiring Site Response Analysis"

class RiskCategory(Enum):
    """Risk category per ASCE 7-22"""
    I = 1      # Low hazard to human life
    II = 2     # Standard occupancy
    III = 3    # Substantial hazard to human life
    IV = 4     # Essential facilities

class StructuralSystem(Enum):
    """Structural system types for R factors"""
    BEARING_WALL = "Bearing Wall System"
    BUILDING_FRAME = "Building Frame System"
    MOMENT_FRAME = "Moment-Resisting Frame System"
    DUAL_SYSTEM = "Dual System"
    SHEAR_WALL = "Shear Wall-Frame Interactive System"
    CANTILEVER = "Cantilever Column System"

@dataclass
class BuildingSeismicData:
    """Building seismic input parameters"""
    # Basic Building Properties
    height: float = 30.0  # meters
    width: float = 20.0   # meters
    length: float = 40.0  # meters
    total_weight: float = 50000.0  # kN
    number_of_stories: int = 10
    
    # Site Properties
    site_class: SiteClass = SiteClass.C
    ss: float = 1.5  # Mapped spectral response acceleration (short periods)
    s1: float = 0.6  # Mapped spectral response acceleration (1-second period)
    
    # Design Parameters
    risk_category: RiskCategory = RiskCategory.II
    structural_system: StructuralSystem = StructuralSystem.MOMENT_FRAME
    importance_factor: float = 1.0  # Ie
    response_modification: float = 8.0  # R
    overstrength_factor: float = 3.0  # Ω0
    deflection_amplification: float = 5.5  # Cd
    
    # Custom Parameters
    sms: Optional[float] = None  # Site-modified short period
    sm1: Optional[float] = None  # Site-modified 1-second period
    sds: Optional[float] = None  # Design short period
    sd1: Optional[float] = None  # Design 1-second period
    
    # Analysis Options
    include_accidental_torsion: bool = True
    vertical_acceleration: bool = False
    p_delta_effects: bool = True

@dataclass 
class SeismicForces:
    """Seismic force calculation results"""
    # Base Shear
    base_shear_x: float = 0.0
    base_shear_y: float = 0.0
    
    # Periods
    period_x: float = 0.0
    period_y: float = 0.0
    
    # Coefficients
    cs_x: float = 0.0  # Seismic response coefficient X
    cs_y: float = 0.0  # Seismic response coefficient Y
    
    # Distribution
    story_forces_x: List[float] = None
    story_forces_y: List[float] = None
    story_heights: List[float] = None
    
    # Design Parameters
    sds: float = 0.0
    sd1: float = 0.0
    sms: float = 0.0
    sm1: float = 0.0
    
    # Factors
    fa: float = 1.0  # Site coefficient for short periods
    fv: float = 1.0  # Site coefficient for 1-second period
    
    def __post_init__(self):
        if self.story_forces_x is None:
            self.story_forces_x = []
        if self.story_forces_y is None:
            self.story_forces_y = []
        if self.story_heights is None:
            self.story_heights = []

class SeismicLoadASCE7:
    """ASCE 7-22 Seismic Load Calculator"""
    
    def __init__(self):
        """Initialize the seismic calculator"""
        self.site_coefficients = self._initialize_site_coefficients()
        self.r_factors = self._initialize_r_factors()
        self.importance_factors = self._initialize_importance_factors()
    
    def _initialize_site_coefficients(self) -> Dict:
        """Initialize site modification factors per ASCE 7-22 Tables 11.4-1 and 11.4-2"""
        return {
            'fa': {  # Site coefficient for short periods
                SiteClass.A: {0.25: 0.8, 0.5: 0.8, 0.75: 0.8, 1.0: 0.8, 1.25: 0.8, 1.5: 0.8, 1.75: 0.8, 2.0: 0.8},
                SiteClass.B: {0.25: 1.0, 0.5: 1.0, 0.75: 1.0, 1.0: 1.0, 1.25: 1.0, 1.5: 1.0, 1.75: 1.0, 2.0: 1.0},
                SiteClass.C: {0.25: 1.2, 0.5: 1.2, 0.75: 1.1, 1.0: 1.0, 1.25: 1.0, 1.5: 1.0, 1.75: 1.0, 2.0: 1.0},
                SiteClass.D: {0.25: 1.6, 0.5: 1.4, 0.75: 1.2, 1.0: 1.1, 1.25: 1.0, 1.5: 1.0, 1.75: 1.0, 2.0: 1.0},
                SiteClass.E: {0.25: 2.5, 0.5: 1.7, 0.75: 1.2, 1.0: 0.9, 1.25: 0.9, 1.5: 0.9, 1.75: 0.9, 2.0: 0.9},
                SiteClass.F: {0.25: 2.5, 0.5: 1.7, 0.75: 1.2, 1.0: 0.9, 1.25: 0.9, 1.5: 0.9, 1.75: 0.9, 2.0: 0.9}
            },
            'fv': {  # Site coefficient for 1-second periods
                SiteClass.A: {0.1: 0.8, 0.2: 0.8, 0.3: 0.8, 0.4: 0.8, 0.5: 0.8, 0.6: 0.8, 0.8: 0.8, 1.0: 0.8},
                SiteClass.B: {0.1: 1.0, 0.2: 1.0, 0.3: 1.0, 0.4: 1.0, 0.5: 1.0, 0.6: 1.0, 0.8: 1.0, 1.0: 1.0},
                SiteClass.C: {0.1: 1.8, 0.2: 1.6, 0.3: 1.5, 0.4: 1.4, 0.5: 1.3, 0.6: 1.25, 0.8: 1.2, 1.0: 1.2},
                SiteClass.D: {0.1: 2.4, 0.2: 2.0, 0.3: 1.8, 0.4: 1.6, 0.5: 1.5, 0.6: 1.5, 0.8: 1.5, 1.0: 1.5},
                SiteClass.E: {0.1: 3.5, 0.2: 3.2, 0.3: 2.8, 0.4: 2.4, 0.5: 2.4, 0.6: 2.4, 0.8: 2.4, 1.0: 2.4},
                SiteClass.F: {0.1: 3.5, 0.2: 3.2, 0.3: 2.8, 0.4: 2.4, 0.5: 2.4, 0.6: 2.4, 0.8: 2.4, 1.0: 2.4}
            }
        }
    
    def _initialize_r_factors(self) -> Dict:
        """Initialize response modification factors per ASCE 7-22 Table 12.2-1"""
        return {
            StructuralSystem.BEARING_WALL: {
                'special_reinforced_concrete': 5.0,
                'ordinary_reinforced_concrete': 3.0,
                'special_reinforced_masonry': 3.5,
                'intermediate_reinforced_masonry': 2.0,
                'ordinary_reinforced_masonry': 1.5
            },
            StructuralSystem.MOMENT_FRAME: {
                'special_steel': 8.0,
                'special_steel_truss': 7.0,
                'intermediate_steel': 4.5,
                'ordinary_steel': 3.5,
                'special_reinforced_concrete': 8.0,
                'intermediate_reinforced_concrete': 5.0,
                'ordinary_reinforced_concrete': 3.0
            },
            StructuralSystem.DUAL_SYSTEM: {
                'special_steel_with_special_concrete_wall': 8.0,
                'special_steel_with_special_steel_wall': 7.0,
                'special_concrete_with_special_concrete_wall': 7.0,
                'intermediate_concrete_with_special_concrete_wall': 6.0
            }
        }
    
    def _initialize_importance_factors(self) -> Dict:
        """Initialize importance factors per ASCE 7-22 Table 1.5-2"""
        return {
            RiskCategory.I: 1.0,
            RiskCategory.II: 1.0,
            RiskCategory.III: 1.25,
            RiskCategory.IV: 1.5
        }
    
    def get_site_coefficient(self, coefficient_type: str, site_class: SiteClass, 
                           spectral_value: float) -> float:
        """Get site modification coefficient (Fa or Fv)"""
        try:
            coeffs = self.site_coefficients[coefficient_type][site_class]
            
            # Find closest spectral value
            spectral_values = sorted(coeffs.keys())
            
            if spectral_value <= spectral_values[0]:
                return coeffs[spectral_values[0]]
            elif spectral_value >= spectral_values[-1]:
                return coeffs[spectral_values[-1]]
            else:
                # Linear interpolation
                for i in range(len(spectral_values) - 1):
                    if spectral_values[i] <= spectral_value <= spectral_values[i + 1]:
                        x1, y1 = spectral_values[i], coeffs[spectral_values[i]]
                        x2, y2 = spectral_values[i + 1], coeffs[spectral_values[i + 1]]
                        return y1 + (y2 - y1) * (spectral_value - x1) / (x2 - x1)
                        
        except KeyError:
            # Default values if not found
            return 1.0
    
    def calculate_site_modified_parameters(self, data: BuildingSeismicData) -> Tuple[float, float, float, float]:
        """Calculate site-modified seismic parameters per ASCE 7-22 Section 11.4"""
        
        # Get site coefficients
        fa = self.get_site_coefficient('fa', data.site_class, data.ss)
        fv = self.get_site_coefficient('fv', data.site_class, data.s1)
        
        # Site-modified spectral response accelerations (Equations 11.4-1 and 11.4-2)
        sms = fa * data.ss
        sm1 = fv * data.s1
        
        # Design spectral response accelerations (Equations 11.4-3 and 11.4-4)
        sds = (2.0 / 3.0) * sms
        sd1 = (2.0 / 3.0) * sm1
        
        return sms, sm1, sds, sd1, fa, fv
    
    def calculate_fundamental_period(self, data: BuildingSeismicData) -> Tuple[float, float]:
        """Calculate approximate fundamental period per ASCE 7-22 Section 12.8.2"""
        
        # Building height
        h = data.height  # meters
        
        # Approximate period calculation (Table 12.8-2)
        # Default values for moment frame buildings
        ct = 0.028  # For steel moment frames
        x = 0.8     # For steel moment frames
        
        # Adjust for structural system
        if data.structural_system == StructuralSystem.MOMENT_FRAME:
            ct = 0.028  # Steel moment frame
            x = 0.8
        elif data.structural_system == StructuralSystem.SHEAR_WALL:
            ct = 0.02   # Reinforced concrete shear wall
            x = 0.75
        elif data.structural_system == StructuralSystem.BEARING_WALL:
            ct = 0.02   # All other structural systems
            x = 0.75
        
        # Calculate approximate period (Equation 12.8-7)
        ta = ct * (h ** x)
        
        # Upper limit period (Equation 12.8-8)
        # Cu depends on SD1 (Table 12.8-1)
        sds = data.sds if data.sds else self.calculate_site_modified_parameters(data)[2]
        
        if sds >= 1.5:
            cu = 1.2
        elif sds >= 1.25:
            cu = 1.3
        elif sds >= 1.0:
            cu = 1.4
        elif sds >= 0.75:
            cu = 1.5
        else:
            cu = 1.7
        
        t_upper = cu * ta
        
        # For most analyses, use Ta for both directions
        return ta, ta
    
    def calculate_seismic_response_coefficient(self, data: BuildingSeismicData, 
                                            period: float, direction: str = 'x') -> float:
        """Calculate seismic response coefficient Cs per ASCE 7-22 Section 12.8.1"""
        
        # Get design parameters
        sms, sm1, sds, sd1, fa, fv = self.calculate_site_modified_parameters(data)
        
        # Update data object with calculated values
        if data.sds is None:
            data.sds = sds
        if data.sd1 is None:
            data.sd1 = sd1
        if data.sms is None:
            data.sms = sms
        if data.sm1 is None:
            data.sm1 = sm1
        
        r = data.response_modification
        ie = data.importance_factor
        
        # Calculate Cs per Equation 12.8-2
        cs1 = sds / (r / ie)
        
        # Calculate Cs per Equation 12.8-3 (need not exceed)
        cs2 = sd1 / (period * (r / ie))
        
        # Take minimum of the two
        cs = min(cs1, cs2)
        
        # Minimum value per Equation 12.8-5
        cs_min = max(0.044 * sds * ie, 0.01)
        
        # For certain conditions, additional minimum per Equation 12.8-6
        if data.s1 >= 0.6:
            cs_min = max(cs_min, 0.5 * data.s1 / (r / ie))
        
        # Apply minimum
        cs = max(cs, cs_min)
        
        return cs
    
    def calculate_static_seismic(self, data: BuildingSeismicData) -> SeismicForces:
        """Calculate static seismic forces per ASCE 7-22 Section 12.8"""
        
        # Calculate fundamental periods
        period_x, period_y = self.calculate_fundamental_period(data)
        
        # Calculate seismic response coefficients
        cs_x = self.calculate_seismic_response_coefficient(data, period_x, 'x')
        cs_y = self.calculate_seismic_response_coefficient(data, period_y, 'y')
        
        # Calculate base shear (Equation 12.8-1)
        w = data.total_weight
        base_shear_x = cs_x * w
        base_shear_y = cs_y * w
        
        # Calculate story forces (vertical distribution)
        story_forces_x, story_forces_y, story_heights = self.calculate_story_forces(
            data, base_shear_x, base_shear_y, period_x, period_y)
        
        # Get site parameters
        sms, sm1, sds, sd1, fa, fv = self.calculate_site_modified_parameters(data)
        
        # Create results object
        results = SeismicForces(
            base_shear_x=base_shear_x,
            base_shear_y=base_shear_y,
            period_x=period_x,
            period_y=period_y,
            cs_x=cs_x,
            cs_y=cs_y,
            story_forces_x=story_forces_x,
            story_forces_y=story_forces_y,
            story_heights=story_heights,
            sds=sds,
            sd1=sd1,
            sms=sms,
            sm1=sm1,
            fa=fa,
            fv=fv
        )
        
        return results
    
    def calculate_story_forces(self, data: BuildingSeismicData, 
                             base_shear_x: float, base_shear_y: float,
                             period_x: float, period_y: float) -> Tuple[List[float], List[float], List[float]]:
        """Calculate vertical distribution of seismic forces per ASCE 7-22 Section 12.8.3"""
        
        # Assume uniform story heights
        story_height = data.height / data.number_of_stories
        story_heights = [(i + 1) * story_height for i in range(data.number_of_stories)]
        
        # Assume uniform weight distribution
        story_weight = data.total_weight / data.number_of_stories
        
        # Calculate story forces for X direction
        story_forces_x = []
        story_forces_y = []
        
        for direction, base_shear, period in [('x', base_shear_x, period_x), ('y', base_shear_y, period_y)]:
            
            # Calculate k factor (ASCE 7-22 Section 12.8.3)
            if period <= 0.5:
                k = 1.0
            elif period >= 2.5:
                k = 2.0
            else:
                k = 1.0 + (period - 0.5) / 2.0
            
            # Calculate Cvx for each story (Equation 12.8-12)
            numerator_sum = 0
            cvx_values = []
            
            for i, height in enumerate(story_heights):
                wx = story_weight  # Assuming uniform weight
                numerator = wx * (height ** k)
                numerator_sum += numerator
                cvx_values.append(numerator)
            
            # Calculate story forces
            story_forces = []
            for cvx_num in cvx_values:
                cvx = cvx_num / numerator_sum
                fx = cvx * base_shear
                story_forces.append(fx)
            
            if direction == 'x':
                story_forces_x = story_forces
            else:
                story_forces_y = story_forces
        
        return story_forces_x, story_forces_y, story_heights
    
    def generate_response_spectrum(self, data: BuildingSeismicData, 
                                 spectrum_type: str = "design") -> Tuple[List[float], List[float]]:
        """Generate ASCE 7-22 response spectrum per Section 11.4.6"""
        
        # Get design parameters
        sms, sm1, sds, sd1, fa, fv = self.calculate_site_modified_parameters(data)
        
        if spectrum_type.lower() == "mce":
            # MCE Response Spectrum uses SMS and SM1
            sa_short = sms
            sa_1sec = sm1
        else:
            # Design Response Spectrum uses SDS and SD1
            sa_short = sds
            sa_1sec = sd1
        
        # Transition periods
        ts = sd1 / sds if sds > 0 else 0.5  # Equation 11.4-5
        to = 0.2 * ts                       # Equation 11.4-6
        tl = 8.0  # Long-period transition (site-specific, simplified)
        
        # Generate period array
        periods = []
        accelerations = []
        
        # Period range from 0 to 4 seconds with 0.02 second increments
        for i in range(201):
            t = i * 0.02
            periods.append(t)
            
            # Calculate spectral acceleration per Equations 11.4-5 through 11.4-8
            if t <= to:
                # Short period range
                sa = sa_short * (0.4 + 0.6 * t / to)
            elif t <= ts:
                # Intermediate period range
                sa = sa_short
            elif t <= tl:
                # Long period range
                sa = sa_1sec / t
            else:
                # Very long period range
                sa = sa_1sec * tl / (t * t)
            
            # Ensure minimum value
            sa = max(sa, 0.01)
            accelerations.append(sa)
        
        return periods, accelerations
    
    def calculate_drift_limits(self, data: BuildingSeismicData) -> Dict[str, float]:
        """Calculate story drift limits per ASCE 7-22 Table 12.12-1"""
        
        # Risk category based drift limits
        if data.risk_category in [RiskCategory.I, RiskCategory.II]:
            if data.structural_system == StructuralSystem.MOMENT_FRAME:
                drift_limit = 0.025  # 2.5%
            else:
                drift_limit = 0.020  # 2.0%
        else:  # Risk Category III and IV
            if data.structural_system == StructuralSystem.MOMENT_FRAME:
                drift_limit = 0.020  # 2.0%
            else:
                drift_limit = 0.015  # 1.5%
        
        return {
            'allowable_story_drift': drift_limit,
            'cd_factor': data.deflection_amplification
        }
    
    def validate_design_parameters(self, data: BuildingSeismicData) -> List[str]:
        """Validate design parameters and return warnings/errors"""
        warnings = []
        
        # Check if site-specific analysis is required
        if data.site_class == SiteClass.F:
            warnings.append("Site Class F requires site-specific ground motion analysis")
        
        # Check for high seismic regions
        sms, sm1, sds, sd1, fa, fv = self.calculate_site_modified_parameters(data)
        
        if sds >= 1.25:
            warnings.append("High seismic region - special detailing requirements apply")
        
        if data.height > 48.0:  # meters (approximately 160 feet)
            warnings.append("Tall building - additional analysis requirements may apply")
        
        # Check R factor compatibility
        if data.response_modification > 8.0:
            warnings.append("High R factor - verify structural system compatibility")
        
        return warnings

# Example usage and testing
def example_seismic_analysis():
    """Example seismic analysis calculation"""
    
    # Create building data
    building = BuildingSeismicData(
        height=30.0,          # 10-story building
        width=20.0,
        length=40.0,
        total_weight=50000.0,  # kN
        number_of_stories=10,
        site_class=SiteClass.C,
        ss=1.5,               # High seismic region
        s1=0.6,
        risk_category=RiskCategory.II,
        structural_system=StructuralSystem.MOMENT_FRAME,
        response_modification=8.0
    )
    
    # Create calculator
    calculator = SeismicLoadASCE7()
    
    # Calculate static seismic forces
    seismic_forces = calculator.calculate_static_seismic(building)
    
    # Generate response spectrum
    periods, accelerations = calculator.generate_response_spectrum(building, "design")
    
    # Calculate drift limits
    drift_limits = calculator.calculate_drift_limits(building)
    
    # Validate design
    warnings = calculator.validate_design_parameters(building)
    
    # Print results
    print("ASCE 7-22 Seismic Analysis Results")
    print("=" * 40)
    print(f"Building Height: {building.height} m")
    print(f"Total Weight: {building.total_weight} kN")
    print(f"Site Class: {building.site_class.name}")
    print(f"SDS: {seismic_forces.sds:.3f}g")
    print(f"SD1: {seismic_forces.sd1:.3f}g")
    print(f"Base Shear X: {seismic_forces.base_shear_x:.1f} kN")
    print(f"Base Shear Y: {seismic_forces.base_shear_y:.1f} kN")
    print(f"Period X: {seismic_forces.period_x:.3f} sec")
    print(f"Period Y: {seismic_forces.period_y:.3f} sec")
    print(f"Response Coeff Cs: {seismic_forces.cs_x:.4f}")
    print(f"Drift Limit: {drift_limits['allowable_story_drift']*100:.1f}%")
    
    if warnings:
        print("\\nWarnings:")
        for warning in warnings:
            print(f"• {warning}")
    
    return seismic_forces, periods, accelerations

if __name__ == "__main__":
    example_seismic_analysis()
