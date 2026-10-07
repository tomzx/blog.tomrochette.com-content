---
title: Jevals
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, guardrails, jev, decision-models, python]
readability: 3
audience_notes: >
  Engineers evaluating agents who find the LLM judge too slow, expensive, or inconsistent to run on
  every trace.
  Assumes you know what LLM-as-judge evals and tool-call traces are.
---

Jevals is OpenLayer's MIT-licensed Python library of agent evals and guardrails that replaces the LLM judge with typed Jev-class decision models, packing all checks for one trace into a single request costing thousandths of a cent and returning in a few hundred milliseconds.

## What it is

**The judge stops being a chat model: each check is a typed question (yes/no, choice, rubric) answered with a calibrated probability in one forward pass.**
Thirty-seven built-in evals cover agent behavior (tool choice, groundedness, scope, loop detection, goal completion), security (indirect injection, PHI and PII, secrets, jailbreaks), and the Ragas-style quality metrics.
Gates map eval answers to allow, escalate, or block policies written in Python or YAML, so the same definition scores traces offline and enforces inside the agent loop.
Backends are pluggable: Jev through TypeSafe or Vercel's gateway, Kev or Laya locally on a Mac, Eikos on one GPU, or any chat LLM emulating the format; there is an MCP server so coding agents can author, validate, and run evals.
It comes from OpenLayer (the openlayer-ai organization), is alpha, MIT, Python 3.10+, and pip-installable.

## Status

**Sixteen days old and already carrying more independent evidence than most month-old tools ever get.**
102 stars and 9 forks as of 2026-10-06 (repository created 2026-09-20, last push 2026-10-01), PyPI 0.1.4 published 2026-09-20, and a 47-point Show HN with 6 comments the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=openlayer-ai/jevals&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=openlayer-ai/jevals&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=openlayer-ai/jevals&type=date&legend=top-left" />
</picture>

The self-run bench (September 2026, v0.1.4) measures one request per trace: $0.03 per 1,000 samples on Jev versus $2.60 for Ragas on gpt-4.1-mini, p50 244ms and p95 371ms.
The independent checks cut both ways: LangChain's experiment found 92x to 913x lower score variance than GPT and Claude judges at $0.00035 per call, while JevBench's independent run puts Jev at small-model accuracy with calibration that varies by task.

## Strengths

- One request per trace makes per-trace evaluation and in-loop guardrails economically realistic where an LLM judge forced 1% sampling.
- One eval definition serves as offline metric, production monitor, and in-loop gate, so enforcement cannot drift from measurement.
- Calibration is a first-class command: `jevals calibrate` fits deploy thresholds against your labels and reports wrong-pass and missed-pass rates per threshold.
- The self-limitation section is unusually frank: no test-set generation, no dashboard, and LLM judges stay necessary for multi-step reasoning and written critiques.

## Cautions

- **Accuracy is small-model class**: JevBench measured 80.3% on Banking77 with 608 failures, 29 of them at confidence 1.00, and recall moving from 85.7% to 98.4% on nothing but a prompt change.
- The whole stack is young on top of young: Jev, Kev, Laya, and Eikos are all September 2026 or later releases, so wire-format churn is likely.
- Gates fail open by default when a backend goes down; the fail-closed `on_error="block"` is opt-in and belongs on anything irreversible.
- Framework adapters are written to SDK docs and tested against fakes, not run live, per the README's own status section.

## Pricing

The library is MIT and free.
The hosted Jev backend (TypeSafe) is $0.042 per million input tokens with no output-token billing, and the local backends cost nothing beyond your hardware.

## Price history

The tracked price is the Jev backend Jevals calls, not Jevals itself, which has no paid tier.

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | Jev backend (TypeSafe) | Baseline: $0.042/M input tokens, no output-token charge, as documented at note creation. | https://raw.githubusercontent.com/openlayer-ai/jevals/main/README.md |

## Compared to

- [deepeval](../deepeval/index.md): the pytest-style LLM-judge framework, broader metric coverage but per-check LLM calls; choose Jevals for in-loop gates, deepeval for CI suites.
- [Langfuse](../langfuse/index.md) and [Phoenix](../phoenix/index.md): observability platforms that judge sampled traces with managed LLM evaluators; Jevals judges every trace but ships no dashboard.
- [Workshop](../workshop/index.md): the local trace-to-fix debugger, a different job on the same traces.

## Bottom line

Recommended for engineers who need guardrails inside the agent loop or evals on every trace at near-zero cost, and who will calibrate thresholds against their own labels before trusting them.
Not for judgments that need multi-step reasoning or a written critique (keep an LLM judge there), and not for teams that need a dashboard or a test-set generator.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the openlayer-ai/jevals star history chart to the Status section.

## See also

- [deepeval](../deepeval/index.md) - the LLM-judge CI framework Jevals counter-positions against
- [Jev](../../hybrid-execution/jev/index.md) - the decision model most Jevals backends speak to
- [Kev](../../hybrid-execution/kev/index.md) - the local Mac backend that makes Jevals free to run
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - where the Jevals column sits

## References

- https://api.github.com/repos/openlayer-ai/jevals - repository facts (102 stars, 9 forks, MIT, Python, pushed 2026-10-01, as of 2026-10-06)
- https://raw.githubusercontent.com/openlayer-ai/jevals/main/README.md - the eval catalog, gates, backends, self-run bench, and the $0.042/M Jev price
- https://pypi.org/pypi/jevals/json - PyPI 0.1.4 (published 2026-09-20), MIT, alpha classifier
- https://hn.algolia.com/api/v1/items/49780849 - the 47-point Show HN thread (2026-09-20) and the author's answers on backends
- https://www.langchain.com/blog/jev-agent-evals-langsmith - the independent LangChain experiment: 92x to 913x lower variance, $0.00035/call, 100% binary oracle match across 500 repetitions
- https://jevbench.xyz - the independent evaluation archive: Banking77 at 80.3% accuracy, 29 failures at confidence 1.00, and the prompt-sensitivity finding
