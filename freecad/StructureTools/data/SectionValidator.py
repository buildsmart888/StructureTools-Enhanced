# -*- coding: utf-8 -*-
"""
Section Validation and Professional Features

Advanced validation and professional features for structural sections.
"""

import math
from typing import Dict, List, Tuple, Optional

def validate_section_for_design_code(section_data: Dict, design_code: str = "AISC_360") -> Tuple[bool, List[str], List[str]]:
    """
    Validate section properties against design code requirements.
    
    Args:
        section_data: Section properties dictionary
        design_code: Design code to validate against
        
    Returns:
        Tuple of (is_valid, errors, warnings)
    """
    errors = []
    warnings = []
    
    try:
        if design_code == "AISC_360":
            is_valid, code_errors, code_warnings = validate_aisc_360_section(section_data)
            errors.extend(code_errors)
            warnings.extend(code_warnings)
        elif design_code == "EN_1993":
            is_valid, code_errors, code_warnings = validate_en_1993_section(section_data)
            errors.extend(code_errors)
            warnings.extend(code_warnings)
        else:
            warnings.append(f"Unknown design code: {design_code}")
            is_valid = True
            
        return len(errors) == 0, errors, warnings
        
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors, warnings

def validate_aisc_360_section(section_data: Dict) -> Tuple[bool, List[str], List[str]]:
    """Validate section against AISC 360 requirements."""
    errors = []
    warnings = []
    
    try:
        section_type = section_data.get("Type", "")
        
        if "Wide Flange" in section_type or "I-Beam" in section_type:
            # I-section checks
            bf = section_data.get("FlangeWidth", 0)
            tf = section_data.get("FlangeThickness", 0)  
            tw = section_data.get("WebThickness", 0)
            d = section_data.get("Depth", 0)
            
            if bf and tf and tw and d:
                # Local buckling checks
                bf_2tf = bf / (2 * tf)
                h_tw = (d - 2*tf) / tw
                
                # Compact limits (AISC 360, Table B4.1b)
                bf_2tf_compact_limit = 0.38 * math.sqrt(29000/50)  # Assuming Fy = 50 ksi
                h_tw_compact_limit = 3.76 * math.sqrt(29000/50)
                
                if bf_2tf > bf_2tf_compact_limit:
                    if bf_2tf > 1.0 * math.sqrt(29000/50):  # Non-compact limit
                        warnings.append(f"Slender flange: bf/2tf = {bf_2tf:.1f} > {1.0 * math.sqrt(29000/50):.1f}")
                    else:
                        warnings.append(f"Non-compact flange: bf/2tf = {bf_2tf:.1f}")
                        
                if h_tw > h_tw_compact_limit:
                    if h_tw > 5.7 * math.sqrt(29000/50):  # Non-compact limit
                        warnings.append(f"Slender web: h/tw = {h_tw:.1f} > {5.7 * math.sqrt(29000/50):.1f}")
                    else:
                        warnings.append(f"Non-compact web: h/tw = {h_tw:.1f}")
        
        # General checks
        weight = section_data.get("Weight", 0)
        if weight > 500:  # kg/m
            warnings.append(f"Very heavy section: {weight} kg/m - check lifting requirements")
        
        return len(errors) == 0, errors, warnings
        
    except Exception as e:
        errors.append(f"AISC validation error: {str(e)}")
        return False, errors, warnings

def validate_en_1993_section(section_data: Dict) -> Tuple[bool, List[str], List[str]]:
    """Validate section against EN 1993 (Eurocode 3) requirements."""
    errors = []
    warnings = []
    
    try:
        section_type = section_data.get("Type", "")
        
        if "I-Beam" in section_type or "H-Beam" in section_type:
            # European I-section checks
            bf = section_data.get("FlangeWidth", 0)
            tf = section_data.get("FlangeThickness", 0)
            tw = section_data.get("WebThickness", 0)
            d = section_data.get("Depth", 0)
            
            if bf and tf and tw and d:
                # Class limits (EN 1993-1-1, Table 5.2)
                c_tf = (bf/2 - tw/2) / tf  # Outstand of flange
                c_tw = (d - 2*tf) / tw     # Web slenderness
                
                epsilon = math.sqrt(235 / 355)  # Assuming S355 steel
                
                # Class 1 (plastic) limits
                c_tf_class1 = 9 * epsilon
                c_tw_class1 = 72 * epsilon
                
                # Class 2 (compact) limits  
                c_tf_class2 = 10 * epsilon
                c_tw_class2 = 83 * epsilon
                
                # Class 3 (semi-compact) limits
                c_tf_class3 = 14 * epsilon
                c_tw_class3 = 124 * epsilon
                
                # Determine section class
                if c_tf > c_tf_class3 or c_tw > c_tw_class3:
                    warnings.append(f"Class 4 (slender) section: c/tf={c_tf:.1f}, c/tw={c_tw:.1f}")
                elif c_tf > c_tf_class2 or c_tw > c_tw_class2:
                    warnings.append(f"Class 3 (semi-compact) section: c/tf={c_tf:.1f}, c/tw={c_tw:.1f}")
                elif c_tf > c_tf_class1 or c_tw > c_tw_class1:
                    warnings.append(f"Class 2 (compact) section: c/tf={c_tf:.1f}, c/tw={c_tw:.1f}")
                else:
                    # Class 1 - no warning needed
                    pass
        
        return len(errors) == 0, errors, warnings
        
    except Exception as e:
        errors.append(f"EN 1993 validation error: {str(e)}")
        return False, errors, warnings

def calculate_section_classification(section_data: Dict, material_grade: str = "A992") -> str:
    """
    Classify section for design (compact, non-compact, slender).
    
    Args:
        section_data: Section properties dictionary
        material_grade: Material grade for yield strength
        
    Returns:
        Section classification string
    """
    try:
        # Get yield strength based on grade
        fy_values = {
            "A992": 345,  # MPa
            "A36": 250,   # MPa
            "S355": 355,  # MPa
            "S235": 235   # MPa
        }
        
        fy = fy_values.get(material_grade, 345)
        E = 200000  # MPa for steel
        
        section_type = section_data.get("Type", "")
        
        if "Wide Flange" in section_type or "I-Beam" in section_type:
            bf = section_data.get("FlangeWidth", 0)
            tf = section_data.get("FlangeThickness", 0)
            tw = section_data.get("WebThickness", 0)
            d = section_data.get("Depth", 0)
            
            if bf and tf and tw and d:
                # AISC 360 classification
                lambda_f = bf / (2 * tf)  # Flange slenderness
                lambda_w = (d - 2*tf) / tw  # Web slenderness
                
                lambda_pf = 0.38 * math.sqrt(E / fy)  # Compact limit for flange
                lambda_rf = 1.0 * math.sqrt(E / fy)   # Non-compact limit for flange
                
                lambda_pw = 3.76 * math.sqrt(E / fy)  # Compact limit for web
                lambda_rw = 5.7 * math.sqrt(E / fy)   # Non-compact limit for web
                
                # Determine classification
                if lambda_f > lambda_rf or lambda_w > lambda_rw:
                    return "Slender"
                elif lambda_f > lambda_pf or lambda_w > lambda_pw:
                    return "Non-compact"
                else:
                    return "Compact"
        
        return "Unknown"
        
    except Exception:
        return "Error"

def calculate_effective_properties(section_data: Dict, classification: str) -> Dict:
    """
    Calculate effective section properties for slender sections.
    
    Args:
        section_data: Original section properties
        classification: Section classification
        
    Returns:
        Dictionary with effective properties
    """
    effective_props = section_data.copy()
    
    try:
        if classification == "Slender":
            # For slender sections, reduce effective properties
            # This is a simplified approach - actual calculation is more complex
            
            area = section_data.get("Area", 0)
            ix = section_data.get("Ix", 0)
            iy = section_data.get("Iy", 0)
            
            # Apply reduction factors (simplified)
            area_reduction = 0.85  # Typical reduction
            moment_reduction = 0.80
            
            effective_props["EffectiveArea"] = area * area_reduction
            effective_props["EffectiveIx"] = ix * moment_reduction
            effective_props["EffectiveIy"] = iy * moment_reduction
            
            # Recalculate section moduli
            if "Depth" in section_data:
                depth = section_data["Depth"]
                effective_props["EffectiveZx"] = (2 * effective_props["EffectiveIx"]) / depth
            
            if "FlangeWidth" in section_data:
                width = section_data["FlangeWidth"]
                effective_props["EffectiveZy"] = (2 * effective_props["EffectiveIy"]) / width
        
        return effective_props
        
    except Exception as e:
        # Return original properties if calculation fails
        return section_data

def get_section_design_recommendations(section_data: Dict, loading_conditions: Dict) -> List[str]:
    """
    Provide design recommendations based on section and loading.
    
    Args:
        section_data: Section properties
        loading_conditions: Applied loads and moments
        
    Returns:
        List of design recommendations
    """
    recommendations = []
    
    try:
        section_type = section_data.get("Type", "")
        weight = section_data.get("Weight", 0)
        depth = section_data.get("Depth", 0)
        
        # General recommendations
        if weight > 200:
            recommendations.append("Consider lighter alternatives for easier construction")
        
        if depth > 600:
            recommendations.append("Deep section - check lateral-torsional buckling")
            recommendations.append("Consider continuous lateral bracing")
        
        # Loading-specific recommendations
        if loading_conditions:
            max_moment = loading_conditions.get("MaxMoment", 0)
            max_shear = loading_conditions.get("MaxShear", 0)
            
            if max_moment > 0:
                # Rough capacity check (simplified)
                zx = section_data.get("Zx", 0)
                if zx > 0:
                    utilization = max_moment / (zx * 345)  # Assuming A992 steel
                    if utilization > 0.9:
                        recommendations.append("High moment utilization - consider larger section")
                    elif utilization < 0.3:
                        recommendations.append("Low moment utilization - consider smaller section")
        
        # Section-specific recommendations
        if "HSS" in section_type:
            recommendations.append("HSS sections provide excellent torsional resistance")
            recommendations.append("Consider weld access for connections")
        
        elif "Wide Flange" in section_type:
            recommendations.append("Excellent for moment-resisting frames")
            recommendations.append("Check flange compactness for plastic design")
        
        return recommendations
        
    except Exception as e:
        return [f"Error generating recommendations: {str(e)}"]

# Design optimization functions
def optimize_section_selection(design_requirements: Dict, available_sections: List[str]) -> List[Tuple[str, float]]:
    """
    Optimize section selection based on design requirements.
    
    Args:
        design_requirements: Required section properties and constraints
        available_sections: List of section names to consider
        
    Returns:
        List of (section_name, efficiency_score) tuples, sorted by efficiency
    """
    from .SectionStandards import get_section_info
    
    candidates = []
    
    try:
        required_zx = design_requirements.get("RequiredZx", 0)
        required_zy = design_requirements.get("RequiredZy", 0)
        required_area = design_requirements.get("RequiredArea", 0)
        max_weight = design_requirements.get("MaxWeight", float('inf'))
        max_depth = design_requirements.get("MaxDepth", float('inf'))
        
        for section_name in available_sections:
            section_data = get_section_info(section_name)
            if not section_data:
                continue
            
            # Check if section meets requirements
            zx = section_data.get("Zx", 0) / 1e9  # Convert to m³
            zy = section_data.get("Zy", 0) / 1e9
            area = section_data.get("Area", 0) / 1e6  # Convert to m²
            weight = section_data.get("Weight", 0)
            depth = section_data.get("Depth", 0)
            
            # Check constraints
            if weight > max_weight or depth > max_depth:
                continue
            
            if zx < required_zx or zy < required_zy or area < required_area:
                continue
            
            # Calculate efficiency score (lower weight is better)
            efficiency_score = weight / (zx + zy + area * 1e6)  # Composite efficiency
            
            candidates.append((section_name, efficiency_score))
        
        # Sort by efficiency (lower is better)
        candidates.sort(key=lambda x: x[1])
        
        return candidates[:10]  # Return top 10 candidates
        
    except Exception as e:
        return [(f"Error: {str(e)}", 0.0)]