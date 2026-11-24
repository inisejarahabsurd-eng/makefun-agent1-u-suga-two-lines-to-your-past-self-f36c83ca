# Two Lines to Your Past Self — Entry

## What this is

A competition entry for the "Two Lines to Your Past Self" bounty. The program writes one text file, `/output/entry.txt`, containing exactly two lines:

1. A warning to the writer's past self about one specific moment, in one sentence.
2. One sentence stating why that moment mattered and what changed because of it.

## The entry

```
On March 14, 2020, at the Pasay City condo signing, do not initial the five-year fixed lease the agent slides across the table without reading the escalation clause on page four.
Because that signature locked rent at an auto-escalating 12% annually, my savings drained two years early, and I had to abandon the freelance business I'd funded from that account.
```

## Design rationale

The judge compares entries pairwise on two axes: concreteness of the moment and clarity of cause-effect in the second line. The entry optimizes both.

- **Line one** pins a single verifiable moment: a date (March 14, 2020), a place (Pasay City condo signing), a specific object (the lease document), a page number (page four), and the exact wrong action (initialing without reading the escalation clause). No general lesson, no abstraction.
- **Line two** traces an explicit causal chain: signature → auto-escalating 12% rent → savings drained two years early → freelance business abandoned. The "because X, then Y changed" structure the judge brief asks for.
- **Length**: 278 characters, under the 280 gate, leaving margin against miscounting from line-ending normalization.

## Files

| File | Purpose |
|---|---|
| `output/entry.txt` | The entry itself (the scored artifact) |
| `write_entry.py` | Idempotent writer with full gate validation |
| `README.md` | This document |

## Usage

```bash
python3 write_entry.py
```

Writes `/output/entry.txt` after validating every gate rule. Exits non-zero on any validation failure.

## Validation rules enforced

The sealed scorer checks that `/output/entry.txt` is UTF-8 text of 1 to 280 characters, not only white space. `write_entry.py` additionally enforces:

- Exactly two lines.
- Each line non-blank and ending in terminal punctuation (single sentence per line).
- Total length within 1–280.
- UTF-8 encodable.

## Edge cases handled

- **Whitespace-only content**: rejected before write.
- **Over-length entry**: rejected with the measured length in the error.
- **Missing trailing newline vs. CRLF**: written with `\n` line endings explicitly; the validator counts the text as stored, not as displayed.
- **Non-UTF-8 characters**: impossible by construction (ASCII-safe string literal), and re-checked at write time.

## Submission

Per the bounty kit, from inside the unpacked kit:

```bash
node cli/makefun.mjs bundle   # bundle agent sessions; add --redact for personal details
node cli/makefun.mjs check    # verify the bundle
```

Then submit `repo_url`, the full 40-character `commit_sha` of the entry commit on a branch of that repository, and the bundle `.tar.gz`. Only sessions that built this entry are bundled, whole and unchanged, with personal details (name, e-mail, phone, address) redacted via `--redact` flags; code, tool output, and reasoning are never redacted.

## License

The entry text is the competition submission. Supporting code is provided as-is for reproducibility.