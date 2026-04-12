#!/usr/bin/env python3
"""
Example Matcher for Castellated and Cellular Beam Design
=========================================================

Match user design requirements to appropriate worked examples from AISC Design Guide 31.
Provides decision tree to select among Examples 4.1, 4.2, 4.3, and 4.4.

예제 매칭기 - 캐스틸레이티드 및 셀룰러 보 설계
사용자 설계 요구사항에 적합한 예제 선택

Usage:
    python3 example_matcher.py --composite --type CB
    python3 example_matcher.py --type LB
    python3 example_matcher.py --interactive
"""

import sys
import argparse
from pathlib import Path
from typing import Dict, Optional

# Example metadata
EXAMPLES = {
    '4.1': {
        'title': 'Example 4.1: Noncomposite Castellated Beam',
        'file': 'Example_4-1_Noncomposite_Castellated.md',
        'composite': False,
        'beam_type': 'CB',
        'parent_section': 'W18x35',
        'expanded_section': 'CB27x35',
        'opening': 'Hexagonal (60°)',
        'span': '60 ft',
        'description': 'Simply supported noncomposite castellated beam with hexagonal openings',
        'key_checks': [
            'Vierendeel bending (Section 3.2)',
            'Web post buckling (Section 3.4.1)',
            'Vertical shear (Section 3.5)',
            'Lateral-torsional buckling (Section 3.6)',
            'Deflection (Section 3.7)',
        ],
    },
    '4.2': {
        'title': 'Example 4.2: Noncomposite Cellular Beam',
        'file': 'Example_4-2_Noncomposite_Cellular.md',
        'composite': False,
        'beam_type': 'LB',
        'parent_section': 'W21x44',
        'expanded_section': 'LB32x44',
        'opening': 'Circular',
        'span': '50 ft',
        'description': 'Simply supported noncomposite cellular beam with circular openings',
        'key_checks': [
            'Vierendeel bending (Section 3.2)',
            'Web post buckling (Section 3.4.2)',
            'Vertical shear (Section 3.5)',
            'Lateral-torsional buckling (Section 3.6)',
            'Deflection (Section 3.7)',
        ],
    },
    '4.3': {
        'title': 'Example 4.3: Composite Castellated Beam',
        'file': 'Example_4-3_Composite_Castellated.md',
        'composite': True,
        'beam_type': 'CB',
        'parent_section': 'W18x35',
        'expanded_section': 'CB27x35',
        'opening': 'Hexagonal (60°)',
        'span': '60 ft',
        'deck': '3-inch deck + 2.5-inch concrete',
        'description': 'Composite castellated beam with concrete deck and hexagonal openings',
        'key_checks': [
            'Composite PNA location',
            'Vierendeel bending (Section 3.3)',
            'Concrete deck shear contribution',
            'Web post buckling (Section 3.4.1)',
            'Vertical shear (Section 3.5)',
            'Deflection (Section 3.7)',
        ],
    },
    '4.4': {
        'title': 'Example 4.4: Composite Cellular Beam',
        'file': 'Example_4-4_Composite_Cellular.md',
        'composite': True,
        'beam_type': 'LB',
        'parent_section': 'W21x44',
        'expanded_section': 'LB32x44',
        'opening': 'Circular',
        'span': '50 ft',
        'deck': '3-inch deck + 2.5-inch concrete',
        'description': 'Composite cellular beam with concrete deck and circular openings',
        'key_checks': [
            'Composite PNA location',
            'Vierendeel bending (Section 3.3)',
            'Concrete deck shear contribution',
            'Web post buckling (Section 3.4.2)',
            'Vertical shear (Section 3.5)',
            'Deflection (Section 3.7)',
        ],
    },
}


class ExampleMatcher:
    """Match design requirements to appropriate examples."""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def match(self, composite: Optional[bool] = None,
             beam_type: Optional[str] = None,
             keywords: Optional[list] = None) -> Dict:
        """
        Match to appropriate example based on criteria.

        Args:
            composite: True for composite, False for noncomposite
            beam_type: 'CB' for castellated, 'LB' for cellular
            keywords: Additional keywords to match

        Returns:
            Dictionary with matched example(s)
        """
        matches = []

        for example_num, example_data in EXAMPLES.items():
            score = 0

            # Composite match
            if composite is not None:
                if example_data['composite'] == composite:
                    score += 10
                else:
                    continue  # Hard requirement

            # Beam type match
            if beam_type is not None:
                if example_data['beam_type'] == beam_type:
                    score += 10
                else:
                    continue  # Hard requirement

            # Keyword matching
            if keywords:
                searchable_text = (
                    example_data['title'] + ' ' +
                    example_data['description'] + ' ' +
                    ' '.join(example_data['key_checks'])
                ).lower()

                for keyword in keywords:
                    if keyword.lower() in searchable_text:
                        score += 2

            if score > 0:
                matches.append({
                    'example_num': example_num,
                    'score': score,
                    **example_data
                })

        # Sort by score
        matches.sort(key=lambda x: x['score'], reverse=True)

        return matches

    def get_example(self, example_num: str) -> Dict:
        """Get specific example by number."""
        if example_num in EXAMPLES:
            example = EXAMPLES[example_num].copy()
            example['example_num'] = example_num
            return example
        return None

    def decision_tree(self) -> str:
        """
        Interactive decision tree to select example.

        Returns:
            Example number (e.g., '4.1')
        """
        print("\n" + "="*80)
        print("  Example Selection Decision Tree")
        print("="*80 + "\n")

        # Question 1: Composite?
        print("1. Is the beam composite (with concrete deck)?")
        print("   a) Yes - Composite")
        print("   b) No - Noncomposite")
        response = input("\nSelect (a/b): ").strip().lower()

        composite = response == 'a'

        # Question 2: Beam type?
        print("\n2. What type of beam?")
        print("   a) Castellated (hexagonal openings)")
        print("   b) Cellular (circular openings)")
        response = input("\nSelect (a/b): ").strip().lower()

        beam_type = 'CB' if response == 'a' else 'LB'

        # Match
        if not composite and beam_type == 'CB':
            return '4.1'
        elif not composite and beam_type == 'LB':
            return '4.2'
        elif composite and beam_type == 'CB':
            return '4.3'
        elif composite and beam_type == 'LB':
            return '4.4'


def print_example(example: Dict, show_file_path: bool = True):
    """Print example details."""
    print("\n" + "="*80)
    print(f"  {example['title']}")
    print("="*80)

    print(f"\nExample Number: {example['example_num']}")
    print(f"Beam Type: {'Composite' if example['composite'] else 'Noncomposite'} "
          f"{example['beam_type']}")
    print(f"Parent Section: {example['parent_section']}")
    print(f"Expanded Section: {example['expanded_section']}")
    print(f"Opening Type: {example['opening']}")
    print(f"Span: {example['span']}")

    if 'deck' in example:
        print(f"Deck: {example['deck']}")

    print(f"\nDescription:")
    print(f"  {example['description']}")

    print(f"\nKey Design Checks:")
    for check in example['key_checks']:
        print(f"  • {check}")

    if show_file_path:
        file_path = Path(__file__).parent.parent / 'data' / 'examples' / example['file']
        print(f"\nFile Location:")
        print(f"  {file_path}")

    print("="*80)


def print_comparison_table():
    """Print comparison table of all examples."""
    print("\n" + "="*80)
    print("  Comparison of Design Guide 31 Examples")
    print("="*80 + "\n")

    print(f"{'Ex.':<6} {'Type':<15} {'Beam':<8} {'Parent':<10} {'Opening':<20} {'Span':<8}")
    print("-"*80)

    for num in ['4.1', '4.2', '4.3', '4.4']:
        ex = EXAMPLES[num]
        comp_type = 'Composite' if ex['composite'] else 'Noncomposite'
        print(f"{num:<6} {comp_type:<15} {ex['beam_type']:<8} {ex['parent_section']:<10} "
              f"{ex['opening']:<20} {ex['span']:<8}")

    print("\n" + "="*80)
    print("\nQuick Selection Guide:")
    print("  Example 4.1 = Noncomposite + Castellated (CB)")
    print("  Example 4.2 = Noncomposite + Cellular (LB)")
    print("  Example 4.3 = Composite + Castellated (CB)")
    print("  Example 4.4 = Composite + Cellular (LB)")
    print("="*80)


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Match design requirements to appropriate worked example',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Select composite castellated example:
    python3 example_matcher.py --composite --type CB

  Select noncomposite cellular example:
    python3 example_matcher.py --no-composite --type LB

  Interactive decision tree:
    python3 example_matcher.py --interactive

  Show specific example:
    python3 example_matcher.py --example 4.3

  Show comparison table:
    python3 example_matcher.py --compare
        """
    )

    parser.add_argument('--composite', action='store_true', help='Composite beam')
    parser.add_argument('--no-composite', action='store_true', help='Noncomposite beam')
    parser.add_argument('--type', choices=['CB', 'LB'], help='Beam type: CB=Castellated, LB=Cellular')
    parser.add_argument('--keywords', nargs='+', help='Additional keywords to match')
    parser.add_argument('--example', choices=['4.1', '4.2', '4.3', '4.4'], help='Show specific example')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive decision tree')
    parser.add_argument('--compare', action='store_true', help='Show comparison table')

    args = parser.parse_args()

    # Find data directory
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / 'data'

    matcher = ExampleMatcher(data_dir)

    # Comparison table mode
    if args.compare:
        print_comparison_table()
        return

    # Specific example mode
    if args.example:
        example = matcher.get_example(args.example)
        if example:
            print_example(example)
        else:
            print(f"Error: Example {args.example} not found")
        return

    # Interactive mode
    if args.interactive:
        example_num = matcher.decision_tree()
        example = matcher.get_example(example_num)
        print_example(example)
        return

    # Criteria-based matching
    composite = None
    if args.composite:
        composite = True
    elif args.no_composite:
        composite = False

    if composite is None and args.type is None:
        print("Error: Specify criteria (--composite/--no-composite and/or --type)")
        print("       or use --interactive, --example, or --compare")
        parser.print_help()
        sys.exit(1)

    matches = matcher.match(
        composite=composite,
        beam_type=args.type,
        keywords=args.keywords
    )

    if not matches:
        print("\nNo examples match the specified criteria.")
        print("Try --compare to see all available examples.")
        return

    print(f"\nFound {len(matches)} matching example(s):\n")

    for i, match in enumerate(matches, 1):
        print(f"{i}. Example {match['example_num']}: {match['title']}")
        print(f"   Score: {match['score']}")
        print(f"   {match['description']}")
        print()

    # Show details of best match
    if matches:
        print("\n" + "="*80)
        print("  Best Match:")
        print_example(matches[0])


if __name__ == '__main__':
    main()
