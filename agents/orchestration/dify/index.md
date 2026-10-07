---
title: Dify
created: 2026-09-29
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, workflow, low-code]
readability: 3
audience_notes: >
  Teams picking a self-hostable platform for agentic business apps who need the license and cost picture.
  Assumes you know what a visual LLM workflow builder is and why the Flowise shutdown matters to the genre.
---

Dify is LangGenius's open-source platform for building agentic workflows and RAG pipelines on a visual collaborative workspace, deployable on cloud, VPC, or self-hosted, and at 157,786 stars it is the largest repository in this category (GitHub API, as of 2026-10-04).

**Scale is Dify's moat: it is the surviving giant of the visual LLM-workflow genre, the same genre whose weakest incumbent, Flowise, just archived itself.**

## What it is

A visual workflow studio plus knowledge pipeline, agent strategies, and a marketplace of tools and models, shipped as a TypeScript and Python application.
Deployment is a choice of Dify Cloud (hosted SaaS), Enterprise (private deployment), or Community Edition (self-hosted with Docker).
The license is a modified Apache 2.0: commercial use is allowed, but multi-tenant SaaS and some other conditions require a commercial license from LangGenius, which is why GitHub reports NOASSERTION.
The repo sits at 157,786 stars with 24,900 forks, created 2023-04-12 (GitHub API, as of 2026-10-04).

## Status

Active: last push 2026-10-05, latest release 1.17.1 on 2026-09-10 (GitHub API, as of 2026-10-05).
Its 2024 HN launch drew 185 points, and the community has kept growing since.
The category context is the risk: Flowise's shutdown discussion argued that capable coding agents are eroding the rigid low-code workflow approach, and that argument applies to every member of the genre, Dify included.

[![Star History Chart](https://api.star-history.com/chart?repos=langgenius/dify&type=date&legend=top-left)](https://www.star-history.com/?repos=langgenius%2Fdify&type=date&legend=top-left)

## Strengths

- **The community is the deepest in the genre**: 157k stars and 24.8k forks give it a durability none of its visual-workflow rivals can match.
- Breadth under one roof: agentic workflows, RAG pipelines, knowledge bases, a marketplace, and enterprise deployment options.
- Self-hosting with Docker is first-class, and the cloud tier exists for teams that do not want to operate it.
- Multi-agent coordination is inside the product (agent strategies in workflows), so it overlaps this category's subject matter without being a coding-agent tool.

## Cautions

- **The license is not plain Apache**: multi-tenant SaaS use needs a commercial license, so check the conditions before building a product on it.
- It is a business-app platform, not a coding-agent orchestrator; nothing here manages worktrees, sessions, or parallel coding agents.
- Cloud pricing moved to annual billing with message-credit metering, which is a cost model that punishes experimentation.
- The Flowise shutdown argument, that reasoning models plus coding agents beat rigid visual workflows as tasks get complex, is the genre's standing strategic risk.

## Pricing

Community Edition is free and self-hosted (open source under the modified Apache 2.0).
Dify Cloud bills annually per workspace: Professional at $590 per workspace per year (5,000 message credits per month) and Team at $1,590 per workspace per year (10,000 message credits per month).
Enterprise is custom private deployment.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-29 | Professional (Cloud) | observed at $590 per workspace per year, annual billing | https://dify.ai/pricing |
| 2026-09-29 | Team (Cloud) | observed at $1590 per workspace per year, annual billing | https://dify.ai/pricing |

## Compared to

- [Sim](../sim/index.md): the younger Apache-2.0 rival; Dify wins on ecosystem depth and enterprise options, Sim on license cleanliness and building modes.
- [Flowise](../flowise/index.md): the archived predecessor in the genre; Dify is the migration target its self-hosters need.
- [AutoGPT](../autogpt/index.md): the other platform member of this category; AutoGPT sells autonomous workflows, Dify sells a broader app-building workspace.

## Bottom line

Recommended for teams building conversational and agentic business applications with RAG on a self-hosted or cloud platform, at scales where community depth matters.
Not for coordinating parallel coding agents, and not for multi-tenant SaaS builders who cannot accept the commercial-license conditions.

## Changes

- 2026-09-29 - Created when the deferred framework-tier pile from the 2026-09-27 triage resolved.
- 2026-10-07 - Added the langgenius/dify star history chart to the Status section.

## See also

- [Flowise](../flowise/index.md) - the archived genre-mate whose shutdown names the category's risk
- [Sim](../sim/index.md) - the Apache-2.0 challenger for the same visual-workflow builders
- [AutoGPT](../autogpt/index.md) - the other workflow-platform member of this category
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/langgenius/dify - GitHub API (200): 157,458 stars, 24,813 forks, pushed 2026-09-29, created 2023-04-12 (as of 2026-09-29)
- https://dify.ai - official site (200): products, deployment options
- https://dify.ai/pricing - pricing page (200): Professional $590 and Team $1590 per workspace per year, annual billing
- https://docs.dify.ai - official documentation, live (200)
- https://raw.githubusercontent.com/langgenius/dify/main/LICENSE - license text (200): modified Apache 2.0 with multi-tenant commercial conditions
- https://api.github.com/repos/langgenius/dify/releases/latest - releases API (200): 1.17.1, published 2026-09-10
- https://hn.algolia.com/api/v1/items/40121318 - launch thread (200): 185 points, 38 comments, 2024-04-22
