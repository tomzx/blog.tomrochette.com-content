---
title: goose
created: 2026-08-24
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, coding-agents, harnesses, open-source, linux-foundation]
readability: 3
audience_notes: >
  Engineers weighing an open agent whose stewardship does not depend on one company.
  Assumes you know what MCP is and the difference between a provider key and a subscription.

---

goose is an open-source (Apache-2.0) general-purpose AI agent written in Rust, started inside Block and now governed by the Agentic AI Foundation (AAIF) at the Linux Foundation.

**goose matters less for what it does than for how it is owned: it is the first major coding-adjacent agent to move from a corporate parent to a foundation, an exit path no other open harness offers.**

## What it is

**A desktop app, a CLI, and an API from one Rust codebase, for code and for everything else.**
goose runs on macOS, Linux, and Windows as a native app, or as a CLI in terminal workflows, or embedded via its API.
It talks to 15+ providers (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and more), and can reuse your existing Claude, ChatGPT, or Gemini subscriptions through ACP rather than requiring keys.
70+ extensions connect through MCP, recipes package repeatable workflows, and a goose 2.0 beta reworks the architecture and clients.

## Status

**Active and foundation-governed.**
The repository (moved from Block's org to `aaif-goose/goose`) shows about 55.3k stars as of 2026-10-15, was last pushed 2026-11-11 (GitHub API, as of 2026-11-11), and ships a steady train: v1.59.0 (November 10, adding minimal deferred MCP tools in ToolExecutionOperation, configurable per-start voice instructions for live voice, a configurable GPT-Live endpoint, model, and key, and ACP session-list filtering by client tags), after v1.58.1 (November 10, rewording the compaction prompt Opus 5.5 refused as distillation and refreshing Databricks OAuth tokens before they expire) and v1.58.0 (November 9, an opt-in context-relevance operation, a context-window report and viewer, and AIHubMix, RouterPlex, and Lemonade declarative providers), after v1.57.0 (October 28, adding an allowlist that requires HTTPS, validates redirects, and blocks on policy failure, caller-supplied Goose session IDs, OpenRouter variant suffixes like `:free` and `:nitro` resolving to the base model, and desktop, scheduler, voice, and custom-prompt fixes).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aaif-goose/goose&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aaif-goose/goose&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aaif-goose/goose&type=date&legend=top-left" />
</picture>

The January 2025 launch drew a 249-point Hacker News thread, and coverage through 2026 describes adoption scaling to a majority of Block's engineers, though that figure comes from a third-party course site, not a Block primary source.
Block contributed goose at the AAIF's formation on December 9, 2025, alongside Anthropic's MCP and OpenAI's AGENTS.md, and the project completed its migration to the aaif-goose organization on April 7, 2026.

## Strengths

- **Neutral stewardship**: a Linux Foundation home means no single vendor decides its roadmap or repricing.
- General-purpose design covers research, writing, and automation beyond code edits.
- ACP subscription reuse is rare in the field: pay for a model subscription once, drive it from goose.
- Rust core with desktop, CLI, and API surfaces, plus a documented custom-distro path for teams.

## Cautions

- **Generalist first, coder second**: fewer of the coding-specific conveniences (repo-map editing, IDE-grade grounding) than the coding-native harnesses.
- The 2.0 architecture rewrite plus the org migration means churn; the move announcement itself lists broken links, redirects, and CI as open migration work.
- Adoption claims beyond the launch thread are thinly sourced; treat the "60% of Block" number as unverified by Block itself.
- Community discussion volume is modest relative to star count.

## Pricing

Free and Apache-2.0; providers bill you directly.
The unusual path is subscription reuse: existing Claude, ChatGPT, or Gemini subscriptions can supply usage via ACP, so you may need no new billing relationship at all.

## Compared to

- [OpenCode](../opencode/index.md): the coding-specialized MIT harness with the larger community; choose it when code is the whole job.
- [Cline](../cline/index.md): IDE-native and coding-first versus goose's desktop-generalist spread.
- [Amp](../amp/index.md): paid remote execution with orbs versus goose's local, free execution.

## Bottom line

**Recommended for engineers who want an agent whose stewardship outlives any one company, and for automation work beyond pure coding.**
Not for teams that want a coding-specialized harness or a single vendor's support contract.

## Changes

- 2026-08-24 - Created in a new-entrant scan with the AAIF move and ACP subscription-reuse path recorded.
- 2026-08-26 - Reconciled the AAIF timeline (contribution at the December 9, 2025 formation, migration completed April 7, 2026).
- 2026-08-27 - Canonicalized the aaif.io formation-announcement reference.
- 2026-09-16 - Refreshed repository scale to about 54.3k stars.
- 2026-10-07 - Added the aaif-goose/goose star history chart to the Status section.
- 2026-10-17 - Recorded the v1.54.0 and v1.55.0 releases (October 8 and 16), the latter adding a declarative AIgateway provider, ACP-to-MCP trace-context propagation, a Responses API preference, and the 225k auto-compaction cap, and re-fetched every cited reference in the rotation pass.
- 2026-10-24 - Recorded the v1.56.0 release (October 23): automatic thinking-level operation, resumable delegate subagents with view-only session links, the GOOSE_MAX_CONCURRENT_SUBAGENTS cap, OSC 7501 status reporting, an IO Intelligence provider, and Boa replacing PCTX as the code-mode runtime.
- 2026-10-29 - Recorded the v1.57.0 release (October 28): an allowlist that requires HTTPS, validates redirects, and blocks on policy failure, caller-supplied Goose session IDs, OpenRouter variant suffixes like `:free` and `:nitro` resolving to the base model, and desktop, scheduler, voice, and custom-prompt fixes; refreshed the push date to 2026-10-28.
- 2026-11-06 - Rotation re-verification, re-fetching every cited reference (all live), with v1.57.0 confirmed the newest release and the push date refreshed to 2026-11-06.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - goose in the independent tail of the harness layer
- [ACP](../../protocols/acp/index.md) - the protocol goose uses for both subscriptions and editor hosting
- [MCP](../../protocols/mcp/index.md) - the extension standard behind goose's 70+ integrations
- [The Shifting Bottleneck](../../../the-shifting-bottleneck/index.md) - why agent context and cost, not generation, decide outcomes

## References

- https://github.com/aaif-goose/goose - README, license, surfaces, repository scale as of 2026-10-11
- https://goose-docs.ai/docs/getting-started/installation - install paths, desktop and CLI, AAIF banner
- https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif - the April 7, 2026 migration-completion announcement
- https://aaif.io/news/linux-foundation-announces-formation-of-aaif - the December 9, 2025 formation announcement listing goose as a founding contribution
- https://news.ycombinator.com/item?id=42879323 - the January 2025 launch thread (249 points, 68 comments)
- https://news.ycombinator.com/item?id=48279117 - the "60% of Block" coverage, a weak-sourced claim worth marking
