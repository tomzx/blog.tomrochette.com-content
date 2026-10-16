---
title: WrenAI
created: 2026-10-10
updated: 2026-10-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, semantic-layer, text-to-sql, genbi]
readability: 3
audience_notes: >
  Engineers wiring analytics agents to governed data warehouses who need business definitions to survive the trip into the prompt.
  Assumes you know what a semantic layer and MCP are; this is a context engine over business data, not code.
---

WrenAI is Canner's open-source GenBI engine: a governed semantic layer (MDL as reviewable YAML in your repo) plus an AI context layer that gives agents you already run the business meaning behind your data, so their questions come back as correct, guarded SQL and shareable dashboards.

**The context-engine reading is the point: schemas tell an agent where data lives, Wren tells it what the data means (approved metrics, enums, units, joins, worked examples), and that context is versioned in git rather than baked into one vendor's chat UI, which makes it this category's first engine over business semantics instead of code.**

## What it is

An Apache-2.0 core (MDL semantic layer, governed text-to-SQL, MCP server, CLI, SDK, and an installable agent skill that fetches workflow guides on demand) with commercial Wren AI Cloud and self-hosted Enterprise editions on top, made by Canner.
The pipeline claims schema-aware retrieval, MDL planning, dry-plan validation, row limits, value profiling, and structured errors with hints, and serves 22+ data sources (BigQuery, Snowflake, PostgreSQL, ClickHouse, Databricks, and more) on one Apache DataFusion engine.
Delivery is built for agents: `pip install wrenai` for the CLI and SDK, an MCP server, and a roughly 50-line discovery stub via `npx skills add Canner/WrenAI` so instructions match the installed version.
Everything Wren writes is plain YAML and Markdown in a repo you own, and Git Sync turns that repo into a governed team deployment with CI on definition changes.

## Status

Established and active: 17,877 stars, 2,062 forks, and 266 open issues as of 2026-10-16, created 2024-03-13, pushed 2026-10-16, with the wren-v0.16.0 release on 2026-10-16 and PyPI (wrenai) tracking the same 0.16.0.
The docs page claims SOC 2 Type II certification and 15k+ GitHub stars (conservative against the live count), though it says 17+ data sources where the README says 22+ (both figures re-checked unchanged 2026-10-11).
The community footprint is lopsided: a Hacker News search returns over a thousand matches but every thread is small (the largest found carries 6 points), so nearly five figures of stars have produced no front-page discussion.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Canner/WrenAI&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Canner/WrenAI&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Canner/WrenAI&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- Business context that survives review: metric definitions and examples live as diffable YAML in pull requests, which is the governance story most text-to-SQL tools skip.
- It meets agents where they are: MCP, CLI, and a skill for Claude Code, Cursor, Cline, and Codex, with no new chat product to adopt.
- The guardrails are named and mechanical (dry-plan validation, row limits, structured errors), which is what governed SQL actually requires.
- Open core with a workable self-host path, and the cloud entry tier is genuinely free rather than a timed trial.

## Cautions

- Every accuracy claim is vendor-run: the README's comparison table and correctness story are marketing artifacts, and no independent benchmark of the governed-SQL quality exists in the fetched material.
- The credit model prices questions, not seats: cloud tiers meter usage in credits, so a rollout that succeeds gets more expensive, and Enterprise features (MCP integration, row- and column-level control, audit) sit behind the $559 monthly tier.
- The category fit is a scope call: it is an engine over business semantics and produces SQL plus dashboards, not code context, so it sits at the edge of what this section covers.
- Deep BI-market competition (traditional BI tools and bare semantic layers) is the vendor's own framing, and the 17-plus versus 22-plus data-source discrepancy between docs and README needs watching.

## Pricing

Free open-source core (Apache-2.0, self-hostable) and a free cloud tier with 20 monthly credits (about 55 questions a month on the named model), 2 projects, 2 members, and 10 tables per project.
Essential Cloud is $179 per month billed annually (13,200 annual credits, extra credits at $0.10, rollover up to 2x).
Enterprise Cloud is $559 per month billed annually (24,000 annual credits) adding MCP integration, row- and column-level data control, and audit.
A fourth tier, Enterprise Plus, is quoted by sales: self-hosted in your own cloud, on-prem, or air-gapped, licensed by concurrent sessions rather than credits, annual contract only, adding SSO and SCIM 2.0, the evaluation framework, and thread tracing.
All as of 2026-10-13, the credit tiers re-verified unchanged against the live pricing page.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-10 | Free | Recorded at $0, 20 monthly credits, 2 projects, 2 members | https://www.getwren.ai/pricing |
| 2026-10-10 | Essential Cloud | Recorded at $179/month billed annually, 13,200 annual credits | https://www.getwren.ai/pricing |
| 2026-10-10 | Enterprise Cloud | Recorded at $559/month billed annually, 24,000 annual credits | https://www.getwren.ai/pricing |

## Compared to

- [Context7](../context7/index.md): the other outside-knowledge context engine, injecting library docs; Context7 serves code knowledge, WrenAI serves your business's data semantics.
- [qmd](../qmd/index.md): local hybrid search over your own docs and notes; qmd is generic retrieval, WrenAI is structured, governed semantics for warehouses.
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): the code-context platform with the only published scale threshold; both sell context to any agent over MCP, one over code and one over data.

## Bottom line

**Recommended for teams whose analytics agents already write SQL but keep missing what metrics mean: the git-versioned semantic layer over MCP is a working context engine for data work.**
Not for code tasks, and not for anyone who needs independently verified SQL accuracy, since every quality claim here is the vendor's own.

## Changes

- 2026-10-10 - Created from the hybrid-execution and context-engines resolution pass, placed in this category as the first data-semantic context engine (business meaning rather than code).
- 2026-10-11 - Re-checked the flagged docs-versus-README data-source discrepancy (docs 17+, README 22+, both unchanged) and refreshed the volatile numbers (17,841 stars); the credit tiers re-verified unchanged against the live pricing page.
- 2026-10-11 - Added Vanna to See also, the archived text-to-SQL RAG ancestor admitted to the category the same day.
- 2026-10-12 - Added the Enterprise Plus tier (self-hosted, concurrent-session licensed, quoted by sales) to the pricing section; the three credit tiers re-verified unchanged against the live pricing page, and the volatile numbers refreshed (17,848 stars).

## See also

- [Context7](../context7/index.md) - the docs-injection sibling on the same delivery axis
- [qmd](../qmd/index.md) - the local-search contrast for knowledge bases
- [Vanna](../vanna/index.md) - the archived text-to-SQL RAG ancestor of the data-semantics column
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [MCP](../../protocols/mcp/index.md) - the protocol behind its agent delivery

## References

- https://github.com/Canner/WrenAI - repository: README, architecture, open-core split, license badge
- https://api.github.com/repos/Canner/WrenAI - stars, forks, issues, creation and push dates as of 2026-10-16
- https://api.github.com/repos/Canner/WrenAI/releases - wren-v0.16.0 published 2026-10-16 and the component release train (fetched 2026-10-16)
- https://www.getwren.ai/pricing - the credit tiers, quotas, and Enterprise feature gates as of 2026-10-10
- https://docs.getwren.ai/ - the docs portal: editions, SOC 2 claim, and the 15k-plus star line
- https://pypi.org/pypi/wrenai/json - CLI and SDK version 0.16.0 with the semantic-SQL-layer description (fetched 2026-10-16)
- https://raw.githubusercontent.com/Canner/WrenAI/main/README.md - the full README: mechanism, comparison table, Git Sync, open-core terms
- https://hn.algolia.com/api/v1/search?query=WrenAI&tags=story&hitsPerPage=8 - the lopsided community-footprint check as of 2026-10-10
