---
title: GBrain
created: 2026-10-07
updated: 2026-10-08
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

A local-first daemon ("your hardware, your DB, your keys") published under garrytan on GitHub, built in public to run the author's own OpenClaw and Hermes deployments.
Pages are explicit markdown with sources; durable preferences and facts can be shared across agents while transient task state stays local.
Retrieval starts keyless with keyword search, then layers semantic search, a typed knowledge graph with no-LLM auto-linking, and a synthesis layer that returns cited answers plus an explicit account of what the brain does not know yet.
Remote access ships as one command: `gbrain mcp expose` publishes the brain over MCP on a Tailscale tailnet (with a funnel mode for cloud agents such as Grok Bot and ChatGPT).
Guides cover Grok Bot, Muse, Codex, and Claude Code, plus a company-brain tutorial where remote clients are constrained by source and operation grants and visibility filters.
A shared-brain skill catalog lets approved editors publish memory skills beside the knowledge.

## Status

**Active, single-author-plus-contributors, and unusually eval-disciplined for a personal project.**
30,672 stars with the repository pushed 2026-10-08, created 2026-04-05, MIT, as of 2026-10-08 (GitHub API), with five or more contributors and a companion garrytan/gbrain-evals repository (431 stars, pushed 2026-10-07) holding dated benchmark reports.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=garrytan/gbrain&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=garrytan/gbrain&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=garrytan/gbrain&type=date&theme=dark&legend=top-left" />
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
- The authorization model is explicit that its tests exercise specific access paths, not a universal no-leak guarantee, and local files plus shared database credentials are a different trust boundary.
- The benchmark numbers are self-published and self-judged (the verification record itself notes the answer judgments do not support independent re-judging), and the deployment evidence is one famous user's own brain.
- Markdown export is not a full database backup, and a founder-driven project this personal carries bus-factor and scope risk no corporate vendor has.

## Pricing

Pricing does not apply: free and open under MIT, with the costs being your hardware, database, keys, and any configured cloud providers.

## Compared to

- [Engrim](../engrim/index.md): the cross-CLI episodic engine with origin-agent provenance in SQLite; GBrain is markdown-page-based with human-editable pages and a graph, Engrim is turn-level records tuned for coding sessions.
- [File-based agent memory](../file-based-agent-memory/index.md): the convention GBrain extends; the convention stores notes in the repo, GBrain adds sources, corrections, withdrawal, retrieval, and cross-agent serving.
- [Memoryfields](../memoryfields/index.md): the portability spec; GBrain is a running daemon whose pages are portable but whose graph and enrichment stay local.

## Bottom line

**Recommended for people running two or more agents who want one inspectable, correctable brain with provenance, and who value published eval discipline over vendor polish.**
Not for teams needing supported infrastructure, contractual isolation, or a multi-user hosted service.

## Changes

- 2026-10-07 - Created from the 2026-10-07 awesome-list entrant scan, with seven fetched sources and the self-published-benchmark-plus-single-famous-user profile recorded as the critical angle.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Engrim](../engrim/index.md) - the other cross-agent local memory engine, turn-level where this is page-level
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention this extends with provenance and serving
- [Memoryfields](../memoryfields/index.md) - the format-spec sibling of the explicit-pages position

## References

- https://github.com/garrytan/gbrain - repository, MIT license, 30,672 stars, activity, as of 2026-10-08
- https://raw.githubusercontent.com/garrytan/gbrain/master/README.md - the page model, corrections and withdrawal, MCP serving, the 155,795-page deployment claim, and the BrainBench comparison
- https://github.com/garrytan/gbrain-evals - the companion evals repository (431 stars) with dated benchmark reports and verification records
- https://raw.githubusercontent.com/garrytan/gbrain-evals/main/docs/benchmarks/2026-09-09-retrieval-refresh.md - the September 9 retrieval refresh: 95.53 percent all-evidence LongMemEval retrieval, the flagged 433-of-500 answer count, and the October 4 opaque-id re-count
- https://hn.algolia.com/api/v1/search?query=gbrain&tags=story - the discussion record (9-point April thread, 5-point May commentary, 23-point June skill thread)
- https://api.github.com/repos/garrytan/gbrain/license - the MIT LICENSE file, verified through the GitHub API
- https://hn.algolia.com/api/v1/items/48514124 - the 23-point third-party visualization-skill thread (2026-06-13), the largest community record
