#!/usr/bin/env python3
"""
Castellated and Cellular Beam Design Guide Smart Search
========================================================

Intelligent search across AISC Design Guide 31 chapters and examples.
Supports category-based queries with relevance ranking.

캐스틸레이티드 및 셀룰러 보 설계 가이드 스마트 검색
카테고리 기반 검색 및 관련성 순위 지원

Usage:
    python3 smart_search.py "Vierendeel bending" --category design
    python3 smart_search.py "web post buckling" --chapter 3
    python3 smart_search.py "composite beam" --examples-only
"""

import re
import argparse
from pathlib import Path
from typing import List, Dict
import sys

# Category mappings for intelligent search
CATEGORY_KEYWORDS = {
    'manufacturing': ['manufacturing', 'fabrication', 'cutting pattern', 'hexagonal', 'circular',
                     'castellated', 'cellular', 'litzka', 'expansion', 'nomenclature'],
    'applications': ['application', 'use case', 'long span', 'service', 'utilities', 'architectural',
                    'economy', 'advantage', 'disadvantage'],
    'vierendeel': ['vierendeel', 'moment', 'bending', 'opening', 'local forces', 'axial force',
                  'flexural strength', 'T0', 'T1', 'Mvr', 'Equation 3-3', 'Equation 3-10'],
    'webpost': ['web post', 'buckling', 'horizontal shear', 'post', 'dp', 'stability',
               'Equation 3-22', 'Equation 3-28', 'Mocr', 'elastic buckling'],
    'shear': ['shear', 'vertical shear', 'web shear', 'gross section', 'net section',
             'shear strength', 'Vn'],
    'deflection': ['deflection', 'serviceability', 'stiffness', 'camber', 'I-effective',
                  'moment of inertia', 'net section'],
    'ltb': ['lateral-torsional', 'LTB', 'unbraced length', 'Lb', 'buckling', 'bracing'],
    'composite': ['composite', 'concrete deck', 'slab', 'shear connector', 'PNA', 'partially composite',
                 'fully composite', 'Vc', 'Xt'],
    'examples': ['example', 'calculation', 'design', 'W18', 'W21', 'W24', 'CB', 'LB',
                'Example 4.1', 'Example 4.2', 'Example 4.3', 'Example 4.4'],
}

# Chapter/file mapping
CHAPTER_FILES = {
    '1': 'design-guide/Chapter_1_Introduction.md',
    '2': 'design-guide/Chapter_2_Use_Cases.md',
    '3': 'design-guide/Chapter_3_Design_Procedures.md',
    'example_4.1': 'examples/Example_4-1_Noncomposite_Castellated.md',
    'example_4.2': 'examples/Example_4-2_Noncomposite_Cellular.md',
    'example_4.3': 'examples/Example_4-3_Composite_Castellated.md',
    'example_4.4': 'examples/Example_4-4_Composite_Cellular.md',
}


class DesignGuideSearcher:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.results = []

    def search(self, query: str, category: str = None, chapter: str = None,
              examples_only: bool = False, max_results: int = 20) -> List[Dict]:
        """
        Search design guide documents with intelligent filtering.

        Args:
            query: Search query string
            category: Category filter (manufacturing, vierendeel, webpost, etc.)
            chapter: Specific chapter to search (1, 2, 3)
            examples_only: Only search examples
            max_results: Maximum number of results to return
        """
        self.results = []

        # Determine search directories
        search_files = self._get_search_files(category, chapter, examples_only)

        # Perform search
        for file_path in search_files:
            if not file_path.exists():
                continue

            self._search_file(file_path, query)

        # Rank and sort results
        self._rank_results(query, category)

        return self.results[:max_results]

    def _get_search_files(self, category: str, chapter: str, examples_only: bool) -> List[Path]:
        """Determine which files to search based on filters."""
        files = []

        if examples_only:
            # Search only example files
            example_dir = self.data_dir / 'examples'
            if example_dir.exists():
                files.extend(example_dir.glob('Example_*.md'))
            return files

        if chapter:
            # Search specific chapter
            if chapter in CHAPTER_FILES:
                files.append(self.data_dir / CHAPTER_FILES[chapter])
            else:
                print(f"Warning: Unknown chapter {chapter}", file=sys.stderr)
            return files

        if category:
            # Category-based search - prioritize relevant chapters
            if category == 'manufacturing':
                files.append(self.data_dir / CHAPTER_FILES['1'])
            elif category == 'applications':
                files.append(self.data_dir / CHAPTER_FILES['2'])
            elif category in ['vierendeel', 'webpost', 'shear', 'deflection', 'ltb', 'composite']:
                files.append(self.data_dir / CHAPTER_FILES['3'])
            elif category == 'examples':
                example_dir = self.data_dir / 'examples'
                if example_dir.exists():
                    files.extend(example_dir.glob('Example_*.md'))

        if not files:
            # Search all files
            design_guide_dir = self.data_dir / 'design-guide'
            examples_dir = self.data_dir / 'examples'

            if design_guide_dir.exists():
                files.extend(design_guide_dir.glob('Chapter_*.md'))
            if examples_dir.exists():
                files.extend(examples_dir.glob('Example_*.md'))

        return files

    def _search_file(self, file_path: Path, query: str):
        """Search within a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find matches (case-insensitive)
            pattern = re.compile(re.escape(query), re.IGNORECASE)
            matches = list(pattern.finditer(content))

            if not matches:
                # Try partial word matching
                words = query.lower().split()
                if all(word in content.lower() for word in words):
                    matches = [None]  # Placeholder for partial match

            if matches:
                # Extract context for each match
                for match in matches[:5]:  # Limit to 5 matches per file
                    if match:
                        context = self._extract_context(content, match.start(), match.end())
                        line_num = content[:match.start()].count('\n') + 1
                    else:
                        # Partial match - find first occurrence of first word
                        first_word = words[0]
                        idx = content.lower().find(first_word)
                        context = self._extract_context(content, idx, idx + len(first_word))
                        line_num = content[:idx].count('\n') + 1 if idx >= 0 else 1

                    self.results.append({
                        'file': file_path.relative_to(self.data_dir),
                        'line': line_num,
                        'context': context,
                        'relevance': 0  # Will be calculated later
                    })

        except Exception as e:
            print(f"Error searching {file_path}: {e}", file=sys.stderr)

    def _extract_context(self, content: str, start: int, end: int, context_lines: int = 3) -> str:
        """Extract context around match."""
        lines = content.split('\n')
        match_line = content[:start].count('\n')

        start_line = max(0, match_line - context_lines)
        end_line = min(len(lines), match_line + context_lines + 1)

        context_lines_list = lines[start_line:end_line]

        # Truncate long lines
        truncated = []
        for line in context_lines_list:
            if len(line) > 150:
                line = line[:147] + '...'
            truncated.append(line)

        return '\n'.join(truncated)

    def _rank_results(self, query: str, category: str = None):
        """Rank results by relevance."""
        query_lower = query.lower()

        for result in self.results:
            score = 0
            context_lower = result['context'].lower()
            file_str = str(result['file']).lower()

            # Exact phrase match
            if query_lower in context_lower:
                score += 10

            # Word matches
            words = query_lower.split()
            for word in words:
                if word in context_lower:
                    score += 2

            # File type priority
            if 'chapter_3' in file_str:
                score += 5  # Design procedures most important
            elif 'example' in file_str:
                score += 4  # Examples second
            elif 'chapter_2' in file_str:
                score += 3
            elif 'chapter_1' in file_str:
                score += 2

            # Category keyword matching
            if category and category in CATEGORY_KEYWORDS:
                for keyword in CATEGORY_KEYWORDS[category]:
                    if keyword in context_lower:
                        score += 3

            # Formula/equation indicators
            if any(pattern in context_lower for pattern in ['equation', '=', 'formula', '$$']):
                score += 3

            # Specific technical terms
            technical_terms = ['vierendeel', 'web post', 'buckling', 'castellated', 'cellular']
            for term in technical_terms:
                if term in query_lower and term in context_lower:
                    score += 5

            result['relevance'] = score

        # Sort by relevance
        self.results.sort(key=lambda x: x['relevance'], reverse=True)


def print_results(results: List[Dict], verbose: bool = False):
    """Print search results in a readable format."""
    if not results:
        print("No results found.")
        return

    print(f"\n{'='*80}")
    print(f"Found {len(results)} results:")
    print(f"{'='*80}\n")

    for i, result in enumerate(results, 1):
        print(f"{i}. {result['file']}:{result['line']}")
        print(f"   Relevance: {result['relevance']}")
        if verbose:
            print(f"\n{result['context']}\n")
        print()


def main():
    parser = argparse.ArgumentParser(
        description='Smart search tool for AISC Design Guide 31',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Search for Vierendeel bending:
    python3 smart_search.py "Vierendeel bending" --category vierendeel

  Search for web post buckling:
    python3 smart_search.py "web post buckling" --category webpost

  Search in Chapter 3 only:
    python3 smart_search.py "composite" --chapter 3

  Search examples only:
    python3 smart_search.py "W18x35" --examples-only

  Verbose output with context:
    python3 smart_search.py "Equation 3-3" --verbose
        """
    )

    parser.add_argument('query', help='Search query')
    parser.add_argument('--category', choices=['manufacturing', 'applications', 'vierendeel',
                       'webpost', 'shear', 'deflection', 'ltb', 'composite', 'examples'],
                       help='Category to search')
    parser.add_argument('--chapter', choices=['1', '2', '3'], help='Specific chapter to search')
    parser.add_argument('--examples-only', action='store_true', help='Only search examples')
    parser.add_argument('--max-results', type=int, default=20, help='Maximum results to show')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show context for each result')

    args = parser.parse_args()

    # Find data directory
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / 'data'

    if not data_dir.exists():
        print(f"Error: Data directory not found at {data_dir}", file=sys.stderr)
        sys.exit(1)

    # Perform search
    searcher = DesignGuideSearcher(data_dir)
    results = searcher.search(
        args.query,
        category=args.category,
        chapter=args.chapter,
        examples_only=args.examples_only,
        max_results=args.max_results
    )

    # Print results
    print_results(results, verbose=args.verbose)

    # Summary
    if results:
        print(f"{'='*80}")
        unique_files = set(str(r['file']) for r in results[:5])
        print(f"Top files: {', '.join(unique_files)}")
        print(f"{'='*80}")


if __name__ == '__main__':
    main()
