---
title: puppyone
created: 2026-10-27
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, ai-editors, open-source, agent-context]
readability: 3
audience_notes: >
  Engineers and technical teams choosing where agents should work when the job spans code
  and business documents, and anyone tracking the editor generation that treats the folder,
  not the chat, as the product.
  Assumes you know what a coding-agent CLI and a git diff are.
---

puppyone is a free, Apache-2.0 desktop editor that opens any folder on your machine and lets AI agents work in it, tracking every change in Git down to a redline view for Word documents.

**Its bet is that the folder, not the chat or the editor project, is the durable unit of agent work: agents come and go, your folder stays, and every change any of them made is one rollback away.**

## What it is

An Electron desktop app for macOS and Windows (or an npm-installed CLI) that renders documents, spreadsheets, slides, PDFs, images, audio and video, 3D models, and code in place, so an agent works in the same folder you open.
Agents connect four ways: a built-in puppyone Agent (trial credit, then pay as you go, or your own API key or local model), a bundled WorkBuddy agent, your installed coding CLIs (Claude Code, Codex, OpenCode, Cursor, Pi), and through the optional puppyone Cloud, consumer agents such as ChatGPT, Claude, and Manus or any MCP client.
Every write lands in Git automatically: text gets line diffs, Word documents get a tracked-changes redline, binaries get a change summary, and any file or the whole folder rolls back to an earlier version.
The same vendor runs a cloud service of the same name that its docs call a Context File System: SaaS connectors (Notion, GitHub, Gmail, Google Drive, Airtable) mounted into one file tree, per-agent access points scoped by path, audit logs, and distribution over MCP, REST, CLI, or local sync; the desktop app's cloud panel is Early Access.
The maker is puppyone Tech Pte Ltd, and desktop telemetry is two documented pseudonymous events you can switch off.

## Status

**Active and very young, with zero independent coverage.**
The repository was created 2026-06-29 and shows 1,331 stars and 124 forks as of 2026-10-27, with commits landing the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=puppyone-ai/puppyone&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=puppyone-ai/puppyone&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=puppyone-ai/puppyone&type=date&legend=top-left" />
</picture>

A Hacker News search returns no story about the project as of 2026-10-27, only substring matches, and no third-party review has appeared; the footprint is the repository and the vendor's own site.
The dual identity is the thing to watch: the README sells a local-first agent editor, the docs sell a governed context file system, and the Meirtz context-engineering list carries it under the second label.

## Strengths

- **Agent-swap without migration is the core promise, and it holds**: the same plain folder serves coding CLIs today and a different agent tomorrow, which is the portability most editors only approximate.
- Git-tracked changes with redlines give agent review a format non-engineers already read.
- The format list (DOCX, XLSX, PPTX, PDF, 3D) reaches work the code editors ignore.
- Per-agent access points with path scoping are a cleaner answer than shared credentials.

## Cautions

- **The product's center of gravity is business context, not code**: the vendor's own docs say not to use it as a code repository host, so the coding support is genuine but not the spine.
- The two-sided story (desktop editor versus context file system) is still settling, and the cloud side is Early Access.
- Young and fast-moving; expect churn.
- Zero third-party coverage means every claim beyond the vendor's own is untested.

## Pricing

The desktop app is free and open source; the built-in agent runs on trial credit, then pay as you go, or on your own API key or local model at no charge.
The cloud service is Free ($0, one member, one project, three agent access points, 2 GB), Developer at $19 per project per month, Team at $99 per project per month for ten members, and Enterprise custom, as of 2026-10-27.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-27 | Cloud plans | Baseline: Free $0, Developer $19/project/mo, Team $99/project/mo, Enterprise custom. | [puppyone pricing](https://www.puppyone.ai/pricing.md) |

## Compared to

- [Nimbalyst](../nimbalyst/index.md): the richer co-editing workspace for people and agents on code and documents; pick it for per-block diff review of editor artifacts, puppyone for a plain folder any agent already knows how to work in.
- [Cate](../cate/index.md): the canvas of agent terminals for hands-on supervision; puppyone is for leaving agents in a folder and reviewing what they wrote.
- [OpenChamber](../openchamber/index.md): the OpenCode session cockpit; choose it for parallel session management, puppyone for document-heavy shared work.

## Bottom line

**Recommended for engineers and technical teams who want coding CLIs and general agents working in one ordinary folder with reversible, reviewable changes.**
Not for anyone needing a session grid, scheduled work, or a product with an independent track record.

## Changes

- 2026-10-27 - Created from the context-engines scanner handoff (surfaced by the Meirtz context-engineering list under a context-filesystem label), admitted as a local-first agent editor with the dual-positioning caution recorded.

## See also

- [Nimbalyst](../nimbalyst/index.md) - the co-editing workspace neighbor with the same agents-swap stance and richer editors
- [Cate](../cate/index.md) - the canvas workspace supervising the same parallel-agent problem from the terminal side
- [OpenChamber](../openchamber/index.md) - the session cockpit that shares the your-machines-only stance on where work runs
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/puppyone-ai/puppyone - repository, Apache-2.0, 1,331 stars and 124 forks as of 2026-10-27 (GitHub API)
- https://raw.githubusercontent.com/puppyone-ai/puppyone/main/README.md - the desktop editor: formats, the agent connection table, Git tracking with redlines, the telemetry contract
- https://www.puppyone.ai/ - the site's positioning and developer entry points (CLI, REST API, MCP, agent auth)
- https://www.puppyone.ai/en/docs - the Context File System framing: connectors, access points, audit logs, distribution channels
- https://www.puppyone.ai/pricing.md - the cloud plans (Free, Developer $19, Team $99, Enterprise custom), fetched 2026-10-27
- https://hn.algolia.com/api/v1/search?query=puppyone&tags=story - the zero-coverage footprint evidence, fetched 2026-10-27
