---
title: beads
created: 2026-08-27
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, task-management, issue-tracking, open-source, byok]
readability: 3
audience_notes: >
  Engineers whose coding agents lose the plan across sessions and want structured task state instead of markdown TODO files.
  Assumes you run at least one CLI agent and are comfortable with a database living inside your repo.
---

beads is Steve Yegge's distributed graph issue tracker for AI agents (`bd`): a Dolt-backed database of tasks with dependencies, atomic claims, and cross-machine sync, designed as persistent memory for coding agents.

**The dependency graph with atomic claims, not the markdown file, is the task interface agents actually need, and beads is the reference implementation of that claim even for people who end up choosing something simpler.**

## What it is

A Go CLI (brew or npm install) that replaces markdown plans with structured state: `bd ready` lists unblocked work, `bd update --claim` atomically takes a task, `bd close` finishes it and releases dependents.
Storage is [Dolt](https://github.com/dolthub/dolt), a version-controlled SQL database, embedded by default or against a server for multiple concurrent writers, with cross-machine sync through `bd dolt push` and `bd dolt pull` over a git remote.
Hash-based IDs (`bd-a1b2`) prevent merge collisions between agents, closed tasks get summarized by a memory-decay compaction step to save context, and `bd remember` stores project memory that `bd prime` re-injects.
`bd init` writes an AGENTS.md section and installs hooks for Claude Code, Codex, Factory Droid, Cursor, and others.
It lives in the gastownhall organization (renamed from steveyegge, the old name still redirects), MIT-licensed, with docs at [beads.gascity.com](https://beads.gascity.com/).

## Status

Active and moving fast.
As of 2026-10-31: 27,853 stars (as of 2026-10-14), 1,912 forks, 1,614 open issues, created 2025-10-12, pushed 2026-10-31, latest stable release v1.3.2 on 2026-10-24, a fix-only patch that closed the v1.3.2-rc.1 to rc.3 prerelease train of 2026-10-05, 2026-10-10, and 2026-10-23 after v1.3.1 of 2026-09-30, and 33,156 npm downloads over the trailing month to 2026-10-31.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=gastownhall/beads&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=gastownhall/beads&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=gastownhall/beads&type=date&legend=top-left" />
</picture>

The repository description now leads with the memory framing ("A memory upgrade for your coding agent") rather than "issue tracker", the positioning moving toward what the `bd remember` and memory-decay sentences below describe.
**There is no Show HN launch thread; adoption ran through Yegge's audience and the ecosystem instead, which is itself the community signal.**
That ecosystem is real: a community Rust port ([beads_rust](https://github.com/Dicklesworthstone/beads_rust), about 1.1k stars) froze the "classic" SQLite-plus-JSONL architecture, a [beads planner plugin](https://news.ycombinator.com/item?id=47263696) and web UIs exist, and the architecture has churned enough (SQLite to Dolt, schema migrations) that people built [drop-in replacements](https://news.ycombinator.com/item?id=46487580).

## Strengths

- `bd ready` plus atomic claims is the correct primitive for multiple agents sharing one queue without stomping each other.
- Dolt gives the task database cell-level merge, branching, and sync, which markdown files cannot have.
- Memory decay and `bd remember` attack context-window cost directly, the tax every long-running agent project pays.
- Works git-free (Sapling, Jujutsu, monorepos, CI) and stealth mode keeps it out of shared repos.

## Cautions

- The architecture churned twice in a year, and the beads_rust fork exists precisely because early adopters needed to freeze it.
- A SQL database inside your repo is a bigger bet than markdown files; schema-version guards and migration steps now exist for a reason.
- The simplicity camp defected publicly: the top replacement thread ("faster, simpler Markdown-based task tracker", 84 points) is the standing rebuttal.
- Roughly 1,500 open issues against a fast-moving core means the tracker itself gets triaged by attention, not process.

## Pricing

Free and open source under MIT.
No paid tier; optional Dolt remotes can use DoltHub's free tier.

## Compared to

- [Backlog.md](../backlog-md/index.md): markdown-native and human-first; choose it when git-diffable files matter more than atomic multi-agent claims.
- [Task Master](../task-master/index.md): PRD-to-tasks pipeline, now the engine of a commercial product; choose it when you want the vendor to run the method.
- A TODO.md in the repo: zero dependencies and agent-readable, which remains beads' hardest competitor at small scale.

## Bottom line

**Recommended for teams running several agents over long-horizon work where lost context is the measured cost.**
Not for solo-agent or small-project work, where a markdown file's simplicity wins, or for shops that will not accept a database in the repo.
The disagreeable claim I will defend: every markdown task file is a beads database with worse concurrency, and the file format's familiarity is doing more work than its engineering.

## Changes

- 2026-08-27 - Created in the Task management category seed, recording the gastownhall rename, the Dolt-backed architecture, and the missing Show HN launch thread.
- 2026-09-04 - Refreshed the status sentence, noting the v1.3.0-rc.1 prerelease.
- 2026-09-05 - Corrected the v1.3.0-rc.1 prerelease date to 2026-08-31.
- 2026-09-16 - Recorded v1.3.0 shipping stable on 2026-09-15 after the rc prereleases.
- 2026-09-21 - Recorded the v1.3.1-rc.1 prerelease (published 2026-09-21), the first release after v1.3.0 stable, and refreshed repository counts.
- 2026-09-27 - Refreshed counts (27,460 stars, 1,270 open issues, 23,924 npm downloads); v1.3.1-rc.1 still the newest release.
- 2026-10-02 - Recorded v1.3.1 shipping stable on 2026-09-30 after the rc prereleases and refreshed counts (27,574 stars, 1,266 open issues, 28,681 npm downloads last month).
- 2026-10-06 - Recorded the v1.3.2-rc.1 prerelease (2026-10-05), refreshed counts (27,658 stars, 1,373 open issues), and noted the repository description now leading with the memory framing.
- 2026-10-07 - Added the gastownhall/beads star history chart to the Status section.
- 2026-10-10 - Recorded the v1.3.2-rc.2 prerelease (2026-10-10) and refreshed counts (27,777 stars, 1,879 forks, 1,415 open issues, 33,707 npm downloads).
- 2026-10-17 - Rotation re-verification with every cited URL re-fetched live (repository, API, docs site, the Rust port, the replacement thread, npm); refreshed counts (1,487 open issues, 1,893 forks, pushed 2026-10-17), with v1.3.2-rc.2 still the newest tag after the v1.3.1 stable.
- 2026-10-23 - Recorded the v1.3.2-rc.3 prerelease (2026-10-23) and refreshed counts (1,900 forks, 1,513 open issues, pushed 2026-10-23).
- 2026-10-25 - Recorded v1.3.2 shipping stable on 2026-10-24 after the rc train (a fix-only patch release) and refreshed counts (1,519 open issues, pushed 2026-10-25, 32,270 npm downloads).
- 2026-10-28 - Refreshed counts (1,907 forks, 1,544 open issues, pushed 2026-10-28, 32,046 npm downloads over the trailing month to 2026-10-28); v1.3.2 still the newest release.
- 2026-10-31 - Refreshed counts (1,912 forks, 1,614 open issues, pushed 2026-10-31, 33,156 npm downloads over the trailing month to 2026-10-31); v1.3.2 still the newest release.

## See also

- [Gas Town](../../orchestration/gastown/index.md) - the orchestration system beads feeds, from the same org
- [Backlog.md](../backlog-md/index.md) - the markdown-native counterargument
- [Task Master](../task-master/index.md) - the productized alternative
- [AGENTS.md](../../protocols/agents-md/index.md) - the convention `bd init` writes into

## References

- https://github.com/gastownhall/beads - README: commands, Dolt modes, setup, git-free usage
- https://api.github.com/repos/gastownhall/beads - stars, forks, push dates, MIT license as of 2026-10-31
- https://beads.gascity.com/ - official documentation site
- https://github.com/Dicklesworthstone/beads_rust - the community Rust port freezing classic beads, and the Gas Town evolution note
- https://news.ycombinator.com/item?id=46487580 - the 84-point replacement thread, the critical source
- https://api.npmjs.org/downloads/point/2026-10-01:2026-10-31/@beads/bd - 33,156 downloads over the trailing month to 2026-10-31
