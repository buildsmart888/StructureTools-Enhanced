"""
Member Force Summary Module

Extracts maximum and minimum member force values with their positions
from PyNite FE analysis results.
"""

import FreeCAD
from typing import Dict, List, Tuple, Optional, Any
import logging

try:
    from numpy import argmax, argmin
except ImportError:
    # Fallback if numpy not available
    def argmax(arr):
        return max(range(len(arr)), key=lambda i: arr[i])
    def argmin(arr):
        return min(range(len(arr)), key=lambda i: arr[i])

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class MemberForceSummary:
    """Extract and store member force extremes from analysis results."""
    
    # Force components to analyze
    FORCE_COMPONENTS = [
        ('Fx', 'Axial'),      # Axial force
        ('Fy', 'Shear'),      # Shear Y
        ('Fz', 'Shear'),      # Shear Z
        ('Mx', 'Torsion'),    # Torsion
        ('My', 'Bending'),    # Bending Y
        ('Mz', 'Bending'),    # Bending Z
    ]
    
    def __init__(self, calc_obj: Any, n_points: int = 21):
        """
        Initialize with FreeCAD Calc object.
        
        Args:
            calc_obj: FreeCAD calculation object
            n_points: Number of points for array sampling (used for logic, though cached data determines actual points)
        """
        self.calc_obj = calc_obj
        # Import internally to avoid circular dependencies if any
        from .analysis.unified_result_interface import UnifiedResultInterface
        self.interface = UnifiedResultInterface(calc_obj)
        self.n_points = n_points
        self._results_cache = {}
    
    def get_members_dict(self) -> Optional[Dict]:
        """Deprecated: Direct model access removed."""
        return None
    
    def get_load_combos(self) -> List[str]:
        """Get list of available load combinations."""
        # ResultManager stores current results for ONE combo usually.
        # But if we need list, we might need to query object if it stores them.
        # For now, return what's active.
        if hasattr(self.calc_obj, 'LoadCombination'):
             return [self.calc_obj.LoadCombination]
        return ['default']
    
    def get_member_names(self) -> List[str]:
        """Get list of member names."""
        return self.interface.get_all_member_names()
    
    def _get_force_array(self, member_name: str, component: str, combo_name: str) -> Tuple[List, List]:
        """
        Get x positions and force values as arrays.
        
        Returns (x_array, value_array)
        """
        try:
            # Map simplified component names to UnifiedResultInterface names
            comp_map = {
                'Fx': 'Axial',
                'Fy': 'ShearY',
                'Fz': 'ShearZ', 
                'Mx': 'Torque',
                'My': 'MomentY',
                'Mz': 'MomentZ'
            }
            
            uri_comp = comp_map.get(component)
            if not uri_comp:
                return [], []
            
            # Get values from interface
            values = self.interface.get_diagram_data(member_name, uri_comp)
            
            if not values:
                return [], []
                
            # Get X-axis
            x_vals = self.interface.get_diagram_x_axis(member_name, len(values))
            
            return x_vals, values
            
        except Exception as e:
            logger.debug(f"Error getting {component} array for member: {e}")
            return [], []
    
    def _get_force_value(self, member_name: str, component: str, x: float, combo_name: str) -> float:
        """Get force value at a specific position by interpolating diagram data."""
        try:
            x_arr, val_arr = self._get_force_array(member_name, component, combo_name)
            if not x_arr:
                return 0.0
                
            # Simple nearest neighbor or linear interpolation
            # Since we assume x comes from the array, nearest match should be fine
            # But let's be safe
            
            # If x matches exactly
            for i, pos in enumerate(x_arr):
                if abs(pos - x) < 1e-4:
                    return val_arr[i]
            
            # Find closest
            idx = min(range(len(x_arr)), key=lambda i: abs(x_arr[i] - x))
            return val_arr[idx]
            
        except Exception as e:
            logger.debug(f"Error getting {component} at x={x}: {e}")
            return 0.0
    
    def get_all_forces_at_position(self, member_name: str, x: float, combo_name: str) -> Dict[str, float]:
        """Get all force values at a specific position on a member."""
        forces = {}
        for comp, _ in self.FORCE_COMPONENTS:
            forces[comp] = self._get_force_value(member_name, comp, x, combo_name)
        return forces
    
    def find_extremes_for_member(self, member_name: str, combo_name: str) -> List[Dict]:
        """
        Find max and min for each force component in a member.
        
        Returns list of dicts with:
        - type: 'Max Fx', 'Min Fx', etc.
        - member: member name
        - combo: load combination
        - d: distance from end A
        - forces: dict with all force values at that point
        """
        results = []
        
        for component, category in self.FORCE_COMPONENTS:
            x_arr, val_arr = self._get_force_array(member_name, component, combo_name)
            
            if not x_arr or not val_arr:
                continue
            
            # Find max position
            max_idx = argmax(val_arr)
            max_x = x_arr[max_idx]
            max_val = val_arr[max_idx]
            
            # Find min position
            min_idx = argmin(val_arr)
            min_x = x_arr[min_idx]
            min_val = val_arr[min_idx]
            
            # Get all forces at max position
            max_forces = self.get_all_forces_at_position(member_name, max_x, combo_name)
            
            results.append({
                'type': f'Max {component}',
                'category': category,
                'member': member_name,
                'combo': combo_name,
                'd': max_x,
                'value': max_val,
                'forces': max_forces
            })
            
            # Get all forces at min position
            min_forces = self.get_all_forces_at_position(member_name, min_x, combo_name)
            
            results.append({
                'type': f'Min {component}',
                'category': category,
                'member': member_name,
                'combo': combo_name,
                'd': min_x,
                'value': min_val,
                'forces': min_forces
            })
        
        return results
    
    def extract_force_extremes(
        self, 
        load_combos: Optional[List[str]] = None,
        member_names: Optional[List[str]] = None
    ) -> List[Dict]:
        """
        Extract max/min values for each force component.
        
        Args:
            load_combos: Filter by specific load combinations. None = all.
            member_names: Filter by specific members. None = all.
            
        Returns:
            List of result dicts, one per max/min per component
        """
        members = self.get_member_names()
        if not members:
            # logger.warning("No members found in model") 
            return []
        
        # Get all combos if not specified
        if load_combos is None:
            load_combos = self.get_load_combos()
        
        if not load_combos:
            logger.warning("No load combinations found")
            return []
        
        # Get all members if not specified
        if member_names is None:
            member_names = members
        
        all_results = []
        
        for combo in load_combos:
            for name in member_names:
                # if name in members_dict: # Removed dict check
                results = self.find_extremes_for_member(name, combo)
                all_results.extend(results)
        
        return all_results
    
    def find_global_extremes(
        self,
        load_combos: Optional[List[str]] = None,
        member_names: Optional[List[str]] = None
    ) -> Dict[str, Dict]:
        """
        Find the global max/min for each force component across all members.
        
        Returns dict keyed by 'Max Fx', 'Min Fx', etc., with the extreme value info.
        """
        all_results = self.extract_force_extremes(load_combos, member_names)
        
        global_extremes = {}
        
        for result in all_results:
            result_type = result['type']
            
            if result_type.startswith('Max'):
                # Keep record with highest value
                if result_type not in global_extremes:
                    global_extremes[result_type] = result
                elif result['value'] > global_extremes[result_type]['value']:
                    global_extremes[result_type] = result
            else:
                # Min - keep record with lowest value
                if result_type not in global_extremes:
                    global_extremes[result_type] = result
                elif result['value'] < global_extremes[result_type]['value']:
                    global_extremes[result_type] = result
        
        return global_extremes
    
    def get_summary_table_data(
        self,
        load_combos: Optional[List[str]] = None,
        member_names: Optional[List[str]] = None
    ) -> List[List]:
        """
        Get data formatted for table display.
        
        Returns list of rows: [Type, Beam, L/C, d(m), Fx, Fy, Fz, Mx, My, Mz]
        """
        extremes = self.find_global_extremes(load_combos, member_names)
        
        # Order: Max Fx, Min Fx, Max Fy, Min Fy, Max Fz, Min Fz, Max Mx, Min Mx, Max My, Min My, Max Mz, Min Mz
        ordered_types = [
            'Max Fx', 'Min Fx', 
            'Max Fy', 'Min Fy', 
            'Max Fz', 'Min Fz',
            'Max Mx', 'Min Mx', 
            'Max My', 'Min My', 
            'Max Mz', 'Min Mz'
        ]
        
        rows = []
        for t in ordered_types:
            if t in extremes:
                r = extremes[t]
                forces = r.get('forces', {})
                rows.append([
                    t,
                    r.get('member', ''),
                    r.get('combo', ''),
                    r.get('d', 0.0),
                    forces.get('Fx', 0.0),
                    forces.get('Fy', 0.0),
                    forces.get('Fz', 0.0),
                    forces.get('Mx', 0.0),
                    forces.get('My', 0.0),
                    forces.get('Mz', 0.0)
                ])
        
        return rows


def create_member_force_summary(calc_obj) -> Optional[MemberForceSummary]:
    """
    Factory function to create MemberForceSummary from a calc object.
    
    Args:
        calc_obj: FreeCAD Calc object with model attribute
        
    Returns:
        MemberForceSummary instance or None if no model found
    """
    # Just verify the object looks valid (has member results or minimal props)
    if hasattr(calc_obj, 'NameMembers') or hasattr(calc_obj, 'MemberResults'):
        return MemberForceSummary(calc_obj)
    
    return None
