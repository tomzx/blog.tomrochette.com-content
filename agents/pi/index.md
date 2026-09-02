---
title: Pi
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harnesses, coding-agents, open-source, byok, extensibility]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent who want to own the harness instead of configuring it.
  Assumes you know what BYOK, a system prompt, and an agent loop are.
---

Pi is an MIT-licensed TypeScript agent toolkit from Earendil whose flagship is a minimal, self-extensible terminal coding agent that you adapt through extensions rather than configuring a closed product.
Facts below verified as of 2026-09-02.

**Pi's thesis is that a coding agent should be a small frozen core plus your code, and it is the only harness at this scale whose author treats missing features as policy rather than backlog.**

## What it is

A CLI (`@earendil-works/pi-coding-agent`) plus reusable packages: `pi-ai` (unified API for 15+ providers with mid-session model switching), `pi-agent-core` (the agent loop), `pi-tui`, and `pi-telemetry`.
Four surfaces come from one binary: interactive TUI, one-shot print mode, RPC over stdio, and a Node SDK.
Sessions are tree-structured JSONL with in-place branching, compaction, and HTML export.
Extensions, skills, prompt templates, and themes are TypeScript, shareable as npm or git packages, and the system prompt is under 1,000 tokens and replaceable.
Install is npm or a standalone Bun binary; models come from your own API keys or existing subscriptions (Claude, ChatGPT, Copilot) or local llama.cpp servers.
Made by Earendil Inc., created by Mario Zechner with Armin Ronacher as the second-largest contributor; formerly badlogic/pi-mono.

## Status

Active and ascending: 100,732 stars (past the 100k mark), 12,518 forks, 170 open issues and PRs as of 2026-09-02.
Created 2025-08-09, 5,838 commits, pushed the day of verification, releases roughly weekly (v0.84.4 on 2026-08-28).
**The ecosystem is the strongest signal: OpenClaw runs on Pi, and oh-my-pi, a batteries-included fork with 28,974 stars, exists precisely because some users want the features Pi refuses to ship.**

## Strengths

- Radical extensibility: subagents, plan mode, and permission gates all exist as extensions you can read, and the agent can modify and reload itself.
- Provider freedom with cross-provider context handoff, plus a deliberately minimal and stable prompt and tool surface.
- Supply-chain discipline: pinned dependencies, `--ignore-scripts` install, audit in CI, standalone binaries built from signed sources.
- Credible maintainers and a public Terminal-Bench 2.0 submission.

## Cautions

- No sandbox: the README says it runs with full user permissions, and isolation is your job (containers, micro-VMs), which was the most contested point in its Hacker News thread.
- Opinionated omissions are policy: no MCP, no sub-agents, no plan mode, no built-in todos by design; you build or install them.
- Contribution gatekeeping: new contributors' issues and PRs are auto-closed by default, and the author is explicit about dictatorial scope control.
- 84 minor versions in a year means real breakage risk, and the name is nearly unsearchable.

## Pricing

Free and open source under MIT.
No hosted tier; the only costs are the model providers you connect.

## Compared to

- [Claude Code](../claude-code/index.md): sealed, subscription-first, rich built-ins that change every release; choose Pi when context control and stability matter more than hand-holding.
- [OpenCode](../opencode/index.md): also open and multi-provider, but batteries-included with a full TUI; choose OpenCode for rich defaults, Pi to own the harness.
- [Codex](../codex/index.md): OpenAI-tied with kernel-enforced sandboxing; choose Pi for model flexibility if you bring your own isolation.

## Bottom line

**Recommended for engineers who want a harness they can read, extend, and pin, and who will take sandboxing seriously themselves.**
Not for teams wanting turnkey guardrails, MCP-centric stacks, or a stable API surface this year.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability comparison this note joins
- [OpenClaw](../openclaw/index.md) - the largest product built on the Pi toolkit
- [OpenCode](../opencode/index.md) - the batteries-included counterpart
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where Pi sits in the harness layer

## References

- https://github.com/earendil-works/pi - repository, packages, license, contribution policy
- https://raw.githubusercontent.com/earendil-works/pi/HEAD/packages/coding-agent/README.md - install, providers, four modes, philosophy
- https://pi.dev - positioning, extension model, and the list of features deliberately not built
- https://mariozechner.at/posts/2025-11-30-pi-coding-agent/ - the author's rationale for the minimal prompt and YOLO default
- https://news.ycombinator.com/item?id=46844822 - the 421-point thread with pushback on the security posture
- https://github.com/can1357/oh-my-pi - the 28k-star batteries-included fork, the counterargument in running code
