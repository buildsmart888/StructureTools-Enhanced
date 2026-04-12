import math

class SteelDesignChecker:
    """
    Performs basic steel design checks (ASD).
    Calculates stress ratios for members based on internal forces and capacity.
    """
    
    def __init__(self, model):
        self.model = model

    def check_member(self, member_name, forces):
        """
        Check a single member.
        forces: dict with keys {'P', 'My', 'Mz', 'Vy', 'Vz'} (Max absolute values)
        Returns:
            ratio (float): Interaction ratio (Demand/Capacity)
            details (dict): Breakdown of ratio (axial, bending, etc.)
        """
        
        # 1. Get Member, Material, Section
        if member_name not in self.model.members:
            return 0.0, {'status': 'Error: Member not found'}
            
        mem = self.model.members[member_name]
        mat_name = mem.material_name
        sec_name = mem.section_name
        
        if mat_name not in self.model.materials or sec_name not in self.model.sections:
             return 0.0, {'status': 'Error: Property not found'}
             
        mat = self.model.materials[mat_name]
        sec = self.model.sections[sec_name]
        
        # 2. Get Properties
        # Yield Strength passed from ModelBuilder (in Solver Units)
        Fy = getattr(mat, 'Fy', 250000.0) # Default ~250 MPa (assuming units are consistent)
        
        A = sec.A
        
        # Mapping FreeCAD S to Solver Axes
        # Based on ModelBuilder mapping:
        # FreeCAD Y (Horizontal) -> Solver Z
        # FreeCAD Z (Vertical) -> Solver Y
        # So Solver Mz checks against S about Z (Horizontal) -> Sy_freecad
        # Solver My checks against S about Y (Vertical) -> Sz_freecad
        
        Sx_solver = getattr(sec, 'Sy_freecad', 0.0) # Mz capacity (Strong axis usually)
        Sy_solver = getattr(sec, 'Sz_freecad', 0.0) # My capacity (Weak axis usually)
        
        # Fallback estimation if zero
        # Note: This is rough and assumes I ~ S * (d/2). using sqrt(A) as proxy for d/2 is weak but better than 0.
        if Sx_solver == 0 and sec.Iz > 0:
            Sx_solver = sec.Iz / (math.sqrt(A) * 0.5) if A > 0 else 0
            
        if Sy_solver == 0 and sec.Iy > 0:
            Sy_solver = sec.Iy / (math.sqrt(A) * 0.5) if A > 0 else 0

        # 3. Capacities (Simplified ASD)
        # Tensile/Compressive Pn = 0.6 * Fy * A
        Pn = 0.6 * Fy * A
        
        # Bending Mn = 0.66 * Fy * S (Compact)
        Mn_z = 0.66 * Fy * Sx_solver
        Mn_y = 0.66 * Fy * Sy_solver

        # 4. Demand
        Pu = abs(forces.get('P', 0.0))
        Mu_z = abs(forces.get('Mz', 0.0))
        Mu_y = abs(forces.get('My', 0.0))
        
        # 5. Ratios
        ratio_axial = Pu / Pn if Pn > 0 else 0.0
        ratio_bend_z = Mu_z / Mn_z if Mn_z > 0 else 0.0
        ratio_bend_y = Mu_y / Mn_y if Mn_y > 0 else 0.0
        
        # Simplified Interaction (Sum)
        ratio = ratio_axial + ratio_bend_z + ratio_bend_y
        
        # 6. Return
        return ratio, {
            'axial': ratio_axial,
            'bending_z': ratio_bend_z,
            'bending_y': ratio_bend_y,
            'Pn': Pn,
            'Mn_z': Mn_z,
            'Mn_y': Mn_y
        }
