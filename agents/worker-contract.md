---
build:
  render: never
  list: never
  publishResources: false
title: Worker contract
created: 2026-10-16
updated: 2026-10-16
status: finished
tags: [agents]
readability: 0
---

# Worker contract (agents section)

You are a worker in the daily refresh of the agents section of this repository.
This file plus the files named under Reads are everything you need; read nothing else by default.
The rules here mirror `agents/AGENTS.md`; that file stays canonical, and the daily refresh keeps this copy in sync with it.

## Reads

1. `agents/worker-contract.md` (this file).
2. `agents/standing-decisions.md`, the scope digest: standing rejections, family scopes, routing precedents, re-review triggers. Consult it before any admission or rejection.
3. Your work list at `agents/worklists/<category>.yaml`: members with slugs, titles, subject repositories, and last-verified dates, the mapped sources with their last-checked dates, and the queue questions governing the scope.

The dispatch message names your category, the repo-root path, your scope path, and any extra context.
Do not read `agents/AGENTS.md`, `agents/queue.md`, or `agents/_index.md`; everything you need from them is here or in the work list.
Consult `agents/log.md` only on demand, when the digest and the work list lack history you actually need; no run requires you to read it.

## Write scope

- Only paths under your own category directory (or, for the section-root worker, the essay and matrix directories named in the dispatch).
- Never write: `agents/log.md`, `agents/queue.md`, `agents/_index.md`, `agents/standing-decisions.md`, `agents/worker-contract.md`, `agents/worklists/`, `agents/AGENTS.md`, `agents/starred-checkpoint.txt`, or anything outside your scope.
- Leave the owner's unrelated working-tree changes untouched.
- The coordinator writes shared files from your report; propose shared-file lines, never write them yourself.

## Every run

- Check links, front matter (no `type` field, mandatory tags present), and as-of dates; fix what is broken.
- Keep the feature matrix matched to membership: columns sorted case-insensitively by member title, the separator row and every row at header width, membership checked by link slug.
- Keep the category `_index.md` entry list matched to membership and alphabetical; its `## Changes` stays append-only.
- Re-check category fit; propose cross-category moves rather than making them.
- Volatile re-verification, activity-gated: members whose subject released, repriced, or changed status since their last-verified date; the work list flags these. **Star figures are exempt everywhere**: the star-history chart is the live signal, and existing star counts (note prose, matrix cells, index one-liners) are never refreshed.
- Rotation: fully re-verify about one seventh of the category, oldest last-verified first (the work list names them), re-fetching every cited URL and fixing dead sources.
- Fully re-verify out of rotation, the same run, any note a signal says is wrong.

## Entrant scan

- Fetch the mapped sources named in the work list and cross-check every listed repository against membership.
- A source unchanged since its last check (commit history suffices to show that) carries its scan over; scan only additions.
- Resolve every new candidate in the same run: a note if it clears the citation bar below, otherwise an explicit rejection with reasons. Standing family rejections in the digest apply without re-deriving.
- Cross-category candidates are report-only; never write notes outside your scope.

## Note format

Research notes carry: `title`, `created`, `updated`, `status`, `tags` (`[research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, <content tags>]`; never remove an existing `llm=` tag), `readability: 3`, and `audience_notes` (folded `>`). Never set a `type` field.
Section order: one-sentence definition, `## What it is`, `## Status`, `## Strengths`, `## Cautions`, `## Pricing`, `## Compared to`, `## Bottom line`, then `## Changes`, `## See also`, `## References` in that order.
`## Changes` is append-only, one `- YYYY-MM-DD - <what changed>` bullet per material change, oldest first, first bullet records creation; routine volatile refreshes get no bullet.
A pricing section stating actual prices needs `## Price history` immediately after it: an append-only, sourced, oldest-first table (Date, Plan, Change, Source), seeded at creation and appended the run a price or tier changes.
People-and-publications notes carry `## Top 5 recommended reading` between `## Bottom line` and `## Changes`, five linked pieces of the person's own output, one line each, best first, every URL fetched in the run that writes it.
A note whose subject is one GitHub repository carries this chart in `## Status`, after the status prose:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=OWNER/REPO&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=OWNER/REPO&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=OWNER/REPO&type=date&legend=top-left" />
</picture>
```

Subjects without a repository (websites, specs, people, closed products) carry no chart; multi-repository subjects may comma-separate repositories only when every one exists.
Set `updated:` to the run date on any revision.

## Citation bar

- Minimum 5 primary sources fetched in this run, primary first (repo, docs, pricing page, announcements).
- At least one critical or skeptical source when one exists; a missing community footprint is itself a signal to state.
- Volatile numbers carry "as of <date>". Stars are fetched once, at creation, as the dated baseline, and never refreshed afterward.

## Style

- First person, one sentence per line, no em- or en-dashes.
- Never the words shape, honest, load bearing; avoid "real" in new prose (existing uses are documented exceptions; leave them).
- Internal links per the depth rules: same category `../<slug>/index.md`, other categories `../<category>/<slug>/index.md`, own category index `../_index.md`; verify every target exists on disk before adding it.
- External links must be durable and canonical, and every URL you cite must have been fetched in this run.

## Pacing

- The model provider rate-limits hard under parallel load: fetch in small batches, and on any rate-limit error wait and retry instead of giving up.

## Report

Reply with: every file changed or created (one line each), the proposed log lines, each entrant candidate resolved or rejected with a one-line reason, cross-category flags (report only), and anything you could not finish and why.

## Variants

- Cross-category scanner: no category; the dispatch names the broad sources, the checkpoint handling, and the governing queue questions. Writes nothing under `agents/` except by coordinator instruction; reports candidates and routing flags.
- Section-root worker: the essays and the model-provider matrix; same duties per run (links, as-of dates, volatile numbers minus stars, tracker as-of clause in the first paragraph), same style and report rules.
