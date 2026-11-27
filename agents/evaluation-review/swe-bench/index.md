---
title: SWE-bench
created: 2026-11-18
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, benchmark, evaluation, coding-agents]
readability: 3
audience_notes: >
  Engineers choosing a coding-agent harness or model who need to know what the industry's default resolved-issue yardstick measures, and where it misleads.
  Assumes you know what a pull request and a unit-test suite are.
---

SWE-bench is the Princeton NLP benchmark that scores a coding system on whether its generated patch resolves a real GitHub issue, judged by the repository's own held-out test suite running in a per-issue Docker container.

**SWE-bench is the ground benchmark every harness study in this category runs on or argues with, and its documented failure modes (solution leakage, weak tests, training-data contamination, and a Git-history leak in the task setup) are the reason those studies exist.**

## What it is

A benchmark plus a containerized evaluation harness: 2,294 issue-PR pairs drawn from 12 popular Python repositories, each task handing the system a codebase at the parent commit and the issue text, then applying the generated patch and running FAIL_TO_PASS and PASS_TO_PASS tests to decide resolved or not.
The harness builds a Docker image per issue for reproducibility, the sb-cli tool submits runs to the public leaderboards, and Modal supports fully cloud-hosted evaluation.
The family has grown around the core: SWE-bench Lite (300 tasks), SWE-bench Verified (500 problems that human engineers confirmed are solvable, from the OpenAI Preparedness collaboration), SWE-bench Multilingual, and SWE-bench Multimodal (480 tasks open-sourced with its v2 on 2026-09-01), all MIT, from the Princeton NLP group, which also built SWE-agent on top of it.

## Status

Mature and the field's default scoreboard: 6,215 stars, MIT, created 2023-10-04, pushed 2026-09-18 (the dataset is stable, so the repository moves slowly; the leaderboards and the task family carry the activity), ICLR 2024 oral, as of 2026-11-18.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=SWE-bench/SWE-bench&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=SWE-bench/SWE-bench&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=SWE-bench/SWE-bench&type=date&legend=top-left" />
</picture>

**The footprint is the largest in this category's orbit, and so is the criticism: a 466-point Hacker News thread traced score skew to Git history leaking into task context (filed as the project's own issue 465), a 343-point 2026-04 thread declared SWE-bench Verified no longer able to separate frontier systems, and a 278-point thread found many passing patches that human reviewers would not merge.**

## Strengths

- The judge is the repository's own test suite, deterministic and sweatable by the model, not a vibe from a judge model.
- Real issues against real repositories keep the task distribution anchored to actual maintenance work.
- Fully public: datasets, harness, leaderboards, and the Docker evaluation path, so any score can be reproduced or contested.
- The family (Lite, Verified, Multilingual, Multimodal) covers the common variations without changing the mechanics.

## Cautions

- Contamination and leakage are documented, not hypothetical: the SWE-Bench+ study found solution leakage in issue descriptions and weak tests that pass plausible-but-wrong patches, and the 466-point thread traced Git history into the task context.
- A passing patch is not a mergeable patch, per the 278-point would-not-be-merged analysis, so leaderboard resolution overstates shipping readiness.
- Verified was built to be trustworthy and now saturates: the 2026-04 discussion says it no longer separates frontier systems.
- Repository-level scores confound harness with model, which is exactly the variable FrontierHarness Eval and HarnessTax control for.

## Pricing

Free: MIT datasets and harness; a run costs your model's tokens plus the Docker compute.

## Compared to

- [FrontierHarness Eval](../frontierharness-eval/index.md): the vendor-run study that holds the model constant on custom tasks; SWE-bench is the public object such studies measure against.
- [Harbor](../harbor/index.md): the runner that executes benchmark datasets in containers; choose SWE-bench to be measured, Harbor to run the measurement.
- [HarnessTax](../harnesstax/index.md): the academic study running SWE-bench Lite across harnesses to price what the harness adds on it.

## Bottom line

**Recommended as the shared yardstick to report against, read with the leakage, contamination, and test-quality caveats attached.**
Not as a frontier-capability separator (Verified has stopped separating them), and not as evidence a passing patch would survive human review.

## Changes

- 2026-11-18 - Created from the awesome-agent-observability 2026-11-15 evals-expansion scan, admitted as the ground benchmark beside the harness-variance studies this category already holds.
- 2026-11-27 - Rotation re-verification: every cited URL re-fetched and live, the release heads unchanged (no GitHub releases); the GitHub releases API URL answers the shared unauthenticated limit with 403 and was read through the authenticated API instead.

## See also

- [HarnessTax](../harnesstax/index.md) - the academic study that runs SWE-bench Lite across harnesses and prices the difference
- [FrontierHarness Eval](../frontierharness-eval/index.md) - the vendor-run benchmark holding the model constant, built because SWE-bench's scores confound harness with model
- [Harbor](../harbor/index.md) - the runner this category's benchmark ecosystem standardizes on
- [SWE-agent](../../harnesses/swe-agent/index.md) - the Princeton agent built on this benchmark, in the harnesses category

## References

- https://github.com/SWE-bench/SWE-bench - repository: README, the family news through Multimodal v2, license, containerized evaluation
- https://arxiv.org/abs/2310.06770 - the ICLR 2024 paper defining the task and metrics
- https://www.swebench.com/ - the leaderboards (SWE-bench, Verified, Multilingual, Multimodal, Lite) and the sb-cli submission tool
- https://huggingface.co/datasets/princeton-nlp/SWE-bench - the 2,294-task dataset card
- https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified - the 500-task human-verified subset
- https://arxiv.org/abs/2410.06992 - SWE-Bench+: the solution-leakage and weak-test critique
- https://hn.algolia.com/api/v1/search?query=SWE-bench&tags=story&hitsPerPage=5 - the footprint scan: the 466-point Git-history thread (the project's issue 465), the 343-point Verified-capability thread, and the 278-point mergeability thread
