---
title: Spec-Driven Develop
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, github-issues, workflow, open-source]
readability: 3
audience_notes: >
  Engineers running large rewrites or migrations through a coding agent who want the work tracked in GitHub Issues instead of repo-side markdown state.
  Assumes you know what a delivery batch and a review gate are.
---

Spec-Driven Develop is a solo-maintained, MIT-licensed pack of three pure-Markdown skills that routes large changes through a seven-phase spec-driven pipeline ending in GitHub Issues and one batch pull request per phase, with an architecture-principles checklist and a drift score keeping execution aligned with the plan.

**It is this category's GitHub-native wing: the spec artifacts are conventional markdown, but the tracker is Issues, Milestones, and one reviewable batch PR per phase, and its drift score is the only execution control in the category that measures how far reality has left the plan and halts at thresholds.**

## What it is

Three Markdown skills (the main Spec-Driven Develop pipeline, Deep Discuss for structured problem analysis, and Review SPD for findings-first code review) plus optional plugin manifests for Claude Code, Codex, and OpenCode, install scripts for Cursor, and a generic copy-the-SKILL.md path for any agent that reads Markdown skills.
No runtime, no SDK, no dependencies.
The pipeline runs intent capture, deep analysis with a per-module S.U.P.E.R health score, grounded intent refinement, task decomposition into delivery batches, MASTER.md progress tracking, a confirmation gate, then execution and archiving.
In GitHub modes it creates one Issue per task organized by Milestones and Labels and integrates one batch PR per phase; without the `gh` CLI it degrades to local-only markdown.
Release v1.15 made execution orchestrator-centric with tiered subagent dispatch (direct execution as the norm, one coder for heavy batches, up to four parallel lanes in worktrees) and tiered review (machine validation and the orchestrator's own diff by default, an independent reviewer reserved for lanes and high-risk work).

## Status

Quiet since late July.
As of 2026-10-11: 987 stars and 100 forks since creation on 2026-03-21, pushed 2026-07-26, MIT, solo author (the zhu1090093659 account).
All five GitHub releases landed in July 2026, three of them on July 1, and nothing has shipped since v1.15.0 (2026-07-26).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=zhu1090093659/spec_driven_develop&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=zhu1090093659/spec_driven_develop&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=zhu1090093659/spec_driven_develop&type=date&legend=top-left" />
</picture>

**No Hacker News thread about it exists as of 2026-10-11, and the only independent coverage found is a Hysen Labs directory review (updated 2026-09-10) that is more skeptical than the star count suggests, so the adoption case rests on stars and the bilingual README's Chinese-language community distribution (a linux.do link sits in the README's friendly-links section).**

## Strengths

- GitHub-native tracking is the distinctive move: Issues are the atomic acceptance records and the batch PR owns integration, so progress lives in the tools teams already watch instead of a progress file only the agent reads.
- The drift-score loop is an actual control system: execution telemetry after every task feeds thresholds at 20, 40, and 60 percent that annotate, halt and re-decompose, or force a return to scope re-evaluation.
- S.U.P.E.R turns architecture principles into per-task check items with a stated escalation rule (all pass, proceed; one or two fail, fix first; three or more, stop and refactor).
- Brownfield is the default target: the pipeline exists for rewrites and migrations, and Phase 1 inventories and grades the existing architecture before anything is planned.

## Cautions

- Dormant for over two months (last push 2026-07-26) with a solo maintainer, so the format can stall without notice.
- Nothing is enforced: Hysen's review makes the point that this is all prompts an agent may interpret differently next month, the same ceiling every prompt-only column in this category carries.
- The README contains an "LLM-Friendly Summary" section that tells other tools what to write about the project, an unusual self-description surface that Hysen flagged, and worth weighing when reading the README's own claims.
- Two of its three modes require a GitHub issue tracker, and the seven-phase ceremony only pays off on large changes, which the keyword trigger handles by never firing on small work.

## Pricing

Does not apply: MIT, free, no paid tier recorded as of 2026-10-11.

## Compared to

- [Spec Kitty](../spec-kitty/index.md): the other governance-and-tracking member; Spec Kitty keeps state in your repo and sells a platform around it, Spec-Driven Develop drives GitHub's own tracker and has no company attached.
- [GSD](../gsd/index.md): the other large-change loop; GSD quarantines phases in fresh-context subagents and keeps state in markdown, Spec-Driven Develop keeps one orchestrator and tracks state in Issues.
- [Vibe Coding Prompt Template](../vibe-coding-prompt-template/index.md): the other pure-Markdown, zero-runtime workflow; the prompt pack sequences a human through planning in chat, Spec-Driven Develop hands the whole pipeline to the agent.

## Bottom line

**Recommended for teams already working in GitHub Issues that point an agent at a large rewrite or migration and want the work to land as reviewable batch PRs.**
Not for small changes, not for repos outside GitHub's tracker model, and not for anyone who needs an enforced process or an actively maintained steward.

## Changes

- 2026-10-11 - Created from the task-management scan's cross-category flag, resolving zhu1090093659/spec_driven_develop into this category as the GitHub-native tracker column.

## See also

- [Spec Kitty](../spec-kitty/index.md) - the other governance-and-tracking member, repo-side state versus GitHub-native state
- [GSD](../gsd/index.md) - the other large-change phase loop
- [Vibe Coding Prompt Template](../vibe-coding-prompt-template/index.md) - the other pure-Markdown, zero-runtime workflow
- [GitHub Spec Kit](../spec-kit/index.md) - the movement root whose fixed ceremony this category keeps reworking
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/zhu1090093659/spec_driven_develop - repository: stars, forks, dates, license (987 stars as of 2026-10-11)
- https://raw.githubusercontent.com/zhu1090093659/spec_driven_develop/main/README.md - the seven-phase pipeline, the S.U.P.E.R table, the drift thresholds, and the platform install surface
- https://raw.githubusercontent.com/zhu1090093659/spec_driven_develop/main/README.zh-CN.md - the Chinese README grounding the bilingual distribution claim
- https://github.com/zhu1090093659/spec_driven_develop/releases.atom - the release history: five releases, all July 2026, through v1.15.0 (2026-07-26)
- https://hysenlabs.com/en/projects/zhu1090093659-spec-driven-develop - the independent directory review (updated 2026-09-10), the critical source
- https://hn.algolia.com/api/v1/search?query=zhu1090093659&hitsPerPage=5 - the missing Hacker News footprint, checked 2026-10-11
