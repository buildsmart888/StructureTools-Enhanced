#!/usr/bin/env python3
from pathlib import Path
import sys
repo_root = Path(__file__).parents[1]
sys.path.insert(0, str(repo_root))

def main():
    try:
        from freecad.StructureTools.data.EnhancedSteelDatabase import get_enhanced_database
        from freecad.StructureTools.data.ImportedProfilesImporter import import_profiles_json
    except Exception as e:
        print('Import error:', e)
        raise

    db = get_enhanced_database()
    print('db.available =', getattr(db, 'available', None))
    print('Has sections_database:', hasattr(db, 'sections_database'))
    if hasattr(db, 'sections_database'):
        print('sections_database keys:', list(db.sections_database.keys()))

    json_file = Path('data/generated_steel_db.json')
    if not json_file.exists():
        print('Generated JSON not found:', json_file)
        return 2

    ok = import_profiles_json(str(json_file), db)
    print('import_profiles_json returned', ok)
    if hasattr(db, 'sections_database'):
        print('After import keys:', list(db.sections_database.keys()))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
