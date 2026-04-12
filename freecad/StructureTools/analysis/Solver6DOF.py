# -*- coding: utf-8 -*-
"""
Solver6DOF - Enhanced FEM solver supporting 6-DOF per node

Supports:
- 3-DOF (beam/truss) and 6-DOF (plate/shell) mixed elements
- Global stiffness assembly
- Boundary condition enforcement
- Load vector assembly
- Static linear analysis
"""

import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.linalg import spsolve
from typing import Dict, List, Tuple, Optional, Any
import warnings


class DOFMapping:
    """Manages degree of freedom mapping between local and global systems."""
    
    def __init__(self):
        """Initialize DOF mapper."""
        self.element_dofs = {}  # {elem_id: [dof_indices]}
        self.node_to_dofs = {}  # {node_id: [dof_indices]}
        self.dof_to_node = {}   # {dof_id: (node_id, local_dof)}
        self.global_dofs = 0
        self.node_dof_count = {}  # {node_id: num_dofs}
    
    def add_node(self, node_id: int, num_dofs: int = 3) -> None:
        """
        Add node with specified DOF count.
        
        Args:
            node_id: Node identifier
            num_dofs: Number of DOFs per node (3 for beam, 6 for plate)
        """
        if node_id in self.node_to_dofs:
            raise ValueError(f"Node {node_id} already exists")
        
        self.node_dof_count[node_id] = num_dofs
        dof_indices = list(range(self.global_dofs, self.global_dofs + num_dofs))
        
        self.node_to_dofs[node_id] = dof_indices
        
        for local_dof, global_dof in enumerate(dof_indices):
            self.dof_to_node[global_dof] = (node_id, local_dof)
        
        self.global_dofs += num_dofs
    
    def add_element(self, elem_id: int, node_ids: List[int]) -> None:
        """
        Add element and compute global DOF indices.
        
        Args:
            elem_id: Element identifier
            node_ids: List of node IDs connected to element
        """
        element_dofs = []
        
        for node_id in node_ids:
            if node_id not in self.node_to_dofs:
                raise ValueError(f"Node {node_id} not found in DOF map")
            
            element_dofs.extend(self.node_to_dofs[node_id])
        
        self.element_dofs[elem_id] = element_dofs
    
    def get_element_dofs(self, elem_id: int) -> List[int]:
        """Get global DOF indices for element."""
        return self.element_dofs.get(elem_id, [])
    
    def get_node_dofs(self, node_id: int) -> List[int]:
        """Get global DOF indices for node."""
        return self.node_to_dofs.get(node_id, [])


class BoundaryCondition:
    """Represents a boundary condition."""
    
    def __init__(self, node_id: int, dof: int, value: float = 0.0):
        """
        Initialize boundary condition.
        
        Args:
            node_id: Node with BC
            dof: DOF index (0-2 for translations, 3-5 for rotations)
            value: Prescribed value (usually 0 for fixed)
        """
        self.node_id = node_id
        self.dof = dof
        self.value = value
    
    def __repr__(self):
        dof_names = ['Ux', 'Uy', 'Uz', 'Rx', 'Ry', 'Rz']
        return f"BC(node={self.node_id}, {dof_names[self.dof]}={self.value})"


class Solver6DOF:
    """
    6-DOF FEM solver for mixed beam/plate/shell structures.
    
    Supports:
    - Assembly of global stiffness matrix
    - Multiple element types with different DOF counts
    - Enforced boundary conditions
    - Load vector assembly
    - Static linear system solution
    """
    
    def __init__(self, sparse: bool = True):
        """
        Initialize solver.
        
        Args:
            sparse: Use sparse matrix format (recommended for large systems)
        """
        self.sparse = sparse
        self.dof_map = DOFMapping()
        self.K_global = None
        self.F_global = None
        self.U_global = None
        
        self.elements = {}  # {elem_id: {'nodes': [...], 'K': matrix, 'type': '...'}}
        self.boundary_conditions = []  # List of BoundaryCondition objects
        self.loads = {}  # {dof_id: force_value}
        
        self.displacement_results = None
        self.reaction_forces = None
        self.stress_results = {}
    
    def add_node(self, node_id: int, num_dofs: int = 3) -> None:
        """Add node to system."""
        self.dof_map.add_node(node_id, num_dofs)
    
    def add_element(self, elem_id: int, node_ids: List[int], 
                   K_local: np.ndarray, elem_type: str = "Unknown") -> None:
        """
        Add element to system.
        
        Args:
            elem_id: Element ID
            node_ids: Connected node IDs
            K_local: Local stiffness matrix
            elem_type: Element type string (for reporting)
        """
        # Verify nodes exist and have compatible DOFs
        total_local_dofs = K_local.shape[0]
        expected_dofs = sum(self.dof_map.node_dof_count.get(nid, 3) for nid in node_ids)
        
        if total_local_dofs != expected_dofs:
            raise ValueError(
                f"Element {elem_id}: Local matrix size {total_local_dofs} "
                f"doesn't match expected {expected_dofs} DOFs"
            )
        
        # Map element DOFs
        self.dof_map.add_element(elem_id, node_ids)
        
        # Store element data
        self.elements[elem_id] = {
            'nodes': node_ids,
            'K': K_local.copy(),
            'type': elem_type
        }
    
    def add_boundary_condition(self, bc: BoundaryCondition) -> None:
        """Add boundary condition."""
        self.boundary_conditions.append(bc)
    
    def add_load(self, node_id: int, dof: int, value: float) -> None:
        """
        Add nodal load.
        
        Args:
            node_id: Node with load
            dof: DOF index
            value: Load value
        """
        node_dofs = self.dof_map.get_node_dofs(node_id)
        
        if dof >= len(node_dofs):
            raise ValueError(f"Node {node_id} doesn't have DOF {dof}")
        
        global_dof = node_dofs[dof]
        self.loads[global_dof] = self.loads.get(global_dof, 0) + value
    
    def assemble(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Assemble global stiffness matrix and load vector.
        
        Returns:
            K_global: Global stiffness matrix
            F_global: Global load vector
        """
        n_dofs = self.dof_map.global_dofs
        
        # Initialize matrices
        if self.sparse:
            K_global = lil_matrix((n_dofs, n_dofs))
        else:
            K_global = np.zeros((n_dofs, n_dofs))
        
        F_global = np.zeros(n_dofs)
        
        # Assemble stiffness matrix from elements
        for elem_id, elem_data in self.elements.items():
            elem_dofs = self.dof_map.get_element_dofs(elem_id)
            K_local = elem_data['K']
            
            # Add to global matrix
            for i, global_i in enumerate(elem_dofs):
                for j, global_j in enumerate(elem_dofs):
                    if self.sparse:
                        K_global[global_i, global_j] += K_local[i, j]
                    else:
                        K_global[global_i, global_j] += K_local[i, j]
        
        # Assemble load vector
        for global_dof, force in self.loads.items():
            F_global[global_dof] += force
        
        # Convert sparse matrix if needed
        if self.sparse:
            K_global = csr_matrix(K_global)
        
        self.K_global = K_global
        self.F_global = F_global
        
        return K_global, F_global
    
    def apply_boundary_conditions(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Apply boundary conditions using penalty method or direct elimination.
        
        Returns:
            K_modified: Modified stiffness matrix
            F_modified: Modified load vector
        """
        if self.K_global is None or self.F_global is None:
            raise ValueError("Must call assemble() before applying BCs")
        
        n_dofs = self.dof_map.global_dofs
        
        # Create modified matrices
        if self.sparse:
            K_mod = self.K_global.tolil()
        else:
            K_mod = self.K_global.copy()
        
        F_mod = self.F_global.copy()
        
        # Apply each BC
        constrained_dofs = set()
        
        for bc in self.boundary_conditions:
            node_dofs = self.dof_map.get_node_dofs(bc.node_id)
            
            if bc.dof >= len(node_dofs):
                warnings.warn(f"BC on {bc}: DOF {bc.dof} doesn't exist for node")
                continue
            
            global_dof = node_dofs[bc.dof]
            constrained_dofs.add(global_dof)
            
            # Direct elimination method
            # Set row and column to identity
            if self.sparse:
                K_mod[global_dof, :] = 0
                K_mod[global_dof, global_dof] = 1.0
            else:
                K_mod[global_dof, :] = 0
                K_mod[global_dof, global_dof] = 1.0
            
            # Set load to prescribed value
            F_mod[global_dof] = bc.value
        
        # Convert back to csr if sparse
        if self.sparse:
            K_mod = csr_matrix(K_mod)
        
        return K_mod, F_mod
    
    def solve(self, method: str = 'direct') -> np.ndarray:
        """
        Solve linear system.
        
        Args:
            method: 'direct' for dense or sparse direct solver
            
        Returns:
            U_global: Global displacement vector
        """
        # Assemble system
        self.assemble()
        
        # Apply boundary conditions
        K_mod, F_mod = self.apply_boundary_conditions()
        
        # Solve
        try:
            if self.sparse:
                # Use sparse solver
                U_global = spsolve(K_mod, F_mod)
            else:
                # Use dense solver
                U_global = np.linalg.solve(K_mod, F_mod)
        except np.linalg.LinAlgError as e:
            raise RuntimeError(f"Solver failed: {e}")
        
        self.U_global = U_global
        return U_global
    
    def get_displacements(self, node_id: int) -> np.ndarray:
        """
        Get displacements at node.
        
        Args:
            node_id: Node ID
            
        Returns:
            Displacement vector [Ux, Uy, Uz, Rx, Ry, Rz] (only non-zero components)
        """
        if self.U_global is None:
            raise ValueError("Must solve system first")
        
        node_dofs = self.dof_map.get_node_dofs(node_id)
        return self.U_global[node_dofs]
    
    def get_reaction_forces(self) -> Dict[int, np.ndarray]:
        """
        Calculate reaction forces at constrained DOFs.
        
        Returns:
            Dictionary {node_id: reaction_vector}
        """
        if self.U_global is None:
            raise ValueError("Must solve system first")
        
        reactions = {}
        
        # Calculatete F = K * U for constrained nodes
        if self.sparse:
            F_reactions = self.K_global @ self.U_global
        else:
            F_reactions = self.K_global @ self.U_global
        
        # Extract reactions at constrained DOFs
        for bc in self.boundary_conditions:
            node_id = bc.node_id
            node_dofs = self.dof_map.get_node_dofs(node_id)
            global_dof = node_dofs[bc.dof]
            
            # Reaction force = applied force - computed force
            reaction = self.F_global[global_dof] - F_reactions[global_dof]
            
            if node_id not in reactions:
                reactions[node_id] = np.zeros(len(node_dofs))
            
            reactions[node_id][bc.dof] = reaction
        
        return reactions
    
    def get_element_forces(self, elem_id: int) -> np.ndarray:
        """
        Calculate element internal forces.
        
        Args:
            elem_id: Element ID
            
        Returns:
            Element force vector (local DOFs)
        """
        if self.U_global is None:
            raise ValueError("Must solve system first")
        
        if elem_id not in self.elements:
            raise ValueError(f"Element {elem_id} not found")
        
        elem_dofs = self.dof_map.get_element_dofs(elem_id)
        K_local = self.elements[elem_id]['K']
        
        # Get element displacements
        U_elem = self.U_global[elem_dofs]
        
        # Element forces
        F_elem = K_local @ U_elem
        
        return F_elem
    
    def get_stiffness_check(self) -> Dict[str, float]:
        """
        Compute stiffness matrix properties (for diagnostics).
        
        Returns:
            Dictionary with matrix properties
        """
        if self.K_global is None:
            raise ValueError("Must assemble system first")
        
        K = self.K_global
        if self.sparse:
            K = K.toarray()
        
        eigenvalues = np.linalg.eigvalsh(K)
        
        return {
            'condition_number': np.linalg.cond(K),
            'rank': np.linalg.matrix_rank(K),
            'min_eigenvalue': np.min(eigenvalues),
            'max_eigenvalue': np.max(eigenvalues),
            'num_zero_eigenvalues': np.sum(np.abs(eigenvalues) < 1e-10),
            'matrix_norm': np.linalg.norm(K),
            'sparsity': 1 - np.count_nonzero(K) / K.size if K.size > 0 else 0
        }
    
    def get_summary(self) -> Dict[str, Any]:
        """Get solution summary."""
        return {
            'num_nodes': len(self.dof_map.node_to_dofs),
            'num_dofs': self.dof_map.global_dofs,
            'num_elements': len(self.elements),
            'num_boundary_conditions': len(self.boundary_conditions),
            'num_loads': len(self.loads),
            'max_displacement': np.max(np.abs(self.U_global)) if self.U_global is not None else None,
            'solution_converged': self.U_global is not None
        }
