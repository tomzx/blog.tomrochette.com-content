---
title: Better Harness
created: 2026-10-13
updated: 2026-10-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, harness-engineering, workflow-quality]
readability: 3
audience_notes: >
  Engineers who review agent output and suspect the workflow around the agent, not the model, is the weak point.
  Assumes you run at least one coding harness and know what a review gate is.
---

Better Harness is Qoder's MIT-licensed harness-engineering platform that turns project and session evidence into prioritized findings about the agent work loop, each finding tied to its evidence, expected outcome, repair boundary, and validation route.

**Its object of judgment is the workflow, not the diff: where every other column here scores model outputs or harness costs, Better Harness scores the loop around them, five dimensions at a time (fuzzy goals, improvised steps, missing validation, bypassed safeguards, lost lessons).**

## What it is

A self-hosted platform from Qoder, the commercial coding-agent vendor, distributed as an npm CLI (`@qoder-ai/better-harness`) with thin host adapters and published docs.
It gathers project evidence and session evidence where the host supports it, evaluates the five work-loop dimensions, and renders reports whose findings carry acceptance checks, so a team can fix one workflow issue at a time and prove the fix later.
The project opens three layers: engineering-practice guidance, the evaluation model (evidence states, findings, scoring boundaries, longitudinal validation), and the runnable implementation (collectors, analyzers, renderers, host adapters).
Ten hosts are documented, including Claude Code, Codex, Cursor, Copilot CLI, Qwen Code, Pi, Kimi Code, and the vendor's own Qoder.

## Status

Active, early, and vendor-backed: 2,374 stars, 192 forks, and 12 open issues as of 2026-10-13, created 2026-07-21 and pushed 2026-10-20, with npm at 0.6.6 (2026-08-31, eleven versions) as the newest stable and two alphas after it (0.7.0-alpha1, 2026-09-03, on npm; 0.7.0-alpha2, 2026-09-12, GitHub-only, never npm-published).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=QoderAI/better-harness&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=QoderAI/better-harness&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=QoderAI/better-harness&type=date&legend=top-left" />
</picture>

**The footprint is the weakness: I found no Hacker News or Reddit thread of its own (searches return only irrelevant comment matches), and the npm train stopped in August while the repository pushes daily, so adoption evidence outside the vendor's own surfaces does not exist yet.**
The docs are candid about the epistemics, which builds trust: unobserved behavior stays explicit, and only a comparable later result can prove a loop improved.

## Strengths

- The judged object is the system around the agent, which is the failure location practitioners actually report, and no other column here scores it continuously.
- Findings carry repair boundaries and validation routes instead of vibes, so each report decomposes into assignable work.
- The five-dimension rubric (goals, steps, validation, safeguards, lessons) maps to failure modes that occur in practice and is written down, so it can be argued with.
- Host adapters are thin and documented for ten harnesses, so the platform follows the team's existing tools instead of replacing them.
- The candor rules (evidence states, no unsupported scores) are enforced in the evaluation model, not left to the operator.

## Cautions

- The rubric is the vendor's own model, unvalidated by any third party, and the vendor sells a competing commercial agent, so the referee is not independent.
- Zero independent community footprint: no threads, no third-party writeups found, the stars-ahead-of-discussion pattern this section flags elsewhere.
- Reports are advisory: there is no recorded CI gate or merge-blocking surface, so improvement depends on a human reading them.
- One maintainer org and an npm stable line idle since August 2026 (two September alphas aside, the second never npm-published) make supply-chain and continuity review part of any adoption decision.
- Session evidence depends on host support, so the same project gets shallower findings on some harnesses than others.

## Pricing

Free and open source under MIT.
There is no hosted tier and no Better Harness subscription; the vendor's commercial products (the Qoder agent) are billed separately and are not required to run this.

## Compared to

- [Workshop](../workshop/index.md): the eval platform for running harness experiments against scenarios; Better Harness observes the ongoing work loop instead of staging experiments.
- [HarnessTax](../harnesstax/index.md): the Berkeley study that held models constant across harnesses once; Better Harness is that measurement turned into a continuous in-repo loop.
- [FrontierHarness Eval](../frontierharness-eval/index.md): the vendor-run public benchmark with a 17.5x cost spread; use it to pick a harness, Better Harness to improve the one you run.

## Bottom line

**Recommended for teams that already review agent output and want the workflow around it measured, with the evidence discipline to prove changes worked.**
Not for anyone needing an independent referee (the vendor grades its own category), a CI gate, or a tool with third-party field reports behind it.

## Changes

- 2026-10-13 - Created.
- 2026-10-17 - Corrected the npm-line claim: 0.7.0-alpha1 shipped 2026-09-03 after stable 0.6.6, so the line is idle since August at the stable channel, not entirely.
- 2026-10-21 - Corrected the alpha count again: v0.7.0-alpha2 shipped 2026-09-12 on GitHub only and never reached npm, so the alpha line has two entries and the npm channel one.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Workshop](../workshop/index.md) - the experiment-platform neighbor judging harnesses under controlled scenarios
- [HarnessTax](../harnesstax/index.md) - the academic one-shot of the same question Better Harness runs continuously
- [FrontierHarness Eval](../frontierharness-eval/index.md) - the vendor-run benchmark counterpart
- [Plannotator](../plannotator/index.md) - the plan-annotation surface whose evidence Better Harness would consume

## References

- https://github.com/QoderAI/better-harness - repository, MIT license, stars, forks, push activity, and the three-layer structure as of 2026-10-13
- https://qoderai.github.io/better-harness/docs/introduction - the five work-loop dimensions, the evidence-and-findings model, and the deliberately candid epistemics
- https://qoderai.github.io/better-harness/demo/better-harness-report/ - the rendered example report showing findings with evidence, outcomes, repair boundaries, and validation routes
- https://www.npmjs.com/package/@qoder-ai/better-harness - package version 0.6.6 (2026-08-31) and the eleven-version history (the npm site 403s to curl, verified through the registry API)
- https://martinfowler.com/articles/harness-engineering.html - the harness-engineering framing the README builds its feedforward-and-feedback model on
