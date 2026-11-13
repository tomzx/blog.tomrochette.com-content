---
title: Repowise
created: 2026-10-13
updated: 2026-11-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, code-intelligence, mcp, code-health, static-analysis]
readability: 3
audience_notes: >
  Engineers wiring a coding agent to a large codebase who want one local index to serve
  both agent context and code-health analytics, and who can tolerate an AGPL core with
  proposal-priced commercial tiers. Assumes you know what a call graph, MCP, and
  technical-debt scoring are.
---

Repowise is an AGPL-3.0 local code-intelligence tool that parses a repository's code, call graph, git history, tests, docs, and architectural decisions into one local index, then serves it to coding agents through ten task-shaped MCP tools and to humans through a dashboard and CLI.

**Repowise is the broadest bet in this category that understanding, not retrieval, is the product: the same index that answers an agent's "what calls this" also scores every file's health, finds the dead code, and ranks what to fix first, and it is the only member that benchmarked itself against this table's other columns directly.**

## What it is

A Python CLI (`uv tool install repowise`) that builds the index in `.repowise/` with zero LLM calls, then serves it through `repowise serve` as a local dashboard plus an MCP server with ten tools (`get_overview`, `get_answer`, `get_context`, `get_symbol`, `search_codebase`, `get_risk`, `get_change_risk`, `get_why`, `get_dead_code`, `get_health`, plus `list_repos` for workspaces).
The deterministic layers (graph, git, health, tests, dead code, docs) never call a model; model-written prose and decision mining are opt-in on your own key or offline through Ollama.
Beyond the agent surface it writes `CLAUDE.md` and `AGENTS.md` from the real index, keeps them current, shrinks command output with `repowise distill`, seeds linked worktrees from the base checkout, and spans repositories into workspaces with cross-repo contract checks.
Hosted repowise.dev runs the same engine as a service, and a commercial licence adds modification rights, in-VPC or air-gapped deployment, and SLA support, priced per seat, per indexed repository, or enterprise-wide.
Made by the repowise-dev organization, AGPL-3.0 or commercial, Python, active on PyPI as `repowise`.

## Status

Young and growing: 7,800 stars as of 2026-10-18, 1,013 forks and 378 open issues as of 2026-11-13, created 2026-03-23 and pushed 2026-11-13, PyPI at 0.60.1 (the 0.60 train shipped 2026-11-01 to 2026-11-02: v0.60.0 surfaced a plugin API with a plugin author guide, plugin provider loading, and a PLUGIN_API_VERSION constant alongside health-finding and update-performance fixes, and v0.60.1 folded commit-mined decisions into their merge records, added a confirm-a-decision-with-reason action, and reports phase timings from incremental updates).
Main's unreleased merge batches above v0.60.1, newest from 2026-11-13, add an opt-in `mcp.always_load` keeping the core read tools loaded in Claude Code, MCP server instructions that name only the tools the client is served, live reads using the served checkout rather than the stored path, workspace reading of Redis streams and Redis pub/sub in Go, Java, and .NET, Temporal task queues read as worker and client contracts, Kotlin extension bare-calls bound to the receiver's members first, Swift dead-code qualification for files used by unindexed sources, 2 to 8 MB source files parsed serially, and faster symbol/path search, following the 2026-11-11 batch (a health refinement wave in the large_method complexity scorer with literal table rows and view trees in SwiftUI, Compose, and Flutter counted as data, early-exit guard runs and setter chains counted once, framework-owned JVM signatures exempted, constructor parameter grace per language, low-precision markers advisory per language, and `#if` conditions no longer runtime branches, plus `get_why` dashboard explanations of why each stale decision is stale, decision-add JSON reporting blockers and the next confirmation command, the stale-wiki check running after pull, merge, rebase, and cherry-pick on Claude Code, and a language read off the extension for path-only test-tree callers), the 2026-11-08 batch (workspace reading of Dapr pub/sub topics in Java, JavaScript, Python, and Go, a local MCP tool-latency log with p50/p90 shown in status, a recovery hint attached to empty `search_codebase` concept replies, decision merging into an evidence-confirmed decision, plugin name-and-directory enforcement, a Java static-import binding fix, decision-mining cost recorded in `llm_costs` and the init cost line, and Gemini thinking-token costs included in output cost) and the 2026-11-06 merge train's sixteen community fixes and Maven-coordinate linking.
**The community footprint is thin for the star count: two Show HN posts drew 4 and 1 points in April 2026 and the vendor's own blog threads stayed single-digit, so the adoption signal is stars and downloads (about 16.8k PyPI downloads in the trailing month) without practitioner debate.**
The vendor publishes the most checkable benchmark claims in this category: call-graph precision of 0.976 to 0.995 against the Go and TypeScript compilers' own resolution, and a self-built 42-instance context-tool comparison where its file coverage (0.876) leads Graphify, code-review-graph, and Serena, with the losing rows published.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=repowise-dev/repowise&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=repowise-dev/repowise&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=repowise-dev/repowise&type=date&legend=top-left" />
</picture>

## Strengths

- The agent surface is genuinely task-shaped: a question like "what breaks if I change this" returns symbol-level blast radius plus the tests that reach it, in one call, which is the context-selection job this category exists for.
- The benchmark section is the category's most falsifiable: compiler-graded call-graph precision per language, a sealed held-out comparison split, and losing rows published next to the wins.
- One index serves agents, humans, and CI at once, so the health scores and the agent's answers come from the same parsed facts rather than two divergent tools.
- The agent integrations go past MCP: generated `CLAUDE.md`/`AGENTS.md` from the real index keep non-MCP agents informed, and `repowise distill` applies reversible output shrinking in the same tool.

## Cautions

- **Every published number is self-run**: the ContextBench comparison split is the vendor's own construction, and no third party has replicated any figure as of 2026-10-13.
- The suite is far wider than the context job (health scores, security signals, SBOM and compliance reporting on the commercial roadmap), and the vendor's own commercial document labels capabilities GA, in-development, or planned, so expect uneven maturity across layers.
- AGPL-3.0 is a stop sign for embedders who will not accept copyleft, and the commercial licence that removes the obligation publishes no figures, only proposal-based pricing in three models.
- The thin footprint cuts both ways: 7.6k stars with two single-digit Show HNs is the star-velocity-without-debate pattern this section has flagged before.

## Pricing

Free and open source under AGPL-3.0: the local CLI, dashboard, MCP server, and the full deterministic layer set (graph, git, health, tests, dead code, docs, decisions) with zero LLM calls and no API key.
Hosted repowise.dev is free to start.
The commercial licence (modification without AGPL obligations, in-VPC or air-gapped deployment, SLA support, patent grant) is priced per seat, per indexed repository with unlimited seats, or enterprise-wide, with specific figures provided by proposal only, none published as of 2026-10-13.

## Compared to

- [code-review-graph](../code-review-graph/index.md): the closest member, also a stored local graph with blast radius, risk scores, and dead code; repowise adds git analytics, health scores, generated docs, decision mining, and workspaces, plus a commercial tier code-review-graph refuses to have.
- [Graphify](../graphify/index.md): both parse a repo into a queryable graph, but Graphify's is a deterministic AST map for structural questions while repowise's is compiler-checked with per-edge confidence stamps and carries git, tests, and decision context alongside.
- [Serena](../serena/index.md): Serena parses the working tree live for symbol-precise retrieval and editing; repowise keeps a standing index for repo-scale questions and change risk, so they compose on a large codebase.

## Bottom line

**Recommended for teams whose agents burn tokens re-discovering a large codebase and who want one local index to also carry the health and dead-code answers, after re-running the vendor's benchmark protocol on your own repository.**
Not for buyers who need published prices, a permissive licence, or independently replicated numbers, because none of those exist here yet.
My disagreeable claim: a context engine that also tells you what to fix first is the right product for the agent era, and the pure-retrieval columns in this table will sprout analytics layers within a year or lose the budget line to tools like this one.

## Changes

- 2026-10-13 - Created from the cross-category scan's flag (repowise-dev/repowise), admitted after the API's NOASSERTION license reading resolved to AGPL-3.0 and the kind call held (a local index served to agents over MCP, with analytics riding the same index), with the self-run-benchmark and thin-footprint cautions recorded as the critical angle.
- 2026-10-24 - Full rotation re-verification: every cited URL re-fetched; the ten-tool MCP surface, the 42-instance benchmark tables, and the commercial document's proposal-only pricing re-verified unchanged, v0.57.0 and v0.58.0 (2026-10-15 and 2026-10-20) both already in the recorded range, and the README's language support now 28 parsed to an AST; volatile numbers refreshed (944 forks, 405 open issues, pushed 2026-10-24, 913 npm downloads in the month to 2026-10-22, PyPIstats trailing month unchanged at 16,776).
- 2026-10-26 - Recorded v0.59.0 (2026-10-25: per-function coverage with the CRAP score and an untested-complexity finding in the health suite, plus test-reach and coverage-index fixes).
- 2026-11-05 - Full rotation re-verification: every cited URL re-fetched (repo, README, commercial document, PyPI, PyPI stats, npm downloads, the HN search, docs, and the hosted site all intact); the ten-tool surface, the benchmark claims, and the proposal-only commercial pricing unchanged.
- 2026-11-05 - Recorded the 0.60 train (v0.60.0 on 2026-11-01: plugin API with a plugin author guide, provider loading, and PLUGIN_API_VERSION, plus health and update-performance fixes; v0.60.1 on 2026-11-02: decision-record folding, confirm-a-decision-with-reason, update phase timings) and refreshed activity counts to 2026-11-05.
- 2026-11-07 - Recorded main's unreleased 2026-11-06 merge train (about sixteen community fixes and Maven-coordinate linking for Java and Kotlin imports) above v0.60.1; no release since.
- 2026-11-08 - Recorded main's unreleased 2026-11-08 merge batch (Dapr pub/sub topic reading in workspaces, a local MCP tool-latency log with p50/p90 in status, an empty-search recovery hint, decision merging and plugin name-and-directory fixes, a Java static-import binding fix, decision-mining cost in `llm_costs`, Gemini thinking-token costs) and refreshed the counts (989 forks, 433 open issues, pushed 2026-11-08); PyPI unchanged at 0.60.1.
- 2026-11-11 - Recorded main's unreleased 2026-11-11 merge batch (the large_method health wave counting literal rows, view trees, and guard runs as data with framework-owned JVM signatures exempted and low-precision markers advisory per language, `get_why` stale-decision explanations, decision-add blockers in CLI JSON, the stale-wiki check after pull/merge/rebase/cherry-pick on Claude Code, and the extension-based test-tree language read) and refreshed the counts (1,009 forks, 476 open issues, pushed 2026-11-11); PyPI unchanged at 0.60.1 and the trailing-month PyPI figure held at 16,776.
- 2026-11-13 - Recorded main's unreleased 2026-11-13 merge batch (opt-in `mcp.always_load` keeping the core read tools loaded in Claude Code, MCP instructions naming only the served tools, live reads from the served checkout, Redis streams and pub/sub workspace reading in Go, Java, and .NET, Temporal task queues as contracts, Kotlin extension receiver binding, Swift dead-code qualification, serial parsing of 2 to 8 MB source files, and faster symbol/path search) and refreshed the counts (1,013 forks, 378 open issues, pushed 2026-11-13); PyPI unchanged at 0.60.1.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins as the twenty-first column
- [code-review-graph](../code-review-graph/index.md) - the closest stored-graph member, one job over
- [Graphify](../graphify/index.md) - the deterministic AST-graph sibling it benchmarked against
- [Serena](../serena/index.md) - the live-parse counterpart it also benchmarked against

## References

- https://api.github.com/repos/repowise-dev/repowise - stars, forks, issues, AGPL-3.0 license, creation and push dates as of 2026-11-13 (stars kept at the 2026-10-18 baseline)
- https://raw.githubusercontent.com/repowise-dev/repowise/main/README.md - the three-way product map, the ten MCP tools, the benchmark tables with their losing rows, and the deployment matrix
- https://raw.githubusercontent.com/repowise-dev/repowise/main/docs/business/COMMERCIAL.md - the AGPL/commercial split, the three pricing models with no published figures, and the GA/in-development/planned capability labels
- https://pypi.org/pypi/repowise/json - the distribution at 0.60.1 (re-fetched 2026-11-05)
- https://pypistats.org/api/packages/repowise/recent - 16,776 downloads in the trailing month, unchanged when re-fetched 2026-11-05
- https://api.npmjs.org/downloads/range/2026-10-06:2026-11-05/repowise - 184 downloads summed for 2026-10-06 to 2026-11-05 (fetched 2026-11-05)
- https://hn.algolia.com/api/v1/search?query=repowise&tags=story&hitsPerPage=10 - the footprint check: two Show HNs at 4 and 1 points, the rest unrelated or the vendor's own blog threads (fetched 2026-10-13, query re-checked 2026-11-05)
- https://docs.repowise.dev - the docs portal (fetched 200, 2026-10-13)
- https://repowise.dev - the hosted service site (fetched 200 after redirect, 2026-10-13)
