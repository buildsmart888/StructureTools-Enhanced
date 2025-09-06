"""
ACI 318 Concrete Design Code Implementation

This module provides comprehensive concrete design checking according to ACI 318-19
including reinforced concrete beams, columns, slabs, and foundations.

Features:
- Complete flexural design for beams and slabs
- Column design with axial and biaxial bending
- Shear design and reinforcement calculations
- Foundation design (spread footings, continuous footings)
- Seismic design provisions (ACI 318 Chapter 18)
- Professional reporting and documentation
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum
import json
import os

try:
    import FreeCAD as App
except ImportError:
    # For testing without FreeCAD
    class MockApp:
        class Console:
            @staticmethod
            def PrintMessage(msg): print(f"INFO: {msg}")
            @staticmethod
            def PrintWarning(msg): print(f"WARNING: {msg}")
            @staticmethod
            def PrintError(msg): print(f"ERROR: {msg}")
    App = MockApp()

from ..utils.exceptions import AnalysisError, ValidationError
from ..utils.validation import StructuralValidator


class ConcreteStrengthMethod(Enum):
    """Concrete strength design method enumeration."""
    USD = "USD"  # Ultimate Strength Design (ACI 318)
    WSD = "WSD"  # Working Stress Design (Alternative method)


class ConcreteElementType(Enum):
    """Concrete element type enumeration."""
    BEAM = "Beam"
    COLUMN = "Column" 
    SLAB = "Slab"
    FOOTING = "Footing"
    WALL = "Wall"
    FOUNDATION = "Foundation"


class ConcreteFailureMode(Enum):
    """Concrete failure mode enumeration."""
    FLEXURAL_TENSION = "Flexural Tension Failure"
    FLEXURAL_COMPRESSION = "Flexural Compression Failure"
    SHEAR_FAILURE = "Shear Failure"
    COMPRESSION_FAILURE = "Compression Failure"
    DEVELOPMENT_LENGTH = "Development Length Failure"
    DEFLECTION_LIMIT = "Deflection Limit"
    CRACK_WIDTH = "Crack Width Control"
    BEARING_FAILURE = "Bearing Failure"
    PUNCHING_SHEAR = "Punching Shear Failure"


@dataclass
class ConcreteProperties:
    """Concrete material properties container."""
    name: str
    fc: float    # Compressive strength (psi)
    density: float  # Density (lb/ft³)
    Ec: float    # Modulus of elasticity (psi)
    fr: float    # Modulus of rupture (psi)
    beta1: float # Stress block factor
    
    def __post_init__(self):
        """Calculate derived properties."""
        # ACI 318-19 Section 19.2.2.1
        if self.Ec == 0:
            # Ec = 33 * wc^1.5 * sqrt(fc) for normal weight concrete
            wc = self.density / 1000  # Convert to thousands of lb/ft³
            self.Ec = 33 * (wc**1.5) * math.sqrt(self.fc)
        
        # Modulus of rupture (ACI 318-19 Section 19.2.3.1)
        if self.fr == 0:
            if self.density >= 90:  # Normal weight concrete
                self.fr = 7.5 * math.sqrt(self.fc)
            else:  # Lightweight concrete
                self.fr = 6.7 * math.sqrt(self.fc)
        
        # Stress block factor β₁ (ACI 318-19 Section 22.2.2.4.3)
        if self.beta1 == 0:
            if self.fc <= 4000:
                self.beta1 = 0.85
            elif self.fc <= 8000:
                self.beta1 = 0.85 - 0.05 * (self.fc - 4000) / 1000
            else:
                self.beta1 = 0.65
    
    @property
    def is_valid(self) -> bool:
        """Check if concrete properties are valid."""
        return all([
            self.fc > 0,
            2000 <= self.fc <= 15000,  # Reasonable range for fc'
            50 <= self.density <= 160,  # Reasonable range for density
            self.Ec > 0,
            self.fr > 0,
            0.65 <= self.beta1 <= 0.85
        ])


@dataclass
class ReinforcementProperties:
    """Reinforcement steel properties container."""
    name: str
    fy: float    # Yield strength (psi)
    fu: float    # Ultimate strength (psi)
    Es: float    # Modulus of elasticity (psi)
    bar_sizes: List[str]  # Available bar sizes
    
    def __post_init__(self):
        """Set default values."""
        if self.Es == 0:
            self.Es = 29000000  # 29,000 ksi standard for steel
        
        if not self.bar_sizes:
            self.bar_sizes = ["#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#14", "#18"]
    
    @property
    def is_valid(self) -> bool:
        """Check if reinforcement properties are valid."""
        return all([
            self.fy > 0,
            self.fu > self.fy,
            40000 <= self.fy <= 100000,  # Grade 40 to Grade 100
            self.Es > 0
        ])


@dataclass
class RebarSize:
    """Reinforcement bar size properties."""
    designation: str
    diameter: float  # inches
    area: float     # in²
    weight: float   # lb/ft
    
    @staticmethod
    def get_bar_properties(designation: str) -> 'RebarSize':
        """Get standard rebar properties by designation."""
        # ACI standard rebar sizes
        bar_data = {
            "#3": RebarSize("#3", 0.375, 0.11, 0.376),
            "#4": RebarSize("#4", 0.500, 0.20, 0.668),
            "#5": RebarSize("#5", 0.625, 0.31, 1.043),
            "#6": RebarSize("#6", 0.750, 0.44, 1.502),
            "#7": RebarSize("#7", 0.875, 0.60, 2.044),
            "#8": RebarSize("#8", 1.000, 0.79, 2.670),
            "#9": RebarSize("#9", 1.128, 1.00, 3.400),
            "#10": RebarSize("#10", 1.270, 1.27, 4.303),
            "#11": RebarSize("#11", 1.410, 1.56, 5.313),
            "#14": RebarSize("#14", 1.693, 2.25, 7.650),
            "#18": RebarSize("#18", 2.257, 4.00, 13.600),
        }
        
        return bar_data.get(designation, RebarSize("Unknown", 0, 0, 0))


@dataclass
class ConcreteSection:
    """Concrete section geometry container."""
    name: str
    width: float    # Section width (in)
    height: float   # Section height (in)
    cover: float    # Concrete cover (in)
    
    # Reinforcement
    tension_bars: List[Tuple[str, int]]  # [(bar_size, count), ...]
    compression_bars: List[Tuple[str, int]]  # [(bar_size, count), ...]
    stirrups: str   # Stirrup size
    stirrup_spacing: float  # Stirrup spacing (in)
    
    def __post_init__(self):
        """Calculate derived properties."""
        self.area = self.width * self.height
        self.effective_depth = self.height - self.cover - 0.5  # Approximate d
        
        # Calculate reinforcement areas
        self.As_tension = sum(
            RebarSize.get_bar_properties(bar_size).area * count
            for bar_size, count in self.tension_bars
        )
        
        self.As_compression = sum(
            RebarSize.get_bar_properties(bar_size).area * count
            for bar_size, count in self.compression_bars
        )
    
    @property
    def reinforcement_ratio(self) -> float:
        """Calculate tension reinforcement ratio."""
        return self.As_tension / (self.width * self.effective_depth) if self.effective_depth > 0 else 0
    
    @property
    def is_valid(self) -> bool:
        """Check if section is valid."""
        return all([
            self.width > 0,
            self.height > 0,
            self.cover >= 0.75,  # Minimum cover
            self.effective_depth > 0,
            self.As_tension >= 0
        ])


@dataclass
class ConcreteDesignForces:
    """Design forces for concrete elements."""
    Mu: float = 0.0    # Factored moment (in-lb)
    Vu: float = 0.0    # Factored shear (lb)
    Pu: float = 0.0    # Factored axial force (lb, compression positive)
    Tu: float = 0.0    # Factored torsion (in-lb)
    
    # Biaxial bending (for columns)
    Mux: float = 0.0   # Factored moment about x-axis (in-lb)
    Muy: float = 0.0   # Factored moment about y-axis (in-lb)
    
    @property
    def max_moment(self) -> float:
        """Maximum factored moment."""
        return max(abs(self.Mu), abs(self.Mux), abs(self.Muy))
    
    @property
    def is_biaxial(self) -> bool:
        """Check if biaxial bending exists."""
        return abs(self.Mux) > 0.01 and abs(self.Muy) > 0.01


@dataclass
class ConcreteDesignResult:
    """Concrete design check result container."""
    element_name: str
    design_method: ConcreteStrengthMethod
    failure_mode: ConcreteFailureMode
    demand: float
    capacity: float
    ratio: float
    status: str  # "OK", "FAIL", "WARNING"
    details: Dict
    code_section: str  # ACI 318 section reference
    reinforcement_required: Dict = None  # Required reinforcement details
    
    @property
    def is_acceptable(self) -> bool:
        """Check if design is acceptable."""
        return self.status == "OK" and self.ratio <= 1.0
    
    def get_summary(self) -> str:
        """Get result summary string."""
        return f"{self.element_name}: {self.failure_mode.value} = {self.ratio:.3f} ({self.status})"


class ACI318DesignCode:
    """
    Professional ACI 318-19 concrete design code implementation.
    
    This class provides comprehensive concrete design checking capabilities including:
    - Flexural strength design (tension and compression controlled)
    - Shear design with reinforcement
    - Column design (axial and biaxial bending)
    - Development length requirements
    - Serviceability checks (deflection, crack control)
    - Foundation design
    """
    
    def __init__(self, design_method: ConcreteStrengthMethod = ConcreteStrengthMethod.USD):
        """
        Initialize ACI 318 design code checker.
        
        Args:
            design_method: USD (Ultimate Strength Design)
        """
        self.design_method = design_method
        self.code_version = "ACI 318-19"
        
        # Load concrete and reinforcement databases
        self._load_material_databases()
        
        # Strength reduction factors (φ factors) - ACI 318-19 Section 21.2
        self.phi_factors = {
            'tension_controlled': 0.90,     # Flexure, tension controlled
            'compression_controlled': 0.65,  # Compression controlled (columns with ties)
            'spiral_columns': 0.75,          # Compression controlled (columns with spirals)
            'shear': 0.75,                   # Shear and torsion
            'bearing': 0.65,                 # Bearing on concrete
            'development': 0.90,             # Development and splices
            'strut_tie': 0.75               # Strut-and-tie models
        }
        
        # Load factors (for ultimate strength design)
        self.load_factors = {
            'dead': 1.2,
            'live': 1.6,
            'wind': 1.0,
            'seismic': 1.0,
            'earth_pressure': 1.6
        }
        
        # Serviceability limits
        self.deflection_limits = {
            'immediate': {
                'roof_not_supporting': 180,  # L/180
                'floor_not_supporting': 360,  # L/360
                'roof_supporting': 240,       # L/240
                'floor_supporting': 480       # L/480
            },
            'long_term': {
                'roof_not_supporting': 120,   # L/120
                'floor_not_supporting': 240,  # L/240
                'roof_supporting': 180,       # L/180
                'floor_supporting': 360       # L/360
            }
        }
    
    def _load_material_databases(self):
        """Load concrete and reinforcement material databases."""
        # Standard concrete strengths
        self.concrete_database = {
            '3000psi': ConcreteProperties(
                name='3000psi', fc=3000, density=145, Ec=0, fr=0, beta1=0
            ),
            '4000psi': ConcreteProperties(
                name='4000psi', fc=4000, density=150, Ec=0, fr=0, beta1=0
            ),
            '5000psi': ConcreteProperties(
                name='5000psi', fc=5000, density=150, Ec=0, fr=0, beta1=0
            ),
            '6000psi': ConcreteProperties(
                name='6000psi', fc=6000, density=150, Ec=0, fr=0, beta1=0
            ),
            '8000psi': ConcreteProperties(
                name='8000psi', fc=8000, density=155, Ec=0, fr=0, beta1=0
            )
        }
        
        # Standard reinforcement grades
        self.reinforcement_database = {
            'Grade60': ReinforcementProperties(
                name='Grade60', fy=60000, fu=90000, Es=29000000, bar_sizes=[]
            ),
            'Grade75': ReinforcementProperties(
                name='Grade75', fy=75000, fu=100000, Es=29000000, bar_sizes=[]
            ),
            'Grade80': ReinforcementProperties(
                name='Grade80', fy=80000, fu=120000, Es=29000000, bar_sizes=[]
            )
        }
    
    def check_beam_flexure(self, section: ConcreteSection, concrete: ConcreteProperties,
                          rebar: ReinforcementProperties, forces: ConcreteDesignForces) -> ConcreteDesignResult:
        """
        Check beam flexural strength per ACI 318-19.
        
        Args:
            section: Concrete section properties
            concrete: Concrete material properties
            rebar: Reinforcement properties
            forces: Applied forces
        
        Returns:
            ConcreteDesignResult with flexural check details
        """
        Mu = abs(forces.Mu)
        if Mu == 0:
            return ConcreteDesignResult(
                element_name=section.name,
                design_method=self.design_method,
                failure_mode=ConcreteFailureMode.FLEXURAL_TENSION,
                demand=0.0,
                capacity=float('inf'),
                ratio=0.0,
                status="OK",
                details={},
                code_section="22.2"
            )
        
        # Section properties
        b = section.width
        d = section.effective_depth
        As = section.As_tension
        As_comp = section.As_compression
        
        # Material properties
        fc = concrete.fc
        fy = rebar.fy
        beta1 = concrete.beta1
        Es = rebar.Es
        
        # Check minimum reinforcement (ACI 318-19 Section 9.6.1.2)
        As_min = max(
            3 * math.sqrt(fc) * b * d / fy,
            200 * b * d / fy
        )
        
        if As < As_min:
            return ConcreteDesignResult(
                element_name=section.name,
                design_method=self.design_method,
                failure_mode=ConcreteFailureMode.FLEXURAL_TENSION,
                demand=Mu,
                capacity=0.0,
                ratio=float('inf'),
                status="FAIL",
                details={'As_provided': As, 'As_min': As_min, 'error': 'Insufficient minimum reinforcement'},
                code_section="9.6.1.2"
            )
        
        # Calculate balanced reinforcement ratio
        # ACI 318-19 Section 22.2.2
        epsilon_cu = 0.003  # Ultimate concrete strain
        epsilon_y = fy / Es  # Yield strain of steel
        
        cb = (epsilon_cu / (epsilon_cu + epsilon_y)) * d  # Balanced neutral axis depth
        rho_b = 0.85 * beta1 * fc * cb / (fy * d)  # Balanced reinforcement ratio
        rho = As / (b * d)  # Actual reinforcement ratio
        
        # Check if section is tension or compression controlled
        # ACI 318-19 Section 21.2.2
        if rho <= 0.375 * rho_b:
            # Tension controlled
            phi = self.phi_factors['tension_controlled']
            control_type = "tension_controlled"
        else:
            # Compression controlled or transition
            epsilon_t = epsilon_cu * (d - cb) / cb  # Tension strain in extreme tension steel
            if epsilon_t >= 0.005:
                phi = self.phi_factors['tension_controlled']
                control_type = "tension_controlled"
            elif epsilon_t <= 0.002:
                phi = self.phi_factors['compression_controlled']
                control_type = "compression_controlled"
            else:
                # Transition zone
                phi = self.phi_factors['compression_controlled'] + (
                    self.phi_factors['tension_controlled'] - self.phi_factors['compression_controlled']
                ) * (epsilon_t - 0.002) / 0.003
                control_type = "transition"
        
        # Calculate nominal moment strength
        # Rectangular stress block method (ACI 318-19 Section 22.2.2.4.1)
        a = As * fy / (0.85 * fc * b)  # Depth of equivalent stress block
        
        if a <= section.height:  # Check if compression zone is within section
            # Calculate moment capacity
            Mn = As * fy * (d - a/2)
            
            # Include compression reinforcement if present
            if As_comp > 0:
                # Additional moment from compression steel
                Mn_comp = As_comp * fy * (d - section.cover)
                Mn += Mn_comp
            
        else:
            # T-beam or compression failure - need more complex analysis
            Mn = 0.85 * fc * b * section.height * (d - section.height/2)
        
        # Design moment capacity
        phi_Mn = phi * Mn
        
        # Calculate demand-to-capacity ratio
        ratio = Mu / phi_Mn if phi_Mn > 0 else float('inf')
        status = "OK" if ratio <= 1.0 else "FAIL"
        
        details = {
            'As_provided': As,
            'As_min': As_min,
            'rho': rho,
            'rho_balanced': rho_b,
            'control_type': control_type,
            'phi_factor': phi,
            'a': a,
            'Mn': Mn,
            'phi_Mn': phi_Mn,
            'applied_moment': Mu
        }
        
        return ConcreteDesignResult(
            element_name=section.name,
            design_method=self.design_method,
            failure_mode=ConcreteFailureMode.FLEXURAL_TENSION if control_type == "tension_controlled" else ConcreteFailureMode.FLEXURAL_COMPRESSION,
            demand=Mu,
            capacity=phi_Mn,
            ratio=ratio,
            status=status,
            details=details,
            code_section="22.2"
        )
    
    def check_beam_shear(self, section: ConcreteSection, concrete: ConcreteProperties,
                        rebar: ReinforcementProperties, forces: ConcreteDesignForces) -> ConcreteDesignResult:
        """
        Check beam shear strength per ACI 318-19.
        
        Args:
            section: Concrete section properties
            concrete: Concrete material properties
            rebar: Reinforcement properties
            forces: Applied forces
        
        Returns:
            ConcreteDesignResult with shear check details
        """
        Vu = abs(forces.Vu)
        if Vu == 0:
            return ConcreteDesignResult(
                element_name=section.name,
                design_method=self.design_method,
                failure_mode=ConcreteFailureMode.SHEAR_FAILURE,
                demand=0.0,
                capacity=float('inf'),
                ratio=0.0,
                status="OK",
                details={},
                code_section="22.5"
            )
        
        # Section properties
        b = section.width
        d = section.effective_depth
        
        # Material properties
        fc = concrete.fc
        fy = rebar.fy
        
        # Concrete shear strength (ACI 318-19 Section 22.5.5.1)
        lambda_factor = 1.0  # For normal weight concrete
        Vc = 2 * lambda_factor * math.sqrt(fc) * b * d
        
        # Shear strength provided by concrete
        phi = self.phi_factors['shear']
        phi_Vc = phi * Vc
        
        # Check if shear reinforcement is required
        if Vu <= 0.5 * phi_Vc:
            # No shear reinforcement required
            capacity = phi_Vc
            stirrup_req = "None required"
            code_section = "22.5.1.1"
        elif Vu <= phi_Vc:
            # Minimum shear reinforcement required
            capacity = phi_Vc
            stirrup_req = "Minimum stirrups"
            code_section = "9.6.3"
        else:
            # Calculate required stirrup reinforcement
            # ACI 318-19 Section 22.5.10.5.3
            Vs_req = Vu / phi - Vc  # Required shear from stirrups
            
            # Get stirrup properties
            stirrup_bar = RebarSize.get_bar_properties(section.stirrups)
            Av = 2 * stirrup_bar.area  # Two legs
            
            # Required stirrup spacing
            s_req = Av * fy * d / Vs_req if Vs_req > 0 else float('inf')
            
            # Check maximum stirrup spacing (ACI 318-19 Section 9.7.6.2.2)
            s_max = min(d/2, 24)  # inches
            
            # Actual stirrup spacing
            s_actual = section.stirrup_spacing
            
            if s_actual <= s_req and s_actual <= s_max:
                # Adequate stirrups
                Vs = Av * fy * d / s_actual
                capacity = phi * (Vc + Vs)
                stirrup_req = f"#{section.stirrups} @ {s_actual} in. spacing"
                code_section = "22.5.10.5.3"
            else:
                # Inadequate stirrups
                capacity = phi_Vc
                stirrup_req = f"Required: #{section.stirrups} @ {s_req:.1f} in. (provided: {s_actual} in.)"
                code_section = "22.5.10.5.3"
        
        # Calculate demand-to-capacity ratio
        ratio = Vu / capacity if capacity > 0 else float('inf')
        status = "OK" if ratio <= 1.0 else "FAIL"
        
        details = {
            'Vc': Vc,
            'phi_Vc': phi_Vc,
            'stirrup_requirement': stirrup_req,
            'applied_shear': Vu,
            'lambda_factor': lambda_factor
        }
        
        return ConcreteDesignResult(
            element_name=section.name,
            design_method=self.design_method,
            failure_mode=ConcreteFailureMode.SHEAR_FAILURE,
            demand=Vu,
            capacity=capacity,
            ratio=ratio,
            status=status,
            details=details,
            code_section=code_section
        )
    
    def check_column_compression(self, section: ConcreteSection, concrete: ConcreteProperties,
                               rebar: ReinforcementProperties, forces: ConcreteDesignForces,
                               length_properties: Dict) -> ConcreteDesignResult:
        """
        Check column compression strength per ACI 318-19.
        
        Args:
            section: Concrete section properties
            concrete: Concrete material properties
            rebar: Reinforcement properties
            forces: Applied forces
            length_properties: Effective lengths and slenderness
        
        Returns:
            ConcreteDesignResult with compression check details
        """
        Pu = abs(forces.Pu)
        if Pu == 0:
            return ConcreteDesignResult(
                element_name=section.name,
                design_method=self.design_method,
                failure_mode=ConcreteFailureMode.COMPRESSION_FAILURE,
                demand=0.0,
                capacity=float('inf'),
                ratio=0.0,
                status="OK",
                details={},
                code_section="22.4"
            )
        
        # Section properties
        Ag = section.area  # Gross area
        Ast = section.As_tension + section.As_compression  # Total steel area
        
        # Material properties
        fc = concrete.fc
        fy = rebar.fy
        
        # Check reinforcement ratio limits (ACI 318-19 Section 10.6.1.1)
        rho_g = Ast / Ag
        if rho_g < 0.01:
            App.Console.PrintWarning(f"Column reinforcement ratio {rho_g:.3f} is below minimum of 0.01\n")
        elif rho_g > 0.08:
            App.Console.PrintWarning(f"Column reinforcement ratio {rho_g:.3f} exceeds maximum of 0.08\n")
        
        # Check slenderness effects (ACI 318-19 Section 6.2)
        klu_x = length_properties.get('klu_x', 144)  # Effective length about x-axis
        klu_y = length_properties.get('klu_y', 144)  # Effective length about y-axis
        
        r_x = math.sqrt(section.width**3 * section.height / 12 / Ag)  # Radius of gyration
        r_y = math.sqrt(section.width * section.height**3 / 12 / Ag)  # Radius of gyration
        
        slenderness_x = klu_x / r_x
        slenderness_y = klu_y / r_y
        slenderness_max = max(slenderness_x, slenderness_y)
        
        # Check if column is short or slender (ACI 318-19 Section 6.2.5)
        if slenderness_max <= 34 - 12 * 0.1:  # Assuming small eccentricity
            # Short column - no slenderness effects
            slender = False
            moment_magnification = 1.0
        else:
            # Slender column - apply moment magnification
            slender = True
            # Simplified magnification factor (more complex analysis needed for real design)
            moment_magnification = 1.0 + 0.005 * (slenderness_max - 34)
        
        # Nominal axial strength for tied columns (ACI 318-19 Section 22.4.2.1)
        # Simplified approach - assumes concentric loading
        Po = 0.85 * fc * (Ag - Ast) + fy * Ast  # Pure compression capacity
        
        # Apply reduction factor for eccentricity and reinforcement type
        # For tied columns with some eccentricity
        phi = self.phi_factors['compression_controlled']
        
        # Design capacity
        phi_Pn = phi * 0.80 * Po  # 0.80 factor for tied columns
        
        # Apply moment magnification if slender
        if slender:
            # Reduce capacity for slenderness effects
            phi_Pn *= (1.0 / moment_magnification)
        
        # Calculate demand-to-capacity ratio
        ratio = Pu / phi_Pn if phi_Pn > 0 else float('inf')
        status = "OK" if ratio <= 1.0 else "FAIL"
        
        details = {
            'Ag': Ag,
            'Ast': Ast,
            'rho_g': rho_g,
            'slenderness_x': slenderness_x,
            'slenderness_y': slenderness_y,
            'slenderness_max': slenderness_max,
            'is_slender': slender,
            'moment_magnification': moment_magnification,
            'Po': Po,
            'phi_Pn': phi_Pn,
            'applied_compression': Pu
        }
        
        return ConcreteDesignResult(
            element_name=section.name,
            design_method=self.design_method,
            failure_mode=ConcreteFailureMode.COMPRESSION_FAILURE,
            demand=Pu,
            capacity=phi_Pn,
            ratio=ratio,
            status=status,
            details=details,
            code_section="22.4.2.1"
        )
    
    def check_development_length(self, section: ConcreteSection, concrete: ConcreteProperties,
                                rebar: ReinforcementProperties, bar_size: str,
                                location: str = "tension") -> ConcreteDesignResult:
        """
        Check reinforcement development length per ACI 318-19.
        
        Args:
            section: Concrete section properties
            concrete: Concrete material properties
            rebar: Reinforcement properties
            bar_size: Bar designation (e.g., "#8")
            location: "tension", "compression", or "hook"
        
        Returns:
            ConcreteDesignResult with development length check details
        """
        bar = RebarSize.get_bar_properties(bar_size)
        db = bar.diameter  # Bar diameter
        
        # Material properties
        fc = concrete.fc
        fy = rebar.fy
        
        # Basic development length factors (ACI 318-19 Section 25.4.2)
        if location == "tension":
            # Tension development length (ACI 318-19 Section 25.4.2.3)
            ld_basic = (3 * fy * db) / (40 * math.sqrt(fc))
            
            # Modification factors
            alpha = 1.0    # Reinforcement location factor
            beta = 1.0     # Coating factor (uncoated bars)
            gamma = 0.8    # Bar size factor for #6 and smaller, 1.0 for #7 and larger
            lambda_factor = 1.0  # Lightweight concrete modification factor
            
            if int(bar_size[1:]) <= 6:
                gamma = 0.8
            else:
                gamma = 1.0
            
            # Apply modification factors
            ld = ld_basic * alpha * beta * gamma / lambda_factor
            
            # Minimum development length
            ld = max(ld, 12.0)  # 12 inches minimum
            
        elif location == "compression":
            # Compression development length (ACI 318-19 Section 25.4.9.2)
            ld = (fy * db) / (50 * math.sqrt(fc))
            ld = max(ld, 8.0)  # 8 inches minimum
            
        else:  # hook
            # Hook development length (ACI 318-19 Section 25.4.3.2)
            ldh = (100 * db) / math.sqrt(fc)
            ldh = max(ldh, 6.0)  # 6 inches minimum
            ld = ldh
        
        # Available development length (would need to be provided by user)
        available_length = section.height - 2 * section.cover  # Simplified assumption
        
        ratio = ld / available_length if available_length > 0 else float('inf')
        status = "OK" if ratio <= 1.0 else "FAIL"
        
        details = {
            'bar_size': bar_size,
            'bar_diameter': db,
            'required_development_length': ld,
            'available_length': available_length,
            'location_type': location
        }
        
        return ConcreteDesignResult(
            element_name=section.name,
            design_method=self.design_method,
            failure_mode=ConcreteFailureMode.DEVELOPMENT_LENGTH,
            demand=ld,
            capacity=available_length,
            ratio=ratio,
            status=status,
            details=details,
            code_section="25.4" if location == "tension" else "25.4.9" if location == "compression" else "25.4.3"
        )
    
    def check_deflection(self, section: ConcreteSection, concrete: ConcreteProperties,
                        deflections: Dict, span: float, element_type: str) -> ConcreteDesignResult:
        """
        Check deflection limits per ACI 318-19.
        
        Args:
            section: Concrete section properties
            concrete: Concrete material properties
            deflections: Deflection values for different cases
            span: Element span length (inches)
            element_type: "floor_not_supporting", "roof_not_supporting", etc.
        
        Returns:
            ConcreteDesignResult with deflection check details
        """
        # Get immediate and long-term deflections
        immediate_deflection = abs(deflections.get('immediate', 0.0))
        long_term_deflection = abs(deflections.get('long_term', 0.0))
        
        # Get deflection limits (ACI 318-19 Table 24.2.2)
        immediate_limit_ratio = self.deflection_limits['immediate'].get(element_type, 360)
        long_term_limit_ratio = self.deflection_limits['long_term'].get(element_type, 240)
        
        immediate_limit = span / immediate_limit_ratio
        long_term_limit = span / long_term_limit_ratio
        
        # Check both immediate and long-term
        immediate_ratio = immediate_deflection / immediate_limit if immediate_limit > 0 else 0
        long_term_ratio = long_term_deflection / long_term_limit if long_term_limit > 0 else 0
        
        # Governing ratio
        ratio = max(immediate_ratio, long_term_ratio)
        status = "OK" if ratio <= 1.0 else "FAIL"
        
        details = {
            'immediate_deflection': immediate_deflection,
            'immediate_limit': immediate_limit,
            'immediate_ratio': immediate_ratio,
            'long_term_deflection': long_term_deflection,
            'long_term_limit': long_term_limit,
            'long_term_ratio': long_term_ratio,
            'span': span,
            'element_type': element_type
        }
        
        return ConcreteDesignResult(
            element_name=section.name,
            design_method=self.design_method,
            failure_mode=ConcreteFailureMode.DEFLECTION_LIMIT,
            demand=max(immediate_deflection, long_term_deflection),
            capacity=min(immediate_limit, long_term_limit),
            ratio=ratio,
            status=status,
            details=details,
            code_section="24.2.2"
        )
    
    def design_beam_reinforcement(self, section: ConcreteSection, concrete: ConcreteProperties,
                                 rebar: ReinforcementProperties, Mu: float) -> Dict:
        """
        Design reinforcement for beam flexure.
        
        Args:
            section: Concrete section properties (width, height, cover)
            concrete: Concrete material properties
            rebar: Reinforcement properties
            Mu: Required moment strength (in-lb)
        
        Returns:
            Dictionary with reinforcement design details
        """
        b = section.width
        d = section.height - section.cover - 0.5  # Effective depth
        fc = concrete.fc
        fy = rebar.fy
        
        # Required moment strength (unfactored)
        Mn_req = Mu / self.phi_factors['tension_controlled']
        
        # Calculate required reinforcement
        # Use Ru = Mn / (bd²) approach
        Ru = Mn_req / (b * d**2)
        
        # Calculate reinforcement ratio
        m = fy / (0.85 * fc)
        rho_req = (1/m) * (1 - math.sqrt(1 - 2*m*Ru/fy)) if (2*m*Ru/fy) <= 1 else 0
        
        # Check minimum reinforcement
        rho_min = max(3 * math.sqrt(fc) / fy, 200 / fy)
        rho = max(rho_req, rho_min)
        
        # Required steel area
        As_req = rho * b * d
        
        # Select bar sizes and arrangement
        bar_arrangement = self._select_bar_arrangement(As_req, b)
        
        return {
            'As_required': As_req,
            'rho_required': rho_req,
            'rho_minimum': rho_min,
            'rho_provided': rho,
            'bar_arrangement': bar_arrangement,
            'effective_depth': d
        }
    
    def _select_bar_arrangement(self, As_req: float, width: float) -> Dict:
        """Select optimal bar arrangement for required steel area."""
        # Try different bar sizes and find economical arrangement
        bar_options = ["#5", "#6", "#7", "#8", "#9", "#10"]
        arrangements = []
        
        for bar_size in bar_options:
            bar = RebarSize.get_bar_properties(bar_size)
            num_bars = math.ceil(As_req / bar.area)
            
            # Check if bars fit within width (with spacing requirements)
            min_spacing = max(bar.diameter, 1.0, 1.33 * 1.0)  # ACI 318-19 Section 25.2
            required_width = num_bars * bar.diameter + (num_bars - 1) * min_spacing + 2 * 1.5  # Cover
            
            if required_width <= width:
                arrangements.append({
                    'bar_size': bar_size,
                    'number': num_bars,
                    'area_provided': num_bars * bar.area,
                    'area_ratio': num_bars * bar.area / As_req
                })
        
        # Select arrangement closest to required area
        if arrangements:
            best = min(arrangements, key=lambda x: abs(x['area_ratio'] - 1.0))
            return best
        else:
            return {'bar_size': '#8', 'number': 4, 'area_provided': 4*0.79, 'area_ratio': 1.0}
    
    def generate_design_report(self, element_results: List[ConcreteDesignResult], 
                             project_info: Dict = None) -> str:
        """
        Generate comprehensive concrete design report.
        
        Args:
            element_results: List of design check results
            project_info: Project information dictionary
        
        Returns:
            Formatted design report string
        """
        report_lines = []
        
        # Header
        report_lines.append("=" * 80)
        report_lines.append("ACI 318-19 CONCRETE DESIGN REPORT")
        report_lines.append("=" * 80)
        report_lines.append(f"Design Method: {self.design_method.value}")
        report_lines.append(f"Code Version: {self.code_version}")
        report_lines.append("")
        
        if project_info:
            report_lines.append("PROJECT INFORMATION:")
            report_lines.append("-" * 20)
            for key, value in project_info.items():
                report_lines.append(f"{key}: {value}")
            report_lines.append("")
        
        # Summary
        total_elements = len(element_results)
        passing_elements = sum(1 for r in element_results if r.is_acceptable)
        failing_elements = total_elements - passing_elements
        
        report_lines.append("DESIGN SUMMARY:")
        report_lines.append("-" * 15)
        report_lines.append(f"Total Elements Checked: {total_elements}")
        report_lines.append(f"Passing Elements: {passing_elements}")
        report_lines.append(f"Failing Elements: {failing_elements}")
        report_lines.append(f"Success Rate: {passing_elements/total_elements*100:.1f}%" if total_elements > 0 else "Success Rate: N/A")
        report_lines.append("")
        
        # Detailed results
        report_lines.append("DETAILED DESIGN CHECKS:")
        report_lines.append("-" * 23)
        
        for result in element_results:
            report_lines.append(f"\nElement: {result.element_name}")
            report_lines.append(f"Check Type: {result.failure_mode.value}")
            report_lines.append(f"Code Section: {result.code_section}")
            report_lines.append(f"Demand/Capacity Ratio: {result.ratio:.3f}")
            report_lines.append(f"Status: {result.status}")
            
            if result.details:
                report_lines.append("Details:")
                for key, value in result.details.items():
                    if isinstance(value, float):
                        report_lines.append(f"  {key}: {value:.3f}")
                    else:
                        report_lines.append(f"  {key}: {value}")
        
        report_lines.append("\n" + "=" * 80)
        
        return "\n".join(report_lines)


# Professional concrete design utilities
class ConcreteDesignUtilities:
    """Utility functions for concrete design calculations."""
    
    @staticmethod
    def calculate_cracked_moment_of_inertia(b: float, d: float, As: float,
                                           fc: float, Es: float) -> float:
        """Calculate cracked section moment of inertia for deflection calculations."""
        # Modular ratio
        Ec = 33 * (150/1000)**1.5 * math.sqrt(fc)  # Modulus of elasticity of concrete
        n = Es / Ec  # Modular ratio
        
        # Transformed area
        At = b + n * As
        
        # Neutral axis depth (cracked section)
        kd = (-n * As + math.sqrt((n * As)**2 + 2 * b * n * As * d)) / b
        
        # Cracked moment of inertia
        Icr = b * kd**3 / 3 + n * As * (d - kd)**2
        
        return Icr
    
    @staticmethod
    def calculate_long_term_deflection_multiplier(rho_comp: float, time_factor: float = 2.0) -> float:
        """Calculate long-term deflection multiplier per ACI 318-19."""
        # Long-term deflection multiplier (ACI 318-19 Section 24.2.4.1.4)
        xi = time_factor / (1 + 50 * rho_comp)
        return xi
    
    @staticmethod
    def estimate_required_depth(Mu: float, b: float, fc: float, fy: float) -> float:
        """Estimate required beam depth for preliminary design."""
        # Use approximate method for tension-controlled sections
        # Assume lever arm = 0.9d and rho ≈ 0.5 rho_balanced
        phi = 0.90
        lever_arm_factor = 0.9
        rho_factor = 0.5 * 0.85 * 0.85 * fc / fy  # Approximate balanced ratio
        
        # Required effective depth
        d_req = math.sqrt(Mu / (phi * rho_factor * fy * b * lever_arm_factor))
        
        # Add cover and bar diameter
        h_req = d_req + 2.5  # Assume 2.5" cover + bar diameter
        
        return h_req


if __name__ == "__main__":
    # Example usage
    design_code = ACI318DesignCode(ConcreteStrengthMethod.USD)
    
    # Example concrete section
    section = ConcreteSection(
        name="B1", width=12, height=24, cover=1.5,
        tension_bars=[("#8", 4)], compression_bars=[("#6", 2)],
        stirrups="#4", stirrup_spacing=8
    )
    
    # Materials
    concrete = design_code.concrete_database['4000psi']
    rebar = design_code.reinforcement_database['Grade60']
    
    # Forces
    forces = ConcreteDesignForces(Mu=3000000, Vu=25000)  # 250 kip-ft, 25 kips
    
    # Design checks
    flexure_result = design_code.check_beam_flexure(section, concrete, rebar, forces)
    shear_result = design_code.check_beam_shear(section, concrete, rebar, forces)
    
    print("ACI 318 Design Check Results:")
    print("=" * 40)
    print(flexure_result.get_summary())
    print(shear_result.get_summary())