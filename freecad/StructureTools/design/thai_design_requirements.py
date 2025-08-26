# -*- coding: utf-8 -*-
"""
Thai Design Requirements - Thai Ministry B.E. 2566 Standards
กำหนดค่าการออกแบบตามกฎกระทรวง พ.ศ. 2566

This module provides comprehensive design requirements and calculations
according to Thai building codes and standards.
"""

import math
from typing import Dict, Any, Optional, Tuple


class ThaiDesignRequirements:
    """
    Thai design requirements according to Ministry B.E. 2566
    ข้อกำหนดการออกแบบตามกฎกระทรวง พ.ศ. 2566
    """
    
    def __init__(self):
        """Initialize Thai design requirements."""
        self.code_version = "พ.ศ. 2566"  # B.E. 2566
        self.standard_name = "กฎกระทรวงกำหนดหลักเกณฑ์และวิธีการในการออกแบบและก่อสร้างอาคาร"
        
        # Load factors according to Thai standards
        self.load_factors = {
            'dead': 1.4,        # ปัจจัยภาระตาย
            'live': 1.7,        # ปัจจัยภาระจร
            'wind': 1.6,        # ปัจจัยภาระลม
            'seismic': 1.0,     # ปัจจัยภาระแผ่นดินไหว
            'snow': 1.6,        # ปัจจัยภาระหิมะ
            'thermal': 1.2      # ปัจจัยภาระอุณหภูมิ
        }
        
        # Resistance factors for materials
        self.resistance_factors = {
            'concrete': {
                'compression': 0.85,    # ϕc - ปัจจัยลดกำลังอัด
                'tension': 0.90,        # ϕt - ปัจจัยลดกำลังดึง
                'shear': 0.85,          # ϕv - ปัจจัยลดกำลังเฉือน
                'bond': 0.90            # ϕb - ปัจจัยลดกำลังยึดเกาะ
            },
            'steel': {
                'tension': 0.90,        # ϕt - ปัจจัยลดกำลังดึง
                'compression': 0.90,    # ϕc - ปัจจัยลดกำลังอัด
                'shear': 0.90,          # ϕv - ปัจจัยลดกำลังเฉือน
                'bearing': 0.75,        # ϕb - ปัจจัยลดกำลังแบร์ริง
                'buckling': 0.90        # ϕb - ปัจจัยลดกำลังการดำ
            }
        }
        
        # Deflection limits according to Thai standards
        self.deflection_limits = {
            'beam': {
                'live': {'limit': 'L/360', 'description': 'ภาระจร - คาน'},
                'total': {'limit': 'L/240', 'description': 'ภาระรวม - คาน'},
                'cantilever_live': {'limit': 'L/180', 'description': 'ภาระจร - คานยื่น'},
                'cantilever_total': {'limit': 'L/120', 'description': 'ภาระรวม - คานยื่น'}
            },
            'slab': {
                'live': {'limit': 'L/360', 'description': 'ภาระจร - พื้น'},
                'total': {'limit': 'L/240', 'description': 'ภาระรวม - พื้น'}
            },
            'column': {
                'drift': {'limit': 'h/500', 'description': 'การเยื้องคอลัมน์'}
            }
        }
    
    def get_concrete_design_strength(self, fc_prime, unit='MPa'):
        """
        Calculate concrete design strength according to Thai standards
        คำนวณกำลังออกแบบคอนกรีตตามมาตรฐานไทย
        
        Args:
            fc_prime: กำลังอัดคอนกรีต (MPa หรือ ksc)
            unit: หน่วย ('MPa' หรือ 'ksc')
        """
        if unit == 'ksc':
            fc_prime_mpa = fc_prime * 0.0980665  # แปลง ksc เป็น MPa
        else:
            fc_prime_mpa = fc_prime
            
        # กำลังออกแบบ = ϕ × fc'
        design_strength_mpa = self.resistance_factors['concrete']['compression'] * fc_prime_mpa
        design_strength_ksc = design_strength_mpa / 0.0980665
        
        # คำนวณ modulus ของคอนกรีตตามสูตรไทย
        # Ec = 4700√fc' (MPa) หรือ Ec = 15000√fc' (ksc)
        if unit == 'ksc':
            Ec_ksc = 15000 * math.sqrt(fc_prime)
            Ec_mpa = Ec_ksc * 0.0980665
        else:
            Ec_mpa = 4700 * math.sqrt(fc_prime_mpa)
            Ec_ksc = Ec_mpa / 0.0980665
        
        return {
            'design_strength_MPa': design_strength_mpa,
            'design_strength_ksc': design_strength_ksc,
            'elastic_modulus_MPa': Ec_mpa,
            'elastic_modulus_ksc': Ec_ksc,
            'resistance_factor': self.resistance_factors['concrete']['compression'],
            'formula_thai': 'ϕc × fc\' และ Ec = 4700√fc\' (MPa) หรือ Ec = 15000√fc\' (ksc)',
            'code': self.standard_name
        }
    
    def get_steel_design_strength(self, fy, fu=None, unit='MPa'):
        """
        Calculate steel design strength according to Thai standards
        คำนวณกำลังออกแบบเหล็กตามมาตรฐานไทย
        
        Args:
            fy: กำลังครากเหล็ก (MPa หรือ ksc)
            fu: กำลังต้านทานสูงสุด (MPa หรือ ksc)
            unit: หน่วย ('MPa' หรือ 'ksc')
        """
        if unit == 'ksc':
            fy_mpa = fy * 0.0980665  # แปลง ksc เป็น MPa
            fu_mpa = fu * 0.0980665 if fu else None
        else:
            fy_mpa = fy
            fu_mpa = fu
        
        # กำลังออกแบบดึง
        design_tension_mpa = self.resistance_factors['steel']['tension'] * fy_mpa
        design_tension_ksc = design_tension_mpa / 0.0980665
        
        # กำลังออกแบบอัด
        design_compression_mpa = self.resistance_factors['steel']['compression'] * fy_mpa
        design_compression_ksc = design_compression_mpa / 0.0980665
        
        # กำลังออกแบบเฉือน
        design_shear_mpa = self.resistance_factors['steel']['shear'] * fy_mpa * 0.6  # 0.6Fy for shear
        design_shear_ksc = design_shear_mpa / 0.0980665
        
        # Modulus ของเหล็ก (Es = 200,000 MPa หรือ 2,040,000 ksc)
        Es_mpa = 200000
        Es_ksc = 2040000
        
        result = {
            'design_tension_MPa': design_tension_mpa,
            'design_tension_ksc': design_tension_ksc,
            'design_compression_MPa': design_compression_mpa,
            'design_compression_ksc': design_compression_ksc,
            'design_shear_MPa': design_shear_mpa,
            'design_shear_ksc': design_shear_ksc,
            'elastic_modulus_MPa': Es_mpa,
            'elastic_modulus_ksc': Es_ksc,
            'resistance_factors': self.resistance_factors['steel'],
            'code': self.standard_name
        }
        
        if fu_mpa:
            design_ultimate_mpa = self.resistance_factors['steel']['tension'] * fu_mpa
            design_ultimate_ksc = design_ultimate_mpa / 0.0980665
            result.update({
                'design_ultimate_MPa': design_ultimate_mpa,
                'design_ultimate_ksc': design_ultimate_ksc
            })
        
        return result
    
    def get_load_combinations(self):
        """
        Get load combinations according to Thai Ministry B.E. 2566
        สูตรการรวมภาระตามกฎกระทรวง พ.ศ. 2566
        """
        return {
            'LRFD': {
                'basic': {
                    'formula': '1.4D + 1.7L',
                    'description': 'ภาระพื้นฐาน',
                    'description_thai': 'ภาระตาย + ภาระจร',
                    'factors': {'D': 1.4, 'L': 1.7}
                },
                'wind': {
                    'formula': '1.2D + 1.0L + 1.6W',
                    'description': 'รวมภาระลม',
                    'description_thai': 'ภาระตาย + ภาระจร + ภาระลม',
                    'factors': {'D': 1.2, 'L': 1.0, 'W': 1.6}
                },
                'seismic': {
                    'formula': '1.2D + 1.0L + 1.0E',
                    'description': 'รวมภาระแผ่นดินไหว',
                    'description_thai': 'ภาระตาย + ภาระจร + ภาระแผ่นดินไหว',
                    'factors': {'D': 1.2, 'L': 1.0, 'E': 1.0}
                },
                'wind_reduced': {
                    'formula': '0.9D + 1.6W',
                    'description': 'ภาระลมลดภาระตาย',
                    'description_thai': 'ภาระตายลด + ภาระลม',
                    'factors': {'D': 0.9, 'W': 1.6}
                },
                'seismic_reduced': {
                    'formula': '0.9D + 1.0E',
                    'description': 'ภาระแผ่นดินไหวลดภาระตาย',
                    'description_thai': 'ภาระตายลด + ภาระแผ่นดินไหว',
                    'factors': {'D': 0.9, 'E': 1.0}
                }
            },
            'ASD': {
                'basic': {
                    'formula': 'D + L',
                    'description': 'ภาระพื้นฐาน',
                    'description_thai': 'ภาระตาย + ภาระจร',
                    'factors': {'D': 1.0, 'L': 1.0}
                },
                'wind': {
                    'formula': 'D + L + W',
                    'description': 'รวมภาระลม',
                    'description_thai': 'ภาระตาย + ภาระจร + ภาระลม',
                    'factors': {'D': 1.0, 'L': 1.0, 'W': 1.0}
                },
                'seismic': {
                    'formula': 'D + L + E',
                    'description': 'รวมภาระแผ่นดินไหว',
                    'description_thai': 'ภาระตาย + ภาระจร + ภาระแผ่นดินไหว',
                    'factors': {'D': 1.0, 'L': 1.0, 'E': 1.0}
                }
            }
        }
    
    def calculate_reinforcement_requirements(self, moment, fc_prime, fy, b, d, unit='MPa'):
        """
        Calculate reinforcement requirements for concrete beams according to Thai standards
        คำนวณเหล็กเสริมสำหรับคานคอนกรีตตามมาตรฐานไทย
        
        Args:
            moment: โมเมนต์ (kN.m)
            fc_prime: กำลังอัดคอนกรีต (MPa หรือ ksc)
            fy: กำลังครากเหล็ก (MPa หรือ ksc)
            b: ความกว้างคาน (mm)
            d: ความลึกใช้งาน (mm)
            unit: หน่วยกำลัง ('MPa' หรือ 'ksc')
        """
        if unit == 'ksc':
            fc_prime_mpa = fc_prime * 0.0980665
            fy_mpa = fy * 0.0980665
        else:
            fc_prime_mpa = fc_prime
            fy_mpa = fy
        
        # ค่าสัมประสิทธิ์ตามมาตรฐานไทย
        phi = self.resistance_factors['concrete']['compression']  # ϕ = 0.85
        beta1 = 0.85 if fc_prime_mpa <= 28 else 0.85 - 0.05 * (fc_prime_mpa - 28) / 7
        beta1 = max(beta1, 0.65)  # ไม่น้อยกว่า 0.65
        
        # คำนวณ ρ_balanced
        Es = 200000  # MPa
        epsilon_y = fy_mpa / Es  # ความเครียดครากเหล็ก
        rho_balanced = 0.85 * beta1 * fc_prime_mpa / fy_mpa * (0.003 / (0.003 + epsilon_y))
        
        # ρ_max = 0.75 × ρ_balanced (ตามมาตรฐานไทย)
        rho_max = 0.75 * rho_balanced
        
        # ρ_min สำหรับคาน
        rho_min = max(1.4 / fy_mpa, math.sqrt(fc_prime_mpa) / (4 * fy_mpa))
        
        # คำนวณ moment factored
        Mu = moment * 1000000  # แปลงเป็น N.mm
        
        # คำนวณ Rn
        Rn = Mu / (phi * b * d**2)
        
        # คำนวณ ρ required
        rho_req = (0.85 * fc_prime_mpa / fy_mpa) * (1 - math.sqrt(1 - 2 * Rn / (0.85 * fc_prime_mpa)))
        
        # ตรวจสอบขีดจำกัด
        if rho_req < rho_min:
            rho_use = rho_min
            status = "ใช้เหล็กเสริมขั้นต่ำ"
        elif rho_req > rho_max:
            rho_use = rho_max
            status = "เกินขีดจำกัด - ต้องปรับขนาดหน้าตัด"
        else:
            rho_use = rho_req
            status = "ปกติ"
        
        # พื้นที่เหล็กเสริม
        As_req = rho_use * b * d  # mm²
        As_min = rho_min * b * d  # mm²
        As_max = rho_max * b * d  # mm²
        
        # จำนวนเส้นเหล็กเสริม (สมมติใช้ DB16)
        bar_area = math.pi * (16/2)**2  # mm² สำหรับ DB16
        num_bars = math.ceil(As_req / bar_area)
        As_provided = num_bars * bar_area
        
        return {
            'As_required_mm2': As_req,
            'As_minimum_mm2': As_min,
            'As_maximum_mm2': As_max,
            'As_provided_mm2': As_provided,
            'rho_required': rho_req,
            'rho_minimum': rho_min,
            'rho_maximum': rho_max,
            'rho_balanced': rho_balanced,
            'rho_used': rho_use,
            'num_bars_DB16': num_bars,
            'bar_size_suggested': 'DB16',
            'beta1': beta1,
            'phi_factor': phi,
            'status': status,
            'status_thai': status,
            'code': self.standard_name,
            'formula_thai': 'As = ρbd, ρ = 0.85fc\'/fy × (1 - √(1 - 2Rn/(0.85fc\')))'
        }
    
    def check_deflection_limits(self, actual_deflection, span_length, member_type='beam', load_type='total'):
        """
        Check deflection limits according to Thai standards
        ตรวจสอบขีดจำกัดการโก่งตามมาตรฐานไทย
        
        Args:
            actual_deflection: การโก่งจริง (mm)
            span_length: ความยาวช่วง (mm)
            member_type: ประเภทสมาชิก ('beam', 'slab', 'cantilever')
            load_type: ประเภทภาระ ('live', 'total')
        """
        deflection_limits = self.deflection_limits
        
        if member_type == 'cantilever':
            key = f'cantilever_{load_type}'
            member_category = 'beam'
        else:
            key = load_type
            member_category = member_type
        
        if member_category not in deflection_limits or key not in deflection_limits[member_category]:
            return {
                'status': 'ไม่สามารถตรวจสอบได้',
                'error': f'ไม่พบข้อมูลสำหรับ {member_type} {load_type}'
            }
        
        limit_info = deflection_limits[member_category][key]
        limit_str = limit_info['limit']
        
        # แปลงขีดจำกัดเป็นตัวเลข
        if 'L/' in limit_str:
            denominator = int(limit_str.split('L/')[1])
            allowable_deflection = span_length / denominator
        elif 'h/' in limit_str:
            denominator = int(limit_str.split('h/')[1])
            allowable_deflection = span_length / denominator  # สมมติ h = span_length
        else:
            allowable_deflection = 0
        
        # ตรวจสอบ
        ratio = actual_deflection / allowable_deflection if allowable_deflection > 0 else 0
        is_ok = actual_deflection <= allowable_deflection
        
        return {
            'actual_deflection_mm': actual_deflection,
            'allowable_deflection_mm': allowable_deflection,
            'deflection_ratio': ratio,
            'limit_formula': limit_str,
            'is_acceptable': is_ok,
            'status': 'ผ่าน' if is_ok else 'ไม่ผ่าน',
            'status_thai': 'ผ่านเกณฑ์' if is_ok else 'เกินขีดจำกัดการโก่ง',
            'description_thai': limit_info['description'],
            'code': self.standard_name,
            'span_length_mm': span_length,
            'member_type': member_type,
            'load_type': load_type
        }
    
    def get_seismic_design_categories(self):
        """
        Get seismic design categories for Thailand
        หมวดหมู่การออกแบบแผ่นดินไหวสำหรับประเทศไทย
        """
        return {
            'zones': {
                'very_low': {
                    'factor': 0.15,
                    'regions': ['กรุงเทพฯ', 'ปทุมธานี', 'สมุทรปราการ', 'นนทบุรี', 'สมุทรสาคร'],
                    'description': 'เขตเสี่ยงต่ำมาก',
                    'requirements': 'ความต้านทานแผ่นดินไหวขั้นพื้นฐาน'
                },
                'low': {
                    'factor': 0.25,
                    'regions': ['ชลบุรี', 'ระยอง', 'จันทบุรี', 'ตราด', 'ประจวบคีรีขันธ์'],
                    'description': 'เขตเสี่ยงต่ำ',
                    'requirements': 'ความต้านทานแผ่นดินไหวปานกลาง'
                },
                'moderate': {
                    'factor': 0.35,
                    'regions': ['เชียงใหม่', 'ลำปาง', 'ลำพูน', 'พิษณุโลก', 'สุโขทัย'],
                    'description': 'เขตเสี่ยงปานกลาง',
                    'requirements': 'ความต้านทานแผ่นดินไหวปานกลาง-สูง'
                },
                'high': {
                    'factor': 0.50,
                    'regions': ['เชียงราย', 'แม่ฮ่องสอน', 'น่าน', 'พะเยา', 'กาญจนบุรี'],
                    'description': 'เขตเสี่ยงสูง',
                    'requirements': 'ความต้านทานแผ่นดินไหวสูง + รายละเอียดพิเศษ'
                }
            },
            'soil_types': {
                'A': 'หินแข็งมาก (Vs > 1500 m/s)',
                'B': 'หินแข็ง/ดินแข็งมาก (760 < Vs ≤ 1500 m/s)',
                'C': 'ดินแข็งปานกลาง (360 < Vs ≤ 760 m/s)',
                'D': 'ดินอ่อน (180 < Vs ≤ 360 m/s)',
                'E': 'ดินอ่อนมาก (Vs ≤ 180 m/s)'
            }
        }
    
    def get_wind_speed_map(self):
        """
        Get wind speed map for Thailand according to Thai standards
        แผนที่ความเร็วลมสำหรับประเทศไทยตามมาตรฐานไทย
        """
        return {
            'regions': {
                'central': {
                    'basic_wind_speed_ms': 35,
                    'provinces': ['กรุงเทพฯ', 'สมุทรปราการ', 'นนทบุรี', 'ปทุมธานี', 'สมุทรสาคร', 'นครปฐม'],
                    'description': 'ภาคกลาง',
                    'terrain': 'suburban',
                    'factors': {'gust': 1.2, 'direction': 1.0}
                },
                'northern': {
                    'basic_wind_speed_ms': 30,
                    'provinces': ['เชียงใหม่', 'เชียงราย', 'ลำปาง', 'ลำพูน', 'น่าน', 'พะเยา', 'แพร่'],
                    'description': 'ภาคเหนือ',
                    'terrain': 'suburban',
                    'factors': {'gust': 1.1, 'direction': 1.0}
                },
                'northeastern': {
                    'basic_wind_speed_ms': 32,
                    'provinces': ['นครราชสีมา', 'ขอนแก่น', 'อุดรธานี', 'อุบลราชธานี', 'สกลนคร'],
                    'description': 'ภาคตะวันออกเหนือ',
                    'terrain': 'open',
                    'factors': {'gust': 1.15, 'direction': 1.0}
                },
                'eastern': {
                    'basic_wind_speed_ms': 40,
                    'provinces': ['ชลบุรี', 'ระยอง', 'จันทบุรี', 'ตราด', 'สระแก้ว'],
                    'description': 'ภาคตะวันออก',
                    'terrain': 'coastal',
                    'factors': {'gust': 1.3, 'direction': 1.1}
                },
                'western': {
                    'basic_wind_speed_ms': 35,
                    'provinces': ['เพชรบุรี', 'ประจวบคีรีขันธ์', 'กาญจนบุรี', 'ราชบุรี'],
                    'description': 'ภาคตะวันตก',
                    'terrain': 'suburban',
                    'factors': {'gust': 1.2, 'direction': 1.0}
                },
                'southern': {
                    'basic_wind_speed_ms': 45,
                    'provinces': ['สงขลา', 'นครศรีธรรมราช', 'สุราษฎร์ธานี', 'ภูเก็ต', 'กระบี่', 'ตรัง'],
                    'description': 'ภาคใต้',
                    'terrain': 'coastal',
                    'factors': {'gust': 1.4, 'direction': 1.2}
                }
            },
            'special_zones': {
                'coastal_high_wind': {
                    'basic_wind_speed_ms': 50,
                    'description': 'เขตชายฝั่งลมแรง',
                    'provinces': ['สงขลา', 'นราธิวาส', 'ปัตตานี', 'ยะลา']
                },
                'mountain_sheltered': {
                    'basic_wind_speed_ms': 25,
                    'description': 'เขตภูเขากำบัง',
                    'provinces': ['แม่ฮ่องสอน', 'ตาก']
                }
            }
        }


def get_thai_design_instance():
    """Get singleton instance of Thai design requirements."""
    if not hasattr(get_thai_design_instance, 'instance'):
        get_thai_design_instance.instance = ThaiDesignRequirements()
    return get_thai_design_instance.instance


# Convenience functions for quick access
def get_thai_load_factors():
    """Get Thai load factors."""
    return get_thai_design_instance().load_factors

def get_thai_resistance_factors():
    """Get Thai resistance factors."""
    return get_thai_design_instance().resistance_factors

def get_thai_load_combinations():
    """Get Thai load combinations."""
    return get_thai_design_instance().get_load_combinations()

def calculate_thai_concrete_design(fc_prime, unit='MPa'):
    """Calculate Thai concrete design strength."""
    return get_thai_design_instance().get_concrete_design_strength(fc_prime, unit)

def calculate_thai_steel_design(fy, fu=None, unit='MPa'):
    """Calculate Thai steel design strength."""
    return get_thai_design_instance().get_steel_design_strength(fy, fu, unit)
