---
title: jcode
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, rust, yc, memory, multi-agent]
readability: 3
audience_notes: >
  Engineers choosing a terminal harness for heavy parallel agent use, or evaluating
  jcode's memory and swarm features. Assumes you know what a harness, PSS, prompt
  caching, and MCP mean.
---

jcode is a Rust terminal coding agent from Solo Systems, the one-person company of Jeremy Huang (YC S26), built on the claim that a tiny RAM footprint is what makes dozens of parallel agents practical.
Facts below verified as of 2026-08-30.

**jcode is the first harness whose headline feature is not intelligence but arithmetic: a roughly 28 MB native process per session, so running a dozen agents stops being a memory decision, and it ships the memory graph and swarm coordination that assume you will.**

## What it is

An MIT-licensed, Rust-native harness with a TUI, headless `jcode run`, a persistent server/client daemon (`jcode serve`, `jcode connect`), and a TypeScript SDK ([repo](https://github.com/1jehuang/jcode), [docs](https://jcode.sh/docs)).
It carries 30-plus provider integrations, subscription OAuth (Claude, ChatGPT, Gemini, Copilot, Azure) with multi-account switching, local models via Ollama and LM Studio, native AGENTS.md, hooks, and skills injected by embedding match rather than loaded at startup.
MCP is supported but stdio-only, and jcode reads your Claude Code MCP config live instead of importing a copy.
Its three distinctive systems are an embedding-based memory graph with passive recall and consolidation, same-repo swarm coordination with conflict notifications and agent messaging, and self-dev mode where the agent edits, rebuilds, and hot-swaps its own binary.

## Status

**Active and rising fast, with a bus factor of one.**
Created January 5, 2026, it shows 18,828 stars, 2,149 forks, 7,274 commits, and a push the day of verification (GitHub API), with near-daily releases (v0.81.3 on August 30, 2026).
It is Y Combinator-backed (S26), and the author reports 11,977 contributions in the last year ([about page](https://jcode.sh/about)).
The independent footprint is thin so far: two Hacker News threads at 3 and 5 points with zero comments (April 30 and August 10, 2026) and one favorable third-party comparison; 18.8k stars against that little discussion is unusual and worth watching.

## Strengths

- Resource efficiency is measured and published in detail: about 27.8 MB PSS per session with local embedding off (about 10 MB per added session) and 14 ms to first frame, versus 2.3 GB and 3.4 s for Claude Code in the same self-run comparison ([jcode.sh](https://jcode.sh/)).
- The memory system is the most complete shipping design in any harness: vector-embedded graph, passive cosine-similarity recall, a verifying sideagent, scopes, confidence decay, and contradiction relations.
- Swarm coordination is harness-native rather than bolted on: same-repo agents get file-conflict notifications, DM or broadcast messaging, and can spawn their own worker teams.
- Verification is harness-enforced: todo confidence scoring with a spike check, auto-poke when a turn ends with incomplete todos, and hill-climbability ratings on goals.
- Context engineering is disciplined: append-only conversation, an MCP schema cache so startup never busts the prompt cache, KV-cache-aware input interleaving, a structure-aware agent grep with adaptive truncation, and a 671-token system prompt.
- Session portability: it resumes Claude Code, Codex, OpenCode, and pi sessions, and jcode bench is a genuinely interesting uncontaminatable benchmark design with public transcripts.

## Cautions

- **Every number is self-published**: benchmarks run on the author's machine with author-chosen versions, and the RAM headline uses embeddings off, with embeddings on it is about 167 MB, six times the headline.
- Self-dev mode hands the agent its own source and the README itself warns that weaker models make subtle, breaking changes; treating your harness as mutable is a supply-chain decision.
- Solo founder, v0.x line, near-daily releases; churn is a real cost, and the site carries its own "under construction" flag.
- MCP is stdio-only; HTTP and SSE servers are recognized and skipped ([docs](https://jcode.sh/docs)).
- Ambient mode and the iOS app are announced but were not shipped as of the independent August 1, 2026 review ([grigio.org](https://grigio.org/jcode-the-coding-agent-that-raises-the-skill-ceiling-vs-opencode-and-pi/)).
- Community scrutiny is thin; most third-party material so far echoes the README.

## Pricing

The software is free under MIT with no feature gates.
Hosted inference is $10/month for $20 of credit (the first $20 effectively 50% off provider API price), then usage at 10% off provider API prices, hard-capped by default at $100/month ([pricing](https://jcode.sh/pricing)).
Enterprise is custom.

## Compared to

- [OpenCode](../opencode/index.md): the TypeScript full-environment harness with the broadest plugin ecosystem and ACP story; pick OpenCode for ecosystem breadth, jcode when parallel session density and built-in memory matter more.
- [Claude Code](../claude-code/index.md): the platform benchmark with the deepest IDE and web surface; jcode is the counter-bet that the terminal daemon wins on resources and coordination.
- pi (no note yet): the minimalism pole of the same terminal-first triangle the independent comparisons draw; jcode is its maximalist opposite, with everything pi refuses built in.

## Bottom line

Recommended for engineers running many parallel agents on one machine who want memory and multi-agent coordination built in, and who accept self-published numbers and v0.x churn.
Not for teams needing IDE integration, HTTP MCP, or independent benchmarking today.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - jcode measured against the other fourteen harnesses on shared rows
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where jcode lands in the harness layer's independent tail
- [OpenCode](../opencode/index.md) - the ecosystem-first counterpoint in the same terminal niche
- [File-based agent memory](../file-based-agent-memory/index.md) - the markdown conventions jcode's vector memory graph replaces

## References

- https://github.com/1jehuang/jcode - repository, MIT license, Rust, scale, release cadence, feature README, as of 2026-08-30
- https://jcode.sh/ - mission, RAM and startup benchmarks, memory, swarm, self-dev, prompt-size study, changelog
- https://jcode.sh/docs - AGENTS.md loading, hooks, skills, stdio-only MCP, remote daemon, ambient config
- https://jcode.sh/about - Solo Systems, Jeremy Huang, solo founder, YC S26
- https://jcode.sh/pricing - hosted inference and enterprise terms
- https://grigio.org/jcode-the-coding-agent-that-raises-the-skill-ceiling-vs-opencode-and-pi/ - independent three-way comparison and the ambient-mode caveat
- https://news.ycombinator.com/item?id=49249151 - the August 10, 2026 thread, 5 points, zero comments
- https://news.ycombinator.com/item?id=47961940 - the April 30, 2026 Show HN, 3 points, zero comments
