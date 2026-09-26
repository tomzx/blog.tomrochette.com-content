---
title: GSD
created: 2026-09-16
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, context-engineering, workflow, open-source]
readability: 3
audience_notes: >
  Engineers choosing a spec-driven workflow system for their coding agent and wondering what happened to the 64k-star get-shit-done repository.
  Assumes you know what a slash command and a phase loop are.
---

GSD (Get Shit Done) is the MIT meta-prompting, context-engineering, and spec-driven workflow system for Claude Code created by Lex Christopherson (TÂCHES), whose roughly 64.5k-star original repository is archived and whose development continues as the community-run open-gsd/gsd-core.

**GSD is the cautionary lineage of the spec-driven movement: the most-starred workflow system in this category died with its creator's controversy, and the successor is one maintainer's attempt to keep the loop while returning the work to the people who show up.**

## What it is

An npm-installed command-and-prompt framework (originally the `get-shit-done-cc` package, now `@opengsd/gsd-core`) that drives coding agents through a five-step phase loop per milestone: discuss, plan, execute, verify, ship.
Its context-engineering thesis is that heavy research, planning, and execution run in fresh-context subagents while the main session stays lean, with structured artifacts such as STATE.md and CONTEXT.md surviving session boundaries.
The original targeted Claude Code; the successor's installer covers Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, and Windsurf, with 65-plus slash commands documented.
Open GSD has grown an ecosystem around the loop: gsd-pi (a standalone harness), gsd-browser (CDP-based verification evidence), gsd-graph, and gsd-loop, with desktop and cloud surfaces listed as coming soon.

## Status

Split between a dead root and a live successor.
The original gsd-build/get-shit-done is archived at 64,462 stars and 5,443 forks, last pushed 2026-05-31, with its README now a redirect notice to open-gsd/gsd-core.
The successor, created 2026-05-22, is actively developed: 9,827 stars, 706 forks, pushed 2026-09-25, release v1.14.0 on 2026-09-14, and 40,895 npm downloads last month for @opengsd/gsd-core, while the legacy get-shit-done-cc package still records 48,374.
**The transition was not clean: Blake Watson's widely-linked build story added a 2026-07-31 update telling readers not to install the original, reporting that people say a crypto scam took place around the creator, and naming OpenGSD the consensus successor.**
Open GSD's own origin page confirms the chapter without specifics, stating trust was damaged, people were hurt, public channels disappeared, and crediting Christopherson with the original idea.

## Strengths

- The fresh-context subagent loop is the most explicit context-rot answer in this category, predating several tools that now market the same idea.
- One installer covers ten runtimes, and the docs site is the category's most complete (tutorials, how-to guides, reference, explanation).
- Brownfield is first-class: /gsd-onboard for existing repos sits beside /gsd-new-project.
- The verify step walks through what was built before a phase is declared done, and gsd-browser adds deterministic browser evidence when the work needs it.

## Cautions

- **The founder catastrophe is the caution: whatever the exact events, the category's most-starred workflow system is archived, its successor holds about 15 percent of the original's star count, and trust in the lineage is still being rebuilt by a steward months into the job.**
- The Hacker News footprint is thin: the project's own submission drew 2 points in January 2026, the largest thread (a 24-point accessibility build story, February 2026) is a personal narrative, and I found no substantive skeptical discussion of the framework itself on HN, which means the community record neither damns nor validates the loop.
- The five-step loop repeats per milestone whatever the change's size, so small changes pay full ceremony unless you drop to the lighter quick-task mode.
- Core-loop verification is a human walk-through; the machine-checkable evidence lives in a separate product rather than the framework.

## Pricing

Free and open source under MIT, both the archived original (copyright Lex Christopherson) and the successor (copyright Open GSD).
No paid tier exists today; the coming gsd-cloud is listed as a hosted surface without published pricing.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): the movement's root by stewardship and adoption; Spec Kit scaffolds artifact conventions for a heterogeneous org, GSD runs an opinionated loop with subagent context hygiene.
- [OpenSpec](../openspec/index.md): the delta-ledger alternative; OpenSpec versions the spec itself, GSD versions milestone state.
- [BMad Method](../bmad-method/index.md): the other whole-method bet; BMad sizes ceremony to the change and adds roles, GSD fixes the loop and keeps a single operator.

## Bottom line

**Recommended for engineers who want a disciplined phase loop that quarantines heavy work in fresh-context subagents, and who accept adopting a project whose governance is weeks old.**
Not for anyone who needs the community's trust problems fully in the past, or who wants ceremony right-sized per change out of the box.
The disagreeable claim I will defend: 64,462 stars is the strongest evidence the discuss-plan-execute-verify-ship loop works, and the same number is now the category's loudest warning that a workflow system dies with its steward's credibility, not with its code.

## Changes

- 2026-09-16 - Created.
- 2026-09-25 - Refreshed counts (archived original at 64,462 stars, successor at 9,827) and corrected the successor's share to about 15 percent.

## See also

- [GitHub Spec Kit](../spec-kit/index.md) - the movement root GSD sits alongside
- [OpenSpec](../openspec/index.md) - the delta-ledger alternative
- [BMad Method](../bmad-method/index.md) - the method-heavy counterpart
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map tracking these workflow systems

## References

- https://github.com/open-gsd/gsd-core - successor README: the loop, installer, runtimes, docs structure
- https://api.github.com/repos/open-gsd/gsd-core - successor stars, forks, push date, MIT as of 2026-09-21
- https://api.github.com/repos/gsd-build/get-shit-done - the archived original: 64,462 stars, last push 2026-05-31
- https://github.com/gsd-build/get-shit-done - the redirect README naming gsd-core the continuation
- https://opengsd.net - the ecosystem site and product family
- https://opengsd.net/origin - the origin-credit page acknowledging the broken chapter
- https://opengsd.net/promise - the successor's operating principles and steward
- https://docs.opengsd.net/ - the documentation: three tools, 65-plus commands
- https://blakewatson.com/journal/i-used-claude-code-and-gsd-to-build-the-accessibility-tool-ive-always-wanted/ - the firsthand account and its 2026-07-31 do-not-install update, the critical source
- https://news.ycombinator.com/item?id=47086847 - the largest GSD thread, 24 points, February 2026
- https://api.npmjs.org/downloads/point/last-month/@opengsd/gsd-core - 40,895 downloads last month
