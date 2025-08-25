# -*- coding: utf-8 -*-
"""
Material Database for StructureTools
Contains comprehensive material properties for common structural materials
following international standards.
"""

class MaterialDatabase:
    """Database of standard structural materials with properties"""
    
    @staticmethod
    def get_steel_materials():
        """Get standard steel materials"""
        return {
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
            }
        }
    
    @staticmethod
    def get_concrete_materials():
        """Get standard concrete materials"""
        return {
            # ACI Concrete Standards
            "Normal Weight C25": {
                "name": "Normal Weight Concrete f'c = 25 MPa",
                "standard": "ACI 318",
                "type": "Normal Weight Concrete",
                "modulus_elasticity": 25743,  # MPa (4700√f'c)
                "poisson_ratio": 0.20,
                "density": 2400,  # kg/m³
                "compressive_strength": 25,  # MPa
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