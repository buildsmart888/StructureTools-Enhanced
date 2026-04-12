#!/usr/bin/env python3
"""
AISC Formula Finder
===================

Extracts formulas from AISC Specification documents with context.

Usage:
    python3 formula_finder.py "Mn =" "Chapter_F"
    python3 formula_finder.py "φ =" "Chapter_E"
    python3 formula_finder.py "Fcr =" --all

Output:
    JSON array of formulas with context (±5 lines)
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Paths
SKILL_DIR = Path(__file__).parent.parent
SPEC_DIR = SKILL_DIR / "data" / "specification"
SYMBOLS_FILE = SKILL_DIR / "references" / "symbols.md"

# Formula patterns (common AISC formula indicators)
FORMULA_PATTERNS = [
    r'[A-Z][a-z]?\s*=\s*',  # Variable = (Mn =, Fcr =, etc.)
    r'φ\s*=\s*',             # φ = (resistance factor)
    r'Ω\s*=\s*',             # Ω = (safety factor)
    r'\$.*?=.*?\$',          # LaTeX math
]


def find_formula_lines(content: str, pattern: str) -> List[Tuple[int, str]]:
    """Find lines containing formula pattern."""
    lines = content.split('\n')
    matches = []

    # Create regex from pattern
    if pattern.endswith('='):
        # Exact variable match
        regex = re.escape(pattern) + r'.*'
    else:
        # General pattern
        regex = pattern

    for i, line in enumerate(lines, 1):
        if re.search(regex, line, re.IGNORECASE):
            matches.append((i, line))

    return matches


def get_context(content: str, line_num: int, context_lines: int = 5) -> Dict:
    """Get context around formula line."""
    lines = content.split('\n')
    total_lines = len(lines)

    start = max(0, line_num - context_lines - 1)
    end = min(total_lines, line_num + context_lines)

    before = lines[start:line_num-1]
    formula = lines[line_num-1] if line_num <= total_lines else ""
    after = lines[line_num:end]

    return {
        "line_number": line_num,
        "before": before,
        "formula": formula,
        "after": after
    }


def extract_section_number(context: Dict) -> str:
    """Try to extract section number from context."""
    all_lines = context['before'] + [context['formula']] + context['after']

    for line in all_lines:
        # Look for section patterns like "F2.1", "E3.2", etc.
        match = re.search(r'[A-Z]\d+\.\d+', line)
        if match:
            return match.group(0)

    return "Unknown"


def search_file(filepath: Path, pattern: str) -> List[Dict]:
    """Search for formulas in a single file."""
    results = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        matches = find_formula_lines(content, pattern)

        for line_num, line_text in matches:
            context = get_context(content, line_num)
            section = extract_section_number(context)

            results.append({
                "file": filepath.name,
                "section": section,
                "line_number": line_num,
                "formula": line_text.strip(),
                "context": context
            })

    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)

    return results


def find_formulas(pattern: str, chapter: str = None) -> Dict:
    """Main formula finder function."""
    results = []

    if chapter and chapter != "--all":
        # Search specific chapter
        files = list(SPEC_DIR.glob(f"*{chapter}*.md"))
    else:
        # Search all specification files
        files = list(SPEC_DIR.glob("*.md"))

    for filepath in files:
        if filepath.name == "README.md":
            continue

        file_results = search_file(filepath, pattern)
        results.extend(file_results)

    return {
        "pattern": pattern,
        "chapter_filter": chapter,
        "total_matches": len(results),
        "formulas": results
    }


def load_symbol_definition(symbol: str) -> str:
    """Load symbol definition from symbols.md."""
    try:
        with open(SYMBOLS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for symbol definition
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if f"${symbol}$" in line or f" {symbol} " in line:
                return line.strip()

    except Exception:
        pass

    return "Definition not found"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 formula_finder.py \"pattern\" [chapter]")
        print("\nExamples:")
        print("  python3 formula_finder.py \"Mn =\" \"Chapter_F\"")
        print("  python3 formula_finder.py \"φ =\" --all")
        print("  python3 formula_finder.py \"Fcr\" \"Chapter_E\"")
        sys.exit(1)

    pattern = sys.argv[1]
    chapter = sys.argv[2] if len(sys.argv) > 2 else None

    results = find_formulas(pattern, chapter)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
