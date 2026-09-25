---
showArticleList: false
title: Evaluation and review
created: 2026-09-24
visible: true
status: in progress
tags: [agents, evaluation-review]
readability: 3
---

Where quality control lives in the agent workflow: CI gates, dashboards, machine review, human annotation, and the academic studies that benchmark the harnesses themselves.

- [deepeval](deepeval/index.md) - the pytest-style eval framework with roughly fifty judge metrics that gates merges in CI.
- [FrontierHarness Eval](frontierharness-eval/index.md) - the public benchmark that held the model constant and varied nine harnesses in twelve configurations, cost spread 17.5x, vendor-run caveat attached.
- [HarnessTax](harnesstax/index.md) - the UC Berkeley study that held seven models constant across three harnesses on SWE-bench Lite and Terminal-Bench, finding harness swaps cost up to 5x while success barely moves.
- [Langfuse](langfuse/index.md) - the MIT-core tracing and eval platform, 35.0k stars, inside ClickHouse since January with the proprietary ee/ split as the caution.
- [Phoenix](phoenix/index.md) - Arize's OTel-native observability and eval platform, self-hostable under an Elastic license.
- [Plannotator](plannotator/index.md) - the local review surface that turns your annotations on agent plans and diffs into the agent's next instruction.
- [Workshop](workshop/index.md) - Raindrop's local debugger where the coding agent reads traces, writes evals, and fixes what fails.

Its members are compared on shared rows in the [Evaluation and Review Feature Matrix](evaluation-review-feature-matrix/index.md).

## Changes

- 2026-08-30 - Added deepeval.
- 2026-08-30 - Added Phoenix.
- 2026-08-30 - Added Plannotator.
- 2026-08-30 - Added Workshop.
- 2026-09-05 - Added FrontierHarness Eval.
- 2026-09-16 - Added Langfuse.
- 2026-09-18 - Added HarnessTax.
