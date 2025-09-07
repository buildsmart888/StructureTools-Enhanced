#!/usr/bin/env python3
"""Run the import_steelpy_shapes.py to generate JSON and then merge it into the EnhancedSteelDatabase in this repository.

Usage:
  python scripts\merge_generated_json.py --shapes-folder data/raw --output data/generated_steel_db.json
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_generate(input_dir: str, output_file: str) -> int:
    # Call the script in this repo
    script = Path(__file__).parent / 'import_steelpy_shapes.py'
    cmd = [sys.executable, str(script), '--input-dir', input_dir, '--output', output_file]
    print('Running:', ' '.join(cmd))
    return subprocess.call(cmd)


def merge_into_db(json_file: str) -> int:
    # Import the repo module to run the importer
    # The repository layout places the `freecad` package inside the
    # StructureTools folder (one level up from scripts). Ensure that
    # the parent of `freecad` is on sys.path so imports like
    # `from freecad.StructureTools...` resolve correctly.
    repo_root = Path(__file__).parents[1]
    sys.path.insert(0, str(repo_root))
    try:
        from freecad.StructureTools.data.EnhancedSteelDatabase import get_enhanced_database
        from freecad.StructureTools.data.ImportedProfilesImporter import import_profiles_json
    except Exception as e:
        print('Failed to import repo modules:', e)
        return 2

    db = get_enhanced_database()
    ok = import_profiles_json(json_file, db)
    return 0 if ok else 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shapes-folder', required=True)
    parser.add_argument('--output', default='data/generated_steel_db.json')
    args = parser.parse_args()

    input_dir = args.shapes_folder
    out_file = args.output

    rc = run_generate(input_dir, out_file)
    if rc != 0:
        print('Generator script failed with code', rc)
        return rc

    rc2 = merge_into_db(out_file)
    return rc2


if __name__ == '__main__':
    raise SystemExit(main())
