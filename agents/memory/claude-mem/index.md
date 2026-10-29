---
title: claude-mem
created: 2026-08-30
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, session-memory, compression, open-source]
readability: 3
audience_notes: >
  Engineers whose coding agents re-explain the same context every session and who want automated memory instead of hand-curated files.
  Assumes you know what Claude Code hooks and MCP are.
---

claude-mem is an open-source Apache-2.0 plugin that gives coding agents persistent cross-session memory by capturing session activity through lifecycle hooks, compressing it into observations with LLM calls, storing them in local SQLite, and injecting relevant context back into future sessions.

**claude-mem is the strongest evidence yet that session memory has crossed from experiment to default expectation, and its cost model is the field's open question: it captures everything and pays your tokens to compress it.**

## What it is

A TypeScript plugin (Node 20+ or Bun) that hooks session lifecycle events: SessionStart injects context from recent sessions, UserPromptSubmit and PostToolUse capture activity, PreToolUse on Read adds file context, Stop summarizes.
A background worker compresses observations through the Claude Agent SDK (or Gemini or OpenRouter), and storage is a local SQLite database with FTS5 full-text search and optional Chroma vector search.
Retrieval is exposed as MCP tools plus a `mem-search` skill using three-layer progressive disclosure, which the project credits with roughly tenfold token savings over fetching full observations.
It targets Claude Code first-class, with install paths for OpenCode, Codex CLI, Gemini CLI, Cursor, Windsurf, Antigravity, OpenClaw, and, since v13.34.0, first-party Pi and DeepSeek Harness extensions.
Made by Alex Newman (thedotmack), a solo author in the Vercel OSS Program, with a commercial cloud arm at cmem.ai.

## Status

Very large and fast: about 101.1k stars as of 2026-10-16, with 63,865 npm downloads in the trailing month (2026-09-23 to 2026-10-22).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=thedotmack/claude-mem&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=thedotmack/claude-mem&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=thedotmack/claude-mem&type=date&legend=top-left" />
</picture>

Created 2025-08-31, pushed 2026-10-28, latest tagged release v15.4.0 on 2026-10-28 with npm in sync at 15.4.0 as of 2026-10-28.
The README now brands the project Grok Mem (the package is still `claude-mem`), and v13.24.0 shipped it as two independent Cursor and Grok Bot marketplace plugins alongside the Claude Code install path.
**The v13.x version line tells you the churn rate: near-daily releases with major-version jumps, which is velocity and breakage risk in the same number.**
v13.30.0 (2026-10-04) reworked hook delivery so hooks spool each event to disk and return without waiting on the worker, made observer prompts provider-cache-friendly, and dropped the separate per-prompt observer call, and v13.31.0 (2026-10-05) cut SessionStart's newest-memories query from seconds to milliseconds with new indexes.
v13.31.1 (2026-10-06) fixed cloud sync stalling behind Supabase's firewall (uploads are now compressed before forwarding, and HTML blocks are retried instead of read as bad tokens), and v13.32.0 (2026-10-06) restored the File Read Gate on by default: full-file Reads of observed code files are blocked and served the observation timeline plus outline tools instead, with partial reads exempt so edits never deadlock.
Same-day follow-ups: v13.34.0 added first-party Pi and DeepSeek Harness integrations (a self-contained ESM extension under ~/.pi/agent/extensions and a bundled @claude-mem/dsh plugin installed through DSH's own profile commands), v13.34.1 restored the CMEM Pro public trial to 30 days from the shorter "up to 14 days" wording, and v13.34.2 fixed a worker regression that had broken prompt-cache reuse on OpenAI-compatible observers (OpenRouter, Gemini) since v13.29.0.
The 2026-10-12-to-13 train (v13.36.0, v13.36.1, v13.37.0) is the first recorded privacy regression and capture outage in the same week: v13.36.0, a mostly community release, made the observer pause and keep the work instead of dropping memories when the provider refuses (an empty Anthropic credit balance, a blocked organization, or a local model server down) and fixed non-ASCII Windows home folders; v13.36.1 fixed a server-runtime leak where `<private>` sections still left the hook and were stored in the server's raw event record until prompt build (the default worker runtime was not affected); and v13.37.0 repaired the marketplace update of v13.36.1 itself, which had shipped built plugin files containing leftover `git stash` conflict markers, so auto-updated installs failed to start the worker and MCP search and memory capture stopped until upgrade (the npm package was published before the bad change and was unaffected).
The 2026-10-13-to-17 train continued at the same clip: v13.38.0 stopped the Windows console-window flashing by having every hook launch claude-mem directly in exec form with 16 community fixes from five contributors, v13.39.0 restored the memory timeline to Codex subagent threads after compaction through a new PostCompact hook, v13.40.0 brought TeamBrain team joins to the terminal (`npx claude-mem teambrain join` with device-code sign-in and per-project sharing), and v13.41.0 added build, release, and work-state visibility workflow skills that delegate through make-plan, do, and babysit.
The same day closed the v13 line: v14.0.0 shipped My Work, a free local dashboard that lists the requests you gave your agents as cards with plain-language summaries, live statuses, and a human review step so an agent's "done" is never mistaken for a person's confirmation, and it moved TeamBrain from design-partner pilot to self-serve at $50 per seat per month; v14.0.1 followed within the hour, while cmem.ai/pricing still described TeamBrain as an unpriced pilot when fetched 2026-10-18.
v15.0.0 (2026-10-20) opened the next line by making Smart memory search the default recall path, a three-step flow where the agent searches the compact index, inspects context around relevant results, and fetches only selected details, reasoning between the steps, with the old one-call lookup demoted to an explicit `dumb_search`; v15.0.1 the same day fixed project-scope consistency so observations found through a merged project alias stay reachable across the flow's steps, and v15.0.2 (2026-10-23) disabled reasoning on observer model calls so reasoning tokens stop consuming the output budget.
v15.1.0 (2026-10-25) rebuilt the My Work dashboard as a React viewer on live worker data that is always live, moved per-prompt semantic injection into server mode, added an opt-in loopback HTTP MCP transport with per-session workspaces, and broadened secret redaction to lowercase-named AWS secret keys, PGP private key blocks, and encrypted PKCS#8 keys.
Later the same day, v15.2.0 gave fresh installs a browser setup funnel that reads the last 30 days of supported local agent history, filters and redacts it, and uploads the filtered owner prompts to CMEM Cloud for hosted intent extraction before setup finishes, with anonymous installs getting a private installation credential; v15.2.1 (2026-10-25) changed no runtime behavior and only moved npm publishing to OIDC trusted publishing with provenance attestations, fixing a publish path that had failed on every tag since v13.26.1.
v15.3.0 (2026-10-26) added Deliverables to the My Work card: the Stop hook copies what a turn produced (decks, reports, pages, attached files) into `~/.claude-mem/deliverables/<project>/` under content-addressed names so the copy outlives the worktree or scratch folder it was made in, the worker serves each copy over loopback, entirely-`<private>` turns leave no copy, and `CLAUDE_MEM_DELIVERABLES_ENABLED=false` turns the feature off.
v15.4.0 (2026-10-28) rebuilt My Work around Focus areas: a MY FOCUS rail lists your focus areas in priority order with a needs-you count on each, every request sits in exactly one area or in Other, area pages carry a goal sentence with combined progress and the asks not yet started, new areas are suggested automatically with keep, rename, merge, or dismiss per suggestion, and the My Goals page is retired into the area pages.

## Strengths

- Local-first by default: everything lives in `~/.claude-mem/`, with `<private>` tags excluding sensitive content and no account required.
- Token-aware retrieval design: progressive-disclosure search keeps the injection cost bounded instead of dumping raw history.
- One engine covers the harness landscape, so memory survives switching between Claude Code and OpenCode.
- Real adoption: the npm and star numbers make it the most-installed dedicated memory layer for coding agents.

## Cautions

- Compression runs an LLM call on every tool observation, often 100+ times per session, billed to your own quota; a competing memory author publicly calls the capture-everything family noisy and token-expensive.
- The cloud tier's own docs warn that enabling sync uploads observation narratives and full prompt text to your cmem.ai account.
- The v15.2.0 browser setup funnel makes that upload the default first-run path for fresh installs: the last 30 days of owner prompts leave the machine for CMEM Cloud's hosted extraction during setup, filtered and redacted by the configured rules but still an outbound default (release notes, 2026-10-25).
- Operational surface is real: a background worker on a local port, optional Bun, Python, and Chroma dependencies, and a documented `npm install -g` footgun that installs the SDK without hooks.
- The README's association with a third-party CMEM crypto token is a credibility smell some buyers will not overlook.

## Pricing

The engine is free and Apache-2.0, fully local.
The commercial arm restructured on 2026-10-06: CMEM Pro is $30/month for hosted observation and cloud sync (private MCP link, memory generation on the hosted observer) after a 30-day free trial, Heavy is $70/month with more included usage, and CMEM Max is $100/month with the largest allowance plus billed overages, each with a usage allowance and automatic upgrade settings.
The former CMEM Cloud $20/month plan and the $333/seat/month Team tier are gone; the team product (TeamBrain) moved to self-serve at $50/seat/month with v14.0.0 on 2026-10-17, though cmem.ai/pricing still listed it as a design-partner pilot with pricing unannounced when fetched 2026-10-18.
The hidden cost is compression: those LLM calls draw on your own model subscription or API budget, and no official per-session figure is published.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09 | CMEM Cloud | Baseline: engine free (Apache-2.0); CMEM Cloud $20/mo for sync and one private MCP link, Team $333/seat/mo for 3-50 seats. | [claude-mem.ai](https://claude-mem.ai) |
| 2026-10-06 | CMEM Pro, Heavy, CMEM Max | CMEM Cloud $20/mo and Team $333/seat/mo replaced: CMEM Pro $30/mo, Heavy $70/mo, CMEM Max $100/mo (allowance tiers with billed overages); TeamBrain pilot has no public price. | [cmem.ai/pricing](https://cmem.ai/pricing) |
| 2026-10-06 | CMEM Pro | 30-day free trial restored as the public offer, from the shorter "up to 14 days" wording; $30/mo unchanged. | [cmem.ai/pricing](https://cmem.ai/pricing) |
| 2026-10-17 | TeamBrain | Self-serve at $50/seat/mo, from a design-partner pilot with no public price; announced in the v14.0.0 release notes, with the pricing page still showing the pilot at fetch. | [v14.0.0 release](https://github.com/thedotmack/claude-mem/releases/tag/v14.0.0) |

## Compared to

- [File-based agent memory](../file-based-agent-memory/index.md): free, transparent, version-controlled, best for stable facts; claude-mem automates recall of what happened, which files cannot do.
- [mem0](../mem0/index.md): a memory API for products you build; choose claude-mem when you are the end user of coding agents and want hooks already written.
- [Letta](../letta/index.md): a framework where memory is a runtime primitive for agents you architect; choose claude-mem to bolt memory onto agents you already run.

## Bottom line

**Recommended for heavy daily Claude Code or OpenCode users who feel the re-explaining tax every morning and accept the token bill for compression.**
Not for privacy-strict environments, anyone unwilling to run a local worker service, or small projects where a curated CLAUDE.md is still the right answer.

## Changes

- 2026-08-30 - Created as a memory note covering session capture, compression, and reinjection, with 92,602 stars recorded.
- 2026-09-06 - Recorded the README rebrand to Grok Mem and the added Cursor and Grok Bot marketplace plugins.
- 2026-09-16 - Recorded the npm/GitHub release lag (npm at 13.25.1, the releases page still on v13.24.23) and refreshed stars to 94.0k with 191 open issues and PRs.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-22 - The npm-versus-GitHub channel drift closed: GitHub tagged v13.25.3 and npm published 13.25.3 within minutes on 2026-09-21, so the two release channels are back in sync.
- 2026-09-27 - Refreshed the volatile facts: about 94.8k stars, 312 open issues and PRs, 68,101 trailing-month npm downloads, and release v13.28.0 (2026-09-26) with npm in sync.
- 2026-10-03 - Recorded GitHub release v13.29.0 (2026-10-03) with npm lagging at 13.28.0 at fetch time, the first channel drift since 2026-09-21; refreshed stars to about 95.2k, 109 open issues and PRs, and 68,674 trailing-month npm downloads.
- 2026-10-04 - The npm-versus-GitHub channel drift closed: npm published 13.29.0, matching the v13.29.0 GitHub tag; refreshed stars to about 95.6k, 8.5k forks, and 128 open issues and PRs.
- 2026-10-05 - Recorded the v13.30.0, v13.30.1, and v13.31.0 releases (spooled hooks, cacheable observer prompts, indexed SessionStart) with npm in sync at 13.31.0; refreshed stars to about 96.3k, 105 open issues and PRs, and 68,891 trailing-month downloads.
- 2026-10-06 - Recorded the v13.31.1 and v13.32.0 releases (the cloud-sync firewall fix, and the File Read Gate restored on by default) with npm in sync at 13.32.0; refreshed stars to about 96.7k, 87 open issues and PRs, and 69,573 trailing-month downloads.
- 2026-10-06 - The commercial arm restructured its pricing: CMEM Cloud $20/mo and Team $333/seat/mo replaced by CMEM Pro $30/mo, Heavy $70/mo, and CMEM Max $100/mo, with TeamBrain a design-partner pilot without a public price (Price history row); the pricing reference repointed to cmem.ai, which claude-mem.ai now redirects to.
- 2026-10-07 - Added the thedotmack/claude-mem star history chart to the Status section.
- 2026-10-07 - Recorded the v13.34.0 through v13.34.2 releases (first-party Pi and DeepSeek Harness integrations, the CMEM Pro trial restored to 30 days, and the observer prompt-cache regression fix) with npm in sync at 13.34.2 and appended the trial-terms Price history row.
- 2026-10-09 - Recorded the v13.35.0 release (one guided mem_search tool replacing the multi-tool surface, curated text replies instead of raw JSON, an explicit save_memory note tool, a native-memory-lookup bridge for Claude Code and Codex, and an opt-in markdown-note watcher) with npm in sync at 13.35.0; refreshed stars to about 98.7k and downloads to 72,524.
- 2026-10-13 - Recorded the v13.36.0, v13.36.1, and v13.37.0 releases (the observer pausing instead of dropping memories when the provider refuses, the server-runtime `<private>` leak fixed, and the broken 13.36.1 marketplace update repaired after it stopped memory capture on auto-updated installs) with npm in sync at 13.37.0; refreshed stars to about 100.2k (past 100k) and trailing-month downloads to 66,625.
- 2026-10-16 - Recorded the v13.38.0 and v13.39.0 releases (hooks calling claude-mem directly instead of through bash to stop the Windows console flash, sixteen community fixes, and the Codex memory timeline returning to subagent threads after compaction) with npm in sync at 13.39.0; refreshed stars to about 101.1k and trailing-month downloads to 68,478.
- 2026-10-17 - Recorded the v13.40.0 and v13.41.0 releases (TeamBrain team joins from the terminal with device-code sign-in and per-project sharing, and build, release, and work-state workflow skills delegating through make-plan, do, and babysit) with the Status train narrative extended to the full 10-13-to-17 run and npm re-verified in sync at 13.41.0.
- 2026-10-18 - Recorded the v14.0.0 and v14.0.1 releases (the free local My Work request dashboard with summaries, live statuses, and a human review step, and TeamBrain moving from design-partner pilot to self-serve at $50/seat/month, Price history row) with npm in sync at 14.0.1 and the pricing page's remaining pilot wording noted at fetch time.
- 2026-10-22 - Recorded the v15.0.0 release (Smart memory search now the default recall path: three-step index search, context inspection, and selective fetch with the agent reasoning between steps, and the old one-call lookup demoted to `dumb_search`) and the v15.0.1 project-scope consistency fix; npm re-verified in sync at 15.0.1.
- 2026-10-24 - Recorded v15.0.2 (October 23): observer model calls now disable reasoning by default so reasoning tokens stop consuming the output budget, with a logged single retry on empty length-capped replies; npm re-verified in sync at 15.0.2.
- 2026-10-25 - Recorded v15.1.0 (the React My Work viewer on live worker data that is always live, per-prompt semantic injection in server mode, an opt-in loopback HTTP MCP transport with per-session workspaces, and broader secret redaction) with npm in sync at 15.1.0; trailing-month npm downloads refreshed to 63,865 (2026-09-23 to 2026-10-22).
- 2026-10-26 - Recorded the same-day v15.2.0 and v15.2.1 releases: the browser install funnel that scans 30 days of local agent history and uploads filtered owner prompts to CMEM Cloud for hosted intent extraction as the default fresh-install path (new caution), and the npm OIDC trusted-publishing fix that repairs a publish path broken since v13.26.1; npm re-verified in sync at 15.2.1.
- 2026-10-27 - Recorded the v15.3.0 release (October 26): Deliverables on the My Work card, the Stop hook copying turn output into content-addressed project folders served over loopback, with private turns excluded and an off-switch; npm re-verified in sync at 15.3.0.
- 2026-10-28 - Recorded v15.4.0: My Work rebuilt around Focus areas (a priority-ordered MY FOCUS rail with needs-you counts, every request in exactly one area, goal-sentence area pages, and auto-suggested areas with keep, rename, merge, or dismiss), retiring the My Goals page; npm re-verified in sync at 15.4.0.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [File-based agent memory](../file-based-agent-memory/index.md) - the free convention it automates
- [Context Management Patterns](../../context-management-patterns/index.md) - the injection-cost problem it tries to bound
- [mem0](../mem0/index.md) - the API-layer alternative

## References

- https://github.com/thedotmack/claude-mem - repository, supported agents, install methods, license
- https://docs.claude-mem.ai/ - feature set, pipeline, supported IDEs
- https://docs.claude-mem.ai/architecture/overview - hook architecture and the compression flow behind the token-cost caution
- https://docs.claude-mem.ai/cloud-sync - the documented privacy trade-off of the cloud tier
- https://claude-mem.ai - pricing tiers and adoption stats (now redirects to cmem.ai)
- https://cmem.ai/pricing - the restructured CMEM ladder ($30/$70/$100); TeamBrain still described as an unpriced design-partner pilot with public pricing unannounced at the 2026-10-24 re-fetch
- https://github.com/thedotmack/claude-mem/releases/tag/v14.0.0 - the My Work dashboard announcement and the TeamBrain self-serve $50/seat/month pricing (2026-10-17)
- https://github.com/thedotmack/claude-mem/releases/tag/v15.2.0 - the browser install funnel: the 30-day history scan and the default owner-prompt upload to CMEM Cloud (2026-10-25)
- https://api.npmjs.org/downloads/point/last-month/claude-mem - the 75,274 monthly downloads (2026-09-11 to 2026-10-10) as of 2026-10-12
- https://news.ycombinator.com/item?id=47422611 - the critical take from a competing memory author on the capture-everything approach
