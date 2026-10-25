---
title: Vectara Hallucination Leaderboard
created: 2026-10-13
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, benchmarks, hallucination, leaderboards]
readability: 3
audience_notes: >
  Engineers choosing models for RAG or summarization features who want a hallucination-rate read, and who need to know what that number does and does not measure.
  Assumes you know what RAG grounding and factual consistency mean.
---

The Vectara Hallucination Leaderboard ranks LLMs by how often they hallucinate when summarizing short documents, scored by Vectara's own HHEM hallucination-detection model.

**It is the only member of this category that measures a single failure mode, factual inconsistency with a provided source, and the only one whose judge is a model you can download and run against your own outputs.**

## What it is

A GitHub repository carrying the ranked table, a Hugging Face Space rendering it interactively, and the HHEM-2.1-Open judge model behind the scores.
Each refresh runs a fixed set of short-document summarization tasks per model and reports hallucination rate, factual consistency rate, answer rate, and average summary length; the README table is stamped "Last updated on October 22, 2026" (as of 2026-10-25; the previous stamp read October 16, 2026), and the Space's files were last modified 2026-10-06.
HHEM judges whether a summary is supported by its source, and it targets the case the model card calls "factual but hallucinated": an answer that is true in the world but contradicts the retrieved context.
The work began at Vectara under Simon Hughes, who died in November 2023; the repository and model card both carry a memorial line, and Vectara has kept the leaderboard and the model updated since.

## Status

Active and notably adopted for its size: the repository holds 3,318 stars and 107 forks as of 2026-10-13, pushed 2026-10-23, and the Hugging Face Space shows 203 likes with files modified 2026-10-06.
The judge model itself shows roughly 135,000 downloads on Hugging Face with a live demo Space, so the leaderboard's engine has outlived the leaderboard thread that launched it (Hugging Face, as of 2026-10-13).
The 2023 launch footprint was substantial: the leaderboard thread drew 107 points on Hacker News in November 2023, and the author pointed to a New York Times feature the same month in the Show HN thread.
The current leader is antgroup/finix_s1_32b at a 1.8 percent hallucination rate (README table, stamped 2026-10-22, unchanged leader across the September 22, October 16, and October 22 stamps).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vectara/hallucination-leaderboard&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vectara/hallucination-leaderboard&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vectara/hallucination-leaderboard&type=date&legend=top-left" />
</picture>

## Strengths

- **The number is the narrowest and most checkable in the category**: one failure mode, one task family, and a judge model anyone can download and rerun against their own summaries.
- The table lives in git, so every refresh is diffable and the history of who led when is preserved in commit history.
- The measurement has survived into practice: HHEM is used as a consistency guardrail in RAG pipelines, which is more production contact than most 2023-era eval artifacts can claim.

## Cautions

- **One vendor's model judges everyone else's models, and the vendor sells RAG products whose value rises with hallucination anxiety.**
- The task is one narrow slice: summarization of short documents, so a low rate here says nothing about tool use, agents, or long-context faithfulness.
- No published human validation or research paper grounds the scores: asked in the Show HN thread whether the rows carried human verification, the team answered that a paper might come "at some point", so every score is a model's judgment twice over, an LLM summarizing and another model judging.
- The Answer Rate column exposes a gaming vector the board does not police: a model can lower its hallucination rate by answering less, and the table itself shows the trade (Phi-4 at an 80.7 percent answer rate against a 3.7 percent hallucination rate in the same row).
- Continuity now rests on a company rather than a person: updates continued after the founding author's death, but the current maintainer set and process are undisclosed.

## Pricing

Free: the repository, the Space, and the HHEM-2.1-Open weights (an identity-gated download on Hugging Face) are public.
No paid tier exists, so no price history applies.

## Compared to

- [Artificial Analysis](../artificial-analysis/index.md): broad multi-benchmark measurement with published weights and a dated changelog; Vectara is one metric, one task, one judge.
- [LiveBench](../livebench/index.md): objective ground-truth scoring on rotating questions; Vectara's ground truth is a model's judgment of consistency, not a verified answer.
- [LLM Stats](../llm-stats/index.md): aggregates many benchmarks into a composite; Vectara isolates the single failure mode RAG builders care about.

## Bottom line

**Recommended as a directional hallucination-rate read before wiring RAG or summarization features, and as a downloadable judge for checking your own pipeline's consistency; not as a general capability signal, and not as a reason to pick one model over another by a decimal point.**
My disagreeable claim: the Answer Rate column is the most interesting number on the board, because it quietly shows that some of the least-hallucinating models are the ones that abstain the most, and no other member of this category exposes that trade.

## Changes

- 2026-10-13 - Created from the 2026-10-13 entrant scan, with the model-judged-scores caution and the answer-rate trade as the critical angles.
- 2026-10-17 - Volatile re-verification after the repository's 2026-10-17 push: the README table stamp moved to October 16, 2026 (from September 22), with the leader unchanged (antgroup/finix_s1_32b at 1.8 percent).

## See also

- [Artificial Analysis](../artificial-analysis/index.md) - the broad measurement layer this single-metric board complements
- [LiveBench](../livebench/index.md) - the objective-ground-truth contrast to a model-judged consistency score
- [LLM Stats](../llm-stats/index.md) - the aggregator that can carry a hallucination score as one input among many
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/vectara/hallucination-leaderboard - repository and table: task definition, table columns, "Last updated on October 22, 2026" stamp, top rows, memorial line (re-fetched 200, 2026-10-25, stamp moved from October 16, leader unchanged)
- https://api.github.com/repos/vectara/hallucination-leaderboard - exact counters (3,318 stars, 107 forks, Apache-2.0, created 2023-10-31, pushed 2026-10-23 as of 2026-10-25; star figure unchanged by policy) (re-fetched 200, 2026-10-25)
- https://huggingface.co/spaces/vectara/leaderboard - the interactive Space: 203 likes, files last modified 2026-10-06 (re-fetched 200, 2026-10-17, likes unchanged at 203)
- https://huggingface.co/vectara/hallucination_evaluation_model - HHEM-2.1-Open model card: the factual-but-hallucinated definition, asymmetry, identity-gated download, roughly 135k downloads, memorial (fetched 200, 2026-10-13)
- https://news.ycombinator.com/item?id=38167310 - the Show HN thread (65 points): the methodology exchange (model-judged, no human verification, a paper deferred), the New York Times mention, author participation (fetched 200, 2026-10-13)
- https://news.ycombinator.com/item?id=38286761 - the November 2023 leaderboard thread (107 points), the launch footprint (fetched 200, 2026-10-13)
- https://hn.algolia.com/api/v1/search?query=%22hallucination%20leaderboard%22&tags=story - the footprint search behind the community record (fetched 200, 2026-10-13)
