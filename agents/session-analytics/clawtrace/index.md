---
title: ClawTrace
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, session-analytics, observability, openclaw, cost-tracking]
readability: 3
audience_notes: >
  Engineers running OpenClaw agents who want full-payload traces, per-step cost, and an AI analyst, and who can accept a hosted service.
  Assumes you know what an OpenClaw plugin and a trace span are.
---

ClawTrace is a hosted tracing and cost-attribution platform for OpenClaw agents: an Apache-2.0 OpenClaw plugin streams every run to a cloud pipeline that renders trace trees, call graphs, Gantt timelines, per-step dollar cost, and an AI analyst named Tracy.

**ClawTrace is this category's first hosted answer, and that is also its central trade-off: it sees more of each run than the local tools (real LLM payloads, sub-agent graphs, live cost) because your agent's traffic leaves your machine for its data lake.**

## What it is

The `@epsilla/clawtrace` plugin intercepts eight OpenClaw hook types (`session_start`, `session_end`, `llm_input`, `llm_output`, `before_tool_call`, `after_tool_call`, `subagent_spawning`, `subagent_ended`) and batches events to a hosted ingest service.
The pipeline writes partitioned JSON to cloud storage, materializes it through Databricks into Iceberg tables, exposes it as a Cypher graph in PuppyGraph (Tenant, Agent, Trace, and Span vertices with CHILD_OF edges), and serves a FastAPI backend and a Next.js UI.
Three views cover each trace: an execution tree with per-node cost badges, a force-directed call graph, and a Gantt timeline, plus a trajectory dashboard with daily trends.
Tracy is an AI analyst wired to the graph: it runs live Cypher queries, generates charts, and answers plain-English questions such as why a run cost so much or which tool fails most.
Pricing covers more than 80 models with cache-aware rates (fresh input, cached input, cache write, and output billed separately).
Setup is three shell commands, and the vendor is Epsilla, the company behind the Epsilla vector database.
The repository is Apache-2.0, but the hosted cloud is the product and no self-hosted deployment path is documented.

## Status

Active but with the thinnest footprint in the category: 47 stars, 11 forks, 3 open issues, created 2026-04-10, last pushed 2026-08-15, with the npm plugin at version 0.1.23 published 2026-04-16, as of 2026-10-02.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=epsilla-cloud/clawtrace&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=epsilla-cloud/clawtrace&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=epsilla-cloud/clawtrace&type=date&legend=top-left" />
</picture>

It launched on Hacker News twice in April 2026 (a 2-point post and a 1-point Show HN, neither with a comment beyond the author's own), and I found no Reddit discussion.
It also carries a paper, "ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation" (arXiv 2604.23853), which is unusually rigorous for a tool at this stage.
**A hosted product from a small org with an academic paper and almost no community discussion, so treat the roadmap's self-evolving-agent promises as research rather than shipped features.**

## Strengths

- Full-payload tracing is the most detailed column in this category: real LLM inputs and outputs and tool payloads, not just token counts and tool names.
- Cost attribution at step granularity with more than 80 models and cache-aware pricing, aimed squarely at the incident the README describes (an agent burning roughly 40 times its budget by replaying 1,500 messages of history).
- Three complementary views plus Ask Tracy, which turns the trace graph into natural-language answers instead of leaving interpretation to the reader.
- The self-evolve skill and `/v1/evolve/ask` endpoint let the agent query its own trajectories, an unusual closed loop inside the product.
- The published paper gives it more methodological transparency than most tools in the category.

## Cautions

- It is hosted and cloud-only: trace payloads, including LLM inputs and outputs, stream to the vendor's data lake, the opposite of the local-first stance the rest of this category shares.
- Consumption billing meters storage continuously at 1.35 credits per MB per day, so idle traces keep drawing credits until they are deleted.
- The vendor's own paper reports no aggregate cost saving across the full 84-task SkillsBench transfer and no aggregate cost reduction when prune patches are removed, which undercuts the cheapest-sounding promise.
- Single-harness by design: OpenClaw only, and the data only exists if the OpenClaw plugin is installed and authenticated.
- Independent signal is very thin: two low-point Hacker News posts, no comments, and no third-party review I could find.

## Pricing

Consumption-based credits, with no monthly seat fee.
New users get 100 free credits, and credit packages run $10 for 1,000 credits, $50 for 5,000, $90 for 10,000 (listed as 10% off), and $400 for 50,000, with all packages expiring one year after purchase.
Usage is metered per feature: storage 1.35 credits per MB per day, listing trajectories 0.5 credits per query, trajectory detail 0.2 credits per query, Tracy input 0.5 credits per 1k tokens, and Tracy output 2.5 credits per 1k tokens.
Reaching zero credits puts the account into a deficit state that blocks ingestion and queries until it is topped up.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Credit packages | Starter introduced at $10 / 1,000 credits; Growth at $50 / 5,000; Pro at $90 / 10,000; Scale at $400 / 50,000; storage metered at 1.35 credits/MB/day | https://www.clawtrace.ai/docs/billing/credits |

## Compared to

- [agents-observe](../agents-observe/index.md): the local, MIT live dashboard for Claude Code and Codex; ClawTrace is hosted and OpenClaw-only but captures full payloads, so choose ClawTrace only if you run OpenClaw and can upload traces.
- [agenttrace](../agenttrace/index.md): the local-first audit that also reads OpenClaw logs; choose agenttrace instead when the data cannot leave the machine.
- [Langfuse](../../evaluation-review/langfuse/index.md): a self-hostable LLM observability stack with traces and evals; choose ClawTrace for OpenClaw-specific cost attribution and the built-in analyst, Langfuse for a bring-your-own stack.

## Bottom line

**Recommended for OpenClaw operators who want full-payload traces, per-step cost, and an AI analyst, and who accept a hosted cloud.**
Not for anyone who needs traces to stay local, multi-harness coverage, or a self-hosted observability stack.

## Changes

- 2026-09-27 - Created.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-07 - Added the epsilla-cloud/clawtrace star history chart to the Status section.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins
- [OpenClaw](../../assistant-runtimes/openclaw/index.md) - the runtime whose eight hooks feed ClawTrace
- [agents-observe](../agents-observe/index.md) - the local live dashboard this hosted tool parallels
- [agenttrace](../agenttrace/index.md) - the local-first alternative that also covers OpenClaw logs

## References

- https://github.com/epsilla-cloud/clawtrace - the repository, Apache-2.0 license, stars, and forks as of 2026-09-27
- https://raw.githubusercontent.com/epsilla-cloud/clawtrace/main/README.md - the plugin, eight hooks, cloud pipeline, graph schema, pricing detail, self-evolve skill, and paper citation
- https://www.clawtrace.ai/ - the product pitch, three views, and the headline claim of showing what failed and where spend leaked
- https://www.clawtrace.ai/docs/billing/credits - the credit packages, consumption rates, free credits, and deficit state
- https://www.clawtrace.ai/docs/getting-started/install-plugin - the eight hook types and the three-step setup
- https://www.clawtrace.ai/docs/ask-tracy - what the Tracy analyst answers from the trace graph
- https://arxiv.org/abs/2604.23853 - the paper and its no-aggregate-savings and regression-lane findings
- https://hn.algolia.com/api/v1/items/47769889 - the 1-point Show HN behind the thin-community claim
