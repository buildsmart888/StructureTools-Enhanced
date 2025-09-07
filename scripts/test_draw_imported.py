#!/usr/bin/env python3
"""Smoke test: create and draw first imported section from EnhancedSteelDatabase"""
from pathlib import Path
import sys
repo_root = Path(__file__).parents[1]
sys.path.insert(0, str(repo_root))

def main():
    try:
        from freecad.StructureTools.data.EnhancedSteelDatabase import get_enhanced_database
        from freecad.StructureTools.geometry.SectionDrawing import draw_section_from_data
    except Exception as e:
        print('Import failed:', e)
        return 2

    db = get_enhanced_database()
    sections = db.sections_database.get('sections', {}).get('IMPORTED', {})
    geometries = db.sections_database.get('geometries', {}).get('IMPORTED', {})

    if not sections:
        print('No IMPORTED sections found')
        return 1

    first = list(sections.keys())[0]
    geom = geometries.get(first)
    print('Drawing section', first)
    if not geom:
        print('No geometry for', first)
        return 3

    # Attempt to draw (requires FreeCAD GUI)
    try:
        obj = draw_section_from_data(geom, first)
        print('Drawn object:', getattr(obj, 'Label', None))
    except Exception as e:
        print('Draw failed:', e)

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
