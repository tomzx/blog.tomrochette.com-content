---
title: claude-mem
created: 2026-08-30
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, session-memory, compression, open-source]
readability: 3
audience_notes: >
  Engineers whose coding agents re-explain the same context every session and who want automated memory instead of hand-curated files.
  Assumes you know what Claude Code hooks and MCP are.
---

claude-mem is an open-source Apache-2.0 plugin that gives coding agents persistent cross-session memory by capturing session activity through lifecycle hooks, compressing it into observations with LLM calls, storing them in local SQLite, and injecting relevant context back into future sessions.

**claude-mem is the strongest evidence yet that session memory has crossed from experiment to default expectation, and its cost model is the field's open question: it captures everything and pays your tokens to compress it.**

## What it is

A TypeScript plugin (Node 20+ or Bun) that hooks session lifecycle events: SessionStart injects context from recent sessions, UserPromptSubmit and PostToolUse capture activity, PreToolUse on Read adds file context, Stop summarizes.
A background worker compresses observations through the Claude Agent SDK (or Gemini or OpenRouter), and storage is a local SQLite database with FTS5 full-text search and optional Chroma vector search.
Retrieval is exposed as MCP tools plus a `mem-search` skill using three-layer progressive disclosure, which the project credits with roughly tenfold token savings over fetching full observations.
It targets Claude Code first-class, with install paths for OpenCode, Codex CLI, Gemini CLI, Cursor, Windsurf, Antigravity, OpenClaw, and more.
Made by Alex Newman (thedotmack), a solo author in the Vercel OSS Program, with a commercial cloud arm at cmem.ai.

## Status

Very large and fast: about 96.7k stars, 8.5k forks, and 87 open issues and pull requests as of 2026-10-06, with 69,573 npm downloads in the last month (2026-09-05 to 2026-10-04).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=thedotmack/claude-mem&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=thedotmack/claude-mem&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=thedotmack/claude-mem&type=date&legend=top-left" />
</picture>

Created 2025-08-31, pushed 2026-10-06, latest tagged release v13.32.0 on 2026-10-06 with npm in sync at 13.32.0 as of 2026-10-06.
The README now brands the project Grok Mem (the package is still `claude-mem`), and v13.24.0 shipped it as two independent Cursor and Grok Bot marketplace plugins alongside the Claude Code install path.
**The v13.x version line tells you the churn rate: near-daily releases with major-version jumps, which is velocity and breakage risk in the same number.**
v13.30.0 (2026-10-04) reworked hook delivery so hooks spool each event to disk and return without waiting on the worker, made observer prompts provider-cache-friendly, and dropped the separate per-prompt observer call, and v13.31.0 (2026-10-05) cut SessionStart's newest-memories query from seconds to milliseconds with new indexes.
v13.31.1 (2026-10-06) fixed cloud sync stalling behind Supabase's firewall (uploads are now compressed before forwarding, and HTML blocks are retried instead of read as bad tokens), and v13.32.0 (2026-10-06) restored the File Read Gate on by default: full-file Reads of observed code files are blocked and served the observation timeline plus outline tools instead, with partial reads exempt so edits never deadlock.

## Strengths

- Local-first by default: everything lives in `~/.claude-mem/`, with `<private>` tags excluding sensitive content and no account required.
- Token-aware retrieval design: progressive-disclosure search keeps the injection cost bounded instead of dumping raw history.
- One engine covers the harness landscape, so memory survives switching between Claude Code and OpenCode.
- Real adoption: the npm and star numbers make it the most-installed dedicated memory layer for coding agents.

## Cautions

- Compression runs an LLM call on every tool observation, often 100+ times per session, billed to your own quota; a competing memory author publicly calls the capture-everything family noisy and token-expensive.
- The cloud tier's own docs warn that enabling sync uploads observation narratives and full prompt text to your cmem.ai account.
- Operational surface is real: a background worker on a local port, optional Bun, Python, and Chroma dependencies, and a documented `npm install -g` footgun that installs the SDK without hooks.
- The README's association with a third-party CMEM crypto token is a credibility smell some buyers will not overlook.

## Pricing

The engine is free and Apache-2.0, fully local.
The commercial arm restructured on 2026-10-06: CMEM Pro is $30/month for hosted observation and cloud sync (private MCP link, memory generation on the hosted observer), Heavy is $70/month with more included usage, and CMEM Max is $100/month with the largest allowance plus billed overages, each with a usage allowance and automatic upgrade settings.
The former CMEM Cloud $20/month plan and the $333/seat/month Team tier are gone; the team product (TeamBrain) is a design-partner pilot whose price is set on a fit call, with no public price.
The hidden cost is compression: those LLM calls draw on your own model subscription or API budget, and no official per-session figure is published.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09 | CMEM Cloud | Baseline: engine free (Apache-2.0); CMEM Cloud $20/mo for sync and one private MCP link, Team $333/seat/mo for 3-50 seats. | [claude-mem.ai](https://claude-mem.ai) |
| 2026-10-06 | CMEM Pro, Heavy, CMEM Max | CMEM Cloud $20/mo and Team $333/seat/mo replaced: CMEM Pro $30/mo, Heavy $70/mo, CMEM Max $100/mo (allowance tiers with billed overages); TeamBrain pilot has no public price. | [cmem.ai/pricing](https://cmem.ai/pricing) |

## Compared to

- [File-based agent memory](../file-based-agent-memory/index.md): free, transparent, version-controlled, best for stable facts; claude-mem automates recall of what happened, which files cannot do.
- [mem0](../mem0/index.md): a memory API for products you build; choose claude-mem when you are the end user of coding agents and want hooks already written.
- [Letta](../letta/index.md): a framework where memory is a runtime primitive for agents you architect; choose claude-mem to bolt memory onto agents you already run.

## Bottom line

**Recommended for heavy daily Claude Code or OpenCode users who feel the re-explaining tax every morning and accept the token bill for compression.**
Not for privacy-strict environments, anyone unwilling to run a local worker service, or small projects where a curated CLAUDE.md is still the right answer.

## Changes

- 2026-08-30 - Created as a memory note covering session capture, compression, and reinjection, with 92,602 stars recorded.
- 2026-09-06 - Recorded the README rebrand to Grok Mem and the added Cursor and Grok Bot marketplace plugins.
- 2026-09-16 - Recorded the npm/GitHub release lag (npm at 13.25.1, the releases page still on v13.24.23) and refreshed stars to 94.0k with 191 open issues and PRs.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-22 - The npm-versus-GitHub channel drift closed: GitHub tagged v13.25.3 and npm published 13.25.3 within minutes on 2026-09-21, so the two release channels are back in sync.
- 2026-09-27 - Refreshed the volatile facts: about 94.8k stars, 312 open issues and PRs, 68,101 trailing-month npm downloads, and release v13.28.0 (2026-09-26) with npm in sync.
- 2026-10-03 - Recorded GitHub release v13.29.0 (2026-10-03) with npm lagging at 13.28.0 at fetch time, the first channel drift since 2026-09-21; refreshed stars to about 95.2k, 109 open issues and PRs, and 68,674 trailing-month npm downloads.
- 2026-10-04 - The npm-versus-GitHub channel drift closed: npm published 13.29.0, matching the v13.29.0 GitHub tag; refreshed stars to about 95.6k, 8.5k forks, and 128 open issues and PRs.
- 2026-10-05 - Recorded the v13.30.0, v13.30.1, and v13.31.0 releases (spooled hooks, cacheable observer prompts, indexed SessionStart) with npm in sync at 13.31.0; refreshed stars to about 96.3k, 105 open issues and PRs, and 68,891 trailing-month downloads.
- 2026-10-06 - Recorded the v13.31.1 and v13.32.0 releases (the cloud-sync firewall fix, and the File Read Gate restored on by default) with npm in sync at 13.32.0; refreshed stars to about 96.7k, 87 open issues and PRs, and 69,573 trailing-month downloads.
- 2026-10-06 - The commercial arm restructured its pricing: CMEM Cloud $20/mo and Team $333/seat/mo replaced by CMEM Pro $30/mo, Heavy $70/mo, and CMEM Max $100/mo, with TeamBrain a design-partner pilot without a public price (Price history row); the pricing reference repointed to cmem.ai, which claude-mem.ai now redirects to.
- 2026-10-07 - Added the thedotmack/claude-mem star history chart to the Status section.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [File-based agent memory](../file-based-agent-memory/index.md) - the free convention it automates
- [Context Management Patterns](../../context-management-patterns/index.md) - the injection-cost problem it tries to bound
- [mem0](../mem0/index.md) - the API-layer alternative

## References

- https://github.com/thedotmack/claude-mem - repository, supported agents, install methods, license
- https://docs.claude-mem.ai/ - feature set, pipeline, supported IDEs
- https://docs.claude-mem.ai/architecture/overview - hook architecture and the compression flow behind the token-cost caution
- https://docs.claude-mem.ai/cloud-sync - the documented privacy trade-off of the cloud tier
- https://claude-mem.ai - pricing tiers and adoption stats (now redirects to cmem.ai)
- https://cmem.ai/pricing - the restructured CMEM ladder ($30/$70/$100) and the TeamBrain pilot terms, as of 2026-10-06
- https://api.npmjs.org/downloads/point/last-month/claude-mem - the 68,891 monthly downloads (2026-09-04 to 2026-10-03) as of 2026-10-05
- https://news.ycombinator.com/item?id=47422611 - the critical take from a competing memory author on the capture-everything approach
