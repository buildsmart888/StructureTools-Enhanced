# -*- coding: utf-8 -*-
"""
LoadTemplates.py - Preset load templates for common building occupancies

This module provides standardized load values based on building codes
including Thai Ministry of Interior B.E. 2566, ASCE 7-16, and IBC 2018.
"""

# Load templates organized by building code
LOAD_TEMPLATES = {
    # ==========================================================================
    # Thai Ministry of Interior B.E. 2566
    # ==========================================================================
    "Thai_BE2566": {
        "name": "กฎกระทรวง พ.ศ. 2566",
        "loads": {
            "DL_Concrete_Slab_15cm": {
                "type": "DL",
                "name": "พื้น คสล. หนา 15 ซม.",
                "magnitude_kN_m2": 3.6,
                "magnitude_ksc": 0.36,
                "description": "Dead load for 15cm reinforced concrete slab"
            },
            "DL_Concrete_Slab_20cm": {
                "type": "DL",
                "name": "พื้น คสล. หนา 20 ซม.",
                "magnitude_kN_m2": 4.8,
                "magnitude_ksc": 0.48,
                "description": "Dead load for 20cm reinforced concrete slab"
            },
            "DL_Tile_Finish": {
                "type": "DL",
                "name": "ปูกระเบื้อง + ปูน",
                "magnitude_kN_m2": 1.0,
                "magnitude_ksc": 0.10,
                "description": "Floor tile and mortar finish"
            },
            "DL_Ceiling_MEP": {
                "type": "DL",
                "name": "ฝ้าเพดาน + งาน M&E",
                "magnitude_kN_m2": 0.5,
                "magnitude_ksc": 0.05,
                "description": "Suspended ceiling and MEP systems"
            },
            "LL_Office": {
                "type": "LL",
                "name": "สำนักงาน",
                "magnitude_kN_m2": 2.0,
                "magnitude_ksc": 0.20,
                "description": "Office live load per Thai code"
            },
            "LL_Residential": {
                "type": "LL",
                "name": "ที่พักอาศัย",
                "magnitude_kN_m2": 1.5,
                "magnitude_ksc": 0.15,
                "description": "Residential live load per Thai code"
            },
            "LL_Retail": {
                "type": "LL",
                "name": "ห้างสรรพสินค้า",
                "magnitude_kN_m2": 4.0,
                "magnitude_ksc": 0.40,
                "description": "Retail/department store live load"
            },
            "LL_Parking": {
                "type": "LL",
                "name": "ที่จอดรถยนต์",
                "magnitude_kN_m2": 5.0,
                "magnitude_ksc": 0.50,
                "description": "Parking garage live load"
            },
            "LL_Corridor": {
                "type": "LL",
                "name": "ทางเดิน/บันได",
                "magnitude_kN_m2": 3.0,
                "magnitude_ksc": 0.30,
                "description": "Corridor and stair live load"
            },
            "LL_Assembly": {
                "type": "LL",
                "name": "ห้องประชุม",
                "magnitude_kN_m2": 5.0,
                "magnitude_ksc": 0.50,
                "description": "Assembly area live load"
            },
            "LL_Roof": {
                "type": "LL_Roof",
                "name": "หลังคา (ไม่ขึ้นได้)",
                "magnitude_kN_m2": 0.5,
                "magnitude_ksc": 0.05,
                "description": "Inaccessible roof live load"
            },
            "LL_Roof_Accessible": {
                "type": "LL_Roof",
                "name": "หลังคา (ขึ้นได้)",
                "magnitude_kN_m2": 1.5,
                "magnitude_ksc": 0.15,
                "description": "Accessible roof live load"
            }
        }
    },
    
    # ==========================================================================
    # ASCE 7-16
    # ==========================================================================
    "ASCE_7_16": {
        "name": "ASCE 7-16",
        "loads": {
            "LL_Office": {
                "type": "LL",
                "name": "Office",
                "magnitude_kN_m2": 2.4,  # 50 psf
                "magnitude_psf": 50,
                "description": "Office floor live load"
            },
            "LL_Residential": {
                "type": "LL",
                "name": "Residential",
                "magnitude_kN_m2": 1.9,  # 40 psf
                "magnitude_psf": 40,
                "description": "Residential floor live load"
            },
            "LL_Retail_First_Floor": {
                "type": "LL",
                "name": "Retail (First Floor)",
                "magnitude_kN_m2": 4.8,  # 100 psf
                "magnitude_psf": 100,
                "description": "First floor retail live load"
            },
            "LL_Retail_Upper": {
                "type": "LL",
                "name": "Retail (Upper Floors)",
                "magnitude_kN_m2": 3.6,  # 75 psf
                "magnitude_psf": 75,
                "description": "Upper floor retail live load"
            },
            "LL_Corridor_Public": {
                "type": "LL",
                "name": "Corridor (Public)",
                "magnitude_kN_m2": 4.8,  # 100 psf
                "magnitude_psf": 100,
                "description": "Public corridor live load"
            },
            "LL_Assembly_Fixed_Seats": {
                "type": "LL",
                "name": "Assembly (Fixed Seats)",
                "magnitude_kN_m2": 2.9,  # 60 psf
                "magnitude_psf": 60,
                "description": "Assembly with fixed seats"
            },
            "LL_Assembly_Movable_Seats": {
                "type": "LL",
                "name": "Assembly (Movable Seats)",
                "magnitude_kN_m2": 4.8,  # 100 psf
                "magnitude_psf": 100,
                "description": "Assembly with movable seats"
            },
            "LL_Library_Reading": {
                "type": "LL",
                "name": "Library (Reading Room)",
                "magnitude_kN_m2": 2.9,  # 60 psf
                "magnitude_psf": 60,
                "description": "Library reading room"
            },
            "LL_Library_Stack": {
                "type": "LL",
                "name": "Library (Stack Room)",
                "magnitude_kN_m2": 7.2,  # 150 psf
                "magnitude_psf": 150,
                "description": "Library stack room"
            },
            "LL_Hospital": {
                "type": "LL",
                "name": "Hospital",
                "magnitude_kN_m2": 1.9,  # 40 psf
                "magnitude_psf": 40,
                "description": "Hospital patient room"
            },
            "LL_Parking_Car": {
                "type": "LL",
                "name": "Parking (Passenger Cars)",
                "magnitude_kN_m2": 1.9,  # 40 psf
                "magnitude_psf": 40,
                "description": "Parking for passenger vehicles"
            },
            "LL_Storage_Light": {
                "type": "LL",
                "name": "Storage (Light)",
                "magnitude_kN_m2": 6.0,  # 125 psf
                "magnitude_psf": 125,
                "description": "Light storage"
            },
            "LL_Storage_Heavy": {
                "type": "LL",
                "name": "Storage (Heavy)",
                "magnitude_kN_m2": 12.0,  # 250 psf
                "magnitude_psf": 250,
                "description": "Heavy storage"
            },
            "LL_Roof_Ordinary": {
                "type": "LL_Roof",
                "name": "Roof (Ordinary)",
                "magnitude_kN_m2": 1.0,  # 20 psf
                "magnitude_psf": 20,
                "description": "Ordinary flat roof"
            }
        }
    }
}


def get_template(code: str, template_id: str) -> dict:
    """
    Get a specific load template.
    
    Args:
        code: Building code identifier (e.g., "Thai_BE2566", "ASCE_7_16")
        template_id: Template identifier (e.g., "LL_Office")
    
    Returns:
        Template dictionary or None if not found
    """
    if code in LOAD_TEMPLATES:
        return LOAD_TEMPLATES[code]["loads"].get(template_id)
    return None


def get_all_templates(code: str = None) -> list:
    """
    Get all templates, optionally filtered by building code.
    
    Args:
        code: Optional building code filter
    
    Returns:
        List of (code, template_id, template_dict) tuples
    """
    result = []
    codes = [code] if code else LOAD_TEMPLATES.keys()
    
    for c in codes:
        if c in LOAD_TEMPLATES:
            for tid, template in LOAD_TEMPLATES[c]["loads"].items():
                result.append((c, tid, template))
    
    return result


def get_template_categories() -> dict:
    """
    Get templates organized by load type category.
    
    Returns:
        Dictionary with load types as keys and template lists as values
    """
    categories = {"DL": [], "LL": [], "LL_Roof": [], "W": [], "E": []}
    
    for code, code_data in LOAD_TEMPLATES.items():
        for tid, template in code_data["loads"].items():
            load_type = template.get("type", "OTHER")
            if load_type not in categories:
                categories[load_type] = []
            categories[load_type].append({
                "code": code,
                "id": tid,
                **template
            })
    
    return categories
