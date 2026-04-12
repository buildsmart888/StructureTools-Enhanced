
import math

class ConcreteDesignChecker:
    """
    Performs basic reinforced concrete design checks (ACI 318).
    Calculates flexural capacity for rectangular beams.
    """
    
    def __init__(self, model):
        self.model = model

    def check_member(self, member_name, forces):
        """
        Check a single member (RC).
        forces: dict with keys {'P', 'My', 'Mz', 'Vy', 'Vz'} (Max absolute values)
        Returns:
            ratio (float): Utilization ratio (Mu / phi*Mn)
            details (dict): Calculations
        """
        
        if member_name not in self.model.members:
            return 0.0, {'status': 'Error: Member not found'}
            
        mem = self.model.members[member_name]
        mat_name = mem.material_name
        sec_name = mem.section_name
        
        if mat_name not in self.model.materials or sec_name not in self.model.sections:
             return 0.0, {'status': 'Error: Property not found'}
             
        mat = self.model.materials[mat_name]
        sec = self.model.sections[sec_name]
        
        # 1. Concrete Properties
        # Fc is likely in kPa or similar solver unit (Force/Area)
        fc = getattr(mat, 'Fc', 28000.0) # Default 28 MPa (assumed kPa if using kN/m)
        
        # 2. Section Properties / Geometry
        A = sec.A # Gross Area
        Iz = sec.Iz # Moment of Inertia (Strong Axis)
        
        # Estimate b and h for Rectangular Section (MVP Assumption)
        # h = sqrt(12 * Iz / A)
        # b = A / h
        if A <= 0 or Iz <= 0:
             return 0.0, {'status': 'Error: Invalid Geometry'}
             
        h = math.sqrt(12 * Iz / A)
        b = A / h
        
        # 3. Reinforcement
        # Need As (Bottom/Tension) for Positive Moment
        # Need As' (Top/Tension) for Negative Moment
        # Pynite section might only store one set if simplistic.
        # Let's check both Mz+ and Mz-?
        # For simplicity, we check Absolute Max Moment against RebarAreaBottom (assuming simple span / gravity dominant).
        # TODO: Distinguish Top/Bottom moment checks.
        
        As_bot = getattr(sec, 'RebarAreaBottom', 0.0)
        As_top = getattr(sec, 'RebarAreaTop', 0.0)
        cover = getattr(sec, 'ConcreteCover', 0.040) # 40mm default
        rebar_fy = getattr(sec, 'RebarFy', 420000.0) # 420 MPa default
        
        # Effective depth d
        d = h - cover
        
        if As_bot <= 0:
             # No reinforcement -> Fail or treat as Plain Concrete (very weak)
             # Return High Ratio to indicate "Design Required"
             return 9.99, {'status': 'Error: No Reinforcement Defined', 'phiMn': 0.0}

        # 4. Flexural Capacity (Singly Reinforced Rectangular Section)
        # a = (As * fy) / (0.85 * fc * b)
        # Mn = As * fy * (d - a/2)
        # phi = 0.9 (Tension controlled assumption)
        
        # Check against Strong Axis Moment (Mz)
        # Assuming Mz is the major moment.
        Mz_u = abs(forces.get('Mz', 0.0))
        
        phi = 0.9
        
        # Calculatetion for Bottom Steel (Positive Moment Capacity)
        # Note: If Mz is negative (hogging), we should use As_top.
        # But 'forces' passed here is MAX ABSOLUTE. We don't know sign.
        # Conservative: Check max moment against available steel.
        # Ideally, we check As_bot if Mz > 0, As_top if Mz < 0.
        # MVP: Check against As_bot (assuming simple beam Positive moment is critical).
        # Improvement: Check both if As_top is defined?
        
        # Calculatete 'a' block depth
        # fc is usually concrete strength. 0.85 factor is standard.
        if fc <= 0: fc = 28000.0
        
        a = (As_bot * rebar_fy) / (0.85 * fc * b)
        
        # Check limits
        if a > d: 
            # Over-reinforced section or very small concrete area?
            # Cap 'a' at some limit or flag error?
            # Assuming ductile failure not guaranteed.
            pass
            
        Mn = As_bot * rebar_fy * (d - a/2)
        phi_Mn = phi * Mn
        
        # 5. Ratio
        if phi_Mn > 0:
            ratio = Mz_u / phi_Mn
        else:
            ratio = 9.99
            
        return ratio, {
            'b': b,
            'h': h,
            'd': d,
            'a': a,
            'As': As_bot,
            'fc': fc,
            'fy': rebar_fy,
            'phiMn': phi_Mn,
            'Mu': Mz_u
        }

if __name__ == "__main__":
    pass
