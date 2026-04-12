#!/usr/bin/env python3
"""
Castellated and Cellular Beam Geometry Calculator
==================================================

Calculate expanded beam geometry and tee section properties from parent W-section.
Supports both castellated beams (CB) and cellular beams (LB - Litzka Beams).

캐스틸레이티드 및 셀룰러 보 기하학 계산기
부재 W단면으로부터 확장 보 기하학 및 티 단면 특성을 계산합니다.

Usage:
    python3 geometry_calculator.py W18x35 --type CB --opening-height 5.5 --spacing 11.0
    python3 geometry_calculator.py W21x44 --type LB --diameter 14.0 --spacing 21.0
    python3 geometry_calculator.py W24x55 --interactive

Output:
    - Expanded depth (dg)
    - Tee section properties (Atop, Abot, Itop, Ibot, Stop, Sbot)
    - Expanded beam nomenclature (e.g., "CB27x35")
"""

import sys
import argparse
import math
from pathlib import Path
from typing import Dict, Optional

# Standard W-section properties database (simplified)
# Format: designation -> (d, bf, tw, tf, A, Ix, Sx, Zx)
W_SECTIONS = {
    # W18 series
    "W18x35": (17.7, 6.00, 0.300, 0.425, 10.3, 510, 57.6, 66.5),
    "W18x40": (17.9, 6.02, 0.315, 0.525, 11.8, 612, 68.4, 78.4),
    "W18x46": (18.1, 6.06, 0.360, 0.605, 13.5, 712, 78.8, 90.7),
    "W18x50": (18.0, 7.50, 0.355, 0.570, 14.7, 800, 88.9, 101),

    # W21 series
    "W21x44": (20.7, 6.50, 0.350, 0.450, 13.0, 843, 81.6, 95.4),
    "W21x50": (20.8, 6.53, 0.380, 0.535, 14.7, 984, 94.5, 110),
    "W21x57": (21.1, 6.56, 0.405, 0.650, 16.7, 1170, 111, 129),
    "W21x62": (21.0, 8.24, 0.400, 0.615, 18.3, 1330, 127, 144),

    # W24 series
    "W24x55": (23.6, 7.01, 0.395, 0.505, 16.2, 1350, 114, 134),
    "W24x62": (23.7, 7.04, 0.430, 0.590, 18.2, 1550, 131, 153),
    "W24x68": (23.7, 8.97, 0.415, 0.585, 20.1, 1830, 154, 177),
    "W24x76": (23.9, 8.99, 0.440, 0.680, 22.4, 2100, 176, 200),

    # W27 series
    "W27x84": (26.7, 9.96, 0.460, 0.640, 24.8, 2850, 213, 244),
    "W27x94": (26.9, 9.99, 0.490, 0.745, 27.7, 3270, 243, 278),

    # W30 series
    "W30x90": (29.5, 10.4, 0.470, 0.610, 26.4, 3610, 245, 283),
    "W30x99": (29.7, 10.5, 0.520, 0.670, 29.1, 3990, 269, 312),
}


class BeamGeometryCalculator:
    """
    Calculate castellated and cellular beam geometry and properties.
    """

    def __init__(self, parent_section: str):
        """
        Initialize with parent W-section designation.

        Args:
            parent_section: W-section designation (e.g., "W18x35")
        """
        # Normalize to match database format (e.g., "W18x35")
        self.parent_section = parent_section.replace('X', 'x').replace('W', 'W')

        if self.parent_section not in W_SECTIONS:
            raise ValueError(f"Unknown section: {parent_section}. Available: {list(W_SECTIONS.keys())}")

        # Unpack parent section properties
        d, bf, tw, tf, A, Ix, Sx, Zx = W_SECTIONS[self.parent_section]

        self.d = d        # Depth (in)
        self.bf = bf      # Flange width (in)
        self.tw = tw      # Web thickness (in)
        self.tf = tf      # Flange thickness (in)
        self.A = A        # Area (in²)
        self.Ix = Ix      # Moment of inertia (in⁴)
        self.Sx = Sx      # Section modulus (in³)
        self.Zx = Zx      # Plastic modulus (in³)

        # Calculate web height
        self.h = d - 2*tf

    def calculate_castellated(self, opening_height: float, spacing: Optional[float] = None,
                             theta: float = 60.0) -> Dict:
        """
        Calculate castellated beam geometry (hexagonal openings).

        캐스틸레이티드 보 기하학 계산 (육각형 개구부)

        Args:
            opening_height: Opening height ho (in) - 개구부 높이
            spacing: Center-to-center spacing S (in) - 중심간 간격
            theta: Cut angle in degrees (default 60°) - 절단 각도

        Returns:
            Dictionary with geometry and properties
        """
        ho = opening_height
        theta_rad = math.radians(theta)

        # Calculate opening width e from geometry
        # For hexagonal opening: e = ho / sin(theta)
        e = ho / math.sin(theta_rad)

        # For 60° cuts: e = 2*ho/√3
        if abs(theta - 60.0) < 0.1:
            e = 2.0 * ho / math.sqrt(3)

        # Default spacing if not provided (typical: S ≈ 1.5*e)
        if spacing is None:
            spacing = 1.5 * e

        S = spacing

        # Calculate expanded depth
        # dg = d + ho (for castellated beams)
        dg = self.d + ho

        # Calculate tee section properties
        # Cut occurs at mid-height of parent web
        cut_location = self.d / 2.0

        # Tee flange = original flange
        # Tee web = half of original web + half of ho
        tee_web_height = self.h / 2.0 + ho / 2.0

        # Top and bottom tee areas (symmetric for castellated)
        Atee = self.bf * self.tf + tee_web_height * self.tw

        # Calculate tee centroid from flange face
        # y_bar = (A_flange * tf/2 + A_web * (tf + h_web/2)) / A_tee
        A_flange = self.bf * self.tf
        A_web = tee_web_height * self.tw

        y_bar = (A_flange * self.tf/2 + A_web * (self.tf + tee_web_height/2)) / Atee

        # Calculate tee moment of inertia about its own centroid
        # I_tee = I_flange + I_web (using parallel axis theorem)
        I_flange = (self.bf * self.tf**3 / 12.0 +
                   A_flange * (y_bar - self.tf/2)**2)
        I_web = (self.tw * tee_web_height**3 / 12.0 +
                A_web * (self.tf + tee_web_height/2 - y_bar)**2)

        Itee = I_flange + I_web

        # Tee section moduli
        # Distance from centroid to extreme fibers
        c_top = y_bar  # to flange tip
        c_bot = self.tf + tee_web_height - y_bar  # to web tip

        S_top = Itee / c_top
        S_bot = Itee / c_bot

        # Effective depth between tee centroids
        d_effec = dg - 2*y_bar

        # Generate nomenclature
        # Weight per foot is approximately the same
        weight = int(self.parent_section.split('x')[1])
        nomenclature = f"CB{int(round(dg))}x{weight}"

        # Calculate expansion ratio
        expansion_ratio = dg / self.d

        return {
            "type": "Castellated",
            "parent_section": self.parent_section,
            "nomenclature": nomenclature,
            "theta": theta,
            "opening_height_ho": round(ho, 2),
            "opening_width_e": round(e, 2),
            "spacing_S": round(S, 2),
            "parent_depth_d": round(self.d, 2),
            "expanded_depth_dg": round(dg, 2),
            "expansion_ratio": round(expansion_ratio, 3),
            "web_thickness_tw": round(self.tw, 3),
            "flange_width_bf": round(self.bf, 2),
            "flange_thickness_tf": round(self.tf, 3),
            "tee_area_Atop": round(Atee, 2),
            "tee_area_Abot": round(Atee, 2),
            "tee_inertia_Itop": round(Itee, 1),
            "tee_inertia_Ibot": round(Itee, 1),
            "tee_modulus_Stop": round(S_top, 2),
            "tee_modulus_Sbot": round(S_bot, 2),
            "tee_centroid_ytop": round(y_bar, 2),
            "tee_centroid_ybot": round(y_bar, 2),
            "effective_depth_deffec": round(d_effec, 2),
        }

    def calculate_cellular(self, diameter: float, spacing: Optional[float] = None) -> Dict:
        """
        Calculate cellular beam geometry (circular openings).

        셀룰러 보 기하학 계산 (원형 개구부)

        Args:
            diameter: Opening diameter Do (in) - 개구부 직경
            spacing: Center-to-center spacing s (in) - 중심간 간격

        Returns:
            Dictionary with geometry and properties
        """
        Do = diameter

        # Default spacing if not provided (typical: s ≈ 1.5*Do)
        if spacing is None:
            spacing = 1.5 * Do

        s = spacing

        # Calculate expanded depth
        # dg = d + Do (for cellular beams cut at mid-height)
        dg = self.d + Do

        # Calculate tee section properties
        # Cut occurs at mid-height of parent web
        cut_location = self.d / 2.0

        # Tee web height = half of parent web + Do
        tee_web_height = self.h / 2.0 + Do

        # Top and bottom tee areas (symmetric for cellular)
        Atee = self.bf * self.tf + tee_web_height * self.tw

        # Calculate tee centroid from flange face
        A_flange = self.bf * self.tf
        A_web = tee_web_height * self.tw

        y_bar = (A_flange * self.tf/2 + A_web * (self.tf + tee_web_height/2)) / Atee

        # Calculate tee moment of inertia
        I_flange = (self.bf * self.tf**3 / 12.0 +
                   A_flange * (y_bar - self.tf/2)**2)
        I_web = (self.tw * tee_web_height**3 / 12.0 +
                A_web * (self.tf + tee_web_height/2 - y_bar)**2)

        Itee = I_flange + I_web

        # Tee section moduli
        c_top = y_bar
        c_bot = self.tf + tee_web_height - y_bar

        S_top = Itee / c_top
        S_bot = Itee / c_bot

        # Effective depth between tee centroids
        d_effec = dg - 2*y_bar

        # Generate nomenclature (LB for Litzka Beam / Cellular)
        weight = int(self.parent_section.split('x')[1])
        nomenclature = f"LB{int(round(dg))}x{weight}"

        # Calculate expansion ratio
        expansion_ratio = dg / self.d

        return {
            "type": "Cellular",
            "parent_section": self.parent_section,
            "nomenclature": nomenclature,
            "opening_diameter_Do": round(Do, 2),
            "spacing_s": round(s, 2),
            "parent_depth_d": round(self.d, 2),
            "expanded_depth_dg": round(dg, 2),
            "expansion_ratio": round(expansion_ratio, 3),
            "web_thickness_tw": round(self.tw, 3),
            "flange_width_bf": round(self.bf, 2),
            "flange_thickness_tf": round(self.tf, 3),
            "tee_area_Atop": round(Atee, 2),
            "tee_area_Abot": round(Atee, 2),
            "tee_inertia_Itop": round(Itee, 1),
            "tee_inertia_Ibot": round(Itee, 1),
            "tee_modulus_Stop": round(S_top, 2),
            "tee_modulus_Sbot": round(S_bot, 2),
            "tee_centroid_ytop": round(y_bar, 2),
            "tee_centroid_ybot": round(y_bar, 2),
            "effective_depth_deffec": round(d_effec, 2),
        }


def print_results(results: Dict):
    """Print calculation results in formatted output."""
    print("\n" + "="*80)
    print(f"  {results['type']} Beam Geometry Calculator")
    print("="*80)

    print(f"\nParent Section: {results['parent_section']}")
    print(f"Expanded Nomenclature: {results['nomenclature']}")
    print(f"Expansion Ratio: {results['expansion_ratio']}")

    print("\n--- Opening Geometry ---")
    if results['type'] == 'Castellated':
        print(f"Opening Height (ho):    {results['opening_height_ho']} in")
        print(f"Opening Width (e):      {results['opening_width_e']} in")
        print(f"Spacing (S):            {results['spacing_S']} in")
        print(f"Cut Angle (θ):          {results['theta']}°")
    else:
        print(f"Opening Diameter (Do):  {results['opening_diameter_Do']} in")
        print(f"Spacing (s):            {results['spacing_s']} in")

    print("\n--- Beam Depths ---")
    print(f"Parent Depth (d):       {results['parent_depth_d']} in")
    print(f"Expanded Depth (dg):    {results['expanded_depth_dg']} in")
    print(f"Effective Depth:        {results['effective_depth_deffec']} in")

    print("\n--- Flange Properties ---")
    print(f"Flange Width (bf):      {results['flange_width_bf']} in")
    print(f"Flange Thickness (tf):  {results['flange_thickness_tf']} in")
    print(f"Web Thickness (tw):     {results['web_thickness_tw']} in")

    print("\n--- Tee Section Properties ---")
    print(f"Top Tee Area (Atop):    {results['tee_area_Atop']} in²")
    print(f"Bot Tee Area (Abot):    {results['tee_area_Abot']} in²")
    print(f"Top Tee Inertia (Itop): {results['tee_inertia_Itop']} in⁴")
    print(f"Bot Tee Inertia (Ibot): {results['tee_inertia_Ibot']} in⁴")
    print(f"Top Tee Modulus (Stop): {results['tee_modulus_Stop']} in³")
    print(f"Bot Tee Modulus (Sbot): {results['tee_modulus_Sbot']} in³")
    print(f"Top Tee Centroid:       {results['tee_centroid_ytop']} in from flange")

    print("\n" + "="*80)


def interactive_mode():
    """Interactive calculator mode."""
    print("\n" + "="*80)
    print("  Castellated and Cellular Beam Geometry Calculator")
    print("  Interactive Mode")
    print("="*80)

    # Select parent section
    print("\nAvailable W-sections:")
    sections = sorted(W_SECTIONS.keys())
    for i, section in enumerate(sections, 1):
        if i % 5 == 1:
            print()
        print(f"  {section:10s}", end="")
    print("\n")

    parent = input("Enter parent section (e.g., W18x35): ").strip().replace('X', 'x')

    # Select beam type
    print("\nBeam Types:")
    print("  1. Castellated Beam (CB) - Hexagonal openings")
    print("  2. Cellular Beam (LB) - Circular openings")

    beam_type = input("Select beam type (1 or 2): ").strip()

    try:
        calc = BeamGeometryCalculator(parent)

        if beam_type == "1":
            # Castellated beam
            ho = float(input("\nEnter opening height ho (in): "))
            S = input("Enter spacing S (in) [or press Enter for auto]: ").strip()
            S = float(S) if S else None
            theta = input("Enter cut angle θ (degrees) [or press Enter for 60°]: ").strip()
            theta = float(theta) if theta else 60.0

            results = calc.calculate_castellated(ho, S, theta)

        elif beam_type == "2":
            # Cellular beam
            Do = float(input("\nEnter opening diameter Do (in): "))
            s = input("Enter spacing s (in) [or press Enter for auto]: ").strip()
            s = float(s) if s else None

            results = calc.calculate_cellular(Do, s)

        else:
            print("Invalid beam type selection.")
            return

        print_results(results)

    except Exception as e:
        print(f"\nError: {e}")


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Calculate castellated and cellular beam geometry',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Castellated beam (60° hexagonal openings):
    python3 geometry_calculator.py W18x35 --type CB --opening-height 5.5 --spacing 11.0

  Cellular beam (circular openings):
    python3 geometry_calculator.py W21x44 --type LB --diameter 14.0 --spacing 21.0

  Interactive mode:
    python3 geometry_calculator.py --interactive
        """
    )

    parser.add_argument('section', nargs='?', help='Parent W-section (e.g., W18x35)')
    parser.add_argument('--type', choices=['CB', 'LB'], help='Beam type: CB=Castellated, LB=Cellular')
    parser.add_argument('--opening-height', type=float, help='Opening height ho for castellated (in)')
    parser.add_argument('--diameter', type=float, help='Opening diameter Do for cellular (in)')
    parser.add_argument('--spacing', type=float, help='Center-to-center spacing (in)')
    parser.add_argument('--theta', type=float, default=60.0, help='Cut angle for castellated (degrees, default 60°)')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')

    args = parser.parse_args()

    # Interactive mode
    if args.interactive or not args.section:
        interactive_mode()
        return

    # Command-line mode
    try:
        calc = BeamGeometryCalculator(args.section)

        if args.type == 'CB':
            if not args.opening_height:
                print("Error: --opening-height required for castellated beam")
                sys.exit(1)
            results = calc.calculate_castellated(args.opening_height, args.spacing, args.theta)

        elif args.type == 'LB':
            if not args.diameter:
                print("Error: --diameter required for cellular beam")
                sys.exit(1)
            results = calc.calculate_cellular(args.diameter, args.spacing)

        else:
            print("Error: --type required (CB or LB)")
            sys.exit(1)

        print_results(results)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
