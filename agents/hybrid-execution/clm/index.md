---
title: CLM
created: 2026-10-11
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, contrastive-learning, open-weights]
readability: 3
audience_notes: >
  Engineers who followed the Jev wave and want to know whether a non-LoRA architecture, a contrastive state-action encoder instead of a fine-tuned decoder, changes the accuracy-versus-speed trade.
  Assumes you know what an embedding encoder and a contrastive objective are, and have read this category's Jev note.
---

CLM is an Apache-2.0 System One decision model from Contrastive-LM that answers Choice, Noul, and Score questions over a TypeSafe-compatible API by scoring states against actions in embedding space, an 8B Qwen3 encoder plus a 75 MB reference head trained with a contrastive objective rather than a decision fine-tune.

**CLM is the wave's first architectural dissent: every other open entrant fine-tunes a decoder to read options, while CLM pretrains state-action agreement over 60 million pairs, and the two independent scoreboards answer that dissent with the lowest scores in the category.**

## What it is

The repository serves CLM-8B behind a TypeSafe-compatible API: a vLLM-served Qwen3-8B pooling encoder (states truncate at 2,048 tokens by default) plus a 75 MB reference head loaded by `clm-serve`, installed as `pip install contrastive-lm`.
The README reports pretraining on 60M Nemotron question-answer pairs, mid-training on 30M synthetic hard negatives, and post-training on 1M agentic trajectories, with states and actions disaggregated so their embeddings cache and reuse independently.
The shipped checkpoint is CLM-v0.1-8B on Hugging Face (Apache-2.0, created 2026-09-21), and the project claims Jev-parity on computer-use, gaming, and tool-calling tasks at up to 9x lower latency, plus a verifier state of the art from lightweight fine-tuning: 87.6 percent on Terminal-Bench 2.1 and 81.6 percent on DeepSWE (all self-run, as of 2026-10-11).

## Status

Active and star-heavy, with the boards unmoved by it, as of 2026-10-11.
The repository was created 2026-09-23 and pushed 2026-10-05, with 2,959 stars as of 2026-10-11, and the checkpoint shows 4,915 downloads and 780 likes as of 2026-10-18, the second-highest like count in this category after Laya's model card (Hugging Face and GitHub APIs).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Contrastive-LM/CLM&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Contrastive-LM/CLM&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Contrastive-LM/CLM&type=date&legend=top-left" />
</picture>

The two independent scoreboards rank it last or nearly last: JevBench's composite scores CLM-8B at 0.0 (intelligence axis 0.1, measured 2026-10-02 on the runner's protocol), and the Decision Index 0.3.2 board, as regenerated 2026-10-16 with 174 configurations, scores clm-v0.1-8b at 6.24, rank 162, against Jev's 60.11.
The third-party local-jev-bench suite calls it one of the two least accurate engines it runs, and Ollaya's own table scores clm:8b at 0.357 on typed decisions.
I read the gap between the GitHub traction and the scoreboard readings as the note's central fact: the architecture argument is winning attention while the measured decisions are not winning comparisons.

## Strengths

- The architecture is genuinely different: contrastive state-action scoring with cached, reusable embeddings is cheaper to serve at scale than a decoder forward pass per question, and it is the only entrant here whose training story is not LoRA-plus-pointer on a Qwen or Gemma base.
- The verifier results, if they reproduce, would be a category first: 87.6 percent on Terminal-Bench 2.1 as a fine-tuned verifier targets the agent-verification use this category's models keep being proposed for.
- Everything needed to run it ships: weights, server, fine-tuning tutorial, and a Discord, with the TypeSafe-compatible surface preserving drop-in code.

## Cautions

- **The scoreboard evidence is uniformly negative so far: JevBench 0.0, Decision Index 6.24 (rank 162 of 174), and last-place local-jev-bench accuracy are the only third-party readings, and none of the README's parity or verifier claims has been independently reproduced.**
- The default 2,048-token state limit is the shortest in the category against Jev's advertised 32k-plus, and raising it means raising the encoder's vLLM memory too.
- The training data recipe (Nemotron pairs, synthetic hard negatives, agentic trajectories) is described but not released, so the parity claims cannot be audited.
- The 760-like checkpoint shows a community watching rather than a community shipping: I found no downstream integrations beyond Ollaya's packaging.

## Pricing

Free and open: Apache-2.0 code and weights, no hosted service and no paid tier.
The cost is the vLLM deployment of the 8B encoder and your own GPU.

## Compared to

- [Jev](../jev/index.md): the closed original whose parity CLM claims and whose 60.11 Decision Index score CLM's 6.24 sits against; choose Jev for measured accuracy today.
- [Kev](../kev/index.md): the decoder-based replica family with the strongest eval discipline; Kev's boards disagree about it, but they do not zero it.
- [Winnow](../winnow/index.md): the other community-scale challenger on different weights, which third-party readings place in the top group rather than the bottom.

## Bottom line

**Recommended for researchers who want to test whether the contrastive architecture can be closed-loop trained into competitiveness, not for anyone choosing a decision engine by score.**
Not for production typed decisions today: the only independent readings place it at or near the bottom of the category.
The disagreeable claim I will defend: CLM's traction is a lesson about this category's audiences, the architecture story travels faster than the scoreboard row, and a reader who ships on stars rather than boards will meet the same gap Ollaya's own table already shows.

## Changes

- 2026-10-11 - Created from the entrant scan (awesome-jev cross-check), accepted on standing (2,959 stars, 760-like checkpoint) with the boards' near-zero readings recorded as the governing caution.
- 2026-10-11 - Added the star history chart.
- 2026-10-15 - The Decision Index citation moved from the stale 0.3.1 label to the current 0.3.2 board at the unchanged 6.24, now rank 154 of 166, with JevBench's 0.0 composite row unchanged.
- 2026-10-18 - Rotation re-verification: every cited URL re-fetched; the Decision Index's 2026-10-16 regeneration (174 configurations) moved the unchanged 6.24 from rank 154 to 162, JevBench's v1.6.1 rows re-confirmed (composite 0.0, intelligence 0.1), and the checkpoint's counts refreshed to 4,915 downloads and 780 likes.

## See also

- [Jev](../jev/index.md) - the closed contract CLM claims parity with and the boards measure it against
- [Kev](../kev/index.md) - the decoder-side replica family with the eval discipline CLM's claims still lack
- [Winnow](../winnow/index.md) - the community challenger the third-party benches place at the top instead
- [Ollaya](../ollaya/index.md) - the runtime whose packaged clm:8b carries the parity table's least flattering row
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Contrastive-LM/CLM - repository: Apache-2.0, the contrastive recipe, the vLLM-plus-head architecture, the Terminal-Bench 2.1 and DeepSWE claims (GitHub API and README, as of 2026-10-11)
- https://huggingface.co/Contrastive-LM/CLM-v0.1-8B - the checkpoint: Apache-2.0, created 2026-09-21, 4,915 downloads and 780 likes (Hugging Face API, as of 2026-10-18)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.3.2 board scoring clm-v0.1-8b at 6.24, rank 162 of 174, against Jev's 60.11 (generated 2026-10-16, fetched 2026-10-18; the score unchanged across the 0.3.1 and 0.3.2 builds)
- https://benchmarkheaven.com/api/jevbench/v1.6.1 - the JevBench aggregate scoring CLM-8B at 0.0 composite, intelligence axis 0.1, measured 2026-10-02 (re-fetched 2026-10-18; the served snapshot predates the site's v1.7.46 board moves, the CLM row unchanged)
- https://raw.githubusercontent.com/tak-bro/local-jev-bench/HEAD/README.md - the third-party Apple Silicon suite calling CLM one of its two least accurate engines (re-fetched 2026-10-18)
- https://ollaya.dev/ - Ollaya's packaged clm:8b at 0.357 on typed decisions, the runtime's least flattering row for the model (re-fetched 2026-10-18)
