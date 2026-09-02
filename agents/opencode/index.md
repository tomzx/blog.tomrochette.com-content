---
title: OpenCode
created: 2026-08-22
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, coding-agents, harnesses, open-source, developer-tools]
readability: 3
audience_notes: >
  Engineers who pay for their own tokens or switch providers often, evaluating the main vendor-neutral harness.
  Assumes familiarity with AGENTS.md, MCP, and what a prompt-cache prefix is.

---

OpenCode is the open-source (MIT), provider-neutral coding agent from Anomaly: a TUI, desktop app, IDE extension, and web view built off one codebase, running against any provider's API keys.
Facts below verified as of 2026-09-02.

**OpenCode is what a harness should cost in tokens, roughly a fifth of Claude Code's measured baseline, and its 2026 security and legal history is a working lesson in why agent clients need audits too.**

## What it is

The `opencode` TUI ships build and plan agents (Tab to switch), a general subagent, `/init` generating an AGENTS.md, `/undo` and `/redo` of agent changes, and shareable conversation links.
**One codebase also produces a desktop app, a VS Code extension, a web view, an SDK, a server, and `opencode acp`, which hosts the agent inside ACP-speaking editors (Zed, JetBrains, Neovim) unchanged.**
Providers are configured by API key; OpenCode Zen is the team's curated, tested model gateway.

## Status

**Very active.**
The repository moved from `sst` to `anomalyco/opencode` and shows about 203.1k stars, 26.5k forks, and 15,636 commits under MIT as of 2026-09-02.
It originated in the 2025 opencode-ai/Charm split that also produced Crush.
OpenCode is the continuation that kept the name, the domain, and the community.

## Strengths

- **The leanest measured harness of the majors**: about 7k baseline tokens versus about 33k for Claude Code, byte-stable cache prefixes, and about 3.7x cheaper on a matched pass/fail benchmark ([July 2026 proxy study](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)).
- Truly provider-neutral, reading both AGENTS.md and CLAUDE.md.
- ACP support makes your editor choice irrelevant while keeping one harness.
- Undo/redo and share are small features that match how people actually work.

## Cautions

- **[CVE-2026-22812](https://cy.md/opencode-rce/)**: before v1.0.216 any website could execute code on your machine via the auto-started server; before v1.1.10 the server started silently; since v1.1.10 the server is off by default but still unauthenticated when enabled, with some vectors unfixed at disclosure.
- Pin your version and read the config.
- In March 2026 [Anthropic legal requests](https://github.com/anomalyco/opencode/pull/18186) removed the Claude Pro/Max OAuth login and Anthropic-branded defaults, so your Claude subscription will not drive OpenCode; use API keys or Zen.
- Fast-moving config surface; the docs carry 'versions older than 0.1.x' style of breaking-change warnings.
- Windows works best under WSL.

## Pricing

The software is free and MIT.
**You pay providers directly for tokens**, or route through OpenCode Zen with its own billing.
There is no bundled subscription usage, which is the point.

## Compared to

- [Claude Code](../claude-code/index.md): the platform-in-a-subscription; costs more per token by design.
- [Crush](../crush/index.md): same ancestor, Go and FSL-licensed, prettier; pick OpenCode for MIT and the larger community.
- [aider](../aider/index.md): also BYOK, but pair-programming style rather than an autonomous loop.

## Bottom line

**Recommended as the default for token-paying, provider-switching engineers.**
Not for teams that need subscription billing simplicity or cannot audit a fast-moving open codebase.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the vendor-neutral slot in the harness layer
- [The Shifting Bottleneck](../../the-shifting-bottleneck/index.md) - why lean harnesses matter as generation gets cheaper
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - what running several OpenCode sessions looks like
- [Claude Code](../claude-code/index.md) - the measured token-overhead comparison

## References

- https://opencode.ai/docs/ - features, install, providers, Zen
- https://github.com/anomalyco/opencode - repository scale, MIT license, desktop builds, as of 2026-09-02
- https://github.com/anomalyco/opencode/pull/18186 - the March 2026 Anthropic legal-request removals
- https://cy.md/opencode-rce/ - CVE-2026-22812 disclosure with versions and mitigations
- https://systima.ai/blog/claude-code-vs-opencode-token-overhead - the measured baseline and cache comparison
