#!/usr/bin/env python3
"""
ACI 318-25 Formula Finder Script
=================================

Purpose: Extract formulas and equations from ACI 318-25 documents with context
         Find variable definitions and related equations

Author: Claude Code
Date: 2025-11-14
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import argparse


@dataclass
class Formula:
    """Container for formula information"""
    equation_number: str
    formula_text: str
    section_id: str
    file_name: str
    page_reference: str
    context_before: List[str]
    context_after: List[str]
    variables: Dict[str, str]  # variable: definition


class FormulaFinder:
    """Find and extract formulas from ACI 318-25 documents"""

    def __init__(self, data_dir: str):
        """
        Initialize formula finder

        Args:
            data_dir: Path to consolidated data directory
        """
        self.data_dir = Path(data_dir)
        self.code_dir = self.data_dir / 'code'
        self.commentary_dir = self.data_dir / 'commentary'
        self.notation_file = self.data_dir / 'Notation_Symbols.md'

        # Load notation symbols
        self.symbols = self._load_symbols()

    def _load_symbols(self) -> Dict[str, str]:
        """Load symbol definitions from Chapter 2 Notation"""
        symbols = {}

        if not self.notation_file.exists():
            return symbols

        try:
            with open(self.notation_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Pattern to match symbol definitions
            # Example: "f'c = specified compressive strength of concrete, psi"
            pattern = r'([A-Za-z][A-Za-z0-9\'_]*)\s*=\s*([^,\n]+(?:,[^,\n]+)?)'

            for match in re.finditer(pattern, content):
                symbol = match.group(1).strip()
                definition = match.group(2).strip()
                symbols[symbol] = definition

        except Exception as e:
            print(f"Warning: Could not load symbols: {e}")

        return symbols

    def find_formulas(self, pattern: Optional[str] = None,
                     section: Optional[str] = None,
                     search_commentary: bool = False) -> List[Formula]:
        """
        Find formulas matching pattern

        Args:
            pattern: Regex pattern to match (e.g., "V_c =", "M_n")
            section: Specific section to search (e.g., "22.5", "9.6")
            search_commentary: Whether to search commentary as well

        Returns:
            List of Formula objects
        """
        formulas = []

        # Search CODE files
        for code_file in self.code_dir.glob('*.md'):
            formulas.extend(self._extract_from_file(code_file, pattern, section))

        # Search COMMENTARY files if requested
        if search_commentary:
            for commentary_file in self.commentary_dir.glob('*.md'):
                formulas.extend(self._extract_from_file(commentary_file, pattern, section))

        return formulas

    def _extract_from_file(self, file_path: Path, pattern: Optional[str],
                          section: Optional[str]) -> List[Formula]:
        """Extract formulas from a single file"""
        formulas = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return formulas

        # Split into sections
        sections = self._split_sections(content)

        for section_id, section_content in sections:
            # Filter by section if specified
            if section and not section_id.startswith(section):
                continue

            # Find formulas in this section
            section_formulas = self._find_formulas_in_section(
                section_content, section_id, file_path
            )

            # Filter by pattern if specified
            if pattern:
                section_formulas = [
                    f for f in section_formulas
                    if re.search(pattern, f.formula_text, re.IGNORECASE)
                ]

            formulas.extend(section_formulas)

        return formulas

    def _split_sections(self, content: str) -> List[Tuple[str, str]]:
        """Split content into sections"""
        sections = []

        # Pattern for section headers
        section_pattern = r'^(R?\d+\.\d+(?:\.\d+)*(?:\.\d+)?)\s'

        lines = content.split('\n')
        current_section = None
        current_content = []

        for line in lines:
            match = re.match(section_pattern, line)
            if match:
                if current_section:
                    sections.append((current_section, '\n'.join(current_content)))
                current_section = match.group(1)
                current_content = [line]
            else:
                current_content.append(line)

        if current_section:
            sections.append((current_section, '\n'.join(current_content)))

        return sections

    def _find_formulas_in_section(self, content: str, section_id: str,
                                 file_path: Path) -> List[Formula]:
        """Find all formulas in a section"""
        formulas = []
        lines = content.split('\n')

        # Patterns for formulas
        # 1. Inline math: $...$
        # 2. Display math: $$...$$
        # 3. Explicit equations with labels
        # 4. Common formula patterns (Vc =, Mn =, etc.)

        for i, line in enumerate(lines):
            # Look for equation patterns
            eq_patterns = [
                r'([A-Z][a-z]?_[a-z]+)\s*=',  # Vc =, Mn =
                r'\$\$(.+?)\$\$',  # $$...$$
                r'(?:Eq\.|Equation)\s*\(?([\d.]+)\)?',  # Eq. (22.5.8.5.3)
            ]

            for eq_pattern in eq_patterns:
                matches = re.finditer(eq_pattern, line)
                for match in matches:
                    # Extract equation number if present
                    eq_num = self._extract_equation_number(lines, i)

                    # Get context
                    context_before = lines[max(0, i-3):i]
                    context_after = lines[i+1:min(len(lines), i+4)]

                    # Extract formula text
                    formula_text = self._extract_formula_text(lines, i)

                    # Extract variables
                    variables = self._extract_variables(content, formula_text)

                    # Extract page reference
                    page_ref = self._extract_page_reference(content)

                    formulas.append(Formula(
                        equation_number=eq_num,
                        formula_text=formula_text,
                        section_id=section_id,
                        file_name=file_path.name,
                        page_reference=page_ref,
                        context_before=context_before,
                        context_after=context_after,
                        variables=variables
                    ))

                    break  # Only process first match per line

        return formulas

    def _extract_equation_number(self, lines: List[str], index: int) -> str:
        """Extract equation number from surrounding lines"""
        # Look in current line and next few lines
        search_range = lines[index:min(len(lines), index+3)]
        search_text = ' '.join(search_range)

        # Pattern: Eq. (22.5.8.5.3) or (22.5.8.5.3)
        match = re.search(r'(?:Eq\.|Equation)?\s*\(?([\d.]+)\)?', search_text)
        if match:
            return match.group(1)

        return "N/A"

    def _extract_formula_text(self, lines: List[str], index: int) -> str:
        """Extract the actual formula text"""
        line = lines[index]

        # Try to extract from math delimiters
        math_match = re.search(r'\$\$(.+?)\$\$|\$(.+?)\$', line)
        if math_match:
            return math_match.group(1) or math_match.group(2)

        # Otherwise return the line with common patterns
        formula_match = re.search(r'([A-Z][a-z]?_[a-z]+\s*=.+?)(?:\s{2,}|$)', line)
        if formula_match:
            return formula_match.group(1)

        return line.strip()

    def _extract_variables(self, content: str, formula: str) -> Dict[str, str]:
        """Extract variable definitions for formula"""
        variables = {}

        # Find variables in formula (single letters, subscripted variables)
        var_pattern = r'([A-Za-z][A-Za-z0-9\'_]*)'
        found_vars = set(re.findall(var_pattern, formula))

        # Look up in symbols dictionary
        for var in found_vars:
            if var in self.symbols:
                variables[var] = self.symbols[var]
            else:
                # Try to find local definition in content
                local_def = self._find_local_definition(content, var)
                if local_def:
                    variables[var] = local_def

        return variables

    def _find_local_definition(self, content: str, variable: str) -> Optional[str]:
        """Find variable definition in local context"""
        # Pattern: "variable = definition"
        pattern = f'{re.escape(variable)}\\s*=\\s*([^,\\n]+(?:,[^,\\n]+)?)'

        match = re.search(pattern, content)
        if match:
            return match.group(1).strip()

        return None

    def _extract_page_reference(self, content: str) -> str:
        """Extract page reference"""
        match = re.search(r'<!-- From Page (\d+) -->', content)
        if match:
            return f"Page {match.group(1)}"
        return "N/A"


def format_formula(formula: Formula, show_context: bool = True) -> str:
    """Format formula for display"""
    output = []

    output.append(f"Section: {formula.section_id}")
    if formula.equation_number != "N/A":
        output.append(f"Equation: ({formula.equation_number})")
    output.append(f"File: {formula.file_name}")
    output.append(f"Page: {formula.page_reference}")
    output.append("")
    output.append(f"Formula: {formula.formula_text}")
    output.append("")

    if formula.variables:
        output.append("Variables:")
        for var, definition in formula.variables.items():
            output.append(f"  {var} = {definition}")
        output.append("")

    if show_context:
        if formula.context_before:
            output.append("Context (before):")
            for line in formula.context_before:
                output.append(f"  {line}")
            output.append("")

        if formula.context_after:
            output.append("Context (after):")
            for line in formula.context_after[:3]:  # Limit context
                output.append(f"  {line}")
            output.append("")

    return '\n'.join(output)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Find formulas in ACI 318-25 documents'
    )
    parser.add_argument(
        '--pattern',
        type=str,
        help='Regex pattern to match (e.g., "V_c =", "M_n")'
    )
    parser.add_argument(
        '--section',
        type=str,
        help='Specific section to search (e.g., "22.5", "9.6")'
    )
    parser.add_argument(
        '--data-dir',
        type=str,
        default='/home/hankm/Code_Work/ACI318_Engineer/.claude/skills/aci-318-concrete-design/data',
        help='Path to data directory'
    )
    parser.add_argument(
        '--commentary',
        action='store_true',
        help='Include commentary in search'
    )
    parser.add_argument(
        '--no-context',
        action='store_true',
        help='Hide context in output'
    )

    args = parser.parse_args()

    # Run search
    finder = FormulaFinder(args.data_dir)
    formulas = finder.find_formulas(
        pattern=args.pattern,
        section=args.section,
        search_commentary=args.commentary
    )

    # Display results
    if not formulas:
        print("No formulas found.")
        return

    print(f"\nFound {len(formulas)} formulas:\n")
    print("=" * 80)

    for i, formula in enumerate(formulas[:10], 1):  # Limit to first 10
        print(f"\n{i}.")
        print(format_formula(formula, show_context=not args.no_context))
        print("-" * 80)


if __name__ == '__main__':
    main()
