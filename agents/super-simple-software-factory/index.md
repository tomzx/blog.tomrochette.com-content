---
title: "Super Simple Software Factory"
created: 2026-08-29
updated: 2026-08-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, software-factory, agentic-workflows, sdlc]
readability: 3
audience_notes: >
  Engineers who have used a coding agent and want a repeatable, deterministic pipeline around it.
  Assumes you know what a skill, a phase, and a gate are in an agentic workflow.
---

A software factory, and the founding member of this category, is a repeatable agents-plus-code workflow packaged as one skill and stamped into any repo: deterministic Python owns the sequencing and the coding agent owns only one bounded phase at a time.
Facts below verified as of 2026-08-29.

## What it is

Disler's (IndyDevDan) Super Simple Software Factory, SSSF for short, is an MIT open-source skill, `.claude/skills/sssf/`, that installs into a target repository and stamps twelve starter workflows called ADWs (AI Developer Workflows).
The core thesis is "agent proposes, code disposes": a deterministic Python script owns phases, retries, and acceptance, while the coding agents work inside named phases and hand typed JSON envelopes across the seams.
Each run is traced to a SQLite database in near real time, so a factory run is observable while it is running, not reconstructed after.
It is built on the `pi` coding agent plus `uv`, and there is a Vue-and-Bun visualizer for the trace.

## Status

Active, young, and deliberately small: 764 stars and 189 forks since creation on 2026-08-02, with the last push on 2026-08-04, per the GitHub API as of 2026-08-29.
The repository has a single commit on `main`, no releases, and a separate `example` branch that holds a demo repo with the factory already stamped in and real traces.
This is a one-author starting point ("nothing here is meant to survive contact with your codebase unchanged"), not an actively multiplying ecosystem.

## Strengths

- **Code owns the loop**, so the same workflow run a hundred times behaves like the first: retries and acceptance live in Python, not in the prompt.
- **Bounded, typed phases**: agents return a declared JSON envelope parsed against a schema, and gates verify artifacts and test results after the fact.
- **Correction instead of restart**: when an envelope fails to parse or a gate fails, the same session is re-prompted with a named correction rather than started cold.
- **Observable by construction**: every phase and tool call streams into a WAL SQLite database, and the trace UI reads that same db.

## Cautions

- **v1 locks you to the `pi` coding agent**: `claude_code` is schema-valid but stubbed, and the README's `pi` repository link is dead as of 2026-08-29, so the chosen model is a moving target.
- **It runs on your current branch**: there is no sandbox, no branch-per-run, no merge step, and no human approval phase, all admitted as missing on purpose.
- **The shipped test gates are placeholders** that exit 0 until you wire in your real quality commands, so a fresh install's green test phase is theater until customized.
- **A bare model pattern trips validation**: a model id that matches several providers refuses to spawn, forcing you to write `provider/model-id` everywhere.

## Pricing

MIT license, free, self-hosted: you bring the API keys for whatever providers your roster names, and it is designed to run entirely on your own machine or CI.
There is no paid tier and no cloud component.

## Compared to

- [Fluent](../fluent/index.md) is a self-improving factory with isolated worktrees, a deterministic final Tester, and a learning loop, at the cost of far more ceremony; SSSF is the lighter stamped loop that runs on the current branch.
- [HAR](../har/index.md) coordinates a fleet of coding agents around a `.har/` contract with deterministic verification; SSSF stamps one Python loop into the repo instead of running alongside existing agents.
- [Spec-driven development](../spec-driven-development-feature-matrix/index.md), as in [Spec Kit](../spec-kit/index.md), pulls the plan into a structured pre-agent artifact; SSSF instead makes the whole plan-build-test-review loop a stamped pipeline, spec included but not the point.
- [Hybrid execution](../hybrid-execution-feature-matrix/index.md) covers the deterministic-orchestrates-LLM principle at the layer of structured outputs, whereas SSSF applies it to a full SDLC workflow packaged as a skill.
- [Executions](../executions-feature-matrix/index.md) is about scheduled and event-triggered runs; SSSF is a factory you invoke by hand or by chain, not a scheduler.

## Bottom line

Recommended for teams that run the same multi-agent workflow over and over and want deterministic, auditable, repeatable runs on top of a coding agent.
Not for one-off features, which a single agent prompt handles cheaper, and not for anyone unwilling to wire their own gates and prompts, because the shipped defaults are deliberate placeholders.

## See also

- [Code Factories: Factorio](../../code-factories-factorio/index.md) - the factory metaphor the corpus develops, which this category names its geometry after
- [The Self-Evolving Repository](../../the-self-evolving-repository/index.md) - the full-automation end of the spectrum this factory is a tractable step toward
- [Rethinking Code Review in the Age of LLMs](../../rethinking-code-review-in-the-age-of-llms/index.md) - the reviewer phase inside the factory restates that article's thesis
- [SSSF trace UI vs the landscape](../agentic-coding-tools-landscape/index.md) - where a stamped factory sits among harnesses and orchestration
- [Spec-driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the spec-first alternative to a full factory

## References

- https://github.com/disler/super-simple-software-factory - the skill repo, README, architecture, and the twelve starter workflows
- https://github.com/disler/super-simple-software-factory/tree/example - the example branch with the factory stamped into a demo app and real traces
- https://youtu.be/haUfb1ievTE - IndyDevDan's full video breakdown of the factory
- https://agenticengineer.com - the author's agentic-engineering site and the "Master Agentic Coding" framing
- https://github.com/huggingface/tau - a confirmed Python port of the underlying pi agent, evidence the agent is real despite the dead README link
