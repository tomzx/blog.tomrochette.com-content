---
title: Graft
created: 2026-09-12
updated: 2026-09-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, code-graphs, claude-code, open-source]
readability: 3
audience_notes: >
  Engineers wiring a coding agent to a large codebase, deciding between a readable map
  of the repo and an embedding index. Assumes you know what tree-sitter, MCP, and
  Claude Code hooks are.
---

Graft is an MIT-licensed CLI from NanoNets (attributed on its own site to Trail) that builds a repo's context graph as a folder of linked markdown files plus a tree-sitter code graph, then wires itself into coding agents through skills, hooks, a six-tool MCP server, and a statusline so the map rides along in every session.
Facts below verified as of 2026-09-12.

**Graft collected 7,276 stars in ten weeks on a story every agent user feels, yet every number behind that story, including the 54%-to-66% SWE-bench jump, is the vendor's own until someone replicates it, and distribution clearly ran ahead of independent validation.**

## What it is

**The graph is plain files your agent already reads, and the intelligence in them is opt-in.**
`graft build` parses 23 languages with tree-sitter into a per-symbol wiring graph, and an optional `--deep` pass (any LLM provider under your own key) writes `graft/*.md` concept nodes with plain-English summaries, crux code excerpts, and typed wikilinks like `depends_on` and `produces`.
The folder is a gitignored local cache like `node_modules`; what you commit is the wiring `graft init` drops into `.claude/`, `AGENTS.md`, and the MCP config, so teammates regenerate their own graphs.
Every query re-syncs the structural graph against the working tree first (about 3 ms, free, no model), so answers cover uncommitted edits; the CLI, MCP server, and Claude Code hooks add blast-radius warnings on every edit.
The npm scope and telemetry endpoint are NanoNets-branded, the product site attributes to Trail (trailhq.com), and Trail Brain, the hosted "company brain", is the upsell.

## Status

Young and very hot: created 2026-07-03, 7,276 stars and 664 forks by 2026-09-12, last push the day of verification, 128 open issues, v0.18.0 on npm with 34,055 downloads in the trailing month, all as of 2026-09-12 (GitHub and npm APIs).
**The community footprint is thin for the star count: a third-party Show HN drew 3 points and 2 comments, the creator's own follow-up reached 39 points and 44 comments, and its most substantive comments were criticisms.**
In that thread the creator confirmed the README's marketing register is model-written ("Opus 5 is very paranoid on giving proofs... so I let it keep this one line"), and the only cross-tool numbers anywhere (graft over Graphify, MRR 0.73 vs 0.38) are his own tests, not a published benchmark.
No independent benchmark or third-party evaluation exists as of 2026-09-12.

## Strengths

- **The delivery is the deepest in this category**: per-agent instruction files across nine surfaces, six MCP tools, post-edit hooks with blast-radius warnings, a live statusline, and auto-resync, so the map actually gets used instead of ignored.
- The structural layer is deterministic, key-free, and local, and the LLM layer is bring-your-own-provider, so the tool never sits between you and a model bill.
- Freshness is engineered rather than promised: millisecond structural re-sync per query, content-hash caching, and a `graft check` drift report.
- The telemetry posture is unusually explicit: a published allowlist contract with bucketed values, opt-out via `DO_NOT_TRACK=1`, and off by default in CI and source builds.

## Cautions

- **Every performance number is self-run**: the up-to-4x-cheaper and 3x-faster headline, the +46% tool-call, +42% token, and +60% time savings, and the 54%-to-66% SWE-bench Verified result (official harness, but their run, their repos, not on the public leaderboard).
- The differentiating plain-English summaries are the part the creator calls experimental, writing on HN that they are "still testing whether the summaries are worth it at all".
- The README's prose is LLM-written and commenters flagged the "empty calorie language" before the creator confirmed its origin, which tells you how much of the polish to discount.
- The detailed benchmark tables behind the 4x headline cover only PocketBase (a 21% cost cut), so the "up to" is doing real work.
- The Trail Brain upsell is aggressive ("a living skill file that learns from every task" is the hosted product, not this repo), 128 open issues is a lot for ten weeks, and the rename trail (context-graph-engine to Graft, NanoNets to trailhq) scatters canonical links.

## Pricing

Graft is free, MIT, no account; your only cost is the LLM usage the optional deep pass makes under your own key.
The money is in Trail Brain (as of 2026-09-12): Free ($0, 100 rules, 1 editor, 10K agent reads/month), Small ($20k/year), Medium ($60k/year), and Large ($150k/year with in-VPC and HIPAA BAA), priced on rules, editors, and monthly agent reads.

## Compared to

- [Graphify](../graphify/index.md): both are local, file-based graph tools with no vectors, but Graphify's graph is fully deterministic while graft's differentiating summaries are LLM-written; Graphify for structure only, graft for a map written in English.
- [Semble](../semble/index.md): Semble answers where-is-the-code with fused static embeddings and BM25; graft answers what-does-this-subsystem-do and who-depends-on-it with readable files and typed links.
- [Augment Code](../augment-code/index.md): Augment's real-time index is cloud-side and drives only its own harness; graft's map is local files any agent that reads files can use, with correspondingly less enterprise polish.

## Bottom line

I would try graft on a repo big enough that my agent visibly wanders, keeping the free structural layer as the default and treating every headline number as a hypothesis my own workload has to replicate.
I would not skip TELEMETRY.md for a compliance-sensitive team, and I would not buy Trail Brain on the strength of this repo, because the open-source map and the paid company brain are different bets.

## Changes

- 2026-09-12 - Created in the Context engines category during the three-entrant resolution run.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Context Management Patterns](../context-management-patterns/index.md) - the manual onboarding practice graft automates
- [Speeding up LLM work on a single codebase](../../speeding-up-llm-work-on-a-single-codebase/index.md) - the corpus article whose core problem graft attacks

## References

- https://github.com/NanoNets/Graft - repository, stats, topics, and rename (answers to trailhq/Graft), as of 2026-09-12
- https://raw.githubusercontent.com/NanoNets/Graft/main/README.md - architecture, benchmark tables, SWE-bench Verified numbers, delivery surfaces
- https://graft.nanonets.ai - product site, Trail attribution, and marketing claims
- https://raw.githubusercontent.com/NanoNets/context-graph-engine/main/TELEMETRY.md - the telemetry allowlist contract
- https://registry.npmjs.org/@nanonets/graft/latest - package version 0.18.0 and metadata
- https://api.npmjs.org/downloads/point/last-month/@nanonets/graft - 34,055 downloads, trailing month as of 2026-09-12
- https://hn.algolia.com/api/v1/items/49197687 - the 3-point Show HN and the creator's tree-sitter-only clarification
- https://hn.algolia.com/api/v1/items/49299985 - the 39-point thread: staleness, README register critique, and the vendor-run Graphify comparison
- https://trailhq.com/pricing - Trail Brain plans as of 2026-09-12
- https://trailhq.com - the vendor and the Trail Brain upsell positioning
