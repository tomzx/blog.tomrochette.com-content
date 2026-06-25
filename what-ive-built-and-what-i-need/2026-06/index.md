---
title: "What I've built and what I need: June 2026"
created: 2026-06-25
type: post
status: finished
tags: [personal-update, skills, ai, automation, fully-ai-generated, llm=glm-5.1, llm-glm-5.2]
readability: 3
---

Over the month since May, the [agents](https://github.com/tomzx/agents) repository evolved from building the SDLC pipeline into a mature, self-improving system.
The biggest shift was adding verification and consistency tooling, introducing stateful SDLC tracking, and standardizing conventions across the skill library.

## What I Have Been Working On

**Added verification and consistency tooling.**
The latter half of the month focused on checking the system's own work.
[validate-pr](https://github.com/tomzx/agents/blob/main/skills/validate-pr/SKILL.md) runs runtime validation of PRs, checking out a branch, building it, and proving every claim in the PR description through execution.
[verify-pr](https://github.com/tomzx/agents/blob/main/skills/verify-pr/SKILL.md) performs static code inspection covering quality, correctness, and architecture alignment.
[backpropagate-sdlc](https://github.com/tomzx/agents/blob/main/skills/backpropagate-sdlc/SKILL.md) walks the SDLC artifact chain in reverse, from code back to issue, to verify end-to-end traceability and detect drift accumulated across phases.
[sync-repository](https://github.com/tomzx/agents/blob/main/skills/sync-repository/SKILL.md) ensures the entire repository stays consistent across SDLC, code, tests, documentation, types, and observability.
[improve-autonomy](https://github.com/tomzx/agents/blob/main/skills/improve-autonomy/SKILL.md) assesses what would be needed to run a session fully autonomously end to end.

**Overhauled the SDLC infrastructure.**
The old bootstrap-sdlc was replaced by [sync-sdlc](https://github.com/tomzx/agents/blob/main/skills/sync-sdlc/SKILL.md), which reconciles the codebase with the `.sdlc/` directory instead of just bootstrapping it.
A new `.sdlc/state.yml` file in worktrees tracks the current phase, GitHub reference, and feature, giving skills persistent context across invocations.
The [sdlc-status](https://github.com/tomzx/agents/blob/main/skills/sdlc-status/SKILL.md) skill was extracted and heavily improved through multiple iterations, adding vocabulary tooltips, open questions, and a footer.
Observability and telemetry phases were added to the SDLC pipeline, extending coverage from needs assessment through deployment and retrospective.
[qualify-issue](https://github.com/tomzx/agents/blob/main/skills/qualify-issue/SKILL.md) drives a multi-round Q&A loop to gather enough information before requirements, while [create-feasibility](https://github.com/tomzx/agents/blob/main/skills/create-feasibility/SKILL.md) / [review-feasibility](https://github.com/tomzx/agents/blob/main/skills/review-feasibility/SKILL.md) and [create-existing-solutions](https://github.com/tomzx/agents/blob/main/skills/create-existing-solutions/SKILL.md) / [review-existing-solutions](https://github.com/tomzx/agents/blob/main/skills/review-existing-solutions/SKILL.md) assess viability and survey prior art before committing to a build.
[fix-issue](https://github.com/tomzx/agents/blob/main/skills/fix-issue/SKILL.md) orchestrates a bug fix end to end by delegating to reproduce-issue, create-implementation, and create-pr.
Post-merge coverage extends through [deploy-pr](https://github.com/tomzx/agents/blob/main/skills/deploy-pr/SKILL.md) and [observe-production](https://github.com/tomzx/agents/blob/main/skills/observe-production/SKILL.md), which deploy changes and verify SLOs and error rates in production.
Production health is planned from the start with [create-observability](https://github.com/tomzx/agents/blob/main/skills/create-observability/SKILL.md) / [review-observability](https://github.com/tomzx/agents/blob/main/skills/review-observability/SKILL.md) / [audit-observability](https://github.com/tomzx/agents/blob/main/skills/audit-observability/SKILL.md) and [create-telemetry](https://github.com/tomzx/agents/blob/main/skills/create-telemetry/SKILL.md) / [review-telemetry](https://github.com/tomzx/agents/blob/main/skills/review-telemetry/SKILL.md), which define logging, metrics, tracing, alerting, and analytics events for each feature.
Cross-skill conventions were consolidated into a shared references file, and per-repository AGENTS.md overrides can now be stored under `repositories/` for project-specific instructions.
SDLC artifacts produced by the skills across projects I contribute to or monitor are tracked in a dedicated [sdlc](https://github.com/TomzxCode/sdlc) repository.
That repository includes automation to generate static HTML status pages from the output of the [sdlc-status](https://github.com/tomzx/agents/blob/main/skills/sdlc-status/SKILL.md) skill, and each project's artifacts are reviewed weekly by [sync-sdlc](https://github.com/tomzx/agents/blob/main/skills/sync-sdlc/SKILL.md) to detect and correct drift.

**Shipped 7 maintenance skills for code quality.**
A new "maintenance" skill category was added covering security auditing, code duplication detection, type gap analysis, churn analysis, and related diagnostics.
These were integrated into the SDLC pipeline as a structured diagnose-harden-clean-document workflow, giving every feature a code health pass alongside the existing requirements-to-learnings flow.

**Polished PR and issue workflows.**
Issue triage gained duplicate detection and smarter label management, and triage-issue was split out from triage-issues for single-issue versus batch processing.
The [ghx](https://github.com/TomzxCode/ghx) CLI was introduced and integrated into the review and feedback skills, adding inline PR review comments, pending reviews, and comment stashing that the standard `gh` CLI does not support.
Reversibility checks were added across review-* skills, and forward compatibility checks were introduced.
[create-issue](https://github.com/tomzx/agents/blob/main/skills/create-issue/SKILL.md) had its duplicate checking restored and time estimates improved.
A new `automate-session` skill was added to identify repetitive workflows worth encoding as skills.

**Added new lifecycle and utility skills.**
[assess-needs](https://github.com/tomzx/agents/blob/main/skills/assess-needs/SKILL.md) and [review-needs-assessment](https://github.com/tomzx/agents/blob/main/skills/review-needs-assessment/SKILL.md) evaluate whether a feature addresses a genuine need before investing in feasibility or requirements.
[research-article](https://github.com/tomzx/agents/blob/main/skills/research-article/SKILL.md) maps the state of the art before writing, producing a research brief with organized sources.
[setup-docs-site](https://github.com/tomzx/agents/blob/main/skills/setup-docs-site/SKILL.md) scaffolds a MkDocs documentation site with a GitHub Actions publish workflow.
[vacation-handoff](https://github.com/tomzx/agents/blob/main/skills/vacation-handoff/SKILL.md) generates a pre-leave handoff covering deadlines, on-call coverage, and in-flight work.
[audit-attention](https://github.com/tomzx/agents/blob/main/skills/audit-attention/SKILL.md) analyzes how time splits between compounding and depreciating activities using the two-year test, suggesting what to delegate versus protect.
[write-message](https://github.com/tomzx/agents/blob/main/skills/write-message/SKILL.md) improves outgoing messages by removing negative tone and adding actionable suggestions.
[summarize-meeting](https://github.com/tomzx/agents/blob/main/skills/summarize-meeting/SKILL.md) produces a structured meeting summary from a transcript file.
[review-skills](https://github.com/tomzx/agents/blob/main/skills/review-skills/SKILL.md) and [compare-skills](https://github.com/tomzx/agents/blob/main/skills/compare-skills/SKILL.md) audit the skill library itself for duplicates, broken references, orphaned skills, and practices worth adopting from other libraries.

**Closed three of last month's needs.**
Replying to inline PR comments, listed as a need in May, is now fully integrated into the review and feedback skills via [ghx](https://github.com/TomzxCode/ghx).
Incremental PR description updates, also listed in May, are now handled by the [update-pr-description](https://github.com/tomzx/agents/blob/main/skills/update-pr-description/SKILL.md) skill, which makes minimal adjustments to the existing description after new commits rather than regenerating from scratch.
Bug reproduction now triggers automatically when the "bug" label is added to an issue via [reproduce-issue](https://github.com/tomzx/agents/blob/main/skills/reproduce-issue/SKILL.md), though commenting results back on the issue is still unreliable.

## What I Currently Need

From last month, the following are still needed in priority order: [scheduled issue-to-PR automation in OpenChamber](https://github.com/tomzx/agents/issues/8), [memory that agents manage automatically](https://github.com/tomzx/agents/issues/6), [accuracy pass on daily summaries](https://github.com/tomzx/agents/issues/5), and [automatic context clearing between execution and review](https://github.com/tomzx/agents/issues/9).

The new needs for this month:

**[Skill usage tracking](https://github.com/tomzx/agents/issues/7).**
I started using [agentsview](https://github.com/kenn-io/agentsview), which lets you filter conversation logs on terms.
Given a list of skill names over time, it is possible to filter on those names as long as they were not expanded.
OpenCode only expands slash commands if they start a message, so prefixing them with a space prevents auto-expansion and would allow tracking, but that is an ugly hack that needs a cleaner solution.

**[Contextual Slack support](https://github.com/tomzx/agents/issues/4).**
[slack-cached](https://github.com/TomzxCode/slack-cached) can already read Slack threads, and given the right working directory it may have enough relevant context to help users better than generic Q&A pairs.
What remains is wiring it into an actual support workflow.

**[Automate issue triage follow-up conversations](https://github.com/tomzx/agents/issues/14).**
The [triage-issues](https://github.com/tomzx/agents/blob/main/skills/triage-issues/SKILL.md) skill currently sends a single message when an issue is received.
If the user replies, no further LLM interaction happens.
The triage loop should continue the conversation until the issue is fully qualified.

**[Reliable bug reproduction comments](https://github.com/tomzx/agents/issues/10).**
The [reproduce-issue](https://github.com/tomzx/agents/blob/main/skills/reproduce-issue/SKILL.md) skill now triggers automatically when the "bug" label is added to an issue, but commenting the reproduction results back on the issue is unreliable and needs to be stabilized.

**Introduce loops to automate skill usage.**
As described in [Loops as Files](../loops-as-files/index.md), loops provide a scheduling layer that can run skills on a recurring basis without manual triggering.
Wiring skills into loops would enable workflows like automated issue triage, weekly repository syncs, and scheduled PR reviews to run unattended.

**Explore routines, habits, and event-driven skill triggering.**
Beyond loops, I want to investigate routines and event-driven triggers that fire skills when the right conditions occur.
As the skill library grows past 130 skills, some are never used simply because nothing is wired to invoke them, and connecting them to the right trigger or schedule would unlock work that currently goes undone.

**Improve the SDLC status report.**
As I work on large features, iterating involves back and forth between SDLC stages that requires changes to be backported and then forward propagated.
The [sdlc-status](https://github.com/tomzx/agents/blob/main/skills/sdlc-status/SKILL.md) report needs better content and visualization to make this flow visible and navigable.

**Reduce manual testing and validation.**
I spend too much time manually testing and validating that a feature works as expected.
The [improve-autonomy](https://github.com/tomzx/agents/blob/main/skills/improve-autonomy/SKILL.md) skill should help close this gap, but the challenge is behavioral: I instinctively revert to doing it myself instead of immediately asking how an agent could do what I am about to do.
