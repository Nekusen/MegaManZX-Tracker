#!/usr/bin/env python3
"""Zip the tracker pack for a release, in the layout Universal Tracker expects
from an external pack (images/ at the zip root), plus README and LICENSE:

    build/mmzx_tracker.zip   images/   the game's own level art, one map per area and per room

    python build_pack.py [--out-dir build]
"""
import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKS = {
    "mmzx_tracker.zip": ROOT / "images",
}


def build(name: str, images: Path, out_dir: Path) -> None:
    out = out_dir / name
    files = sorted(images.glob("*.png"))
    if not files:
        print("%s: no images in %s, skipped" % (name, images))
        return
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, "images/" + f.name)
        for doc in ("README.md", "LICENSE"):
            z.write(ROOT / doc, doc)
    print("%s: %d images, %.1f KB" % (out, len(files), out.stat().st_size / 1024))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out-dir", default=str(ROOT / "build"))
    args = p.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, images in PACKS.items():
        build(name, images, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
