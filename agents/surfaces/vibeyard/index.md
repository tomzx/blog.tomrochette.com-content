---
title: Vibeyard
created: 2026-10-10
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, ai-editors, session-management, open-source]
readability: 3
audience_notes: >
  Engineers running Claude Code, Codex CLI, or Gemini CLI who want one desktop to run, watch, and pay for the sessions,
  and anyone comparing the session-cockpit class of surfaces.
  Assumes you know what a PTY and a session resume flag are.
---

Vibeyard is an MIT-licensed open-source desktop IDE (Electron) built around agent CLIs rather than an editor: it wraps Claude Code, OpenAI Codex CLI, and Gemini CLI in managed sessions, adds a kanban board that spawns and closes those sessions, and tracks cost, tokens, and context per session in a live inspector.

**Vibeyard's bet is that the cockpit, not the editor, is the product: the CLIs keep doing the work, and the surface owns everything above them, sessions, tasks, costs, and sharing.**

## What it is

An Electron and TypeScript desktop app where each agent session runs in its own PTY, with a drag-and-drop project dashboard (AI Readiness, Kanban, Team, Sessions, Provider Tools, live GitHub PRs and Issues widgets), a swarm-mode grid of every session at once, and a keyboard-first shortcut layer.
The kanban loop is the differentiator: a card spawns or resumes a CLI session in one click, and tasks auto-move to Done when their session completes, so the board tracks what the agents actually finished.
Multiple Claude profiles run side by side (work and personal licenses), each session backed by its own isolated config directory so credentials, settings, and history never mix.
Cost, token, and context-window tracking run per session, the inspector (Cmd+Shift+I) adds a timeline, cost breakdown, and tool-usage stats, and smart alerts flag missing tools, context bloat, and session health issues.
Sessions share over encrypted peer-to-peer WebRTC with PIN authentication, read-only or read-write, no server in between, and an embedded browser tab can feed an element's selector, text, and URL to the agent as edit context.
An opt-in tab-control server rounds the loop out: with "Allow tabs to control tabs" on, every agent tab gets `$VIBEYARD_CTL` and a per-tab token, so an agent running inside Vibeyard can spawn, rename, close, and list tabs, with the README stating plainly that the token is not a security boundary since every process the tab starts inherits it.
It is an independent one-maintainer project by elirantutia, distributed through signed and notarized macOS builds, Windows installers, Linux packages, and an npm one-liner, and the README states it is not affiliated with or endorsed by Anthropic.

## Status

Quiet, then stirring: 1,387 stars and 173 forks as of 2026-10-16, created 2026-03-19, released v0.3.4 (2026-07-22) through v0.3.8 (2026-09-03), and the release train sat still for ten weeks until it resumed on 2026-11-13 with v0.3.9 (no written notes) and v0.3.10 (whose notes say "No user-facing changes; this release only fixes the release pipeline"), the first releases after the repository woke on 2026-11-01 with the vibeyard-ctl tab-control feature, now documented in the README as an opt-in agent-drives-the-app mechanism.
The only public launch trace is a self-submitted Show HN thread from 2026-04-23 that drew 2 points and zero comments (re-checked 2026-11-14, still the only thread), and no third-party coverage surfaced in this run's search.
MIT throughout.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=elirantutia/vibeyard&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=elirantutia/vibeyard&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=elirantutia/vibeyard&type=date&legend=top-left" />
</picture>

## Strengths

- **The kanban-to-session loop is unique in this category: the board spawns the work and closes the card off the session's own completion, so task state is derived from agent behavior rather than maintained by hand.**
- Multiple isolated Claude profiles make running a work and a personal license side by side safe, which no other member documents.
- WebRTC session sharing with PIN auth is the only live share path in the category that needs no server.
- Cost, token, and context tracking per session plus the inspector put spend and window pressure next to the terminal.
- Signed and notarized desktop builds plus an npm one-liner keep install friction low.

## Cautions

- **The train resumed but its notes did not: the first releases in ten weeks (v0.3.9 and v0.3.10, November 13) carry no user-facing notes, one maintainer, no community, and no stated roadmap, so you cannot tell from a release what changed and vibeyard-ctl's arrival is visible only in the README.**
- vibeyard-ctl is opt-in and, per the README's own words, its per-tab token "is not a security boundary", since every process the tab starts inherits it; agents you run can drive the app.
- The community footprint is nearly empty, so nothing independent has exercised the feature claims (the P2P share path and profile isolation especially).
- It wraps three CLIs and inherits whatever they change; the README itself says more providers are "coming soon", unshipped as of 2026-10-10.
- MCP and AGENTS.md support are not documented anywhere, so rules and tool servers stay managed inside the CLIs.
- No cloud, scheduled, or mobile story: sessions are local, and sharing ends at the WebRTC session.

## Pricing

Free and open source under MIT; no paid tier exists.

## Compared to

- [OpenChamber](../openchamber/index.md): the incumbent session cockpit, with multi-model fusion and cron that Vibeyard lacks; Vibeyard answers back with the task board and the share path.
- [Cate](../cate/index.md): the canvas-shaped cockpit; Cate organizes worktrees in space, Vibeyard organizes sessions in a board.
- [Whiteboard](../whiteboard/index.md): the review surface where finished agents draw their work; Vibeyard supervises the run itself instead.

## Bottom line

**Recommended for engineers running Claude Code, Codex CLI, or Gemini CLI who want a task board and a cost view above their terminals, and who accept a single-maintainer app whose November releases resumed with unexplained notes.**
Not for anyone who needs a cockpit whose release notes explain what shipped (OpenChamber's train is moving and its notes do), MCP or rules management in the surface, or any cloud and mobile reach.

## Changes

- 2026-10-10 - Created from the category entrant scan, admitted on its differentiated kanban-to-session and share mechanisms with the quiet-window caution recorded.
- 2026-10-20 - Rotation re-verification, all cited URLs re-fetched live: the quiet stands (repository pushed 2026-09-03, release train still ending at v0.3.8, the README's coming-soon providers still unshipped, and the Show HN thread still the only footprint at 2 points and 0 comments); the quiet window reads seven weeks.
- 2026-10-31 - Rotation re-verification, all cited URLs re-fetched live: the quiet stands (repository still pushed 2026-09-03 and not archived, the release train still ending at v0.3.8, the README unchanged with the coming-soon providers still unshipped, and the HN search still returning the one 2-point Show HN); the quiet window reads about eight weeks.
- 2026-11-03 - Volatile re-verification on the pushed signal, all cited URLs re-fetched live: the quiet broke on the code side, the repository pushed 2026-11-01 with the unreleased vibeyard-ctl external agent-control feature (pull request #169 closing issue #168), while the release train still ends at v0.3.8 (2026-09-03) and the README still lists the coming-soon providers; the status, cautions, and bottom line rewritten around the quiet train and the unshipped work.
- 2026-11-13 - Rotation re-verification, all cited URLs re-fetched live: the quiet stands, the repository still pushed 2026-11-01 and not archived with no release after v0.3.8 (2026-09-03, about ten weeks), the README unchanged with the coming-soon providers still unshipped and vibeyard-ctl still unreleased, and the HN search still returning the one 2-point Show HN.
- 2026-11-14 - Volatile re-verification on the released signal (full note re-verified the same run), all cited URLs re-fetched live: the ten-week quiet broke on 2026-11-13 with v0.3.9 (no written notes) and v0.3.10 (a release-pipeline fix only, per its notes) as the new latest releases, the README now documents vibeyard-ctl as an opt-in tab-control server for agents with the not-a-security-boundary token caveat and shows Windows installers beside the macOS and Linux builds, while the coming-soon providers remain unshipped and the HN footprint still reads one 2-point Show HN; the status, cautions, and bottom line rewritten around the resumed-but-unexplained train.

## See also

- [OpenChamber](../openchamber/index.md) - the session cockpit incumbent this note joins as a challenger
- [Cate](../cate/index.md) - the canvas neighbor solving the same supervision problem spatially
- [Whiteboard](../whiteboard/index.md) - the review-side canvas that complements the run-side cockpit
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/elirantutia/vibeyard - 1,387 stars, 173 forks, MIT license, created 2026-03-19, pushed 2026-09-03, as of 2026-10-16 (stars and forks), re-fetched 2026-10-20 (still pushed 2026-09-03, not archived), re-fetched 2026-11-14 (pushed 2026-11-13, not archived)
- https://raw.githubusercontent.com/elirantutia/vibeyard/main/README.md - the feature set (kanban-to-session loop, swarm grid, isolated Claude profiles, WebRTC sharing, inspector, embedded browser), install paths, and the not-affiliated notice; re-fetched 2026-11-14 with the vibeyard-ctl tab-control section, its not-a-security-boundary token caveat, and Windows installers added
- https://api.github.com/repos/elirantutia/vibeyard/releases - the v0.3.4 (2026-07-22) through v0.3.8 (2026-09-03) release train, re-fetched 2026-11-14 with v0.3.9 (2026-11-13, no written notes) and v0.3.10 (2026-11-13, "No user-facing changes; this release only fixes the release pipeline") above it
- https://hn.algolia.com/api/v1/search?query=vibeyard&tags=story - the search that found exactly one relevant thread, re-fetched 2026-11-14 (still only the Show HN among the vineyard noise)
- https://hn.algolia.com/api/v1/items/47872787 - the self-submitted Show HN thread (2 points, 0 comments, 2026-04-23), the empty-footprint evidence, re-fetched 2026-11-14
