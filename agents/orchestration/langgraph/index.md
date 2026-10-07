---
title: LangGraph
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agent-framework, graph-runtime, durable-execution, python, typescript]
readability: 3
audience_notes: >
  Engineers choosing a runtime for agents they will build themselves, who need to know how a framework compares to the session orchestrators around it.
  Assumes you know what an agent loop is and are comfortable writing code against a library.
---

LangGraph is LangChain's MIT-licensed, low-level orchestration runtime for building stateful agents as graphs, with durable execution, streaming, human-in-the-loop interrupts, and persistence as the core primitives.

**LangGraph is the most-installed orchestration option in this category at 4.55 million npm downloads a week, and the least orchestration-like: it hands you a state machine instead of a team, and its own documentation treats LangSmith, the commercial layer, as the place where a serious deployment ends up.**

## What it is

A Python and JavaScript library from LangChain that builds agents as graphs of steps and model calls coordinated through shared state.
The documentation's pitch is durable execution, real-time streaming, human-in-the-loop interrupts, and persistence, which is the machinery the session-oriented columns in the orchestration matrix implement for you.
The core is open source under MIT; LangChain's commercial LangSmith platform is a separate product the documentation references throughout, and I record no prices for it here.
LangGraph shows up in eight other section articles (this category's feature matrix, the Agno and LangChain notes, and the control-planes coverage among them) without having had a note of its own until now.

## Status

Active and enormous: 42,752 stars, 7,268 forks, and 100+ contributors as of 2026-10-05, with the repository created in August 2023.

[![Star History Chart](https://api.star-history.com/chart?repos=langchain-ai/langgraph&type=date&legend=top-left)](https://www.star-history.com/?repos=langchain-ai%2Flanggraph&type=date&legend=top-left)

Release 1.2.13 shipped 2026-10-05 on GitHub and PyPI alike, continuing a 1.2.x line that has run all year.
npm `@langchain/langgraph` served 4,552,953 downloads in the week ending 2026-10-04.
**For scale: that is more weekly installs than any other column in this matrix by a wide margin, and probably more than the rest of the table combined.**

## Strengths

- Distribution and ecosystem: 4.5 million installs a week means hiring, examples, and answered questions are not a problem here.
- The primitives production agents need (durable execution, interrupts, persistence) are the library's core, not plugins.
- MIT across the core, with a release train that keeps shipping.
- Practitioner validation: qodo's 83-point write-up of building a coding agent on LangGraph is the most substantive engineering discussion in this category outside Scion's launch thread.

## Cautions

- It is not an out-of-the-box coding-team runner: no worktrees, no external-CLI harness driving, no review surface, because you build the team and the matrix's session columns do the rest.
- The documentation's visible LangSmith upsell blurs the line between the free core and the commercial product exactly where procurement questions start.
- Low-level by design: expect to write and own the graph, the state schema, and the failure handling.
- 820 open issues as of 2026-10-05 against that install base is a small ratio, but the issues that matter to you may sit in the closed-source platform, not the repo.

## Pricing

The open source core is free under MIT.
LangChain sells LangSmith separately as the commercial layer for deployment, tracing, and management; I found no price table in the pages I checked this run, so I record none rather than guess.

## Compared to

- [Agno](../agno/index.md): the other Python option, with a runtime and a paid control plane attached; choose Agno for a platform you can deploy and bill against, LangGraph for raw graph control you own.
- [Mastra](../mastra/index.md): the TypeScript sibling with evals and a supported platform; choose Mastra in TypeScript stacks, LangGraph in Python ones.
- [CrewAI](../crewai/index.md): role-based crews assembled in minutes; choose CrewAI for speed of assembly, LangGraph for control over state, interrupts, and recovery.

## Bottom line

**Recommended for Python or TypeScript teams building custom multi-step agents who want durable-execution primitives under an MIT license.**
Not for engineers who want a dashboard, worktrees, and a review flow around existing coding CLIs, because that is what the rest of this category does.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the langchain-ai/langgraph star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Agno](../agno/index.md) - the Python platform alternative
- [Mastra](../mastra/index.md) - the TypeScript sibling framework
- [CrewAI](../crewai/index.md) - the assembly-speed alternative
- [LangChain](../../retrieval/langchain/index.md) - the parent project this runtime grew out of

## References

- https://api.github.com/repos/langchain-ai/langgraph - stars, forks, open issues, MIT license, and push date as of 2026-10-05
- https://docs.langchain.com/oss/python/langgraph/ - durable execution, streaming, human-in-the-loop, persistence, and the LangSmith references throughout
- https://api.github.com/repos/langchain-ai/langgraph/releases - release 1.2.13 (2026-10-05) and the cadence behind it
- https://api.npmjs.org/downloads/point/last-week/@langchain/langgraph - 4,552,953 downloads in the week ending 2026-10-04
- https://pypi.org/pypi/langgraph/json - PyPI version 1.2.13
- https://news.ycombinator.com/item?id=43468435 - qodo's "We chose LangGraph to build our coding agent" at 83 points, the practitioner discussion
