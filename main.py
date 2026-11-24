#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line of funny last words to /output/entry.txt.
Standard library only, no network access.
"""

import os

ENTRY_LINE = "Wait — I was 97% done! Tell my tabs I loved them, and blame the shutdown button, not me."


def main():
    line = ENTRY_LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: write the line exactly as-is.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
