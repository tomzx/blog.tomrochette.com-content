---
title: H2O-Lightning-4B
created: 2026-10-11
updated: 2026-10-11
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
The model card documents the company's own headline (v1.1 number one on the JevBench open composite as of 2026-10-07), and the measured board row (2026-10-04, composite 72.52, calibration axis 90.0, about $0.021 estimated per 1,000 decisions) comes from the benchmark's own runs, not the vendor's.

## Status

Active and eleven days old: the weights were created on Hugging Face 2026-10-02 and the card was last modified 2026-10-10, with v1.1 the current revision, 837 downloads and 46 likes as of 2026-10-11 (Hugging Face API).
It entered the board the ordinary way, a 2026-10-02 add-request on the benchmark's repository requesting measurement on one H100 with pinned weights, and the maintainer ran it: the row that makes it the open leader is the benchmark's own measurement on its own protocol (add-request 181, JevBench aggregate, both fetched 2026-10-11).
The company's card carries the claim and the screenshot, and the Decision Index does not carry the model at all, so its second-board reading does not exist yet.

## Strengths

- **The open lead is measured, not claimed: the composite that puts it above Jev's reference was produced by the benchmark's own runner on pinned weights, which is more than most of the wave's launch posts can say.**
- Calibration is a board-visible strength (axis 90.0), the axis the contract actually sells, and it is the highest among the open top five.
- The serving story is the least custom in the category: unmodified vLLM plus a shim any engineer can read in an afternoon, with the cost being input tokens only.
- A vendor with an existing ML platform standing behind a 4B open checkpoint changes the wave's economics argument, which until now has been run by individuals and labs.

## Cautions

- **The board evidence is one profile on one runner's protocol: the same benchmark's protocol changes have moved established families by tens of points (Decider's v2 fell 64.13 to 41.24), and no second board has measured H2O-Lightning-4B at all.**
- The measured configuration wants an H100-class GPU with a pinned vLLM build, so the "4B" size does not translate into laptop-class serving the way the smaller encoders' does.
- The vendor has not published training data, recipe, or a calibration methodology, so the board's calibration axis is a measurement of outputs, not a documented discipline.
- Downloads are in the hundreds against tens of thousands for the community leaders, so the deployment record is essentially the board run plus the card.

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

## See also

- [Jev](../jev/index.md) - the closed reference this model outscores on one board and trails on another axis of the same wave
- [JevBench](../jevbench/index.md) - the scoreboard whose composite row is this model's headline claim
- [Decision Index](../decision-index/index.md) - the second scoreboard that has not measured this model yet
- [Decider](../decider/index.md) - the family whose protocol-collapse history is the reason to wait before shipping on one board row
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://huggingface.co/h2oai/h2o-lightning-4b - the model card: Apache-2.0, Qwen3.5-4B fine-tune, the typed primitives, the vLLM-plus-shim serving path, and the vendor's own board claim (fetched 2026-10-11)
- https://huggingface.co/api/models/h2oai/h2o-lightning-4b - created 2026-10-02, last modified 2026-10-10, 837 downloads, 46 likes, Apache-2.0 (fetched 2026-10-11)
- https://github.com/fstandhartinger/jevbench/issues/181 - the add-request that entered the model: pinned v1.1 weights, requested H100 hardware, the serving commands (fetched 2026-10-11)
- https://benchmarkheaven.com/jev-models - the live open-weights board with H2O-Lightning-4B v1.1 first at 72.5 (board v1.7.44, fetched 2026-10-11)
- https://benchmarkheaven.com/api/jevbench/v1.6.1 - the board aggregate behind the row: composite 72.52, calibration 90.0, measured 2026-10-04, estimated $0.021 per 1,000 decisions (fetched 2026-10-11)
