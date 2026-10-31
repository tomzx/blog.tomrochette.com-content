---
title: H2O-Lightning-4B
created: 2026-10-11
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, multimodal]
readability: 3
audience_notes: >
  Engineers tracking the open decision-model wave who want to know what the first company-built system to outscore hosted Jev on an independent board actually is.
  Assumes you know what a fine-tune and a composite leaderboard score are, and have read this category's Jev note.
---

H2O-Lightning-4B is H2O.ai's Apache-2.0 decision model, a Qwen3.5-4B fine-tune that answers choice, yes/no, and score questions about a record and its attached images, one forward pass and one output token per decision, served on unmodified vLLM 0.30.0 behind a small standard-library shim.

**H2O-Lightning-4B v1.1 is the first open-weights system to outscore hosted Jev on an independent board, 72.5 against Jev's 71.5 unranked reference on JevBench's open-weights composite, and it did it as a 4B, ahead of every open 12B, 26B, and 31B on that board.**

## What it is

A multimodal decision fine-tune of Qwen3.5-4B (pipeline tag image-text-to-text) that returns a probability for every option: choice over named options, the probability a statement is true, and an ordinal score level with its distribution.
The serving path is deliberately boring: stock vLLM 0.30.0 plus `h2o_lightning_shim.py`, a standard-library shim that exposes the decision surface, so nothing custom has to be installed or trusted beyond the weights (the current card's recommended two-way path adds the vendor's own 30-file per-request-attention vLLM build on top, with stock vLLM as the one-way fallback).
The measured board row (2026-10-04, composite 72.52, calibration axis 90.0, about $0.021 estimated per 1,000 decisions) comes from the benchmark's own runs, not the vendor's; the card's own number-one headline, which carried a claim window from October 7 through October 20, was retired outright in the 2026-10-27 card rewrite for v1.4.1.

## Status

Active and moving fast: the weights were created on Hugging Face 2026-10-02 and the card was last modified 2026-10-27, with 7,209 downloads and 95 likes as of 2026-10-27 (Hugging Face API).
It entered the board the ordinary way, a 2026-10-02 add-request on the benchmark's repository requesting measurement on one H100 with pinned weights, and the maintainer ran it: the row that made it the open leader is the benchmark's own measurement on its own protocol (add-request 181, JevBench aggregate, both fetched 2026-10-12), and that v1.1 row held the official open-weights composite lead from 2026-10-08 through the 2026-10-20 read (board v1.7.46, 184 ranked systems).
The lead is now gone: on the 2026-10-27 read of board revision v1.7.48 under method v1.7 (232 ranked systems), the official composite #1 became Torchcast Decision 4B with this model's v1.1 row at #2, and on the 2026-10-31 read under the new method v1.8 (235 ranked systems, the self-hosted cost basis re-based to GPU time), the v1.1 row sits #2 at a re-based 77.94 (39th by the Capability Score at 75.0) behind Torchcast Decision 4B v1.3 at 80.49, the larger H2O-Lightning-31B v1.0.7 sibling is seventh by composite and fourth by capability at 84.3 (baselabs' mammoth-1 the new capability leader), and a new v1.4.1 row (the `main` weights) joined unranked at 81.06 pending its draw's equating, so the company checkpoint's headline is a historical first rather than the current standing.
The card no longer carries the claim either: the 2026-10-27 card rewrite retired the number-one claim and its October 7-20 claim window entirely, and the card now documents **v1.4.1** (`main`), new weights that continue the fine-tune on more training data, read 2026-10-26, served two-way on one engine of the vendor's own per-request-attention vLLM build, with v1.3.x, v1.2.3, and v1.1 (the board's revision) pinnable by tag.
The v1.4.1 card's own measurements (all self-run, on one L40S): JevBench's 231 public items at 206 correct (89.2 percent) through the benchmark's own CLI, the Decision Index 0.3 public suite at text 63.16 and vision 69.42 with the kit's scorer (explicitly not a leaderboard result), and calibration error 0.0705 on the text rows, against v1.4.0's 62.38, 69.03, and 0.0640.
Distribution widened along the way with GGUF and community MLX builds, a Nemotron-Nano-base text-only variant, and a Hugging Face Spaces demo.
The Decision Index board still does not carry the 4B at all (its 2026-10-29 regeneration at 248 configurations carries an H2O Lightning 31B row, seventh at 68.64, a larger sibling rather than this model), so the 4B's second-board reading still does not exist.

## Strengths

- **The open lead is measured, not claimed: the composite that puts it above Jev's reference was produced by the benchmark's own runner on pinned weights, which is more than most of the wave's launch posts can say.**
- Calibration is a board-visible strength (axis 90.0), the axis the contract actually sells, and it is the highest among the open top five.
- The serving story is the least custom in the category: unmodified vLLM plus a shim any engineer can read in an afternoon, with the cost being input tokens only.
- A vendor with an existing ML platform standing behind a 4B open checkpoint changes the wave's economics argument, which until now has been run by individuals and labs.

## Cautions

- **The board evidence is one profile on one runner's protocol: the same benchmark's protocol changes have moved established families by tens of points (Decider's v2 fell 64.13 to 41.24), and no second board has measured H2O-Lightning-4B at all.**
- The measured configuration wants an H100-class GPU with a pinned vLLM build, so the "4B" size does not translate into laptop-class serving the way the smaller encoders' does.
- The vendor has not published training data, recipe, or a calibration methodology, so the board's calibration axis is a measurement of outputs, not a documented discipline.
- Downloads are in the thousands against tens of thousands for the community leaders, so the deployment record is essentially the board run plus the card.

## Pricing

Free and open: Apache-2.0 weights on Hugging Face, no hosted service and no paid tier.
The cost is the GPU the measured path wants and input tokens only at serving time, one output token per decision.

## Compared to

- [Jev](../jev/index.md): the closed reference it outscores on one board; Jev keeps the hosted SLA, the longer track record, and the second-board lead, and its own note carries the seven development waves this model belongs to.
- [JevBench](../jevbench/index.md): the scoreboard that produced the claim; read the two together, because the model's headline is that board's composite and carries its methodology caveats.
- [Decider](../decider/index.md): the cautionary family on the same board, whose first-place run ended in a protocol change; the reason to wait for a second-board reading before shipping on this one.

## Bottom line

**Recommended for engineers who want a company-built, benchmark-measured open checkpoint and can serve vLLM on data-centre hardware, reading the composite lead it held through mid-October as one protocol's verdict.**
Not for laptop-class serving, not for anyone who needs a second independent reading before trusting a board row, and no longer as "the current open #1": Torchcast Decision 4B took the official composite lead, the capability lead has since passed to baselabs' mammoth-1, and the model's own new v1.4.1 row sits unranked at 81.06.
The disagreeable claim I will defend: a company checkpoint taking the open lead on a hobbyist benchmark is the moment the wave stopped being a community curiosity, and the interesting question is no longer whether open weights can match Jev but whether vendor-built open checkpoints will crowd the individuals out of their own category.

## Changes

- 2026-10-11 - Created from the entrant scan (awesome-jev cross-check), accepted on the measured open-weights lead of the primary independent scoreboard with the single-protocol caveat recorded.
- 2026-10-12 - Recorded the card's 2026-10-12 revision (a comparison section against Microsoft's Microsoft-Decision-1 announcement with both JevBench scores, plus the Capability Score explanation) and refreshed the checkpoint to 1,254 downloads and 54 likes.
- 2026-10-15 - The card's 2026-10-15 revision extended its #1-on-JevBench claim window through October 15 with a same-day board re-read and moved the comparison's API latency rows onto JevBench's measured medians (Microsoft-Decision-1 460 ms at API #6, OpenAI Decisions 298 ms at API #8); refreshed the checkpoint to 2,568 downloads and 71 likes.
- 2026-10-20 - Rotation re-verification, every cited URL re-fetched: the card's #1 claim window now runs through October 20 (still composite leader on the 2026-10-20 board read, 184 ranked systems); recorded the v1.3 line (v1.3.1 on main with two-way reading, bidirectional attention on the full-attention layers, one pass either way; v1.2.3 and v1.1 pinnable), the vendor's own Decision Index 0.3 public-suite runs (57.86 text two-way, 68.22 vision, own runs not a board result, the board still carrying no row), the 2026-10-19 vision-column correction (fallback-font Mind2Web screenshots re-read on a verified suite), and the wider distribution (GGUF and community MLX builds, a Nemotron-Nano-base text-only variant, an HF Spaces demo); refreshed the checkpoint to 4,944 downloads and 84 likes.
- 2026-10-22 - The Decision Index's edition-0.4 rebuild (226 configurations) entered an H2O Lightning 31B row (sixteenth at 66.58), a larger sibling and not this 4B, whose second-board reading still does not exist.
- 2026-10-27 - Rotation re-verification, every cited URL re-fetched, with three changes the current sources forced: the card was rewritten 2026-10-27 for v1.4.1 (`main`, new weights continuing the fine-tune, read 2026-10-26, two-way on the vendor's per-request-attention vLLM build, self-run JevBench public items 206 of 231 and Decision Index 0.3 public suite text 63.16, vision 69.42), retiring the number-one claim and its October 7-20 window outright, and the board's 2026-10-27 read (revision v1.7.48, method v1.7, 232 ranked systems) moved the v1.1 row from official composite #1 to #2 at its unchanged 72.52 behind new leader Torchcast Decision 4B, with the 31B sibling #3 and the capability leader at 84.3; the 31B's Decision Index row moved from sixteenth to seventeenth at the board's 2026-10-26 regeneration (230 configurations); refreshed the checkpoint to 7,209 downloads and 95 likes.
- 2026-10-31 - Out-of-rotation board re-fetch at the drift signal: the board moved to method v1.8 (the self-hosted cost basis re-based to GPU time, page updated 2026-10-30, 235 ranked systems), where the v1.1 row holds official composite #2 at a re-based 77.94 (39th by capability), the 31B sibling falls to seventh by composite and fourth by capability with mammoth-1 the new leader, and a new v1.4.1 row joined unranked at 81.06 pending equating; the Decision Index's 2026-10-29 regeneration moved the 31B row to seventh at 68.64 and still carries no 4B row.

## See also

- [Jev](../jev/index.md) - the closed reference this model outscores on one board and trails on another axis of the same wave
- [JevBench](../jevbench/index.md) - the scoreboard whose composite row is this model's headline claim
- [Decision Index](../decision-index/index.md) - the second scoreboard that has not measured this model yet
- [Decider](../decider/index.md) - the family whose protocol-collapse history is the reason to wait before shipping on one board row
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://huggingface.co/h2oai/h2o-lightning-4b - the model card: Apache-2.0, Qwen3.5-4B fine-tune, the typed primitives, the vLLM-plus-shim serving path, the v1.4.1 rewrite of 2026-10-27 (two-way reading, the benchmark-maintainer runbooks, the retired number-one claim), and the self-run JevBench and Decision Index 0.3 rows (re-fetched 2026-10-27)
- https://huggingface.co/api/models/h2oai/h2o-lightning-4b - created 2026-10-02, last modified 2026-10-27, 7,209 downloads, 95 likes, Apache-2.0 (fetched 2026-10-27)
- https://github.com/fstandhartinger/jevbench/issues/181 - the add-request that entered the model: pinned v1.1 weights, requested H100 hardware, the serving commands (re-fetched 2026-10-27, 200)
- https://benchmarkheaven.com/jev-models - the live open-weights board ordered by the Capability Score, method v1.8, 235 ranked systems (fetched 2026-10-31): Torchcast Decision 4B v1.3 the official composite #1 at 80.49, H2O-Lightning-4B v1.1 #2 at its re-based 77.94 (capability 39th), H2O-Lightning-31B v1.0.7 fourth by capability at 84.3, and a new v1.4.1 row unranked at 81.06
- https://benchmarkheaven.com/api/jevbench/v1.6.1 - the board aggregate behind the row: composite 72.52, calibration 90.0, measured 2026-10-04, estimated $0.021 per 1,000 decisions (fetched 2026-10-11, re-fetched 2026-10-27, the row unchanged)
