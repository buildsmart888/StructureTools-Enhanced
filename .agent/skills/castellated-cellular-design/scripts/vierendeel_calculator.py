#!/usr/bin/env python3
"""
Vierendeel Bending Calculator for Castellated and Cellular Beams
=================================================================

Calculate Vierendeel bending moments, axial forces, and interaction ratios
at web openings per AISC Design Guide 31.

비렌딜 휨 계산기 - 캐스틸레이티드 및 셀룰러 보
AISC Design Guide 31에 따른 개구부에서의 비렌딜 휨모멘트, 축력, 상호작용비 계산

Usage:
    python3 vierendeel_calculator.py --shear 25.0 --type CB --opening-width 11.0 --Atee 5.5 --deffec 16.0
    python3 vierendeel_calculator.py --shear 30.0 --type LB --diameter 14.0 --composite --Fy 50
    python3 vierendeel_calculator.py --interactive

Key Formulas:
    Noncomposite: Equations 3-3 to 3-8 (Section 3.2)
    Composite: Equations 3-10 to 3-18 (Section 3.3)
    Interaction: AISC Specification H1-1a, H1-1b
"""

import sys
import argparse
import math
from typing import Dict, Optional


class VierendeelCalculator:
    """
    Calculate Vierendeel bending effects in castellated and cellular beams.
    """

    def __init__(self, Fy: float = 50.0):
        """
        Initialize calculator.

        Args:
            Fy: Yield stress (ksi) - 항복응력
        """
        self.Fy = Fy

    def calculate_noncomposite_castellated(
        self,
        Vr: float,
        e: float,
        Atee: float,
        deffec: float,
        Itee: float = None,
        Stee: float = None,
        design_method: str = 'LRFD'
    ) -> Dict:
        """
        Calculate Vierendeel bending for noncomposite castellated beam.

        비합성 캐스틸레이티드 보의 비렌딜 휨 계산

        Args:
            Vr: Required global shear force (kips) - 요구 전단력
            e: Opening width (in) - 개구부 폭
            Atee: Tee section area (in²) - 티 단면적
            deffec: Effective depth between tee centroids (in) - 유효깊이
            Itee: Tee moment of inertia (in⁴) - 티 단면2차모멘트
            Stee: Tee section modulus (in³) - 티 단면계수
            design_method: 'LRFD' or 'ASD'

        Returns:
            Dictionary with Vierendeel moments and forces
        """
        # Vierendeel moment (Equation 3-7 for castellated)
        # M_vr = V_r * (e/2) for castellated beams
        Mvr = Vr * (e / 2.0)

        # For symmetric sections, top and bottom are equal
        Mvr_top = Mvr
        Mvr_bot = Mvr

        # Note: In actual design, M_vr is distributed between top and bottom
        # based on relative stiffness. For symmetric sections, it's 50/50.

        return {
            "type": "Noncomposite Castellated",
            "design_method": design_method,
            "Vr": round(Vr, 2),
            "opening_width_e": round(e, 2),
            "Mvr_top": round(Mvr_top, 2),
            "Mvr_bot": round(Mvr_bot, 2),
            "Atee": round(Atee, 2),
            "deffec": round(deffec, 2),
            "Fy": self.Fy,
            "notes": "Per Equations 3-3 to 3-8 (AISC DG 31 Section 3.2)"
        }

    def calculate_noncomposite_cellular(
        self,
        Vr: float,
        Do: float,
        Atee_crit: float,
        deffec_crit: float,
        design_method: str = 'LRFD'
    ) -> Dict:
        """
        Calculate Vierendeel bending for noncomposite cellular beam.

        비합성 셀룰러 보의 비렌딜 휨 계산

        Args:
            Vr: Required global shear force (kips) - 요구 전단력
            Do: Opening diameter (in) - 개구부 직경
            Atee_crit: Critical tee section area (in²) - 임계 티 단면적
            deffec_crit: Effective depth at critical section (in) - 임계 유효깊이
            design_method: 'LRFD' or 'ASD'

        Returns:
            Dictionary with Vierendeel moments and forces
        """
        # Vierendeel moment (Equation 3-8 for cellular)
        # Critical section is located 0.225*Do from opening center
        # M_vr = V_r * (Do/4) at critical location
        Mvr = Vr * (Do / 4.0)

        Mvr_top = Mvr
        Mvr_bot = Mvr

        return {
            "type": "Noncomposite Cellular",
            "design_method": design_method,
            "Vr": round(Vr, 2),
            "opening_diameter_Do": round(Do, 2),
            "Mvr_top": round(Mvr_top, 2),
            "Mvr_bot": round(Mvr_bot, 2),
            "Atee_crit": round(Atee_crit, 2),
            "deffec_crit": round(deffec_crit, 2),
            "Fy": self.Fy,
            "critical_location": f"0.225*Do = {round(0.225*Do, 2)} in from opening center",
            "notes": "Per Equations 3-3 to 3-8 (AISC DG 31 Section 3.2)"
        }

    def calculate_composite_castellated(
        self,
        Vr: float,
        e: float,
        Atee: float,
        Ag: float,
        deffec: float,
        Mr: float,
        Xt: float = None,
        q: float = 1.0,
        Vc: float = 0.0,
        design_method: str = 'LRFD'
    ) -> Dict:
        """
        Calculate Vierendeel bending for composite castellated beam.

        합성 캐스틸레이티드 보의 비렌딜 휨 계산

        Args:
            Vr: Required global shear force (kips) - 요구 전단력
            e: Opening width (in) - 개구부 폭
            Atee: Tee section area (in²) - 티 단면적
            Ag: Gross section area (in²) - 총 단면적
            deffec: Effective depth (in) - 유효깊이
            Mr: Required global moment (kip-ft) - 요구 휨모멘트
            Xt: Distance from top of steel to composite PNA (in) - 합성 중립축 위치
            q: Degree of composite action (0 to 1) - 합성도
            Vc: Available concrete shear strength (kips) - 콘크리트 전단강도
            design_method: 'LRFD' or 'ASD'

        Returns:
            Dictionary with composite Vierendeel analysis
        """
        # Net shear after concrete contribution (Equation 3-16)
        Vr_net = Vr - Vc

        # Vierendeel moment (Equation 3-17 for composite castellated)
        # M_vr = V_r,net * (A_tee / A_g) * (e/2)
        Mvr = Vr_net * (Atee / Ag) * (e / 2.0)

        # For composite sections, calculate axial forces if Xt provided
        if Xt is not None:
            # Axial force calculations (Equations 3-10 to 3-13)
            # Simplified - actual implementation would be more complex
            Mt = Mr * 12.0  # Convert to kip-in

            # T0 = Mt * [1 - q*Xt/T1] / deffec (Equation 3-12)
            # T1 = q*Xt + T0 (Equation 3-13)
            # This is iterative, simplified here:
            T0_approx = Mt / deffec
            T1_approx = T0_approx

            axial_forces = {
                "T0_top": round(T0_approx, 2),
                "T1_bot": round(T1_approx, 2),
                "composite_PNA_Xt": round(Xt, 2) if Xt else "N/A"
            }
        else:
            axial_forces = {
                "T0_top": "Not calculated",
                "T1_bot": "Not calculated",
                "composite_PNA_Xt": "Not provided"
            }

        return {
            "type": "Composite Castellated",
            "design_method": design_method,
            "Vr": round(Vr, 2),
            "Vc": round(Vc, 2),
            "Vr_net": round(Vr_net, 2),
            "opening_width_e": round(e, 2),
            "Mvr_top": round(Mvr, 2),
            "Mvr_bot": round(Mvr, 2),
            "composite_degree_q": q,
            "Atee": round(Atee, 2),
            "Ag": round(Ag, 2),
            "deffec": round(deffec, 2),
            "Fy": self.Fy,
            "axial_forces": axial_forces,
            "notes": "Per Equations 3-10 to 3-18 (AISC DG 31 Section 3.3)"
        }

    def calculate_composite_cellular(
        self,
        Vr: float,
        Do: float,
        Atee_crit: float,
        Acrit: float,
        deffec_crit: float,
        Vc: float = 0.0,
        design_method: str = 'LRFD'
    ) -> Dict:
        """
        Calculate Vierendeel bending for composite cellular beam.

        합성 셀룰러 보의 비렌딜 휨 계산

        Args:
            Vr: Required global shear force (kips) - 요구 전단력
            Do: Opening diameter (in) - 개구부 직경
            Atee_crit: Critical tee area (in²) - 임계 티 단면적
            Acrit: Sum of top and bottom critical areas (in²) - 임계 단면 총 면적
            deffec_crit: Effective depth at critical section (in) - 임계 유효깊이
            Vc: Available concrete shear strength (kips) - 콘크리트 전단강도
            design_method: 'LRFD' or 'ASD'

        Returns:
            Dictionary with composite cellular Vierendeel analysis
        """
        # Net shear after concrete contribution
        Vr_net = Vr - Vc

        # Vierendeel moment (Equation 3-18 for composite cellular)
        # M_vr = V_r,net * (A_tee-crit / A_crit) * (Do/4)
        Mvr = Vr_net * (Atee_crit / Acrit) * (Do / 4.0)

        return {
            "type": "Composite Cellular",
            "design_method": design_method,
            "Vr": round(Vr, 2),
            "Vc": round(Vc, 2),
            "Vr_net": round(Vr_net, 2),
            "opening_diameter_Do": round(Do, 2),
            "Mvr_top": round(Mvr, 2),
            "Mvr_bot": round(Mvr, 2),
            "Atee_crit": round(Atee_crit, 2),
            "Acrit": round(Acrit, 2),
            "deffec_crit": round(deffec_crit, 2),
            "Fy": self.Fy,
            "critical_location": f"0.225*Do = {round(0.225*Do, 2)} in from opening center",
            "notes": "Per Equations 3-10 to 3-18 (AISC DG 31 Section 3.3)"
        }

    def check_interaction(
        self,
        Pr: float,
        Pn: float,
        Mr: float,
        Mn: float,
        phi: float = 0.9,
        Omega: float = 1.67,
        design_method: str = 'LRFD'
    ) -> Dict:
        """
        Check AISC combined axial and flexural interaction (H1-1a, H1-1b).

        AISC 축력 및 휨 상호작용 검토

        Args:
            Pr: Required axial force (kips) - 요구 축력
            Pn: Nominal axial capacity (kips) - 공칭 축력 강도
            Mr: Required moment (kip-ft or kip-in) - 요구 휨모멘트
            Mn: Nominal moment capacity (kip-ft or kip-in) - 공칭 휨강도
            phi: Resistance factor for LRFD - 저항계수
            Omega: Safety factor for ASD - 안전계수
            design_method: 'LRFD' or 'ASD'

        Returns:
            Dictionary with interaction check results
        """
        if design_method == 'LRFD':
            # Available strengths
            phiPn = phi * Pn
            phiMn = phi * Mn

            # Interaction ratio
            Pr_ratio = Pr / phiPn if phiPn > 0 else 0
            Mr_ratio = Mr / phiMn if phiMn > 0 else 0

            # AISC H1-1a: If Pr/phiPn >= 0.2
            if Pr_ratio >= 0.2:
                interaction = Pr_ratio + (8.0/9.0) * Mr_ratio
                equation = "H1-1a"
            else:
                # AISC H1-1b: If Pr/phiPn < 0.2
                interaction = Pr_ratio / 2.0 + Mr_ratio
                equation = "H1-1b"

            status = "OK" if interaction <= 1.0 else "NG"
            utilization = interaction * 100.0

            return {
                "design_method": "LRFD",
                "Pr": round(Pr, 2),
                "phiPn": round(phiPn, 2),
                "Pr_ratio": round(Pr_ratio, 3),
                "Mr": round(Mr, 2),
                "phiMn": round(phiMn, 2),
                "Mr_ratio": round(Mr_ratio, 3),
                "interaction_ratio": round(interaction, 3),
                "equation": equation,
                "utilization_%": round(utilization, 1),
                "status": status
            }

        else:  # ASD
            # Allowable strengths
            Pn_Omega = Pn / Omega
            Mn_Omega = Mn / Omega

            # Interaction ratio
            Pr_ratio = Pr / Pn_Omega if Pn_Omega > 0 else 0
            Mr_ratio = Mr / Mn_Omega if Mn_Omega > 0 else 0

            # AISC H1-1a: If Pr/(Pn/Omega) >= 0.2
            if Pr_ratio >= 0.2:
                interaction = Pr_ratio + (8.0/9.0) * Mr_ratio
                equation = "H1-1a"
            else:
                # AISC H1-1b: If Pr/(Pn/Omega) < 0.2
                interaction = Pr_ratio / 2.0 + Mr_ratio
                equation = "H1-1b"

            status = "OK" if interaction <= 1.0 else "NG"
            utilization = interaction * 100.0

            return {
                "design_method": "ASD",
                "Pr": round(Pr, 2),
                "Pn_Omega": round(Pn_Omega, 2),
                "Pr_ratio": round(Pr_ratio, 3),
                "Mr": round(Mr, 2),
                "Mn_Omega": round(Mn_Omega, 2),
                "Mr_ratio": round(Mr_ratio, 3),
                "interaction_ratio": round(interaction, 3),
                "equation": equation,
                "utilization_%": round(utilization, 1),
                "status": status
            }


def print_results(results: Dict):
    """Print Vierendeel calculation results."""
    print("\n" + "="*80)
    print(f"  Vierendeel Bending Analysis: {results['type']}")
    print("="*80)

    print(f"\nDesign Method: {results['design_method']}")
    print(f"Yield Stress: {results['Fy']} ksi")

    print("\n--- Global Forces ---")
    print(f"Required Shear (Vr):    {results['Vr']} kips")

    if 'Vc' in results and results['Vc'] > 0:
        print(f"Concrete Shear (Vc):    {results['Vc']} kips")
        print(f"Net Shear (Vr,net):     {results['Vr_net']} kips")

    print("\n--- Opening Geometry ---")
    if 'opening_width_e' in results:
        print(f"Opening Width (e):      {results['opening_width_e']} in")
    if 'opening_diameter_Do' in results:
        print(f"Opening Diameter (Do):  {results['opening_diameter_Do']} in")
        print(f"Critical Location:      {results.get('critical_location', 'N/A')}")

    print("\n--- Vierendeel Moments ---")
    print(f"Top Tee (Mvr,top):      {results['Mvr_top']} kip-in")
    print(f"Bottom Tee (Mvr,bot):   {results['Mvr_bot']} kip-in")

    if 'axial_forces' in results:
        print("\n--- Axial Forces ---")
        af = results['axial_forces']
        print(f"Top Tee (T0):           {af['T0_top']} kips")
        print(f"Bottom Tee (T1):        {af['T1_bot']} kips")
        if af['composite_PNA_Xt'] != "Not provided":
            print(f"Composite PNA (Xt):     {af['composite_PNA_Xt']} in")

    print("\n--- Notes ---")
    print(results['notes'])
    print("="*80)


def print_interaction_results(results: Dict):
    """Print interaction check results."""
    print("\n" + "="*80)
    print(f"  AISC Combined Forces Interaction Check")
    print("="*80)

    print(f"\nDesign Method: {results['design_method']}")
    print(f"Governing Equation: AISC {results['equation']}")

    print("\n--- Axial Force ---")
    print(f"Required (Pr):          {results['Pr']} kips")
    if results['design_method'] == 'LRFD':
        print(f"Available (φPn):        {results['phiPn']} kips")
    else:
        print(f"Allowable (Pn/Ω):      {results['Pn_Omega']} kips")
    print(f"Ratio (Pr/Pn):          {results['Pr_ratio']}")

    print("\n--- Flexural Moment ---")
    print(f"Required (Mr):          {results['Mr']} kip-in")
    if results['design_method'] == 'LRFD':
        print(f"Available (φMn):        {results['phiMn']} kip-in")
    else:
        print(f"Allowable (Mn/Ω):      {results['Mn_Omega']} kip-in")
    print(f"Ratio (Mr/Mn):          {results['Mr_ratio']}")

    print("\n--- Interaction Check ---")
    print(f"Interaction Ratio:      {results['interaction_ratio']}")
    print(f"Utilization:            {results['utilization_%']}%")
    print(f"Status:                 {results['status']}")

    if results['status'] == 'OK':
        print("\n✓ PASS - Section is adequate")
    else:
        print("\n✗ FAIL - Section is overstressed")

    print("="*80)


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Calculate Vierendeel bending in castellated and cellular beams',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Noncomposite castellated beam:
    python3 vierendeel_calculator.py --shear 25.0 --type CB --opening-width 11.0 --Atee 5.5 --deffec 16.0

  Composite cellular beam:
    python3 vierendeel_calculator.py --shear 30.0 --type LB --diameter 14.0 --composite --Vc 5.0

  Interaction check:
    python3 vierendeel_calculator.py --interaction --Pr 50 --Pn 120 --Mr 80 --Mn 150
        """
    )

    parser.add_argument('--shear', type=float, help='Required global shear Vr (kips)')
    parser.add_argument('--type', choices=['CB', 'LB'], help='Beam type: CB=Castellated, LB=Cellular')
    parser.add_argument('--opening-width', type=float, help='Opening width e for castellated (in)')
    parser.add_argument('--diameter', type=float, help='Opening diameter Do for cellular (in)')
    parser.add_argument('--Atee', type=float, help='Tee section area (in²)')
    parser.add_argument('--deffec', type=float, help='Effective depth (in)')
    parser.add_argument('--composite', action='store_true', help='Composite beam')
    parser.add_argument('--Vc', type=float, default=0.0, help='Concrete shear strength (kips)')
    parser.add_argument('--Ag', type=float, help='Gross section area for composite (in²)')
    parser.add_argument('--Fy', type=float, default=50.0, help='Yield stress (ksi, default 50)')
    parser.add_argument('--design-method', choices=['LRFD', 'ASD'], default='LRFD', help='Design method')

    # Interaction check parameters
    parser.add_argument('--interaction', action='store_true', help='Perform interaction check only')
    parser.add_argument('--Pr', type=float, help='Required axial force (kips)')
    parser.add_argument('--Pn', type=float, help='Nominal axial capacity (kips)')
    parser.add_argument('--Mr', type=float, help='Required moment (kip-in)')
    parser.add_argument('--Mn', type=float, help='Nominal moment capacity (kip-in)')

    args = parser.parse_args()

    calc = VierendeelCalculator(Fy=args.Fy)

    # Interaction check mode
    if args.interaction:
        if not all([args.Pr, args.Pn, args.Mr, args.Mn]):
            print("Error: --interaction requires --Pr, --Pn, --Mr, --Mn")
            sys.exit(1)

        results = calc.check_interaction(
            args.Pr, args.Pn, args.Mr, args.Mn,
            design_method=args.design_method
        )
        print_interaction_results(results)
        return

    # Vierendeel calculation mode
    if not args.shear or not args.type:
        print("Error: --shear and --type required (or use --interaction)")
        parser.print_help()
        sys.exit(1)

    try:
        if args.type == 'CB':
            if not args.opening_width or not args.Atee or not args.deffec:
                print("Error: Castellated beam requires --opening-width, --Atee, --deffec")
                sys.exit(1)

            if args.composite:
                if not args.Ag:
                    print("Error: Composite beam requires --Ag")
                    sys.exit(1)
                results = calc.calculate_composite_castellated(
                    args.shear, args.opening_width, args.Atee, args.Ag,
                    args.deffec, Mr=0, Vc=args.Vc, design_method=args.design_method
                )
            else:
                results = calc.calculate_noncomposite_castellated(
                    args.shear, args.opening_width, args.Atee, args.deffec,
                    design_method=args.design_method
                )

        elif args.type == 'LB':
            if not args.diameter or not args.Atee or not args.deffec:
                print("Error: Cellular beam requires --diameter, --Atee, --deffec")
                sys.exit(1)

            if args.composite:
                Acrit = args.Ag if args.Ag else args.Atee * 2
                results = calc.calculate_composite_cellular(
                    args.shear, args.diameter, args.Atee, Acrit,
                    args.deffec, Vc=args.Vc, design_method=args.design_method
                )
            else:
                results = calc.calculate_noncomposite_cellular(
                    args.shear, args.diameter, args.Atee, args.deffec,
                    design_method=args.design_method
                )

        print_results(results)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
