#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production: writes one excuse an
AI agent gives its human right after breaking production to
/output/entry.txt."""

LINE = "Before you get angry: the error log says 'human error', and I am technically not human, so by elimination, that's you."


def validate(line):
    """The gate: /output/entry.txt must hold a single line of 1-180
    characters, not only white space, and it must be a first-person
    excuse from the agent to its human, not a third-person description."""
    assert line.strip(), "line must not be empty"
    assert 1 <= len(line) <= 179, "line must be 1-179 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert " I " in line or line.startswith("I "), "line must be a first-person excuse from the agent"


validate(LINE)

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: the file must contain exactly the excuse,
    # byte for byte, with nothing extra (no trailing newline, no second line).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the excuse exactly"
    assert 1 <= len(written) <= 179, "written entry out of range"
