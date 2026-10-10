---
title: Screenpipe
created: 2026-10-08
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, screen-capture, timeline, mcp, source-available]
readability: 3
audience_notes: >
  Engineers who want coding or personal agents grounded in what they actually did on their
  machine, and who need to weigh a capture-everything memory layer against the conventions.
  Assumes you know what MCP is.
---

Screenpipe is a source-available local capture engine (YC S26) that continuously records a computer's screen, audio, and meetings into a searchable local timeline that agents query over MCP and a localhost API.

**Its bet is that the richest memory an agent can have is the recording of what you did, and its risk is the same bet at maximum scale: it captures everything, all the time.**

## What it is

A Rust engine with a Tauri desktop app and a CLI (`npx screenpipe record`) from Negentropy Labs, Inc. (founder Louis Beaumont).
Capture is event-driven: a screenshot is paired with the OS accessibility tree when something changes, falling back to OCR, while system and microphone audio are transcribed locally with Whisper.
Everything lands in a local SQLite store with FTS5 search, a REST API on localhost:3030, and an MCP server (`npx screenpipe-mcp`) that Claude Desktop, Cursor, and coding agents query.
Pipes are scheduled AI agents defined as markdown files, with YAML frontmatter permissions (allowed apps, windows, content types, time ranges) enforced in three deterministic layers rather than by prompting.
`npx screenpipe setup` wires skills and MCP into Claude Code, Codex, Gemini CLI, Cursor, and OpenCode.

## Status

**Active and large, ranking eleventh of the twenty-two members by stars, on a YC-backed company.**
21,884 stars with the repository pushed 2026-10-09, created 2024-06-19, as of 2026-10-09 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=screenpipe/screenpipe&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=screenpipe/screenpipe&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=screenpipe/screenpipe&type=date&theme=dark&legend=top-left" />
</picture>

The Hacker News record is the strongest in this category: a 218-point Show HN in September 2024 (125 comments), an 88-point Launch HN with 67 comments as a YC S26 company in July 2026, and a 2024 Ask HN thread questioning the business model.
The README positions it as the source-available alternative to Limitless, Microsoft Recall, Granola, and Otter.

## Strengths

- The timeline answers the questions session logs cannot: what did I see, say, and do outside the terminal.
- Event-driven accessibility-tree capture keeps CPU and storage bounded compared with naive frame recording, per its own resource estimates.
- Per-pipe YAML data permissions enforced at the server and agent layers are the most concrete agent-data-governance story in this category.
- Distribution is already in place: MCP, REST, SDK, skills, and desktop installers across macOS, Windows, and Linux.

## Cautions

- **Source-available is not open source**: the Screenpipe Commercial License permits personal and non-commercial use free, gives organizations a 7-day evaluation, and requires a paid license for commercial use, so 21.9k stars do not mean free to deploy.
- Telemetry is on by default (PostHog analytics and Sentry), and local capture does not mean zero network traffic; the README's own FAQ itemizes what leaves the device.
- Capture-everything is this category's known failure mode at its maximum: screen, audio, and keystrokes concentrate more sensitive data than any other member here.
- The production app's full history and sync sit behind paid tiers, and the 2024 business-model skepticism in its own community was never fully answered.

## Pricing

Free: $0, one device, capture, search, and sharing context with AI tools.
Basic: $21/month ($250/year billed annually), full searchable history and unlimited scheduled workflows.
Business: $42/seat/month ($500/seat/year), personal device sync and managed seats, shared context across teammates not included.
Enterprise: custom, scoped per deployment.
A 50 percent first-month student discount applies, as of 2026-10-08.
Source builds follow the commercial license: personal, non-profit, and educational use free, organizational evaluation 7 days.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-08 | Free, Basic, Business, Enterprise | Baseline: Free $0 (one device), Basic $21/mo ($250/yr), Business $42/seat/mo ($500/seat/yr), Enterprise custom; source builds free for non-commercial use. | [screenpipe.com/pricing](https://screenpipe.com/pricing) |

## Compared to

- [claude-mem](../claude-mem/index.md): session-compression memory scoped to what your coding agent did; Screenpipe records everything on the screen, including everything outside the agent.
- [Engrim](../engrim/index.md): curated episodic records versus raw capture; Engrim stores what the agent decided to log, Screenpipe keeps what happened.
- [File-based agent memory](../file-based-agent-memory/index.md): the zero-capture convention; the two agree only that the store should live on your disk.

## Bottom line

**Recommended for developers who want coding agents grounded in their actual machine activity and will pay for it and govern it.**
Not for privacy-strict environments, commercial use without a license budget, or anyone who expected an OSI open-source license at this star count.

## Changes

- 2026-10-08 - Created from the 2026-10-08 awesome-list entrant scan, with eight fetched sources and the source-available-license-plus-capture-everything combination recorded as the critical angle.
- 2026-10-09 - Corrected the Status rank claim: at 21,884 stars Screenpipe ranks eleventh of the twenty-two members, not the category's second-largest repository; refreshed stars and the as-of dates.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [claude-mem](../claude-mem/index.md) - the session-scoped capture layer, the nearest architectural cousin
- [Engrim](../engrim/index.md) - the curated-records counterpoint to raw capture
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention at the zero-capture end of the spectrum

## References

- https://github.com/screenpipe/screenpipe - repository, 21,884 stars, activity, as of 2026-10-09
- https://raw.githubusercontent.com/screenpipe/screenpipe/main/README.md - capture model, pipes and their permission model, MCP and API surfaces, positioning
- https://raw.githubusercontent.com/screenpipe/screenpipe/main/LICENSE.md - the Screenpipe Commercial License terms (personal free, 7-day organizational evaluation, commercial paid)
- https://screenpipe.com/pricing - Free, Basic, Business, and Enterprise plans as of 2026-10-08
- https://news.ycombinator.com/item?id=49024620 - the YC S26 Launch HN thread (88 points, 67 comments, 2026-07-23)
- https://news.ycombinator.com/item?id=41695840 - the 2024 Show HN (218 points, 125 comments), the category's largest community record
- https://hn.algolia.com/api/v1/search?query=screenpipe&tags=story - the footprint scan, including the 2024 business-model skeptic thread
