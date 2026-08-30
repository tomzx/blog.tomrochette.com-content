---
title: Void
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, open-source]
readability: 3
audience_notes: >
  Engineers who want an open-source AI editor and are checking whether Void is still alive.
  Assumes you know what a VS Code fork is and what BYOK means.
---

Void is the open-source Cursor alternative: an Apache-2.0 VS Code fork with BYOK AI, about 28.8k GitHub stars as of 2026-08-24, and a release cadence that has slowed to a crawl.
Facts below verified as of 2026-08-30.

**Void proved the demand for an open AI editor (948 points on its breakout thread) and then demonstrated the second lesson: in this category, open source does not keep pace with funded velocity.**

## What it is

A VS Code fork with AI features integrated directly: chat, completion, and agent-style edits against your own API keys, with no subscription layer.
**The pitch is ownership: every AI feature runs through keys you hold, and the whole editor is auditable source.**

## Status

**Dormant-leaning; releases stalled.**
The last tagged release is v1.3.4 from April 2025, over a year before this verification date, and repository activity since has thinned to a trickle (last push June 2026).
A December 2025 Show HN appeared titled "after Void slowed down", which is the community recording the same fact independently.

## Strengths

- Fully open source under Apache-2.0, the permissive license, not FSL like Crush.
- BYOK with no metering, subscription, or account requirement.
- Still installs and runs for users whose priority is an auditable editor over new features.

## Cautions

- **The stall is the caution**: an AI editor that stops tracking model and harness changes ages faster than a plain editor, because the model side moves monthly.
- Bug fixes and security patches now depend on whoever shows up, not a company.
- Community energy moved to Zed (open, fast) and OpenChamber (open, sessions-first).

## Pricing

Free and open source; all AI costs are your providers' API bills.
No paid tier exists, as of 2026-08-24.

## Compared to

- [Zed](../zed/index.md): the open editor with velocity; pick it over Void today.
- [Cursor](../cursor/index.md): the closed source fork with the features; Void is the inverse trade.
- [OpenChamber](../openchamber/index.md): open and active, but sessions-first rather than editor-first.

## Bottom line

**Recommended only for engineers who specifically need an Apache-2.0 editor fork and accept frozen features.**
Not for anyone who wants the project's best days ahead of it.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [Zed](../zed/index.md) - the active open alternative
- [ai-tools-i-have-used](../../ai-tools-i-have-used/index.md) - the pattern of tools stalling as attention moves

## References

- https://voideditor.com/ - product page and download
- https://github.com/voideditor/void - source, about 28.8k stars, Apache-2.0, as of 2026-08-24
- https://github.com/voideditor/void/releases - release history ending at v1.3.4, April 2025
- https://news.ycombinator.com/item?id=43927926 - the 948-point breakout thread, May 2025
- https://news.ycombinator.com/item?id=46274927 - the "after Void slowed down" thread, December 2025
