
import json

class ResultManager:
    """
    Manages the extraction and organization of analysis results.
    Separates result parsing from the main calculation logic.
    """
    
    def __init__(self, solver):
        """
        Initialize with a SolverInterface instance.
        """
        self.solver = solver
    
    def prepare_results_for_object(self, obj, active_load_combination, num_points_config=None):
        """
        Extract results from solver and populate the FreeCAD object properties.
        
        Args:
            obj: The FreeCAD object to store results on (Calc object)
            active_load_combination: The load combination to retrieve results for
            num_points_config: Dict with 'moment', 'shear', 'axial', 'deflection', 'torque' point counts
        """
        if num_points_config is None:
            num_points_config = {}
            
        # 0. Set Active info
        if hasattr(obj, 'ActiveLoadCombination'):
             obj.ActiveLoadCombination = active_load_combination
            
        # 1. Collect Reaction Results
        self._collect_reactions(obj, active_load_combination)

        # 1b. Collect Member Lengths (Needed for diagram reconstruction)
        self._collect_member_lengths(obj)
        
        # 2. Collect Member Forces and Deflections (Arrays for diagrams)
        self._collect_member_diagram_data(obj, active_load_combination, num_points_config)
        
        # 3. Collect Member Min/Max Values
        self._collect_member_min_max(obj, active_load_combination)
        
        # 4. Create Structured Member Results (JSON-serializable summary)
        member_results = self._build_member_results_summary(obj, active_load_combination, num_points_config)
        
        # Store structured results on object
        if hasattr(obj, 'MemberResults'):
            obj.MemberResults = member_results
        else:
            try:
                # Attempt to add property if missing (though usually done in init)
                obj.addProperty("App::PropertyPythonObject", "MemberResults", "Calc", "structured per-member results")
                obj.MemberResults = member_results
            except Exception:
                pass


    def _collect_reactions(self, obj, load_combo):
        """Collect reaction forces and moments for supported nodes."""
        reaction_nodes = []
        rx, ry, rz = [], [], []
        rmx, rmy, rmz = [], [], []
        
        node_names = self.solver.get_node_names()
        
        for node_name in node_names:
            reactions = self.solver.get_node_reaction(node_name, load_combo)
            
            # Check if any non-zero reaction exists (or if it's a support)
            # Logic: Pynite only creates Rxn attributes if supported. 
            # SolverInterface.get_node_reaction should return dict of 0.0s if not supported or no reaction.
            # But we want to filter for meaningful reactions or just supported nodes.
            # Ideally we check supports. But generic interface might not expose supports easily yet.
            # Based on calc.py, it iterated nodes and checked `.support_DX` etc.
            # Let's rely on checking non-zero reactions for now? 
            # Or better, we assume SolverInterface provides what is needed.
            # PyniteAdapter returns 0.0 if not found.
            
            # Actually, `calc.py` iterated all nodes and checked `is_supported`.
            # We assume the solver tracks supports. 
            # For now, let's keep it simple: if there are non-zero reactions, store them.
            # OR better: Add `is_node_supported` to SolverInterface?
            
            is_supported = False
            has_nonzero = False
            if reactions:
                for val in reactions.values():
                    if abs(val) > 1e-9:
                        has_nonzero = True
                        break
            
            if reactions and has_nonzero:
                reaction_nodes.append(node_name)
                rx.append(reactions['FX'])
                ry.append(reactions['FY'])
                rz.append(reactions['FZ'])
                rmx.append(reactions['MX'])
                rmy.append(reactions['MY'])
                rmz.append(reactions['MZ'])
                
        obj.ReactionNodes = reaction_nodes
        obj.ReactionX = rx
        obj.ReactionY = ry
        obj.ReactionZ = rz
        obj.ReactionMX = rmx
        obj.ReactionMY = rmy
        obj.ReactionMZ = rmz
        obj.ReactionMY = rmy
        obj.ReactionMZ = rmz
        obj.ReactionLoadCombo = load_combo

    def _collect_member_lengths(self, obj):
        """Collect lengths of all members."""
        lengths = []
        member_names = self.solver.get_member_names()
        for name in member_names:
            length = self.solver.get_member_length(name)
            lengths.append(length)
        
        obj.MemberLengths = lengths
        obj.NameMembers = member_names
        
    def _collect_member_diagram_data(self, obj, load_combo, config):
        """Collect data arrays for diagrams."""
        n_moment = config.get('moment', 5)
        n_shear = config.get('shear', 4)
        n_axial = config.get('axial', 3)
        n_torque = config.get('torque', 3)
        n_defl = config.get('deflection', 4)
        
        momenty, momentz = [], []
        sheary, shearz = [], []
        axial, torque = [], []
        defly, deflz = [], []
        
        member_names = self.solver.get_member_names()
        
        for name in member_names:
            # Forces
            forces = self.solver.get_member_forces(name, load_combo, n_moment) # Reuse max points? No, different arrays.
            # We need standard sizes for specific diagrams as per calc.py defaults
            
            # Re-fetch with specific point counts to match calc.py behavior perfectly?
            # calc.py used:
            # Moment: NumPointsMoment (default 5)
            # Shear: NumPointsShear (default 4)
            # Axial: NumPointsAxial (default 3)
            # Torque: NumPointsTorque (default 3)
            # Deflection: NumPointsDeflection (default 4)
            
            f_moment = self.solver.get_member_forces(name, load_combo, n_moment)
            momenty.append(','.join(str(v) for v in f_moment['momentY']))
            momentz.append(','.join(str(v) for v in f_moment['momentZ']))
            
            f_shear = self.solver.get_member_forces(name, load_combo, n_shear)
            sheary.append(','.join(str(v) for v in f_shear['shearY']))
            shearz.append(','.join(str(v) for v in f_shear['shearZ']))
            
            f_axial = self.solver.get_member_forces(name, load_combo, n_axial)
            axial.append(','.join(str(v) for v in f_axial['axial']))
            
            f_torque = self.solver.get_member_forces(name, load_combo, n_torque)
            torque.append(','.join(str(v) for v in f_torque['torque']))
            
            # Deflections
            dy = self.solver.get_member_deflection(name, load_combo, 'dy', n_defl)
            dz = self.solver.get_member_deflection(name, load_combo, 'dz', n_defl)
            defly.append(','.join(str(v) for v in dy))
            deflz.append(','.join(str(v) for v in dz))
            
        obj.MomentY = momenty
        obj.MomentZ = momentz
        obj.ShearY = sheary
        obj.ShearZ = shearz
        obj.AxialForce = axial
        obj.Torque = torque
        obj.DeflectionY = defly
        obj.DeflectionZ = deflz
        obj.NameMembers = member_names # Also update list of names

    def _collect_member_min_max(self, obj, load_combo):
        """Collect scalar min/max values for members."""
        minMy, maxMy = [], []
        minMz, maxMz = [], []
        minFy, maxFy = [], []
        minFz, maxFz = [], []
        minTq, maxTq = [], []
        # Deflection min/max? generic accessor in SolverInterface needed?
        # Pynite has min_deflection / max_deflection.
        
        member_names = self.solver.get_member_names()
        for name in member_names:
             min_my, max_my = self.solver.get_min_max_forces(name, load_combo, 'My')
             minMy.append(min_my); maxMy.append(max_my)
             
             min_mz, max_mz = self.solver.get_min_max_forces(name, load_combo, 'Mz')
             minMz.append(min_mz); maxMz.append(max_mz)
             
             min_fy, max_fy = self.solver.get_min_max_forces(name, load_combo, 'Fy')
             minFy.append(min_fy); maxFy.append(max_fy)
             
             min_fz, max_fz = self.solver.get_min_max_forces(name, load_combo, 'Fz')
             minFz.append(min_fz); maxFz.append(max_fz)
             
             # Torque and Deflection need explicit support in SolverInterface or we assume get_min_max handles them?
             # Let's add them to PyniteAdapter's get_min_max_forces or add new method.
             # PyniteAdapter.get_min_max_forces currently handles My, Mz, Fy, Fz.
             # We should probably extend it.
             
        obj.MinMomentY = minMy; obj.MaxMomentY = maxMy
        obj.MinMomentZ = minMz; obj.MaxMomentZ = maxMz
        obj.MinShearY = minFy; obj.MaxShearY = maxFy
        obj.MinShearZ = minFz; obj.MaxShearZ = maxFz
        # Skip torque/deflection min/max for now to match interface; add later.

    def _build_member_results_summary(self, obj, load_combo, config):
        """Build structured list of dicts for MemberResults."""
        results = []
        member_names = self.solver.get_member_names()
        
        for name in member_names:
            # We invoke getters again? Optimization: cache this if performance indicates.
            # Ideally ResultManager would fetch once and distribute. 
            # For refactoring phase 1 of ResultManager, simple repeated calls are safer and cleaner.
            
            n_moment = config.get('moment', 3)
            # Fetch minimal data for summary
            
            f_moment = self.solver.get_member_forces(name, load_combo, n_moment)
            f_shear = self.solver.get_member_forces(name, load_combo, n_moment)
            f_axial = self.solver.get_member_forces(name, load_combo, n_moment)
            
            min_my, max_my = self.solver.get_min_max_forces(name, load_combo, 'My')
            min_mz, max_mz = self.solver.get_min_max_forces(name, load_combo, 'Mz')
            
            item = {
                'name': name,
                'momentY': f_moment['momentY'],
                'momentZ': f_moment['momentZ'], 
                'shearY': f_shear['shearY'],
                'shearZ': f_shear['shearZ'],
                'axial': f_axial['axial'],
                'minMomentY': min_my, 'maxMomentY': max_my,
                'minMomentZ': min_mz, 'maxMomentZ': max_mz
            }
            results.append(item)
            
        return results

    def get_max_member_forces(self, member_name, load_combo):
        """
        Get absolute maximum forces for a member, used for design checks.
        Returns dict: {'P': max_axial, 'My': max_moment_y, 'Mz': max_moment_z, ...}
        """
        keys = ['P', 'My', 'Mz', 'Fy', 'Fz']
        forces = {}
        for k in keys:
            min_val, max_val = self.solver.get_min_max_forces(member_name, load_combo, k)
            forces[k] = max(abs(min_val), abs(max_val))
            
        return forces

