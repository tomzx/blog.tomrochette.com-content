---
title: H2O-Lightning-4B
created: 2026-10-11
updated: 2026-10-20
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
The serving path is deliberately boring: stock vLLM 0.30.0 plus `h2o_lightning_shim.py`, a standard-library shim that exposes the decision surface, so nothing custom has to be installed or trusted beyond the weights.
The model card documents the company's own headline (v1.1 number one on the JevBench open composite, a claim window the card now runs from October 7 through October 20 on two same-spanning board reads), and the measured board row (2026-10-04, composite 72.52, calibration axis 90.0, about $0.021 estimated per 1,000 decisions) comes from the benchmark's own runs, not the vendor's.

## Status

Active and eighteen days old: the weights were created on Hugging Face 2026-10-02 and the card was last modified 2026-10-20, with 4,944 downloads and 84 likes as of 2026-10-20 (Hugging Face API).
It entered the board the ordinary way, a 2026-10-02 add-request on the benchmark's repository requesting measurement on one H100 with pinned weights, and the maintainer ran it: the row that makes it the open leader is the benchmark's own measurement on its own protocol (add-request 181, JevBench aggregate, both fetched 2026-10-12), and the row still tops the official open-weights composite on the 2026-10-20 read (board v1.7.46, updated 2026-10-18, 184 ranked systems).
The company's card carries the claim and the screenshot, the 2026-10-12 card revision added a comparison section against Microsoft's Microsoft-Decision-1 announcement (Microsoft's accuracy numbers kept, latency corrected onto one H100 basis, both JevBench scores shown), which also explains the board's new Capability Score ordering as the Intelligence-plus-Calibration average that excludes speed and cost, and the current card extends the headline's claim window through October 20 with the same-day board re-read.
The card's main revision is no longer the board's weights: since the v1.3 line `main` carries v1.3.1, the v1.3 weights continued for one more pass and trained for **two-way reading** (bidirectional attention on the model's full-attention layers, so the answer position sees the record in both directions, one forward pass and one output token either way, two-way the recommended default), with v1.3.0.5, v1.2.3, and v1.1 (the board's revision) all pinnable.
The vendor also published its own runs of the Decision Index 0.3 public suite with the official scorer (v1.3.1 text 57.86 two-way, vision 68.22, explicitly not a leaderboard result), corrected the vision column on 2026-10-19 after a fallback-font defect in its Mind2Web screenshots, and widened distribution with GGUF and community MLX builds, a Nemotron-Nano-base text-only variant, and a Hugging Face Spaces demo.
The Decision Index board still does not carry the model at all, so its second-board reading does not exist yet.

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

**Recommended for engineers who want the strongest measured open checkpoint today and can serve vLLM on data-centre hardware, reading the lead as one protocol's verdict.**
Not for laptop-class serving, and not for anyone who needs a second independent reading before trusting a board row.
The disagreeable claim I will defend: a company checkpoint taking the open lead on a hobbyist benchmark is the moment the wave stopped being a community curiosity, and the interesting question is no longer whether open weights can match Jev but whether vendor-built open checkpoints will crowd the individuals out of their own category.

## Changes

- 2026-10-11 - Created from the entrant scan (awesome-jev cross-check), accepted on the measured open-weights lead of the primary independent scoreboard with the single-protocol caveat recorded.
- 2026-10-12 - Recorded the card's 2026-10-12 revision (a comparison section against Microsoft's Microsoft-Decision-1 announcement with both JevBench scores, plus the Capability Score explanation) and refreshed the checkpoint to 1,254 downloads and 54 likes.
- 2026-10-15 - The card's 2026-10-15 revision extended its #1-on-JevBench claim window through October 15 with a same-day board re-read and moved the comparison's API latency rows onto JevBench's measured medians (Microsoft-Decision-1 460 ms at API #6, OpenAI Decisions 298 ms at API #8); refreshed the checkpoint to 2,568 downloads and 71 likes.
- 2026-10-20 - Rotation re-verification, every cited URL re-fetched: the card's #1 claim window now runs through October 20 (still composite leader on the 2026-10-20 board read, 184 ranked systems); recorded the v1.3 line (v1.3.1 on main with two-way reading, bidirectional attention on the full-attention layers, one pass either way; v1.2.3 and v1.1 pinnable), the vendor's own Decision Index 0.3 public-suite runs (57.86 text two-way, 68.22 vision, own runs not a board result, the board still carrying no row), the 2026-10-19 vision-column correction (fallback-font Mind2Web screenshots re-read on a verified suite), and the wider distribution (GGUF and community MLX builds, a Nemotron-Nano-base text-only variant, an HF Spaces demo); refreshed the checkpoint to 4,944 downloads and 84 likes.

## See also

- [Jev](../jev/index.md) - the closed reference this model outscores on one board and trails on another axis of the same wave
- [JevBench](../jevbench/index.md) - the scoreboard whose composite row is this model's headline claim
- [Decision Index](../decision-index/index.md) - the second scoreboard that has not measured this model yet
- [Decider](../decider/index.md) - the family whose protocol-collapse history is the reason to wait before shipping on one board row
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://huggingface.co/h2oai/h2o-lightning-4b - the model card: Apache-2.0, Qwen3.5-4B fine-tune, the typed primitives, the vLLM-plus-shim serving path, the two-way and one-way reading modes, the Decision Index public-suite runs, and the vendor's own board claim (re-fetched 2026-10-20)
- https://huggingface.co/api/models/h2oai/h2o-lightning-4b - created 2026-10-02, last modified 2026-10-20, 4,944 downloads, 84 likes, Apache-2.0 (fetched 2026-10-20)
- https://github.com/fstandhartinger/jevbench/issues/181 - the add-request that entered the model: pinned v1.1 weights, requested H100 hardware, the serving commands (re-fetched 2026-10-20, unchanged since 2026-10-07)
- https://benchmarkheaven.com/jev-models - the live open-weights board ordered by the Capability Score with H2O-Lightning-4B v1.1 the composite leader (official #1; capability 75.0, tenth), board v1.7.46 updated 2026-10-18, 184 ranked systems (fetched 2026-10-20)
- https://benchmarkheaven.com/api/jevbench/v1.6.1 - the board aggregate behind the row: composite 72.52, calibration 90.0, measured 2026-10-04, estimated $0.021 per 1,000 decisions (fetched 2026-10-11, re-fetched 2026-10-20)
