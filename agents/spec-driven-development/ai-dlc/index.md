---
title: AI-DLC
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, sdlc, multi-agent, workflow, open-source]
readability: 3
audience_notes: >
  Engineers choosing a whole-lifecycle process layer for AI coding agents and wondering what AWS's own methodology looks like as running code.
  Assumes you know what an approval gate and an audit trail are.
---

AI-DLC is AWS Labs' harness-neutral implementation of the AI-Driven Development Life Cycle: one methodology core, installed by a native CLI, that runs a gated, audited, 5-phase delivery workflow natively inside seven coding agents.

**AI-DLC is the only member of this category backed by a cloud vendor's methodology org, and that is both its distribution advantage and its conflict: the reference implementation of a vendor's process is also a path toward that vendor's runtime.**

## What it is

A MIT-0 repository and `aidlc` installer (no Bun or Node required) that packages one hand-authored methodology core into per-harness runtimes for Claude Code, Kiro CLI, Kiro IDE, Codex CLI, Cursor, opencode, and GitHub Copilot; you invoke `/aidlc <request>` and the engine routes it into one of 11 workflow profiles.
The workflow spans 5 phases and 33 stages from initialization through operation, worked by 14 agents (11 domain experts, 2 reviewers, and an adaptive composer), stopping at human approval gates and recording a 113-event audit trail with persistent state and learned team rules.
The methodology behind the repo comes from AWS principal solutions architect Raja SP (blog post July 31, 2025): AI plans and asks, humans decide, teams elaborate together ("Mob Elaboration"), and sprints become "bolts" measured in hours or days.
Amazon's own docs position it as the successor to retrofitting AI onto human processes, and the repo's provider story quietly favors the house: `aidlc config providers` can apply Amazon Bedrock settings, and Kiro needs no provider answer because model access comes with Kiro.

## Status

Large and fast-moving for an eighteen-month-old methodology repo.
As of 2026-10-06: 5,002 stars, 910 forks, 334 open issues, created 2025-11-13, pushed 2026-10-06, stable release v2.10.0 with near-daily v2.10.1-preview builds, MIT-0 licensed, documented at [awslabs.github.io/aidlc-workflows](https://awslabs.github.io/aidlc-workflows/).

[![Star History Chart](https://api.star-history.com/chart?repos=awslabs/aidlc-workflows&type=date&legend=top-left)](https://www.star-history.com/?repos=awslabs%2Faidlc-workflows&type=date&legend=top-left)

<a href="https://www.star-history.com/?repos=awslabs%2Faidlc-workflows&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=awslabs/aidlc-workflows&type=date&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=awslabs/aidlc-workflows&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=awslabs/aidlc-workflows&type=date&legend=top-left" />
 </picture>
</a>

**Its Hacker News footprint is thin (the methodology's threads run 2 to 5 points), so adoption signals rest on the star count and AWS's institutional push rather than independent discussion.**

## Strengths

- The only column here that spans the whole lifecycle, requirements through operations, instead of stopping at tasks or specs.
- Approval gates and a 113-event audit trail are engine features, not conventions, so the gates hold across every supported harness the same way.
- One methodology core with generated per-harness runtimes means a team on mixed agents runs one process, the same bet Spec Kit makes with more machinery.
- Workflow profiles (Classic, Express, and focused variants for bugs, infrastructure, security, proofs of concept) size the ceremony without dropping the gates.

## Cautions

- The vendor conflict is structural: the methodology's distribution runs through AWS surfaces, the recommended model is Claude Opus 4.8 via your harness, and Bedrock and Kiro get first-class provider treatment.
- The sharpest critique (Will Mitchell, ex-Dropbox and Asana) argues AI-DLC solves the wrong bottleneck: when code is fast, the constraints move to user understanding, validation, and stakeholder alignment, none of which the lifecycle touches.
- The vocabulary is a moat and a cost: bolts, units of work, Mob Elaboration, and 33 named stages mean substantial retraining, the same adoption-price objection BMad carries.
- "Thought-terminating cliché" is the critic's phrase for the pitch that old processes must be discarded wholesale, and the 33-stage machinery is exactly what that critique predicts.

## Pricing

Free and open source under MIT-0.
No paid tier exists; model costs follow your harness and provider.

## Compared to

- [BMad Method](../bmad-method/index.md): the other whole-method column; BMad is community-owned and right-sizes by design, AI-DLC is vendor-backed and sizes through profiles while keeping all 33 stages available.
- [GitHub Spec Kit](../spec-kit/index.md): both are harness-neutral process layers; Spec Kit scaffolds markdown conventions, AI-DLC runs a stateful engine with gates and audit evidence.
- [GSD](../gsd/index.md): the other multi-runtime loop; GSD keeps one operator and quarantines context in subagents, AI-DLC orchestrates a 14-agent cast around human gates.

## Bottom line

**Recommended for teams that want a whole-lifecycle, gate-enforced process that runs identically across several agents, and that accept learning AWS's vocabulary and noticing where the exits lead back to AWS.**
Not for solo work, and not for anyone who wants a process layer with no vendor's fingerprints on it.

## Changes

- 2026-10-06 - Created from the entrant-resolution run, profiling awslabs/aidlc-workflows as the category's first vendor-backed whole-lifecycle column.
- 2026-10-07 - Added the awslabs/aidlc-workflows star history chart to the Status section.

## See also

- [Kiro](../../surfaces/kiro/index.md) - the AWS spec-first IDE and CLI AI-DLC integrates with natively
- [BMad Method](../bmad-method/index.md) - the community-owned whole-method alternative
- [GitHub Spec Kit](../spec-kit/index.md) - the harness-neutral scaffolding alternative
- [GSD](../gsd/index.md) - the single-operator multi-runtime loop

## References

- https://github.com/awslabs/aidlc-workflows - repository, README: profiles, phases, agents, audit trail, harness table (5,002 stars as of 2026-10-06)
- https://raw.githubusercontent.com/awslabs/aidlc-workflows/main/README.md - the installer, harness runtimes, and provider story
- https://awslabs.github.io/aidlc-workflows/ - the documentation site: guides, stage reference, agent deep dives
- https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/ - the methodology announcement by Raja SP, July 31, 2025
- https://wakamoleguy.com/p/ai-dlc-solves-wrong-bottleneck - the critical essay on where the bottleneck actually sits, fetched 2026-10-06
- https://hn.algolia.com/api/v1/search?query=AI-DLC&tags=story - the thin HN footprint, threads at 2 to 5 points
