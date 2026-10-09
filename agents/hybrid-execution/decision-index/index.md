---
title: Decision Index
created: 2026-10-07
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, benchmarking, model-evaluation, leaderboard]
readability: 3
audience_notes: >
  Engineers choosing between Jev and the open decision-model wave who want a second independent scoreboard beyond JevBench, and want to know which part of it they can re-run themselves.
  Assumes you know what a chance-corrected score and a held-out test split are, and have read this category's Jev and JevBench notes.
---

The Decision Index is an independent leaderboard for typed decision engines: a frozen public suite of 110,201 requests over 42 benchmarks that anyone can rebuild from pinned sources with an MIT kit, combined with unpublished private tests into a Full score that ranks 114 configurations with hosted Jev third.

**The category's evidence layer just doubled: JevBench measures decision models deeply on 1,500 decisions per system, the Decision Index measures them broadly across 110,201 requests in five areas, and on the new 0.3 board two 27B-class systems (Perplexity's open-weights Decider v1.1 at 62.75 and Fastino's not-yet-open GLiDE at 60.21) sit above hosted Jev (60.11) for the first time on any independent reading.**

## What it is

**A leaderboard with a public reproducible floor and a private ceiling.**
It is built by apolinário (GitHub apolinario), who works on ML for art and creativity at Hugging Face, and lives as the Hugging Face Space multimodalart/jev-decision-index (created 2026-09-17, 480 likes as of 2026-10-07) with its official kit at apolinario/decision-index (MIT, created 2026-09-22).
The public part is the frozen suite: 42 benchmarks across five areas (knowledge and reasoning, language understanding, retrieval and classification, tools and automation, arts and human taste), every score chance-corrected so guessing scores zero, rebuilt locally from pinned upstream sources because upstream licenses forbid redistribution (about 7 GB of downloads), or run end to end as one Hugging Face Job on an RTX PRO 6000.
The Full score blends that public index at 20 percent with 50 percent private tests of the same skills and 30 percent private decision tasks from new domains, none of which are published; configurations within 0.9 Full-score points share a rank, and any model slower than 1,000 ms median on the maintainer's own RTX PRO 6000 is excluded as no longer Jev-like.
Editions 0.1 through 0.3 shipped between 2026-09-22 and 2026-10-06, 0.3 rebuilding GSM8K's options so option-pattern rules stop scoring and retiring ForecastBench, and the kit's parity tests reproduce every one of the 67 entrants on the live 0.2.1 board, Jev's 57.89 included.

## Status

Active and current, with a near-zero independent discussion footprint, as of 2026-10-08.
The 0.3 board data was regenerated 2026-10-07 (from the 2026-10-06 build): 114 configurations, jev-1.13.0 as the reference row, a 21-entrant vision board beside the text suite, and a reasoning board announced for 0.3.x.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=apolinario/decision-index&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=apolinario/decision-index&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=apolinario/decision-index&type=date&theme=dark&legend=top-left" />
</picture>

The kit repository shows 25 stars and 58 forks as of 2026-10-08 (pushed 2026-10-07), and the board's HN submissions sit between 1 and 6 points, so unlike JevBench's contested 154-point thread this one has barely been stress-tested in public.
On the 0.3 board Perplexity's Decider v1.1 leads at 62.75 (a 27B full fine-tune whose weights Perplexity published Apache-2.0 on the Hub on 2026-10-05, 25 likes as of 2026-10-07), Fastino's GLiDE no-thinking (28B) sits at 60.21 with its weights promised but not shipped, hosted Jev holds third at 60.11, Torchcast Decision 27B is fourth at 59.91, the regeneration's best new entrant deck31b (a frozen Gemma-4-31B) took fifth at 59.03, and Kev 27B holds sixth at 58.78, just ahead of the open Quyet-1.0-Large LoRA (58.71); the top four scores are unchanged from the 2026-10-06 build.
Bespoke Labs exercised the submission flow the day its v3 shipped: Bespoke-Nimble-9B-v3 carries a full published 0.2.1 run (56.88) with the raw results in its own dataset, the first author-submitted run of this suite I can find.

## Strengths

- **Breadth is the contribution: 110,201 chance-corrected requests across 42 benchmarks is an order of magnitude beyond any other decision-model scoreboard, and the five-area breakdown shows where a decision model is weak instead of only how it ranks.**
- The public floor is genuinely reproducible: pinned sources and hashes, byte-identical suite rebuilds, parity tests against every 0.2.1 board row including Jev, and a one-command Hugging Face Job path.
- The private 80 percent attacks exactly the selection problem JevBench's sealed revision exposed: skills probed on items nobody can train on, drawn from domains the public suite does not cover.
- The latency gate keeps the board Jev-class, so a slow general LLM cannot buy the top rank with capability alone.

## Cautions

- **The headline is one maintainer's private measurement: 80 percent of the Full score is unpublished and unrunnable by anyone else, so the number at the top of the board is the part you cannot check, and even Decider v1.1's Apache-2.0 weights do not let you re-run its 62.75.**
- The systems above Jev are barely documented: Decider v1.1 shipped its weights only on 2026-10-05 with no training recipe, GLiDE's weights are promised but not shipped, and neither team has published how its board run was served.
- The two boards disagree violently about the same checkpoints: Kev 27B is sixth here (58.78) and composites at 5.8 on JevBench's v1.6.1 scale, which says more about protocol sensitivity than about either scoreboard.
- The Space's own Jev reproductions tracker states the boundary plainly: no open artifact has Jev's weights, the RLCD algorithm, or its calibration, and the best open scorers reach about 90 percent agreement while confidence does not reliably flag their errors.

## Pricing

Free and open at the tooling layer: the kit and scoring code are MIT, the board is a free Hugging Face Space, and there is no paid tier.
Running the public suite costs your own GPU time (or one Hugging Face Job at that platform's GPU rates), about 7 GB of downloads, and each measured system bills at its own provider's rates.

## Compared to

- [JevBench](../jevbench/index.md): the other independent scoreboard; JevBench runs 1,500 decisions per system and folds intelligence, calibration, speed, and cost into one composite, the Decision Index runs 110,201 requests and weights breadth with private components, and they disagree about the same checkpoints by tens of points.
- The Jev workflow evals (evals.typesafe.ai): the vendor's own scoreboard, biased by its own admission; both independent boards exist to answer it.
- [Nimble](../nimble/index.md): its PUBLIC_BENCHMARKS.md suite remains the only human-labeled evidence (3,880 records, Jev versus one replica), where these two boards' gold labels are model-written or private.

## Bottom line

**Recommended as the breadth scoreboard and as the reproducible public suite to re-run any checkpoint against, read with the private-80-percent caveat attached to every Full score.**
Not for per-decision cost and calibration comparisons, which is JevBench's axis, and not as a verdict on Jev: a third-place rank whose 80 percent is unpublished is a reading, not a conclusion.
The disagreeable claim I will defend: the most important number on this board is not Jev's rank but the spread between the boards about identical checkpoints (Kev 27B, sixth here, near the bottom of JevBench), because it means the category still has no measurement strong enough to settle its central argument, and everyone citing a board is citing a protocol.

## Changes

- 2026-10-07 - Created from the entrant scan after the 0.3 board data (112 configurations, Jev third at 60.11) surfaced while re-verifying the JevBench board.
- 2026-10-08 - The 0.3 board regenerated 2026-10-07 with two more configurations (114) and new entrants immediately below the top four (deck31b, a frozen Gemma-4-31B, fifth at 59.03, with Blink and Decider chat Gemma-4-31B behind); the top four scores, Jev's third, and Kev 27B's sixth (58.78) are unchanged; refreshed the kit to 25 stars and 58 forks.

## See also

- [JevBench](../jevbench/index.md) - the other independent scoreboard, deeper per system and the source of the disagreement recorded here
- [Jev](../jev/index.md) - the closed model both boards measure and the reference row on this one
- [Kev](../kev/index.md) - the family whose two-board spread (sixth here, near the bottom of JevBench) this note flags
- [Nimble](../nimble/index.md) - whose v3 checkpoint carried the first author-submitted 0.2.1 run (56.88)
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://huggingface.co/spaces/multimodalart/jev-decision-index - the board (client-rendered Space; the data files below carry its content)
- https://huggingface.co/api/spaces/multimodalart/jev-decision-index - Hub API: created 2026-09-17, 480 likes, static SDK (as of 2026-10-07)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/index.json - the 0.3 board data (generated 2026-10-06T17:39:21Z): 112 configurations, per-model scores, the Jev reference row, the 42-benchmark suite header
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the 0.3 Full-score components: the 20/50/30 weights, per-model ranks, and the vision board's 21 entrants
- https://raw.githubusercontent.com/apolinario/decision-index/main/README.md - the kit: editions, scoring, submission flow, parity tests, the latency gate, licensing
- https://api.github.com/repos/apolinario/decision-index - kit repository: MIT, created 2026-09-22, 23 stars, 56 forks, pushed 2026-10-07 (as of 2026-10-07)
- https://raw.githubusercontent.com/apolinario/decision-index/main/docs/suite.md - the frozen suite: pinned sources, the GSM8K rebuild, subset and exclusion rules
- https://huggingface.co/bespokelabs/Bespoke-Nimble-9B-v3 - the first author-submitted 0.2.1 run (56.88) and the CC BY-NC 4.0 license on it
- https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b - the board leader's weights: Apache-2.0, published 2026-10-05, 25 likes (as of 2026-10-07)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/raw/main/news.html - the board's own Jev reproductions tracker: no open artifact has Jev's weights, RLCD, or calibration
- https://news.ycombinator.com/item?id=49934879 - the 4-point 0.2.1 submission grounding the near-zero HN footprint (fetched via the Algolia search API)
