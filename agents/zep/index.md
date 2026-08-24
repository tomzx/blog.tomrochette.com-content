---
title: Zep
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, agent-memory, knowledge-graphs]
readability: 3
audience_notes: >
  Engineers and platform leads evaluating memory infrastructure for production agents, assumed comfortable with graphs, retrieval, and compliance vocabulary.
  Skew toward teams with real governance requirements rather than solo builders.
---

Zep is an enterprise agent-memory service built on temporal knowledge graphs: facts carry validity windows, contradictions invalidate old facts instead of overwriting them, and everything traces back to source episodes.
Facts below verified as of 2026-08-24.

**Zep is the only major memory vendor whose core claim is handling change over time, and the market is slowly conceding the point as rivals bolt on entity links and temporal retrieval.**

## What it is

Zep Software (founded 2023, founder Daniel Chalef) sells a managed memory platform: Cloud, cloud with your own keys, and bring-your-own-cloud deployments, with SOC 2 Type II and HIPAA BAA options.
Under it sits Graphiti, the Apache 2.0 temporal context-graph engine (episodes, entities, facts with bi-temporal validity, hybrid semantic/BM25/graph retrieval, an MCP server), which you can also run yourself against Neo4j, FalkorDB, or Neptune.
**The managed tier adds the parts self-hosting lacks: a proprietary graph engine serving millions of per-user graphs at claimed sub-200ms retrieval, access control, retention policy, and audit.**
A Memory MCP Server and plugins for Claude Code, Codex, and Cursor push Zep memory into the harnesses themselves.

## Status

**Active, enterprise-focused, post-open-core.**
Graphiti shows about 30.2k stars and 951 commits as of 2026-08-24; its Show HN drew 142 points.
Zep Community Edition, the self-hostable open-core server, was discontinued in April 2025, with the company saying the two-product split starved the OSS side.
The site lists Samsung, Zscaler, Quorum, and HoneyBook among customers, and an S&P Global Market Intelligence report (April 2026) covers its temporal context graph.
I found no announced venture funding, which is itself a signal: it is bootstrapped or undisclosed, unusual among memory startups.

## Strengths

- **Bi-temporal fact invalidation is the differentiator**: query what is true now or what was true on any past date, which vector stores cannot do.
- Provenance: every fact traces to the episode that produced it, which is what audit actually needs.
- Graphiti is a real OSS engine, not a crippleware teaser, with active commits and a usable MCP server.
- Compliance and deployment flexibility (BYOK, BYOC) that rivals at this price lack.

## Cautions

- **The benchmark war with Mem0 is unresolved and both sides fumbled**: Mem0's paper evaluated a misconfigured Zep, and Zep's rebuttal headline (outperforms by 24%) itself needed a correction to 10%.
- Self-hosting Zep-the-product is dead; the path is Graphiti plus your own graph database, structured-output-capable LLMs, and low default ingestion concurrency (10 concurrent operations out of the box).
- Entry pricing starts at $104/month (annual) for 50k credits versus $19 at Mem0, and credits meter by episode size.
- Community skeptics call the knowledge-graph stack heavy infrastructure for personal or small-scale memory.

## Pricing

Free: 10,000 credits per month, no rollover.
Flex $104/month billed annually ($125 monthly) with 50,000 credits; Flex Plus $312/month annually ($375 monthly) with 200,000; Enterprise custom, as of 2026-08-24.
A credit covers one episode up to 350 bytes; retrieval, storage, and users are unmetered.

## Compared to

- [Mem0](../mem0/index.md): simpler, cheaper, wider adoption; choose Zep when temporal accuracy and governance are non-negotiable, Mem0 for speed to market.
- [Letta](../letta/index.md): memory inside a harness versus memory as a service; they compose more than they compete.
- Graphiti self-hosted: the free subset, at the cost of operating a graph database and losing the governance layer.

## Bottom line

**Recommended for production deployments where facts change (preferences, roles, prices, relationships) and where "why did the agent say that" must have an auditable answer.**
Not for solo builders or small budgets, and my disagreeable claim is that Mem0's April 2026 algorithm changelog (entity linking, temporal reasoning) reads as validation that Zep chose the right architecture first.

## See also

- [Mem0](../mem0/index.md) - the adoption leader it benchmarks against
- [Letta](../letta/index.md) - the harness-side approach to the same problem
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map this infrastructure plugs into
- [Gemini CLI](../gemini-cli/index.md) - a harness whose GEMINI.md file conventions are the zero-cost counterpoint

## References

- https://www.getzep.com/ - product claims, retrieval latency, customer list, deployment models
- https://github.com/getzep/graphiti - engine architecture, stars and commits as of 2026-08-24, self-host requirements
- https://github.com/getzep/zep - Community Edition deprecation and current repo role
- https://arxiv.org/abs/2501.13956 - the Zep paper (temporal knowledge graph for agent memory)
- https://www.getzep.com/pricing - plans and credit metering as of 2026-08-24
- https://blog.getzep.com/announcing-a-new-direction-for-zeps-open-source-strategy/ - the open-core retreat, April 2025
- https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/ - the benchmark rebuttal, with its own correction
