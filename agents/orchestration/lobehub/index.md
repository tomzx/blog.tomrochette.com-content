---
title: LobeHub
created: 2026-09-27
updated: 2026-09-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agent-platform, source-available, self-hosted]
readability: 3
audience_notes: >
  People choosing a self-hostable or hosted home for many AI agents and chat sessions across multiple model providers.
  Assumes you know what a bring-your-own-key chat client is and have compared a couple of them.
---

LobeHub is the TypeScript platform (formerly LobeChat) that repositioned itself from open-source AI chat client into a "Chief Agent Operator" which, in its README's words, organizes your agents into 7x24 operation by hiring, scheduling, and reporting on your entire AI team.

**LobeHub's 82k stars measure demand for a polished multi-provider chat client, not for agent operations, and the Chief Agent Operator story is a renaming of that demand rather than evidence for it.**

## What it is

A Next.js TypeScript application you can self-host (Docker, desktop apps) or use on LobeHub Cloud, with a plugin and skills ecosystem the README counts at 10,000+ tools and MCP-compatible plugins.
The agent-operations layer is new positioning on top of the chat product: assistants you "hire" get scheduled to run recurring work, and a reporting view shows what your agent team did while you were offline.
It speaks to many providers out of the box, and its pricing page shows GLM, GPT, Claude, and Kimi models metered through a credits system.
Deployment spans cloud, self-hosted servers with private models, and desktop canary builds.
The vendor is LobeHub LLC, which grew the product from the LobeChat project created in May 2023.

## Status

Active and shipping fast: the repo shows 82,839 stars, about 15.9k forks, and a push on 2026-09-27, the day I checked (GitHub API).
The release train is canary-grade desktop builds published several times a day; v2.2.19-canary.28 landed 2026-09-26 and five more canaries followed within hours.
The rebrand from LobeChat is visible in the license text itself, which reads "From 1.0, LobeChat is licensed under the LobeHub Community License".
Community footprint outside its own channels is thin: the best HN thread about it (as LobeChat) reached 7 points in July 2024, and my HN search for the current name returned nothing above noise.
A Product Hunt "top post" badge for the multi-agent-work launch and a Trendshift badge suggest its audience lives on Product Hunt and Chinese-language channels, not HN.

## Strengths

- **The self-hosted, bring-your-own-model base is real and polished**, with cloud, Docker, desktop, and private-model paths that few agent platforms match.
- A 10,000+ skills and plugin ecosystem gives scheduled agents something to actually do on day one.
- Multi-provider by design, so model churn lands on their pricing page instead of your migration backlog.
- Release velocity is unusual; the canary cadence means fixes arrive in hours, not quarters.

## Cautions

- **The license is not open source**: the LobeHub Community License is Apache 2.0 plus conditions that allow commercial use only without modifying the source, and require a commercial license for derivative works.
- The same license grants the producer the right to change terms and to use contributed code commercially, a one-way contributor bargain.
- The agent-operations layer is young positioning; I found no independent evidence, benchmarks, or case studies that the "hire, schedule, report" loop works at production depth.
- HN-scale scrutiny is nearly absent, so the safety question a commenter asked in 2024, how safe is this, still has mostly vendor-provided answers.

## Pricing

Cloud tiers meter usage in credits (as of 2026-09-27): Free with 500,000 credits per month, Starter at $9.9 per month (5M credits), Premium at $19.9 (15M), and Ultimate at $39.9 (35M), with yearly billing saving 20 percent versus monthly rates of $12.9, $24.9, and $49.9.
Self-hosting is free to run against your own provider keys, with private-model and custom integration options behind a contact link.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Starter / Premium / Ultimate | Baseline recorded: $9.9 / $19.9 / $39.9 per month billed yearly (monthly $12.9 / $24.9 / $49.9) | https://lobehub.com/pricing |

## Compared to

- [AutoGPT](../autogpt/index.md): the closest hosted rival; AutoGPT builds structure around workflows, LobeHub wraps operations around chat agents, and LobeHub's license is less restrictive for commercial use.
- [Vibe Kanban](../vibe-kanban/index.md): the developer-side scheduling board; choose it when the agents are coding agents in worktrees, LobeHub when they are general assistants.
- [Omnara](../omnara/index.md): the open control plane for supervising agents you already run, closer to LobeHub's reporting story but developer-first and Apache-style licensed.

## Bottom line

Recommended for individuals and teams who want a beautiful self-hosted home for multi-provider assistants with light scheduled automation, and who accept a source-available license.
Not for anyone who needs an OSI-licensed foundation, a commercial derivative product, or production-grade evidence behind the agent-operations claims.
My disagreeable claim: the hire-and-schedule framing will not hold, because the hard problems in 24/7 agent operations are permissions, credentials, and verification, none of which a chat client's architecture makes easy.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.

## See also

- [AutoGPT](../autogpt/index.md) - the hosted platform rival chasing the same operations story
- [Vibe Kanban](../vibe-kanban/index.md) - the developer-side take on scheduled parallel agents
- [Assistant runtimes](../../assistant-runtimes/_index.md) - the sibling category of self-hosted chat and agent runtimes
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/lobehub/lobehub - GitHub API (200): 82,839 stars, pushed 2026-09-27, TypeScript, created 2023-05-21 (as of 2026-09-27)
- https://raw.githubusercontent.com/lobehub/lobehub/canary/README.md - Chief Agent Operator pitch, 7x24 hire/schedule/report language, 10,000+ skills (200)
- https://raw.githubusercontent.com/lobehub/lobehub/canary/LICENSE - LobeHub Community License text: Apache 2.0 plus commercial conditions (200) (critical source)
- https://lobehub.com/pricing - Free/Starter/Premium/Ultimate tiers, credit system, self-host and private-model options (200, 2026-09-27)
- https://github.com/lobehub/lobehub/releases - releases (200): Desktop Canary v2.2.19-canary.28, published 2026-09-26
- https://lobehub.com/docs - documentation root (200)
- https://hn.algolia.com/api/v1/items/41070091 - the main LobeChat HN thread (200): 7 points, 2024-07-25, includes the creator's design-engineer answer and a safety question (critical source)
- https://hn.algolia.com/api/v1/search?query=lobehub&tags=story - search API (200): no LobeHub-named thread above noise, grounding the thin-footprint observation
