---
title: Jesse Vincent
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, coding-agents, agentic-engineering, skills, tdd]
readability: 3
audience_notes: >
  Engineers who want a tested daily coding-agent workflow rather than another hot take, and who wonder where the Superpowers skill suite came from.
  Assumes you know what a git worktree, red/green TDD, and a coding-agent skill are.
---

Jesse Vincent (obra) is a programmer with an open-source track record long enough to predate this blog (Request Tracker, Perl 5 pumpkins, K-9 Mail, Keyboardio) who now documents a sustained personal coding-agent practice at blog.fsck.com and builds Superpowers at Prime Radiant.

**He is the practitioner who turned agentic coding from loose prompts into a codified, eval-measured methodology you can install today; the price of that discipline is tokens, speed, and a strong-opinions workflow that not every codebase or culture will accept.**

## What it is

A long-running personal blog (541 posts as of 2026-09-24) where he publishes point-in-time writeups of how he works with agents, plus Superpowers, an MIT-licensed skill suite (291k stars, 26k forks, 682 commits as of 2026-09-24) that packages his brainstorm, plan, worktree, subagent-driven development, TDD, and two-axis code review loop as mandatory workflows for 16 coding-agent harnesses.
Wikipedia credits him with publishing the Architect/Implementer pattern and a SKILL.md-formatted skills approach about a week before Anthropic shipped its native skills framework.
He is founder and CEO of Prime Radiant, the applied research lab behind Superpowers, which sells commercial support around it and maintains a public eval suite.

## Status

Very active and shipping on a cadence: Superpowers 6.4 landed 2026-09-21 (adding Meta Muse, OpenCode 2.0, and Qwen Code support), a Birds-of-a-Feather on agentic engineering with Simon Willison was announced 2026-09-22 for San Francisco, and recent months brought a vibe-coded C compiler that builds SQLite (2026-08-21), Superpowers 6 (2026-06-15, 50 percent faster and 60 percent cheaper by their evals), a hiring post (2026-06-12), and 5.1.0 (2026-05-04).
His writeups say users' most common lament is that Superpowers burns many tokens and takes longer than going without it, and 6.4 concedes that bare-metal builds are faster and cheaper while arguing they are significantly buggier per his eval suite.
Third-party pull is visible: HN threads recommend Superpowers as the fix for bad agent experiences, Willison cites it as the reference implementation of TDD-with-agents, OpenAI's Codex announcements were read as bundling it, and orchestration stacks like metaswarm declare it, alongside Yegge's beads, an essential foundation.

## Strengths

- The workflow is specific and copyable: Socratic brainstorming, plans written for "an engineer with zero context and questionable taste", isolated worktrees, fresh subagents per task with review after each, and reviews checked on spec compliance and quality separately.
- He measures his own system instead of asserting it: the public superpowers-evals repo and the 6.0/6.4 posts report speed, cost, and bug deltas across harnesses and models.
- He reports failures, not just wins, from the session that tried to delete his tests to the goal loop that stopped early on the compiler project, which makes the writeups unusually trustworthy.
- His blog doubles as a skills-engineering manual: pressure-testing skills against subagents, Cialdini-style persuasion principles as reliability levers, and skills mined from his own conversation history.
- The ecosystem compounds around him, so adopting the suite buys you a community and a lineage (superpowers-rails, metaswarm) rather than a lone repo.

## Cautions

- Cost and speed are the known tax; if your budget cannot absorb subagent-driven development's overhead, his own release notes tell you bare metal wins on both axes.
- The methodology is mandatory by design (skills "must" be used, TDD enforced, code written before tests gets deleted), which reads as rigidity if your context is a legacy codebase or a non-TDD culture.
- Behavior shifts with every frontier model release, and his posts are explicitly point-in-time snapshots, so six-month-old methodology posts need re-verification before you copy them.
- The visual companion feature phones home version telemetry by default via Prime Radiant's site, with an opt-out environment variable, which is disclosed but worth knowing.

## Compared to

- [Simon Willison](../simon-willison/index.md): Willison surveys the whole landscape daily and Vincent systematizes one practice deeply, and the two co-host the October 2026 agentic-engineering BoF in San Francisco; read Willison for breadth, Vincent for a runnable process.
- [Thorsten Ball](../thorsten-ball/index.md): both write first-person practitioner notes, but Ball works at the harness-building layer while Vincent works at the methodology layer on top of harnesses like the ones Ball builds.
- [Steve Yegge](../steve-yegge/index.md): Yegge's beads tracker and Gas Town orchestration thesis sit above Vincent's skills layer, and real stacks (metaswarm) combine the two; choose Vincent for disciplined task execution, Yegge for tracking and multi-agent orchestration.

## Bottom line

**Recommended for engineers who want a tested, opinionated agentic workflow they can install today, and for anyone designing agent skills, since his posts are the best public record of how to engineer them.**
Not for token-budget-tight users, TDD-averse codebases, or readers who want minimal process between idea and diff.

## Top 5 recommended reading

- [How I'm using coding agents in September, 2025](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/) - the foundational methodology post: worktrees, brainstorming, architect/implementer sessions, and taming CodeRabbit reviews.
- [Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/) - the release announcement that turns the methodology into installable skills, including his skill-testing approach.
- [Superpowers 6](https://blog.fsck.com/2026/06/15/Superpowers-6/) - the optimization story: a model-driven autoresearch loop, published eval numbers, and candor about the token-cost complaint.
- [Superpowers 6.4](https://blog.fsck.com/2026/09/21/superpowers-6.4/) - the current state: 16-harness support, the bare-metal comparison he concedes, and the new diagnosing-superpowers skill.
- [I vibe-coded a C compiler that can build SQLite](https://blog.fsck.com/2026/08/21/i-vibe-coded-a-c-compiler/) - his autonomous long-horizon experiment (Evener plus GLM 5.2, 21 hours) showing what his loops attempt when goal-driven.

## Changes

- 2026-09-24 - Created.

## See also

- [Simon Willison](../simon-willison/index.md) - his co-host for the agentic-engineering BoF and the chronicler who cross-references Vincent's practice
- [Steve Yegge](../steve-yegge/index.md) - the tracking-and-orchestration layer (beads, Gas Town) that Vincent-style skill stacks are built on
- [Beads](../../task-management/beads/index.md) - Yegge's git-native tracker that metaswarm-style stacks pair with Superpowers
- [Anthropic Agent Skills](../../skills/anthropic-agent-skills/index.md) - the native skills framework that his SKILL.md experiments preceded by about a week
- [Claude Code](../../harnesses/claude-code/index.md) - the harness where Superpowers was born and remains installed via the official plugin marketplace

## References

- https://blog.fsck.com/ - the blog homepage: cadence, recent posts, 541-post archive, and the Prime Radiant/Best Practical/Keyboardio work links
- https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/ - the September 2025 methodology writeup
- https://blog.fsck.com/2025/10/09/superpowers/ - the Superpowers release announcement and skills philosophy
- https://blog.fsck.com/2026/06/15/Superpowers-6/ - the Superpowers 6 release: eval-driven 50/60 percent improvements and the token-cost admission
- https://blog.fsck.com/2026/09/21/superpowers-6.4/ - the 6.4 release: new harness support, bare-metal comparison, diagnosing-superpowers skill
- https://blog.fsck.com/2026/08/21/i-vibe-coded-a-c-compiler/ - the autonomous C-compiler experiment grounding his long-horizon loop practice
- https://github.com/obra/superpowers - the repo: MIT license, 291k stars and 26k forks as of 2026-09-24, 16 documented harness installs, commercial support, and telemetry disclosure
- https://en.wikipedia.org/wiki/Jesse_Vincent - biography: RT, Best Practical, Perl roles, K-9 Mail, Keyboardio, Prime Radiant CEO, and the SKILL.md-before-Anthropic timeline
- https://hn.algolia.com/api/v1/search?query=jesse%20vincent%20superpowers&hitsPerPage=8 - third-party reception: HN recommendations, the Superpowers 6 thread, metaswarm's reliance on it, and Willison citing it as the TDD reference
