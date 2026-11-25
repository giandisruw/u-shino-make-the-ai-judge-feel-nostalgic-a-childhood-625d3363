#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory — make.fun entry.

Writes one nostalgic sentence (at most 280 characters) recalling a
childhood memory to /output/entry.txt (or to the path given as an argument).

Tournament winner (v2, line unchanged): candidate #14 won a 14-line Swiss
tournament judged by the Caffeine Inference router under the house brief —
2 game wins, highest cumulative score (2.35), final 0.55 vs runner-up #3.
A v2 revision was tried (drawer ending instead of "the summer that never
came back") and tied 0.50 head-to-head against this line, so it was NOT
adopted: the tournament line stands.

Standard library only. Deterministic: no network, no randomness, no input.
"""

import sys
from pathlib import Path

# Tournament winner, candidate #14 (150 chars): the last-day-of-school
# shirts, signed in marker — the judge praised the concrete ink-and-sweat
# detail and the small honest act over greeting-card phrasing.
LINE = (
    "On the last day of school we signed each other's shirts in marker, "
    "and mine still smells faintly of ink and sweat and the summer that "
    "never came back."
)

MAX_CHARS = 280


def validate(line: str) -> None:
    """Check the line against the bounty gate before anything is written."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line or "\t" in line:
        raise ValueError("line must be a single line (no line breaks or tabs)")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if not line.isprintable():
        raise ValueError("line must contain only printable characters")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")


def main(argv: list[str]) -> int:
    out_path = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    validate(LINE)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    out_path.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
