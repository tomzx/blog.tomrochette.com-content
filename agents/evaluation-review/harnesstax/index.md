---
title: HarnessTax
created: 2026-09-18
updated: 2026-09-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, benchmark, coding-agents]
readability: 3
audience_notes: >
  Engineers choosing between coding-agent harnesses who want an independent academic cross-check on harness cost and quality claims.
  Assumes you know what a pass rate, a token price list, and a confidence interval are.
---

HarnessTax is an academic benchmark study from UC Berkeley and the Arena team that measures how much a coding agent's harness matters by running 21 model-harness pairs across seven models and three harnesses (Claude Code, Codex CLI, and Pi) on SWE-bench Lite and Terminal-Bench 2.0.
Facts below verified as of 2026-09-20.

**HarnessTax is the independent counterweight to FrontierHarness Eval: where the vendor-run benchmark found harness choice moved cost 17.5x, this academic team finds the same model can cost up to 5x more for a success rate within a few points, and names the difference the harness tax.**

## What it is

A study by Melissa Z. Pan, Shuo Yang, Negar Arabzadeh, Wei-Lin Chiang, Ion Stoica, and Matei Zaharia of UC Berkeley and the Arena team, published free on the web with its data in a public GitHub Pages repository.
Each pair runs 30 randomly sampled tasks per benchmark, three attempts per task, scored by each benchmark's official evaluator, with 95 percent confidence intervals from 10,000 bootstrap resamples and a fixed September 1, 2026 direct-API price list.
The design crosses harnesses and models on purpose: three harnesses, seven models, a 100-agent-turn cap, and each harness's native high-effort configuration, so the harness effect can be separated from the model effect statistically rather than by holding one constant.
The authors promise a public release of profiling traces, and the repository carries no license as of 2026-09-18.

## Status

New and already the most-discussed artifact in this category's week: the study surfaced on Hacker News on 2026-09-16 and drew 229 points and 22 comments as of 2026-09-20.
The repository was created 2026-09-14 and pushed 2026-09-16, with 1 star, because the study page is the artifact and the code is just its vehicle.
**The traction here is academic credibility rather than community adoption: Ion Stoica and Matei Zaharia anchor the author list, and the thread argued the findings instead of the provenance.**

## Strengths

- Varies harness and model together across 21 pairs, then separates the harness effect with confidence intervals, the statistical version of the question FrontierHarness Eval answers by holding the model constant.
- Quantifies the tax: across shared models Claude Code costs about 2.0x Pi and 1.6x Codex on SWE-bench Lite while the average harness effect on success stays within about plus or minus 2 percent.
- The tax starts with the first model call: Claude Code's mean initial context is over 10x Pi's, from longer instructions and larger tool schemas.
- The most actionable finding is that models often do best outside their own harness, with an alternative harness achieving the highest observed success rate in 9 of 12 provider-model comparisons.

## Cautions

- Two benchmarks only, both open-source and possibly in the models' training data, a limitation the authors flag themselves.
- Three harnesses cover a small slice of the harnesses FrontierHarness Eval runs, so nothing here ranks the wider field.
- The tax framing drew the thread's sharpest pushback: heavier harnesses carry security and permission machinery (sandboxing, approval classifiers) that a four-tool harness omits, so cost parity is not risk parity.
- The profiling traces are promised but not published, and the repository has no license.

## Pricing

Not applicable; the study is free to read, and reproducing its matrix costs whatever your models' tokens cost against the price list the authors fixed on September 1, 2026.

## Compared to

- [FrontierHarness Eval](../frontierharness-eval/index.md): the same harness-cost question with the opposite design and publisher; HarnessTax is academic, crosses harness with model, and scores benchmark-native tasks, FrontierHarness is vendor-run, holds the model constant, and runs custom tasks, and the overlap in their conclusions (Claude Code as the expensive default) is the signal worth trusting.
- SWE-bench Lite and Terminal-Bench 2.0: the ground benchmarks it varies harnesses on; used normally they confound harness with model, which is exactly the confound HarnessTax prices rather than removes.
- [deepeval](../deepeval/index.md): a CI framework for gating your own application's outputs, a different object than a public study of third-party harnesses.

## Bottom line

**Recommended as the independent cross-check on any harness-cost claim, including FrontierHarness Eval's, and as evidence that a provider's default pairing is not automatically the optimal one.**
Not as a harness shopping leaderboard, since three harnesses and two contamination-prone benchmarks bound what it can rank.

## Changes

- 2026-09-18 - Created from the entrant-resolution run after the 217-point Hacker News thread.

## See also

- [FrontierHarness Eval](../frontierharness-eval/index.md) - the vendor-run benchmark asking the same question with the opposite design
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the capability view of the harnesses this study prices
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map of harnesses the study samples from
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins

## References

- https://harnesstax.github.io/ - the study, its findings, and its methodology
- https://github.com/HarnessTax/HarnessTax.github.io - the public repository holding the site and the study data
- https://hn.algolia.com/api/v1/items/49733726 - the 229-point launch thread, including the security-framing criticism
- https://www.swebench.com/lite - the first ground benchmark
- https://arxiv.org/abs/2601.11868 - Terminal-Bench, the second ground benchmark
