---
title: Decider
created: 2026-10-11
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, fine-tuning]
readability: 3
audience_notes: >
  Engineers choosing among the open decision-model families who want the one with the widest checkpoint range and the deepest scoreboard record, told with its collapse under the sealed protocol attached.
  Assumes you know what a fine-tune and a sealed test set are, and have read this category's Jev note.
---

Decider is Mapika's Apache-2.0 family of one-pass typed decision models on Qwen3.5 decoders (2B, 4B, 12B, and a 35B-A3B), serving Choice, Score, and Noul probabilities from a single forward pass with no decoding, packaged as `pip install decider-ai` with an HTTP server and GGUF exports.

**Decider is the wave's workhorse family: it took JevBench's first open-weights number one (decider-4b v2, September 2026), fields the most checkpoint sizes of any entrant, and then watched that same v2 checkpoint fall from 64.13 to 41.24 when the board switched to the sealed v1.6 protocol, the clearest before-and-after the category has on protocol sensitivity.**

## What it is

A family of fine-tuned Qwen3.5 decoders that read a state plus typed questions and return one probability distribution per question from one forward pass, Choice over 2 to 255 options, Score over 2 to 10 described levels, and Noul as the probability of yes.
The code is Apache-2.0 with a tests badge, the pip package pulls weights on first use (CUDA, else MPS, else CPU), and the family spans decider-2b (164,599 downloads and 111 likes on Hugging Face as of 2026-10-26), decider-4b, decider-12b (created 2026-09-29), and a 35B-A3B, plus GGUF loading for llama.cpp-class runtimes.
The README leads with game demos (Tetris, Breakout, Pong, Snake, Connect Four at one forward pass per move) and a three-line decide call, with demos, seeds, and windows documented in docs/DEMOS.md.

## Status

Active and scoreboard-native: the repository was created 2026-09-16 and pushed 2026-10-20, with 1,143 stars as of 2026-10-15 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Mapika/decider&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Mapika/decider&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Mapika/decider&type=date&legend=top-left" />
</picture>

The family's scoreboard record is the deepest of any entrant's: decider-4b v2 took JevBench's top spot at 64.13 on the sealed v1.4.2 board (2026-09-26), the first system to end Jev's first-place run, and on the current v1.6 protocol decider-12b v2 ranks fourth among open weights at 70.88 with decider chat on Gemma-4-31B at 66.08, while decider-4b v2 collapsed to 41.24 and decider-2b to 7.67 (JevBench aggregate, re-fetched 2026-10-31 with every row unchanged; the live method-v1.8 board re-bases decider-12b v2 to 73.73, official #27, fetched 2026-10-31).
On the Decision Index 0.4.1 board (edition 0.4, regenerated 2026-10-29, 248 configurations, the Full score now entirely private) the family still spans the whole range: the Decider 31B (NVFP4) holds twenty-seventh at its unchanged 66.03 (fifth of 174 on the last 0.3.2 build before the board went fully private and new entrants crowded in), Perplexity's pplx-decider v1.2 twelfth at its unchanged 67.98 and the pplx-decider Flash v1.2 (4B) eighty-first at 54.29, while decider chat on Gemma-4-31B scores 61.63 (forty-second), decider-35b-nvfp4 46.64 (104th), decider-4b 36.30 (148th), and decider-2b 23.65 (189th), against the vendor's Jev 1.14 at 60.24.
The third-party local-jev-bench suite (measured 2026-10-10) calls Decider-4B a strong generalist, level with Kev-4B and Kev-9B on transfer and ahead of Winnow on transfer and BANKING77, and Ollaya packages decider:2b and decider:4b with author calibration.

## Strengths

- **The checkpoint range is the widest in the wave, 2B to 35B-A3B, so one family covers laptop CPU to data-centre GPU budgets with the same wire format, and the 31B entry holds a top-thirty place on the Decision Index's 0.4.1 board.**
- The scoreboard record is long enough to show its own fragility: first on one protocol, fourth-and-collapsing on the next, which is more decision-useful information than a single good row.
- Per-question distributions ship for every question type (not just argmax), and the local-jev-bench third-party reading places the 4B at the top group on transfer, the one axis most replicas fail.
- Pip, server, and GGUF paths make it the easiest family to try across runtimes, and Ollaya's packaging inherits the author's calibration.

## Cautions

- **The v1.4-to-v1.6 swing (64.13 to 41.24 for the same decider-4b v2) is the wave's sharpest measured protocol collapse, so any Decider number is a property of the benchmark that produced it until someone runs a sealed replication.**
- The 2B checkpoint scores 7.67 on the current JevBench protocol and 23.65 on the Decision Index, so the family's small members are weak in absolute terms despite the download count.
- The game-heavy README demos say nothing about the calibration the contract is supposed to sell, and no independent party has re-run the served probabilities.
- The author's training data and recipe are not documented in the repository, so the 35B-A3B's underperformance (24.77 on JevBench) has no published explanation.

## Pricing

Free and open: Apache-2.0 code and weights, no hosted service and no paid tier.
The cost is your own GPU, and the pip pull is the only download step.

## Compared to

- [Jev](../jev/index.md): the closed original still leads both independent composites among single systems; Decider is the multi-size open alternative whose sealed-board record is the caution.
- [Kev](../kev/index.md): the other trained family; Kev ships the pre-registered eval discipline and a 27B flagship, Decider ships the wider size range and the deeper (and more humbling) scoreboard history.
- [Winnow](../winnow/index.md): the other community family the benches like; Winnow leads on typed-decisions accuracy per local-jev-bench, Decider leads on transfer and size range.

## Bottom line

**Recommended as the open family to serve when you need one contract across several hardware budgets, reading its numbers per protocol and per checkpoint size.**
Not for threshold logic on the 2B, and not for anyone who needs a number stable across benchmark revisions.
The disagreeable claim I will defend: decider-4b v2's fall from first to 41.24 in one protocol change is the single most valuable data point in the category, because it demonstrates, on a shipped family rather than a toy, that Jev-class scores are protocol artifacts first and model facts second.

## Changes

- 2026-10-11 - Created from the entrant scan (awesome-jev cross-check), accepted on the deepest scoreboard record in the wave, the JevBench protocol-collapse evidence recorded as the governing caution.
- 2026-10-11 - Added the star history chart.
- 2026-10-12 - Recorded the Decision Index 0.3.1 regeneration (144 configurations) where a new Decider 31B (NVFP4) took second at 65.56, the family's first top-two board position, beside the unchanged lower rows; refreshed stars to 1,128.
- 2026-10-13 - The 0.3.2 relabel and second same-day regeneration (149 configurations) rescored the 31B's second place to 64.62 with the lower rows unchanged; refreshed stars to 1,135 and the pushed date to 2026-10-12.
- 2026-10-15 - The Decision Index's 2026-10-14 regeneration (166 configurations) moved the 31B from second to third at its unchanged 64.62 as new entrant linne-oak 1.0 (65.61) passed it, with the family's lower rows unchanged; refreshed stars to 1,143.
- 2026-10-18 - Rotation re-verification: every cited URL re-fetched; the Decision Index's 2026-10-16 regeneration (174 configurations) moved the unchanged 64.62 from third to fifth as vLLM-SR d3 (66.26) and Perplexity's pplx-decider v1.2 (65.55) entered above, with the family's lower rows and JevBench's v1.6.1 rows re-confirmed unchanged, and the 2B checkpoint's counts refreshed to 334,268 downloads and 107 likes.
- 2026-10-22 - The Decision Index jumped to edition 0.4.1 (generated 2026-10-22, 226 configurations, the Full score now entirely private): the 31B (NVFP4) fell from fifth to nineteenth at 66.03 as 52 new entrants crowded the board, pplx-decider v1.2 rose to fourth at 67.98 with a new Flash v1.2 (4B) row at 54.29, and the family's lower rows rescored (chat 61.63, 35B 46.64, 4B 36.30, 2B 23.65) against Jev 1.14's 60.24; pushed date moved to 2026-10-20.
- 2026-10-26 - Rotation re-verification, every cited URL re-fetched and live: the Decision Index's same-day regeneration grew the 0.4.1 board to 229 configurations and moved the family's rows (31B still nineteenth at 66.03, chat thirty-fourth, 35B ninety-fourth, 4B 134th, 2B 172nd, Flash seventy-first), JevBench's v1.6.1 aggregate re-fetched with every Decider row unchanged, the 2B checkpoint's counts refreshed to 164,599 downloads and 111 likes, the stale 25.8 Decision Index figure in Cautions corrected to the current 23.65, and the pushed date (2026-10-20) plus local-jev-bench's strong-generalist reading re-confirmed unchanged.
- 2026-10-27 - Out-of-rotation re-fetch at the drift signal: the board's 2026-10-26 regeneration (230 configurations) crowd-shifted the family's rows one place each at unchanged scores (31B nineteenth to twentieth, chat thirty-fourth to thirty-fifth, 35B ninety-fourth to ninety-fifth, 4B 134th to 135th, 2B 172nd to 173rd, Flash seventy-first to seventy-second), and the JevBench aggregate re-fetched with every Decider row unchanged; fetched and re-cited.
- 2026-10-31 - Out-of-rotation board re-fetch at the drift signal, both boards: the Decision Index's 2026-10-29 regeneration (248 configurations) crowd-shifted the family's unchanged scores to 31B twenty-seventh, pplx v1.2 twelfth, Flash eighty-first, chat forty-second, 35B 104th, 4B 148th, and 2B 189th, and JevBench's method-v1.8 re-basing re-based decider-12b v2 to 73.73 (official #27) with the frozen aggregate rows unchanged on their re-fetch.

## See also

- [Jev](../jev/index.md) - the closed original Decider's family replicates in the open and benchmarks against
- [JevBench](../jevbench/index.md) - the scoreboard whose v1.4-to-v1.6 protocol change produced Decider's collapse
- [Winnow](../winnow/index.md) - the community family that beats Decider on typed-decisions accuracy per the third-party bench
- [Ollaya](../ollaya/index.md) - the runtime that packages decider:2b and decider:4b with author calibration
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Mapika/decider - repository: Apache-2.0, created 2026-09-16, 1,143 stars as of 2026-10-15, pushed 2026-10-20 (GitHub API, as of 2026-10-22; re-fetched 2026-10-26 with the pushed date unchanged), the family design, pip and server surfaces, and the game demos (GitHub API and README)
- https://huggingface.co/Mapika/decider-2b - the 2B checkpoint: Apache-2.0, created 2026-09-16, 164,599 downloads and 111 likes (Hugging Face API, as of 2026-10-26)
- https://huggingface.co/Mapika/decider-12b - the 12B checkpoint: Apache-2.0, created 2026-09-29 (Hugging Face API, as of 2026-10-11)
- https://benchmarkheaven.com/api/jevbench/v1.6.1 - the JevBench aggregate: decider-12b v2 at 70.88 (fourth open), decider-4b v2 at 41.24, decider-2b at 7.67, decider-35b-a3b at 24.77 (re-fetched 2026-10-31, all rows unchanged)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.4.1 rows for the family, including the 31B (NVFP4) at twenty-seventh of 248, 66.03, and the pplx-decider Flash v1.2 row at 54.29 (regenerated 2026-10-29, fetched 2026-10-31)
- https://raw.githubusercontent.com/tak-bro/local-jev-bench/HEAD/README.md - the third-party Apple Silicon reading of Decider-4B and Decider-2B (measured 2026-10-10, re-fetched 2026-10-26, the strong-generalist reading unchanged)
- https://ollaya.dev/ - Ollaya's packaged decider:2b and decider:4b rows in the accuracy and comparison tables (re-fetched 2026-10-26, the rows unchanged)
