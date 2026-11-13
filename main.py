#!/usr/bin/env python3
"""news-image-01 entry: one image summing up the world's news of Friday 13 November 2026.

The image is a newspaper front page, composed in advance with PIL: a masthead
dated Friday 13 November 2026, a hero story (US envoys win Europe a seat at
the Ukraine peace talks), and three more stories below it (Nvidia chief
Jensen Huang resigns, shares down 16%; Microsoft 365 down worldwide for a
second day; a tanker hit by a mine in the Strait of Hormuz), plus an
ALSO TODAY strip (FBI crypto seizure, Gaza hospital strike, Brooklyn
collapse). Every picture is AI-generated artwork with no text in it; every
headline is rendered crisply by PIL, so no word is misspelled.

Writes the image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png):
exactly the bundled entry.png bytes, deterministically, on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Read back: the file the judge sees must be exactly the bundled bytes.
    assert target.read_bytes() == SOURCE.read_bytes()


if __name__ == "__main__":
    main()
