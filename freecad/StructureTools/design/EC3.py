# -*- coding: utf-8 -*-
"""
Eurocode 3 (EN 1993-1-1) Steel Design Implementation

Provides steel member design checking per EN 1993-1-1:2005+A1:2014
including cross-section classification, flexure, shear, compression,
and combined loading interaction checks.

Units: SI (N, mm, MPa) unless otherwise noted.

Reference:
    EN 1993-1-1:2005+A1:2014 — Design of steel structures
"""

import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class EC3DesignApproach(Enum):
    """National Annex design approach."""
    GENERAL = "General"
    UK_NA = "UK National Annex"
    DE_NA = "German National Annex"


class SectionClassification(Enum):
    """EN 1993-1-1 Table 5.2 cross-section class."""
    CLASS_1 = 1  # Plastic design
    CLASS_2 = 2  # Compact
    CLASS_3 = 3  # Semi-compact
    CLASS_4 = 4  # Slender


# ---------------------------------------------------------------------------
# Material
# ---------------------------------------------------------------------------

@dataclass
class EC3SteelMaterial:
    """Steel material per EN 10025."""
    name: str
    fy: float   # Yield strength (MPa) for t ≤ 40 mm
    fu: float   # Ultimate tensile strength (MPa)
    E: float = 210_000.0   # Modulus of elasticity (MPa)
    G: float = 81_000.0    # Shear modulus (MPa)
    nu: float = 0.3        # Poisson's ratio
    density: float = 7850.0  # kg/m³
    gamma_M0: float = 1.00  # Partial factor for resistance (cross-section)
    gamma_M1: float = 1.00  # Partial factor for resistance (buckling)

    @property
    def epsilon(self) -> float:
        """Material factor ε = √(235/fy), used for classification limits."""
        return math.sqrt(235.0 / self.fy)


# Standard steel grades
STEEL_GRADES: Dict[str, EC3SteelMaterial] = {
    'S235': EC3SteelMaterial('S235', fy=235, fu=360),
    'S275': EC3SteelMaterial('S275', fy=275, fu=430),
    'S355': EC3SteelMaterial('S355', fy=355, fu=510),
    'S420': EC3SteelMaterial('S420', fy=420, fu=520),
    'S460': EC3SteelMaterial('S460', fy=460, fu=540),
}


# ---------------------------------------------------------------------------
# Section properties
# ---------------------------------------------------------------------------

@dataclass
class EC3SectionProperties:
    """I/H section properties (SI units: mm, mm², mm⁴, mm³)."""
    name: str
    h: float      # Total depth
    b: float      # Flange width
    tw: float     # Web thickness
    tf: float     # Flange thickness
    r: float      # Root radius
    A: float      # Cross-sectional area (mm²)
    Iy: float     # Second moment of area, strong axis (mm⁴)
    Iz: float     # Second moment of area, weak axis (mm⁴)
    Wpl_y: float  # Plastic section modulus, strong (mm³)
    Wpl_z: float  # Plastic section modulus, weak (mm³)
    Wel_y: float  # Elastic section modulus, strong (mm³)
    Wel_z: float  # Elastic section modulus, weak (mm³)
    It: float     # Torsional constant (mm⁴)
    Iw: float     # Warping constant (mm⁶)
    iy: float = 0.0  # Radius of gyration, strong (mm)
    iz: float = 0.0  # Radius of gyration, weak (mm)

    def __post_init__(self):
        if self.iy == 0 and self.A > 0:
            self.iy = math.sqrt(self.Iy / self.A)
        if self.iz == 0 and self.A > 0:
            self.iz = math.sqrt(self.Iz / self.A)


# ---------------------------------------------------------------------------
# Design forces
# ---------------------------------------------------------------------------

@dataclass
class EC3DesignForces:
    """Factored internal forces for checking."""
    NEd: float = 0.0   # Axial force (N), compression positive
    VEd: float = 0.0   # Shear force (N)
    MyEd: float = 0.0  # Bending moment, strong axis (N·mm)
    MzEd: float = 0.0  # Bending moment, weak axis (N·mm)
    TEd: float = 0.0   # Torsion (N·mm)


# ---------------------------------------------------------------------------
# Design result
# ---------------------------------------------------------------------------

@dataclass
class EC3DesignResult:
    """Result of an EN 1993-1-1 design check."""
    member_name: str
    check_type: str
    clause: str
    demand: float
    capacity: float
    ratio: float
    status: str   # "OK" or "FAIL"
    details: Dict = field(default_factory=dict)

    @property
    def is_acceptable(self) -> bool:
        return self.ratio <= 1.0

    def summary(self) -> str:
        return f"{self.member_name}: {self.check_type} = {self.ratio:.3f} ({self.status}) [{self.clause}]"


# ---------------------------------------------------------------------------
# Cross-section classification (Table 5.2)
# ---------------------------------------------------------------------------

def classify_section(
    section: EC3SectionProperties,
    material: EC3SteelMaterial,
    NEd: float = 0.0,
) -> Dict:
    """Classify an I/H section per EN 1993-1-1 Table 5.2.

    Args:
        section: Section geometric properties.
        material: Steel material.
        NEd: Axial compression (positive) for web classification.

    Returns:
        Dict with 'flange_class', 'web_class', 'section_class', and ratios.
    """
    eps = material.epsilon

    # --- Flange (outstand, Table 5.2 Sheet 2) ---
    c_f = (section.b - section.tw - 2 * section.r) / 2.0
    cf_tf = c_f / section.tf

    if cf_tf <= 9 * eps:
        flange_class = SectionClassification.CLASS_1
    elif cf_tf <= 10 * eps:
        flange_class = SectionClassification.CLASS_2
    elif cf_tf <= 14 * eps:
        flange_class = SectionClassification.CLASS_3
    else:
        flange_class = SectionClassification.CLASS_4

    # --- Web (internal, Table 5.2 Sheet 1) ---
    c_w = section.h - 2 * section.tf - 2 * section.r
    cw_tw = c_w / section.tw

    # Determine stress ratio α for combined bending + compression
    if NEd <= 0:
        # Pure bending
        if cw_tw <= 72 * eps:
            web_class = SectionClassification.CLASS_1
        elif cw_tw <= 83 * eps:
            web_class = SectionClassification.CLASS_2
        elif cw_tw <= 124 * eps:
            web_class = SectionClassification.CLASS_3
        else:
            web_class = SectionClassification.CLASS_4
    else:
        # Pure compression
        if cw_tw <= 33 * eps:
            web_class = SectionClassification.CLASS_1
        elif cw_tw <= 38 * eps:
            web_class = SectionClassification.CLASS_2
        elif cw_tw <= 42 * eps:
            web_class = SectionClassification.CLASS_3
        else:
            web_class = SectionClassification.CLASS_4

    # Governing class
    section_class = max(flange_class, web_class, key=lambda c: c.value)

    return {
        'flange_class': flange_class,
        'web_class': web_class,
        'section_class': section_class,
        'cf_tf': cf_tf,
        'cw_tw': cw_tw,
        'epsilon': eps,
    }


# ---------------------------------------------------------------------------
# Resistance checks
# ---------------------------------------------------------------------------

class EC3DesignCode:
    """EN 1993-1-1 steel design checker.

    Provides member resistance checks for I/H sections covering:
        - Cross-section resistance in bending (§6.2.5)
        - Cross-section resistance in shear (§6.2.6)
        - Cross-section resistance in compression (§6.2.4)
        - Flexural buckling (§6.3.1)
        - Lateral-torsional buckling (§6.3.2)
        - Combined bending and compression (§6.3.3)
    """

    def __init__(self, approach: EC3DesignApproach = EC3DesignApproach.GENERAL):
        self.approach = approach

    # --- Cross-section: Bending (§6.2.5) ---
    def check_bending(
        self,
        section: EC3SectionProperties,
        material: EC3SteelMaterial,
        forces: EC3DesignForces,
    ) -> EC3DesignResult:
        """Bending resistance check per §6.2.5."""
        cls_info = classify_section(section, material, forces.NEd)
        cls = cls_info['section_class']

        if cls.value <= 2:
            Mc_Rd = material.fy * section.Wpl_y / material.gamma_M0
        elif cls == SectionClassification.CLASS_3:
            Mc_Rd = material.fy * section.Wel_y / material.gamma_M0
        else:
            # Class 4 — effective section (simplified)
            Mc_Rd = material.fy * section.Wel_y * 0.85 / material.gamma_M0

        MEd = abs(forces.MyEd)
        ratio = MEd / Mc_Rd if Mc_Rd > 0 else float('inf')

        return EC3DesignResult(
            member_name=section.name,
            check_type="Bending (§6.2.5)",
            clause="6.2.5",
            demand=MEd,
            capacity=Mc_Rd,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'class': cls.value, 'Mc_Rd': Mc_Rd},
        )

    # --- Cross-section: Shear (§6.2.6) ---
    def check_shear(
        self,
        section: EC3SectionProperties,
        material: EC3SteelMaterial,
        forces: EC3DesignForces,
    ) -> EC3DesignResult:
        """Shear resistance check per §6.2.6."""
        # Shear area for rolled I/H section
        hw = section.h - 2 * section.tf
        Av = max(section.A - 2 * section.b * section.tf + (section.tw + 2 * section.r) * section.tf,
                 1.0 * hw * section.tw)

        Vpl_Rd = Av * (material.fy / math.sqrt(3)) / material.gamma_M0

        VEd = abs(forces.VEd)
        ratio = VEd / Vpl_Rd if Vpl_Rd > 0 else float('inf')

        return EC3DesignResult(
            member_name=section.name,
            check_type="Shear (§6.2.6)",
            clause="6.2.6",
            demand=VEd,
            capacity=Vpl_Rd,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'Av': Av, 'Vpl_Rd': Vpl_Rd},
        )

    # --- Flexural buckling (§6.3.1) ---
    def check_flexural_buckling(
        self,
        section: EC3SectionProperties,
        material: EC3SteelMaterial,
        forces: EC3DesignForces,
        Lcr_y: float = 0.0,
        Lcr_z: float = 0.0,
        buckling_curve_y: str = 'a',
        buckling_curve_z: str = 'b',
    ) -> EC3DesignResult:
        """Flexural buckling resistance per §6.3.1.

        Args:
            Lcr_y, Lcr_z: Buckling lengths about y and z axes (mm).
            buckling_curve_y, buckling_curve_z: EC3 buckling curve (a0/a/b/c/d).
        """
        NEd = abs(forces.NEd)

        # Imperfection factors (Table 6.1)
        alpha_map = {'a0': 0.13, 'a': 0.21, 'b': 0.34, 'c': 0.49, 'd': 0.76}

        results = {}
        for axis, Lcr, i_r, curve in [
            ('y', Lcr_y, section.iy, buckling_curve_y),
            ('z', Lcr_z, section.iz, buckling_curve_z),
        ]:
            if Lcr <= 0 or i_r <= 0:
                results[axis] = float('inf')
                continue

            lambda_bar = (Lcr / i_r) / (math.pi * math.sqrt(material.E / material.fy))
            alpha_imp = alpha_map.get(curve, 0.34)

            phi = 0.5 * (1 + alpha_imp * (lambda_bar - 0.2) + lambda_bar ** 2)
            chi = 1.0 / (phi + math.sqrt(phi ** 2 - lambda_bar ** 2))
            chi = min(chi, 1.0)

            Nb_Rd = chi * section.A * material.fy / material.gamma_M1
            results[axis] = Nb_Rd

        # Governing
        Nb_Rd_min = min(results.values())
        ratio = NEd / Nb_Rd_min if Nb_Rd_min > 0 else float('inf')

        return EC3DesignResult(
            member_name=section.name,
            check_type="Flexural Buckling (§6.3.1)",
            clause="6.3.1",
            demand=NEd,
            capacity=Nb_Rd_min,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'Nb_Rd_y': results.get('y'), 'Nb_Rd_z': results.get('z')},
        )

    # --- Lateral-torsional buckling (§6.3.2) ---
    def check_ltb(
        self,
        section: EC3SectionProperties,
        material: EC3SteelMaterial,
        forces: EC3DesignForces,
        Lcr: float = 0.0,
        C1: float = 1.0,
        ltb_curve: str = 'b',
    ) -> EC3DesignResult:
        """Lateral-torsional buckling per §6.3.2.

        Args:
            Lcr: Lateral buckling length (mm).
            C1: Moment distribution factor.
            ltb_curve: LTB buckling curve (a/b/c/d).
        """
        MEd = abs(forces.MyEd)
        cls_info = classify_section(section, material, forces.NEd)
        cls = cls_info['section_class']

        if cls.value <= 2:
            Wy = section.Wpl_y
        else:
            Wy = section.Wel_y

        if Lcr <= 0:
            Mb_Rd = Wy * material.fy / material.gamma_M1
        else:
            # Elastic critical moment (Mcr) — simplified formula
            kw = 1.0  # warping factor
            kz = 1.0  # end restraint
            zg = 0.0  # load application point offset

            Mcr = (C1 * math.pi ** 2 * material.E * section.Iz / (kz * Lcr) ** 2 *
                   math.sqrt(
                       (kz / kw) ** 2 * section.Iw / section.Iz +
                       (kz * Lcr) ** 2 * material.G * section.It / (math.pi ** 2 * material.E * section.Iz)
                   ))

            lambda_LT = math.sqrt(Wy * material.fy / Mcr) if Mcr > 0 else 10.0

            alpha_map = {'a': 0.21, 'b': 0.34, 'c': 0.49, 'd': 0.76}
            alpha_LT = alpha_map.get(ltb_curve, 0.34)

            phi_LT = 0.5 * (1 + alpha_LT * (lambda_LT - 0.2) + lambda_LT ** 2)
            chi_LT = 1.0 / (phi_LT + math.sqrt(max(phi_LT ** 2 - lambda_LT ** 2, 0)))
            chi_LT = min(chi_LT, 1.0)

            Mb_Rd = chi_LT * Wy * material.fy / material.gamma_M1

        ratio = MEd / Mb_Rd if Mb_Rd > 0 else float('inf')

        return EC3DesignResult(
            member_name=section.name,
            check_type="LTB (§6.3.2)",
            clause="6.3.2",
            demand=MEd,
            capacity=Mb_Rd,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'Mb_Rd': Mb_Rd},
        )

    # --- Combined bending + compression (§6.3.3, Eq 6.61/6.62) ---
    def check_combined(
        self,
        section: EC3SectionProperties,
        material: EC3SteelMaterial,
        forces: EC3DesignForces,
        Lcr_y: float = 0.0,
        Lcr_z: float = 0.0,
        Lcr_LT: float = 0.0,
        buckling_curve_y: str = 'a',
        buckling_curve_z: str = 'b',
        ltb_curve: str = 'b',
        Cmy: float = 0.9,
        Cmz: float = 0.9,
    ) -> EC3DesignResult:
        """Combined bending + axial per §6.3.3 Equations 6.61 and 6.62."""
        NEd = abs(forces.NEd)
        MyEd = abs(forces.MyEd)
        MzEd = abs(forces.MzEd)

        # Get individual capacities
        buck = self.check_flexural_buckling(
            section, material, EC3DesignForces(NEd=forces.NEd),
            Lcr_y, Lcr_z, buckling_curve_y, buckling_curve_z,
        )
        ltb = self.check_ltb(
            section, material, EC3DesignForces(MyEd=forces.MyEd),
            Lcr_LT, ltb_curve=ltb_curve,
        )

        NRk = section.A * material.fy
        MyRk = section.Wpl_y * material.fy
        MzRk = section.Wpl_z * material.fy

        chi_y_Nb = buck.details.get('Nb_Rd_y', NRk)
        chi_z_Nb = buck.details.get('Nb_Rd_z', NRk)
        chi_y = chi_y_Nb * material.gamma_M1 / NRk if NRk > 0 else 1.0
        chi_z = chi_z_Nb * material.gamma_M1 / NRk if NRk > 0 else 1.0
        chi_LT = ltb.capacity * material.gamma_M1 / MyRk if MyRk > 0 else 1.0

        # Interaction factors (simplified Method 2, Annex B)
        kyy = Cmy * (1 + 0.6 * NEd / (chi_y * NRk / material.gamma_M1))
        kyy = min(kyy, Cmy * (1 + 0.6))
        kzz = Cmz * (1 + 0.6 * NEd / (chi_z * NRk / material.gamma_M1))
        kzz = min(kzz, Cmz * (1 + 0.6))
        kyz = 0.6 * kzz
        kzy = 0.6 * kyy

        gM1 = material.gamma_M1

        # Eq 6.61
        eq_661 = (NEd / (chi_y * NRk / gM1) +
                  kyy * MyEd / (chi_LT * MyRk / gM1) +
                  kyz * MzEd / (MzRk / gM1))

        # Eq 6.62
        eq_662 = (NEd / (chi_z * NRk / gM1) +
                  kzy * MyEd / (chi_LT * MyRk / gM1) +
                  kzz * MzEd / (MzRk / gM1))

        ratio = max(eq_661, eq_662)

        return EC3DesignResult(
            member_name=section.name,
            check_type="Combined (§6.3.3)",
            clause="6.3.3",
            demand=ratio,
            capacity=1.0,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'eq_6.61': eq_661, 'eq_6.62': eq_662,
                     'kyy': kyy, 'kzz': kzz, 'kyz': kyz, 'kzy': kzy},
        )

    # --- Report ---
    def generate_report(self, results: List[EC3DesignResult], project_info: Dict = None) -> str:
        """Generate EN 1993-1-1 design report."""
        lines = [
            "=" * 70,
            "EN 1993-1-1 STEEL DESIGN REPORT",
            "=" * 70,
            f"Approach: {self.approach.value}",
            "",
        ]
        if project_info:
            for k, v in project_info.items():
                lines.append(f"{k}: {v}")
            lines.append("")

        total = len(results)
        passing = sum(1 for r in results if r.is_acceptable)
        lines.extend([
            f"Members checked: {total}",
            f"Passing: {passing} / {total}",
            "",
        ])

        for r in results:
            lines.append(r.summary())
        lines.append("=" * 70)
        return "\n".join(lines)
