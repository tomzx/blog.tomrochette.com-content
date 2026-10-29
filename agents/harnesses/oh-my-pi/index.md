---
title: Oh My Pi
created: 2026-10-10
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, cli, coding-agent, lsp, fork]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent who want IDE-grade grounding, and readers of the Pi note deciding between the frozen core and its batteries-included fork.
  Assumes you know what MCP, AGENTS.md, and BYOK mean.
---

Oh My Pi (omp) is a batteries-included fork of the Pi harness, built by Stencil Labs, whose bet is that the IDE should be wired into the agent loop instead of the core staying frozen.

## What it is

A TypeScript CLI on Bun with a native Rust core of roughly 80,000 lines, MIT-licensed, distributed through an install script at omp.sh, Homebrew, bun/npm (`@oh-my-pi/pi-coding-agent`), Nix, and a Windows PowerShell script.
It is a fork of Mario Zechner's Pi (the `badlogic/pi-mono` line), and it keeps Pi's extensibility while adding what Pi refuses to ship: 60-plus providers, 31 built-in tools, LSP operations wired into every write, DAP debugger control (lldb, dlv, debugpy), first-class subagents that fan out into worktrees and return typed results, an advisor model that watches every turn, live session sharing over `/collab`, and native Windows without WSL.
The hook is the name of the design: everything your IDE knows, the agent knows.

## Status

Very active and past its parent in stars: 35,472 stars and 3,876 forks as of 2026-10-15 (GitHub API), on a repository created 2025-12-31 and pushed 2026-10-27 (GitHub API, as of 2026-10-27).
The npm latest is 18.13.2 (published 2026-10-27), and the changelog logs a near-daily train with pull requests numbered past 16,000: 18.9.0 through 18.9.2 landed October 11 (fixes across apply_patch, local-model discovery, and fork spending inheritance), 18.10.0 landed October 12 (a `/fork` that opens a new Tern pane while a turn streams, `omp session pack`, `unpack`, and `moved` for carrying a session with its artifacts to another machine, `omp auth export` and `import` for model sign-ins, and a native owner-only transport for every local IPC endpoint including Windows named pipes), 18.10.1 followed the same day (a per-answer copy button in Tern), 18.10.2 and 18.10.3 landed that evening (late tool-update frames from background jobs now reach `onDetachedToolUpdate` subscribers instead of being dropped, and a breaking cleanup removing `estimateImageContentTokens()` in favor of `Tokenizer.imageTokens(size, detail)`), the 18.11.x train ran October 14 through 16 (18.11.0 added `AgentTool.delegationGuidance` for same-name extension replacements and dropped `ApprovalDetailsOptions` in a breaking cleanup, 18.11.3 tagged queued-message batches with their queue so `prepareQueuedMessages` can tell steering from follow-ups, and the pi-ai JSON Schema dereferencer stopped rewriting literal values in `const`, `enum`, and `default` positions), the 18.12 train ran October 17 through 21 (18.12.0 added `ThinkingContent.narration` for Anthropic and Bedrock thinking blocks marked as between-tool narration with `presentNarrationAsAnswer` to surface them as reply text, and replaced `PI_CODEX_ZSTD` with `PI_REQUEST_COMPRESSION` in a breaking cleanup, 18.12.1 fixed every request failing behind a TLS-inspecting proxy that refuses compressed uploads and removed `display()` from eval in both Python and JavaScript, 18.12.2 corrected the failed-tool-call feedback sent to DeepSeek models to also cover chat-template tool-call tokens and fixed Ollama chat-history estimates that skewed compaction after model switches, 18.12.3 added the `approvalCacheTargets` hook the `always-ask-cached` approval mode uses to check and record per-file grants and passed unknown root arguments to tools with `lenientArgValidation`, 18.12.4 enabled native compaction for supported Bedrock Claude models and added an opt-in `reclaimAbovePct` account policy for automatic session reclaim, 18.12.5 requested OpenAI's 12-hour prompt-cache retention for GPT-5.6+ on the Responses API and fixed every OpenAI Codex request failing against the long-cache setting, and 18.12.6 added a `prompt-cache-persistent` catalog axis for providers whose endpoint caches never expire and refreshed the bundled Yolo-Auto catalog), and the 18.13 pair landed October 26 through 27 (18.13.0 rebuilt remote compaction to send cache and session headers for the endpoint it actually targets, added `PI_ANTHROPIC_API_VERSION=2026-10-21` for the official Anthropic API, gave OpenCode Go shared-lane requests an explicit prompt-cache key so forks, Task siblings, and parents reuse one gateway cache, fixed repeated compaction on small or provider-capped windows, and broke `OpenAIRequestSetupModel` by requiring catalog-policy fields, and 18.13.1 added `Agent.isPaused` so hosts can tell paused agents from draining turns, stopped exhausted Codex spend-cap accounts being picked through credit overage, fixed Codex capacity 429s waiting hours instead of the server's Retry-After, and added GPT-6.1 Terra and Kimi K3.1 Pro with Highspeed to the catalog, and 18.13.2 the same day let TUI extensions switch plan, vibe, goal, and loop modes directly through `ctx.sessionModes` with a `mode_changed` event instead of submitted slash commands, added draft-only speech-to-text capture with live previews for RPC hosts, let custom providers opt out of the reasoning ladder their `/v1/models` rows advertise through `discovery.advertisedReasoning`, scoped WATCHDOG advisor entries to main or subagent sessions, added `session.worktreeScope` to keep the resume picker scoped to one directory, and gave LM Studio decision models a `judge` role served over their `/v1/decisions` endpoint).
Contribution policy loosened from a vouch requirement to temporarily-open PRs while the maintainers evaluate how open contributions go.
The Hacker News footprint is modest for the star count: a 42-point launch thread on July 21, 2026, and a 35-point "Harness Playbook" thread in September, which reads as adoption spreading through practitioners rather than through tech-media coverage.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=can1357/oh-my-pi&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=can1357/oh-my-pi&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=can1357/oh-my-pi&type=date&legend=top-left" />
</picture>

## Strengths

- **The strongest editor grounding in the terminal-harness field: renames go through LSP, and debugging happens through a DAP adapter (lldb, dlv, debugpy) instead of print statements.**
- It inherits what your other tools already wrote, reading Cursor MDC, Cline `.clinerules`, Codex AGENTS.md, Copilot `applyTo`, and more in their native shapes, plus MCP servers from `.claude`, `.cursor`, and friends on first run.
- Coding-plan and OAuth routes cover the subscription you may already pay (Anthropic, OpenAI Codex, GitHub Copilot, Kimi Code, GLM Coding Plan), alongside 60-plus raw providers and local Ollama, LM Studio, llama.cpp, and vLLM endpoints.

## Cautions

- Fork lineage is the structural risk: at 18.x against its parent's 1.1.x, omp is a permanently diverging codebase, and a re-merge is not a realistic plan.
- Subscription reuse carries terms-of-service risk: the launch thread's sharpest comment reports provider OAuth flows warning that only official tools may log in, so routing a paid plan through omp could violate the provider's terms.
- The benchmark table in the README is self-run, and launch-thread commenters questioned the evaluation rigor (one called the CI "benchmaxxing" incomplete); the surface is also large enough that reviewing what omp does is a project of its own.

## Pricing

Free and MIT-licensed.
There is no paid tier; usage flows through your own providers, subscriptions, or local servers, on their prices.

## Compared to

- [Pi](../pi/index.md): its parent, which keeps the core frozen and pushes features into extensions you can read in an afternoon; choose Pi for auditability, omp for the batteries.
- [Claude Code](../claude-code/index.md): the closed incumbent omp out-features on paper, with none of Anthropic's first-party model economics.
- [OpenCode](../opencode/index.md): the other big open terminal harness, provider-neutral like omp but without the LSP-first grounding.

## Bottom line

Recommended for power users who want IDE-grade diagnostics, debugger control, and heavy subagent fan-out in one terminal agent.
Not for anyone who needs a small core they can fully audit, and not for ToS-cautious subscription reuse until the provider OAuth question is settled.

## Changes

- 2026-10-10 - Created from the awesome-claude-code and GitHub topic scan, admitted as the batteries-included fork counterargument to the Pi column.
- 2026-10-12 - Recorded the npm train reaching 18.10.1 (October 12) after 18.9.x on October 11, with 18.10.0 adding session pack and unpack across machines, auth export and import, streaming-turn /fork panes, and a native owner-only local IPC transport, and refreshed repository counters.
- 2026-10-13 - Recorded the npm train reaching 18.10.3 (October 12 evening): 18.10.2 added `onDetachedToolUpdate` so late background tool-update frames reach subscribers, and 18.10.3 removed `estimateImageContentTokens()` in a breaking cleanup in favor of `Tokenizer.imageTokens(size, detail)`, and refreshed repository counters.
- 2026-10-17 - Recorded the npm train reaching 18.11.3 (October 16): the 18.11.x releases added `AgentTool.delegationGuidance`, broke out `ApprovalDetailsOptions`, tagged queued-message batches by queue in `prepareQueuedMessages`, and fixed the JSON Schema dereferencer rewriting literals in `const` and `enum` positions.
- 2026-10-18 - Recorded the npm train reaching 18.12.1 (October 17): 18.12.0 added between-tool thinking narration for Anthropic and Bedrock with `presentNarrationAsAnswer` and replaced `PI_CODEX_ZSTD` with `PI_REQUEST_COMPRESSION` in a breaking cleanup, and 18.12.1 fixed requests behind TLS-inspecting proxies that refuse compressed uploads and removed `display()` from eval.
- 2026-10-20 - Extended the release train through 18.12.3 (October 19): DeepSeek chat-template token corrections, Ollama compaction-estimate fixes, the approvalCacheTargets hook, and lenient argument validation.
- 2026-10-24 - Extended the release train through 18.12.6 (October 21): Bedrock Claude native compaction with an opt-in reclaimAbovePct account policy, OpenAI 12-hour prompt-cache retention for GPT-5.6+ on the Responses API with its Codex failure fix, and the prompt-cache-persistent catalog axis, and refreshed the push date.
- 2026-10-27 - Extended the release train through 18.13.1 (October 26-27): remote compaction pinned to the endpoint it actually targets, the Anthropic 2026-10-21 API version opt-in, OpenCode Go shared prompt-cache keys, repeated-compaction and Codex spend-cap/429 fixes, `Agent.isPaused`, and GPT-6.1 Terra plus Kimi K3.1 Pro catalog additions, with the breaking `OpenAIRequestSetupModel` catalog-policy requirement in 18.13.0.
- 2026-10-28 - Recorded the npm train reaching 18.13.2 (October 27): extension-driven session-mode switching through `ctx.sessionModes` with a `mode_changed` event, draft-only speech-to-text capture for RPC hosts, the `discovery.advertisedReasoning` opt-out for custom providers, WATCHDOG advisor scopes, `session.worktreeScope`, and an LM Studio judge role over `/v1/decisions`.

## See also

- [Pi](../pi/index.md) - the frozen-core parent whose minimalism omp exists to argue with
- [Claude Code](../claude-code/index.md) - the closed platform benchmark omp's feature table is measured against
- [OpenCode](../opencode/index.md) - the other large open harness in the same buyer's shortlist
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability comparison this column joins

## References

- https://omp.sh - the product site, install script, and the "IDE wired in" positioning
- https://api.github.com/repos/can1357/oh-my-pi - 35,122 stars, 3,822 forks, MIT, created 2025-12-31, pushed 2026-10-12, as of 2026-10-12
- https://api.github.com/repos/can1357/oh-my-pi/readme - the feature surface: 60-plus providers, LSP and DAP wiring, subagents, advisor, rules-format inheritance, local engines, and the provider list
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/packages/coding-agent/CHANGELOG.md - the 18.12 train of October 17 through 19, the 18.11.x train of October 14 through 16, the 18.10.x train of October 12, and the near-daily train behind the Status section
- https://registry.npmjs.org/@oh-my-pi/pi-coding-agent - npm distribution and the 18.13.1 latest tag (re-verified via the registry API, 2026-10-27)
- https://hn.algolia.com/api/v1/items/48994611 - the 42-point launch thread, cited for the OAuth terms-of-service caution and the benchmark-rigor skepticism
