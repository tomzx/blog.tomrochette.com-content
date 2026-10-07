---
title: MiMo Code
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, harnesses, coding-agents, open-source, xiaomi, long-horizon]
readability: 3
audience_notes: >
  Engineers evaluating a terminal coding agent that bets on long-horizon reliability and cheap access to a Chinese vendor's models.
  Assumes familiarity with AGENTS.md, MCP, BYOK, and what the OpenCode fork lineage means for a harness.
---

MiMo Code is Xiaomi's MIT-licensed terminal coding agent, an OpenCode fork that adds a persistent memory layer, checkpoint-based context rebuilds, and goal-verified autonomous loops, released in June 2026.

**MiMo Code's differentiator is not a better model but a runtime built to survive hundreds of steps, and the defensible case for it today is auditable source plus cheap Xiaomi tokens, not its self-reported benchmark gap.**

## What it is

The `mimo` CLI is installed by a curl script or the `@mimo-ai/cli` npm package, and the same engine ships as the core of Xiaomi's MiMo Desktop app.
It carries three primary agents (build, plan, and compose), an on-demand subagent system with parallel execution and lifecycle tracking, a tree-structured task store (`T1`, `T1.1`), MCP with local, remote, and OAuth servers, LSP integration, and a plugin and skills surface inherited from OpenCode.
**The parts Xiaomi actually added are the long-horizon machinery:** a checkpoint-writer subagent that writes structured state at roughly 20, 45, and 70 percent of the context budget, a four-layer memory (session checkpoint, project `MEMORY.md`, global memory, and a full SQLite history), a rebuild step that reassembles the window from those files in about 65K tokens, `/dream` and `/distill` memory-maintenance passes, an independent judge behind the `/goal` stop condition, and best-of-N Max Mode.
Provider access follows the OpenCode approach: any of 75+ providers through the AI SDK and Models.dev, local models through an OpenAI-compatible endpoint, or Xiaomi's own platform.

## Status

**Active and pre-1.0.**
The repository was created 2026-06-10 and lists about 13.6k stars and 1.4k forks under MIT as of 2026-10-04, with 1,369 commits and a push on 2026-10-03.

[![Star History Chart](https://api.star-history.com/chart?repos=XiaomiMiMo/MiMo-Code&type=date&legend=top-left)](https://www.star-history.com/?repos=XiaomiMiMo%2FMiMo-Code&type=date&legend=top-left)

The newest release by publication time is v0.1.14 (published 2026-09-23), published a day after v0.1.15 (2026-09-22), so five months after launch the project is still on a 0.1.x line.
The launch drew a 557-point Hacker News thread with 315 comments on 2026-06-11, and the tracker carries roughly 800 open issues plus 284 open pull requests, many auto-filed and low-signal.

## Strengths

- **The context design is the differentiated part:** moving state extraction out of the main loop into a separate writer subagent, and checkpointing well below the window limit rather than at the moment of overflow, is a deliberate answer to the lost-in-the-middle degradation that ordinary compaction ignores.
- The `/goal` verifier and Max Mode are two orthogonal uses of test-time compute, serial self-checking and parallel sampling, and they are conventional enough to compare against Claude Code's subagents and Arbor-style hypothesis trees.
- Deterministic workflows turn orchestration into bounded JavaScript rather than prompt, which removes the "the model skipped a step" failure class for large fan-out jobs.
- Provider-neutral, local-model capable, and self-hostable weights mean the model is a separate purchase from the agent, and the international API prices sit far below the frontier vendors.
- The MIT source is fully auditable, which matters for a tool that runs your shell.

## Cautions

- **The fork does the heavy lifting:** the LICENSE preserves `Copyright (c) 2025 opencode`, and open issues still flag leftover OpenCode names in `CONTRIBUTING.md` (#29) and in the published config docs (#1150), so evaluate Xiaomi's contribution as the memory and orchestration layer, not the polished TUI, plugin system, and provider abstraction.
- **The benchmark case is vendor-run.** Xiaomi reports 62 versus 57 on SWE-bench Pro and 73 versus 68 on Terminal Bench 2 against Claude Code with the model held constant, but MiMo Code appears on neither public leaderboard and nobody independent has reproduced the gap; Xiaomi's own write-up says the two agents perform about the same below 200 execution steps, which is exactly the case a one-shot benchmark does not measure.
- **The Token Plan's "4.1 billion" quota is in Credits, not tokens, and the cache-miss multiplier is 100x** (2 Credits cache hit, 100 cache miss, 200 output for the V2.5 line), an ambiguity one open issue calls a bait-and-switch after a 62.6M-token session consumed 903M of a 4.1B quota.
- Pre-1.0 churn: breaking changes between 0.1.x releases, a fast-moving config surface, and reports of single-request 429s rendering a Max plan unusable.
- Importing a Claude Code login or ChatGPT account into a third-party CLI can run against those providers' terms, and Xiaomi is a Chinese vendor whose hosted endpoints are regional (China, Singapore, Europe).
- MIT is paired with a separate `USE_RESTRICTIONS.md` that adds conditions (no military use, no unsupervised high-risk autonomous actions) beyond the license grant.

## Pricing

The agent is free and open source under MIT; you pay for tokens, either through Xiaomi or through your own provider.
Xiaomi's [Token Plan](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription) sells four individual monthly tiers, all covering the V2.6 and V2.5 model lines plus ASR and TTS: Lite $6 (4.1B Credits), Standard $16 (11B), Pro $50 (38B), and Max $100 (82B), with annual billing about 12 percent cheaper, a one-time 12 percent first-purchase discount, and an off-peak 0.8x consumption rate between 16:00 and 24:00 UTC; the V2.5 models in the lineup (mimo-v2.5-pro and mimo-v2.5) retire on October 21, 2026, leaving the V2.6 line, per the same page as of 2026-10-04.
Pay-as-you-go international prices per million tokens are $0.435 in (cache miss) and $0.87 out for `mimo-v2.6-pro`, and $0.14 and $0.28 for `mimo-v2.6-flash`, with cache hits at a few thousandths of a dollar.
Any OpenAI-compatible provider, including a local model, can be configured instead, so the Token Plan is optional.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Token Plan Lite | Baseline: introduced at $6/month (¥39), 4.1B Credits | https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription |
| 2026-09-27 | Token Plan Standard | Baseline: introduced at $16/month (¥99), 11B Credits | https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription |
| 2026-09-27 | Token Plan Pro | Baseline: introduced at $50/month (¥329), 38B Credits | https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription |
| 2026-09-27 | Token Plan Max | Baseline: introduced at $100/month (¥659), 82B Credits | https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription |
| 2026-09-27 | Pay-as-you-go (international) | Baseline: mimo-v2.6-pro $0.435/$0.87 per M in/out, mimo-v2.6-flash $0.14/$0.28 | https://mimo.mi.com/docs/en-US/price/pay-as-you-go |

## Compared to

- [OpenCode](../opencode/index.md): the upstream project; choose OpenCode for the longer track record, the larger community, and the leanest measured token baseline, and MiMo Code only if the memory and long-horizon additions justify a fork you now depend on.
- [Kimi Code](../kimi-code/index.md): the closest peer, another terminal harness tuned by a challenger lab for its own cheap models; pick on which vendor's models and quota structure you prefer, not on benchmark claims.
- [Claude Code](../claude-code/index.md): the platform benchmark MiMo Code positions against; Claude Code buys polish and subscription simplicity, MiMo Code buys open source and low per-token cost.

## Bottom line

**Recommended for engineers who want an auditable terminal agent with explicit long-horizon state management and some of the cheapest credible token prices, and who are willing to run a 0.1.x tool.**
Not for teams that need release stability, and not because a vendor benchmark says it beats Claude Code past 200 steps.
My disagreeable claim: the co-evolution story is mostly packaging, since the mature harness arrived with the OpenCode fork and the observable Xiaomi contribution is a checkpoint-and-memory layer plus a model bundle, which is genuinely useful but narrower than the tagline suggests.

## Changes

- 2026-09-27 - Created.
- 2026-09-27 - Corrected the latest-release fact: the newest release by publication time is v0.1.14 (published 2026-09-23), a day after v0.1.15 (2026-09-22); the 0.1.x status is unchanged.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-04 - Recorded the subscription page's retirement date for the V2.5 models (October 21, 2026), refreshed repository activity, and re-verified the tier prices unchanged.
- 2026-10-07 - Added the XiaomiMiMo/MiMo-Code star history chart to the Status section.

## See also

- [OpenCode](../opencode/index.md) - the upstream fork this is built on, and the token-efficiency baseline it inherits
- [Kimi Code](../kimi-code/index.md) - the other challenger-vendor terminal harness tuned for its maker's own cheap models
- [Claude Code](../claude-code/index.md) - the harness the vendor benchmarks compare against, and the endurance-gap framing
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - where MiMo's price and long-horizon claims fit the model side of the decision
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this note's category belongs to

## References

- https://mimo.xiaomi.com/mimocode/start - official docs: surfaces, agents, skills, MCP, and the memory layer
- https://github.com/XiaomiMiMo/MiMo-Code - repository, MIT license, OpenCode fork relationship, and feature README
- https://api.github.com/repos/XiaomiMiMo/MiMo-Code - 13,595 stars, 1,418 forks, MIT, created 2026-06-10, pushed 2026-10-03, as of 2026-10-04
- https://api.github.com/repos/XiaomiMiMo/MiMo-Code/releases/latest - returns v0.1.14 (published 2026-09-23), published a day after v0.1.15 (2026-09-22), as of 2026-10-04
- https://mimo.xiaomi.com/blog/mimo-code-long-horizon - the design write-up: checkpoints, four-layer memory, `/goal`, Max Mode, and the vendor benchmarks
- https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription - individual Token Plan tiers, Credits, discounts, and the V2.5 retirement date, re-verified 2026-10-04
- https://mimo.mi.com/docs/en-US/price/pay-as-you-go - international and domestic per-token prices
- https://mimo.mi.com/docs/en-US/tokenplan/integration/mimo-code - MiMo Code configuration and Token Plan support
- https://mimo.xiaomi.com/mimocode/skills - skill discovery, including the `.claude`, `.agents`, `.codex`, and `.opencode` compatibility roots
- https://www.ssdnodes.com/learn/mimo-code-ai-coding-agent - independent coverage: the fork-credit issue, the vendor-benchmark caveat, and the pre-1.0 caution
- https://thenewstack.io/coding-agent-endurance-gap/ - the endurance-gap framing and the self-reported-benchmark caveat
- https://hn.algolia.com/api/v1/items/48490826 - the 2026-06-11 launch thread, 557 points and 315 comments
- https://github.com/XiaomiMiMo/MiMo-Code/issues/2142 - the open Token Plan credit-multiplier complaint behind the pricing caution
- https://github.com/XiaomiMiMo/MiMo-Code/issues/1150 - open issue on config docs still documenting OpenCode names
- https://raw.githubusercontent.com/XiaomiMiMo/MiMo-Code/main/USE_RESTRICTIONS.md - the use-restrictions addendum paired with the MIT license
- https://raw.githubusercontent.com/XiaomiMiMo/MiMo-Code/main/LICENSE - MIT with the preserved opencode copyright line
