
from typing import Dict, List, Optional, Tuple, Any

class UnifiedResultInterface:
    """
    Abstracts access to analysis results for UI panels and reports.
    Decouples the UI from the specific storage mechanism (FreeCAD properties, JSON, etc.)
    """
    
    def __init__(self, calc_obj):
        """
        Initialize with the FreeCAD Calc object containing results.
        
        Args:
            calc_obj: The FreeCAD document object with result properties
        """
        self.calc_obj = calc_obj
        self.calc_obj = calc_obj
        self._member_results_cache = {}
        self._solver_adapter = None
        self._result_manager = None
        
        # Initialize internal ResultManager if model is available on object
        # This allows accessing non-stored results (like other load combos)
        # Check standard locations for model
        model = None
        if hasattr(calc_obj, 'model') and calc_obj.model:
            model = calc_obj.model
        elif hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            model = calc_obj.FEModel
        elif hasattr(calc_obj, 'Proxy') and hasattr(calc_obj.Proxy, 'model') and calc_obj.Proxy.model:
            model = calc_obj.Proxy.model

        if model:
            try:
                from .pynite_adapter import PyniteAdapter
                from .result_manager import ResultManager
                self._solver_adapter = PyniteAdapter(model)
                self._result_manager = ResultManager(self._solver_adapter)
            except ImportError:
                pass
        
    def get_load_combinations(self) -> List[str]:
        """Get list of available load combinations."""
        # Method 1: Get from dynamic model if available
        if self._solver_adapter:
            # SolverInterface doesn't strictly expose get_load_combos (PyniteAdapter does via model)
            # But let's check PyniteAdapter specific methods or add to interface
             if hasattr(self._solver_adapter, 'model') and hasattr(self._solver_adapter.model, 'load_combos'):
                 return list(self._solver_adapter.model.load_combos.keys())

        # Method 2: Get from calc object properties
        if hasattr(self.calc_obj, 'LoadCombination'):
             val = self.calc_obj.LoadCombination
             if isinstance(val, list):
                 return val
             return [str(val)]
             
        # Method 3: Fallback default
        if hasattr(self.calc_obj, 'ActiveLoadCombination') and self.calc_obj.ActiveLoadCombination:
             return [self.calc_obj.ActiveLoadCombination]
             
        return []

    def get_all_member_names(self) -> List[str]:
        """Get list of all member names in the model."""
        if hasattr(self.calc_obj, 'NameMembers'):
            return self.calc_obj.NameMembers
        return []

    def get_member_results(self, member_name: str) -> Optional[Dict[str, Any]]:
        """
        Get structured results for a specific member.
        Returns None if member not found.
        """
        # Try retrieving from MemberResults property (list of dicts)
        if hasattr(self.calc_obj, 'MemberResults'):
            # This search could be slow for many members; caching recommended if persistent
            # Check cache first (though calc_obj might change, so minimal caching)
            
            # Simple linear search for now, assuming MemberResults is a list of dicts
            results = self.calc_obj.MemberResults
            if results:
                for res in results:
                    if res.get('name') == member_name:
                        return res
        return None

    def get_diagram_data(self, member_name: str, component: str) -> List[float]:
        """
        Get numeric data array for plotting diagrams.
        
        Args:
            member_name: Name of the member
            component: 'MomentY', 'MomentZ', 'ShearY', 'ShearZ', 'Axial', 'Torque', 'DeflectionY', 'DeflectionZ'
        """
        # Get index of member
        try:
            members = self.calc_obj.NameMembers
            idx = members.index(member_name)
        except (ValueError, AttributeError):
            return []
            
        # Map component string to property name
        prop_map = {
            'MomentY': 'MomentY',
            'MomentZ': 'MomentZ',
            'ShearY': 'ShearY',
            'ShearZ': 'ShearZ',
            'Axial': 'AxialForce',
            'Torque': 'Torque',
            'DeflectionY': 'DeflectionY',
            'DeflectionZ': 'DeflectionZ'
        }
        
        prop_name = prop_map.get(component)
        if not prop_name or not hasattr(self.calc_obj, prop_name):
            return []
            
        # Get raw string data (comma separated)
        raw_list = getattr(self.calc_obj, prop_name)
        if idx < len(raw_list):
            raw_data = raw_list[idx]
            try:
                # Convert "1.0, 2.0, ..." to [1.0, 2.0, ...]
                return [float(x) for x in raw_data.split(',')]
            except ValueError:
                return []
        
        return []

    def get_member_length(self, member_name: str) -> float:
        """Get the length of a member."""
        try:
            members = self.calc_obj.NameMembers
            idx = members.index(member_name)
            
            if hasattr(self.calc_obj, 'MemberLengths'):
                lengths = self.calc_obj.MemberLengths
                if idx < len(lengths):
                    return lengths[idx]
            
            # Fallback to MemberResults if lengths not stored directly
            res = self.get_member_results(member_name)
            if res and 'length' in res:
                return res['length']
                
            return 0.0
        except (ValueError, AttributeError):
            return 0.0

    def get_diagram_x_axis(self, member_name: str, num_points: int) -> List[float]:
        """
        Get X-axis positions (local distance along member) for diagrams.
        Assumes equal spacing based on member length.
        """
        length = self.get_member_length(member_name)
        if length <= 0 or num_points <= 1:
            return []
            
        step = length / (num_points - 1)
        return [i * step for i in range(num_points)]

    def get_min_max_values(self, member_name: str) -> Dict[str, Tuple[float, float]]:
        """
        Get min/max envelope values for a member.
        Returns dict with keys 'MomentY', 'MomentZ', etc. containing (min, max) tuples.
        """
        # Get index
        try:
            members = self.calc_obj.NameMembers
            idx = members.index(member_name)
        except (ValueError, AttributeError):
            return {}
            
        components = ['MomentY', 'MomentZ', 'ShearY', 'ShearZ'] # Add others as needed
        envelope = {}
        
        for comp in components:
            min_prop = f"Min{comp}"
            max_prop = f"Max{comp}"
            
            if hasattr(self.calc_obj, min_prop) and hasattr(self.calc_obj, max_prop):
                min_list = getattr(self.calc_obj, min_prop)
                max_list = getattr(self.calc_obj, max_prop)
                
                if idx < len(min_list) and idx < len(max_list):
                    envelope[comp] = (min_list[idx], max_list[idx])
                else:
                    envelope[comp] = (0.0, 0.0)
                    
        return envelope

        return envelope

    def get_reaction_node_names(self, load_combo: Optional[str] = None) -> List[str]:
        """Get names of nodes that have reactions."""
        # Case 1: Stored properties (Active Combo)
        active_combo = getattr(self.calc_obj, 'ReactionLoadCombo', None)
        use_stored = (load_combo is None) or (active_combo and load_combo == active_combo)
        
        if use_stored and hasattr(self.calc_obj, 'ReactionNodes'):
            return self.calc_obj.ReactionNodes
            
        # Case 2: Dynamic - Scan model (Expensive but necessary if switching combos)
        if self._solver_adapter:
            # We must iterate all nodes and check for reactions
            valid_nodes = []
            all_nodes = self._solver_adapter.get_node_names()
            for name in all_nodes:
                rxn = self._solver_adapter.get_node_reaction(name, load_combo)
                # Check for non-zero
                if rxn and any(abs(v) > 1e-9 for v in rxn.values()):
                    valid_nodes.append(name)
            return valid_nodes
            
        return []

    def get_node_coordinates(self, node_name: str) -> Tuple[float, float, float]:
        """Get (x, y, z) coordinates of a node."""
        # 1. Try dynamic model first (most reliable for geometry)
        if self._solver_adapter:
             if hasattr(self._solver_adapter, 'model') and self._solver_adapter.model:
                 if node_name in self._solver_adapter.model.nodes:
                     n = self._solver_adapter.model.nodes[node_name]
                     return (n.X, n.Y, n.Z)
        
        # 2. Try parsing from legacy properties if available? 
        # StructureTools usually doesn't store Node coords as simple lists on calc_obj
        # But maybe we can find it in 'Nodes' property if it's a list of objects?
        # Usually calc_obj.Nodes is the input property.
        
        # Try finding in Nodes input dictionary/list
        if hasattr(self.calc_obj, 'Nodes'): # Often a dict or list for input
             nodes = self.calc_obj.Nodes
             if isinstance(nodes, dict) and node_name in nodes:
                 # It might be a dict of coords or objects
                 n = nodes[node_name]
                 if hasattr(n, 'X'): return (n.X, n.Y, n.Z) # Object
                 if isinstance(n, (list, tuple)) and len(n) >= 3: return (n[0], n[1], n[2])
                 
        return (0.0, 0.0, 0.0)

    def get_reactions_for_node(self, node_name: str, load_combo: Optional[str] = None) -> Dict[str, float]:
        """
        Get reactions for a specific node.
        Returns {'FX': val, 'FY': val, ...} or empty dict if no reaction.
        """
        # Case 1: Active load combo matches stored results (or no combo specified)
        active_combo = None
        if hasattr(self.calc_obj, 'ReactionLoadCombo'):
            active_combo = self.calc_obj.ReactionLoadCombo
            
        use_stored = False
        if load_combo is None:
            use_stored = True
        elif active_combo and load_combo == active_combo:
            use_stored = True
            
        if use_stored and hasattr(self.calc_obj, 'ReactionNodes'):
            try:
                nodes = self.calc_obj.ReactionNodes
                if node_name in nodes:
                    idx = nodes.index(node_name)
                    
                    reactions = {}
                    map_keys = {'ReactionX': 'FX', 'ReactionY': 'FY', 'ReactionZ': 'FZ',
                               'ReactionMX': 'MX', 'ReactionMY': 'MY', 'ReactionMZ': 'MZ'}
                               
                    for prop, key in map_keys.items():
                        if hasattr(self.calc_obj, prop):
                            vals = getattr(self.calc_obj, prop)
                            if idx < len(vals):
                                reactions[key] = vals[idx]
                    return reactions
            except (ValueError, AttributeError):
                pass
        
        # Case 2: Specific combo requested, query solver directly if available
        if self._solver_adapter and load_combo:
            reactions = self._solver_adapter.get_node_reaction(node_name, load_combo)
            # Only return if non-zero? PyniteAdapter returns dict of zeros if no reaction
            # The interface implies returning only relevant reactions? 
            # Original code filtered for supported nodes.
            # But get_node_reaction returns values for ANY node.
            # If we want to mimic "is supported", we might need that check.
            # But here we return values.
            return reactions if reactions else {}

        return {}
