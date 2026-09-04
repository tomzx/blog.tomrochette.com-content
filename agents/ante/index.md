---
title: Ante
created: 2026-08-30
updated: 2026-09-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, rust, single-binary, local-models]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding harness who care about resource footprint, offline
  operation, or running many agents on one machine.
  Assumes you know what a harness, Terminal-Bench, and BYOK mean.
---

Ante is a self-contained coding harness from Antigma Labs that ships as one ~15MB Rust binary with an embedded llama.cpp engine, so it can drive cloud models or run GGUF models fully offline.
Facts below verified as of 2026-09-04.

**Ante is the first harness whose pitch is that footprint and offline capability are the product: the TUI, an embedded ripgrep, PDF/OCR, and a natively managed local inference engine all live inside one binary with zero runtime dependencies.**

## What it is

A terminal agent in the Claude Code/Codex form factor, written in Rust and built by Antigma Labs, a startup that also publishes its own Terminal-Bench 2.1 evaluation results.
The architecture is client-daemon: a TUI client, a headless CLI, an `ante serve` JSONL server for editor plugins, and an ACP crate (ante-acp) all drive the same daemon.
It reads AGENTS.md conventions, supports skills, sub-agents, MCP, and persistent memory, and takes any of 12+ providers by API key or subscription with no account or telemetry gate.
Source is published under Apache-2.0 (crates: exec, llm, protocol-shape, ante-sdk), while the prebuilt release binaries ship under separate Binary Preview Terms.

## Status

**Active, preview-stage, and growing fast for a five-month-old repo.**
1,927 stars and 62 forks as of 2026-09-04, repo created December 23, 2025, with the latest release v0.preview.94 published September 4, 2026 (GitHub API).
The Show HN launch on August 10, 2026 drew 169 points and 92 comments ([HN](https://news.ycombinator.com/item?id=49245437)).
At launch commenters flagged that the repo hosted binaries without agent source; the Rust source is now published, which resolves the objection.
The company publishes Terminal-Bench 2.1 runs at antigma.ai/eval, pinning every result to a public release and a raw Harbor run; its best self-reported score is 82.7% with DeepSeek V4 Flash, updated August 9, 2026.

## Strengths

- **The footprint numbers are measured, not vibes**: the docs claim ~7x less peak memory, ~9x less average CPU, and ~5x less disk I/O than Claude Code across 20 parallel tasks, consistent with its run-thousands-of-agents thesis.
- Native offline mode: the embedded llama.cpp engine runs GGUF models locally with no API key and no account, which no mainstream harness does in-binary.
- Public, auditable evals: every Terminal-Bench result names the exact downloadable build and links the raw Harbor run.
- BYOK breadth with subscription support across Anthropic, OpenAI, Gemini, Grok, OpenRouter, and more, plus a no-telemetry stance.

## Cautions

- **The binary and the source have different licenses**: prebuilt releases are governed by Binary Preview Terms (alpha research preview, distribution can be discontinued), so the Apache-2.0 repo does not mean the artifact you download is freely relicensed.
- v0.preview stage: features may change or be removed at any time, per the project's own terms.
- The benchmark claims come from the vendor itself; the runs are auditable but independent replication is thin so far.
- Launch-day trust was damaged by the binary-only debut; the correction is recent and worth remembering.

## Pricing

Free to use in preview, both as source (Apache-2.0) and as prebuilt binaries under the Binary Preview Terms.
You pay only your own model costs, whether API keys, subscriptions, or free local GGUF models.
No paid tiers exist as of 2026-09-02.

## Compared to

- [Claude Code](../claude-code/index.md): the reference harness Ante benchmarks itself against; pick Claude Code for the mature ecosystem, Ante when memory, offline operation, or per-agent cost is the constraint.
- [Codex](../codex/index.md): OpenAI's harness assumes its own models and cloud; Ante is provider-agnostic and local-first.
- [fx](../fx/index.md): the other tiny single-binary harness, but fx is built to be embedded inside other programs while Ante is built to be your terminal agent that happens to be light.

## Bottom line

**Recommended for terminal developers running local models, resource-constrained machines, or many parallel agents on one box; not for teams that need a stable 1.0 contract or an independently audited benchmark record today.**
I expect the harness market to consolidate on footprint and cost per agent, and I think Ante is currently the clearest bet that the winner is the lightest credible thing, not the most featureful one.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where Ante lands in the harness layer's independent tail
- [fx](../fx/index.md) - the other minimal single-binary harness, with the opposite embedding thesis
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - Ante not yet a column; the incumbents it is measured against are
- [Claude Code](../claude-code/index.md) - the incumbent whose resource profile Ante claims to beat

## References

- https://github.com/AntigmaLabs/ante - repository, Apache-2.0 source, 1,927 stars as of 2026-09-04
- https://docs.antigma.ai/ - architecture, offline mode, providers, footprint claims
- https://antigma.ai/eval - self-reported Terminal-Bench 2.1 results, pinned builds and Harbor runs
- https://raw.githubusercontent.com/AntigmaLabs/ante/main/README.md - feature surface and provider list
- https://raw.githubusercontent.com/AntigmaLabs/ante/main/BINARY-TERMS.md - the separate preview license for prebuilt binaries
- https://news.ycombinator.com/item?id=49245437 - the August 10, 2026 launch thread, 169 points (verified via Algolia API)
- https://github.com/AntigmaLabs/ante/releases - v0.preview.94, published 2026-09-04 (verified via GitHub API)
