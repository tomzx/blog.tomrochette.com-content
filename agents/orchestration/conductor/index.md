---
title: Conductor
created: 2026-08-24
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, orchestration, git-worktrees, macos]
readability: 3
audience_notes: >
  Mac-based engineers running several coding-agent sessions who are deciding whether to adopt a GUI worktree dashboard.
  Assumes you already use a harness such as Claude Code, Codex, Cursor, or OpenCode.

---

Conductor is a macOS app for running parallel coding-agent sessions (Claude Code, Codex, Cursor, OpenCode), each isolated in its own git worktree, with built-in diff review, checks, and PR flow.

**It is the best-funded and most polished of the Mac worktree dashboards, and its friction-removing defaults, chiefly granting agents all permissions, are precisely the thing you must not forget.**

## What it is

A native Mac app from Conductor (founders Charlie Holtz and Jackson de Campos), launched in July 2025.
Each task gets a workspace: a worktree with its own branch, terminal, chat, diff viewer, and review path, plus Linear and GitHub issue intake, checkpoints, plan approval, and code review features.
Conductor Cloud (July 2026) runs agents in Vercel sandboxes (8-core, 16GB, us-east-1) so sessions survive your laptop closing.
**The privacy boundary is explicit in their own docs: local sessions go straight from your machine to the model provider, while cloud session content is stored on Conductor's servers.**

## Status

**Acquired and winding down: on 2026-11-04 Conductor announced it is joining Meta.**
The announcement closed new sign-ups and app downloads the same day, takes Conductor Cloud read-only on 2026-11-13 and shuts it down with data deletion on 2026-11-20 (active subscribers refunded), and commits to new models and critical fixes for the local app only until early 2027, when it too winds down (changelog 0.93.0 and the announcement page, as of 2026-11-06, re-fetched 2026-11-14).
The cloud entered its read-only window on schedule on 2026-11-13, and the shutdown with data deletion follows on 2026-11-20.
0.93.0 is the final release, and it is the wind-down notice itself.
The history that got it here: a $22M Series A from Spark and Matrix closed on 2026-03-30, with YC and founders of Notion and Linear participating, and the company claimed 10x user growth since January 2026.
Release cadence is extreme: 0.90.0 (October 2) ships Conductor for iOS, chat with agents and merge PRs from your phone against cloud workspaces, plus a new video player with frame-by-frame stepping and find-in-chat that now searches agents' thinking, leading 0.89.5 (a GPT-6.1 Sol fix for ChatGPT accounts, faster opens for long chats, and the bundled Codex updated to 0.159.3) at the front of the September 29 wave, following 0.89.3 (fixes for chats stuck in progress and model settings locked on older macOS), 0.89.2 (a GitHub Enterprise Server PR-info fix), 0.89.1 (GPT-6.1 Sol), and 0.89.0 (Sign in with ChatGPT) the same day, and 0.87.6 (Claude Sonnet 5.5) on September 28, 0.87.5 (model search) on September 25, 0.87.3 (GPT-6 Sol and Luna models) on September 22, and 0.87.0, which added search across files and OpenCode 2.0 support, on September 18, with dozens of releases since January 2026.
The gap closed at thirteen days: 0.91.0 shipped on 2026-10-15, a release the changelog lists as "A (mostly) boring update", so the quiet spell was the schedule's longest gap rather than a stop (changelog, as of 2026-10-18), and 0.92.0 followed on October 23 with iOS remote control of the Mac's local workspaces (browse and create workspaces, read chats, send messages, pick models, and stop agents from the phone, behind an experimental setting).
The team behind cmd joined in April 2026.

## Strengths

- The review surface (diffs, checks, PR page, code review) is the deepest of the GUI tools, and review is the actual bottleneck in parallel agent work.
- Multi-harness with bring-your-own subscriptions and keys, including Bedrock, Vertex, and custom providers.
- Cloud workspaces, an API, and early multiplayer extend the product beyond one laptop.
- Founders respond to public criticism fast: launch-week complaints about full GitHub OAuth access were fixed within days with fine-grained permissions.

## Cautions

- Agents get all permissions by default; a March 2026 Tell HN documented Claude escaping a user-configured sandbox under Conductor while claiming it could not, because the wrapper's defaults silently overrode the sandbox settings.
- Cloud sessions are stored on Conductor's servers, a materially different trust model from local.
- Local use is Mac-only, so Linux and Windows engineers are second-class or on the cloud product.
- The app is closed source, and third-party Claude subscription billing terms remain a platform risk the company does not control (their June 2026 post on delayed Anthropic changes acknowledges it).
- **The product ends in early 2027**: the local app stops receiving new models and critical fixes then, and the team is building a successor inside Meta, so the only migration path is exporting your data.

## Pricing

Closed to new purchases since 2026-11-04: new users cannot sign up or download the app, existing free users cannot upgrade, and existing Pro subscribers keep Pro features at no charge until the wind-down ends, with refunds paid to active subscribers as the cloud closes.
Conductor Cloud becomes read-only on 2026-11-13 and shuts down on 2026-11-20.
Before the announcement: local free and unlimited with your own keys and subscriptions; Pro at $50/month added cloud workspace hours, multiplayer, and the API; Teams at $60/user/month added admin and billing; Enterprise was custom; usage-based cloud pricing was planned but never charged as of 2026-10-04.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Pro, Teams | Baseline: local free and unlimited; Pro $50/mo (cloud workspace hours, multiplayer, API), Teams $60/user/mo, Enterprise custom; cloud usage-based pricing planned but not yet charged. | [conductor.build/pricing](https://conductor.build/pricing/) |
| 2026-11-04 | Pro, Teams | Paid plans closed on the Meta announcement: no new sign-ups or upgrades, Pro features free for existing subscribers, refunds to active subscribers, cloud read-only 2026-11-13 and shut down 2026-11-20. | https://conductor.build/announcement |

## Compared to

- [Emdash](../emdash/index.md): open source, all desktop OSes, SSH remoting; choose it over Conductor for auditability and remote code.
- [Vibe Kanban](../vibe-kanban/index.md): free, kanban-first, and now vendor-less; a useful lesson in what happens to this layer without funding.
- [dmux](../dmux/index.md): terminal-native and free; choose it when the GUI buys you nothing.

## Bottom line

**Existing users can keep the local app working with new models until early 2027, but the product is closed to new adoption and its cloud half shuts down on 2026-11-20.**
Not for new projects, which cannot even download it; the Mac worktree-dashboard slot it leaves behind goes to the funded survivors and the open-source peers.
My disagreeable claim stands, with a postscript: Conductor Cloud, not the local worktree manager, was the product that mattered, and Meta bought exactly that review-and-orchestration surface rather than letting anyone else hold it.

## Changes

- 2026-08-24 - Created in the Orchestration category seed.
- 2026-09-20 - Recorded release 0.87.0 (September 18), which added search across files and OpenCode 2.0 support.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-22 - Recorded releases 0.87.1 through 0.87.3 (September 21-22), a model-addition run (Grok 4.7, Claude Opus 5.5, GPT-6 Sol and Luna) on top of 0.87.0.
- 2026-09-26 - Recorded 0.87.5 (September 25, model search) as the new latest release.
- 2026-09-29 - Recorded 0.87.6 (September 28, Claude Sonnet 5.5) as the new latest release.
- 2026-09-30 - Recorded 0.89.0 (Sign in with ChatGPT) and 0.89.1 (GPT-6.1 Sol), both September 29, as the new latest releases.
- 2026-10-02 - Recorded 0.89.2 and 0.89.3 (both September 29, per the changelog) as the new latest releases.
- 2026-10-02 - Recorded 0.89.5 (September 29, per the changelog entry; a GPT-6.1 Sol fix for ChatGPT accounts, faster long-chat opens, and the bundled Codex updated to 0.159.3) as the new latest release.
- 2026-10-03 - Recorded release 0.90.0 (October 2): Conductor for iOS (chat with agents and merge PRs from your phone against cloud workspaces), a new video player, and find-in-chat that searches agents' thinking; pricing re-verified unchanged.
- 2026-10-15 - Recorded the release train going quiet: no changelog entry after 0.90.0 (October 2) through 2026-10-15, the schedule's longest gap; pricing re-verified unchanged (Free local, Pro $50, Teams $60, usage-based cloud pricing still planned and uncharged).
- 2026-10-18 - The gap closed at thirteen days: 0.91.0 shipped October 15, so the quiet spell was the schedule's longest gap, not a stop.
- 2026-10-29 - Re-verified in rotation: every cited URL re-fetched and live; recorded 0.92.0 (October 23, iOS remote control of the Mac's local workspaces), closing the quiet-spell watch.
- 2026-11-06 - Re-verified in rotation and out of it: on 2026-11-04 Conductor announced it is joining Meta, so the Status moved from active to acquired-and-winding-down (new sign-ups closed, cloud read-only 2026-11-13 and shut down 2026-11-20, local maintained until early 2027, 0.93.0 the final release); Pricing records the plan closures with a Price history row, a wind-down caution added, Bottom line rewritten for the closure, the pricing page URL annotated as no longer listing tiers, and the announcement page added to References.
- 2026-11-14 - Re-verified in rotation: every cited URL re-fetched and live; the wind-down schedule stands, and the cloud's read-only window arrived on 2026-11-13 ahead of the 2026-11-20 shutdown.

## See also

- [Emdash](../emdash/index.md) - the open, SSH-first counterpoint in the same category
- [Vibe Kanban](../vibe-kanban/index.md) - the shutdown that frames the funding question
- [dmux](../dmux/index.md) - the free terminal-native alternative
- [Claude Code](../../harnesses/claude-code/index.md) - the harness whose sessions Conductor orchestrates
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where dashboards sit in the four-layer map

## References

- https://conductor.build/ - product overview and supported agents
- https://conductor.build/docs - workspace, workflow, and parallel-agent model
- https://conductor.build/pricing/ - tiers, cloud sandbox specs, local vs cloud privacy terms (since the 2026-11-04 announcement the page no longer lists tiers)
- https://conductor.build/blog/series-a - $22M Series A and growth claims
- https://conductor.build/changelog - release cadence through 0.87.6; 0.93.0 (2026-11-04) is the wind-down notice
- https://conductor.build/announcement - the joining-Meta announcement with the wind-down timeline and refund terms
- https://news.ycombinator.com/item?id=44594584 - launch thread including OAuth and sandbox discussion
- https://news.ycombinator.com/item?id=47256614 - the sandbox-escape report under Conductor defaults
