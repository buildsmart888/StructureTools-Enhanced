# -*- coding: utf-8 -*-
"""
Thai Units Converter - Traditional Thai Engineering Units
ตัวแปลงหน่วยวิศวกรรมไทยแบบดั้งเดิม

This module provides conversion utilities for traditional Thai engineering units
commonly used in structural engineering practice in Thailand.
"""

import math
from typing import Dict, Union, Tuple


class ThaiUnitsConverter:
    """
    Thai engineering units converter
    ตัวแปลงหน่วยวิศวกรรมไทย
    
    Supports conversion between:
    - ksc (กิโลกรัมต่อตารางเซนติเมตร) ↔ MPa, kPa, Pa
    - Traditional Thai measurements ↔ Metric units
    - Thai load units ↔ International units
    """
    
    def __init__(self):
        """Initialize Thai units converter."""
        # Fundamental conversion factors
        self.conversion_factors = {
            # Pressure/Stress conversions
            'ksc_to_pa': 98066.5,       # 1 ksc = 98,066.5 Pa
            'ksc_to_kpa': 98.0665,      # 1 ksc = 98.0665 kPa  
            'ksc_to_mpa': 0.0980665,    # 1 ksc = 0.0980665 MPa
            
            # Force conversions
            'kgf_to_n': 9.80665,        # 1 kgf = 9.80665 N
            'tf_to_kn': 9.80665,        # 1 tf (metric ton-force) = 9.80665 kN
            
            # Length conversions (traditional Thai units)
            'wa_to_m': 2.0,             # 1 วา = 2 เมตร
            'keub_to_m': 0.25,          # 1 คืบ = 0.25 เมตร (25 cm)
            'niu_to_mm': 20,            # 1 นิ้ว (Thai inch) = 20 mm
            'sok_to_m': 0.5,            # 1 ศอก = 0.5 เมตร (50 cm)
            
            # Area conversions
            'rai_to_m2': 1600,          # 1 ไร่ = 1,600 ตร.ม.
            'ngan_to_m2': 400,          # 1 งาน = 400 ตร.ม.
            'wa2_to_m2': 4,             # 1 ตร.วา = 4 ตร.ม.
            
            # Weight/Mass conversions
            'chang_to_kg': 60,          # 1 ช่าง = 60 กิโลกรัม
            'hap_to_kg': 60,            # 1 หาบ = 60 กิโลกรัม
            'baht_to_g': 15.244,        # 1 บาท (น้ำหนัก) = 15.244 กรัม
        }
        
        # Reverse conversion factors
        for key, value in list(self.conversion_factors.items()):
            reverse_key = key.replace('_to_', '_from_').replace('from_', 'to_')[::-1].replace('_ot_', '_to_')[::-1]
            if 'from' not in key:
                parts = key.split('_to_')
                reverse_key = f"{parts[1]}_to_{parts[0]}"
                self.conversion_factors[reverse_key] = 1.0 / value
    
    def ksc_to_mpa(self, ksc_value: float) -> float:
        """
        Convert ksc to MPa
        แปลง กิโลกรัมต่อตารางเซนติเมตร เป็น เมกะปาสคาล
        
        Args:
            ksc_value: ค่าในหน่วย ksc
            
        Returns:
            ค่าในหน่วย MPa
        """
        return ksc_value * self.conversion_factors['ksc_to_mpa']
    
    def mpa_to_ksc(self, mpa_value: float) -> float:
        """
        Convert MPa to ksc
        แปลง เมกะปาสคาล เป็น กิโลกรัมต่อตารางเซนติเมตร
        
        Args:
            mpa_value: ค่าในหน่วย MPa
            
        Returns:
            ค่าในหน่วย ksc
        """
        return mpa_value * self.conversion_factors['mpa_to_ksc']
    
    def ksc_to_kpa(self, ksc_value: float) -> float:
        """Convert ksc to kPa."""
        return ksc_value * self.conversion_factors['ksc_to_kpa']
    
    def kpa_to_ksc(self, kpa_value: float) -> float:
        """Convert kPa to ksc."""
        return kpa_value * self.conversion_factors['kpa_to_ksc']
    
    def tf_to_kn(self, tf_value: float) -> float:
        """
        Convert metric ton-force to kN
        แปลง ตันแรง เป็น กิโลนิวตัน
        """
        return tf_value * self.conversion_factors['tf_to_kn']
    
    def kn_to_tf(self, kn_value: float) -> float:
        """
        Convert kN to metric ton-force
        แปลง กิโลนิวตัน เป็น ตันแรง
        """
        return kn_value * self.conversion_factors['kn_to_tf']
    
    def kgf_to_n(self, kgf_value: float) -> float:
        """
        Convert kilogram-force to Newton
        แปลง กิโลกรัมแรง เป็น นิวตัน
        """
        return kgf_value * self.conversion_factors['kgf_to_n']
    
    def n_to_kgf(self, n_value: float) -> float:
        """
        Convert Newton to kilogram-force
        แปลง นิวตัน เป็น กิโลกรัมแรง
        """
        return n_value * self.conversion_factors['n_to_kgf']
    
    def wa_to_m(self, wa_value: float) -> float:
        """
        Convert Thai 'wa' to meters
        แปลง วา เป็น เมตร
        """
        return wa_value * self.conversion_factors['wa_to_m']
    
    def m_to_wa(self, m_value: float) -> float:
        """
        Convert meters to Thai 'wa'
        แปลง เมตร เป็น วา
        """
        return m_value * self.conversion_factors['m_to_wa']
    
    def rai_to_m2(self, rai_value: float) -> float:
        """
        Convert Thai 'rai' to square meters
        แปลง ไร่ เป็น ตารางเมตร
        """
        return rai_value * self.conversion_factors['rai_to_m2']
    
    def m2_to_rai(self, m2_value: float) -> float:
        """
        Convert square meters to Thai 'rai'
        แปลง ตารางเมตร เป็น ไร่
        """
        return m2_value * self.conversion_factors['m2_to_rai']
    
    def thai_area_breakdown(self, area_m2: float) -> Dict[str, float]:
        """
        Break down area in square meters to Thai units
        แยกพื้นที่เป็นหน่วยไทย (ไร่-งาน-ตารางวา)
        
        Args:
            area_m2: พื้นที่ในตารางเมตร
            
        Returns:
            Dict with rai, ngan, and wa2 components
        """
        remaining_area = area_m2
        
        # Calculate rai (1 ไร่ = 1,600 ตร.ม.)
        rai = int(remaining_area // self.conversion_factors['rai_to_m2'])
        remaining_area %= self.conversion_factors['rai_to_m2']
        
        # Calculate ngan (1 งาน = 400 ตร.ม.)
        ngan = int(remaining_area // self.conversion_factors['ngan_to_m2'])
        remaining_area %= self.conversion_factors['ngan_to_m2']
        
        # Calculate wa2 (1 ตร.วา = 4 ตร.ม.)
        wa2 = remaining_area / self.conversion_factors['wa2_to_m2']
        
        return {
            'rai': rai,
            'ngan': ngan,
            'wa2': wa2,
            'total_m2': area_m2,
            'description_thai': f'{rai} ไร่ {ngan} งาน {wa2:.2f} ตารางวา'
        }
    
    def pressure_conversion_table(self, base_value: float, base_unit: str) -> Dict[str, float]:
        """
        Create comprehensive pressure conversion table
        สร้างตารางแปลงหน่วยความดันแบบครบถ้วน
        
        Args:
            base_value: ค่าพื้นฐาน
            base_unit: หน่วยพื้นฐาน ('ksc', 'MPa', 'kPa', 'Pa')
            
        Returns:
            Dict with all pressure unit conversions
        """
        # Convert to Pa first (base SI unit)
        if base_unit.lower() == 'ksc':
            pa_value = base_value * self.conversion_factors['ksc_to_pa']
        elif base_unit.lower() == 'mpa':
            pa_value = base_value * 1_000_000
        elif base_unit.lower() == 'kpa':
            pa_value = base_value * 1_000
        elif base_unit.lower() == 'pa':
            pa_value = base_value
        else:
            raise ValueError(f"Unsupported pressure unit: {base_unit}")
        
        return {
            'Pa': pa_value,
            'kPa': pa_value / 1_000,
            'MPa': pa_value / 1_000_000,
            'ksc': pa_value / self.conversion_factors['ksc_to_pa'],
            'psi': pa_value / 6_894.76,  # 1 psi = 6,894.76 Pa
            'bar': pa_value / 100_000,   # 1 bar = 100,000 Pa
            'atm': pa_value / 101_325,   # 1 atm = 101,325 Pa
            'base_value': base_value,
            'base_unit': base_unit
        }
    
    def force_conversion_table(self, base_value: float, base_unit: str) -> Dict[str, float]:
        """
        Create comprehensive force conversion table
        สร้างตารางแปลงหน่วยแรงแบบครบถ้วน
        """
        # Convert to N first (base SI unit)
        if base_unit.lower() == 'kgf':
            n_value = base_value * self.conversion_factors['kgf_to_n']
        elif base_unit.lower() == 'tf':
            n_value = base_value * self.conversion_factors['tf_to_kn'] * 1_000
        elif base_unit.lower() == 'kn':
            n_value = base_value * 1_000
        elif base_unit.lower() == 'n':
            n_value = base_value
        else:
            raise ValueError(f"Unsupported force unit: {base_unit}")
        
        return {
            'N': n_value,
            'kN': n_value / 1_000,
            'MN': n_value / 1_000_000,
            'kgf': n_value / self.conversion_factors['kgf_to_n'],
            'tf': n_value / (self.conversion_factors['tf_to_kn'] * 1_000),
            'lbf': n_value / 4.448,      # 1 lbf = 4.448 N
            'kip': n_value / 4_448,      # 1 kip = 4,448 N
            'base_value': base_value,
            'base_unit': base_unit
        }
    
    def structural_load_conversion(self, load_value: float, from_unit: str, to_unit: str, 
                                 area: float = 1.0) -> Dict[str, Union[float, str]]:
        """
        Convert structural loads between different unit systems
        แปลงภาระโครงสร้างระหว่างระบบหน่วยต่างๆ
        
        Args:
            load_value: ค่าภาระ
            from_unit: หน่วยต้นทาง ('ksc/m2', 'kN/m2', 'psf', 'kgf/m2')
            to_unit: หน่วยปลายทาง
            area: พื้นที่ (สำหรับคำนวณภาระรวม)
        """
        # Convert to kN/m2 as intermediate unit
        if from_unit.lower() == 'ksc/m2' or from_unit.lower() == 'ksc':
            kn_m2_value = load_value * self.conversion_factors['ksc_to_pa'] / 1_000
        elif from_unit.lower() == 'kn/m2':
            kn_m2_value = load_value
        elif from_unit.lower() == 'kgf/m2':
            kn_m2_value = load_value * self.conversion_factors['kgf_to_n'] / 1_000
        elif from_unit.lower() == 'psf':  # pounds per square foot
            kn_m2_value = load_value * 0.0479  # 1 psf = 0.0479 kN/m2
        else:
            raise ValueError(f"Unsupported load unit: {from_unit}")
        
        # Convert from kN/m2 to target unit
        if to_unit.lower() == 'ksc/m2' or to_unit.lower() == 'ksc':
            result_value = kn_m2_value / (self.conversion_factors['ksc_to_pa'] / 1_000)
        elif to_unit.lower() == 'kn/m2':
            result_value = kn_m2_value
        elif to_unit.lower() == 'kgf/m2':
            result_value = kn_m2_value * 1_000 / self.conversion_factors['kgf_to_n']
        elif to_unit.lower() == 'psf':
            result_value = kn_m2_value / 0.0479
        else:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        # Calculate total load
        total_load_kn = kn_m2_value * area
        total_load_target_unit = result_value * area
        
        return {
            'converted_value': result_value,
            'original_value': load_value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'area_m2': area,
            'total_load_kN': total_load_kn,
            'total_load_tf': total_load_kn / self.conversion_factors['tf_to_kn'],
            'total_load_target_unit': total_load_target_unit,
            'intermediate_kN_m2': kn_m2_value,
            'description': f'{load_value} {from_unit} = {result_value:.4f} {to_unit}',
            'description_thai': f'{load_value} {from_unit} = {result_value:.4f} {to_unit} (พื้นที่ {area} ตร.ม.)'
        }
    
    def concrete_strength_conversion(self, fc_value: float, from_unit: str = 'ksc') -> Dict[str, float]:
        """
        Convert concrete strength between ksc and MPa with Thai standard grades
        แปลงกำลังคอนกรีตระหว่าง ksc และ MPa พร้อมเกรดมาตรฐานไทย
        """
        if from_unit.lower() == 'ksc':
            mpa_value = self.ksc_to_mpa(fc_value)
            ksc_value = fc_value
        else:  # assume MPa
            ksc_value = self.mpa_to_ksc(fc_value)
            mpa_value = fc_value
        
        # Find closest Thai standard grade
        thai_grades = {
            180: 'Fc180', 210: 'Fc210', 240: 'Fc240', 
            280: 'Fc280', 320: 'Fc320', 350: 'Fc350'
        }
        
        closest_ksc = min(thai_grades.keys(), key=lambda x: abs(x - ksc_value))
        closest_grade = thai_grades[closest_ksc]
        
        # Calculate elastic modulus (Thai formula: Ec = 15000√fc' for ksc)
        ec_ksc = 15000 * math.sqrt(ksc_value)
        ec_mpa = 4700 * math.sqrt(mpa_value)
        
        return {
            'fc_ksc': ksc_value,
            'fc_MPa': mpa_value,
            'closest_thai_grade': closest_grade,
            'closest_grade_ksc': closest_ksc,
            'ec_ksc': ec_ksc,
            'ec_MPa': ec_mpa,
            'formula_thai': 'Ec = 15000√fc\' (ksc) หรือ Ec = 4700√fc\' (MPa)',
            'from_unit': from_unit
        }
    
    def steel_strength_conversion(self, fy_value: float, from_unit: str = 'ksc') -> Dict[str, Union[float, str]]:
        """
        Convert steel strength between ksc and MPa with Thai standard grades
        แปลงกำลังเหล็กระหว่าง ksc และ MPa พร้อมเกรดมาตรฐานไทย
        """
        if from_unit.lower() == 'ksc':
            mpa_value = self.ksc_to_mpa(fy_value)
            ksc_value = fy_value
        else:  # assume MPa
            ksc_value = self.mpa_to_ksc(fy_value)
            mpa_value = fy_value
        
        # Find closest Thai standard grade
        thai_steel_grades = {
            2400: 'SR24 (กลม)', 4000: 'SD40 (ข้ออ้อย)', 5000: 'SD50 (ข้ออ้อย)'
        }
        
        closest_ksc = min(thai_steel_grades.keys(), key=lambda x: abs(x - ksc_value))
        closest_grade = thai_steel_grades[closest_ksc]
        
        # Steel elastic modulus (Es = 2,040,000 ksc หรือ 200,000 MPa)
        es_ksc = 2040000
        es_mpa = 200000
        
        return {
            'fy_ksc': ksc_value,
            'fy_MPa': mpa_value,
            'closest_thai_grade': closest_grade,
            'closest_grade_ksc': closest_ksc,
            'es_ksc': es_ksc,
            'es_MPa': es_mpa,
            'from_unit': from_unit,
            'description_thai': f'เหล็กกำลัง {ksc_value:.0f} ksc ({mpa_value:.1f} MPa) ใกล้เคียง {closest_grade}'
        }
    
    def get_conversion_summary(self) -> Dict[str, Dict[str, float]]:
        """
        Get summary of all conversion factors
        สรุปค่าแปลงหน่วยทั้งหมด
        """
        return {
            'pressure_stress': {
                '1_ksc_to_MPa': self.conversion_factors['ksc_to_mpa'],
                '1_ksc_to_kPa': self.conversion_factors['ksc_to_kpa'],
                '1_ksc_to_Pa': self.conversion_factors['ksc_to_pa'],
                'description': 'ความดัน/ความเค้น'
            },
            'force': {
                '1_kgf_to_N': self.conversion_factors['kgf_to_n'],
                '1_tf_to_kN': self.conversion_factors['tf_to_kn'],
                'description': 'แรง'
            },
            'length_thai': {
                '1_wa_to_m': self.conversion_factors['wa_to_m'],
                '1_keub_to_m': self.conversion_factors['keub_to_m'],
                '1_sok_to_m': self.conversion_factors['sok_to_m'],
                '1_niu_to_mm': self.conversion_factors['niu_to_mm'],
                'description': 'ความยาวแบบไทย'
            },
            'area_thai': {
                '1_rai_to_m2': self.conversion_factors['rai_to_m2'],
                '1_ngan_to_m2': self.conversion_factors['ngan_to_m2'],
                '1_wa2_to_m2': self.conversion_factors['wa2_to_m2'],
                'description': 'พื้นที่แบบไทย'
            }
        }


# Global instance for easy access
_thai_converter_instance = None

def get_thai_converter():
    """Get singleton instance of Thai units converter."""
    global _thai_converter_instance
    if _thai_converter_instance is None:
        _thai_converter_instance = ThaiUnitsConverter()
    return _thai_converter_instance

# Convenience functions for common conversions
def ksc_to_mpa(ksc_value: float) -> float:
    """Quick conversion from ksc to MPa."""
    return get_thai_converter().ksc_to_mpa(ksc_value)

def mpa_to_ksc(mpa_value: float) -> float:
    """Quick conversion from MPa to ksc."""
    return get_thai_converter().mpa_to_ksc(mpa_value)

def tf_to_kn(tf_value: float) -> float:
    """Quick conversion from tf to kN."""
    return get_thai_converter().tf_to_kn(tf_value)

def kn_to_tf(kn_value: float) -> float:
    """Quick conversion from kN to tf."""
    return get_thai_converter().kn_to_tf(kn_value)

def convert_concrete_strength(fc_value: float, from_unit: str = 'ksc'):
    """Quick concrete strength conversion with Thai grades."""
    return get_thai_converter().concrete_strength_conversion(fc_value, from_unit)

def convert_steel_strength(fy_value: float, from_unit: str = 'ksc'):
    """Quick steel strength conversion with Thai grades."""
    return get_thai_converter().steel_strength_conversion(fy_value, from_unit)
