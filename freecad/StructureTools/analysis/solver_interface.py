
class SolverInterface:
    """
    Abstract base class for structural analysis solvers.
    Defines the standard interface that ModelBuilder and ResultManager expect.
    """
    
    # --- Model Definition Methods ---
    
    def add_node(self, name, x, y, z):
        """Add a node to the model at coordinates (x, y, z)."""
        raise NotImplementedError
        
    def add_member(self, name, i_node, j_node, material, section):
        """Add a member element connecting two nodes."""
        raise NotImplementedError
        
    def def_releases(self, member_name, Dxi=False, Dyi=False, Dzi=False, 
                    Rxi=False, Ryi=False, Rzi=False,
                    Dxj=False, Dyj=False, Dzj=False, 
                    Rxj=False, Ryj=False, Rzj=False):
        """Define member end releases (hinges)."""
        raise NotImplementedError

    def add_material(self, name, E, G, nu, rho):
        """Add a material definition."""
        raise NotImplementedError
        
    def add_section(self, name, A, Iy, Iz, J):
        """Add a cross-section definition."""
        raise NotImplementedError

    def add_plate(self, name, i_node, j_node, m_node, n_node, thickness, material):
        """Add a rectangular plate element."""
        raise NotImplementedError

    def add_quad(self, name, i_node, j_node, m_node, n_node, thickness, material):
        """Add a quadrilateral shell element."""
        raise NotImplementedError

    # --- Loading Methods ---
    
    def add_member_dist_load(self, member_name, direction, w1, w2, case='DL'):
        """Add distributed load to a member."""
        raise NotImplementedError
        
    def add_node_load(self, node_name, direction, value, case='DL'):
        """Add nodal load."""
        raise NotImplementedError

    def add_member_self_weight(self, direction, factor):
        """Add self-weight to all members."""
        raise NotImplementedError
        
    def add_plate_surface_pressure(self, plate_name, pressure, case='DL'):
        """Add surface pressure to a plate."""
        raise NotImplementedError
    
    def add_quad_surface_pressure(self, quad_name, pressure, case='DL'):
        """Add surface pressure to a quad element."""
        raise NotImplementedError

    # --- Support Methods ---
    
    def add_quad_surface_pressure(self, quad_name, pressure, case='DL'):
        """Add surface pressure to a quad element."""
        raise NotImplementedError

    # --- Property Access Methods (for builder/checks) ---
    
    def get_material_property(self, material_name, property_name):
        """Get a specific property of a defined material."""
        raise NotImplementedError

    def get_section_property(self, section_name, property_name):
        """Get a specific property of a defined section."""
        raise NotImplementedError

    # --- Support Methods ---

    # --- Analysis Control ---
    
    def add_load_combo(self, name, factors):
        """Add a load combination. factors is a dict {case: factor}."""
        raise NotImplementedError
        
    def clear_load_combos(self):
        """Remove all defined load combinations."""
        raise NotImplementedError
        
    def analyze(self, check_stability=True):
        """Run the analysis."""
        raise NotImplementedError

    # --- Result Access (Generic) ---
    # These methods aim to decouple direct attribute access
    
    def get_node_names(self):
        """Return list of all node names."""
        raise NotImplementedError
        
    def get_member_names(self):
        """Return list of all member names."""
        raise NotImplementedError
        
    def get_node_reaction(self, node_name, load_combo):
        """Return reaction dict {FX, FY, FZ, MX, MY, MZ} for a node and combo."""
        raise NotImplementedError

    def get_member_forces(self, member_name, load_combo, num_points=5):
        """Return internal forces along member."""
        # This returns a structured object or dict standardizing Pynite's arrays
        raise NotImplementedError

    def get_member_deflection(self, member_name, load_combo, direction='dy', num_points=5):
        """Return deflection arrays."""
        raise NotImplementedError

    def get_min_max_forces(self, member_name, load_combo, component='My'):
         """Return min and max values for a component."""
         raise NotImplementedError
