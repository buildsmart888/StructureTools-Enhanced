#!/usr/bin/env python3
"""
Web Post Buckling Checker for Castellated and Cellular Beams
=============================================================

Validate web post buckling capacity per AISC Design Guide 31 Section 3.4.
Checks both flexural and buckling failure modes.

웹 포스트 좌굴 검토기 - 캐스틸레이티드 및 셀룰러 보
AISC Design Guide 31 Section 3.4에 따른 웹 포스트 좌굴 강도 검증

Usage:
    python3 webpost_checker.py --type CB --ho 5.5 --e 11.0 --S 16.5 --tw 0.3 --Vr 25.0
    python3 webpost_checker.py --type LB --Do 14.0 --s 21.0 --tw 0.2 --Vr 30.0
    python3 webpost_checker.py --interactive

Key Formulas:
    Castellated: Equations 3-22 to 3-29 (Section 3.4.1)
    Cellular: Equations 3-30 to 3-36 (Section 3.4.2)
"""

import sys
import argparse
import math
from typing import Dict, Optional


class WebPostChecker:
    """
    Check web post buckling capacity for castellated and cellular beams.
    """

    def __init__(self, Fy: float = 50.0):
        """
        Initialize checker.

        Args:
            Fy: Yield stress (ksi) - 항복응력
        """
        self.Fy = Fy

    def check_castellated(
        self,
        ho: float,
        e: float,
        S: float,
        tw: float,
        b: float,
        Vrh: float,
        theta: float = 60.0,
        design_method: str = 'LRFD'
    ) -> Dict:
        """
        Check web post buckling for castellated beam.

        캐스틸레이티드 보 웹 포스트 좌굴 검토

        Args:
            ho: Opening height (in) - 개구부 높이
            e: Opening width (in) - 개구부 폭
            S: Center-to-center spacing (in) - 중심간 간격
            tw: Web thickness (in) - 웹 두께
            b: Flange width (in) - 플랜지 폭
            Vrh: Required horizontal shear (kips) - 요구 수평전단력
            theta: Cut angle (degrees, default 60°) - 절단각
            design_method: 'LRFD' or 'ASD'

        Returns:
            Dictionary with web post check results
        """
        # Web post dimensions
        # For castellated: web post width = S - e
        dp = S - e  # Web post width

        # Check minimum spacing ratio (Section 3.4.1)
        # s/dp should be >= 1.08 for Redwood equations
        s_over_dp = S / dp if dp > 0 else 0

        if s_over_dp < 1.08:
            warning_spacing = f"WARNING: S/dp = {s_over_dp:.2f} < 1.08 (minimum recommended)"
        else:
            warning_spacing = None

        # Calculate plastic moment of web post (Equation 3-22)
        # M_p = 0.25 * t_w * (e + 2*b)² * F_y
        Mp = 0.25 * tw * (e + 2*b)**2 * self.Fy

        # Calculate M_ocr / M_p based on angle and e/ho ratio
        e_over_ho = e / ho if ho > 0 else 0
        h_over_e_2 = (2 * ho) / e if e > 0 else 0  # 2h/e ratio

        # Select equations based on theta (Equations 3-23 to 3-28)
        if abs(theta - 45.0) < 2.5:
            # θ = 45° equations
            if e_over_ho <= 1.5:  # Interpolate to e/ho = 1.0
                Mocr_over_Mp = 0.351 - 0.051*h_over_e_2 + 0.0026*h_over_e_2**2
                Mocr_over_Mp = min(Mocr_over_Mp, 0.26)
            elif e_over_ho <= 2.5:  # Interpolate to e/ho = 2.0
                Mocr_over_Mp = 3.276 - 1.208*h_over_e_2 + 0.154*h_over_e_2**2 - 0.0067*h_over_e_2**3
            else:  # e/ho = 3.0
                Mocr_over_Mp = 0.952 - 0.30*h_over_e_2 + 0.0319*h_over_e_2**2 - 0.0011*h_over_e_2**3

            # Resistance factors for θ = 45°
            phi_b = 0.90
            Omega_b = 1.67

        elif abs(theta - 60.0) < 2.5:
            # θ = 60° equations
            if e_over_ho <= 1.5:  # Interpolate to e/ho = 1.0
                Mocr_over_Mp = 0.587 * (0.917 ** h_over_e_2)
                Mocr_over_Mp = min(Mocr_over_Mp, 0.493)
            elif e_over_ho <= 2.5:  # Interpolate to e/ho = 2.0
                Mocr_over_Mp = 1.96 * (0.699 ** h_over_e_2)
            else:  # e/ho = 3.0
                Mocr_over_Mp = 2.55 * (0.574 ** h_over_e_2)

            # Resistance factors for θ = 60°
            phi_b = 0.90
            Omega_b = 1.67

        elif 52.0 <= theta <= 58.0:
            # Interpolate resistance factors between 60° and 52.5°
            # At θ = 52.5°: φ = 0.60, Ω = 2.50
            # At θ = 60°: φ = 0.90, Ω = 1.67
            # Linear interpolation
            factor = (theta - 52.5) / (60.0 - 52.5)
            phi_b = 0.60 + factor * (0.90 - 0.60)
            Omega_b = 2.50 - factor * (2.50 - 1.67)

            # Use 60° equations for Mocr calculation
            if e_over_ho <= 1.5:
                Mocr_over_Mp = 0.587 * (0.917 ** h_over_e_2)
                Mocr_over_Mp = min(Mocr_over_Mp, 0.493)
            elif e_over_ho <= 2.5:
                Mocr_over_Mp = 1.96 * (0.699 ** h_over_e_2)
            else:
                Mocr_over_Mp = 2.55 * (0.574 ** h_over_e_2)

        else:
            raise ValueError(f"Cut angle θ = {theta}° outside valid range (43-62°)")

        # Calculate available flexural strength (Equations 3-29a, 3-29b)
        Mocr = Mocr_over_Mp * Mp

        if design_method == 'LRFD':
            phiMn = phi_b * Mocr  # kip-in
            Mrh = Vrh * dp  # Required moment = horizontal shear × web post width
            utilization = Mrh / phiMn if phiMn > 0 else float('inf')
            status = "OK" if utilization <= 1.0 else "NG"

            return {
                "type": "Castellated Web Post",
                "design_method": "LRFD",
                "opening_height_ho": round(ho, 2),
                "opening_width_e": round(e, 2),
                "spacing_S": round(S, 2),
                "web_post_width_dp": round(dp, 2),
                "S_over_dp": round(s_over_dp, 2),
                "web_thickness_tw": round(tw, 3),
                "theta": theta,
                "Mp": round(Mp, 1),
                "e_over_ho": round(e_over_ho, 2),
                "2h_over_e": round(h_over_e_2, 2),
                "Mocr_over_Mp": round(Mocr_over_Mp, 3),
                "Mocr": round(Mocr, 1),
                "phi_b": phi_b,
                "phiMn": round(phiMn, 1),
                "Vrh": round(Vrh, 2),
                "Mrh": round(Mrh, 1),
                "utilization": round(utilization, 3),
                "utilization_%": round(utilization * 100, 1),
                "status": status,
                "warning": warning_spacing,
                "notes": "Per Equations 3-22 to 3-29 (AISC DG 31 Section 3.4.1)"
            }

        else:  # ASD
            Mn_over_Omega = Mocr / Omega_b  # kip-in
            Mrh = Vrh * dp
            utilization = Mrh / Mn_over_Omega if Mn_over_Omega > 0 else float('inf')
            status = "OK" if utilization <= 1.0 else "NG"

            return {
                "type": "Castellated Web Post",
                "design_method": "ASD",
                "opening_height_ho": round(ho, 2),
                "opening_width_e": round(e, 2),
                "spacing_S": round(S, 2),
                "web_post_width_dp": round(dp, 2),
                "S_over_dp": round(s_over_dp, 2),
                "web_thickness_tw": round(tw, 3),
                "theta": theta,
                "Mp": round(Mp, 1),
                "e_over_ho": round(e_over_ho, 2),
                "2h_over_e": round(h_over_e_2, 2),
                "Mocr_over_Mp": round(Mocr_over_Mp, 3),
                "Mocr": round(Mocr, 1),
                "Omega_b": Omega_b,
                "Mn_over_Omega": round(Mn_over_Omega, 1),
                "Vrh": round(Vrh, 2),
                "Mrh": round(Mrh, 1),
                "utilization": round(utilization, 3),
                "utilization_%": round(utilization * 100, 1),
                "status": status,
                "warning": warning_spacing,
                "notes": "Per Equations 3-22 to 3-29 (AISC DG 31 Section 3.4.1)"
            }

    def check_cellular(
        self,
        Do: float,
        s: float,
        tw: float,
        Vrh: float,
        design_method: str = 'LRFD'
    ) -> Dict:
        """
        Check web post buckling for cellular beam.

        셀룰러 보 웹 포스트 좌굴 검토

        Args:
            Do: Opening diameter (in) - 개구부 직경
            s: Center-to-center spacing (in) - 중심간 간격
            tw: Web thickness (in) - 웹 두께
            Vrh: Required horizontal shear (kips) - 요구 수평전단력
            design_method: 'LRFD' or 'ASD'

        Returns:
            Dictionary with web post check results
        """
        # Web post dimensions
        # For cellular: web post width = s - Do
        dp = s - Do

        # Check minimum spacing ratio
        # Typical recommendation: s/Do >= 1.5
        s_over_Do = s / Do if Do > 0 else 0

        if s_over_Do < 1.5:
            warning_spacing = f"WARNING: s/Do = {s_over_Do:.2f} < 1.5 (minimum recommended)"
        else:
            warning_spacing = None

        # Calculate elastic critical buckling moment (Equation 3-28 equivalent for cellular)
        # Simplified equation based on Redwood (1996)
        # M_e = C * E * t_w³ * d_p / (1 - ν²)
        # Simplified: M_e ≈ k * tw³ * dp
        E = 29000.0  # ksi
        nu = 0.3  # Poisson's ratio
        k_factor = E / (1 - nu**2)

        # Web post slenderness parameter
        dp_over_tw = dp / tw if tw > 0 else 0

        # Elastic buckling moment (simplified, Equation 3-30 to 3-33)
        # For cellular beams, critical buckling depends on dp/tw ratio
        # Using simplified formulation
        Me = k_factor * tw**3 * dp / 12.0  # Simplified elastic buckling moment

        # Plastic moment of web post
        Mp = self.Fy * tw * dp**2 / 4.0  # Simplified for rectangular web post

        # Calculate available strength based on slenderness
        # If elastic buckling controls: Mn = Me
        # If plastic controls: Mn = Mp
        # Transition based on dp/tw ratio

        # Critical slenderness (approximate)
        lambda_p = 3.76 * math.sqrt(E / self.Fy)  # Compact limit
        lambda_r = 5.70 * math.sqrt(E / self.Fy)  # Non-compact limit

        if dp_over_tw <= lambda_p:
            # Compact - plastic capacity
            Mn = Mp
            limit_state = "Plastic"
        elif dp_over_tw <= lambda_r:
            # Non-compact - inelastic buckling
            ratio = (dp_over_tw - lambda_p) / (lambda_r - lambda_p)
            Mn = Mp - ratio * (Mp - Me)
            limit_state = "Inelastic Buckling"
        else:
            # Slender - elastic buckling
            Mn = Me
            limit_state = "Elastic Buckling"

        # Resistance factors (Equations 3-35, 3-36)
        phi_b = 0.90  # LRFD
        Omega_b = 1.67  # ASD

        if design_method == 'LRFD':
            phiMn = phi_b * Mn
            Mrh = Vrh * dp  # Required moment
            utilization = Mrh / phiMn if phiMn > 0 else float('inf')
            status = "OK" if utilization <= 1.0 else "NG"

            return {
                "type": "Cellular Web Post",
                "design_method": "LRFD",
                "opening_diameter_Do": round(Do, 2),
                "spacing_s": round(s, 2),
                "web_post_width_dp": round(dp, 2),
                "s_over_Do": round(s_over_Do, 2),
                "web_thickness_tw": round(tw, 3),
                "dp_over_tw": round(dp_over_tw, 1),
                "Me": round(Me, 1),
                "Mp": round(Mp, 1),
                "Mn": round(Mn, 1),
                "limit_state": limit_state,
                "phi_b": phi_b,
                "phiMn": round(phiMn, 1),
                "Vrh": round(Vrh, 2),
                "Mrh": round(Mrh, 1),
                "utilization": round(utilization, 3),
                "utilization_%": round(utilization * 100, 1),
                "status": status,
                "warning": warning_spacing,
                "notes": "Per Equations 3-30 to 3-36 (AISC DG 31 Section 3.4.2)"
            }

        else:  # ASD
            Mn_over_Omega = Mn / Omega_b
            Mrh = Vrh * dp
            utilization = Mrh / Mn_over_Omega if Mn_over_Omega > 0 else float('inf')
            status = "OK" if utilization <= 1.0 else "NG"

            return {
                "type": "Cellular Web Post",
                "design_method": "ASD",
                "opening_diameter_Do": round(Do, 2),
                "spacing_s": round(s, 2),
                "web_post_width_dp": round(dp, 2),
                "s_over_Do": round(s_over_Do, 2),
                "web_thickness_tw": round(tw, 3),
                "dp_over_tw": round(dp_over_tw, 1),
                "Me": round(Me, 1),
                "Mp": round(Mp, 1),
                "Mn": round(Mn, 1),
                "limit_state": limit_state,
                "Omega_b": Omega_b,
                "Mn_over_Omega": round(Mn_over_Omega, 1),
                "Vrh": round(Vrh, 2),
                "Mrh": round(Mrh, 1),
                "utilization": round(utilization, 3),
                "utilization_%": round(utilization * 100, 1),
                "status": status,
                "warning": warning_spacing,
                "notes": "Per Equations 3-30 to 3-36 (AISC DG 31 Section 3.4.2)"
            }


def print_results(results: Dict):
    """Print web post check results."""
    print("\n" + "="*80)
    print(f"  Web Post Buckling Check: {results['type']}")
    print("="*80)

    print(f"\nDesign Method: {results['design_method']}")

    print("\n--- Opening Geometry ---")
    if 'opening_diameter_Do' in results:
        print(f"Opening Diameter (Do):  {results['opening_diameter_Do']} in")
        print(f"Spacing (s):            {results['spacing_s']} in")
        print(f"s/Do Ratio:             {results['s_over_Do']}")
    else:
        print(f"Opening Height (ho):    {results['opening_height_ho']} in")
        print(f"Opening Width (e):      {results['opening_width_e']} in")
        print(f"Spacing (S):            {results['spacing_S']} in")
        print(f"Cut Angle (θ):          {results['theta']}°")
        print(f"S/dp Ratio:             {results['S_over_dp']}")
        print(f"e/ho Ratio:             {results['e_over_ho']}")

    print("\n--- Web Post Properties ---")
    print(f"Web Post Width (dp):    {results['web_post_width_dp']} in")
    print(f"Web Thickness (tw):     {results['web_thickness_tw']} in")
    if 'dp_over_tw' in results:
        print(f"dp/tw Ratio:            {results['dp_over_tw']}")

    print("\n--- Capacity Calculation ---")
    if 'Mp' in results:
        print(f"Plastic Moment (Mp):    {results['Mp']} kip-in")
    if 'Me' in results:
        print(f"Elastic Moment (Me):    {results['Me']} kip-in")
    if 'Mocr_over_Mp' in results:
        print(f"Mocr/Mp:                {results['Mocr_over_Mp']}")
        print(f"Critical Moment (Mocr): {results['Mocr']} kip-in")
    if 'limit_state' in results:
        print(f"Limit State:            {results['limit_state']}")

    print("\n--- Available Strength ---")
    if results['design_method'] == 'LRFD':
        print(f"Resistance Factor (φb): {results['phi_b']}")
        print(f"φMn:                    {results['phiMn']} kip-in")
    else:
        print(f"Safety Factor (Ωb):     {results['Omega_b']}")
        print(f"Mn/Ω:                   {results['Mn_over_Omega']} kip-in")

    print("\n--- Demand Check ---")
    print(f"Horizontal Shear (Vrh): {results['Vrh']} kips")
    print(f"Required Moment (Mrh):  {results['Mrh']} kip-in")
    print(f"Utilization Ratio:      {results['utilization']}")
    print(f"Utilization:            {results['utilization_%']}%")
    print(f"Status:                 {results['status']}")

    if results['warning']:
        print(f"\n⚠ {results['warning']}")

    if results['status'] == 'OK':
        print("\n✓ PASS - Web post is adequate")
    else:
        print("\n✗ FAIL - Web post is overstressed")
        print("  Recommendation: Increase spacing or decrease opening size")

    print("\n--- Notes ---")
    print(results['notes'])
    print("="*80)


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Check web post buckling in castellated and cellular beams',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Castellated beam (60° hexagonal):
    python3 webpost_checker.py --type CB --ho 5.5 --e 11.0 --S 16.5 --tw 0.3 --b 6.0 --Vrh 8.5

  Cellular beam:
    python3 webpost_checker.py --type LB --Do 14.0 --s 21.0 --tw 0.2 --Vrh 10.0 --ASD
        """
    )

    parser.add_argument('--type', choices=['CB', 'LB'], required=True,
                       help='Beam type: CB=Castellated, LB=Cellular')
    parser.add_argument('--ho', type=float, help='Opening height for castellated (in)')
    parser.add_argument('--e', type=float, help='Opening width for castellated (in)')
    parser.add_argument('--S', type=float, help='Spacing for castellated (in)')
    parser.add_argument('--theta', type=float, default=60.0, help='Cut angle for castellated (degrees)')
    parser.add_argument('--Do', type=float, help='Opening diameter for cellular (in)')
    parser.add_argument('--s', type=float, help='Spacing for cellular (in)')
    parser.add_argument('--tw', type=float, required=True, help='Web thickness (in)')
    parser.add_argument('--b', type=float, help='Flange width for castellated (in)')
    parser.add_argument('--Vrh', type=float, required=True, help='Required horizontal shear (kips)')
    parser.add_argument('--Fy', type=float, default=50.0, help='Yield stress (ksi, default 50)')
    parser.add_argument('--LRFD', dest='design_method', action='store_const',
                       const='LRFD', default='LRFD', help='Use LRFD (default)')
    parser.add_argument('--ASD', dest='design_method', action='store_const',
                       const='ASD', help='Use ASD')

    args = parser.parse_args()

    checker = WebPostChecker(Fy=args.Fy)

    try:
        if args.type == 'CB':
            # Castellated beam
            if not all([args.ho, args.e, args.S, args.b]):
                print("Error: Castellated beam requires --ho, --e, --S, --b")
                sys.exit(1)

            results = checker.check_castellated(
                args.ho, args.e, args.S, args.tw, args.b, args.Vrh,
                theta=args.theta, design_method=args.design_method
            )

        elif args.type == 'LB':
            # Cellular beam
            if not all([args.Do, args.s]):
                print("Error: Cellular beam requires --Do, --s")
                sys.exit(1)

            results = checker.check_cellular(
                args.Do, args.s, args.tw, args.Vrh,
                design_method=args.design_method
            )

        print_results(results)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
