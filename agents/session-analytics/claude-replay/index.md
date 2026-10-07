---
title: claude-replay
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, replay, shareable-artifacts]
readability: 3
audience_notes: >
  Engineers who need to show someone else what an agent session actually did, and anyone comparing session-analytics mechanisms.
  Assumes you know where coding agents store their session transcripts.
---

claude-replay is the MIT CLI that converts coding-agent session transcripts from seven harnesses into one self-contained interactive HTML replay, playable with speed control, diff views, and chapter navigation, and shareable as a single file with zero external dependencies.

**claude-replay fills the share slot this category left open: every other member indexes, audits, or dashboards sessions for the person who ran them, while claude-replay compiles a session into an artifact you can email, host, or embed, which is a different output for a different reader.**

## What it is

A zero-dependency Node CLI (npm install -g claude-replay) by es617, MIT licensed, not affiliated with Anthropic (843 stars, pushed 2026-09-18, as of 2026-10-07).
It auto-detects and reads Claude Code, Cursor, Codex CLI, Gemini CLI, OpenCode, Kimi Code, and Hermes Agent transcripts from their on-disk locations, including OpenCode's export path and Hermes's SQLite store read live.
The output is a single HTML file with an interactive player (playback speed, keyboard shortcuts, diff views, chapters), collapsible tool-call and thinking blocks, six themes with full CSS override, and automatic redaction of API keys and tokens.
A built-in web editor lets you exclude turns, add bookmarks, and edit prompts before export, `--serve --watch` follows a session as it runs, and a Docker mode mounts sessions read-only for sandboxed conversion; a browser version converts uploaded files entirely client-side.

## Status

Active with a quiet recent month: created 2026-03-02, 843 stars, 66 forks, last push 2026-09-18, as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=es617/claude-replay&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=es617/claude-replay&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=es617/claude-replay&type=date&legend=top-left" />
</picture>

The project carries an explicit endorsement listing in the awesome-claude-code directory, which calls the output "fantastic".
Its own traction numbers are modest: about 400 npm downloads in the week to 2026-10-04 and no Hacker News thread of its own, so adoption evidence is the star curve and the directory listing, not download volume.

## Strengths

- The only output in the category built to be shared: one dependency-free HTML file that survives email, static hosting, and blog embeds.
- Seven-harness coverage with format auto-detection, including the awkward cases (OpenCode export, Hermes SQLite).
- Privacy handled at the artifact layer: automatic secret redaction plus fully local conversion, so the replay is safe to publish.
- The live `--serve --watch` mode doubles it as a minimal observation dashboard when a replay is not the goal.

## Cautions

- Smaller scale than the category's spend-auditors and indexers, with modest npm adoption and a one-maintainer bus factor.
- The conversion targets the harnesses' current log formats, and every format change breaks it until patched; the seven-harness list needs re-verification each harness release.
- Replays are for humans: nothing here feeds analytics, cost audits, or search back into your workflow.
- Development paused for the month to 2026-09-18, worth watching before depending on it.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.

## Compared to

- [Memex](../memex/index.md): the indexer that resumes the session you find; claude-replay packages the session you want to show someone else.
- [claude-devtools](../claude-devtools/index.md): the local DevTools for inspecting Claude Code sessions turn by turn; choose it for analysis, claude-replay for publishing.
- [agentsview](../agentsview/index.md): the retrospective search index across dozens of agents; claude-replay covers fewer harnesses but produces an artifact instead of a database row.

## Bottom line

**Recommended for anyone who publishes postmortems, tutorials, or evidence of agent behavior, and for teams that need a session reviewed by someone without tooling installed.**
Not for cost auditing, search, or analytics, and not for teams needing many active maintainers behind a dependency.

## Changes

- 2026-10-07 - Created.

## See also

- [Memex](../memex/index.md) - the resume-in-place counterpart in this category
- [claude-devtools](../claude-devtools/index.md) - the inspection-first Claude Code tool this complements
- [agentsview](../agentsview/index.md) - the broadest retrospective index, built for analytics where this is built for the artifact
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/es617/claude-replay - repository, MIT license, the seven-harness table with transcript locations, and the feature list (fetched 200, 2026-10-07)
- https://api.github.com/repos/es617/claude-replay - stars, forks, created date, and push date for the as-of status (fetched 200, 2026-10-07)
- https://es617.dev/claude-replay/ - the web conversion surface, themes, export options, redaction, and Docker mode (fetched 200, 2026-10-07)
- https://api.npmjs.org/downloads/point/last-week/claude-replay - weekly download volume for the adoption claim (fetched 200, 2026-10-07)
- https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/README.md - the directory endorsement grounding the community-recognition claim (fetched 200, 2026-10-07)
