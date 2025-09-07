Import steelpy shape files into a JSON database
===============================================

What this does
--------------
The `import_steelpy_shapes.py` script parses a folder of shape files (plain text,
CSV-like, or other simple formats) and writes a JSON file of profiles suitable
for loading into the GUI that reads `data/enhanced_steel_database.json`.

Usage
-----
Run in PowerShell (example):

```powershell
python .\scripts\import_steelpy_shapes.py --input-dir "C:\path\to\shape_files" --output "data\generated_steel_db.json"
```

Notes
-----
- The parser uses heuristics and extracts numeric properties and 2D point lists.
- If you have the `steelpy` package installed, the script will attempt to use
  it, but this is a best-effort fallback; steelpy APIs vary by version.
- Inspect `data\generated_steel_db.json` before replacing `data\enhanced_steel_database.json`.

Merging into the project DB
---------------------------
1. Backup the original file: `copy data\enhanced_steel_database.json data\enhanced_steel_database.json.bak`
2. Manually merge entries from `data\generated_steel_db.json` into the original
   or replace the file if you want to use the generated set.

Integration ideas for GUI
-------------------------
- Add a menu action "Import steel profiles" pointing to this script.
- After import, the GUI should list new profiles and allow creating sections from
  the profile points (draw) and sending geometry to the calculation code.
