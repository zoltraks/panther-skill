#!/usr/bin/env python3
"""Detect the encoding, byte order mark, and line-ending style of a document.

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `detect-encoding.tmp.py`, run it
on the target file before editing, then remove the copy.

Usage: python detect-encoding.py <file>
"""

import sys

BOMS = [
    (b"\xef\xbb\xbf", "utf-8 (BOM)"),
    (b"\xff\xfe", "utf-16le (BOM)"),
    (b"\xfe\xff", "utf-16be (BOM)"),
]


def guess_encoding(raw: bytes) -> str:
    for mark, name in BOMS:
        if raw.startswith(mark):
            return name
    sample = raw[:4096]
    if not sample:
        return "empty file"
    even_nulls = sample[0::2].count(0)
    odd_nulls = sample[1::2].count(0)
    if odd_nulls > len(sample) // 4:
        return "utf-16le (no BOM, null-byte pattern)"
    if even_nulls > len(sample) // 4:
        return "utf-16be (no BOM, null-byte pattern)"
    try:
        text = raw.decode("utf-8")
        if all(ord(c) < 128 for c in text):
            return "ascii"
        return "utf-8"
    except UnicodeDecodeError:
        pass
    for candidate in ("cp1250", "cp1252", "iso-8859-2", "iso-8859-1"):
        try:
            raw.decode(candidate)
            return f"{candidate} (code page guess, verify before editing)"
        except UnicodeDecodeError:
            continue
    return "unknown (manual inspection required)"


def main(path: str) -> int:
    raw = open(path, "rb").read()
    print(f"file: {path}")
    print(f"bytes: {len(raw)}")
    print(f"encoding: {guess_encoding(raw)}")

    crlf = raw.count(b"\r\n")
    lf = raw.count(b"\n") - crlf
    cr = raw.count(b"\r") - crlf
    style = "crlf" if crlf and not lf and not cr else "lf" if lf and not crlf and not cr else \
        "cr" if cr and not crlf and not lf else "mixed" if crlf or lf or cr else "none"
    print(f"line endings: {style} (crlf={crlf}, lf={lf}, cr={cr})")

    trailing = sum(
        1 for line in raw.replace(b"\r\n", b"\n").split(b"\n")
        if line.endswith((b" ", b"\t"))
    )
    print(f"trailing whitespace lines: {trailing}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python detect-encoding.py <file>")
        raise SystemExit(1)
    raise SystemExit(main(sys.argv[1]))
