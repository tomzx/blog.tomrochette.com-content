---
title: Atlas
created: 2026-09-29
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, coding-agents, source-control, rust]
readability: 3
audience_notes: >
  Developers running several coding agents against one codebase who want audit-grade history of which agent did what.
  Assumes you use Claude Code or Codex and know what ACP is.
---

Atlas is the Apache-2.0 Tauri desktop app for macOS, Windows, and Linux that bills itself as source control for coding agents: every agent run becomes a checkpoint linking commits back to the session, prompts, tool calls, and reasoning that produced them.

**Atlas is the first entrant in this category whose product is the history rather than the harness: it treats agent sessions as first-class, queryable commits.**

## What it is

A desktop workspace where you run Claude Code, Codex, Atlas's own native agent, or anything from the ACP registry side by side against the same codebase, with shared memory so switching agents mid-task does not reset context (README, docs.tryatlas.cc).
Around the agents it adds an Explorer, a Spaces spatial board for notes and their connections, up to three resizable split-view columns, and a filterable activity log that survives restarts.
The README now also sells the team layer: an organization timeline where every member's sessions land, comment threads anchored to a session, prompt, tool call, or checkpoint, team chat and calls, and remote control of a running session from a browser or phone (README, as of 2026-11-08).
The repo sits at 8,558 stars with 341 forks, Apache-2.0, created 2026-05-14 (GitHub API, as of 2026-10-02).
It is a Tauri v2 app with a React 19 TypeScript frontend over a Rust backend, built from source with Bun and Rust (README, docs/architecture.md, as of 2026-11-08).
The vendor also ships Atlas CLI (tryatlas/cli, Apache-2.0): a headless Go binary that hooks the agents you already run, records every session into the same `.atlas/` folder as the app, and gives every agent one shared memory served by a local embedding model, on macOS and Linux (README, cli README, as of 2026-11-08).
In the app's chat layer a session starts in and stays bound to a project worktree, and each worktree shows and acts on its own branch (docs.tryatlas.cc product chat docs, as of 2026-11-08).
It surfaced as an entrant from the owner's GitHub stars.

## Status

Active and growing fast: 9,601 stars in five months (as of 2026-10-15), last push 2026-11-08, latest release alpha-0.4.1-org-agent on 2026-11-03, after the alpha-0.3.x line that closed with alpha-0.3.4 on 2026-09-27, both 0.4 release bodies empty so the org-agent label is all the tag says (GitHub API, as of 2026-11-08).

**The identity record moved: the repository transferred from pacifio's personal account into the tryatlas organization between the 2026-11-06 verification and this run, the old path a 301 redirect to tryatlas/atlas.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=tryatlas/atlas&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=tryatlas/atlas&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=tryatlas/atlas&type=date&legend=top-left" />
</picture>

Official installers now ship for all three platforms: signed macOS .dmg, Windows .msi, and Linux .deb, .rpm, Arch package, AppImage, and tar.gz for x86-64 with WebKitGTK 4.1 (install docs).
The alpha-0.4.1 release (2026-10-19) carried the Linux set on GitHub, but the newest tag's assets list only macOS and Windows files, so the website download is the steady Linux channel today; on Linux the app notifies about updates without installing them (releases API, install docs, as of 2026-11-08).
The README carries Trendshift badges for Rust, and releases are tags on main with squash-merged conventional-commit pull requests, a sign of release discipline inside alpha.
I re-searched HN this run and still found no launch thread and no third-party coverage: the community footprint as of 2026-11-08 is GitHub stars alone, which is itself a signal.

## Strengths

- **Agent-attributed source control is a genuinely new angle**: checkpoints that keep commit, prompt, tool calls, and reasoning together answer "which agent did exactly what and why" months later, which worktree managers and terminals in this category do not.
- Running Claude Code, Codex, and ACP agents side by side with shared memory makes agent switching cheap instead of a restart.
- The surrounding surface (Explorer, Spaces, split view, pinned activity log) treats the agent workspace as a durable place, not a terminal session.
- Traction is real for its age: 8.3k stars and Trendshift placement within five months of first commit.

## Cautions

- Alpha software (versioned alpha-0.4.x): expect breaking changes, and the squash-merged conventional-commit flow confirms churn.
- **The community footprint outside GitHub is missing**: no HN thread, no independent reviews I could find, so the 8.3k stars have no public scrutiny behind them yet.
- Small-team scale with 362 forks (as of 2026-11-08) and an alpha cadence; bus-factor risk is unquantified.
- The Linux packages need WebKitGTK 4.1 and notify rather than auto-install their updates, and building from source still means a first Rust compile in minutes, not seconds.

## Pricing

The app is still free in the alpha with bring-your-own keys, but the site now lists paid plans: Free $0 (3 members), Pro $20 per month (5 members, 10 GB session storage, $8 of included AI, 20M vectorization tokens), Team $100 per month (25 members, 50 synced projects, 100 GB, $40 AI, 100M tokens), and Business $200 per month (100 members, unlimited synced projects, 500 GB, $80 AI, 300M tokens), all four prices unchanged today (tryatlas.cc, as of 2026-11-08).
The tier features moved under the same prices: Remote Runs now sits on Team and Business only, Pro reads Not included, and the table adds per-thread caps of 8 participants and 4 concurrent runs on the low tiers against 25 and 10 on Business.
The Apache-2.0 repository itself is unchanged.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-18 | Free, Pro, Team, Business | Paid tiers first observed: no pricing page existed at creation (2026-09-29) or at the 2026-10-15 verification; site now lists Pro $20, Team $100, Business $200 per month beside the free tier | https://www.tryatlas.cc |
| 2026-11-08 | Pro, Team, Business | Prices unchanged; Remote Runs moved from Pro to Team and Business (Pro now Not included) | https://www.tryatlas.cc |

## Compared to

- [Conductor](../conductor/index.md): the macOS app for parallel Claude Code and Codex sessions; Conductor is steadier, Atlas adds the per-session audit history.
- [cmux](../cmux/index.md): the terminal-first take on parallel agents; choose cmux for keyboard-driven work, Atlas for a GUI with queryable history.
- [Orca](../orca/index.md): the broader agent development environment across desktop, mobile, and remote; Orca covers more surfaces, Atlas goes deeper on source-control integration.

## Bottom line

Recommended for developers running several coding agents against one codebase who want per-agent, per-session audit history that survives the session.
Not for teams needing a stable 1.0 or a tool with independent community validation.

## Changes

- 2026-09-29 - Created when the owner's GitHub-stars entrant resolved in the carried candidate pile.
- 2026-10-07 - Added the pacifio/atlas star history chart to the Status section.
- 2026-10-18 - Re-verified in rotation (all cited URLs re-fetched, none dead); pricing moved from none to a four-tier page (Pro $20, Team $100, Business $200 per month, app still free in alpha with BYO keys), price history table seeded.
- 2026-10-29 - Re-verified in rotation: every cited URL re-fetched and live; last push 2026-10-27 and alpha-0.3.4 (2026-09-27) unchanged, no factual drift.
- 2026-11-06 - Re-verified in rotation: every cited URL re-fetched and live; last push moved to 2026-11-06, release still alpha-0.4.1-org-agent, pricing page unchanged.
- 2026-11-08 - Recorded the repository's transfer from pacifio's personal account into the tryatlas organization (old path a 301), moved the star-history chart and repository references to the canonical tryatlas/atlas paths.
- 2026-11-08 - Corrected the Linux claim: .deb, .rpm, Arch package, AppImage, and tar.gz installers ship (the alpha-0.4.1 release of 2026-10-19 carried the set on GitHub, and the install docs list all five), so Status, Cautions, and the Bottom line no longer call Linux build-from-source only.
- 2026-11-08 - Folded the vendor sibling Atlas CLI (tryatlas/cli, Apache-2.0, headless session capture and shared memory for the agents you already run) into What it is as prose per the vendor-sibling ruling; no separate note.
- 2026-11-08 - Re-verified in rotation: every cited URL re-fetched; stack description moved to Tauri v2 with a React 19 TypeScript frontend over a Rust backend (GitHub's top language is now TypeScript), the Remote Runs tier fact moved to Team and Business with a price-history row at unchanged prices, and no HN or third-party coverage found.
- 2026-11-08 - Recorded the chat layer's session-to-worktree binding (a session starts in and stays bound to a project worktree, each worktree acting on its own branch) from the product chat docs, and the feature matrix's Atlas worktree-isolation cell moved with it.

## See also

- [Conductor](../conductor/index.md) - the established macOS parallel-agent app Atlas competes with
- [cmux](../cmux/index.md) - the terminal-first alternative for running agents side by side
- [Orca](../orca/index.md) - the broader agent development environment peer
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/tryatlas/atlas - GitHub API (200): 362 forks, Apache-2.0, TypeScript top language, pushed 2026-11-08, created 2026-05-14 (as of 2026-11-08)
- https://api.github.com/repos/tryatlas/atlas/releases/latest - releases API (200): alpha-0.4.1-org-agent, published 2026-11-03, macOS and Windows assets, body empty
- https://api.github.com/repos/tryatlas/atlas/releases/tags/alpha-0.4.1 - releases API (200): the Linux assets (.deb, .rpm, AppImage, Arch package, tar.gz), published 2026-10-19
- https://raw.githubusercontent.com/tryatlas/atlas/main/README.md - README (200): checkpoints, side-by-side agents, shared memory, team timeline and remote control, per-platform downloads, Atlas CLI, build requirements
- https://raw.githubusercontent.com/tryatlas/atlas/main/docs/architecture.md - architecture doc (200): Tauri v2, React 19 TypeScript frontend over a Rust backend, storage layout
- https://docs.tryatlas.cc/docs/getting-started/install - install docs (200): per-platform downloads, Linux packages install `atl` and `tryatlas`, WebKitGTK 4.1 requirement, Linux updates notify only
- https://www.tryatlas.cc - official website, live (200): the four-tier pricing table with Remote Runs on Team and Business
- https://docs.tryatlas.cc/docs/product/explorer - official documentation, live (200)
- https://docs.tryatlas.cc/docs/product/chat - official documentation, sessions, comments, and the session-to-worktree binding, live (200)
- https://github.com/tryatlas/cli - the vendor sibling CLI's repository: Apache-2.0, 3 stars (as of 2026-11-08), macOS and Linux
- https://hn.algolia.com/api/v1/search?query=tryatlas&tags=story - HN search (200): no story about this product, only an unrelated 2020 tryatlas.co Ghost host
