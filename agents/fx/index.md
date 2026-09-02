---
title: fx
created: 2026-08-29
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, zig, vercel, embedding]
readability: 3
audience_notes: >
  Engineers embedding coding agents into other programs, sandboxes, or constrained environments.
  Assumes you know what a harness, an agent loop, and BYOK mean.
---

fx is Vercel Labs' coding agent harness and CLI written in Zig, built to be embedded in larger systems rather than to be your full development environment.
Facts below verified as of 2026-09-02.

**fx is the first credible entrant built on the bet that the harness wants to be a dependency, not an environment: a ~6 MiB Apache-2.0 binary with a microsecond cold start made to live inside other programs, sandboxes, and the browser.**

## What it is

A single Zig binary (~6.19 MiB for v0.0.7 per the [site](https://fx.sh/)) that claims a 10 microsecond cold start and does no unnecessary I/O before accepting input, with a CLI form factor pitched closer to a Unix shell than an IDE-in-the-terminal TUI.
It is open source (Apache-2.0), model-agnostic, and compiles to WebAssembly, which is how the site runs the whole agent in a browser demo.
Feature surface: native [AGENTS.md](https://fx.sh/docs/configure-fx/project-instructions) loading (global, workspace, and per-directory), [MCP](https://fx.sh/docs/capabilities/mcp), Claude-format skills directories (.claude/skills/ and peers), [subagents](https://fx.sh/docs/capabilities/subagents) as persistent child sessions with durable message queues, web search, vision, and an [`fx acp`](https://fx.sh/docs/using-fx/acp) server so ACP-speaking editors can host it.

## Status

**Active and very young.**
The repository was created August 11, 2026 and shows 2,680 stars and 308 forks as of 2026-09-02, with v0.0.7 still the latest release and pushes landing the same day (GitHub API).
The launch thread drew 318 points on August 18, 2026 ([HN](https://news.ycombinator.com/item?id=49353339)).
The README carries its own banner: "Status: Experimental. Use at your own risk."

## Strengths

- **Embeddability is the actual product**: Node SDK, WebAssembly SDK, and browser integration for putting an agent inside sandboxes, CI, and other tools, which no mainstream harness treats as the primary use case.
- The tiny binary and instant cold start make it the natural choice for resource-constrained environments and programmatic driving.
- Reads AGENTS.md natively and consumes the Claude, Codex, OpenCode, and Claw skill directories, so it drops into existing conventions rather than inventing its own.
- Subscription reuse without token exposure: ChatGPT via Codex OAuth and Grok via xAI OAuth, with sessions stored locally and never sent to Vercel ([docs](https://fx.sh/docs/getting-started/authentication)).

## Cautions

- **Open source does not mean vendor-neutral**: every model request routes through Vercel AI Gateway regardless of credential, so Vercel sits on the meter and the metadata even when you self-host the binary ([usage docs](https://fx.sh/docs/using-fx/usage-and-costs)).
- v0.0.x with frequent changes promised; the site's own demo page says "use at your own risk, we will be making frequent changes".
- No local-model path and no direct provider keys are documented: the catalog is Vercel AI Gateway, Codex, or Grok, nothing else (models and authentication pages).
- No hooks or plugins mechanism; skills only.
- The pipe-to-shell installer (`curl ... | bash`) is the default install path; the docs themselves ask you to read the installation page first.

## Pricing

The software is free under Apache-2.0.
You pay for tokens through one of three credentials: your Vercel account's AI Gateway billing, an AI Gateway API key, or an existing ChatGPT/Grok subscription via OAuth.
There is no fx-specific subscription.

## Compared to

- [OpenCode](../opencode/index.md): the MIT full-environment harness with local models and any provider; pick OpenCode as your daily driver, fx when you need an agent inside something you are building.
- [goose](../goose/index.md): the other subscription-reuse story, but as a full Rust agent platform rather than an embeddable minimal binary.
- [Crush](../crush/index.md): the other small single-binary agent, but terminal-first rather than embed-first.

## Bottom line

**I would reach for fx when the agent is a component of my system (a sandbox, a pipeline, a product), and stay on OpenCode or a platform harness when the agent is where I work.**
Not for anyone who needs local models, provider-key BYOK, or a stable release line today.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where fx lands in the harness layer's independent tail
- [OpenCode](../opencode/index.md) - the full-environment MIT harness fx is the minimal counterpoint to
- [goose](../goose/index.md) - the other harness that reuses subscriptions you already pay for
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - fx measured against the other thirteen on shared rows

## References

- https://github.com/vercel-labs/fx - repository, Apache-2.0, scale and releases, as of 2026-09-02
- https://fx.sh/ - product claims, v0.0.7 binary size, Wasm demo, cold start
- https://fx.sh/docs/getting-started/authentication - the three-credential provider model and local token storage
- https://fx.sh/docs/configure-fx/project-instructions - native AGENTS.md loading
- https://fx.sh/docs/capabilities/subagents - the persistent-child subagent system
- https://fx.sh/docs/using-fx/acp - the ACP server mode for editor hosting
- https://fx.sh/docs/using-fx/usage-and-costs - the AI Gateway routing and local usage tracking
- https://news.ycombinator.com/item?id=49353339 - the August 18, 2026 launch thread
- https://vercel.com/oss - Vercel Labs stewardship
