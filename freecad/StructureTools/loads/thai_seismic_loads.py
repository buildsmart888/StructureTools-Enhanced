# -*- coding: utf-8 -*-
"""
Thai Seismic Loads Calculator - TIS 1301/1302-61
================================================

Implementation of Thai seismic load calculations according to:
- TIS 1301-61: Thai Industrial Standard for Earthquake Resistant Design of Buildings
- TIS 1302-61: Thai Industrial Standard for Seismic Load Calculation and Analysis
- Provincial seismic zones with design response spectra

การคำนวณแรงแผ่นดินไหวประเทศไทยตาม:
- มยผ. 1301-61: มาตรฐานการออกแบบอาคารต้านทานแผ่นดินไหว
- มยผ. 1302-61: มาตรฐานการคำนวณและวิเคราะห์แรงแผ่นดินไหว
- โซนแผ่นดินไหวตามจังหวัดพร้อมสเปกตรัมการตอบสนอง

Integration with StructureTools Phase 2 Load Generation Systems
"""

import math
import numpy as np
from typing import Dict, Any, Optional, List, Tuple, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

# Integration with existing load system
try:
    # Try relative import first
    from . import GeneratedLoads, SeismicLoads
    from ..utils.units_manager import get_units_manager
    STRUCTURETOOLS_INTEGRATION = True
except ImportError:
    try:
        # Try direct import if relative fails
        import sys
        import os
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(0, parent_dir)
        STRUCTURETOOLS_INTEGRATION = False
    except:
        STRUCTURETOOLS_INTEGRATION = False


class ThaiSeismicZone(Enum):
    """Thai seismic zones according to TIS 1301/1302-61"""
    ZONE_A = "A"  # โซน A - Low seismic hazard (Ss = 0.15g)
    ZONE_B = "B"  # โซน B - Moderate seismic hazard (Ss = 0.25g)
    ZONE_C = "C"  # โซน C - High seismic hazard (Ss = 0.40g)


class ThaiSoilType(Enum):
    """Thai soil classification according to TIS 1301-61"""
    SOIL_A = "A"  # ดินแข็งมาก / Very hard soil and rock
    SOIL_B = "B"  # ดินแข็ง / Hard soil
    SOIL_C = "C"  # ดินแน่นปานกลาง / Medium dense soil
    SOIL_D = "D"  # ดินอ่อน / Soft soil
    SOIL_E = "E"  # ดินอ่อนมาก / Very soft soil
    SOIL_F = "F"  # ดินพิเศษ / Special soil requiring site-specific analysis


class ThaiSeismicImportance(Enum):
    """Thai seismic importance categories per TIS 1301-61"""
    CATEGORY_I = "I"    # อาคารทั่วไป / Standard buildings
    CATEGORY_II = "II"  # อาคารสำคัญ / Important buildings
    CATEGORY_III = "III" # อาคารจำเป็น / Essential facilities
    CATEGORY_IV = "IV"  # อาคารอันตราย / Hazardous facilities


class ThaiStructuralSystem(Enum):
    """Thai structural system categories for seismic design"""
    CONCRETE_MOMENT_FRAME = "concrete_moment_frame"         # โครงข้อแข็งคอนกรีต
    STEEL_MOMENT_FRAME = "steel_moment_frame"               # โครงข้อแข็งเหล็ก
    CONCRETE_SHEAR_WALL = "concrete_shear_wall"             # ผนังเฉือนคอนกรีต
    STEEL_BRACED_FRAME = "steel_braced_frame"               # โครงเหล็กมีโครงรอง
    CONCRETE_DUAL_SYSTEM = "concrete_dual_system"           # ระบบคู่คอนกรีต
    STEEL_DUAL_SYSTEM = "steel_dual_system"                 # ระบบคู่เหล็ก
    BEARING_WALL_SYSTEM = "bearing_wall_system"             # ระบบผนังรับน้ำหนัก
    BUILDING_FRAME_SYSTEM = "building_frame_system"         # ระบบโครงอาคาร


@dataclass
class ThaiSeismicParameters:
    """Thai seismic design parameters according to TIS 1301/1302-61"""
    ss: float                           # Spectral acceleration at short periods
    s1: float                           # Spectral acceleration at 1-second period
    fa: float                           # Site coefficient for short periods
    fv: float                           # Site coefficient for 1-second period
    sms: float                          # Modified spectral acceleration at short periods
    sm1: float                          # Modified spectral acceleration at 1-second period
    sds: float                          # Design spectral acceleration at short periods
    sd1: float                          # Design spectral acceleration at 1-second period
    ts: float                           # Short period transition
    tl: float                           # Long period transition
    t0: float                           # Very short period


@dataclass
class ThaiBuildingProperties:
    """Thai building properties for seismic analysis"""
    height: float                       # ความสูงอาคาร m / Building height (m)
    weight: float                       # น้ำหนักอาคาร kN / Building weight (kN)
    fundamental_period: float           # คาบการสั่นพื้นฐาน s / Fundamental period (s)
    structural_system: ThaiStructuralSystem  # ระบบโครงสร้าง / Structural system
    importance_category: ThaiSeismicImportance  # ประเภทความสำคัญ / Importance category
    soil_type: ThaiSoilType            # ประเภทดิน / Soil type
    irregularity_factor: float = 1.0   # ค่าประกอบความผิดปกติ / Irregularity factor
    occupancy_type: str = "office"     # ประเภทการใช้งาน / Occupancy type


@dataclass
class ThaiSeismicLoadResult:
    """Thai seismic load calculation result"""
    base_shear: float                   # แรงเฉือนฐาน kN / Base shear (kN)
    design_acceleration: float          # ความเร่งออกแบบ g / Design acceleration (g)
    response_modification_factor: float  # ค่าประกอบการตอบสนอง R / Response modification factor
    importance_factor: float            # ค่าประกอบความสำคัญ I / Importance factor
    seismic_zone: str                   # โซนแผ่นดินไหว / Seismic zone
    province: str                       # จังหวัด / Province
    force_distribution: List[float]     # การกระจายแรงตามชั้น / Story force distribution
    story_heights: List[float]          # ความสูงแต่ละชั้น / Story heights
    displacement_profile: List[float]   # โปรไฟล์การเปลี่ยนรูป / Displacement profile
    spectral_parameters: ThaiSeismicParameters  # พารามิเตอร์สเปกตรัม / Spectral parameters
    description_thai: str              # คำอธิบายไทย / Thai description
    description_english: str           # คำอธิบายอังกฤษ / English description
    calculation_method: str            # วิธีการคำนวณ / Calculation method
    reference: str                     # อ้างอิง / Reference standard


class ThaiSeismicLoads:
    """
    Thai Seismic Loads Calculator - TIS 1301/1302-61
    
    เครื่องคำนวณแรงแผ่นดินไหวไทย - มยผ. 1301/1302-61
    
    Features:
    - Provincial seismic zone mapping (โซนแผ่นดินไหวตามจังหวัด)
    - TIS 1301-61 design procedures (ขั้นตอนการออกแบบ มยผ. 1301-61)
    - TIS 1302-61 analysis methods (วิธีการวิเคราะห์ มยผ. 1302-61)
    - Response spectrum analysis (การวิเคราะห์สเปกตรัมการตอบสนอง)
    - Building importance factors (ค่าประกอบความสำคัญอาคาร)
    - Soil site effects (ผลกระทบประเภทดิน)
    """
    
    def __init__(self):
        """Initialize Thai seismic loads calculator"""
        
        # Seismic zone parameters according to TIS 1301/1302-61
        self.seismic_zone_parameters = {
            ThaiSeismicZone.ZONE_A: {
                'ss': 0.15,  # g
                's1': 0.06,  # g
                'description_thai': 'โซนแผ่นดินไหวต่ำ',
                'description_english': 'Low seismic hazard zone',
                'regions': ['Central Thailand', 'Upper Northern Thailand']
            },
            ThaiSeismicZone.ZONE_B: {
                'ss': 0.25,  # g
                's1': 0.10,  # g
                'description_thai': 'โซนแผ่นดินไหวปานกลาง',
                'description_english': 'Moderate seismic hazard zone',
                'regions': ['Lower Northern Thailand', 'Western Thailand']
            },
            ThaiSeismicZone.ZONE_C: {
                'ss': 0.40,  # g
                's1': 0.16,  # g
                'description_thai': 'โซนแผ่นดินไหวสูง',
                'description_english': 'High seismic hazard zone',
                'regions': ['Far Western Thailand near Myanmar border']
            }
        }
        
        # Site coefficients according to TIS 1301-61
        self.site_coefficients = {
            ThaiSoilType.SOIL_A: {
                'name_thai': 'ดินแข็งมาก/หิน',
                'name_english': 'Very hard soil/rock',
                'vs30_range': '> 1500 m/s',
                'fa_zone_a': 0.8, 'fa_zone_b': 0.8, 'fa_zone_c': 0.8,
                'fv_zone_a': 0.8, 'fv_zone_b': 0.8, 'fv_zone_c': 0.8
            },
            ThaiSoilType.SOIL_B: {
                'name_thai': 'ดินแข็ง/หินอ่อน',
                'name_english': 'Hard soil/soft rock',
                'vs30_range': '750-1500 m/s',
                'fa_zone_a': 1.0, 'fa_zone_b': 1.0, 'fa_zone_c': 1.0,
                'fv_zone_a': 1.0, 'fv_zone_b': 1.0, 'fv_zone_c': 1.0
            },
            ThaiSoilType.SOIL_C: {
                'name_thai': 'ดินแน่นปานกลาง',
                'name_english': 'Medium dense soil',
                'vs30_range': '375-750 m/s',
                'fa_zone_a': 1.2, 'fa_zone_b': 1.2, 'fa_zone_c': 1.1,
                'fv_zone_a': 1.4, 'fv_zone_b': 1.3, 'fv_zone_c': 1.2
            },
            ThaiSoilType.SOIL_D: {
                'name_thai': 'ดินอ่อน',
                'name_english': 'Soft soil',
                'vs30_range': '180-375 m/s',
                'fa_zone_a': 1.5, 'fa_zone_b': 1.4, 'fa_zone_c': 1.2,
                'fv_zone_a': 1.8, 'fv_zone_b': 1.6, 'fv_zone_c': 1.4
            },
            ThaiSoilType.SOIL_E: {
                'name_thai': 'ดินอ่อนมาก',
                'name_english': 'Very soft soil',
                'vs30_range': '< 180 m/s',
                'fa_zone_a': 2.0, 'fa_zone_b': 1.8, 'fa_zone_c': 1.5,
                'fv_zone_a': 2.4, 'fv_zone_b': 2.0, 'fv_zone_c': 1.8
            },
            ThaiSoilType.SOIL_F: {
                'name_thai': 'ดินพิเศษ',
                'name_english': 'Special soil',
                'vs30_range': 'Site-specific',
                'fa_zone_a': 'Site-specific', 'fa_zone_b': 'Site-specific', 'fa_zone_c': 'Site-specific',
                'fv_zone_a': 'Site-specific', 'fv_zone_b': 'Site-specific', 'fv_zone_c': 'Site-specific'
            }
        }
        
        # Importance factors according to TIS 1301-61
        self.importance_factors = {
            ThaiSeismicImportance.CATEGORY_I: {
                'factor': 1.0,
                'description_thai': 'อาคารทั่วไป',
                'description_english': 'Standard buildings',
                'examples_thai': 'อาคารที่อยู่อาศัย, อาคารสำนักงานทั่วไป',
                'examples_english': 'Residential buildings, standard office buildings'
            },
            ThaiSeismicImportance.CATEGORY_II: {
                'factor': 1.15,
                'description_thai': 'อาคารสำคัญ',
                'description_english': 'Important buildings',
                'examples_thai': 'โรงเรียน, อาคารชุมนุมขนาดใหญ่',
                'examples_english': 'Schools, large assembly buildings'
            },
            ThaiSeismicImportance.CATEGORY_III: {
                'factor': 1.25,
                'description_thai': 'อาคารจำเป็น',
                'description_english': 'Essential facilities',
                'examples_thai': 'โรงพยาบาล, สถานีดับเพลิง, สิ่งอำนวยความสะดวกฉุกเฉิน',
                'examples_english': 'Hospitals, fire stations, emergency facilities'
            },
            ThaiSeismicImportance.CATEGORY_IV: {
                'factor': 1.5,
                'description_thai': 'อาคารอันตราย',
                'description_english': 'Hazardous facilities',
                'examples_thai': 'โรงงานเคมี, โรงไฟฟ้าพลังงานนิวเคลียร์',
                'examples_english': 'Chemical plants, nuclear power plants'
            }
        }
        
        # Response modification factors (R) according to TIS 1301-61
        self.response_modification_factors = {
            ThaiStructuralSystem.CONCRETE_MOMENT_FRAME: {
                'r_factor': 8.0,
                'cd_factor': 5.5,
                'omega_factor': 3.0,
                'description_thai': 'โครงข้อแข็งคอนกรีตเสริมเหล็กพิเศษ',
                'description_english': 'Special reinforced concrete moment frame'
            },
            ThaiStructuralSystem.STEEL_MOMENT_FRAME: {
                'r_factor': 8.0,
                'cd_factor': 5.5,
                'omega_factor': 3.0,
                'description_thai': 'โครงข้อแข็งเหล็กพิเศษ',
                'description_english': 'Special steel moment frame'
            },
            ThaiStructuralSystem.CONCRETE_SHEAR_WALL: {
                'r_factor': 6.0,
                'cd_factor': 5.0,
                'omega_factor': 2.5,
                'description_thai': 'ผนังเฉือนคอนกรีตเสริมเหล็กพิเศษ',
                'description_english': 'Special reinforced concrete shear wall'
            },
            ThaiStructuralSystem.STEEL_BRACED_FRAME: {
                'r_factor': 6.0,
                'cd_factor': 5.0,
                'omega_factor': 2.5,
                'description_thai': 'โครงเหล็กมีโครงรองรับแรงเฉือนพิเศษ',
                'description_english': 'Special concentrically braced steel frame'
            },
            ThaiStructuralSystem.CONCRETE_DUAL_SYSTEM: {
                'r_factor': 8.0,
                'cd_factor': 5.5,
                'omega_factor': 2.5,
                'description_thai': 'ระบบคู่คอนกรีตเสริมเหล็กพิเศษ',
                'description_english': 'Special reinforced concrete dual system'
            },
            ThaiStructuralSystem.STEEL_DUAL_SYSTEM: {
                'r_factor': 8.0,
                'cd_factor': 5.5,
                'omega_factor': 2.5,
                'description_thai': 'ระบบคู่เหล็กพิเศษ',
                'description_english': 'Special steel dual system'
            },
            ThaiStructuralSystem.BEARING_WALL_SYSTEM: {
                'r_factor': 5.0,
                'cd_factor': 4.0,
                'omega_factor': 2.5,
                'description_thai': 'ระบบผนังรับน้ำหนัก',
                'description_english': 'Bearing wall system'
            },
            ThaiStructuralSystem.BUILDING_FRAME_SYSTEM: {
                'r_factor': 7.0,
                'cd_factor': 5.0,
                'omega_factor': 2.5,
                'description_thai': 'ระบบโครงอาคาร',
                'description_english': 'Building frame system'
            }
        }
        
        # Thai provinces and their seismic zones
        self.province_seismic_zones = self._initialize_seismic_zones()
    
    def _initialize_seismic_zones(self) -> Dict[str, ThaiSeismicZone]:
        """Initialize Thai province seismic zone mapping"""
        return {
            # Zone A - Low seismic hazard (Central and Upper Northern Thailand)
            'กรุงเทพมหานคร': ThaiSeismicZone.ZONE_A, 'นนทบุรี': ThaiSeismicZone.ZONE_A,
            'ปทุมธานี': ThaiSeismicZone.ZONE_A, 'สมุทรปราการ': ThaiSeismicZone.ZONE_A,
            'นครปฐม': ThaiSeismicZone.ZONE_A, 'สมุทรสาคร': ThaiSeismicZone.ZONE_A,
            'สมุทรสงคราม': ThaiSeismicZone.ZONE_A, 'นครนายก': ThaiSeismicZone.ZONE_A,
            'ปราจีนบุรี': ThaiSeismicZone.ZONE_A, 'สระแก้ว': ThaiSeismicZone.ZONE_A,
            'ชัยนาท': ThaiSeismicZone.ZONE_A, 'ลพบุรี': ThaiSeismicZone.ZONE_A,
            'สิงห์บุรี': ThaiSeismicZone.ZONE_A, 'อ่างทอง': ThaiSeismicZone.ZONE_A,
            'สุพรรณบุรี': ThaiSeismicZone.ZONE_A, 'อยุธยา': ThaiSeismicZone.ZONE_A,
            'สระบุรี': ThaiSeismicZone.ZONE_A,
            
            # Northeastern Thailand - Zone A
            'นครราชสีมา': ThaiSeismicZone.ZONE_A, 'ขอนแก่น': ThaiSeismicZone.ZONE_A,
            'อุดรธานี': ThaiSeismicZone.ZONE_A, 'อุบลราชธานี': ThaiSeismicZone.ZONE_A,
            'สกลนคร': ThaiSeismicZone.ZONE_A, 'นครพนม': ThaiSeismicZone.ZONE_A,
            'มุกดาหาร': ThaiSeismicZone.ZONE_A, 'เลย': ThaiSeismicZone.ZONE_A,
            'หนองคาย': ThaiSeismicZone.ZONE_A, 'บึงกาฬ': ThaiSeismicZone.ZONE_A,
            'ร้อยเอ็ด': ThaiSeismicZone.ZONE_A, 'กาฬสินธุ์': ThaiSeismicZone.ZONE_A,
            'มหาสารคาม': ThaiSeismicZone.ZONE_A, 'ยโสธร': ThaiSeismicZone.ZONE_A,
            'อำนาจเจริญ': ThaiSeismicZone.ZONE_A, 'บุรีรัมย์': ThaiSeismicZone.ZONE_A,
            'สุรินทร์': ThaiSeismicZone.ZONE_A, 'ศีสะเกษ': ThaiSeismicZone.ZONE_A,
            'ชัยภูมิ': ThaiSeismicZone.ZONE_A, 'หนองบัวลำภู': ThaiSeismicZone.ZONE_A,
            
            # Upper Northern Thailand - Zone A
            'เชียงใหม่': ThaiSeismicZone.ZONE_A, 'เชียงราย': ThaiSeismicZone.ZONE_A,
            'ลำปาง': ThaiSeismicZone.ZONE_A, 'ลำพูน': ThaiSeismicZone.ZONE_A,
            'น่าน': ThaiSeismicZone.ZONE_A, 'พะเยา': ThaiSeismicZone.ZONE_A,
            'แพร่': ThaiSeismicZone.ZONE_A,
            
            # Lower Northern Thailand - Zone B
            'แม่ฮ่องสอน': ThaiSeismicZone.ZONE_B, 'ตาก': ThaiSeismicZone.ZONE_B,
            'สุโขทัย': ThaiSeismicZone.ZONE_B, 'พิษณุโลก': ThaiSeismicZone.ZONE_B,
            'เพชรบูรณ์': ThaiSeismicZone.ZONE_B, 'กำแพงเพชร': ThaiSeismicZone.ZONE_B,
            'นครสวรรค์': ThaiSeismicZone.ZONE_B, 'อุตรดิตถ์': ThaiSeismicZone.ZONE_B,
            
            # Western Thailand - Zone B to C
            'กาญจนบุรี': ThaiSeismicZone.ZONE_B, 'ราชบุรี': ThaiSeismicZone.ZONE_B,
            'เพชรบุรี': ThaiSeismicZone.ZONE_B, 'ประจุวบคีรีขันธ์': ThaiSeismicZone.ZONE_B,
            
            # Far Western border areas - Zone C (highest seismic risk)
            # Note: Some border areas with Myanmar have higher seismic risk
            
            # Eastern Thailand - Zone A
            'ชลบุรี': ThaiSeismicZone.ZONE_A, 'ระยอง': ThaiSeismicZone.ZONE_A,
            'จันทบุรี': ThaiSeismicZone.ZONE_A, 'ตราด': ThaiSeismicZone.ZONE_A,
            
            # Southern Thailand - Zone A to B
            'ชุมพร': ThaiSeismicZone.ZONE_A, 'สุราษฎร์ธานี': ThaiSeismicZone.ZONE_A,
            'นครศรีธรรมราช': ThaiSeismicZone.ZONE_A, 'พัทลุง': ThaiSeismicZone.ZONE_A,
            'สงขลา': ThaiSeismicZone.ZONE_A, 'ภูเก็ต': ThaiSeismicZone.ZONE_A,
            'กระบี่': ThaiSeismicZone.ZONE_A, 'ตรัง': ThaiSeismicZone.ZONE_A,
            'สตูล': ThaiSeismicZone.ZONE_A, 'ปัตตานี': ThaiSeismicZone.ZONE_A,
            'ยะลา': ThaiSeismicZone.ZONE_A, 'นราธิวาส': ThaiSeismicZone.ZONE_A,
            'ระนอง': ThaiSeismicZone.ZONE_A, 'พังงา': ThaiSeismicZone.ZONE_A
        }
    
    def get_seismic_zone_for_province(self, province: str) -> Tuple[ThaiSeismicZone, float, float, str]:
        """Get seismic zone information for a Thai province"""
        if province in self.province_seismic_zones:
            zone = self.province_seismic_zones[province]
            zone_params = self.seismic_zone_parameters[zone]
            ss = zone_params['ss']
            s1 = zone_params['s1']
            description = f"Zone {zone.value} - {zone_params['description_thai']}"
            return zone, ss, s1, description
        else:
            # Default to Zone A if province not found
            zone = ThaiSeismicZone.ZONE_A
            zone_params = self.seismic_zone_parameters[zone]
            ss = zone_params['ss']
            s1 = zone_params['s1']
            description = f"Zone {zone.value} - Default (Province not found)"
            return zone, ss, s1, description
    
    def calculate_spectral_parameters(self, zone: ThaiSeismicZone, soil_type: ThaiSoilType) -> ThaiSeismicParameters:
        """Calculate design spectral parameters according to TIS 1301-61"""
        zone_params = self.seismic_zone_parameters[zone]
        soil_params = self.site_coefficients[soil_type]
        
        ss = zone_params['ss']
        s1 = zone_params['s1']
        
        # Get site coefficients based on zone
        if zone == ThaiSeismicZone.ZONE_A:
            fa = soil_params.get('fa_zone_a', 1.0)
            fv = soil_params.get('fv_zone_a', 1.0)
        elif zone == ThaiSeismicZone.ZONE_B:
            fa = soil_params.get('fa_zone_b', 1.0)
            fv = soil_params.get('fv_zone_b', 1.0)
        else:  # Zone C
            fa = soil_params.get('fa_zone_c', 1.0)
            fv = soil_params.get('fv_zone_c', 1.0)
        
        # Handle site-specific cases
        if isinstance(fa, str) or isinstance(fv, str):
            fa, fv = 1.0, 1.0  # Default for site-specific analysis
        
        # Calculate modified spectral accelerations
        sms = fa * ss
        sm1 = fv * s1
        
        # Calculate design spectral accelerations
        sds = (2.0/3.0) * sms
        sd1 = (2.0/3.0) * sm1
        
        # Calculate transition periods
        ts = sd1 / sds if sds > 0 else 0.2
        t0 = 0.2 * ts
        tl = 8.0  # Long-period transition (assumed for Thailand)
        
        return ThaiSeismicParameters(
            ss=ss, s1=s1, fa=fa, fv=fv,
            sms=sms, sm1=sm1, sds=sds, sd1=sd1,
            ts=ts, tl=tl, t0=t0
        )
    
    def calculate_design_response_spectrum(self, spectral_params: ThaiSeismicParameters, 
                                         periods: List[float]) -> List[float]:
        """Calculate design response spectrum values for given periods"""
        sa_values = []
        
        for t in periods:
            if t <= spectral_params.t0:
                # Very short period range
                sa = spectral_params.sds * (0.4 + 0.6 * t / spectral_params.t0)
            elif t <= spectral_params.ts:
                # Short period range
                sa = spectral_params.sds
            elif t <= spectral_params.tl:
                # Intermediate period range
                sa = spectral_params.sd1 / t
            else:
                # Long period range
                sa = spectral_params.sd1 * spectral_params.tl / (t ** 2)
            
            sa_values.append(max(sa, 0.01))  # Minimum value
        
        return sa_values
    
    def estimate_fundamental_period(self, height: float, structural_system: ThaiStructuralSystem) -> float:
        """Estimate fundamental period according to TIS 1301-61"""
        if structural_system in [ThaiStructuralSystem.CONCRETE_MOMENT_FRAME, 
                                ThaiStructuralSystem.CONCRETE_DUAL_SYSTEM]:
            # Concrete moment frame: T = 0.0466 * h^0.9
            t = 0.0466 * (height ** 0.9)
        elif structural_system in [ThaiStructuralSystem.STEEL_MOMENT_FRAME,
                                  ThaiStructuralSystem.STEEL_DUAL_SYSTEM]:
            # Steel moment frame: T = 0.0724 * h^0.8
            t = 0.0724 * (height ** 0.8)
        elif structural_system == ThaiStructuralSystem.STEEL_BRACED_FRAME:
            # Steel braced frame: T = 0.0731 * h^0.75
            t = 0.0731 * (height ** 0.75)
        elif structural_system == ThaiStructuralSystem.CONCRETE_SHEAR_WALL:
            # Concrete shear wall: T = 0.0488 * h^0.75
            t = 0.0488 * (height ** 0.75)
        else:
            # Default approximation
            t = 0.1 * height / 3.0
        
        return t
    
    def calculate_base_shear(self, building: ThaiBuildingProperties, spectral_params: ThaiSeismicParameters) -> float:
        """Calculate seismic base shear according to TIS 1301-61"""
        # Get structural system parameters
        system_params = self.response_modification_factors[building.structural_system]
        r_factor = system_params['r_factor']
        
        # Get importance factor
        importance_info = self.importance_factors[building.importance_category]
        i_factor = importance_info['factor']
        
        # Calculate design spectral acceleration
        t = building.fundamental_period
        if t <= spectral_params.t0:
            sa = spectral_params.sds * (0.4 + 0.6 * t / spectral_params.t0)
        elif t <= spectral_params.ts:
            sa = spectral_params.sds
        elif t <= spectral_params.tl:
            sa = spectral_params.sd1 / t
        else:
            sa = spectral_params.sd1 * spectral_params.tl / (t ** 2)
        
        # Calculate seismic response coefficient
        cs = (sa * i_factor) / r_factor
        
        # Apply minimum and maximum limits
        cs_max = spectral_params.sd1 / (t * r_factor)
        cs = min(cs, cs_max)
        cs = max(cs, 0.01)  # Minimum value
        
        # Calculate base shear
        base_shear = cs * building.weight * building.irregularity_factor
        
        return base_shear
    
    def calculate_vertical_force_distribution(self, building: ThaiBuildingProperties, 
                                            base_shear: float, story_heights: List[float], 
                                            story_weights: List[float]) -> List[float]:
        """Calculate vertical distribution of seismic forces"""
        # Calculate story forces using inverted triangular distribution
        total_weight_height = sum(w * h for w, h in zip(story_weights, story_heights))
        
        story_forces = []
        for i, (weight, height) in enumerate(zip(story_weights, story_heights)):
            if building.fundamental_period <= 0.5:
                # Use uniform distribution for very stiff buildings
                force = base_shear * weight / sum(story_weights)
            else:
                # Use height-weighted distribution
                force = base_shear * (weight * height) / total_weight_height
            
            story_forces.append(force)
        
        return story_forces
    
    def analyze_building_seismic_loads(self, province: str, building: ThaiBuildingProperties,
                                     story_heights: Optional[List[float]] = None,
                                     story_weights: Optional[List[float]] = None) -> ThaiSeismicLoadResult:
        """Complete seismic load analysis for a building according to Thai standards"""
        # Get seismic zone information
        zone, ss, s1, zone_desc = self.get_seismic_zone_for_province(province)
        
        # Calculate spectral parameters
        spectral_params = self.calculate_spectral_parameters(zone, building.soil_type)
        
        # Estimate fundamental period if not provided
        if building.fundamental_period <= 0:
            building.fundamental_period = self.estimate_fundamental_period(
                building.height, building.structural_system
            )
        
        # Calculate base shear
        base_shear = self.calculate_base_shear(building, spectral_params)
        
        # Calculate force distribution
        if story_heights is None:
            story_heights = [building.height]  # Single story equivalent
        if story_weights is None:
            story_weights = [building.weight]
        
        force_distribution = self.calculate_vertical_force_distribution(
            building, base_shear, story_heights, story_weights
        )
        
        # Estimate displacement profile (simplified)
        displacement_profile = []
        for h in story_heights:
            displacement = (base_shear / building.weight) * (h / building.height) ** 2
            displacement_profile.append(displacement)
        
        # Get system information
        system_params = self.response_modification_factors[building.structural_system]
        importance_info = self.importance_factors[building.importance_category]
        
        description_thai = (f"การวิเคราะห์แรงแผ่นดินไหวสำหรับ{importance_info['description_thai']}"
                          f"ในจังหวัด{province} โซน {zone.value}")
        description_english = (f"Seismic analysis for {importance_info['description_english']}"
                             f" in {province}, Zone {zone.value}")
        
        return ThaiSeismicLoadResult(
            base_shear=base_shear,
            design_acceleration=spectral_params.sds,
            response_modification_factor=system_params['r_factor'],
            importance_factor=importance_info['factor'],
            seismic_zone=zone.value,
            province=province,
            force_distribution=force_distribution,
            story_heights=story_heights,
            displacement_profile=displacement_profile,
            spectral_parameters=spectral_params,
            description_thai=description_thai,
            description_english=description_english,
            calculation_method="TIS 1301-61 + TIS 1302-61",
            reference="มยผ. 1301-61 และ มยผ. 1302-61"
        )
    
    def get_seismic_summary(self, province: str, building_height: float, building_weight: float,
                          structural_system: str = "concrete_moment_frame",
                          importance_category: str = "standard",
                          soil_type: str = "medium") -> Dict[str, Any]:
        """Get quick seismic load summary for a province"""
        zone, ss, s1, zone_desc = self.get_seismic_zone_for_province(province)
        
        # Convert string inputs to enums
        system_map = {
            'concrete_moment_frame': ThaiStructuralSystem.CONCRETE_MOMENT_FRAME,
            'steel_moment_frame': ThaiStructuralSystem.STEEL_MOMENT_FRAME,
            'concrete_shear_wall': ThaiStructuralSystem.CONCRETE_SHEAR_WALL,
            'steel_braced_frame': ThaiStructuralSystem.STEEL_BRACED_FRAME
        }
        
        importance_map = {
            'standard': ThaiSeismicImportance.CATEGORY_I,
            'important': ThaiSeismicImportance.CATEGORY_II,
            'essential': ThaiSeismicImportance.CATEGORY_III,
            'hazardous': ThaiSeismicImportance.CATEGORY_IV
        }
        
        soil_map = {
            'hard': ThaiSoilType.SOIL_B,
            'medium': ThaiSoilType.SOIL_C,
            'soft': ThaiSoilType.SOIL_D
        }
        
        building = ThaiBuildingProperties(
            height=building_height,
            weight=building_weight,
            fundamental_period=0,  # Will be estimated
            structural_system=system_map.get(structural_system, ThaiStructuralSystem.CONCRETE_MOMENT_FRAME),
            importance_category=importance_map.get(importance_category, ThaiSeismicImportance.CATEGORY_I),
            soil_type=soil_map.get(soil_type, ThaiSoilType.SOIL_C)
        )
        
        spectral_params = self.calculate_spectral_parameters(zone, building.soil_type)
        period = self.estimate_fundamental_period(building_height, building.structural_system)
        building.fundamental_period = period
        
        base_shear = self.calculate_base_shear(building, spectral_params)
        
        return {
            'province': province,
            'seismic_zone': zone.value,
            'zone_description': zone_desc,
            'spectral_acceleration_ss': ss,
            'spectral_acceleration_s1': s1,
            'design_spectral_sds': spectral_params.sds,
            'design_spectral_sd1': spectral_params.sd1,
            'fundamental_period_s': period,
            'base_shear_kn': base_shear,
            'base_shear_ratio': base_shear / building_weight,
            'building_height_m': building_height,
            'building_weight_kn': building_weight,
            'structural_system': structural_system,
            'importance_category': importance_category,
            'soil_type': soil_type,
            'calculation_standard': 'TIS 1301-61 + TIS 1302-61'
        }
    
    def generate_provincial_seismic_map(self) -> Dict[str, Dict[str, Any]]:
        """Generate comprehensive seismic map for all Thai provinces"""
        seismic_map = {}
        
        for province, zone in self.province_seismic_zones.items():
            zone_params = self.seismic_zone_parameters[zone]
            ss = zone_params['ss']
            s1 = zone_params['s1']
            
            # Calculate for standard conditions
            standard_soil = ThaiSoilType.SOIL_C
            spectral_params = self.calculate_spectral_parameters(zone, standard_soil)
            
            seismic_map[province] = {
                'seismic_zone': zone.value,
                'spectral_acceleration_ss': ss,
                'spectral_acceleration_s1': s1,
                'design_spectral_sds': spectral_params.sds,
                'design_spectral_sd1': spectral_params.sd1,
                'hazard_level': zone_params['description_thai'],
                'hazard_level_english': zone_params['description_english']
            }
        
        return seismic_map
    
    def convert_to_structuretools_format(self, thai_result: ThaiSeismicLoadResult) -> Dict[str, Any]:
        """Convert Thai seismic load result to StructureTools format"""
        if not STRUCTURETOOLS_INTEGRATION:
            return None
        
        seismic_loads = {
            'base_shear': thai_result.base_shear,
            'response_spectrum': thai_result.spectral_parameters.__dict__,
            'story_forces': thai_result.force_distribution,
            'story_heights': thai_result.story_heights,
            'displacement_profile': thai_result.displacement_profile,
            'importance_factor': thai_result.importance_factor,
            'response_modification_factor': thai_result.response_modification_factor,
            'design_acceleration': thai_result.design_acceleration,
            'calculation_method': thai_result.calculation_method,
            'code_reference': thai_result.reference,
            'thai_seismic_zone': thai_result.seismic_zone,
            'thai_province': thai_result.province
        }
        
        return seismic_loads


# Quick access functions
def calculate_thai_seismic_force(province: str, building_height: float, building_weight: float,
                               structural_system: str = "concrete_moment_frame",
                               importance: str = "standard", soil: str = "medium") -> float:
    """Quick function to calculate Thai seismic base shear for a province"""
    calculator = ThaiSeismicLoads()
    summary = calculator.get_seismic_summary(
        province, building_height, building_weight, 
        structural_system, importance, soil
    )
    return summary['base_shear_kn']


def get_thailand_seismic_zones() -> Dict[str, str]:
    """Get mapping of Thai provinces to seismic zones"""
    calculator = ThaiSeismicLoads()
    return {province: zone.value for province, zone in calculator.province_seismic_zones.items()}


# Export main classes and functions
__all__ = [
    'ThaiSeismicLoads',
    'ThaiSeismicZone',
    'ThaiSoilType',
    'ThaiSeismicImportance',
    'ThaiStructuralSystem',
    'ThaiBuildingProperties',
    'ThaiSeismicParameters',
    'ThaiSeismicLoadResult',
    'calculate_thai_seismic_force',
    'get_thailand_seismic_zones'
]


# Module information
__version__ = "1.0.0"
__author__ = "StructureTools Phase 2 - Thai Standards Integration"
__description__ = "Thai seismic load calculations per TIS 1301/1302-61"


# Example usage
if __name__ == "__main__":
    print("Thai Seismic Load Calculator - TIS 1301/1302-61")
    print("=" * 50)
    print()
    
    # Create calculator
    calculator = ThaiSeismicLoads()
    
    # Example: Bangkok office building
    building = ThaiBuildingProperties(
        height=60.0,  # 60m high
        weight=50000.0,  # 50,000 kN
        fundamental_period=0,  # Will be estimated
        structural_system=ThaiStructuralSystem.CONCRETE_MOMENT_FRAME,
        importance_category=ThaiSeismicImportance.CATEGORY_I,
        soil_type=ThaiSoilType.SOIL_C
    )
    
    result = calculator.analyze_building_seismic_loads(
        province='กรุงเทพมหานคร',
        building=building
    )
    
    print(f"Seismic Analysis Result for Bangkok Office Building:")
    print(f"Seismic Zone: {result.seismic_zone}")
    print(f"Design Spectral Acceleration (Sds): {result.design_acceleration:.3f}g")
    print(f"Fundamental Period: {building.fundamental_period:.2f} seconds")
    print(f"Base Shear: {result.base_shear:.0f} kN")
    print(f"Base Shear Ratio: {result.base_shear/building.weight:.3f}")
    print()
    
    # Show seismic map summary
    print("Thai Provincial Seismic Zones:")
    seismic_map = calculator.generate_provincial_seismic_map()
    for province, data in list(seismic_map.items())[:5]:  # Show first 5
        print(f"{province}: Zone {data['seismic_zone']} - Sds={data['design_spectral_sds']:.3f}g")
    
    print(f"\nTotal provinces mapped: {len(seismic_map)}")
    print("Thai Seismic Load Calculator ready!")
