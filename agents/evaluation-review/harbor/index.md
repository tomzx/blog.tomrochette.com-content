---
title: Harbor
created: 2026-11-18
updated: 2026-11-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, benchmark, evaluation, harness]
readability: 3
audience_notes: >
  Engineers who run coding-agent benchmarks and want one runner that executes any agent on any containerized task dataset the same way, locally or in the cloud.
  Assumes you know what a benchmark trial and a Docker container are.
---

Harbor is the Apache-2.0 agent-evaluation framework from the creators of Terminal-Bench that runs any agent on containerized benchmark tasks and scores each trial with the task's own test script, locally in Docker or across thousands of parallel cloud sandboxes.

**Harbor is the runner this category's benchmark ecosystem is standardizing on: it separates the dataset, the agent, and the model so trials compare on equal ground, and its publisher sells no competing agent, which is the neutrality FrontierHarness Eval and ReviewBench cannot claim.**

## What it is

A pip-installable CLI (`pip install harbor` or `uv tool install harbor`) with a dataset registry: `harbor run --dataset terminal-bench@2.0 --agent claude-code --model anthropic/claude-opus-5-5` launches the benchmark locally, and an `--env` flag moves the same run to cloud sandbox providers (Daytona, Modal, LangSmith, Blaxel, Novita Sandbox, Tensorlake, Runta, and Sail).
It evaluates arbitrary agents (Claude Code, OpenHands, Codex CLI, and more through its agent registry), builds and shares custom benchmark datasets, generates rollouts for reinforcement-learning optimization, and scales to thousands of parallel environments.
It is the official harness for Terminal-Bench 2.0, whose dataset repository now lives under the harbor-framework organization (the earlier laude-institute path redirects), and the Harbor Cookbook carries the end-to-end examples.

## Status

Young and fast: 7,186 stars, Apache-2.0, created 2025-08-04, pushed 2026-11-20 (the default branch moving 2026-11-19 with an OpenClaw agent fix for google/* model names and shared Gemini env aliases), on a monthly release train at v0.26.0 (2026-11-13) after v0.25.0 (2026-10-25), as of 2026-11-20.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=harbor-framework/harbor&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=harbor-framework/harbor&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=harbor-framework/harbor&type=date&theme=dark&legend=top-left" />
</picture>

**The score-reporting ecosystem runs through it: Terminal-Bench threads show independent agents topping the board (a 393-point Show HN on 2026-04-27) and vendors reporting headline numbers through its lineage (Cognition's 92.8 on Terminal-Bench 2.1, a 69-point thread), so a Harbor number is what reaches the mainstream discussion.**

## Strengths

- The dataset-agent-model separation makes trials reproducible and cross-comparable, the property the harness-variance studies in this category need and build on.
- Content-addressed public datasets (Terminal-Bench 2.0, and ReviewBench's frozen 219-PR dataset) mean the scored bytes cannot silently change.
- Scale: thousands of parallel sandbox trials through the provider registry, from laptop Docker to cloud.
- Apache-2.0 and a pip install; no agent vendor behind it, so the runner has no horse in the leaderboard.

## Cautions

- Pre-1.0 with monthly releases: the interface has moved five minor versions in four months, so run scripts should expect churn.
- Harbor guarantees the execution, not the measurement: a weak task test still passes a bad patch (the SWE-Bench+ critique applies to every test-script-scored dataset it runs), and registry breadth means most tasks are vetted only by their authors.
- Public score quotes inherit harness and configuration effects, exactly the finding HarnessTax priced, so "92.8 on Terminal-Bench" names a pairing, not a model.
- One of its listed sandbox providers is Runta, the publisher behind FrontierHarness Eval, worth remembering when a FrontierHarness number is read as independent.

## Pricing

Free, Apache-2.0; a run bills your model tokens plus whatever the sandbox provider charges, and local Docker runs are compute-only.

## Compared to

- [SWE-bench](../swe-bench/index.md): the benchmark object; Harbor is the machinery that runs benchmark datasets, SWE-bench is the dataset and harness that defines one.
- [FrontierHarness Eval](../frontierharness-eval/index.md): a published study with its own runner; choose Harbor to reproduce or extend such runs under a neutral framework.
- [HarnessTax](../harnesstax/index.md): the academic cross-examination of harness effects; Harbor is the tool you would reach for to rerun its matrix yourself.

## Bottom line

**Recommended for teams running agent benchmarks across local and cloud sandboxes who want one neutral runner and content-addressed datasets.**
Not for judging your own application's outputs (that is deepeval or agent-qa territory), and not as a guarantee of benchmark validity, which stays with each dataset's tests.

## Changes

- 2026-11-18 - Created from the awesome-agent-observability 2026-11-15 evals-expansion scan, admitted as the category's benchmark runner beside its benchmark studies.

## See also

- [HarnessTax](../harnesstax/index.md) - the academic harness-variance study run on Terminal-Bench 2.0, the dataset Harbor officially harnesses
- [FrontierHarness Eval](../frontierharness-eval/index.md) - the vendor-run benchmark whose publisher appears in Harbor's provider registry
- [ReviewBench](../reviewbench/index.md) - GitHub's code-review benchmark, whose public dataset ships as a frozen Harbor dataset
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the capability view of the agents Harbor runs

## References

- https://github.com/harbor-framework/harbor - repository: README, the provider list, install paths, the Terminal-Bench 2.0 example, license
- https://harborframework.com/docs - the documentation hub
- https://github.com/laude-institute/terminal-bench-2 - the Terminal-Bench 2.0 dataset, now under the harbor-framework organization through this redirecting path
- https://www.tbench.ai - the Terminal-Bench site naming the creators' lineage
- https://github.com/harbor-framework/harbor-cookbook - the end-to-end examples and guides
- https://api.github.com/repos/harbor-framework/harbor/releases - the monthly release train to v0.26.0 (2026-11-13)
- https://hn.algolia.com/api/v1/search?query=terminal-bench&tags=story&hitsPerPage=5 - the score-reporting footprint: the 393-point independent-agent thread and the vendor score reports
