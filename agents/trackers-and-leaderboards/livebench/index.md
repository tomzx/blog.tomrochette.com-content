---
title: LiveBench
created: 2026-10-06
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, benchmarks, open-data]
readability: 3
audience_notes: >
  Engineers who want an objective model score they can download and rerun themselves,
  and who need to know what changed when the site's benchmark jumped from rotated public questions to long-horizon agent work.
  Assumes you know what test-set contamination and a ground-truth-checked benchmark are.
---

LiveBench is a public LLM benchmark in two generations: the website now fronts LiveBench 2.0, a long-horizon leaderboard that gives models end-to-end work (apps, research reports, bug fixes, documents) and grades what they hand back, while the repository keeps v1, the rotated-question benchmark that scores every answer against objective ground truth instead of an LLM judge.

**v1 is still this category's checkable number, with questions, model answers, and judgments all published; 2.0 publishes the scores and their per-task breakdowns but not the tasks, so a 2.0 score cannot yet be recomputed from outside.**

## What it is

v1 (github.com/LiveBench/LiveBench, 1,342 stars as of 2026-10-11) came out of an ICLR 2025 Spotlight paper by Colin White and collaborators including Yann LeCun, Tom Goldstein, and Micah Goldblum, run day to day by Abacus.AI engineers.
Its design calls for monthly question releases drawn from recent sources (math competitions, arXiv papers, news articles, movie synopses), a verifiable ground-truth answer per question, and about 1,000 questions across 6 categories and 18 tasks, with an agentic coding category (joined May 2025) that runs models through repository tasks in Docker using the Mini-SWE-Agent harness, a standing offer to run your model for free, and all questions, model answers, and judgments published on Hugging Face.
The website switched generations between the 2026-10-13 and 2026-10-23 Wayback captures: livebench.ai now fronts LiveBench 2.0, described in its own words as "a challenging, contamination-free long-horizon AI benchmark" where "models do real work (decks, research reports, bug fixes, apps that run for hours) and we grade what they hand back", with the footer reading "sponsored by Abacus.AI".
The 2.0 board holds seven suites (Long Agentic, Reasoning, Coding, Browser, Data Analysis, Research, Design), five of them agentic: the model works with tools through tasks like fixing a bug that a merged pull request fixed (graded by hidden tests), driving a working web app through screenshots, researching a brief into a sourced report, or producing a document rendered and scored against it, while Reasoning and Data Analysis are short single-answer sets checked against ground truth.
The published methodology sets one run per model per suite at the model's highest supported effort setting, each cell as the mean of that suite's task scores on a 0-100 scale, and a hard policy that a task the run could not measure (a harness or provider fault, repeated on its one rerun) scores 0 and stays in the mean; overall weights are Long Agentic 2.0, Coding 1.5, Design 1.5, with per-suite per-task scores published as CSV and JSON files on the site, and v1 still serving the site's cost data ("Cost data is published for v1's latest release only").

## Status

Active but split: the repository was pushed 2026-10-18 (model-configuration merges under its dated-pricing gate) and shows no commits since, the changelog's newest question release stays 2026-01-08 (the frozen-set gap now at ten months), and the README still documents v1 only, with no mention of 2.0.
The rebrand carries no announcement this client can find: an HN search for "LiveBench 2.0" returns zero stories as of 2026-11-08, and the Wayback captures bracket the switch to the second half of October, with no homepage capture between 2026-10-13 and 2026-10-22.
The 2.0 board has its own freshness question: the newest published data snapshot is 2026-10-25, two weeks old at this re-check with no newer table on the live site, and its per-suite leaders are Claude Fable 5.1 on Long Agentic (77.9) and Coding (97.7), GPT-6.1 Sol on Browser (93.3), Gemini 4 Argon on Reasoning (95.1) and Data Analysis (85.2), Muse Wonder 1.0 on Research (88.0), and Claude Opus 5.5 on Design (86.9) across 32 ranked models.
Community footprint stays thin on HN (the 2024 launch thread drew 6 points and 0 comments) even though model cards and release posts cite LiveBench scores routinely.
The site remains a client-rendered app, but its shell now carries the 2.0 title and description, and its per-suite data files (table CSV, breakdown and categories JSON) fetch directly.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=LiveBench/LiveBench&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=LiveBench/LiveBench&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=LiveBench/LiveBench&type=date&legend=top-left" />
</picture>

## Strengths

- v1's objective ground-truth scoring avoids the judge biases the project itself documents (its changelog cites GPT-4-Turbo pass/fail judgments erroring on up to 46% of hard reasoning and math answers).
- v1's full transparency stands: questions, answers, and judgments are downloadable, and the whole run pipeline is public.
- 2.0 measures the deployed-stack work almost no one else in this category scores (fixes checked by hidden tests, documents rendered and checked, browser jobs checked against expected outcomes), with per-task score breakdowns published for every cell.

## Cautions

- The contamination-limiting premise can no longer be checked from outside on 2.0: its tasks are unpublished fixed briefs, so the v1 mechanism (rotate questions, publish everything) has no public counterpart, and v1's own question set has been frozen since 2026-01-08.
- The authors themselves downgraded the claim, retitling the paper from Contamination-Free (v1, 2024) to Contamination-Limited (v2, 2025), and the November 2025 changelog entry says rotation only resolved saturation and contamination "to some extent".
- The site's operator is now also 2.0's declared sponsor (Abacus.AI, a commercial ML-platform vendor), so the benchmark functions still more directly as that company's research marketing.
- One run per suite at a single effort setting, with unmeasurable tasks scored 0 after one rerun rather than excluded, makes each cell a noisy single sample that punishes infrastructure faults as capability failures.
- The repository and the site have decoupled: the public code documents only v1, so nothing about the 2.0 harness (its grading implementations or model settings) can be read or rerun, and its README still carries the stale 2025-04-25 release note and the 150GB agentic-track warning.

## Pricing

Free: the repository, the v1 questions, the answers, the judgments, and the leaderboard are public, and the team evaluates requested models at no charge.
2.0's board, methodology page, and per-suite data files are public too, with Abacus.AI named as sponsor and no reader-facing price.
No paid tier exists, so no price history applies.

## Compared to

- [Artificial Analysis](../artificial-analysis/index.md): the operator's private evals with closed question sets; v1 publishes everything it scores, and 2.0 sits between the two.
- [LLM Stats](../llm-stats/index.md): aggregates other benchmarks' published numbers; LiveBench generates its own evidence.
- [Margin Lab](../margin-lab/index.md): the other member grading deployed-stack work; Margin Lab watches two stacks daily on a fixed subset, 2.0 boards 32 models across seven work suites.

## Bottom line

**Recommended for v1's auditable read (download every question, answer, and judgment and rerun the whole chain), and for 2.0 as a directional read on long-horizon agent work you cannot yet audit; not for preference, spend, or trend questions.**
My disagreeable claim: the interesting event in this note is not any score but the split itself, because the paper-grade transparency stayed with the frozen v1 while the product moved to a board that publishes outcomes only, and that trade, a fresh instrument with closed tasks, is the direction every commercial rival already took.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the LiveBench/LiveBench star history chart to the Status section.
- 2026-10-16 - Rotation re-verification with every cited URL re-fetched live: the configuration train continued through 2026-10-15 (Muse Wonder, Step 5 Preview, MiMo-V2.6-Pro-Max, Gemma 4, Nemotron 3.5 Super VL, plus litellm streaming and Gemini continuation fixes), while the newest question release stayed 2026-01-08, stretching the frozen-set gap past nine months.
- 2026-10-28 - Rotation re-verification with every cited URL re-fetched live: nothing has moved since the 2026-10-18 push (no new commits, the config gate idle), the newest question release still 2026-01-08 with the frozen-set gap approaching ten months, the README's stale-release note and 150GB agentic warning unchanged, and the launch thread still the whole HN footprint at 6 points and 0 comments.
- 2026-11-08 - Rotation re-verification caught what the 2026-10-28 pass (reading only an empty client shell) missed: livebench.ai rebranded to LiveBench 2.0 between the 2026-10-13 and 2026-10-23 Wayback captures, a long-horizon benchmark over seven suites (five agentic) sponsored by Abacus.AI, with 32 models in its newest published table (2026-10-25), one run per model per suite, and unmeasurable tasks scoring 0 after one rerun; the repository documents v1 only (no commits since 2026-10-18, newest question release still 2026-01-08), an HN search for "LiveBench 2.0" returns zero stories, and the note reframed around the v1/2.0 split.

## See also

- [Artificial Analysis](../artificial-analysis/index.md) - the closed-evals counterpart to a fully published benchmark
- [LLM Stats](../llm-stats/index.md) - the aggregator that consumes benchmark outputs like LiveBench's
- [AI Release Tracker](../ai-release-tracker/index.md) - the release stream that dates every model on the leaderboard
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where benchmark scores land when a model choice gets made

## References

- https://api.github.com/repos/LiveBench/LiveBench - repository metadata: 1,342 stars as of 2026-10-11, pushed 2026-10-18, license listed as Other (re-fetched 200, 2026-11-08, pushed_at unchanged at 2026-10-18, 186 open issues; star figure unchanged by policy)
- https://raw.githubusercontent.com/LiveBench/LiveBench/main/README.md - v1 design, 6 categories and 18 tasks, the evaluation offer, the stale release note, the unmaintained local-inference path, and the 150GB agentic warning (fetched 200, 2026-10-06; re-fetched 200, 2026-11-08, unchanged and still v1-only, no mention of 2.0)
- https://raw.githubusercontent.com/LiveBench/LiveBench/main/changelog.md - release history: monthly through 2024, agentic category 2025-05-30, Mini-SWE-Agent switch 2025-10-03, newest question set 2026-01-08, and the 46% GPT-4-Turbo judge-error figure (re-fetched 200, 2026-11-08, newest set still 2026-01-08)
- https://arxiv.org/abs/2406.19314 - the paper: ICLR 2025 Spotlight, the 18-author list including LeCun, and the Contamination-Free to Contamination-Limited title change (fetched 200, 2026-10-06; re-fetched 200, 2026-11-08, unchanged)
- https://api.github.com/repos/LiveBench/LiveBench/commits?per_page=6 - 2026 activity: late-September and October runs add model configurations under the config gate (re-fetched 200 via the authenticated gh api, 2026-11-08, no commits after the 2026-10-18 off-peak-rate fix)
- https://hn.algolia.com/api/v1/search?query=livebench&tags=story - the thin HN footprint: launch thread at 6 points, 0 comments (fetched 200, 2026-10-06; re-fetched 200, 2026-11-08, unchanged, the 2024 launch thread still the top story)
- https://livebench.ai/ - the leaderboard surface (fetched 200, 2026-10-06 as a client-rendered shell; re-fetched 200, 2026-11-08, the shell now titled "LiveBench 2.0 - A challenging, contamination-free long-horizon AI benchmark" with the long-horizon description in its meta)
- https://livebench.ai/static/js/main.1e1ce12d.js - the 2.0 application bundle: the seven-suite methodology text (one run per model per suite, 0-100 mean task scores, unmeasurable tasks scoring 0 after one rerun, highest supported effort setting), the coding suite's hidden-test grading, the browser suite's screenshot-driven tasks, the design suite's rendered-file checks, the "sponsored by Abacus.AI" footer, and the v1-for-cost-data note (fetched 200, 2026-11-08)
- https://livebench.ai/data/20261025/table.csv - the newest published 2.0 board: 32 models scored per suite, Claude Fable 5.1 leading Long Agentic (77.9) and Coding (97.7), with no newer dated table served as of 2026-11-08 (fetched 200, 2026-11-08)
- https://livebench.ai/data/20261025/categories.json - the seven suites and their overall weights (Long Agentic 2.0, Coding 1.5, Design 1.5) (fetched 200, 2026-11-08)
- https://livebench.ai/data/20261025/breakdown.json - per-suite task parts, 32 across the seven suites from Finance & Compliance Apps to Presentations (PPT) (fetched 200, 2026-11-08)
- https://web.archive.org/cdx/search/cdx?url=livebench.ai&matchType=domain - the capture inventory behind the rebrand dating, including the /data/20261014 and /data/20261025 snapshot series (re-fetched 200, 2026-11-08)
- https://web.archive.org/web/20261012232019/https://livebench.ai/ - the 2026-10-12 capture still titled "LiveBench" (fetched 200, 2026-11-08)
- https://web.archive.org/web/20261023112315/https://livebench.ai/ - the 2026-10-23 capture already carrying the LiveBench 2.0 title and long-horizon description (fetched 200, 2026-11-08)
- https://hn.algolia.com/api/v1/search?query=%22LiveBench%202.0%22 - zero hits: the missing announcement footprint of the rebrand, stated as a signal (fetched 200, 2026-11-08)
