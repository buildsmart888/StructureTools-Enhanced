# -*- coding: utf-8 -*-
"""
Universal Thai Units Integration
การผสานรวมหน่วยไทยแบบครอบคลุม

This module provides universal Thai units support across all StructureTools components.
"""

import sys
import os

# Import Thai units converter
try:
    from .thai_units import get_thai_converter
    THAI_UNITS_AVAILABLE = True
except ImportError:
    try:
        from thai_units import get_thai_converter
        THAI_UNITS_AVAILABLE = True
    except ImportError:
        THAI_UNITS_AVAILABLE = False
        get_thai_converter = None


class UniversalThaiUnits:
    """
    Universal Thai units integration for all StructureTools components
    ระบบหน่วยไทยแบบครอบคลุมสำหรับ StructureTools ทั้งหมด
    """
    
    def __init__(self):
        """Initialize universal Thai units system."""
        self.converter = get_thai_converter() if THAI_UNITS_AVAILABLE else None
        self.enabled = THAI_UNITS_AVAILABLE
        
        # Thai conversion factors (CORRECTED VALUES)
        self.KN_TO_KGF = 101.97162129779283  # 1 kN = 101.972 kgf
        self.KN_TO_TF = 0.10197162129779283   # 1 kN = 0.10197 tf
        self.KGF_TO_KN = 1.0 / self.KN_TO_KGF
        self.TF_TO_KN = 1.0 / self.KN_TO_TF
        # FIXED: Pressure/Stress conversion
        self.MPA_TO_KSC = 10.19716  # 1 MPa = 10.19716 ksc (NOT 0.102!)
        self.KSC_TO_MPA = 0.0980665  # 1 ksc = 0.0980665 MPa
    
    # Force conversions
    def kn_to_kgf(self, kn_value):
        """Convert kN to kgf (กิโลนิวตันเป็นกิโลกรัมแรง)"""
        return kn_value * self.KN_TO_KGF
    
    def kgf_to_kn(self, kgf_value):
        """Convert kgf to kN (กิโลกรัมแรงเป็นกิโลนิวตัน)"""
        return kgf_value * self.KGF_TO_KN
    
    def kn_to_tf(self, kn_value):
        """Convert kN to tf (กิโลนิวตันเป็นตันแรง)"""
        return kn_value * self.KN_TO_TF
    
    def tf_to_kn(self, tf_value):
        """Convert tf to kN (ตันแรงเป็นกิโลนิวตัน)"""
        return tf_value * self.TF_TO_KN
    
    # Moment conversions
    def kn_m_to_kgf_cm(self, kn_m_value):
        """Convert kN·m to kgf·cm (กิโลนิวตัน-เมตรเป็นกิโลกรัมแรง-เซนติเมตร)"""
        return kn_m_value * self.KN_TO_KGF * 100  # × 100 for m to cm
    
    def kgf_cm_to_kn_m(self, kgf_cm_value):
        """Convert kgf·cm to kN·m (กิโลกรัมแรง-เซนติเมตรเป็นกิโลนิวตัน-เมตร)"""
        return kgf_cm_value * self.KGF_TO_KN / 100
    
    def kn_m_to_tf_m(self, kn_m_value):
        """Convert kN·m to tf·m (กิโลนิวตัน-เมตรเป็นตันแรง-เมตร)"""
        return kn_m_value * self.KN_TO_TF
    
    def tf_m_to_kn_m(self, tf_m_value):
        """Convert tf·m to kN·m (ตันแรง-เมตรเป็นกิโลนิวตัน-เมตร)"""
        return tf_m_value * self.TF_TO_KN
    
    # Pressure/Stress conversions
    def mpa_to_ksc(self, mpa_value):
        """Convert MPa to ksc (เมกะปาสคาลเป็นกิโลกรัมต่อตารางเซนติเมตร)"""
        return mpa_value * self.MPA_TO_KSC
    
    def ksc_to_mpa(self, ksc_value):
        """Convert ksc to MPa (กิโลกรัมต่อตารางเซนติเมตรเป็นเมกะปาสคาล)"""
        return ksc_value * self.KSC_TO_MPA
    
    def kn_m2_to_ksc_m2(self, kn_m2_value):
        """Convert kN/m² to ksc/m² (กิโลนิวตันต่อตารางเมตรเป็นกิโลกรัมต่อตารางเซนติเมตรต่อตารางเมตร)"""
        return kn_m2_value * self.MPA_TO_KSC  # Same conversion factor as MPa to ksc
    
    def ksc_m2_to_kn_m2(self, ksc_m2_value):
        """Convert ksc/m² to kN/m² (กิโลกรัมต่อตารางเซนติเมตรต่อตารางเมตรเป็นกิโลนิวตันต่อตารางเมตร)"""
        return ksc_m2_value * self.KSC_TO_MPA
    
    def kn_m2_to_tf_m2(self, kn_m2_value):
        """Convert kN/m² to tf/m² (กิโลนิวตันต่อตารางเมตรเป็นตันแรงต่อตารางเมตร)"""
        return kn_m2_value * self.KN_TO_TF
    
    def tf_m2_to_kn_m2(self, tf_m2_value):
        """Convert tf/m² to kN/m² (ตันแรงต่อตารางเมตรเป็นกิโลนิวตันต่อตารางเมตร)"""
        return tf_m2_value * self.TF_TO_KN
    
    # Linear load conversions
    def kn_m_to_kgf_m(self, kn_m_value):
        """Convert kN/m to kgf/m (กิโลนิวตันต่อเมตรเป็นกิโลกรัมแรงต่อเมตร)"""
        return kn_m_value * self.KN_TO_KGF
    
    def kgf_m_to_kn_m(self, kgf_m_value):
        """Convert kgf/m to kN/m (กิโลกรัมแรงต่อเมตรเป็นกิโลนิวตันต่อเมตร)"""
        return kgf_m_value * self.KGF_TO_KN
    
    def kn_m_to_tf_m(self, kn_m_value):
        """Convert kN/m to tf/m (กิโลนิวตันต่อเมตรเป็นตันแรงต่อเมตร)"""
        return kn_m_value * self.KN_TO_TF
    
    def tf_m_to_kn_m(self, tf_m_value):
        """Convert tf/m to kN/m (ตันแรงต่อเมตรเป็นกิโลนิวตันต่อเมตร)"""
        return tf_m_value * self.TF_TO_KN
        
    def enhance_material_data(self, material_data):
        """
        Add Thai units to any material data dictionary
        เพิ่มหน่วยไทยให้กับข้อมูลวัสดุ
        """
        if not self.enabled or not isinstance(material_data, dict):
            return material_data
        
        enhanced_data = material_data.copy()
        
        # Strength properties conversion
        strength_mappings = {
            'yield_strength': 'yield_strength_ksc',
            'ultimate_strength': 'ultimate_strength_ksc', 
            'tensile_strength': 'tensile_strength_ksc',
            'compressive_strength': 'compressive_strength_ksc',
            'shear_strength': 'shear_strength_ksc',
            'modulus_elasticity': 'modulus_elasticity_ksc',
            'elastic_modulus': 'elastic_modulus_ksc'
        }
        
        for mpa_key, ksc_key in strength_mappings.items():
            if mpa_key in enhanced_data and ksc_key not in enhanced_data:
                mpa_value = enhanced_data[mpa_key]
                if isinstance(mpa_value, (int, float)):
                    enhanced_data[ksc_key] = self.converter.mpa_to_ksc(mpa_value)
        
        # Density conversion (kg/m³ to tf/m³)
        if 'density' in enhanced_data and 'density_tf_m3' not in enhanced_data:
            density_kg_m3 = enhanced_data['density']
            if isinstance(density_kg_m3, (int, float)):
                enhanced_data['density_tf_m3'] = density_kg_m3 / 1000
        
        # Add Thai descriptions if not present
        if 'description_thai' not in enhanced_data and 'description' in enhanced_data:
            enhanced_data['description_thai'] = enhanced_data['description']
        
        # Add units information
        enhanced_data['units_system'] = 'SI+Thai'
        enhanced_data['thai_units_supported'] = True
        
        return enhanced_data
    
    def enhance_load_data(self, load_data):
        """
        Add Thai units to load data
        เพิ่มหน่วยไทยให้กับข้อมูลภาระ
        """
        if not self.enabled or not isinstance(load_data, dict):
            return load_data
        
        enhanced_data = load_data.copy()
        
        # Force conversions (kN to tf)
        force_mappings = {
            'force_kN': 'force_tf',
            'load_kN': 'load_tf',
            'moment_kNm': 'moment_tfm',
            'shear_kN': 'shear_tf'
        }
        
        for kn_key, tf_key in force_mappings.items():
            if kn_key in enhanced_data and tf_key not in enhanced_data:
                kn_value = enhanced_data[kn_key]
                if isinstance(kn_value, (int, float)):
                    enhanced_data[tf_key] = self.converter.kn_to_tf(kn_value)
        
        # Pressure conversions (kN/m² to ksc/m²)
        pressure_mappings = {
            'pressure_kN_m2': 'pressure_ksc_m2',
            'load_kN_m2': 'load_ksc_m2',
            'stress_MPa': 'stress_ksc',
            'pressure_MPa': 'pressure_ksc'
        }
        
        for int_key, thai_key in pressure_mappings.items():
            if int_key in enhanced_data and thai_key not in enhanced_data:
                value = enhanced_data[int_key]
                if isinstance(value, (int, float)):
                    if 'MPa' in int_key:
                        enhanced_data[thai_key] = self.converter.mpa_to_ksc(value)
                    else:  # kN/m²
                        enhanced_data[thai_key] = self.converter.mpa_to_ksc(value / 1000)
        
        return enhanced_data
    
    def enhance_geometric_data(self, geom_data):
        """
        Add Thai traditional units to geometric data
        เพิ่มหน่วยไทยดั้งเดิมให้กับข้อมูลเรขาคณิต
        """
        if not self.enabled or not isinstance(geom_data, dict):
            return geom_data
        
        enhanced_data = geom_data.copy()
        
        # Length conversions (m to wa, keub, etc.)
        if 'length_m' in enhanced_data:
            length_m = enhanced_data['length_m']
            if isinstance(length_m, (int, float)):
                enhanced_data['length_wa'] = self.converter.m_to_wa(length_m)
                enhanced_data['length_keub'] = length_m / 0.25  # 1 keub = 0.25 m
        
        # Area conversions (m² to rai, ngan, wa²)
        if 'area_m2' in enhanced_data:
            area_m2 = enhanced_data['area_m2']
            if isinstance(area_m2, (int, float)):
                thai_area = self.converter.thai_area_breakdown(area_m2)
                enhanced_data.update(thai_area)
        
        return enhanced_data
    
    def enhance_calculation_results(self, results):
        """
        Add Thai units to calculation results
        เพิ่มหน่วยไทยให้กับผลการคำนวณ
        """
        if not self.enabled or not isinstance(results, dict):
            return results
        
        enhanced_results = results.copy()
        
        # Apply all enhancement methods
        enhanced_results = self.enhance_material_data(enhanced_results)
        enhanced_results = self.enhance_load_data(enhanced_results)
        enhanced_results = self.enhance_geometric_data(enhanced_results)
        
        # Add metadata
        enhanced_results['thai_units_enhanced'] = True
        enhanced_results['conversion_info'] = {
            'ksc_to_mpa': 0.0980665,
            'tf_to_kn': 9.80665,
            'wa_to_m': 2.0,
            'rai_to_m2': 1600
        }
        
        return enhanced_results
    
    def create_units_summary(self, data):
        """
        Create a summary of all units used in the data
        สร้างสรุปหน่วยทั้งหมดที่ใช้ในข้อมูล
        """
        if not isinstance(data, dict):
            return {}
        
        units_found = {
            'SI_units': [],
            'Thai_units': [],
            'conversion_applied': []
        }
        
        for key, value in data.items():
            if isinstance(value, (int, float)):
                if any(unit in key.lower() for unit in ['mpa', 'kn', 'm2', 'm3']):
                    units_found['SI_units'].append(key)
                elif any(unit in key.lower() for unit in ['ksc', 'tf', 'wa', 'rai']):
                    units_found['Thai_units'].append(key)
                    units_found['conversion_applied'].append(key)
        
        return units_found
    
    def get_conversion_factors(self):
        """Get all conversion factors used in the system."""
        if not self.enabled:
            return {}
        
        return self.converter.get_conversion_summary()


# Global instance
_universal_thai_units = None

def get_universal_thai_units():
    """Get singleton instance of universal Thai units system."""
    global _universal_thai_units
    if _universal_thai_units is None:
        _universal_thai_units = UniversalThaiUnits()
    return _universal_thai_units

# Convenience functions for easy integration
def enhance_with_thai_units(data, data_type='auto'):
    """
    Enhance any data with Thai units
    เพิ่มหน่วยไทยให้กับข้อมูลใดๆ
    
    Args:
        data: Dictionary containing data to enhance
        data_type: Type of data ('material', 'load', 'geometric', 'auto')
    """
    thai_units = get_universal_thai_units()
    
    if not thai_units.enabled:
        return data
    
    if data_type == 'material':
        return thai_units.enhance_material_data(data)
    elif data_type == 'load':
        return thai_units.enhance_load_data(data)
    elif data_type == 'geometric':
        return thai_units.enhance_geometric_data(data)
    else:  # auto - apply all enhancements
        return thai_units.enhance_calculation_results(data)

def add_thai_material_units(material_dict):
    """Quick function to add Thai units to material properties."""
    return enhance_with_thai_units(material_dict, 'material')

def add_thai_load_units(load_dict):
    """Quick function to add Thai units to load data."""
    return enhance_with_thai_units(load_dict, 'load')

def add_thai_geometric_units(geom_dict):
    """Quick function to add Thai units to geometric data."""
    return enhance_with_thai_units(geom_dict, 'geometric')

def get_thai_conversion_summary():
    """Get summary of all Thai unit conversions available."""
    thai_units = get_universal_thai_units()
    return thai_units.get_conversion_factors()

def is_thai_units_available():
    """Check if Thai units system is available."""
    return THAI_UNITS_AVAILABLE

# Integration helpers for specific components
class ThaiUnitsDecorator:
    """
    Decorator class to automatically add Thai units to function results
    คลาสตกแต่งเพื่อเพิ่มหน่วยไทยให้กับผลลัพธ์ฟังก์ชันอัตโนมัติ
    """
    
    def __init__(self, data_type='auto'):
        self.data_type = data_type
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, dict):
                return enhance_with_thai_units(result, self.data_type)
            return result
        return wrapper

# Decorator instances for easy use
thai_material_units = ThaiUnitsDecorator('material')
thai_load_units = ThaiUnitsDecorator('load')
thai_geometric_units = ThaiUnitsDecorator('geometric')
thai_auto_units = ThaiUnitsDecorator('auto')
