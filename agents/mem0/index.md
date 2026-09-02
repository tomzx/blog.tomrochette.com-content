---
title: Mem0
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, agent-memory, developer-tools]
readability: 3
audience_notes: >
  Engineers adding persistent memory to an AI product or agent, assumed familiar with embeddings and retrieval basics.
  Not a coding-agent-specific note; harness users should read it as the memory-API side of the stack.
---

Mem0 is a hosted and self-hostable memory layer for AI agents: it extracts facts from conversations, stores them across vector, graph, and key-value backends, and retrieves the relevant slice into context on demand.
Facts below verified as of 2026-09-02.

**Mem0 has the widest adoption of any dedicated memory product, and its benchmark numbers are the part I trust least.**

## What it is

The open-source SDK (`pip install mem0ai`, Apache 2.0) gives you the extraction and retrieval loop against your own stores.
The managed platform adds graph memory, a consolidation feature called Dream, analytics, and compliance posture (SOC 2, HIPAA, BYOK).
There is also a self-hosted server, a CLI, an MCP integration, and installable agent skills for Claude Code, Codex, Cursor, and others.
**The April 2026 algorithm rewrote the extraction loop around entity linking and temporal retrieval, which is a notable convergence toward graph-first rivals.**
The company (YC S24) was founded by Taranjeet Singh and Deshraj Yadav, previously of Embedchain and Tesla Autopilot's AI platform.

## Status

**Active and the adoption leader.**
The repository shows about 64.6k stars and 2,619 commits as of 2026-09-02.
TechCrunch reported a $24M round (a $3.9M seed plus a $20M Series A led by Basis Set Ventures, with Peak XV and the GitHub Fund) in October 2025, 186M API calls in Q3 2025, and exclusive-memory-provider status for AWS's Agent SDK.
The site claims 150,000+ developers.
The 2024 Show HN drew 201 points and 61 comments, though moderators flagged booster comments in that thread.

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

## Pricing

Free tier: 10,000 add and 1,000 retrieval requests per month.
Starter $19/month, Pro $249/month (graph memory and Dream land at Pro), Enterprise custom with on-prem and SSO, as of 2026-09-02.
**The OSS SDK is free but the benchmarked brain is the paid platform, which is the real price of the headline numbers.**

## Compared to

- [Zep](../zep/index.md): temporal knowledge graphs and governance; choose it when facts change over time and audit matters.
- [Letta](../letta/index.md): a full agent harness with memory built in, versus Mem0's memory API bolted onto your stack.
- File-based conventions ([file-based agent memory](../file-based-agent-memory/index.md)): free and already in every harness; choose Mem0 when memory must span apps and users at scale.

## Bottom line

**Recommended for product teams that want user-facing personalization running this week and are fine with a managed dependency.**
I would not choose any memory vendor on benchmark leaderboards, this field's numbers are too contested; on that view Mem0's real moat is distribution (stars, downloads, the AWS deal), not memory science, and that is a claim readers can disagree with.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where a memory layer sits relative to harnesses and models
- [Claude Code](../claude-code/index.md) - a harness whose skills and MCP surfaces Mem0 plugs into
- [OpenCode](../opencode/index.md) - a lean harness to contrast with memory-API-driven context

## References

- https://mem0.ai/ - product surfaces, developer-count claim, deployment options
- https://github.com/mem0ai/mem0 - stars and commits as of 2026-09-02, April 2026 algorithm, OSS-vs-platform disclaimer
- https://mem0.ai/pricing - tier and quota structure as of 2026-09-02
- https://arxiv.org/abs/2504.19413 - the paper behind the SOTA claims
- https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/ - funding, traction, AWS Agent SDK deal
- https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/ - competitor rebuttal of the benchmark claims
- https://news.ycombinator.com/item?id=41447317 - launch thread, community reception, flagged boosterism
