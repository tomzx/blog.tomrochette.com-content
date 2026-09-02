---
title: Warp Agent CLI
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, terminal, model-routing]
readability: 3
audience_notes: >
  Engineers comparing subscription-backed coding harnesses who know BYOK, MCP, and AGENTS.md,
  and who want to know whether Warp's agent stands on its own outside the Warp terminal.
---

The Warp Agent CLI is Warp's terminal agent unbundled into a standalone binary that runs in any terminal, with built-in model routing, cloud agents, and multi-agent orchestration.
Facts below verified as of 2026-09-02.

**Warp is the first big terminal vendor to sell its agent separately from its own app, and that makes it the default enterprise answer unless you specifically want an open client.**

## What it is

Launched August 4, 2026, it is the same multi-model agent as Warp Terminal packaged as a CLI for Ghostty, iTerm2, VS Code, or the stock Windows and macOS terminals.
A Warp account is required, but the app is not.
It installs through a self-updating script or a Homebrew cask (`warp-agent-cli`).
Model routing is built in: frontier and US-hosted open-weight models from OpenAI, Anthropic, z.ai, and others, plus custom routers and bring-your-own inference.
Because it sits on Warp's terminal infrastructure, it muxes agent sessions natively, and cloud agents and multi-agent orchestration are first-class features.
Warp's Rust codebase is public under AGPL-3.0 at [warpdotdev/warp](https://github.com/warpdotdev/warp), about 64.7k stars as of 2026-09-02.

## Status

Active and freshly launched: announced August 4, 2026, with docs last updated August 27, 2026.
The launch thread reached 111 points on Hacker News (item 49171766).
Vendor traction is real: the terminal repository counts about 64.7k stars as of 2026-09-02, and Anthropic published a Warp engineering story on August 29, 2026.
The CLI itself ships as a managed binary with no separate public repository.

## Strengths

- **Native session muxing plus cloud agents**: the terminal infrastructure shows, and orchestration is not a bolt-on.
- Runs in any terminal, so adoption does not require migrating off your current shell.
- Subscription economics work: included credits at API rates, BYOK, and even Supergrok subscription support.
- Enterprise surface is deep: SAML SSO, admin data controls, self-hosted cloud agents, and cross-harness memory in research preview.
- Documentation is excellent, with llms.txt and a markdown page behind every URL.

## Cautions

- **The client is a closed binary** even though the codebase is AGPL-3.0, and the script install self-updates outside your package manager.
- Usage flows through Warp's credit meter, so cost predictability depends on Warp's reload pricing and spend caps.
- HN reception was skeptical (why reimplement agents rather than host existing ones), and several commenters said the terminal itself regressed as AI features expanded.
- Your sessions, memory, and billing concentrate in one vendor, which is the point, and also the lock.

## Pricing

Free at $0 with CLI access, pay-as-you-go credit reloads, and BYO inference.
Build starts at $20/month ($18 annual) with 1,500 credits ($20 of included usage at API rates).
Max starts at $200/month with 18,000 credits.
Business is $50/user/month with per-seat credits, SAML SSO, and BYOK.
Enterprise is custom, adding BYOLLM routing, self-hosted cloud agents, and cross-harness memory (research preview).
All tiers as of 2026-09-02.

## Compared to

- [Claude Code](../claude-code/index.md): the same subscription model; Claude Code has the deeper ecosystem, Warp has the orchestration and terminal pedigree.
- [Codex](../codex/index.md): open Apache-2.0 client with subscription usage behind it; choose Codex when auditability matters more than cloud orchestration.
- [OpenCode](../opencode/index.md): MIT and community-driven with pure BYOK; choose OpenCode when you want no vendor meter at all.

## Bottom line

**Recommended for teams that already buy developer tooling from a vendor and want agent sessions, cloud runs, and billing in one place.**
Not for BYOK purists, local-model users, or anyone whose policy requires an open client.
I think the CLI exists to follow developers who fled Warp's AI-heavy terminal for Ghostty and iTerm2, and the terminal stopped being the product the day the agent became it.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where this lands in the harness layer
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the terminal-versus-CLI-versus-editor treatment
- [Claude Code](../claude-code/index.md) - the subscription platform it competes with directly
- [Codex](../codex/index.md) - the open-client subscription alternative
- [OpenCode](../opencode/index.md) - the MIT counterpoint

## References

- https://www.warp.dev/blog/introducing-the-warp-agent-cli-coding-agent - launch post: scope, model routing, session muxing, cloud agents
- https://www.warp.dev/pricing - tiers, credits, and enterprise features as of 2026-09-02
- https://docs.warp.dev/agents/cli - CLI overview and documentation structure
- https://docs.warp.dev/agents/cli/quickstart.md - install methods, account requirement, self-update behavior
- https://github.com/warpdotdev/warp - codebase state, AGPL-3.0 license, stars as of 2026-09-02
- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude - Anthropic's account of Warp's agent engineering
- https://news.ycombinator.com/item?id=49171766 - launch thread, 111 points, community reception
