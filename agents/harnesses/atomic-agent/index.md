---
title: Atomic Agent
created: 2026-10-10
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harnesses, local-first, llama-cpp, open-source]
readability: 3
audience_notes: >
  Engineers who want a coding-and-desktop agent that runs a small local model through long multi-step work on consumer hardware.
  Assumes you know what llama.cpp, quantization, and MCP are.
---

Atomic Agent is an MIT local-first agent (TUI, CLI, and a Tauri desktop shell) that runs open-weight models through its own TurboQuant llama.cpp fork and drives your browser, files, shell, git, and MCP tools with the control loop and all state on your machine.

**The bet is that small quantized models stay useful for long, tool-heavy work if the harness does the engineering: grammar-constrained (GBNF) tool calls, a byte-stable prompt prefix for KV-cache reuse, a bounded context tail, and externalized state, so a 9B model clears half of GAIA Level 1 through the loop rather than the model.**

## What it is

A developer-preview Node.js/TypeScript agent installed by curl script with self-update and a documented uninstall flow, released under MIT (v0.6.7 on 2026-10-07, plus a first desktop-v0.0.1 Tauri build the same day).
One inference produces a JSON array of tool calls (grammar-constrained on a local llama-server), independent reads run in parallel, risky actions ask first, and long jobs continue past 25-step checkpoints to a 1,000-step or 2-hour ceiling.
The maker maintains a TurboQuant llama.cpp fork (claimed up to roughly 6.4x KV-cache compression and 30-50% throughput gains from speculative decoding) and a managed mode that downloads and runs the backend for you.
Surfaces go beyond the terminal: an HTTP API whose `/v1/chat/completions` maps one request to one full macro-turn, a Tauri sidecar for embedding, Telegram and Discord bots with approval buttons, and Fusion mode where one model plans and a pool of throwaway workers executes via `fusion.delegate` (workers cannot delegate, reach you, schedule tasks, or write memory).
It imports skills, memory, sessions, and (opt-in) keys from Claude Code, Codex, Pi, Oh My Pi, Hermes, and OpenClaw.

## Status

Active and quick-growing: 3,328 stars and 273 forks as of 2026-10-15, created 2026-04-21, pushed 2026-10-24 (GitHub API, as of 2026-10-24), with a release train that has accelerated from weekly to near-daily (v0.6.8 on October 13, v0.6.9 on October 15 with desktop-v0.0.3, which merged the two surfaces onto one setup: the desktop app now shares the terminal agent's `~/.atomic-agent` folder for chats, memory, skills, keys, and settings, both can run at once without killing each other's local model, scheduled tasks fire once whichever app started first, and `atomic-agent import atomic-desktop` migrates old desktop data, and v0.6.10 on October 21 with desktop-v0.0.4, which added a Studio of image and video pages to the desktop app plus an `image.generate` tool that draws through OpenRouter and saves into the working folder) and a developer-preview warning that APIs and behavior are still moving.
The headline benchmark is self-run: on the public GAIA validation Level 1 split (53 tasks), Atomic Agent scored 69.8% (37/53) against Hermes at 58.5%, both driving the same local `qwen-3.6-35b-a3b` on one M4 Max with the same step budget, with per-task matrices, NDJSON traces, and logs published on the release tag; a model-scaling table shows 52.8% at 9B and 45.3% at 12B on the same split.
No independent reproduction exists, and a Hacker News search finds no thread about the project as of 2026-10-10, so the adoption evidence is the star curve and the published artifacts, not independent technical discussion.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AtomicBot-ai/atomic-agent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AtomicBot-ai/atomic-agent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AtomicBot-ai/atomic-agent&type=date&legend=top-left" />
</picture>

## Strengths

- The most complete local-model engineering in this section: grammar-constrained tool calls, cache-friendly prompt stability, and a compression step are aimed squarely at the failure modes of small models on long tasks.
- Fusion is a pragmatic subagent story: a planner delegates wide reads and drafts to disposable workers and merges the results, with the orchestrator barred from mutating tools.
- The vendor-run benchmark publishes its artifacts (matrices, traces, logs on the release tag) and holds the model and hardware constant against a named rival, which is better evidence practice than most self-reports.
- Full desktop tool surface with approval gating on every dangerous action, plus verify checks that never report an unchecked file as passing.

## Cautions

- Developer preview: the README says APIs, commands, config, and behavior are still moving, so any integration should pin a release.
- The benchmark is vendor-run on one model, one machine, and one 53-task split, and the loser (Hermes) is also the comparison the vendor chose; treat 69.8% as a reproducible claim, not an independent one.
- The ecosystem around the agent is broad consumer surface (Atomic Mail, Atomic Chat, Atomic Wallet, Sigma Browser, Atomic VPN on the vendor site), which is an odd neighborhood for a dev tool and worth factoring into trust.
- Category adjacency: Telegram and Discord channels plus ClawHub skill installs overlap the assistant-runtimes family, so teams should decide whether they want a harness that answers your phone.

## Pricing

Free, MIT, with no paid tier recorded as of 2026-10-10: local models cost nothing, and cloud models bill your own provider keys, including Claude Code and OpenAI Codex subscriptions driven through their signed-in CLIs.

## Compared to

- [Ante](../ante/index.md): the other embedded-llama.cpp bet, roughly 15MB with the engine inside the binary; choose Ante for footprint, Atomic Agent for the fuller tool surface and Fusion.
- [Hermes](../../assistant-runtimes/hermes/index.md): the rival it benchmarks against, a much larger assistant runtime with a learning loop; choose Hermes for channels and self-improvement, Atomic Agent for a local coding-and-desktop agent under your keys.
- [Nanocoder](../nanocoder/index.md): the community-built local-first harness; Nanocoder has the wider documented local-engine list, Atomic Agent ships the deeper local-inference engineering.

## Bottom line

**Recommended for running actual work on small local models, where the harness-side engineering (GBNF calls, cache-stable prompts, externalized memory) is the difference between a demo and a workday.**
Not for anyone needing a stable API contract today (developer preview), and not for teams who want independently reproduced benchmark numbers before adopting.

## Changes

- 2026-10-10 - Created from the harnesses resolution pass (two of three category workers placed it here); the assistant-runtimes adjacency (chat channels, ClawHub skills) is recorded in the cautions.
- 2026-10-13 - Corrected the star-history chart markup: the light source and fallback image dropped the dark-theme parameter to match the canonical chart block.
- 2026-10-17 - Recorded the v0.6.9 release (published October 15) with the desktop-v0.0.3 build: one `~/.atomic-agent` setup shared between the terminal and desktop surfaces, concurrent running with shared local models, deduplicated scheduled tasks, and an `atomic-agent import atomic-desktop` migration path.
- 2026-10-24 - Recorded the v0.6.10 release (published October 21) with the desktop-v0.0.4 build: a Studio group of image and video pages in the desktop app and an `image.generate` tool drawing through OpenRouter with up to four pictures per call.

## See also

- [Ante](../ante/index.md) - the minimal embedded-llama.cpp contrast
- [Hermes](../../assistant-runtimes/hermes/index.md) - the benchmarked rival across the category line
- [Nanocoder](../nanocoder/index.md) - the other community local-first harness
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the category comparison this note joins
- [FrontierHarness Eval](../../evaluation-review/frontierharness-eval/index.md) - the independent harness benchmark to read before believing any vendor self-report

## References

- https://github.com/AtomicBot-ai/atomic-agent - repository: README, architecture, tool surface, license
- https://api.github.com/repos/AtomicBot-ai/atomic-agent - stars, forks, issues, creation and push dates as of 2026-10-12
- https://api.github.com/repos/AtomicBot-ai/atomic-agent/releases - v0.6.10 and desktop-v0.0.4 published 2026-10-21; v0.6.9 and desktop-v0.0.3 published 2026-10-15
- https://atomicagent.io - product site: installer, benchmark banner, and the consumer-ecosystem surface
- https://raw.githubusercontent.com/AtomicBot-ai/atomic-agent/main/eval-agents/docs/GAIA-L1-EXPERIMENT.md - the benchmark write-up: environment, dataset, and artifact publication
- https://raw.githubusercontent.com/AtomicBot-ai/atomic-agent/main/README.md - the full README: loop design, TurboQuant claims, import matrix, privacy and egress
- https://hn.algolia.com/api/v1/search?query=atomic-agent&hitsPerPage=5 - the no-thread community-footprint check as of 2026-10-10
