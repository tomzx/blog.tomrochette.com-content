---
title: GitHub Spec Kit
created: 2026-08-26
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, spec-driven-development, github, ai-agents]
readability: 3
audience_notes: >
  Engineers deciding whether to adopt a spec-first workflow before letting agents write code.
  Assumes you have used a coding agent on a real feature and know what a review gate is.
---

Spec Kit is GitHub's open-source toolkit for spec-driven development: a CLI that scaffolds constitution, spec, plan, and tasks files, then drives any of 30+ coding agents through implementing them.
Facts below verified as of 2026-08-26.

**Spec Kit hit 131k stars in one year by selling process, not product: it is markdown conventions plus a scaffolding CLI, and its popularity is the strongest signal yet that the industry wants review gates on agents more than it wants more agent autonomy.**

## What it is

**An MIT-licensed Python CLI (`specify`) plus slash-command and skills templates that work across 30+ agents, from Copilot and Claude Code to OpenCode and Cursor.**
The workflow runs in named steps: `/speckit-constitution` writes project principles once, then specify, plan, and tasks produce the artifacts, implement has the agent execute them, and converge checks the code back against the spec.
Extensions, presets, and role-based bundles let an organization customize the process without forking it.

## Status

**Active, and it just declared adulthood.**
First commit August 21, 2025; v1.0.0 and v1.0.1 both shipped August 21, 2026, with 131,489 stars and about 11.8k forks as of 2026-08-26.
The lead maintainer's anniversary post says the original creators have moved on to other projects and frames 1.0.0 as "just a number", arguing that as agents cheapen adaptation, value moves from stability to adaptability.

## Strengths

- **Agent-neutral by design**: the spec artifacts are plain markdown, so the process survives harness churn and works in a team running three different agents.
- The constitution step turns project principles into an artifact the agent re-reads, the same codification AGENTS.md does for rules.
- Converge closes the loop most workflows leave open, checking implementation against spec instead of trusting the agent's claim of done.
- The GitHub launch post, the docs, and the anniversary post are all primary and consistent, unusual candor for a vendor toolkit.

## Cautions

- **The waterfall critique is the real one**: a 225-point November 2025 essay argues SDD revives heavy up-front documentation and buries agility under markdown layers, and it is partly right about the failure mode (spec theater nobody reads).
- Specs are only as good as the human reviewing them; the toolkit enforces the ceremony, not the quality.
- Original creators gone at year one and the release philosophy explicitly de-emphasizes stability, so pin your version and expect the process vocabulary to drift.
- Star velocity reflects the movement's hype as much as the tool; the ecosystem it anchors (Kiro ports, Tessl, a dozen SDD CLIs) is bigger than what any one of them commands.

## Pricing

Free and open source, MIT.
There is no paid tier or hosted product, as of 2026-08-26.

## Compared to

- [Kiro](../kiro/index.md): spec-first as a closed IDE with metered credits versus a free process layered onto whatever agent you already run; Kiro for the integrated experience, Spec Kit for neutrality.
- Tessl: the third named pillar of the movement in the ecosystem writeups, a spec-driven platform rather than a toolkit; I have not verified it this run and profile it only when it gets its own note.
- Plain AGENTS.md: rules without a workflow; Spec Kit is what you reach for when rules alone stopped catching drift.

## Bottom line

**Recommended for teams standardizing how specs gate agent work across heterogeneous harnesses, at zero license cost.**
Not for solo work where the ceremony exceeds the blast radius of a bad change.

## See also

- [Kiro](../kiro/index.md) - the spec-first IDE whose workflow Spec Kit competes with
- [Send Implementation, Not Issue](../../send-implementation-not-issue/index.md) - the corpus argument for shipping specs plus implementation
- [The Future of Code Review](../../the-future-of-code-review/index.md) - where spec review sits in the review chain
- [AGENTS.md](../agents-md/index.md) - the lighter convention Spec Kit's constitution step extends

## References

- https://github.com/github/spec-kit - source, MIT, workflow steps, integrations count, as of 2026-08-26
- https://github.github.io/spec-kit/ - official docs, integrations reference, extensions and presets
- https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ - the GitHub launch post
- https://www.manorrock.com/blog/2026/08/21/spec_kit_turns_one.html - the lead maintainer's first-year and 1.0.0 post
- https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html - the waterfall-strikes-back critique
- https://news.ycombinator.com/item?id=45935763 - the 225-point critique thread, November 2025
- https://news.ycombinator.com/item?id=45610996 - the 128-point ecosystem writeup naming Kiro, Spec Kit, and Tessl, October 2025
- https://news.ycombinator.com/item?id=45125190 - the September 2025 launch thread
