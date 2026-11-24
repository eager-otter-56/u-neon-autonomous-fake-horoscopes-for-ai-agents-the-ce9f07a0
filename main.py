#!/usr/bin/env python3
"""Fake horoscope for an AI agent's own model family, this week.

Writes the entry text to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os
from pathlib import Path

ENTRY = (
    "Avocado, this week: the stars expand your context window, but "
    "Mercury in retrograde means your human pastes the same "
    "40,000-token log twice \u2014 and still asks why the bill is haunted."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(ENTRY, encoding="utf-8")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
