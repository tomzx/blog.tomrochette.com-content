---
title: Agno
created: 2026-09-29
updated: 2026-10-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python]
readability: 3
audience_notes: >
  Engineers choosing a Python agent platform who want to know what is behind the benchmark claims and what the control plane costs.
  Assumes you know what an agent runtime is and have compared at least two frameworks.
---

Agno is the Apache-2.0 Python agent framework formerly known as Phidata, repositioned as a full agent platform: an SDK, the AgentOS runtime, and a paid control plane on top.

**Agno turned a popular agent library into a platform company, and its aggressive performance benchmarking is both its megaphone and its credibility risk.**

## What it is

A framework plus runtime for building agents and multi-agent teams with memory, knowledge, tools, and reasoning, serving them through AgentOS, and managing them from a control plane with sessions, traces, and a no-code studio.
It came out of the Phidata project (repo created 2022-05-04) and rebranded to Agno in early 2025, declaring general availability on 2025-04-01 (agno.com).
The repo sits at 42,520 stars with 6,073 forks, Apache-2.0, Python 3.9+ (GitHub API, PyPI, as of 2026-10-03).

## Status

Active: last push 2026-10-03, latest release v3.1.1 on 2026-10-02, `agno` 3.1.1 on PyPI (GitHub API, PyPI, as of 2026-10-03).
v3.1.0 added role-based access control to AgentOS (a role store, scope policies, and an audit log) and a database-backed AgentOS filesystem, with a breaking re-key of the filesystem table that requires a manual upgrade script.
v3.1.1 followed a day later with live progress and cancellation for knowledge page sync (typed `PageSyncProgress` snapshots and a terminal `SyncReport`).
The GA announcement claimed 1M+ new agents created weekly and 22k stars at the time (company claim).
The pricing page now positions the control plane as framework-agnostic, connecting to AgentOS from Agno, LangGraph, or Claude Code.
No disclosed funding round surfaced in my search, which is unusual at this star scale and worth rechecking.

## Strengths

- **The full-stack bet is coherent**: framework, self-hosted runtime, and control plane from one vendor, with the runtime free and unlimited.
- The pricing pitch ("you own your data and compute, there is nothing for us to meter") matches how self-hosting teams actually buy.
- Apache-2.0 with no SaaS-restriction fine print, cleaner than the modified licenses common in this category.
- Multi-agent teams, memory, and knowledge are first-class rather than bolted on.

## Cautions

- **The headline benchmarks invite distrust**: "Agno: Agent framework 10,000x faster than LangChain" was the title of its biggest HN thread (47 points), where commenters challenged the claim, and the "5000x faster than LangGraph" phrasing lives on in the team's own announcements (critical source).
- Version velocity is high: three major versions by late 2026 means API churn for early adopters.
- The control plane is the business; the free runtime is the funnel, so expect the paid surface to grow.
- The benchmark-first marketing makes everything else the team says need independent verification.

## Pricing

Free tier at $0/month: unlimited usage and retention, self-hosted AgentOS, chat sessions, traces, no-code studio, memory, community support.
Pro at $150/month adds the control plane for live AgentOS, 1 live connection, 3 seats included, RBAC, and audit logs; add-ons are $30/month per extra seat, $95/month per extra live connection, and $300/month for SAML SSO.
Enterprise is custom with a free trial.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-29 | Free | observed at $0/month, unlimited usage and retention | https://www.agno.com/pricing |
| 2026-09-29 | Pro | observed at $150/month with $30/seat, $95/connection, $300 SAML add-ons | https://www.agno.com/pricing |

## Compared to

- [CrewAI](../crewai/index.md): the role-based Python rival with an enterprise console; Agno wins on runtime ownership and licensing, CrewAI on crew ergonomics.
- [Mastra](../mastra/index.md): the TypeScript peer; Agno is the pick if you are Python and want to self-host the runtime.
- [AutoGen](../autogen/index.md): the maintenance-mode predecessor; Agno courts exactly this migration with a control plane that accepts other frameworks.

## Bottom line

Recommended for Python teams that want a self-hosted agent runtime today with an optional managed control plane and a clean Apache-2.0 license.
Not for teams allergic to benchmark-driven marketing, or anyone needing a vendor with disclosed funding and a slow-moving API.

## Changes

- 2026-09-29 - Created when the deferred framework-tier pile from the 2026-09-27 triage resolved.
- 2026-10-02 - Recorded v3.1.0 (October 1, RBAC authorization and an AgentOS filesystem, with a breaking filesystem-table re-key) as the new latest release and refreshed star, fork, and push counts.
- 2026-10-03 - Recorded v3.1.1 (October 2, live progress and cancellation for knowledge page sync) as the new latest release on GitHub and PyPI, and refreshed star, fork, and push counts.

## See also

- [CrewAI](../crewai/index.md) - the Python framework it is most often benchmarked against
- [Mastra](../mastra/index.md) - the TypeScript platform with the same framework-plus-cloud structure
- [AutoGen](../autogen/index.md) - the maintenance-mode framework whose users Agno courts
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/agno-agi/agno - GitHub API (200): 42,377 stars, 6,032 forks, Apache-2.0, pushed 2026-09-29, created 2022-05-04 (as of 2026-09-29)
- https://docs.agno.com/introduction - official documentation, live (200)
- https://www.agno.com/pricing - pricing page (200): Free $0, Pro $150/month, add-ons $30/$95/$300
- https://pypi.org/pypi/agno/json - PyPI metadata (200): agno 3.0.11, Python >=3.9,<4
- https://api.github.com/repos/agno-agi/agno/releases/latest - releases API (200): v3.0.11, published 2026-09-23
- https://www.agno.com/articles/ga - GA announcement (200): Phidata rebrand, 2025-04-01, company claims (critical source: vendor claims)
- https://hn.algolia.com/api/v1/items/43274435 - "Agno: Agent framework 10,000x faster than LangChain" thread (200): 47 points, claims challenged (critical source)
- https://hn.algolia.com/api/v1/items/45596272 - Show HN: Agno multi-agent framework, runtime and UI (200): 15 points, 2025-10-15
