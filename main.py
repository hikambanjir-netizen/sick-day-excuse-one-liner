#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.
SPDX-License-Identifier: MIT

Writes exactly one line to /output/entry.txt: a sick-day excuse that is
half believable, turns on a fresh idea, and lands its twist near the end.
Pure standard library; deterministic.
"""

import os

EXCUSE = (
    "My doctor put me on strict bed rest after I pulled a muscle "
    "reaching for the snooze button this morning."
)


def validate(line: str) -> None:
    """Gate: the judge only reads a valid entry — 1-200 chars, one line."""
    if not line.strip():
        raise SystemExit("entry must not be blank")
    if len(line) > 200:
        raise SystemExit(f"entry is {len(line)} chars, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
