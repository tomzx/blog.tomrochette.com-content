---
title: 1Code
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, desktop, worktrees, dormant]
readability: 3
audience_notes: >
  Engineers who saw 1Code in its January 2026 launch wave and want to know whether it is maintained, and anyone studying how fast the coding-agent-client genre churns.
  Assumes you know what Claude Code and a git worktree are.
---

**1Code was the open-source "Cursor for Claude Code" that pulled 5.6k stars in two months and then went silent in March 2026, and it stays here because the silence is the information.**

## What it is

1Code is an open-source (Apache-2.0) coding agent client from the 21st.dev team, shipped as a macOS desktop app plus web, Windows, and Linux surfaces, wrapping Claude Code and Codex behind a Cursor-like UI.
Each chat runs in its own git worktree with diff previews and a built-in git client, sessions organize on a kanban board, and background agents run in cloud sandboxes when the laptop sleeps.
The feature list also carried BYOK model selection, MCP servers and a plugin marketplace, automations triggered from GitHub, Linear, Slack, or git events, chat forking, voice input, and a PWA plus API for starting and monitoring agents from a phone or a script.

## Status

Dormant: the repository shows 5,582 stars, 611 forks, and 45 open issues, but its last push and its last release (v0.0.84) both landed 2026-03-06, seven months before this check (GitHub API, as of 2026-10-06).

[![Star History Chart](https://api.star-history.com/chart?repos=21st-dev/1code&type=date&legend=top-left)](https://www.star-history.com/?repos=21st-dev%2F1code&type=date&legend=top-left)

The launch Show HN drew 75 points and 49 comments on 2026-01-15, and the thread's sharpest exchange was about price: commenters called the $20/month hosted web tier expensive for "a web interface and a sandbox", and the founders answered that the paid tier was about signal, not monetization.
**The product domain now redirects to the GitHub repository, so the hosted surface this note's pricing discussed is gone from the public web, and nothing in the repo records a handoff, an archive notice, or a successor.**
I read the record as an abandoned open-source client rather than a pivot: no successor product is announced, and the team's other properties continued separately.

## Strengths

- The January feature set matched or beat the closed Mac clients on paper: worktree-per-chat, kanban, background cloud agents, automations, phone access, and an API, all under Apache-2.0.
- The launch thread shows demonstrated demand for a GUI over the harness CLI, with the founders' CLI-struggle story drawing hundreds of thousands of views on social media.

## Cautions

- Seven months without a commit or release as of 2026-10-06, with 45 open issues and no maintainer response on record.
- The hosted tier launched at $20/month against a free CLI, and the pricing objection in the launch thread was never resolved by traction evidence.
- The domain redirecting to the repo means there is no product to evaluate today, only a codebase.

## Pricing

The desktop client is free and open source under Apache-2.0.
At launch, the hosted web tier cost $20 per month for remote sandboxes; the hosted surface is no longer verifiably available.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-01 | Hosted web | Baseline: $20/month for the hosted web tier (remote sandboxes) at launch; desktop client free | https://news.ycombinator.com/item?id=46637723 |

## Compared to

- [Emdash](../emdash/index.md): the open cross-platform client that kept shipping; choose Emdash for a maintained Apache-2.0 alternative to the closed Mac apps.
- [AgentGrid](../agentgrid/index.md): the closed canvas client that is still releasing near-daily; AgentGrid is what 1Code's momentum looks like when it continues.
- [Vibe Kanban](../vibe-kanban/index.md): the other vendor-lost project in this category, with the difference that its community kept committing after the shutdown, while 1Code has no recorded handoff at all.

## Bottom line

Recommended only as a study in the client genre's churn: strong launch, fast stars, silent spring.
Not for adoption; if the idea appeals, evaluate Emdash or the maintained closed clients on their own merits.

## Changes

- 2026-10-06 - Created after the entrant scan confirmed the repository has been silent since 2026-03-06; recorded as dormant with the launch-thread pricing record.
- 2026-10-07 - Added the 21st-dev/1code star history chart to the Status section.

## See also

- [Emdash](../emdash/index.md) - the maintained open client in the same genre
- [Vibe Kanban](../vibe-kanban/index.md) - the vendor-loss comparison case with a living community
- [Flowise](../flowise/index.md) - the archived genre-mate whose post-mortem named coding agents as the cause
- [Conductor](../conductor/index.md) - the funded closed client that shows what continued investment looks like

## References

- https://github.com/21st-dev/1code - repository, feature list, license, stars, and the March 2026 last push (GitHub API, as of 2026-10-06)
- https://news.ycombinator.com/item?id=46637723 - the 75-point launch thread and the $20/month pricing critique
- https://1code.dev - the product domain, which now redirects to the GitHub repository (fetched 2026-10-06)
- https://github.com/21st-dev/1code/releases - release history stopping at v0.0.84 (2026-03-06)
- https://api.github.com/repos/21st-dev/1code - the API record of stars, forks, and the 2026-03-06 push date (as of 2026-10-06)
