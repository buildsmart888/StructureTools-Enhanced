#!/usr/bin/env python3
"""
Example matcher - finds relevant worked examples based on loading conditions.

Usage:
    python3 example_matcher.py [options]

Examples:
    python3 example_matcher.py --compression --shear
    python3 example_matcher.py --tension --moment
    python3 example_matcher.py --compression --moment --shear --biaxial
"""

import argparse
from typing import List, Dict

# Example database
EXAMPLES = [
    {
        "number": "4.7.1",
        "title": "Base Connection for Concentric Axial Compression Load (Small Base Plate, Confinement)",
        "page": "64-66",
        "loads": ["compression"],
        "features": ["confinement", "small_plate", "bearing"],
        "complexity": "basic",
        "keywords": ["compression", "bearing", "confinement", "A2/A1"]
    },
    {
        "number": "4.7.2",
        "title": "Base Connection for Concentric Axial Compression Load (Large Base Plate, Confinement)",
        "page": "67-69",
        "loads": ["compression"],
        "features": ["confinement", "large_plate", "bearing"],
        "complexity": "basic",
        "keywords": ["compression", "bearing", "confinement", "large plate"]
    },
    {
        "number": "4.7.3",
        "title": "Base Connection for Concentric Axial Compression (Small Base Plate)",
        "page": "70-75",
        "loads": ["compression"],
        "features": ["bearing"],
        "complexity": "basic",
        "keywords": ["compression", "bearing", "basic"]
    },
    {
        "number": "4.7.4",
        "title": "Base Connection for Concentric Shear Load",
        "page": "76-79",
        "loads": ["compression", "shear"],
        "features": ["friction"],
        "complexity": "intermediate",
        "keywords": ["shear", "friction", "clamping"]
    },
    {
        "number": "4.7.5",
        "title": "Base Connection for Concentric Shear Load (Shear Lug Design)",
        "page": "80-87",
        "loads": ["compression", "shear"],
        "features": ["shear_lug"],
        "complexity": "intermediate",
        "keywords": ["shear", "shear lug", "high shear"]
    },
    {
        "number": "4.7.6",
        "title": "Base Connection for Anchor Rod in Tension and Shear",
        "page": "88-90",
        "loads": ["tension", "shear"],
        "features": ["anchor_tension", "interaction"],
        "complexity": "intermediate",
        "keywords": ["tension", "shear", "anchor rod", "interaction"]
    },
    {
        "number": "4.7.7",
        "title": "Base Connection at Brace Connection to Column (Tension and Compression)",
        "page": "91-93",
        "loads": ["tension", "compression", "shear"],
        "features": ["braced_frame", "reversible"],
        "complexity": "advanced",
        "keywords": ["brace", "tension", "compression", "reversible"]
    },
    {
        "number": "4.7.8",
        "title": "Base Connection at Brace (Tension Only)",
        "page": "94-103",
        "loads": ["tension", "shear"],
        "features": ["braced_frame", "tension_only"],
        "complexity": "advanced",
        "keywords": ["brace", "tension", "uplift"]
    },
    {
        "number": "4.7.9",
        "title": "Base Connection for Eccentric Compression (Small Moment)",
        "page": "104-108",
        "loads": ["compression", "moment"],
        "features": ["small_moment", "uniform_bearing"],
        "complexity": "intermediate",
        "keywords": ["moment", "small moment", "eccentricity", "e ≤ e_crit"]
    },
    {
        "number": "4.7.10",
        "title": "Base Connection for Bending",
        "page": "109-112",
        "loads": ["moment"],
        "features": ["large_moment", "pure_bending"],
        "complexity": "intermediate",
        "keywords": ["bending", "pure moment", "large moment"]
    },
    {
        "number": "4.7.11",
        "title": "Base Connection for Bending and Axial Compression with Shear (Low Moment)",
        "page": "113-117",
        "loads": ["compression", "moment", "shear"],
        "features": ["small_moment", "friction"],
        "complexity": "advanced",
        "keywords": ["moment", "shear", "low moment", "compression"]
    },
    {
        "number": "4.7.12",
        "title": "Base Connection for Bending and Axial Compression with Shear (Large Moment)",
        "page": "118-124",
        "loads": ["compression", "moment", "shear"],
        "features": ["large_moment", "anchor_tension"],
        "complexity": "advanced",
        "keywords": ["moment", "shear", "large moment", "e > e_crit"]
    },
    {
        "number": "4.7.13",
        "title": "Base Connection for Biaxial Compression and Biaxial Bending (Large Moment)",
        "page": "125-130",
        "loads": ["compression", "moment", "biaxial"],
        "features": ["biaxial", "large_moment", "3D"],
        "complexity": "advanced",
        "keywords": ["biaxial", "3D", "biaxial moment"]
    },
    {
        "number": "4.7.14",
        "title": "Base Connection for Biaxial Tension and Biaxial Bending",
        "page": "131-133",
        "loads": ["tension", "moment", "biaxial"],
        "features": ["biaxial", "uplift", "all_tension"],
        "complexity": "advanced",
        "keywords": ["biaxial", "tension", "uplift", "biaxial moment"]
    },
    {
        "number": "4.7.15",
        "title": "Base Connection for Biaxial Bending, Biaxial Shear, and Axial Compression",
        "page": "134-140",
        "loads": ["compression", "moment", "shear", "biaxial"],
        "features": ["biaxial", "most_complex", "stiffener"],
        "complexity": "advanced",
        "keywords": ["biaxial", "shear", "moment", "compression", "stiffener", "most complex"]
    },
]


def match_examples(compression=False, tension=False, moment=False, shear=False, biaxial=False) -> List[Dict]:
    """
    Match examples based on loading conditions.
    """
    matches = []

    for example in EXAMPLES:
        score = 0
        loads = example["loads"]

        # Exact match for primary loads
        if compression and "compression" in loads:
            score += 10
        if tension and "tension" in loads:
            score += 10
        if moment and "moment" in loads:
            score += 10
        if shear and "shear" in loads:
            score += 10
        if biaxial and "biaxial" in loads:
            score += 15  # Biaxial is more specific

        # Bonus for feature matches
        if moment and "small_moment" in example["features"]:
            score += 5
        if moment and "large_moment" in example["features"]:
            score += 5
        if shear and "shear_lug" in example["features"]:
            score += 3
        if shear and "friction" in example["features"]:
            score += 3

        if score > 0:
            matches.append({
                "example": example,
                "score": score
            })

    # Sort by score (descending)
    matches.sort(key=lambda x: x["score"], reverse=True)

    return matches


def main():
    parser = argparse.ArgumentParser(
        description="Find relevant Design Guide 1 examples by loading conditions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Find examples with compression and shear:
    python3 example_matcher.py --compression --shear

  Find examples with tension and moment:
    python3 example_matcher.py --tension --moment

  Find biaxial loading examples:
    python3 example_matcher.py --biaxial

  Complex loading:
    python3 example_matcher.py --compression --moment --shear
        """
    )

    parser.add_argument("--compression", action="store_true",
                       help="Include axial compression")
    parser.add_argument("--tension", action="store_true",
                       help="Include axial tension/uplift")
    parser.add_argument("--moment", action="store_true",
                       help="Include bending moment")
    parser.add_argument("--shear", action="store_true",
                       help="Include shear force")
    parser.add_argument("--biaxial", action="store_true",
                       help="Include biaxial loading")
    parser.add_argument("--max-results", type=int, default=5,
                       help="Maximum number of results (default: 5)")

    args = parser.parse_args()

    # Check if any load specified
    if not any([args.compression, args.tension, args.moment, args.shear, args.biaxial]):
        print("Error: Please specify at least one loading condition.")
        print("Use --help for usage information.")
        return 1

    print("=" * 70)
    print("DESIGN GUIDE 1 - EXAMPLE MATCHER")
    print("=" * 70)
    print()

    print("SEARCH CRITERIA:")
    criteria = []
    if args.compression:
        criteria.append("Axial Compression")
    if args.tension:
        criteria.append("Axial Tension/Uplift")
    if args.moment:
        criteria.append("Bending Moment")
    if args.shear:
        criteria.append("Shear Force")
    if args.biaxial:
        criteria.append("Biaxial Loading")

    for criterion in criteria:
        print(f"  ✓ {criterion}")
    print()

    # Find matches
    matches = match_examples(
        compression=args.compression,
        tension=args.tension,
        moment=args.moment,
        shear=args.shear,
        biaxial=args.biaxial
    )

    if not matches:
        print("No matching examples found.")
        print()
        print("SUGGESTIONS:")
        print("  - Try different load combinations")
        print("  - Consider starting with simpler load cases")
        return 0

    print(f"FOUND {len(matches)} MATCHING EXAMPLE(S):")
    print()

    # Show top matches
    for i, match in enumerate(matches[:args.max_results], 1):
        example = match["example"]
        score = match["score"]

        print(f"{i}. Example {example['number']}: {example['title']}")
        print(f"   Page: {example['page']}")
        print(f"   Complexity: {example['complexity'].upper()}")
        print(f"   Load Components: {', '.join(example['loads'])}")
        if example['features']:
            print(f"   Key Features: {', '.join(example['features'])}")
        print(f"   Match Score: {score}")
        print()

    if len(matches) > args.max_results:
        print(f"... and {len(matches) - args.max_results} more example(s)")
        print()

    print("RECOMMENDED WORKFLOW:")
    if matches:
        first_match = matches[0]["example"]
        if first_match["complexity"] == "basic":
            print("  1. Start with the basic example above")
            print("  2. Understand the fundamental approach")
            print("  3. Adapt to your specific loading")
        elif first_match["complexity"] == "intermediate":
            print("  1. Review basic examples (4.7.1-4.7.3) first if needed")
            print("  2. Study the matched example above")
            print("  3. Apply to your design case")
        else:  # advanced
            print("  1. Start with simpler examples:")
            print("     - Compression only: Example 4.7.1")
            print("     - Add moment: Example 4.7.9 or 4.7.12")
            print("     - Add shear: Example 4.7.11")
            print("  2. Build understanding progressively")
            print("  3. Then tackle the complex example above")

    print()
    print("=" * 70)

    return 0


if __name__ == "__main__":
    exit(main())
