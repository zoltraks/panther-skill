# Encoding

## Purpose

> **Scope:** Character encoding and byte-level rules for documents created and edited with this
> skill
> **Key items:** UTF-8 default, BOM, UTF-16/UCS-2, code pages such as CP1250, line endings,
> composed diacritics

This file defines how the skill handles document encodings.

Load it when a document's encoding is not UTF-8, when the request mentions encodings or code
pages, or when `tools/detect-encoding.py` reports an unexpected result.

## Default

Create every new file in UTF-8 without a byte order mark.

Use LF line endings for new files, or the dominant line-ending style of the target directory when
it clearly uses CRLF.

## Preservation On Edit

Preserve the encoding, byte order mark, and line-ending style of every existing file.

A file in UTF-16, UCS-2, or a code page such as CP1250 stays in that encoding after the edit.

Never transcode a file as a side effect of an unrelated change.

Never convert LF to CRLF or back as a side effect of an unrelated change.

Mixing encodings inside one file is never allowed - an edited file keeps exactly one encoding.

## Detection

Detect the encoding before editing an existing file.

Copy `tools/detect-encoding.py` into the working repository as `detect-encoding.tmp.py` and run it
on the target file, see `tools/README.md`.

Detection order:

1. **Byte order mark** - `EF BB BF` means UTF-8, `FF FE` means UTF-16 LE, `FE FF` means UTF-16 BE.
2. **Null-byte pattern** - interleaved zero bytes indicate UTF-16/UCS-2 even without a BOM.
3. **UTF-8 validation** - bytes that decode as valid UTF-8 with multibyte sequences are UTF-8.
4. **ASCII** - bytes below `0x80` only.
5. **Code page fallback** - bytes in `0x80-0xFF` that are not valid UTF-8 usually mean a legacy
   code page. For Polish content, try CP1250 first.

When detection is ambiguous, report the ambiguity and ask the user rather than guessing.

## Conversion

Transcode a file only when the request explicitly asks for a target encoding.

State the source encoding, the target encoding, and the BOM decision before converting.

Verify the converted file decodes correctly before reporting completion.

A conversion never silently fixes or strips characters, a character that does not exist in the
target encoding is an error, not a substitution.

## Diacritics

Write diacritical letters in composed form, one Unicode code point per letter (NFC).

Do not use combining characters where a composed letter exists.

This matters for table width measurement - the language files' table rules count source
characters, and a decomposed letter counts as two.

## Legacy Encodings

Code pages such as CP1250 (Central European), CP1252 (Western), or ISO-8859-2 may appear in older
documents.

When editing such a file, write the new bytes in the same encoding.

Tools that only read UTF-8 will corrupt these files - always go through the detected encoding,
never through a default.
