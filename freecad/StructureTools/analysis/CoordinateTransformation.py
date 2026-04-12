# -*- coding: utf-8 -*-
"""
CoordinateTransformation - 3D coordinate transformation for shell elements

Handles:
- Local to global coordinate system conversions
- 3D rotation matrices
- Drilling DOF transformation
- Element orientation in 3D space
"""

import numpy as np
from typing import Tuple, Optional


class CoordinateTransformer:
    """Transform between local and global coordinate systems."""
    
    def __init__(self, element_nodes: np.ndarray):
        """
        Initialize transformer with element node coordinates.
        
        Args:
            element_nodes: Array of node coordinates (N x 3)
        """
        self.element_nodes = np.array(element_nodes)
        self.local_system = None
        self.rotation_matrix = None
        self.compute_local_system()
    
    def compute_local_system(self) -> None:
        """
        Compute local coordinate system from element nodes.
        
        For shell elements:
        - Local X: along first edge (node0 -> node1)
        - Local Y: in plane, perpendicular to X
        - Local Z: normal to element surface
        """
        if len(self.element_nodes) < 3:
            raise ValueError("Need at least 3 nodes to define local system")
        
        # Get three corner nodes
        p0 = self.element_nodes[0]
        p1 = self.element_nodes[1]
        p2 = self.element_nodes[2]
        
        # Vector along first edge (local X)
        v1 = p1 - p0
        local_x = v1 / np.linalg.norm(v1)
        
        # Vector from first to third node
        v2 = p2 - p0
        
        # Normal to element (local Z)
        v_normal = np.cross(v1, v2)
        local_z = v_normal / np.linalg.norm(v_normal)
        
        # Perpendicular to X and Z (local Y)
        local_y = np.cross(local_z, local_x)
        local_y = local_y / np.linalg.norm(local_y)
        
        # Store local system as transformation matrix (columns are basis vectors)
        self.local_system = np.column_stack([local_x, local_y, local_z])
        
        # Rotation matrix from local to global
        # R: global = R @ local
        self.rotation_matrix = self.local_system.T
    
    def get_rotation_matrix(self) -> np.ndarray:
        """
        Get 3x3 rotation matrix from local to global coordinates.
        
        Returns:
            R: 3x3 matrix where [x_global] = R^T @ [x_local]
        """
        return self.local_system
    
    def get_inverse_rotation(self) -> np.ndarray:
        """Get rotation matrix from global to local."""
        return self.rotation_matrix
    
    def local_to_global_vector(self, v_local: np.ndarray) -> np.ndarray:
        """
        Transform vector from local to global coordinates.
        
        Args:
            v_local: Vector in local coordinates
            
        Returns:
            v_global: Vector in global coordinates
        """
        return self.local_system @ v_local
    
    def global_to_local_vector(self, v_global: np.ndarray) -> np.ndarray:
        """
        Transform vector from global to local coordinates.
        
        Args:
            v_global: Vector in global coordinates
            
        Returns:
            v_local: Vector in local coordinates
        """
        return self.rotation_matrix @ v_global
    
    def local_to_global_matrix(self, M_local: np.ndarray) -> np.ndarray:
        """
        Transform stiffness/mass matrix from local to global coordinates.
        
        For 6-DOF elements: [K_global] = [T]^T @ [K_local] @ [T]
        where T is block diagonal with rotation matrices
        
        Args:
            M_local: Local matrix (n_dofs x n_dofs)
            
        Returns:
            M_global: Global matrix (n_dofs x n_dofs)
        """
        n_dofs = M_local.shape[0]
        n_nodes = n_dofs // 6
        
        if n_dofs % 6 != 0:
            raise ValueError(f"Matrix size {n_dofs} not multiple of 6")
        
        # Build transformation matrix for 6-DOF per node
        T_full = np.zeros((n_dofs, n_dofs))
        
        for node_idx in range(n_nodes):
            start = node_idx * 6
            
            # Translation DOFs (0-2)
            T_full[start:start+3, start:start+3] = self.local_system
            
            # Rotation DOFs (3-5) - same rotation matrix
            T_full[start+3:start+6, start+3:start+6] = self.local_system
        
        # Transform: M_global = T^T @ M_local @ T
        M_global = T_full.T @ M_local @ T_full
        
        return M_global
    
    def global_to_local_matrix(self, M_global: np.ndarray) -> np.ndarray:
        """
        Transform matrix from global to local coordinates.
        
        Args:
            M_global: Global matrix
            
        Returns:
            M_local: Local matrix
        """
        n_dofs = M_global.shape[0]
        n_nodes = n_dofs // 6
        
        # Build inverse transformation
        T_inv = np.zeros((n_dofs, n_dofs))
        
        for node_idx in range(n_nodes):
            start = node_idx * 6
            T_inv[start:start+3, start:start+3] = self.rotation_matrix
            T_inv[start+3:start+6, start+3:start+6] = self.rotation_matrix
        
        # M_local = T_inv @ M_global @ T_inv^T
        M_local = T_inv @ M_global @ T_inv.T
        
        return M_local


class DrillingDOFHandler:
    """Handle drilling DOF (rotation about surface normal) for shell elements."""
    
    def __init__(self, stiffness_factor: float = 1e-6):
        """
        Initialize drilling DOF handler.
        
        Args:
            stiffness_factor: Relative stiffness for drilling DOF
                (small value to avoid singular matrix)
        """
        self.stiffness_factor = stiffness_factor
    
    def add_drilling_stiffness(self, K_local: np.ndarray, 
                               E: float, t: float, elem_type: str) -> np.ndarray:
        """
        Add drilling stiffness to element matrix.
        
        Prevents singular matrix from free drilling rotation.
        
        Args:
            K_local: Local stiffness matrix (6*n_nodes x 6*n_nodes)
            E: Young's modulus
            t: Element thickness
            elem_type: 'quad4', 'tri3', or 'tri6'
            
        Returns:
            K_modified: Matrix with drilling stiffness added
        """
        K_mod = K_local.copy()
        
        n_dofs = K_local.shape[0]
        n_nodes = n_dofs // 6
        
        # Calculate characteristic drilling stiffness
        # Based on membrane stiffness
        G = E / (2 * (1 + 0.3))  # Shear modulus (assume nu=0.3)
        K_drill = self.stiffness_factor * G * t
        
        # Add to drilling DOF (rotation about Z, index 5 per node)
        for node_idx in range(n_nodes):
            dof_drill = node_idx * 6 + 5
            K_mod[dof_drill, dof_drill] += K_drill
        
        return K_mod


class ElementOrientation:
    """Manage element orientation in 3D space."""
    
    def __init__(self, normal_vector: np.ndarray, 
                 reference_vector: Optional[np.ndarray] = None):
        """
        Initialize element orientation.
        
        Args:
            normal_vector: Surface normal vector (Z-axis)
            reference_vector: Optional reference vector for X-axis orientation
        """
        self.normal = np.array(normal_vector) / np.linalg.norm(normal_vector)
        
        # Set reference vector
        if reference_vector is None:
            # Choose reference perpendicular to normal
            if abs(self.normal[2]) < 0.9:
                reference_vector = np.array([0, 0, 1])
            else:
                reference_vector = np.array([1, 0, 0])
        
        self.reference = np.array(reference_vector) / np.linalg.norm(reference_vector)
        
        # Build orthonormal system
        self._build_local_system()
    
    def _build_local_system(self) -> None:
        """Build local coordinate system."""
        # X-axis: projection of reference perpendicular to normal
        x_temp = self.reference - np.dot(self.reference, self.normal) * self.normal
        self.local_x = x_temp / np.linalg.norm(x_temp)
        
        # Y-axis: perpendicular to both X and Z(normal)
        self.local_y = np.cross(self.normal, self.local_x)
        self.local_y = self.local_y / np.linalg.norm(self.local_y)
    
    def get_axes(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Get local coordinate axes.
        
        Returns:
            x, y, z: Unit vectors for local X, Y, Z axes
        """
        return self.local_x, self.local_y, self.normal
    
    def get_rotation_matrix(self) -> np.ndarray:
        """
        Get rotation matrix from local to global.
        
        Returns:
            R: 3x3 matrix (columns are local axes in global coords)
        """
        return np.column_stack([self.local_x, self.local_y, self.normal])
    
    def rotate_vector(self, v_local: np.ndarray) -> np.ndarray:
        """Rotate vector from local to global."""
        R = self.get_rotation_matrix()
        return R @ v_local
    
    def unrotate_vector(self, v_global: np.ndarray) -> np.ndarray:
        """Rotate vector from global to local."""
        R = self.get_rotation_matrix()
        return R.T @ v_global


class PlatePlaneDefinition:
    """Define plate plane in 3D space (useful for inclined plates)."""
    
    def __init__(self, plane_point: np.ndarray, 
                 plane_normal: np.ndarray,
                 plane_x_direction: Optional[np.ndarray] = None):
        """
        Initialize plate plane definition.
        
        Args:
            plane_point: Point on the plate plane
            plane_normal: Normal vector to plane
            plane_x_direction: Direction for local X-axis (optional)
        """
        self.point = np.array(plane_point)
        self.normal = np.array(plane_normal) / np.linalg.norm(plane_normal)
        
        if plane_x_direction is None:
            # Default X direction (perpendicular to normal and Z-axis)
            if abs(self.normal[2]) < 0.9:
                plane_x_direction = np.array([0, 0, 1])
            else:
                plane_x_direction = np.array([1, 0, 0])
        
        # Project X direction to plane
        self.x_direction = np.array(plane_x_direction)
        self.x_direction -= np.dot(self.x_direction, self.normal) * self.normal
        self.x_direction /= np.linalg.norm(self.x_direction)
        
        # Y direction
        self.y_direction = np.cross(self.normal, self.x_direction)
        self.y_direction /= np.linalg.norm(self.y_direction)
    
    def project_point_to_plane(self, point: np.ndarray) -> np.ndarray:
        """Project point onto plane."""
        to_point = np.array(point) - self.point
        distance = np.dot(to_point, self.normal)
        return np.array(point) - distance * self.normal
    
    def get_plane_coords(self, point: np.ndarray) -> Tuple[float, float]:
        """
        Get 2D coordinates of point in plane.
        
        Returns:
            x, y: Coordinates in plane
        """
        to_point = np.array(point) - self.point
        x = np.dot(to_point, self.x_direction)
        y = np.dot(to_point, self.y_direction)
        return x, y
    
    def get_global_coords(self, x: float, y: float) -> np.ndarray:
        """Get 3D global coordinates from 2D plane coordinates."""
        return self.point + x * self.x_direction + y * self.y_direction
