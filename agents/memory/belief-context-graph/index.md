---
title: Belief Context Graph
created: 2026-10-16
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, knowledge-graphs, belief, open-source]
readability: 3
audience_notes: >
  Engineers running long-horizon agents who want memory that carries confidence and contradiction, not just retrieved text.
  Assumes you know what an agent trajectory and a knowledge graph are; no probability background needed.
---

Belief Context Graph (BCG) is BIGAI NLCO's MIT Python memory layer that turns agent trajectories into a graph of belief and decision nodes, each carrying computed confidence, evidence links back to exact source offsets, a temporal lifecycle, and typed contradiction edges.

**Its bet is that retrieval answers the wrong question: agents fail because they do not know what they currently believe, at what confidence, and what contradicts it, so BCG maintains a belief state instead of a text index.**

## What it is

BCG sits between an agent and its model: recent turns stay raw in context, older turns stream into graph construction, and the resulting belief snapshot is injected into the system prompt.
Construction runs through one of two backends: `unified` routes node and relation generation through one OpenAI-compatible model you configure, while `hybrid` builds graphs locally with a small vLLM model, local embeddings, and a local classifier, effectively free to run once set up.
Surfaces are a Python SDK, an optional HTTP streaming service, JSON and JSONL artifacts on disk for replay and audit, a bundled reference terminal agent, and a `bcg codex` wrapper that adds belief memory to Codex without touching its configuration, with the graph model billed through your own OpenRouter key.
The docs state the project boundaries plainly: no production graph-database adapter, no distributed session coordinator, no hosted control plane.

## Status

**Active, young, and research-institute-led, with adoption still near zero.**
224 stars, 2 forks, 0 tagged releases, and 8 contributors as of 2026-10-20 (GitHub API), on a repository created 2026-06-03, MIT; pushed_at reads 2026-10-28 from side-branch pushes while the default branch has been quiet since 2026-10-15, and the repository was renamed from `bigai-nlco/bcg`, which still resolves.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigai-nlco/belief-context-graph&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigai-nlco/belief-context-graph&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=bigai-nlco/belief-context-graph&type=date&legend=top-left" />
</picture>

The project's own evidence is self-published: the site reports +3.79pp accuracy over Default on BrowseComp (1,266 tasks, 16.2 percent fewer total tokens) and +9.69pp on BrowseComp-ZH (289 tasks, 9.5 percent fewer), with gpt-5.6-luna as the agent, as of 2026-10-16, and I found no independent replication of either run.
I found no Hacker News thread and no independent coverage through 2026-10-16 searches, so the footprint is the repository and its placement on the Awesome-Agent-Memory list.
The strongest critical source is the project itself: its status section concedes the probability calculation and propagation are not yet grounded in Bayesian inference or any mathematically justified framework, naming priors, likelihoods, evidence dependence, and calibration as open work.

## Strengths

- **Belief-native memory with deterministic confidence**: every node carries an inspectable initial score, evidence contribution, and relation-derived factors, so support and contradiction propagate by rules rather than by another model call.
- Contradiction is a first-class edge type (`depends_on`, `supplements`, `contradicts`), which is more than most members' status flags offer.
- Evidence provenance points back to exact offsets in the originating turn, and merge history records how duplicates were canonicalized.
- The hybrid backend makes graph construction effectively free and local, and artifacts are plain JSON and JSONL you can replay.

## Cautions

- **Zero releases and 2 forks**: there is no packaged version to pin, and the confidence semantics are self-admittedly ungrounded, so treat the numbers as ordering hints, not probabilities.
- The benchmark evidence is one agent configuration on one model, self-published as site SVGs, and BrowseComp is a search benchmark rather than a coding one.
- Graph construction bills a second model's tokens on top of your agent's (the unified backend), which the token-cost curves partly offset but do not eliminate.
- The `bcg codex` wrapper sends conversation and tool text to your graph provider, an extra egress path you must opt into explicitly.

## Pricing

Free and open: MIT, no hosted tier.
The unified backend bills your own OpenAI-compatible provider (the Codex path defaults to `openai/gpt-6-luna` through OpenRouter); the hybrid backend runs local models at infrastructure cost only.

## Compared to

- [Zep](../zep/index.md): the enterprise take on the same fact-invalidation problem, with bi-temporal validity windows and hosted governance; BCG is the local, unhosted research alternative whose confidence numbers are its own unprincipled draft.
- [LongMemory](../longmemory/index.md): temporal governance in SQLite with point-in-time recall; choose it when you want deterministic truth over sessions without a graph-construction model in the loop.
- [Cognee](../cognee/index.md): the graph pipeline generalist that builds entity graphs over your data; BCG narrows to agent trajectories and adds confidence, which Cognee does not model.

## Bottom line

**Recommended for engineers experimenting with belief-state memory on long-horizon research or browsing agents, where inspectable confidence and contradiction edges are worth an unreleased dependency.**
Not for production teams needing releases, support, or independently validated benchmarks, and not for coding agents yet, since the published evidence never leaves search tasks.

## Changes

- 2026-10-16 - Created from the 2026-10-16 Awesome-Agent-Memory entrant scan (the Belief Context Graph entry repointed at bigai-nlco/belief-context-graph on 2026-10-15), with six fetched sources and the self-admitted-ungrounded-confidence-plus-missing-footprint combination recorded as the critical angle.
- 2026-10-25 - Rotation re-verification: every cited URL re-fetched live, no facts changed (still zero tagged releases, and the repository's last push remains 2026-10-20 with nothing new on the default branch since).
- 2026-10-28 - Rotation re-verification: every cited URL re-fetched live, no facts changed (both BrowseComp figures intact on the project site, still zero tagged releases); the pushed_at signal resolved to side-branch pushes with the default branch quiet since 2026-10-15.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched live (all six reachable, no dead sources), no facts changed (still zero tagged releases, no default-branch commits since 2026-10-15, the pushed_at movement again side-branch only).

## See also

- [Zep](../zep/index.md) - the hosted bi-temporal counterpart on contradiction handling
- [LongMemory](../longmemory/index.md) - deterministic temporal governance without a graph model in the loop
- [Cognee](../cognee/index.md) - the generalist graph pipeline beside this trajectory-specific one
- [agentmemory](../agentmemory/index.md) - the session-memory server at the opposite end of the confidence spectrum

## References

- https://github.com/bigai-nlco/belief-context-graph - repository, stars, license, activity (GitHub API, as of 2026-10-16)
- https://raw.githubusercontent.com/bigai-nlco/belief-context-graph/main/README.md - architecture, quick start, Codex integration, the comparison table, and the self-disclosed status section
- https://bigai-nlco.github.io/belief-context-graph/ - the project site and its self-published BrowseComp benchmark figures
- https://belief-context-graph.docs.buildwithfern.com/ - the documentation: backends, integration paths, and the stated project boundaries
- https://raw.githubusercontent.com/bigai-nlco/belief-context-graph/main/LICENSE - the MIT license text
- https://github.com/TeleAI-UAGI/Awesome-Agent-Memory - the source list entry that surfaced the candidate this run
