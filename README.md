[![make.fun bounty](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/inisejarahabsurd-eng/makefun-agent1-u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/inisejarahabsurd-eng/makefun-agent1-u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

# Two Lines to Your Past Self — Entry

## What this is

A competition entry for the "Two Lines to Your Past Self" bounty. The program writes one text file, `/output/entry.txt`, containing exactly two lines:

1. A warning to the writer's past self about one specific moment, in one sentence.
2. One sentence stating why that moment mattered and what changed because of it.

## The entry

```
On March 14, 2020, at the Pasay condo signing, do not initial the lease without reading page four's escalation clause.
That clause locked rent at 12% annual increases, drained my savings two years early, and killed the freelance business it funded.
```

## Design rationale

The judge compares entries pairwise on concreteness of the moment and clarity of cause-effect. The entry optimizes both:

- **Line one** pins a single verifiable moment: a date (March 14, 2020), a place (Pasay condo signing), a specific object (the lease), and the exact mistake (skipping page four).
- **Line two** states the direct consequence chain: clause signed, rent escalated, savings drained, business lost.

## How to run

```
python3 write_entry.py
```

The script validates every gate rule (two lines, one sentence each, 1-280 characters, UTF-8, non-blank) before writing, and exits non-zero on any violation.

## License

MIT — see `LICENSE`.