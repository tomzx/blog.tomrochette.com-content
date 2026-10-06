---
title: Mastra
created: 2026-09-29
updated: 2026-10-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, typescript]
readability: 3
audience_notes: >
  TypeScript engineers choosing an agent framework, and platform buyers who want to know what the June 2026 supply-chain attack means.
  Assumes you know npm and have used at least one agent framework.
---

Mastra is the TypeScript agent framework built by the team behind Gatsby, now a platform with Studio, Server, and Memory Gateway layered over the open-source core.

**Mastra has the fastest commercial trajectory in this note set, 6.1 million npm downloads a month and $35M raised in 18 months, and it has already survived one supply-chain attack.**

## What it is

A TypeScript framework providing agents, workflows, tools, memory, evals, and tracing, with the Mastra platform (launched 2026-04-09) adding Studio for evaluation and observability, Server for deployment, and Memory Gateway for cross-framework agent memory.
It was founded by Sam Bhagwat, Shane Thomas, and Abhi Aiyer, the Gatsby leadership, went through YC, and launched in early 2025.
The repo sits at 28,407 stars with 2,879 forks, created 2024-08-06; the core is Apache-2.0 with `ee/` directories under a commercial license (GitHub API, LICENSE, as of 2026-09-29).

## Status

Active and shipping fast: last push 2026-10-05, `@mastra/core` 1.74.0 published to npm 2026-10-01, with GitHub releases through @mastra/core@1.72.0 on 2026-09-30 (GitHub API, npm, as of 2026-10-05).
npm recorded 7,348,015 downloads of `@mastra/core` in the month ending 2026-10-03, the largest install base in this note set.
Funding: $13M seed announced 2025-10-08 from 120+ investors including YC, Paul Graham, Gradient, and Guillermo Rauch, then a $22M Series A led by Spark Capital on 2026-04-09, totaling $35M (mastra.ai blog).
On 2026-06-16 Mastra disclosed a supply-chain attack that compromised multiple npm packages, with an incident report and fixes.

## Strengths

- **The TypeScript-native bet won its niche**: when Python teams get CrewAI and Agno, JS teams get a framework with Gatsby-grade DX polish and six million monthly installs.
- Evals and observability were built in from the start, not bolted on when enterprise buyers appeared.
- The platform launch (Studio, Server, Memory Gateway) gives production deployments a supported path.
- Real enterprise logos claim production use (SoftBank, PayPal, Adobe, Replit, Marsh McLennan per the company blog).

## Cautions

- **The supply-chain attack is the caution**: on 2026-06-16 multiple mastra npm packages were compromised, disclosed in an incident report, and the HN thread drew only 4 points, so most users likely never heard of it (critical source).
- The `ee/` directories are commercially licensed, so "Apache-2.0" is true only for the core; check before embedding.
- Enterprise traction numbers are company blog claims, not audited figures.
- Platform pricing is young and the free Starter tier carries metered limits (100K observability events, 24 CPU hours).

## Pricing

The open-source framework is free (Apache-2.0 core, commercial-license `ee/` portions).
Mastra Cloud has a Starter plan at $0/month, a Teams plan at $250/month, and Enterprise at custom pricing; metered overages apply (for example $10 per additional 100K observability events on Starter).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-29 | Cloud Starter | observed at $0/month | https://www.mastra.ai/pricing |
| 2026-09-29 | Cloud Teams | observed at $250/month | https://www.mastra.ai/pricing |

## Compared to

- [CrewAI](../crewai/index.md): the Python equivalent by community size; Mastra wins for JS stacks and built-in evals, CrewAI for role-based crews.
- [Agno](../agno/index.md): the Python platform rival with a similar framework-plus-control-plane structure; Agno self-hosts free, Mastra meters the cloud.
- [AutoGen](../autogen/index.md): the maintenance-mode predecessor; Mastra's book, courses, and studio aim directly at the developer-education slot AutoGen vacated.

## Bottom line

Recommended for TypeScript teams shipping agents to production who want evals, tracing, and a supported platform from one vendor.
Not for security-strict environments that cannot accept a recent npm supply-chain incident, or teams that need a pure single-license codebase.

## Changes

- 2026-09-29 - Created when the deferred framework-tier pile from the 2026-09-27 triage resolved.
- 2026-10-02 - Recorded @mastra/core 1.74.0 (October 1 on npm) as the new latest release and refreshed download, star, and push counts.

## See also

- [CrewAI](../crewai/index.md) - the Python framework with the closest community profile
- [Agno](../agno/index.md) - the Python platform rival with the same runtime-plus-control-plane structure
- [AutoGen](../autogen/index.md) - the maintenance-mode framework it displaces for JS teams
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/mastra-ai/mastra - GitHub API (200): 28,407 stars, 2,879 forks, pushed 2026-09-29, created 2024-08-06 (as of 2026-09-29)
- https://www.mastra.ai/pricing - pricing page (200): Starter $0, Teams $250/month, Enterprise custom
- https://mastra.ai/blog/seed-round - $13M seed announcement (200): YC, pg, Gradient, 120+ investors, 2025-10-08
- https://mastra.ai/blog/series-a - $22M Series A announcement (200): Spark Capital, total $35M, platform launch, 2026-04-09
- https://registry.npmjs.org/@mastra%2Fcore - npm metadata (200): @mastra/core 1.71.0, Apache-2.0
- https://api.npmjs.org/downloads/point/last-month/@mastra/core - npm downloads API (200): 6,113,628 downloads, month ending 2026-09-27
- https://raw.githubusercontent.com/mastra-ai/mastra/main/LICENSE.md - license text (200): Apache-2.0 with commercially licensed ee/ directories
- https://hn.algolia.com/api/v1/items/43103073 - launch thread (200): 442 points, 154 comments, 2025-02-19
- https://hn.algolia.com/api/v1/items/46693959 - Mastra 1.0 thread (200): 213 points, 70 comments, 2026-01-20
- https://hn.algolia.com/api/v1/items/48564925 - "Multiple mastra NPM packages compromised" thread (200): 4 points, 2026-06-17 (critical source)
