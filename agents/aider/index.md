---
title: aider
created: 2026-08-22
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, coding-agents, harnesses, pair-programming, open-source]
readability: 3
audience_notes: >
  Engineers who want cheap, controlled edits against their own API keys rather than an autonomous agent.
  Assumes you know git well enough to read a diff and revert a commit.

---

aider is AI pair programming in your terminal: a Python, Apache-2.0, bring-your-own-key tool by Paul Gauthier (Aider-AI) that predates the agentic coding wave.
Facts below verified as of 2026-09-05.

**aider's refusal to become an autonomous agent is a feature: it is the cheapest precise-edit tool in the field, and its stale public leaderboard is still more trustworthy than any vendor's own benchmark claims.**

## What it is

You add files to the chat, aider edits them, and every change lands as an automatic git commit you can diff, manage, and undo.
A tree-sitter repo map gives the model a view of the whole codebase without loading it, supporting 100+ languages.
Lint and test hooks run after each edit, images and web pages can join the chat, there is a voice mode, and a copy/paste mode for driving web chat UIs instead of APIs.
It connects to nearly any LLM, including local models.

## Status

**Development stalled; the tool itself still works.**
About 48.7k stars and 4.9k forks as of 2026-09-05, but the default branch has had no commits since May 22, 2026, and the last tagged release (v0.86.0) dates to August 2025.
The polyglot leaderboard (225 Exercism exercises) is still published, but its headline results date to August 2025, and the site's "works best with" copy still names Claude 3.7 Sonnet-era models.

## Strengths

- Deterministic and git-first: every edit is a commit, every commit is reviewable, nothing happens outside the files you added.
- Cheap: you bring the key, pick the model, and watch the metered cost per task.
- The leaderboard, even stale, is an independent yardstick the whole industry used for two years.
- Runs against local models when labs are unreachable or disallowed.

## Cautions

- It is not agentic: no autonomous explore-plan-implement loop, no MCP support, and you must curate context yourself; every agentic-tool thread eventually names those gaps out loud.
- The leaderboard's age now matters; use it for relative history, not current model choice.
- Install it isolated (pipx or the installer) or its Python dependencies will fight your project's.
- Community energy has moved to the harness generation; expect fewer of the workflow innovations to arrive here first.
- **Maintenance is the risk now**: no commits on the default branch since May 22, 2026, and no tagged release since v0.86.0 (August 2025), as of 2026-09-05, so budget for dependency drift and no fixes.

## Pricing

Free, open source, sponsor-funded; all model costs are whatever your providers charge.
No subscription exists to buy.

## Compared to

- [OpenCode](../opencode/index.md): agentic, MIT, still BYOK; choose it when the task is long and exploratory.
- [Crush](../crush/index.md): agentic with LSP context; the terminal-aesthetics pick.
- [Claude Code](../claude-code/index.md): the subscription platform; costs more per edit than aider by an order of magnitude on light tasks.

## Bottom line

Recommended for precise, reviewable edits on your own keys, and as the low-cost baseline every fancier tool should justify itself against.
I still open it when I want the diff to be the entire story.
Not for long autonomous tasks, hands-off refactors, or teams that need an actively maintained tool.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - aider as the surviving pre-agentic tool in the harness layer
- [my-ai-workflow](../../my-ai-workflow/index.md) - practitioner rotations that keep a cheap tool in the mix
- [ai-tools-i-have-used](../../ai-tools-i-have-used/index.md) - the longer history of tools of this generation
- [Rethinking Code Review in the Age of LLMs](../../rethinking-code-review-in-the-age-of-llms/index.md) - why commit-per-edit workflows age well

## References

- https://aider.chat/ - features, install stats, model recommendations
- https://github.com/Aider-AI/aider - repository scale and license, as of 2026-09-05
- https://aider.chat/docs/leaderboards/ - the polyglot benchmark, results dated August 2025
- https://news.ycombinator.com/item?id=39995725 - launch-era discussion of strengths and failure modes
- https://news.ycombinator.com/item?id=43672712 - critical thread on aider's wasted inference spend against agentic rivals
