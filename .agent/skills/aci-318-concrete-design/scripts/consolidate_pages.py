#!/usr/bin/env python3
"""
ACI 318-25 Page Consolidation Script
====================================

Purpose: Merge 702 individual page markdown files into logical chapter-based files
         Split CODE and COMMENTARY sections into separate files

Author: Claude Code
Date: 2025-11-14
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict

# Chapter structure mapping based on ACI 318-25 table of contents
CHAPTER_STRUCTURE = {
    # Part 1: General (Pages 9-68)
    'Part_1_General': {
        'start_page': 10,
        'end_page': 68,
        'chapters': [
            {'num': 1, 'title': 'General'},
            {'num': 2, 'title': 'Notation and Terminology'},
            {'num': 3, 'title': 'Referenced Standards'},
            {'num': 4, 'title': 'Structural System Requirements'}
        ]
    },
    # Part 2: Loads & Analysis (Pages 69-97)
    'Part_2_Loads_Analysis': {
        'start_page': 69,
        'end_page': 97,
        'chapters': [
            {'num': 5, 'title': 'Loads'},
            {'num': 6, 'title': 'Structural Analysis'}
        ]
    },
    # Part 3: Members (Pages 99-208)
    'Part_3_Members': {
        'start_page': 100,
        'end_page': 208,
        'chapters': [
            {'num': 7, 'title': 'One-Way Slabs'},
            {'num': 8, 'title': 'Two-Way Slabs'},
            {'num': 9, 'title': 'Beams'},
            {'num': 10, 'title': 'Columns'},
            {'num': 11, 'title': 'Walls'},
            {'num': 12, 'title': 'Diaphragms'},
            {'num': 13, 'title': 'Foundations'}
        ]
    },
    # Part 4: Joints and Connections (Pages 209-300)
    'Part_4_Joints_Connections': {
        'start_page': 209,
        'end_page': 300,
        'chapters': [
            {'num': 14, 'title': 'Joints'},
            {'num': 15, 'title': 'Connections Between Members'},
            {'num': 16, 'title': 'Connections to Concrete'}
        ]
    },
    # Part 5: Earthquake Resistance (Pages 303-394)
    'Part_5_Earthquake_Resistance': {
        'start_page': 303,
        'end_page': 394,
        'chapters': [
            {'num': 17, 'title': 'Earthquake-Resistant Structures'}
        ]
    },
    # Part 6: Materials, Construction & Durability (Pages 395-434)
    'Part_6_Materials_Durability': {
        'start_page': 395,
        'end_page': 434,
        'chapters': [
            {'num': 18, 'title': 'Concrete: Design and Durability Requirements'},
            {'num': 19, 'title': 'Concrete: Design and Durability Requirements (continued)'},
            {'num': 20, 'title': 'Steel Reinforcement Properties, Durability, and Embedments'}
        ]
    },
    # Part 7: Strength & Serviceability (Pages 435-564)
    'Part_7_Strength_Serviceability': {
        'start_page': 435,
        'end_page': 564,
        'chapters': [
            {'num': 21, 'title': 'Strength Reduction Factors'},
            {'num': 22, 'title': 'Sectional Strength'},
            {'num': 23, 'title': 'Strut-and-Tie Method'},
            {'num': 24, 'title': 'Serviceability'},
            {'num': 25, 'title': 'Reinforcement Details'}
        ]
    },
    # Part 8: Construction (Pages 565-607)
    'Part_8_Construction': {
        'start_page': 565,
        'end_page': 607,
        'chapters': [
            {'num': 26, 'title': 'Construction Documents and Submittals'}
        ]
    },
    # Part 10: Evaluation (Pages 609-620)
    'Part_10_Evaluation': {
        'start_page': 609,
        'end_page': 620,
        'chapters': [
            {'num': 27, 'title': 'Strength Evaluation of Existing Structures'}
        ]
    }
}

# Appendices structure
APPENDICES = {
    'Appendix_A_Nonlinear_Analysis': {
        'title': 'Design Verification Using Nonlinear Response History Analysis',
        'start_page': 621,
        'end_page': 635
    },
    'Appendix_B_Performance_Wind': {
        'title': 'Performance-Based Wind Design',
        'start_page': 636,
        'end_page': 654
    },
    'Appendix_C_Sustainability': {
        'title': 'Sustainability and Resilience',
        'start_page': 655,
        'end_page': 662
    },
    'Appendix_D_Steel_Info': {
        'title': 'Steel Reinforcement Information',
        'start_page': 663,
        'end_page': 698
    }
}


class PageConsolidator:
    """Consolidate ACI 318-25 page files into chapter files"""

    def __init__(self, source_dir: str, output_base: str):
        """
        Initialize consolidator

        Args:
            source_dir: Directory containing individual page markdown files
            output_base: Base directory for consolidated output
        """
        self.source_dir = Path(source_dir)
        self.output_base = Path(output_base)
        self.code_dir = self.output_base / 'data' / 'code'
        self.commentary_dir = self.output_base / 'data' / 'commentary'
        self.appendix_dir = self.output_base / 'data' / 'appendices'

        # Create output directories
        self.code_dir.mkdir(parents=True, exist_ok=True)
        self.commentary_dir.mkdir(parents=True, exist_ok=True)
        self.appendix_dir.mkdir(parents=True, exist_ok=True)

    def read_page(self, page_num: int) -> Optional[str]:
        """Read a single page file"""
        filename = f"ACI 318-25_page_{page_num:03d}.md"
        filepath = self.source_dir / filename

        if not filepath.exists():
            print(f"Warning: Page {page_num} not found: {filepath}")
            return None

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading page {page_num}: {e}")
            return None

    def split_code_commentary(self, content: str) -> Tuple[str, str]:
        """
        Split content into CODE and COMMENTARY sections

        Returns:
            Tuple of (code_content, commentary_content)
        """
        # Pattern to detect CODE and COMMENTARY headers
        code_sections = []
        commentary_sections = []

        # Split by major section headers
        lines = content.split('\n')
        current_mode = None  # 'CODE' or 'COMMENTARY'
        current_buffer = []

        for line in lines:
            # Detect section headers
            if re.match(r'^##?\s*CODE\s*$', line, re.IGNORECASE) or \
               re.match(r'^\*\*CODE\*\*\s*$', line):
                if current_mode == 'COMMENTARY' and current_buffer:
                    commentary_sections.append('\n'.join(current_buffer))
                current_mode = 'CODE'
                current_buffer = [line]
            elif re.match(r'^##?\s*COMMENTARY\s*$', line, re.IGNORECASE) or \
                 re.match(r'^\*\*COMMENTARY\*\*\s*$', line):
                if current_mode == 'CODE' and current_buffer:
                    code_sections.append('\n'.join(current_buffer))
                current_mode = 'COMMENTARY'
                current_buffer = [line]
            elif current_mode in ['CODE', 'COMMENTARY']:
                current_buffer.append(line)
            else:
                # Before any section detected, include in both
                current_buffer.append(line)

        # Flush remaining buffer
        if current_mode == 'CODE' and current_buffer:
            code_sections.append('\n'.join(current_buffer))
        elif current_mode == 'COMMENTARY' and current_buffer:
            commentary_sections.append('\n'.join(current_buffer))
        elif current_buffer and not current_mode:
            # Front matter, add to both
            preamble = '\n'.join(current_buffer)
            code_sections.insert(0, preamble)
            commentary_sections.insert(0, preamble)

        code_content = '\n\n'.join(code_sections)
        commentary_content = '\n\n'.join(commentary_sections)

        return code_content, commentary_content

    def clean_content(self, content: str) -> str:
        """Clean up content (remove copyright footers, etc.)"""
        # Remove copyright footers
        content = re.sub(
            r'Copyright American Concrete Institute.*?MDT',
            '',
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Remove excessive blank lines
        content = re.sub(r'\n{4,}', '\n\n\n', content)

        return content.strip()

    def consolidate_part(self, part_name: str, part_info: Dict) -> None:
        """Consolidate a single part"""
        print(f"\nConsolidating {part_name}...")

        code_content = []
        commentary_content = []

        # Add part header
        part_title = part_name.replace('_', ' ').title()
        code_header = f"# {part_title}\n\n"
        code_header += f"*ACI 318-25 Building Code for Structural Concrete*\n\n"
        code_header += f"**CODE Requirements**\n\n"
        code_header += f"---\n\n"

        commentary_header = f"# {part_title}\n\n"
        commentary_header += f"*ACI 318-25 Building Code for Structural Concrete*\n\n"
        commentary_header += f"**COMMENTARY**\n\n"
        commentary_header += f"---\n\n"

        code_content.append(code_header)
        commentary_content.append(commentary_header)

        # Process each page in range
        for page_num in range(part_info['start_page'], part_info['end_page'] + 1):
            page_content = self.read_page(page_num)
            if not page_content:
                continue

            # Split CODE and COMMENTARY
            code_part, commentary_part = self.split_code_commentary(page_content)

            if code_part.strip():
                code_content.append(f"\n<!-- From Page {page_num} -->\n")
                code_content.append(self.clean_content(code_part))

            if commentary_part.strip():
                commentary_content.append(f"\n<!-- From Page {page_num} -->\n")
                commentary_content.append(self.clean_content(commentary_part))

        # Write consolidated files
        code_file = self.code_dir / f"{part_name}.md"
        commentary_file = self.commentary_dir / f"Commentary_{part_name}.md"

        with open(code_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(code_content))
        print(f"  Created: {code_file} ({len(code_content)} sections)")

        with open(commentary_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(commentary_content))
        print(f"  Created: {commentary_file} ({len(commentary_content)} sections)")

    def consolidate_appendix(self, appendix_name: str, appendix_info: Dict) -> None:
        """Consolidate a single appendix"""
        print(f"\nConsolidating {appendix_name}...")

        content = []

        # Add appendix header
        appendix_title = appendix_info['title']
        header = f"# {appendix_name.replace('_', ' ').title()}\n\n"
        header += f"**{appendix_title}**\n\n"
        header += f"*ACI 318-25 Building Code for Structural Concrete*\n\n"
        header += f"---\n\n"

        content.append(header)

        # Process each page in range
        for page_num in range(appendix_info['start_page'], appendix_info['end_page'] + 1):
            page_content = self.read_page(page_num)
            if not page_content:
                continue

            content.append(f"\n<!-- From Page {page_num} -->\n")
            content.append(self.clean_content(page_content))

        # Write consolidated file
        appendix_file = self.appendix_dir / f"{appendix_name}.md"

        with open(appendix_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(content))
        print(f"  Created: {appendix_file} ({len(content)} sections)")

    def extract_chapter_2_notation(self) -> None:
        """Extract Chapter 2 notation to separate symbols file"""
        print("\nExtracting Chapter 2 Notation...")

        # Chapter 2 is in Part 1 (pages ~13-30 estimated)
        notation_content = []

        # Read pages that likely contain Chapter 2
        for page_num in range(13, 35):
            page_content = self.read_page(page_num)
            if not page_content:
                continue

            # Check if this page contains notation/terminology
            if re.search(r'CHAPTER 2', page_content, re.IGNORECASE) or \
               re.search(r'Notation|Terminology', page_content, re.IGNORECASE):
                notation_content.append(f"\n<!-- From Page {page_num} -->\n")
                notation_content.append(self.clean_content(page_content))

        # Write notation file
        notation_file = self.output_base / 'data' / 'Notation_Symbols.md'

        header = "# ACI 318-25 Notation and Symbols\n\n"
        header += "*Chapter 2: Notation and Terminology*\n\n"
        header += "---\n\n"

        with open(notation_file, 'w', encoding='utf-8') as f:
            f.write(header + '\n\n'.join(notation_content))
        print(f"  Created: {notation_file}")

    def generate_metadata(self) -> None:
        """Generate metadata about consolidation"""
        metadata = {
            'source_directory': str(self.source_dir),
            'total_pages': 702,
            'parts_consolidated': len(CHAPTER_STRUCTURE),
            'appendices_consolidated': len(APPENDICES),
            'output_directory': str(self.output_base)
        }

        metadata_file = self.output_base / 'consolidation_metadata.txt'

        with open(metadata_file, 'w', encoding='utf-8') as f:
            f.write("ACI 318-25 Consolidation Metadata\n")
            f.write("=" * 50 + "\n\n")
            for key, value in metadata.items():
                f.write(f"{key}: {value}\n")

        print(f"\nMetadata saved to: {metadata_file}")

    def run(self) -> None:
        """Run full consolidation process"""
        print("=" * 60)
        print("ACI 318-25 Page Consolidation")
        print("=" * 60)

        # Consolidate all parts
        for part_name, part_info in CHAPTER_STRUCTURE.items():
            self.consolidate_part(part_name, part_info)

        # Consolidate appendices
        for appendix_name, appendix_info in APPENDICES.items():
            self.consolidate_appendix(appendix_name, appendix_info)

        # Extract Chapter 2 notation
        self.extract_chapter_2_notation()

        # Generate metadata
        self.generate_metadata()

        print("\n" + "=" * 60)
        print("Consolidation Complete!")
        print("=" * 60)


def main():
    """Main entry point"""
    import sys

    # Default paths
    source_dir = "/home/hankm/Code_Work/ACI318_Engineer/markdown"
    output_base = "/home/hankm/Code_Work/ACI318_Engineer/.claude/skills/aci-318-concrete-design"

    # Allow command-line override
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    if len(sys.argv) > 2:
        output_base = sys.argv[2]

    # Run consolidation
    consolidator = PageConsolidator(source_dir, output_base)
    consolidator.run()


if __name__ == '__main__':
    main()
