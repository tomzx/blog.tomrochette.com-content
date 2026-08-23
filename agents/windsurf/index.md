---
title: Windsurf
created: 2026-08-23
updated: 2026-08-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, cognition, devin]
readability: 3
audience_notes: >
  Engineers who standardized on Windsurf or are evaluating what Cognition did with it.
  Assumes you followed the 2025 AI-editor market at least from the sidelines.
---

Windsurf was the agentic IDE that survived an aborted $3 billion OpenAI acquisition and a Cognition rescue, and it is now being rebranded out of existence as Devin Desktop.
Facts below verified as of 2026-08-23.

**Windsurf is the category's cautionary tale: the number-two AI editor was bought, broken up, and rebranded within two months in mid-2025, and its retirement into Devin Desktop is the reminder that loyalty to an AI editor has no asset value.**

## What it is

The editor was a VS Code fork from the Codeium lineage, with the Cascade agent at its core; its package infrastructure still lives under codeiumdata.com.
Under Cognition it became Windsurf 2.0 with an Agent Command Center and Devin inside, then **Devin Desktop, introduced June 2, 2026 as "the next generation of Windsurf"**: agent management as the default IDE surface, Spaces for shared agent context, and ACP support so any ACP-compatible agent runs alongside Devin.
The docs now ship the product as `devin-desktop`, authenticate with a Devin account, and run Devin Local, the harness shared with Devin CLI.

## Status

**Pivoted, and the brand is being retired.**
May 2025: OpenAI reached agreement to buy Windsurf for $3 billion.
July 11, 2025: that deal was off and the CEO went to Google; a July 24 thread from an early employee claimed a payout of about 1% of what the shares were worth.
July 14, 2025: Cognition signed the definitive agreement for the IP, product, trademark, brand, and team, citing $82M ARR, 350+ enterprise customers, and hundreds of thousands of daily active users.
June 2026: Devin Desktop shipped, and the documentation domain now describes a Devin product.

## Strengths

- **The Cascade lineage survives inside a well-funded owner**: agentic IDE mechanics honed by that user base now back Devin's stack.
- ACP support makes Devin Desktop a host for rival agents, an unusually open posture for an acquired product.
- Full backwards compatibility with Windsurf settings and extensions meant existing teams were not stranded.
- Cognition's own model line (SWE-1.6 preview, March 2026) continues underneath the editor.

## Cautions

- **You cannot buy Windsurf anymore, you buy Devin**: check whether your workflow survives an owner whose flagship is a cloud autonomous agent.
- windsurf.com rate-limits automated fetches (HTTP 429 on every attempt this run), so plan pages could not be re-verified as of 2026-08-23.
- The equity dispute thread is a reminder of how much human turbulence this product absorbed in 2025.
- A rebrand in progress means docs, packages, and repositories still say windsurf in places; expect transitional breakage.

## Pricing

**The classic Windsurf consumer plans are gone with the rebrand; Devin Desktop authenticates with a Devin account and meters usage as credits.**
Enterprise relationships carry over through Cognition sales.
Current tier prices were not verifiable this run because windsurf.com rejected automated fetches.

## Compared to

- [Cursor](../cursor/index.md): the survivor and category leader; the natural landing spot for teams leaving the Windsurf transition.
- [VS Code + Copilot](../vscode-copilot/index.md): the safe default with no ownership drama.
- [Zed](../zed/index.md): independence and speed over platform breadth.

## Bottom line

**Recommended only for existing Windsurf or Devin shops riding the transition.**
Not for new adoption: picking a brand mid-retirement means betting on one company's roadmap.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [ai-tools-i-have-used](../../ai-tools-i-have-used/index.md) - the shelf life of tool loyalty
- [Whoever Ships First Decides](../../whoever-ships-first-decides/index.md) - why market leadership consolidated this fast

## References

- https://cognition.ai/blog/windsurf - the July 14, 2025 acquisition agreement, ARR, and customer counts
- https://cognition.ai/blog/introducing-devin-desktop - the June 2, 2026 rebrand announcement
- https://docs.windsurf.com/ - current product docs as Devin Desktop (package, harness, credits)
- https://news.ycombinator.com/item?id=44536988 - the July 2025 deal-collapse and CEO-to-Google thread
- https://news.ycombinator.com/item?id=44673296 - the early-employee equity dispute thread
- https://news.ycombinator.com/item?id=43900877 - the May 2025 $3 billion agreement thread
