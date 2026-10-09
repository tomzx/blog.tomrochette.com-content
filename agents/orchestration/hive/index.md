---
title: Hive
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python]
readability: 3
audience_notes: >
  Engineers evaluating multi-agent runtimes for long-running business-process automation who want the colony model and its caveats without the marketing.
  Assumes you know what an agent loop and an agent harness are.
---

Hive is Aden's Apache-2.0 Python runtime for "colonies" of agents: a persistent Queen lead that spawns worker clones of itself around a shared tracker ledger and a persistent plan, positioned for business-process automation rather than coding sessions.

**Its bet is that coordination needs one primitive, not a graph: the Queen is an agent loop and every worker is a clone of it, so there is no orchestration DSL to learn and the colony grows at runtime.**

## What it is

A zero-setup, model-agnostic runtime (OpenAI, Anthropic, and Gemini are the documented providers) where you describe an outcome in natural language and the Queen grows a colony of specialized clones to run it, coordinating through a shared ledger and a persistent plan with crash-safe park/resume and cost enforcement.
Human oversight is built in as Sentinel, an out-of-band human-in-the-loop channel, alongside three-level observability.
Surfaces are a CLI (`hive run`, `hive tui`, `hive deploy`), Docker self-host, and Aden Cloud for managed deployment, with a documented Claude Code integration (`/hive`) for building the agents.
It is made by Aden, a five-person San Francisco company from Y Combinator's Winter 2020 batch that previously built the Acho data-worker app.

## Status

Active but uneven: 11,086 stars as of 2026-10-08 on a repository created 2026-01-12, with branches pushed the day before this check (GitHub API).
The default branch's last commit is 2026-09-14 and the GitHub release line stopped at v0.11.0 on 2026-05-02, five months before this check, so the code ships without tagged releases.
Three contributors dominate the history (about 1,179, 868, and 451 contributions), which matches a five-person company rather than a community.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aden-hive/hive&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aden-hive/hive&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aden-hive/hive&type=date&legend=top-left" />
</picture>

**The independent footprint is near zero: no Hacker News thread about it cleared 3 points through 2026-10-08, and the sharpest record is a 1-point, zero-comment December 2025 thread accusing Hive of taking Beads' approach to agent memory, unanswered and uncorroborated.**
The name also collides with Apache Hive, Hive OS, and a smart-home product line, so every search for it is polluted.

## Strengths

- One coordination primitive: workers are clones of the Queen, so new colony members inherit the same tools and model without wiring a graph.
- The production plumbing is real in the docs: crash-safe park/resume, per-colony cost enforcement, three-level observability, and Sentinel human approval.
- Apache-2.0 with Docker self-host or Aden Cloud deploy, and a Claude Code path for building the agents with the harness you already run.

## Cautions

- The release train stopped at v0.11.0 in May 2026 while trunk commits run monthly, the same ship-without-releasing pattern this category flagged on AgentsMesh.
- Three contributors dominate the history, so this is a single company's product with no community governance.
- Naming costs: the repo is hive, the product is OpenHive or Aden Hive, the company is Aden, and three unrelated Hives own the search results.
- The adoption record is the star count alone: no independent field reports, and an unresolved December 2025 provenance complaint from the Beads camp sits in the record.

## Pricing

No public prices: the runtime is free and Apache-2.0, and Aden Cloud is the hosted deploy without a published price table as of 2026-10-08.
No price history table until a price is published.

## Compared to

- [CAMEL](../camel/index.md): the research framework for studying agent societies; choose CAMEL to study colonies, Hive to operate one.
- [AG2](../ag2/index.md): the AutoGen community fork's conversational framework; choose AG2 for community-governed Python conversations, Hive for a ledger-and-clones runtime with crash recovery.
- [Raven](../raven/index.md): the DAG-planning host over coding agents; Raven plans engineering tasks, Hive's colonies run business processes.

## Bottom line

**Recommended for teams automating long-running business processes who accept a young, company-driven runtime with a stalled release train.**
Not for coding-session orchestration, where the parallel-agent columns are stronger, or for anyone who needs an active release line, community governance, or independent validation.
My disagreeable claim: **the 11.1k stars measure the colony pitch, not the artifact, because five months without a release, three dominant contributors, and near-zero independent discussion mean the count is riding the multi-agent wave rather than adoption, and I expect it to decouple from usage unless the release train restarts.**

## Changes

- 2026-10-08 - Created from the kaushikb11/awesome-llm-agents entrant scan.

## See also

- [CAMEL](../camel/index.md) - the research wing of the framework family this note joins
- [AG2](../ag2/index.md) - the community-fork framework alternative in the same wing
- [Raven](../raven/index.md) - the DAG-planning host agent with its own launch controversy
- [PraisonAI](../praisonai/index.md) - the low-code multi-agent framework closest in packaging
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/aden-hive/hive - repository, colony model, Sentinel, license, and README claims
- https://api.github.com/repos/aden-hive/hive - stars, created and push dates, and license, as of 2026-10-08
- https://github.com/aden-hive/hive/releases - the release line stopped at v0.11.0 (2026-05-02)
- https://docs.adenhq.com/ - the framework docs, quickstart, deployment surfaces, and Aden Cloud
- https://www.ycombinator.com/companies/aden - Aden's Winter 2020 batch, five-person team, founders, and Acho history
- https://hn.algolia.com/api/v1/search?query=hive%20agents&tags=story - the thin HN footprint, queried 2026-10-08
- https://hn.algolia.com/api/v1/items/46418623 - the 1-point Beads provenance thread (2025-12-29)
