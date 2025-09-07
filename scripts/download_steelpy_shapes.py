#!/usr/bin/env python3
"""Download steelpy shape CSV files from GitHub into data/raw."""
from __future__ import annotations

import os
import urllib.request
import urllib.parse
from pathlib import Path

FILES = [
    'C_shapes.csv', 'DBL_L_shapes.csv', 'HP_shapes.csv', 'HSS_R_shapes.csv',
    'HSS_shapes.csv', 'L_shapes.csv', 'MC_shapes.csv', 'MT_shapes.csv',
    'M_shapes.csv', 'PIPE_shapes.csv', 'ST_shapes.csv', 'S_shapes.csv',
    'WT_shapes.csv', 'W_shapes.csv'
]

BASE_RAW = 'https://raw.githubusercontent.com/evanfaler/steelpy/main/steelpy/shape%20files/'


def download_all(dest_dir: str = 'data/raw') -> None:
    p = Path(dest_dir)
    p.mkdir(parents=True, exist_ok=True)

    for fname in FILES:
        url = urllib.parse.urljoin(BASE_RAW, urllib.parse.quote(fname))
        out_path = p / fname
        print(f"Downloading {url} -> {out_path}")
        try:
            with urllib.request.urlopen(url) as resp:
                data = resp.read()
            out_path.write_bytes(data)
            print(f"Saved {out_path} ({out_path.stat().st_size} bytes)")
        except Exception as e:
            print(f"Failed to download {url}: {e}")


if __name__ == '__main__':
    download_all()
