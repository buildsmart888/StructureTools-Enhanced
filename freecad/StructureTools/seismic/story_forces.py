"""
Story Forces Distribution Implementation for Static Seismic Analysis

This module contains functions to distribute seismic forces to building stories
according to various distribution methods (ASCE 7-22, linear, uniform, custom).
"""

import math
from typing import List, Tuple, Dict, Optional, Union


def calculate_seismic_coefficient(sds: float, sd1: float, period: float, 
                                 r_factor: float, importance_factor: float) -> float:
    """
    Calculate the seismic response coefficient (Cs) according to ASCE 7-22.
    
    Args:
        sds: Design spectral response acceleration parameter at short periods
        sd1: Design spectral response acceleration parameter at 1-second period
        period: Fundamental period of the structure
        r_factor: Response modification factor
        importance_factor: Importance factor
        
    Returns:
        Seismic response coefficient Cs
    """
    # Calculate Cs according to ASCE 7-22 Equation 12.8-2
    cs_max = sds / (r_factor / importance_factor)
    
    # Calculate Cs according to ASCE 7-22 Equation 12.8-3
    cs_period = sd1 / (period * (r_factor / importance_factor))
    
    # Take the minimum of the two values
    cs = min(cs_max, cs_period)
    
    # Apply minimum values according to ASCE 7-22 Section 12.8.1.1
    cs_min = max(0.044 * sds * importance_factor, 0.01)
    
    # Return the final value
    return max(cs, cs_min)


def calculate_base_shear(total_weight: float, cs: float) -> float:
    """
    Calculate the seismic base shear.
    
    Args:
        total_weight: Total effective seismic weight of the structure (kN)
        cs: Seismic response coefficient
        
    Returns:
        Base shear force (kN)
    """
    return total_weight * cs


def distribute_forces_asce(base_shear: float, story_heights: List[float], 
                          story_weights: List[float], period: float) -> List[float]:
    """
    Distribute the base shear to stories according to ASCE 7-22 method.
    
    Args:
        base_shear: Base shear force (kN)
        story_heights: List of story heights from ground (m)
        story_weights: List of story weights (kN)
        period: Fundamental period of the structure (sec)
        
    Returns:
        List of story forces (kN)
    """
    n_stories = len(story_heights)
    forces = [0.0] * n_stories
    
    # Calculate k factor based on period (ASCE 7-22 Section 12.8.3)
    if period <= 0.5:
        k = 1.0
    elif period >= 2.5:
        k = 2.0
    else:
        k = 1.0 + 0.5 * (period - 0.5) / 2.0
    
    # Calculate story weights times height to the power of k
    weight_height_k = [w * (h ** k) for w, h in zip(story_weights, story_heights)]
    sum_weight_height_k = sum(weight_height_k)
    
    # Calculate forces
    if sum_weight_height_k > 0:
        for i in range(n_stories):
            forces[i] = base_shear * weight_height_k[i] / sum_weight_height_k
    
    return forces


def distribute_forces_linear(base_shear: float, story_heights: List[float]) -> List[float]:
    """
    Distribute the base shear to stories linearly with height.
    
    Args:
        base_shear: Base shear force (kN)
        story_heights: List of story heights from ground (m)
        
    Returns:
        List of story forces (kN)
    """
    n_stories = len(story_heights)
    forces = [0.0] * n_stories
    
    # Calculate sum of heights
    sum_heights = sum(story_heights)
    
    # Calculate forces
    if sum_heights > 0:
        for i in range(n_stories):
            forces[i] = base_shear * story_heights[i] / sum_heights
    
    return forces


def distribute_forces_uniform(base_shear: float, n_stories: int) -> List[float]:
    """
    Distribute the base shear uniformly to all stories.
    
    Args:
        base_shear: Base shear force (kN)
        n_stories: Number of stories
        
    Returns:
        List of story forces (kN)
    """
    force_per_story = base_shear / n_stories
    return [force_per_story] * n_stories


def calculate_vertical_component(base_shear: float, sds: float, 
                                factor: Optional[float] = None) -> float:
    """
    Calculate the vertical seismic force component.
    
    Args:
        base_shear: Base shear force (kN)
        sds: Design spectral response acceleration parameter at short periods
        factor: Custom factor (if None, will use 0.2*SDS per ASCE 7-22)
        
    Returns:
        Vertical seismic force (kN)
    """
    if factor is not None:
        vertical_factor = factor
    else:
        # ASCE 7-22 method
        vertical_factor = 0.2 * sds
    
    return base_shear * vertical_factor


def calculate_story_percentages(forces: List[float]) -> List[float]:
    """
    Calculate the percentage of the total force for each story.
    
    Args:
        forces: List of story forces (kN)
        
    Returns:
        List of percentages (0-100)
    """
    total_force = sum(forces)
    if total_force > 0:
        return [100.0 * f / total_force for f in forces]
    else:
        return [0.0] * len(forces)


def create_story_data_table(story_forces: List[float], story_heights: List[float], 
                           story_weights: List[float]) -> List[Dict[str, Union[int, float, str]]]:
    """
    Create a list of dictionaries containing story data for tabular display.
    
    Args:
        story_forces: List of story forces (kN)
        story_heights: List of story heights from ground (m)
        story_weights: List of story weights (kN)
        
    Returns:
        List of dictionaries with story data
    """
    n_stories = len(story_forces)
    percentages = calculate_story_percentages(story_forces)
    
    table_data = []
    for i in range(n_stories):
        story_num = n_stories - i
        row = {
            'story': story_num,
            'height': story_heights[i],
            'weight': story_weights[i],
            'force': story_forces[i],
            'percentage': percentages[i]
        }
        table_data.append(row)
    
    return table_data


def format_story_data_for_plot(story_forces: List[float], 
                              story_heights: List[float]) -> Tuple[List[float], List[float]]:
    """
    Format the story data for plotting.
    
    Args:
        story_forces: List of story forces (kN)
        story_heights: List of story heights from ground (m)
        
    Returns:
        Tuple of (forces, heights) for plotting
    """
    # Return copies to avoid modifying the original data
    return story_forces.copy(), story_heights.copy()


# Example usage
if __name__ == "__main__":
    # Example building data
    building_height = 30.0  # m
    n_stories = 10
    story_height = building_height / n_stories
    story_heights = [story_height * (i + 1) for i in range(n_stories)]
    total_weight = 50000.0  # kN
    story_weights = [total_weight / n_stories] * n_stories
    
    # Seismic parameters
    sds = 1.0
    sd1 = 0.4
    period = 0.85
    r_factor = 8.0
    importance_factor = 1.0
    
    # Calculations
    cs = calculate_seismic_coefficient(sds, sd1, period, r_factor, importance_factor)
    base_shear = calculate_base_shear(total_weight, cs)
    
    # Distribution methods
    forces_asce = distribute_forces_asce(base_shear, story_heights, story_weights, period)
    forces_linear = distribute_forces_linear(base_shear, story_heights)
    forces_uniform = distribute_forces_uniform(base_shear, n_stories)
    
    # Vertical component
    vertical_force = calculate_vertical_component(base_shear, sds)
    
    # Print results
    print(f"Building height: {building_height} m")
    print(f"Number of stories: {n_stories}")
    print(f"Total weight: {total_weight} kN")
    print(f"Period: {period} sec")
    print(f"Cs: {cs:.4f}")
    print(f"Base shear: {base_shear:.1f} kN")
    print(f"Vertical force: {vertical_force:.1f} kN")
    print("\nStory Forces (ASCE 7-22 Distribution):")
    for i, force in enumerate(forces_asce):
        print(f"Story {n_stories - i}: {force:.1f} kN")