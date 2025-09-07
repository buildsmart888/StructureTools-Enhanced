"""
Download steelpy shape CSV files and store them and a small SQLite DB locally.

Usage:
    python download_and_import_steelpy.py --out-dir "..." --db "..."

This script downloads the known shape CSVs from the steelpy repo and saves them to out-dir/raw,
then creates a SQLite DB with one table `profiles` containing raw CSV rows with a `source_file` column.

The DB is intentionally simple: each profile row stores the original CSV text line and parsed columns
as a JSON blob for later import into EnhancedSteelDatabase.
"""
import os
import sys
import argparse
import csv
import json
import sqlite3
from urllib.request import urlopen

STEELPY_BASE = "https://raw.githubusercontent.com/evanfaler/steelpy/main/steelpy/shape%20files"
CSV_FILES = [
    "C_shapes.csv",
    "DBL_L_shapes.csv",
    "HP_shapes.csv",
    "HSS_R_shapes.csv",
    "HSS_shapes.csv",
    "L_shapes.csv",
    "MC_shapes.csv",
    "MT_shapes.csv",
    "M_shapes.csv",
    "PIPE_shapes.csv",
    "ST_shapes.csv",
    "S_shapes.csv",
    "WT_shapes.csv",
    "W_shapes.csv",
]


def download_file(filename, out_dir):
    url = STEELPY_BASE + "/" + filename
    out_path = os.path.join(out_dir, filename)
    print(f"Downloading {url} -> {out_path}")
    with urlopen(url) as r, open(out_path, "wb") as f:
        f.write(r.read())
    return out_path


def create_db(db_path):
    print(f"Creating sqlite DB at {db_path}")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_file TEXT NOT NULL,
        raw_line TEXT NOT NULL,
        parsed_json TEXT
    )
    """)
    conn.commit()
    return conn


def ingest_csv_to_db(csv_path, source_filename, conn):
    cur = conn.cursor()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        # try to sniff delimiter
        sample = csvfile.read(2048)
        csvfile.seek(0)
        dialect = csv.Sniffer().sniff(sample)
        reader = csv.reader(csvfile, dialect)
        headers = next(reader)
        for row in reader:
            raw = ",".join(row)
            try:
                parsed = dict(zip(headers, row))
            except Exception:
                parsed = {"_row": row}
            cur.execute("INSERT INTO profiles (source_file, raw_line, parsed_json) VALUES (?, ?, ?)",
                        (source_filename, raw, json.dumps(parsed)))
    conn.commit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=os.path.join(os.getcwd(), "data"))
    parser.add_argument("--db", default=os.path.join(os.getcwd(), "data", "steelpy_shapes.db"))
    args = parser.parse_args()

    raw_dir = os.path.join(args.out_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)

    # download
    for name in CSV_FILES:
        try:
            download_file(name, raw_dir)
        except Exception as e:
            print(f"Failed to download {name}: {e}")

    # create db
    conn = create_db(args.db)

    # ingest
    for name in CSV_FILES:
        path = os.path.join(raw_dir, name)
        if os.path.exists(path):
            try:
                ingest_csv_to_db(path, name, conn)
                print(f"Ingested {name}")
            except Exception as e:
                print(f"Failed to ingest {name}: {e}")
        else:
            print(f"Skipped missing {name}")

    conn.close()
    print("Done")


if __name__ == '__main__':
    main()
