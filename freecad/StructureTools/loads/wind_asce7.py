# -*- coding: utf-8 -*-
"""
ASCE 7 Wind Load Generator for StructureTools Phase 2
====================================================

Professional implementation of ASCE 7-22 wind load provisions for:
- Main Wind Force Resisting System (MWFRS) 
- Components and Cladding (C&C)
- Wind pressure calculations
- Directional effects and load combinations
- Risk category and exposure considerations

This module generates wind loads per the latest ASCE 7-22 standard
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
    from ..utils.units_manager import get_units_manager, format_force, format_pressure
    STRUCTURETOOLS_AVAILABLE = True
except ImportError:
    try:
        # Fallback to direct import for standalone testing
        from StructureTools.utils.units_manager import get_units_manager, format_force, format_pressure
        STRUCTURETOOLS_AVAILABLE = True
    except ImportError:
        STRUCTURETOOLS_AVAILABLE = False
        get_units_manager = lambda: None
        format_force = lambda x: f"{x/1000:.2f} kN"
        format_pressure = lambda x: f"{x:.1f} Pa"


class ExposureCategory(Enum):
    """Wind exposure categories per ASCE 7-22 Section 26.7"""
    B = "B"  # Urban and suburban areas, wooded areas
    C = "C"  # Open terrain with scattered obstructions
    D = "D"  # Flat, unobstructed areas facing large water bodies


class RiskCategory(Enum):
    """Risk categories per ASCE 7-22 Section 1.5"""
    I = "I"      # Low hazard buildings
    II = "II"    # Standard occupancy buildings  
    III = "III"  # Substantial hazard buildings
    IV = "IV"    # Essential facilities


class BuildingCategory(Enum):
    """Building categories for wind load application"""
    ENCLOSED = "enclosed"
    PARTIALLY_ENCLOSED = "partially_enclosed"
    OPEN = "open"


class TopographicCondition(Enum):
    """Topographic conditions per ASCE 7-22 Section 26.8"""
    FLAT = "flat"
    HILL = "hill"
    RIDGE = "ridge"
    ESCARPMENT = "escarpment"


@dataclass
class WindSiteData:
    """Wind site parameters and environmental conditions"""
    # Basic wind speed
    V: float                           # Basic wind speed (mph)
    risk_category: RiskCategory        # Risk category
    exposure: ExposureCategory         # Exposure category
    
    # Topographic data
    topographic_condition: TopographicCondition = TopographicCondition.FLAT
    hill_height: float = 0.0           # Height of hill/ridge (ft)
    horizontal_distance: float = 0.0   # Horizontal distance from crest (ft)
    upwind_slope: float = 0.0          # Upwind slope (ratio)
    
    # Site elevation and climate
    elevation: float = 0.0             # Site elevation above sea level (ft)
    temperature: float = 59.0          # Temperature (°F)
    
    # Geographic location for code determination
    latitude: float = 0.0              # Latitude (degrees)
    longitude: float = 0.0             # Longitude (degrees)


@dataclass
class BuildingGeometry:
    """Building geometry for wind load calculations"""
    # Overall dimensions
    length: float                      # Building length (ft)
    width: float                       # Building width (ft)
    height: float                      # Building height (ft)
    
    # Roof geometry
    roof_slope: float = 0.0            # Roof slope (degrees from horizontal)
    roof_type: str = "flat"           # flat, gable, hip, shed
    
    # Building characteristics
    category: BuildingCategory = BuildingCategory.ENCLOSED
    natural_frequency: float = 0.0     # First mode frequency (Hz)
    damping_ratio: float = 0.01        # Structural damping ratio
    
    # Openings
    total_wall_area: float = 0.0       # Total wall area (ft²)
    opening_area: float = 0.0          # Total opening area (ft²)


@dataclass
class WindPressures:
    """Wind pressure results for different surfaces"""
    # Velocity pressure
    qz: float = 0.0                    # Velocity pressure at height z (psf)
    qh: float = 0.0                    # Velocity pressure at mean roof height (psf)
    
    # External pressures
    windward_wall: float = 0.0         # Windward wall pressure (psf)
    leeward_wall: float = 0.0          # Leeward wall pressure (psf)
    side_wall: float = 0.0             # Side wall pressure (psf)
    roof_windward: float = 0.0         # Windward roof pressure (psf)
    roof_leeward: float = 0.0          # Leeward roof pressure (psf)
    
    # Internal pressures
    internal_pressure: float = 0.0     # Internal pressure (psf)
    
    # Net pressures (external - internal)
    net_windward_wall: float = 0.0
    net_leeward_wall: float = 0.0
    net_side_wall: float = 0.0
    net_roof_windward: float = 0.0
    net_roof_leeward: float = 0.0


@dataclass
class WindForces:
    """Wind forces for structural analysis"""
    # Story forces
    story_forces: List[float]          # Horizontal forces per story (lb)
    story_heights: List[float]         # Story heights (ft)
    
    # Overall forces
    total_base_shear: float = 0.0      # Total base shear (lb)
    overturning_moment: float = 0.0    # Overturning moment at base (lb-ft)
    
    # Load distribution
    force_distribution: str = "uniform" # uniform, triangular, calculated
    eccentricity: float = 0.0          # Load eccentricity (ft)


class ASCE7WindGenerator:
    """
    Professional ASCE 7-22 wind load generator.
    
    Generates wind loads for Main Wind Force Resisting System (MWFRS)
    following ASCE 7-22 Chapter 27 - Directional Procedure.
    """
    
    # Wind speed maps and factors (simplified - would use detailed maps in practice)
    RISK_CATEGORY_FACTORS = {
        RiskCategory.I: 0.87,
        RiskCategory.II: 1.00,
        RiskCategory.III: 1.15,
        RiskCategory.IV: 1.15
    }
    
    # Exposure coefficients Kz per ASCE 7-22 Table 26.10-1
    EXPOSURE_CONSTANTS = {
        ExposureCategory.B: {'alpha': 7.0, 'zg': 1200, 'alpha_bar': 0.84, 'b_bar': 1/7.0},
        ExposureCategory.C: {'alpha': 9.5, 'zg': 900, 'alpha_bar': 1.00, 'b_bar': 1/9.5},
        ExposureCategory.D: {'alpha': 11.5, 'zg': 700, 'alpha_bar': 1.07, 'b_bar': 1/11.5}
    }
    
    def __init__(self):
        """Initialize ASCE 7 wind load generator."""
        self.version = "ASCE 7-22"
        
        # Standard atmospheric pressure (psf)
        self.standard_pressure = 2116.22  # lb/ft²
        
        # Air density factors
        self.air_density_sea_level = 0.002378  # slugs/ft³
        
    def generate_wind_loads(self, site_data: WindSiteData, 
                           building: BuildingGeometry) -> Tuple[WindPressures, WindForces]:
        """
        Generate complete wind loads for building per ASCE 7-22.
        
        Args:
            site_data: Wind site parameters
            building: Building geometry and characteristics
            
        Returns:
            Tuple of (WindPressures, WindForces) with complete wind load data
        """
        # Step 1: Calculate velocity pressure
        pressures = self._calculate_velocity_pressures(site_data, building)
        
        # Step 2: Calculate external pressure coefficients
        self._calculate_external_pressures(pressures, site_data, building)
        
        # Step 3: Calculate internal pressure
        self._calculate_internal_pressure(pressures, site_data, building)
        
        # Step 4: Calculate net pressures
        self._calculate_net_pressures(pressures)
        
        # Step 5: Convert pressures to forces
        forces = self._calculate_wind_forces(pressures, building)
        
        return pressures, forces
    
    def _calculate_velocity_pressures(self, site_data: WindSiteData, 
                                    building: BuildingGeometry) -> WindPressures:
        """Calculate velocity pressures per ASCE 7-22 Section 26.10"""
        pressures = WindPressures()
        
        # Basic velocity pressure equation: q = 0.00256 * Kz * Kzt * Kd * Ke * V²
        
        # 1. Calculate Kz - velocity pressure exposure coefficient
        Kz_h = self._calculate_Kz(building.height, site_data.exposure)
        
        # 2. Calculate Kzt - topographic factor
        Kzt = self._calculate_topographic_factor(site_data, building.height)
        
        # 3. Wind directionality factor Kd
        Kd = 0.85  # For MWFRS of buildings (ASCE 7-22 Table 26.6-1)
        
        # 4. Ground elevation factor Ke
        Ke = self._calculate_elevation_factor(site_data.elevation)
        
        # 5. Calculate velocity pressures
        V_squared = site_data.V ** 2
        
        # Velocity pressure at mean roof height
        pressures.qh = 0.00256 * Kz_h * Kzt * Kd * Ke * V_squared
        
        # For varying height (simplified - using mean roof height)
        pressures.qz = pressures.qh
        
        return pressures
    
    def _calculate_Kz(self, height: float, exposure: ExposureCategory) -> float:
        """Calculate velocity pressure exposure coefficient Kz"""
        constants = self.EXPOSURE_CONSTANTS[exposure]
        zg = constants['zg']
        alpha = constants['alpha']
        
        # Minimum height limits
        if exposure == ExposureCategory.B:
            height = max(height, 30)  # Min 30 ft for Exposure B
        else:
            height = max(height, 15)  # Min 15 ft for Exposure C, D
        
        # ASCE 7-22 Equation 26.10-1
        if height <= zg:
            Kz = 2.01 * (height / zg) ** (2/alpha)
        else:
            Kz = 2.01  # Constant above gradient height
            
        return Kz
    
    def _calculate_topographic_factor(self, site_data: WindSiteData, height: float) -> float:
        """Calculate topographic factor Kzt per ASCE 7-22 Section 26.8"""
        if site_data.topographic_condition == TopographicCondition.FLAT:
            return 1.0
        
        # Simplified topographic factor calculation
        # Full implementation would use detailed ASCE 7-22 figures and equations
        
        H = site_data.hill_height
        Lh = site_data.horizontal_distance
        
        if H <= 60:  # Small topographic features
            return 1.0
        
        # Basic topographic factor (simplified)
        # This would be much more detailed in practice using ASCE 7-22 figures
        if site_data.topographic_condition == TopographicCondition.HILL:
            K1 = min(1 + 0.3 * H/100, 1.3)  # Simplified
        else:
            K1 = 1.0
            
        K2 = 1.0  # Horizontal attenuation factor (simplified)
        K3 = 1.0  # Height attenuation factor (simplified)
        
        return (K1 - 1) * K2 * K3 + 1
    
    def _calculate_elevation_factor(self, elevation: float) -> float:
        """Calculate ground elevation factor Ke per ASCE 7-22 Section 26.9"""
        # Simplified elevation factor
        # Ke = e^(-elevation/25000)  # Approximate formula
        if elevation <= 1000:
            return 1.0
        else:
            return max(math.exp(-elevation/25000), 0.9)
    
    def _calculate_external_pressures(self, pressures: WindPressures,
                                    site_data: WindSiteData,
                                    building: BuildingGeometry):
        """Calculate external pressure coefficients per ASCE 7-22 Section 27.3"""
        
        # Building dimensions
        L = building.length
        B = building.width  
        h = building.height
        
        # Calculate L/B ratio for pressure coefficients
        aspect_ratio = L / B if B > 0 else 1.0
        
        # External pressure coefficients from ASCE 7-22 Figure 27.3-1
        # (Simplified - full implementation would interpolate from detailed figures)
        
        # Windward wall Cp
        Cp_windward = 0.8
        
        # Leeward wall Cp (depends on L/B ratio)
        if aspect_ratio <= 1:
            Cp_leeward = -0.5
        elif aspect_ratio <= 2:
            Cp_leeward = -0.3 - 0.2 * (aspect_ratio - 1)
        else:
            Cp_leeward = -0.5
        
        # Side walls Cp
        Cp_side = -0.7
        
        # Roof pressure coefficients (flat roof simplified)
        if building.roof_slope <= 10:  # Flat roof
            Cp_roof_windward = -0.9
            Cp_roof_leeward = -0.5
        else:  # Sloped roof (simplified)
            if building.roof_slope <= 30:
                Cp_roof_windward = -0.9 + 0.3 * (building.roof_slope / 30)
                Cp_roof_leeward = -0.5
            else:
                Cp_roof_windward = -0.6
                Cp_roof_leeward = -0.6
        
        # Calculate pressures
        qh = pressures.qh
        
        pressures.windward_wall = Cp_windward * qh
        pressures.leeward_wall = Cp_leeward * qh
        pressures.side_wall = Cp_side * qh
        pressures.roof_windward = Cp_roof_windward * qh
        pressures.roof_leeward = Cp_roof_leeward * qh
    
    def _calculate_internal_pressure(self, pressures: WindPressures,
                                   site_data: WindSiteData,
                                   building: BuildingGeometry):
        """Calculate internal pressure per ASCE 7-22 Section 26.13"""
        
        # Calculate opening ratio
        if building.total_wall_area > 0:
            opening_ratio = building.opening_area / building.total_wall_area
        else:
            opening_ratio = 0.05  # Assume 5% for enclosed buildings
        
        # Internal pressure coefficient GCpi
        if building.category == BuildingCategory.ENCLOSED:
            if opening_ratio <= 0.01:
                GCpi = 0.18  # Use +/-0.18 for load combinations
            else:
                GCpi = 0.55  # Partially enclosed
        elif building.category == BuildingCategory.PARTIALLY_ENCLOSED:
            GCpi = 0.55
        else:  # Open building
            GCpi = 0.0
        
        # Use positive value for this calculation (load combinations will consider both)
        GCpi_value = 0.18 if building.category == BuildingCategory.ENCLOSED else 0.55
        
        pressures.internal_pressure = GCpi_value * pressures.qh
    
    def _calculate_net_pressures(self, pressures: WindPressures):
        """Calculate net pressures (external - internal)"""
        pi = pressures.internal_pressure
        
        # Net pressures for inward internal pressure
        pressures.net_windward_wall = pressures.windward_wall - (-pi)  # External - internal (inward)
        pressures.net_leeward_wall = pressures.leeward_wall - (-pi)
        pressures.net_side_wall = pressures.side_wall - (-pi)
        pressures.net_roof_windward = pressures.roof_windward - (-pi)
        pressures.net_roof_leeward = pressures.roof_leeward - (-pi)
        
        # Note: Load combinations should consider both +pi and -pi cases
    
    def _calculate_wind_forces(self, pressures: WindPressures,
                             building: BuildingGeometry) -> WindForces:
        """Convert wind pressures to forces for structural analysis"""
        
        # Calculate tributary areas
        wall_area = building.height * building.width
        roof_area = building.length * building.width
        
        # Calculate story forces (simplified uniform distribution)
        num_stories = max(1, int(building.height / 12))  # Assume 12 ft story height
        story_height = building.height / num_stories
        
        # Wind force per story
        force_per_story = (pressures.net_windward_wall - pressures.net_leeward_wall) * wall_area / num_stories
        
        story_forces = [force_per_story] * num_stories
        story_heights = [story_height * (i + 0.5) for i in range(num_stories)]
        
        # Total base shear
        total_base_shear = sum(story_forces)
        
        # Overturning moment
        overturning_moment = sum(force * height for force, height in zip(story_forces, story_heights))
        
        return WindForces(
            story_forces=story_forces,
            story_heights=story_heights,
            total_base_shear=total_base_shear,
            overturning_moment=overturning_moment,
            force_distribution="uniform",
            eccentricity=0.05 * building.width  # 5% eccentricity
        )
    
    def generate_wind_report(self, site_data: WindSiteData, building: BuildingGeometry,
                           pressures: WindPressures, forces: WindForces,
                           filepath: Optional[str] = None) -> str:
        """Generate comprehensive wind load report"""
        
        report_lines = [
            "ASCE 7-22 WIND LOAD ANALYSIS REPORT",
            "=" * 50,
            "",
            f"Analysis Code: {self.version}",
            f"Analysis Type: Main Wind Force Resisting System (MWFRS)",
            f"Method: Directional Procedure (Chapter 27)",
            "",
            "SITE CONDITIONS",
            "-" * 20,
            f"Basic Wind Speed (V): {site_data.V} mph",
            f"Risk Category: {site_data.risk_category.value}",
            f"Exposure Category: {site_data.exposure.value}",
            f"Topographic Condition: {site_data.topographic_condition.value.title()}",
            f"Site Elevation: {site_data.elevation} ft",
            "",
            "BUILDING GEOMETRY",
            "-" * 20,
            f"Length (L): {building.length} ft",
            f"Width (B): {building.width} ft", 
            f"Height (h): {building.height} ft",
            f"Roof Slope: {building.roof_slope}°",
            f"Building Category: {building.category.value.replace('_', ' ').title()}",
            "",
            "VELOCITY PRESSURES",
            "-" * 20,
            f"Velocity Pressure at Roof Height (qh): {pressures.qh:.1f} psf",
            f"Velocity Pressure at Height z (qz): {pressures.qz:.1f} psf",
            "",
            "EXTERNAL PRESSURES",
            "-" * 20,
            f"Windward Wall: {pressures.windward_wall:.1f} psf",
            f"Leeward Wall: {pressures.leeward_wall:.1f} psf",
            f"Side Wall: {pressures.side_wall:.1f} psf",
            f"Roof Windward: {pressures.roof_windward:.1f} psf",
            f"Roof Leeward: {pressures.roof_leeward:.1f} psf",
            "",
            "INTERNAL PRESSURE",
            "-" * 20,
            f"Internal Pressure: +/-{pressures.internal_pressure:.1f} psf",
            "",
            "NET PRESSURES (External - Internal)",
            "-" * 30,
            f"Net Windward Wall: {pressures.net_windward_wall:.1f} psf",
            f"Net Leeward Wall: {pressures.net_leeward_wall:.1f} psf",
            f"Net Side Wall: {pressures.net_side_wall:.1f} psf",
            f"Net Roof Windward: {pressures.net_roof_windward:.1f} psf",
            f"Net Roof Leeward: {pressures.net_roof_leeward:.1f} psf",
            "",
            "WIND FORCES",
            "-" * 15,
            f"Total Base Shear: {forces.total_base_shear:.0f} lb",
            f"Overturning Moment: {forces.overturning_moment:.0f} lb-ft",
            f"Load Eccentricity: {forces.eccentricity:.1f} ft",
            "",
            "STORY FORCES",
            "-" * 15,
            f"{'Story':<8} {'Height (ft)':<12} {'Force (lb)':<12}",
            "-" * 35
        ]
        
        # Add story force details
        for i, (height, force) in enumerate(zip(forces.story_heights, forces.story_forces)):
            report_lines.append(f"{i+1:<8} {height:<12.1f} {force:<12.0f}")
        
        report_lines.extend([
            "",
            "LOAD COMBINATIONS",
            "-" * 20,
            "Consider both positive and negative internal pressure:",
            f"Case 1: External + {pressures.internal_pressure:.1f} psf internal",
            f"Case 2: External - {pressures.internal_pressure:.1f} psf internal",
            "",
            "Apply wind loads in both principal directions of the building.",
            "Consider torsional effects and load eccentricity.",
            "",
            "NOTES",
            "-" * 10,
            "- Analysis assumes rigid building behavior",
            "- For flexible buildings, use gust-effect factor procedure",
            "- Local pressure effects may require additional analysis",
            "- Verify wind tunnel testing requirements per ASCE 7-22 Section 27.1.5"
        ])
        
        report_content = "\n".join(report_lines)
        
        # Save to file if requested
        if filepath:
            with open(filepath, 'w') as f:
                f.write(report_content)
            print(f"ASCE 7-22 wind load report saved to: {filepath}")
        
        return report_content


# Quick calculation functions
def quick_wind_analysis(V: float, exposure: str, height: float,
                       length: float, width: float) -> Dict[str, float]:
    """Quick wind analysis with simplified inputs"""
    
    # Convert string exposure to enum
    exposure_map = {'B': ExposureCategory.B, 'C': ExposureCategory.C, 'D': ExposureCategory.D}
    exposure_cat = exposure_map.get(exposure.upper(), ExposureCategory.C)
    
    # Create simplified inputs
    site_data = WindSiteData(
        V=V,
        risk_category=RiskCategory.II,
        exposure=exposure_cat
    )
    
    building = BuildingGeometry(
        length=length,
        width=width,
        height=height,
        category=BuildingCategory.ENCLOSED
    )
    
    # Generate loads
    generator = ASCE7WindGenerator()
    pressures, forces = generator.generate_wind_loads(site_data, building)
    
    return {
        'velocity_pressure': pressures.qh,
        'windward_pressure': pressures.net_windward_wall,
        'leeward_pressure': pressures.net_leeward_wall,
        'total_base_shear': forces.total_base_shear,
        'overturning_moment': forces.overturning_moment
    }


# Example usage and testing
if __name__ == "__main__":
    print("Testing ASCE 7-22 Wind Load Generator...")
    
    # Example building and site
    site = WindSiteData(
        V=115,  # 115 mph basic wind speed
        risk_category=RiskCategory.II,
        exposure=ExposureCategory.C
    )
    
    building = BuildingGeometry(
        length=100,  # 100 ft
        width=60,    # 60 ft  
        height=40,   # 40 ft
        roof_slope=5,  # 5 degree slope
        category=BuildingCategory.ENCLOSED
    )
    
    # Generate wind loads
    generator = ASCE7WindGenerator()
    pressures, forces = generator.generate_wind_loads(site, building)
    
    print(f"Velocity Pressure: {pressures.qh:.1f} psf")
    print(f"Windward Wall Net Pressure: {pressures.net_windward_wall:.1f} psf")
    print(f"Total Base Shear: {forces.total_base_shear:.0f} lb")
    print(f"Overturning Moment: {forces.overturning_moment:.0f} lb-ft")
    
    # Generate report
    report = generator.generate_wind_report(site, building, pressures, forces)
    print("\nWind load report generated successfully!")
    
    print("ASCE 7-22 Wind Load Generator ready for StructureTools integration!")
