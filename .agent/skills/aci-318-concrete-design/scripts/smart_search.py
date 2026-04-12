#!/usr/bin/env python3
"""
ACI 318-25 Smart Search Script
===============================

Purpose: Intelligent keyword-based search across ACI 318-25 consolidated documents
         Maps common queries to appropriate chapters and sections

Author: Claude Code
Date: 2025-11-14
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass
import argparse


@dataclass
class SearchResult:
    """Container for search results"""
    file_path: str
    section_id: str
    context: str
    relevance_score: float
    page_reference: str


# Keyword-to-chapter mapping
KEYWORD_MAPPINGS = {
    # Flexural design
    'flexure': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'bending': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'moment': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'beam': ['Part_3_Members'],

    # Shear design
    'shear': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'punching': ['Part_3_Members'],
    'two-way shear': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'one-way shear': ['Part_3_Members', 'Part_7_Strength_Serviceability'],

    # Slabs
    'slab': ['Part_3_Members'],
    'one-way slab': ['Part_3_Members'],
    'two-way slab': ['Part_3_Members'],
    'flat plate': ['Part_3_Members'],
    'flat slab': ['Part_3_Members'],

    # Columns
    'column': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'compression': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'axial': ['Part_3_Members', 'Part_7_Strength_Serviceability'],

    # Walls
    'wall': ['Part_3_Members', 'Part_5_Earthquake_Resistance'],
    'shear wall': ['Part_3_Members', 'Part_5_Earthquake_Resistance'],
    'structural wall': ['Part_3_Members', 'Part_5_Earthquake_Resistance'],

    # Foundations
    'foundation': ['Part_3_Members'],
    'footing': ['Part_3_Members'],
    'pile cap': ['Part_3_Members'],

    # Seismic design
    'seismic': ['Part_5_Earthquake_Resistance'],
    'earthquake': ['Part_5_Earthquake_Resistance'],
    'SDC': ['Part_5_Earthquake_Resistance'],
    'moment frame': ['Part_5_Earthquake_Resistance'],
    'special moment frame': ['Part_5_Earthquake_Resistance'],
    'intermediate moment frame': ['Part_5_Earthquake_Resistance'],
    'ordinary moment frame': ['Part_5_Earthquake_Resistance'],
    'ductility': ['Part_5_Earthquake_Resistance'],
    'confinement': ['Part_5_Earthquake_Resistance'],

    # Reinforcement detailing
    'development': ['Part_7_Strength_Serviceability'],
    'development length': ['Part_7_Strength_Serviceability'],
    'splice': ['Part_7_Strength_Serviceability'],
    'hook': ['Part_7_Strength_Serviceability'],
    'anchorage': ['Part_7_Strength_Serviceability'],
    'reinforcement': ['Part_7_Strength_Serviceability'],

    # Exposure and durability
    'exposure': ['Part_6_Materials_Durability'],
    'durability': ['Part_6_Materials_Durability'],
    'corrosion': ['Part_6_Materials_Durability'],
    'cover': ['Part_6_Materials_Durability', 'Part_7_Strength_Serviceability'],
    'freezing': ['Part_6_Materials_Durability'],
    'sulfate': ['Part_6_Materials_Durability'],
    'chloride': ['Part_6_Materials_Durability'],

    # Materials
    'concrete': ['Part_6_Materials_Durability'],
    'strength': ['Part_6_Materials_Durability', 'Part_7_Strength_Serviceability'],
    'fc': ['Part_6_Materials_Durability'],
    'fy': ['Part_6_Materials_Durability'],

    # Connections
    'connection': ['Part_4_Joints_Connections'],
    'joint': ['Part_4_Joints_Connections', 'Part_5_Earthquake_Resistance'],
    'beam-column joint': ['Part_4_Joints_Connections', 'Part_5_Earthquake_Resistance'],
    'anchor': ['Part_4_Joints_Connections'],
    'embed': ['Part_4_Joints_Connections'],

    # Serviceability
    'deflection': ['Part_7_Strength_Serviceability'],
    'crack': ['Part_7_Strength_Serviceability'],
    'vibration': ['Part_7_Strength_Serviceability'],

    # Analysis
    'analysis': ['Part_2_Loads_Analysis'],
    'load': ['Part_2_Loads_Analysis'],
    'load combination': ['Part_2_Loads_Analysis'],
    'P-delta': ['Part_2_Loads_Analysis'],
    'second-order': ['Part_2_Loads_Analysis'],

    # Strut-and-tie
    'strut-and-tie': ['Part_7_Strength_Serviceability'],
    'strut': ['Part_7_Strength_Serviceability'],
    'tie': ['Part_7_Strength_Serviceability'],
    'nodal zone': ['Part_7_Strength_Serviceability'],

    # Prestressed
    'prestressed': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'post-tensioned': ['Part_3_Members', 'Part_7_Strength_Serviceability'],
    'tendon': ['Part_3_Members', 'Part_7_Strength_Serviceability'],

    # Construction
    'construction': ['Part_8_Construction'],
    'formwork': ['Part_8_Construction'],
    'curing': ['Part_8_Construction'],

    # Strength reduction factors
    'phi': ['Part_7_Strength_Serviceability'],
    'strength reduction': ['Part_7_Strength_Serviceability'],
}


class SmartSearch:
    """Smart search engine for ACI 318-25 documents"""

    def __init__(self, data_dir: str):
        """
        Initialize search engine

        Args:
            data_dir: Path to consolidated data directory
        """
        self.data_dir = Path(data_dir)
        self.code_dir = self.data_dir / 'code'
        self.commentary_dir = self.data_dir / 'commentary'
        self.appendix_dir = self.data_dir / 'appendices'

    def search(self, query: str, search_commentary: bool = True,
               max_results: int = 20) -> List[SearchResult]:
        """
        Search for query across documents

        Args:
            query: Search query (keywords or phrase)
            search_commentary: Whether to search commentary as well
            max_results: Maximum number of results to return

        Returns:
            List of SearchResult objects, sorted by relevance
        """
        results = []

        # Determine which files to search based on keyword mapping
        target_files = self._get_target_files(query)

        # Search CODE files
        for file_path in target_files['code']:
            results.extend(self._search_file(file_path, query, 'CODE'))

        # Search COMMENTARY files if requested
        if search_commentary:
            for file_path in target_files['commentary']:
                results.extend(self._search_file(file_path, query, 'COMMENTARY'))

        # Sort by relevance score
        results.sort(key=lambda x: x.relevance_score, reverse=True)

        return results[:max_results]

    def _get_target_files(self, query: str) -> Dict[str, List[Path]]:
        """Determine which files to search based on query keywords"""
        query_lower = query.lower()
        target_parts = set()

        # Check keyword mappings
        for keyword, parts in KEYWORD_MAPPINGS.items():
            if keyword.lower() in query_lower:
                target_parts.update(parts)

        # If no specific mapping found, search all files
        if not target_parts:
            target_parts = {'Part_1_General', 'Part_2_Loads_Analysis', 'Part_3_Members',
                           'Part_4_Joints_Connections', 'Part_5_Earthquake_Resistance',
                           'Part_6_Materials_Durability', 'Part_7_Strength_Serviceability',
                           'Part_8_Construction', 'Part_10_Evaluation'}

        code_files = []
        commentary_files = []

        for part in target_parts:
            code_file = self.code_dir / f"{part}.md"
            if code_file.exists():
                code_files.append(code_file)

            commentary_file = self.commentary_dir / f"Commentary_{part}.md"
            if commentary_file.exists():
                commentary_files.append(commentary_file)

        return {'code': code_files, 'commentary': commentary_files}

    def _search_file(self, file_path: Path, query: str, doc_type: str) -> List[SearchResult]:
        """Search within a single file"""
        results = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return results

        # Split into sections
        sections = self._split_sections(content)

        # Search each section
        for section_id, section_content in sections:
            score = self._calculate_relevance(section_content, query)
            if score > 0:
                # Extract context around matches
                context = self._extract_context(section_content, query)
                page_ref = self._extract_page_reference(section_content)

                results.append(SearchResult(
                    file_path=str(file_path),
                    section_id=section_id,
                    context=context,
                    relevance_score=score,
                    page_reference=page_ref
                ))

        return results

    def _split_sections(self, content: str) -> List[Tuple[str, str]]:
        """Split content into sections based on section numbers"""
        sections = []

        # Pattern for section headers (e.g., 7.2.3.1, R7.2.3.1, 22.5.8.5.3)
        section_pattern = r'^(R?\d+\.\d+(?:\.\d+)*(?:\.\d+)?)\s'

        lines = content.split('\n')
        current_section = None
        current_content = []

        for line in lines:
            match = re.match(section_pattern, line)
            if match:
                # Save previous section
                if current_section:
                    sections.append((current_section, '\n'.join(current_content)))

                # Start new section
                current_section = match.group(1)
                current_content = [line]
            else:
                current_content.append(line)

        # Save last section
        if current_section:
            sections.append((current_section, '\n'.join(current_content)))

        return sections

    def _calculate_relevance(self, text: str, query: str) -> float:
        """Calculate relevance score for text based on query"""
        text_lower = text.lower()
        query_lower = query.lower()

        # Exact phrase match gets highest score
        if query_lower in text_lower:
            score = 10.0
        else:
            score = 0.0

        # Individual word matches
        query_words = query_lower.split()
        for word in query_words:
            if len(word) > 2:  # Skip very short words
                count = text_lower.count(word)
                score += count * 0.5

        # Boost score if found in headers
        if re.search(r'^#+\s.*' + query_lower, text, re.IGNORECASE | re.MULTILINE):
            score *= 1.5

        # Boost for equation references
        if re.search(r'Eq\.\s*\d', text) and any(w in query_lower for w in ['formula', 'equation']):
            score *= 1.2

        return score

    def _extract_context(self, text: str, query: str, context_lines: int = 3) -> str:
        """Extract context around query matches"""
        lines = text.split('\n')
        query_lower = query.lower()
        context_snippets = []

        for i, line in enumerate(lines):
            if query_lower in line.lower():
                # Get surrounding lines
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                snippet = '\n'.join(lines[start:end])
                context_snippets.append(snippet)

        # Return first few snippets
        return '\n\n...\n\n'.join(context_snippets[:2])

    def _extract_page_reference(self, text: str) -> str:
        """Extract page reference from section"""
        match = re.search(r'<!-- From Page (\d+) -->', text)
        if match:
            return f"Page {match.group(1)}"
        return "N/A"


def format_results(results: List[SearchResult]) -> str:
    """Format search results for display"""
    if not results:
        return "No results found."

    output = [f"\nFound {len(results)} results:\n"]
    output.append("=" * 80 + "\n")

    for i, result in enumerate(results, 1):
        file_name = Path(result.file_path).name
        output.append(f"{i}. Section {result.section_id}")
        output.append(f"   File: {file_name}")
        output.append(f"   Page: {result.page_reference}")
        output.append(f"   Relevance: {result.relevance_score:.1f}")
        output.append(f"\n   Context:")
        # Indent context
        context_lines = result.context.split('\n')
        for line in context_lines[:10]:  # Limit context display
            output.append(f"   {line}")
        output.append("\n" + "-" * 80 + "\n")

    return '\n'.join(output)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Smart search for ACI 318-25 documents'
    )
    parser.add_argument(
        'query',
        type=str,
        help='Search query (keywords or phrase)'
    )
    parser.add_argument(
        '--data-dir',
        type=str,
        default='/home/hankm/Code_Work/ACI318_Engineer/.claude/skills/aci-318-concrete-design/data',
        help='Path to data directory'
    )
    parser.add_argument(
        '--no-commentary',
        action='store_true',
        help='Exclude commentary from search'
    )
    parser.add_argument(
        '--max-results',
        type=int,
        default=20,
        help='Maximum number of results to return'
    )

    args = parser.parse_args()

    # Run search
    searcher = SmartSearch(args.data_dir)
    results = searcher.search(
        args.query,
        search_commentary=not args.no_commentary,
        max_results=args.max_results
    )

    # Display results
    print(format_results(results))


if __name__ == '__main__':
    main()
