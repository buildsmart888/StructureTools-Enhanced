# -*- coding: utf-8 -*-
"""
Thai Wind Loads Calculator - TIS 1311-50 & Ministry Regulation B.E. 2566
========================================================================

Implementation of Thai wind load calculations according to:
- TIS 1311-50: Thai Industrial Standard for Wind Load Calculation and Building Response
- Ministry Regulation B.E. 2566 Chapter 4: Wind Load Requirements
- Provincial wind zones with specific wind speeds

การคำนวณแรงลมประเทศไทยตาม:
- มยผ. 1311-50: มาตรฐานการคำนวณแรงลมและการตอบสนองของอาคาร  
- กฎกระทรวง พ.ศ. 2566 หมวด 4: ข้อกำหนดแรงลม
- โซนลมตามจังหวัดพร้อมความเร็วลมเฉพาะ

Integration with StructureTools Phase 2 Load Generation Systems
"""

import math
from typing import Dict, Any, Optional, List, Tuple, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

# Integration with existing load system
try:
    # Try relative import first
    from . import GeneratedLoads, WindLoads
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


class ThaiWindZone(Enum):
    """Thai wind zones according to TIS 1311-50"""
    ZONE_1 = "1"  # ภาคเหนือ / Northern regions - 30 m/s
    ZONE_2 = "2"  # ภาคกลาง / Central regions - 25 m/s
    ZONE_3 = "3"  # ภาคใต้ / Southern regions - 35 m/s
    ZONE_4 = "4"  # พื้นที่ชายฝั่ง / Coastal areas - 40 m/s


class ThaiTerrainCategory(Enum):
    """Thai terrain categories according to TIS 1311-50"""
    CATEGORY_I = "I"      # ภูมิประเทศเปิด / Open terrain
    CATEGORY_II = "II"    # ภูมิประเทศขรุขระ / Rough terrain
    CATEGORY_III = "III"  # ภูมิประเทศเมือง / Urban terrain
    CATEGORY_IV = "IV"    # ภูมิประเทศเมืองหนาแน่น / Dense urban terrain


class ThaiBuildingImportance(Enum):
    """Thai building importance categories per Ministry Regulation B.E. 2566"""
    STANDARD = "standard"      # อาคารทั่วไป / Standard buildings
    IMPORTANT = "important"    # อาคารสำคัญ / Important buildings  
    ESSENTIAL = "essential"    # อาคารจำเป็น / Essential facilities
    HAZARDOUS = "hazardous"    # อาคารอันตราย / Hazardous facilities


class ThaiTopographyType(Enum):
    """Thai topography types for wind calculations"""
    FLAT = "flat"              # ที่ราบ / Flat terrain
    HILL = "hill"              # เนินเขา / Hill
    RIDGE = "ridge"            # สันเขา / Ridge
    ESCARPMENT = "escarpment"  # หน้าผา / Escarpment
    VALLEY = "valley"          # หุบเขา / Valley


@dataclass
class ThaiBuildingGeometry:
    """Thai building geometry parameters for wind analysis"""
    height: float                           # ความสูง m / Height (m)
    width: float                           # ความกว้าง m / Width (m)
    depth: float                           # ความลึก m / Depth (m)
    roof_angle: float = 0.0                # มุมหลังคา องศา / Roof angle (degrees)
    building_type: str = "rectangular"     # ประเภทอาคาร / Building type
    exposure_category: ThaiTerrainCategory = ThaiTerrainCategory.CATEGORY_III


@dataclass
class ThaiWindLoadResult:
    """Thai wind load calculation result"""
    design_wind_pressure: float         # แรงดันลมออกแบบ Pa / Design wind pressure (Pa)
    design_wind_speed: float           # ความเร็วลมออกแบบ m/s / Design wind speed (m/s)
    basic_wind_speed: float            # ความเร็วลมพื้นฐาน m/s / Basic wind speed (m/s)
    terrain_factor: float              # ค่าประกอบภูมิประเทศ / Terrain factor
    topographic_factor: float          # ค่าประกอบภูมิทัศน์ / Topographic factor
    importance_factor: float           # ค่าประกอบความสำคัญ / Importance factor
    pressure_coefficients: Dict[str, float]  # ค่าสัมประสิทธิ์แรงดัน / Pressure coefficients
    total_wind_force: float            # แรงลมรวม N / Total wind force (N)
    wind_zone: str                     # โซนลม / Wind zone
    province: str                      # จังหวัด / Province
    description_thai: str              # คำอธิบายไทย / Thai description
    description_english: str           # คำอธิบายอังกฤษ / English description
    calculation_method: str            # วิธีการคำนวณ / Calculation method
    reference: str                     # อ้างอิง / Reference standard


class ThaiWindLoads:
    """
    Thai Wind Loads Calculator - TIS 1311-50 & Ministry Regulation B.E. 2566
    
    เครื่องคำนวณแรงลมไทย - มยผ. 1311-50 และกฎกระทรวง พ.ศ. 2566
    
    Features:
    - Provincial wind zone mapping (โซนลมตามจังหวัด)
    - TIS 1311-50 calculation procedures
    - Ministry Regulation B.E. 2566 compliance
    - Building importance factors
    - Terrain and topographic effects
    """
    
    def __init__(self):
        """Initialize Thai wind loads calculator"""
        
        # Basic wind speeds by zone (m/s) according to TIS 1311-50
        self.basic_wind_speeds = {
            ThaiWindZone.ZONE_1: 30.0,  # ภาคเหนือ / Northern Thailand
            ThaiWindZone.ZONE_2: 25.0,  # ภาคกลาง / Central Thailand
            ThaiWindZone.ZONE_3: 35.0,  # ภาคใต้ / Southern Thailand
            ThaiWindZone.ZONE_4: 40.0   # พื้นที่ชายฝั่ง / Coastal areas
        }
        
        # Terrain parameters according to TIS 1311-50
        self.terrain_parameters = {
            ThaiTerrainCategory.CATEGORY_I: {
                'name_thai': 'ภูมิประเทศเปิด',
                'name_english': 'Open terrain',
                'description_thai': 'แหล่งน้ำขนาดใหญ่ พื้นที่เปิดโล่ง',
                'description_english': 'Large water bodies, open flat terrain',
                'z0': 0.03, 'zmin': 10, 'alpha': 0.12
            },
            ThaiTerrainCategory.CATEGORY_II: {
                'name_thai': 'ภูมิประเทศขรุขระ',
                'name_english': 'Rough terrain',
                'description_thai': 'ที่โล่งมีสิ่งกีดขวางกระจายอยู่',
                'description_english': 'Open terrain with scattered obstructions',
                'z0': 0.3, 'zmin': 15, 'alpha': 0.16
            },
            ThaiTerrainCategory.CATEGORY_III: {
                'name_thai': 'ภูมิประเทศเมือง',
                'name_english': 'Urban terrain',
                'description_thai': 'ชานเมือง เมืองเล็ก',
                'description_english': 'Suburban areas, small towns',
                'z0': 1.0, 'zmin': 20, 'alpha': 0.22
            },
            ThaiTerrainCategory.CATEGORY_IV: {
                'name_thai': 'ภูมิประเทศเมืองหนาแน่น',
                'name_english': 'Dense urban terrain',
                'description_thai': 'เขตเมืองหนาแน่น ใจกลางเมือง',
                'description_english': 'Dense urban areas, city centers',
                'z0': 2.5, 'zmin': 30, 'alpha': 0.30
            }
        }
        
        # Importance factors according to Ministry Regulation B.E. 2566
        self.importance_factors = {
            ThaiBuildingImportance.STANDARD: {
                'factor': 1.0,
                'description_thai': 'อาคารทั่วไป',
                'description_english': 'Standard buildings',
                'examples_thai': 'อาคารที่อยู่อาศัย อาคารสำนักงาน',
                'examples_english': 'Residential buildings, office buildings'
            },
            ThaiBuildingImportance.IMPORTANT: {
                'factor': 1.15,
                'description_thai': 'อาคารสำคัญ',
                'description_english': 'Important buildings',
                'examples_thai': 'โรงเรียน โรงพยาบาล อาคารชุมนุม',
                'examples_english': 'Schools, hospitals, assembly buildings'
            },
            ThaiBuildingImportance.ESSENTIAL: {
                'factor': 1.25,
                'description_thai': 'อาคารจำเป็น',
                'description_english': 'Essential facilities',
                'examples_thai': 'สิ่งอำนวยความสะดวกฉุกเฉิน โรงไฟฟ้า',
                'examples_english': 'Emergency facilities, power plants'
            },
            ThaiBuildingImportance.HAZARDOUS: {
                'factor': 1.25,
                'description_thai': 'อาคารอันตราย',
                'description_english': 'Hazardous facilities',
                'examples_thai': 'โรงงานเคมี คลังเก็บสารพิษ',
                'examples_english': 'Chemical plants, toxic storage facilities'
            }
        }
        
        # Pressure coefficients for different building shapes
        self.pressure_coefficients = {
            'rectangular_building': {
                'windward_wall': 0.8, 'leeward_wall': -0.5,
                'side_walls': -0.7, 'flat_roof': -0.7
            },
            'low_rise_building': {
                'windward_wall': 0.8, 'leeward_wall': -0.5,
                'side_walls': -0.7, 'roof_windward': -0.7, 'roof_leeward': -0.3
            }
        }
        
        # Topographic factors
        self.topographic_factors = {
            ThaiTopographyType.FLAT: 1.0, ThaiTopographyType.HILL: 1.1,
            ThaiTopographyType.RIDGE: 1.15, ThaiTopographyType.ESCARPMENT: 1.2,
            ThaiTopographyType.VALLEY: 0.9
        }
        
        # Thai provinces and their wind zones
        self.province_wind_zones = self._initialize_province_zones()
    
    def _initialize_province_zones(self) -> Dict[str, ThaiWindZone]:
        """Initialize Thai province wind zone mapping"""
        return {
            # Northern Thailand (Zone 1) - 30 m/s
            'เชียงใหม่': ThaiWindZone.ZONE_1, 'เชียงราย': ThaiWindZone.ZONE_1,
            'ลำปาง': ThaiWindZone.ZONE_1, 'ลำพูน': ThaiWindZone.ZONE_1,
            'แม่ฮ่องสอน': ThaiWindZone.ZONE_1, 'น่าน': ThaiWindZone.ZONE_1,
            'พะเยา': ThaiWindZone.ZONE_1, 'แพร่': ThaiWindZone.ZONE_1,
            
            # Central Thailand (Zone 2) - 25 m/s
            'กรุงเทพมหานคร': ThaiWindZone.ZONE_2, 'นนทบุรี': ThaiWindZone.ZONE_2,
            'ปทุมธานี': ThaiWindZone.ZONE_2, 'สมุทรปราการ': ThaiWindZone.ZONE_2,
            'นครปฐม': ThaiWindZone.ZONE_2, 'ราชบุรี': ThaiWindZone.ZONE_2,
            'กาญจนบุรี': ThaiWindZone.ZONE_2, 'เพชรบุรี': ThaiWindZone.ZONE_2,
            'ลพบุรี': ThaiWindZone.ZONE_2, 'สระบุรี': ThaiWindZone.ZONE_2,
            'อยุธยา': ThaiWindZone.ZONE_2, 'อ่างทอง': ThaiWindZone.ZONE_2,
            'สิงห์บุรี': ThaiWindZone.ZONE_2, 'ชัยนาท': ThaiWindZone.ZONE_2,
            'สุพรรณบุรี': ThaiWindZone.ZONE_2, 'นครนายก': ThaiWindZone.ZONE_2,
            'ปราจีนบุรี': ThaiWindZone.ZONE_2, 'สมุทรสาคร': ThaiWindZone.ZONE_2,
            'สมุทรสงคราม': ThaiWindZone.ZONE_2,
            
            # Northeastern Thailand (Zone 2) - 25 m/s
            'นครราชสีมา': ThaiWindZone.ZONE_2, 'ขอนแก่น': ThaiWindZone.ZONE_2,
            'อุดรธานี': ThaiWindZone.ZONE_2, 'อุบลราชธานี': ThaiWindZone.ZONE_2,
            'สกลนคร': ThaiWindZone.ZONE_2, 'นครพนม': ThaiWindZone.ZONE_2,
            'มุกดาหาร': ThaiWindZone.ZONE_2, 'เลย': ThaiWindZone.ZONE_2,
            'หนองคาย': ThaiWindZone.ZONE_2, 'บึงกาฬ': ThaiWindZone.ZONE_2,
            'ร้อยเอ็ด': ThaiWindZone.ZONE_2, 'กาฬสินธุ์': ThaiWindZone.ZONE_2,
            'มหาสารคาม': ThaiWindZone.ZONE_2, 'ยโสธร': ThaiWindZone.ZONE_2,
            'อำนาจเจริญ': ThaiWindZone.ZONE_2, 'บุรีรัมย์': ThaiWindZone.ZONE_2,
            'สุรินทร์': ThaiWindZone.ZONE_2, 'ศีสะเกษ': ThaiWindZone.ZONE_2,
            'ชัยภูมิ': ThaiWindZone.ZONE_2, 'หนองบัวลำภู': ThaiWindZone.ZONE_2,
            
            # Eastern Thailand (Zone 4) - 40 m/s (Coastal)
            'ชลบุรี': ThaiWindZone.ZONE_4, 'ระยอง': ThaiWindZone.ZONE_4,
            'จันทบุรี': ThaiWindZone.ZONE_4, 'ตราด': ThaiWindZone.ZONE_4,
            'สระแก้ว': ThaiWindZone.ZONE_2,  # Inland
            
            # Southern Thailand (Zone 3 & 4)
            'สุราษฎร์ธานี': ThaiWindZone.ZONE_3, 'นครศรีธรรมราช': ThaiWindZone.ZONE_3,
            'กระบี่': ThaiWindZone.ZONE_4, 'ภูเก็ต': ThaiWindZone.ZONE_4,
            'สงขลา': ThaiWindZone.ZONE_4, 'สตูล': ThaiWindZone.ZONE_4,
            'ตรัง': ThaiWindZone.ZONE_4, 'พัทลุง': ThaiWindZone.ZONE_3,
            'ปัตตานี': ThaiWindZone.ZONE_4, 'ยะลา': ThaiWindZone.ZONE_4,
            'นราธิวาส': ThaiWindZone.ZONE_4, 'ชุมพร': ThaiWindZone.ZONE_4,
            'ระนอง': ThaiWindZone.ZONE_4, 'พังงา': ThaiWindZone.ZONE_4,
            
            # Western Thailand (Zone 2)
            'ตาก': ThaiWindZone.ZONE_2, 'กาญจนบุรี': ThaiWindZone.ZONE_2,
            'เพชรบุรี': ThaiWindZone.ZONE_2, 'ประจุวบคีรีขันธ์': ThaiWindZone.ZONE_4
        }
    
    def get_wind_zone_for_province(self, province: str) -> Tuple[ThaiWindZone, float, str]:
        """Get wind zone information for a Thai province"""
        if province in self.province_wind_zones:
            zone = self.province_wind_zones[province]
            wind_speed = self.basic_wind_speeds[zone]
            description = f"Zone {zone.value} - {province}"
            return zone, wind_speed, description
        else:
            # Default to Zone 2 if province not found
            zone = ThaiWindZone.ZONE_2
            wind_speed = self.basic_wind_speeds[zone]
            description = f"Zone {zone.value} - Default (Province not found)"
            return zone, wind_speed, description
    
    def calculate_terrain_factor(self, height: float, terrain: ThaiTerrainCategory) -> float:
        """Calculate terrain exposure factor according to TIS 1311-50"""
        params = self.terrain_parameters[terrain]
        h = max(height, params['zmin'])
        
        if terrain == ThaiTerrainCategory.CATEGORY_I:
            kr = (h / 10.0) ** params['alpha']
        else:
            z0 = params['z0']
            kr = 0.85 * (h / 10.0) ** (0.22 + 0.07 * math.log(z0))
        
        return min(kr, 2.0)  # Limit maximum factor
    
    def calculate_design_wind_pressure(self, basic_wind_speed: float, height: float,
                                     terrain: ThaiTerrainCategory, 
                                     building_importance: ThaiBuildingImportance,
                                     topography: ThaiTopographyType = ThaiTopographyType.FLAT) -> float:
        """Calculate design wind pressure according to TIS 1311-50"""
        kr = self.calculate_terrain_factor(height, terrain)
        kt = self.topographic_factors[topography]
        ki = self.importance_factors[building_importance]['factor']
        
        design_wind_speed = basic_wind_speed * kr * kt * ki
        air_density = 1.225  # kg/m³ at sea level
        design_pressure = 0.5 * air_density * (design_wind_speed ** 2)
        
        return design_pressure  # Pa
    
    def analyze_building_wind_loads(self, province: str, building_geometry: ThaiBuildingGeometry,
                                  building_importance: ThaiBuildingImportance,
                                  topography: ThaiTopographyType = ThaiTopographyType.FLAT) -> ThaiWindLoadResult:
        """Complete wind load analysis for a building according to Thai standards"""
        zone, basic_wind_speed, zone_desc = self.get_wind_zone_for_province(province)
        
        design_pressure = self.calculate_design_wind_pressure(
            basic_wind_speed, building_geometry.height, 
            building_geometry.exposure_category, building_importance, topography
        )
        
        kr = self.calculate_terrain_factor(building_geometry.height, building_geometry.exposure_category)
        kt = self.topographic_factors[topography]
        ki = self.importance_factors[building_importance]['factor']
        design_wind_speed = basic_wind_speed * kr * kt * ki
        
        building_shape = 'low_rise_building' if building_geometry.height <= 18 else 'rectangular_building'
        pressure_coeffs = self.pressure_coefficients[building_shape].copy()
        
        windward_area = building_geometry.height * building_geometry.width
        cp_windward = pressure_coeffs.get('windward_wall', 0.8)
        total_force = design_pressure * cp_windward * windward_area
        
        importance_info = self.importance_factors[building_importance]
        description_thai = f"การวิเคราะห์แรงลมสำหรับ{importance_info['description_thai']}ในจังหวัด{province}"
        description_english = f"Wind analysis for {importance_info['description_english']} in {province}"
        
        return ThaiWindLoadResult(
            design_wind_pressure=design_pressure,
            design_wind_speed=design_wind_speed,
            basic_wind_speed=basic_wind_speed,
            terrain_factor=kr,
            topographic_factor=kt,
            importance_factor=ki,
            pressure_coefficients=pressure_coeffs,
            total_wind_force=total_force,
            wind_zone=zone.value,
            province=province,
            description_thai=description_thai,
            description_english=description_english,
            calculation_method="TIS 1311-50 + Ministry Regulation B.E. 2566",
            reference="มยผ. 1311-50 และ กฎกระทรวง พ.ศ. 2566"
        )
    
    def get_wind_load_summary(self, province: str, building_height: float,
                            building_importance: ThaiBuildingImportance = ThaiBuildingImportance.STANDARD) -> Dict[str, Any]:
        """Get quick wind load summary for a province"""
        zone, basic_speed, zone_desc = self.get_wind_zone_for_province(province)
        terrain = ThaiTerrainCategory.CATEGORY_III
        
        design_pressure = self.calculate_design_wind_pressure(
            basic_speed, building_height, terrain, building_importance
        )
        
        force_per_sqm = design_pressure * 0.8  # Windward wall coefficient
        
        return {
            'province': province,
            'wind_zone': zone.value,
            'zone_description': zone_desc,
            'basic_wind_speed_ms': basic_speed,
            'basic_wind_speed_kmh': basic_speed * 3.6,
            'design_pressure_pa': design_pressure,
            'design_pressure_kpa': design_pressure / 1000,
            'force_per_sqm_n': force_per_sqm,
            'force_per_sqm_kgf': force_per_sqm / 9.80665,
            'building_height_m': building_height,
            'importance_category': building_importance.value,
            'calculation_standard': 'TIS 1311-50 + Ministry Regulation B.E. 2566'
        }
    
    def generate_provincial_wind_map(self) -> Dict[str, Dict[str, Any]]:
        """Generate comprehensive wind map for all Thai provinces"""
        wind_map = {}
        
        for province, zone in self.province_wind_zones.items():
            basic_speed = self.basic_wind_speeds[zone]
            
            # Calculate for standard 25m building
            standard_height = 25.0
            standard_terrain = ThaiTerrainCategory.CATEGORY_III
            standard_importance = ThaiBuildingImportance.STANDARD
            
            design_pressure = self.calculate_design_wind_pressure(
                basic_speed, standard_height, standard_terrain, standard_importance
            )
            
            wind_map[province] = {
                'wind_zone': zone.value,
                'basic_wind_speed_ms': basic_speed,
                'basic_wind_speed_kmh': basic_speed * 3.6,
                'design_pressure_25m_kpa': design_pressure / 1000,
                'region': self._get_region_for_zone(zone),
                'coastal': zone in [ThaiWindZone.ZONE_4]
            }
        
        return wind_map
    
    def _get_region_for_zone(self, zone: ThaiWindZone) -> str:
        """Get region description for wind zone"""
        region_map = {
            ThaiWindZone.ZONE_1: 'ภาคเหนือ (Northern)',
            ThaiWindZone.ZONE_2: 'ภาคกลาง/ภาคตะวันออกเฉียงเหนือ (Central/Northeast)',
            ThaiWindZone.ZONE_3: 'ภาคใต้ (Southern)',
            ThaiWindZone.ZONE_4: 'พื้นที่ชายฝั่ง (Coastal areas)'
        }
        return region_map.get(zone, 'ไม่ระบุ (Unknown)')
    
    def convert_to_structuretools_format(self, thai_result: ThaiWindLoadResult) -> Dict[str, Any]:
        """Convert Thai wind load result to StructureTools format"""
        if not STRUCTURETOOLS_INTEGRATION:
            return None
        
        # Convert to StructureTools WindLoads format
        wind_loads = {
            'base_shear': thai_result.total_wind_force,
            'velocity_pressure': thai_result.design_wind_pressure,
            'external_pressure': thai_result.design_wind_pressure * 0.8,  # Windward
            'internal_pressure': thai_result.design_wind_pressure * 0.18,  # Internal
            'force_coefficients': thai_result.pressure_coefficients,
            'exposure_category': thai_result.province,
            'basic_wind_speed': thai_result.basic_wind_speed,
            'design_wind_speed': thai_result.design_wind_speed,
            'importance_factor': thai_result.importance_factor,
            'terrain_factor': thai_result.terrain_factor,
            'topographic_factor': thai_result.topographic_factor,
            'calculation_method': thai_result.calculation_method,
            'code_reference': thai_result.reference,
            'thai_wind_zone': thai_result.wind_zone,
            'thai_province': thai_result.province
        }
        
        return wind_loads


# Quick access functions for common calculations
def calculate_thai_wind_pressure(province: str, building_height: float, 
                               building_importance: str = "standard",
                               terrain: str = "urban") -> float:
    """Quick function to calculate Thai wind pressure for a province"""
    calculator = ThaiWindLoads()
    
    # Convert string inputs to enums
    importance_map = {
        'standard': ThaiBuildingImportance.STANDARD,
        'important': ThaiBuildingImportance.IMPORTANT,
        'essential': ThaiBuildingImportance.ESSENTIAL,
        'hazardous': ThaiBuildingImportance.HAZARDOUS
    }
    
    terrain_map = {
        'open': ThaiTerrainCategory.CATEGORY_I,
        'rough': ThaiTerrainCategory.CATEGORY_II,
        'urban': ThaiTerrainCategory.CATEGORY_III,
        'dense_urban': ThaiTerrainCategory.CATEGORY_IV
    }
    
    zone, basic_speed, _ = calculator.get_wind_zone_for_province(province)
    design_pressure = calculator.calculate_design_wind_pressure(
        basic_speed, building_height, 
        terrain_map.get(terrain, ThaiTerrainCategory.CATEGORY_III),
        importance_map.get(building_importance, ThaiBuildingImportance.STANDARD)
    )
    
    return design_pressure


def get_thailand_wind_zones() -> Dict[str, str]:
    """Get mapping of Thai provinces to wind zones"""
    calculator = ThaiWindLoads()
    return {province: zone.value for province, zone in calculator.province_wind_zones.items()}


# Export main classes and functions
__all__ = [
    'ThaiWindLoads',
    'ThaiWindZone',
    'ThaiTerrainCategory', 
    'ThaiBuildingImportance',
    'ThaiTopographyType',
    'ThaiBuildingGeometry',
    'ThaiWindLoadResult',
    'calculate_thai_wind_pressure',
    'get_thailand_wind_zones'
]


# Module information
__version__ = "1.0.0"
__author__ = "StructureTools Phase 2 - Thai Standards Integration"
__description__ = "Thai wind load calculations per TIS 1311-50 & Ministry Regulation B.E. 2566"


# Example usage
if __name__ == "__main__":
    print("Thai Wind Load Calculator - TIS 1311-50 & Ministry Regulation B.E. 2566")
    print("=" * 70)
    print()
    
    # Create calculator
    calculator = ThaiWindLoads()
    
    # Example: Bangkok office building
    building = ThaiBuildingGeometry(
        height=50.0,  # 50m high
        width=30.0,   # 30m wide
        depth=20.0,   # 20m deep
        exposure_category=ThaiTerrainCategory.CATEGORY_III
    )
    
    result = calculator.analyze_building_wind_loads(
        province='กรุงเทพมหานคร',
        building_geometry=building,
        building_importance=ThaiBuildingImportance.STANDARD
    )
    
    print(f"Analysis Result for Bangkok Office Building:")
    print(f"Wind Zone: {result.wind_zone}")
    print(f"Basic Wind Speed: {result.basic_wind_speed:.1f} m/s")
    print(f"Design Wind Pressure: {result.design_wind_pressure:.1f} Pa")
    print(f"Total Wind Force: {result.total_wind_force:.0f} N")
    print()
    
    # Show wind map summary
    print("Thai Provincial Wind Zones:")
    wind_map = calculator.generate_provincial_wind_map()
    for province, data in list(wind_map.items())[:5]:  # Show first 5
        print(f"{province}: Zone {data['wind_zone']} - {data['basic_wind_speed_ms']:.0f} m/s")
    
    print(f"\nTotal provinces mapped: {len(wind_map)}")
    print("Thai Wind Load Calculator ready!")
