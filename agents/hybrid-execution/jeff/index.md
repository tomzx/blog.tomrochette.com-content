---
title: Jeff
created: 2026-09-29
updated: 2026-10-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, fine-tuning]
readability: 3
audience_notes: >
  Engineers who followed the Jev wave and want a small, fine-tunable model that speaks the Jev request format on their own hardware.
  Assumes you know what a fine-tune and a fitted temperature are.
---

Jeff is an MIT-licensed family of small Jev-compatible decision models, three fine-tunes (Qwen3.5-0.8B, Qwen3.5-2B, and Gemma 4 E2B) that read a situation plus plain-word options and return one calibrated probability per option in a single forward pass, served locally in Jev's request format.

**Jeff ships the frankest self-run benchmark table the wave has produced: it matches hosted Jev's published overall accuracy (83.1 versus 83.0) while conceding every reasoning-heavy benchmark, and it prints the losses in the same table as the wins.**

## What it is

A fork-line of AutoJev, Denis Yarats' MIT recipe that fine-tunes Qwen3.8-27B for Jev-style decisions: Jeff keeps the core design (one forward pass per decision, a trained answer readout, one fitted temperature for calibration) and swaps in small students (0.8B and 2B Qwen3.5, Gemma 4 E2B), a local synthetic-data pipeline with a leak filter, and MLX serving on Apple Silicon.
Three checkpoints on Hugging Face under mstrasser (Apache-2.0 weights), a local server exposing `/v1/systemone` with Jev's choice, noul, and score questions, and an independence disclaimer ("not affiliated with or endorsed by TypeSafe") in the README.
Training ran entirely on local hardware: one RTX PRO 6000 workstation GPU (the 0.8B trains in about 2 hours, the 2B in about 3.5), synthetic data written by an open model (Qwen3.8-Flash-Next) on two DGX Sparks, and no closed-model output in the training data.
The training data itself is not released (some sources are share-alike), and since 2026-10-05 the project has been organized around v1.3: an adapter-first base (deliberately weaker zero-shot on long option lists, with a prompt layout built for caching), fifteen task adapters with GGUF exports for llama.cpp (licences differ by adapter: sanctions and soc are CC BY-NC 4.0, aml and trading-desk carry data-source terms), and Jeff-Code, two adapters that let the 0.8B decide when a paired Qwen3.8-27B should think, now shipped in their own firelex/jeff-code repository built on the Pi agent, with jeffhub.ai as the results and docs hub.

## Status

Twenty-two days old and shipping: the launch Show HN thread (2026-09-28) reached 576 points as of 2026-10-20.
The repository was created 2026-09-28 and pushed 2026-10-07, with about 1,500 stars and 73 forks; the v1.2 checkpoints on Hugging Face now live under a jeff-legacy org that the README's original links redirect to, with 3,053 downloads registered for the 0.8B as of 2026-10-20.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=firelex/jeff&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=firelex/jeff&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=firelex/jeff&type=date&legend=top-left" />
</picture>

Latency is the headline: about 22 ms per decision on an RTX PRO 6000, 28 ms on an M4 Max through MLX, 463 ms on a 32-thread CPU, against Jev's published 114-212 ms per API call in its Doom runs (not measured on the same hardware); the v1.3 base and adapters measure 26.6 to 31.8 ms per decision on the same idle GPU as v1.2 (October 5 table).
The self-run benchmarks cover 4,599 questions from five public suites (BBH, Financial PhraseBank, JudgeBench, RAGTruth, WinoGrande) plus JevBench's public hard tier scored separately: Jeff-2B posts 83.1 overall against Jev's published 83.0 and AutoJev-27B's 84.9, winning Financial PhraseBank (96.3 versus 77.0) and RAGTruth (88.9 versus 77.3) while staying well below Jev on BBH (68.0 versus 94.3), JudgeBench, WinoGrande, and the JevBench hard tier (53.3 versus 73.3).
The v1.3 Jeff-Code claim is the agent-facing headline: paired-equal quality (62.4 percent against 62.8 percent pass rate over 1,242 paired tasks) at 47 percent faster per task (0.68x the baseline's time, 32 percent less time), with no clear speed-up on Terminal-Bench 2.0 or SkillsBench, all self-run.
Zero-shot games back the generality claim: Jeff-0.8B took 57.0 of 98 Pac-Man pellets against 11.2 for random moves, and Doom kills matching a hand-coded rule bot.
None of it has been checked by a third party, and JevBench's board, which listed no Jeff checkpoint when this note was written, now carries Jeff-1.0-Large at official rank twelve of 184 (composite 68.6, capability 81.5, third behind basal-omni-1.0-ultra's 82.5 and Quyet-1.0-Large's 81.7, as of the 2026-10-20 read of board v1.7.46, updated 2026-10-18), so the family's accuracy claim has a first outside reading even though the board's methodology remains the contested one-runner design.

## Strengths

- **The benchmark table argues against itself in public: reasoning-tier losses to Jev are printed next to classification wins, which is the evidence discipline this category's launch posts skipped.**
- Speed at 0.8B scale is real and local: 22 ms on one workstation GPU, 28 ms on a laptop-class Apple chip, no API and no waitlist.
- The fine-tune path is demonstrated, not promised: a voice-navigation fine-tune moved held-out accuracy from 31.7% to 95.8% in under half an hour on one GPU.
- Everything needed to re-run or retrain ships in the repository: training scripts, data-source licenses, leak filter, and a dashboard.

## Cautions

- **The launch thread's real-world reports split hard: one commenter measured 70% for Jeff against 94% for Jev on his own classification and called it unacceptable, and another called the 0.8B "completely useless" on job-ad classification, so the zero-shot numbers do not transfer to every domain.**
- "Trained at home" ran on an RTX PRO 6000 plus two DGX Sparks, which is workstation spending, not hobbyist hardware, and the thread said so.
- Hard option ceilings by checkpoint: the Qwen models take up to 254 options (widened from the original A-Z coding in v1.1) and the Gemma E2B checkpoint still caps at 26; inputs beyond the trained 8,192 tokens are refused with a 422 unless `JEFF_MAX_TOKENS` raises the limit, and accuracy beyond that length is unmeasured.
- Benchmark scores do not predict game play (the 2B plays the games worse than the 0.8B), forecasting-style questions score at random, and it is English and text only.
- Every comparison to Jev is self-run against published figures measured on different samples, and no third party has verified any of it.

## Pricing

Free and open: MIT-licensed code (including AutoJev's notice) and Apache-2.0 weights on Hugging Face, no hosted service and no paid tier; the v1.3 adapter weights split by licence, sanctions and soc CC BY-NC 4.0 and aml and trading-desk under their data sources' terms, so commercial reuse needs an adapter-by-adapter check.
The cost is your own GPU and, if you retrain, the synthetic-data generation run.

## Compared to

- [Jev](../jev/index.md): the closed original wins every reasoning-heavy benchmark and carries no weights; Jeff wins the classification slices and runs at 22 ms on your own machine, which is exactly the trade its README states.
- [Kev](../kev/index.md): the other Jev-API-compatible family; kev ships the pre-registered locked-test eval discipline and delta fine-tunes, Jeff ships the frankest benchmark table and the cheaper training recipe.
- [NanoJev](../nanojev/index.md): the other small self-run replica; NanoJev benchmarked games with zero community attention, Jeff arrived with a 573-point thread in its first week.

## Bottom line

**Recommended for engineers who want a small Jev-format student model they can specialize on their own data in an afternoon, and for studying how far 0.8-2B fine-tunes close on a frontier decision API.**
Not as a Jev replacement on reasoning-heavy workloads, and not for anyone who needs a number a second party has confirmed.
The disagreeable claim I will defend: matching Jev's published overall while conceding every reasoning benchmark is the strongest evidence yet that the decision contract and the reasoning are separable, which is this category's founding thesis made falsifiable on a workstation GPU.

## Changes

- 2026-09-29 - Created from the entrant scan after the 2026-09-28 Show HN thread cleared the bar (471 points, the frankest benchmark table in the wave).
- 2026-10-06 - Recorded the v1.3 restructure (adapter-first base, fifteen adapters with GGUF exports, Jeff-Code's paired-equal-quality-at-47-percent-less-time claim, the v1.2 checkpoints' move to a jeff-legacy Hugging Face org) and refreshed traction (about 1,400 stars, 575-point thread, pushed 2026-10-05).
- 2026-10-06 - Corrected the age claim (created 2026-09-28, eight days old, not three weeks).
- 2026-10-07 - Added the firelex/jeff star history chart to the Status section.
- 2026-10-15 - JevBench's board, which listed no Jeff checkpoint at the last verification, now carries Jeff-1.0-Large at official rank ten of 162 (composite 68.6, capability 81.5 second), the family's first third-party board reading; the note's no-board claim corrected.
- 2026-10-20 - Rotation re-verification, every cited URL re-fetched, with two corrections the current README forced: the Jeff-Code speedup reads 47 percent faster per task (0.68x the baseline, 32 percent less time), not 47 percent less task time as this note had it, and the hard 26-option ceiling belongs to the Gemma E2B checkpoint alone, the Qwen models having taken 254 options since v1.1 with an 8,192-token input cap since v1.3; also recorded Jeff-Code's move into its own firelex/jeff-code repository on Pi with jeffhub.ai as the hub, the adapter licence split (sanctions and soc CC BY-NC 4.0), the board row's move to official #12 of 184 (composite 68.6, capability third), the thread at 576 points, and the 0.8B checkpoint at 3,053 downloads under the jeff-legacy redirect.

## See also

- [Jev](../jev/index.md) - the closed original whose request format Jeff speaks and whose published numbers anchor the benchmark table
- [Kev](../kev/index.md) - the other Jev-API-compatible open family, with the stricter eval discipline
- [JevBench](../jevbench/index.md) - the third-party scoreboard whose hard tier appears in Jeff's table as a separately-scored column
- [NanoJev](../nanojev/index.md) - the other small self-run replica, games instead of public benchmarks
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/firelex/jeff - repository: MIT, created 2026-09-28, about 1,500 stars, 73 forks, pushed 2026-10-07 (GitHub API, as of 2026-10-20)
- https://raw.githubusercontent.com/firelex/jeff/main/README.md - the benchmark table, games, speed table, caveats, the Jeff-Code repository and jeffhub.ai links, and the AutoJev lineage (re-fetched 2026-10-20)
- https://huggingface.co/mstrasser/Jeff-Qwen3.5-0.8B - the 0.8B checkpoint: Apache-2.0, created 2026-09-28, redirecting to the jeff-legacy org, 3,053 downloads as of 2026-10-20
- https://news.ycombinator.com/item?id=49883844 - the launch thread (576 points as of 2026-10-20, 2026-09-28), including the negative reports from classification use outside the benchmark suites
- https://github.com/denis-pplx/autojev - the parent recipe: MIT, 120 stars, fine-tunes Qwen3.8-27B for Jev-style decisions (re-verified 2026-10-20)
- https://benchmarkheaven.com/jev-models - the live board (v1.7.46, updated 2026-10-18) carrying Jeff-1.0-Large at official #12 of 184, composite 68.6 (capability 81.5, third) (fetched 2026-10-20)
