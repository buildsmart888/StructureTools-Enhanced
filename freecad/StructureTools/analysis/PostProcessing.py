# -*- coding: utf-8 -*-
"""
PostProcessing - Results processing and stress calculation for shell elements

Calculates:
- Membrane stresses (Nx, Ny, Nxy)
- Bending stresses (Mx, My, Mxy)
- Transverse shear stresses (Qx, Qy)
- Principal stresses
- Von Mises equivalent stress
- Safety factors
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass


@dataclass
class StressResult:
    """Container for stress results at a point."""
    location: str  # "top", "middle", "bottom"
    sigma_x: float
    sigma_y: float
    sigma_z: float
    tau_xy: float
    tau_yz: float
    tau_zx: float
    
    @property
    def principal_stresses(self) -> Tuple[float, float, float]:
        """Calculate principal stresses."""
        # For plane stress (in-plane): sigma_z = 0
        stress_matrix = np.array([
            [self.sigma_x, self.tau_xy, 0],
            [self.tau_xy, self.sigma_y, 0],
            [0, 0, 0]
        ])
        
        eigenvalues = np.linalg.eigvalsh(stress_matrix)
        return tuple(sorted(eigenvalues, reverse=True))
    
    @property
    def von_mises(self) -> float:
        """Calculate Von Mises equivalent stress."""
        s1, s2, s3 = self.principal_stresses
        vm = np.sqrt(0.5 * ((s1 - s2)**2 + (s2 - s3)**2 + (s3 - s1)**2))
        return vm


class StressCalculator:
    """Calculate stresses from element forces and displacements."""
    
    def __init__(self, E: float = 210000, nu: float = 0.3, t: float = 10):
        """
        Initialize stress calculator.
        
        Args:
            E: Young's modulus (MPa)
            nu: Poisson's ratio
            t: Thickness (mm)
        """
        self.E = E
        self.nu = nu
        self.t = t
        
        # Membrane and bending stiffness
        self.D_mem = self.E * self.t / (1 - self.nu**2)
        self.D_bend = self.E * self.t**3 / (12 * (1 - self.nu**2))
    
    def calculate_membrane_stresses(self, 
                                    strains: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate membrane stresses from strains.
        
        Args:
            strains: {'ex': ..., 'ey': ..., 'exy': ...}
            
        Returns:
            Stresses: {'nx': ..., 'ny': ..., 'nxy': ...}
        """
        ex = strains.get('ex', 0)
        ey = strains.get('ey', 0)
        exy = strains.get('exy', 0)
        
        # Membrane stress-strain relationship
        # σ = D * ε (plane stress)
        C = self.E / (1 - self.nu**2) * np.array([
            [1, self.nu, 0],
            [self.nu, 1, 0],
            [0, 0, (1 - self.nu) / 2]
        ])
        
        strain_vector = np.array([ex, ey, exy])
        stress_vector = C @ strain_vector
        
        return {
            'sigma_x': stress_vector[0],
            'sigma_y': stress_vector[1],
            'tau_xy': stress_vector[2],
            'N_x': stress_vector[0] * self.t,  # Force per unit width
            'N_y': stress_vector[1] * self.t,
            'N_xy': stress_vector[2] * self.t
        }
    
    def calculate_bending_stresses(self,
                                   curvatures: Dict[str, float],
                                   z: float = None) -> Dict[str, float]:
        """
        Calculate bending stresses from curvatures.
        
        Args:
            curvatures: {'kappa_x': ..., 'kappa_y': ..., 'kappa_xy': ...}
            z: Height from neutral axis (if None, use top surface)
            
        Returns:
            Bending stresses
        """
        if z is None:
            z = self.t / 2  # Top surface
        
        kx = curvatures.get('kappa_x', 0)
        ky = curvatures.get('kappa_y', 0)
        
        # Bending moment
        M_x = self.D_bend * (kx + self.nu * ky)
        M_y = self.D_bend * (ky + self.nu * kx)
        
        # Bending stress: σ = M * z / I
        # For plate: I = t^3/12
        I = self.t**3 / 12
        
        sigma_x_bend = M_x * z / I
        sigma_y_bend = M_y * z / I
        
        return {
            'M_x': M_x,
            'M_y': M_y,
            'sigma_x_bending': sigma_x_bend,
            'sigma_y_bending': sigma_y_bend,
            'bending_stress_top': max(abs(sigma_x_bend), abs(sigma_y_bend)),
            'bending_stress_bottom': -max(abs(sigma_x_bend), abs(sigma_y_bend))
        }
    
    def calculate_shear_stresses(self, 
                                 shear_forces: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate transverse shear stresses.
        
        Args:
            shear_forces: {'Q_x': ..., 'Q_y': ...}
            
        Returns:
            Shear stresses
        """
        Qx = shear_forces.get('Q_x', 0)
        Qy = shear_forces.get('Q_y', 0)
        
        # Average shear stress: τ = V / A = Q / t
        tau_x = 1.5 * Qx / self.t  # 1.5 for rectangular section
        tau_y = 1.5 * Qy / self.t
        
        return {
            'tau_xz': tau_x,
            'tau_yz': tau_y,
            'max_shear': np.sqrt(tau_x**2 + tau_y**2)
        }
    
    def calculate_principal_stresses(self, 
                                     sigma_x: float, sigma_y: float, 
                                     tau_xy: float) -> Tuple[float, float, float]:
        """
        Calculate principal stresses for 2D stress state.
        
        Args:
            sigma_x, sigma_y: Normal stresses
            tau_xy: Shear stress
            
        Returns:
            (sigma_1, sigma_2, max_shear_stress)
        """
        # Average stress
        sigma_avg = (sigma_x + sigma_y) / 2
        
        # Radius of Mohr circle
        R = np.sqrt(((sigma_x - sigma_y) / 2)**2 + tau_xy**2)
        
        # Principal stresses
        sigma_1 = sigma_avg + R
        sigma_2 = sigma_avg - R
        
        # Maximum shear stress
        tau_max = R
        
        return sigma_1, sigma_2, tau_max
    
    def calculate_von_mises(self, sigma_x: float, sigma_y: float, 
                           tau_xy: float) -> float:
        """
        Calculate Von Mises equivalent stress.
        
        For 2D: σ_vm = √(σ_x² - σ_x*σ_y + σ_y² + 3*τ_xy²)
        
        Args:
            sigma_x, sigma_y, tau_xy: Stress components
            
        Returns:
            Von Mises stress
        """
        sigma_vm = np.sqrt(sigma_x**2 - sigma_x * sigma_y + sigma_y**2 + 
                          3 * tau_xy**2)
        return sigma_vm


class ElementResultsProcessor:
    """Process results for a shell element."""
    
    def __init__(self, element_id: int, element_type: str,
                 E: float = 210000, nu: float = 0.3, t: float = 10):
        """
        Initialize element results processor.
        
        Args:
            element_id: Element identifier
            element_type: "Quad4", "Tri3", or "Tri6"
            E, nu, t: Material properties
        """
        self.element_id = element_id
        self.element_type = element_type
        self.E = E
        self.nu = nu
        self.t = t
        
        self.stress_calc = StressCalculator(E, nu, t)
        self.results = {
            'membrane': {},
            'bending': {},
            'shear': {},
            'combined': {}
        }
    
    def process_element_displacements(self, 
                                     displacements: np.ndarray,
                                     node_coords: np.ndarray) -> Dict[str, Any]:
        """
        Process element displacements and calculate strains.
        
        Args:
            displacements: 6*n_nodes displacement vector
            node_coords: Node coordinates (n x 3)
            
        Returns:
            Strains at element center
        """
        # Simplified strain calculation
        # In a real implementation, would use element shape functions
        
        # Get translations (first 3 DOFs of each node)
        n_nodes = len(node_coords)
        translations = np.zeros((n_nodes, 3))
        
        for i in range(n_nodes):
            translations[i] = displacements[i*6:(i*6+3)]
        
        # Average strains at center (simplified)
        strains = {
            'ex': 0.0,
            'ey': 0.0,
            'exy': 0.0,
            'kappa_x': 0.0,
            'kappa_y': 0.0
        }
        
        return strains
    
    def calculate_element_stresses(self, 
                                   displacements: np.ndarray,
                                   node_coords: np.ndarray) -> Dict[str, Any]:
        """
        Calculate stresses for element.
        
        Args:
            displacements: Element displacement vector
            node_coords: Node coordinates
            
        Returns:
            Stress results dictionary
        """
        # Process displacements
        strains = self.process_element_displacements(displacements, node_coords)
        
        # Calculatete membrane stresses
        membrane = self.stress_calc.calculate_membrane_stresses(strains)
        
        # Calculatete bending stresses
        bending_top = self.stress_calc.calculate_bending_stresses(
            {'kappa_x': strains['kappa_x'], 'kappa_y': strains['kappa_y']},
            z=self.t/2
        )
        bending_bot = self.stress_calc.calculate_bending_stresses(
            {'kappa_x': strains['kappa_x'], 'kappa_y': strains['kappa_y']},
            z=-self.t/2
        )
        
        # Combined stresses
        combined_top = {
            'sigma_x': membrane['sigma_x'] + bending_top['sigma_x_bending'],
            'sigma_y': membrane['sigma_y'] + bending_top['sigma_y_bending'],
            'tau_xy': membrane['tau_xy']
        }
        
        combined_bot = {
            'sigma_x': membrane['sigma_x'] + bending_bot['sigma_x_bending'],
            'sigma_y': membrane['sigma_y'] + bending_bot['sigma_y_bending'],
            'tau_xy': membrane['tau_xy']
        }
        
        # Von Mises at critical points
        vm_top = self.stress_calc.calculate_von_mises(
            combined_top['sigma_x'], combined_top['sigma_y'], combined_top['tau_xy']
        )
        vm_bot = self.stress_calc.calculate_von_mises(
            combined_bot['sigma_x'], combined_bot['sigma_y'], combined_bot['tau_xy']
        )
        
        self.results = {
            'membrane': membrane,
            'bending_top': bending_top,
            'bending_bottom': bending_bot,
            'combined_top': combined_top,
            'combined_bottom': combined_bot,
            'von_mises_top': vm_top,
            'von_mises_bottom': vm_bot,
            'max_von_mises': max(vm_top, vm_bot)
        }
        
        return self.results


class StructuralAnalysisResults:
    """Container for overall structural analysis results."""
    
    def __init__(self):
        """Initialize results container."""
        self.node_displacements = {}  # {node_id: displacement_vector}
        self.node_reactions = {}       # {node_id: reaction_vector}
        self.element_results = {}      # {elem_id: element_results}
        self.load_cases = {}
        
        self.global_max_displacement = 0.0
        self.global_max_stress = 0.0
        self.critical_element = None
    
    def add_element_results(self, elem_id: int, results: Dict) -> None:
        """Add element results."""
        self.element_results[elem_id] = results
        
        # Update global max stress
        if 'max_von_mises' in results:
            if results['max_von_mises'] > self.global_max_stress:
                self.global_max_stress = results['max_von_mises']
                self.critical_element = elem_id
    
    def calculate_deflection_ratio(self, span: float) -> float:
        """
        Calculate deflection ratio (span/deflection).
        
        Args:
            span: Span length
            
        Returns:
            Span to deflection ratio
        """
        if self.global_max_displacement > 0:
            return span / self.global_max_displacement
        return float('inf')
    
    def check_serviceability(self, span: float, 
                            ratio_limit: float = 240) -> Dict[str, Any]:
        """
        Check serviceability limit state.
        
        Args:
            span: Span length
            ratio_limit: Maximum allowed span/deflection ratio
            
        Returns:
            Check result
        """
        actual_ratio = self.calculate_deflection_ratio(span)
        
        return {
            'span': span,
            'max_deflection': self.global_max_displacement,
            'required_ratio': ratio_limit,
            'actual_ratio': actual_ratio,
            'check': actual_ratio >= ratio_limit,
            'status': 'OK' if actual_ratio >= ratio_limit else 'FAIL'
        }
    
    def check_strength(self, material_yield: float = 250, 
                      safety_factor: float = 1.5) -> Dict[str, Any]:
        """
        Check strength limit state.
        
        Args:
            material_yield: Material yield stress (MPa)
            safety_factor: Design safety factor
            
        Returns:
            Check result
        """
        allowable_stress = material_yield / safety_factor
        
        return {
            'yield_stress': material_yield,
            'safety_factor': safety_factor,
            'allowable_stress': allowable_stress,
            'max_stress': self.global_max_stress,
            'critical_element': self.critical_element,
            'check': self.global_max_stress <= allowable_stress,
            'stress_ratio': self.global_max_stress / allowable_stress,
            'status': 'OK' if self.global_max_stress <= allowable_stress else 'FAIL'
        }
    
    def get_summary(self) -> Dict[str, Any]:
        """Get results summary."""
        return {
            'num_elements': len(self.element_results),
            'num_nodes': len(self.node_displacements),
            'max_displacement': self.global_max_displacement,
            'max_stress': self.global_max_stress,
            'critical_element': self.critical_element,
            'num_load_cases': len(self.load_cases)
        }
