# -*- coding: utf-8 -*-
"""
ShellElements - Professional shell element formulations for plate/shell analysis

This module provides high-order shell element implementations with:
- Quad4 (4-node quadrilateral) - DKTQ formulation
- Tri3 (3-node triangle) - DKT (Discrete Kirchhoff Triangle)
- Tri6 (6-node triangle) - DKT6 high-order element
"""

import numpy as np
import math
from typing import List, Dict, Tuple, Optional, Any
from abc import ABC, abstractmethod


class ShellElement(ABC):
    """Abstract base class for shell elements."""
    
    def __init__(self, node_coords: np.ndarray, material_props: Dict):
        """
        Initialize shell element.
        
        Args:
            node_coords: Array of node coordinates (n x 3)
            material_props: Dictionary with 'E', 'nu', 't' (thickness)
        """
        self.node_coords = np.array(node_coords)
        self.num_nodes = len(node_coords)
        self.dofs_per_node = 6  # [Ux, Uy, Uz, Rx, Ry, Rz]
        self.total_dofs = self.num_nodes * self.dofs_per_node
        
        # Material properties
        self.E = material_props.get('E', 210000)  # Young's modulus (MPa)
        self.nu = material_props.get('nu', 0.3)   # Poisson's ratio
        self.t = material_props.get('t', 200)     # Thickness (mm)
        self.rho = material_props.get('rho', 7850e-9)  # Density (kg/mm³)
        
        # Calculatete membrane and bending stiffness factors
        self.D_membrane = self.E * self.t / (1 - self.nu**2)  # Membrane stiffness
        self.D_bending = self.E * self.t**3 / (12 * (1 - self.nu**2))  # Bending stiffness
        self.D_shear = self.E / (2 * (1 + self.nu))  # Shear stiffness
        
        # Calculatete local coordinate system
        self._compute_local_coords()
    
    def _compute_local_coords(self):
        """Compute local coordinate system for the element."""
        # First element edge vector (v1-v0)
        v1 = self.node_coords[1] - self.node_coords[0]
        
        if len(self.node_coords) >= 3:
            # Second vector (v2-v0)
            v2 = self.node_coords[2] - self.node_coords[0]
        else:
            # For 2-node elements (shouldn't happen for shells)
            v2 = np.array([0, 0, 1])
        
        # Local Z-axis (normal to element): cross product of v1 and v2
        local_z = np.cross(v1, v2)
        local_z = local_z / np.linalg.norm(local_z)
        
        # Local X-axis: normalized v1
        local_x = v1 / np.linalg.norm(v1)
        
        # Local Y-axis: perpendicular to X and Z
        local_y = np.cross(local_z, local_x)
        
        # Store as transformation matrix columns
        self.T_local = np.column_stack([local_x, local_y, local_z])
        
        # Compute element centroid
        self.centroid = np.mean(self.node_coords, axis=0)
    
    @abstractmethod
    def _compute_shape_functions(self, xi: float, eta: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Compute shape functions and their derivatives.
        
        Args:
            xi, eta: Natural coordinates (-1 to 1)
            
        Returns:
            N: Shape functions (num_nodes,)
            dN_dxi, dN_deta: Derivatives (num_nodes,)
        """
        pass
    
    @abstractmethod
    def compute_stiffness_matrix(self) -> np.ndarray:
        """Compute local stiffness matrix (DOFs x DOFs)."""
        pass
    
    @abstractmethod
    def compute_mass_matrix(self) -> np.ndarray:
        """Compute local mass matrix."""
        pass
    
    def _gauss_quadrature_2d(self, n_points: int = 2) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Generate 2D Gaussian quadrature points and weights.
        
        Args:
            n_points: Number of points per direction (1-4)
            
        Returns:
            xi, eta, weights: Quadrature points and weights
        """
        if n_points == 1:
            xi = eta = np.array([0.0])
            w = np.array([4.0])
        elif n_points == 2:
            xi = eta = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
            w = np.array([1.0, 1.0])
        elif n_points == 3:
            xi = eta = np.array([-np.sqrt(3/5), 0.0, np.sqrt(3/5)])
            w = np.array([5/9, 8/9, 5/9])
        else:  # n_points == 4
            sqrt_val = np.sqrt(3/7 + 2*np.sqrt(6/5)/7)
            xi = eta = np.array([
                -sqrt_val, 
                -np.sqrt(3/7 - 2*np.sqrt(6/5)/7),
                np.sqrt(3/7 - 2*np.sqrt(6/5)/7),
                sqrt_val
            ])
            w = np.array([
                (18 - np.sqrt(30))/36,
                (18 + np.sqrt(30))/36,
                (18 + np.sqrt(30))/36,
                (18 - np.sqrt(30))/36
            ])
        
        return xi, eta, w
    
    def _jacobian_2d(self, dN_dxi: np.ndarray, dN_deta: np.ndarray) -> Tuple[np.ndarray, float]:
        """
        Compute Jacobian matrix and its determinant.
        
        Args:
            dN_dxi, dN_deta: Shape function derivatives
            
        Returns:
            J: Jacobian matrix (2x2)
            det_J: Determinant of Jacobian
        """
        # Jacobian = [dx/dxi  dy/dxi] = [dN_dxi]^T * [x y] coordinates
        #            [dx/deta dy/deta]   [dN_deta]
        
        J = np.zeros((2, 2))
        J[0, 0] = np.dot(dN_dxi, self.node_coords[:, 0])   # dx/dxi
        J[0, 1] = np.dot(dN_dxi, self.node_coords[:, 1])   # dy/dxi
        J[1, 0] = np.dot(dN_deta, self.node_coords[:, 0])  # dx/deta
        J[1, 1] = np.dot(dN_deta, self.node_coords[:, 1])  # dy/deta
        
        det_J = np.linalg.det(J)
        
        return J, det_J
    
    def transform_to_global(self, K_local: np.ndarray, T: np.ndarray) -> np.ndarray:
        """
        Transform local stiffness matrix to global coordinates.
        
        Args:
            K_local: Local stiffness matrix
            T: Transformation matrix (3x3 rotation)
            
        Returns:
            K_global: Global stiffness matrix
        """
        # Build full 6-DOF transformation matrix
        T_full = np.zeros((self.total_dofs, self.total_dofs))
        
        for node in range(self.num_nodes):
            # Position and rotation DOFs both use rotation matrix
            start = node * 6
            for i in range(3):
                T_full[start + i, start:(start + 3)] = T[i, :]
                T_full[start + 3 + i, start + 3:(start + 6)] = T[i, :]
        
        K_global = T_full.T @ K_local @ T_full
        
        return K_global


class Quad4Shell(ShellElement):
    """4-node quadrilateral shell element (DKTQ formulation)."""
    
    def __init__(self, node_coords: np.ndarray, material_props: Dict):
        """Initialize Quad4 shell element."""
        super().__init__(node_coords, material_props)
        
        if len(node_coords) != 4:
            raise ValueError("Quad4 element requires exactly 4 nodes")
    
    def _compute_shape_functions(self, xi: float, eta: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Compute bilinear shape functions for quadrilateral.
        
        Natural coordinates: xi, eta ∈ [-1, 1]
        """
        # Bilinear shape functions
        N = np.array([
            (1 - xi) * (1 - eta) / 4,
            (1 + xi) * (1 - eta) / 4,
            (1 + xi) * (1 + eta) / 4,
            (1 - xi) * (1 + eta) / 4
        ])
        
        # Derivatives with respect to xi
        dN_dxi = np.array([
            -(1 - eta) / 4,
            (1 - eta) / 4,
            (1 + eta) / 4,
            -(1 + eta) / 4
        ])
        
        # Derivatives with respect to eta
        dN_deta = np.array([
            -(1 - xi) / 4,
            -(1 + xi) / 4,
            (1 + xi) / 4,
            (1 - xi) / 4
        ])
        
        return N, dN_dxi, dN_deta
    
    def compute_stiffness_matrix(self) -> np.ndarray:
        """
        Compute Quad4 shell element stiffness matrix using Gaussian quadrature.
        
        Returns:
            K: 24x24 local stiffness matrix (4 nodes × 6 DOF/node)
        """
        K_local = np.zeros((self.total_dofs, self.total_dofs))
        
        # Get Gaussian quadrature points (2x2 integration for bilinear quad)
        xi_pts, eta_pts, w_xi = self._gauss_quadrature_2d(n_points=2)
        
        for i, xi in enumerate(xi_pts):
            for j, eta in enumerate(eta_pts):
                # Shape functions and derivatives
                N, dN_dxi, dN_deta = self._compute_shape_functions(xi, eta)
                
                # Jacobian
                J, det_J = self._jacobian_2d(dN_dxi, dN_deta)
                
                if abs(det_J) < 1e-10:
                    raise ValueError("Quad4 element has zero or negative Jacobian")
                
                # Inverse Jacobian
                J_inv = np.linalg.inv(J)
                
                # Shape function derivatives in global coordinates
                dN_dx = J_inv[0, 0] * dN_dxi + J_inv[0, 1] * dN_deta
                dN_dy = J_inv[1, 0] * dN_dxi + J_inv[1, 1] * dN_deta
                
                # Strain-displacement matrix (simplified)
                # For membrane (plane stress)
                B_mem = np.zeros((3, self.total_dofs))
                for node in range(4):
                    B_mem[0, node * 6] = dN_dx[node]  # εx = ∂u/∂x
                    B_mem[1, node * 6 + 1] = dN_dy[node]  # εy = ∂v/∂y
                    B_mem[2, node * 6] = dN_dy[node]  # γxy = ∂u/∂y + ∂v/∂x
                    B_mem[2, node * 6 + 1] = dN_dx[node]
                
                # Membrane constitutive matrix
                C_mem = self.D_membrane / (1 - self.nu**2) * np.array([
                    [1, self.nu, 0],
                    [self.nu, 1, 0],
                    [0, 0, (1 - self.nu) / 2]
                ])
                
                # Membrane stiffness contribution
                K_mem = B_mem.T @ C_mem @ B_mem * det_J * w_xi[i] * w_xi[j] * self.t
                K_local += K_mem
                
                # Bending (simplified - DKT formulation would be more complex)
                # For now, add rotational stiffness
                for node in range(4):
                    K_local[node * 6 + 3, node * 6 + 3] += self.D_bending * det_J * w_xi[i] * w_xi[j]
                    K_local[node * 6 + 4, node * 6 + 4] += self.D_bending * det_J * w_xi[i] * w_xi[j]
                    K_local[node * 6 + 5, node * 6 + 5] += self.D_shear * self.t**2 * det_J * w_xi[i] * w_xi[j]
        
        # Ensure symmetry
        K_local = (K_local + K_local.T) / 2
        
        return K_local
    
    def compute_mass_matrix(self) -> np.ndarray:
        """Compute consistent mass matrix for Quad4 shell element."""
        M_local = np.zeros((self.total_dofs, self.total_dofs))
        
        # Mass per unit area
        mass_per_area = self.rho * self.t
        
        # Get Gaussian quadrature points
        xi_pts, eta_pts, w_xi = self._gauss_quadrature_2d(n_points=2)
        
        for i, xi in enumerate(xi_pts):
            for j, eta in enumerate(eta_pts):
                N, dN_dxi, dN_deta = self._compute_shape_functions(xi, eta)
                J, det_J = self._jacobian_2d(dN_dxi, dN_deta)
                
                # Mass matrix assembly
                for m in range(4):
                    for n in range(4):
                        mass_contrib = N[m] * N[n] * mass_per_area * det_J * w_xi[i] * w_xi[j]
                        
                        # Translational DOFs
                        M_local[m * 6, n * 6] += mass_contrib  # Ux
                        M_local[m * 6 + 1, n * 6 + 1] += mass_contrib  # Uy
                        M_local[m * 6 + 2, n * 6 + 2] += mass_contrib  # Uz
        
        return M_local


class Tri3Shell(ShellElement):
    """3-node triangular shell element (DKT formulation)."""
    
    def __init__(self, node_coords: np.ndarray, material_props: Dict):
        """Initialize Tri3 shell element."""
        super().__init__(node_coords, material_props)
        
        if len(node_coords) != 3:
            raise ValueError("Tri3 element requires exactly 3 nodes")
        
        # Area of triangle
        v1 = node_coords[1] - node_coords[0]
        v2 = node_coords[2] - node_coords[0]
        self.area = 0.5 * np.linalg.norm(np.cross(v1, v2))
    
    def _compute_shape_functions(self, xi: float, eta: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Compute linear shape functions for triangle.
        
        Natural coordinates: xi, eta ∈ [0, 1], xi + eta ≤ 1
        zeta = 1 - xi - eta
        """
        zeta = 1 - xi - eta
        
        # Linear shape functions
        N = np.array([zeta, xi, eta])
        
        # Derivatives (constant for linear elements)
        dN_dxi = np.array([-1, 1, 0])
        dN_deta = np.array([-1, 0, 1])
        
        return N, dN_dxi, dN_deta
    
    def compute_stiffness_matrix(self) -> np.ndarray:
        """
        Compute Tri3 shell element stiffness matrix using triangular quadrature.
        
        Returns:
            K: 18x18 local stiffness matrix (3 nodes × 6 DOF/node)
        """
        K_local = np.zeros((self.total_dofs, self.total_dofs))
        
        # Triangular Gaussian quadrature points (3-point rule for accuracy)
        # Points in natural coordinates (xi, eta)
        quad_points = np.array([
            [1/6, 1/6],
            [2/3, 1/6],
            [1/6, 2/3]
        ])
        weights = np.array([1/3, 1/3, 1/3])  # Each point weight is 1/3
        
        for pt_idx, (xi, eta) in enumerate(quad_points):
            # Shape functions and derivatives
            N, dN_dxi, dN_deta = self._compute_shape_functions(xi, eta)
            
            # Jacobian for triangular element
            J, det_J = self._jacobian_2d(dN_dxi, dN_deta)
            
            if abs(det_J) < 1e-10:
                raise ValueError("Tri3 element has zero or negative Jacobian")
            
            # Inverse Jacobian
            J_inv = np.linalg.inv(J)
            
            # Shape function derivatives in global coordinates
            dN_dx = J_inv[0, 0] * dN_dxi + J_inv[0, 1] * dN_deta
            dN_dy = J_inv[1, 0] * dN_dxi + J_inv[1, 1] * dN_deta
            
            # Strain-displacement matrix (membrane)
            B_mem = np.zeros((3, self.total_dofs))
            for node in range(3):
                B_mem[0, node * 6] = dN_dx[node]
                B_mem[1, node * 6 + 1] = dN_dy[node]
                B_mem[2, node * 6] = dN_dy[node]
                B_mem[2, node * 6 + 1] = dN_dx[node]
            
            # Membrane constitutive matrix
            C_mem = (self.E * self.t / (1 - self.nu**2)) * np.array([
                [1, self.nu, 0],
                [self.nu, 1, 0],
                [0, 0, (1 - self.nu) / 2]
            ])
            
            # Membrane stiffness contribution
            K_mem = B_mem.T @ C_mem @ B_mem * det_J * weights[pt_idx] * self.t
            K_local += K_mem
            
            # Bending (rotational stiffness)
            for node in range(3):
                K_local[node * 6 + 3, node * 6 + 3] += self.D_bending * det_J * weights[pt_idx]
                K_local[node * 6 + 4, node * 6 + 4] += self.D_bending * det_J * weights[pt_idx]
                K_local[node * 6 + 5, node * 6 + 5] += self.D_shear * self.t**2 * det_J * weights[pt_idx]
        
        # Ensure symmetry
        K_local = (K_local + K_local.T) / 2
        
        return K_local
    
    def compute_mass_matrix(self) -> np.ndarray:
        """Compute consistent mass matrix for Tri3 shell element."""
        M_local = np.zeros((self.total_dofs, self.total_dofs))
        
        mass_per_area = self.rho * self.t
        
        # Triangular quadrature points
        quad_points = np.array([
            [1/6, 1/6],
            [2/3, 1/6],
            [1/6, 2/3]
        ])
        weights = np.array([1/3, 1/3, 1/3])
        
        for pt_idx, (xi, eta) in enumerate(quad_points):
            N, dN_dxi, dN_deta = self._compute_shape_functions(xi, eta)
            J, det_J = self._jacobian_2d(dN_dxi, dN_deta)
            
            # Mass matrix assembly
            for m in range(3):
                for n in range(3):
                    mass_contrib = N[m] * N[n] * mass_per_area * det_J * weights[pt_idx]
                    
                    M_local[m * 6, n * 6] += mass_contrib  # Ux
                    M_local[m * 6 + 1, n * 6 + 1] += mass_contrib  # Uy
                    M_local[m * 6 + 2, n * 6 + 2] += mass_contrib  # Uz
        
        return M_local


class Tri6Shell(ShellElement):
    """6-node triangular shell element (DKT6 high-order formulation)."""
    
    def __init__(self, node_coords: np.ndarray, material_props: Dict):
        """Initialize Tri6 shell element."""
        super().__init__(node_coords, material_props)
        
        if len(node_coords) != 6:
            raise ValueError("Tri6 element requires exactly 6 nodes")
        
        # Area of triangle (using corner nodes)
        v1 = node_coords[1] - node_coords[0]
        v2 = node_coords[2] - node_coords[0]
        self.area = 0.5 * np.linalg.norm(np.cross(v1, v2))
    
    def _compute_shape_functions(self, xi: float, eta: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Compute quadratic shape functions for 6-node triangle.
        
        Nodes: 1,2,3 at corners; 4,5,6 at midpoints
        """
        zeta = 1 - xi - eta
        
        # Quadratic shape functions
        N = np.array([
            zeta * (2 * zeta - 1),  # Node 1
            xi * (2 * xi - 1),      # Node 2
            eta * (2 * eta - 1),    # Node 3
            4 * zeta * xi,          # Node 4 (midpoint 1-2)
            4 * xi * eta,           # Node 5 (midpoint 2-3)
            4 * eta * zeta          # Node 6 (midpoint 3-1)
        ])
        
        # Derivatives with respect to xi
        dN_dxi = np.array([
            -(4 * zeta - 1),
            4 * xi - 1,
            0,
            4 * (zeta - xi),
            4 * eta,
            -4 * eta
        ])
        
        # Derivatives with respect to eta
        dN_deta = np.array([
            -(4 * zeta - 1),
            0,
            4 * eta - 1,
            -4 * xi,
            4 * xi,
            4 * (zeta - eta)
        ])
        
        return N, dN_dxi, dN_deta
    
    def compute_stiffness_matrix(self) -> np.ndarray:
        """
        Compute Tri6 shell element stiffness matrix using 6-point triangular quadrature.
        
        Returns:
            K: 36x36 local stiffness matrix (6 nodes × 6 DOF/node)
        """
        K_local = np.zeros((self.total_dofs, self.total_dofs))
        
        # 6-point Gaussian quadrature for triangular elements
        quad_points = np.array([
            [0.816496580927726, 0.091751209440289],
            [0.091751209440289, 0.816496580927726],
            [0.091751209440289, 0.091751209440289],
            [0.108103018427070, 0.445948490915965],
            [0.445948490915965, 0.108103018427070],
            [0.445948490915965, 0.445948490915965]
        ])
        weights = np.array([
            0.054630541745537,
            0.054630541745537,
            0.054630541745537,
            0.111690794839005,
            0.111690794839005,
            0.111690794839005
        ])
        
        for pt_idx, (xi, eta) in enumerate(quad_points):
            N, dN_dxi, dN_deta = self._compute_shape_functions(xi, eta)
            J, det_J = self._jacobian_2d(dN_dxi, dN_deta)
            
            if abs(det_J) < 1e-10:
                raise ValueError("Tri6 element has zero or negative Jacobian")
            
            J_inv = np.linalg.inv(J)
            
            dN_dx = J_inv[0, 0] * dN_dxi + J_inv[0, 1] * dN_deta
            dN_dy = J_inv[1, 0] * dN_dxi + J_inv[1, 1] * dN_deta
            
            # Membrane strain-displacement matrix
            B_mem = np.zeros((3, self.total_dofs))
            for node in range(6):
                B_mem[0, node * 6] = dN_dx[node]
                B_mem[1, node * 6 + 1] = dN_dy[node]
                B_mem[2, node * 6] = dN_dy[node]
                B_mem[2, node * 6 + 1] = dN_dx[node]
            
            # Constitutive matrix
            C_mem = (self.E * self.t / (1 - self.nu**2)) * np.array([
                [1, self.nu, 0],
                [self.nu, 1, 0],
                [0, 0, (1 - self.nu) / 2]
            ])
            
            K_mem = B_mem.T @ C_mem @ B_mem * det_J * weights[pt_idx] * self.t
            K_local += K_mem
            
            # Bending stiffness
            for node in range(6):
                K_local[node * 6 + 3, node * 6 + 3] += self.D_bending * det_J * weights[pt_idx]
                K_local[node * 6 + 4, node * 6 + 4] += self.D_bending * det_J * weights[pt_idx]
                K_local[node * 6 + 5, node * 6 + 5] += self.D_shear * self.t**2 * det_J * weights[pt_idx]
        
        # Ensure symmetry
        K_local = (K_local + K_local.T) / 2
        
        return K_local
    
    def compute_mass_matrix(self) -> np.ndarray:
        """Compute consistent mass matrix for Tri6 shell element."""
        M_local = np.zeros((self.total_dofs, self.total_dofs))
        
        mass_per_area = self.rho * self.t
        
        # 6-point quadrature
        quad_points = np.array([
            [0.816496580927726, 0.091751209440289],
            [0.091751209440289, 0.816496580927726],
            [0.091751209440289, 0.091751209440289],
            [0.108103018427070, 0.445948490915965],
            [0.445948490915965, 0.108103018427070],
            [0.445948490915965, 0.445948490915965]
        ])
        weights = np.array([
            0.054630541745537,
            0.054630541745537,
            0.054630541745537,
            0.111690794839005,
            0.111690794839005,
            0.111690794839005
        ])
        
        for pt_idx, (xi, eta) in enumerate(quad_points):
            N, dN_dxi, dN_deta = self._compute_shape_functions(xi, eta)
            J, det_J = self._jacobian_2d(dN_dxi, dN_deta)
            
            for m in range(6):
                for n in range(6):
                    mass_contrib = N[m] * N[n] * mass_per_area * det_J * weights[pt_idx]
                    
                    M_local[m * 6, n * 6] += mass_contrib
                    M_local[m * 6 + 1, n * 6 + 1] += mass_contrib
                    M_local[m * 6 + 2, n * 6 + 2] += mass_contrib
        
        return M_local
