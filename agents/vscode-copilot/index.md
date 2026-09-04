---
title: VS Code + Copilot
created: 2026-08-23
updated: 2026-09-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, surfaces, ai-editors, microsoft, github]
readability: 3
audience_notes: >
  Engineers deciding between the default editor stack and a dedicated AI editor.
  Assumes you know what a harness is and what a usage credit buys.
---

VS Code plus GitHub Copilot is Microsoft's agent surface: an MIT-licensed editor that now hosts several agent harnesses, with Copilot sold as a plan family from free to $100/month.
Facts below verified as of 2026-09-04.

**VS Code won the surface war by refusing to pick a winner: it runs Copilot, Claude Code, and Codex as swappable harnesses inside one editor, and that neutrality is worth more than any single agent feature.**

## What it is

The editor is open source (MIT, about 190k GitHub stars as of 2026-09-03) with AI built in.
The 2026 docs reorganize everything around agents: an Agents window for managing multiple sessions, a Chat view, browser tools, subagents, memory, hooks, skills, and MCP.
**Sessions hand off across surfaces, and VS Code discovers sessions created by Copilot CLI, Claude Code, and Codex.**
Cloud agents run on GitHub, where assigning an issue to Copilot produces a pull request from an ephemeral Actions environment.

## Status

**Active and default.**
The repository shows commits landing daily and about 190k stars as of 2026-09-03.
Every Copilot plan now includes Copilot CLI and the Copilot desktop app, and the agent docs are the editor documentation's front door as of August 2026.
One contraction is ending: new self-serve Copilot Business and Copilot Enterprise purchases were paused on April 22, 2026, and on September 3, 2026 GitHub announced it is gradually reopening self-serve sign-ups for card and PayPal payers over the following weeks.

## Strengths

- **Harness-agnostic by design**: provider harnesses (Copilot, Claude, Codex) and a local harness sit behind one session model, plus bring-your-own and local models.
- The free tier is real, with 2,000 completions a month and limited agents, and students pay nothing.
- Enterprise policy control over models, tools, and agent behavior is the deepest in the category.
- Review-and-revert of agent edits is a first-class surface inside the editor.

## Cautions

- **Copilot metering moved to GitHub AI Credits, and plan differences are now credit allotments** (1,500 monthly on Pro up to 20,000 on Max), so comparing value means reading a rate card, not a feature list.
- Copilot Free is auto-model-selection only, so the $0 agent experience is deliberately narrow.
- The April-to-September self-serve pause on Business and Enterprise showed the organization tier's plumbing can wobble, and the reopening is only gradual.
- The May 2025 coding-agent launch thread was full of quality skepticism about delegating real issues, so treat cloud delegation as incremental, not overnight.

## Pricing

Copilot Free ($0), Student (free), Pro $10/month, Pro+ $39/month, Max $100/month, Business $19/seat, Enterprise $39/seat, as of 2026-09-03.
Paid individual plans carry 1,500 (Pro), 7,000 (Pro+), or 20,000 (Max) monthly AI credits.

## Compared to

- [Cursor](../cursor/index.md): the integrated rival; pick Cursor for one vendor's opinionated stack, VS Code for choice.
- [Zed](../zed/index.md): the performance rival; pick Zed for raw speed and simpler pricing.
- [JetBrains IDEs](../jetbrains/index.md): the heavy-IDE rival; pick JetBrains for deep language analysis, VS Code for breadth.

## Bottom line

**Recommended as the default surface for anyone who wants multiple harnesses and models one toggle away at the lowest entry price.**
Not for teams that want the editor itself to come with strong opinions.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [my-ai-workflow](../../my-ai-workflow/index.md) - rotating tools instead of marrying one
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the workload the Agents window exists for
- [OpenCode](../opencode/index.md) - the harness that also treats editors as replaceable hosts

## References

- https://code.visualstudio.com/docs/copilot/overview - the agent-centric docs, harness and session model
- https://docs.github.com/en/copilot/get-started/plans - plan prices and AI credit allotments, as of 2026-09-03
- https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent - the cloud agent and issue assignment
- https://github.blog/changelog/2026-09-03-reopening-copilot-business-and-enterprise-signups - the September 3, 2026 reopening announcement for self-serve Business and Enterprise sign-ups
- https://github.com/microsoft/vscode - MIT license and repository scale, as of 2026-09-03
- https://news.ycombinator.com/item?id=44031432 - coding-agent launch discussion with early skepticism
