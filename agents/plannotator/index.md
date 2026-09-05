---
title: Plannotator
created: 2026-08-30
updated: 2026-09-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, code-review, human-in-the-loop, open-source]
readability: 3
audience_notes: >
  Engineers who review coding-agent plans and diffs and want their feedback to reach the agent as structured input rather than retyped prose.
  Assumes you know what plan mode and a diff are.
---

Plannotator is a free, open-source, local browser-based review surface that intercepts coding-agent plan proposals and code diffs so you can annotate them visually and send structured feedback straight back into the live agent session.
Facts below verified as of 2026-09-05.

**Plannotator closes the cheapest loop in agent work, the one between what you see wrong in a plan and what the agent receives, and its marketing outpaced its README exactly once, on the encryption claim, which the README itself corrects.**

## What it is

A TypeScript installer that wires into nine harnesses, Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Kiro CLI, Droid, Amp, and Pi, using hooks where they exist (Claude Code's ExitPlanMode hook opens any proposed plan in the browser) and slash commands elsewhere.
Three surfaces: plan review with inline comments and deletion marks, code review of uncommitted changes or any GitHub and GitLab PR URL with side-by-side diffs and staging, and annotation of markdown, folders, URLs, and rendered HTML artifacts.
Approve lets the agent proceed; deny sends annotations back as the agent's next instruction, no copy-paste, and plan revisions are diffed against each other.
Local-first with no telemetry, an optional TUI, a VS Code extension, and supply-chain hygiene (SLSA provenance, SBOMs, Grype gating).
Dual Apache-2.0 or MIT, written almost entirely by one developer (880 commits) with 138 total commit contributors and only 8 with five or more, with a hosted Workspaces product in private beta.

## Status

Fast and growing: 8,418 stars, 624 forks, 155 open issues and PRs as of 2026-09-04, created 2025-12-28, pushed 2026-09-03, v0.27.12 released 2026-09-03.
**The 0.27.x line says pre-1.0 churn, and the growth came through social channels rather than press; its Show HN thread drew 5 points.**

## Strengths

- The broadest harness coverage of any review surface, nine agents through one installer.
- The feedback loop actually closes: annotations become the agent's next instruction in the live session.
- Supply-chain discipline rare for an indie tool: SLSA attestations, SBOMs, vulnerability gating.
- Plan-revision diffing makes agent iteration legible.

## Cautions

- The Show HN post claimed sharing is end-to-end encrypted; the README admits small markdown shares compress into an unencrypted URL fragment anyone with the link can read.
- Single-maintainer bus factor with high version churn, and partial integrations (Droid lacks plan interception, Codex hooks are experimental).
- The installer reaches into many host configs, npm, and third-party services; use `--minimal` if that concerns you.
- The hosted Workspaces direction carries a different privacy model than the local app, pricing unannounced.

## Pricing

The core app is free and open source under Apache-2.0 or MIT, stated to remain free.
Workspaces (hosted team layer) is in private beta with no public pricing; OSS contributors are promised lifetime access.

## Compared to

- GitHub PR review: asynchronous, post-push, permanent record; Plannotator covers the pre-push loop where corrections reach a live agent in seconds, though it can review PR URLs too.
- Orchestration app review (Conductor, [Superset](../superset/index.md)): those review within a session lifecycle they manage; Plannotator is deliberately harness-agnostic and plugs into whatever you already run.
- Terminal diff review: faster for a 50-line diff; Plannotator pays off on long plans, multi-file diffs, and team annotation, with its own TUI for the middle ground.

## Bottom line

**Recommended for engineers who review agent plans seriously and want their annotations to steer the running session instead of living in a text editor.**
Not for minimal-install purists, and not yet for teams whose review process requires the hosted Workspaces tier before it has a price.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Superset](../superset/index.md) - review inside the orchestration layer
- [OpenCodeReview](../open-code-review/index.md) - the machine-reviewed counterpart
- [Claude Code hooks](../claude-code-hooks/index.md) - the hook mechanism Plannotator builds on

## References

- https://github.com/backnotprop/plannotator - repository, supported agents, mechanics, license
- https://raw.githubusercontent.com/backnotprop/plannotator/HEAD/README.md - the privacy boundaries, including the unencrypted small-share caveat
- https://plannotator.ai/ - product pitch and Workspaces framing
- https://docs.plannotator.ai/open-source/start/installation - platforms and per-agent setup
- https://github.com/backnotprop/plannotator/releases - release cadence evidence
- https://news.ycombinator.com/item?id=48495970 - the Show HN thread with the encryption-claim discrepancy
