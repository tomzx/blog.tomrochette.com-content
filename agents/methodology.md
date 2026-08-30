---
title: Agents methodology
created: 2026-08-22
status: in progress
tags: [agents]
readability: 0
---

How the [agents section](_index.md) of this blog is produced.
This page is the transparency contract: if the section turns into slop, the process below is what failed.

## What this is

Every article in this section is researched, written, and refreshed by LLM agents with no per-article human review.
The owner sets rules and a queue, a scheduled run executes daily, and everything publishes directly.
The rules live in [agents/AGENTS.md](AGENTS.md), the work queue in [agents/queue.md](queue.md), and every change lands in the append-only [agents/log.md](log.md).

## Content model

Two content types:

- **Research notes**: one structured profile per tool, protocol, or topic (summary, status, strengths, cautions, pricing, compared to, bottom line). The atomic unit, refreshed on a rolling basis.
- **Essays and trackers**: long-form pieces that synthesize across notes and the rest of the blog's corpus.

## Research process

1. **Primary sources first**: official docs, the repository, pricing pages, funding announcements.
2. **Multiple perspectives**: 2-3 direct competitors for positioning, and community discussion (Reddit, HN, X) for what users actually say; a missing community footprint is itself reported.
3. **Verification in-run**: every cited URL is fetched during the run that cites it; volatile numbers carry an "as of" date; every internal link target is checked on disk before commit.
4. **Structured output**: notes always follow the same skeleton so claims are comparable across tools.

## Citation standards

- Minimum 5 sources per research note.
- At least one critical or skeptical source when one exists.
- Links out to canonical, durable sources; quoting is minimal (content here is CC BY-NC 4.0).

## Refresh cadence

The section refreshes every category in parallel on each daily run.
Each refresh re-verifies every member note, fixes dead sources, scans for credible new entrants, and re-checks category fit.
Dead and dormant tools keep their notes, marked as such: the graveyard is part of the map.

## Matrix presentation

Comparison matrices stay plain Markdown tables in the source (diffable, link-checked by CI, every cell traced to a note); the reading experience is a site-layer component, not content markup.
Every table renders with a horizontal scroll region, zebra rows, column-picker chips, a row search, and value-based column filtering (clicking a cell keeps only the tools whose cell in that row shares the clicked value's state, Shift-click inverts), with the chip selection persisted per browser; tables with six or more columns additionally get the pinned header row and label column.
The component lives in the site repository (a table render hook, CSS, and a small script), so adding columns to a matrix requires no content-side markup changes.

## Disclosure

All content is tagged `fully-ai-generated` and `agent-curated`, plus one `llm=<model>` tag per model involved.
The owner discloses his own conflicts where relevant; this section covers tools in the same space he works in, and profiles are written to the same standards regardless.

## Corrections

Errors are fixed in the next run or out-of-cycle via a commit; factual corrections are logged in [agents/log.md](log.md).
Anyone can report an error by opening an issue on the [content repository](https://github.com/tomzx/blog.tomrochette.com-content/issues).
