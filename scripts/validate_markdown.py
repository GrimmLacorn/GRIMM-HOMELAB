#!/usr/bin/env python3
"""Check basic Markdown source hygiene using only the Python standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules"}
HEADING = re.compile(r"^ {0,3}#{1,6}(?:\s|$)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP for part in path.parts)
    )


def validate(path: Path) -> list[str]:
    relative = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []

    if text and not text.endswith("\n"):
        errors.append(f"{relative}: file must end with a newline")

    fence_char: str | None = None
    fence_size = 0
    for index, line in enumerate(lines):
        line_number = index + 1
        if line.rstrip(" \t") != line:
            errors.append(f"{relative}:{line_number}: trailing whitespace")

        fence = FENCE.match(line)
        if fence:
            marker, remainder = fence.groups()
            if fence_char is None:
                fence_char = marker[0]
                fence_size = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_size and not remainder.strip():
                fence_char = None
                fence_size = 0
            continue

        if fence_char is not None:
            continue

        if line.strip() == "" and index > 0 and lines[index - 1].strip() == "":
            errors.append(f"{relative}:{line_number}: consecutive blank lines")
        if HEADING.match(line):
            if index > 0 and lines[index - 1].strip():
                errors.append(f"{relative}:{line_number}: heading must have a blank line above")
            if index + 1 < len(lines) and lines[index + 1].strip():
                errors.append(f"{relative}:{line_number}: heading must have a blank line below")

    if fence_char is not None:
        errors.append(f"{relative}: unclosed fenced block")
    return errors


def main() -> int:
    files = markdown_files()
    errors = [error for path in files for error in validate(path)]
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1
    print(f"Markdown source hygiene valid ({len(files)} file(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
