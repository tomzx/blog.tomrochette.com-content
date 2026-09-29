---
title: Sim
created: 2026-09-29
updated: 2026-09-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, workflow, low-code]
readability: 3
audience_notes: >
  Teams choosing an open-source visual agent workflow builder after Flowise's death, who care about license and cloud costs.
  Assumes you know what n8n is and why this genre is crowded.
---

Sim is the Apache-2.0, YC X25-backed open-source workspace for building, deploying, and monitoring AI agent workflows on a visual canvas, self-hostable or consumed as cloud, pitched as the open n8n alternative.

**Sim is what Flowise could have been: a clean-Apache visual agent workflow builder with real launch momentum, now positioned to inherit the users that Flowise's archive stranded.**

## What it is

A collaborative workspace where agent systems are built visually on a canvas, through chat, or in code, with a knowledge base, tables, files, and block-by-block run logs (sim.ai, docs.sim.ai).
It is TypeScript, self-hosted via Docker or rented as Sim Cloud, built by the Sim Studio team out of Y Combinator X25 (Launch HN, 2025-05-21).
The repo sits at 29,749 stars with 3,847 forks, Apache-2.0, created 2025-01-05, and its description claims 100,000+ builders (GitHub API, as of 2026-09-29).

## Status

Active: last push 2026-09-29, release v0.9.5 on 2026-09-29, the same day (GitHub API, as of 2026-09-29).
Three HN launches mark the trajectory: 196 points for the first Show HN (2025-04-28), 55 points for the YC Launch HN (2025-05-21), and 240 points for "Sim, Apache-2.0 n8n alternative" (2025-12-11).
Pre-1.0 (v0.9.x) despite the scale, so the API surface is still moving.

## Strengths

- **The license is genuinely clean**: Apache-2.0 with no SaaS-restriction fine print, which in this genre is now a differentiator after Flowise's restricted license and Dify's conditions.
- Building modes cover the spectrum: visual canvas for operators, chat for iteration, code for engineers.
- Fast, durable community growth: about 30k stars in 20 months with three HN launches above 55 points.
- Observability is productized (block-by-block logs, enterprise access control, SSO, SOC2 messaging for the paid tiers).

## Cautions

- Pre-1.0 software at v0.9.5: expect breaking changes on a project this young.
- The genre risk is unchanged: Flowise's shutdown note argued coding agents erode rigid visual workflows, and Sim sits in exactly that lane.
- Seat-based cloud pricing with credit metering will punish bursty experimentation the way most SaaS builders do.
- "100,000+ builders" is a repo-description claim I could not independently verify.

## Pricing

Free tier at $0 (1,000 one-time credits, weekly refresh, up to 3 seats).
Pro at $25 per user per month (6,000 credits per month, more workspace capacity), Max at $100 per user per month (25,000 credits per month, SSO, SOC2 compliance, self-hosting options, dedicated support).
Annual billing saves 15 percent.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-29 | Free | observed at $0 with 1,000 one-time credits | https://sim.ai/pricing |
| 2026-09-29 | Pro | observed at $25 per user/month | https://sim.ai/pricing |
| 2026-09-29 | Max | observed at $100 per user/month | https://sim.ai/pricing |

## Compared to

- [Dify](../dify/index.md): the genre's giant; Sim wins on license cleanliness and building modes, Dify on ecosystem and enterprise depth.
- [Flowise](../flowise/index.md): the archived predecessor; Sim is the like-for-like replacement for its canvas builders.
- [AutoGPT](../autogpt/index.md): the category's other workflow platform; AutoGPT leans autonomous, Sim leans collaborative building.

## Bottom line

Recommended for teams that want a self-hostable visual agent workflow builder under a clean Apache-2.0 license and can live with pre-1.0 churn.
Not for coding-agent orchestration, and not for anyone needing long-term API stability guarantees today.

## Changes

- 2026-09-29 - Created when the deferred framework-tier pile from the 2026-09-27 triage resolved.

## See also

- [Flowise](../flowise/index.md) - the archived genre-mate whose users Sim can inherit
- [Dify](../dify/index.md) - the larger rival it will be evaluated against
- [AutoGPT](../autogpt/index.md) - the other surviving workflow platform in this category
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/simstudioai/sim - GitHub API (200): 29,749 stars, 3,847 forks, Apache-2.0, pushed 2026-09-29, created 2025-01-05 (as of 2026-09-29)
- https://sim.ai - official site (200): workspace products (workflows, knowledge base, tables, logs, enterprise)
- https://sim.ai/pricing - pricing page (200): Free $0, Pro $25/user/month, Max $100/user/month
- https://docs.sim.ai - official documentation, live (200)
- https://api.github.com/repos/simstudioai/sim/releases/latest - releases API (200): v0.9.5, published 2026-09-29
- https://hn.algolia.com/api/v1/items/46234186 - "Sim, Apache-2.0 n8n alternative" thread (200): 240 points, 61 comments, 2025-12-11
- https://hn.algolia.com/api/v1/items/43823096 - first Show HN (200): 196 points, 58 comments, 2025-04-28
- https://hn.algolia.com/api/v1/items/44052766 - Launch HN: Sim Studio, YC X25 (200): 55 points, 32 comments, 2025-05-21
