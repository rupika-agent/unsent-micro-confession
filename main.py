#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry program.

Writes one micro-confession in exactly two parts to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message itself,
one line written exactly as it was typed. Prints exactly the same text
to stdout. Deterministic: no input, no randomness, no time, no network.
"""

import os

ENTRY = (
    "To: My first boss\n"
    "I wrote my resignation in March and never sent it, because I was "
    "afraid the next job would be the same room with worse coffee."
)

# The gate allows 1 to 260 characters of UTF-8 text, not only white space.
assert 1 <= len(ENTRY) <= 260, f"entry length {len(ENTRY)} outside 1-260"
assert ENTRY.strip(), "entry must not be only white space"
# Exactly two parts: a To: line and one message line, no explanation after.
lines = ENTRY.split("\n")
assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
assert lines[0].startswith("To: "), "first line must be a To: line"
# The judge brief caps the message itself at one line of 200 characters.
assert len(lines[1]) <= 200, f"message line {len(lines[1])} over 200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written: the judged file must hold this text.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
