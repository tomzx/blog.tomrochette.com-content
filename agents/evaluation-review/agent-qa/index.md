---
title: agent-qa
created: 2026-10-27
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, qa, testing, e2e, mobile]
readability: 3
audience_notes: >
  Engineers whose coding agents ship features faster than anyone writes acceptance tests, and who want the app itself judged on actual browsers and devices before merge.
  Assumes you know what an end-to-end test and Playwright are.
---

agent-qa is vostride's fair-source, self-improving QA agent that runs plain-English user journeys against actual web, Android, and iOS apps through Playwright and Appium, judging each step on screen and keeping the evidence of every verdict.

**Its bet is that QA needs its own agent, because the coding agent that wrote the code cannot adversarially test it, and its discipline is evidence: screenshots, console and network logs, the accessibility tree, and video behind every step's verdict.**

## What it is

An npm-distributed CLI (Node 24+) plus a local dashboard that executes natural-language YAML tests: Playwright drives an actual browser on web, Appium an actual device or emulator on Android and iOS, and a separate verifier must agree each step is done before a verdict records.
Tests, configuration, hooks, and the memidex knowledge store are files in your repository, reviewable in pull requests, while the `.agent-qa/` run evidence stays machine-local or uploads as CI artifacts.
Self-improvement turns validated run lessons into reviewable records, and marking a verdict wrong corrects the knowledge or the test in the same call.
Coding agents drive it through an MCP server (20 tools) and four skills; CI runs it with exit codes carrying the verdict and JUnit output.
Made by vostride, the project of founder Pranshu Chittora, licensed FSL-1.1-ALv2 with an Apache-2.0 future license on each version's second anniversary.

## Status

Young and moving fast: 896 stars, 23 forks, and 6 open issues and PRs as of 2026-10-27, repository created 2026-05-07, with v0.2.3 released 2026-10-24 (three releases that day, the first after the npm train had sat on 0.1.21 since June) and the npm package publishing through GitHub Actions OIDC under SLSA provenance, 3,616 downloads over 2026-09-27 to 2026-10-27.
The 50-point launch thread (2026-05-19) is the main independent discussion, and the README sets its own bar: "Early stage. Expect bugs."
The headline benchmark claims are self-published: 116/116 on AndroidWorld and 99.6% completion on AppControlBench, run on gpt-6-sol with memory and self-improvement off, every task's run published with steps, screenshots, and video, and the site discloses that agent-qa is not an entry on the official AppControlBench leaderboard and that models, judges, and OS versions differ between compared columns.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vostride/agent-qa&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vostride/agent-qa&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vostride/agent-qa&type=date&legend=top-left" />
</picture>

## Strengths

- Judges the shipped surface, not the code: journeys run against the actual app, so the tests cannot inherit the implementation's blind spots the way agent-written tests do.
- Evidence on every step makes a false pass auditable instead of mysterious.
- Everything learned is a repo file you review and revert, and your feedback overrides the agent's verdicts.
- Real CI fit: exit codes carry the verdict, JUnit output, and the docs ship the GitHub Actions job.

## Cautions

- The benchmarks are the vendor's own runs: per-task evidence is unusually open, but no third party has reproduced the 100% AndroidWorld claim, and the compared columns differ in models, judges, and OS versions.
- FSL-1.1-ALv2 is fair-source, not open source: you cannot offer the product as a service until each version converts to Apache-2.0 two years after release.
- Memory and self-improvement add a second moving part to trust: a lesson validated by runs can still encode a wrong verdict until your feedback catches it.
- One maintainer, an early-stage README, and a 3,616-download month are thin adoption signals for the claims being made.

## Pricing

Does not apply: the site states there is no paid tier, hosted lock-in, seat fee, or required model vendor, and teams bring their own model credentials and devices.

## Compared to

- [deepeval](../deepeval/index.md): judges LLM outputs you supply with roughly fifty metrics and gates merges in pytest; agent-qa judges the app surface through a browser or device. Choose deepeval for model behavior, agent-qa for user journeys.
- [HermesGate](../hermes-gate/index.md): both judge completion claims, but HermesGate runs your repository's own checks against a receipt while agent-qa drives the actual UI to verdicts no pre-existing check covers.
- [FrontierHarness Eval](../frontierharness-eval/index.md): the vendor-runs-its-own-benchmark caveat applies to both; FrontierHarness prices harnesses on fixed tasks, agent-qa's benchmarks price the QA agent itself.

## Bottom line

**Recommended for teams whose coding agents outpace their acceptance tests and who want the actual app judged, on web or mobile, with per-step evidence living in the repo.**
Not for anyone needing an OSI-approved license today, a proven adoption base, or benchmark numbers someone else has reproduced.

## Changes

- 2026-10-27 - Created, resolving the carried spec-driven-development handoff: the dormancy hold from 2026-10-12 triggered on the 2026-10-24 push and three releases, and the citation bar cleared with docs, benchmark evidence, npm, and the launch thread.

## See also

- [deepeval](../deepeval/index.md) - the CI-gating judge for model outputs, the counterpart to judging the app surface
- [HermesGate](../hermes-gate/index.md) - the receipt-bound completion gate for check-based claims
- [FrontierHarness Eval](../frontierharness-eval/index.md) - the vendor-run benchmark precedent this note's caveat mirrors
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/vostride/agent-qa - repository, README claims, install, license badge, counts as of 2026-10-27
- https://vostride.com/agent-qa - the no-paid-tier statement, benchmark summaries, and the non-leaderboard disclosure
- https://vostride.com/docs/agent-qa - the docs hub: plain-English tests, memidex, self-improvement, MCP server, skills
- https://vostride.com/docs/agent-qa/guides/ci - CI exit codes, JUnit output, artifact and learning rules
- https://vostride.com/benchmark/android-world - the self-published 116/116 runs with per-task evidence
- https://vostride.com/benchmark/app-control-bench - the AppControlBench runs, judge model, and comparison caveats
- https://raw.githubusercontent.com/vostride/agent-qa/HEAD/LICENSE.md - FSL-1.1-ALv2 and the Apache-2.0 future-license grant
- https://registry.npmjs.org/agent-qa/latest - npm 0.2.3, Node 24 engine, SLSA provenance attestations
- https://api.npmjs.org/downloads/point/2026-09-27:2026-10-27/agent-qa - the trailing-month download figure
- https://news.ycombinator.com/item?id=48191312 - the 50-point launch thread with the why-not-codex-and-playwright challenge
