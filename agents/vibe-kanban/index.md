---
title: Vibe Kanban
created: 2026-08-24
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, orchestration, kanban, git-worktrees, open-source]
readability: 3
audience_notes: >
  Engineers evaluating a kanban-style front end for parallel coding agents, or anyone studying which parts of this category survive their vendor.
  Assumes you already run a CLI agent and know what a git worktree is.

---

Vibe Kanban is an Apache-2.0 kanban board for managing parallel coding agents in isolated workspaces, launched by Bloop AI in June 2025; the company shut down in April 2026 and the project continues community-maintained.
Facts below verified as of 2026-09-03.

**It is the category's most-adopted artifact and its clearest cautionary tale at once: about 28k GitHub stars, thousands of daily users, and no business model survived it.**

## What it is

A Rust backend with a web UI that you start with `npx vibe-kanban`; the last published version is 0.1.44.
The workflow is plan on a kanban board, dispatch a card to a workspace (a git worktree with its own branch, terminal, and dev server), then review diffs with inline comments, preview the app in a built-in browser, and open a PR.
It supports 10+ agents including Claude Code, Codex, Gemini CLI, Copilot, Amp, Cursor, OpenCode, Droid, CCR, Qwen Code, and Aider.
Self-hosting via Docker was documented for teams.

## Status

Company dead, project alive.
Bloop shut down on 2026-04-10, with CEO Louis Knight-Webb writing that "the vast majority are free users and we couldn't find a business model".
Remote services (kanban issues, comments, projects, organisations) were removed 30 days after the announcement; refunds were issued and subscriptions terminated.
**Local workspaces keep working, but "community-maintained" is still a promise rather than activity: as of 2026-09-03 the repo still shows no push since 2026-04-24 and no release beyond 0.1.44, while open issues climbed from 383 (2026-08-24) to 539.**

## Strengths

- Planning-first UX: the backlog feeds agent tasks directly, which matches how parallel work actually gets sequenced.
- Widest adoption in the category, which means the most community knowledge to fall back on.
- Fully local after the sunset: worktree execution never depended on the company's servers.
- The shutdown was handled unusually well, with data export, refunds, and a written post-mortem.

## Cautions

- Nobody is paid to fix your bug anymore, and nearly five months after the shutdown no community release has shipped either; the community roadmap was still pending when I checked.
- At launch, telemetry defaulted to on and collected emails and GitHub usernames, switched to opt-in only after HN criticism (the fix shipped within hours, but the default tells you about the growth incentives).
- The team features (shared issues, orgs) are exactly the part that died, which is the part companies would pay for.
- GitHub integration historically asked for broad permissions, a recurring complaint across this whole category.

## Pricing

Free and open source (Apache-2.0).
Cloud subscriptions existed before the shutdown and were terminated with refunds.

## Compared to

- [Conductor](../conductor/index.md) and Emdash: funded, actively developed dashboards; choose them when you want a vendor.
- [Claude Squad](../claude-squad/index.md) and [dmux](../dmux/index.md): terminal equivalents with far less surface to maintain.
- [OpenChamber](../openchamber/index.md): a different axis of the same idea, scheduling agent sessions rather than parallelizing them interactively.

## Bottom line

**Recommended as a free, local kanban for individual parallel-agent workflows, especially now that it is pure infrastructure with no vendor to churn under you.**
Not for teams who need accountability, because there is no vendor left.
My disagreeable claim: bloop's failure is evidence that this orchestration layer wants to be free infrastructure rather than SaaS margin, and I expect at least one more funded competitor to learn the same lesson.

## See also

- [Conductor](../conductor/index.md) - the funded GUI counterpart whose fate will test that claim
- [Claude Squad](../claude-squad/index.md) - the minimal terminal version of parallel dispatch
- [dmux](../dmux/index.md) - the terminal-native worktree multiplexer
- [OpenChamber](../openchamber/index.md) - scheduled agent sessions, the non-interactive complement

## References

- https://github.com/BloopAI/vibe-kanban - README, sunset banner, feature list, star count
- https://www.vibekanban.com/blog/shutdown - shutdown announcement, service removal details, refunds
- https://www.vibekanban.com/ - product overview, 30,000 active users claim, sunset banner
- https://news.ycombinator.com/item?id=44533004 - launch thread with the telemetry and permissions critique
- https://registry.npmjs.org/vibe-kanban/latest - version 0.1.44 metadata and maintainers
