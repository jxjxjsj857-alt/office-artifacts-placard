#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes one museum placard (169 characters) for an ordinary office
stapler, treated as an ancient ritual artifact, to /output/entry.txt.
"""

import os

LINE = (
    "Stapler, pressed steel, c. 1997. Ritual press of the priests of "
    "Accounts, who bound two leaves into one covenant with a single "
    "bite. Gift of the Department of Paperwork."
)

# The gate allows 1 to 180 characters of UTF-8 text, not only whitespace.
# The line is a single placard: no trailing newline, so the gate reads
# exactly one line of 169 characters.
assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars, must be 1-180"
assert LINE.strip(), "line must not be only whitespace"


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    if "--dry-run" in __import__("sys").argv:
        print(LINE)
    else:
        main()
