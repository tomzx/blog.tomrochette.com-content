---
title: Decider
created: 2026-10-11
updated: 2026-10-12
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
The code is Apache-2.0 with a tests badge, the pip package pulls weights on first use (CUDA, else MPS, else CPU), and the family spans decider-2b (331,214 downloads and 105 likes on Hugging Face as of 2026-10-11), decider-4b, decider-12b (created 2026-09-29), and a 35B-A3B, plus GGUF loading for llama.cpp-class runtimes.
The README leads with game demos (Tetris, Breakout, Pong, Snake, Connect Four at one forward pass per move) and a three-line decide call, with demos, seeds, and windows documented in docs/DEMOS.md.

## Status

Active and scoreboard-native: the repository was created 2026-09-16 and pushed 2026-10-07, with 1,128 stars as of 2026-10-12 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Mapika/decider&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Mapika/decider&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Mapika/decider&type=date&legend=top-left" />
</picture>

The family's scoreboard record is the deepest of any entrant's: decider-4b v2 took JevBench's top spot at 64.13 on the sealed v1.4.2 board (2026-09-26), the first system to end Jev's first-place run, and on the current v1.6 protocol decider-12b v2 ranks fourth among open weights at 70.88 with decider chat on Gemma-4-31B at 66.08, while decider-4b v2 collapsed to 41.24 and decider-2b to 7.67 (JevBench aggregate, as of 2026-10-12).
On the Decision Index 0.3.1 board the family now spans the whole range: a new Decider 31B (NVFP4) took second of 144 at 65.56 when the board regenerated 2026-10-12, while decider-4b scores 40.33, decider-35b-nvfp4 48.53, decider chat on Gemma-4-31B 57.62, and decider-2b 25.8, against Jev's 60.11.
The third-party local-jev-bench suite (measured 2026-10-10) calls Decider-4B a strong generalist, level with Kev-4B and Kev-9B on transfer and ahead of Winnow on transfer and BANKING77, and Ollaya packages decider:2b and decider:4b with author calibration.

## Strengths

- **The checkpoint range is the widest in the wave, 2B to 35B-A3B, so one family covers laptop CPU to data-centre GPU budgets with the same wire format, and the 31B entry now holds second place on the Decision Index.**
- The scoreboard record is long enough to show its own fragility: first on one protocol, fourth-and-collapsing on the next, which is more decision-useful information than a single good row.
- Per-question distributions ship for every question type (not just argmax), and the local-jev-bench third-party reading places the 4B at the top group on transfer, the one axis most replicas fail.
- Pip, server, and GGUF paths make it the easiest family to try across runtimes, and Ollaya's packaging inherits the author's calibration.

## Cautions

- **The v1.4-to-v1.6 swing (64.13 to 41.24 for the same decider-4b v2) is the wave's sharpest measured protocol collapse, so any Decider number is a property of the benchmark that produced it until someone runs a sealed replication.**
- The 2B checkpoint scores 7.67 on the current JevBench protocol and 25.8 on the Decision Index, so the family's small members are weak in absolute terms despite the download count.
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

## See also

- [Jev](../jev/index.md) - the closed original Decider's family replicates in the open and benchmarks against
- [JevBench](../jevbench/index.md) - the scoreboard whose v1.4-to-v1.6 protocol change produced Decider's collapse
- [Winnow](../winnow/index.md) - the community family that beats Decider on typed-decisions accuracy per the third-party bench
- [Ollaya](../ollaya/index.md) - the runtime that packages decider:2b and decider:4b with author calibration
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Mapika/decider - repository: Apache-2.0, created 2026-09-16, 1,128 stars, pushed 2026-10-07, the family design, pip and server surfaces, and the game demos (GitHub API and README, as of 2026-10-12)
- https://huggingface.co/Mapika/decider-2b - the 2B checkpoint: Apache-2.0, created 2026-09-16, 331,214 downloads and 105 likes (Hugging Face API, as of 2026-10-11)
- https://huggingface.co/Mapika/decider-12b - the 12B checkpoint: Apache-2.0, created 2026-09-29 (Hugging Face API, as of 2026-10-11)
- https://benchmarkheaven.com/api/jevbench/v1.6.1 - the JevBench aggregate: decider-12b v2 at 70.88 (fourth open), decider-4b v2 at 41.24, decider-2b at 7.67, decider-35b-a3b at 24.77 (fetched 2026-10-11)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.3.1 rows for the family, including the new Decider 31B at 65.56 second of 144 (generated 2026-10-12, fetched 2026-10-12)
- https://raw.githubusercontent.com/tak-bro/local-jev-bench/HEAD/README.md - the third-party Apple Silicon reading of Decider-4B and Decider-2B (measured 2026-10-10, fetched 2026-10-11)
- https://ollaya.dev/ - Ollaya's packaged decider:2b and decider:4b rows in the accuracy and comparison tables (fetched 2026-10-11)
