---
title: Roo Code
created: 2026-08-26
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, open-source, byok]
readability: 3
audience_notes: >
  Engineers who used Roo Code or are choosing among Cline-lineage VS Code extensions, and anyone tracking consolidation among open-source coding agents.
  Assumes you know what a fork is and what BYOK means.
---

Roo Code was an Apache-2.0 VS Code extension coding agent forked from Cline, with a mode system and its own Cloud and Router products; its team sunset the whole suite on May 15, 2026 to build Roomote, a cloud coding agent.
Facts below verified as of 2026-08-26.

**The sunset notice's own words, "we don't believe IDEs are the future of coding", are the category's bluntest epitaph: the fork-and-extend extension generation died not by losing to Copilot but by its own makers deciding the IDE was the dead end.**

## What it is

A VS Code extension (marketplace id RooVeterinaryInc.roo-cline, 1,956,325 installs as of 2026-08-26) forked from Cline in early 2025, initially as "Roo Cline".
**Its differentiator was modes**: built-in code, architect, ask, and debug personas plus fully custom modes, each with its own rules, and an orchestrator mode that delegated subtasks to child modes.
Rules came from `.roorules` files and directories, and the [custom instructions docs](https://roocodeinc.github.io/Roo-Code/features/custom-instructions) show it also read AGENTS.md from the workspace root when present and enabled.
MCP servers were supported throughout, with [dedicated docs](https://roocodeinc.github.io/Roo-Code/features/mcp/overview), and BYOK to any provider including [Ollama](https://roocodeinc.github.io/Roo-Code/providers/ollama) for local models.

## Status

Dead, sunset on a published schedule.
The [announcement](http://web.archive.org/web/20260508092828/https://roocode.com/blog/sunsetting-roo-code-extension-cloud-and-router) (2026-04-20, the live URL now serves the pivot product) committed to supporting everything through May 15, shutting down Roo Code Cloud and Router with refunds, and archiving the extension repo.
The evidence matches: the last release (v3.54.0) and the last push both landed 2026-05-15, and the repo shows 24,325 stars, 3,415 forks, and 1,035 open issues as of 2026-08-26.
The announcement claimed "past 3m extension downloads" and pointed users to Cline, which "incorporated much of what we built".
**The team's new product is [roomote.dev](https://roomote.dev/), a cloud coding agent, and roocode.com now sells that instead.**

## Strengths

- The mode system was the most expressive role model in the extension generation, and Cline absorbing it is direct confirmation it worked.
- Read AGENTS.md natively on top of its own .roorules, so rule files ported.
- A 4.72 marketplace rating across about two million installs, among the best in this category's history.
- The sunset was unusually clean: a schedule, refunds, and a named successor.

## Cautions

- Unmaintained by decision, with 1,035 open issues accumulating since May.
- The recommended successor is Cline, its own upstream; forks of Roo (Kilo Code and others) carry the code on but split the community further.
- Roomote is a different product category, so this is an exit, not a migration path.
- The [28-point HN thread](https://news.ycombinator.com/item?id=47851734) on the shutdown read it as fork economics: forking an actively maintained repo for commercial purposes means competing with your upstream where moats are weak.

## Pricing

The extension was free and open source with BYOK.
Roo Code Cloud and Router were paid until the shutdown, with unused balances refunded.

## Compared to

- [Cline](../cline/index.md): the upstream that outlived the fork and absorbed its best ideas; the recommended and correct landing spot.
- [Continue](../continue/index.md): the same generation's other death, by acquisition instead of pivot.
- [Void](../void/index.md): the fellow open-source surface that stalled rather than sunset, a quieter version of the same story.

## Bottom line

**Recommended only as a case study in fork economics and category exit.**
I would not install it today; the sunset post itself tells you where to go.
The disagreeable claim I will defend: Roo's death was not failure, its team correctly priced where value was moving (cloud execution) and left before the extension market forced the same exit on everyone else.

## See also

- [Cline](../cline/index.md) - the upstream and successor
- [Continue](../continue/index.md) - the acquisition death completing the pattern
- [Void](../void/index.md) - the stall death next door
- [VS Code + Copilot](../vscode-copilot/index.md) - the host surface all three lived in

## References

- http://web.archive.org/web/20260508092828/https://roocode.com/blog/sunsetting-roo-code-extension-cloud-and-router - the sunset announcement, archived (live URL repurposed)
- https://github.com/RooCodeInc/Roo-Code - repository state, license
- https://api.github.com/repos/RooCodeInc/Roo-Code - last push 2026-05-15, stars, forks, issues as of 2026-08-26
- https://github.com/RooCodeInc/Roo-Code/releases - v3.54.0, 2026-05-15, the final release
- https://news.ycombinator.com/item?id=47851734 - the shutdown thread with the fork-economics critique
- https://thenewstack.io/roo-code-cloud-ides-ai-coding/ - press coverage of the pivot
- https://roomote.dev/ - where the team went
- https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline - install count and rating
