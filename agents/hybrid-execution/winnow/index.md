---
title: Winnow
created: 2026-10-11
updated: 2026-10-15
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, gguf, multimodal]
readability: 3
audience_notes: >
  Engineers choosing an open decision model who want the community family the third-party benches rank at the top, told with its self-run tables and private training data attached.
  Assumes you know what a LoRA merge and a GGUF quant are, and have read this category's Jev note.
---

Winnow is EldanRing's Apache-2.0 family of Gemma 4 fine-tunes (E2B, E4B, and 12B) for local typed decisions, chat, and image input, served through a MIT inference server that scores options through `/v1/systemone` without generating an explanation, distributed as merged GGUF weights with checksums.

**Winnow is the community family the independent benches agree on: Ollaya's human-labeled comparison calls winnow:12b its most accurate model (0.773, ahead of Ollama's best), local-jev-bench puts it in the top group on every set it runs, and on its own frozen panel Winnow-12B Q8 matches Jev answer for answer on JevBench's public subset while Jev keeps the transfer lead.**

## What it is

A Gemma 4 LoRA fine-tune with the adapter merged into the weights, published in three sizes (Winnow-E2B, Winnow-E4B, and Winnow-12B, the 12B created 2026-09-20 and last modified 2026-10-06), each with Q8_0, BF16, and NVFP4 GGUF targets plus an F16 vision projector for image input.
The winnow-inference server (MIT, created 2026-09-21) loads one model for both `/v1/systemone` decisions and ordinary `/v1/chat/completions`, supports noul, choice, and score with a shared state prefill and cached prefixes, and documents an RTX 5070 Ti 16 GB deployment profile for the 12B Q8 target.
The self-run panel (measured 2026-09-21, one RTX PRO 5000) scores Winnow-12B Q8 at 85.71 percent on JevBench's 231-item public subset against hosted Jev's 85.71, and 81.55 against Jev's 87.00 on Kev-v9 clean, with the training data private and not distributed.

## Status

Active and community-scale: the 12B checkpoint shows 57,761 downloads and 66 likes, the E4B 43,204 downloads, and the inference server 26 stars as of 2026-10-12 (Hugging Face and GitHub APIs).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=EldanRing/winnow-inference&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=EldanRing/winnow-inference&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=EldanRing/winnow-inference&type=date&legend=top-left" />
</picture>

On JevBench's official open-weights composite Winnow-12B Q8 ranks eighth at its unchanged 68.89 (measured 2026-10-02; fifth before the mid-October additions crowded the board past 162 ranked systems), and on the Decision Index 0.3.2 board winnow-12b-q8 scores 49.27 and winnow-e4b-q8 38.73 against Jev's 60.11.
The third-party local-jev-bench suite (12B measured 2026-10-10) reads it as top-group everywhere: transfer-v4 83 percent, level with Kev-9B and Clef, typed-decisions 71 percent level with its E4B sibling, and the suite's regression note that Winnow now beats Kev-9B on typed-decisions with non-overlapping Wilson intervals.
Ollaya's Ollama comparison calls winnow:12b its most accurate model on Bespoke Labs' 3,880 human-labeled questions, 0.773 against Ollama 0.35's best 0.749.

## Strengths

- **The third-party record is the strongest of any community family: two independent suites plus Ollaya's human-labeled table all place it at or near the top, which is the verification most of this wave still lacks.**
- The GGUF distribution with checksums, documented 16 GB deployment profiles, and vision via a projector make it the wave's most practical local download for mixed text-and-image decisions.
- The self-run panel prints the losses in the same table as the ties (Jev's 5.45-point transfer lead on Kev-v9 clean), the frankness discipline Jeff introduced, kept.
- Chat and decisions share one loaded model, so a local stack can keep one weights file for both its assistant and its decision layer.

## Cautions

- **The training data is private and the recipe undocumented, so the close-to-Jev headline cannot be audited for contamination, and the card's own "clean" caveat concedes the question.**
- Transfer is where Jev still leads (87.00 versus 81.55 on the panel's out-of-distribution additions, 69.23 against 85.64 on v9 additions), so near-parity holds on public subsets, not everywhere.
- The official composite (68.89) sits well below the public-subset accuracy the card leads with, because the composite's cost, speed, and sealed axes cut the other way.
- The inference server is a 26-star companion repo, so the weights' ecosystem rests on one small server plus third-party runtimes (Ollaya, llama.cpp-class).

## Pricing

Free and open: Apache-2.0 weights and an MIT server, no hosted service and no paid tier.
The cost is the GGUF download (12.67 GB for the 12B Q8 target) and a GPU in the 16 GB class for the documented profile.

## Compared to

- [Jev](../jev/index.md): the closed original it ties on the public subset and trails on transfer; choose Jev when out-of-distribution accuracy leads, Winnow when local, private, image-bearing decisions do.
- [Kev](../kev/index.md): the other family the benches compare it to; Kev ships the eval discipline and the 27B flagship, Winnow the better typed-decisions accuracy per local-jev-bench and the easier GGUF deployment.
- [Decider](../decider/index.md): the other community generalist; Decider leads on transfer in the same third-party bench, Winnow on typed-decisions and multilingual sets.

## Bottom line

**Recommended as the default local decision model for engineers who want the most-third-party-verified open checkpoint with text and image states, budgeting a 16 GB-class GPU for the 12B.**
Not for out-of-distribution-critical routing where Jev's transfer lead holds, and not for anyone who needs the training data behind a near-frontier score to be public.
The disagreeable claim I will defend: Winnow matching Jev answer-for-answer on a public subset is the weaker half of its case, and the stronger half is that three independent readers agree on it, which is exactly the verification Jev still does not have.

## Changes

- 2026-10-11 - Created from the entrant scan (awesome-jev cross-check), accepted on the strongest third-party verification record among the community families, the private-training-data caution recorded.
- 2026-10-11 - Added the star history chart.
- 2026-10-12 - The JevBench composite rank moved from fifth to seventh on the unchanged 68.89 as the open board grew to 152 ranked systems; refreshed the checkpoint to 57,761 downloads and 66 likes.
- 2026-10-15 - The JevBench rank moved from seventh to eighth on the unchanged 68.89 as the board passed 162 ranked systems, and the Decision Index citation moved from the stale 0.3.1 label to the current 0.3.2 board at unchanged scores (49.27 and 38.73).

## See also

- [Jev](../jev/index.md) - the closed original Winnow ties on public subsets and trails on transfer
- [Kev](../kev/index.md) - the family the benches most often compare it against
- [Decider](../decider/index.md) - the other community generalist with the opposite accuracy profile
- [Ollaya](../ollaya/index.md) - the runtime whose human-labeled comparison is Winnow's strongest third-party table
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://huggingface.co/EldanRing/Winnow-12B - the model card: Apache-2.0, Gemma 4 12B fine-tune, GGUF targets, the self-run panel against Jev, Kev, and Laya, and the private-training-data statement (fetched 2026-10-11)
- https://huggingface.co/EldanRing/Winnow-12B/raw/main/docs/BENCHMARKS.md - the benchmark report: the 85.71 versus 85.71 public-subset tie, the 81.55 versus 87.00 transfer gap, and the measurement conditions (fetched 2026-10-11)
- https://huggingface.co/api/models/EldanRing/Winnow-12B - created 2026-09-20, last modified 2026-10-06, 57,761 downloads, 66 likes (fetched 2026-10-12)
- https://github.com/EldanRing/winnow-inference - the MIT server: created 2026-09-21, 26 stars, pushed 2026-10-06, the /v1/systemone plus chat surface and the 16 GB deployment profile (GitHub API, as of 2026-10-11)
- https://benchmarkheaven.com/api/jevbench/v1.6.1 - the JevBench aggregate: Winnow-12B Q8 seventh on the open composite at 68.89, measured 2026-10-02 (fetched 2026-10-12)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.3.2 rows (winnow-12b-q8 49.27, winnow-e4b-q8 38.73), regenerated 2026-10-14, fetched 2026-10-15
- https://raw.githubusercontent.com/tak-bro/local-jev-bench/HEAD/README.md - the third-party Apple Silicon readings placing Winnow in the top group, including the Kev-9B typed-decisions regression note (fetched 2026-10-11)
- https://ollaya.dev/ - the human-labeled Ollama comparison where winnow:12b is the most accurate model at 0.773 (fetched 2026-10-11)
