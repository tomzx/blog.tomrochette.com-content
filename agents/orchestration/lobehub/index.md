---
title: LobeHub
created: 2026-09-27
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, orchestration, agent-platform, source-available, self-hosted]
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

Active and shipping fast: the repo shows 83,237 stars, about 16k forks, and a push on 2026-11-25 (GitHub API, as of 2026-11-25), with v2.3.4 stable shipped 2026-11-18 (the weekly release turning Channels into a place where people and agents work together, 291 commits and 13 contributors since v2.3.3), then v2.3.5 stable shipped 2026-11-22 (a community-release backport: the cyan, green, and red agent cover colors from #23624, because a fresh install of main could resolve `@lobehub/ui` 6.19.0 inside the declared range and the old seven-entry palette failed type-checking there, plus the share upload lock's canary test), then v2.3.6 stable shipped 2026-11-24 (the weekly release making Agents easier to share and to work with in Channels, regrouping Skills, Connectors, and Agents into one Marketplace of 175 official MCP servers, adding on-demand tools that load only when a run activates them, and a Compact interface density, 358 merged pull requests from 12 contributors), and a v2.3.7-canary.1 riding ahead since 2026-11-24 (GitHub releases, as of 2026-11-25).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=lobehub/lobehub&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=lobehub/lobehub&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=lobehub/lobehub&type=date&legend=top-left" />
</picture>

The release train is canary-grade desktop builds published several times a day; the v2.2.19 line shipped stable on 2026-10-07, v2.2.20 followed on 2026-10-18 after canaries through 2026-10-17, and v2.3.0 shipped stable on 2026-11-01 with v2.3.1 (2026-11-03), v2.3.2 (2026-11-06), v2.3.3 (2026-11-12), v2.3.4 (2026-11-18), v2.3.5 (2026-11-22), and v2.3.6 (2026-11-24) following (GitHub releases, as of 2026-11-25).
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

The cloud plans no longer carry fixed monthly credit allowances, though model usage is still metered in credits (lobehub.com pricing, as of 2026-11-24): Free at $0 with standard models, about 50 agent tasks a month, 15 MB of file storage, and 100 vector entries; Basic at $10 a month or $9 on yearly billing ($108 a year) with 1,000 runs a month and no model usage, your own API key, and 1,000 vector entries; Plus at $20 a month or $18 yearly ($216 a year) behind the standard five-hour limit, with ultra models, 2 GB of file storage, and 10,000 vector entries; Pro at $100 a month or $90 yearly ($1,080 a year) at five times the Plus limits with 50,000 vector entries; Enterprise Edition (private deployment, a self-hosted provider, private models) on contact.
Yearly billing saves 10 percent, against the 20 percent the earlier credit plans carried, and every plan pays $0.01 per agent task.
Self-hosting is free to run against your own provider keys, with private-model and custom integration options behind a contact link.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Starter / Premium / Ultimate | Baseline recorded: $9.9 / $19.9 / $39.9 per month billed yearly (monthly $12.9 / $24.9 / $49.9) | https://lobehub.com/pricing |
| 2026-11-24 | Free, Basic, Plus, Pro, Enterprise Edition | the credit plans restructured: Starter, Premium, and Ultimate replaced by Basic $10 a month (yearly $9, $108 a year), Plus $20 ($18, $216), and Pro ($90, $1,080); credit allowances replaced by run and limit quotas (Free about 50 agent tasks a month, Basic 1,000 runs with no model usage); the yearly saving cut from 20 to 10 percent | https://lobehub.com/pricing |

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
- 2026-10-07 - Added the lobehub/lobehub star history chart to the Status section.
- 2026-10-08 - Recorded the v2.2.19 line shipping stable on October 7 after the canary train.
- 2026-10-27 - Re-verified in rotation: all cited sources re-fetched and live (repo API, README, license, pricing, releases, docs, HN thread and search); the push date refreshed to 2026-10-27, v2.2.20 still the newest stable, and the pricing tiers unchanged on the live page.
- 2026-11-01 - Recorded v2.3.0 stable (2026-11-01) on the release train.
- 2026-11-04 - Recorded v2.3.1 stable (2026-11-03) on the release train, the push date refreshed to 2026-11-04.
- 2026-11-13 - Volatile refresh: Recorded v2.3.3 stable (2026-11-12) on the release train (v2.3.2 having shipped 2026-11-06 inside the last verification window), the push date refreshed to 2026-11-13, plus the rotation re-fetch of every cited URL (all live; the docs root now redirects to the only-ai markdown path).
- 2026-11-19 - Volatile refresh: recorded v2.3.4 stable (2026-11-18, the Channels weekly release, 291 commits since v2.3.3) and the v2.3.5 canary line opening, the push date refreshed to 2026-11-19.
- 2026-11-24 - Volatile refresh: recorded v2.3.5 stable (2026-11-22, the community-release backport of the agent cover colors and the share upload lock test) and the v2.3.6-canary.1 line opening, the push date refreshed to 2026-11-24.
- 2026-11-24 - Rotation re-verification: every cited URL re-fetched live (the three GitHub API endpoints through the authenticated client after plain fetches returned 403, and lobehub.com pricing and docs, which answer scripted curl with HTTP 402, both read in full through a second client); the HN search and thread as recorded.
- 2026-11-24 - Recorded the pricing change: the Free, Starter ($9.9), Premium ($19.9), and Ultimate ($39.9) credit plans replaced by Free, Basic $10, Plus $20, and Pro $100 a month (yearly $9, $18, and $90, a 10 percent saving against the earlier 20), credit allowances replaced by run and limit quotas, Enterprise Edition on contact, with a Price history row.
- 2026-11-25 - Volatile refresh: recorded v2.3.6 stable (2026-11-24, Agent Share, Channels that agents act in, the combined Marketplace, on-demand tools, and Compact density) and the v2.3.7-canary.1 line opening, the push date refreshed to 2026-11-25.

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
- https://lobehub.com/docs - documentation root (200; re-fetched 2026-11-13, when the path began redirecting to lobehub.com/only-ai/markdown/docs/en)
- https://hn.algolia.com/api/v1/items/41070091 - the main LobeChat HN thread (200): 7 points, 2024-07-25, includes the creator's design-engineer answer and a safety question (critical source)
- https://hn.algolia.com/api/v1/search?query=lobehub&tags=story - search API (200): no LobeHub-named thread above noise, grounding the thin-footprint observation
- https://api.github.com/repos/lobehub/lobehub/releases/tags/v2.3.5 - the v2.3.5 release notes (2026-11-22): the agent cover-color backport from #23624 and the share upload lock canary test (fetched 2026-11-24)
- https://api.github.com/repos/lobehub/lobehub/releases/tags/v2.3.6 - the v2.3.6 release notes (2026-11-24): Agent Share, Channels agents act in, the Marketplace, on-demand tools, and Compact density (fetched 2026-11-25)
- https://api.github.com/repos/lobehub/lobehub/releases?per_page=6 - the release feed, v2.3.7-canary.1 (2026-11-24) back to v2.3.5 (2026-11-22), as of 2026-11-25
