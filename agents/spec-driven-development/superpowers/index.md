---
title: Superpowers
created: 2026-10-09
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, methodology, agent-skills, worktrees, open-source]
readability: 3
audience_notes: >
  Engineers choosing a spec-first process layer and wondering what the movement's largest adoption figure actually is.
  Assumes you know what a skill, a subagent, and a git worktree are.
---

Superpowers is Jesse Vincent and Prime Radiant's complete software development methodology for coding agents, distributed as composable skills that trigger automatically and walk every build from a teased-out spec through plan, TDD, per-task subagent review, and branch cleanup.

**Superpowers carries the category's largest single adoption figure, about 296.7k stars, more than double Spec Kit's, and it bought that with the strictest position in the movement: the workflows are mandatory, not suggestions, and the cost is paid in tokens up front.**

## What it is

An MIT-licensed skills-and-plugin suite installed per harness (16 documented installs, from Claude Code, Codex, Cursor, and Gemini CLI to OpenCode, Pi, Kimi Code, and Muse), most often through each harness's official plugin marketplace.
A session-start bootstrap injects a `using-superpowers` skill that makes the agent check for relevant skills before any task, so the process starts from the first message.
The core loop runs brainstorming (the spec is teased out in chunks short enough to read), an isolated git worktree, a plan written for "an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing", then subagent-driven development or inline execution with a fresh review at the end.
Test-driven development is enforced with teeth: the skill's rule is red-green-refactor, and code written before its test gets deleted.
Prime Radiant, the applied research lab behind it, sells commercial support, additional tooling, and managed spending, and publishes the behavioral eval lab the skills are tested against.

## Status

Large, active, and distribution-backed in a way no other column is.
As of 2026-10-09: 296,692 stars, 26,498 forks, 323 open issues and pull requests, created 2025-10-09, pushed 2026-10-09, MIT, newest release v6.4.2 (2026-09-25).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=obra/superpowers&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=obra/superpowers&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=obra/superpowers&type=date&theme=dark&legend=top-left" />
</picture>

**Its launch thread is the largest independent discussion in this category: 435 points and 219 comments in October 2025, with substantive skepticism about the cost of the ceremony alongside the recommendations.**
Unlike every other column here, it reached that scale through harness marketplaces (Anthropic's official plugin marketplace among them) rather than a standalone CLI.
It entered this category's scan as a Development Frameworks entry on the Engineering4AI awesome list.

## Strengths

- Enforcement is structural: the bootstrap makes the agent consult its skills before every task, so the spec-first loop does not depend on the model remembering to follow a convention.
- The TDD gate is the category's only one with a stated deletion rule, and per-task fresh-context subagent review plus a two-stage check (spec compliance, then code quality) gives the oversight teeth.
- It is the only column tested against its own public behavioral eval lab (superpowers-evals), which grades harness compliance across Claude, Codex, Gemini, and Kimi CLI runs.
- One skill set covers 16 harnesses, the widest documented install surface in this category.

## Cautions

- **The steward's own 6.4 release concedes the trade: building without Superpowers is faster and cheaper, and the claim is only that builds with it are significantly buggier per their evals, so the price of the method is measured in tokens and hours.**
- Ceremony sizing is absent by design; the brainstorm-plan-worktree loop fires on every build the way spec-kit's fixed ceremony does, with less negotiation than a profile system offers.
- Company stewardship with support as the business model, plus a disclosed telemetry default (the visual companion's logo fetch reports the version in use, opt-out via `SUPERPOWERS_DISABLE_TELEMETRY`).
- New skills from outside are generally not accepted, so the method's content is curated by one company even though the code is open.

## Pricing

Free and open source under MIT.
Prime Radiant sells commercial support, additional tooling, and managed spending by contact, with no published tiers as of 2026-10-09.

## Compared to

- [cc-sdd](../cc-sdd/index.md): both install spec-first workflows as skills across many agents; cc-sdd routes ceremony through discovery and closes with a GO/NO-GO verdict, Superpowers fixes the loop and enforces TDD inside it.
- [GSD](../gsd/index.md): the other subagent-quarantine loop; GSD is community-run after its founder's controversy, Superpowers is company-run by its still-active founder with an eval suite to check the claims against.
- [GitHub Spec Kit](../spec-kit/index.md): the neutral scaffolding alternative; Spec Kit waits to be invoked, Superpowers takes over the session from the first message.

## Bottom line

**Recommended for engineers who want the process enforced rather than suggested, and who accept paying a measured token-and-time premium for the bug-rate reduction the evals claim.**
Not for anyone who needs ceremony sized to the change, and not for anyone whose workflow cannot carry a company-curated skill set.
The disagreeable claim I will defend: 296.7k stars for a mandatory methodology is evidence that most developers did not want to choose their process per task, they wanted it imposed, and every column in this category that negotiates ceremony is swimming against that finding.

## Changes

- 2026-10-09 - Created from the Engineering4AI awesome-list entrant scan, profiling obra/superpowers as the category's mandatory-workflow skill suite and its largest single adoption figure.

## See also

- [Jesse Vincent](../../people-and-publications/jesse-vincent/index.md) - the steward the section already profiles, with the eval record and the token-cost lament in his own words
- [cc-sdd](../cc-sdd/index.md) - the other skill-installed spec workflow, the nearest structural neighbor
- [GSD](../gsd/index.md) - the other fresh-context-subagent loop
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/obra/superpowers - repository: workflow, harness table, philosophy, licensing (296,692 stars as of 2026-10-09)
- https://raw.githubusercontent.com/obra/superpowers/main/README.md - the seven-skill core loop, 16 harness installs, contribution policy, and telemetry disclosure
- https://api.github.com/repos/obra/superpowers - stars, forks, issues, dates, and MIT as of 2026-10-09
- https://github.com/prime-radiant-inc/superpowers-evals - the public behavioral eval lab grading harness compliance
- https://blog.fsck.com/2025/10/09/superpowers/ - the release announcement and the skills-are-mandatory philosophy
- https://blog.fsck.com/2026/09/21/superpowers-6.4/ - the 6.4 release and the bare-metal faster-and-cheaper concession
- https://news.ycombinator.com/item?id=45547344 - the 435-point, 219-comment launch thread, the category's largest independent discussion
