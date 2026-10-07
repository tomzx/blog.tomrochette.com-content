---
title: GPT Researcher
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, deep-research, open-source]
readability: 3
audience_notes: >
  Engineers choosing a deep-research agent to run themselves or cite as the open baseline.
  Assumes you know what a retrieval-augmented research loop is.
---

GPT Researcher is the Apache-2.0 open-source research agent that plans a question into sub-questions, searches the web or your own documents in parallel, filters the passages, and writes a cited report, on any LLM provider.

**It is the canonical open deep-research agent this category predates itself on: running since 2023, cited in more than 150 academic papers as the baseline to beat, and still shipping, now with a Jev-class context filter in its default pipeline.**

## What it is

A Python package (pip install gpt-researcher), a REST API stack, and a Docker image by Assaf Elovic, installable from PyPI or Docker Hub (29,933 stars, pushed 2026-10-01, as of 2026-10-07).
The loop runs in four stages: plan the sub-questions, search each in parallel across 20-plus sources per report, keep only passages that answer the question, and write the cited report in Markdown, PDF, or Word.
Around the core sit a recursive deep-research mode that branches until a topic is exhausted, LangGraph and AG2 multi-agent teams that plan, research, review, and publish together, MCP servers as sources, and your own PDFs, Word files, spreadsheets, and Markdown joined with the web.
Since v3.7.0 the context filter runs Jev by default with a local keyword-ranking fallback, so no embeddings provider or key is required.

## Status

Active: created 2023-05-12, 29,933 stars, release v3.7.0 published 2026-09-26, PyPI package at 0.16.1, as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=assafelovic/gpt-researcher&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=assafelovic/gpt-researcher&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=assafelovic/gpt-researcher&type=date&legend=top-left" />
</picture>

The docs claim citation in more than 150 research papers, including DeepResearchGym's evaluation sandbox and ACL 2025's Dolphin, and that claim is checkable on Google Scholar.
Its own Hacker News footprint is small (the 2024 Show HN drew 4 points), so the credibility case is the academic-citation record rather than forum traction.

## Strengths

- The de facto open baseline: when a paper evaluates deep-research agents, this is usually one of the systems on the table, which makes its behavior comparable across studies.
- Provider-agnostic by design, working with any LLM from OpenAI and Anthropic to local models through its retriever and planner abstractions.
- The plan-search-filter-write decomposition is legible and hackable, which is why it keeps being forked into domain research agents.
- The default Jev context filter removes the embeddings-service dependency most RAG loops carry.

## Cautions

- Output is prose with citations and no machine judge, so the human stays the verifier, the same caveat as every product-tier rival.
- The 150-paper citation claim is self-compiled; the papers mostly use it as a comparison point, not a validation.
- pip package versioning (0.16.1) has drifted from GitHub release tagging (v3.7.0), which confuses upgrade paths.
- Search quality still depends on whatever retrievers you configure, and the free search tiers it can fall back to are rate-limited.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are your LLM tokens and any paid search-provider keys you attach.

## Compared to

- [OpenAI Deep Research](../openai-deep-research/index.md): the closed product tier with zero setup; choose GPT Researcher for control, self-hosting, and your own documents in the loop.
- [Local Deep Research](../local-deep-research/index.md): the local-first privacy sibling with an encrypted document library; GPT Researcher is the older, more-cited generalist, LDR the privacy-focused specialist.
- [OpenResearch](../openresearch/index.md): the workspace that turns coding agents into researchers with experiment trees; GPT Researcher answers questions with cited reports rather than executing experiments.

## Bottom line

**Recommended as the default open baseline: the agent you run when you want a cited report under your own keys, and the one you compare fancier loops against.**
Not for machine-verified conclusions, and not for anyone who needs a vendor SLA behind the research run.

## Changes

- 2026-10-07 - Created.

## See also

- [OpenAI Deep Research](../openai-deep-research/index.md) - the productized counterpart this project has tracked since 2023
- [Local Deep Research](../local-deep-research/index.md) - the local-first open sibling accepted into the category the same day
- [OpenResearch](../openresearch/index.md) - the other open harness, experiment trees instead of reports
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [Jev](../../hybrid-execution/jev/index.md) - the decision-model family whose context filter now sits in GPT Researcher's default pipeline

## References

- https://github.com/assafelovic/gpt-researcher - repository, Apache-2.0 license, architecture, and the plan-and-solve and RAG paper lineage (fetched 200, 2026-10-07)
- https://api.github.com/repos/assafelovic/gpt-researcher - stars, created date, push date, and license for the as-of status (fetched 200, 2026-10-07)
- https://docs.gptr.dev - the four-stage loop, deep-research mode, multi-agent teams, MCP sources, the Jev default filter, and the 150-paper citation claim (fetched 200, 2026-10-07)
- https://pypi.org/pypi/gpt-researcher/json - the published package version 0.16.1 and Python requirement (fetched 200, 2026-10-07)
- https://api.github.com/repos/assafelovic/gpt-researcher/releases - the v3.7.0 release of 2026-09-26 and the cadence before it (fetched 200, 2026-10-07)
- https://hn.algolia.com/api/v1/items/41234914 - the August 2024 Show HN thread, 4 points, grounding the small-HN-footprint observation (fetched 200, 2026-10-07)
