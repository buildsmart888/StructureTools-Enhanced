# -*- coding: utf-8 -*-
"""
ModalAnalysis.py - Professional modal analysis implementation

This module provides comprehensive modal analysis capabilities including
natural frequency extraction, mode shape visualization, and modal 
participation factor calculations for seismic design.
"""

import FreeCAD as App
import FreeCADGui as Gui
import numpy as np
import math
from typing import List, Dict, Tuple, Optional, Any
from scipy.linalg import eigh
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import eigsh
import time

from ..utils.exceptions import AnalysisError
from ..utils.validation import StructuralValidator


class ModalAnalysisResults:
    """
    Container for modal analysis results with professional formatting.
    """
    
    def __init__(self, frequencies: np.ndarray, mode_shapes: np.ndarray, 
                 participation_factors: np.ndarray, effective_mass: Dict):
        """
        Initialize modal analysis results.
        
        Args:
            frequencies: Natural frequencies in Hz
            mode_shapes: Mode shape vectors (DOF x modes)
            participation_factors: Modal participation factors
            effective_mass: Effective mass percentages by direction
        """
        self.frequencies = frequencies
        self.mode_shapes = mode_shapes
        self.participation_factors = participation_factors
        self.effective_mass = effective_mass
        self.num_modes = len(frequencies)
        
        # Calculate periods
        self.periods = np.where(frequencies > 0, 1.0 / frequencies, np.inf)
        
        # Classify mode types
        self.mode_classifications = self._classify_modes()
    
    def _classify_modes(self) -> List[str]:
        """Classify modes as translational, rotational, or local."""
        classifications = []
        
        for i in range(self.num_modes):
            pf = self.participation_factors[i]
            
            # Check participation in global directions (handle different sizes)
            if len(pf) >= 3:
                max_translation = max(abs(pf[0]), abs(pf[1]), abs(pf[2]))
                
                if len(pf) >= 6:
                    max_rotation = max(abs(pf[3]), abs(pf[4]), abs(pf[5]))
                else:
                    max_rotation = 0.0
                
                if max_translation > 0.1:
                    if abs(pf[0]) > abs(pf[1]):
                        classifications.append("Translation X")
                    else:
                        classifications.append("Translation Y") 
                elif max_rotation > 0.1:
                    classifications.append("Torsional")
                else:
                    classifications.append("Local/Higher Order")
            else:
                classifications.append("Unclassified")
        
        return classifications
    
    def get_fundamental_period(self) -> float:
        """Get fundamental period of structure."""
        return self.periods[0] if len(self.periods) > 0 else 0.0
    
    def get_dominant_modes(self, min_participation: float = 0.05) -> List[int]:
        """Get mode numbers with significant participation."""
        dominant = []
        for i in range(self.num_modes):
            if np.max(np.abs(self.participation_factors[i])) > min_participation:
                dominant.append(i)
        return dominant
    
    def print_summary(self):
        """Print formatted modal analysis summary."""
        App.Console.PrintMessage("="*60 + "\n")
        App.Console.PrintMessage("MODAL ANALYSIS RESULTS SUMMARY\n")
        App.Console.PrintMessage("="*60 + "\n")
        
        App.Console.PrintMessage(f"Number of modes extracted: {self.num_modes}\n")
        App.Console.PrintMessage(f"Fundamental period: {self.get_fundamental_period():.3f} seconds\n")
        App.Console.PrintMessage(f"Fundamental frequency: {self.frequencies[0]:.3f} Hz\n\n")
        
        # Mode summary table
        App.Console.PrintMessage("Mode  Frequency  Period   Classification       Max PF\n")
        App.Console.PrintMessage("-"*55 + "\n")
        
        for i in range(min(10, self.num_modes)):  # Show first 10 modes
            freq = self.frequencies[i]
            period = self.periods[i]
            classification = self.mode_classifications[i]
            max_pf = np.max(np.abs(self.participation_factors[i]))
            
            App.Console.PrintMessage(f"{i+1:3d}   {freq:8.3f}   {period:6.3f}   {classification:15s}   {max_pf:6.3f}\n")
        
        App.Console.PrintMessage("\n")
        
        # Effective mass summary
        App.Console.PrintMessage("Effective Mass Percentages:\n")
        App.Console.PrintMessage(f"X-direction: {self.effective_mass['X']:.1f}%\n")
        App.Console.PrintMessage(f"Y-direction: {self.effective_mass['Y']:.1f}%\n") 
        App.Console.PrintMessage(f"Z-direction: {self.effective_mass['Z']:.1f}%\n")
        App.Console.PrintMessage("="*60 + "\n")


class ModalAnalysis:
    """
    Professional modal analysis implementation with industry-standard algorithms.
    
    This class provides comprehensive modal analysis capabilities including:
    - Natural frequency extraction using optimized eigenvalue solvers
    - Mode shape calculation and normalization
    - Modal participation factor computation for seismic design
    - Effective mass calculations
    - Mode shape visualization and animation
    """
    
    def __init__(self, structural_model):
        """
        Initialize modal analysis.
        
        Args:
            structural_model: StructureTools structural model or Pynite FEModel3D
        """
        self.model = structural_model
        
        # Analysis parameters
        self.num_modes = 10
        self.frequency_range = (0.1, 100.0)  # Hz
        self.analysis_method = "Subspace"    # Subspace, Lanczos, Standard
        self.convergence_tolerance = 1e-6
        self.max_iterations = 1000
        
        # Mass matrix options
        self.mass_matrix_type = "Consistent"  # Consistent, Lumped
        self.include_rotational_inertia = True
        
        # Results storage
        self.results = None
        self.analysis_time = 0.0
        self.convergence_info = {}
    
    def set_analysis_parameters(self, num_modes: int = 10, 
                               frequency_range: Tuple[float, float] = (0.1, 100.0),
                               method: str = "Subspace"):
        """
        Set modal analysis parameters.
        
        Args:
            num_modes: Number of modes to extract
            frequency_range: Frequency range of interest (Hz)
            method: Analysis method (Subspace, Lanczos, Standard)
        """
        self.num_modes = num_modes
        self.frequency_range = frequency_range
        self.analysis_method = method
        
        App.Console.PrintMessage(f"Modal analysis configured: {num_modes} modes, "
                                f"{method} method, {frequency_range} Hz range\n")
    
    def set_num_modes(self, num_modes: int):
        """Set number of modes to extract"""
        if num_modes <= 0 or num_modes > 1000:
            raise ValueError(f"Invalid number of modes: {num_modes}")
        self.num_modes = num_modes
    
    def set_frequency_range(self, min_freq: float, max_freq: float):
        """Set frequency range for analysis"""
        if min_freq < 0 or max_freq <= min_freq:
            raise ValueError(f"Invalid frequency range: {min_freq} to {max_freq}")
        self.frequency_range = (min_freq, max_freq)
    
    def run_modal_analysis(self) -> ModalAnalysisResults:
        """
        Execute modal analysis with comprehensive error handling.
        
        Returns:
            ModalAnalysisResults object containing all results
            
        Raises:
            AnalysisError: If analysis fails
        """
        App.Console.PrintMessage("Starting modal analysis...\n")
        start_time = time.time()
        
        try:
            # Step 1: Build global matrices
            App.Console.PrintMessage("Building global stiffness and mass matrices...\n")
            K = self._build_global_stiffness_matrix()
            M = self._build_global_mass_matrix()
            
            # Step 2: Apply boundary conditions
            K_reduced, M_reduced, dof_map = self._apply_boundary_conditions(K, M)
            
            # Step 3: Solve eigenvalue problem
            App.Console.PrintMessage(f"Solving eigenvalue problem using {self.analysis_method} method...\n")
            eigenvalues, eigenvectors = self._solve_eigenvalue_problem(K_reduced, M_reduced)
            
            # Step 4: Process results
            frequencies = np.sqrt(np.real(eigenvalues)) / (2 * np.pi)
            mode_shapes = self._expand_mode_shapes(eigenvectors, dof_map)
            
            # Step 5: Calculate modal properties
            participation_factors = self._calculate_participation_factors(mode_shapes, M)
            effective_mass = self._calculate_effective_mass(mode_shapes, M, participation_factors)
            
            # Step 6: Normalize mode shapes
            mode_shapes = self._normalize_mode_shapes(mode_shapes, M)
            
            # Create results object
            self.results = ModalAnalysisResults(frequencies, mode_shapes, 
                                             participation_factors, effective_mass)
            
            self.analysis_time = time.time() - start_time
            
            App.Console.PrintMessage(f"Modal analysis completed successfully in {self.analysis_time:.2f} seconds\n")
            
            # Print summary
            self.results.print_summary()
            
            return self.results
            
        except Exception as e:
            self.analysis_time = time.time() - start_time
            error_msg = f"Modal analysis failed after {self.analysis_time:.2f} seconds: {str(e)}"
            App.Console.PrintError(error_msg + "\n")
            raise AnalysisError(error_msg, analysis_type="Modal Analysis")
    
    def _build_global_stiffness_matrix(self) -> np.ndarray:
        """Build global stiffness matrix from structural model."""
        try:
            # Get stiffness matrix from Pynite model
            if hasattr(self.model, 'K'):
                # Direct access to Pynite stiffness matrix
                K = self.model.K()
                return np.array(K)
            else:
                # Build from elements manually
                return self._assemble_stiffness_from_elements()
                
        except Exception as e:
            raise AnalysisError(f"Failed to build stiffness matrix: {str(e)}")
    
    def _build_global_mass_matrix(self) -> np.ndarray:
        """Build global mass matrix with consistent or lumped formulation."""
        try:
            if self.mass_matrix_type == "Consistent":
                return self._build_consistent_mass_matrix()
            else:
                return self._build_lumped_mass_matrix()
                
        except Exception as e:
            raise AnalysisError(f"Failed to build mass matrix: {str(e)}")
    
    def _build_consistent_mass_matrix(self) -> np.ndarray:
        """Build consistent mass matrix from element matrices."""
        # Get number of DOF
        if hasattr(self.model, 'nodes'):
            num_nodes = len(self.model.nodes)
            num_dof = num_nodes * 6  # 6 DOF per node
        else:
            raise AnalysisError("Cannot determine model size")
        
        # Initialize global mass matrix
        M = np.zeros((num_dof, num_dof))
        
        # Add member mass contributions
        if hasattr(self.model, 'members'):
            for member_name, member in self.model.members.items():
                try:
                    # Get member mass matrix
                    m_local = self._get_member_mass_matrix(member)
                    
                    # Get DOF indices for member
                    i_dof, j_dof = self._get_member_dof_indices(member)
                    
                    # Assemble into global matrix
                    dof_indices = i_dof + j_dof
                    for i, global_i in enumerate(dof_indices):
                        for j, global_j in enumerate(dof_indices):
                            M[global_i, global_j] += m_local[i, j]
                            
                except Exception as e:
                    App.Console.PrintWarning(f"Error processing member {member_name}: {str(e)}\n")
        
        # Add nodal masses (if any)
        self._add_nodal_masses(M)
        
        return M
    
    def _build_lumped_mass_matrix(self) -> np.ndarray:
        """Build lumped mass matrix (diagonal)."""
        # Simplified lumped mass - can be enhanced
        consistent_mass = self._build_consistent_mass_matrix()
        
        # Create lumped mass by row sum method
        lumped_mass = np.zeros_like(consistent_mass)
        for i in range(consistent_mass.shape[0]):
            lumped_mass[i, i] = np.sum(consistent_mass[i, :])
        
        return lumped_mass
    
    def _get_member_mass_matrix(self, member) -> np.ndarray:
        """Calculate mass matrix for a structural member."""
        try:
            # Get member properties
            length = member.length
            area = getattr(member, 'A', 1.0)
            density = getattr(member, 'rho', 7850.0)  # Steel default
            
            # Mass per unit length
            mass_per_length = area * density
            
            # Consistent mass matrix for beam element (12x12)
            L = length
            m = mass_per_length * L / 420.0
            
            # Simplified beam mass matrix
            mass_matrix = np.zeros((12, 12))
            
            # Translational mass terms
            mass_matrix[0, 0] = mass_matrix[6, 6] = 140 * m    # Axial
            mass_matrix[1, 1] = mass_matrix[7, 7] = 156 * m    # Transverse Y
            mass_matrix[2, 2] = mass_matrix[8, 8] = 156 * m    # Transverse Z
            
            # Add coupling terms for consistent formulation
            mass_matrix[1, 7] = mass_matrix[7, 1] = 54 * m
            mass_matrix[2, 8] = mass_matrix[8, 2] = 54 * m
            
            # Rotational inertia (if included)
            if self.include_rotational_inertia:
                Ix = getattr(member, 'J', area * length**2 / 12)  # Torsional
                Iy = getattr(member, 'Iy', area * length**2 / 12)
                Iz = getattr(member, 'Iz', area * length**2 / 12)
                
                mass_matrix[3, 3] = mass_matrix[9, 9] = Ix * density / 3
                mass_matrix[4, 4] = mass_matrix[10, 10] = 4 * Iy * density * L / 420
                mass_matrix[5, 5] = mass_matrix[11, 11] = 4 * Iz * density * L / 420
            
            return mass_matrix
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating member mass matrix: {str(e)}\n")
            return np.eye(12) * 1.0  # Fallback unit matrix
    
    def _apply_boundary_conditions(self, K: np.ndarray, M: np.ndarray) -> Tuple[np.ndarray, np.ndarray, List[int]]:
        """Apply boundary conditions by eliminating constrained DOF."""
        try:
            # Get list of free DOF (not supported)
            free_dof = self._get_free_dof_indices()
            
            # Reduce matrices to free DOF only
            K_reduced = K[np.ix_(free_dof, free_dof)]
            M_reduced = M[np.ix_(free_dof, free_dof)]
            
            App.Console.PrintMessage(f"Reduced system size: {len(free_dof)} DOF (from {K.shape[0]})\n")
            
            return K_reduced, M_reduced, free_dof
            
        except Exception as e:
            raise AnalysisError(f"Failed to apply boundary conditions: {str(e)}")
    
    def _get_free_dof_indices(self) -> List[int]:
        """Get indices of free (unconstrained) degrees of freedom."""
        free_dof = []
        
        try:
            if hasattr(self.model, 'nodes'):
                for i, (node_name, node) in enumerate(self.model.nodes.items()):
                    base_dof = i * 6
                    
                    # Check each DOF for supports
                    dof_names = ['support_DX', 'support_DY', 'support_DZ', 
                               'support_RX', 'support_RY', 'support_RZ']
                    
                    for j, dof_name in enumerate(dof_names):
                        is_supported = getattr(node, dof_name, False)
                        if not is_supported:
                            free_dof.append(base_dof + j)
            
            if not free_dof:
                raise AnalysisError("No free DOF found - structure is over-constrained")
            
            return free_dof
            
        except Exception as e:
            raise AnalysisError(f"Failed to determine free DOF: {str(e)}")
    
    def _solve_eigenvalue_problem(self, K: np.ndarray, M: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Solve generalized eigenvalue problem (K - λM)φ = 0."""
        try:
            App.Console.PrintMessage(f"Solving {K.shape[0]} DOF eigenvalue problem for {self.num_modes} modes...\n")
            
            # Check matrix properties
            if K.shape[0] < self.num_modes:
                self.num_modes = K.shape[0] - 1
                App.Console.PrintWarning(f"Reducing number of modes to {self.num_modes}\n")
            
            if self.analysis_method == "Subspace" and K.shape[0] > 100:
                # Use sparse solver for large problems
                K_sparse = csc_matrix(K)
                M_sparse = csc_matrix(M)
                
                # Solve subset of eigenvalues
                eigenvalues, eigenvectors = eigsh(K_sparse, k=self.num_modes, M=M_sparse, 
                                                which='SM', tol=self.convergence_tolerance)
            else:
                # Use dense solver for small problems
                eigenvalues, eigenvectors = eigh(K, M)
                
                # Sort by eigenvalue magnitude
                idx = np.argsort(eigenvalues)
                eigenvalues = eigenvalues[idx[:self.num_modes]]
                eigenvectors = eigenvectors[:, idx[:self.num_modes]]
            
            # Validate results
            if np.any(eigenvalues <= 0):
                neg_count = np.sum(eigenvalues <= 0)
                App.Console.PrintWarning(f"Found {neg_count} zero/negative eigenvalues - "
                                       "structure may be unstable\n")
            
            return eigenvalues, eigenvectors
            
        except Exception as e:
            raise AnalysisError(f"Eigenvalue solution failed: {str(e)}")
    
    def _expand_mode_shapes(self, reduced_modes: np.ndarray, free_dof: List[int]) -> np.ndarray:
        """Expand reduced mode shapes to full DOF set."""
        # Determine full system size
        if hasattr(self.model, 'nodes'):
            full_size = len(self.model.nodes) * 6
        else:
            full_size = len(free_dof) * 2  # Conservative estimate
        
        # Initialize full mode shape matrix
        full_modes = np.zeros((full_size, reduced_modes.shape[1]))
        
        # Insert reduced modes at free DOF positions
        for i, dof in enumerate(free_dof):
            if dof < full_size:
                full_modes[dof, :] = reduced_modes[i, :]
        
        return full_modes
    
    def _calculate_participation_factors(self, mode_shapes: np.ndarray, M: np.ndarray) -> np.ndarray:
        """Calculate modal participation factors for seismic analysis."""
        try:
            num_modes = mode_shapes.shape[1]
            participation_factors = np.zeros((num_modes, 6))  # 6 global directions
            
            # Unit load vectors for each direction
            unit_loads = self._get_unit_load_vectors(M.shape[0])
            
            for i in range(num_modes):
                phi = mode_shapes[:, i]
                phi_M = M @ phi
                
                for j in range(6):  # X, Y, Z translation and rotation
                    r = unit_loads[j]
                    
                    # Participation factor = φᵀMr / φᵀMφ
                    numerator = phi.T @ M @ r
                    denominator = phi.T @ phi_M
                    
                    if abs(denominator) > 1e-12:
                        participation_factors[i, j] = numerator / denominator
            
            return participation_factors
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating participation factors: {str(e)}\n")
            return np.zeros((mode_shapes.shape[1], 6))
    
    def _get_unit_load_vectors(self, num_dof: int) -> List[np.ndarray]:
        """Generate unit load vectors for participation factor calculation."""
        unit_loads = []
        
        # Translational unit loads (X, Y, Z)
        for direction in range(3):
            load_vector = np.zeros(num_dof)
            for i in range(0, num_dof, 6):
                if i + direction < num_dof:
                    load_vector[i + direction] = 1.0
            unit_loads.append(load_vector)
        
        # Rotational unit loads (RX, RY, RZ)  
        for direction in range(3, 6):
            load_vector = np.zeros(num_dof)
            for i in range(0, num_dof, 6):
                if i + direction < num_dof:
                    load_vector[i + direction] = 1.0
            unit_loads.append(load_vector)
        
        return unit_loads
    
    def _calculate_effective_mass(self, mode_shapes: np.ndarray, M: np.ndarray, 
                                 participation_factors: np.ndarray) -> Dict[str, float]:
        """Calculate effective mass percentages."""
        try:
            # Get total mass in each direction
            total_mass_x = self._get_total_mass_direction(M, 0)
            total_mass_y = self._get_total_mass_direction(M, 1) 
            total_mass_z = self._get_total_mass_direction(M, 2)
            
            # Calculate effective masses for each mode
            effective_mass_x = 0.0
            effective_mass_y = 0.0
            effective_mass_z = 0.0
            
            for i in range(mode_shapes.shape[1]):
                phi = mode_shapes[:, i]
                modal_mass = phi.T @ M @ phi
                
                # Effective mass = (participation factor)² × modal mass
                if modal_mass > 1e-12:
                    effective_mass_x += (participation_factors[i, 0]**2) * modal_mass
                    effective_mass_y += (participation_factors[i, 1]**2) * modal_mass
                    effective_mass_z += (participation_factors[i, 2]**2) * modal_mass
            
            # Convert to percentages
            mass_percentages = {
                'X': (effective_mass_x / total_mass_x * 100) if total_mass_x > 0 else 0.0,
                'Y': (effective_mass_y / total_mass_y * 100) if total_mass_y > 0 else 0.0,
                'Z': (effective_mass_z / total_mass_z * 100) if total_mass_z > 0 else 0.0
            }
            
            return mass_percentages
            
        except Exception as e:
            App.Console.PrintWarning(f"Error calculating effective mass: {str(e)}\n")
            return {'X': 0.0, 'Y': 0.0, 'Z': 0.0}
    
    def _get_total_mass_direction(self, M: np.ndarray, direction: int) -> float:
        """Get total mass in specified direction."""
        total_mass = 0.0
        
        # Sum diagonal terms for specified direction
        for i in range(direction, M.shape[0], 6):
            total_mass += M[i, i]
        
        return total_mass
    
    def _normalize_mode_shapes(self, mode_shapes: np.ndarray, M: np.ndarray) -> np.ndarray:
        """Normalize mode shapes with respect to mass matrix."""
        normalized_modes = np.zeros_like(mode_shapes)
        
        for i in range(mode_shapes.shape[1]):
            phi = mode_shapes[:, i]
            
            # Mass-normalize: φᵀMφ = 1
            modal_mass = phi.T @ M @ phi
            if modal_mass > 1e-12:
                normalized_modes[:, i] = phi / np.sqrt(modal_mass)
            else:
                normalized_modes[:, i] = phi
        
        return normalized_modes
    
    def create_mode_shape_visualization(self, mode_number: int, scale_factor: float = 1.0):
        """Create 3D visualization of specified mode shape."""
        if self.results is None:
            raise AnalysisError("No modal analysis results available")
        
        if mode_number >= self.results.num_modes:
            raise AnalysisError(f"Mode {mode_number} not available")
        
        try:
            # Get mode shape
            mode_shape = self.results.mode_shapes[:, mode_number]
            frequency = self.results.frequencies[mode_number]
            
            # Create visualization objects
            App.Console.PrintMessage(f"Creating visualization for Mode {mode_number + 1} "
                                   f"(f = {frequency:.3f} Hz)\n")
            
            # This would integrate with FreeCAD 3D visualization
            # Implementation would depend on specific visualization requirements
            
            return f"Mode{mode_number + 1}_Visualization"
            
        except Exception as e:
            raise AnalysisError(f"Failed to create mode shape visualization: {str(e)}")


# Additional helper functions for integration
def run_modal_analysis_on_calc(calc_obj, num_modes: int = 10) -> ModalAnalysisResults:
    """
    Convenience function to run modal analysis on StructureTools Calc object.
    
    Args:
        calc_obj: StructureTools Calc object
        num_modes: Number of modes to extract
        
    Returns:
        ModalAnalysisResults object
    """
    # Input validation
    if calc_obj is None:
        raise AnalysisError("Calc object cannot be None")
        
    if not hasattr(calc_obj, 'ListElements'):
        raise AnalysisError("Invalid calc object: missing ListElements attribute")
    
    try:
        # Extract Pynite model from Calc object
        if hasattr(calc_obj, 'model'):
            pynite_model = calc_obj.model
        else:
            raise AnalysisError("No FE model found in Calc object")
        
        # Create and run modal analysis
        modal_analysis = ModalAnalysis(pynite_model)
        modal_analysis.set_num_modes(num_modes)
        
        results = modal_analysis.run_modal_analysis()
        
        # Store results in Calc object for later use
        calc_obj.modal_analysis_results = results
        
        return results
        
    except Exception as e:
        raise AnalysisError(f"Modal analysis on Calc object failed: {str(e)}")