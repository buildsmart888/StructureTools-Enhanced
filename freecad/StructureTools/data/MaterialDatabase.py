# -*- coding: utf-8 -*-
"""
Material Database for StructureTools
Contains comprehensive material properties for common structural materials
following international standards with full Thai units support.
"""

# Import Thai units support
try:
    from ..utils.thai_units import get_thai_converter
    THAI_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    get_thai_converter = None

class MaterialDatabase:
    """Database of standard structural materials with properties and Thai units support"""
    
    def __init__(self):
        """Initialize material database with Thai units converter."""
        self.thai_converter = get_thai_converter() if THAI_UNITS_AVAILABLE else None
    
    def _add_thai_units(self, material_data):
        """Add Thai units to material properties."""
        if not self.thai_converter:
            return material_data
        
        # Add Thai units for strength properties
        if 'yield_strength' in material_data:
            fy_mpa = material_data['yield_strength']
            material_data['yield_strength_ksc'] = self.thai_converter.mpa_to_ksc(fy_mpa)
        
        if 'ultimate_strength' in material_data:
            fu_mpa = material_data['ultimate_strength']
            material_data['ultimate_strength_ksc'] = self.thai_converter.mpa_to_ksc(fu_mpa)
        
        if 'compressive_strength' in material_data:
            fc_mpa = material_data['compressive_strength']
            material_data['compressive_strength_ksc'] = self.thai_converter.mpa_to_ksc(fc_mpa)
        
        if 'modulus_elasticity' in material_data:
            e_mpa = material_data['modulus_elasticity']
            material_data['modulus_elasticity_ksc'] = self.thai_converter.mpa_to_ksc(e_mpa)
        
        # Add force conversion for density (to tf/m³)
        if 'density' in material_data:
            density_kg_m3 = material_data['density']
            material_data['density_tf_m3'] = density_kg_m3 / 1000  # tf/m³
        
        return material_data
    
    @staticmethod
    def get_steel_materials():
        """Get standard steel materials with Thai units support"""
        materials = {
            # ASTM Steel Standards
            "ASTM A36": {
                "name": "ASTM A36 - Structural Steel",
                "standard": "ASTM A36/A36M",
                "type": "Carbon Steel",
                "modulus_elasticity": 200000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 250,  # MPa
                "ultimate_strength": 400,  # MPa
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "General purpose structural steel"
            },
            "ASTM A572 Gr50": {
                "name": "ASTM A572 Grade 50 - High Strength Steel",
                "standard": "ASTM A572/A572M",
                "type": "High Strength Low Alloy Steel",
                "modulus_elasticity": 200000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 345,  # MPa
                "ultimate_strength": 450,  # MPa
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "High strength structural steel for bridges and buildings"
            },
            "ASTM A992": {
                "name": "ASTM A992 - Wide Flange Steel",
                "standard": "ASTM A992/A992M",
                "type": "Carbon Steel",
                "modulus_elasticity": 200000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 345,  # MPa (50 ksi)
                "ultimate_strength": 450,  # MPa (65 ksi)
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "Standard for structural shapes, plates and bars"
            },
            
            # European Steel Standards (EN)
            "S235": {
                "name": "EN 10025 S235 - Structural Steel",
                "standard": "EN 10025-2",
                "type": "Non-alloy Structural Steel",
                "modulus_elasticity": 210000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 235,  # MPa
                "ultimate_strength": 360,  # MPa
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "General structural steel (European standard)"
            },
            "S355": {
                "name": "EN 10025 S355 - High Strength Steel",
                "standard": "EN 10025-2",
                "type": "Non-alloy Structural Steel",
                "modulus_elasticity": 210000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 355,  # MPa
                "ultimate_strength": 510,  # MPa
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "High strength structural steel (European standard)"
            },
            "S460": {
                "name": "EN 10025 S460 - Very High Strength Steel",
                "standard": "EN 10025-4",
                "type": "Thermomechanical Steel",
                "modulus_elasticity": 210000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 460,  # MPa
                "ultimate_strength": 570,  # MPa
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "Very high strength structural steel"
            },
            
            # Japanese Steel Standards (JIS)
            "SS400": {
                "name": "JIS G3101 SS400 - Rolled Steel",
                "standard": "JIS G3101",
                "type": "Carbon Steel",
                "modulus_elasticity": 205000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 245,  # MPa
                "ultimate_strength": 400,  # MPa
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "General structural rolled steel (Japanese standard)"
            },
            "SM490": {
                "name": "JIS G3106 SM490 - Welded Steel",
                "standard": "JIS G3106",
                "type": "Rolled Steel for Welded Structure",
                "modulus_elasticity": 205000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 325,  # MPa
                "ultimate_strength": 490,  # MPa
                "thermal_expansion": 12.0e-6,  # /°C
                "description": "Weldable structural steel (Japanese standard)"
            },
            
            # Thai Standards (TIS & Ministry B.E. 2566)
            "TIS 20-2543 SR24": {
                "name": "TIS 20-2543 SR24 - Thai Mild Steel",
                "standard": "TIS 20-2543 (Thai Ministry B.E. 2566)",
                "type": "Round Bar Steel",
                "modulus_elasticity": 200000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 235.4,  # MPa (2400 ksc)
                "ultimate_strength": 372.7,  # MPa (3800 ksc)
                "thermal_expansion": 12.0e-6,  # /°C
                "fy_ksc": 2400,  # Thai traditional unit
                "fu_ksc": 3800,
                "description": "เหล็กกลม SR24 สำหรับงานโครงสร้างทั่วไป",
                "description_english": "Round steel SR24 for general structural use",
                "applications": ["เหล็กเส้นเสริม", "งานโครงสร้างทั่วไป"],
                "applications_english": ["reinforcement bars", "general structures"]
            },
            "TIS 24-2548 SD40": {
                "name": "TIS 24-2548 SD40 - Thai Deformed Bar",
                "standard": "TIS 24-2548 (Thai Ministry B.E. 2566)",
                "type": "Deformed Bar Steel",
                "modulus_elasticity": 200000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 392.4,  # MPa (4000 ksc)
                "ultimate_strength": 589.5,  # MPa (6000 ksc)
                "thermal_expansion": 12.0e-6,  # /°C
                "fy_ksc": 4000,  # Thai traditional unit
                "fu_ksc": 6000,
                "min_elongation": 18.0,  # %
                "surface_type": "deformed",
                "description": "เหล็กข้ออ้อย SD40 สำหรับคอนกรีตเสริมเหล็ก",
                "description_english": "Deformed bar SD40 for reinforced concrete",
                "applications": ["คอนกรีตเสริมเหล็ก", "งานโครงสร้างหลัก"],
                "applications_english": ["reinforced concrete", "main structural work"],
                "bar_sizes": ["DB10", "DB12", "DB16", "DB20", "DB25", "DB32"],
                "typical_uses": ["เสาคอนกรีต", "คานคอนกรีต", "พื้นคอนกรีต"]
            },
            "TIS 24-2548 SD50": {
                "name": "TIS 24-2548 SD50 - Thai High Strength Deformed Bar",
                "standard": "TIS 24-2548 (Thai Ministry B.E. 2566)",
                "type": "High Strength Deformed Bar Steel",
                "modulus_elasticity": 200000,  # MPa
                "poisson_ratio": 0.30,
                "density": 7850,  # kg/m³
                "yield_strength": 490.5,  # MPa (5000 ksc)
                "ultimate_strength": 686.7,  # MPa (7000 ksc)
                "thermal_expansion": 12.0e-6,  # /°C
                "fy_ksc": 5000,  # Thai traditional unit
                "fu_ksc": 7000,
                "min_elongation": 16.0,  # %
                "surface_type": "deformed",
                "description": "เหล็กข้ออ้อย SD50 ความแข็งแรงสูง",
                "description_english": "High strength deformed bar SD50",
                "applications": ["งานโครงสร้างพิเศษ", "อาคารสูง", "สะพาน"],
                "applications_english": ["special structures", "high-rise buildings", "bridges"],
                "bar_sizes": ["DB16", "DB20", "DB25", "DB32", "DB36", "DB40"],
                "typical_uses": ["อาคารสูง", "งานโครงสร้างหนัก", "สะพาน"]
            }
        }
        
        # Add Thai units to all materials
        if THAI_UNITS_AVAILABLE:
            converter = get_thai_converter()
            db = MaterialDatabase()
            for key, material in materials.items():
                materials[key] = db._add_thai_units(material)
        
        return materials
    
    @staticmethod
    def get_concrete_materials():
        """Get standard concrete materials with Thai units support"""
        materials = {
            # Thai Standards (Ministry B.E. 2566)
            "Thai Fc180": {
                "name": "Thai Fc180 - คอนกรีตเกรด 180",
                "standard": "Thai Ministry B.E. 2566 (มยผ. 1101)",
                "type": "Normal Weight Concrete",
                "compressive_strength": 18.0,  # MPa
                "yield_strength": 18.0,  # MPa
                "ultimate_strength": 18.0,  # MPa
                "compressive_strength_ksc": 180.0,  # Thai unit
                "elastic_modulus": 19998,  # MPa (4700√fc)
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "thermal_expansion": 10.0e-6,  # /°C
                "min_cement_content": 280,  # kg/m³
                "max_water_cement_ratio": 0.65,
                "slump_range": [5, 15],  # cm
                "description": "คอนกรีตเกรด 180 กิโลกรัมต่อตารางเซนติเมตร",
                "description_english": "Concrete Grade 180 ksc",
                "typical_uses": ["งานทั่วไป", "รั้ว", "ฐานราก"],
                "typical_uses_english": ["general work", "fencing", "foundations"],
                "phi_factors": {
                    "flexure": 0.90,
                    "compression": 0.65,
                    "shear": 0.75
                }
            },
            "Thai Fc210": {
                "name": "Thai Fc210 - คอนกรีตเกรด 210",
                "standard": "Thai Ministry B.E. 2566 (มยผ. 1101)",
                "type": "Normal Weight Concrete",
                "compressive_strength": 21.0,  # MPa
                "yield_strength": 21.0,  # MPa
                "ultimate_strength": 21.0,  # MPa
                "compressive_strength_ksc": 210.0,  # Thai unit
                "elastic_modulus": 21579,  # MPa (4700√fc)
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "thermal_expansion": 10.0e-6,  # /°C
                "min_cement_content": 300,  # kg/m³
                "max_water_cement_ratio": 0.60,
                "slump_range": [5, 15],  # cm
                "description": "คอนกรีตเกรด 210 กิโลกรัมต่อตารางเซนติเมตร",
                "description_english": "Concrete Grade 210 ksc (Most Common)",
                "typical_uses": ["อาคารพักอาศัย", "โรงงาน", "อาคารพาณิชย์"],
                "typical_uses_english": ["residential buildings", "factories", "commercial buildings"],
                "phi_factors": {
                    "flexure": 0.90,
                    "compression": 0.65,
                    "shear": 0.75
                }
            },
            "Thai Fc280": {
                "name": "Thai Fc280 - คอนกรีตเกรด 280",
                "standard": "Thai Ministry B.E. 2566 (มยผ. 1101)",
                "type": "High Strength Normal Weight Concrete",
                "compressive_strength": 28.0,  # MPa
                "yield_strength": 28.0,  # MPa
                "ultimate_strength": 28.0,  # MPa
                "compressive_strength_ksc": 280.0,  # Thai unit
                "elastic_modulus": 24870,  # MPa (4700√fc)
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "thermal_expansion": 10.0e-6,  # /°C
                "min_cement_content": 350,  # kg/m³
                "max_water_cement_ratio": 0.50,
                "slump_range": [5, 12],  # cm
                "description": "คอนกรีตเกรด 280 กิโลกรัมต่อตารางเซนติเมตร",
                "description_english": "High Strength Concrete Grade 280 ksc",
                "typical_uses": ["อาคารสูง", "สะพาน", "งานโครงสร้างหนัก"],
                "typical_uses_english": ["high-rise buildings", "bridges", "heavy structures"],
                "phi_factors": {
                    "flexure": 0.90,
                    "compression": 0.65,
                    "shear": 0.75
                },
                "durability_class": "high",
                "environmental_suitability": ["normal", "aggressive"]
            },
            "Thai Fc350": {
                "name": "Thai Fc350 - คอนกรีตเกรด 350",
                "standard": "Thai Ministry B.E. 2566 (มยผ. 1101)",
                "type": "Very High Strength Concrete",
                "compressive_strength": 35.0,  # MPa
                "yield_strength": 35.0,  # MPa
                "ultimate_strength": 35.0,  # MPa
                "compressive_strength_ksc": 350.0,  # Thai unit
                "elastic_modulus": 27838,  # MPa (4700√fc)
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "thermal_expansion": 10.0e-6,  # /°C
                "min_cement_content": 400,  # kg/m³
                "max_water_cement_ratio": 0.45,
                "slump_range": [5, 10],  # cm
                "description": "คอนกรีตกำลังสูงสุด Fc350",
                "description_english": "Maximum strength concrete Fc350",
                "typical_uses": ["งานพิเศษ", "วิจัยและพัฒนา"],
                "typical_uses_english": ["special applications", "research and development"],
                "phi_factors": {
                    "flexure": 0.90,
                    "compression": 0.65,
                    "shear": 0.75
                },
                "durability_class": "very_high",
                "environmental_suitability": ["normal", "aggressive", "marine"],
                "special_requirements": "ต้องมีการควบคุมคุณภาพพิเศษ"
            },
            
            # ACI Concrete Standards
            "Normal Weight C25": {
                "name": "Normal Weight Concrete f'c = 25 MPa",
                "standard": "ACI 318",
                "type": "Normal Weight Concrete",
                "modulus_elasticity": 25743,  # MPa (4700√f'c)
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "compressive_strength": 25,  # MPa
                "yield_strength": 25,  # MPa
                "ultimate_strength": 25,  # MPa
                "tensile_strength": 2.7,  # MPa (0.33√f'c)
                "thermal_expansion": 10.0e-6,  # /°C
                "description": "Standard concrete for general construction"
            },
            "Normal Weight C30": {
                "name": "Normal Weight Concrete f'c = 30 MPa",
                "standard": "ACI 318",
                "type": "Normal Weight Concrete",
                "modulus_elasticity": 28043,  # MPa
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "compressive_strength": 30,  # MPa
                "yield_strength": 30,  # MPa
                "ultimate_strength": 30,  # MPa
                "tensile_strength": 2.96,  # MPa
                "thermal_expansion": 10.0e-6,  # /°C
                "description": "Standard concrete for structural applications"
            },
            "High Strength C50": {
                "name": "High Strength Concrete f'c = 50 MPa",
                "standard": "ACI 318",
                "type": "High Strength Concrete",
                "modulus_elasticity": 36197,  # MPa
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "compressive_strength": 50,  # MPa
                "yield_strength": 50,  # MPa
                "ultimate_strength": 50,  # MPa
                "tensile_strength": 3.82,  # MPa
                "thermal_expansion": 10.0e-6,  # /°C
                "description": "High strength concrete for high-rise buildings"
            },
            
            # European Concrete Standards (Eurocode)
            "C20/25": {
                "name": "Concrete C20/25 (EN 1992)",
                "standard": "EN 1992 (Eurocode 2)",
                "type": "Normal Weight Concrete",
                "modulus_elasticity": 30000,  # MPa (Table 3.1 EC2)
                "poisson_ratio": 0.20,
                "density": 2500,  # kg/m³
                "compressive_strength": 20,  # MPa (cylinder)
                "cube_strength": 25,  # MPa (cube)
                "yield_strength": 20,  # MPa
                "ultimate_strength": 20,  # MPa
                "tensile_strength": 2.2,  # MPa
                "thermal_expansion": 10.0e-6,  # /°C
                "description": "Standard concrete (Eurocode 2)"
            },
            "C30/37": {
                "name": "Concrete C30/37 (EN 1992)",
                "standard": "EN 1992 (Eurocode 2)",
                "type": "Normal Weight Concrete",
                "modulus_elasticity": 33000,  # MPa
                "poisson_ratio": 0.20,
                "density": 2500,  # kg/m³
                "compressive_strength": 30,  # MPa (cylinder)
                "cube_strength": 37,  # MPa (cube)
                "yield_strength": 30,  # MPa
                "ultimate_strength": 30,  # MPa
                "tensile_strength": 2.9,  # MPa
                "thermal_expansion": 10.0e-6,  # /°C
                "description": "Medium strength concrete (Eurocode 2)"
            },
            
            # Lightweight Concrete
            "Lightweight C20": {
                "name": "Lightweight Concrete f'c = 20 MPa",
                "standard": "ACI 318",
                "type": "Lightweight Concrete",
                "modulus_elasticity": 17000,  # MPa (reduced for LW concrete)
                "poisson_ratio": 0.20,
                "density": 1800,  # kg/m³
                "compressive_strength": 20,  # MPa
                "yield_strength": 20,  # MPa
                "ultimate_strength": 20,  # MPa
                "tensile_strength": 1.8,  # MPa (lower for LW)
                "thermal_expansion": 8.0e-6,  # /°C
                "description": "Lightweight concrete for reduced dead load"
            }
        }
    
    @staticmethod
    def get_aluminum_materials():
        """Get standard aluminum materials"""
        return {
            # Aluminum Alloys
            "6061-T6": {
                "name": "Aluminum Alloy 6061-T6",
                "standard": "ASTM B221",
                "type": "Heat-treated Aluminum Alloy",
                "modulus_elasticity": 68900,  # MPa (10,000 ksi)
                "poisson_ratio": 0.33,
                "density": 2700,  # kg/m³
                "yield_strength": 276,  # MPa (40 ksi)
                "ultimate_strength": 310,  # MPa (45 ksi)
                "thermal_expansion": 23.6e-6,  # /°C
                "description": "General purpose structural aluminum alloy"
            },
            "6063-T5": {
                "name": "Aluminum Alloy 6063-T5",
                "standard": "ASTM B221",
                "type": "Extruded Aluminum Alloy",
                "modulus_elasticity": 68900,  # MPa
                "poisson_ratio": 0.33,
                "density": 2700,  # kg/m³
                "yield_strength": 214,  # MPa (31 ksi)
                "ultimate_strength": 241,  # MPa (35 ksi)
                "thermal_expansion": 23.6e-6,  # /°C
                "description": "Extruded aluminum for architectural applications"
            },
            "5083-H116": {
                "name": "Aluminum Alloy 5083-H116",
                "standard": "ASTM B209",
                "type": "Marine Grade Aluminum",
                "modulus_elasticity": 70300,  # MPa
                "poisson_ratio": 0.33,
                "density": 2660,  # kg/m³
                "yield_strength": 228,  # MPa (33 ksi)
                "ultimate_strength": 317,  # MPa (46 ksi)
                "thermal_expansion": 23.8e-6,  # /°C
                "description": "Marine grade aluminum with high corrosion resistance"
            }
        }
    
    @staticmethod
    def get_timber_materials():
        """Get standard timber materials"""
        return {
            # Softwood Timber
            "Douglas Fir-Larch": {
                "name": "Douglas Fir-Larch (Structural)",
                "standard": "NDS (National Design Specification)",
                "type": "Softwood Lumber",
                "modulus_elasticity": 13100,  # MPa (1.9M psi)
                "poisson_ratio": 0.30,
                "density": 550,  # kg/m³
                "bending_strength": 12.4,  # MPa (Grade: Select Structural)
                "yield_strength": 12.4,  # MPa
                "ultimate_strength": 12.4,  # MPa
                "compression_parallel": 7.6,  # MPa
                "compression_perpendicular": 6.2,  # MPa
                "thermal_expansion": 4.5e-6,  # /°C (parallel to grain)
                "description": "High strength structural softwood"
            },
            "Southern Pine": {
                "name": "Southern Pine (Structural)",
                "standard": "NDS",
                "type": "Softwood Lumber",
                "modulus_elasticity": 14500,  # MPa
                "poisson_ratio": 0.30,
                "density": 590,  # kg/m³
                "bending_strength": 11.2,  # MPa
                "yield_strength": 11.2,  # MPa
                "ultimate_strength": 11.2,  # MPa
                "compression_parallel": 8.3,  # MPa
                "compression_perpendicular": 5.9,  # MPa
                "thermal_expansion": 4.2e-6,  # /°C
                "description": "Dense structural softwood"
            },
            
            # Engineered Timber
            "Glulam Class GL24h": {
                "name": "Glued Laminated Timber GL24h",
                "standard": "EN 14080",
                "type": "Glued Laminated Timber",
                "modulus_elasticity": 11500,  # MPa
                "poisson_ratio": 0.30,
                "density": 420,  # kg/m³
                "bending_strength": 24.0,  # MPa
                "yield_strength": 24.0,  # MPa
                "ultimate_strength": 24.0,  # MPa
                "compression_parallel": 24.0,  # MPa
                "compression_perpendicular": 2.7,  # MPa
                "thermal_expansion": 5.0e-6,  # /°C
                "description": "High strength glued laminated timber"
            },
            "CLT Grade C24": {
                "name": "Cross Laminated Timber (CLT) C24",
                "standard": "EN 16351",
                "type": "Cross Laminated Timber",
                "modulus_elasticity": 12000,  # MPa (major direction)
                "poisson_ratio": 0.30,
                "density": 470,  # kg/m³
                "bending_strength": 24.0,  # MPa
                "yield_strength": 24.0,  # MPa
                "ultimate_strength": 24.0,  # MPa
                "compression_parallel": 21.0,  # MPa
                "compression_perpendicular": 3.0,  # MPa
                "thermal_expansion": 5.0e-6,  # /°C
                "description": "Cross laminated timber for structural panels"
            }
        }
    
    @staticmethod
    def get_masonry_materials():
        """Get standard masonry materials"""
        return {
            # Clay Brick Masonry
            "Clay Brick (High Strength)": {
                "name": "Clay Brick Masonry (High Strength)",
                "standard": "ASTM C62",
                "type": "Clay Brick Masonry",
                "modulus_elasticity": 20000,  # MPa
                "poisson_ratio": 0.20,
                "density": 2000,  # kg/m³
                "compressive_strength": 20.0,  # MPa
                "yield_strength": 20.0,  # MPa
                "ultimate_strength": 20.0,  # MPa
                "flexural_strength": 1.5,  # MPa
                "thermal_expansion": 5.4e-6,  # /°C
                "description": "High strength clay brick masonry"
            },
            
            # Concrete Masonry Units
            "CMU Normal Weight": {
                "name": "Concrete Masonry Unit (Normal Weight)",
                "standard": "ASTM C90",
                "type": "Concrete Masonry",
                "modulus_elasticity": 18000,  # MPa
                "poisson_ratio": 0.20,
                "density": 2100,  # kg/m³
                "compressive_strength": 15.0,  # MPa
                "yield_strength": 15.0,  # MPa
                "ultimate_strength": 15.0,  # MPa
                "flexural_strength": 1.2,  # MPa
                "thermal_expansion": 8.0e-6,  # /°C
                "description": "Standard concrete masonry units"
            },
            
            # Stone Masonry
            "Granite": {
                "name": "Granite (Natural Stone)",
                "standard": "ASTM C615",
                "type": "Natural Stone",
                "modulus_elasticity": 60000,  # MPa
                "poisson_ratio": 0.25,
                "density": 2650,  # kg/m³
                "compressive_strength": 130.0,  # MPa
                "yield_strength": 130.0,  # MPa
                "ultimate_strength": 130.0,  # MPa
                "flexural_strength": 8.0,  # MPa
                "thermal_expansion": 8.0e-6,  # /°C
                "description": "High strength natural granite"
            }
        }
    
    @staticmethod
    def get_all_materials():
        """Get all materials organized by category"""
        return {
            "Steel": MaterialDatabase.get_steel_materials(),
            "Concrete": MaterialDatabase.get_concrete_materials(),  
            "Aluminum": MaterialDatabase.get_aluminum_materials(),
            "Timber": MaterialDatabase.get_timber_materials(),
            "Masonry": MaterialDatabase.get_masonry_materials()
        }
    
    @staticmethod
    def get_material_by_name(material_name):
        """Get specific material by name"""
        all_materials = MaterialDatabase.get_all_materials()
        
        for category, materials in all_materials.items():
            if material_name in materials:
                return materials[material_name]
        
        return None
    
    @staticmethod
    def search_materials_by_standard(standard_name):
        """Search materials by standard (e.g., 'ASTM', 'EN', 'ACI')"""
        results = {}
        all_materials = MaterialDatabase.get_all_materials()
        
        for category, materials in all_materials.items():
            category_results = {}
            for name, props in materials.items():
                if standard_name.upper() in props["standard"].upper():
                    category_results[name] = props
            
            if category_results:
                results[category] = category_results
        
        return results
    
    @staticmethod
    def get_material_categories():
        """Get list of available material categories"""
        return ["Steel", "Concrete", "Aluminum", "Timber", "Masonry"]