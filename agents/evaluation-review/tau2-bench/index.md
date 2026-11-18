---
title: "τ²-bench"
created: 2026-11-18
updated: 2026-11-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, benchmark, evaluation, tool-agents, voice]
readability: 3
audience_notes: >
  Engineers building customer-facing tool-using agents who want a comparable benchmark for the whole conversation loop, including the voice case.
  Assumes you know what a tool call and a pass/fail reward are.
---

τ²-bench is Sierra's benchmark that scores a tool-using customer-service agent by having it serve an LLM-simulated user who can also act, then checking whether the simulated business database ends in the required state and whether the required information was communicated.

**τ²-bench judges the conversation loop rather than a single output: the agent must both drive its tools to change a database and elicit the right details from a user who has tools of their own, the dual-control gap that single-shot benchmarks skip.**

## What it is

A MIT benchmark and Python CLI (`tau2 run`) from Sierra, the customer-service AI company, with tasks across airline, retail, and telecom domains plus a banking_knowledge retrieval domain and a new intake (τ-Entity) domain of over 200 tasks that scores exact entity capture on outbound calls.
The reward is deterministic: pass or fail by the database's end state against the gold state, plus checks that required information was communicated; in some domains (telecom) the simulated user holds tools of their own, so the agent must guide them through actions instead of doing everything itself.
Version 2.0.0 (2026-10-20) added τ-i18n: the same tasks in six languages (English, Spanish, Portuguese, Hindi, Chinese, Korean) with localized tasks, databases, and caller personas, full-duplex voice runs against realtime models, post-hoc judges that score naturalness and speech fidelity without changing the task reward, and frozen published benchmarks (text-v1 and voice-v2 at 900 calls each, voice-v1 English-only at 278) so runs stay comparable.
A live leaderboard sits at taubench.com, and the design is the paper's (arXiv 2506.07982), extending the original 2024 τ-bench with the user-side tools.

## Status

Active and adopted: 2,473 stars, MIT, created 2025-06-09, pushed 2026-11-10, as of 2026-11-18, on a release train that ran v0.2.0 (2025-10-06, the web leaderboard), v1.0.0 (2026-03-18, voice, banking_knowledge, self-named τ³), and v2.0.0 (2026-10-20, multilingual and voice).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=sierra-research/tau2-bench&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=sierra-research/tau2-bench&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=sierra-research/tau2-bench&type=date&theme=dark&legend=top-left" />
</picture>

**The footprint is practitioner-grade: a 197-point Hacker News thread measured a prompt rewrite moving GPT-5-mini by 22 percent on the benchmark, and vendor score reports cite its voice leaderboards, so its numbers are quoted and argued with rather than ignored.**

## Strengths

- Dual control measures what single-turn tool-call benchmarks cannot: information elicitation and user-side action under simulation.
- The reward is deterministic (database end-state plus communication checks), so scores do not inherit judge-model variance.
- Frozen published benchmark configs (text-v1, voice-v2, voice-v1) pin the scored bytes, in the same spirit as Harbor's content-addressed datasets.
- Voice and six-language coverage is unique in this category, and the post-hoc judges keep speech quality separate from reward.

## Cautions

- The user is a simulated LLM: its behavior bounds and biases the measured loop, so results describe agent-plus-simulator, not agent-plus-human.
- Prompt sensitivity is demonstrated on its own board: the 197-point thread's 22 percent swing from a prompt rewrite means leaderboard gaps need a prompt-variance caveat.
- Domain coverage is narrow (airline, retail, telecom, banking knowledge, intake), so it says little about coding or research agents.
- The voice judges are post-hoc and advisory: naturalness scores never change the reward, so a smooth-sounding failing run still fails.

## Pricing

Free, MIT; a run bills your agent's model tokens plus the simulated user's, and voice runs bill the realtime model.

## Compared to

- [SWE-bench](../swe-bench/index.md): deterministic judging on both sides, but SWE-bench scores a patch against a repository's tests while τ²-bench scores a service conversation against a database end-state.
- [FrontierHarness Eval](../frontierharness-eval/index.md): the harness-comparison study; τ²-bench is a fixed benchmark you run agents on, not a comparison of the harnesses themselves.
- [agent-qa](../agent-qa/index.md): also judges interactive agent behavior, but against the actual app UI with a per-step verifier, where τ²-bench checks the simulated business's end state.

## Bottom line

**Recommended for teams building customer-facing tool agents who want a comparable, deterministic-reward loop benchmark, in text or voice.**
Not for coding-agent evaluation, and never without the simulator and prompt-variance caveats attached to its leaderboard numbers.

## Changes

- 2026-11-18 - Created from the awesome-agent-observability 2026-11-15 evals-expansion scan, admitted as the category's dual-control service-agent benchmark.

## See also

- [SWE-bench](../swe-bench/index.md) - the deterministic ground benchmark on the coding side of the same judging idea
- [agent-qa](../agent-qa/index.md) - the acceptance-test harness judging interactive agent behavior against the real app
- [FrontierHarness Eval](../frontierharness-eval/index.md) - the harness-comparison study for when the question is which harness, not how good the agent
- [MLR-Bench](../mlr-bench/index.md) - the research-agent benchmark whose judge panel is validated against expert humans, the calibration τ²-bench's deterministic reward sidesteps

## References

- https://github.com/sierra-research/tau2-bench - repository: README (the τ-bench 2.0 features, the benchmarks table, domain list), license
- https://arxiv.org/abs/2506.07982 - the paper defining the dual-control evaluation
- https://taubench.com - the live leaderboard
- https://sierra.ai/blog/benchmarking-agents-in-collaborative-real-world-scenarios - the maker's announcement of the benchmark
- https://api.github.com/repos/sierra-research/tau2-bench/releases - the release train from v0.2.0 (2025-10-06) to v2.0.0 (2026-10-20)
- https://hn.algolia.com/api/v1/search?query=tau2-bench&hitsPerPage=6 - the footprint: the 197-point prompt-sensitivity thread and the vendor voice-leaderboard reports
