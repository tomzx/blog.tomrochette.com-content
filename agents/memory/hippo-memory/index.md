---
title: Hippo Memory
created: 2026-11-25
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, memory, agent-memory, coding-agents, mcp, local-first, open-source]
readability: 3
audience_notes: >
  Engineers who correct the same coding agent in every session and want one store that every agent on the machine reads, profiled against the capture plugins and the transcript indexes.
  Assumes you know what Claude Code hooks, MCP, and BM25 retrieval are.
---

Hippo Memory (the hippo-memory npm package) is an MIT-licensed Node CLI and MCP server with zero runtime dependencies that stores the rules and lessons you teach one coding agent in a per-project SQLite store with markdown mirrors, weakens the memories behind bad answers, and serves the same store to every agent you run.

**Hippo's bet is that memory needs no model on its default path: capture finds rules and errors by word patterns, recall is BM25 with no network call, and every model-driven part is optional.**

## What it is

`hippo init` creates a `.hippo/` store in the project, adds a short block to an existing `CLAUDE.md` or `AGENTS.md`, installs Claude Code's hooks, and schedules a daily run at 6:15 that stores lessons from the day's commits and installs a local embedder (each part skippable with a flag).
`hippo recall` is keyword search with no model or network call, and `--why` shows the match.
A `SessionEnd` hook pins what you said as always, never, or must; `hippo outcome --bad` weakens the memories behind a bad answer; `hippo supersede` retires a replaced fact while keeping it on record; `hippo sleep` merges related memories and stores faded ones ready to restore.
It works with Claude Code, Codex, Cursor, Pi, OpenClaw, OpenCode, Gemini CLI, and any MCP client, imports notes from ChatGPT, `CLAUDE.md`, Cursor rules, Slack, and markdown, and needs Node.js 22.16 or newer.
It is made by kitfunso, a single author holding 1,271 commits against 124 by a Claude account and 19 by dependabot (GitHub API, as of 2026-11-25).

## Status

**Active and fast, with adoption ahead of independent discussion.**
793 stars and 46 forks as of 2026-11-25 (GitHub API), created 2026-03-15, pushed 2026-11-24, MIT, with 14 open issues and pull requests as of 2026-11-25 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kitfunso/hippo-memory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kitfunso/hippo-memory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kitfunso/hippo-memory&type=date&legend=top-left" />
</picture>

Latest release v3.16.0 (2026-11-24) with npm in sync at 3.16.0 as of 2026-11-25, and 12,086 npm downloads in the trailing month (2026-10-23 to 2026-11-22); the releases endpoint's newest hundred entries reach back only to v1.26.0, a train past a hundred releases.
The project's own eval, with the plan registered before the run, reports repeated mistakes per 100 chances across 29 repositories falling from 84 with no memory and 26 with Claude Code's built-in memory to 12 with built-in plus Hippo, at 1.006 times the cost.
In the benchmark table its README assembles, Hippo's column leads on a few official setups (HaluMem at 70.23 medium and 65.99 long, PersonaMem v1 at 61.97, EverMemBench at 44.20) and trails named members on most OmniMemEval shared setups (LoCoMo 74.72 against MemOS 88.83, Cognee 83.48, and Hindsight 81.99; LongMemEval-S 83.84 against MemOS 89.20), and it scores 10 of 100 on MemFail's coexisting-facts test against Mem0's 35 of 100.
The discussion footprint is one thread, the author's own 128-point Show HN (April 2026, 29 comments), where commenters question whether exponential decay catches a sharp migration and note the README never mentions the similarly named HippoRAG.

## Strengths

- **No model on the default path**: capture and recall run without an LLM call or a network call, so the bill is zero and nothing leaves the machine unless you opt into an API embedder, a reranker, or model-read rule capture.
- Memory health is an explicit loop: pinning, outcome weakening, superseding, and sleep consolidation are commands you can run and inspect.
- Every memory has a markdown mirror you can grep, commit, and review, so the store stays readable without the tool.
- The repeat-mistake eval registered its plan before the run and publishes every figure.

## Cautions

- **The benchmark table is self-assembled**: Hippo trails named members on most shared setups, and the repeat-mistake study is the author's own.
- Capture by word patterns is narrow by design: what you did not phrase as a rule or an error is not captured.
- A single-author project with a near-daily release train and no writeup beyond its own launch thread.
- `hippo init` edits `CLAUDE.md` or `AGENTS.md`, installs hooks, schedules a daily job, and installs a 480 MB local embedder unless you pass `--no-embeddings`.
- The team server binds a key to a tenant, not to a project: any member key can name another project, a limit the README states itself.

## Pricing

Hippo is free and MIT with no account or API key.
Optional features that call an outside provider bill through it: API embedders, and a reranker the README prices at about $0.0004 a recall.
A team server shares one store over MCP with API keys and admin and member roles, and a commercial edition with SSO, SCIM, SIEM export, hosting, and an SLA is planned with no price published as of 2026-11-25.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-25 | Hippo | Baseline: free and MIT, no account or API key; provider-billed optional features (API embedders, reranker at about $0.0004 a recall); commercial edition planned and unpriced. | [README](https://api.github.com/repos/kitfunso/hippo-memory/readme) |

## Compared to

- [File-based agent memory](../file-based-agent-memory/index.md): the free convention Hippo automates; files stay hand-curated, Hippo adds weakening, superseding, and consolidation.
- [claude-mem](../claude-mem/index.md): captures everything and pays tokens to compress it; Hippo captures only what reads as a rule or an error, with no model call.
- [deja](../deja/index.md): indexes the transcripts agents already wrote, so memory starts full; Hippo stores only what it captured since install but keeps strength and decay as first-class.

## Bottom line

**Recommended for a solo developer who corrects the same agent repeatedly and wants one readable, commit-able store shared by every agent on the machine, with no model bill.**
Not for anyone who needs retroactive memory of past sessions, per-project access control on a shared server, or benchmark numbers backed by an independent run.

## Changes

- 2026-11-25 - Created from the TeleAI source's 2026-11-23 additions, with the registered repeat-mistake eval set against the self-assembled benchmark table as the critical angle.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention Hippo automates
- [claude-mem](../claude-mem/index.md) - the capture-and-compress plugin it answers with a no-model path
- [deja](../deja/index.md) - the transcript index that starts full where Hippo starts empty
- [agentmemory](../agentmemory/index.md) - the other keyless local server shared across coding agents

## References

- https://api.github.com/repos/kitfunso/hippo-memory - repository metadata: 793 stars, 46 forks, created 2026-03-15, pushed 2026-11-24, MIT, 14 open issues and pull requests, as of 2026-11-25
- https://api.github.com/repos/kitfunso/hippo-memory/readme - install behavior, capture, recall, outcomes, sleep consolidation, the repeat-mistake eval, the benchmark table, the team server limits, and the cost FAQ
- https://github.com/kitfunso/hippo-memory/releases/tag/v3.16.0 - the latest release notes (2026-11-24)
- https://api.npmjs.org/downloads/point/2026-10-23:2026-11-22/hippo-memory - 12,086 downloads in the trailing month
- https://registry.npmjs.org/hippo-memory/latest - version 3.16.0, MIT, Node.js 22.16 or newer
- https://hippo-memory.com/benchmarks/ - the published benchmark pages
- https://github.com/kitfunso/hippo-memory/blob/master/docs/evals/2026-11-08-z0-round3-result.md - the registered repeat-mistake result
- https://hn.algolia.com/api/v1/items/47667672 - the 128-point Show HN thread and its skeptical comments (April 2026)
- https://api.github.com/repos/kitfunso/hippo-memory/contributors - the single-author commit distribution
