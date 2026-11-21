---
title: WrenAI
created: 2026-10-10
updated: 2026-11-21
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

Established and active: 17,877 stars as of 2026-10-18, 2,119 forks and 247 open issues as of 2026-11-21, created 2024-03-13, pushed 2026-11-19 (docs-only link fixes after the 2026-11-17 wren-core fix requiring every primary-key column in TO_MANY partial models, both unreleased above wren-v0.18.0), with wren-v0.18.0 published 2026-11-10 and PyPI (wrenai) tracking 0.18.0 (re-checked 2026-11-21), following wren-v0.17.1 on 2026-10-30.
Release 0.18.0 serves a project-bound agent and governed MCP through a shared context layer (the follow-up commit addressing the deferred review findings landed the same week), alongside fixes that keep result columns sharing a name in JSON output, preserve physical-column renames across Ossie export/import, respect CTE visibility when expanding semantic models, and scope flag grouping to its select.
Release 0.17.0 shipped the Apache Ossie work recorded here on 10-24 (the `wren context import` and `export` ossie commands joining dbt and OpenMetadata, plus importing a Wren project from an OpenMetadata catalog) alongside ClickHouse dialect-translation fixes, JSON output that keeps dates and integers intact, an MCP SDK major-version pin, and wren-core-py 0.8.2 (2026-10-23) with the DISTINCT ON column fix in the bindings, with the wren-v0.17.1 patch (2026-10-30) carrying the DuckDB 2.0 `to_arrow_table` compatibility fix between it and 0.18.0.
The docs page claims SOC 2 Type II certification and now quotes 17.8k GitHub stars against the live count; its old 17-plus data-source figure is gone (the README stays at 22-plus), closing the discrepancy flagged on 2026-10-11.
The community footprint is lopsided: a Hacker News search returns over a thousand matches but every thread is small (the largest found carries 6 points), so nearly five figures of stars have produced no front-page discussion.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Canner/WrenAI&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Canner/WrenAI&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Canner/WrenAI&type=date&legend=top-left" />
</picture>

## Strengths

- Business context that survives review: metric definitions and examples live as diffable YAML in pull requests, which is the governance story most text-to-SQL tools skip.
- It meets agents where they are: MCP, CLI, and a skill for Claude Code, Cursor, Cline, and Codex, with no new chat product to adopt.
- The guardrails are named and mechanical (dry-plan validation, row limits, structured errors), which is what governed SQL actually requires.
- Open core with a workable self-host path, and the cloud entry tier is genuinely free rather than a timed trial.

## Cautions

- Every accuracy claim is vendor-run: the README's comparison table and correctness story are marketing artifacts, and no independent benchmark of the governed-SQL quality exists in the fetched material.
- The credit model prices questions, not seats: cloud tiers meter usage in credits, so a rollout that succeeds gets more expensive, and row- and column-level control, audit, and the evaluation framework sit behind the $559 monthly tier (MCP moved into Essential in the same November 2026 restructure that removed the free tier).
- The category fit is a scope call: it is an engine over business semantics and produces SQL plus dashboards, not code context, so it sits at the edge of what this section covers.
- Deep BI-market competition (traditional BI tools and bare semantic layers) is the vendor's own framing, and the accuracy table that frames it is unchanged marketing.

## Pricing

Free open-source core (Apache-2.0, self-hostable, no UI).
Essential Cloud is $179 per month billed annually (13,200 annual credits, extra credits at $0.10, rollover up to 2x) and now includes the MCP server and embedded API; Enterprise Cloud is $559 per month billed annually (24,000 annual credits) adding row- and column-level data control, LDAP/AD and OIDC, the evaluation framework, and thread tracing; Enterprise Plus is quoted by sales: self-hosted in your own cloud, on-prem, or air-gapped, licensed by concurrent sessions rather than credits, annual contract only, adding SSO and SCIM 2.0.
Both cloud plans carry a card-required 7-day free trial and 20 free monthly credits on top of the included pool; the standalone free cloud tier the site listed through October (20 credits a month, 2 projects, 2 members, 10 tables per project) is gone from the pricing page and the billing docs as of 2026-11-15, the docs' users-and-projects line now reading unlimited, and the open-core page's FAQ still sends evaluators to that free Cloud tier as stale copy.
All figures as of 2026-11-15.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-10 | Free | Recorded at $0, 20 monthly credits, 2 projects, 2 members | https://www.getwren.ai/pricing |
| 2026-10-10 | Essential Cloud | Recorded at $179/month billed annually, 13,200 annual credits | https://www.getwren.ai/pricing |
| 2026-10-10 | Enterprise Cloud | Recorded at $559/month billed annually, 24,000 annual credits | https://www.getwren.ai/pricing |
| 2026-11-15 | Free cloud tier | Removed from the public pricing page and the billing docs: the 20 monthly credits became an add-on to both paid Cloud plans, the 7-day trial now requires a credit card, the 2-project/2-member/10-table caps are gone (users and projects unlimited), and the MCP server moved from Enterprise into Essential. | [getwren.ai/pricing](https://www.getwren.ai/pricing) |

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
- 2026-10-22 - Rotation re-verification: every cited URL re-fetched, the star-history picture block corrected (its light-theme source and fallback carried the dark theme), and the docs-versus-README data-source discrepancy closed (the docs page now quotes 17.8k GitHub stars and no longer carries a source count); pricing tiers re-verified unchanged, forks and open issues refreshed.
- 2026-10-24 - Recorded the context import/export surface gaining Apache Ossie (2026-10-22, joining dbt and OpenMetadata under one import command with a matching export) and wren-core-py 0.8.2 (2026-10-23, the DISTINCT ON fix shipped in the bindings); volatile numbers refreshed (2,067 forks, 257 open issues, pushed 2026-10-23).
- 2026-10-27 - Recorded wren-v0.17.0 (published 2026-10-27: the Ossie context import/export commands and rename, OpenMetadata catalog project import, ClickHouse dialect-translation fixes, JSON output keeping dates and integers intact, and an MCP SDK major-version pin) with PyPI wrenai tracking 0.17.0; volatile numbers refreshed (2,070 forks, 262 open issues, pushed 2026-10-27).
- 2026-10-30 - Recorded wren-v0.17.1 (2026-10-30: the DuckDB 2.0 `to_arrow_table` compatibility fix) with PyPI tracking 0.17.1; volatile numbers refreshed (2,073 forks, 263 open issues, pushed 2026-10-30) and the credit tiers re-verified unchanged against the live pricing page.
- 2026-11-06 - Recorded main's unreleased SDK fixes (2026-11-02: cold connector initialization synchronized, and agent prompts now include v5 business rules); no release since wren-v0.17.1.
- 2026-11-11 - Recorded wren-v0.18.0 (2026-11-10: a project-bound agent and governed MCP served through a shared context layer, with the deferred-review follow-up, result columns sharing a name kept in JSON output, physical-column renames preserved across Ossie export/import, CTE visibility respected in semantic-model expansion, and flag grouping scoped to its select) with PyPI tracking 0.18.0; volatile numbers refreshed (2,091 forks, 246 open issues, pushed 2026-11-10).
- 2026-11-15 - Full rotation re-verification: every cited URL re-fetched and intact (repository and README still at 22-plus data sources, the releases feed, pull request #2821, PyPI at 0.18.0, the pricing page, the docs portal quoting 17.8k stars and SOC 2 Type II, and the HN search with the largest thread at 6 points); volatile numbers refreshed (2,106 forks, 249 open issues, pushed 2026-11-13); recorded main's unreleased SDK fix (2026-11-13: each project's .env secrets resolved per toolkit); no release since wren-v0.18.0.
- 2026-11-15 - Recorded the tier restructure observed on the pricing page and billing docs: the standalone free cloud tier (20 credits a month, 2 projects, 2 members, 10 tables per project) no longer exists, 20 free monthly credits became an add-on to both paid Cloud plans, the 7-day trial requires a credit card, the MCP server moved from Enterprise into Essential, and users and projects now read unlimited; the Pricing section rewritten, the stale Enterprise-gates-MCP caution corrected, and a Price history row appended.
- 2026-11-21 - Full rotation re-verification: every cited URL re-fetched and intact (the repository and README still at 22-plus data sources, the releases feed still topped by wren-v0.18.0, pull request #2821, PyPI at 0.18.0, the pricing page with Essential $179, Enterprise $559, and Enterprise Plus quoted by sales, the docs portal quoting 17.8k stars and SOC 2 Type II, the billing docs with the card-required trial and the 20-credit add-on, and the HN search with the largest thread at 6 points); recorded main's 2026-11-19 commits (the core docs index rebuild and the stale wren-README link fixes) as docs-only and non-material per the standing ruling, with the repository's 2026-11-20 pushed date read as off-main activity; volatile numbers refreshed (2,119 forks, 247 open issues); no release since wren-v0.18.0.

## See also

- [Context7](../context7/index.md) - the docs-injection sibling on the same delivery axis
- [qmd](../qmd/index.md) - the local-search contrast for knowledge bases
- [Vanna](../vanna/index.md) - the archived text-to-SQL RAG ancestor of the data-semantics column
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [MCP](../../protocols/mcp/index.md) - the protocol behind its agent delivery

## References

- https://github.com/Canner/WrenAI - repository: README, architecture, open-core split, license badge
- https://api.github.com/repos/Canner/WrenAI - forks, open issues, creation and push dates as of 2026-11-21 (stars kept at the 2026-10-18 baseline)
- https://api.github.com/repos/Canner/WrenAI/releases - wren-v0.18.0 published 2026-11-10 (the served project-bound agent and governed MCP context layer) after wren-v0.17.1 on 2026-10-30, plus the component release train (re-fetched 2026-11-21)
- https://api.github.com/repos/Canner/WrenAI/pulls/2821 - the Ossie import/export merge: Apache Ossie joining dbt and OpenMetadata under one `wren context import` command (fetched 2026-10-24; re-fetched intact 2026-11-15)
- https://www.getwren.ai/pricing - the credit tiers, quotas, and Enterprise feature gates (re-fetched 2026-11-21: Essential $179, Enterprise $559, Enterprise Plus quoted by sales, the free tier still gone, MCP server in Essential, card-required trial)
- https://docs.getwren.ai/cp/guide/account/billing - the billing docs confirming the card-required 7-day trial, the 20 free monthly credits as a paid-plan perk, and the unlimited users-and-projects line (fetched 2026-11-15)
- https://docs.getwren.ai/ - the docs portal: editions, SOC 2 claim, and the 15k-plus star line (re-fetched 2026-11-15)
- https://pypi.org/pypi/wrenai/json - CLI and SDK version 0.18.0 (re-fetched 2026-11-17)
- https://raw.githubusercontent.com/Canner/WrenAI/main/README.md - the full README: mechanism, comparison table, Git Sync, open-core terms
- https://hn.algolia.com/api/v1/search?query=WrenAI&tags=story&hitsPerPage=8 - the lopsided community-footprint check as of 2026-10-10
