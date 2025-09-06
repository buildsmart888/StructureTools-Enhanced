# -*- coding: utf-8 -*-
"""
Load Generation Systems for StructureTools Phase 2 with Thai Standards
======================================================================

This module provides comprehensive load generation capabilities including:
- Wind load generation per ASCE 7-22 and TIS 1311-50 (Thai)
- Seismic load generation per ASCE 7-22/IBC 2021 and TIS 1301/1302-61 (Thai)
- Thai provincial wind and seismic zone mapping
- Ministry Regulation B.E. 2566 compliance (Thai wind loads)
- Dead and live load calculations
- Load combination generation
- Integration with structural analysis

The module serves as the unified interface for all load generation in
StructureTools Phase 2, providing professional-grade loading per current
international and Thai building codes.
"""

# ASCE 7-22 (US) Standards
from .wind_asce7 import (
    ASCE7WindGenerator, ExposureCategory, RiskCategory, BuildingCategory,
    TopographicCondition, WindSiteData, BuildingGeometry, WindPressures,
    WindForces, quick_wind_analysis
)

from .seismic_asce7 import (
    ASCE7SeismicGenerator, SiteClass, SeismicDesignCategory, StructuralSystem,
    SeismicSiteData, BuildingSeismicData, ResponseSpectrum, SeismicForces,
    quick_seismic_analysis
)

# Thai Standards (TIS 1311-50, Ministry Regulation B.E. 2566, TIS 1301/1302-61)
from .thai_load_standards import (
    ThaiLoadStandards, ThaiLoadType, ThaiLoadConfiguration, ThaiLoadResult,
    calculate_thai_loads_quick, get_all_thai_provinces, get_thai_load_zones_map
)

from .thai_wind_loads import (
    ThaiWindLoads, ThaiWindZone, ThaiTerrainCategory, ThaiBuildingImportance,
    ThaiTopographyType, ThaiBuildingGeometry, ThaiWindLoadResult,
    calculate_thai_wind_pressure, get_thailand_wind_zones
)

from .thai_seismic_loads import (
    ThaiSeismicLoads, ThaiSeismicZone, ThaiSoilType, ThaiSeismicImportance,
    ThaiStructuralSystem, ThaiBuildingProperties, ThaiSeismicParameters,
    ThaiSeismicLoadResult, calculate_thai_seismic_force, get_thailand_seismic_zones
)

from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum
import numpy as np

# Import Phase 1 foundation if available
try:
    from ..utils.units_manager import get_units_manager
    STRUCTURETOOLS_AVAILABLE = True
except ImportError:
    STRUCTURETOOLS_AVAILABLE = False


class LoadType(Enum):
    """Types of loads that can be generated"""
    DEAD = "dead"
    LIVE = "live"
    ROOF_LIVE = "roof_live"
    SNOW = "snow"
    WIND = "wind"
    SEISMIC = "seismic"
    # Thai specific load types
    WIND_THAI = "wind_thai"
    SEISMIC_THAI = "seismic_thai"
    COMBINED_THAI = "combined_thai"


class LoadStandard(Enum):
    """Load calculation standards supported"""
    ASCE_7_22 = "asce_7_22"          # US Standard
    IBC_2021 = "ibc_2021"            # US Building Code
    TIS_1311_50 = "tis_1311_50"      # Thai Wind Standard
    MINISTRY_2566 = "ministry_2566"   # Thai Ministry Regulation B.E. 2566
    TIS_1301_61 = "tis_1301_61"      # Thai Seismic Standard
    TIS_1302_61 = "tis_1302_61"      # Thai Seismic Analysis Standard


class LoadCombination(Enum):
    """Standard load combinations per ASCE 7-22 and Thai standards"""
    # Strength Design (LRFD) - ASCE 7-22
    COMBO_1 = "1.4D"
    COMBO_2 = "1.2D + 1.6L + 0.5(Lr or S or R)"
    COMBO_3 = "1.2D + 1.6(Lr or S or R) + (L or 0.5W)"
    COMBO_4 = "1.2D + 1.0W + L + 0.5(Lr or S or R)"
    COMBO_5 = "1.2D + 1.0E + L + 0.2S"
    COMBO_6 = "0.9D + 1.0W"
    COMBO_7 = "0.9D + 1.0E"
    
    # Allowable Stress Design (ASD) - ASCE 7-22
    ASD_1 = "D"
    ASD_2 = "D + L"
    ASD_3 = "D + (Lr or S or R)"
    ASD_4 = "D + 0.75L + 0.75(Lr or S or R)"
    ASD_5 = "D + (0.6W or 0.7E)"
    ASD_6 = "D + 0.75L + 0.75(0.6W)"
    ASD_7 = "D + 0.75L + 0.75(0.7E)"
    ASD_8 = "0.6D + 0.6W"
    ASD_9 = "0.6D + 0.7E"
    
    # Thai Load Combinations - TIS Standards
    THAI_SERVICE_WIND = "D + L + W (Thai)"
    THAI_SERVICE_SEISMIC = "D + 0.5L + E (Thai)"
    THAI_ULTIMATE_WIND = "1.2D + 1.6L + 1.6W (Thai)"
    THAI_ULTIMATE_SEISMIC = "1.2D + 0.5L + 1.0E (Thai)"
    THAI_WIND_SEISMIC_COMBO = "1.2D + 0.5L + 1.0W + 1.0E (Thai)"


@dataclass
class LoadParameters:
    """General load parameters for different load types"""
    # Dead loads (psf or kN/m²)
    dead_floor: float = 25.0          # Typical floor dead load
    dead_roof: float = 20.0           # Typical roof dead load
    
    # Live loads (psf)
    live_floor: float = 50.0          # Typical office live load
    live_roof: float = 20.0           # Typical roof live load
    
    # Snow loads (psf)
    ground_snow: float = 30.0         # Ground snow load
    
    # Material weights (pcf)
    concrete_weight: float = 150.0    # Normal weight concrete
    steel_weight: float = 490.0       # Structural steel


@dataclass
class GeneratedLoads:
    """Container for all generated loads on a structure"""
    # Load values by type
    dead_loads: Dict[str, float]      # Dead load values
    live_loads: Dict[str, float]      # Live load values
    wind_loads: Dict[str, float]      # Wind load values
    seismic_loads: Dict[str, float]   # Seismic load values
    
    # Load combinations
    load_combinations: Dict[str, float]  # Combined load values
    
    # Detailed results
    wind_pressures: Optional[WindPressures] = None
    wind_forces: Optional[WindForces] = None
    seismic_spectrum: Optional[ResponseSpectrum] = None
    seismic_forces: Optional[SeismicForces] = None


class LoadGenerator:
    """
    Master load generator providing unified interface to all load types.
    
    This class integrates wind, seismic, and gravity load generation
    with automatic load combination generation per ASCE 7-22 and Thai standards.
    
    Supports:
    - ASCE 7-22 wind and seismic loads (US)
    - TIS 1311-50 and Ministry Regulation B.E. 2566 wind loads (Thailand)
    - TIS 1301/1302-61 seismic loads (Thailand)
    - Provincial zone mapping for Thailand
    - International and Thai load combinations
    """
    
    def __init__(self):
        """Initialize load generator with all capabilities."""
        # US Standards (ASCE 7-22)
        self.wind_generator = ASCE7WindGenerator()
        self.seismic_generator = ASCE7SeismicGenerator()
        
        # Thai Standards (TIS)
        self.thai_load_system = ThaiLoadStandards()
        
        # Load factors per ASCE 7-22 Section 2.3
        self.lrfd_factors = {
            LoadType.DEAD: 1.2,
            LoadType.LIVE: 1.6,
            LoadType.ROOF_LIVE: 1.6,
            LoadType.SNOW: 1.6,
            LoadType.WIND: 1.0,
            LoadType.SEISMIC: 1.0,
            LoadType.WIND_THAI: 1.6,    # Thai wind factor
            LoadType.SEISMIC_THAI: 1.0  # Thai seismic factor
        }
        
        self.asd_factors = {
            LoadType.DEAD: 1.0,
            LoadType.LIVE: 1.0,
            LoadType.ROOF_LIVE: 1.0,
            LoadType.SNOW: 1.0,
            LoadType.WIND: 0.6,
            LoadType.SEISMIC: 0.7,
            LoadType.WIND_THAI: 1.0,    # Thai wind service factor
            LoadType.SEISMIC_THAI: 1.0  # Thai seismic service factor
        }
        
        # Thai load factors per TIS standards
        self.thai_factors = {
            'service': {
                LoadType.DEAD: 1.0,
                LoadType.LIVE: 1.0,
                LoadType.WIND_THAI: 1.0,
                LoadType.SEISMIC_THAI: 1.0
            },
            'ultimate': {
                LoadType.DEAD: 1.2,
                LoadType.LIVE: 1.6,
                LoadType.WIND_THAI: 1.6,
                LoadType.SEISMIC_THAI: 1.0
            }
        }
    
    def generate_all_loads(self, 
                          # Building geometry
                          length: float, width: float, height: float,
                          # Wind parameters
                          wind_speed: float = None, exposure: ExposureCategory = None,
                          # Seismic parameters  
                          Ss: float = None, S1: float = None, site_class: SiteClass = None,
                          structural_system: StructuralSystem = None,
                          # Thai parameters
                          thai_province: str = None, 
                          thai_terrain: str = "urban",
                          thai_soil: str = "medium",
                          thai_importance: str = "standard",
                          thai_structural_system: str = "concrete_moment_frame",
                          # Load parameters
                          load_params: LoadParameters = None,
                          # Analysis options
                          include_combinations: bool = True,
                          load_standard: LoadStandard = LoadStandard.ASCE_7_22) -> GeneratedLoads:
        """
        Generate all loads for a building including combinations.
        
        Args:
            length, width, height: Building dimensions (ft)
            wind_speed: Basic wind speed (mph)
            exposure: Wind exposure category
            Ss, S1: Seismic ground motion parameters
            site_class: Site classification
            structural_system: Structural system type
            load_params: Load parameter overrides
            include_combinations: Whether to generate load combinations
            
        Returns:
            GeneratedLoads with all load types and combinations
        """
        if load_params is None:
            load_params = LoadParameters()
        
        # Calculate building properties
        floor_area = length * width
        roof_area = length * width
        total_volume = length * width * height
        
        # Estimate building weight
        estimated_weight = self._estimate_building_weight(
            floor_area, height, structural_system, load_params
        )
        
        # Generate gravity loads
        dead_loads = self._generate_dead_loads(floor_area, roof_area, load_params)
        live_loads = self._generate_live_loads(floor_area, roof_area, load_params)
        
        # Generate wind loads
        wind_data = self._generate_wind_loads(
            length, width, height, wind_speed, exposure
        )
        
        # Generate seismic loads
        seismic_data = self._generate_seismic_loads(
            height, estimated_weight, Ss, S1, site_class, structural_system
        )
        
        # Create load dictionary
        loads = GeneratedLoads(
            dead_loads=dead_loads,
            live_loads=live_loads,
            wind_loads=wind_data['loads'],
            seismic_loads=seismic_data['loads'],
            load_combinations={},
            wind_pressures=wind_data.get('pressures'),
            wind_forces=wind_data.get('forces'),
            seismic_spectrum=seismic_data.get('spectrum'),
            seismic_forces=seismic_data.get('forces')
        )
        
        # Generate load combinations if requested
        if include_combinations:
            loads.load_combinations = self._generate_load_combinations(loads)
        
        return loads
    
    def _estimate_building_weight(self, floor_area: float, height: float,
                                 structural_system: StructuralSystem,
                                 load_params: LoadParameters) -> float:
        """Estimate total building seismic weight"""
        
        # Dead load weight
        dead_weight = (load_params.dead_floor * floor_area + 
                      load_params.dead_roof * floor_area)
        
        # Live load weight (reduced for seismic)
        live_weight = 0.25 * load_params.live_floor * floor_area  # 25% of live load
        
        # Structural weight estimate
        if "steel" in structural_system.value or "frame" in structural_system.value:
            structural_weight = 8 * floor_area  # psf for steel frame
        else:
            structural_weight = 15 * floor_area  # psf for concrete/masonry
        
        total_weight = dead_weight + live_weight + structural_weight
        return total_weight
    
    def _generate_dead_loads(self, floor_area: float, roof_area: float,
                           load_params: LoadParameters) -> Dict[str, float]:
        """Generate dead load values"""
        return {
            'floor_dead_load': load_params.dead_floor * floor_area,
            'roof_dead_load': load_params.dead_roof * roof_area,
            'total_dead_load': (load_params.dead_floor * floor_area + 
                               load_params.dead_roof * roof_area)
        }
    
    def _generate_live_loads(self, floor_area: float, roof_area: float,
                           load_params: LoadParameters) -> Dict[str, float]:
        """Generate live load values"""
        return {
            'floor_live_load': load_params.live_floor * floor_area,
            'roof_live_load': load_params.live_roof * roof_area,
            'total_live_load': (load_params.live_floor * floor_area + 
                               load_params.live_roof * roof_area)
        }
    
    def _generate_wind_loads(self, length: float, width: float, height: float,
                           wind_speed: float, exposure: ExposureCategory) -> Dict:
        """Generate wind loads using ASCE 7 wind generator"""
        
        # Create wind site data
        wind_site = WindSiteData(
            V=wind_speed,
            risk_category=RiskCategory.II,
            exposure=exposure
        )
        
        # Create building geometry
        building_geom = BuildingGeometry(
            length=length,
            width=width,
            height=height,
            category=BuildingCategory.ENCLOSED
        )
        
        # Generate wind loads
        pressures, forces = self.wind_generator.generate_wind_loads(wind_site, building_geom)
        
        return {
            'loads': {
                'base_shear': forces.total_base_shear,
                'overturning_moment': forces.overturning_moment,
                'velocity_pressure': pressures.qh,
                'windward_pressure': pressures.net_windward_wall,
                'leeward_pressure': pressures.net_leeward_wall
            },
            'pressures': pressures,
            'forces': forces
        }
    
    def _generate_seismic_loads(self, height: float, weight: float,
                              Ss: float, S1: float, site_class: SiteClass,
                              structural_system: StructuralSystem) -> Dict:
        """Generate seismic loads using ASCE 7 seismic generator"""
        
        # Create seismic site data
        seismic_site = SeismicSiteData(
            latitude=0, longitude=0,  # Would be actual coordinates
            Ss=Ss, S1=S1,
            site_class=site_class
        )
        
        # Create building seismic data
        num_stories = max(1, int(height / 12))  # Assume 12 ft story height
        story_height = height / num_stories
        story_weight = weight / num_stories
        
        building_seismic = BuildingSeismicData(
            height=height,
            weight=weight,
            occupancy_category=RiskCategory.II,
            structural_system=structural_system,
            story_heights=[story_height] * num_stories,
            story_weights=[story_weight] * num_stories
        )
        
        # Generate seismic loads
        spectrum, forces = self.seismic_generator.generate_seismic_loads(seismic_site, building_seismic)
        
        return {
            'loads': {
                'base_shear': forces.V,
                'response_coefficient': forces.Cs,
                'fundamental_period': forces.Ta,
                'SDS': seismic_site.SDS,
                'SD1': seismic_site.SD1
            },
            'spectrum': spectrum,
            'forces': forces
        }
    
    def _generate_load_combinations(self, loads: GeneratedLoads) -> Dict[str, float]:
        """Generate ASCE 7-22 load combinations"""
        
        # Extract load values
        D = loads.dead_loads.get('total_dead_load', 0)
        L = loads.live_loads.get('total_live_load', 0)
        W = loads.wind_loads.get('base_shear', 0)
        E = loads.seismic_loads.get('base_shear', 0)
        
        # LRFD Load Combinations per ASCE 7-22 Section 2.3.2
        combinations = {
            # Basic combinations
            '1.4D': 1.4 * D,
            '1.2D + 1.6L': 1.2 * D + 1.6 * L,
            
            # Wind combinations
            '1.2D + 1.0W + L': 1.2 * D + 1.0 * W + L,
            '0.9D + 1.0W': 0.9 * D + 1.0 * W,
            
            # Seismic combinations
            '1.2D + 1.0E + L': 1.2 * D + 1.0 * E + L,
            '0.9D + 1.0E': 0.9 * D + 1.0 * E,
            
            # Maximum values for design
            'max_gravity': max(1.4 * D, 1.2 * D + 1.6 * L),
            'max_wind': max(1.2 * D + 1.0 * W + L, 0.9 * D + 1.0 * W),
            'max_seismic': max(1.2 * D + 1.0 * E + L, 0.9 * D + 1.0 * E),
            'governing': max(
                1.4 * D,
                1.2 * D + 1.6 * L,
                1.2 * D + 1.0 * W + L,
                0.9 * D + 1.0 * W,
                1.2 * D + 1.0 * E + L,
                0.9 * D + 1.0 * E
            )
        }
        
        return combinations
    
    def generate_thai_loads(self,
                           # Building geometry
                           length: float, width: float, height: float,
                           # Thai parameters
                           province: str,
                           terrain_category: str = "urban",
                           soil_type: str = "medium", 
                           building_importance: str = "standard",
                           structural_system: str = "concrete_moment_frame",
                           topography: str = "flat",
                           # Load parameters
                           building_weight: Optional[float] = None,
                           load_params: LoadParameters = None,
                           # Analysis options
                           include_combinations: bool = True,
                           load_type: ThaiLoadType = ThaiLoadType.COMBINED_WIND_SEISMIC) -> GeneratedLoads:
        """
        Generate loads according to Thai standards (TIS 1311-50, TIS 1301/1302-61)
        
        Args:
            length: Building length (m)
            width: Building width (m) 
            height: Building height (m)
            province: Thai province name (in Thai)
            terrain_category: Terrain category ("open", "rough", "urban", "dense_urban")
            soil_type: Soil type ("very_hard", "hard", "medium", "soft", "very_soft")
            building_importance: Building importance ("standard", "important", "essential", "hazardous")
            structural_system: Structural system type
            topography: Topography type ("flat", "hill", "ridge", "escarpment", "valley")
            building_weight: Building weight (kN), estimated if not provided
            load_params: Load parameters for gravity loads
            include_combinations: Include Thai load combinations
            load_type: Type of Thai load analysis
            
        Returns:
            GeneratedLoads with Thai wind/seismic loads and combinations
        """
        if load_params is None:
            load_params = LoadParameters()
        
        # Calculate building properties
        floor_area = length * width
        roof_area = length * width
        
        # Estimate building weight in kN if not provided
        if building_weight is None:
            # Estimate based on typical Thai construction (15-20 kN/m²)
            building_weight = floor_area * (height / 3.0) * 18.0  # kN
        
        # Generate gravity loads (convert to Thai units if needed)
        dead_loads = self._generate_dead_loads(floor_area, roof_area, load_params)
        live_loads = self._generate_live_loads(floor_area, roof_area, load_params)
        
        # Create Thai load configuration
        thai_config = ThaiLoadConfiguration(
            province=province,
            load_type=load_type,
            building_height=height,
            building_weight=building_weight,
            building_width=width,
            building_depth=length,
            terrain_category=terrain_category,
            soil_type=soil_type,
            building_importance=building_importance,
            structural_system=structural_system,
            topography=topography
        )
        
        # Calculate Thai loads
        thai_result = self.thai_load_system.calculate_combined_loads(thai_config)
        
        # Convert Thai results to GeneratedLoads format
        wind_loads = {}
        seismic_loads = {}
        
        if thai_result.wind_loads:
            wind_loads = {
                'base_shear': thai_result.wind_loads.total_wind_force,  # N
                'velocity_pressure': thai_result.wind_loads.design_wind_pressure,  # Pa
                'basic_wind_speed': thai_result.wind_loads.basic_wind_speed,  # m/s
                'design_wind_speed': thai_result.wind_loads.design_wind_speed,  # m/s
                'wind_zone': thai_result.wind_loads.wind_zone,
                'pressure_coefficients': thai_result.wind_loads.pressure_coefficients,
                'thai_standard': thai_result.wind_loads.calculation_method
            }
        
        if thai_result.seismic_loads:
            seismic_loads = {
                'base_shear': thai_result.seismic_loads.base_shear * 1000,  # Convert kN to N
                'design_acceleration': thai_result.seismic_loads.design_acceleration,  # g
                'response_modification_factor': thai_result.seismic_loads.response_modification_factor,
                'importance_factor': thai_result.seismic_loads.importance_factor,
                'seismic_zone': thai_result.seismic_loads.seismic_zone,
                'fundamental_period': thai_result.seismic_loads.spectral_parameters.ts,  # s
                'thai_standard': thai_result.seismic_loads.calculation_method
            }
        
        # Create GeneratedLoads object
        loads = GeneratedLoads(
            dead_loads=dead_loads,
            live_loads=live_loads,
            wind_loads=wind_loads,
            seismic_loads=seismic_loads,
            load_combinations={}
        )
        
        # Generate Thai load combinations if requested
        if include_combinations:
            loads.load_combinations = self._generate_thai_load_combinations(loads, thai_result)
        
        return loads
    
    def _generate_thai_load_combinations(self, loads: GeneratedLoads, 
                                       thai_result: ThaiLoadResult) -> Dict[str, Dict[str, float]]:
        """Generate load combinations according to Thai standards"""
        combinations = {}
        
        dead_total = sum(loads.dead_loads.values())
        live_total = sum(loads.live_loads.values())
        wind_force = loads.wind_loads.get('base_shear', 0)
        seismic_force = loads.seismic_loads.get('base_shear', 0)
        
        # Thai service load combinations
        combinations['Thai Service - Dead + Live'] = {
            'total': dead_total + live_total,
            'dead': dead_total * 1.0,
            'live': live_total * 1.0,
            'description': 'D + L (Thai Service)'
        }
        
        if wind_force > 0:
            combinations['Thai Service - Wind'] = {
                'total': dead_total + live_total + wind_force,
                'dead': dead_total * 1.0,
                'live': live_total * 1.0,
                'wind': wind_force * 1.0,
                'description': 'D + L + W (Thai Service)'
            }
            
            combinations['Thai Ultimate - Wind'] = {
                'total': dead_total * 1.2 + live_total * 1.6 + wind_force * 1.6,
                'dead': dead_total * 1.2,
                'live': live_total * 1.6,
                'wind': wind_force * 1.6,
                'description': '1.2D + 1.6L + 1.6W (Thai Ultimate)'
            }
        
        if seismic_force > 0:
            combinations['Thai Service - Seismic'] = {
                'total': dead_total + live_total * 0.5 + seismic_force,
                'dead': dead_total * 1.0,
                'live': live_total * 0.5,
                'seismic': seismic_force * 1.0,
                'description': 'D + 0.5L + E (Thai Service)'
            }
            
            combinations['Thai Ultimate - Seismic'] = {
                'total': dead_total * 1.2 + live_total * 0.5 + seismic_force * 1.0,
                'dead': dead_total * 1.2,
                'live': live_total * 0.5,
                'seismic': seismic_force * 1.0,
                'description': '1.2D + 0.5L + 1.0E (Thai Ultimate)'
            }
        
        # Combined wind and seismic (if both present)
        if wind_force > 0 and seismic_force > 0:
            combinations['Thai Combined - Wind + Seismic'] = {
                'total': dead_total * 1.2 + live_total * 0.5 + wind_force * 1.0 + seismic_force * 1.0,
                'dead': dead_total * 1.2,
                'live': live_total * 0.5,
                'wind': wind_force * 1.0,
                'seismic': seismic_force * 1.0,
                'description': '1.2D + 0.5L + 1.0W + 1.0E (Thai Combined)'
            }
        
        return combinations
    
    def get_thai_province_info(self, province: str) -> Dict[str, Any]:
        """Get wind and seismic zone information for a Thai province"""
        return self.thai_load_system.get_province_load_summary(province)
    
    def list_thai_provinces(self) -> List[str]:
        """Get list of all supported Thai provinces"""
        return get_all_thai_provinces()
    
    def generate_load_report(self, loads: GeneratedLoads,
                           building_info: Dict[str, Any] = None,
                           filepath: Optional[str] = None,
                           thai_analysis: bool = False) -> str:
        """Generate comprehensive load analysis report"""
        
        if building_info is None:
            building_info = {}
        
        # Determine if this is Thai analysis
        is_thai = thai_analysis or any('thai' in str(loads.wind_loads.get(k, '')).lower() or 
                                      'tis' in str(loads.wind_loads.get(k, '')).lower() 
                                      for k in loads.wind_loads.keys()) if loads.wind_loads else False
        
        if not is_thai:
            is_thai = any('thai' in str(loads.seismic_loads.get(k, '')).lower() or 
                         'tis' in str(loads.seismic_loads.get(k, '')).lower() 
                         for k in loads.seismic_loads.keys()) if loads.seismic_loads else False
        
        report_lines = [
            "COMPREHENSIVE LOAD ANALYSIS REPORT",
            "StructureTools Phase 2 - Load Generation Systems",
            "=" * 65,
            "",
            "ANALYSIS STANDARDS",
            "-" * 20
        ]
        
        if is_thai:
            report_lines.extend([
                "Dead Loads: ASCE 7-22 Chapter 3 / Thai Building Code",
                "Live Loads: ASCE 7-22 Chapter 4 / Thai Building Code", 
                "Wind Loads: TIS 1311-50 & Ministry Regulation B.E. 2566",
                "Seismic Loads: TIS 1301-61 & TIS 1302-61",
                "Load Combinations: Thai Building Standards",
                "",
                "การวิเคราะห์ตามมาตรฐานไทย (Thai Standards Analysis)",
                "- มยผ. 1311-50: การคำนวณแรงลม",
                "- กฎกระทรวง พ.ศ. 2566: ข้อกำหนดแรงลม", 
                "- มยผ. 1301-61: การออกแบบอาคารต้านทานแผ่นดินไหว",
                "- มยผ. 1302-61: การวิเคราะห์แรงแผ่นดินไหว"
            ])
        else:
            report_lines.extend([
                "Dead Loads: ASCE 7-22 Chapter 3",
                "Live Loads: ASCE 7-22 Chapter 4", 
                "Wind Loads: ASCE 7-22 Chapter 27",
                "Seismic Loads: ASCE 7-22 Chapter 12",
                "Load Combinations: ASCE 7-22 Section 2.3"
            ])
        
        report_lines.extend([
            "",
            "BUILDING INFORMATION",
            "-" * 25
        ])
        
        # Add building info if provided
        for key, value in building_info.items():
            report_lines.append(f"{key}: {value}")
        
        report_lines.extend([
            "",
            "GRAVITY LOADS",
            "-" * 15,
            "Dead Loads:"
        ])
        
        for load_type, value in loads.dead_loads.items():
            unit = "N" if is_thai else "lb"
            report_lines.append(f"  {load_type.replace('_', ' ').title()}: {value:.0f} {unit}")
        
        report_lines.append("\nLive Loads:")
        for load_type, value in loads.live_loads.items():
            unit = "N" if is_thai else "lb"
            report_lines.append(f"  {load_type.replace('_', ' ').title()}: {value:.0f} {unit}")
        
        report_lines.extend([
            "",
            "LATERAL LOADS", 
            "-" * 15,
            "Wind Loads:"
        ])
        
        for load_type, value in loads.wind_loads.items():
            if isinstance(value, (int, float)):
                if is_thai:
                    if "force" in load_type or "shear" in load_type:
                        unit = "N"
                    elif "pressure" in load_type:
                        unit = "Pa"
                    elif "speed" in load_type:
                        unit = "m/s"
                    else:
                        unit = ""
                else:
                    unit = "lb" if "force" in load_type or "shear" in load_type else "psf" if "pressure" in load_type else "lb-ft" if "moment" in load_type else ""
                
                report_lines.append(f"  {load_type.replace('_', ' ').title()}: {value:.1f} {unit}")
            elif isinstance(value, str):
                report_lines.append(f"  {load_type.replace('_', ' ').title()}: {value}")
        
        report_lines.append("\nSeismic Loads:")
        for load_type, value in loads.seismic_loads.items():
            if isinstance(value, (int, float)):
                if is_thai:
                    if "shear" in load_type:
                        unit = "N"
                    elif "period" in load_type:
                        unit = "s"
                    elif "acceleration" in load_type:
                        unit = "g"
                    else:
                        unit = ""
                else:
                    unit = "lb" if "shear" in load_type else "sec" if "period" in load_type else "g" if load_type in ['SDS', 'SD1'] else ""
                
                report_lines.append(f"  {load_type.replace('_', ' ').title()}: {value:.3f} {unit}")
            elif isinstance(value, str):
                report_lines.append(f"  {load_type.replace('_', ' ').title()}: {value}")
        
        if loads.load_combinations:
            report_lines.extend([
                "",
                "LOAD COMBINATIONS (LRFD)",
                "-" * 30
            ])
            
            for combo_name, value in loads.load_combinations.items():
                report_lines.append(f"{combo_name}: {value:.0f} lb")
        
        report_lines.extend([
            "",
            "DESIGN RECOMMENDATIONS",
            "-" * 25,
            "1. Verify all load assumptions with project requirements",
            "2. Consider load path analysis for complex geometries", 
            "3. Check governing load combination for each member",
            "4. Apply appropriate importance factors for occupancy",
            "5. Consider dynamic effects for tall or flexible buildings",
            "",
            "NOTES",
            "-" * 10,
            "- Load values are based on simplified analysis methods",
            "- Detailed analysis may be required for complex structures",
            "- Local building codes may have additional requirements",
            "- Professional engineering judgment required for final design"
        ])
        
        report_content = "\n".join(report_lines)
        
        # Save to file if requested
        if filepath:
            with open(filepath, 'w') as f:
                f.write(report_content)
            print(f"Load analysis report saved to: {filepath}")
        
        return report_content


# Convenience functions for quick load generation
def quick_load_generation(length: float, width: float, height: float,
                         wind_speed: float = 110, exposure: str = "C",
                         Ss: float = 1.0, S1: float = 0.4, site_class: str = "D") -> Dict:
    """Quick load generation with simplified inputs"""
    
    # Convert string inputs to enums
    exposure_map = {'B': ExposureCategory.B, 'C': ExposureCategory.C, 'D': ExposureCategory.D}
    site_class_map = {'A': SiteClass.A, 'B': SiteClass.B, 'C': SiteClass.C, 
                     'D': SiteClass.D, 'E': SiteClass.E}
    
    exposure_enum = exposure_map.get(exposure.upper(), ExposureCategory.C)
    site_class_enum = site_class_map.get(site_class.upper(), SiteClass.D)
    
    # Generate loads
    generator = LoadGenerator()
    loads = generator.generate_all_loads(
        length, width, height,
        wind_speed, exposure_enum,
        Ss, S1, site_class_enum,
        StructuralSystem.SMF  # Default to special moment frame
    )
    
    return {
        'dead_load': loads.dead_loads.get('total_dead_load', 0),
        'live_load': loads.live_loads.get('total_live_load', 0),
        'wind_shear': loads.wind_loads.get('base_shear', 0),
        'seismic_shear': loads.seismic_loads.get('base_shear', 0),
        'governing_combo': loads.load_combinations.get('governing', 0)
    }


# Export main classes and functions
__all__ = [
    # Core load generation
    'LoadGenerator',
    'LoadType',
    'LoadStandard',
    'LoadCombination',
    'LoadParameters',
    'GeneratedLoads',
    'quick_load_generation',
    'quick_thai_load_analysis',
    
    # Wind exports - ASCE 7
    'ASCE7WindGenerator',
    'ExposureCategory',
    'RiskCategory',
    'BuildingCategory',
    'TopographicCondition',
    'WindSiteData',
    'BuildingGeometry',
    'WindPressures',
    'WindForces',
    'quick_wind_analysis',
    
    # Seismic exports - ASCE 7
    'ASCE7SeismicGenerator',
    'SiteClass',
    'SeismicDesignCategory',
    'StructuralSystem',
    'SeismicSiteData',
    'BuildingSeismicData',
    'ResponseSpectrum',
    'SeismicForces',
    'quick_seismic_analysis',
    
    # Thai Standards exports
    'ThaiLoadStandards',
    'ThaiLoadType',
    'ThaiLoadConfiguration',
    'ThaiLoadResult',
    'calculate_thai_loads_quick',
    'get_all_thai_provinces',
    'get_thai_load_zones_map',
    
    # Thai Wind Loads
    'ThaiWindLoads',
    'ThaiWindZone',
    'ThaiTerrainCategory',
    'ThaiBuildingImportance',
    'ThaiTopographyType',
    'ThaiBuildingGeometry',
    'ThaiWindLoadResult',
    'calculate_thai_wind_pressure',
    'get_thailand_wind_zones',
    
    # Thai Seismic Loads
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
__version__ = "2.0.0"
__author__ = "StructureTools Phase 2 Development Team"
__description__ = "Professional load generation systems per ASCE 7-22, IBC 2021, and Thai Standards (TIS 1311-50, TIS 1301/1302-61)"


# Quick access functions
def quick_thai_load_analysis(province: str, building_height: float, 
                           building_width: float = 30.0, building_length: float = 20.0,
                           load_type: str = "combined") -> Dict[str, Any]:
    """Quick Thai load analysis for common cases"""
    generator = LoadGenerator()
    
    thai_loads = generator.generate_thai_loads(
        length=building_length,
        width=building_width, 
        height=building_height,
        province=province,
        load_type=ThaiLoadType.COMBINED_WIND_SEISMIC if load_type == "combined" else 
                  ThaiLoadType.WIND_TIS_1311_50 if load_type == "wind" else 
                  ThaiLoadType.SEISMIC_TIS_1301_61
    )
    
    return {
        'province': province,
        'building_height_m': building_height,
        'wind_force_n': thai_loads.wind_loads.get('base_shear', 0),
        'seismic_force_n': thai_loads.seismic_loads.get('base_shear', 0),
        'wind_zone': thai_loads.wind_loads.get('wind_zone', 'N/A'),
        'seismic_zone': thai_loads.seismic_loads.get('seismic_zone', 'N/A'),
        'thai_combinations': len(thai_loads.load_combinations)
    }


# Example usage
if __name__ == "__main__":
    print("StructureTools Phase 2 - Load Generation Systems")
    print("=" * 55)
    print("")
    
    # Example comprehensive load generation
    print("Example: 100x60x40 ft building with 115 mph wind, high seismicity")
    
    generator = LoadGenerator()
    loads = generator.generate_all_loads(
        length=100, width=60, height=40,
        wind_speed=115, exposure=ExposureCategory.C,
        Ss=1.5, S1=0.6, site_class=SiteClass.D,
        structural_system=StructuralSystem.SMF
    )
    
    print(f"Total Dead Load: {loads.dead_loads['total_dead_load']:.0f} lb")
    print(f"Total Live Load: {loads.live_loads['total_live_load']:.0f} lb")
    print(f"Wind Base Shear: {loads.wind_loads['base_shear']:.0f} lb")
    print(f"Seismic Base Shear: {loads.seismic_loads['base_shear']:.0f} lb")
    print(f"Governing Load Combination: {loads.load_combinations['governing']:.0f} lb")
    print("")
    
    # Quick load generation example
    print("Quick Analysis: 80x50x30 ft building")
    quick_result = quick_load_generation(80, 50, 30)
    print(f"Wind Shear: {quick_result['wind_shear']:.0f} lb")
    print(f"Seismic Shear: {quick_result['seismic_shear']:.0f} lb")
    print("")
    
    print("Load Generation Systems ready for StructureTools Phase 2!")
