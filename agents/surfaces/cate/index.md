---
title: Cate
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, ai-editors, open-source, canvas]
readability: 3
audience_notes: >
  Engineers running several agent CLIs in parallel who want one spatial surface to supervise them.
  Assumes you know what a worktree and an agent CLI are.
---

Cate is an MIT-licensed open-source desktop workspace (Electron) that lays editors, terminals, browsers, and agent chats on one infinite canvas, with each terminal reporting whether its agent is working, finished, or waiting on you.

**Cate's bet is that parallel agents need spatial memory, not more tabs: one canvas per project, one colored territory per worktree, and a notification the moment any agent blocks on you.**

## What it is

**A canvas-shaped cockpit, not an editor with AI bolted on**: panels (Monaco editors, terminals, browsers, PDF and image viewers, nested canvases) float, dock, or detach into their own windows, and the layout persists per project.
Agent chats run through an embedded T3 Code integration (Codex, Claude Code, Cursor, Grok, OpenCode, and Antigravity in one chat panel), while plain terminals gain agent-awareness from the CLIs' own hook events: turn start, turn end, and permission prompts become running, waiting, or finished states with notifications.
One click spins up a git worktree on its own branch, off a local branch, a remote branch, or an open PR, drawn as a colored territory on the canvas, and sessions survive restarts, reattaching each agent with its resume command.
The `cate` CLI closes the loop by letting an agent drive the app back: open a browser panel, read another terminal, manage panels.
SSH and WSL targets run terminals, git, and search remotely while the canvas, editors, and browser stay local.
It is built by the 0-AI-UG organization, with the v1.0 launch shared on Hacker News under the BlueBerry2001 handle.

## Status

**Active and young: a six-month-old project with a steady release train.**
The repository was created 2026-03-29, and v1.0 landed May 25, 2026 behind a 65-point Show HN thread (66 comments), preceded by a smaller spatial-workspace thread in May.
The v2 line carries it now: v2.0.5 (2026-09-30, T3 Connect startup fixes in packaged builds, false agent-ready notification fixes during automatic approval, a hooks-settings rework) is the latest release after v2.0.4 and v2.0.3 in the two weeks before it, and the repository was pushed 2026-10-07.
About 2.2k stars (2,174) and 141 forks as of 2026-10-08.
Installs go through prebuilt DMG, NSIS, AppImage, DEB, and tar archives plus a Homebrew cask, and the README tells daily users not to build from source.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=0-AI-UG/cate&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=0-AI-UG/cate&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=0-AI-UG/cate&type=date&legend=top-left" />
</picture>

## Strengths

- **The agent-state feedback loop is the differentiator**: every terminal shows running, waiting, or finished, and Cate pings you when an agent blocks, which is the parallel-agent supervision problem in its rawest form.
- Worktrees drawn as colored canvas territories keep five parallel branches five visibly separate workstreams instead of a pile of tabs.
- Free and MIT and local-first, and SSH or WSL gives a remote machine the same path.
- The `cate` CLI makes the workspace itself scriptable by the agents it hosts.

## Cautions

- **The launch thread's sharpest question is still open: what does an infinite canvas solve that a window manager does not?** The project answers "Cate is not a window manager replacement", but commenters kept reading the feature list as window management anyway.
- The same thread's canvas skeptics predicted cognitive overload: no intuition for where things are, no expiry for abandoned panels, and every canvas becoming a mess with age.
- Electron, admitted in the thread, against competition that sells native performance.
- The agent chats are a T3 Code integration, so that surface inherits another project's scope and pace, and the product homepage is a client-rendered shell that grounds nothing by itself.
- Commenters reached for the abandoned Haystack Editor as the prior art this canvas-idea already buried once.

## Pricing

Free and open source under MIT; no paid tier exists.

## Compared to

- [Whiteboard](../whiteboard/index.md): the other canvas entrant, but for review, a surface where a finished agent draws its work for humans; Cate is the workspace where the work happens.
- [OpenChamber](../openchamber/index.md): the session cockpit with the same supervision goal, who is blocked and what finished; OpenChamber organizes sessions in a list, Cate organizes them in space.
- [Zed](../zed/index.md): the native-performance editor bet; Cate is the opposite trade, Electron flexibility spent on spatial layout.

## Bottom line

**Recommended for engineers running three or more agent CLIs who think in spatial layouts and accept a young Electron app.**
Not for keyboard-first minimalists, and not for anyone whose window manager already answers the question Cate raises.

## Changes

- 2026-10-08 - Created from the awesome-list entrant scan (surfaced by ai-for-developers/awesome-ai-coding-tools), with the 65-point v1.0 thread as the critical source.

## See also

- [Whiteboard](../whiteboard/index.md) - the review-side canvas that complements Cate's workspace-side one
- [OpenChamber](../openchamber/index.md) - the list-shaped answer to the same parallel-agent supervision problem
- [T3 Code](../../orchestration/t3code/index.md) - the six-harness control surface embedded as Cate's chat panel
- [Zed](../zed/index.md) - the native-performance editor contrast

## References

- https://github.com/0-AI-UG/cate - repository and README (T3 Code chats, agent-aware terminals, worktree territories, the cate CLI, SSH and WSL), MIT license, 2,174 stars and 141 forks as of 2026-10-08
- https://github.com/0-AI-UG/cate/releases - v2.0.5 (2026-09-30) as the latest release on the v2 train, after v2.0.4 and v2.0.3
- https://cate.cero-ai.com - the product homepage, a client-rendered shell this run (title only, no server-rendered content)
- https://news.ycombinator.com/item?id=48265470 - the 65-point v1.0 Show HN thread (66 comments): the window-manager, cognitive-overload, Electron, and Haystack-editor critiques
- https://hn.algolia.com/api/v1/items/48265470 - the thread text and comment tree, fetched via the Algolia items API
- https://github.com/ai-for-developers/awesome-ai-coding-tools - the awesome list that surfaced the candidate
