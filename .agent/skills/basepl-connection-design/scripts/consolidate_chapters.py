#!/usr/bin/env python3
"""
Consolidate 220 individual page markdown files into 8 chapter files.

Usage:
    python3 consolidate_chapters.py

This script combines AISC Design Guide 1 pages into logical chapters:
- Chapter 1: Pages 1-6 (Introduction)
- Chapter 2: Pages 7-10 (Materials)
- Chapter 3: Pages 11-18 (Base Plate Design Theory)
- Chapter 4: Pages 19-140 (Exposed Connections - largest chapter)
- Chapter 5: Pages 141-150 (Embedded Connections)
- Chapter 6: Pages 151-162 (Seismic Design)
- Appendix A: Pages 163-172 (Specialty Anchors)
- Appendix B: Pages 173-220 (Alternate Methods)
"""

import os
from pathlib import Path

# Base paths
MARKDOWN_DIR = Path("/home/hankm/Code_Work/BasePL_Engineer/markdown")
OUTPUT_DIR = Path("/home/hankm/Code_Work/BasePL_Engineer/.claude/skills/basepl-connection-design/data")

# Chapter definitions: (output_filename, start_page, end_page, title)
CHAPTERS = [
    ("Chapter_1_Introduction.md", 1, 6, "Chapter 1: Introduction"),
    ("Chapter_2_Materials.md", 7, 10, "Chapter 2: Materials, Fabrication, Selection, and Other Considerations"),
    ("Chapter_3_Base_Plate_Design.md", 11, 18, "Chapter 3: Base Plate Design"),
    ("Chapter_4_Exposed_Connections.md", 19, 140, "Chapter 4: Design of Exposed Column Base Connections"),
    ("Chapter_5_Embedded_Connections.md", 141, 150, "Chapter 5: Design of Embedded Base Connections"),
    ("Chapter_6_Seismic_Design.md", 151, 162, "Chapter 6: Seismic Design"),
    ("Appendix_A_Specialty_Anchors.md", 163, 172, "Appendix A: Specialty Anchor Systems"),
    ("Appendix_B_Alternate_Methods.md", 173, 220, "Appendix B: Alternate Methods"),
]


def get_page_filename(page_num):
    """Generate the filename for a given page number."""
    return f"AISC-Design-Guide-01-Base-Connection-Design-for-Steel-Structures-3rd-Ed_page_{page_num:03d}.md"


def consolidate_chapter(output_file, start_page, end_page, title):
    """Consolidate pages into a single chapter file."""
    print(f"Consolidating {title} (pages {start_page}-{end_page})...")

    output_path = OUTPUT_DIR / output_file

    with open(output_path, 'w', encoding='utf-8') as outfile:
        # Write chapter header
        outfile.write(f"# {title}\n\n")
        outfile.write(f"*Source: AISC Design Guide 1 - Base Connection Design for Steel Structures (3rd Edition)*\n\n")
        outfile.write(f"*Pages {start_page}-{end_page}*\n\n")
        outfile.write("---\n\n")

        # Consolidate all pages
        for page_num in range(start_page, end_page + 1):
            page_file = MARKDOWN_DIR / get_page_filename(page_num)

            if not page_file.exists():
                print(f"  WARNING: {page_file.name} not found, skipping...")
                continue

            with open(page_file, 'r', encoding='utf-8') as infile:
                content = infile.read()

                # Remove the "<!-- Page X -->" comments
                lines = content.split('\n')
                filtered_lines = [line for line in lines if not line.strip().startswith('<!-- Page')]

                # Remove excessive blank lines at the start
                while filtered_lines and not filtered_lines[0].strip():
                    filtered_lines.pop(0)

                # Write content with page separator
                outfile.write(f"<!-- SOURCE: Page {page_num} -->\n\n")
                outfile.write('\n'.join(filtered_lines))
                outfile.write('\n\n')

    print(f"  ✓ Created {output_file} ({end_page - start_page + 1} pages)")

    # Return file stats
    file_size = output_path.stat().st_size
    return file_size


def main():
    """Main consolidation process."""
    print("AISC Design Guide 1 - Chapter Consolidation")
    print("=" * 60)
    print()

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_size = 0
    stats = []

    # Process each chapter
    for output_file, start_page, end_page, title in CHAPTERS:
        size = consolidate_chapter(output_file, start_page, end_page, title)
        total_size += size
        stats.append((output_file, end_page - start_page + 1, size))
        print()

    # Print summary
    print("=" * 60)
    print("CONSOLIDATION SUMMARY")
    print("=" * 60)
    print(f"{'File':<40} {'Pages':<8} {'Size (KB)':<10}")
    print("-" * 60)

    for filename, page_count, size in stats:
        print(f"{filename:<40} {page_count:<8} {size/1024:<10.1f}")

    print("-" * 60)
    print(f"{'TOTAL':<40} {220:<8} {total_size/1024:<10.1f}")
    print()
    print(f"✓ Successfully consolidated 220 pages into {len(CHAPTERS)} chapter files")
    print(f"✓ Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
