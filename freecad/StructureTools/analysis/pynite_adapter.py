
try:
    from ..Pynite_main.FEModel3D import FEModel3D
except ImportError:
    # Fallback for standalone tests where Pynite might not be in the expected relative path
    try:
        from StructureTools.Pynite_main.FEModel3D import FEModel3D
    except ImportError:
        # Last resort - mock for testing if real Pynite isn't found
        FEModel3D = None

from .solver_interface import SolverInterface

class PyniteAdapter(SolverInterface):
    """
    Adapter for the Pynite FEA solver.
    """
    
    def __init__(self, model=None):
        if FEModel3D is None and model is None:
            raise ImportError("Pynite FEModel3D could not be imported")
        
        if model is not None:
            self.model = model
        else:
            self.model = FEModel3D()
        
    def add_node(self, name, x, y, z):
        return self.model.add_node(name, x, y, z)
        
    def add_member(self, name, i_node, j_node, material, section):
        return self.model.add_member(name, i_node, j_node, material, section)
        
    def def_releases(self, member_name, **kwargs):
        # Pynite uses Dxi, Dyi, etc. Match kwargs directly or map them
        return self.model.def_releases(member_name, **kwargs)

    def add_material(self, name, E, G, nu, rho):
        return self.model.add_material(name, E, G, nu, rho)
        
    def add_section(self, name, A, Iy, Iz, J):
        return self.model.add_section(name, A, Iy, Iz, J)
        
    def add_plate(self, name, i_node, j_node, m_node, n_node, thickness, material):
        return self.model.add_plate(name, i_node, j_node, m_node, n_node, thickness, material)

    def add_quad(self, name, i_node, j_node, m_node, n_node, thickness, material):
        return self.model.add_quad(name, i_node, j_node, m_node, n_node, thickness, material)
        
    def add_member_dist_load(self, member_name, direction, w1, w2, case='DL'):
        return self.model.add_member_dist_load(member_name, direction, w1, w2, case)
        
    def add_node_load(self, node_name, direction, value, case='DL'):
        return self.model.add_node_load(node_name, direction, value, case)

    def add_member_self_weight(self, direction, factor):
        # Pynite has this method
        return self.model.add_member_self_weight(direction, factor)
        
    def add_plate_surface_pressure(self, plate_name, pressure, case='DL'):
        return self.model.add_plate_surface_pressure(plate_name, pressure, case)
    
    def add_quad_surface_pressure(self, quad_name, pressure, case='DL'):
        return self.model.add_quad_surface_pressure(quad_name, pressure, case)

    def get_material_property(self, material_name, property_name):
        if material_name in self.model.materials:
            mat = self.model.materials[material_name]
            if hasattr(mat, property_name):
                return getattr(mat, property_name)
        return None

    def get_section_property(self, section_name, property_name):
        if section_name in self.model.sections:
            sec = self.model.sections[section_name]
            if hasattr(sec, property_name):
                return getattr(sec, property_name)
        return None
        
    def def_support(self, node_name, u1, u2, u3, r1, r2, r3):
        return self.model.def_support(node_name, u1, u2, u3, r1, r2, r3)

    def add_load_combo(self, name, factors):
        self.model.add_load_combo(name, factors)
        
    def clear_load_combos(self):
        # Pynite stores combos in a dict
        if hasattr(self.model, 'load_combos'):
            self.model.load_combos.clear()
            
    def analyze(self, check_stability=True):
        self.model.analyze(check_stability=check_stability)

    # --- Result Accessors ---
    
    def get_node_names(self):
        return list(self.model.nodes.keys())
        
    def get_member_names(self):
        return list(self.model.members.keys())

    def get_member_length(self, member_name):
        if member_name not in self.model.members:
            return 0.0
        return self.model.members[member_name].L()
        
    def get_node_reaction(self, node_name, load_combo):
        if node_name not in self.model.nodes:
            return None
        node = self.model.nodes[node_name]
        
        # Helper to safe get
        def get_val(attr_name):
            if hasattr(node, attr_name) and load_combo in getattr(node, attr_name):
                return getattr(node, attr_name)[load_combo]
            return 0.0
            
        return {
            'FX': get_val('RxnFX'),
            'FY': get_val('RxnFY'), 
            'FZ': get_val('RxnFZ'),
            'MX': get_val('RxnMX'),
            'MY': get_val('RxnMY'),
            'MZ': get_val('RxnMZ')
        }

    def get_member_forces(self, member_name, load_combo, num_points=5):
        if member_name not in self.model.members:
            return None
        member = self.model.members[member_name]
        
        # Pynite returns tuple (x_vals, y_vals)
        try:
            return {
                'axial': member.axial_array(num_points, load_combo)[1],
                'shearY': member.shear_array('Fy', num_points, load_combo)[1],
                'shearZ': member.shear_array('Fz', num_points, load_combo)[1],
                'momentY': member.moment_array('My', num_points, load_combo)[1],
                'momentZ': member.moment_array('Mz', num_points, load_combo)[1],
                'torque': member.torque_array(num_points, load_combo)[1]
            }
        except Exception:
            # Return zeros if calculation fails
            zeros = [0.0]*num_points
            return {k: zeros for k in ['axial', 'shearY', 'shearZ', 'momentY', 'momentZ', 'torque']}

    def get_member_deflection(self, member_name, load_combo, direction='dy', num_points=5):
         if member_name not in self.model.members:
            return None
         member = self.model.members[member_name]
         try:
             return member.deflection_array(direction, num_points, load_combo)[1]
         except Exception:
             return [0.0]*num_points

    def get_min_max_forces(self, member_name, load_combo, component='My'):
        if member_name not in self.model.members:
            return 0.0, 0.0
        member = self.model.members[member_name]
        
        try:
            if component == 'My':
                return member.min_moment('My', load_combo), member.max_moment('My', load_combo)
            elif component == 'Mz':
                return member.min_moment('Mz', load_combo), member.max_moment('Mz', load_combo)
            elif component == 'Fy':
                return member.min_shear('Fy', load_combo), member.max_shear('Fy', load_combo)
            elif component == 'Fz':
                return member.min_shear('Fz', load_combo), member.max_shear('Fz', load_combo)
            # ... others
        except Exception:
            return 0.0, 0.0
        return 0.0, 0.0
