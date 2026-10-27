---
title: Superpowers
created: 2026-10-09
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, methodology, agent-skills, worktrees, open-source]
readability: 3
audience_notes: >
  Engineers choosing a spec-first process layer and wondering what the movement's largest adoption figure actually is.
  Assumes you know what a skill, a subagent, and a git worktree are.
---

Superpowers is Jesse Vincent and Prime Radiant's complete software development methodology for coding agents, distributed as composable skills that trigger automatically and walk every build from a teased-out spec through plan, TDD, per-task subagent review, and branch cleanup.

**Superpowers carries the category's largest single adoption figure, about 299k stars as of 2026-10-14 and by its steward's count about to cross 300k, more than double Spec Kit's, and it bought that by making the workflow mandatory from session start, a position 7.0 softened at the edges by rebuilding brainstorming to size the ceremony to the work.**

## What it is

An MIT-licensed skills-and-plugin suite installed per harness (16 documented installs, from Claude Code, Codex, Cursor, and Gemini CLI to OpenCode, Pi, Kimi Code, and Muse), most often through each harness's official plugin marketplace.
A session-start bootstrap injects a `using-superpowers` skill that makes the agent check for relevant skills before any task, so the process starts from the first message.
The core loop runs brainstorming (the spec is teased out in chunks short enough to read), an isolated git worktree, a plan written for "an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing", then subagent-driven development or inline execution with a fresh review at the end.
Test-driven development is enforced with teeth: the skill's rule is red-green-refactor, and code written before its test gets deleted.
Prime Radiant, the applied research lab behind it, sells commercial support, additional tooling, and managed spending, and publishes the behavioral eval lab the skills are tested against.

## Status

Large, active, and distribution-backed in a way no other column is.
As of 2026-10-14: 298,672 stars, 26,695 forks, 328 open issues and pull requests, created 2025-10-09, pushed 2026-10-23, MIT, newest release v7.0.1 (2026-10-21).
v7.0.0 shipped on the project's first anniversary with a rebuilt brainstorming skill that sizes the process to the work, running a quick task immediately, agreeing a small change in chat, or writing a full design document, and it replaces the spec-document reviewer with a builder check that reads the design as the person who will build it.
v7.0.1 retuned that rebuild after users called the new questions formulaic: brainstorming now digs for context before it asks anything, lays out the approaches and writes the design doc before building (in the steward's own test, it skipped the doc unprompted in 24 of 24 runs before the fix and 3 of 24 after), three long skills were trimmed to survive Claude Code's 20,000-character compaction cutoff, and the contribution rules now require a human-written summary and refuse agent-written PRs that fix someone else's issue.
The steward's anniversary post reports the repo about to cross 300,000 stars (12th most starred project on GitHub by his count), the number-one third-party Claude Code plugin at more than 1.1M installs, and 50M clones every two weeks from 1.95M unique IPs.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=obra/superpowers&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=obra/superpowers&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=obra/superpowers&type=date&legend=top-left" />
</picture>

**Its launch thread is the largest independent discussion in this category: 435 points and 231 comments since October 2025, with substantive skepticism about the cost of the ceremony alongside the recommendations.**
Unlike every other column here, it reached that scale through harness marketplaces (Anthropic's official plugin marketplace among them) rather than a standalone CLI.
It entered this category's scan as a Development Frameworks entry on the Engineering4AI awesome list.

## Strengths

- Enforcement is structural: the bootstrap makes the agent consult its skills before every task, so the spec-first loop does not depend on the model remembering to follow a convention.
- The TDD gate is the category's only one with a stated deletion rule, and per-task fresh-context subagent review plus a two-stage check (spec compliance, then code quality) gives the oversight teeth.
- It is the only column tested against its own public behavioral eval lab (superpowers-evals), which grades harness compliance across Claude, Codex, Gemini, and Kimi CLI runs.
- One skill set covers 16 harnesses, the widest documented install surface in this category.

## Cautions

- **The steward's own 6.4 release concedes the trade: building without Superpowers is faster and cheaper, and the claim is only that builds with it are significantly buggier per their evals, so the price of the method is measured in tokens and hours.**
- Ceremony sizing is the agent's call, not a mode you pick: brainstorming sizes the work as of 7.0, but you negotiate by overriding its judgment rather than by choosing a ceremony level up front, and the skills still fire on every build by default.
- The coverage is the inner build loop, and the community's loudest ask (multi-agent team execution) is still not in the box, per the competitor-published three-way comparison.
- The one controlled head-to-head published so far (a single task, competitor-adjacent) found it slower to first code but stronger on up-front reasoning, so the token premium buys thought before code rather than speed.
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
Not for anyone who wants to set the ceremony level themselves rather than override the agent's sizing, and not for anyone whose workflow cannot carry a company-curated skill set.
The disagreeable claim I will defend: 297k stars for a mandatory methodology is evidence that most developers did not want to choose their process per task, they wanted it imposed, and every column in this category that negotiates ceremony is swimming against that finding.

## Changes

- 2026-10-09 - Created from the Engineering4AI awesome-list entrant scan, profiling obra/superpowers as the category's mandatory-workflow skill suite and its largest single adoption figure.
- 2026-10-10 - Recorded the v7.0.0 anniversary release (rebuilt brainstorming that sizes the process to the work, the builder check replacing the spec-document reviewer), the steward's 300k-star and 1.1M-install claims, the three-way comparison and its head-to-head, and refreshed counts.
- 2026-10-23 - Rotation re-verification of every cited source and recorded the v7.0.1 release (2026-10-21): the brainstorming retune after the formulaic-questions feedback, the design-doc-before-building fix (24 of 24 unprompted skips down to 3 of 24), the 20,000-character compaction trims, and the human-written-summary contribution rule.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart light-source markup (the light source carried the dark-theme parameter; it now points at the default chart).

## See also

- [Jesse Vincent](../../people-and-publications/jesse-vincent/index.md) - the steward the section already profiles, with the eval record and the token-cost lament in his own words
- [cc-sdd](../cc-sdd/index.md) - the other skill-installed spec workflow, the nearest structural neighbor
- [GSD](../gsd/index.md) - the other fresh-context-subagent loop
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/obra/superpowers - repository: workflow, harness table, philosophy, licensing (298,672 stars as of 2026-10-14)
- https://raw.githubusercontent.com/obra/superpowers/main/README.md - the seven-skill core loop, 16 harness installs, contribution policy, and telemetry disclosure
- https://api.github.com/repos/obra/superpowers - stars, forks, issues, dates, and MIT as of 2026-10-23
- https://raw.githubusercontent.com/obra/superpowers/main/RELEASE-NOTES.md - the release notes through v7.0.1, grounding the rebuilt brainstorming, the builder check, and the retune
- https://blog.fsck.com/2026/10/09/what-a-year/ - the anniversary post grounding the 7.0 framing and the 300k-star, 1.1M-install, and clone-volume claims
- https://primeradiant.com/claude-plugin-stats/ - the steward's tracker of Anthropic's plugin-stats feed behind the 1.1M-install figure
- https://raw.githubusercontent.com/addyosmani/agent-skills/main/docs/comparison.md - the three-way comparison and its linked single-task head-to-head, the newest critical source
- https://github.com/prime-radiant-inc/superpowers-evals - the public behavioral eval lab grading harness compliance
- https://blog.fsck.com/2025/10/09/superpowers/ - the release announcement and the skills-are-mandatory philosophy
- https://blog.fsck.com/2026/09/21/superpowers-6.4/ - the 6.4 release and the bare-metal faster-and-cheaper concession
- https://news.ycombinator.com/item?id=45547344 - the 435-point, 219-comment launch thread, the category's largest independent discussion
