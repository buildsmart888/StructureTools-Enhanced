Download and import steelpy shape CSVs

This script downloads the steelpy shape CSV files and stores them in the module `data/raw` directory and creates a small SQLite DB `data/steelpy_shapes.db`.

Usage (PowerShell on Windows):

    python .\scripts\download_and_import_steelpy.py --out-dir ".\data" --db ".\data\steelpy_shapes.db"

After running, you'll find:

- data/raw/*.csv  (raw downloaded CSV files)
- data/steelpy_shapes.db  (SQLite DB with table `profiles` containing parsed JSON per-row)

Next steps: write a merger to map rows from `profiles` into EnhancedSteelDatabase.json using the existing `ImportedProfilesImporter` module.
