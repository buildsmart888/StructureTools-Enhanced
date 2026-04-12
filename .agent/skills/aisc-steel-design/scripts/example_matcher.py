#!/usr/bin/env python3
"""
AISC Example Matcher
====================

Matches user queries to appropriate design examples.

Usage:
    python3 example_matcher.py "W-shape beam" "flexure"
    python3 example_matcher.py "column" "compression"
    python3 example_matcher.py "bolt connection"

Output:
    JSON array of matching examples with descriptions
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict

# Paths
SKILL_DIR = Path(__file__).parent.parent
EXAMPLES_INDEX = SKILL_DIR / "references" / "design-examples-index.md"
EXAMPLES_DIR = SKILL_DIR / "data" / "design-examples"

# Example categories mapping
CATEGORY_KEYWORDS = {
    "beam": ["Part_I/Chapter_F", "Part_I/Chapter_G"],
    "column": ["Part_I/Chapter_E"],
    "tension": ["Part_I/Chapter_D"],
    "flexure": ["Part_I/Chapter_F"],
    "compression": ["Part_I/Chapter_E"],
    "shear": ["Part_I/Chapter_G"],
    "combined": ["Part_I/Chapter_H"],
    "composite": ["Part_I/Chapter_I"],
    "connection": ["Part_I/Chapter_J", "Part_II"],
    "bolt": ["Part_II/Chapter_IIA"],
    "weld": ["Part_II/Chapter_IIA", "Part_II/Chapter_IIB"],
    "moment": ["Part_II/Chapter_IIB"],
    "bracing": ["Part_II/Chapter_IIC"],
    "HSS": ["Part_I/Chapter_K"],
    "stability": ["Part_III"],
    "building": ["Part_III"],
}


def parse_examples_index() -> List[Dict]:
    """Parse the design examples index file."""
    examples = []

    try:
        with open(EXAMPLES_INDEX, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract example entries (look for example numbers like "E.1A", "F.1-1A", etc.)
        lines = content.split('\n')

        current_chapter = None
        for line in lines:
            # Detect chapter headers
            if line.startswith('##') and 'Chapter' in line:
                current_chapter = line.strip('#').strip()

            # Detect example entries (simplified parsing)
            if re.search(r'[A-Z]\.\d+[A-Z]?', line) or re.search(r'II-[A-Z]\.\d+', line):
                examples.append({
                    "chapter": current_chapter,
                    "line": line.strip(),
                    "text": line.strip()
                })

    except Exception as e:
        print(f"Error parsing examples index: {e}", file=sys.stderr)

    return examples


def match_query_to_categories(query: str) -> List[str]:
    """Match query keywords to example categories."""
    query_lower = query.lower()
    matched_categories = []

    for keyword, categories in CATEGORY_KEYWORDS.items():
        if keyword in query_lower:
            matched_categories.extend(categories)

    return list(set(matched_categories))


def find_example_files(categories: List[str]) -> List[Dict]:
    """Find example files matching categories."""
    results = []

    for category in categories:
        category_path = EXAMPLES_DIR / category

        if category_path.is_file():
            # Direct file match
            results.append({
                "category": category,
                "file": str(category_path.relative_to(SKILL_DIR)),
                "size_kb": category_path.stat().st_size / 1024
            })
        elif '*' in category or category.endswith('/'):
            # Glob pattern
            pattern = category if category.endswith('*') else category + "*.md"
            for match in EXAMPLES_DIR.glob(pattern):
                if match.is_file() and match.name != "README.md":
                    results.append({
                        "category": category,
                        "file": str(match.relative_to(SKILL_DIR)),
                        "size_kb": match.stat().st_size / 1024
                    })
        else:
            # Try as directory
            try:
                for match in Path(EXAMPLES_DIR / category).glob("*.md"):
                    if match.name != "README.md":
                        results.append({
                            "category": category,
                            "file": str(match.relative_to(SKILL_DIR)),
                            "size_kb": match.stat().st_size / 1024
                        })
            except:
                pass

    return results


def search_examples_content(query: str, files: List[Dict]) -> List[Dict]:
    """Search example files for query keywords."""
    results = []

    for file_info in files:
        filepath = SKILL_DIR / file_info['file']

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Count keyword matches
            query_lower = query.lower()
            content_lower = content.lower()
            match_count = sum(1 for word in query_lower.split() if word in content_lower)

            if match_count > 0:
                # Extract first few lines for preview
                lines = content.split('\n')
                preview = '\n'.join(lines[:10])

                results.append({
                    **file_info,
                    "match_score": match_count,
                    "preview": preview[:500]  # First 500 chars
                })

        except Exception as e:
            print(f"Error reading {filepath}: {e}", file=sys.stderr)

    # Sort by match score
    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results


def match_examples(query: str) -> Dict:
    """Main example matching function."""
    categories = match_query_to_categories(query)
    files = find_example_files(categories)
    matches = search_examples_content(query, files)

    # Also parse index for structured data
    indexed_examples = parse_examples_index()

    return {
        "query": query,
        "matched_categories": categories,
        "total_files": len(files),
        "top_matches": matches[:5],  # Top 5 matches
        "indexed_examples_count": len(indexed_examples)
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 example_matcher.py \"query\" [additional keywords]")
        print("\nExamples:")
        print("  python3 example_matcher.py \"W-shape beam flexure\"")
        print("  python3 example_matcher.py \"column compression\"")
        print("  python3 example_matcher.py \"bolt connection\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    results = match_examples(query)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
