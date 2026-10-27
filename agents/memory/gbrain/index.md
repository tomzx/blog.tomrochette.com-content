---
title: GBrain
created: 2026-10-07
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, provenance, mcp, personal-knowledge]
readability: 3
audience_notes: >
  Engineers running several personal agents who want one inspectable, provenance-tagged
  memory daemon profiled against the episodic engines and the file conventions.
  Assumes you know what MCP is and are comfortable running a local service.
---

GBrain is Garry Tan's MIT-licensed personal agent-memory daemon: it stores explicit markdown pages with their sources, supports corrections and withdrawal as first-class operations, and serves the same memory to any agent over MCP, with optional semantic search, background enrichment, a typed knowledge graph, and cited synthesis.

**Its bet is that an agent's memory should be an explicit, correctable record you own, not a learned embedding blob, and its proof is that the author runs it as his production brain: 155,795 pages, 24,589 people, and 5,340 companies maintained by 66 cron jobs, with a companion evals repository that publishes its own defects.**

## What it is

A local-first daemon ("your hardware, your DB, your keys") published under garrytan on GitHub, built in public to run the author's own OpenClaw and Hermes deployments, with a hosted team-workspace service at gbrain.io beside it.
Pages are explicit markdown with sources; durable preferences and facts can be shared across agents while transient task state stays local.
Retrieval starts keyless with keyword search, then layers semantic search, a typed knowledge graph with no-LLM auto-linking, and a synthesis layer that returns cited answers plus an explicit account of what the brain does not know yet.
Remote access ships as one command: `gbrain mcp expose` publishes the brain over MCP on a Tailscale tailnet (with a funnel mode for cloud agents such as Grok Bot and ChatGPT).
Guides cover Grok Bot, Muse, Codex, and Claude Code, plus a company-brain tutorial where remote clients are constrained by source and operation grants and visibility filters.
A shared-brain skill catalog lets approved editors publish memory skills beside the knowledge.

## Status

**Active, single-author-plus-contributors, and unusually eval-disciplined for a personal project.**
30,910 stars as of 2026-10-16 (GitHub API), with the repository pushed 2026-10-20, created 2026-04-05, MIT, as of 2026-10-20 (GitHub API), with five or more contributors and a companion garrytan/gbrain-evals repository (439 stars as of 2026-10-16, pushed 2026-10-20) holding dated benchmark reports.
The README now fronts a hosted service, gbrain.io, a YC-backed team workspace ("Built by Garry Tan") that sells the same brain as a subscription, so the deployment model is no longer self-host-only.
The release train has continued past the September refresh to v0.60.463.0 (2026-10-26), whose headline is a security fix: a migration (v275) backfills row-level security onto every Postgres table still without it, after the four incremental-derivation tables added in v273 and some older tables could be left RLS-off, which on Supabase with the Data API on made them reachable with the anon key; v0.60.462.0 the same day fixed a fact-extraction write race that silently dropped facts when two notes saved close together named the same entity page.
Nine further releases landed by v0.60.472.0 (2026-10-27): the notable ones are v0.60.468.0, which requires Bun 1.4.4 or newer to fix a TLS-Postgres connection that grew unbounded until a memory guard killed it (and carries the Brotli fix for CVE-2026-111497), and v0.60.470.0, which closed a hole where any database session could create an empty table named like a purge list and have purged or forgotten content stored again, with the rest covering killed-sync visibility, `--flag=value` handling, a v265 upgrade fix, and a crashed sources refresh no longer wedging the managed checkout.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=garrytan/gbrain&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=garrytan/gbrain&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=garrytan/gbrain&type=date&legend=top-left" />
</picture>

The September 9, 2026 retrieval refresh (gbrain v0.48.4.0) reports all-evidence retrieval on 449 of 470 answerable LongMemEval questions (95.53 percent) and any-evidence on 469 of 470, with the machine-readable summary, saved receipts, and a verification record published; the 433-of-500 answer-judgment count was flagged for a leak (`answer_` session ids visible to the answer model) and re-counted with opaque ids on October 4, which confirmed the retrieval numbers.
The README's BrainBench comparison reports the graph adapter at precision@5 0.3421 and recall@5 0.9791 against 0.1917 and 0.6874 for plain hybrid retrieval.
The Hacker News record is modest: a 9-point memex launch thread (April 2026), a 5-point commentary thread (May), and a 23-point third-party visualization-skill thread (June), so the 30k stars in six months rest on the author's prominence and the eval discipline, not a community hub.

## Strengths

- **Corrections and withdrawal are first-class operations**, which most memory layers treat as an afterthought, and every page carries its sources, so "why does the agent believe this" has an answer.
- The evals repository is the honesty outlier in this category: planned matrices including losses, machine-readable summaries, and a self-flagged benchmark defect re-run with opaque ids.
- One brain serves every agent you run over MCP, with staged migration preserving sharing choices and personal edits.
- The synthesis layer returns actual answers with citations and gap analysis instead of a page list, and the gap analysis is the part that changes daily use.

## Cautions

- **Keyless does not mean private**: recalled memory reaches the harness model even in keyless mode, and configured cloud embedding, reranking, extraction, and synthesis providers receive text, so the trust boundary is your provider list, not the daemon.
- The authorization model is explicit that its tests exercise specific access paths, not a universal no-leak guarantee, and local files plus shared database credentials are a different trust boundary; the v0.60.463.0 RLS backfill (2026-10-26) is the record of a concrete gap in that model, four derivation tables left unprotected on migrations-only upgrades until the fix.
- The benchmark numbers are self-published and self-judged (the verification record itself notes the answer judgments do not support independent re-judging), and the deployment evidence is one famous user's own brain.
- Markdown export is not a full database backup, and a founder-driven project this personal carries bus-factor and scope risk no corporate vendor has.

## Pricing

The MIT daemon stays free, with the costs being your hardware, database, keys, and any configured cloud providers.
The hosted service, gbrain.io, sells two plans as of 2026-10-20: Personal $49/month and Teams $199/month (the whole team in one workspace at no extra seat cost, with $100 of AI credit per month).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-20 | Personal, Teams | Baseline: Personal $49/mo, Teams $199/mo (unlimited team seats, $100/mo AI credit); MIT daemon free. | [gbrain.io/pricing](https://gbrain.io/pricing) |

## Compared to

- [Engrim](../engrim/index.md): the cross-CLI episodic engine with origin-agent provenance in SQLite; GBrain is markdown-page-based with human-editable pages and a graph, Engrim is turn-level records tuned for coding sessions.
- [File-based agent memory](../file-based-agent-memory/index.md): the convention GBrain extends; the convention stores notes in the repo, GBrain adds sources, corrections, withdrawal, retrieval, and cross-agent serving.
- [Memoryfields](../memoryfields/index.md): the portability spec; GBrain is a running daemon whose pages are portable but whose graph and enrichment stay local.

## Bottom line

**Recommended for people running two or more agents who want one inspectable, correctable brain with provenance, and who value published eval discipline over vendor polish.**
Not for teams needing supported infrastructure, contractual isolation, or a multi-user hosted service.

## Changes
- 2026-10-07 - Created from the 2026-10-07 awesome-list entrant scan, with seven fetched sources and the self-published-benchmark-plus-single-famous-user profile recorded as the critical angle.
- 2026-10-20 - Recorded the hosted gbrain.io service the README now fronts (Personal $49/mo, Teams $199/mo, new Price history baseline) and the release train's continuation to v0.60.322.0.
- 2026-10-24 - Recorded the release train's continuation to v0.60.422.0 (October 24, tightened Postgres crash-robot CI ceilings, no memory behavior change).
- 2026-10-25 - Recorded the release train's continuation to v0.60.444.0 (six October 25 releases, repair steps now printing one commit-push command; still no retrieval behavior change).
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup: the light-theme source carried the dark-theme parameter; it now points at the default chart.
- 2026-10-26 - Recorded the train's continuation to v0.60.463.0: the v275 migration backfills row-level security onto every Postgres table, closing the RLS-off exposure the four v273 derivation tables carried on migrations-only upgrades (Supabase anon-key reachability), plus the v0.60.462.0 fact-extraction write-race fix; the authorization caution gains the gap's record.
- 2026-10-27 - Recorded the train's continuation to v0.60.472.0 (nine releases, October 26-27): the Bun 1.4.4 floor with the TLS-Postgres memory-growth and Brotli CVE fixes (v0.60.468.0) and the purge-guard hole closed, a temporary table no longer able to re-store purged or forgotten content (v0.60.470.0), with the rest covering killed-sync visibility, flag spelling, a v265 upgrade fix, and crashed-refresh recovery.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Engrim](../engrim/index.md) - the other cross-agent local memory engine, turn-level where this is page-level
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention this extends with provenance and serving
- [Memoryfields](../memoryfields/index.md) - the format-spec sibling of the explicit-pages position

## References

- https://github.com/garrytan/gbrain - repository, MIT license, 30,756 stars, activity, as of 2026-10-11
- https://raw.githubusercontent.com/garrytan/gbrain/master/README.md - the page model, corrections and withdrawal, MCP serving, the 155,795-page deployment claim, and the BrainBench comparison
- https://github.com/garrytan/gbrain-evals - the companion evals repository (436 stars) with dated benchmark reports and verification records
- https://raw.githubusercontent.com/garrytan/gbrain-evals/main/docs/benchmarks/2026-09-09-retrieval-refresh.md - the September 9 retrieval refresh: 95.53 percent all-evidence LongMemEval retrieval, the flagged 433-of-500 answer count, and the October 4 opaque-id re-count
- https://hn.algolia.com/api/v1/search?query=gbrain&tags=story - the discussion record (9-point April thread, 5-point May commentary, 23-point June skill thread)
- https://api.github.com/repos/garrytan/gbrain/license - the MIT LICENSE file, verified through the GitHub API
- https://hn.algolia.com/api/v1/items/48514124 - the 23-point third-party visualization-skill thread (2026-06-13), the largest community record
- https://gbrain.io/?ref=readme - the hosted service's landing page: team workspaces, YC backing, and the plain-file memory positioning
- https://gbrain.io/pricing - the hosted Personal $49/mo and Teams $199/mo plans and the $100/mo AI credit, as of 2026-10-20
- https://github.com/garrytan/gbrain/releases/tag/v0.60.463.0 - the RLS backfill release: every Postgres table guarded, the v273 derivation-table exposure named and closed (2026-10-26)
