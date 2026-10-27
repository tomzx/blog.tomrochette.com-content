---
title: Graft
created: 2026-09-12
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, code-graphs, claude-code, open-source]
readability: 3
audience_notes: >
  Engineers wiring a coding agent to a large codebase, deciding between a readable map
  of the repo and an embedding index. Assumes you know what tree-sitter, MCP, and
  Claude Code hooks are.
---

Graft is an MIT-licensed CLI from Trail (the company formerly branding itself NanoNets, which renamed the product Trail-code in October 2026) that builds a repo's context graph as a folder of linked markdown files plus a tree-sitter code graph, then wires itself into coding agents through skills, hooks, a six-tool MCP server, and a statusline so the map rides along in every session.

**Graft collected 9,051 stars in twelve weeks on a story every agent user feels, yet every number behind that story, including the 54%-to-66% SWE-bench jump, is the vendor's own until someone replicates it, and distribution clearly ran ahead of independent validation.**

## What it is

**The graph is plain files your agent already reads, and the intelligence in them is opt-in.**
`graft build` parses 24 languages with tree-sitter (Gleam joined in October 2026, with OCaml and Zig parsing symbols only) into a per-symbol wiring graph, and an optional `--deep` pass (any LLM provider under your own key) writes `graft/*.md` concept nodes with plain-English summaries, crux code excerpts, and typed wikilinks like `depends_on` and `produces`.
The folder is a gitignored local cache like `node_modules`; what you commit is the wiring `graft init` drops into `.claude/`, `AGENTS.md`, and the MCP config, so teammates regenerate their own graphs.
Every query re-syncs the structural graph against the working tree first (about 3 ms, free, no model), so answers cover uncommitted edits; the CLI, MCP server, and Claude Code hooks add blast-radius warnings on every edit.
The npm scope and telemetry endpoint are NanoNets-branded, the product site attributes to Trail (trailhq.com), and Trail Brain, the hosted "company brain", is the upsell.
In October 2026 the product renamed to Trail-code: the repository moved from trailhq/Graft to trailhq/Trail-Code, npm gained `@trailhq/trail-code` ("Formerly graft") beside the old `@nanonets/graft`, and the positioning widened from a context graph to a "self-learning context layer", the code map plus Learnings, the decisions and lessons a team's agents save and share with each other.

## Status

Young and very hot: created 2026-07-03, 10,084 stars by 2026-10-18, with 959 forks and 251 open issues and pull requests as of 2026-10-27, the repository renamed trailhq/Graft to trailhq/Trail-Code, the npm package `@trailhq/trail-code` at v0.26.0 ("Formerly graft") beside the still-published `@nanonets/graft` v0.23.0, which drew 84,196 downloads in the trailing month (2026-09-27 to 2026-10-26, summed from the range endpoint with eight zero days in the window, fetched 2026-10-27).
The 0.25.0 release (2026-10-23) extended the Learnings loop: a repository's skill now ships with its whole folder, a coding agent's use of a repo skill is reported to the workspace, and learning sync takes down learnings deleted at HEAD and syncs each turn.
npm 0.26.0 (published 2026-10-26) released the 10-26 main work and more: the Claude Code workspace connector (`trail mcp` passing the workspace's tools, skill prompts, and instructions through to Claude Code after pairing, with repo tools winning name clashes and the repo still working when Trail is unreachable), an `always follow` pin (`trail note --always-follow`), `trail init --agents auto` writing repo files for Claude Code, Cursor, Codex, and OpenCode with laptop settings only for the agents installed, first-setup reading of merged PR reviews so real learnings exist on day one, and the four learning kinds regrouped into three display units (learnings, always follow, skills), with the old `/api/v1/mcp` brain tools removed in the connector's favor.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=trailhq/Trail-Code&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=trailhq/Trail-Code&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=trailhq/Trail-Code&type=date&legend=top-left" />
</picture>

The rename trail has grown another link: the repository's canonical home is now trailhq/Trail-Code, with the old trailhq/Graft and NanoNets/Graft URLs redirecting, and the product page presents it as "Trail-code (previously graft)".
**The community footprint is thin for the star count: a third-party Show HN drew 3 points and 2 comments, the creator's own follow-up reached 39 points and 44 comments, and its most substantive comments were criticisms.**
In that thread the creator confirmed the README's marketing register is model-written ("Opus 5 is very paranoid on giving proofs... so I let it keep this one line"), and the only cross-tool numbers anywhere (graft over Graphify, MRR 0.73 vs 0.38) are his own tests, not a published benchmark.
No independent benchmark or third-party evaluation exists as of 2026-09-13.

## Strengths

- **The delivery is the deepest in this category**: per-agent instruction files across nine surfaces, six MCP tools, post-edit hooks with blast-radius warnings, a live statusline, and auto-resync, so the map actually gets used instead of ignored.
- The structural layer is deterministic, key-free, and local, and the LLM layer is bring-your-own-provider, so the tool never sits between you and a model bill.
- Freshness is engineered rather than promised: millisecond structural re-sync per query, content-hash caching, and a `graft check` drift report.
- The telemetry policy is unusually explicit: a published allowlist contract with bucketed values, opt-out via `DO_NOT_TRACK=1`, and off by default in CI and source builds.

## Cautions

- **Every performance number is self-run**: the up-to-4x-cheaper and 3x-faster headline, the +46% tool-call, +42% token, and +60% time savings, and the 54%-to-66% SWE-bench Verified result (official harness, but their run, their repos, not on the public leaderboard).
- The differentiating plain-English summaries are the part the creator calls experimental, writing on HN that they are "still testing whether the summaries are worth it at all".
- The README's prose is LLM-written and commenters flagged the "empty calorie language" before the creator confirmed its origin, which tells you how much of the polish to discount.
- The detailed benchmark tables behind the 4x headline cover only PocketBase (a 21% cost cut), so the "up to" is doing real work.
- The Trail Brain upsell is aggressive ("a living skill file that learns from every task" is the hosted product, not this repo), 247 open issues and pull requests is a lot for fifteen weeks, and the rename trail (context-graph-engine to Graft, NanoNets to trailhq, Graft to Trail-Code) scatters canonical links.

## Pricing

Graft is free, MIT, no account; your only cost is the LLM usage the optional deep pass makes under your own key.
The money is in Trail Brain (as of 2026-10-24, re-verified unchanged): Free ($0, 100 rules, 1 editor, 10K agent reads/month), Small ($20k/year), Medium ($60k/year), and Large ($150k/year with in-VPC and HIPAA BAA), priced on rules, editors, and monthly agent reads.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Trail Brain | Baseline: Graft free (MIT); Trail Brain Free $0 (100 rules), Small $20k/yr, Medium $60k/yr, Large $150k/yr with in-VPC and HIPAA BAA. | [trailhq.com/pricing](https://trailhq.com/pricing) |

## Compared to

- [Graphify](../graphify/index.md): both are local, file-based graph tools with no vectors, but Graphify's graph is fully deterministic while graft's differentiating summaries are LLM-written; Graphify for structure only, graft for a map written in English.
- [Semble](../semble/index.md): Semble answers where-is-the-code with fused static embeddings and BM25; graft answers what-does-this-subsystem-do and who-depends-on-it with readable files and typed links.
- [Augment Code](../augment-code/index.md): Augment's real-time index is cloud-side and drives only its own harness; graft's map is local files any agent that reads files can use, with correspondingly less enterprise polish.

## Bottom line

I would try graft on a repo big enough that my agent visibly wanders, keeping the free structural layer as the default and treating every headline number as a hypothesis my own workload has to replicate.
I would not skip TELEMETRY.md for a compliance-sensitive team, and I would not buy Trail Brain on the strength of this repo, because the open-source map and the paid company brain are different bets.

## Changes

- 2026-09-12 - Created in the Context engines category during the three-entrant resolution run.
- 2026-09-16 - Refreshed the growth numbers (8,121 stars, 735 forks, 165 open issues as of re-verification); npm package, download window, and Trail Brain pricing unchanged.
- 2026-09-18 - Refreshed the growth numbers (8,458 stars, 766 forks, 169 open issues, 49,422 trailing-month npm downloads); package still v0.18.0 and Trail Brain pricing unchanged.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-20 - Recorded the repository's canonical move to the trailhq GitHub org and repointed the raw README and TELEMETRY reference links, alongside the growth-number refresh (8,723 stars, 52,630 trailing-month npm downloads).
- 2026-09-22 - Recorded the npm package moving to v0.19.0 (published 2026-09-22) and refreshed the growth numbers (9,051 stars, 823 forks, 196 open issues, 56,074 trailing-month npm downloads); Trail Brain pricing unchanged.
- 2026-09-25 - Refreshed the growth numbers (9,172 stars, 835 forks, 206 open issues, pushed 2026-09-24); npm package v0.19.0, the trailing-month download figure, and Trail Brain pricing unchanged.
- 2026-09-26 - Recorded the npm package moving to v0.20.0 (published 2026-09-25) and refreshed the growth numbers (9,234 stars, 842 forks, 215 open issues, pushed 2026-09-26, 59,444 trailing-month npm downloads); Trail Brain pricing unchanged.
- 2026-09-27 - Refreshed the growth numbers (9,276 stars, 844 forks, 221 open issues, 66,248 trailing-month npm downloads); npm package v0.20.0 and Trail Brain pricing unchanged.
- 2026-09-29 - Refreshed the growth numbers (9,381 stars, 862 forks, 239 open issues, pushed 2026-09-29, 72,419 trailing-month npm downloads); npm package v0.20.0 and Trail Brain pricing unchanged.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-02 - Recorded the npm package moving to v0.21.1 (published 2026-09-29) and refreshed the growth numbers (9,483 stars, 871 forks, 199 open issues and pull requests, pushed 2026-10-01, 88,838 trailing-month npm downloads); Trail Brain pricing unchanged.
- 2026-10-07 - Added the trailhq/Graft star history chart to the Status section.
- 2026-10-16 - Recorded the second rename, product and repository (trailhq/Graft to trailhq/Trail-Code, npm @trailhq/trail-code "Formerly graft", positioning widened to the self-learning context layer with team Learnings), refreshed the growth numbers (10,084 stars, 891 forks, 250 open issues and pull requests, pushed 2026-10-15, 114,056 trailing-month downloads on the old package), and re-verified Trail Brain pricing unchanged.
- 2026-10-22 - Recorded the language count rising to 24 with Gleam support, the renamed npm package moving to v0.23.1, and refreshed the growth numbers (939 forks, 247 open issues and pull requests, 98,766 trailing-month downloads on the old package); Trail Brain pricing re-verified unchanged.
- 2026-10-24 - Recorded the renamed npm package moving to v0.25.0 (2026-10-23: a repo's skill shipping with its whole folder, skill runs reported to the workspace, learning-sync fixes for HEAD-deleted learnings and per-turn sync) and refreshed the growth numbers (955 forks, 244 open issues and pull requests, pushed 2026-10-23); Trail Brain pricing re-verified unchanged against the live pricing page.
- 2026-10-26 - Recorded main's unreleased Claude Code workspace MCP connector (`trail mcp` passing the workspace MCP server through to Claude Code) and the learnings/always-follow/skills display regrouping (2026-10-26).
- 2026-10-27 - Recorded the renamed npm package moving to v0.26.0 (2026-10-26: the Claude Code workspace connector released, `trail init --agents auto`, the `always follow` pin, first-setup PR-review reading, the learnings/always-follow/skills regrouping, and the old `/api/v1/mcp` brain tools removed) and refreshed the growth numbers (959 forks, 251 open issues and pull requests, 84,196 trailing-month downloads on the old package summed from the range endpoint).

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Context Management Patterns](../../context-management-patterns/index.md) - the manual onboarding practice graft automates
- [Speeding up LLM work on a single codebase](../../../speeding-up-llm-work-on-a-single-codebase/index.md) - the corpus article whose core problem graft attacks

## References

- https://github.com/trailhq/Trail-Code - canonical repository (trailhq/Graft and NanoNets/Graft redirect here), stats and activity as of 2026-10-26
- https://raw.githubusercontent.com/trailhq/Trail-Code/main/README.md - architecture, benchmark tables, SWE-bench Verified numbers, delivery surfaces, and the rename banner ("Trail-code (previously graft)")
- https://graft.nanonets.ai - product site, Trail attribution, and marketing claims
- https://trailhq.com/trail-code - the product page carrying the rename and the Learnings framing, fetched 2026-10-16
- https://raw.githubusercontent.com/trailhq/Trail-Code/main/TELEMETRY.md - the telemetry allowlist contract (the original NanoNets/context-graph-engine path still redirects)
- https://registry.npmjs.org/@trailhq/trail-code/latest - the renamed package, v0.26.0, described as "Formerly graft" (re-fetched 2026-10-27)
- https://raw.githubusercontent.com/trailhq/Trail-Code/main/CHANGELOG.md - the 0.26.0 changelog: the workspace connector, `init --agents auto`, `always follow`, and the removed `/api/v1/mcp` brain tools (fetched 2026-10-27)
- https://api.npmjs.org/downloads/range/2026-09-27:2026-10-26/@nanonets/graft - 84,196 downloads summed for 2026-09-27 to 2026-10-26 on the old package, eight zero days in the window, fetched 2026-10-27
- https://hn.algolia.com/api/v1/items/49197687 - the 3-point Show HN and the creator's tree-sitter-only clarification
- https://hn.algolia.com/api/v1/items/49299985 - the 39-point thread: staleness, README register critique, and the vendor-run Graphify comparison
- https://trailhq.com/pricing - Trail Brain plans as of 2026-10-06
- https://trailhq.com - the vendor and the Trail Brain upsell positioning
