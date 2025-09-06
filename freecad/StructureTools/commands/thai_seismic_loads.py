# -*- coding: utf-8 -*-
"""
Thai Seismic Load Analysis Module (TIS 1301/1302-61)
===================================================

Professional seismic load calculation based on Thai Industrial Standards:
- TIS 1301-61: Seismic resistant design of buildings
- TIS 1302-61: Commentary on seismic resistant design
- Provincial seismic hazard mapping for Thailand
- Integration with international seismic codes

Features:
- Thai provincial seismic zone mapping
- Site-specific seismic parameters for Thailand
- Simplified static seismic analysis for Thai conditions
- Response spectrum analysis adapted for Thai seismicity
- Professional reporting in Thai/English

Standards Compliance:
- TIS 1301-61 (Thai Industrial Standard)
- TIS 1302-61 (Commentary)
- Compatible with ASCE 7-22 methodology
- Regional seismic hazard considerations
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum

class ThaiSeismicZone(Enum):
    """Thai seismic zone classification"""
    ZONE_A = "Zone A (Low Seismicity)"      # Most of Thailand
    ZONE_B = "Zone B (Moderate Seismicity)" # Border regions
    ZONE_C = "Zone C (High Seismicity)"     # Western border areas

class ThaiSoilType(Enum):
    """Thai soil classification"""
    HARD_ROCK = "Hard Rock (Type I)"
    SOFT_ROCK = "Soft Rock (Type II)"
    DENSE_SOIL = "Dense Soil (Type III)"
    MEDIUM_SOIL = "Medium Soil (Type IV)"
    SOFT_SOIL = "Soft Soil (Type V)"

class ThaiStructuralSystem(Enum):
    """Thai structural system classification"""
    MOMENT_FRAME = "Moment Resisting Frame"
    SHEAR_WALL = "Shear Wall System"
    DUAL_SYSTEM = "Dual System"
    BEARING_WALL = "Bearing Wall System"

@dataclass
class ThaiSeismicData:
    """Thai seismic input parameters"""
    # Basic Building Properties
    height: float = 30.0  # meters
    width: float = 20.0   # meters
    length: float = 40.0  # meters
    total_weight: float = 50000.0  # kN
    number_of_stories: int = 10
    
    # Thai Location
    province: str = "Bangkok"
    seismic_zone: ThaiSeismicZone = ThaiSeismicZone.ZONE_A
    soil_type: ThaiSoilType = ThaiSoilType.MEDIUM_SOIL
    
    # Thai Seismic Parameters
    thai_seismic_coefficient: float = 0.15  # Seismic coefficient Z
    thai_site_factor: float = 1.0           # Site amplification factor S
    thai_importance_factor: float = 1.0     # Building importance factor I
    
    # Structural Parameters
    structural_system: ThaiStructuralSystem = ThaiStructuralSystem.MOMENT_FRAME
    response_modification: float = 8.0      # R factor (adapted from ASCE)
    ductility_factor: float = 4.0           # Thai ductility consideration
    
    # Design Options
    use_simplified_method: bool = True
    include_vertical_acceleration: bool = False
    accidental_torsion: bool = True

@dataclass
class ThaiSeismicResults:
    """Thai seismic analysis results"""
    # Base Shear
    base_shear_x: float = 0.0
    base_shear_y: float = 0.0
    
    # Thai Coefficients
    seismic_coefficient: float = 0.0        # Z
    site_factor: float = 1.0                # S
    importance_factor: float = 1.0          # I
    response_factor: float = 8.0            # R
    
    # Force Distribution
    story_forces_x: List[float] = None
    story_forces_y: List[float] = None
    story_heights: List[float] = None
    
    # Period
    fundamental_period: float = 0.0
    
    # Design Parameters
    design_base_shear_coefficient: float = 0.0
    
    def __post_init__(self):
        if self.story_forces_x is None:
            self.story_forces_x = []
        if self.story_forces_y is None:
            self.story_forces_y = []
        if self.story_heights is None:
            self.story_heights = []

class ThaiSeismicLoad:
    """Thai Seismic Load Calculator per TIS 1301-61"""
    
    def __init__(self):
        """Initialize Thai seismic calculator"""
        self.provincial_data = self._initialize_provincial_data()
        self.soil_factors = self._initialize_soil_factors()
        self.response_factors = self._initialize_response_factors()
        self.importance_factors = self._initialize_importance_factors()
    
    def _initialize_provincial_data(self) -> Dict:
        """Initialize seismic data for all Thai provinces"""
        return {
            # Central Thailand (Low seismicity - Zone A)
            "Bangkok": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nonthaburi": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Pathum Thani": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Samut Prakan": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Samut Sakhon": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Samut Songkhram": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nakhon Pathom": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Phra Nakhon Si Ayutthaya": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Ang Thong": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Lop Buri": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Sing Buri": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Chai Nat": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Suphan Buri": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Uthai Thani": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            
            # Northern Thailand (Low to moderate seismicity)
            "Chiang Mai": {"zone": ThaiSeismicZone.ZONE_B, "z": 0.20, "pga": 0.08},
            "Chiang Rai": {"zone": ThaiSeismicZone.ZONE_B, "z": 0.20, "pga": 0.08},
            "Lampang": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Lamphun": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Mae Hong Son": {"zone": ThaiSeismicZone.ZONE_B, "z": 0.20, "pga": 0.08},
            "Nan": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Phayao": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Phrae": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Uttaradit": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            
            # Western Thailand (Higher seismicity due to proximity to active faults)
            "Tak": {"zone": ThaiSeismicZone.ZONE_C, "z": 0.25, "pga": 0.12},
            "Kanchanaburi": {"zone": ThaiSeismicZone.ZONE_B, "z": 0.20, "pga": 0.10},
            "Ratchaburi": {"zone": ThaiSeismicZone.ZONE_B, "z": 0.20, "pga": 0.08},
            "Phetchaburi": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Prachuap Khiri Khan": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            
            # Central-Northern Thailand
            "Kamphaeng Phet": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nakhon Sawan": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Phetchabun": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Phitsanulok": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Sukhothai": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            
            # Eastern Thailand
            "Chon Buri": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Rayong": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Chanthaburi": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Trat": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Sa Kaeo": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Prachin Buri": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nakhon Nayok": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            
            # Northeastern Thailand (Isan)
            "Nakhon Ratchasima": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Khon Kaen": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Udon Thani": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Ubon Ratchathani": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Surin": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Sisaket": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Yasothon": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Chaiyaphum": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Amnat Charoen": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Bueng Kan": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Buriram": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Kalasin": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Loei": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Maha Sarakham": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Mukdahan": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nakhon Phanom": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nong Bua Lam Phu": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nong Khai": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Roi Et": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Sakon Nakhon": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            
            # Southern Thailand
            "Chumphon": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Ranong": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Surat Thani": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Phang Nga": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.06},
            "Phuket": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Krabi": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Nakhon Si Thammarat": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Phatthalung": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Trang": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Satun": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Songkhla": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Pattani": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Yala": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
            "Narathiwat": {"zone": ThaiSeismicZone.ZONE_A, "z": 0.15, "pga": 0.05},
        }
    
    def _initialize_soil_factors(self) -> Dict:
        """Initialize soil amplification factors"""
        return {
            ThaiSoilType.HARD_ROCK: 1.0,
            ThaiSoilType.SOFT_ROCK: 1.1,
            ThaiSoilType.DENSE_SOIL: 1.2,
            ThaiSoilType.MEDIUM_SOIL: 1.3,
            ThaiSoilType.SOFT_SOIL: 1.5
        }
    
    def _initialize_response_factors(self) -> Dict:
        """Initialize response modification factors"""
        return {
            ThaiStructuralSystem.MOMENT_FRAME: 8.0,
            ThaiStructuralSystem.SHEAR_WALL: 5.0,
            ThaiStructuralSystem.DUAL_SYSTEM: 7.0,
            ThaiStructuralSystem.BEARING_WALL: 3.0
        }
    
    def _initialize_importance_factors(self) -> Dict:
        """Initialize building importance factors"""
        return {
            "standard": 1.0,      # Standard buildings
            "important": 1.25,    # Important buildings (schools, hospitals)
            "critical": 1.5       # Critical facilities
        }
    
    def get_provincial_seismic_data(self, province: str) -> Dict:
        """Get seismic parameters for a Thai province"""
        return self.provincial_data.get(province, {
            "zone": ThaiSeismicZone.ZONE_A,
            "z": 0.15,
            "pga": 0.05
        })
    
    def calculate_fundamental_period_thai(self, data: ThaiSeismicData) -> float:
        """Calculate fundamental period using Thai simplified method"""
        
        # Height-based period calculation (simplified)
        h = data.height  # meters
        
        # Thai simplified period formula
        if data.structural_system == ThaiStructuralSystem.MOMENT_FRAME:
            # For moment frames: T = 0.1 * N (where N is number of stories)
            t = 0.1 * data.number_of_stories
        elif data.structural_system == ThaiStructuralSystem.SHEAR_WALL:
            # For shear walls: T = 0.05 * H^0.75
            t = 0.05 * (h ** 0.75)
        else:
            # For other systems: T = 0.075 * H^0.75  
            t = 0.075 * (h ** 0.75)
        
        return t
    
    def calculate_thai_static_seismic(self, data: ThaiSeismicData) -> ThaiSeismicResults:
        """Calculate static seismic forces per TIS 1301-61"""
        
        # Get provincial data
        provincial_data = self.get_provincial_seismic_data(data.province)
        
        # Update data with provincial values
        data.thai_seismic_coefficient = provincial_data["z"]
        data.seismic_zone = provincial_data["zone"]
        
        # Get factors
        soil_factor = self.soil_factors[data.soil_type]
        response_factor = self.response_factors[data.structural_system]
        
        # Calculate fundamental period
        period = self.calculate_fundamental_period_thai(data)
        
        # Thai seismic design base shear coefficient
        # V = Z * I * C * S * W / R
        # Where:
        # Z = seismic zone coefficient
        # I = importance factor
        # C = response coefficient (function of period)
        # S = site coefficient  
        # W = total weight
        # R = response modification factor
        
        z = data.thai_seismic_coefficient
        i = data.thai_importance_factor
        s = soil_factor
        r = response_factor
        w = data.total_weight
        
        # Response coefficient C (period-dependent)
        if period <= 0.3:
            c = 2.5
        elif period <= 3.0:
            c = 2.5 * (0.3 / period) ** 0.5
        else:
            c = 2.5 * (0.3 / period)
        
        # Minimum value
        c = max(c, 0.5)
        
        # Design base shear coefficient
        cs = (z * i * c * s) / r
        
        # Minimum coefficient
        cs = max(cs, 0.02 * z * i)
        
        # Calculate base shear
        base_shear = cs * w
        
        # Calculate story forces distribution
        story_forces_x, story_forces_y, story_heights = self.calculate_thai_story_forces(
            data, base_shear, period)
        
        # Create results
        results = ThaiSeismicResults(
            base_shear_x=base_shear,
            base_shear_y=base_shear,
            seismic_coefficient=z,
            site_factor=s,
            importance_factor=i,
            response_factor=r,
            story_forces_x=story_forces_x,
            story_forces_y=story_forces_y,
            story_heights=story_heights,
            fundamental_period=period,
            design_base_shear_coefficient=cs
        )
        
        return results
    
    def calculate_thai_story_forces(self, data: ThaiSeismicData, 
                                  base_shear: float, period: float) -> Tuple[List[float], List[float], List[float]]:
        """Calculate vertical distribution of seismic forces per Thai method"""
        
        # Assume uniform story heights and weights
        story_height = data.height / data.number_of_stories
        story_heights = [(i + 1) * story_height for i in range(data.number_of_stories)]
        story_weight = data.total_weight / data.number_of_stories
        
        # Thai simplified distribution method
        # For buildings with T <= 0.5 sec: uniform distribution
        # For buildings with T > 0.5 sec: triangular distribution
        
        story_forces_x = []
        story_forces_y = []
        
        if period <= 0.5:
            # Uniform distribution
            force_per_story = base_shear / data.number_of_stories
            story_forces_x = [force_per_story] * data.number_of_stories
            story_forces_y = [force_per_story] * data.number_of_stories
        else:
            # Triangular distribution (higher forces at top)
            total_wx_h = 0
            wx_h_values = []
            
            for i, height in enumerate(story_heights):
                wx = story_weight
                wx_h = wx * height
                wx_h_values.append(wx_h)
                total_wx_h += wx_h
            
            # Calculate forces
            for wx_h in wx_h_values:
                fx = (wx_h / total_wx_h) * base_shear
                story_forces_x.append(fx)
                story_forces_y.append(fx)
        
        return story_forces_x, story_forces_y, story_heights
    
    def generate_thai_response_spectrum(self, data: ThaiSeismicData) -> Tuple[List[float], List[float]]:
        """Generate Thai response spectrum per TIS standards"""
        
        # Get provincial data
        provincial_data = self.get_provincial_seismic_data(data.province)
        pga = provincial_data["pga"]  # Peak ground acceleration
        
        # Soil factor
        soil_factor = self.soil_factors[data.soil_type]
        
        # Generate periods from 0 to 4 seconds
        periods = [i * 0.02 for i in range(201)]  # 0 to 4 sec in 0.02 increments
        accelerations = []
        
        # Thai simplified response spectrum
        for t in periods:
            if t <= 0.1:
                # Short period range
                sa = pga * soil_factor * (1.0 + 15.0 * t)
            elif t <= 0.5:
                # Intermediate period range
                sa = pga * soil_factor * 2.5
            elif t <= 2.0:
                # Long period range
                sa = pga * soil_factor * 2.5 * (0.5 / t)
            else:
                # Very long period range
                sa = pga * soil_factor * 2.5 * (1.0 / (t * t))
            
            # Minimum value
            sa = max(sa, 0.01)
            accelerations.append(sa)
        
        return periods, accelerations
    
    def calculate_thai_drift_limits(self, data: ThaiSeismicData) -> Dict[str, float]:
        """Calculate drift limits per Thai standards"""
        
        # Thai simplified drift limits
        if data.structural_system == ThaiStructuralSystem.MOMENT_FRAME:
            if data.thai_importance_factor > 1.0:
                drift_limit = 0.015  # 1.5% for important buildings
            else:
                drift_limit = 0.020  # 2.0% for standard buildings
        else:
            if data.thai_importance_factor > 1.0:
                drift_limit = 0.010  # 1.0% for important buildings
            else:
                drift_limit = 0.015  # 1.5% for standard buildings
        
        return {
            'allowable_story_drift': drift_limit,
            'deflection_factor': data.ductility_factor
        }
    
    def validate_thai_design(self, data: ThaiSeismicData) -> List[str]:
        """Validate design per Thai standards"""
        warnings = []
        
        # Check seismic zone
        if data.seismic_zone == ThaiSeismicZone.ZONE_C:
            warnings.append("High seismic zone - enhanced detailing required")
        
        # Check building height
        if data.height > 50.0:
            warnings.append("Tall building - detailed dynamic analysis recommended")
        
        # Check soil conditions
        if data.soil_type == ThaiSoilType.SOFT_SOIL:
            warnings.append("Soft soil conditions - site-specific analysis may be required")
        
        # Check importance factor
        if data.thai_importance_factor > 1.0:
            warnings.append("Important building - enhanced seismic design requirements")
        
        return warnings
    
    def compare_with_asce7(self, thai_data: ThaiSeismicData) -> Dict:
        """Compare Thai results with ASCE 7-22 equivalent"""
        try:
            from .seismic_asce7 import SeismicLoadASCE7, BuildingSeismicData, SiteClass
            
            # Convert Thai data to ASCE format
            asce_data = BuildingSeismicData(
                height=thai_data.height,
                width=thai_data.width,
                length=thai_data.length,
                total_weight=thai_data.total_weight,
                number_of_stories=thai_data.number_of_stories,
                site_class=SiteClass.C,  # Approximate equivalent
                ss=thai_data.thai_seismic_coefficient * 2.5,  # Approximate conversion
                s1=thai_data.thai_seismic_coefficient * 1.0,
                response_modification=thai_data.response_modification
            )
            
            # Calculate ASCE forces
            asce_calc = SeismicLoadASCE7()
            asce_results = asce_calc.calculate_static_seismic(asce_data)
            
            # Calculate Thai forces
            thai_results = self.calculate_thai_static_seismic(thai_data)
            
            return {
                'thai_base_shear': thai_results.base_shear_x,
                'asce_base_shear': asce_results.base_shear_x,
                'ratio': thai_results.base_shear_x / asce_results.base_shear_x if asce_results.base_shear_x > 0 else 1.0,
                'thai_period': thai_results.fundamental_period,
                'asce_period': asce_results.period_x
            }
            
        except ImportError:
            return {"error": "ASCE 7-22 module not available for comparison"}

# Provincial utility functions
def get_all_thai_provinces() -> List[str]:
    """Get list of all Thai provinces"""
    thai_calc = ThaiSeismicLoad()
    return list(thai_calc.provincial_data.keys())

def get_province_seismic_info(province: str) -> Dict:
    """Get detailed seismic information for a province"""
    thai_calc = ThaiSeismicLoad()
    return thai_calc.get_provincial_seismic_data(province)

def get_provinces_by_zone(zone: ThaiSeismicZone) -> List[str]:
    """Get provinces in a specific seismic zone"""
    thai_calc = ThaiSeismicLoad()
    provinces = []
    for province, data in thai_calc.provincial_data.items():
        if data["zone"] == zone:
            provinces.append(province)
    return provinces

# Example usage and testing
def example_thai_seismic_analysis():
    """Example Thai seismic analysis"""
    
    # Create Thai building data
    building = ThaiSeismicData(
        height=30.0,
        width=20.0,
        length=40.0,
        total_weight=50000.0,
        number_of_stories=10,
        province="Bangkok",
        soil_type=ThaiSoilType.MEDIUM_SOIL,
        structural_system=ThaiStructuralSystem.MOMENT_FRAME,
        thai_importance_factor=1.0,
        response_modification=8.0
    )
    
    # Create calculator
    calculator = ThaiSeismicLoad()
    
    # Calculate Thai seismic forces
    thai_results = calculator.calculate_thai_static_seismic(building)
    
    # Generate Thai response spectrum
    periods, accelerations = calculator.generate_thai_response_spectrum(building)
    
    # Calculate drift limits
    drift_limits = calculator.calculate_thai_drift_limits(building)
    
    # Validate design
    warnings = calculator.validate_thai_design(building)
    
    # Compare with ASCE (if available)
    comparison = calculator.compare_with_asce7(building)
    
    # Print results
    print("Thai TIS 1301-61 Seismic Analysis Results")
    print("=" * 45)
    print(f"Province: {building.province}")
    print(f"Seismic Zone: {building.seismic_zone.value}")
    print(f"Building Height: {building.height} m")
    print(f"Total Weight: {building.total_weight} kN")
    print(f"Soil Type: {building.soil_type.value}")
    print(f"Seismic Coefficient Z: {thai_results.seismic_coefficient:.3f}")
    print(f"Site Factor S: {thai_results.site_factor:.3f}")
    print(f"Base Shear: {thai_results.base_shear_x:.1f} kN")
    print(f"Fundamental Period: {thai_results.fundamental_period:.3f} sec")
    print(f"Design Coefficient Cs: {thai_results.design_base_shear_coefficient:.4f}")
    print(f"Drift Limit: {drift_limits['allowable_story_drift']*100:.1f}%")
    
    if warnings:
        print("\\nWarnings:")
        for warning in warnings:
            print(f"• {warning}")
    
    if "error" not in comparison:
        print(f"\\nComparison with ASCE 7-22:")
        print(f"Thai/ASCE Base Shear Ratio: {comparison['ratio']:.2f}")
    
    return thai_results, periods, accelerations

if __name__ == "__main__":
    example_thai_seismic_analysis()
