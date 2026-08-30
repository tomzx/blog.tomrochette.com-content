---
title: claude-mem
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, session-memory, compression, open-source]
readability: 3
audience_notes: >
  Engineers whose coding agents re-explain the same context every session and who want automated memory instead of hand-curated files.
  Assumes you know what Claude Code hooks and MCP are.
---

claude-mem is an open-source Apache-2.0 plugin that gives coding agents persistent cross-session memory by capturing session activity through lifecycle hooks, compressing it into observations with LLM calls, storing them in local SQLite, and injecting relevant context back into future sessions.
Facts below verified as of 2026-08-30.

**claude-mem is the strongest evidence yet that session memory has crossed from experiment to default expectation, and its cost model is the field's open question: it captures everything and pays your tokens to compress it.**

## What it is

A TypeScript plugin (Node 20+ or Bun) that hooks session lifecycle events: SessionStart injects context from recent sessions, UserPromptSubmit and PostToolUse capture activity, PreToolUse on Read adds file context, Stop summarizes.
A background worker compresses observations through the Claude Agent SDK (or Gemini or OpenRouter), and storage is a local SQLite database with FTS5 full-text search and optional Chroma vector search.
Retrieval is exposed as MCP tools plus a `mem-search` skill using three-layer progressive disclosure, which the project credits with roughly tenfold token savings over fetching full observations.
It targets Claude Code first-class, with install paths for OpenCode, Codex CLI, Gemini CLI, Cursor, Windsurf, Antigravity, OpenClaw, and more.
Made by Alex Newman (thedotmack), a solo author in the Vercel OSS Program, with a commercial cloud arm at cmem.ai.

## Status

Very large and fast: 92,651 stars, 8,153 forks, 270 open issues as of 2026-08-30, 73,623 npm downloads in the last month.
Created 2025-08-31, pushed 2026-08-29, latest release v13.18.0 on 2026-08-29.
**The v13.x version line tells you the churn rate: near-daily releases with major-version jumps, which is velocity and breakage risk in the same number.**

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
CMEM Cloud is $20/month for sync and one private MCP link; a Team tier lists $333/seat/month for 3-50 seats.
The hidden cost is compression: those LLM calls draw on your own model subscription or API budget, and no official per-session figure is published.

## Compared to

- [File-based agent memory](../file-based-agent-memory/index.md): free, transparent, version-controlled, best for stable facts; claude-mem automates recall of what happened, which files cannot do.
- [mem0](../mem0/index.md): a memory API for products you build; choose claude-mem when you are the end user of coding agents and want hooks already written.
- [Letta](../letta/index.md): a framework where memory is a runtime primitive for agents you architect; choose claude-mem to bolt memory onto agents you already run.

## Bottom line

**Recommended for heavy daily Claude Code or OpenCode users who feel the re-explaining tax every morning and accept the token bill for compression.**
Not for privacy-strict environments, anyone unwilling to run a local worker service, or small projects where a curated CLAUDE.md is still the right answer.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [File-based agent memory](../file-based-agent-memory/index.md) - the free convention it automates
- [Context Management Patterns](../context-management-patterns/index.md) - the injection-cost problem it tries to bound
- [mem0](../mem0/index.md) - the API-layer alternative

## References

- https://github.com/thedotmack/claude-mem - repository, supported agents, install methods, license
- https://docs.claude-mem.ai/ - feature set, pipeline, supported IDEs
- https://docs.claude-mem.ai/architecture/overview - hook architecture and the compression flow behind the token-cost caution
- https://docs.claude-mem.ai/cloud-sync - the documented privacy trade-off of the cloud tier
- https://claude-mem.ai - pricing tiers and adoption stats
- https://api.npmjs.org/downloads/point/last-month/claude-mem - the 73,623 monthly downloads as of 2026-08-30
- https://news.ycombinator.com/item?id=47422611 - the critical take from a competing memory author on the capture-everything approach
