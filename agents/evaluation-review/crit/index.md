---
title: Crit
created: 2026-10-12
updated: 2026-10-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, code-review, human-in-the-loop, open-source]
readability: 3
audience_notes: >
  Engineers who review coding-agent output in a browser and want their comments to reach the agent without copy-paste, including review of the running app the agent is building.
  Assumes you know what a git diff and a pull request review are.
---

Crit is a local-first browser review surface for coding-agent output: a single Go binary renders the agent's plans, branch diffs, running dev servers, and static HTML pages into reviewable pages, your line comments collect into a structured review file, and the agent reads that file on its next turn.

**Crit is the fourth human-review surface in this category and the first whose surface extends past the text the agent wrote to the app the agent is writing: you can pin a comment to a button in the running app, not only to the line that produced it.**

## What it is

An MIT tool from Tomasz Tomczyk, a solo staff engineer, distributed as one Go binary through Homebrew core, go install, Nix, and Windows releases, with an optional hosted sharing service (crit.md) and a self-hostable server (crit-web).
Five review modes: plans and docs render markdown with per-line comments, code mode auto-detects git, jj, or sapling changes into syntax-highlighted diffs with a round-to-round view, story mode adds an LLM-authored chaptered overview of a branch, PR, or range, live mode proxies a running dev server behind a comment layer you can pin to DOM elements, and preview mode renders static HTML in an iframe.
The protocol is a file: reviews live under ~/.crit/reviews/ isolated per branch, and any agent that can read a file and run a command can consume them, which `crit install` wires for fourteen named agents (Claude Code, Cursor, GitHub Copilot, Codex, OpenCode, Gemini, Qwen, Hermes, Pi, Grok, Amp, Windsurf, Cline, and Aider), with OMO and omp listed in the README besides.
Beyond the local loop it syncs both ways with GitHub PRs and GitLab MRs (pull replies and discussion state, push comments and approve or request-changes outcomes), supports experimental send-to-agent live threads through a global-only agent_cmd, and shares reviews as public or organization-scoped URLs.

## Status

Active and steadily growing: 1,209 stars, 97 forks, and 15 open issues as of 2026-10-13, created 2026-02-16, pushed 2026-10-12, with v0.22.0 released 2026-10-07 and the author claiming a weekly release cadence.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=tomasz-tomczyk/crit&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=tomasz-tomczyk/crit&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=tomasz-tomczyk/crit&type=date&theme=dark&legend=top-left" />
</picture>

The growth happened without a launch thread: a Hacker News search finds no dedicated Show HN for crit, only the author's comments in Ask HN threads (April and May 2026), a Homebrew core acceptance he announced in May 2026, and testimonials on the product site.

## Strengths

- The five modes cover the whole agent output range, and live mode is the only surface in this category that reviews the running app itself.
- The file protocol keeps it agent-agnostic: no API, no SDK, and the fourteen installers are the widest browser-surface coverage here.
- Two-way forge sync means crit comments can be pushed into GitHub PRs and GitLab MRs as ordinary review comments, approve and request-changes included, instead of living in a parallel silo.
- Local-first discipline: loopback binding, zero telemetry, one version-check request, and a global-only trust boundary for the agent-executing agent_cmd.

## Cautions

- Story mode is model spend on your own key, about $1 to $1.40 per complex PR on Claude Opus 5 by the project's own estimate, and it is an explainer, not a verdict.
- The author's own HN comment (2026-09-26) says he now uses crit less for plans because models increasingly get it on the first pass, and he wonders whether the review space is shrinking; the tool's plan-review core is aimed at a practice its own author sees fading.
- Solo maintainer, pre-1.0, weekly releases: config keys, share behavior, and installer paths should be expected to move.
- Sharing uploads to crit.md by default with a GitHub OAuth account; staying fully local means never clicking Share, or self-hosting crit-web.

## Pricing

Free and MIT, with no paid tier recorded as of 2026-10-12.
The costs are your own model tokens in story mode and, if you use them, the hosted crit.md share service, which publishes no prices in the fetched material.

## Compared to

- [Plannotator](../plannotator/index.md): the closest sibling, also a browser review surface feeding the agent; Plannotator intercepts plans through harness hooks across nine agents and diffs plan revisions, while crit is invoked explicitly and adds running apps, story chapters, and forge two-way sync.
- [Hunk](../hunk/index.md): the terminal answer to the same problem; choose Hunk when the loop never leaves the terminal, crit when line-precise comments on long plans and live pages pay for the browser context switch.
- [PR Lens](../pr-lens/index.md): both add an LLM-authored comprehension layer (story chapters versus animated diagrams), but PR Lens renders a verdict-free walkthrough on the pull request while crit keeps review anchored to your local lines and comments.

## Bottom line

**Recommended for engineers whose agent loop produces plans, diffs, and running apps and who want one local browser surface to push all three back to the agent.**
Not for terminal-only workflows (Hunk), not for CI gating (nothing here exits nonzero on failure), and not for anyone needing a team layer today, since the sharing service is early and unpriced.

## Changes

- 2026-10-12 - Created from the entrant resolution pass, admitted as the fourth human-review surface next to Plannotator, Hunk, and PR Lens, with the author's plan-mode skepticism recorded as the critical angle.

## See also

- [Plannotator](../plannotator/index.md) - the hook-intercepting sibling with nine-harness coverage
- [Hunk](../hunk/index.md) - the terminal diff stream for the same loop
- [PR Lens](../pr-lens/index.md) - the verdict-free PR walkthrough with diagrams
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/tomasz-tomczyk/crit - repository: license, stars, forks, and dates as of 2026-10-12
- https://raw.githubusercontent.com/tomasz-tomczyk/crit/main/README.md - the five modes, integrations, forge sync, agent_cmd trust boundary, and the story-mode cost estimate
- https://api.github.com/repos/tomasz-tomczyk/crit - stars, forks, issues, creation and push dates as of 2026-10-12
- https://api.github.com/repos/tomasz-tomczyk/crit/releases - v0.22.0 published 2026-10-07
- https://crit.md - the five-mode product surface, founder context, the weekly-release claim, and crit-web self-hosting
- https://hn.algolia.com/api/v1/search?query=crit.md&hitsPerPage=5 - the footprint scan: no dedicated thread, the author's Ask HN comments, and the 2026-09-26 plan-mode skepticism
