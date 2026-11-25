"""Worst Superpower entry: write one useless superpower to /output/entry.txt.

The power: teleportation that only returns you to the exact spot you were
standing five seconds ago — and only if you close your eyes and really commit
to it. A superpower so pointless that using it is the whole joke: you arrive
exactly where you just were, a little dizzy, having achieved nothing at all.
"""

import os
from pathlib import Path

LINE = "I can teleport instantly to the exact spot I was standing five seconds ago, provided I close my eyes and really commit to it."

MAX_CHARS = 140  # the competition gate's character cap for entry.txt
MIN_CHARS = 1  # the gate also requires at least one character

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def validate(line: str) -> str:
    """Enforce the competition gate before writing anything.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 140
    characters, not only whitespace, and the task requires a single line.
    Fail loudly instead of writing a bad entry.
    """
    if not line or not line.strip():
        raise ValueError("line must not be empty or whitespace-only")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} chars, gate allows at most {MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line, encoding="utf-8")
    os.chmod(OUTPUT_FILE, 0o644)
    written = OUTPUT_FILE.read_text(encoding="utf-8")
    assert written == line, "entry.txt does not match the line"
    assert MIN_CHARS <= len(written) <= MAX_CHARS, (
        "written entry is outside 1-140 chars"
    )


if __name__ == "__main__":
    main()
