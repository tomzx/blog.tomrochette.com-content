---
title: MetaGPT
created: 2026-09-27
updated: 2026-10-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python, software-engineering]
readability: 3
audience_notes: >
  Engineers who lived through the 2023 multi-agent wave and want to know what became of its most-cited framework.
  Assumes you know what an agent harness is and have seen one role-play framework before.
---

MetaGPT is the MIT-licensed Python framework from FoundationAgents that pitched the "software company as multi-agent system": one line of requirements in, and a cast of product managers, architects, project managers, and engineers outputs user stories, competitive analysis, data structures, APIs, and code along a standardized operating procedure.

**MetaGPT won the 2023 multi-agent hype cycle on a metaphor rather than on output quality, and the organization's own behavior since, a frozen main repo with the energy moved to OpenManus, is the market's verdict on that trade.**

## What it is

A framework where roles collaborate through standardized operating procedures, which the original paper (arXiv 2308.00352, fifteen authors including Chenglin Wu and Jürgen Schmidhuber, submitted 2023-08-01) argued reduces error cascades versus free-form chat chains.
The README's promise is concrete: it takes a one line requirement and produces documents, diagrams, and a working codebase assembled by its internal software company.
It runs as a Python library and CLI, and its paper became one of the field's most cited artifacts, with an ICLR 2024 oral presentation per the HN submission record.
The commercial continuation is MGX (MetaGPT X, mgx.dev), launched February 2025 as "the world's first AI agent development team" per the README news log.
The framework itself is free software; MGX is the hosted product.

## Status

Dormant in everything but stars: the repo shows 70,731 stars, about 9k forks, and a last push of 2026-01-21, roughly eight and a half months before this check (GitHub API, as of 2026-10-04).
The latest release is v0.8.2, published 2025-03-09, eighteen months old at writing.
The README news section stops at March 2025, when MGX topped Product Hunt, and nothing newer was added since.
The FoundationAgents org is not dead: OpenManus, its open reproduction of Manus, holds 58,455 stars with a push on 2026-09-30, and smaller research repos (AOrchestra, ReCode, AutoEnv) keep landing.
I read that pattern as the team building a next generation while leaving the framework that made them famous in maintenance.

## Strengths

- **The role-and-SOP metaphor is the best demo interface the category has produced**: a software company is instantly legible to executives, which is why this repo out-cited nearly everything of its generation.
- Structured intermediate artifacts (requirements, designs, APIs) between roles are a genuinely good idea that later graph-of-work frameworks absorbed.
- The paper gave the field shared vocabulary (SOPs, role specialization, assembly-line decomposition) that survives the framework itself.
- MIT license and a Python install that still works make it low risk to resurrect for research.

## Cautions

- Eight months without a push and eighteen months without a release, so I would not start new production work here (as of 2026-09-27).
- The 2023 magic was demos: commenters on the launch thread observed the hype dissipating within months, and an Ask HN thread asking for production success stories closed with zero answers.
- The docs are partially unhealthy: docs.deepwisdom.ai served HTTP 500 on its /v2/en/ path when I fetched it on 2026-09-27, though the /main/en/ path worked.
- The star count is a museum number; most of those 70k stargazers starred a moment, not a tool they run.
- Its engineering claims never survived contact with real repositories; the framework generated impressive greenfield toys, not maintenance work.

## Pricing

The framework is free and open source under MIT.
MGX at mgx.dev is the commercial hosted product; I did not verify its pricing, so no dollars are stated here.

## Compared to

- [AutoGPT](../autogpt/index.md): the other 2023 phenomenon; AutoGPT rebuilt itself into a living platform, MetaGPT froze and cashed the metaphor out into MGX.
- [AutoGen](../autogen/index.md): the conversation-first rival from Microsoft; MetaGPT structures roles into a pipeline, AutoGen lets agents talk, and both now sit in the museum wing.
- [Claude Code](../../harnesses/claude-code/index.md): the single-agent harness that made the argument moot for coding; one good agent with a tight loop outperforms a simulated software company on real codebases.

## Bottom line

Recommended for researchers studying how multi-agent metaphors spread, and for anyone who wants the historical primary source of the 2023 wave.
Not for new production builds; pick a modern harness for solo work or an actively maintained platform for pipelines.
My disagreeable claim: OpenManus, not MetaGPT, is the real continuation of this work, and MetaGPT's lasting output is its vocabulary rather than its code.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.

## See also

- [AutoGPT](../autogpt/index.md) - the sibling 2023 phenomenon whose rebuild strategy contrasts with MetaGPT's freeze
- [AutoGen](../autogen/index.md) - the conversation-based multi-agent framework it competed with
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins
- [Claude Code](../../harnesses/claude-code/index.md) - the single-agent approach that displaced simulated teams
- [Assistant runtimes](../../assistant-runtimes/_index.md) - where hosted agent platforms live now

## References

- https://api.github.com/repos/FoundationAgents/MetaGPT - GitHub API (200): 70,637 stars, pushed 2026-01-21, MIT, Python, created 2023-06-30 (as of 2026-09-27)
- https://raw.githubusercontent.com/FoundationAgents/MetaGPT/main/README.md - roles, SOP pitch, MGX launch and Product Hunt news log (200)
- https://github.com/FoundationAgents/MetaGPT/releases - releases API (200): v0.8.2 latest, published 2025-03-09
- https://arxiv.org/abs/2308.00352 - the MetaGPT paper: authors, SOP thesis, submitted 2023-08-01 (200)
- https://docs.deepwisdom.ai/main/en/ - documentation site (200); note the /v2/en/ path returned HTTP 500 on 2026-09-27
- https://api.github.com/orgs/FoundationAgents/repos - org listing (200): OpenManus at 58,421 stars, pushed 2026-08-22
- https://hn.algolia.com/api/v1/items/37076125 - launch thread (200): 152 points, 82 comments, 2023-08-10, with hype-dissipation comments (critical source)
- https://hn.algolia.com/api/v1/search?query=metagpt&tags=story - search API (200): the zero-answer Ask HN success-stories thread and the ICLR 2024 oral submission record
- https://mgx.dev - the commercial MGX product site (200)
