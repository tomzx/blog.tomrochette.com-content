---
title: Unreal Agent
created: 2026-09-25
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harness, coding-agent, go, async]
readability: 3
audience_notes: >
  Engineers choosing a coding-agent harness who care about token cost and steering latency.
  Assumes you know what KV cache, Terminal-Bench, and a tool-call loop are.
---

Unreal Agent is an async-first coding-agent harness whose tool calls run in the background, so the model never spends tokens managing waits, polls, or heartbeats.
Facts below verified as of 2026-09-25.

## What it is

A Go harness from Unreal Labs, shipped as three surfaces: a Go library you embed in your own service, a runner executable comparable to `claude -p` or `codex exec`, and a benchmark runner compatible with Harbor.
The architecture is a coordinator around an append-only, forkable session store, tool translators that validate calls into serializable operations, and an actor-style operations manager that executes those operations in the background.
The context builder returns the assembled model input together with a record of everything it omitted, truncated, or compacted.
Unreal Labs says it was founded by engineers from CERN, Meta, Snap, Bloomberg, and DeepMind, and is backed by Sequoia and First Round.

## Status

Active and three days old at verification.
The repo was created 2026-09-21, the launch thread landed 2026-09-22 at 242 points with 122 comments, and the repo stood at 1,879 stars and 97 forks with the default branch pushed 2026-09-23 (GitHub, as of 2026-09-25).
Three tagged releases exist, v0.1.0 and v0.1.1 on launch day and v0.2.0 on 2026-09-23.
That traction at day three is exo-class: exo entered this index at 1,919 stars on a 169-point thread.

## Strengths

- **The async tool-call model is the whole product, and it is coherent.** Every issued tool call immediately appends an in-progress event and keeps executing while the conversation continues, which is what lets a user steer mid-setup and lets the agent pack more tool work between model turns.
- **The vendor's cost claim is unusually specific.** Its Harbor-linked runs report Terminal-Bench 4.0 at 57.9 percent with 1.73M input tokens per trial against Pi's 55.0 percent at 2.83M, with similar spreads on SWE-Atlas and DeepSWE 1.1, all on GPT-6 Astra xhigh.
- **Durability is designed in, not bolted on.** Versioned serializable session records, forkable sessions, crash-recovery inboxes, and atomic tool-call status recording are stated invariants in the README.
- **It cites its own critics' frame.** The announcement opens by citing the HarnessTax study, which is the same harness-swap evidence this section uses to argue harness design matters.

## Cautions

- **The benchmarks are vendor-run.** The launch thread's sharpest comment notes the headline chart compares Unreal Agent on Astra xhigh against Codex leaderboard runs on Astra max, so the 40-percent-savings headline is not like-for-like.
- **Three days of history.** No community footprint beyond the launch thread, a single org's commits, and a benchmark suite the vendor selected.
- **The extension story is deliberately absent.** The tool registry owns a fixed set of Bash, ViewImage, and skill-use definitions, with no subagents, no workflows, and no MCP mentioned anywhere in the README.
- **Security is explicitly pushed outside the harness.** The blog argues sandbox and environment constraints beat hooks and approval gates, which moves isolation work onto your infrastructure.
- **The name collides with Epic's Unreal Engine**, a trademark point raised on the launch thread and unanswered so far.

## Pricing

Does not apply: the harness is MIT-licensed and there is no hosted tier or paid plan.
Unreal Labs invites engineering contact by email rather than selling the harness, so there is no price history table.

## Compared to

[Pi](../pi/index.md) is the comparator in Unreal Agent's own benchmarks and the opposite bet: a minimal, extensible single-binary harness where Unreal Agent is a library with a fixed internal architecture.
[Codex](../codex/index.md) is the incumbent baseline the savings claims are measured against, and OpenAI's own harness is separately ramping native async tool calling.
[Fx](../fx/index.md) shares the embed-first thesis (a dependency, not an environment) but couples it to a sponsor gateway, while Unreal Agent's adapter is provider-agnostic and nothing about its thesis requires a specific vendor.

## Bottom line

I would pilot Unreal Agent where token cost and steering latency dominate and the workload looks like its Harbor runs, and I would not adopt it yet anywhere that needs an extension ecosystem, IDE integration, scheduled cloud runs, or a release-tagged dependency with community proof.
The plain summary is that its one claim, async tool calls cut harness token overhead, is exactly the kind of claim HarnessTax says is worth testing, and its own linked runs are the test, run by the vendor.

## Changes

- 2026-09-25 - Created.

## See also

- [Pi](../pi/index.md) - the comparator harness in the vendor's benchmarks and the opposite minimalism bet
- [HarnessTax](../../evaluation-review/harnesstax/index.md) - the harness-swap study the announcement cites for its framing
- [Fx](../fx/index.md) - the other embed-first harness in the category
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - where this note's capability cells live
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the tracker this note joins

## References

- https://github.com/unreallabsai/unreal-agent - the repo, MIT license, releases, and star and fork counts as of 2026-09-25
- https://unreallabs.ai/blog/unreal-agent/ - the architecture, async tool-call model, Harbor-linked benchmark tables, and company backing
- https://news.ycombinator.com/item?id=49805748 - the launch thread (242 points, 122 comments as of 2026-09-25) and the baseline-mismatch critique
- https://unreallabs.ai/ - the company positioning and the Sequoia and First Round backing line
- https://arena.ai/blog/coding-agents-harness-tax - the HarnessTax study the announcement cites as its framing reference
