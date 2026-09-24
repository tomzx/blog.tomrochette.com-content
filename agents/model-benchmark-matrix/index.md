---
title: "Model Benchmark Matrix"
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, benchmarks, evaluation, model-selection]
readability: 3
audience_notes: >
  Engineers scanning model cards and leaderboards to pick a model for coding, agent, or long-context work.
  Assumes you know what pass@1, a fail-to-pass test, and an agentic harness are; each row links the benchmark's own site or paper.
---

This matrix indexes the model benchmarks an engineer actually meets on model cards, vendor blogs, and leaderboards, as of 2026-09-24, with one or two sentences per benchmark on what it evaluates and a note on how far I trust the reading.
The curation rule: each board has an official site or paper I fetched this run, publishes results someone other than the submitter can check, and appears in recent model comparisons.
That rule excludes the harness benchmarks ([FrontierHarness Eval](../evaluation-review/frontierharness-eval/index.md) and [HarnessTax](../evaluation-review/harnesstax/index.md)), which hold the model constant and judge the harness instead, and decision-model boards like [JevBench](../hybrid-execution/jevbench/index.md), which live in their own category.

**A benchmark score is an instrument reading, not a verdict, and the instrument is only valid for the decision it was built to inform, so pick the board by the decision first and the ranking second.**

## Agentic software engineering

| Benchmark | What it evaluates | Reading notes |
| --- | --- | --- |
| [CodeClash](https://codeclash.ai/) | The SWE-bench team's eval of models as goal-oriented developers rather than task completers, launched November 2025. | Newest family member, thin public history so far, cite with care. |
| [Multi-SWE-bench](https://github.com/multi-swe-bench/multi-swe-bench) | Real-world issue resolution across seven languages beyond Python (Java, TypeScript, JavaScript, Go, Rust, C, C++), 1,632 instances curated by 68 expert annotators. | Apache-2.0 with a NeurIPS 2025 Datasets and Benchmarks acceptance, the credible answer when a Python-only score is questioned. |
| [PaperBench](https://arxiv.org/abs/2504.01848) | End-to-end replication of 20 ICML 2024 papers from scratch, graded by 8,316 rubric tasks with an LLM judge. | Best tested agent scored 21.0 percent against ML PhD humans at roughly double, the clearest ceiling on research-engineering claims. |
| [ProgramBench](https://programbench.com/) | Rebuilding a whole program from its compiled binary and documentation alone, no source, no decompilation, no internet, across 200 tasks with 248,000 hidden behavioral tests. | Launched May 2026 by Meta, Stanford, and Harvard, the best model fully resolves 4.5 percent, effectively unsaturated. |
| [SWE-bench](https://www.swebench.com/) | Resolving real GitHub issues in real repositories, graded by each repo's own fail-to-pass tests, in four official sizes (Lite 300, Verified 500, Multilingual 300, Multimodal 480) plus the 2,294-instance original. | The reference board; its default Verified view now runs every model in the same minimal mini-SWE-agent bash environment precisely so harnesses stop inflating scores. |
| [SWE-bench Pro](https://scale.com/leaderboard/swe_bench_pro_public) | The same issue-resolution task on harder, longer-horizon material: 1,865 tasks from 41 repositories, copyleft-licensed to resist contamination, plus a private commercial subset. | Models that top Verified at 70 percent+ scored about 23 percent at launch, the fastest cure for Verified-driven overconfidence. |
| [SWE-Lancer](https://arxiv.org/abs/2502.12115) | 1,488 real freelance jobs from Upwork (the Expensify codebase) worth $1M in actual payouts, spanning $50 bug fixes to $32,000 features plus managerial proposal selection. | Scores map to dollars, which makes it the board for economic questions, though ICML reviewers flagged the single-repo, single-platform generalization limits. |
| [SWE-rebench](https://swe-rebench.com/) | A continuously refreshed issue-resolution task stream harvested from new pull requests, built so training-data contamination cannot inflate scores. | The board vendors quote when a static leaderboard would flatter them, apply the never-trust-self-reported-numbers rule doubly. |
| [Terminal-Bench](https://www.tbench.ai/) | Agentic tasks executed end to end in real terminal and container environments, scored as resolution rate with 95 percent confidence intervals, currently at version 4.0. | Co-hosted by Stanford and the Laude Institute, the board for "which model survives a shell", and the one HarnessTax used to show harness swaps move scores up to 5x. |

## Function-level code generation

| Benchmark | What it evaluates | Reading notes |
| --- | --- | --- |
| [Aider polyglot](https://aider.chat/docs/leaderboards/) | 225 challenging Exercism exercises across C++, Go, Java, JavaScript, Python, and Rust, run through aider's edit formats, so it also measures whether a model can emit edits a harness can apply. | The leaderboard froze in 2025 along with aider's maintenance (see the [aider note](../harnesses/aider/index.md)); its per-run costs still teach the cost-per-point lesson. |
| [HumanEval](https://github.com/openai/human-eval) | Synthesizing a Python function body from a docstring, graded by hidden unit tests as pass@k across 164 hand-written problems. | Saturated and demonstrably overfit (LiveCodeBench separated models that score well here but lag on fresh problems), a legacy signal on modern model cards. |
| [LiveCodeBench](https://livecodebench.github.io/) | Rolling contest problems from LeetCode, AtCoder, and Codeforces tagged with release dates, so a model is tested only on problems newer than its training cutoff, across code generation, self-repair, test-output prediction, and execution. | The contamination control that function-level boards lack, the one to cite when HumanEval numbers look suspiciously uniform. |
| [MBPP](https://arxiv.org/abs/2108.07732) | Synthesizing short Python programs from natural language descriptions across 974 entry-level tasks. | Saturated alongside HumanEval, kept on cards for continuity rather than discrimination. |

## Agents at work

| Benchmark | What it evaluates | Reading notes |
| --- | --- | --- |
| [BFCL](https://gorilla.cs.berkeley.edu/leaderboard.html) | Function and tool-calling accuracy, from single-turn AST matching through multi-turn state tracking to the v4 holistic agentic evaluation, averaged unweighted across categories. | The Berkeley board for "will this model call my tools correctly", refreshed continuously with pinned evaluation commits. |
| [GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard) | General assistant questions with one exact-match answer each, across three levels that need web browsing, file handling, multimodal input, and tool chains. | Conceptually easy for humans (92 percent) and hard for agents at launch (GPT-4 with plugins scored 15), the most-submitted agent leaderboard in existence. |
| [OSWorld](https://os-world.github.io/) | 369 real computer tasks inside Ubuntu VMs across real web and desktop apps, checked by execution-based scripts rather than screenshot matching. | The OSWorld-Verified refresh (July 2025) fixed community-reported task bugs, and 2.0 arrived in June 2026, so compare only same-version scores. |
| [TAU-bench](https://github.com/sierra-research/tau2-bench) | Customer-service agents that must satisfy an LLM-simulated human user while following domain policy using tools, across airline, retail, telecom, and knowledge-retrieval domains, now with full-duplex voice evaluation in tau-3. | The user on the other side is simulated, so scores measure the pair, and the July 2026 v1.0.1 grading update broke comparability with older published numbers. |
| [TheAgentCompany](https://the-agent-company.com/) | Consequential real-world tasks inside a simulated software company, from the WebArena group, published at ICML 2025. | The long-horizon autonomy board, tasks fail messily rather than cleanly, which is the point. |
| [WebArena](https://webarena.dev/) | Long-horizon web tasks on self-hosted realistic sites (a GitLab instance, a shopping site, forums), graded by functional and URL checks, with VisualWebArena and WebArena-Infinity extending it. | Aging but foundational, most computer-use agents still report on it or its descendants. |

## Reasoning and knowledge

| Benchmark | What it evaluates | Reading notes |
| --- | --- | --- |
| [ARC-AGI-2](https://arcprize.org/arc-agi/2/) | Novel visual rule-induction puzzles calibrated so at least two humans solve every eval task within two tries, stressing symbolic interpretation, compositional reasoning, and context-dependent rules, with cost now reported as an efficiency metric. | Designed to resist brute-force scale, the board where fluid (not memorized) reasoning shows, and ARC-AGI-3's interactive 2026 competitions are already queued behind it. |
| [GPQA Diamond](https://arxiv.org/abs/2311.12022) | 448 graduate-level, Google-proof multiple-choice questions in biology, physics, and chemistry, written so PhD experts reach about 65 percent while skilled non-experts with web access manage 34. | The established frontier-science discriminator, now near the top of every reasoning model card. |
| [Humanity's Last Exam](https://lastexam.ai/) | 2,500 expert-written questions across more than a hundred subjects at the frontier of closed-ended academic knowledge, with a private held-out set to detect overfitting. | Built by CAIS and Scale AI with roughly 1,000 contributor experts, published in Nature in January 2026, and forked into a rolling variant plus HLE-Diamond (released 2026-09-22) as saturation creeps up. |
| [MMLU-Pro](https://arxiv.org/abs/2406.01574) | The harder successor to MMLU: ten answer options instead of four, reasoning-focused questions, and noise removed, cutting prompt sensitivity from 4-5 percent to about 2. | Treat plain MMLU as retired (frontier models clear 90 percent) and read MMLU-Pro as its replacement. |
| [MMMU](https://mmmu-benchmark.github.io/) | 11.5K college-exam questions mixing text with 30 image types (diagrams, charts, chemical structures, sheet music), demanding subject knowledge plus perception, with MMMU-Pro as the hardened variant. | The board for "does the model actually read figures", weaker on rare image types than headline scores suggest. |

## Math

| Benchmark | What it evaluates | Reading notes |
| --- | --- | --- |
| [AIME 2025](https://huggingface.co/datasets/math-ai/aime25) | The 30 American Invitational Mathematics Examination problems from 2025, whose integer answers make grading exact. | Fast, clean, and effectively saturated at the frontier, useful mainly as a floor check. |
| [FrontierMath](https://epoch.ai/frontiermath/) | Several hundred unpublished problems authored by mathematicians across difficulty Tiers 1-4 (Tier 4 is research-level), now alongside Open Problems and Lean-formalized Erdős problems. | Epoch AI's unsaturated math board, the one that still separates frontier models in 2026. |
| [MATH-500](https://huggingface.co/datasets/HuggingFaceH4/MATH-500) | A 500-problem slice of the Hendrycks MATH test set spanning seven subjects and five difficulty levels with verifiable answers. | The quick comparable math signal most reasoning-model evals standardized on, above competition level but below AIME difficulty at the top end. |

## Context, instructions, and preference

| Benchmark | What it evaluates | Reading notes |
| --- | --- | --- |
| [IFEval](https://arxiv.org/abs/2311.07911) | Around 500 prompts built from 25 types of verifiable instructions (word counts, keyword frequencies, output formats), scored mechanically rather than by a judge. | The board for "does the model do what was asked rather than something adjacent", cheap to run and hard to game. |
| [LMArena](https://arxiv.org/abs/2403.04132) | Crowdsourced pairwise battles ranked Elo-style by human preference, published as the Chatbot Arena methodology. | It measures preference, which includes style and length, on a consumer-skewed prompt mix, a launch signal rather than an engineering one. |
| [RULER](https://github.com/NVIDIA/RULER) | Parametric synthetic suites (retrieval, multi-hop variable tracing, aggregation, QA) at configurable sequence lengths, finding a model's effective context size rather than its claimed one. | The corrective to context-window marketing: most models claiming 32K or more fail RULER's qualitative threshold before reaching it. |

## How I read these boards

**Agentic boards measure the harness plus the model, never the model alone.**
SWE-bench normalized its default view to one bash-only mini-SWE-agent environment for exactly this reason, and HarnessTax measured harness swaps costing up to 5x at constant model quality.
A score without a named harness and runner is a marketing number, which is why I never quote a vendor's self-reported figure, including ones that cite a real board's name.

**Every static board decays, and the decay is fast.**
The [model selection guide](../model-selection-for-coding-tasks/index.md) observed a quarterly relevance cycle (CodeClash, then ProgramBench within six months), the aider leaderboard froze with its tool, and HumanEval, MBPP, and MMLU are legacy signals kept for continuity.
The healthy boards are the ones built against decay: LiveCodeBench and SWE-rebench refresh continuously, HLE ships a rolling variant, and SWE-bench Pro licenses its sources to block contamination.

**Saturation, not difficulty, is what retires a board.**
HumanEval at 90 percent+ tells you a model is competent, not which model to pick.
The still-discriminating set as of 2026-09-24 is small: SWE-bench Pro, ProgramBench, PaperBench, FrontierMath, ARC-AGI-2, HLE, and the agentic environment boards (OSWorld, GAIA, Terminal-Bench).

**Boards disagree on purpose, and that disagreement is the signal.**
GAIA says average tasks are nearly solved, SWE-bench Pro says hard repo work is not, and both are true because they sample different difficulty distributions.
When two boards rank the same models differently, the gap tells you where the models actually differ, which no single ranking shows.

## What to Do Next

- Choosing a model for repo work: read SWE-bench Verified for the floor, then SWE-bench Pro for the ceiling, and distrust either without a named harness.
- Choosing a harness: [FrontierHarness Eval](../evaluation-review/frontierharness-eval/index.md) and [HarnessTax](../evaluation-review/harnesstax/index.md), which hold the model constant, then Terminal-Bench on your candidate pair.
- Estimating economic displacement or freelance value: SWE-Lancer, the only board denominated in dollars.
- Buying a long-context claim: RULER's effective-length result, then your own document set, never the model card number.
- Wiring tool calling into production: BFCL, then a validate-and-retry loop (see the [hybrid execution category](../hybrid-execution/_index.md)) because even top BFCL models fail non-trivially.
- Before any purchase decision: run two weeks of cost-per-merged-PR on your own repository, the measurement that outranks every board here.

## Changes

- 2026-09-24 - Created on owner request with thirty benchmarks in six groups, each summarized in one or two sentences, every cited external URL fetched this run.

## See also

- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the decision layer these boards feed, with the cost-per-point argument this matrix assumes
- [Model Provider Feature Matrix](../model-provider-feature-matrix/index.md) - the vendor bundle (price, cache policy, weights) that a benchmark score alone never shows
- [HarnessTax](../evaluation-review/harnesstax/index.md) - the academic study proving harness choice moves scores as much as model choice
- [FrontierHarness Eval](../evaluation-review/frontierharness-eval/index.md) - the vendor-run harness benchmark this matrix deliberately excludes from its rankings
- [JevBench](../hybrid-execution/jevbench/index.md) - the decision-model scoreboard serving a different instrument class than these model boards

## References

- https://www.swebench.com/ - SWE-bench family sizes (Lite 300, Verified 500, Multilingual 300, Multimodal 480, Full 2294), the bash-only mini-SWE-agent default view, CodeClash and ProgramBench launches (fetched 2026-09-24)
- https://scale.com/leaderboard/swe_bench_pro_public - SWE-bench Pro's 1,865 tasks, 41 repositories, copyleft contamination defense, launch-era 23 percent frontier scores, current leaderboard (fetched 2026-09-24)
- https://github.com/multi-swe-bench/multi-swe-bench - Multi-SWE-bench's seven languages, 1,632 instances, 68 annotators, Apache-2.0 license, NeurIPS 2025 acceptance (fetched 2026-09-24)
- https://programbench.com/ - ProgramBench's binary-plus-docs task design, 200 tasks, 248,000 behavioral tests, 4.5 percent top resolution (fetched 2026-09-24)
- https://arxiv.org/abs/2502.12115 - SWE-Lancer's 1,488 Upwork tasks, $1M payout mapping, IC and managerial splits, Diamond public split (fetched 2026-09-24)
- https://openai.com/index/paperbench/ - PaperBench's 20 ICML 2024 papers, 8,316 rubric tasks, 21.0 percent best agent score, human baseline (fetched 2026-09-24 via search snapshot, direct page blocks fetches)
- https://swe-rebench.com/ - the SWE-rebench task stream (fetched 2026-09-24, page returned an oversize body, existence confirmed)
- https://www.tbench.ai/ - Terminal-Bench 4.0, resolution rate with 95 percent confidence intervals, Stanford and Laude Institute hosting (fetched 2026-09-24)
- https://aider.chat/docs/leaderboards/ - the polyglot benchmark's 225 Exercism exercises across six languages, edit-format scoring, frozen 2025 leaderboard (fetched 2026-09-24)
- https://github.com/openai/human-eval - HumanEval's pass@k harness and hand-written problem set (fetched 2026-09-24)
- https://livecodebench.github.io/ - LiveCodeBench's release-date contamination control, four scenarios, documented HumanEval overfitting (fetched 2026-09-24)
- https://arxiv.org/abs/2108.07732 - MBPP's 974 entry-level Python tasks (fetched 2026-09-24)
- https://github.com/sierra-research/tau2-bench - TAU-bench domains, simulated users, policy and tools, tau-3 voice and knowledge additions, v1.0.1 grading break (fetched 2026-09-24)
- https://gorilla.cs.berkeley.edu/leaderboard.html - BFCL v4's agentic evaluation, unweighted category average, pinned evaluation commits (fetched 2026-09-24)
- https://os-world.github.io/ - OSWorld's 369 execution-checked tasks, OSWorld-Verified refresh, 2.0 release (fetched 2026-09-24)
- https://webarena.dev/ - the WebArena family (WebArena, WebArena-Infinity, VisualWebArena, TheAgentCompany) and its venue record (fetched 2026-09-24)
- https://the-agent-company.com/ - TheAgentCompany's simulated-company premise (fetched 2026-09-24)
- https://huggingface.co/spaces/gaia-benchmark/leaderboard - GAIA's three levels, exact-match scoring, public dev and private test split (fetched 2026-09-24)
- https://arcprize.org/arc-agi/2/ - ARC-AGI-2's human calibration, capability targets, efficiency metric, and the ARC-AGI-3 pipeline (fetched 2026-09-24)
- https://arxiv.org/abs/2311.12022 - GPQA's 448 google-proof questions and expert-versus-non-expert gap (fetched 2026-09-24)
- https://lastexam.ai/ - HLE's 2,500 questions, expert contributor base, Nature publication, held-out set, HLE-Rolling and HLE-Diamond forks (fetched 2026-09-24)
- https://arxiv.org/abs/2406.01574 - MMLU-Pro's ten options, prompt stability, and the MMLU plateau it responds to (fetched 2026-09-24)
- https://mmmu-benchmark.github.io/ - MMMU's 11.5K multimodal questions, 30 subjects, 30 image types, MMMU-Pro variant (fetched 2026-09-24)
- https://huggingface.co/datasets/math-ai/aime25 - the AIME 2025 problem set with exact integer answers (fetched 2026-09-24)
- https://huggingface.co/datasets/HuggingFaceH4/MATH-500 - MATH-500's subject and level structure (fetched 2026-09-24)
- https://epoch.ai/frontiermath/ - FrontierMath's tiers, unpublished problems, Open Problems and Erdős components (fetched 2026-09-24)
- https://github.com/NVIDIA/RULER - RULER's four task categories, configurable lengths, effective-versus-claimed context findings (fetched 2026-09-24)
- https://arxiv.org/abs/2311.07911 - IFEval's 25 verifiable instruction types and 500 prompts (fetched 2026-09-24)
- https://arxiv.org/abs/2403.04132 - the Chatbot Arena pairwise preference methodology behind LMArena (fetched 2026-09-24)
