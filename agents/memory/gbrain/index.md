---
title: GBrain
created: 2026-10-07
updated: 2026-11-08
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
30,910 stars as of 2026-10-16 (GitHub API), with the repository pushed 2026-11-08, created 2026-04-05, MIT, as of 2026-11-08 (GitHub API), with five or more contributors and a companion garrytan/gbrain-evals repository (439 stars as of 2026-10-16, pushed 2026-10-20) holding dated benchmark reports.
The README now fronts a hosted service, gbrain.io, a YC-backed team workspace ("Built by Garry Tan") that sells the same brain as a subscription, so the deployment model is no longer self-host-only.
The release train has continued past the September refresh to v0.60.463.0 (2026-10-26), whose headline is a security fix: a migration (v275) backfills row-level security onto every Postgres table still without it, after the four incremental-derivation tables added in v273 and some older tables could be left RLS-off, which on Supabase with the Data API on made them reachable with the anon key; v0.60.462.0 the same day fixed a fact-extraction write race that silently dropped facts when two notes saved close together named the same entity page.
Nine further releases landed by v0.60.472.0 (2026-10-27): the notable ones are v0.60.468.0, which requires Bun 1.4.4 or newer to fix a TLS-Postgres connection that grew unbounded until a memory guard killed it (and carries the Brotli fix for CVE-2026-111497), and v0.60.470.0, which closed a hole where any database session could create an empty table named like a purge list and have purged or forgotten content stored again, with the rest covering killed-sync visibility, `--flag=value` handling, a v265 upgrade fix, and a crashed sources refresh no longer wedging the managed checkout.
v0.60.479.0 (2026-10-28) fixed the upgrade path itself: a brain created before v0.60.412.0 never recorded the old v0.13.1 migration, so upgrading it re-ran that migration, stamped `validate: false` into every page's frontmatter, and changed every content hash, desyncing a repo brain's database from the files in git; the stamp is now recorded as complete and the upgrade changes no page.
Twenty-six releases followed through v0.60.505.0 (2026-10-30), and the notable cluster is privacy: three releases (v0.60.483.0, v0.60.485.0, v0.60.487.0) close the hole where a page asking for `visibility: private` in a spelling the privacy reader does not parse (capitalization, block scalars, lists) synced or imported world-readable, now held as `visibility_noncanonical` or refused with `visibility_not_applied`; v0.60.486.0 stops a remote agent from rewriting where a page came from and stops provenance removal from raising trust, with a `gbrain repair provenance` command that only lowers trust. Behavior moved too: the brain-first rule now rides every turn in every harness install instead of the system prompt alone (v0.60.495.0, v0.60.498.0, v0.60.505.0, the last also failing an unloadable per-turn hook instead of passing quietly), search supersedes corrected facts (v0.60.493.0, corrections ahead of the retracted fact in 27 of 27 replayed reads), and a budgeted `query` leads with the question's dated saved facts, answering 183 of a sealed 200-question set against 151 without it (v0.60.491.0).
Thirty-one more releases ran through v0.60.536.0 (2026-11-01), and the notable cluster is injection defense and scope narrowing: the quoted-as-source fence that started on conversation pages extends to agent-written, ingested, and unverified-origin text on every read, with embedded tool calls summarized (v0.60.507.0, v0.60.521.0, v0.60.536.0), `recall` and `list_pages` now honor the per-request source narrowing `search` already had (v0.60.522.0), shared brains gain an opt-in private-pages grant so a member's agent reads only that member's private pages (v0.60.527.0), a worker's turns can be attributed to the agent rather than the user with `GBRAIN_SESSION_AGENT` (v0.60.523.0), and an unnamed search limit now returns at most 3 meaning-only matches, a change whose own harness run took tasks passed from 0 of 39 to 18 of 40 (v0.60.506.0), with the rest covering sync, repair, and CI paths.
Twenty-three more ran through v0.60.559.0 (2026-11-03), whose headline is an opt-in `--skill-loading spring` mode: setup writes a compact one-line-per-skill index beside the brain-first block instead of copying every bundled skill into the harness's native skills directory (Claude Code lists about 87 per turn and mostly ignores them), and the agent loads a skill's full text on demand, an A/B run through the Claude Code and Codex CLIs themselves across three frontier models got the right skill loaded before acting in 29 of 36 Claude Code trials against 15 with native skills and 0 with none, tied native on Codex at 22 of 24, for about a quarter of native's standing per-turn tokens.
Four more ran through v0.60.570.0 (2026-11-04): `ship` now carries its unit, serial, slow, and E2E test lanes from a passed full-CI run instead of re-running them (v0.60.567.0), an engine opened from settings keeps its file operations in its own storage config with a new `file_verify` (v0.60.568.0), SkillOpt's iterative loop is deprecated with removal on or after 2026-12-03 after every edit it kept proved to come from its first step at about 1.8 times the cost (v0.60.569.0), and get_page accepts GPT-style calls that fill several window selectors at once instead of refusing them, the old refusal having failed 52 percent of GPT-6.1 Sol's briefing reads and 84 percent of its fact-check reads in a SkillOpt re-read (v0.60.570.0).
Thirty-one more ran through v0.60.601.0 (2026-11-04 to 07), and the notable ones: v0.60.575.0's Train R makes searches find pages by identifier or handle (`#412`, `INV-2026-00417`, `dan-example`) and adds `gbrain find`/`find_pages`; v0.60.578.0's memory train makes `forget` edit the page files first, lets `recall` weigh how far a fact deserves belief, gives page versions a human-readable reason with date access, and lets agents read and switch the saving rules; v0.60.587.0 lets an HTTP MCP caller label which AI made a write (`X-Gbrain-Agent-Label`), with attribution reads showing it; v0.60.589.0 adds opt-in Wakeshift wakes so a conversation is woken when a job it started finishes; v0.60.595.0 closes a shared-channel privacy hole where a `memory_recall` naming sources could read as the attested person and recall one member's private facts into a shared channel; and v0.60.601.0 is a security wave from a `/cso` audit that closes four remote-surface holes on `gbrain serve --http` and `gbrain mcp expose`, including a write-scoped token that could replace, through `POST /ingest`, pages every MCP write refuses it.
Twelve more ran through v0.60.613.0 (2026-11-08), and the headline is distribution: installs now follow a stable channel by default, a stable tag that moves only to a release whose exact tree passed the production soak (promoted within a day for important fixes, otherwise weekly), ending the every-release upgrade train (v0.60.604.0 through v0.60.606.0), while a TLA+ model of the refresh write barrier and its deferred-write queue runs in CI (v0.60.602.0); the ingest-capture path got three race fixes (a dropped capture no longer answers 202 and an unsigned webhook can no longer time-probe which repositories a brain syncs, a pre-channel retry no longer queues a second stale write, and a re-run capture no longer reverts a newer page edit), v0.60.612.0 stops page writes and managed fact extractions from retiring facts the page's fence never held with `gbrain repair unwithdrawn-facts` restoring ones already retired, and doctor's foreign_writers check now fails closed on unreadable ledgers and skipped repository roots.

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
- 2026-10-28 - Recorded v0.60.479.0: upgrades of brains created before v0.60.412.0 no longer re-run the v0.13.1 migration, stamp `validate: false` into every page, and re-hash every page (the change that desynced repo brains from git); the stamp is recorded as complete and the upgrade changes no page.
- 2026-10-30 - Recorded the train's continuation to v0.60.505.0 (twenty-six releases, October 28-30): the privacy cluster that holds or refuses pages asking for `visibility: private` in a spelling the privacy reader does not parse (previously synced world-readable), provenance no longer rewritable by remote agents, the brain-first rule riding every turn in every harness install, search superseding corrected facts (27 of 27 replayed reads), and the dated-saved-facts lead in budgeted queries (183 of 200 sealed questions answered versus 151).
- 2026-11-01 - Recorded the train's continuation to v0.60.536.0 (thirty-one releases, October 30 to November 1): quoted-as-source fences extended to agent-written, ingested, and unverified-origin text on every read, recall and list_pages honoring per-request source narrowing, opt-in per-member private-page grants on shared brains, worker-session attribution via GBRAIN_SESSION_AGENT, and the default search limit capping meaning-only matches at 3 pages (tasks passed 0 of 39 to 18 of 40); pricing re-verified unchanged (Personal $49/mo, Teams $199/mo).
- 2026-11-03 - Recorded the train's continuation to v0.60.559.0 (twenty-three releases, November 1 to 3): the opt-in spring skill-loading mode writes a compact skill index beside the brain-first block instead of copying all bundled skills into the harness directory, cutting standing tokens to about a quarter of native while raising right-skill-first loads on Claude Code (29 of 36 A/B trials versus 15 native).
- 2026-11-04 - Recorded the train's continuation to v0.60.570.0 (four releases, November 3-4): ship lanes carried from passed full-CI runs, per-engine file storage for settings-opened brains with file_verify, the SkillOpt iterative loop deprecated for removal on or after 2026-12-03, and get_page accepting the multi-selector GPT-style calls the old refusal failed on 52 percent of briefing reads; the push date refreshed to 2026-11-04.
- 2026-11-07 - Recorded the train's continuation to v0.60.601.0 (31 releases, November 4-7): Train R identifier and handle search with `gbrain find`, the memory train (forget edits files first, recall belief weighing, reasoned page versions, agent-readable saving rules), HTTP MCP agent attribution, opt-in Wakeshift job-finish wakes, the shared-channel privacy fix on source-scoped memory_recall, and the four-hole `/cso`-audit security wave on serve --http and mcp expose; the push date refreshed to 2026-11-07.
- 2026-11-08 - Recorded the train's continuation to v0.60.613.0 (12 releases, November 7-8): installs now follow a stable channel by default (a soak-gated stable tag promoted daily for important fixes, otherwise weekly, ending the every-release upgrade train), a TLA+ model of the refresh write barrier runs in CI, the ingest-capture path's three race fixes closed (no 202 on dropped captures with webhook timing hardened, no stale second write from pre-channel retries, no newer-edit reverts from re-run captures), v0.60.612.0 stopped fence-external fact retirement with the unwithdrawn-facts repair, and doctor's foreign_writers check fails closed; the push date refreshed to 2026-11-08.

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
- https://github.com/garrytan/gbrain/releases/tag/v0.60.559.0 - the spring skill-loading release: the compact skill index, its A/B numbers, and the itemized setup and doctor changes (2026-11-03)
