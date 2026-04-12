#!/usr/bin/env python3
"""
Smart search for AISC Design Guide 1 content.

Usage:
    python3 smart_search.py "query" [--data-dir PATH]

Examples:
    python3 smart_search.py "bearing strength"
    python3 smart_search.py "shear lug" --data-dir ../data

This script searches consolidated chapter files for relevant content based on keyword mapping.
"""

import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Keyword to chapter mapping
KEYWORD_MAP = {
    # Load types
    "compression": ["Chapter_4_Exposed_Connections.md", "Chapter_3_Base_Plate_Design.md"],
    "tension": ["Chapter_4_Exposed_Connections.md"],
    "uplift": ["Chapter_4_Exposed_Connections.md"],
    "moment": ["Chapter_4_Exposed_Connections.md", "Chapter_3_Base_Plate_Design.md"],
    "bending": ["Chapter_4_Exposed_Connections.md", "Chapter_3_Base_Plate_Design.md"],
    "shear": ["Chapter_4_Exposed_Connections.md"],
    "biaxial": ["Chapter_4_Exposed_Connections.md"],

    # Design features
    "bearing": ["Chapter_4_Exposed_Connections.md", "Chapter_3_Base_Plate_Design.md"],
    "anchor rod": ["Chapter_4_Exposed_Connections.md", "Chapter_2_Materials.md"],
    "anchor": ["Chapter_4_Exposed_Connections.md", "Chapter_2_Materials.md"],
    "shear lug": ["Chapter_4_Exposed_Connections.md"],
    "embedded": ["Chapter_5_Embedded_Connections.md"],
    "base plate": ["Chapter_4_Exposed_Connections.md", "Chapter_3_Base_Plate_Design.md"],
    "thickness": ["Chapter_4_Exposed_Connections.md"],

    # Materials
    "concrete": ["Chapter_4_Exposed_Connections.md", "Chapter_2_Materials.md"],
    "grout": ["Chapter_4_Exposed_Connections.md", "Chapter_2_Materials.md"],
    "f1554": ["Chapter_2_Materials.md", "Chapter_4_Exposed_Connections.md"],
    "astm": ["Chapter_2_Materials.md"],

    # Analysis
    "small moment": ["Chapter_4_Exposed_Connections.md"],
    "large moment": ["Chapter_4_Exposed_Connections.md"],
    "eccentricity": ["Chapter_4_Exposed_Connections.md", "Chapter_3_Base_Plate_Design.md"],
    "lrfd": ["Chapter_4_Exposed_Connections.md"],
    "asd": ["Chapter_4_Exposed_Connections.md"],

    # Design codes
    "aci 318": ["Chapter_4_Exposed_Connections.md"],
    "aci": ["Chapter_4_Exposed_Connections.md"],
    "aisc": ["Chapter_4_Exposed_Connections.md"],

    # Seismic
    "seismic": ["Chapter_6_Seismic_Design.md"],
    "earthquake": ["Chapter_6_Seismic_Design.md"],
    "braced frame": ["Chapter_4_Exposed_Connections.md", "Chapter_6_Seismic_Design.md"],

    # Special topics
    "friction": ["Chapter_4_Exposed_Connections.md"],
    "breakout": ["Chapter_4_Exposed_Connections.md"],
    "pullout": ["Chapter_4_Exposed_Connections.md"],
    "pryout": ["Chapter_4_Exposed_Connections.md"],
    "confinement": ["Chapter_4_Exposed_Connections.md"],
    "weld": ["Chapter_4_Exposed_Connections.md", "Chapter_2_Materials.md"],
    "grouting": ["Chapter_4_Exposed_Connections.md", "Chapter_2_Materials.md"],
    "tolerance": ["Chapter_4_Exposed_Connections.md"],

    # Specialty
    "specialty anchor": ["Appendix_A_Specialty_Anchors.md"],
    "alternate method": ["Appendix_B_Alternate_Methods.md"],
    "triangular": ["Appendix_B_Alternate_Methods.md", "Chapter_4_Exposed_Connections.md"],
}


def search_files(query: str, data_dir: Path) -> List[Tuple[str, List[str], int]]:
    """
    Search for query in relevant chapter files.

    Returns:
        List of tuples: (filename, matching_lines, relevance_score)
    """
    query_lower = query.lower()
    results = []

    # Determine relevant files based on keywords
    relevant_files = set()
    for keyword, files in KEYWORD_MAP.items():
        if keyword in query_lower:
            relevant_files.update(files)

    # If no keyword match, search all files
    if not relevant_files:
        relevant_files = set(f.name for f in data_dir.glob("*.md"))

    # Search each relevant file
    for filename in relevant_files:
        filepath = data_dir / filename
        if not filepath.exists():
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

        # Find matching lines
        matches = []
        for i, line in enumerate(lines, 1):
            if query_lower in line.lower():
                # Include context (±2 lines)
                context_start = max(0, i-3)
                context_end = min(len(lines), i+2)
                context = lines[context_start:context_end]
                matches.append(f"Line {i}: " + '\n'.join(context))

        if matches:
            # Calculate relevance score
            score = len(matches)
            # Boost score if query appears in filename
            if query_lower in filename.lower():
                score += 10

            results.append((filename, matches[:10], score))  # Limit to 10 matches per file

    # Sort by relevance score
    results.sort(key=lambda x: x[2], reverse=True)

    return results


def main():
    parser = argparse.ArgumentParser(description="Search AISC Design Guide 1 content")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--data-dir",
                       default="../data",
                       help="Path to data directory (default: ../data)")
    parser.add_argument("--max-results",
                       type=int,
                       default=5,
                       help="Maximum number of results to show (default: 5)")

    args = parser.parse_args()

    # Resolve data directory path
    script_dir = Path(__file__).parent
    data_dir = (script_dir / args.data_dir).resolve()

    if not data_dir.exists():
        print(f"Error: Data directory not found: {data_dir}")
        return 1

    print(f"Searching for: '{args.query}'")
    print(f"Data directory: {data_dir}")
    print("=" * 70)
    print()

    results = search_files(args.query, data_dir)

    if not results:
        print("No results found.")
        print()
        print("Suggestions:")
        print("  - Try different keywords (e.g., 'bearing', 'anchor', 'moment')")
        print("  - Check spelling")
        print("  - Try broader terms")
        return 0

    print(f"Found {len(results)} file(s) with matches:")
    print()

    # Show top results
    for i, (filename, matches, score) in enumerate(results[:args.max_results], 1):
        print(f"{i}. {filename} (Relevance: {score})")
        print(f"   {len(matches)} match(es) found")
        if matches:
            print(f"   First match:")
            print("   " + matches[0].replace('\n', '\n   '))
        print()

    if len(results) > args.max_results:
        print(f"... and {len(results) - args.max_results} more file(s)")

    return 0


if __name__ == "__main__":
    exit(main())
