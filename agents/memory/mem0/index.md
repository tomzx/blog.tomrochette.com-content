---
title: Mem0
created: 2026-08-24
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, agent-memory, developer-tools]
readability: 3
audience_notes: >
  Engineers adding persistent memory to an AI product or agent, assumed familiar with embeddings and retrieval basics.
  Not a coding-agent-specific note; harness users should read it as the memory-API side of the stack.
---

Mem0 is a hosted and self-hostable memory layer for AI agents: it extracts facts from conversations, stores them across vector, graph, and key-value backends, and retrieves the relevant slice into context on demand.

**Mem0 has the widest adoption of any dedicated memory product, and its benchmark numbers are the part I trust least.**

## What it is

The open-source SDK (`pip install mem0ai`, Apache 2.0) gives you the extraction and retrieval loop against your own stores.
The managed platform adds graph memory, a consolidation feature called Dream, analytics, and compliance posture (SOC 2, HIPAA, BYOK).
There is also a self-hosted server, a CLI, an MCP integration, and installable agent skills for Claude Code, Codex, Cursor, and others.
**The April 2026 algorithm rewrote the extraction loop around entity linking and temporal retrieval, which is a notable convergence toward graph-first rivals.**
The company (YC S24) was founded by Taranjeet Singh and Deshraj Yadav, previously of Embedchain and Tesla Autopilot's AI platform.

## Status

**Active and the adoption leader.**
The repository shows about 67.3k stars as of 2026-10-16 and 2,674 commits as of 2026-10-22.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=mem0ai/mem0&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=mem0ai/mem0&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=mem0ai/mem0&type=date&legend=top-left" />
</picture>

TechCrunch reported a $24M round (a $3.9M seed plus a $20M Series A led by Basis Set Ventures, with Peak XV and the GitHub Fund) in October 2025, 186M API calls in Q3 2025, and exclusive-memory-provider status for AWS's Agent SDK.
The site claims 150,000+ developers.
**The company launched its own benchmark, DolphinBench** (September 2026): three knowledge-work personas with roughly 500k tokens of history each, 600 tasks graded on the action an agent takes rather than on recall, with cost and latency mandatory in every report.
The harness is Apache-2.0 at mem0ai/dolphinbench (35 stars as of 2026-10-08), the paper (arXiv 2609.24971) carries Mem0's founders among its authors, and the leaderboard's results are client-rendered, so I could not verify any standings.
The 2024 Show HN drew 201 points and 61 comments, though moderators flagged booster comments in that thread.
The first independent academic comparison naming Mem0 has landed: SWE-ContextBench (arXiv 2602.08316, twelve academic authors, February 2026) ran four memory-retrieval frameworks on 99 related coding tasks, and its paper reports Mem0 weakest of the four on fail-to-pass tests (20.24 percent against Supermemory's 55.95) at the highest per-task cost ($0.62), on a benchmark measuring coding-agent context reuse rather than conversational memory.

## Strengths

- **The shortest path from zero to working memory**: two SDK calls, or a five-second agent self-signup via the CLI.
- Genuinely model-agnostic, with integrations across LangGraph, CrewAI, MCP, and the major coding harnesses.
- Real deployment options: managed, self-hosted server, on-prem, and a local-first OpenMemory variant.
- The evaluation suite is open-sourced, which is more reproducible than most rivals offer.

## Cautions

- **The advertised scores are platform scores**: the README itself says open-source users should expect "directionally similar gains but not identical numbers", so OSS and cloud are not the same product.
- Zep published a detailed rebuttal of the Mem0 paper, showing a misconfigured competitor setup, a flawed benchmark (LoCoMo), and Mem0's own full-context baseline beating its memory system; Mem0's response did not resolve the dispute.
- Community skepticism persists: HN threads question whether it learns user patterns or just stores sentences, and the launch thread raised GDPR gaps (since addressed with a trust center, per the site).
- Memory quality claims move fast here; the algorithm was replaced wholesale in April 2026.
- **DolphinBench extends the vendor-run-benchmark pattern this section flags on Hindsight, Supermemory, and MemOS**: the scoreboard's operator is the contestant's parent, and the action-grading framing has no independent replication yet.

## Pricing

The paid ladder restructured on 2026-10-26: Starter $19/month and Pro $249/month (graph memory and Dream land at Pro) are no longer sold to new accounts, existing subscribers keep their price, limits, and billing date, and plan changes or higher limits now go through the team as custom plans.
The free plan is the default path: the first 30 days run on Mem0-paid model calls with 10,000 adds and 1,000 retrievals a month, after which you connect your own LLM key and the limits rise to 50,000 adds and 10,000 retrievals a month at no charge from Mem0; past-limit calls error until the month resets, and without a key after the 30 days, adds error out while searches continue up to 1,000 a month.
The BYOK bill is real: Mem0's recommended models cost about $3.55 to $5.34 per 1,000 adds (GPT-6 Luna, Claude Haiku 5.5, DeepSeek V4.1 Flash), billed to your own provider account, which is how the free tier stays free at the higher limits.
Enterprise custom with on-prem and SSO remains.
**The OSS SDK is free but the benchmarked brain is the paid platform, which is the real price of the headline numbers.**

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Starter, Pro | Baseline: Hobby free (10k add and 1k retrieval requests/mo), Starter $19/mo, Pro $249/mo, Enterprise custom; OSS SDK free. | [mem0.ai/pricing](https://mem0.ai/pricing) |
| 2026-10-26 | Free, Starter, Pro | Starter $19/mo and Pro $249/mo stopped being sold to new accounts (existing plans grandfathered, plan changes go through custom plans); the free plan rebuilt around BYOK: 30 days of Mem0-paid model calls at 10k adds/1k retrievals per month, then your own LLM key lifts limits to 50k adds/10k retrievals at no Mem0 charge. | [docs.mem0.ai/platform/pricing](https://docs.mem0.ai/platform/pricing) |

## Compared to

- [Zep](../zep/index.md): temporal knowledge graphs and governance; choose it when facts change over time and audit matters.
- [Letta](../letta/index.md): a full agent harness with memory built in, versus Mem0's memory API bolted onto your stack.
- File-based conventions ([file-based agent memory](../file-based-agent-memory/index.md)): free and already in every harness; choose Mem0 when memory must span apps and users at scale.

## Bottom line

**Recommended for product teams that want user-facing personalization running this week and are fine with a managed dependency.**
I would not choose any memory vendor on benchmark leaderboards, this field's numbers are too contested; on that view Mem0's real moat is distribution (stars, downloads, the AWS deal), not memory science, and that is a claim readers can disagree with.

## Changes

- 2026-08-24 - Created among the four memory notes of the research index seeding run.
- 2026-09-05 - Relabeled the free tier as Hobby on the pricing page's rename, quotas identical.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-10-07 - Added the mem0ai/mem0 star history chart to the Status section.
- 2026-10-08 - Recorded DolphinBench, Mem0's own action-graded agent-memory benchmark (three personas, 600 tasks, cost and latency mandatory, Apache-2.0 harness, paper arXiv 2609.24971 with the founders as authors); the leaderboard is client-rendered and unverified, and the vendor-run-benchmark caution added; refreshed stars to about 66.8k and re-verified pricing unchanged.
- 2026-10-22 - Added the first independent academic comparison naming Mem0: SWE-ContextBench (arXiv 2602.08316) reports Mem0 weakest of four memory-retrieval frameworks on fail-to-pass coding-task tests (20.24 percent versus Supermemory's 55.95) at the highest per-task cost, on a coding-agent context-reuse benchmark rather than conversational memory.
- 2026-10-27 - Rotation re-verification: every cited URL re-fetched live (all eleven reachable, no dead sources), and the pricing restructure recorded (Starter and Pro no longer sold to new accounts, the free plan rebuilt around BYOK with a 30-day sponsored window, Price history row); the only default-branch push since the last verification is the pricing FAQ page itself.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched live (all twelve reachable, no dead sources), no facts changed; the only default-branch commits since the last verification are two update-versus-delete race fixes (a deleted memory is no longer re-created by a racing update) in the Python and TypeScript SDKs, with no release or pricing change.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where a memory layer sits relative to harnesses and models
- [Claude Code](../../harnesses/claude-code/index.md) - a harness whose skills and MCP surfaces Mem0 plugs into
- [OpenCode](../../harnesses/opencode/index.md) - a lean harness to contrast with memory-API-driven context

## References

- https://mem0.ai/ - product surfaces, developer-count claim, deployment options
- https://github.com/mem0ai/mem0 - stars and commits as of 2026-10-08, April 2026 algorithm, OSS-vs-platform disclaimer
- https://mem0.ai/pricing - tier and quota structure re-verified unchanged as of 2026-10-08 (Hobby free, Starter $19, Pro $249)
- https://docs.mem0.ai/platform/pricing - the pricing FAQ page (added 2026-10-26): legacy-plan grandfathering, the free plan's 30-day sponsored window and post-window BYOK limits, and the per-1,000-adds provider cost estimate
- https://dolphinbench.ai/ - DolphinBench: the action-graded benchmark, its three personas and 600 tasks, and the client-rendered leaderboard
- https://arxiv.org/abs/2609.24971 - the DolphinBench paper (submitted 2026-09-21) with Mem0's founders as authors
- https://github.com/mem0ai/dolphinbench - the Apache-2.0 benchmark harness, 37 stars as of 2026-10-09
- https://arxiv.org/abs/2504.19413 - the paper behind the SOTA claims
- https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/ - funding, traction, AWS Agent SDK deal
- https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/ - competitor rebuttal of the benchmark claims
- https://arxiv.org/abs/2602.08316 - SWE-ContextBench: the independent four-framework comparison on coding-task context reuse (Mem0 weakest, highest cost)
- https://news.ycombinator.com/item?id=41447317 - launch thread, community reception, flagged boosterism
