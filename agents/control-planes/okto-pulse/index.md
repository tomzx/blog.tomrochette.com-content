---
title: Okto Pulse
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, spec-driven-development, governance-gates, coding-agents, mcp, local-first]
readability: 3
audience_notes: >
  Engineers running coding agents on long-lived codebases who want "done" to mean evidence rather than a plausible message from the agent.
  Assumes you already use an MCP-capable coding agent and know what spec-driven development and coverage gates are.
---

Okto Pulse (OktoLabsAI/okto-pulse) is an Elastic-2.0 local-first SDLC workbench that runs coding agents over MCP behind 17 named governance gates, blocking status transitions until spec coverage, validation, and evidence requirements are met.

**Its thesis is that AI can generate the implementation but cannot guarantee that every requirement was covered or every acceptance criterion has evidence, so the workbench turns product intent into a governed pipeline (stories, ideation, refinement, spec, sprint, tasks, tests, bugs) and refuses to let work reach done without proof.**

## What it is

`pip install okto-pulse` starts one Python process serving a web UI and API on port 8100 and an MCP server on 8101, with all state local under `~/.okto-pulse/` in SQLite plus an embedded graph database.
The same vendor ships a sibling product, [Okto Nexus](https://github.com/OktoLabsAI/okto-nexus) (`okto-nexus` 0.1.10 on PyPI, under the same Elastic License 2.0 plus SaaS/Branding Addendum): a local-first MCP coordination hub where agents in one repository get durable identities, presence, messages, inboxes, handoffs, artifacts, an event log, and governance controls without a cloud broker.
The platform page now lists a third product alongside them, [Okto Neuron](https://oktolabs.ai/platform/neuron/) (formerly Marginalia, 0.3.1, Elastic-2.0 source-available): a local-first knowledge-graph memory that extracts claims from Markdown notes and serves them over MCP with byte-range citations.
One `okto-nexus serve` port exposes the whole hub (streamable-HTTP MCP at `/mcp`, operator REST and SSE, and a bundled React dashboard) over a SQLite database in WAL mode, with 43 MCP tools by default and 46 with memory enabled.
The architecture splits into `okto-pulse-core`, which owns the SDLC domain, the governance gates, and knowledge-graph contracts as pure protocol seams, and `okto-pulse`, which supplies every concrete mechanism (SQLite, the Okto Grafx graph engine, the filesystem, scheduler, and MCP host); an unfilled slot fails closed rather than silently defaulting.
The gates cover resource readiness, spec coverage across acceptance criteria, requirements, business rules, API contracts, decisions, and test scenarios, plus task validation, test evidence, architecture findings, and sprint closure.
Tasks cannot start until the parent spec has the required scenario coverage, done transitions are held while unresolved issues remain, and test cards require evidence before being marked passed or failed.
An embedded knowledge graph keeps decisions, constraints, bugs, and learnings queryable with provenance across sessions.

## Status

Active and young: 110 stars, 4 forks, and 8 open issues as of 2026-10-07, created 2026-04-22, last pushed 2026-10-07, current PyPI version 0.3.3.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=OktoLabsAI/okto-pulse&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=OktoLabsAI/okto-pulse&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=OktoLabsAI/okto-pulse&type=date&legend=top-left" />
</picture>

No GitHub releases are published, so the PyPI package is the release channel, and the website still advertises v0.2.6 while the repository README documents v0.3.3.
**The internal numbers do not agree across surfaces: the README prose and the website both say 17 governance gates while the README's own platform table says 18, and the README says 340 core MCP tools while the product page says 215.**
The community footprint is thin: a Hacker News search for Okto Pulse returns nothing, so the evidence is the repository and the product site alone.

## Strengths

- The gate model is the point: coverage and evidence are enforced structurally before done, not reviewed after the fact.
- Local-first with no account, SQLite plus embedded graph, and an MCP endpoint that plugs into Claude Code, Cursor, Windsurf, Cline, or any MCP agent.
- The core and community split with fail-closed ports is an unusually clean separation for a young project.
- Spec-driven development and an operational knowledge graph in one tool, so requirements, decisions, and tests stay linked instead of spread across chat history.

## Cautions

- Elastic License 2.0 is source-available, not OSI open source; commercial use is allowed but you may not offer it to third parties as a hosted or managed service.
- Disagreements between the website, README prose, and README tables (gate and tool counts, version) make every volatile number worth re-checking before you cite it.
- Young project (0.3.x) with a single organization behind it, no published releases, and a very small community.
- It governs the coding workflow, not spending: it is not a budget or approval control plane in the Paperclip sense, despite sitting in this category.

## Pricing

Free to run locally with no account.
The README describes a possible SaaS edition and a core-and-community split, but no prices are published, so there is nothing to track yet.

## Compared to

- [Paperclip](../paperclip/index.md): a company-level control plane with budgets, org charts, and approvals; choose Paperclip to run a business of agents, and Okto Pulse to govern the requirements and evidence of one codebase.
- [Spec Kit](../../spec-driven-development/spec-kit/index.md): a lighter spec-driven development toolkit; choose Spec Kit for prompt-and-template discipline and Okto Pulse when you want gates and an audit trail on the transitions.
- [beads](../../task-management/beads/index.md): a dependency-aware issue tracker for agents; choose beads for the ledger and Okto Pulse when delivery also needs coverage and validation evidence.

## Bottom line

**Recommended for teams using coding agents on long-lived codebases who want spec coverage and delivery evidence enforced before work is accepted. Not for teams that need an OSI-approved license, a multi-agent org control plane, or a tool with a large community and stable versioning.**

## Changes

- 2026-09-27 - Created.
- 2026-09-29 - Added Okto Nexus as the vendor's sibling product (a local-first MCP coordination hub, okto-nexus 0.1.10, served from one `okto-nexus serve` port, same Elastic license).
- 2026-10-02 - Added Okto Neuron as the vendor's third product (formerly Marginalia, 0.3.1, Elastic-2.0, local-first knowledge-graph memory served over MCP with byte-range citations).
- 2026-10-07 - Added the OktoLabsAI/okto-pulse star history chart to the Status section.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category compared on shared rows
- [Paperclip](../paperclip/index.md) - the company-scale control plane this complements
- [Veto](../veto/index.md) - the pre-execution tool-call gate, a different enforcement point
- [Spec-Driven Development Feature Matrix](../../spec-driven-development/spec-driven-development-feature-matrix/index.md) - the adjacent shelf for spec-first tools
- [What Needs Updating When Agents Do the Work](../../../what-needs-updating-when-agents-do-the-work/index.md) - the corpus argument for keeping requirements and evidence current

## References

- https://github.com/OktoLabsAI/okto-pulse - README: gates, MCP surface, architecture, licensing, local data layout
- https://api.github.com/repos/OktoLabsAI/okto-pulse - stars, forks, issues, push dates as of 2026-10-06
- https://pypi.org/pypi/okto-pulse/json - current version 0.3.3 and Elastic-2.0 license metadata (re-checked 2026-10-02)
- https://oktolabs.ai/platform/pulse/ - product site: workflow, gate and tool counts, value proposition (re-fetched 2026-10-06, still advertising v0.2.6 and 17 gates)
- https://oktolabs.ai/platform/neuron/ - the Neuron product page: Marginalia rename, 0.3.1, ELv2, byte-range provenance, five MCP tools
- https://github.com/OktoLabsAI/okto-nexus - the sibling product's README: serve ports, tool counts, SQLite/WAL storage, dashboard, licensing (69 stars, pushed 2026-10-04, as of 2026-10-04)
- https://pypi.org/pypi/okto-nexus/json - okto-nexus 0.1.10 under Elastic License 2.0 plus the SaaS/Branding Addendum
- https://docs.oktolabs.ai - documentation index: install, quickstart, MCP setup, knowledge graph
