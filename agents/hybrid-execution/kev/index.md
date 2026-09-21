---
title: Kev
created: 2026-09-21
updated: 2026-09-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, fine-tuning]
readability: 3
audience_notes: >
  Engineers who read this category's Jev note and want a trainable, self-hosted model that speaks the same System One API.
  Assumes you know what a LoRA adapter and a Brier score are.
---

Kev is Jared Palmer's Apache-2.0 family of small decision models (0.8B, 4B, and 9B LoRA adapters on Qwen3.5 bases) that reimplements the Jev contract on your own GPU, serving the same typed questions over an endpoint the official TypeSafe SDK can target unchanged.
Facts below verified as of 2026-09-21.

**Kev is the first Jev replica whose evaluation discipline is stronger than the vendor it replicates: pre-registered criteria, a locked test set read once per checkpoint, and published gap tables against live Jev.**

## What it is

A repository with training code, a serving server exposing `POST /v1/systemone` (noul, choice, and score questions), a web playground for option-order probes, and frozen eval suites, plus three Qwen3.5 checkpoints in a Hugging Face collection, with the earlier Qwen3 generation and a 0.5B prototype kept published.
Each checkpoint is a rank-16 LoRA adapter and a small pointer head on a fixed base, with an attention mask giving question isolation (the Qwen3.5 models' recurrent DeltaNet layers run each question as its own row against a shared state cache).
Code and weights are Apache-2.0, matching the Qwen bases, and the author credits the [Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked) write-up for the design and notes the project was built with Devin.
The API tests run TypeSafe's own example requests against the local server, which is the compatibility claim made testable.

## Status

**Active and four days old, with traction that clears the bar on author standing and the eval ecosystem rather than on thread points.**
The repository was created 2026-09-17 and pushed the day I verified, with 1,347 stars and 77 forks as of 2026-09-21, and two releases (the 0.5B prototype on 2026-09-17, the 0.8B/4B/9B family on 2026-09-20).
The Hacker News thread (2026-09-21) sat at about 30 points and 16 comments, below this category's 100-point bar, and I state that gap explicitly.
What carries it over: the author is the Turborepo founder, now VP of Engineering at Cognition, with 10,408 GitHub followers, and the thread drew substantive use-case discussion (coding-agent verifiers, spam filtering, knowledge-cutoff concerns) rather than drive-by upvotes.
Most tellingly, the README converts two independent third-party test sets, SemIf's 144 authored decisions and scienthoon's 900-ticket Jev calibration, and scores its models against those projects' own published live-Jev results.

## Strengths

- **Verifiability is designed in: the research log records pre-registered adopt criteria, a locked test read once, and a gap table that concedes every weakness (MMLU 0.74 versus Jev's 0.90, Brier 0.291 versus 0.211, confident errors 7.5% versus 3.7%).**
- API compatibility is the practical hook: point the TypeSafe SDK at `127.0.0.1` and code written against Jev runs locally.
- External test sets score well: on SemIf's decisions Kev-9B takes 0.917 against Jev's 0.965, and on scienthoon's tickets it wins routing 0.952 versus 0.897 while essentially tying tone (0.911 versus 0.914).
- `--init_from` delta fine-tunes are minutes, not hours, and one user's report on 836 support-tool decisions kept 0.83 on Kev's own eval while reaching 0.88 on the new domain.
- The limitations section names failure modes by number, including that fine-tuning erodes the base's date arithmetic (0.82 to 0.72 on deadline questions).

## Cautions

- Calibration is the gap that matters for threshold logic: on new-source data Kev-4B assigns at least 0.9 probability to a wrong answer on 8.2% of questions (7.5% for the 9B), so test on your own data before branching on confidence.
- Mac latency regressed with the Qwen3.5 bases (4B: 779 ms versus 174 ms on the deprecated Qwen3 checkpoint), and the planned MLX backend is not shipped.
- Option order can flip answers despite question isolation, training covered only 384-token states against the 8,192-token serving limit, and the single-threaded server has no authentication.
- Every comparison to Jev is self-run and admittedly uncontrolled, since nobody knows what Jev was trained on.

## Pricing

Free and open: Apache-2.0 code and weights on Hugging Face, no hosted tier and no paid plan.
The real cost is hardware and training spend if you reproduce the family; the author's logged budget was about $475 of a $500 overnight authorization on rented H100s.

## Compared to

- [Jev](../jev/index.md): the closed original keeps 32k-plus context and better calibration; choose kev when the API contract matters more than those two things and you want inspectable weights you can fine-tune.
- [Laya](../laya/index.md): the other multi-checkpoint open family; Laya is encoder-scale, multilingual, and routed, while kev is decoder-scale, English-focused, and drop-in compatible with the TypeSafe SDK.
- [Nimble](../nimble/index.md): the one-day recipe with a human-labeled external benchmark suite; choose kev for the maintained server, playground, and delta fine-tuning path, Nimble for the curation method.

## Bottom line

**Recommended for engineers who want the System One contract running on their own hardware with a real evaluation harness, and who will fit decision thresholds on their own data rather than trusting the shipped calibration.**
Not for low-latency Mac serving today, for long-context states, or for anyone who needs Jev-level calibration out of the box.
The disagreeable claim I will defend: the weights are the second-most valuable artifact here, and the pre-registered, locked-test research log is the first, because it is a higher evidentiary standard than the closed vendor it replicates, and the rest of this category should be judged against it.

## Changes

- 2026-09-21 - Created from the owner-prompted open-alternative scan; accepted below the 100-point HN bar on author standing, star traction, and the external-eval ecosystem.

## See also

- [Jev](../jev/index.md) - the closed model whose System One API kev reimplements locally
- [Laya](../laya/index.md) - the other open-weights decision family, encoder-scale and multilingual
- [Nimble](../nimble/index.md) - the contrastive-curation recipe trained on Qwen3.5-9B
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the planner that sits above a decision layer gets chosen

## References

- https://github.com/jaredpalmer/kev - repository: Apache-2.0, created 2026-09-17, 1,347 stars, 77 forks (GitHub API, as of 2026-09-21)
- https://raw.githubusercontent.com/jaredpalmer/kev/main/README.md - the LoRA-plus-pointer-head architecture, question isolation, eval tables against Jev, serving and training limits
- https://raw.githubusercontent.com/jaredpalmer/kev/main/PLAN.md - the pre-registered research log: gap table to Jev, locked-test discipline, the $475-of-$500 budget
- https://news.ycombinator.com/item?id=49783999 - the launch thread (about 30 points, 16 comments as of 2026-09-21), its use-case confusion and bandwagon skepticism the critical signals
- https://huggingface.co/collections/jaredpalmer/kev-6aad9d0ea49f2589665e07cd - the weight collection; kev-4b created 2026-09-19, Apache-2.0, 170 downloads (as of 2026-09-21)
- https://github.com/TheoLeeCJ/SemIf - the independent 144-decision test set (2,680 stars) whose live-Jev results kev converts and scores against
- https://github.com/scienthoon/jev-ood-calibration - the independent 900-ticket Jev calibration whose test set appears in kev's external evals
- https://archerhume.com/posts/jevs-architecture-unmasked - the architecture write-up kev credits for the design
- https://github.com/jaredpalmer - the author's profile grounding the Turborepo and Cognition standing
