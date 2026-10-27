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

- [agent-qa](agent-qa/index.md) - vostride's fair-source self-improving QA agent that runs plain-English user journeys against actual web, Android, and iOS apps, judging each step on screen with recorded evidence, its benchmark claims self-published.
- [Better Harness](better-harness/index.md) - Qoder's MIT harness-engineering platform that judges the agent work loop itself (goals, steps, validation, safeguards, lessons) from project and session evidence, findings carrying acceptance checks, 2.4k stars and no independent footprint yet.
- [Crit](crit/index.md) - Tomasz Tomczyk's MIT local-first browser surface where agent plans, diffs, running apps, and static HTML get line comments that flow back through a review file any agent can read.
- [deepeval](deepeval/index.md) - the pytest-style eval framework with roughly fifty judge metrics that gates merges in CI.
- [FrontierHarness Eval](frontierharness-eval/index.md) - the public benchmark that held the model constant and varied nine harnesses in twelve configurations, cost spread 17.5x, vendor-run caveat attached.
- [HarnessTax](harnesstax/index.md) - the UC Berkeley study that held seven models constant across three harnesses on SWE-bench Lite and Terminal-Bench, finding harness swaps cost up to 5x while success barely moves.
- [HermesGate](hermes-gate/index.md) - Hermes Labs' Apache-2.0 receipt-bound gate that runs a repository's own checks and reuses a PASS only while the checked bytes still match, judging completion claims rather than code.
- [Hunk](hunk/index.md) - Modem's MIT review-first terminal diff viewer, one annotated stream for the whole agent changeset, judging nothing itself.
- [Jevals](jevals/index.md) - OpenLayer's MIT evals-and-guardrails library that swaps the LLM judge for typed Jev decision models, one calibrated request per trace.
- [Kiln](kiln/index.md) - Chesterfield Laboratories' local-first desktop eval workbench where non-engineers rate outputs and the ratings become judge metrics, fine-tuning sets, and optimization targets.
- [Kitaru](kitaru/index.md) - ZenML's Apache-2.0 replay-based eval platform: recorded or imported production sessions re-executed against your next change, human-pinned judgments calibrating the evaluators, the catching cohort becoming the CI gate, 308 stars as of 2026-10-14.
- [Langfuse](langfuse/index.md) - the MIT-core tracing and eval platform, 35.8k stars as of 2026-10-13, inside ClickHouse since January with the proprietary ee/ split as the caution.
- [MLR-Bench](mlr-bench/index.md) - the NUS-led NeurIPS 2025 D&B benchmark scoring AI research agents over 201 workshop tasks with MLR-Judge, a rubric-based two-model LLM panel validated against expert reviewers, whose headline finding is fabricated results in 8 of 10 coding-agent tasks.
- [Phoenix](phoenix/index.md) - Arize's OTel-native observability and eval platform, self-hostable under an Elastic license.
- [Plannotator](plannotator/index.md) - the local review surface that turns your annotations on agent plans and diffs into the agent's next instruction.
- [PR Lens](pr-lens/index.md) - coldtea's MIT visualizer that draws every pull request as animated architecture and data-flow diagrams in a PR comment, judging nothing itself; its hosted App adds model-authored review findings.
- [ReviewBench](reviewbench/index.md) - GitHub's open AI-code-review benchmark: 219 public PRs, a multi-source golden set, Claude Sonnet 5 as judge, and a leaderboard whose scores publish only on maintainer approval.
- [slop-grader](slop-grader/index.md) - the MIT CLI that grades documents and diffs line by line against Markdown rulesets with Jev decision models, exhaustive by construction and priced in thousandths of a cent per question.
- [Verbatim Citation Gate](verbatim-citation-gate/index.md) - the MIT two-stage citation auditor: a zero-token deterministic gate for fabricated quotes, then a skeptical judge that fails closed.
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
- 2026-10-06 - Added Jevals.
- 2026-10-06 - Added Hunk.
- 2026-10-07 - Added ReviewBench.
- 2026-10-10 - Added Kiln.
- 2026-10-10 - Added PR Lens.
- 2026-10-10 - Added Verbatim Citation Gate.
- 2026-10-12 - Added Crit.
- 2026-10-13 - Added Better Harness.
- 2026-10-14 - Added Kitaru.
- 2026-10-14 - Added MLR-Bench.
- 2026-10-16 - Added HermesGate.
- 2026-10-21 - Added slop-grader.
- 2026-10-27 - Added agent-qa.
