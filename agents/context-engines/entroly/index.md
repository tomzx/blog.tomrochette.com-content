---
title: Entroly
created: 2026-10-12
updated: 2026-10-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, compression, receipts, open-source]
readability: 3
audience_notes: >
  Engineers choosing a compression layer for coding agents who care more about
  proving what was dropped than maximizing the headline savings. Assumes you
  know what a context window, a proxy, and an MCP server are.
---

Entroly is an Apache-2.0, local-first context layer that selects evidence within a token budget before an agent's request leaves the machine, records every omission in a receipt, and recovers the exact original bytes from a content-addressed store on demand.

**Entroly is the first member of this category whose product is the audit rather than the compression: the savings are modest and self-run, but every drop is receipted, byte-exact recoverable, and verifiable offline with one command, which is a guarantee none of the bigger compressors here offers.**

## What it is

A Python package (`pip install entroly`) carrying the full surface (CLI, SDK, localhost proxy, MCP server, dashboard), plus a Node/WASM CLI on npm, a Rust binary, a Homebrew tap, and a Docker image, all published at the same version and smoke-tested by the release workflow, by a solo maintainer (juyterman1000).
Selection is budgeted and query-conditioned: `compress`, `compress_messages`, and `optimize` return smaller payloads whose omitted spans get content hashes, and `entroly recover sha256:...` restores any of them exactly.
Delivery is wherever the request already flows: a proxy on localhost:9377 you point `ANTHROPIC_BASE_URL` or `OPENAI_BASE_URL` at, an MCP server, a reversible prompt hook for Claude Code, Codex, Cursor, Kiro, and VS Code, and SDK calls in your own prompt assembly.
A runaway-session rescue compacts bulky tool output in flight while keeping the prompt prefix byte-stable so the provider's warm cache survives.
Two offline commands are the trust surface: `entroly verify-claims` runs twelve local checks with no API key, and `entroly simulate` measures selection on your own repo before you connect a paid key.

## Status

Young, active, and barely discovered: 475 stars, 72 forks, created 2026-03-07, pushed 2026-10-12, PyPI and npm both at 1.0.86 across 104 releases, as of 2026-10-12 (GitHub, PyPI, and npm APIs).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=juyterman1000/entroly&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=juyterman1000/entroly&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=juyterman1000/entroly&type=date&legend=top-left" />
</picture>

Adoption is near zero for now: about 1,455 PyPI downloads and 1,044 npm downloads in the trailing month (PyPIstats and npm API, as of 2026-10-12), and a Hacker News search returns no story about the product (checked 2026-10-12, every hit unrelated entropy content).
Its one external listing is the [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) survey's Context Optimization Engines section, the same list that surfaced LLMLingua here.
The missing community footprint is itself the finding to weigh: at this size the project is one person's bet with no independent signal in either direction.

## Strengths

- **The receipt model answers LLMLingua's worst property and Headroom's open question at once**: nothing is silently dropped, recovery is byte-exact (the README ships 13-of-13 public SDK recovery probes and a 5,117-of-5,117 source-span fidelity check as repository artifacts), and `entroly verify-claims` proves the installed path works without an API key.
- The honesty markers are above the field's baseline: the README's own benchmark table shows the SQuAD 2.0 regression (80 to 72 percent) in bold, marks GSM8K as pass-through rather than a win, and prints Wilson confidence intervals with reproduction scripts.
- The proxy's session rescue keeps the prompt prefix byte-stable during in-flight compaction, which protects provider prompt-cache pricing, a detail most compression layers ignore because it never shows in a benchmark.
- Activation is checkable: `entroly activation status --json` reports whether a host hook actually ran, and MCP-only integrations are labeled advisory because the model can skip them.

## Cautions

- **Every performance number is self-run at hobby scale**: the README table runs 20 to 50 samples per row on gpt-4o-mini, a toy next to the multi-thousand-run tables Sourcegraph and Augment publish, and the vendor's own docs say savings exist only "when requests traverse an Entroly-controlled route".
- No independent evaluation, no practitioner threads, and four-digit monthly downloads mean the tool has never been fight-tested outside its author's benchmarks, as of 2026-10-12.
- The native engine is a separate install with runtime repair off by default; without it, query-conditioned selection is unavailable and the README labels reduction figures "unearned", so the out-of-box experience can be much weaker than the tables.
- Solo human maintainer (2,089 of 2,141 contributions), 104 releases in seven months, and a 20-topic keyword spread on the repository all say the bus factor and the focus are unproven.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
The costs are your own machine for the selection pass and the tokens you fail to save.

## Compared to

- [Headroom](../headroom/index.md): the closest sibling, also a local multi-channel compressor with a retrieve path; Headroom ships more surfaces and bigger claimed savings, Entroly ships receipts, byte-exact recovery, and the verification commands.
- [LLMLingua](../llmlingua/index.md): the peer-reviewed ancestor whose deletions are permanent; Entroly's selection is the reversible counter-design, with almost none of its evidence base.
- [rtk](../rtk/index.md): compresses the shell-output channel per command; Entroly sits at the request boundary across all channels and adds the audit layer.

## Bottom line

**Recommended for teams on metered provider bills who want compression they can audit, starting with `entroly simulate` on their own repo and treating every published percentage as a hypothesis at n=20.**
Not for anyone who needs an independently validated tool, a supported product, or the largest claimed savings, because none of those exist here yet.
My disagreeable claim: this category's arms race measures the wrong thing, and a smaller saving a buyer can prove beats a bigger saving nobody can check, which would make receipts, not ratios, the feature the next generation of compressors copies.

## Changes

- 2026-10-12 - Created from the 2026-10-12 Meirtz/Awesome-Context-Engineering entrant scan (the list's Entroly entry under Context Optimization Engines), with the zero-community-footprint finding and the small-n self-run-benchmark caveat recorded as the critical angle.

## See also

- [Headroom](../headroom/index.md) - the bigger, better-known compression sibling Entroly adds the audit layer to
- [LLMLingua](../llmlingua/index.md) - the destructive-pruning ancestor whose failure mode the receipts answer
- [rtk](../rtk/index.md) - the output-channel filter in the same token-bill fight
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins as the nineteenth column

## References

- https://api.github.com/repos/juyterman1000/entroly - stars, forks, created and pushed dates, Apache-2.0 license, and topics as of 2026-10-12
- https://raw.githubusercontent.com/juyterman1000/entroly/main/README.md - mechanism, install surfaces, receipt and recovery model, the README benchmark table with the disclosed SQuAD regression, and the activation-status honesty notes (fetched 200, 2026-10-12)
- https://raw.githubusercontent.com/juyterman1000/entroly/main/docs/BENCHMARKS.md - full benchmark protocols, sample sizes, the 24/24 versus 18/24 model-recovery holdout, and the WITNESS hallucination-detection numbers (fetched 200, 2026-10-12)
- https://pypi.org/pypi/entroly/json - version 1.0.86 (uploaded 2026-10-04) and the 104-release train
- https://registry.npmjs.org/entroly - the npm distribution at 1.0.86
- https://api.npmjs.org/downloads/point/last-month/entroly - 1,044 downloads in the month to 2026-10-10
- https://pypistats.org/api/packages/entroly/recent - 1,455 downloads in the trailing month as of 2026-10-12
- https://hn.algolia.com/api/v1/search?query=entroly&hitsPerPage=5 - the footprint check: no story about the product, all hits unrelated (fetched 2026-10-12)
- https://marketplace.visualstudio.com/items?itemName=entroly.entroly-vscode - the VS Code extension surface (fetched 200, 2026-10-12)
- https://github.com/Meirtz/Awesome-Context-Engineering - the entrant source: Entroly listed under Context Optimization Engines (repository and README fetched via the GitHub API, 2026-10-12)
