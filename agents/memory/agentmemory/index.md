---
title: agentmemory
created: 2026-10-09
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, session-memory, mcp, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents who want one local memory server with a keyless
  default, profiled against claude-mem, Engrim, and the file conventions.
  Assumes you know what MCP and BM25 are.
---

agentmemory is an Apache-2.0 persistent memory server for AI coding agents: hooks and plugins capture session activity, an optional LLM pass compresses it into observations, and recall is served back over MCP, REST, and native plugins from a local state store, with BM25 working keyless from the first minute.

**Its bet is that session memory should be a shared server every harness on the machine reads, not a plugin per harness, and that retrieval should work with no API keys at all.**

## What it is

A Node CLI (`npx -y @agentmemory/agentmemory@latest`) from Rohit Ghumare (rohitg00), built on a pinned iii engine (v0.22.1) with a file-backed state store by default and an optional plain-Redis backend.
Keyless mode runs BM25 recall only; local embeddings (all-MiniLM-L6-v2, downloaded once) add semantic search without an API key, and any OpenAI-compatible endpoint enables LLM-written observation compression behind an explicit opt-in flag.
The surface is wide: 54 MCP tools, 12 Claude Code hooks, native plugins for Claude Code, Codex CLI, Cursor, OpenClaw, Hermes, and pi, MCP or REST wiring for roughly 20 more agents (Copilot CLI, Gemini CLI, Antigravity, Devin, Zed, Cline, Droid, and others), 17 installable skills, and Python, Rust, and Node programmatic access.
The design doc extends Karpathy's LLM-wiki pattern with confidence scores, lifecycle states, and a knowledge graph, and a companion gist carrying 1.6k stars is the project's founding artifact.

## Status

**Large and active, with adoption that outruns its discussion footprint.**
29,257 stars, 2,557 forks, and 554 open issues and pull requests, created 2026-02-25, pushed 2026-10-09, as of 2026-10-09 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=rohitg00/agentmemory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=rohitg00/agentmemory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=rohitg00/agentmemory&type=date&legend=top-left" />
</picture>

Latest release v0.9.30 (2026-10-06) with npm in sync at 0.9.30, and 30,196 trailing-month npm downloads (2026-09-08 to 2026-10-07).
The release train runs roughly monthly (v0.9.27 in June, v0.9.28 in July, v0.9.29 in August, v0.9.30 in October).
I found no dedicated Hacker News thread through 2026-10-09 searches, so the stars came through awesome-list placement and agent registries rather than public debate, the same stars-ahead-of-discussion pattern this section has flagged on Supermemory, Cabinet, and memU.

## Strengths

- **Keyless BM25 recall is the default that runs before any configuration**: the memory works before you configure any provider, which neither claude-mem nor the hosted APIs offer.
- The adapter surface is the category's widest for a self-hosted member, with one server sharing memory across every wired harness.
- **The benchmark receipts are unusually self-critical**: the published scorecard for the in-house corpus admits grep matches agentmemory on precision and that the lift is recall and temporal coverage, and the LongMemEval harness ships as an adapter-pluggable eval others can rerun.
- The README publishes a measured compression-spend table (888k tokens across 35 active hours) instead of leaving the token bill vague.

## Cautions

- **The headline numbers are still self-run**: LongMemEval-S 95.2 percent R@5 is the project's own harness, and the system does not appear among the published commercial leaders of the independent Agent Memory Leaderboard's first cycle.
- The pinned iii engine is a hard coupling: the server refuses a different engine version, so the dependency's fate is the project's fate.
- The runtime is a heavier footprint than the SQLite peers: four local ports, a background worker, and an optional Redis path whose pinned client does not speak TLS, a gap the README documents itself.
- The repo description's "#1 persistent memory" and the README's competitor table are marketing, and LLM compression bills your own provider when enabled.

## Pricing

Pricing does not apply: the engine is free and Apache-2.0 with no hosted tier of its own.
The costs are your hardware and, when observation compression is enabled, your own model provider's tokens.

## Compared to

- [claude-mem](../claude-mem/index.md): the same capture-and-compress idea bound to per-harness plugins with far larger adoption, where agentmemory is one server shared across harnesses with a keyless default.
- [Engrim](../engrim/index.md): the other cross-agent local store; Engrim is a thin curated SQLite scratchpad, agentmemory is a full server with 54 tools and a pinned engine.
- [File-based agent memory](../file-based-agent-memory/index.md): the zero-infrastructure convention; agentmemory earns its keep when capture of what happened, not curated notes, is the point.

## Bottom line

**Recommended for engineers running three or more coding agents who want one memory server, can accept a young pinned-engine dependency, and will rerun the eval harness on their own sessions.**
Not for single-harness users (claude-mem is simpler and battle-tested), privacy-strict environments that need zero background services, or anyone requiring independently audited benchmarks.

## Changes

- 2026-10-09 - Created from the 2026-10-09 awesome-list entrant scan, with eight fetched sources and the self-run-benchmark-plus-pinned-engine combination recorded as the critical angle.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [claude-mem](../claude-mem/index.md) - the adoption leader of the same capture-and-compress school
- [Engrim](../engrim/index.md) - the thin cross-agent local store at the opposite complexity end
- [Hindsight](../hindsight/index.md) - the Postgres-backed engine whose published-artifacts pattern agentmemory imitates
- [File-based agent memory](../file-based-agent-memory/index.md) - the zero-infra convention this automates against

## References

- https://github.com/rohitg00/agentmemory - repository, 29,257 stars, forks, open-issue count, activity, description, as of 2026-10-09
- https://raw.githubusercontent.com/rohitg00/agentmemory/main/README.md - architecture, the pinned iii engine, adapters, 54 tools, keyless mode, benchmark tables, the self-critical scorecard note, and the compression-spend measurement
- https://api.github.com/repos/rohitg00/agentmemory/license - the Apache-2.0 license file, verified through the GitHub API
- https://api.github.com/repos/rohitg00/agentmemory/releases - the release train (v0.9.27 through v0.9.30), as of 2026-10-09
- https://registry.npmjs.org/@agentmemory/agentmemory - npm at 0.9.30, in sync with the GitHub release
- https://api.npmjs.org/downloads/point/last-month/@agentmemory/agentmemory - 30,196 trailing-month downloads (2026-09-08 to 2026-10-07)
- https://hn.algolia.com/api/v1/search?query=agentmemory&tags=story - the footprint scan finding no dedicated thread (2026-10-09), the stars-ahead-of-discussion record
- https://agentmemoryleaderboard.ai/ - the independent academic-consortium leaderboard whose published first-cycle commercial leaders do not include this system
