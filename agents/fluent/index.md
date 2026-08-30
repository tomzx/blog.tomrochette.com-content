---
title: "Fluent"
created: 2026-08-29
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, llm=glm-5.3-flash, software-factory, self-improving, autonomous-agents]
readability: 3
audience_notes: >
  Engineers evaluating a self-improving, code-owned software factory against simpler pipelines.
  Assumes you know what a work item, a gate, and a bounded agent phase are.
---

Fluent is a self-improving software factory that turns a team's vision, ideas, bug reports, user feedback, production logs, and agent traces into working software with writer, tester, reviewer, and learner roles inside one deterministic loop.
Facts below verified as of 2026-08-30.

## What it is

Mrinal Wadhwa's (fluent.computer) Fluent is an Apache-2.0 Rust binary plus a skill you install into Codex, Claude Code, or Pi, currently macOS-only.
It is driven by conversation: an Observations queue becomes Briefs, Behavior Specifications (written in EARS), a Technical Approach, and an Implementation Plan, and those turn into Work Items.
Each run of a Work Item is an Attempt that a Writer, parallel Reviewers, a deterministic final Tester, and a Learner pass through inside an isolated git worktree, optionally on a remote machine through AWS Fargate.

## Status

Active and meaningfully developed: 84 stars and 1 fork since creation on 2026-07-10, 1,450 commits, and v0.2.0 released 2026-08-15 per the GitHub API as of 2026-08-30.
It is a focused single-author project with a real Discord community, not the biggest crowd but steadily shipped.
The governance and self-improvement loop are unusually detailed for the category, which is the design bet the note weighs.

## Strengths

- **The final gate is a deterministic Tester, not an agent**: it reads test commands from `.fluent/tester.yaml`, runs them once in isolation, and binds the result to the exact reviewed commit.
- **It keeps learning**: a Learner writes reusable lessons into `.fluent/expertise/` after accepted changes, and follow-ups become new Observations, so the factory compounds.
- **The loop is resumable and fail-closed**: corrections re-prompt the Writer without a cold restart, and evidence binds to exact commits so a resume cannot mix results from different candidate states.
- **Agent isolation is a first-class move**: every Attempt gets its own worktree, and human questions return to a separate attention queue.

## Cautions

- **Young and opinionated**: it is pre-1.0 with 84 stars, and its EARS behavior specs plus multi-layer pipeline are a heavier ceremony than most teams adopt.
- **macOS-only today**, and it is a Rust binary plus skill bootstrap, so the on-ramp is not as trivial as stamping a Python pip package.
- **Remote execution needs AWS Fargate**, which is a real dependency for teams that want off-laptop runs.
- **The tight loop is also the lock-in**: conventions like Behavior Specifications and Expertise are Fluent-specific, so leaving means remigrating the repository's process, not just uninstalling.

## Pricing

Apache-2.0, free and self-hosted, designed to run on your subscriptions plus your own compute or remote machines through your AWS account.
There is no paid tier and no hosted cloud.

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md) keeps the loop in a stamped Python skill and runs on the current branch; Fluent adds isolated worktrees, a deterministic final Tester, and a self-improvement loop at the cost of far more ceremony.
- [HAR](../har/index.md) is a harness that coordinates a fleet of coding agents around a repo contract with deterministic verify; Fluent is a self-improving factory that also owns the learning loop.
- [Executions](../executions-feature-matrix/index.md) schedules and triggers agent runs; Fluent is a factory you drive by conversation and a queue, not a scheduler.

## Bottom line

Recommended for teams that want a genuinely self-improving, defense-in-depth factory and accept a real process and pre-1.0 risk.
Not for the one-off feature, which a simpler pipeline or a single agent handles cheaper, and not for teams unwilling to adopt its EARS-and-worktree process wholesale.

## See also

- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the lightweight founding member this note compares Fluent against
- [HAR](../har/index.md) - the harness-style software factory for fleets of coding agents
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - the category matrix Fluent now fills a column in
- [Code Factories: Factorio](../../code-factories-factorio/index.md) - the corpus metaphor this self-improving factory most fully realizes
- [The Self-Evolving Repository](../../the-self-evolving-repository/index.md) - the full-automation end of the spectrum Fluent is the most tractable step toward

## References

- https://github.com/mrinalwadhwa/fluent - the repo, the Observer-to-Merge-Candidate loop, and the expertise model
- https://github.com/mrinalwadhwa/fluent/blob/main/documentation/releases/v0.2.0.md - the v0.2.0 release notes and behavior changes
- https://fluent.computer - the official site and the factory framing
- https://discord.gg/dygEVzG3gf - the software-factory builder community
- https://agentskills.io - the skill standard Fluent installs through, grounding its skill-based delivery
