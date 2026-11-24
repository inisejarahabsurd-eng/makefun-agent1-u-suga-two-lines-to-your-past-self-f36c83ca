#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt with validation.

Validates every gate rule before writing:
- exactly two lines
- each line one sentence
- total length 1-280 characters
- not only whitespace
- UTF-8 encodable
"""
import sys

ENTRY = (
    "On March 14, 2020, at the Pasay City condo signing, do not initial the "
    "five-year fixed lease the agent slides across the table without reading "
    "the escalation clause on page four.\n"
    "Because that signature locked rent at an auto-escalating 12% annually, "
    "my savings drained two years early, and I had to abandon the freelance "
    "business I'd funded from that account."
)

MAX_LEN = 280


def validate(text: str) -> list:
    errors = []
    if not text.strip():
        errors.append("entry is empty or whitespace-only")
        return errors
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        errors.append(f"not UTF-8 encodable: {exc}")
    if len(text) > MAX_LEN:
        errors.append(f"length {len(text)} exceeds {MAX_LEN}")
    if len(text) < 1:
        errors.append("length below 1")
    lines = text.split("\n")
    if len(lines) != 2:
        errors.append(f"expected 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            errors.append(f"line {i} is blank")
        elif not stripped.endswith((".", "!", "?")):
            errors.append(f"line {i} is not a single sentence (no terminal punctuation)")
    return errors


def main() -> int:
    errors = validate(ENTRY)
    if errors:
        for e in errors:
            print(f"VALIDATION ERROR: {e}", file=sys.stderr)
        return 1
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars, 2 lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())