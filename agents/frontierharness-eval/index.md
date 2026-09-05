---
title: "FrontierHarness Eval"
created: 2026-09-05
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, benchmark, coding-agents]
readability: 3
audience_notes: >
  Engineers choosing between coding-agent harnesses who want independent cost and quality numbers instead of vendor benchmarks.
  Assumes you know what a pass rate, token cost, and a cache hit are.
---

**FrontierHarness Eval is the first public benchmark to hold the model constant and vary only the harness, and its headline finding is that harness choice moved cost 17.5x while quality stayed within about 13 points.**
Facts below verified as of 2026-09-05.

## What it is

A multi-harness benchmark from Runta: the same Kimi K3 model ran through nine coding-agent harnesses in twelve configurations over the same 30 software-engineering tasks, 360 runs total, with identical cold starts.
The public results table puts Codex first on quality (66.7 percent pass, $3.47 median per pass), Exo Harness first on cost ($1.05), DSH Minimal first on speed (5m 41s), and Claude Code mid-quality at $18.34, the most expensive cell.
Task definitions, difficulty metadata, harness versions, and normalized results are public in the repository, and an agent-neutral skill lets third parties re-run the evaluation.

## Status

New and gaining traction: the repository was created 2026-08-31 and pushed 2026-09-04, and the launch drew an 81-point Hacker News thread with substantive methodological discussion.
**The benchmark is vendor-run: Runta sells an execution layer for AI agents and announced a $20M seed led by a16z, so the neutrality that makes the numbers useful is asserted, not structural.**
The repository carries no license as of 2026-09-05, which limits reuse of the task definitions themselves.

## Strengths

- The design isolates the variable this whole section cares about: with model, tasks, and runtime fixed, the harness is the only explanation left for a 17.5x cost spread.
- Full public artifacts, including failed runs and task-level results, not just a leaderboard.
- Covers harnesses this section profiles (Codex, Claude Code, Pi, OpenCode, Hermes, DeepSeek Harness configurations, Kimi Code, Exo), so the numbers cross-check our notes directly.

## Cautions

- **The conflict of interest is real**: a benchmark published by a company selling agent infrastructure, however well-designed, deserves the same skepticism as a vendor SWE-bench number.
- Thirty tasks is a small sample; one task swing moves a pass rate by 3.3 points, and the HN thread pressed exactly this.
- 30 tasks, one model (Kimi K3), and one snapshot date: results say as much about that pairing as about the harnesses, and the repository has no license.

## Pricing

Not applicable; the benchmark is free to read and the runner installs via `npx @frontierharness/eval`.
Reproducing a run costs whatever your chosen harness's tokens cost.

## Compared to

- SWE-bench and its variants: repository-grounded but model-confounded, since harness and model change together; FrontierHarness's value is precisely the held-constant model.
- [deepeval](../deepeval/index.md): a framework for evaluating your own LLM app, not a public leaderboard of third-party harnesses.
- [Phoenix](../phoenix/index.md): observability for your own traces, complementary rather than competing.

## Bottom line

Recommended as the current best evidence for the harness-choice cost question, read with the vendor-run caveat attached.
Not as a final ranking, and not for teams whose tasks look nothing like its 30.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability view of the same harnesses this benchmark prices
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the Kimi K3 pricing that sets the benchmark's cost scale
- [Hamel Husain](../hamel-husain/index.md) - the eval-methodology lens for reading a 30-task benchmark
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map of harnesses the benchmark samples from

## References

- https://frontierharness.org - the live results and interactive report
- https://github.com/frontier-harness-eval/eval - public tasks, metadata, results, and the evaluation skill
- https://runta.com/blog/introducing-frontierharness-eval/ - the launch article and evaluation design
- https://hn.algolia.com/api/v1/items/49538490 - the 81-point launch thread and its methodological criticism
- https://runta.com - the publisher and its funding context
