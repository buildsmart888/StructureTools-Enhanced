#!/usr/bin/env python3
"""
Base plate preliminary sizing calculator.

Performs quick calculations for base plate bearing strength and thickness.

Usage:
    python3 base_plate_calculator.py --help

Examples:
    # LRFD compression-only design
    python3 base_plate_calculator.py --method lrfd --load 200 --fc 4000 --fy 36 --N 18 --B 14

    # ASD with confinement
    python3 base_plate_calculator.py --method asd --load 150 --fc 3000 --fy 36 --N 20 --B 16 --A2-factor 1.5
"""

import argparse
import math


def concrete_bearing_strength(method, A1, A2_factor, fc):
    """
    Calculate available concrete bearing strength per ACI 318.

    Args:
        method: 'lrfd' or 'asd'
        A1: Base plate area (in²)
        A2_factor: √(A2/A1) confinement factor (max 2.0)
        fc: Concrete compressive strength (psi)

    Returns:
        Available bearing strength (kips)
    """
    fc_ksi = fc / 1000.0  # Convert psi to ksi

    # Limit confinement factor
    A2_factor = min(A2_factor, 2.0)

    if method == 'lrfd':
        phi_c = 0.65
        # φP_p = φ × 0.85f'_c × A1 × √(A2/A1)
        Pp_confined = phi_c * 0.85 * fc_ksi * A1 * A2_factor
        # Maximum: φ × 1.7f'_c × A1
        Pp_max = phi_c * 1.7 * fc_ksi * A1
        return min(Pp_confined, Pp_max)
    else:  # ASD
        Omega_c = 2.31
        # P_p/Ω = (0.85f'_c × A1 × √(A2/A1)) / Ω
        Pp_confined = (0.85 * fc_ksi * A1 * A2_factor) / Omega_c
        # Maximum: (1.7f'_c × A1) / Ω
        Pp_max = (1.7 * fc_ksi * A1) / Omega_c
        return min(Pp_confined, Pp_max)


def plate_thickness_cantilever(P, fp_max, Fy, N, B, m):
    """
    Calculate required base plate thickness using cantilever method.

    Args:
        P: Axial load (kips)
        fp_max: Maximum bearing pressure (ksi)
        Fy: Plate yield stress (ksi)
        N, B: Plate dimensions (in)
        m: Cantilever dimension (in)

    Returns:
        Required plate thickness (in)
    """
    # Simplified cantilever approach
    # t_pl = m × sqrt(2P / (0.9 Fy B N))
    phi = 0.90
    t_reqd = m * math.sqrt((2 * P) / (phi * Fy * B * N))
    return t_reqd


def main():
    parser = argparse.ArgumentParser(
        description="Base plate preliminary sizing calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  LRFD compression design:
    python3 base_plate_calculator.py --method lrfd --load 200 --fc 4000 --fy 36 --N 18 --B 14

  ASD with confinement:
    python3 base_plate_calculator.py --method asd --load 150 --fc 3000 --fy 36 --N 20 --B 16 --A2-factor 1.5
        """
    )

    parser.add_argument("--method", choices=["lrfd", "asd"], required=True,
                       help="Design method (LRFD or ASD)")
    parser.add_argument("--load", type=float, required=True,
                       help="Axial compression load (kips)")
    parser.add_argument("--fc", type=float, required=True,
                       help="Concrete compressive strength f'c (psi)")
    parser.add_argument("--fy", type=float, default=36,
                       help="Base plate yield stress Fy (ksi, default: 36)")
    parser.add_argument("--N", type=float, required=True,
                       help="Base plate length N (in)")
    parser.add_argument("--B", type=float, required=True,
                       help="Base plate width B (in)")
    parser.add_argument("--A2-factor", type=float, default=1.0,
                       help="Confinement factor √(A2/A1) (default: 1.0, max: 2.0)")
    parser.add_argument("--column-depth", type=float,
                       help="Column depth d (in) for cantilever calc")
    parser.add_argument("--column-flange", type=float,
                       help="Column flange width bf (in) for cantilever calc")

    args = parser.parse_args()

    # Calculations
    A1 = args.N * args.B
    fc_ksi = args.fc / 1000.0

    print("=" * 70)
    print("BASE PLATE PRELIMINARY SIZING CALCULATOR")
    print("=" * 70)
    print()
    print("INPUT PARAMETERS:")
    print(f"  Design Method: {args.method.upper()}")
    print(f"  Axial Load: {args.load} kips")
    print(f"  Concrete Strength f'c: {args.fc} psi")
    print(f"  Plate Yield Stress Fy: {args.fy} ksi")
    print(f"  Base Plate Dimensions: {args.N}\" × {args.B}\"")
    print(f"  Base Plate Area A1: {A1:.1f} in²")
    print(f"  Confinement Factor √(A2/A1): {args.A2_factor}")
    print()

    # Concrete bearing strength
    Pp_avail = concrete_bearing_strength(args.method, A1, args.A2_factor, args.fc)

    print("CONCRETE BEARING STRENGTH:")
    if args.method == 'lrfd':
        print(f"  φP_p (available): {Pp_avail:.1f} kips")
        print(f"  P_u (required): {args.load:.1f} kips")
        ratio = args.load / Pp_avail
        status = "OK" if ratio <= 1.0 else "NG - INCREASE PLATE SIZE"
        print(f"  Utilization: {ratio:.2f} ({status})")
    else:
        print(f"  P_p/Ω (allowable): {Pp_avail:.1f} kips")
        print(f"  P_a (required): {args.load:.1f} kips")
        ratio = args.load / Pp_avail
        status = "OK" if ratio <= 1.0 else "NG - INCREASE PLATE SIZE"
        print(f"  Utilization: {ratio:.2f} ({status})")
    print()

    # Bearing pressure
    fp_actual = args.load / A1
    print("BEARING PRESSURE:")
    print(f"  Actual bearing pressure: {fp_actual:.3f} ksi")
    print(f"  Maximum (from bearing strength): {Pp_avail/A1:.3f} ksi")
    print()

    # Plate thickness (if column dimensions provided)
    if args.column_depth and args.column_flange:
        m = (args.N - 0.95 * args.column_depth) / 2.0
        n = (args.B - 0.80 * args.column_flange) / 2.0
        m_critical = max(m, n)

        t_reqd = plate_thickness_cantilever(args.load, fp_actual, args.fy,
                                            args.N, args.B, m_critical)

        print("PLATE THICKNESS (Simplified Cantilever Method):")
        print(f"  Column depth d: {args.column_depth}\"")
        print(f"  Column flange bf: {args.column_flange}\"")
        print(f"  Cantilever m: {m:.2f}\"")
        print(f"  Cantilever n: {n:.2f}\"")
        print(f"  Critical cantilever: {m_critical:.2f}\"")
        print(f"  Required thickness t_pl: {t_reqd:.3f}\"")
        print()

        # Suggest standard thickness
        standard_thicknesses = [0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0,
                               1.125, 1.25, 1.375, 1.5, 1.75, 2.0, 2.25, 2.5]
        t_selected = next((t for t in standard_thicknesses if t >= t_reqd), None)
        if t_selected:
            print(f"  Suggested standard thickness: {t_selected}\"")
        else:
            print(f"  Required thickness exceeds 2.5\" - check design")
        print()

    print("NOTES:")
    print("  - This is a preliminary sizing tool")
    print("  - For complete design, refer to Design Guide 1 Chapter 4")
    print("  - Check all applicable limit states")
    print("  - Consider moment and shear if applicable")
    if args.A2_factor > 1.0:
        print(f"  - Confinement factor {args.A2_factor} applied (verify A2 geometry)")
    print()
    print("=" * 70)

    return 0


if __name__ == "__main__":
    exit(main())
