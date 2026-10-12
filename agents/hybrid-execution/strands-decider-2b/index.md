---
title: Strands Decider 2B
created: 2026-10-12
updated: 2026-10-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights]
readability: 3
audience_notes: >
  Engineers tracking who ships the decision-model contract as a vendor product, and whether a hyperscaler-backed open checkpoint is worth a slot beside the community fine-tunes.
  Assumes you know what a LoRA adapter and a Brier score are, and have read this category's Jev note.
---

Strands Decider 2B is the Strands Agents team's Apache-2.0 decision model, a 2B LoRA-plus-pointer readout on Qwen3.5 that answers choice, score, and yes/no questions with calibrated confidence in one pass, shipped with a pip CLI and positioned as the decision component for agentic workflows built on the Strands Agents SDK.

**This is the wave's second company-built open checkpoint, and the first from a hyperscaler's agent team, and it arrives with the strongest self-run evaluation culture in the category and the weakest third-party result: the seed tables and calibration contract are published to a standard nobody else matches, while the one independent board that has measured it ranks it 107th of 144.**

## What it is

A small decision model in this category's standard pattern: a state and typed questions go in, one probability per option comes out, no generated text.
The released checkpoint, `strands-decider-2B-qwen3.5-v1-2610` on Hugging Face, is a rank-48 adapter plus a readout head trained on a 246,678-row mix whose builders describe every source family, drop the 20,000 rows whose terms restrict commercial use, and use an Apache-2.0 Gemma 4 teacher with Claude only as an independent row filter whose text never enters the data.
The v1 checkpoint is a soup of three training runs (the per-layer mean of three seeds' LoRA updates with stacked heads), anchored to the previous release with a KL term so answers do not drift.
Serving is a pip CLI (`pip install strands-decider`, PyPI 0.1.0) with CPU, CUDA, MPS, and MLX extras, MLX running 1.4 to 1.6x faster than MPS on Apple silicon per the README.
It comes from strands-labs, the org behind the Strands Agents SDK, an AWS-backed agent framework, and the README positions the model as a natural fit for decisions inside workflows built on that SDK.

## Status

Active and fresh: the repository was created 2026-09-29 and pushed 2026-10-09, with 585 stars and 77 forks, and the Hugging Face checkpoint was published 2026-10-09, too recently for the Hub's download counter, with 5 likes (GitHub and Hugging Face APIs, as of 2026-10-12).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=strands-labs/strands-decider&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=strands-labs/strands-decider&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=strands-labs/strands-decider&type=date&legend=top-left" />
</picture>

The launch post (2026-10-07) drew a 285-point Show HN thread, above the bar most of this wave cleared, and the tone was warmer than most decision-model threads: early commenters reported on-device deployments rather than methodology fights, one running it in a browser extension to filter email.
The self-run evidence is unusually disciplined: evaluation/results.md publishes per-seed tables next to the soup's numbers (JevBench public items 180 of 231 tasks right, Brier 0.280, ECE 0.072, HotpotQA 0.832 never trained on), states that the training-data builders are not yet on `main` so the data cannot be rebuilt from the repository, and dates every measurement.
The headline reliability claim is a confidence contract: on short classification tasks it has never seen, answers at confidence 0.9 or higher are right about 95 percent of the time, with "confirm or ask a person" below that, which is the deployment logic the calibrated-probability columns all promise.
The one independent reading so far is adverse: the Decision Index 0.3.1 board (regenerated 2026-10-12, 144 configurations) scores strands-decider-2b at 21.75, rank 107, against hosted Jev's 60.11 at ninth, while the project's own balanced-skill self-run reads 30.82, and JevBench carries no row for it yet.

## Strengths

- **The evaluation culture is the strongest in the category: per-seed results beside the released soup, a KL anchor to the previous release, held-out sets named with their train-split relationships disclosed, and a calibration contract stated as a number you can act on.**
- Vendor standing is concrete: the Strands Agents SDK is one of the major agent frameworks, and a decision model shipped as its native component is the distribution path the H2O note predicted would crowd the individuals.
- The data mix is documented past what most of the wave publishes, including the commercially restricted rows it removed and the teacher-versus-filter roles of the two LLMs.
- Small enough for CPU and Apple-silicon serving with a pip one-liner, which keeps the deployment story inside processes no GPU touches.

## Cautions

- **The only third-party reading is near the bottom of the board: 21.75 against Jev's 60.11 on the Decision Index, with no JevBench row yet, so the calibration contract is self-run until a second board confirms it.**
- 585 stars and a checkpoint too new for download counts make this the weakest traction of any admitted entry in this wave; the thread's warmth has not yet become deployments at scale.
- The training-data builders are not on `main`, so the one thing the results tables imply you could check, the data, cannot be rebuilt from the repository yet.
- The project is tied to the Strands SDK's roadmap, and the README's own framing ("an experimental typed classifier" on PyPI) keeps expectations deliberately low.

## Pricing

Pricing does not apply: Apache-2.0 code and weights, a free PyPI package, and no hosted service.
The cost is your own hardware, and the 2B size keeps that small.

## Compared to

- [Jev](../jev/index.md): the closed original whose published numbers this model's self-run tables use as yardsticks; Jev keeps the latency and the SLA, Strands Decider ships inspectable weights with a calibration contract.
- [Decider](../decider/index.md): the open family with the widest checkpoint range, whose new 31B ranks second on the Decision Index where Strands' 2B ranks 107th; choose Decider for measured accuracy across budgets, Strands Decider for the eval discipline and the SDK tie-in.
- [H2O-Lightning-4B](../h2o-lightning-4b/index.md): the other company-built open checkpoint, measured first on the board that has not measured this one; the two are the test case for whether vendors or individuals populate this category.

## Bottom line

**Recommended for engineers inside the Strands ecosystem who want a local, calibrated decision component with published per-seed evidence, and for anyone studying how a vendor should disclose a training run.**
Not as a measured engine today: one adverse third-party reading and no second board row.
The disagreeable claim I will defend: the fair comparison is not with the community fine-tunes but with the vendor APIs, and Strands Decider is the first open artifact whose confidence contract is stated precisely enough to be falsifiable, which is worth more than the 60 points of Decision Index score separating it from Jev.

## Changes

- 2026-10-12 - Created from the entrant scan (HN and release-feed sweep), accepted on the 285-point thread, AWS Strands team standing, and the published seed-level evaluation culture, with the adverse Decision Index reading recorded as the governing caution.

## See also

- [Jev](../jev/index.md) - the closed contract this model reimplements openly and self-measures against
- [Decider](../decider/index.md) - the open family measured beside it on the Decision Index, 65.56 versus 21.75
- [H2O-Lightning-4B](../h2o-lightning-4b/index.md) - the other vendor-built open checkpoint in the wave
- [Kev](../kev/index.md) - the pre-registered-eval precedent this project's seed tables most resemble
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/strands-labs/strands-decider - repository: Apache-2.0, created 2026-09-29, 585 stars, 77 forks, pushed 2026-10-09, the CLI surfaces and device extras (GitHub API and README, as of 2026-10-12)
- https://strandsagents.com/blog/introducing-strands-decider/ - the launch post: the decision-model positioning, the confidence contract, and the SDK tie-in (fetched 2026-10-12)
- https://raw.githubusercontent.com/strands-labs/strands-decider/main/evaluation/results.md - the seed tables, the soup design, the KL anchor, the data-mix disclosure, and the not-yet-rebuilt-data statement (fetched 2026-10-12)
- https://huggingface.co/StrandsAgents/strands-decider-2B-qwen3.5-v1-2610 - the checkpoint: Apache-2.0, published 2026-10-09, 5 likes, downloads not yet tracked (Hugging Face API, as of 2026-10-12)
- https://news.ycombinator.com/item?id=49987076 - the 285-point launch thread (2026-10-07, fetched via the Algolia items API), its on-device deployment reports the early traction evidence
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.3.1 board scoring strands-decider-2b at 21.75, rank 107 of 144 (generated 2026-10-12, fetched 2026-10-12)
- https://pypi.org/project/strands-decider/ - the package, 0.1.0, self-described as an experimental typed classifier (fetched 2026-10-12)
