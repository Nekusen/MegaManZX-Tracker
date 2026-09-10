#!/usr/bin/env python3
"""Zip the tracker pack for a release: build/mmzx_tracker.zip with images/ at
the root (the layout Universal Tracker expects for an external pack), plus
README and LICENSE.

    python build_pack.py [--out build/mmzx_tracker.zip]
"""
import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", default=str(ROOT / "build" / "mmzx_tracker.zip"))
    args = p.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    files = sorted((ROOT / "images").glob("*.png")) + [ROOT / "README.md", ROOT / "LICENSE"]
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, f.relative_to(ROOT).as_posix())
    print("%s: %d files, %.1f KB" % (out, len(files), out.stat().st_size / 1024))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
