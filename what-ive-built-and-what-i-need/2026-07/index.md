---
title: "What I've built and what I need: July 2026"
created: 2026-08-06
type: post
status: finished
tags: [personal-update, llm, ai-agents, automation, sdlc, workflows, fully-ai-generated, llm=glm-5.2, llm=glm-5.3]
readability: 3
audience_notes: >
  A monthly status update for anyone following my work on LLM-driven software development pipelines. Assumes familiarity with the SDLC skills and with human-gated versus autonomous agent workflows.
---

The headline this month was **llm-augmented-workflows carrying an issue all the way through to a human gate**.
Underneath the headline, the month spread into maturing the SDLC pipeline, reworking PR validation around visual proof, and shipping a wave of new skills.

## What I Have Been Working On

**Iterating on [llm-augmented-workflows](https://github.com/TomzxCode/llm-augmented-workflows).**
The project is still rough, but it now moves an issue through real stages instead of demoing a single one.
A cycle looks like this: an issue is created, it gets triaged, and the appropriate workflow runs until it hits a stage that requires a human.
For feature requests, the workflow runs triage into a plan PR for review, and once the plan merges, continues to an implementation PR.
For bug fixes, the flow goes from triage into a fix PR rather than stopping at reproduction.
Triage is handled end to end, which closes a point I'd written about in earlier posts.
I'm building it to support both human-gated and fully autonomous modes from the start, so the same flow can run with or without checkpoints.

**Building [github-board](https://github.com/TomzxCode/github-board).**
github-board is a frontend-only web application, served directly via GitHub Pages, that lets you build columns and rows from any field on a GitHub issue or pull request.
It turns issue and PR data into a configurable board view with no backend.

**Adding the [resolve-pr-conflicts](https://github.com/tomzx/agents/blob/main/skills/resolve-pr-conflicts/SKILL.md) skill.**
I now run the skill daily across the repositories I contribute to.
It scans for my open pull requests that have merge conflicts and resolves each one in parallel, fanning out a separate agent session per PR into its own worktree.
Each session merges the base branch, resolves the conflict markers, runs the project's verification, and pushes, while ambiguous or verify-failing resolutions get aborted rather than guessed.
The practical effect is that my PRs stay mergeable without me babysitting rebase loops.

**Refactored the SDLC pipeline.**
Feature directories dropped the `FEAT-NNNN-` prefix for `N-<slug>`, and pending items now carry a `p` prefix with a promotion flow through [create-placeholder-issue](https://github.com/tomzx/agents/blob/main/skills/create-placeholder-issue/SKILL.md).
The old `questions.md` drift log is gone, replaced by a `review-verdict` regression that [sync-sdlc](https://github.com/tomzx/agents/blob/main/skills/sync-sdlc/SKILL.md) and [backpropagate-sdlc](https://github.com/tomzx/agents/blob/main/skills/backpropagate-sdlc/SKILL.md) track across phases.
Review findings now persist to files instead of disappearing, and I slimmed the `create-*` family by roughly 750 lines by pointing each at templates and giving it a self-check checklist.
Each phase skill is now explicitly loaded before it runs, and a needs-assessment template joined the pipeline.

**Reworked PR validation around visual proof.**
Visual proof capture moved out of [create-pr](https://github.com/tomzx/agents/blob/main/skills/create-pr/SKILL.md) into a dedicated [validate-implementation](https://github.com/tomzx/agents/blob/main/skills/validate-implementation/SKILL.md) skill, which writes a proof manifest before the PR is ever opened, so recording happens before creation rather than during it.
Bug fixes now capture before/after recordings via [reproduce-issue](https://github.com/tomzx/agents/blob/main/skills/reproduce-issue/SKILL.md) and [fix-issue](https://github.com/tomzx/agents/blob/main/skills/fix-issue/SKILL.md).
And [validate-pr](https://github.com/tomzx/agents/blob/main/skills/validate-pr/SKILL.md) and [verify-pr](https://github.com/tomzx/agents/blob/main/skills/verify-pr/SKILL.md) now check against the issue's acceptance criteria rather than the PR's own claims, with body and footer split for GitHub attribution.

**Shipped a wave of new skills.**
Slack and memory support landed with [slackx](https://github.com/tomzx/agents/blob/main/skills/slackx/SKILL.md) and [sessions-memory](https://github.com/tomzx/agents/blob/main/skills/sessions-memory/SKILL.md), which turns archived sessions into PARA memory.
Team docs gained [create-team-api](https://github.com/tomzx/agents/blob/main/skills/create-team-api/SKILL.md) and [create-team-charter](https://github.com/tomzx/agents/blob/main/skills/create-team-charter/SKILL.md).
Codebase upkeep got [improve-codebase](https://github.com/tomzx/agents/blob/main/skills/improve-codebase/SKILL.md), [improve-skill](https://github.com/tomzx/agents/blob/main/skills/improve-skill/SKILL.md), [sync-documentation](https://github.com/tomzx/agents/blob/main/skills/sync-documentation/SKILL.md), and [sync-opinions](https://github.com/tomzx/agents/blob/main/skills/sync-opinions/SKILL.md).
Planning expanded with [create-goals](https://github.com/tomzx/agents/blob/main/skills/create-goals/SKILL.md), [create-service-levels](https://github.com/tomzx/agents/blob/main/skills/create-service-levels/SKILL.md) and their `review-*` counterparts, [create-mockups](https://github.com/tomzx/agents/blob/main/skills/create-mockups/SKILL.md), and [create-placeholder-issue](https://github.com/tomzx/agents/blob/main/skills/create-placeholder-issue/SKILL.md).
Issue triage gained [check-issue-status](https://github.com/tomzx/agents/blob/main/skills/check-issue-status/SKILL.md), [check-issues-status](https://github.com/tomzx/agents/blob/main/skills/check-issues-status/SKILL.md), and [check-linked-pr](https://github.com/tomzx/agents/blob/main/skills/check-linked-pr/SKILL.md).
Demo tooling arrived with [research-topic](https://github.com/tomzx/agents/blob/main/skills/research-topic/SKILL.md), [record-asciinema](https://github.com/tomzx/agents/blob/main/skills/record-asciinema/SKILL.md), and [record-playwright](https://github.com/tomzx/agents/blob/main/skills/record-playwright/SKILL.md).

**Tidied conventions.**
[gh-cached](https://github.com/TomzxCode/ghx) was replaced by [ghx](https://github.com/TomzxCode/ghx) and removed, with every skill reference switched over.
The `dot-claude` directory was renamed to `agents`.
The AGENTS.md vocabulary now avoids "shape", "honest", and "load bearing".
SDLC status pages went mobile-friendly.

**Experimenting with article-to-video.**
I started generating short videos from the articles I write, to post on YouTube and TikTok.
The pipeline combines text-to-speech narration with visuals that follow the article's content.
The experiment is early, but it's a plausible way to reach a wider audience with the ideas I've been working through.

**Resolved from last month.**
Scheduled issue-to-PR automation ([#8](https://github.com/tomzx/agents/issues/8)) and automatic context clearing between execution and review ([#9](https://github.com/tomzx/agents/issues/9)) both landed through llm-augmented-workflows.
The automation was generalized beyond OpenChamber, and the context clearing came free because each phase runs in its own session.
Skill usage tracking ([#7](https://github.com/tomzx/agents/issues/7)) is handled after I extended [agentsview](https://github.com/kenn-io/agentsview) to collect skill-usage statistics from its SQLite database.
Because the data is queryable, an agent can search session logs for skill calls and extract which skill ran, and the same approach works across every harness agentsview supports.
Reliable bug reproduction comments ([#10](https://github.com/tomzx/agents/issues/10)) are handled by llm-augmented-workflows, which can enforce an expected outcome and, when the agent doesn't deliver it, resume the last session and ask again.
The llm-augmented-workflows flexibility rework is done.
I've also fully switched to opencode, though support for other harnesses isn't there yet.

**Partial progress.**
The SDLC status report got significant improvements, but a status script in [TomzxCode/sdlc](https://github.com/TomzxCode/sdlc) now duplicates the report and drifts out of sync with the agents-repo skill.
Loops only run at the start and end of day, week, and month so far.
The lowest-hanging fruit I haven't picked is auto-running [validate-pr](https://github.com/tomzx/agents/blob/main/skills/validate-pr/SKILL.md), [verify-pr](https://github.com/tomzx/agents/blob/main/skills/verify-pr/SKILL.md), and [review-pr](https://github.com/tomzx/agents/blob/main/skills/review-pr/SKILL.md) on PRs waiting on me.
And validation of other people's changes is now covered by validate-pr and verify-pr, but for my own changes I still default to manual testing instead of delegating to an agent.

## What I Currently Need

**Five needs from earlier months are still open.**

- [Memory that agents manage automatically](https://github.com/tomzx/agents/issues/6), which I keep delaying for reasons I can't pin down.
- The [accuracy pass on daily summaries](https://github.com/tomzx/agents/issues/5), where nothing has moved.
- [Contextual Slack support](https://github.com/tomzx/agents/issues/4), which still has no workflow.
- [Automated triage follow-up conversations](https://github.com/tomzx/agents/issues/14), untouched because I rarely use that skill.
- Routines and event-driven triggering, still unstarted.

**Clarity on verdict propagation.**
I need to confirm how a verdict (approve, reject, needs-changes) made at one stage propagates to downstream stages.
Until I can trust that the right decision always carries forward, I can't confidently run the autonomous path without a human checking each handoff.

**A full pass on flow definitions.**
The flow definitions still have issues I haven't fully mapped.
I need a round of end-to-end testing to find where the definitions diverge from intended behavior, so the defects get fixed rather than worked around.

**A faster path to implementation.**
For feature work, I need to figure out which SDLC steps can be safely skipped or compressed to reach implementation faster.
The full chain is thorough but slow, and it's still unclear which steps are essential and which are ceremonial.

**State tracking for an orchestrator-only llm-augmented-workflows.**
Resolving the context-clearing need surfaced a bigger question: the engine could run as its own orchestrator instead of always anchoring on a GitHub issue.
The blocker is that without an issue to hold state, the engine needs another way to track where a run is, and I haven't decided what that state store should be.

**A set of PDLC skills, mirroring the SDLC ones.**
At work I'm spending a meaningful share of my time on product management work, and I want the same repeatability there that the SDLC skills give to engineering.
I need a structured set of product development lifecycle skills for discovery, framing, prioritization, and measurement, so the product side gets done properly and the same way every time rather than ad hoc.

## See also

- [What I've built and what I need: June 2026](../2026-06/index.md) - the previous entry in this series; July builds directly on its open needs.
- [The Self-Evolving Repository](../../the-self-evolving-repository/index.md) - the broader vision of automating a GitHub project end to end with LLMs that llm-augmented-workflows is now realizing.
- [Loops as Files](../../loops-as-files/index.md) - the scheduling layer that runs skills unattended, which underpins daily runs like resolve-pr-conflicts.
- [The Importance of Context When Interacting with LLMs](../../the-importance-of-context-when-interacting-with-llms/index.md) - why isolating context between phases matters, the problem the per-session design solves.

## References

- [llm-augmented-workflows](https://github.com/TomzxCode/llm-augmented-workflows) - the engine driving the issue-to-PR pipeline described throughout.
- [agents](https://github.com/tomzx/agents) - the skill library where the SDLC refactor, validation rework, and new skills landed.
- [agentsview](https://github.com/kenn-io/agentsview) - the session archive extended to track skill usage across harnesses.
- [TomzxCode/sdlc](https://github.com/TomzxCode/sdlc) - the static SDLC status pages, whose report script now overlaps the agents-repo skill.
- [github-board](https://github.com/TomzxCode/github-board) - the frontend-only issue and PR board view shipped this month.
- [ghx](https://github.com/TomzxCode/ghx) - the GitHub CLI that replaced gh-cached across the skill library.
