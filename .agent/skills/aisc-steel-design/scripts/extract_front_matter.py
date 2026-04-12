#!/usr/bin/env python3
"""
AISC Front Matter Extraction Script

Extracts reference materials from page-level markdown files:
- Symbols table (a360 pages 33-51)
- Glossary (a360 pages 52-67)
- Abbreviations (a360 page 68)
- Specification ToC (a360 pages 11-32)
- Design Examples ToC (design_ex pages 7-10)
- Conventions (design_ex page 5)

Author: Claude Code
Date: 2025-11-09
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

# ============================================================================
# CONFIGURATION
# ============================================================================

# Base directories (absolute paths)
AISC_ROOT = Path("/Users/hi/2025OFFICEWORK/AISC_Engineer")
A360_DIR = AISC_ROOT / "a360_markdown"
DESIGN_EX_DIR = AISC_ROOT / "Design_ex_markdown"
OUTPUT_DIR = Path(__file__).parent.parent / "references"

# Page ranges to extract
EXTRACTIONS = {
    "symbols": {
        "source_dir": A360_DIR,
        "pages": range(33, 52),  # pages 33-51
        "filename_pattern": "a360-22w_page_{:03d}.md",
        "output": "symbols.md",
        "title": "# AISC 360-22 Symbols and Notation",
        "description": "Complete symbols table extracted from AISC 360-22 Specification pages 33-51."
    },
    "glossary": {
        "source_dir": A360_DIR,
        "pages": range(52, 68),  # pages 52-67
        "filename_pattern": "a360-22w_page_{:03d}.md",
        "output": "glossary.md",
        "title": "# AISC 360-22 Glossary",
        "description": "Technical terms and definitions from AISC 360-22 Specification pages 52-67."
    },
    "abbreviations": {
        "source_dir": A360_DIR,
        "pages": [68],
        "filename_pattern": "a360-22w_page_{:03d}.md",
        "output": "abbreviations.md",
        "title": "# AISC 360-22 Abbreviations",
        "description": "Standard abbreviations from AISC 360-22 Specification page 68."
    },
    "spec_toc": {
        "source_dir": A360_DIR,
        "pages": range(11, 33),  # pages 11-32
        "filename_pattern": "a360-22w_page_{:03d}.md",
        "output": "specification-structure.md",
        "title": "# AISC 360-22 Specification Structure",
        "description": "Table of contents and chapter structure from AISC 360-22 Specification pages 11-32."
    },
    "examples_toc": {
        "source_dir": DESIGN_EX_DIR,
        "pages": range(7, 11),  # pages 7-10
        "filename_pattern": "v16.0_vol-1_design-examples_page_{:03d}.md",
        "output": "design-examples-index.md",
        "title": "# AISC Design Examples Index",
        "description": "Complete table of contents and example index from Design Examples v16.0 pages 7-10."
    },
    "conventions": {
        "source_dir": DESIGN_EX_DIR,
        "pages": [5],
        "filename_pattern": "v16.0_vol-1_design-examples_page_{:03d}.md",
        "output": "conventions.md",
        "title": "# AISC Design Conventions",
        "description": "Design conventions and methodology from Design Examples v16.0 page 5."
    },
    "modifications": {
        "source_dir": A360_DIR,
        "pages": range(7, 10),  # pages 7-9
        "filename_pattern": "a360-22w_page_{:03d}.md",
        "output": "key-modifications-360-22.md",
        "title": "# AISC 360-22 Key Modifications",
        "description": "Summary of major changes in 2022 edition from AISC 360-22 Specification pages 7-9."
    }
}

# Patterns to remove (headers, footers, page markers)
REMOVAL_PATTERNS = [
    r'^<!-- Page \d+ -->$',
    r'^# Page [A-Z0-9-]+$',
    r'^Page [A-Z0-9-]+$',
    r'^\*\*16\.1-[ivxlcdm\d]+\*\*$',
    r'^\*\*Page:\*\* .+$',
]

FOOTER_STRINGS = [
    "*Specification for Structural Steel Buildings*, August 1, 2022",
    "*Specification for Structural Steel Buildings, August 1, 2022*",
    "AMERICAN INSTITUTE OF STEEL CONSTRUCTION",
    "*V16.0 Companion, Vol. 1: Design Examples*",
    "V16.0 Companion, Vol. 1: Design Examples",
]


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def clean_content(content: str) -> str:
    """Remove headers, footers, and page markers."""
    lines = content.split('\n')
    cleaned_lines = []

    for line in lines:
        # Skip empty lines at start
        if not cleaned_lines and not line.strip():
            continue

        # Check removal patterns
        skip = False
        for pattern in REMOVAL_PATTERNS:
            if re.match(pattern, line):
                skip = True
                break

        # Check literal footer strings
        for footer in FOOTER_STRINGS:
            if footer in line:
                skip = True
                break

        if not skip:
            cleaned_lines.append(line)

    # Join and cleanup
    cleaned = '\n'.join(cleaned_lines)
    cleaned = re.sub(r'\n---\n---\n', '\n---\n', cleaned)
    cleaned = cleaned.rstrip() + '\n'

    return cleaned


def read_page(source_dir: Path, filename: str) -> str:
    """Read a single page file."""
    filepath = source_dir / filename

    if not filepath.exists():
        print(f"⚠️  Warning: File not found: {filepath}")
        return ""

    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def merge_pages(source_dir: Path, pages: List[int], filename_pattern: str) -> str:
    """Merge multiple pages into single content."""
    combined = []

    for page_num in pages:
        filename = filename_pattern.format(page_num)
        content = read_page(source_dir, filename)

        if content:
            cleaned = clean_content(content)
            if cleaned.strip():
                combined.append(cleaned)

    return '\n\n'.join(combined)


def create_reference_file(name: str, config: dict):
    """Create a single reference file from configuration."""
    print(f"\n📄 Creating {config['output']}...")

    # Merge pages
    content = merge_pages(
        config['source_dir'],
        config['pages'],
        config['filename_pattern']
    )

    # Add metadata header
    header = f"""{config['title']}

**Source**: {config['description']}
**Extracted**: 2025-11-09
**Format**: Markdown

---

"""

    full_content = header + content

    # Write output
    output_path = OUTPUT_DIR / config['output']
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

    # Statistics
    lines = len(full_content.split('\n'))
    size_kb = len(full_content.encode('utf-8')) / 1024

    print(f"   ✅ Created: {output_path}")
    print(f"   Lines: {lines:,}")
    print(f"   Size: {size_kb:.1f} KB")

    return size_kb


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 80)
    print("AISC Front Matter Extraction")
    print("=" * 80)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    stats = {
        'total_files': 0,
        'total_size': 0
    }

    # Process each extraction
    for name, config in EXTRACTIONS.items():
        size = create_reference_file(name, config)
        stats['total_files'] += 1
        stats['total_size'] += size

    # Summary
    print("\n" + "=" * 80)
    print("EXTRACTION COMPLETE")
    print("=" * 80)
    print(f"\n📊 Statistics:")
    print(f"   Files created: {stats['total_files']}")
    print(f"   Total size: {stats['total_size']:.1f} KB")
    print(f"   Average per file: {stats['total_size'] / stats['total_files']:.1f} KB")
    print(f"\n✅ All reference files created in: {OUTPUT_DIR.absolute()}")
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
