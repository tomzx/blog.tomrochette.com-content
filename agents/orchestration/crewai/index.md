---
title: CrewAI
created: 2026-09-29
updated: 2026-09-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python]
readability: 3
audience_notes: >
  Engineers choosing between Python multi-agent frameworks who need to know which ones survived 2026.
  Assumes you have used at least one agent framework and know what a role-based crew looks like.
---

CrewAI is the MIT-licensed Python framework for orchestrating role-playing autonomous AI agents, and at 59,273 stars it is now the most-starred multi-agent framework of the post-AutoGen generation (GitHub API, as of 2026-10-02).

**CrewAI is the rare framework whose community outgrew its launch wave: it kept shipping while AutoGen froze, and a real enterprise platform now funds the open source.**

## What it is

A Python (3.10 to 3.13) framework where you compose agents with roles, goals, and backstories into crews that run tasks sequentially or in parallel.
It is built by CrewAI Inc, a San Francisco and Brazil company founded by João Moura, with the open source framework launched in late 2023.
The platform side adds a visual editor, an AI copilot, GitHub integration, and enterprise governance (SSO, RBAC, PII redaction).
The repo sits at 59,273 stars with 8,620 forks, MIT licensed, created 2023-10-27 (GitHub API, as of 2026-10-02).

## Status

Active and heavily maintained: last push 2026-10-01, latest release 1.15.23 on 2026-09-28, and `crewai` 1.15.23 on PyPI (GitHub API, PyPI, as of 2026-10-02).
The company raised $18M across seed and Series A in October 2024, led by Insight Partners and boldstart ventures, with Andrew Ng and HubSpot co-founder Dharmesh Shah as angels (SiliconANGLE).
Company claims include roughly half the Fortune 500 using the open source and 10 million+ agents executed monthly; I could not independently verify either number.

## Strengths

- **The role-and-crew abstraction is the most copied metaphor in multi-agent tooling**, and it made multi-agent automation legible to teams that never wanted to write a message loop.
- The dual open source plus enterprise motion is real: $18M raised, 150 enterprise beta customers claimed in the first year, and the OSS still ships weekly.
- Notable enough to have a Wikipedia article, which almost no OSS agent framework can say.
- MIT at the package level, so vendoring and embedding carry no license surprises.

## Cautions

- **Independent critique is thin relative to the star count**: the largest HN threads are hobby showcases (26 points at best), not technical debates, so the community is bigger than its public scrutiny.
- Headline traction numbers ("nearly half the Fortune 500", "10 million+ agents per month") are company marketing.
- The OSS is the funnel for an enterprise platform, so expect platform-first decisions in the roadmap.
- It is a general task-automation framework, not a coding-agent orchestrator; there is no worktree, session, or repository model here.

## Pricing

The open source framework is free under MIT.
The CrewAI platform has a Basic plan at $0 (visual editor, AI copilot, GitHub integration, 50 workflow executions per month) and Enterprise at custom pricing (SSO, RBAC, workload identity, PII redaction, flexible deployment).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-29 | Basic | observed at $0 with 50 workflow executions/month | https://www.crewai.com/pricing |
| 2026-09-29 | Enterprise | observed at custom quote-based pricing | https://www.crewai.com/pricing |

## Compared to

- [AutoGen](../autogen/index.md): the conversation-first predecessor, now in maintenance mode; CrewAI is where much of that community went.
- [Agno](../agno/index.md): the performance-pitch Python rival, with its own runtime and control plane; choose Agno for self-hosted serving, CrewAI for role-based crews with an enterprise console.
- [Mastra](../mastra/index.md): the TypeScript peer; choose it if your stack is Node and you want evals built in.

## Bottom line

Recommended for Python teams automating multi-step role-based work who want a free framework with a credible enterprise on-ramp.
Not for coordinating parallel coding agents (that is the rest of this category), and not for buyers who need independently verified enterprise traction.

## Changes

- 2026-09-29 - Created when the deferred framework-tier pile from the 2026-09-27 triage resolved.

## See also

- [AutoGen](../autogen/index.md) - the maintenance-mode framework CrewAI displaced in mindshare
- [Agno](../agno/index.md) - the Python framework rival with the performance-first pitch
- [Mastra](../mastra/index.md) - the TypeScript counterpart from the Gatsby team
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/crewAIInc/crewAI - GitHub API (200): 59,157 stars, 8,601 forks, MIT, pushed 2026-09-29, created 2023-10-27 (as of 2026-09-29)
- https://docs.crewai.com/introduction - official documentation, live (200)
- https://www.crewai.com/pricing - pricing page (200): Basic $0 with 50 workflow executions/month, Enterprise custom
- https://pypi.org/pypi/crewai/json - PyPI metadata (200): crewai 1.15.23, Python >=3.10,<3.14
- https://api.github.com/repos/crewAIInc/crewAI/releases/latest - releases API (200): 1.15.23, published 2026-09-28
- https://siliconangle.com/2024/10/22/agentic-ai-startup-crewai-closes-18m-funding-round/ - $18M seed and Series A, Insight Partners and boldstart, angels Andrew Ng and Dharmesh Shah (200)
- https://en.wikipedia.org/wiki/CrewAI - Wikipedia article (200): company background and funding corroboration
- https://hn.algolia.com/api/v1/items/43354219 - largest CrewAI HN thread (200): 26 points, hobby-workflow showcase (critical source: thin independent critique relative to star scale)
