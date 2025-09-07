"""
Ingest a single CSV file into the existing steelpy SQLite DB, forcing comma delimiter.
Usage:
    python ingest_single_csv.py <csv_path> <db_path>
"""
import sys
import os
import csv
import json
import sqlite3


def ingest_csv_to_db(csv_path, source_filename, conn):
    cur = conn.cursor()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
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


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python ingest_single_csv.py <csv_path> <db_path>")
        sys.exit(1)
    csv_path = sys.argv[1]
    db_path = sys.argv[2]
    if not os.path.exists(csv_path):
        print(f"CSV not found: {csv_path}")
        sys.exit(2)
    if not os.path.exists(db_path):
        print(f"DB not found: {db_path}")
        sys.exit(3)
    conn = sqlite3.connect(db_path)
    ingest_csv_to_db(csv_path, os.path.basename(csv_path), conn)
    conn.close()
    print("Ingest complete")
