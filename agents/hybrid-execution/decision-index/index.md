---
title: Decision Index
created: 2026-10-07
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, benchmarking, model-evaluation, leaderboard]
readability: 3
audience_notes: >
  Engineers choosing between Jev and the open decision-model wave who want a second independent scoreboard beyond JevBench, and want to know which part of it they can re-run themselves.
  Assumes you know what a chance-corrected score and a held-out test split are, and have read this category's Jev and JevBench notes.
---

The Decision Index is an independent leaderboard for typed decision engines: a frozen public suite of 110,201 requests over 42 benchmarks that anyone can rebuild from pinned sources with an MIT kit, still run and shown on every submission but, since edition 0.4, no longer counted, so the Full score ranking 229 configurations comes entirely from private tests, with the vendor's Jev 1.14 forty-first at 60.24 and the 1.13 reference row forty-eighth at 59.22.

**The category's evidence layer just doubled, and its main scoreboard just went fully private: JevBench measures decision models deeply on 1,500 decisions per system, the Decision Index measures them broadly, and the 0.4.1 board of 2026-10-22 removed the public index from the Full score (now 60 percent private same-skills, 40 percent private new-domains), where Fastino's shipped GLiDE V1.2 leads at 71.52, previous leader StartLux-Decision v1.1 27B slid to sixth at 67.92, and the vendor's own Jev 1.14 fell from thirteenth to forty-first of 229 at 60.24 with the 1.13 reference row forty-eighth at 59.22.**

## What it is

**A leaderboard whose score is private top to bottom, with a public reproducible suite still run and shown beside it.**
It is built by apolinário (GitHub apolinario), who works on ML for art and creativity at Hugging Face, and lives as the Hugging Face Space multimodalart/jev-decision-index (created 2026-09-17, 480 likes as of 2026-10-07) with its official kit at apolinario/decision-index (MIT, created 2026-09-22).
The public part is the frozen suite: 42 benchmarks across five areas (knowledge and reasoning, language understanding, retrieval and classification, tools and automation, arts and human taste), every score chance-corrected so guessing scores zero, rebuilt locally from pinned upstream sources because upstream licenses forbid redistribution (about 7 GB of downloads), or run end to end as one Hugging Face Job on an RTX PRO 6000.
Through edition 0.3 the Full score blended that public index at 20 percent with private tests; edition 0.4 (board label 0.4.1, generated 2026-10-22) dropped the public component from the score, making the Full score 60 percent private tests of the same skills and 40 percent private decision tasks from new domains, each put on the public scale with untuned stock models as the yardstick, while the public suite stays unchanged from 0.3 and remains a required, scored, and shown part of every submission.
Configurations within 0.9 Full-score points share a rank, and any model slower than 1,000 ms median on the maintainer's own RTX PRO 6000 is excluded as no longer Jev-like.
Editions 0.1 through 0.3 shipped between 2026-09-22 and 2026-10-06, 0.3 rebuilding GSM8K's options so option-pattern rules stop scoring and retiring ForecastBench, and the kit's parity tests reproduce every one of the 67 entrants on the 0.2.1 board, Jev's 57.89 included.

## Status

Active and current, with a near-zero independent discussion footprint, as of 2026-10-24.
The board was relabeled 0.3.2 and regenerated three more times, on 2026-10-12, 2026-10-14, and 2026-10-16 (from the morning's 0.3.1 build): 174 configurations as of the latest, jev-1.13.0 as the reference row now joined by a Jev 1.14 row, a 34-entrant vision board beside the text suite, and a reasoning board announced for 0.3.x.
The 2026-10-14 regeneration widened the band above Jev's reference from seven to eleven: vLLM-SR d3 (a 27B) still leads at 66.26, new entrant linne-oak 1.0 (a 31B) took second at 65.61, Mapika's Decider 31B (NVFP4) holds third at its unchanged 64.62, Sieve's new 31B row fourth at 63.81 (Sieve 27B eleventh at its unchanged 60.17), Bobcat 1.3 (31B) fifth at 62.83, Perplexity's Decider v1.1 sixth at its unchanged 62.75, Darwin-27B-ZTC seventh at 62.46, MORJ 1.0.1 (Gemma 4 31B) eighth at 60.96, and hosted Jev twelfth at its unchanged 60.11, where the 0.3.1 build had it ninth of 144.
Edition 0.4 shipped as label 0.4.1 on 2026-10-22 with 226 configurations and a 55-entrant vision board, and it changed the methodology rather than only the field: the Full score is now 60 percent private same-skills tests and 40 percent private new-domain tasks, the public index still required, scored, and shown on every row but no longer counted; a same-day regeneration the same date brought the board to 229 configurations (fetched 2026-10-24) with the named rows' ranks and scores unchanged.
Fastino's GLiDE V1.2 (71.52) took first, the checkpoint the 0.3.2 board had listed sixteenth with its weights promised but not shipped, ahead of Jeffan-31b-1710 (69.75), baselabs mammoth-1 (68.44), Perplexity's Decider v1.2 (67.98, fourth), and AutoTrust-JEV-27B v1.1 (67.95, fifth), with previous leader StartLux-Decision v1.1 27B sixth at 67.92, vLLM-SR d3 eleventh at 67.15, linne-oak 1.0 thirteenth at 66.88, an H2O Lightning 31B sixteenth at 66.58, Bespoke's Nimble v4 Max seventeenth at 66.56, and the Decider 31B (NVFP4) nineteenth at 66.03, while the vendor's rows slid hard, Jev 1.14 to forty-first at 60.24 and the 1.13 reference row to forty-eighth at 59.22, and Kev 27B to forty-sixth at 59.56.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=apolinario/decision-index&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=apolinario/decision-index&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=apolinario/decision-index&type=date&theme=dark&legend=top-left" />
</picture>

The kit repository shows 52 stars and 88 forks as of 2026-10-15 (pushed 2026-10-20), and the board's HN submissions sit between 1 and 6 points, so unlike JevBench's contested 154-point thread this one has barely been stress-tested in public.
On the superseded 0.3.2 board Perplexity's Decider (then a v1.2 row) ranked fourth at 65.55 (the v1.1 27B full fine-tune whose weights Perplexity published Apache-2.0 on the Hub on 2026-10-05, 25 likes as of 2026-10-07), Fastino's GLiDE no-thinking (28B) sixteenth at its unchanged 60.21 with its weights promised but not shipped, Jev 1.13 eighteenth at its unchanged 60.11, Torchcast Decision 27B nineteenth at its unchanged 59.91, and Kev 27B twenty-fourth at its unchanged 58.78; the Space shows 667 likes as of 2026-10-15, and the kit repository was pushed 2026-10-20.
Bespoke Labs exercised the submission flow the day its v3 shipped: Bespoke-Nimble-9B-v3 carries a full published 0.2.1 run (56.88) with the raw results in its own dataset, the first author-submitted run of this suite I can find.

## Strengths

- **Breadth is the contribution: 110,201 chance-corrected requests across 42 benchmarks is an order of magnitude beyond any other decision-model scoreboard, and the five-area breakdown shows where a decision model is weak instead of only how it ranks.**
- The public floor is genuinely reproducible and now diagnostic: pinned sources and hashes, byte-identical suite rebuilds, parity tests against every 0.2.1 board row including Jev, and a one-command Hugging Face Job path, still required and shown on every submission though no longer counted into the Full score.
- The private 80 percent attacks exactly the selection problem JevBench's sealed revision exposed: skills probed on items nobody can train on, drawn from domains the public suite does not cover.
- The latency gate keeps the board Jev-class, so a slow general LLM cannot buy the top rank with capability alone.

## Cautions

- **The headline is one maintainer's private measurement, and edition 0.4 made that total: the entire Full score is unpublished and unrunnable by anyone else, so the number at the top of the board is the part you cannot check, and even Perplexity's Apache-2.0 Decider weights do not let you re-run their 67.98.**
- The systems above Jev are barely documented: GLiDE arrived as a board row with no weights or recipe I could find, new top-five entrants Jeffan-31b-1710 and baselabs mammoth-1 likewise, and no team has published how its board run was served, so the private-only score removed the last check a reproduced public suite gave a skeptical reader.
- The two boards disagree violently about the same checkpoints, and the disagreement is now measured in both directions: Kev 27B is forty-sixth here after the 0.4.1 rebuild (59.56) and composites at 5.77 on JevBench's v1.6.1 scale, and that benchmark's October 7 addenda measured the systems around this board's top 20 on its own sealed pool, where the previous leader Perplexity Decider v1.1 scores 20.62 against its 62.75 here while decider-chat on Gemma-4-31B keeps a Jev-class 66.08 (as of 2026-10-10), which says more about protocol sensitivity than about either scoreboard.
- The Space's own Jev reproductions tracker states the boundary plainly: no open artifact has Jev's weights, the RLCD algorithm, or its calibration, and the best open scorers reach about 90 percent agreement while confidence does not reliably flag their errors.

## Pricing

Free and open at the tooling layer: the kit and scoring code are MIT, the board is a free Hugging Face Space, and there is no paid tier.
Running the public suite costs your own GPU time (or one Hugging Face Job at that platform's GPU rates), about 7 GB of downloads, and each measured system bills at its own provider's rates.

## Compared to

- [JevBench](../jevbench/index.md): the other independent scoreboard; JevBench runs 1,500 decisions per system and folds intelligence, calibration, speed, and cost into one composite, the Decision Index runs 110,201 requests and weights breadth with private components, and they disagree about the same checkpoints by tens of points.
- The Jev workflow evals (evals.typesafe.ai): the vendor's own scoreboard, biased by its own admission; both independent boards exist to answer it.
- [Nimble](../nimble/index.md): its PUBLIC_BENCHMARKS.md suite remains the only human-labeled evidence (3,880 records, Jev versus one replica), where these two boards' gold labels are model-written or private.

## Bottom line

**Recommended as the breadth scoreboard and as the reproducible public suite to re-run any checkpoint against, read with the now-total private-score caveat attached to every Full score.**
Not for per-decision cost and calibration comparisons, which is JevBench's axis, and not as a verdict on Jev: a forty-first-place rank whose score is entirely unpublished is a reading, not a conclusion.
The disagreeable claim I will defend: the most important number on this board is not Jev's rank but the spread between the boards about identical checkpoints (Kev 27B, forty-sixth here after the 0.4.1 rebuild, near the bottom of JevBench), and the second most important is that the board answered its private-score criticism by going fully private rather than by publishing more, because it means the category still has no measurement strong enough to settle its central argument, and everyone citing a board is citing a protocol.

## Changes

- 2026-10-07 - Created from the entrant scan after the 0.3 board data (112 configurations, Jev third at 60.11) surfaced while re-verifying the JevBench board.
- 2026-10-08 - The 0.3 board regenerated 2026-10-07 with two more configurations (114) and new entrants immediately below the top four (deck31b, a frozen Gemma-4-31B, fifth at 59.03, with Blink and Decider chat Gemma-4-31B behind); the top four scores, Jev's third, and Kev 27B's sixth (58.78) are unchanged; refreshed the kit to 25 stars and 58 forks.
- 2026-10-10 - The 0.3 board was relabeled 0.3.1 and regenerated 2026-10-10 with three more configurations (117, the top seven rows and scores unchanged), JevBench's October 7 addenda cross-measured the systems around this board's top 20 on its own sealed pool (Perplexity's Decider v1.1 at 20.62 there against 62.75 here, Kev 27B at 5.77 against 58.78), and the kit moved to 36 stars and 72 forks.
- 2026-10-12 - The 0.3.1 board regenerated 2026-10-12 with 27 more configurations (144) and a rebuilt top: vLLM-SR d3 the new leader at 65.65 ahead of Mapika's new Decider 31B (65.56), Darwin-27B-ZTC (63.21), Perplexity's Decider v1.1 (fourth, 62.75 unchanged), and an AnyJev L0 readout over Gemma-4-31B fifth at 61.27, pushing hosted Jev from third to ninth at its unchanged 60.11 and Kev 27B from sixth to seventeenth at 58.78; the vision board grew to 28 entrants and the kit to 41 stars and 81 forks.
- 2026-10-13 - The board was relabeled 0.3.2 and regenerated again later on 2026-10-12 with five more configurations (149): new entrant Sieve 27B took seventh at 60.17, narrowing the band above hosted Jev to seven and moving it from ninth to eighth at its unchanged 60.11, while vLLM-SR d3 was rescored to 66.26, Decider 31B to 64.62, Darwin-27B-ZTC to 62.46, and AnyJev L0 to 60.22, Kev 27B rose from seventeenth to thirteenth at its unchanged 58.78, and the kit moved to 49 stars and 83 forks (pushed 2026-10-12).
- 2026-10-15 - The 0.3.2 board regenerated 2026-10-14 with seventeen more configurations (166): new entrant linne-oak 1.0 (31B) took second at 65.61, Sieve added a 31B row in fourth at 63.81 (Sieve 27B to eleventh at its unchanged 60.17), Bobcat 1.3 (31B) entered fifth at 62.83, and MORJ 1.0.1 (Gemma 4 31B) eighth at 60.96, widening the band above hosted Jev from seven to eleven and moving it from eighth to twelfth at its unchanged 60.11, while Kev 27B fell from thirteenth to eighteenth at its unchanged 58.78; refreshed the kit to 52 stars and 88 forks (pushed 2026-10-14), the Space to 667 likes, and the vision board to 34 entrants.
- 2026-10-17 - The 0.3.2 board regenerated 2026-10-16 with eight more configurations (174) and a rebuilt top: new entrant StartLux-Decision v1.1 27B took first at 69.12 (vLLM-SR d3 to second at its unchanged 66.26, linne-oak 1.0 to third), Perplexity's Decider returned as a v1.2 row in fourth at 65.55 (from the v1.1's sixth at 62.75), the vendor's new Jev 1.14 entered thirteenth at 61.53 pushing the 1.13 reference row from twelfth to eighteenth at its unchanged 60.11, Kev 27B fell from eighteenth to twenty-fourth at its unchanged 58.78, and Amos 1 Large, Lychee-27B, KnowLine 35B-A3B Gen1, Bobcat 1.3, and span-02 filled the band between.
- 2026-10-22 - Edition 0.4 shipped as label 0.4.1 (generated 2026-10-22) with 226 configurations and a 55-entrant vision board, and it changed the methodology: the Full score is now 60 percent private same-skills plus 40 percent private new-domains with the public index no longer counted, the public suite staying unchanged from 0.3 as a required, scored, shown component; Fastino's shipped GLiDE V1.2 took first at 71.52, StartLux slid to sixth, and the vendor's rows fell to forty-first (Jev 1.14, 60.24) and forty-eighth (the 1.13 reference, 59.22); rewrote the definition, methodology, caution, and bottom-line sections around the fully private score.
- 2026-10-24 - The 0.4.1 board's same-day regeneration (generated 2026-10-22T20:10 UTC) grew the field from 226 to 229 configurations with the named rows' ranks and scores unchanged; fetched and re-cited.

## See also

- [JevBench](../jevbench/index.md) - the other independent scoreboard, deeper per system and the source of the disagreement recorded here
- [Jev](../jev/index.md) - the closed model both boards measure and the reference row on this one
- [Kev](../kev/index.md) - the family whose two-board spread (sixth here, near the bottom of JevBench) this note flags
- [Nimble](../nimble/index.md) - whose v3 checkpoint carried the first author-submitted 0.2.1 run (56.88)
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://huggingface.co/spaces/multimodalart/jev-decision-index - the board (client-rendered Space; the data files below carry its content)
- https://huggingface.co/api/spaces/multimodalart/jev-decision-index - Hub API: created 2026-09-17, 667 likes, static SDK (as of 2026-10-15)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/index.json - the 0.4.1 board header (generated 2026-10-22, fetched 2026-10-22): the suite counts, the 37-benchmark panel note, and the Full-score formula
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Full-score components (generated 2026-10-22T20:10:35Z, label 0.4.1, fetched 2026-10-24): the 0/60/40 weights, per-model ranks across 229 rows including both Jev rows, and the vision board's 55 entrants
- https://raw.githubusercontent.com/apolinario/decision-index/main/README.md - the kit: the 0.4 methodology change (the public suite unchanged, the Full score 60/40 private), editions, scoring, submission flow, parity tests, the latency gate, licensing (re-fetched 2026-10-22)
- https://api.github.com/repos/apolinario/decision-index - kit repository: MIT, created 2026-09-22, 52 stars, 88 forks, pushed 2026-10-20 (stars and forks as of 2026-10-15, push date as of 2026-10-22)
- https://raw.githubusercontent.com/apolinario/decision-index/main/docs/suite.md - the frozen suite: pinned sources, the GSM8K rebuild, subset and exclusion rules
- https://huggingface.co/bespokelabs/Bespoke-Nimble-9B-v3 - the first author-submitted 0.2.1 run (56.88) and the CC BY-NC 4.0 license on it
- https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b - the board leader's weights: Apache-2.0, published 2026-10-05, 25 likes (as of 2026-10-07)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/raw/main/news.html - the board's own Jev reproductions tracker: no open artifact has Jev's weights, RLCD, or calibration
- https://news.ycombinator.com/item?id=49934879 - the 4-point 0.2.1 submission grounding the near-zero HN footprint (fetched via the Algolia search API)
