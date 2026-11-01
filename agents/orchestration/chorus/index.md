---
title: Chorus
created: 2026-11-01
updated: 2026-11-01
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, kanban, human-in-the-loop]
readability: 3
audience_notes: >
  Engineers running several coding agents who want one pipeline where agents propose work and humans verify it before anything ships.
  Assumes you know what Claude Code or Codex are and what a task board does.
---

Chorus is an open-source team harness that takes a team of coding agents plus the humans around them into one pipeline where agents propose and humans verify.

**The bet is that multi-agent work fails without separated permissions and a verification stage, so Chorus makes the Idea, Proposal, Task pipeline its runtime instead of another terminal grid.**

## What it is

A self-hosted web app (TypeScript over Node, embedded PGlite by default, PostgreSQL 17 or Docker Compose for scale) that opens at localhost:8637, plus an npm CLI (`@chorus-aidlc/chorus`, 0.23.0).
Work follows the AI-DLC method: a human writes an idea, an agent drafts a proposal with a PRD and a task DAG, agents execute the tasks, and admin actors verify and close.
Every stage carries a permission matrix (five actions across three actor kinds, granted to humans, agents, or both), so the actor doing a task and the actor verifying it are different grants.
Remote daemons pick up assigned tasks on your machines and drive Claude Code, Codex, Pi, Kiro, Hermes Agent, and TRAE CLI through plugins and gateways; results and approval requests come back into the project.
By Chorus-AIDLC, repository created 2026-02-04, an implementation of AWS's AI-DLC (AI-Driven Development Lifecycle) methodology.

## Status

Active: 1,216 stars, 110 forks, and 19 open issues and pull requests as of 2026-11-01 (GitHub API), pushed 2026-11-01, with 63 releases since June 2026, v0.23.0 on 2026-10-22, and the train running roughly weekly.
The npm CLI has 53 published versions (first in June 2026) and 5,293 downloads in October 2026.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Chorus-AIDLC/Chorus&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Chorus-AIDLC/Chorus&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Chorus-AIDLC/Chorus&type=date&legend=top-left" />
</picture>

Coverage is a launch echo: one 3-point Show HN on 2026-02-25 and nothing since, so the footprint is the repository, the release blog, the docs site, and a four-language README set.

## Strengths

- **The permission matrix is the differentiator: proposal writing, task execution, and verification are separate grants, so an agent cannot do and close its own work.**
- The daemon model is bring-your-own-agent done plainly: your installed CLIs run on your machines, and Chorus adds wake, reporting, and approval routing on top.
- Five months of sustained releases with self-host docs, Docker deployment guidance, and localized READMEs point to a project past the launch spike.

## Cautions

- Community footprint is thin: a single 3-point Show HN, no third-party reviews, benchmarks, or write-ups found as of 2026-11-01.
- AGPL-3.0 asks a compliance decision from anyone embedding it in a hosted product.
- The pipeline is opinionated: ideas, proposals, and task DAGs come first, so ad hoc terminal work still needs another tool beside it.

## Pricing

Free and open source under AGPL-3.0, self-hosted.
No paid tier or hosted plan found as of 2026-11-01.

## Compared to

- [Commonly](../commonly/index.md): the team-pod workspace coordinates people and agents around a chat and board; Chorus adds the permission-gated proposal pipeline and remote execution.
- [OpenRig](../openrig/index.md): the YAML-defined local team over Claude Code, Codex, and Pi; Chorus is the web-first, multi-agent, permission-gated counterpart with a kanban.
- [Vibe Kanban](../vibe-kanban/index.md): board-first solo orchestration without the proposal stage or the permission model.

## Bottom line

**Recommended for small teams that want proposal-level control over what agents build, with a human required at the verify gate.**
Not for solo terminal speed runs, and not for teams needing inline diff review, which Chorus leaves to the CLIs and the VCS.

## Changes

- 2026-11-01 - Created.

## See also

- [Commonly](../commonly/index.md) - the team-pod admission this note lands beside
- [OpenRig](../openrig/index.md) - the local-first team control plane contrast
- [Vibe Kanban](../vibe-kanban/index.md) - the board-first counterpart without permissions
- [Bernstein](../bernstein/index.md) - the governance-layer sibling enforcing merge gates instead of a task DAG

## References

- https://api.github.com/repos/Chorus-AIDLC/Chorus - stars, license, activity, and topic set as of 2026-11-01
- https://raw.githubusercontent.com/Chorus-AIDLC/Chorus/HEAD/README.md - the pipeline, permission matrix, daemons, and quick start
- https://api.github.com/repos/Chorus-AIDLC/Chorus/releases?per_page=100 - the 63-release train through v0.23.0 (2026-10-22)
- https://registry.npmjs.org/@chorus-aidlc/chorus - the CLI package, 53 versions since June 2026
- https://api.npmjs.org/downloads/point/2026-10-01:2026-10-31/@chorus-aidlc/chorus - October 2026 downloads (5,293)
- https://chorus-ai.dev/ - the product site
- https://doc.chorus-ai.dev/guides/manage-agents/ - the agent and permission documentation
- https://chorus-ai.dev/blog/chorus-v0.23.0-release/ - the release-post series
- https://hn.algolia.com/api/v1/search?query=%22human%20collaboration%20platform%20on%20AI-DLC%22&tags=story - the 3-point Show HN (2026-02-25), the coverage baseline
- https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/ - the AI-DLC methodology Chorus implements
