---
title: CAMEL
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python, research, role-playing]
readability: 3
audience_notes: >
  Engineers and researchers comparing multi-agent frameworks, who know the 2023
  role-playing wave from its papers and want to know which of those projects is
  still worth installing. Assumes basic Python and LLM API familiarity.
---

CAMEL is the open-source Python multi-agent framework behind the 2023 role-playing paper, now a research community hunting what it calls the scaling law of agents.

## What it is

CAMEL (Communicative Agents for "Mind" Exploration of Large Language Model Society) began as the March 2023 paper that popularized role-playing agent societies, and grew into the camel-ai community with its own framework, docs, and model zoo.
The framework is Apache-2.0, Python-first, and installable as `camel-ai` from PyPI, with Workforce-style agent societies, tool use, and simulated environments among its abstractions.
The same organization maintains OWL, the task-automation framework that GitHub's own blog named in its 2025 top-ten open-source AI projects list.
This is the fourth member of the 2023 conversational and role-play family this section carries, beside AutoGen, MetaGPT, and CrewAI, and the one with the strongest research lineage.

## Status

Active and researched: 17,817 stars, a push on 2026-10-05, and continuous PyPI releases with `camel-ai` at 0.2.90 as of 2026-10-07 (GitHub API, PyPI), on a repository created 2023-03-17.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=camel-ai/camel&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=camel-ai/camel&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=camel-ai/camel&type=date&theme=dark&legend=top-left" />
</picture>

**The footprint is academic and community-shaped rather than press-shaped: I found no CAMEL launch thread of note on Hacker News, while GitHub's blog named the org's Owl framework among the top open-source AI projects and the Eigent workforce launch (8 points, July 2025) was built on CAMEL.**
That is the opposite of the pattern in the tools columns of this category, where a launch thread is the traction proof; here the citation record (the paper, GitHub's blog, and the Trendshift badge) does that work.
A disambiguation trap worth naming: camelai.com is an unrelated natural-language analytics company, and its HN launch threads are what a naive search for "CamelAI" surfaces.

## Strengths

- The role-playing lineage's reference implementation, with the paper, the docs, and a large model zoo behind it.
- Still shipping on PyPI while its 2023 peers froze (AutoGen is in maintenance mode, MetaGPT dormant).
- OWL gives the research a product-shaped sibling for task automation.

## Cautions

- Research-first abstractions (societies, role-play, incubation) are heavier than what daily coding-agent work needs, and there is no worktree or review model.
- The 0.2.x version line has run for years, so interfaces move without a stable 1.0 contract.
- The name collides with an unrelated analytics company, which pollutes searches and star comparisons.

## Pricing

Free, open source under Apache-2.0; no paid tier found.

## Compared to

AutoGen is the other 2023 conversational framework, now frozen in maintenance mode with Microsoft pointing users at its own successor, while CAMEL kept shipping.
CrewAI inherited the role-based-crew idea and wrapped it in a funded enterprise platform; choose CrewAI for product support, CAMEL for the research line.
LangGraph is the build-your-own graph runtime when you want durable execution rather than role-play conventions.

## Bottom line

Recommended for researchers studying multi-agent behavior at scale and teams that want the role-playing lineage's original, still-maintained implementation.
Not for engineers who need a session orchestrator around external coding CLIs; every tool column in this category answers that question and CAMEL deliberately does not.

## Changes

- 2026-10-07 - Created.

## See also

- [AutoGen](../autogen/index.md) - the fellow 2023 conversational framework, now in maintenance mode, whose successor story parallels CAMEL's continuity.
- [MetaGPT](../metagpt/index.md) - the other role-play-era framework gone dormant, the counterpoint to CAMEL's continued releases.
- [CrewAI](../crewai/index.md) - the commercialized inheritor of the role-based-crew idea CAMEL's paper seeded.
- [LangGraph](../langgraph/index.md) - the graph-runtime alternative when the job is durable execution instead of agent societies.

## References

- https://github.com/camel-ai/camel - the repository, its README framing ("finding the scaling law of agents"), stars, and license.
- https://arxiv.org/abs/2303.17760 - the March 2023 role-playing paper that started the lineage.
- https://www.camel-ai.org/ - the community site and its research framing.
- https://docs.camel-ai.org - the framework documentation.
- https://pypi.org/project/camel-ai/ - the PyPI package and its current 0.2.90 version.
- https://github.blog/open-source/maintainers/from-mcp-to-multi-agents-the-top-10-open-source-ai-projects-on-github-right-now-and-why-they-matter/ - GitHub's top-ten list naming the org's Owl framework, the independent credibility signal.
