#!/usr/bin/env python3
"""
AISC Cross-Reference Tool
==========================

Cross-references between AISC Specification and Design Examples.

Usage:
    python3 cross_reference.py "Chapter_E"
    python3 cross_reference.py "Chapter_F" --show-examples
    python3 cross_reference.py "Example F.1-1A" --show-spec

Output:
    JSON mapping between Specification chapters and related examples
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict

# Paths
SKILL_DIR = Path(__file__).parent.parent
SPEC_DIR = SKILL_DIR / "data" / "specification"
EXAMPLES_DIR = SKILL_DIR / "data" / "design-examples"

# Chapter mapping (Specification → Design Examples)
SPEC_TO_EXAMPLES = {
    "A": ["Part_I/Chapter_A_General_Provisions.md"],
    "B": ["Part_I/Chapter_B_Design_Requirements.md"],
    "C": ["Part_I/Chapter_C_Stability.md", "Part_III/Chapter_Building_System_Analysis.md"],
    "D": ["Part_I/Chapter_D_Tension_Members.md"],
    "E": ["Part_I/Chapter_E_Compression_Members.md"],
    "F": ["Part_I/Chapter_F_Flexural_Members.md"],
    "G": ["Part_I/Chapter_G_Shear_Members.md"],
    "H": ["Part_I/Chapter_H_Combined_Forces.md"],
    "I": ["Part_I/Chapter_I_Composite_Members.md"],
    "J": ["Part_I/Chapter_J_Connections.md", "Part_II/Chapter_IIA_Simple_Shear_Connections.md",
          "Part_II/Chapter_IIB_Moment_Connections.md", "Part_II/Chapter_IIC_Bracing_Connections.md",
          "Part_II/Chapter_IID_Miscellaneous_Connections.md"],
    "K": ["Part_I/Chapter_K_HSS_Connections.md", "Part_II/Chapter_IID_Miscellaneous_Connections.md"],
    "L": [],  # No specific examples
    "M": [],  # No specific examples
    "N": [],  # No specific examples
}


def extract_chapter_letter(identifier: str) -> str:
    """Extract chapter letter from identifier."""
    # Match patterns like "Chapter_E", "E", "Chapter E"
    match = re.search(r'Chapter[_\s]?([A-N])', identifier, re.IGNORECASE)
    if match:
        return match.group(1).upper()

    # Single letter
    if len(identifier) == 1 and identifier.upper() in "ABCDEFGHIJKLMN":
        return identifier.upper()

    return None


def find_spec_file(chapter: str) -> Path:
    """Find specification file for chapter."""
    matches = list(SPEC_DIR.glob(f"Chapter_{chapter}_*.md"))
    return matches[0] if matches else None


def find_example_files(chapter: str) -> List[Path]:
    """Find example files for chapter."""
    if chapter not in SPEC_TO_EXAMPLES:
        return []

    example_files = []
    for rel_path in SPEC_TO_EXAMPLES[chapter]:
        filepath = EXAMPLES_DIR / rel_path
        if filepath.exists():
            example_files.append(filepath)

    return example_files


def extract_spec_citations(filepath: Path) -> List[str]:
    """Extract AISC Specification section citations from example file."""
    citations = set()

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for patterns like "AISC 360-22 Section F2.1", "Section E3.2", etc.
        patterns = [
            r'Section\s+([A-N]\d+\.?\d*)',
            r'AISC\s+360-22\s+Section\s+([A-N]\d+\.?\d*)',
            r'Spec\.\s+Section\s+([A-N]\d+\.?\d*)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, content)
            citations.update(matches)

    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)

    return sorted(list(citations))


def extract_example_numbers(filepath: Path) -> List[str]:
    """Extract example numbers from file."""
    examples = set()

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for example numbers like "Example E.1A", "Example F.1-1A", "Example II-A.1"
        patterns = [
            r'Example\s+([A-Z]\.\d+[A-Z]?)',
            r'Example\s+([A-Z]\.\d+-\d+[A-Z]?)',
            r'Example\s+(II-[A-Z]\.\d+)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, content)
            examples.update(matches)

    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)

    return sorted(list(examples))


def get_file_stats(filepath: Path) -> Dict:
    """Get basic file statistics."""
    if not filepath.exists():
        return {}

    stat = filepath.stat()
    lines = 0

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = len(f.readlines())
    except:
        pass

    return {
        "size_kb": stat.st_size / 1024,
        "lines": lines
    }


def cross_reference_chapter(chapter: str) -> Dict:
    """Generate cross-reference for a chapter."""
    spec_file = find_spec_file(chapter)
    example_files = find_example_files(chapter)

    result = {
        "chapter": chapter,
        "specification": None,
        "design_examples": []
    }

    # Specification info
    if spec_file:
        result["specification"] = {
            "file": str(spec_file.relative_to(SKILL_DIR)),
            "stats": get_file_stats(spec_file),
            "chapter_title": spec_file.stem.replace('Chapter_', '').replace('_', ' ')
        }

    # Design examples info
    for ex_file in example_files:
        citations = extract_spec_citations(ex_file)
        example_nums = extract_example_numbers(ex_file)

        result["design_examples"].append({
            "file": str(ex_file.relative_to(SKILL_DIR)),
            "stats": get_file_stats(ex_file),
            "spec_citations": citations,
            "example_numbers": example_nums,
            "total_examples": len(example_nums)
        })

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cross_reference.py \"Chapter_X\" [--show-examples]")
        print("\nExamples:")
        print("  python3 cross_reference.py \"Chapter_E\"")
        print("  python3 cross_reference.py \"F\" --show-examples")
        print("  python3 cross_reference.py \"Chapter_J\"")
        sys.exit(1)

    identifier = sys.argv[1]
    show_examples = "--show-examples" in sys.argv

    chapter = extract_chapter_letter(identifier)

    if not chapter:
        print(f"Error: Could not extract chapter from '{identifier}'", file=sys.stderr)
        print("Please use format like: 'Chapter_E', 'E', or 'Chapter E'", file=sys.stderr)
        sys.exit(1)

    result = cross_reference_chapter(chapter)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
