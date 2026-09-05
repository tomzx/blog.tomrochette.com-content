---
title: "Machinist"
created: 2026-09-05
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, orchestration, go]
readability: 3
audience_notes: >
  Engineers wiring coding agents into repeatable pipelines who want the control plane local and the agents swappable.
  Assumes you know what a worktree, an executor, and a pull request gate are.
---

**Machinist is an open-source software factory whose whole design is one controlled entrypoint: workers expose named commands over named repositories, and nothing arbitrary crosses the boundary.**
Facts below verified as of 2026-09-05.

## What it is

A MIT-licensed Go control plane that runs coding-agent workflows on your own machine: a config file maps named commands to executors (Codex, Claude Code, any agent CLI, a test runner, a shell script), sends prompts on standard input, streams output, and records durable events, artifacts, terminal outcomes, duration, and reported token use.
Repositories, credentials, model aliases, and executor configuration stay on the worker; the human gate is explicit, since Machinist hands back a pull request and does not decide what ships.
Scripts are deliberately opaque to the controller: no invented child runs, graphs, or checkpoints, and a killed script restarts from the beginning unless the script owns its own checkpointing.

## Status

Active and early: created 2026-07-16, 322 stars and 64 forks, pushed 2026-09-03, releases v0.2.0 through v0.4.0, with the README labeling it early-access software.
**There is no Hacker News thread or independent coverage as of 2026-09-05, so the missing community footprint is itself the signal, and the repository plus the docs site at machinist.sh are the whole evidence base.**
The velocity (four releases in seven weeks) says maintained; the single-author commit history says bus-factor one.

## Strengths

- The named-command boundary is a real security idea: the agent-facing surface is a fixed vocabulary, not shell text, which is more than most factories in this category attempt.
- Bring-your-own-harness by construction, since any executable that reads a prompt on stdin is a valid executor.
- Candid about what it will not do: no hidden orchestration, no automatic shipping, restart-from-zero semantics documented rather than papered over.

## Cautions

- Solo-maintainer risk on an early-access product, with no independent evaluation of the execution model yet.
- No resumable stages or built-in isolation in the controller: the note-level worktree story depends on the executors you configure.
- The missing HN footprint cuts both ways: no drama, but also no second opinion.

## Pricing

Free and open source under MIT; you supply the machine and the model tokens.

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md): the other code-owns-the-loop minimalism, but SSSF packages as a skill and binds to pi, while Machinist is a standalone Go binary that accepts any executor.
- [HAR](../har/index.md): the fleet harness with per-agent worktree slots and a shared .har contract; HAR isolates more, Machinist gates the entrypoint more.
- [Fluent](../fluent/index.md): the self-improving alternative, when you want the factory to learn rather than just record.

## Bottom line

Recommended for engineers who want a local, auditable runner around agent CLIs and are comfortable being close to the only users.
Not for teams needing proven scale, resumable pipelines, or a community to escalate to.

## See also

- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the controlled-entrypoint column sits among the factories
- [HAR](../har/index.md) - the isolation-first factory comparison
- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the skill-packaged minimalism comparison
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - scheduled triggers versus invoked factory runs

## References

- https://github.com/owainlewis/machinist - repository, execution model, configuration, license
- https://machinist.sh - docs site and positioning
- https://github.com/owainlewis/machinist/blob/main/docs/configuration.md - commands, executors, workers, and repositories
- https://github.com/owainlewis/machinist/releases - the release cadence grounding the status section
- https://github.com/owainlewis/machinist/blob/main/examples/workflows/README.md - repository-owned orchestration examples
