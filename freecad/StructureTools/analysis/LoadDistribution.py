# -*- coding: utf-8 -*-
"""
LoadDistribution - Load distribution and conversion for plate/shell elements

Supports:
- Pressure to nodal load conversion
- Non-uniform load patterns
- Load combinations
- Thermal loads
- Thai units integration
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from enum import Enum


class LoadPattern(Enum):
    """Load distribution patterns."""
    UNIFORM = "uniform"
    LINEAR_X = "linear_x"
    LINEAR_Y = "linear_y"
    BILINEAR = "bilinear"
    RADIAL = "radial"
    CUSTOM = "custom"


class LoadDistributor:
    """Distribute loads across element nodes."""
    
    def __init__(self):
        """Initialize load distributor."""
        self.load_patterns = {}
    
    @staticmethod
    def uniform_load(pressure: float, area: float, 
                    num_nodes: int) -> List[float]:
        """
        Distribute uniform pressure to nodes.
        
        Args:
            pressure: Pressure value (Pa or kN/m²)
            area: Element area
            num_nodes: Number of nodes
            
        Returns:
            Nodal loads [F1, F2, ...]
        """
        total_force = pressure * area
        nodal_force = total_force / num_nodes
        return [nodal_force] * num_nodes
    
    @staticmethod
    def linear_x_load(p_min: float, p_max: float, area: float,
                     node_coords: np.ndarray) -> np.ndarray:
        """
        Distribute linearly varying load in X direction.
        
        Pressure varies linearly from p_min to p_max in X direction.
        
        Args:
            p_min: Pressure at x_min
            p_max: Pressure at x_max
            area: Element area
            node_coords: Node coordinates (n x 3)
            
        Returns:
            Nodal loads
        """
        n_nodes = len(node_coords)
        x_coords = node_coords[:, 0]
        x_min = np.min(x_coords)
        x_max = np.max(x_coords)
        
        # Pressure at each node
        pressures = []
        for x in x_coords:
            if x_max > x_min:
                p = p_min + (p_max - p_min) * (x - x_min) / (x_max - x_min)
            else:
                p = (p_min + p_max) / 2
            pressures.append(p)
        
        # Convert to nodal forces (simplified - should use proper integration)
        # For triangular/quad elements, can compute analytically
        avg_pressure = np.mean(pressures)
        total_force = avg_pressure * area
        nodal_loads = np.array(pressures) / np.sum(pressures) * total_force
        
        return nodal_loads
    
    @staticmethod
    def linear_y_load(p_min: float, p_max: float, area: float,
                     node_coords: np.ndarray) -> np.ndarray:
        """
        Distribute linearly varying load in Y direction.
        
        Args:
            p_min: Pressure at y_min
            p_max: Pressure at y_max
            area: Element area
            node_coords: Node coordinates (n x 3)
            
        Returns:
            Nodal loads
        """
        n_nodes = len(node_coords)
        y_coords = node_coords[:, 1]
        y_min = np.min(y_coords)
        y_max = np.max(y_coords)
        
        pressures = []
        for y in y_coords:
            if y_max > y_min:
                p = p_min + (p_max - p_min) * (y - y_min) / (y_max - y_min)
            else:
                p = (p_min + p_max) / 2
            pressures.append(p)
        
        avg_pressure = np.mean(pressures)
        total_force = avg_pressure * area
        nodal_loads = np.array(pressures) / np.sum(pressures) * total_force
        
        return nodal_loads
    
    @staticmethod
    def bilinear_load(p_corners: List[float], area: float,
                     node_coords: np.ndarray) -> np.ndarray:
        """
        Distribute bilinear load pattern.
        
        Pressure varies linearly in both X and Y directions.
        
        Args:
            p_corners: Pressures at 4 corners [p00, p10, p11, p01]
            area: Element area
            node_coords: Node coordinates (n x 3)
            
        Returns:
            Nodal loads
        """
        x_coords = node_coords[:, 0]
        y_coords = node_coords[:, 1]
        
        x_min, x_max = np.min(x_coords), np.max(x_coords)
        y_min, y_max = np.min(y_coords), np.max(y_coords)
        
        pressures = []
        for x, y in zip(x_coords, y_coords):
            # Bilinear interpolation
            xi = (x - x_min) / (x_max - x_min) if x_max > x_min else 0.5
            eta = (y - y_min) / (y_max - y_min) if y_max > y_min else 0.5
            
            # Shape functions at node
            N00 = (1 - xi) * (1 - eta)
            N10 = xi * (1 - eta)
            N11 = xi * eta
            N01 = (1 - xi) * eta
            
            p = (N00 * p_corners[0] + N10 * p_corners[1] + 
                 N11 * p_corners[2] + N01 * p_corners[3])
            pressures.append(p)
        
        avg_pressure = np.mean(pressures)
        total_force = avg_pressure * area
        nodal_loads = np.array(pressures) / np.sum(pressures) * total_force
        
        return nodal_loads
    
    @staticmethod
    def radial_load(pressure: float, center: np.ndarray, area: float,
                   node_coords: np.ndarray) -> np.ndarray:
        """
        Distribute radially varying load from center point.
        
        Args:
            pressure: Pressure at center
            center: Center point coordinate
            area: Element area
            node_coords: Node coordinates (n x 3)
            
        Returns:
            Nodal loads
        """
        distances = np.linalg.norm(node_coords[:, :2] - center[:2], axis=1)
        max_dist = np.max(distances)
        
        # Pressure decreases with distance
        pressures = pressure * (1 - distances / (max_dist + 1e-10))
        
        avg_pressure = np.mean(pressures)
        total_force = avg_pressure * area
        nodal_loads = np.array(pressures) / np.sum(pressures) * total_force
        
        return nodal_loads


class ThermalLoadCalculator:
    """Calculate thermal stresses and strains."""
    
    def __init__(self, alpha: float = 1e-5, E: float = 210000, 
                 nu: float = 0.3, t: float = 10):
        """
        Initialize thermal load calculator.
        
        Args:
            alpha: Thermal expansion coefficient (1/°C)
            E: Young's modulus (MPa)
            nu: Poisson's ratio
            t: Thickness (mm)
        """
        self.alpha = alpha
        self.E = E
        self.nu = nu
        self.t = t
    
    def uniform_temperature_change(self, delta_T: float, 
                                   area: float) -> Dict[str, float]:
        """
        Calculate thermal stress from uniform temperature change.
        
        Args:
            delta_T: Temperature change (°C)
            area: Element area
            
        Returns:
            Dictionary with thermal stress components
        """
        # Thermal strain
        thermal_strain = self.alpha * delta_T
        
        # Thermal stress (in membrane)
        sigma_thermal = self.E * thermal_strain / (1 - self.nu)
        
        # Thermal force
        N_thermal = sigma_thermal * self.t
        
        return {
            'thermal_strain': thermal_strain,
            'thermal_stress': sigma_thermal,
            'thermal_force_per_width': N_thermal,
            'total_thermal_force': N_thermal * area
        }
    
    def temperature_gradient(self, delta_T: float) -> Dict[str, float]:
        """
        Calculate thermal bending from temperature gradient.
        
        Args:
            delta_T: Temperature difference between top and bottom (°C)
            
        Returns:
            Dictionary with bending moment and curvature
        """
        # Curvature due to temperature gradient
        kappa = 12 * self.alpha * delta_T / self.t
        
        # Bending moment
        D = self.E * self.t**3 / (12 * (1 - self.nu**2))
        M_thermal = D * kappa
        
        return {
            'curvature': kappa,
            'bending_moment': M_thermal,
            'max_stress': 6 * M_thermal / self.t**2
        }


class LoadCombination:
    """Manage load combinations for design."""
    
    def __init__(self):
        """Initialize load combination manager."""
        self.load_cases = {}  # {case_id: {'loads': [], 'factor': 1.0}}
        self.combinations = {}  # {combo_id: {case_id: factor}}
    
    def add_load_case(self, case_id: str, description: str = "") -> None:
        """Add load case."""
        self.load_cases[case_id] = {
            'description': description,
            'loads': []
        }
    
    def add_load_to_case(self, case_id: str, node_id: int, 
                        dof: int, value: float) -> None:
        """Add load to load case."""
        if case_id not in self.load_cases:
            self.add_load_case(case_id)
        
        self.load_cases[case_id]['loads'].append({
            'node_id': node_id,
            'dof': dof,
            'value': value
        })
    
    def add_combination(self, combo_id: str, factors: Dict[str, float]) -> None:
        """
        Add load combination.
        
        Args:
            combo_id: Combination identifier
            factors: {case_id: factor}
        """
        self.combinations[combo_id] = factors
    
    def get_combined_loads(self, combo_id: str) -> Dict[Tuple[int, int], float]:
        """
        Get combined loads for a combination.
        
        Args:
            combo_id: Combination ID
            
        Returns:
            Dictionary {(node_id, dof): combined_load}
        """
        if combo_id not in self.combinations:
            raise ValueError(f"Combination {combo_id} not found")
        
        combined = {}
        factors = self.combinations[combo_id]
        
        for case_id, factor in factors.items():
            if case_id not in self.load_cases:
                continue
            
            for load in self.load_cases[case_id]['loads']:
                key = (load['node_id'], load['dof'])
                combined[key] = combined.get(key, 0) + factor * load['value']
        
        return combined
    
    def get_aci_317_combination(self, dl_factor: float = 1.2, 
                               ll_factor: float = 1.6) -> Dict[str, float]:
        """
        Get ACI 317 load combination factors.
        
        Returns:
            Dictionary with combination factors
        """
        return {
            '1.2*DL + 1.6*LL': {'DL': dl_factor, 'LL': ll_factor},
            '1.2*DL + 1.0*LL': {'DL': 1.2, 'LL': 1.0},
            '0.9*DL': {'DL': 0.9}
        }
    
    def get_lrfd_combination(self) -> Dict[str, float]:
        """Get LRFD load combination factors."""
        return {
            '1.4*DL': {'DL': 1.4},
            '1.2*DL + 1.6*LL': {'DL': 1.2, 'LL': 1.6},
            '1.2*DL + 1.0*LL + 1.6*W': {'DL': 1.2, 'LL': 1.0, 'W': 1.6},
            '1.2*DL + 0.5*LL + 1.6*W': {'DL': 1.2, 'LL': 0.5, 'W': 1.6}
        }


class ThaiLoadCombination:
    """Thai Ministry of Interior load combinations (B.E. 2566)."""
    
    @staticmethod
    def get_thai_combinations() -> Dict[str, Dict[str, float]]:
        """
        Get Thai standard load combinations.
        
        Returns:
            Dictionary with combination definitions
        """
        return {
            '1.4*DL': {'DL': 1.4},
            '1.2*DL + 1.6*LL': {'DL': 1.2, 'LL': 1.6},
            '1.2*DL + 1.0*LL + 1.6*W': {'DL': 1.2, 'LL': 1.0, 'W': 1.6},
            '1.2*DL + 1.0*LL + 0.8*W': {'DL': 1.2, 'LL': 1.0, 'W': 0.8},
            '0.9*DL + 1.6*W': {'DL': 0.9, 'W': 1.6},
            '1.2*DL + 1.0*LL + 1.0*E': {'DL': 1.2, 'LL': 1.0, 'E': 1.0},
            '0.9*DL + 1.0*E': {'DL': 0.9, 'E': 1.0}
        }
    
    @staticmethod
    def get_live_load_factors() -> Dict[str, float]:
        """Get Thai live load factors by occupancy."""
        return {
            'residential': 1.5,
            'office': 2.5,
            'commercial': 4.0,
            'warehouse': 5.0,
            'storage': 7.5,
            'roof_general': 1.0,
            'roof_assembly': 1.5
        }
