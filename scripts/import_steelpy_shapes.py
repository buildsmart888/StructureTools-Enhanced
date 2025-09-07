#!/usr/bin/env python3
"""
import_steelpy_shapes.py

Small, defensive importer for steel "shape files" (text/CSV-like) and a fallback
that attempts to extract numeric properties (A, Ix, Iy, J, Zx, Zy, etc.) and
polygon vertex lists. Writes a JSON database compatible with
`data/enhanced_steel_database.json` used by the GUI.

Usage:
  python scripts/import_steelpy_shapes.py --input-dir path/to/shape_files --output data/generated_steel_db.json

This script does not require steelpy. If steelpy is installed, it will try
to use it (best-effort). Otherwise it uses heuristic parsing.

Notes:
- The script is intentionally resilient: it searches for property key/value
  patterns and for lines containing two floats (x y) to build polygon outlines.
- You should inspect and merge the generated JSON into your project DB
  (`data/enhanced_steel_database.json`) once happy.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
from typing import Dict, List, Optional, Tuple


PROPERTY_KEYS = [
    "A",
    "Ix",
    "Iy",
    "Zx",
    "Zy",
    "J",
    "Sx",
    "Sy",
    "d",
    "bf",
    "tf",
    "tw",
]


def try_use_steelpy(path: str) -> Optional[List[Dict]]:
    """Attempt to use steelpy if installed. This is a best-effort attempt and
    will return None if steelpy is not available or its API differs.
    """
    try:
        import importlib

        sp = importlib.import_module("steelpy")
        # steelpy's API changes; attempt common attributes in a defensive way
        # We only attempt this to keep workflow simple if the user has steelpy
        results = []
        # If the package exposes a 'shape' or 'shape_files' module we can try
        for sub in ("shape_files", "shape_files.shape_files", "shape_files.shape"):
            try:
                mod = importlib.import_module(f"steelpy.{sub}")
            except Exception:
                mod = None
            if mod:
                # try to look for a loader or a list of shapes
                loader = getattr(mod, "ShapeFiles", None) or getattr(mod, "ShapeFile", None)
                if loader:
                    # Non-specific: user can adapt this block if their steelpy version
                    # exposes a stable loader
                    try:
                        # Example usage (may fail for many steelpy versions):
                        loaded = loader(path) if callable(loader) else None
                        if loaded:
                            # convert to minimal dicts
                            for name, obj in getattr(loaded, "items", lambda: [])():
                                results.append({"name": name, "properties": {}, "points": []})
                            return results
                    except Exception:
                        pass
        return None
    except Exception:
        return None


def parse_shape_file_text(path: str) -> Dict:
    """Heuristic parser for a single text shape file. Returns a dict with
    keys: name, properties (dict), points (list of [x,y]).
    """
    name = os.path.splitext(os.path.basename(path))[0]
    properties: Dict[str, float] = {}
    points: List[Tuple[float, float]] = []

    float_pair_re = re.compile(r"^\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s+[+-]?\d*\.?\d+(?:[eE][+-]?\d+)?\s*$")
    key_val_re = re.compile(r"^\s*([A-Za-z0-9_]+)\s*[:=]\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s*$")
    # Slightly more permissive: key ... value (space separated)
    key_val_space_re = re.compile(r"^\s*([A-Za-z0-9_]+)\s+([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s*$")

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            # Try key:value pairs
            m = key_val_re.match(line)
            if m:
                k = m.group(1)
                v = float(m.group(2))
                if k in PROPERTY_KEYS or len(k) <= 4:
                    properties[k] = v
                continue
            m = key_val_space_re.match(line)
            if m:
                k = m.group(1)
                try:
                    v = float(m.group(2))
                    if k in PROPERTY_KEYS or len(k) <= 4:
                        properties[k] = v
                        continue
                except Exception:
                    pass

            # Try two-number vertex lines
            parts = line.split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    points.append([x, y])
                    continue
                except Exception:
                    pass

            # Try to find embedded key=value anywhere
            for key in PROPERTY_KEYS:
                rx = re.compile(rf"{re.escape(key)}\s*[:=\s]\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)", re.I)
                mm = rx.search(line)
                if mm:
                    try:
                        properties[key] = float(mm.group(1))
                    except Exception:
                        pass

    return {"name": name, "properties": properties, "points": points}


def parse_csv_file(path: str) -> List[Dict]:
    """Parse a CSV file containing many shape rows (header + rows).
    Returns a list of profile dicts: {id,name,properties,points}
    """
    entries: List[Dict] = []
    try:
        with open(path, newline="", encoding="utf-8", errors="ignore") as cf:
            reader = csv.DictReader(cf)
            if reader.fieldnames is None:
                return entries
            for idx, row in enumerate(reader):
                # Determine a sensible name for the profile
                name = None
                for candidate in ("shape", "Shape", "name", "NAME"):
                    if candidate in row and row[candidate]:
                        name = row[candidate].strip()
                        break
                if not name:
                    base = os.path.splitext(os.path.basename(path))[0]
                    name = f"{base}_{idx}"

                props: Dict[str, float] = {}
                for k, v in (row.items() if hasattr(row, 'items') else []):
                    if v is None:
                        continue
                    s = str(v).strip()
                    if s == "":
                        continue
                    # Try convert numeric values, otherwise keep as string
                    try:
                        # some values contain non-numeric markers like '–' or 'N/A'
                        val = float(s)
                        props[k] = val
                    except Exception:
                        # ignore non-float values for properties
                        pass

                entries.append({"id": name, "name": name, "properties": props, "points": []})
    except Exception:
        return entries
    return entries


def import_folder(input_dir: str) -> List[Dict]:
    entries: List[Dict] = []
    # If steelpy available and recognized, try that first
    sp_result = try_use_steelpy(input_dir)
    if sp_result is not None:
        return sp_result

    for fname in sorted(os.listdir(input_dir)):
        full = os.path.join(input_dir, fname)
        if not os.path.isfile(full):
            continue
        ext = os.path.splitext(fname)[1].lower()
        if ext == ".csv":
            parsed_list = parse_csv_file(full)
            for parsed in parsed_list:
                parsed.setdefault("id", parsed.get("name"))
                entries.append(parsed)
            continue

        if ext in (".txt", ".sct", ".dat", ".shp", ".sec") or True:
            parsed = parse_shape_file_text(full)
            # Add minimal id
            parsed.setdefault("id", parsed["name"])  # id default to filename
            entries.append(parsed)
    return entries


def normalize_entry(e: Dict) -> Dict:
    """Map parsed entry to a minimal stable schema.
    Schema:
      id: string
      name: string
      type: string (e.g. 'steel')
      properties: {A, Ix, Iy, J, ...}
      points: [[x,y], ...]
    """
    out = {
        "id": str(e.get("id") or e.get("name")),
        "name": e.get("name") or e.get("id"),
        "type": "steel",
        "properties": {},
        "points": e.get("points", []),
    }
    props = e.get("properties", {})
    for k, v in props.items():
        if isinstance(v, (int, float)):
            out["properties"][k] = float(v)
        else:
            try:
                out["properties"][k] = float(v)
            except Exception:
                out["properties"][k] = v

    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True, help="Folder with steelpy shape files")
    parser.add_argument("--output", required=True, help="Path to write JSON database")
    args = parser.parse_args()

    input_dir = args.input_dir
    out_file = args.output
    if not os.path.isdir(input_dir):
        raise SystemExit(f"input dir not found: {input_dir}")

    raw = import_folder(input_dir)
    normalized = [normalize_entry(r) for r in raw]

    # Write pretty JSON
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"profiles": normalized}, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(normalized)} profiles to {out_file}")


if __name__ == "__main__":
    main()
