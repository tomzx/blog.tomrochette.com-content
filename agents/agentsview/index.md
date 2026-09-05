---
title: agentsview
created: 2026-08-30
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, observability, token-usage, open-source]
readability: 3
audience_notes: >
  Engineers who run multiple coding agents daily and want a retrospective view of sessions, token spend, and history across all of them.
  Assumes you know where tools like Claude Code store their session files.
---

agentsview is a local-first, MIT-licensed Go application that discovers the session files your coding agents already write on disk, indexes them into a searchable local SQLite archive, and serves a web UI, CLI, and desktop app for browsing, analytics, and token-cost reporting across roughly 60 agent sources.
Facts below verified as of 2026-09-05.

**agentsview's premise is that your agents already write the telemetry; the missing piece was a tool that reads all of it in one place, locally, instead of each harness showing you only its own slice.**

## What it is

A Go daemon that watches known per-agent session directories (Claude Code, Codex, Gemini CLI, Copilot, Cursor, Zed, Windsurf, OpenCode, Qwen Code, Goose, Kiro, and more, roughly 60 sources listed), parses their JSONL and database logs, and syncs them into a local SQLite database with FTS5 full-text search.
Surfaces: a web UI on loopback, a CLI (`agentsview usage daily`, `session search`, `stats`), a Tauri desktop app, Docker, plus optional PostgreSQL push for shared team dashboards, S3-backed session roots, and a DuckDB mirror.
Token-cost reporting uses a model-pricing catalog, and the project's own benchmark claims 84 to 223 times faster cost reports than re-parsing with ccusage, with the docs themselves calling that an upper bound.
Pure local file parsing: no cloud service, no accounts, no LLM calls required; an anonymous activity ping fires by default and can be disabled.
Made by Kenn Software LLC; install via curl script, Homebrew cask, desktop builds, or Docker.

## Status

Young and active: 5,771 stars, 652 forks, 103 open issues and PRs as of 2026-09-05, created 2026-02-19, pushed the day of verification.
Latest release v0.42.0 on 2026-09-01 with roughly weekly releases since July; pre-1.0 with fast feature churn.

## Strengths

- Breadth is the product: one tool indexes every major agent's sessions, where most alternatives are Claude-only.
- A pre-indexed store makes multi-month, multi-agent cost and history questions answerable in seconds instead of ad-hoc parsing.
- Serious team story: PostgreSQL push, machine-labeled filesystem sync, S3 roots, and versioned export schemas.
- Careful local-first hygiene: loopback binding, DNS-rebinding guards, auth for non-loopback exposure, and a documented trust model for untrusted session files.

## Cautions

- Pre-1.0 with breaking schema bumps (usage output is at schema version 5), so scripts consuming its output churn.
- Token coverage is opportunistic: cost rows appear only when a transcript contains both token counts and a priceable model, and the docs admit known undercounts such as Claude WebSearch side-calls.
- The benchmark numbers are vendor-supplied on vendor hardware.
- The daemon, serve, DuckDB, and PostgreSQL surface is real operational weight if all you wanted was a cost report.

## Pricing

Free and open source under MIT, no accounts, everything local.
No paid tiers are published.

## Compared to

- Built-in harness commands (Claude Code's usage and cost views): zero-install and authoritative for the current session, but single-agent, single-machine, and history-free; choose agentsview for retrospective multi-agent analytics.
- simple10/agents-observe: a Claude Code plugin capturing live hook events for in-flight dashboards; choose it for what my agent is doing right now, agentsview for a passive index of everything already written.
- xintaofei/codeg: a full multi-agent workspace where aggregation is a byproduct of running agents inside it; choose agentsview when you keep your existing setups and want a read-only analytics layer.

## Bottom line

**Recommended for engineers running three or more different coding agents who want one private place to answer what did my agents do and cost this month.**
Not for single-agent users well served by built-in cost views, or teams wanting live in-flight observability rather than retrospective indexing.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note seeds
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the per-token economics these reports feed
- [OpenChamber](../openchamber/index.md) - the session cockpit on the run side rather than the analytics side
- [Claude Code](../claude-code/index.md) - the largest single source of the sessions it indexes

## References

- https://github.com/kenn-io/agentsview - repository, supported agents, architecture, license
- https://agentsview.io - docs, architecture, install, and the Kenn Software attribution
- https://agentsview.io/token-usage/ - cost computation, the ccusage benchmark and its upper-bound caveat, and the undercount disclosures
- https://github.com/kenn-io/agentsview/releases - release cadence and current version
- https://github.com/simple10/agents-observe - comparison data for the live-observability alternative
- https://code.claude.com/docs/en/costs - the built-in cost tracking this category extends
