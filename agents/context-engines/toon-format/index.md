---
title: TOON
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, serialization, token-optimization, specification]
readability: 3
audience_notes: >
  Engineers stuffing structured data into LLM prompts and paying per token of JSON punctuation.
  Assumes you know JSON and YAML well enough to compare encodings.
---

TOON (Token-Oriented Object Notation) is an MIT-licensed, spec-backed encoding of the JSON data model that replaces braces and repeated keys with indentation and CSV-style table rows, cutting the token cost of structured data handed to LLMs while staying lossless and human-readable.

**TOON is the packing convention for the structured slice of the context window: it changes nothing about which data enters the window, only how many tokens the same data costs, and its 1.9 million weekly npm downloads make it the most-adopted encoding standard this category holds.**

## What it is

A format specification (version 4.3, Working Draft, 2026-10-06) maintained in its own repository by Johann Schopplich, with the TypeScript reference implementation at `@toon-format/toon` and community ports across languages (25,461 stars, pushed 2026-10-06, as of 2026-10-07).
The design combines YAML's indentation for nested objects with CSV-style tabular rows for arrays of uniform objects: each array declares its length and field list once, then one row per item, with a single active delimiter (comma, tab, or pipe) and strings quoted only when required.
The sweet spot is uniform data, the same fields across many items, where it approaches CSV compactness while keeping structure explicit; the spec itself concedes that deeply nested or non-uniform data can be cheaper as plain JSON.
The intended use is a translation layer: keep JSON in code, encode to TOON at the prompt boundary, decode back from the model's output.

## Status

Active and widely adopted: created 2025-10-22, 25,461 stars, spec at v4.3, about 1,897,900 npm downloads in the week of 2026-09-28 to 2026-10-04, as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=toon-format/toon&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=toon-format/toon&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=toon-format/toon&type=date&legend=top-left" />
</picture>

The launch discussion reached 178 points and 58 comments on Hacker News in October 2025, where the standing objections were set: YAML already exists, and models fine-tuned on JSON might lose accuracy on a format absent from their training data.
A third-party test comparing TOON against JSON and CSV on tabular data came out of that thread, and the spec continues to revise (4.1 to 4.3 across 2026), so the format is stable-but-moving by its own description.

## Strengths

- The token savings on uniform arrays are mechanical and measurable, and the format stays lossless, so it drops into an existing JSON pipeline as a prompt-boundary codec.
- Explicit array lengths and per-row field elision make structure easy for models to validate, which is the argument against just using CSV.
- A specification with conformance requirements and multiple independent implementations, not a single library's output format.
- Adoption at the 1.9-million-downloads-a-week level means tooling and precedent exist when something goes wrong.

## Cautions

- Accuracy effects are unresolved: TOON is not in most models' training distributions, and the strongest community objection since launch is that JSON-heavy fine-tuning may make models measurably worse at reading it on long contexts.
- The win inverts on nested or non-uniform data, so blind encoding can cost tokens rather than save them.
- A young spec (first release late 2025, three revisions in 2026) that carries churn risk for anything storing TOON long-term.
- Round-tripping adds a decode step and a failure mode at exactly the boundary where you are trying to save money.

## Pricing

Free and open standard under MIT; there is no paid tier, so pricing does not apply.

## Compared to

- [rtk](../rtk/index.md): the compressor for unstructured tool output; TOON is the compressor for structured data you serialize yourself, and the two do not overlap.
- [Repomix](../repomix/index.md): packs a whole repository into one file; TOON packs one JSON document into fewer tokens, and both are offline and deterministic.
- [MCP](../../protocols/mcp/index.md): the transport that moves the data; TOON is independent of how the data arrives and can encode an MCP tool's payload at the prompt boundary.

## Bottom line

**Recommended for any pipeline that embeds large uniform JSON (tables, lists, logs of records) into prompts, measuring tokens before and after on your own model and data, since the format's own docs treat the benchmark case as narrow.**
Not for deeply nested or heterogeneous payloads, and not yet for contexts where an unproven accuracy effect on your model is unacceptable.

## Changes

- 2026-10-07 - Created.

## See also

- [rtk](../rtk/index.md) - the unstructured-output counterpart in the same token-bill fight
- [Repomix](../repomix/index.md) - the other deterministic packer in this category
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [llms.txt](../../protocols/llms-txt/index.md) - the other convention that optimizes what models read, from the sites side

## References

- https://github.com/toon-format/toon - repository, MIT license, README design rationale, and the benchmark framing (fetched 200, 2026-10-07)
- https://api.github.com/repos/toon-format/toon - stars, created date, and push date for the as-of status (fetched 200, 2026-10-07)
- https://raw.githubusercontent.com/toon-format/spec/HEAD/SPEC.md - the v4.3 specification: syntax, canonical number formatting, delimiter scoping, strict-mode validation, and conformance requirements (fetched 200, 2026-10-07)
- https://api.npmjs.org/downloads/point/last-week/@toon-format/toon - weekly download volume for the adoption claim (fetched 200, 2026-10-07)
- https://hn.algolia.com/api/v1/items/45715632 - the 178-point launch thread with the YAML and training-data-accuracy objections (fetched 200, 2026-10-07)
