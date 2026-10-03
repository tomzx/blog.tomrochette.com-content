---
title: Squad
created: 2026-09-29
updated: 2026-10-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, coding-agents, copilot]
readability: 3
audience_notes: >
  Developers already working in GitHub Copilot CLI who want persistent multi-agent teamwork without hosting a new runtime.
  Assumes you know what agent roles and routing mean.
---

Squad is Brady Gaster's MIT-licensed CLI that assembles persistent, human-led AI agent teams, frontend, backend, tester, lead, as files inside your repository and runs them through GitHub Copilot CLI.

**Squad's bet is that the right multi-agent primitive for coding is a roster of teammate files versioned in the repo, not a framework import, and 3,249 stars in eight months suggest the bet lands.**

## What it is

A CLI (`npm install -g @bradygaster/squad-cli`) whose `squad init` creates a `.squad/` directory holding `team.md`, member files, charters, and routing rules; each member runs in its own context, reads only its own knowledge, and writes back what it learned so the work stays inspectable (README).
Sessions run inside GitHub Copilot CLI (`copilot --agent squad`), with GitHub authentication wired for issues, PRs, and a workflow the README calls Ralph; a `--preset default` flag gives a configured team instantly.
The repo sits at 3,249 stars with 502 forks, MIT, created 2026-02-06, TypeScript (GitHub API, as of 2026-10-02).
It entered this pile from the Awesome Multi-Agent Orchestrators directory's new entries.

## Status

Active: last push 2026-10-03, latest release v1.0.0 on 2026-10-03, which promoted the dev line to main (GitHub API, as of 2026-10-03).
The 1.0.0 wave caps the alpha period: the README no longer carries the alpha badge that earlier releases warned about, though the project is still a solo-maintainer CLI and the API caveats deserve re-reading before you script against it.
Traction is real but concentrated: npm recorded 7,684 downloads of `@bradygaster/squad-cli` in the month ending 2026-09-30.
Independent discussion is nearly absent: the largest HN thread I found has 2 points, so the footprint is GitHub plus npm alone, which is itself a signal.

## Strengths

- **Files-as-teammates is inspectable by design**: charters, routing rules, and member knowledge are versioned Markdown, so the multi-agent setup diffs and reviews like code.
- It rides GitHub Copilot CLI, so there is no new agent runtime to host, authenticate, or pay for separately beyond Copilot access.
- The human-led stance is explicit in the README: people keep accountability for priorities, approvals, and final changes.
- Fast iteration (v0.13.1 by month eight) and a one-flag preset lower the start cost to nearly nothing.

## Cautions

- Hard-locked to GitHub Copilot CLI; if you use Claude Code, Codex, or OpenCode, this tool is not for you.
- Alpha with documented breaking changes, so team files you build now may need migration later.
- **Community scrutiny is thin**: a 2-point HN thread and no third-party coverage I could find, so traction numbers rest on the maintainer's own channels.
- The teammate-files model is young and unproven at scale; it is a productivity experiment by a single known maintainer, not a supported product.

## Pricing

Free and open source under MIT; Squad itself has no paid tier.
It requires a GitHub Copilot subscription to run sessions, which is the real cost line.

## Compared to

- [MetaGPT](../metagpt/index.md): the role-company framework precedent; MetaGPT hard-codes a software company in Python, Squad keeps roles as editable repo files and runs on Copilot.
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md): the lead-plus-workers bash pattern; both keep a human lead in charge, but that one orchestrates raw Claude Code sessions while Squad structures teams as files.
- [LoopTroop](../looptroop/index.md): the local GUI orchestrator with council planning; LoopTroop is multi-model and GUI-first, Squad is Copilot-only and repo-first.

## Bottom line

Recommended for individual developers already living in GitHub Copilot CLI who want persistent, reviewable multi-agent teamwork with a human in charge.
Not for teams on other agent runtimes, or anyone who needs a stable, community-validated API today.

## Changes

- 2026-09-29 - Created when the new-entries list from the Awesome Multi-Agent Orchestrators directory resolved.
- 2026-10-03 - Status move: v1.0.0 published October 3 (dev line promoted to main), the README no longer badges the project alpha, and star count refreshed to 3,251.

## See also

- [MetaGPT](../metagpt/index.md) - the role-based software-company framework Squad echoes with files
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the lead-and-workers adversarial pattern
- [LoopTroop](../looptroop/index.md) - the GUI-first multi-model alternative
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/bradygaster/squad - GitHub API (200): 3,237 stars, 497 forks, MIT, TypeScript, pushed 2026-09-29, created 2026-02-06 (as of 2026-09-29)
- https://raw.githubusercontent.com/bradygaster/squad/main/README.md - README (200): squad init, .squad/team.md, preset, Copilot CLI usage, alpha warning, human-led stance
- https://registry.npmjs.org/@bradygaster%2Fsquad-cli - npm metadata for the package
- https://api.npmjs.org/downloads/point/last-month/@bradygaster/squad-cli - npm downloads API (200): 7,323 downloads, month ending 2026-09-27
- https://api.npmjs.org/downloads/point/last-week/@bradygaster/squad-cli - npm downloads API (200): 2,575 downloads, week ending 2026-09-27
- https://api.github.com/repos/bradygaster/squad/releases/latest - releases API (200): v0.13.1, published 2026-08-26
- https://hn.algolia.com/api/v1/items/47157294 - only substantive HN thread (200): 2 points, 2026-02-25 (critical source: near-absent independent discussion)
