#!/usr/bin/env python3
"""
Formula Finder for Castellated and Cellular Beam Design
========================================================

Extract formulas and equations from AISC Design Guide 31 with surrounding context.
Identifies mathematical expressions and provides variable definitions.

수식 추출기 - 캐스틸레이티드 및 셀룰러 보 설계
AISC Design Guide 31에서 수식 및 방정식 추출

Usage:
    python3 formula_finder.py "Equation 3-3" --chapter 3
    python3 formula_finder.py "Mvr =" --file Chapter_3_Design_Procedures.md
    python3 formula_finder.py "web post" --all-formulas
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Formula patterns to detect mathematical expressions
FORMULA_PATTERNS = [
    # Equation references
    r'Equation\s+\d+-\d+[a-z]?',  # Equation 3-3, Equation 3-10a
    r'Eq\.\s+\d+-\d+',  # Eq. 3-3

    # Basic patterns
    r'[A-Z_][A-Za-z_0-9]*\s*=\s*',  # Variable assignment: M_vr = ...
    r'≤|≥|<|>',  # Inequality symbols
    r'\d+\.\d+\s*×',  # Decimal multiplication
    r'√',  # Square root

    # LaTeX/mathematical notation
    r'\$\$.*?\$\$',  # Display math: $$...$$
    r'\$.*?\$',  # Inline math: $...$

    # Fractions and divisions
    r'[A-Z_][a-z_]*\s*/\s*[A-Z_][a-z_]*',  # A_s / b_w
    r'\\frac\{[^}]*\}\{[^}]*\}',  # LaTeX fractions

    # Special symbols
    r'φ|Φ|ϕ',  # Phi (resistance factor)
    r'Ω|ω',  # Omega (safety factor)
    r'λ|Λ',  # Lambda (slenderness)
    r'θ',  # Theta (angle)

    # Structural engineering specific
    r'[Ff]_[yck]',  # f_y, f_c, f_ck
    r'[Mm]_[npu]',  # M_n, M_p, M_u
    r'[Vv]_[nru]',  # V_n, V_r, V_u
    r'[Pp]_[nru]',  # P_n, P_r, P_u
    r'[Tt]_[01]',  # T_0, T_1
]

# Equation number patterns
EQUATION_NUMBER_PATTERNS = [
    r'\((\d+-\d+[a-z]?)\)',  # (3-3), (3-10a)
    r'Equation\s+(\d+-\d+[a-z]?)',  # Equation 3-3
]


class FormulaFinder:
    """Extract formulas from design guide documents."""

    def __init__(self):
        pass

    def is_formula_line(self, line: str) -> bool:
        """Check if a line likely contains a formula."""
        for pattern in FORMULA_PATTERNS:
            if re.search(pattern, line):
                return True
        return False

    def extract_equation_number(self, line: str) -> str:
        """Extract equation number from line."""
        for pattern in EQUATION_NUMBER_PATTERNS:
            match = re.search(pattern, line)
            if match:
                return match.group(1)
        return None

    def find_formulas(self, file_path: str, keyword: str = None,
                     equation_num: str = None, context_lines: int = 5) -> List[Dict]:
        """
        Find formulas in a design guide file.

        Args:
            file_path: Path to markdown file
            keyword: Optional keyword to filter formulas
            equation_num: Specific equation number (e.g., "3-3")
            context_lines: Number of lines before/after formula

        Returns:
            List of dictionaries containing formula info
        """
        file_path = Path(file_path)

        if not file_path.exists():
            return []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            return []

        formulas = []

        for i, line in enumerate(lines):
            line_num = i + 1
            line_text = line.strip()

            # Skip empty lines
            if not line_text:
                continue

            # Check if line contains formula
            if self.is_formula_line(line_text):
                # Extract equation number if present
                eq_num = self.extract_equation_number(line_text)

                # If searching for specific equation number, filter
                if equation_num:
                    if not eq_num or eq_num != equation_num:
                        continue

                # If keyword specified, check if it's nearby
                if keyword:
                    start_idx = max(0, i - context_lines)
                    end_idx = min(len(lines), i + context_lines + 1)
                    context = ''.join(lines[start_idx:end_idx])

                    if keyword.lower() not in context.lower():
                        continue

                # Extract context
                start_idx = max(0, i - context_lines)
                end_idx = min(len(lines), i + context_lines + 1)
                context_before = lines[start_idx:i]
                context_after = lines[i+1:end_idx]

                # Build formula info
                formula_info = {
                    "line_number": line_num,
                    "formula": line_text,
                    "equation_number": eq_num,
                    "context_before": [l.strip() for l in context_before if l.strip()],
                    "context_after": [l.strip() for l in context_after if l.strip()],
                }

                # Extract variables from context (look for "where" section)
                variables = self._extract_variables(context_after[:10])
                if variables:
                    formula_info["variables"] = variables

                formulas.append(formula_info)

        return formulas

    def _extract_variables(self, lines: List[str]) -> List[Tuple[str, str]]:
        """Extract variable definitions from lines following formula."""
        variables = []

        in_where_section = False

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Look for "where" keyword
            if re.match(r'^where\s*$', line, re.IGNORECASE):
                in_where_section = True
                continue

            # Stop if we hit a new section
            if line.startswith('#') or line.startswith('**'):
                break

            # Extract variable definitions
            # Pattern: $variable$ = description
            # Pattern: variable = description
            match = re.match(r'^\$?([A-Za-z_][A-Za-z_0-9{}]*)\$?\s*=\s*(.+)', line)
            if match:
                var_name = match.group(1)
                var_def = match.group(2)
                variables.append((var_name, var_def))
                continue

            # Pattern with subscripts in LaTeX
            match = re.match(r'^\$([A-Za-z_][A-Za-z_0-9{}\\]*)\$\s*=\s*(.+)', line)
            if match:
                var_name = match.group(1)
                var_def = match.group(2)
                variables.append((var_name, var_def))

        return variables


def format_output(formulas: List[Dict], file_name: str):
    """Format and print formula findings."""
    if not formulas:
        print(f"No formulas found in {file_name}")
        return

    print(f"\n{'='*80}")
    print(f"Found {len(formulas)} formula(s) in {file_name}")
    print(f"{'='*80}\n")

    for i, formula_info in enumerate(formulas, 1):
        print(f"### Formula {i} ###")
        print(f"Line {formula_info['line_number']}:")

        if formula_info.get('equation_number'):
            print(f"Equation {formula_info['equation_number']}:")

        print(f"{formula_info['formula']}")

        if formula_info.get('variables'):
            print("\nVariables:")
            for var, definition in formula_info['variables']:
                print(f"  {var} = {definition}")

        if formula_info['context_before']:
            print("\nContext before:")
            for line in formula_info['context_before'][-3:]:  # Last 3 lines
                print(f"  {line}")

        if formula_info['context_after']:
            print("\nContext after:")
            for line in formula_info['context_after'][:3]:  # First 3 lines
                print(f"  {line}")

        print(f"{'-'*80}\n")


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Extract formulas from AISC Design Guide 31',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Find specific equation:
    python3 formula_finder.py "3-3" --chapter 3

  Find formulas with keyword:
    python3 formula_finder.py "Vierendeel" --file Chapter_3_Design_Procedures.md

  Find all formulas in a file:
    python3 formula_finder.py --file Chapter_3_Design_Procedures.md --all-formulas

  Search for formula pattern:
    python3 formula_finder.py "Mvr" --chapter 3
        """
    )

    parser.add_argument('query', nargs='?', help='Search query (equation number or keyword)')
    parser.add_argument('--file', help='Specific file to search')
    parser.add_argument('--chapter', choices=['1', '2', '3'], help='Chapter to search')
    parser.add_argument('--example', choices=['4.1', '4.2', '4.3', '4.4'], help='Example to search')
    parser.add_argument('--all-formulas', action='store_true', help='Extract all formulas')
    parser.add_argument('--context', type=int, default=5, help='Context lines (default 5)')

    args = parser.parse_args()

    # Find data directory
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / 'data'

    if not data_dir.exists():
        print(f"Error: Data directory not found at {data_dir}", file=sys.stderr)
        sys.exit(1)

    # Determine file to search
    if args.file:
        file_path = data_dir / 'design-guide' / args.file
        if not file_path.exists():
            file_path = data_dir / 'examples' / args.file
    elif args.chapter:
        chapter_files = {
            '1': 'Chapter_1_Introduction.md',
            '2': 'Chapter_2_Use_Cases.md',
            '3': 'Chapter_3_Design_Procedures.md',
        }
        file_path = data_dir / 'design-guide' / chapter_files[args.chapter]
    elif args.example:
        example_files = {
            '4.1': 'Example_4-1_Noncomposite_Castellated.md',
            '4.2': 'Example_4-2_Noncomposite_Cellular.md',
            '4.3': 'Example_4-3_Composite_Castellated.md',
            '4.4': 'Example_4-4_Composite_Cellular.md',
        }
        file_path = data_dir / 'examples' / example_files[args.example]
    else:
        print("Error: Specify --file, --chapter, or --example")
        parser.print_help()
        sys.exit(1)

    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    # Determine search criteria
    keyword = None
    equation_num = None

    if args.query:
        # Check if query is an equation number (e.g., "3-3")
        if re.match(r'^\d+-\d+[a-z]?$', args.query):
            equation_num = args.query
        else:
            keyword = args.query

    # Find formulas
    finder = FormulaFinder()
    formulas = finder.find_formulas(
        str(file_path),
        keyword=keyword if not args.all_formulas else None,
        equation_num=equation_num,
        context_lines=args.context
    )

    # Format and display output
    format_output(formulas, file_path.name)


if __name__ == "__main__":
    main()
