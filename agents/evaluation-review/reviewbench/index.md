---
title: ReviewBench
created: 2026-10-07
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, benchmark, evaluation, code-review, ai-review-agents]
readability: 3
audience_notes: >
  Engineers choosing among AI code-review agents who want to know what the public numbers can and cannot tell them.
  Assumes you know what precision, recall, and an LLM-as-judge are.
---

ReviewBench is GitHub's open offline benchmark for AI code review agents: 219 pull requests sampled from the public GitHub corpus, a multi-source golden set, a published rubric graded by Claude Sonnet 5, and a public leaderboard at review-bench.ai.

**ReviewBench is the first code-review benchmark built by the company that sells the leading reviewer, so its value rests entirely on the parts it publishes (the dataset, the rubric, the judge, the self-serve runner) and the part it keeps, a maintainer approval gate before any score goes public, is where a reader has to watch hardest.**

## What it is

A research preview built by GitHub with Microsoft and announced on 2026-10-05, with the corpus, methodology, judge prompt, and runner in an MIT-licensed repository.
The benchmark sampled 219 public pull requests from 187 open source licensed repositories across 19 languages, choosing them to match the language and repository-size distribution of 103.9 million GitHub pull requests while weighting PR size toward the reviewable middle.
Ground truth comes from human review comments, issues inferred from author follow-up commits, deterministic analysis tools, and multiple frontier LLMs, deduplicated and validated under one rubric, with Claude Sonnet 5 as the grader and a separate matcher deciding whether a candidate finding corresponds to a golden one.
Six metrics score each system: grounded precision, recall, and F1 against the golden set, and augmented versions that also judge unmatched findings, with grounded recall as the headline cross-system comparison and an adjustable Fβ weight for precision-versus-recall preferences.
Submission is self-serve: sign in with GitHub, register a container image and your own model key, iterate on a 25-PR test set, then run the full 219 three times under the same judge as every other entry.

## Status

A five-day-old research preview: the repository (review-bench/ReviewBench) was created 2026-09-04 and sits at 39 stars and 4 open issues as of 2026-10-09, last pushed 2026-10-08.
The first independent entrants arrived through the self-service portal in the benchmark's first week: five third-party reviewers (Hermes Reviewer on 2026-10-07, then HeyDeer, mesrai, pr-review-agent, and DeepSeek Harness Reviewer on 2026-10-08) merged onboarding registrations, so the submission pipeline works beyond GitHub's own pre-ran entries, though none of their leaderboard scores had published as of 2026-10-09.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=review-bench/ReviewBench&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=review-bench/ReviewBench&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=review-bench/ReviewBench&type=date&theme=dark&legend=top-left" />
</picture>

Validation is the strongest published number: senior engineers who did not build the dataset re-labeled every ground-truth finding and agreed with it 96.6 percent of the time, with 47 findings manually corrected, and GitHub reports the benchmark's offline movement has anticipated production A/B directions for Copilot code review (the lite-tier ensemble experiment: addressed rate up 8.0 percent, recall up 13.6 percent, cost per review down 8.0 percent).
**The inaugural leaderboard's top entry is GitHub's own Copilot code review at 40.1 grounded F1 in its Balanced configuration as of 2026-10-06, and the Hacker News footprint is a 4-point, zero-comment thread from launch day, so the benchmark's reach so far is press and vendor channels, not community debate.**

## Strengths

- Everything needed to reproduce or contest a score is public: the corpus and golden findings, repository mirrors, the rubric, the judge prompt and model configuration, the matcher, and the agent contract.
- The golden set does not depend on any one producer's blind spots, and the augmented metrics give credit for valid findings its creators did not anticipate.
- The Fβ knob plus severity and category slicing let a team re-rank the leaderboard by its own review preference instead of accepting one number.
- GitHub's own usage is a disclosed internal engine: the team states it gates Copilot code review changes on ReviewBench before A/B tests, which is a concrete claim that the offline signal tracks production.

## Cautions

- **The publication gate cuts against the leaderboard's meaning: submissions stay private until a maintainer approves them, and scores publish only if they beat the agent's current leaderboard score (or on first entry), so the public board can only ratchet upward and losing runs stay invisible.**
- GitHub's team generated the initial commercial entries itself by running the publicly available products, the vendors neither conducted nor verified those runs, and the test dates differ (Copilot on 2026-10-01, Greptile and Cubic back in June, per The New Stack).
- 219 PRs is a small corpus, the augmented-recall denominator moves with each agent's own discoveries and is explicitly not cross-comparable, and the judge is a frontier model whose biases the rubric mitigates but does not remove.
- Adoption is early: 39 repository stars as of 2026-10-09 and five third-party reviewers onboarded in the first week, but no independent replication of the leaderboard numbers has published yet.

## Pricing

Free to read and free to submit; GitHub provides the judge, and your cost is your own reviewer's model tokens.
The benchmark datasets are MIT-licensed.

## Compared to

- [FrontierHarness Eval](../frontierharness-eval/index.md): the same vendor-runs-the-benchmark structure one object up, scoring coding-agent harnesses instead of reviewers, with its publisher selling agent infrastructure rather than the top entry itself.
- [HarnessTax](../harnesstax/index.md): the academic counterpart with no product to sell; choose it as the conflict-free cross-examination, ReviewBench for the living leaderboard and self-serve path.
- [Jevals](../jevals/index.md): typed decision-model judges for production traces in your own loop; ReviewBench scores reviewer systems offline, before you have picked one.

## Bottom line

**Recommended for teams comparing AI code reviewers who want a reproducible, fully inspectable yardstick and will read the methodology caveats with the leaderboard.**
Not for CI gating, and not as an unbiased tiebreaker while the publisher's own reviewer holds the top entry under a publication gate only GitHub controls.

## Changes

- 2026-10-07 - Created from the daily-refresh entrant resolution, profiling GitHub's open code-review benchmark with the publication-gate and vendor-conflict cautions.
- 2026-10-09 - Recorded the first five third-party reviewer onboardings through the self-service portal (2026-10-07 and 2026-10-08) and refreshed repository counts.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [FrontierHarness Eval](../frontierharness-eval/index.md) - the vendor-run benchmark precedent for harnesses
- [HarnessTax](../harnesstax/index.md) - the academic, conflict-free counterweight
- [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md) - the reviewer products this benchmark scores

## References

- https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review - the announcement: corpus, golden set, judge, metrics, submission flow, and the publication gate
- https://github.com/review-bench/ReviewBench - the repository: corpus, mirrors, agent contract, methodology, MIT license
- https://raw.githubusercontent.com/review-bench/ReviewBench/main/README.md - corpus composition, test-set tables, mirrors, and the self-serve surface
- https://api.github.com/repos/review-bench/ReviewBench - stars, issues, creation and push dates as of 2026-10-09
- https://github.com/review-bench/ReviewBench/pulls?q=is%3Apr+is%3Amerged+onboard - the five third-party onboarding PRs merged 2026-10-07 and 2026-10-08
- https://review-bench.ai/ - the leaderboard site (a client-rendered shell to fetchers, so its content is grounded in the announcement and press coverage rather than quoted)
- https://thenewstack.io/github-reviewbench-code-review - the critical read: GitHub pre-ran the rival entries, test dates differ, and Copilot's 40.1 grounded F1 leads
- https://hn.algolia.com/api/v1/items/49967574 - the 4-point, zero-comment launch-day thread, the thin-footprint signal
