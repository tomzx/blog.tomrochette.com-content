---
title: GEPA
created: 2026-10-13
updated: 2026-10-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, prompt-optimization, meta-learning]
readability: 3
audience_notes: >
  Engineers who maintain prompt-driven agents and want the prompts improved mechanically against a metric instead of by hand.
  Assumes you know what an eval metric is and can run a Python pipeline.
---

GEPA is an MIT-licensed reflective prompt optimizer from the Databricks research lineage that evolves any text parameter (prompts, code, agent architectures, configs) against any metric using genetic-Pareto search over language-model feedback.

**Its place in the skills category is the factory floor: where the other columns package, gate, and rank skill markdown, GEPA is the optimizer that can write and rewrite that markdown mechanically, its own documentation recording coding-agent skills learned automatically.**

## What it is

A Python library and CLI built on the GEPA paper (arXiv 2507.19457, July 2025), which showed reflective prompt evolution beating grouped reinforcement learning on quality and cost for LLM tasks.
You point it at seed prompts, an evaluator (any metric you can call), and a budget; it proposes mutations, runs candidates, keeps the Pareto frontier, and iterates.
It optimizes "any text parameter", so the same loop covers system prompts, DSPy programs, agent instructions, and skill files, and the project documents coding-agent skills it learned automatically.
Distribution is PyPI (`pip install gepa`, v0.1.4, release-tagged July 2026) with a documented site and worked examples.

## Status

Active with an established research record: 6,973 stars and 576 forks as of 2026-10-13, 137 open issues as of 2026-10-22, created 2025-08-05, pushed 2026-10-21, PyPI at 0.1.4.
The launch reached a 92-point Hacker News thread in July 2025, the paper was accepted to ICLR 2026 as an oral (v2 revised 2026-02-14), and the adoption trail is documented beyond Databricks' own engineering blog: the docs site's roster names Shopify, Google, Microsoft, OpenAI, Dropbox, Pydantic, and Comet ML, and GEPA ships built into DSPy.
**The contested part is the evidence: a "Contra DSPy and GEPA" thread and the DSPy community's methodological argument over GEPA's comparison baselines are the standing critical sources, so the headline claims deserve a re-run on your own metric before adoption.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=gepa-ai/gepa&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=gepa-ai/gepa&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=gepa-ai/gepa&type=date&legend=top-left" />
</picture>

## Strengths

- Optimizer generality: one loop over any metric and any text artifact, which makes it the missing mechanical layer under every skill and prompt column in this category.
- The reflective step uses model reasoning about failures, not blind mutation, so candidate quality stays high and API spend stays bounded.
- Pareto-frontier selection keeps candidates that win on different inputs instead of collapsing to one average prompt.
- A documented adoption trail: the paper, the Databricks production claim, and an active issue tracker give it a verifiable history.
- MIT with a small API surface; you can read the whole search loop in an afternoon.

## Cautions

- The comparison-methodology dispute (the Contra thread) is unresolved; GEPA's reported wins over reinforcement learning and DSPy depend on baseline choices its critics dispute.
- Optimizer runs are expensive in evaluator calls: the budget is your model bill, and a bad metric silently optimizes toward the wrong thing.
- Version 0.1.x means the API moves; pin or expect churn.
- 137 open issues against one org's maintenance bandwidth, and the release cadence (one tag since July 2026) lags the default branch.
- It edits text artifacts directly, so run it against versioned files or it will optimize in place.

## Pricing

Free and open source under MIT.
There is no hosted tier; optimizer runs consume your own model API budget, which is the whole cost.

## Compared to

- [SkillOpt](../skillopt/index.md): Microsoft's skill-specific optimizer; GEPA is the general text-parameter optimizer SkillOpt's job descends from, with more surfaces and less skill-file structure.
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md): the format whose files GEPA can optimize; use the format for packaging, GEPA when the content needs to improve against a metric.
- [Agent Skills open standard](../agent-skills-open-standard/index.md): the interchange spec; GEPA writes artifacts that still need to conform to it before agents load them.

## Bottom line

**Recommended for teams with a trustworthy metric and prompt assets that matter enough to optimize mechanically.**
Not for anyone without an evaluator (GEPA amplifies whatever the metric measures), or for skill distribution problems, which remain the other columns' job.

## Changes

- 2026-10-13 - Created.
- 2026-10-13 - Fixed the star-history chart markup from the creation run: the light source and the img fallback had carried the dark theme parameter.
- 2026-10-13 - Refreshed the volatile numbers (6,973 stars, 576 forks).
- 2026-10-22 - Rotation re-verification: recorded the paper's ICLR 2026 oral acceptance (v2, 2026-02-14) and the docs site's vendor adoption roster (Shopify, Google, Microsoft, OpenAI, Dropbox, Pydantic, Comet ML, plus the built-into-DSPy integration), and refreshed the volatile numbers (137 open issues, pushed 2026-10-21, PyPI still 0.1.4).

## See also

- [Skills Feature Matrix](../skills-feature-matrix/index.md) - the category comparison this note joins
- [SkillOpt](../skillopt/index.md) - the skill-specific optimizer this generalizer sits beside
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the format GEPA-written skills must land in
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the interchange spec for optimized artifacts
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://github.com/gepa-ai/gepa - repository, MIT license, stars, push activity, and the any-text-parameter scope as of 2026-10-22
- https://arxiv.org/abs/2507.19457 - the GEPA paper grounding the reflective-prompt-evolution and Pareto-selection claims, accepted to ICLR 2026 as an oral (v2 revised 2026-02-14)
- https://gepa-ai.github.io/gepa/ - the documented API, examples, and the auto-learned coding-agent skills claim
- https://pypi.org/project/gepa/ - the PyPI distribution, version 0.1.4 (2026-07-15), MIT
- https://news.ycombinator.com/item?id=44744331 - the 92-point July 2025 launch thread
- https://news.ycombinator.com/item?id=46331945 - the Contra DSPy and GEPA thread, the standing critical source on the comparison methodology
