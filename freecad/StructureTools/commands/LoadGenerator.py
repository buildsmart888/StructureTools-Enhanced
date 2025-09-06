# -*- coding: utf-8 -*-
"""
LoadGenerator - Advanced load generation and management system

This module provides sophisticated load generation capabilities for structural analysis,
including automated load patterns, building code compliance, and dynamic load analysis.
"""

import FreeCAD as App
import FreeCADGui as Gui
import math
import json
from typing import List, Dict, Tuple, Optional, Any

# Import Thai units support
try:
    from ..utils.universal_thai_units import enhance_with_thai_units, thai_load_units, get_universal_thai_units
    from ..utils.thai_units import get_thai_converter
    THAI_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    enhance_with_thai_units = lambda x, t: x
    thai_load_units = lambda f: f
    get_universal_thai_units = lambda: None
    get_thai_converter = lambda: None

# Robust Qt imports with fallbacks
try:
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2.QtCore import Qt
except ImportError:
    try:
        from PySide import QtCore, QtGui
        from PySide import QtGui as QtWidgets
        from PySide.QtCore import Qt
    except ImportError:
        try:
            from PyQt5 import QtCore, QtGui, QtWidgets
            from PyQt5.QtCore import Qt
        except ImportError:
            try:
                from PyQt4 import QtCore, QtGui
                from PyQt4 import QtGui as QtWidgets
                from PyQt4.QtCore import Qt
            except ImportError:
                App.Console.PrintError("Could not import Qt libraries\n")
                QtCore = QtGui = QtWidgets = Qt = None


class LoadGeneratorManager:
    """
    Advanced load generation and management system.
    
    Provides comprehensive load generation capabilities including:
    - Automated load pattern generation
    - Building code compliance (ASCE 7, IBC, Eurocode)
    - Dynamic and time-dependent loads
    - Load combination generation
    - Integration with FEM analysis
    """
    
    def __init__(self):
        """Initialize LoadGenerator."""
        self.load_patterns = {}
        self.building_codes = ["ASCE 7-16", "IBC 2021", "Eurocode 1", "Thai Ministry B.E. 2566", "NBCC", "AS/NZS 1170"]
        self.load_types = ["Dead", "Live", "Wind", "Seismic", "Snow", "Thermal", "Dynamic"]
        self.load_combinations = []
        self.environmental_data = {}
        
    @thai_load_units
    def generateDeadLoads(self, structure_data):
        """Generate dead loads based on structure geometry and materials."""
        try:
            dead_loads = {}
            
            if "members" in structure_data:
                for member_id, member in structure_data["members"].items():
                    material = member.get("material", {})
                    geometry = member.get("geometry", {})
                    
                    # Calculate self-weight
                    density = material.get("density", 2400)  # kg/m³
                    volume = self.calculateMemberVolume(geometry)
                    
                    self_weight = density * volume * 9.81  # N
                    
                    dead_loads[f"SelfWeight_{member_id}"] = enhance_with_thai_units({
                        "type": "Dead",
                        "magnitude": self_weight,
                        "direction": [0, 0, -1],
                        "application": "distributed",
                        "member_id": member_id,
                        "force_kN": self_weight / 1000,  # Convert to kN for Thai units
                        "density_kg_m3": density
                    }, 'load')
            
            if "plates" in structure_data:
                for plate_id, plate in structure_data["plates"].items():
                    material = plate.get("material", {})
                    geometry = plate.get("geometry", {})
                    
                    # Calculate plate self-weight
                    density = material.get("density", 2400)
                    thickness = geometry.get("thickness", 0.2)
                    area = geometry.get("area", 1.0)
                    
                    self_weight = density * thickness * area * 9.81  # N
                    
                    dead_loads[f"PlateWeight_{plate_id}"] = {
                        "type": "Dead",
                        "magnitude": self_weight / area,  # N/m²
                        "direction": [0, 0, -1],
                        "application": "area",
                        "plate_id": plate_id
                    }
            
            App.Console.PrintMessage(f"Generated {len(dead_loads)} dead load patterns\n")
            return dead_loads
            
        except Exception as e:
            App.Console.PrintError(f"Error generating dead loads: {e}\n")
            return {}
    
    def generateLiveLoads(self, structure_data, building_code="ASCE 7-16"):
        """Generate live loads based on building code requirements."""
        try:
            live_loads = {}
            
            # Live load values based on building codes (psf converted to Pa)
            live_load_values = {
                "ASCE 7-16": {
                    "office": 50 * 47.88,      # 50 psf
                    "residential": 40 * 47.88,  # 40 psf
                    "classroom": 40 * 47.88,
                    "library": 60 * 47.88,
                    "retail": 75 * 47.88,
                    "warehouse": 125 * 47.88,
                    "parking": 40 * 47.88
                },
                "IBC 2021": {
                    "office": 50 * 47.88,
                    "residential": 40 * 47.88,
                    "classroom": 40 * 47.88,
                    "library": 60 * 47.88,
                    "retail": 75 * 47.88,
                    "warehouse": 125 * 47.88,
                    "parking": 40 * 47.88
                }
            }
            
            occupancy_type = structure_data.get("occupancy", "office")
            load_values = live_load_values.get(building_code, live_load_values["ASCE 7-16"])
            live_load_magnitude = load_values.get(occupancy_type, load_values["office"])
            
            if "floors" in structure_data:
                for floor_id, floor in structure_data["floors"].items():
                    live_loads[f"LiveLoad_{floor_id}"] = {
                        "type": "Live",
                        "magnitude": live_load_magnitude,
                        "direction": [0, 0, -1],
                        "application": "area",
                        "floor_id": floor_id,
                        "code": building_code,
                        "occupancy": occupancy_type
                    }
            
            App.Console.PrintMessage(f"Generated {len(live_loads)} live load patterns using {building_code}\n")
            return live_loads
            
        except Exception as e:
            App.Console.PrintError(f"Error generating live loads: {e}\n")
            return {}
    
    def generateWindLoads(self, structure_data, wind_parameters):
        """Generate wind loads based on building code provisions."""
        try:
            wind_loads = {}
            
            # Extract parameters
            basic_wind_speed = wind_parameters.get("basic_wind_speed", 120)  # mph
            exposure_category = wind_parameters.get("exposure_category", "C")
            building_height = wind_parameters.get("building_height", 30)  # ft
            building_width = wind_parameters.get("building_width", 100)  # ft
            building_length = wind_parameters.get("building_length", 200)  # ft
            
            # Convert to metric
            V = basic_wind_speed * 0.44704  # m/s
            h = building_height * 0.3048    # m
            B = building_width * 0.3048     # m
            L = building_length * 0.3048    # m
            
            # ASCE 7-16 simplified procedure
            # Velocity pressure: qz = 0.613 * Kz * Kzt * Kd * V²
            Kzt = wind_parameters.get("topographic_factor", 1.0)
            Kd = wind_parameters.get("directionality_factor", 0.85)
            
            # Exposure coefficient Kz
            exposure_factors = {
                "B": {"alpha": 7.0, "zg": 365.76},
                "C": {"alpha": 9.5, "zg": 274.32},
                "D": {"alpha": 11.5, "zg": 213.36}
            }
            
            exp_data = exposure_factors.get(exposure_category, exposure_factors["C"])
            alpha = exp_data["alpha"]
            zg = exp_data["zg"]
            
            if h < 4.57:  # 15 ft
                Kz = 0.85
            else:
                Kz = 2.01 * (h / zg) ** (2 / alpha)
            
            qz = 0.613 * Kz * Kzt * Kd * V * V  # Pa
            
            # Pressure coefficients (simplified)
            Cp_windward = 0.8
            Cp_leeward = -0.5
            Cp_side = -0.7
            Cp_roof = -0.9  # Flat roof
            
            # Generate wind pressure loads
            wind_loads["WindLoad_Windward"] = {
                "type": "Wind",
                "magnitude": qz * Cp_windward,
                "direction": [1, 0, 0],
                "application": "area",
                "surface": "windward_wall",
                "wind_speed": basic_wind_speed,
                "exposure": exposure_category
            }
            
            wind_loads["WindLoad_Leeward"] = {
                "type": "Wind",
                "magnitude": abs(qz * Cp_leeward),
                "direction": [-1, 0, 0],
                "application": "area",
                "surface": "leeward_wall"
            }
            
            wind_loads["WindLoad_Side1"] = {
                "type": "Wind",
                "magnitude": abs(qz * Cp_side),
                "direction": [0, -1, 0],
                "application": "area",
                "surface": "side_wall_1"
            }
            
            wind_loads["WindLoad_Side2"] = {
                "type": "Wind",
                "magnitude": abs(qz * Cp_side),
                "direction": [0, 1, 0],
                "application": "area",
                "surface": "side_wall_2"
            }
            
            wind_loads["WindLoad_Roof"] = {
                "type": "Wind",
                "magnitude": abs(qz * Cp_roof),
                "direction": [0, 0, -1],
                "application": "area",
                "surface": "roof"
            }
            
            App.Console.PrintMessage(f"Generated {len(wind_loads)} wind load patterns\n")
            App.Console.PrintMessage(f"Design wind pressure: {qz:.1f} Pa\n")
            
            return wind_loads
            
        except Exception as e:
            App.Console.PrintError(f"Error generating wind loads: {e}\n")
            return {}
    
    def generateSeismicLoads(self, structure_data, seismic_parameters):
        """Generate seismic loads based on building code provisions."""
        try:
            seismic_loads = {}
            
            # Extract parameters
            Ss = seismic_parameters.get("Ss", 1.5)  # Mapped spectral acceleration
            S1 = seismic_parameters.get("S1", 0.6)
            site_class = seismic_parameters.get("site_class", "D")
            importance_factor = seismic_parameters.get("importance_factor", 1.0)
            
            # Site coefficients (simplified)
            site_coefficients = {
                "A": {"Fa": 0.8, "Fv": 0.8},
                "B": {"Fa": 1.0, "Fv": 1.0},
                "C": {"Fa": 1.2, "Fv": 1.5},
                "D": {"Fa": 1.6, "Fv": 2.0},
                "E": {"Fa": 2.5, "Fv": 2.8}
            }
            
            Fa = site_coefficients[site_class]["Fa"]
            Fv = site_coefficients[site_class]["Fv"]
            
            # Design spectral accelerations
            SDS = (2/3) * Fa * Ss
            SD1 = (2/3) * Fv * S1
            
            # Seismic design category (simplified)
            if SDS < 0.167:
                SDC = "A"
            elif SDS < 0.33:
                SDC = "B"
            elif SDS < 0.5:
                SDC = "C"
            elif SDS < 0.75:
                SDC = "D"
            else:
                SDC = "E"
            
            # Base shear calculation (simplified)
            building_weight = structure_data.get("total_weight", 1000000)  # N
            R = seismic_parameters.get("response_modification", 8.0)  # Steel moment frame
            
            # Fundamental period (approximate)
            building_height = structure_data.get("height", 30) * 0.3048  # m
            Ct = 0.028  # Steel moment frame
            x = 0.8
            Ta = Ct * (building_height ** x)
            
            # Design response spectrum
            if Ta <= SD1/SDS:
                Cs = SDS * (0.4 + 0.6 * Ta * SDS / SD1) / R
            else:
                Cs = SD1 / (Ta * R)
            
            # Apply limits
            Cs = max(Cs, 0.044 * SDS * importance_factor)
            Cs = min(Cs, SDS / R)
            
            V = Cs * building_weight  # Base shear
            
            # Distribute base shear over height
            if "floors" in structure_data:
                total_wx_hx = 0
                floor_forces = {}
                
                for floor_id, floor in structure_data["floors"].items():
                    height = floor.get("height", 3.0)
                    weight = floor.get("weight", building_weight / len(structure_data["floors"]))
                    wx_hx = weight * height
                    total_wx_hx += wx_hx
                    floor_forces[floor_id] = {"weight": weight, "height": height, "wx_hx": wx_hx}
                
                for floor_id, data in floor_forces.items():
                    Fx = V * data["wx_hx"] / total_wx_hx
                    
                    seismic_loads[f"SeismicLoad_{floor_id}"] = {
                        "type": "Seismic",
                        "magnitude": Fx,
                        "direction": [1, 0, 0],  # X-direction
                        "application": "concentrated",
                        "floor_id": floor_id,
                        "height": data["height"],
                        "sds": SDS,
                        "sd1": SD1,
                        "sdc": SDC
                    }
            
            App.Console.PrintMessage(f"Generated {len(seismic_loads)} seismic load patterns\n")
            App.Console.PrintMessage(f"Base shear coefficient: {Cs:.4f}\n")
            App.Console.PrintMessage(f"Total base shear: {V:.0f} N\n")
            App.Console.PrintMessage(f"Seismic Design Category: {SDC}\n")
            
            return seismic_loads
            
        except Exception as e:
            App.Console.PrintError(f"Error generating seismic loads: {e}\n")
            return {}
    
    def generateLoadCombinations(self, load_types_present):
        """Generate load combinations based on building code."""
        try:
            combinations = []
            
            # ASCE 7-16 load combinations
            if "Dead" in load_types_present and "Live" in load_types_present:
                combinations.append({
                    "name": "1.4D",
                    "factors": {"Dead": 1.4}
                })
                
                combinations.append({
                    "name": "1.2D + 1.6L",
                    "factors": {"Dead": 1.2, "Live": 1.6}
                })
            
            if "Wind" in load_types_present:
                combinations.append({
                    "name": "1.2D + 1.0L + 1.0W",
                    "factors": {"Dead": 1.2, "Live": 1.0, "Wind": 1.0}
                })
                
                combinations.append({
                    "name": "0.9D + 1.0W",
                    "factors": {"Dead": 0.9, "Wind": 1.0}
                })
            
            if "Seismic" in load_types_present:
                combinations.append({
                    "name": "1.2D + 1.0L + 1.0E",
                    "factors": {"Dead": 1.2, "Live": 1.0, "Seismic": 1.0}
                })
                
                combinations.append({
                    "name": "0.9D + 1.0E",
                    "factors": {"Dead": 0.9, "Seismic": 1.0}
                })
            
            if "Snow" in load_types_present:
                combinations.append({
                    "name": "1.2D + 1.6S",
                    "factors": {"Dead": 1.2, "Snow": 1.6}
                })
                
                combinations.append({
                    "name": "1.2D + 1.0L + 1.6S",
                    "factors": {"Dead": 1.2, "Live": 1.0, "Snow": 1.6}
                })
            
            self.load_combinations = combinations
            App.Console.PrintMessage(f"Generated {len(combinations)} load combinations\n")
            
            return combinations
            
        except Exception as e:
            App.Console.PrintError(f"Error generating load combinations: {e}\n")
            return []
    
    def calculateMemberVolume(self, geometry):
        """Calculate member volume from geometry data."""
        try:
            if "length" in geometry and "cross_section" in geometry:
                length = geometry["length"]
                cross_section = geometry["cross_section"]
                
                if "area" in cross_section:
                    return length * cross_section["area"]
                else:
                    # Estimate area for common sections
                    if "width" in cross_section and "height" in cross_section:
                        return length * cross_section["width"] * cross_section["height"]
            
            return 0.01  # Default small volume
            
        except Exception:
            return 0.01
    
    def exportLoads(self, loads, filename, format_type="JSON"):
        """Export loads to file."""
        try:
            if format_type.upper() == "JSON":
                with open(filename, 'w') as f:
                    json.dump(loads, f, indent=2)
            
            elif format_type.upper() == "CSV":
                import csv
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Load ID", "Type", "Magnitude", "Direction X", "Direction Y", "Direction Z", "Application"])
                    
                    for load_id, load_data in loads.items():
                        direction = load_data.get("direction", [0, 0, 0])
                        writer.writerow([
                            load_id,
                            load_data.get("type", ""),
                            load_data.get("magnitude", 0),
                            direction[0],
                            direction[1],
                            direction[2],
                            load_data.get("application", "")
                        ])
            
            App.Console.PrintMessage(f"Loads exported to: {filename}\n")
            return True
            
        except Exception as e:
            App.Console.PrintError(f"Error exporting loads: {e}\n")
            return False
    
    def calculate_wind_load_thai(self, basic_wind_speed, height, terrain_category, structure_type, region='general'):
        """
        Calculate wind load according to Thai Ministry B.E. 2566
        คำนวณภาระลมตามกฎกระทรวง พ.ศ. 2566
        
        Args:
            basic_wind_speed: ความเร็วลมพื้นฐาน (m/s)
            height: ความสูงอาคาร (m)
            terrain_category: ประเภทภูมิประเทศ ('open', 'suburban', 'urban', 'city')
            structure_type: ประเภทโครงสร้าง ('building', 'tower', 'bridge')
            region: ภูมิภาคในประเทศไทย ('general', 'coastal', 'mountain')
        """
        import math
        
        # ตารางค่าความหยาบผิวสำหรับภูมิประเทศต่างๆ ตามมาตรฐานไทย
        terrain_factors = {
            'open': {'z0': 0.03, 'zmin': 5, 'alpha': 0.12},      # ที่ราบโล่ง
            'suburban': {'z0': 0.30, 'zmin': 10, 'alpha': 0.16}, # ชานเมือง
            'urban': {'z0': 1.00, 'zmin': 15, 'alpha': 0.22},    # เมือง
            'city': {'z0': 2.00, 'zmin': 20, 'alpha': 0.30}      # ใจกลางเมืองใหญ่
        }
        
        # ปัจจัยภูมิภาคสำหรับประเทศไทย
        region_factors = {
            'general': 1.0,    # ทั่วไป
            'coastal': 1.15,   # ชายฝั่งทะเล
            'mountain': 0.85   # ภูเขา/ที่สูง
        }
        
        if terrain_category not in terrain_factors:
            terrain_category = 'suburban'
        if region not in region_factors:
            region = 'general'
            
        terrain = terrain_factors[terrain_category]
        region_factor = region_factors[region]
        
        # ความเร็วลมพื้นฐานปรับปรุงด้วยภูมิภาค
        vb = basic_wind_speed * region_factor
        
        # ความดันลมพื้นฐาน (kN/m²)
        qb = 0.5 * 1.25 * (vb**2) / 1000
        
        # ความสูงขั้นต่ำ
        zmin = terrain['zmin']
        effective_height = max(height, zmin)
        
        # ปัจจัยความสูง (Height factor)
        if effective_height <= 200:
            kr = 0.19 * (terrain['z0'] / 0.05) ** 0.07
            ce = kr * math.log(effective_height / terrain['z0'])
        else:
            # สำหรับอาคารสูงมาก (>200m)
            ce = kr * math.log(200 / terrain['z0']) * (effective_height / 200) ** 0.2
        
        # ปัจจัยแรงกระแทก (Gust factor)
        if structure_type == 'building':
            cf = 1.25  # อาคาร
        elif structure_type == 'tower':
            cf = 1.40  # หอคอย
        elif structure_type == 'bridge':
            cf = 1.30  # สะพาน
        else:
            cf = 1.25
        
        # ความดันลมสูงสุด
        qp = qb * ce * cf
        
        # ค่าสัมประสิทธิ์แรงดัน (ปรับปรุงตามมาตรฐานไทย)
        if structure_type == 'building':
            cpe_windward = 0.8   # ด้านรับลม
            cpe_leeward = -0.5   # ด้านหลังลม
            cpe_side = -0.7      # ด้านข้าง
            cpi = 0.2            # ภายใน (อาคารปิด)
        else:
            cpe_windward = 1.0
            cpe_leeward = -0.4
            cpe_side = -0.6
            cpi = 0.0
        
        # แรงดันลมสุทธิ
        wind_pressure_windward = qp * (cpe_windward - cpi)
        wind_pressure_leeward = qp * (cpe_leeward - cpi)
        wind_pressure_side = qp * (cpe_side - cpi)
        
        # แรงลมรวม (kN/m²)
        total_wind_pressure = abs(wind_pressure_windward) + abs(wind_pressure_leeward)
        
        return {
            'basic_wind_pressure_kN_m2': qb,
            'basic_wind_pressure_ksc_m2': qb * 101.97,  # แปลงเป็น ksc/m²
            'peak_velocity_pressure_kN_m2': qp,
            'peak_velocity_pressure_ksc_m2': qp * 101.97,
            'wind_pressure_windward_kN_m2': wind_pressure_windward,
            'wind_pressure_windward_ksc_m2': wind_pressure_windward * 101.97,
            'wind_pressure_leeward_kN_m2': wind_pressure_leeward,
            'wind_pressure_leeward_ksc_m2': wind_pressure_leeward * 101.97,
            'wind_pressure_side_kN_m2': wind_pressure_side,
            'wind_pressure_side_ksc_m2': wind_pressure_side * 101.97,
            'total_wind_pressure_kN_m2': total_wind_pressure,
            'total_wind_pressure_ksc_m2': total_wind_pressure * 101.97,
            'height_factor': ce,
            'gust_factor': cf,
            'terrain_category': terrain_category,
            'region': region,
            'code': 'Thai Ministry B.E. 2566',
            'code_thai': 'กฎกระทรวง พ.ศ. 2566',
            'description_thai': f'การคำนวณภาระลมสำหรับ{structure_type}ในเขต{terrain_category}ภูมิภาค{region}'
        }
    
    def calculate_seismic_load_thai(self, zone_factor, soil_type, structure_type, importance_factor=1.0, height=10.0, weight=1000.0):
        """
        Calculate seismic load according to Thai Ministry B.E. 2566
        คำนวณภาระแผ่นดินไหวตามกฎกระทรวง พ.ศ. 2566
        
        Args:
            zone_factor: ปัจจัยเขตแผ่นดินไหว (Z) สำหรับประเทศไทย
            soil_type: ประเภทดิน ('A', 'B', 'C', 'D', 'E')
            structure_type: ประเภทโครงสร้าง ('concrete_frame', 'steel_frame', 'masonry', 'wood')
            importance_factor: ปัจจัยความสำคัญ (I)
            height: ความสูงอาคาร (m)
            weight: น้ำหนักอาคาร (kN)
        """
        import math
        
        # ปัจจัยเขตแผ่นดินไหวสำหรับประเทศไทย
        thai_zone_factors = {
            'very_low': 0.15,   # เขตเสี่ยงต่ำมาก (ภาคกลาง ภาคใต้)
            'low': 0.25,        # เขตเสี่ยงต่ำ (ภาคตะวันออก ภาคตะวันตก)
            'moderate': 0.35,   # เขตเสี่ยงปานกลาง (ภาคเหนือตอนล่าง)
            'high': 0.50        # เขตเสี่ยงสูง (ภาคเหนือตอนบน เขตแดนพม่า)
        }
        
        # ปัจจัยดิน (Site coefficients)
        soil_factors = {
            'A': {'Fa': 0.8, 'Fv': 0.8, 'description': 'หินแข็งมาก'},
            'B': {'Fa': 1.0, 'Fv': 1.0, 'description': 'หินแข็ง/ดินแข็งมาก'},
            'C': {'Fa': 1.2, 'Fv': 1.8, 'description': 'ดินแข็งปานกลาง'},
            'D': {'Fa': 1.6, 'Fv': 2.4, 'description': 'ดินอ่อน'},
            'E': {'Fa': 2.5, 'Fv': 3.5, 'description': 'ดินอ่อนมาก'}
        }
        
        # ปัจจัยระบบโครงสร้าง (Response modification factor)
        structure_factors = {
            'concrete_frame': {'R': 8, 'Cd': 5.5, 'description': 'โครงคอนกรีตเสริมเหล็ก'},
            'steel_frame': {'R': 8, 'Cd': 5.5, 'description': 'โครงเหล็ก'},
            'masonry': {'R': 5, 'Cd': 4.0, 'description': 'อิฐบล็อก'},
            'wood': {'R': 6.5, 'Cd': 4.0, 'description': 'โครงไม้'}
        }
        
        if isinstance(zone_factor, str) and zone_factor in thai_zone_factors:
            Z = thai_zone_factors[zone_factor]
            zone_description = zone_factor
        else:
            Z = float(zone_factor)
            zone_description = 'custom'
        
        if soil_type not in soil_factors:
            soil_type = 'C'
        if structure_type not in structure_factors:
            structure_type = 'concrete_frame'
            
        soil = soil_factors[soil_type]
        structure = structure_factors[structure_type]
        
        # การคำนวณตามมาตรฐานไทย (ดัดแปลงจาก ASCE 7)
        # ความเร่งแผ่นดินไหวในแนวนอน
        SMS = Z * soil['Fa']    # Short period
        SM1 = Z * soil['Fv']    # 1-second period
        
        # ความเร่งการออกแบบ
        SDS = (2.0/3.0) * SMS
        SD1 = (2.0/3.0) * SM1
        
        # คาบการสั่นพื้นฐาน (Fundamental period)
        if structure_type == 'concrete_frame':
            Ct = 0.0466
            x = 0.9
        elif structure_type == 'steel_frame':
            Ct = 0.0724
            x = 0.8
        else:
            Ct = 0.0466
            x = 0.75
            
        Ta = Ct * (height ** x)
        
        # ค่าสัมประสิทธิ์แผ่นดินไหวการออกแบบ
        if Ta <= (SD1 / SDS):
            Cs = SDS / structure['R']
        else:
            Cs = SD1 / (Ta * structure['R'])
        
        # ข้อจำกัดค่า Cs
        Cs_max = SMS / structure['R']
        Cs_min = max(0.044 * SDS, 0.01)
        
        if Z >= 0.75:  # เขตแผ่นดินไหวสูง
            Cs_min = max(Cs_min, 0.5 * Z / structure['R'])
            
        Cs = max(min(Cs, Cs_max), Cs_min)
        
        # แรงแผ่นดินไหวพื้นฐาน
        V = Cs * weight
        
        # การกระจายแรงตามความสูง (สำหรับอาคารสม่ำเสมอ)
        if height <= 15:
            # อาคารเตี้ย - แรงกระจายเท่ากัน
            force_distribution = 'uniform'
            base_shear_ratio = 1.0
        else:
            # อาคารสูง - แรงเพิ่มขึ้นตามความสูง
            force_distribution = 'triangular'
            base_shear_ratio = 0.85  # ส่วนใหญ่กระจายแบบสามเหลี่ยม
        
        return {
            'design_base_shear_kN': V,
            'design_base_shear_tf': V / 9.807,  # แปลงเป็นตัน
            'response_coefficient': Cs,
            'design_acceleration_SDS': SDS,
            'design_acceleration_SD1': SD1,
            'fundamental_period_sec': Ta,
            'zone_factor': Z,
            'zone_description': zone_description,
            'soil_type': soil_type,
            'soil_description_thai': soil['description'],
            'structure_type': structure_type,
            'structure_description_thai': structure['description'],
            'importance_factor': importance_factor,
            'response_modification_R': structure['R'],
            'deflection_amplification_Cd': structure['Cd'],
            'force_distribution': force_distribution,
            'base_shear_ratio': base_shear_ratio,
            'code': 'Thai Ministry B.E. 2566',
            'code_thai': 'กฎกระทรวง พ.ศ. 2566',
            'description_thai': f'การคำนวณภาระแผ่นดินไหวสำหรับ{structure["description"]}บนดินประเภท{soil["description"]}'
        }
    
    def calculate_live_load_thai(self, occupancy_type, area=1.0, location='general'):
        """
        Calculate live loads according to Thai Ministry B.E. 2566
        คำนวณภาระจรตามกฎกระทรวง พ.ศ. 2566
        
        Args:
            occupancy_type: ประเภทการใช้งาน
            area: พื้นที่ (m²)
            location: ตำแหน่ง ('general', 'roof', 'balcony')
        """
        # ภาระจรตามมาตรฐานไทย (kN/m² และ ksc/m²)
        thai_live_loads = {
            'residential': {
                'general': {'kN_m2': 1.5, 'description': 'อาคารที่อยู่อาศัย'},
                'roof': {'kN_m2': 0.5, 'description': 'หลังคาอาคารที่อยู่อาศัย'},
                'balcony': {'kN_m2': 3.0, 'description': 'ระเบียงอาคารที่อยู่อาศัย'}
            },
            'office': {
                'general': {'kN_m2': 2.5, 'description': 'อาคารสำนักงาน'},
                'roof': {'kN_m2': 0.75, 'description': 'หลังคาอาคารสำนักงาน'},
                'balcony': {'kN_m2': 4.0, 'description': 'ระเบียงอาคารสำนักงาน'}
            },
            'commercial': {
                'general': {'kN_m2': 4.0, 'description': 'อาคารพาณิชย์'},
                'roof': {'kN_m2': 1.0, 'description': 'หลังคาอาคารพาณิชย์'},
                'balcony': {'kN_m2': 5.0, 'description': 'ระเบียงอาคารพาณิชย์'}
            },
            'industrial': {
                'general': {'kN_m2': 5.0, 'description': 'อาคารอุตสาหกรรม'},
                'roof': {'kN_m2': 1.5, 'description': 'หลังคาอาคารอุตสาหกรรม'},
                'balcony': {'kN_m2': 6.0, 'description': 'ระเบียงอาคารอุตสาหกรรม'}
            },
            'school': {
                'general': {'kN_m2': 3.0, 'description': 'อาคารโรงเรียน'},
                'roof': {'kN_m2': 0.75, 'description': 'หลังคาอาคารโรงเรียน'},
                'balcony': {'kN_m2': 4.0, 'description': 'ระเบียงอาคารโรงเรียน'}
            },
            'hospital': {
                'general': {'kN_m2': 2.0, 'description': 'อาคารโรงพยาบาล'},
                'roof': {'kN_m2': 0.75, 'description': 'หลังคาอาคารโรงพยาบาล'},
                'balcony': {'kN_m2': 4.0, 'description': 'ระเบียงอาคารโรงพยาบาล'}
            },
            'warehouse': {
                'general': {'kN_m2': 7.5, 'description': 'อาคารคลังสินค้า'},
                'roof': {'kN_m2': 1.0, 'description': 'หลังคาอาคารคลังสินค้า'},
                'balcony': {'kN_m2': 7.5, 'description': 'ระเบียงอาคารคลังสินค้า'}
            },
            'parking': {
                'general': {'kN_m2': 2.5, 'description': 'อาคารจอดรถ'},
                'roof': {'kN_m2': 1.0, 'description': 'หลังคาอาคารจอดรถ'},
                'balcony': {'kN_m2': 2.5, 'description': 'ระเบียงอาคารจอดรถ'}
            }
        }
        
        if occupancy_type not in thai_live_loads:
            occupancy_type = 'office'  # default
        if location not in thai_live_loads[occupancy_type]:
            location = 'general'  # default
            
        load_data = thai_live_loads[occupancy_type][location]
        live_load_kN_m2 = load_data['kN_m2']
        
        # ปัจจัยลดภาระจรสำหรับพื้นที่ใหญ่ (ตามมาตรฐานไทย)
        if area > 20 and location == 'general':
            if area <= 100:
                reduction_factor = 0.95
            elif area <= 500:
                reduction_factor = 0.90
            else:
                reduction_factor = 0.85
        else:
            reduction_factor = 1.0
            
        reduced_live_load = live_load_kN_m2 * reduction_factor
        total_load = reduced_live_load * area
        
        return {
            'live_load_kN_m2': reduced_live_load,
            'live_load_ksc_m2': reduced_live_load * 101.97,  # แปลงเป็น ksc/m²
            'total_load_kN': total_load,
            'total_load_tf': total_load / 9.807,  # แปลงเป็นตัน
            'original_load_kN_m2': live_load_kN_m2,
            'reduction_factor': reduction_factor,
            'area_m2': area,
            'occupancy_type': occupancy_type,
            'location': location,
            'description_thai': load_data['description'],
            'code': 'Thai Ministry B.E. 2566',
            'code_thai': 'กฎกระทรวง พ.ศ. 2566'
        }


class LoadGeneratorDialog(QtWidgets.QDialog if QtWidgets else object):
    """Load Generator GUI Dialog."""
    
    def __init__(self):
        """Initialize dialog."""
        if not QtWidgets:
            App.Console.PrintError("Qt not available - cannot create GUI\n")
            return
            
        super(LoadGeneratorDialog, self).__init__()
        self.setWindowTitle("Load Generator")
        self.setModal(True)  # Make dialog modal
        self.resize(800, 600)
        
        self.load_manager = LoadGeneratorManager()
        self.generated_loads = {}
        
        self.setupUI()
    
    def setupUI(self):
        """Setup user interface."""
        if not QtWidgets:
            return
            
        layout = QtWidgets.QVBoxLayout()
        
        # Title
        title = QtWidgets.QLabel("Advanced Load Generator")
        title.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(title)
        
        # Tabs
        tabs = QtWidgets.QTabWidget()
        
        # Dead Loads Tab
        dead_tab = self.createDeadLoadsTab()
        tabs.addTab(dead_tab, "Dead Loads")
        
        # Live Loads Tab
        live_tab = self.createLiveLoadsTab()
        tabs.addTab(live_tab, "Live Loads")
        
        # Wind Loads Tab
        wind_tab = self.createWindLoadsTab()
        tabs.addTab(wind_tab, "Wind Loads")
        
        # Seismic Loads Tab
        seismic_tab = self.createSeismicLoadsTab()
        tabs.addTab(seismic_tab, "Seismic Loads")
        
        # Combinations Tab
        combo_tab = self.createCombinationsTab()
        tabs.addTab(combo_tab, "Load Combinations")
        
        layout.addWidget(tabs)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        generate_btn = QtWidgets.QPushButton("Generate All Loads")
        generate_btn.clicked.connect(self.generateAllLoads)
        button_layout.addWidget(generate_btn)
        
        export_btn = QtWidgets.QPushButton("Export Loads")
        export_btn.clicked.connect(self.exportLoads)
        button_layout.addWidget(export_btn)
        
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        button_layout.addWidget(close_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def createDeadLoadsTab(self):
        """Create dead loads tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Instructions
        instructions = QtWidgets.QLabel(
            "Dead loads are automatically calculated based on material densities and geometry."
        )
        instructions.setWordWrap(True)
        layout.addWidget(instructions)
        
        # Material density override
        density_group = QtWidgets.QGroupBox("Material Density Override")
        density_layout = QtWidgets.QFormLayout()
        
        self.concrete_density = QtWidgets.QSpinBox()
        self.concrete_density.setRange(2000, 3000)
        self.concrete_density.setValue(2400)
        self.concrete_density.setSuffix(" kg/m³")
        density_layout.addRow("Concrete:", self.concrete_density)
        
        self.steel_density = QtWidgets.QSpinBox()
        self.steel_density.setRange(7000, 8000)
        self.steel_density.setValue(7850)
        self.steel_density.setSuffix(" kg/m³")
        density_layout.addRow("Steel:", self.steel_density)
        
        density_group.setLayout(density_layout)
        layout.addWidget(density_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def createLiveLoadsTab(self):
        """Create live loads tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Building code selection
        code_group = QtWidgets.QGroupBox("Building Code")
        code_layout = QtWidgets.QVBoxLayout()
        
        self.building_code = QtWidgets.QComboBox()
        self.building_code.addItems(["ASCE 7-16", "IBC 2021", "Eurocode 1", "NBCC", "AS/NZS 1170"])
        code_layout.addWidget(self.building_code)
        
        code_group.setLayout(code_layout)
        layout.addWidget(code_group)
        
        # Occupancy type
        occupancy_group = QtWidgets.QGroupBox("Occupancy Type")
        occupancy_layout = QtWidgets.QVBoxLayout()
        
        self.occupancy_type = QtWidgets.QComboBox()
        self.occupancy_type.addItems([
            "office", "residential", "classroom", "library", 
            "retail", "warehouse", "parking"
        ])
        occupancy_layout.addWidget(self.occupancy_type)
        
        occupancy_group.setLayout(occupancy_layout)
        layout.addWidget(occupancy_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def createWindLoadsTab(self):
        """Create wind loads tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Wind parameters
        wind_group = QtWidgets.QGroupBox("Wind Parameters")
        wind_layout = QtWidgets.QFormLayout()
        
        self.wind_speed = QtWidgets.QSpinBox()
        self.wind_speed.setRange(80, 200)
        self.wind_speed.setValue(120)
        self.wind_speed.setSuffix(" mph")
        wind_layout.addRow("Basic Wind Speed:", self.wind_speed)
        
        self.exposure_category = QtWidgets.QComboBox()
        self.exposure_category.addItems(["B", "C", "D"])
        self.exposure_category.setCurrentText("C")
        wind_layout.addRow("Exposure Category:", self.exposure_category)
        
        self.building_height = QtWidgets.QDoubleSpinBox()
        self.building_height.setRange(10.0, 500.0)
        self.building_height.setValue(30.0)
        self.building_height.setSuffix(" ft")
        wind_layout.addRow("Building Height:", self.building_height)
        
        self.building_width = QtWidgets.QDoubleSpinBox()
        self.building_width.setRange(10.0, 1000.0)
        self.building_width.setValue(100.0)
        self.building_width.setSuffix(" ft")
        wind_layout.addRow("Building Width:", self.building_width)
        
        self.building_length = QtWidgets.QDoubleSpinBox()
        self.building_length.setRange(10.0, 1000.0)
        self.building_length.setValue(200.0)
        self.building_length.setSuffix(" ft")
        wind_layout.addRow("Building Length:", self.building_length)
        
        wind_group.setLayout(wind_layout)
        layout.addWidget(wind_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def createSeismicLoadsTab(self):
        """Create seismic loads tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Seismic parameters
        seismic_group = QtWidgets.QGroupBox("Seismic Parameters")
        seismic_layout = QtWidgets.QFormLayout()
        
        self.ss_value = QtWidgets.QDoubleSpinBox()
        self.ss_value.setRange(0.1, 3.0)
        self.ss_value.setValue(1.5)
        self.ss_value.setDecimals(2)
        seismic_layout.addRow("Ss (Mapped Spectral Acceleration):", self.ss_value)
        
        self.s1_value = QtWidgets.QDoubleSpinBox()
        self.s1_value.setRange(0.1, 2.0)
        self.s1_value.setValue(0.6)
        self.s1_value.setDecimals(2)
        seismic_layout.addRow("S1 (Mapped Spectral Acceleration):", self.s1_value)
        
        self.site_class = QtWidgets.QComboBox()
        self.site_class.addItems(["A", "B", "C", "D", "E"])
        self.site_class.setCurrentText("D")
        seismic_layout.addRow("Site Class:", self.site_class)
        
        self.importance_factor = QtWidgets.QDoubleSpinBox()
        self.importance_factor.setRange(1.0, 1.5)
        self.importance_factor.setValue(1.0)
        self.importance_factor.setDecimals(1)
        seismic_layout.addRow("Importance Factor:", self.importance_factor)
        
        self.response_modification = QtWidgets.QDoubleSpinBox()
        self.response_modification.setRange(1.0, 10.0)
        self.response_modification.setValue(8.0)
        self.response_modification.setDecimals(1)
        seismic_layout.addRow("Response Modification Factor (R):", self.response_modification)
        
        seismic_group.setLayout(seismic_layout)
        layout.addWidget(seismic_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def createCombinationsTab(self):
        """Create load combinations tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        # Instructions
        instructions = QtWidgets.QLabel(
            "Load combinations will be automatically generated based on the load types present and selected building code."
        )
        instructions.setWordWrap(True)
        layout.addWidget(instructions)
        
        # Results display
        self.combinations_text = QtWidgets.QTextEdit()
        self.combinations_text.setReadOnly(True)
        layout.addWidget(self.combinations_text)
        
        widget.setLayout(layout)
        return widget
    
    def generateAllLoads(self):
        """Generate all selected loads."""
        try:
            # Sample structure data (in practice, this would come from the current model)
            structure_data = {
                "members": {
                    "1": {
                        "material": {"density": self.concrete_density.value()},
                        "geometry": {"length": 10.0, "cross_section": {"area": 0.04}}
                    }
                },
                "plates": {
                    "1": {
                        "material": {"density": self.concrete_density.value()},
                        "geometry": {"thickness": 0.2, "area": 100.0}
                    }
                },
                "floors": {
                    "1": {"height": 3.0, "weight": 500000},
                    "2": {"height": 6.0, "weight": 500000},
                    "3": {"height": 9.0, "weight": 500000}
                },
                "occupancy": self.occupancy_type.currentText(),
                "total_weight": 1500000,
                "height": self.building_height.value()
            }
            
            all_loads = {}
            
            # Generate dead loads
            dead_loads = self.load_manager.generateDeadLoads(structure_data)
            all_loads.update(dead_loads)
            
            # Generate live loads
            live_loads = self.load_manager.generateLiveLoads(
                structure_data, 
                self.building_code.currentText()
            )
            all_loads.update(live_loads)
            
            # Generate wind loads
            wind_parameters = {
                "basic_wind_speed": self.wind_speed.value(),
                "exposure_category": self.exposure_category.currentText(),
                "building_height": self.building_height.value(),
                "building_width": self.building_width.value(),
                "building_length": self.building_length.value()
            }
            wind_loads = self.load_manager.generateWindLoads(structure_data, wind_parameters)
            all_loads.update(wind_loads)
            
            # Generate seismic loads
            seismic_parameters = {
                "Ss": self.ss_value.value(),
                "S1": self.s1_value.value(),
                "site_class": self.site_class.currentText(),
                "importance_factor": self.importance_factor.value(),
                "response_modification": self.response_modification.value()
            }
            seismic_loads = self.load_manager.generateSeismicLoads(structure_data, seismic_parameters)
            all_loads.update(seismic_loads)
            
            self.generated_loads = all_loads
            
            # Generate load combinations
            load_types = list(set(load["type"] for load in all_loads.values()))
            combinations = self.load_manager.generateLoadCombinations(load_types)
            
            # Display combinations
            combo_text = "Generated Load Combinations:\n\n"
            for combo in combinations:
                combo_text += f"{combo['name']}:\n"
                for load_type, factor in combo['factors'].items():
                    combo_text += f"  {factor:.1f} × {load_type}\n"
                combo_text += "\n"
            
            self.combinations_text.setPlainText(combo_text)
            
            QtWidgets.QMessageBox.information(
                self, 
                "Load Generation Complete", 
                f"Successfully generated {len(all_loads)} load patterns and {len(combinations)} load combinations."
            )
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error generating loads: {e}")
    
    def exportLoads(self):
        """Export generated loads."""
        if not self.generated_loads:
            QtWidgets.QMessageBox.warning(self, "Warning", "No loads to export. Generate loads first.")
            return
        
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, 
            "Export Loads", 
            "loads.json", 
            "JSON Files (*.json);;CSV Files (*.csv)"
        )
        
        if filename:
            format_type = "JSON" if filename.lower().endswith('.json') else "CSV"
            success = self.load_manager.exportLoads(self.generated_loads, filename, format_type)
            
            if success:
                QtWidgets.QMessageBox.information(self, "Export Complete", f"Loads exported to {filename}")
            else:
                QtWidgets.QMessageBox.critical(self, "Export Failed", "Failed to export loads")


class LoadGeneratorCommand:
    """Command to open Load Generator dialog."""
    
    def GetResources(self):
        """Get command resources."""
        return {
            'Pixmap': 'load_generator.svg',
            'MenuText': 'Load Generator',
            'ToolTip': 'Generate structural loads automatically based on building codes'
        }
    
    def IsActive(self):
        """Check if command is active."""
        return True
    
    def Activated(self):
        """Execute the command."""
        try:
            if QtWidgets:
                dialog = LoadGeneratorDialog()
                dialog.exec_()
            else:
                App.Console.PrintError("Qt libraries not available - cannot open Load Generator GUI\n")
                App.Console.PrintMessage("Load Generator functionality available through Python API\n")
                
                # Demonstrate API usage
                manager = LoadGeneratorManager()
                
                sample_structure = {
                    "members": {"1": {"material": {"density": 2400}, "geometry": {"length": 10.0, "cross_section": {"area": 0.04}}}},
                    "occupancy": "office"
                }
                
                dead_loads = manager.generateDeadLoads(sample_structure)
                live_loads = manager.generateLiveLoads(sample_structure)
                
                App.Console.PrintMessage("Sample loads generated:\n")
                for load_id, load_data in {**dead_loads, **live_loads}.items():
                    App.Console.PrintMessage(f"  {load_id}: {load_data['magnitude']:.2f} N ({load_data['type']})\n")
        
        except Exception as e:
            App.Console.PrintError(f"Error opening Load Generator: {e}\n")


def createLoadGeneratorCommand():
    """Create and register the Load Generator command."""
    if hasattr(Gui, 'addCommand'):
        Gui.addCommand('LoadGenerator', LoadGeneratorCommand())
        App.Console.PrintMessage("Load Generator command registered\n")
    else:
        App.Console.PrintMessage("Load Generator available as LoadGeneratorManager class\n")


# Register command when module is imported
if __name__ != "__main__":
    try:
        createLoadGeneratorCommand()
    except Exception as e:
        App.Console.PrintMessage(f"Load Generator module loaded (command registration: {e})\n")
