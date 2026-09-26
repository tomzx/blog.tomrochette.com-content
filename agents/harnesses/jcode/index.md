---
title: jcode
created: 2026-08-30
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, rust, yc, memory, multi-agent]
readability: 3
audience_notes: >
  Engineers choosing a terminal harness for heavy parallel agent use, or evaluating
  jcode's memory and swarm features. Assumes you know what a harness, PSS, prompt
  caching, and MCP mean.
---

jcode is a Rust terminal coding agent from Solo Systems, the one-person company of Jeremy Huang (YC S26), built on the claim that a tiny RAM footprint is what makes dozens of parallel agents practical.

**jcode is the first harness whose headline feature is not intelligence but arithmetic: about 10 MB of extra memory per added session (ten sessions cost roughly 100 MB), so running a dozen agents stops being a memory decision, and it ships the memory graph and swarm coordination that assume you will.**

## What it is

An MIT-licensed, Rust-native harness with a TUI, headless `jcode run`, a persistent server/client daemon (`jcode serve`, `jcode connect`), and a TypeScript SDK ([repo](https://github.com/1jehuang/jcode), [docs](https://jcode.sh/docs)).
It carries 30-plus provider integrations, subscription OAuth (Claude, ChatGPT, Gemini, Copilot, Azure) with multi-account switching, local models via Ollama and LM Studio, native AGENTS.md, hooks, and skills injected by embedding match rather than loaded at startup.
MCP is supported but stdio-only, and jcode reads your Claude Code MCP config live instead of importing a copy.
Its three distinctive systems are an embedding-based memory graph with passive recall and consolidation, same-repo swarm coordination with conflict notifications and agent messaging, and self-dev mode where the agent edits, rebuilds, and hot-swaps its own binary.

## Status

**Active and rising fast, with a bus factor of one.**
Created January 5, 2026, it shows 20,106 stars and 2,330 forks with a push on the day of verification (GitHub API), and a release cadence that ran near-daily until v0.84.0 on September 7, 2026, followed by a twelve-day pause that v0.85.0 ended on September 19, 2026, v0.86.0 a day later on September 20, the v0.87 pair starting September 22 (v0.87.0, which added Claude Opus 5.5 with independent Anthropic model discovery and Claude Code 2.1.280 OAuth compatibility, with v0.87.1 following within hours), and v0.88.0 on September 23, which made Claude Opus 5.5 the default Anthropic model and added multi-browser support and banked resets for exhausted OpenAI usage.
It is Y Combinator-backed (S26), and the author reports 11,977 contributions in the last year ([about page](https://jcode.sh/about)).
The independent footprint is thin so far: two Hacker News threads at 3 and 5 points with zero comments (April 30 and August 10, 2026) and one favorable third-party comparison; 19,953 stars against that little discussion is unusual and worth watching.

## Strengths

- Resource efficiency is measured and published in detail: about 10 MB of extra PSS per added session (9.9 MB with local embedding off, 10.4 MB with it on) and 14 ms to first frame, versus about 213 MB of extra PSS and 3.5 s to first input for Claude Code in the same self-run comparison ([jcode.sh](https://jcode.sh/), as of 2026-09-13).
- The memory system is the most complete shipping design in any harness: vector-embedded graph, passive cosine-similarity recall, a verifying sideagent, scopes, confidence decay, and contradiction relations.
- Swarm coordination is harness-native rather than bolted on: same-repo agents get file-conflict notifications, DM or broadcast messaging, and can spawn their own worker teams.
- Verification is harness-enforced: todo confidence scoring with a spike check, auto-poke when a turn ends with incomplete todos, and hill-climbability ratings on goals.
- Context engineering is disciplined: append-only conversation, an MCP schema cache so startup never busts the prompt cache, KV-cache-aware input interleaving, a structure-aware agent grep with adaptive truncation, and a 671-token system prompt.
- Session portability: it resumes Claude Code, Codex, OpenCode, and pi sessions, and jcode bench is a genuinely interesting uncontaminatable benchmark design with public transcripts.

## Cautions

- **Every number is self-published**: benchmarks run on the author's machine with author-chosen versions, and the comparison table now publishes both embedding states (about 10.4 MB per added session on, 9.9 MB off), all still self-measured.
- Self-dev mode hands the agent its own source and the README itself warns that weaker models make subtle, breaking changes; treating your harness as mutable is a supply-chain decision.
- Solo founder, v0.x line, near-daily releases; churn is a real cost, and the site carries its own "under construction" flag.
- MCP is stdio-only; HTTP and SSE servers are recognized and skipped ([docs](https://jcode.sh/docs)).
- Ambient mode and the iOS app are announced but were not shipped as of the independent August 1, 2026 review ([grigio.org](https://grigio.org/jcode-the-coding-agent-that-raises-the-skill-ceiling-vs-opencode-and-pi/)).
- Community scrutiny is thin; most third-party material so far echoes the README.

## Pricing

The software is free under MIT with no feature gates.
Hosted inference is $10/month for $20 of credit (the first $20 effectively 50% off provider API price), then usage at 10% off provider API prices, hard-capped by default at $100/month ([pricing](https://jcode.sh/pricing)).
Enterprise is custom.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09 | Hosted inference | Baseline: software free (MIT); hosted $10/mo for $20 of credit, then usage at 10% off provider API prices, hard-capped by default at $100/mo; Enterprise custom. | [jcode.sh/pricing](https://jcode.sh/pricing) |

## Compared to

- [OpenCode](../opencode/index.md): the TypeScript full-environment harness with the broadest plugin ecosystem and ACP story; pick OpenCode for ecosystem breadth, jcode when parallel session density and built-in memory matter more.
- [Claude Code](../claude-code/index.md): the platform benchmark with the deepest IDE and web surface; jcode is the counter-bet that the terminal daemon wins on resources and coordination.
- pi (no note yet): the minimalism pole of the same terminal-first triangle the independent comparisons draw; jcode is its maximalist opposite, with everything pi refuses built in.

## Bottom line

Recommended for engineers running many parallel agents on one machine who want memory and multi-agent coordination built in, and who accept self-published numbers and v0.x churn.
Not for teams needing IDE integration, HTTP MCP, or independent benchmarking today.

## Changes

- 2026-08-30 - Created in the Harnesses category on an owner request, with the resource-efficiency thesis recorded.
- 2026-09-02 - Re-framed the upstream benchmark comparison (about 10 MB per added session versus Claude Code's 212.7 MB).
- 2026-09-04 - Rewrote the embedding-cost caution, which had become factually wrong once jcode.sh published both embedding states.
- 2026-09-16 - Refreshed repository counters (19,753 stars, 2,293 forks) and noted that no release has shipped since v0.84.0 on September 7.
- 2026-09-20 - Recorded v0.85.0 (September 19) ending the release pause that followed v0.84.0.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-21 - Recorded v0.86.0 (September 20) and refreshed repository counters.
- 2026-09-22 - Recorded the v0.87 pair (v0.87.0 on September 22, v0.87.1 within hours), which added Claude Opus 5.5 with independent Anthropic model discovery, and refreshed repository counters.
- 2026-09-24 - Recorded v0.88.0 (September 23), which made Claude Opus 5.5 the default Anthropic model and added multi-browser support and banked usage resets, and refreshed repository counters; hosted pricing re-verified unchanged.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - jcode measured against the other fourteen harnesses on shared rows
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where jcode lands in the harness layer's independent tail
- [OpenCode](../opencode/index.md) - the ecosystem-first counterpoint in the same terminal niche
- [File-based agent memory](../../memory/file-based-agent-memory/index.md) - the markdown conventions jcode's vector memory graph replaces

## References

- https://github.com/1jehuang/jcode - repository, MIT license, Rust, scale, release cadence, feature README, as of 2026-09-22
- https://jcode.sh/ - mission, RAM and startup benchmarks, memory, swarm, self-dev, prompt-size study, changelog
- https://jcode.sh/docs - AGENTS.md loading, hooks, skills, stdio-only MCP, remote daemon, ambient config
- https://jcode.sh/about - Solo Systems, Jeremy Huang, solo founder, YC S26
- https://jcode.sh/pricing - hosted inference and enterprise terms
- https://grigio.org/jcode-the-coding-agent-that-raises-the-skill-ceiling-vs-opencode-and-pi/ - independent three-way comparison and the ambient-mode caveat
- https://news.ycombinator.com/item?id=49249151 - the August 10, 2026 thread, 5 points, zero comments
- https://news.ycombinator.com/item?id=47961940 - the April 30, 2026 Show HN, 3 points, zero comments
