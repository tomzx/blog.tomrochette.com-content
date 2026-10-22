---
title: SoL-Pi
created: 2026-10-13
updated: 2026-10-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, context-compression, harness-efficiency]
readability: 3
audience_notes: >
  Engineers running long autonomous research loops on the Pi harness who need the session's token spend to stay flat as the loop scales.
  Assumes you know what a coding harness is and what context compaction costs.
---

SoL-Pi is NVIDIA Research's MIT-licensed extension for the Pi coding harness that packages four context-efficiency mechanisms from scaled auto-research loops: Action Fusion, ObservationPack paged recall, an evidence-preserving reducer with verbatim-quote verification, and online context compaction.

**Its argument is that harness efficiency is a scaling problem: the mechanisms exist because the team ran auto-research loops long enough to watch token cost grow with loop length, and each one attacks a measured waste site rather than the context window in general.**

## What it is

A standalone TypeScript extension published by NV Labs (with the accompanying paper, arXiv 2609.20519) that installs beside an unmodified Pi harness.
Action Fusion collapses repeated tool sequences into single replayable actions; ObservationPack pages old tool output out of the live window into recallable chunks; the reducer compresses history while preserving verbatim quotes that downstream verification can check; and online compaction rewrites the working context mid-loop instead of at overflow.
The project page reports the efficiency results from the paper's auto-research benchmarks, and the harness keeps running ordinary Pi sessions when the extension is off.

## Status

Young and active: 3,479 stars as of 2026-10-18, 291 forks and 83 open issues as of 2026-10-22, created 2026-09-02 and pushed 2026-10-22, MIT licensed, with work continuing toward a Pi v1 baseline.
On 2026-10-14 the repository gained an official SoL-Pi skill packaging a Claude Code and Codex hand-off, with a News section of visual examples; it hands the ideas to other agents' sessions rather than porting the mechanisms off Pi.
**The attention record is thin for the star count: three small Hacker News posts between September and October 2026 (3, 2, and 2 points), so the stars ride the NV Labs name and the awesome-list circuit rather than debate.**
It extends unmodified Pi rather than forking it, which distinguishes it from the rejected third-Pi-derivative family in the harnesses category.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=NVlabs/SoL-Pi&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=NVlabs/SoL-Pi&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=NVlabs/SoL-Pi&type=date&legend=top-left" />
</picture>

## Strengths

- The mechanisms target measured waste sites (repeated actions, cold tool output, lossy summaries, overflow-time compaction), so each has a reason to exist independent of the paper.
- Verbatim-quote verification on the reducer is the right candor mechanism: compression that claims to preserve evidence can be checked against the quotes it kept.
- It extends Pi without forking it, so Pi upstream improvements keep flowing to its users.
- NVIDIA Research provenance with a paper, a project page, and reproducible benchmark claims.
- MIT and standalone, so the mechanisms are readable as a design menu even for teams on other harnesses.

## Cautions

- Pi-only: every mechanism is implemented against one harness, so teams elsewhere get ideas, not code.
- Young (one month at verification) with 78 open issues already, so the extension surface is still settling.
- The efficiency claims come from the authors' own auto-research benchmarks, reproduced by nobody independent yet, and the HN footprint is three small posts.
- Compaction and paging change what the model sees, so behavior differences are possible even when token counts improve.
- The paper's loops are research workflows; ordinary feature work may never hit the loop lengths where the wins appear.

## Pricing

Free and open source under MIT.
No hosted tier and no paid plan; the cost is the Pi harness you already run.

## Compared to

- [LLMLingua](../llmlingua/index.md): Microsoft's prompt-compression line compresses text for any LLM call; SoL-Pi's mechanisms are structural (fusion, paging, verified reduction) and live inside one harness's loop.
- [Headroom](../headroom/index.md): the receipt-backed compression layer for tool output in general; SoL-Pi is narrower (Pi only) but adds the verified-reducer idea Headroom lacks.
- [qmd](../qmd/index.md): the session-search tool that answers from archives after the fact; SoL-Pi keeps the live window small during the loop instead.

## Bottom line

**Recommended for Pi users running long autonomous loops who want token cost flat in loop length without losing verifiable evidence.**
Not for other harnesses (port the ideas instead), or for teams needing independently reproduced efficiency numbers before adopting a month-old extension.

## Changes

- 2026-10-13 - Created.
- 2026-10-13 - Corrected the chart markup: the light-scheme source and the img fallback now point at the un-themed chart URL, matching the section convention (only the dark source carries the theme parameter).
- 2026-10-18 - Recorded the official SoL-Pi skill for Claude Code and Codex hand-off (added 2026-10-14 with the News section of visual examples) and refreshed the activity figures.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [LLMLingua](../llmlingua/index.md) - the harness-agnostic compression line
- [Headroom](../headroom/index.md) - the receipt-backed tool-output compressor
- [qmd](../qmd/index.md) - the session-archive search counterpart
- [Pi](../../harnesses/pi/index.md) - the harness this extension builds on

## References

- https://github.com/NVlabs/SoL-Pi - repository, MIT license, stars, forks, push activity, and the four-mechanism structure as of 2026-10-18
- https://arxiv.org/abs/2609.20519 - the paper grounding the four mechanisms and the auto-research benchmark claims
- https://nvlabs.github.io/SoL-Pi/ - the NVIDIA project page with the reported efficiency results
- https://github.com/earendil-works/pi - the Pi harness SoL-Pi extends without forking
- https://news.ycombinator.com/ - Algolia search returned three small SoL-Pi posts (3, 2, and 2 points, September to October 2026), the recorded thin community footprint
