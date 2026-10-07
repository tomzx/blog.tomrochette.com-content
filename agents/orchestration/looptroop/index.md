---
title: LoopTroop
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, planning, worktrees, opencode]
readability: 3
audience_notes: >
  Engineers tackling large, multi-file coding tickets who want planning and recovery structure rather than a chat loop.
  Assumes you run OpenCode and are comfortable with git worktrees.
---

LoopTroop is an MIT-licensed local GUI orchestrator for repo-scale coding tickets that turns a ticket into a planned, reviewable, agent-executed pull request through multi-model council planning, atomic beads, isolated OpenCode worktrees, and fresh-context recovery loops.

**LoopTroop's bet is "slow and perfect": for long, high-correctness feature work it sacrifices chat speed for multi-model planning, minimal per-stage context, and a strict-manager retry that throws away a contaminated agent session instead of arguing with it.**

## What it is

A local web app (installed by curl, npm, Homebrew, Scoop, Bun, pnpm, yarn, or Docker) from looptroop-ai that runs on top of OpenCode.
The pipeline has three layers: planning, where an adaptive interview produces a PRD that an LLM council drafts, anonymously scores, and refines into atomic "beads" (independent units with acceptance criteria and target files); execution, where OpenCode implements each bead in its own git worktree; and shipping, where a final verification pass hands off to your main branch.
Its context engineering rebuilds minimal per-status context for each phase rather than passing a bloated transcript, and its Ralph-style retry preserves a compact error trace, discards the degraded workspace, and retries in a fresh worktree, which the site claims sustains ten or more hours of unattended execution.
A human approval gate sits before any code is committed, and the README and docs cover the ticket state machine, prompts, API, and CLI.

## Status

Active and early: about 160 stars and 14 forks as of 2026-10-06, created 2026-03-03, with commits through 2026-10-01 and a latest release of v0.6.0 (2026-10-01), a major update (80 commits since v0.5.9) that added OpenCode v2 support, traceable skip reasons and decision history, and more than doubled the passing test count to 8,099.

[![Star History Chart](https://api.star-history.com/chart?repos=looptroop-ai/LoopTroop&type=date&legend=top-left)](https://www.star-history.com/?repos=looptroop-ai%2FLoopTroop&type=date&legend=top-left)

The documentation is unusually complete for an alpha, but the project's own status page calls it "early alpha software" with bugs still likely, and it lists two configured constraints: councils of 2 to 10 models, and one active ticket per project in the execution band.
**A repo-scale orchestrator that can only run one ticket at a time per project is betting that depth beats throughput, which is the opposite of the parallel-session tools beside it.**

## Strengths

- Multi-model council planning with independent drafting, anonymous voting, and winner refinement attacks the single-model bias problem directly.
- Atomic bead decomposition with explicit acceptance criteria and per-bead isolation prevents cascading failures across a large change.
- Minimal, rebuilt per-phase context is a principled answer to context rot in long autonomous runs.
- Fresh-context recovery (the Ralph loop) is more robust than retrying inside a degraded session.
- Free, MIT, 100% local, with a complete DOCUMENTED lifecycle and per-bead diff review before merge.

## Cautions

- Early alpha, 154 stars, single vendor, and one active ticket per project, so it is not a parallel fan-out tool.
- OpenCode is the only execution backend; no Claude Code, Codex, or others.
- Agents run with full local user privileges, and the docs themselves recommend running inside a disposable VM or cloud sandbox.
- Planning is deliberately slow: the interview can take over an hour, which is a poor fit for small tasks.
- The local GUI plus Node and OpenCode prerequisites make setup heavier than a CLI tool.

## Pricing

Free and open source under MIT, with no telemetry.
You pay only for the model providers OpenCode is configured to use.

## Compared to

- [Crewplane](../crewplane/index.md): a CLI-first Markdown workflow runner; choose LoopTroop when you want council planning and a GUI rather than repo-owned workflow files.
- [Sandcastle](../sandcastle/index.md): a TypeScript library that sandboxes and merges agents; choose LoopTroop when the problem is planning and recovery for big tickets, not sandbox plumbing.
- [Conductor](../conductor/index.md): the polished Mac dashboard for many small parallel sessions; choose LoopTroop for fewer, long, high-correctness feature runs.

## Bottom line

**Recommended for engineers who want a local, MIT, planning-first orchestrator for large OpenCode tickets with human approval and strong recovery.**
Not for anyone who needs multi-harness support, parallel tickets, or a mature tool.

## Changes

- 2026-09-27 - Created.
- 2026-10-02 - Recorded v0.6.0 (October 1, OpenCode v2 support, traceable skip reasons, and a doubled test suite) as the new latest release and refreshed counts.
- 2026-10-07 - Added the looptroop-ai/LoopTroop star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Crewplane](../crewplane/index.md) - the Markdown-workflow counterpart
- [Sandcastle](../sandcastle/index.md) - the sandboxed-library alternative
- [Conductor](../conductor/index.md) - the parallel, small-session incumbent
- [OpenCode](../../harnesses/opencode/index.md) - the single execution backend LoopTroop drives

## References

- https://github.com/looptroop-ai/LoopTroop - repository, feature set, license, stars, and release data
- https://www.looptroop.ovh/ - product positioning, LLM council, beads, Ralph loop, and human approval gate
- https://www.looptroop.ovh/docs/ - architecture, workflow, context engineering, and the early-alpha status statement
- https://openorchestrators.org/ - the curated directory's LoopTroop entry
- https://news.ycombinator.com/item?id=48643477 - the author's Show HN post introducing the local orchestrator
