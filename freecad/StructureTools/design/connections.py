# -*- coding: utf-8 -*-
"""
Steel Connection Design Module

Foundation for steel connection design per AISC 360-22 Chapter J.
Covers bolted and welded connections with common failure modes.

Units: US customary (kips, inches) unless noted.
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum


class ConnectionType(Enum):
    BOLTED_SHEAR = "Bolted Shear"
    BOLTED_MOMENT = "Bolted Moment"
    WELDED_SHEAR = "Welded Shear"
    WELDED_MOMENT = "Welded Moment"
    BASE_PLATE = "Base Plate"


class BoltGrade(Enum):
    A325 = "A325"
    A490 = "A490"
    F3125_A325 = "F3125 Gr A325"
    F3125_A490 = "F3125 Gr A490"


class WeldType(Enum):
    FILLET = "Fillet"
    CJP = "Complete Joint Penetration"
    PJP = "Partial Joint Penetration"


@dataclass
class BoltProperties:
    """Bolt properties per AISC 360 Table J3.2."""
    grade: BoltGrade
    diameter: float   # in
    Fnv: float = 0.0  # Nominal shear stress (ksi)
    Fnt: float = 0.0  # Nominal tensile stress (ksi)

    def __post_init__(self):
        if self.Fnv == 0:
            if self.grade in (BoltGrade.A325, BoltGrade.F3125_A325):
                self.Fnv = 54.0  # Thread excluded: 68
                self.Fnt = 90.0
            else:
                self.Fnv = 68.0  # Thread excluded: 84
                self.Fnt = 113.0

    @property
    def Ab(self) -> float:
        """Nominal bolt area (in²)."""
        return math.pi * (self.diameter / 2) ** 2


@dataclass
class WeldProperties:
    """Weld properties."""
    weld_type: WeldType
    size: float       # Weld size/leg (in)
    length: float     # Weld length (in)
    electrode: float = 70.0  # Electrode strength FEXX (ksi)

    @property
    def throat(self) -> float:
        """Effective throat thickness (in)."""
        if self.weld_type == WeldType.FILLET:
            return self.size * math.sqrt(2) / 2
        return self.size

    @property
    def area(self) -> float:
        """Effective weld area (in²)."""
        return self.throat * self.length


@dataclass
class ConnectionResult:
    """Result of a connection design check."""
    connection_type: str
    check_name: str
    demand: float
    capacity: float
    ratio: float
    status: str
    clause: str
    details: Dict = field(default_factory=dict)

    @property
    def is_acceptable(self) -> bool:
        return self.ratio <= 1.0


class ConnectionDesign:
    """AISC 360-22 Chapter J connection design checker."""

    def __init__(self, phi_bolt: float = 0.75, phi_weld: float = 0.75):
        self.phi_bolt = phi_bolt
        self.phi_weld = phi_weld

    # --- Bolt checks ---

    def check_bolt_shear(
        self, bolt: BoltProperties, n_bolts: int, n_shear_planes: int, Vu: float
    ) -> ConnectionResult:
        """AISC J3.6 — bolt shear strength."""
        Rn_per_bolt = bolt.Fnv * bolt.Ab * n_shear_planes
        phi_Rn = self.phi_bolt * Rn_per_bolt * n_bolts
        ratio = abs(Vu) / phi_Rn if phi_Rn > 0 else float('inf')

        return ConnectionResult(
            connection_type="Bolted",
            check_name="Bolt Shear (J3.6)",
            demand=abs(Vu),
            capacity=phi_Rn,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            clause="J3.6",
            details={'Rn_per_bolt': Rn_per_bolt, 'n_bolts': n_bolts},
        )

    def check_bolt_tension(
        self, bolt: BoltProperties, n_bolts: int, Tu: float
    ) -> ConnectionResult:
        """AISC J3.6 — bolt tensile strength."""
        Rn_per_bolt = bolt.Fnt * bolt.Ab
        phi_Rn = self.phi_bolt * Rn_per_bolt * n_bolts
        ratio = abs(Tu) / phi_Rn if phi_Rn > 0 else float('inf')

        return ConnectionResult(
            connection_type="Bolted",
            check_name="Bolt Tension (J3.6)",
            demand=abs(Tu),
            capacity=phi_Rn,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            clause="J3.6",
        )

    def check_bolt_bearing(
        self,
        bolt: BoltProperties,
        n_bolts: int,
        Fu_plate: float,
        t_plate: float,
        Lc: float,
        Vu: float,
        deformation_at_service: bool = True,
    ) -> ConnectionResult:
        """AISC J3.10 — bearing/tearout at bolt holes."""
        if deformation_at_service:
            Rn_per_bolt = min(1.2 * Lc * t_plate * Fu_plate, 2.4 * bolt.diameter * t_plate * Fu_plate)
        else:
            Rn_per_bolt = min(1.5 * Lc * t_plate * Fu_plate, 3.0 * bolt.diameter * t_plate * Fu_plate)

        phi_Rn = self.phi_bolt * Rn_per_bolt * n_bolts
        ratio = abs(Vu) / phi_Rn if phi_Rn > 0 else float('inf')

        return ConnectionResult(
            connection_type="Bolted",
            check_name="Bearing/Tearout (J3.10)",
            demand=abs(Vu),
            capacity=phi_Rn,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            clause="J3.10",
        )

    # --- Weld checks ---

    def check_fillet_weld(
        self, weld: WeldProperties, Vu: float, theta: float = 0.0
    ) -> ConnectionResult:
        """AISC J2.4 — fillet weld strength."""
        Fnw = 0.60 * weld.electrode * (1.0 + 0.50 * math.sin(math.radians(theta)) ** 1.5)
        Rn = Fnw * weld.area
        phi_Rn = self.phi_weld * Rn
        ratio = abs(Vu) / phi_Rn if phi_Rn > 0 else float('inf')

        return ConnectionResult(
            connection_type="Welded",
            check_name="Fillet Weld (J2.4)",
            demand=abs(Vu),
            capacity=phi_Rn,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            clause="J2.4",
            details={'Fnw': Fnw, 'effective_area': weld.area},
        )

    def check_base_metal(
        self, Fu: float, Ag: float, Vu: float
    ) -> ConnectionResult:
        """AISC J4.2 — base metal shear rupture."""
        Anv = Ag  # Simplified: no holes
        Rn = 0.6 * Fu * Anv
        phi_Rn = 0.75 * Rn
        ratio = abs(Vu) / phi_Rn if phi_Rn > 0 else float('inf')

        return ConnectionResult(
            connection_type="Base Metal",
            check_name="Shear Rupture (J4.2)",
            demand=abs(Vu),
            capacity=phi_Rn,
            ratio=ratio,
            status="OK" if ratio <= 1.0 else "FAIL",
            clause="J4.2",
        )
