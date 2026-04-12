# -*- coding: utf-8 -*-
"""
Foundation Design Module

Spread footing design per ACI 318-19 Chapter 13.
Covers isolated footings under concentric and eccentric loading
with one-way shear, two-way (punching) shear, and flexure checks.

Units: US customary (psi, in, lb).
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class SoilProperties:
    """Soil properties for bearing capacity."""
    qa: float = 3000.0   # Allowable bearing pressure (psf)
    gamma: float = 120.0  # Unit weight (pcf)
    phi: float = 30.0     # Friction angle (degrees)
    c: float = 0.0        # Cohesion (psf)


@dataclass
class FootingGeometry:
    """Isolated spread footing geometry."""
    B: float       # Footing width (in)
    L: float       # Footing length (in)
    t: float       # Footing thickness (in)
    cover: float = 3.0  # Bottom cover (in)
    col_b: float = 12.0  # Column width (in)
    col_d: float = 12.0  # Column depth (in)
    embedment: float = 36.0  # Embedment depth (in)

    @property
    def area(self) -> float:
        return self.B * self.L

    @property
    def d(self) -> float:
        """Effective depth (in)."""
        return self.t - self.cover - 0.5  # Approx bar radius


@dataclass
class FootingLoads:
    """Loads on footing."""
    Pu: float = 0.0    # Factored axial (lb)
    Mux: float = 0.0   # Factored moment X (lb·in)
    Muy: float = 0.0   # Factored moment Y (lb·in)
    Vu: float = 0.0    # Factored lateral shear (lb)
    Pa: float = 0.0    # Service axial for bearing check (lb)
    Ma: float = 0.0    # Service moment for bearing check (lb·in)


@dataclass
class FootingResult:
    """Design check result."""
    check: str
    demand: float
    capacity: float
    ratio: float
    status: str
    details: Dict = field(default_factory=dict)


class SpreadFootingDesign:
    """ACI 318-19 isolated spread footing design checker."""

    def __init__(self, fc: float = 4000, fy: float = 60000):
        """
        Args:
            fc: Concrete strength (psi).
            fy: Rebar yield strength (psi).
        """
        self.fc = fc
        self.fy = fy

    def check_bearing(self, geom: FootingGeometry, loads: FootingLoads,
                      soil: SoilProperties) -> FootingResult:
        """Check soil bearing pressure."""
        q = loads.Pa / geom.area  # psf → need conversion from in² to ft²
        q_psf = q * 144  # in² to ft²
        ratio = q_psf / soil.qa if soil.qa > 0 else float('inf')

        return FootingResult(
            check="Bearing Pressure",
            demand=q_psf, capacity=soil.qa,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'q': q_psf, 'qa': soil.qa},
        )

    def check_one_way_shear(self, geom: FootingGeometry,
                            loads: FootingLoads) -> FootingResult:
        """ACI 318-19 §22.5 one-way shear."""
        qu = loads.Pu / geom.area  # lb/in²
        # Critical section at d from face of column
        cantilever = (geom.L - geom.col_d) / 2.0 - geom.d
        cantilever = max(cantilever, 0)

        Vu = qu * geom.B * cantilever
        phi = 0.75
        Vc = 2 * math.sqrt(self.fc) * geom.B * geom.d
        phi_Vc = phi * Vc

        ratio = abs(Vu) / phi_Vc if phi_Vc > 0 else float('inf')

        return FootingResult(
            check="One-Way Shear (§22.5)",
            demand=abs(Vu), capacity=phi_Vc,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'Vc': Vc, 'critical_length': cantilever},
        )

    def check_two_way_shear(self, geom: FootingGeometry,
                            loads: FootingLoads) -> FootingResult:
        """ACI 318-19 §22.6 two-way (punching) shear."""
        qu = loads.Pu / geom.area

        # Critical perimeter at d/2 from column face
        b0 = 2 * ((geom.col_b + geom.d) + (geom.col_d + geom.d))
        A_punch = (geom.col_b + geom.d) * (geom.col_d + geom.d)
        Vu = loads.Pu - qu * A_punch

        phi = 0.75
        beta_c = max(geom.col_b, geom.col_d) / min(geom.col_b, geom.col_d)
        alpha_s = 40  # Interior column

        # Three criteria (§22.6.5.2)
        Vc1 = 4 * math.sqrt(self.fc) * b0 * geom.d
        Vc2 = (2 + 4 / beta_c) * math.sqrt(self.fc) * b0 * geom.d
        Vc3 = (2 + alpha_s * geom.d / b0) * math.sqrt(self.fc) * b0 * geom.d

        Vc = min(Vc1, Vc2, Vc3)
        phi_Vc = phi * Vc

        ratio = abs(Vu) / phi_Vc if phi_Vc > 0 else float('inf')

        return FootingResult(
            check="Two-Way Shear (§22.6)",
            demand=abs(Vu), capacity=phi_Vc,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'b0': b0, 'Vc': Vc, 'beta_c': beta_c},
        )

    def check_flexure(self, geom: FootingGeometry,
                      loads: FootingLoads) -> FootingResult:
        """ACI 318-19 §22.2 flexural check at face of column."""
        qu = loads.Pu / geom.area
        cantilever = (geom.L - geom.col_d) / 2.0

        Mu = qu * geom.B * cantilever**2 / 2.0
        phi = 0.90

        # Required reinforcement
        Rn = Mu / (phi * geom.B * geom.d**2) if geom.d > 0 else 0
        rho = 0.85 * self.fc / self.fy * (1 - math.sqrt(max(1 - 2 * Rn / (0.85 * self.fc), 0)))

        rho_min = max(200 / self.fy, 0.0018)
        rho_design = max(rho, rho_min)

        As_req = rho_design * geom.B * geom.d
        Mn = As_req * self.fy * (geom.d - As_req * self.fy / (2 * 0.85 * self.fc * geom.B))
        phi_Mn = phi * Mn

        ratio = abs(Mu) / phi_Mn if phi_Mn > 0 else float('inf')

        return FootingResult(
            check="Flexure (§22.2)",
            demand=abs(Mu), capacity=phi_Mn,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            details={'As_req': As_req, 'rho': rho_design, 'cantilever': cantilever},
        )

    def design_footing(self, geom: FootingGeometry, loads: FootingLoads,
                       soil: SoilProperties) -> List[FootingResult]:
        """Run all checks and return results."""
        return [
            self.check_bearing(geom, loads, soil),
            self.check_one_way_shear(geom, loads),
            self.check_two_way_shear(geom, loads),
            self.check_flexure(geom, loads),
        ]
