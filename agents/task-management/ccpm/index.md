---
title: CCPM
created: 2026-10-23
updated: 2026-10-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, github-issues, worktrees, multi-agent, spec-driven, open-source]
readability: 3
audience_notes: >
  Teams already on GitHub who want a PRD pipeline and parallel agent execution without adopting another datastore, and engineers comparing forge-native task state with repo-local trackers.
  Assumes you know what a PRD, a git worktree, and an Agent Skill are.
---

CCPM is Automaze's MIT-licensed Agent Skill that turns a PRD into epics and GitHub issues and then runs several agents across git worktrees in parallel, with GitHub Issues as the single source of truth.

## What it is

A skill, not an application: a `SKILL.md` entry point plus reference files and fourteen bash scripts that any agentskills.io-compatible harness loads, documented for Claude Code, Codex, OpenCode, Factory, Amp, and Cursor.
The pipeline runs in five phases: guided brainstorming writes a PRD under `.claude/prds/`, parsing turns it into a technical epic, decomposition writes numbered task files carrying `depends_on`, `parallel`, and `conflicts_with` frontmatter, sync creates an epic issue with sub-issues in your repository, and execution splits one issue into parallel work streams inside a dedicated worktree at `../epic-<name>/`.
GitHub Issues carry the project state: progress posts as issue comments, and every agent commit is formatted `Issue #N: <change>`, so the audit trail runs PRD, epic, issue, code, commit.
Deterministic operations (status, standup, next, blocked) run as bash scripts over the local files, costing no model tokens.
It came out of Automaze, Ran Aroussi's CTO-as-a-service consultancy, as the open-source companion to their delivery practice; the original `/pm:*` slash-command version is preserved on the v1 branch.

## Status

Active and used in the vendor's own practice, mid-scale for this category.
As of 2026-10-23: 8,414 stars, 841 forks, 6 open issues, created 2025-08-18, pushed 2026-10-19, MIT-licensed, with no tagged releases, development moving on branches (main, v1, rc).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=automazeio/ccpm&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=automazeio/ccpm&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=automazeio/ccpm&type=date&legend=top-left" />
</picture>

The launch was a 175-point Show HN thread on 2025-08-20 with 112 comments, one of the larger community footprints in this category, and the discussion pushed back hard on the autonomous-parallelism pitch.
A September 2025 thread on subagent parallelization names ccpm beside BMAD and conductor, with the commenter's own doubt that context-poor subagents can rely on a GitHub issue for their context.
In 2026 the project rebranded from "Claude Code PM" slash commands to a harness-agnostic skill following the agentskills.io standard, keeping v1 on its branch, and third-party writeups of the parallel-claims debate keep appearing.

## Strengths

- GitHub Issues as the board means task state lives in the forge your team already watches: notifications, human-AI handoff, and the comment audit trail need no new infrastructure beyond an authenticated `gh` CLI.
- The worktree-per-epic, streams-per-issue model is the clearest published recipe for splitting one feature across several agents, with `conflicts_with` frontmatter naming the collisions before launch.
- Deterministic operations run as bash scripts, so the cheap questions never cost tokens.
- MIT and harness-agnostic under the agentskills.io standard, a license-and-surface combination the productized PRD pipeline in this category no longer offers.
- Traceability is structural, not aspirational: commit prefixes and issue-numbered task files put every code change inside the issue trail without asking for discipline.

## Cautions

- The Proven Results section (89% less context switching, 75% fewer bugs, 3x faster delivery, a 100% versus 27.7% eval) is the vendor's own, with no third-party benchmark behind any figure.
- Launch-week coverage of the parallel pitch found the weak point: developers report agents need supervision and the bottleneck moves to review, so five parallel streams multiply the reviewing, not just the shipping.
- GitHub is a hard dependency: no GitHub repository, no `gh` authentication, no system, and nothing works on GitLab or offline.
- Parent-child issue relationships want the `gh-sub-issue` extension, with a task-list fallback that degrades the sync model.
- No tagged releases means pinning a commit of a moving main branch, and the v1-to-skill rewrite shows the surface can change wholesale.
- Project state lives in `.claude/` directories, a Claude Code-flavored convention inside a nominally harness-agnostic skill.

## Pricing

The skill is free under MIT, with no hosted tier and no account.
Automaze sells consulting around it: CTO-as-a-Service retainers from $5,000 per month and MVP launches from $8,000, as of 2026-10-23.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-23 | Automaze consulting (not the skill) | Baseline: the skill is free under MIT; Automaze's CTO-as-a-Service retainer starts at $5,000/mo and MVP launches at $8,000. | [automaze.io](https://automaze.io) |

## Compared to

- [Task Master](../task-master/index.md): the other PRD-first pipeline; Task Master carries its own task store and a Commons Clause license, CCPM keeps MIT and rents the store from GitHub.
- [beads](../beads/index.md): the repo-local counterpoint when GitHub cannot host your state; beads works offline and forge-agnostic, CCPM trades that for team-visible issues.
- [Backlog.md](../backlog-md/index.md): the review-gate counterpoint; both keep the plan in readable files, Backlog.md's board versions in git while CCPM's lives in GitHub Issues.

## Bottom line

**Recommended for teams already on GitHub and a skills-compatible harness who want the PRD pipeline and parallel agent execution without adopting another datastore.**
Not for non-GitHub or air-gapped setups, or anyone who needs benchmarked claims rather than vendor-reported ones.
My disagreeable claim: GitHub Issues is the most underrated agent task store in this category, and every repo-local tracker here re-creates, worse, the audit trail, assignee model, and notification fabric a forge already ships.

## Changes

- 2026-10-23 - Created from the coordinator handoff after the cross-category scan left automazeio/ccpm unmatched, recording the GitHub-Issues-as-board design, the worktree parallel execution, and the v1-to-skill rewrite.

## See also

- [Task Master](../task-master/index.md) - the PRD pipeline this method descends from, now a commercial engine
- [beads](../beads/index.md) - the repo-local graph tracker for teams that cannot host state on GitHub
- [Backlog.md](../backlog-md/index.md) - the markdown review-gate counterpoint
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - the spec-first process layer without a runtime
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/automazeio/ccpm - repository, MIT license, stars baseline, and push activity as of 2026-10-23
- https://raw.githubusercontent.com/automazeio/ccpm/main/README.md - the workflow, parallel streams, proven-results claims, and the agent-skill rewrite
- https://raw.githubusercontent.com/automazeio/ccpm/main/skill/ccpm/SKILL.md - the skill entry point: the five phases, the script-first rule, and the harness list
- https://api.github.com/repos/automazeio/ccpm - stars, forks, dates, and license as of 2026-10-23
- https://news.ycombinator.com/item?id=44960594 - the 175-point, 112-comment Show HN launch thread (2025-08-20)
- https://hn.algolia.com/api/v1/items/44960594 - the launch thread's comment tree, the supervision and review skepticism
- https://finance.biggo.com/news/202508201915_Claude_Code_PM_Parallel_AI_Development_Questioned - the critical read of the parallel-execution claims
- https://automaze.io - the vendor: Ran Aroussi, CTO-as-a-Service from $5,000/mo
- https://news.ycombinator.com/item?id=45237239 - the 2025-09-14 comment naming ccpm beside BMAD and conductor, with the context-starvation doubt
