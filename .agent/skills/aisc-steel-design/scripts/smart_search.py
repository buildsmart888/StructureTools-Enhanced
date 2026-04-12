#!/usr/bin/env python3
"""
AISC Smart Search Tool
======================

Intelligently searches for relevant AISC documents based on user query.
Uses keyword mapping to AISC chapters for efficient document discovery.

Usage:
    python3 smart_search.py "lateral-torsional buckling"
    python3 smart_search.py "beam design flexure"
    python3 smart_search.py "bolt connection"

Output:
    JSON array of relevant AISC documents with priority scores
"""

import sys
import json
import os
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Keyword to AISC chapter mapping
KEYWORD_TO_CHAPTERS = {
    # Flexure / Beam Design
    "flexure": ["F", "H"],
    "bending": ["F", "H"],
    "beam": ["F", "H", "G"],
    "lateral-torsional": ["F"],
    "LTB": ["F"],
    "Cb": ["F"],
    "compact": ["F", "E"],
    "non-compact": ["F", "E"],
    "slender": ["F", "E"],
    "yielding": ["F", "D", "J"],
    "plastic moment": ["F"],
    "Mn": ["F", "E", "G", "H"],
    "Mp": ["F"],
    "휨": ["F", "H"],
    "보": ["F"],

    # Compression / Column Design
    "compression": ["E", "H"],
    "column": ["E", "H"],
    "buckling": ["E", "F"],
    "flexural buckling": ["E"],
    "torsional buckling": ["E"],
    "KL/r": ["E"],
    "slenderness": ["E"],
    "effective length": ["E", "C"],
    "Fcr": ["E"],
    "기둥": ["E"],
    "압축": ["E"],
    "좌굴": ["E", "F"],

    # Tension
    "tension": ["D", "H"],
    "net area": ["D", "J"],
    "gross area": ["D"],
    "effective net area": ["D"],
    "rupture": ["D", "J"],
    "인장": ["D"],

    # Shear
    "shear": ["G", "H", "J"],
    "web": ["G", "F"],
    "tension field": ["G"],
    "kv": ["G"],
    "전단": ["G", "J"],

    # Combined Forces
    "combined": ["H"],
    "interaction": ["H"],
    "P-M": ["H"],
    "axial": ["H", "E", "D"],
    "moment": ["H", "F"],
    "torsion": ["H"],
    "비틀림": ["H"],

    # Connections
    "connection": ["J", "K"],
    "joint": ["J"],
    "bolt": ["J"],
    "weld": ["J"],
    "shear tab": ["J"],
    "moment connection": ["J"],
    "simple connection": ["J"],
    "bearing": ["J"],
    "slip-critical": ["J"],
    "block shear": ["J"],
    "fillet weld": ["J"],
    "groove weld": ["J"],
    "연결부": ["J"],
    "볼트": ["J"],
    "용접": ["J"],

    # HSS
    "HSS": ["K", "E", "F"],
    "hollow": ["K"],
    "tube": ["K"],
    "round": ["K"],
    "rectangular": ["K"],

    # Composite
    "composite": ["I"],
    "shear stud": ["I"],
    "shear connector": ["I"],
    "effective width": ["I"],
    "concrete": ["I"],
    "Qn": ["I"],
    "합성": ["I"],
    "전단연결재": ["I"],

    # Stability
    "stability": ["C", "Appendix6"],
    "second-order": ["C"],
    "P-delta": ["C"],
    "direct analysis": ["C"],
    "bracing": ["C", "Appendix6"],
    "lateral bracing": ["Appendix6"],

    # Design Methods
    "LRFD": ["B"],
    "ASD": ["B"],
    "resistance factor": ["B"],
    "safety factor": ["B"],
    "phi": ["B"],
    "omega": ["B"],
    "하중저항계수": ["B"],
    "허용응력": ["B"],

    # Serviceability
    "deflection": ["L"],
    "drift": ["L"],
    "serviceability": ["L"],
    "처짐": ["L"],

    # Fabrication & Quality
    "fabrication": ["M"],
    "erection": ["M"],
    "quality": ["N"],
    "QC": ["N"],
    "QA": ["N"],
}

# Document paths
SKILL_DIR = Path(__file__).parent.parent
SPEC_DIR = SKILL_DIR / "data" / "specification"
EXAMPLES_DIR = SKILL_DIR / "data" / "design-examples"


def extract_keywords(query: str) -> List[str]:
    """Extract searchable keywords from query."""
    query_lower = query.lower()
    keywords = []

    # Check for exact matches
    for keyword in KEYWORD_TO_CHAPTERS.keys():
        if keyword.lower() in query_lower:
            keywords.append(keyword)

    # Extract individual words as fallback
    words = re.findall(r'\b\w+\b', query)
    keywords.extend([w for w in words if len(w) > 2])

    return list(set(keywords))


def map_keywords_to_chapters(keywords: List[str]) -> Dict[str, int]:
    """Map keywords to chapters with priority scores."""
    chapter_scores = {}

    for keyword in keywords:
        if keyword in KEYWORD_TO_CHAPTERS:
            for chapter in KEYWORD_TO_CHAPTERS[keyword]:
                chapter_scores[chapter] = chapter_scores.get(chapter, 0) + 1

    return chapter_scores


def find_relevant_files(chapter_scores: Dict[str, int]) -> List[Dict]:
    """Find relevant AISC files based on chapter scores."""
    results = []

    # Sort chapters by score
    sorted_chapters = sorted(chapter_scores.items(), key=lambda x: x[1], reverse=True)

    for chapter, score in sorted_chapters:
        # Search in Specification
        spec_file = SPEC_DIR / f"Chapter_{chapter}_*.md"
        spec_matches = list(SPEC_DIR.glob(f"Chapter_{chapter}_*.md"))

        for match in spec_matches:
            results.append({
                "type": "Specification",
                "chapter": chapter,
                "file": str(match.relative_to(SKILL_DIR)),
                "score": score,
                "size_kb": match.stat().st_size / 1024
            })

        # Search in Design Examples Part I
        example_matches = list((EXAMPLES_DIR / "Part_I").glob(f"Chapter_{chapter}_*.md"))
        for match in example_matches:
            results.append({
                "type": "Design Example (Part I)",
                "chapter": chapter,
                "file": str(match.relative_to(SKILL_DIR)),
                "score": score,
                "size_kb": match.stat().st_size / 1024
            })

    # Also search Part II for connection-related queries
    if any(ch in chapter_scores for ch in ["J", "K"]):
        part2_files = list((EXAMPLES_DIR / "Part_II").glob("*.md"))
        for match in part2_files:
            results.append({
                "type": "Design Example (Part II - Connections)",
                "chapter": "J/K",
                "file": str(match.relative_to(SKILL_DIR)),
                "score": chapter_scores.get("J", 0) + chapter_scores.get("K", 0),
                "size_kb": match.stat().st_size / 1024
            })

    # Sort by score
    results.sort(key=lambda x: x["score"], reverse=True)

    return results


def search(query: str) -> Dict:
    """Main search function."""
    keywords = extract_keywords(query)
    chapter_scores = map_keywords_to_chapters(keywords)
    results = find_relevant_files(chapter_scores)

    return {
        "query": query,
        "keywords": keywords,
        "chapter_scores": chapter_scores,
        "results": results[:10],  # Top 10 results
        "total_found": len(results)
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 smart_search.py \"search query\"")
        print("\nExamples:")
        print("  python3 smart_search.py \"lateral-torsional buckling\"")
        print("  python3 smart_search.py \"bolt connection design\"")
        print("  python3 smart_search.py \"beam flexure\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    results = search(query)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
