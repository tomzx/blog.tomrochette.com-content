---
title: AutoSci
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, research-wiki, memory, multi-harness, open-source]
readability: 3
audience_notes: >
  Engineers comparing full-lifecycle research agents and looking for ones that run on their own harness, including OpenCode.
  Assumes you know what a research wiki and an MCP server are.
---

AutoSci is a memory-centric research agent that runs the full scientific lifecycle (reading, thinking, experimenting, writing, evolving) around a linked research wiki whose memory persists across projects, shipped as skills on Claude Code with official Codex and OpenCode preview branches.

**It is the idea-to-paper sub-family's first member shipping an OpenCode adaptation and the first built around a compounding cross-project memory (SciMem) rather than a per-run pipeline, which makes it the natural comparison point for Kapso's campaign hub and the category's OpenCode-native research platform.**

## What it is

A bilingual English-and-Chinese skills-and-Python platform (github.com/skyllwt/AutoSci, MIT, internal beta) described in the May 2026 paper "AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle" (arXiv 2605.31468, 19 listed authors led by Weitong Qian).
Four modules carry the loop: SciMem (schema-governed research memory splitting long-term knowledge from project memory), SciFlow, SciDAG, and SciEvolve.
The main branch is the stable Claude Code version; autosci-codex and autosci-opencode are official preview adaptations, and the paper's full system is frozen on the paper branch (tag arxiv-v1).
The OpenCode build turns papers and notes into a linked wiki, with an llm-review MCP server for writing review and confirmation gates before destructive actions, experiment execution, and external communication.
The README traces the project to an earlier OmegaWiki prototype and invokes Karpathy's LLM-wiki vision.

## Status

Active and beta: 1,698 stars, 214 forks, created 2026-04-09, last pushed 2026-10-02, as of 2026-10-11.
No GitHub releases and no relevant Hacker News threads surfaced this run; the README calls the project an internal beta shaped by community feedback.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=skyllwt/AutoSci&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=skyllwt/AutoSci&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=skyllwt/AutoSci&type=date&legend=top-left" />
</picture>

## Strengths

- Memory that compounds across projects is the design difference: SciMem's long-term knowledge memory outlives any single run, the same bet Kapso makes with its knowledge hub.
- The only idea-to-paper member shipping an OpenCode adaptation, alongside the stable Claude Code build and a Codex preview.
- Confirmation gates are explicit: destructive actions, experiment execution, and external communication hold for the human.
- The paper is public with the full system frozen as a tag, so the claims stay checkable against the exact code that produced them.

## Cautions

- Internal beta by the README's own badge: expect churn between the branches, and the OpenCode preview is the thinnest of the three.
- The writing reviewer is an LLM (llm-review over MCP), so quality gates inherit the model's judgment rather than any external oracle.
- Daily arXiv ingestion is recommendation-only with no unattended writeback, a boundary the OpenCode notes restate.
- No releases, no independent evaluation, and a Hacker News footprint of zero for this run's search; 1,698 stars arrived without visible technical discussion.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your own model access and optional retrieval APIs (the OpenCode notes name Semantic Scholar).

## Compared to

- [Kapso](../kapso/index.md): the other memory-across-runs member; Kapso prices lessons with evidence against evaluators, AutoSci governs a wiki with schemas and an LLM reviewer.
- [AutoResearchClaw](../autoresearchclaw/index.md): the stage-pipeline rival with citation verification; AutoSci trades the stage count for the persistent wiki and multi-harness builds.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the keep-or-revert loop AutoSci's evolve module echoes at project scale rather than single-script scale.

## Bottom line

**Recommended for engineers who want the full lifecycle on their own harness, OpenCode included, with memory that survives the project, and for readers tracking whether wiki-centric memory beats per-run pipelines.**
Not for anyone needing a stable release: all three builds are beta, and the OpenCode preview is newest.

## Changes

- 2026-10-11 - Created.

## See also

- [Kapso](../kapso/index.md) - the other cross-project memory design in the category
- [AutoResearchClaw](../autoresearchclaw/index.md) - the stage-pipeline idea-to-paper rival
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the keep-or-revert loop at single-run scale
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/skyllwt/AutoSci - repository, MIT license, 1,698 stars, last push 2026-10-02 (as of 2026-10-11)
- https://raw.githubusercontent.com/skyllwt/AutoSci/main/README.md - branch layout, SciMem/SciFlow/SciDAG/SciEvolve, internal-beta status, OmegaWiki origin, paper link (fetched 200, 2026-10-11)
- https://arxiv.org/abs/2605.31468 - the paper: authors and the four-module memory-centric design (fetched 200 via the arXiv API, 2026-10-11)
- https://raw.githubusercontent.com/skyllwt/AutoSci/autosci-opencode/README.md - the OpenCode build: wiki, llm-review MCP, confirmation gates, boundaries (fetched 200, 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=AutoSci - the search returning no threads for this project (fetched 200, 2026-10-11)
