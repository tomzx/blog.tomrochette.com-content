---
title: Crystal
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, orchestration, git-worktrees, desktop-app]
readability: 3
audience_notes: >
  Engineers tracking the consolidation of worktree-manager tools, or evaluating Nimbalyst as a successor product.
  Assumes familiarity with running Claude Code or Codex sessions locally.

---

Crystal was an MIT-licensed desktop app from Stravu for running multiple Claude Code and Codex sessions in parallel git worktrees; it was deprecated in February 2026 and replaced by Nimbalyst, a broader visual workspace from the same team.
Facts below verified as of 2026-09-02.

**Its pivot is the clearest signal in this category that a pure worktree-session manager is a feature, not a standalone product.**

## What it is

An Electron desktop app (macOS first, Linux later) where each agent session got its own worktree, with built-in git operations (rebase, squash, diff viewer) and the ability to build and run the application inside its worktree.
The author pitched it as the first "IVE (Integrated Vibe Environment)" rather than an IDE.
**On deprecation, the README now points all users to Nimbalyst, which keeps worktree isolation but adds visual editors for markdown, mockups, diagrams, spreadsheets, and data models, a session kanban, and an iOS companion app.**
Nimbalyst's desktop and iOS apps are MIT-licensed and free for individuals.

## Status

Dead, superseded by design.
The repository README says "Deprecated: February 2026", and the last push landed 2026-02-26, which matches.
As of 2026-09-02 the repo shows 3,114 stars, 197 forks, and 672 commits, with 68 open issues that will not be worked on.
Nimbalyst itself is actively marketed, with team collaboration in beta and SOC-2 positioning on its site.

## Strengths

- While alive, it did one thing well and got praised for it in competitor launch threads, including Conductor's.
- Worked with existing local checkouts instead of requiring fresh clones through GitHub OAuth.
- The successor inherits the same worktree-isolation core, so the migration path is real rather than rhetorical.
- Full history remains open source for anyone who wants to fork the simpler product.

## Cautions

- The tool you can download today is unmaintained; treat any new install as a fork-first decision.
- Nimbalyst is a much broader bet (editors, teams, mobile) from a small team, and pivots this wide often thin out execution.
- Monetization for Nimbalyst rests on teams and enterprise tiers that are still forming.
- The category context matters: Conductor stayed a session manager and raised money, so the "feature not product" thesis is contested, not settled.

## Pricing

Crystal was free and MIT.
Nimbalyst is free for individuals with MIT-licensed desktop and iOS apps, and sells teams and enterprise tiers.

## Compared to

- [Conductor](../conductor/index.md): the counterexample, a funded pure session manager that kept shipping.
- [Claude Squad](../claude-squad/index.md): the terminal equivalent, still maintained, same minimal scope Crystal abandoned.
- [dmux](../dmux/index.md): a newer terminal tool betting the minimal scope still works.

## Bottom line

**Recommended only as a case study, not as a tool to adopt; if the idea appeals, evaluate Nimbalyst on its own merits.**
My disagreeable claim: Stravu read the market correctly, because harness CLIs were going to commoditize session multiplexing, and pivoting early beat competing head-on with Conductor's $22M.

## See also

- [Conductor](../conductor/index.md) - the funded counterexample that stayed a session manager
- [Vibe Kanban](../vibe-kanban/index.md) - the other 2026 exit in this category, a shutdown instead of a pivot
- [Claude Squad](../claude-squad/index.md) - the still-active minimal terminal alternative
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map showing where this layer sits

## References

- https://github.com/stravu/crystal - deprecation notice, migration links, feature history
- https://api.github.com/repos/stravu/crystal - last push 2026-02-26, stars, MIT license
- https://nimbalyst.com/ - successor product, licensing, feature set
- https://news.ycombinator.com/item?id=44259353 - author's June 2025 launch thread
- https://news.ycombinator.com/item?id=44594584 - Conductor thread where users recommended Crystal
