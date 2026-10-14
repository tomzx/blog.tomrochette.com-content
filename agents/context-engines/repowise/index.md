---
title: Repowise
created: 2026-10-13
updated: 2026-10-13
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

Young and growing: 7,617 stars, 856 forks, and 313 open issues as of 2026-10-13, created 2026-03-23 and pushed 2026-10-12, PyPI at 0.56.0.
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

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins as the twenty-first column
- [code-review-graph](../code-review-graph/index.md) - the closest stored-graph member, one job over
- [Graphify](../graphify/index.md) - the deterministic AST-graph sibling it benchmarked against
- [Serena](../serena/index.md) - the live-parse counterpart it also benchmarked against

## References

- https://api.github.com/repos/repowise-dev/repowise - stars, forks, issues, AGPL-3.0 license, creation and push dates as of 2026-10-13
- https://raw.githubusercontent.com/repowise-dev/repowise/main/README.md - the three-way product map, the ten MCP tools, the benchmark tables with their losing rows, and the deployment matrix
- https://raw.githubusercontent.com/repowise-dev/repowise/main/docs/business/COMMERCIAL.md - the AGPL/commercial split, the three pricing models with no published figures, and the GA/in-development/planned capability labels
- https://pypi.org/pypi/repowise/json - the distribution at 0.56.0
- https://pypistats.org/api/packages/repowise/recent - 16,776 downloads in the trailing month as of 2026-10-13
- https://api.npmjs.org/downloads/point/last-month/repowise - 1,048 downloads in the month to 2026-10-11
- https://hn.algolia.com/api/v1/search?query=repowise&tags=story&hitsPerPage=10 - the footprint check: two Show HNs at 4 and 1 points, the rest unrelated or the vendor's own blog threads (fetched 2026-10-13)
- https://docs.repowise.dev - the docs portal (fetched 200, 2026-10-13)
- https://repowise.dev - the hosted service site (fetched 200 after redirect, 2026-10-13)
