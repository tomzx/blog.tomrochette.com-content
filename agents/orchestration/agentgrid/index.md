---
title: AgentGrid
created: 2026-10-02
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, desktop, canvas, closed-source]
readability: 3
audience_notes: >
  Engineers who run several CLI coding agents and want them visually arranged, delegated to, and reviewed on one desktop canvas.
  Assumes you know what a coding harness session is and are comfortable with closed-source desktop software.
---

AgentGrid is a closed-source desktop app for macOS, Windows, and Linux that puts coding agents, terminals, browsers, source control, and notes as movable panes on one infinite canvas, with a master agent coordinating workers through MCP tools.

**Its bet is visual delegation: the canvas is the coordination surface, so a master agent spawning workers is something you watch, arrange, and interrupt by hand instead of configuring in YAML.**

## What it is

A commercial desktop application built by a two-person team in Vancouver (@0xPaperhead and @yagudaev), distributed as a download with a hosted pricing plan.
Each space in the title bar binds a project folder and owns a pane layout, so new agents and terminals open in the right working directory.
It supports Claude Code, Codex, OpenCode, Antigravity, Cursor, Devin, Grok, Kimi, and Pi, enable-and-ordered in settings, and any pane can be an agent, terminal, source-control view, browser, or note.
A master (or orchestrator) agent starts workers for focused tasks through AgentGrid's MCP tools, choosing any installed harness and an optional model per role, and agent sessions can launch in their own git worktrees with concurrent launches isolated automatically.
A built-in source-control view and an agent review bot put worktree state, pull request conversations, and file diffs beside the canvas.

## Status

Active and fast-moving: v2.9.5 shipped 2026-10-07 (Coordinator runs as a chosen account, PR attribution with a get_pr_cost MCP tool, shared request pricing and ledger types, and GitHub cost comments), hours after v2.9.4 added multi-account-per-harness support and an opt-in performance probe, on top of near-daily releases through September and October.
The vendor's pricing page, which returned HTTP 500 on 2026-10-03, serves again as of 2026-10-05 with the same Free $0 and Pro $16/month tiers, still serving on 2026-10-07, and the changelog and download page carried v2.9.4 as of 2026-10-07 and v2.9.5 as of 2026-10-08.
**The community footprint is the weakest part of the story: a Show HN thread from 2026-08-25 that sits at 1 point with 0 comments, no public repository, and a "5,000+ AI builders" community claim that only the vendor's own site corroborates.**
Treat the traction numbers as marketing until an independent source confirms them.

## Strengths

- The spatial model is genuinely useful for supervision: one glance shows every running agent, terminal, and diff pane, and layouts persist per project space.
- Master/worker delegation through MCP means an agent, not just a human, can arrange and dispatch work on the canvas.
- Nine harnesses supported out of the box with per-role model choice, more than most closed competitors expose.
- Cross-platform desktop builds (macOS, Windows, Linux) where much of this category is macOS-only.
- Bring-your-own subscriptions: the app drives the Claude, ChatGPT, and other accounts you already pay for.

## Cautions

- Closed source with no public repository, so there is nothing to audit and nothing to fork if the two-person team stops shipping.
- Near-zero independent footprint: one 1-point Show HN thread and vendor-claimed community size.
- The pricing is early-adopter churn waiting to happen: Pro is $16/month billed annually as an "early-adopter price" against a stated regular value of $600/year.
- Delegation runs on the vendor's MCP tool surface, so workflows built on it are AgentGrid-specific by construction.
- Pane-per-agent on an infinite canvas invites clutter faster than a board or queue UI; the product leans on your own discipline.

## Pricing

Free tier: $0, 3 projects, up to 10 parallel agents per project, local agents on your own machine.
Pro: $16/month billed annually ($192/year, early-adopter price, stated regular value $600/year) with unlimited canvases, cloud sync across machines, and local plus cloud agents.
AI subscriptions and API usage are paid separately to your providers.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-02 | Free, Pro | Free $0 (3 projects, 10 parallel agents each) and Pro $16/mo billed annually ($192/yr early-adopter, regular value $600/yr) observed | https://agentgrid.sh/pricing |

## Compared to

- [Helmor](../helmor/index.md): Helmor is the open-source Apache-2.0 workbench for planning-through-shipping loops; choose it when source availability matters, AgentGrid for the canvas-first visual model.
- [Emdash](../emdash/index.md): Emdash auto-detects installed CLIs in a plain Electron app; simpler and open, but no master/worker delegation.
- [JetBrains Air](../jetbrains-air/index.md): Air is the vendor bundle play (subscription unlock, org governance); AgentGrid is the independent small-team product with a free local tier.

## Bottom line

**Recommended for engineers who think in layouts and want visible, interruptible master/worker delegation on their own desktop.**
Not for anyone who requires open source, an auditable supply chain, or pricing that will not reset when the early-adopter window closes.

## Changes

- 2026-10-02 - Created.
- 2026-10-05 - Recorded v2.9.3 (October 4) from the vendor changelog, and re-verified the pricing page serving again with unchanged tiers after the 2026-10-03 HTTP 500.
- 2026-10-08 - Recorded v2.9.5 (October 7, PR attribution and a get_pr_cost MCP tool) and re-verified the pricing page tiers unchanged.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Helmor](../helmor/index.md) - the open-source desktop workbench alternative
- [Emdash](../emdash/index.md) - the open auto-detecting Electron alternative
- [JetBrains Air](../jetbrains-air/index.md) - the vendor-bundle desktop entry
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://agentgrid.sh/ - product positioning, platform support, the harness list, and the vendor's community-size claim
- https://agentgrid.sh/docs - the canvas, space, pane, master, and worker mental model and MCP delegation tools
- https://agentgrid.sh/pricing - the Free and Pro tiers, the early-adopter price against the stated regular value, and the BYO-subscription note, fetched 2026-10-02 and re-fetched 2026-10-05 (HTTP 500 on 2026-10-03)
- https://agentgrid.sh/changelog - the release cadence through v2.9.2 (2026-09-29)
- https://news.ycombinator.com/item?id=49436219 - the 2026-08-25 Show HN thread (1 point, 0 comments), evidence of the missing community footprint
