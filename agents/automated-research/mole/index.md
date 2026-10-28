---
title: Mole
created: 2026-10-12
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, deep-research, budget-enforcement, open-source]
readability: 3
audience_notes: >
  Engineers who want deep-research runs with hard cost ceilings and checkable claims, and anyone comparing enforcement-based trust mechanisms.
  Assumes you know what a tool-calling agent and an MCP server are.
---

Mole is Lajos Deme's Apache-2.0 deep-research agent for the terminal: a single Go binary that decomposes a question, searches, reads sources, and returns a cited answer, with a budget ledger that stops the run at the ceiling you set and quote checks that drop claims the source never said.

**Mole is the first member of this category that treats the run's cost as part of the loop's contract: every model call is reserved against the budget before it happens and settled after, so a $0.50 ceiling is a hard stop rather than an estimate, and every claim that survives extraction carries a verbatim quote from its source.**

## What it is

A static Go binary (`mole` plus `mole-mcp`, Apache-2.0) with a SQLite store created on first use, installable by a checksum-verified script, a Homebrew tap, or the AUR.
The loop decomposes a question into leads, searches, reads sources, extracts claims, discards any claim whose quote does not appear verbatim in the page it was mined from, checks the survivors for contradictions, and writes a cited answer, or a structured dataset when `--schema` asks for rows instead of prose.
Toolkit mode inverts the control: your coding agent's model does the reasoning while mole supplies the deterministic half (search, fetch, extraction) over MCP, and `mole crossings` reports exactly what left the machine.
The privacy boundary covers local data too: point it at a CSV or a folder and the model only chooses a hypothesis template and column names, the SQL runs locally, and only aggregates over five or more records are allowed back.

## Status

Active and young: 314 stars, 20 forks, created 2026-08-01, last pushed 2026-10-25 (unreleased main-branch fixes: the verifier stops a pass on a fatal second look instead of continuing, the executor verifies what research found on every ceiling stop, and the budget no longer lets max_leads mask the wall clock), releases v0.1.0 (2026-08-13), v0.2.0 (2026-10-10), and v0.2.1 (2026-10-13) still the latest, as of 2026-10-26.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=lajosdeme/mole&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=lajosdeme/mole&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=lajosdeme/mole&type=date&legend=top-left" />
</picture>

The Show HN thread reached 100 points with 14 comments on 2026-08-14, strong for the deep-research tier where GPT Researcher's own launch thread drew 4 points.
The README's "Honest numbers" table publishes the loop's weak spots alongside the wins: contradiction precision of 51 percent on a single judgement (70 percent when two agree), against 98 and 67 percent recall, next to a measured 0 percent budget overshoot.
The v0.2.1 release note of 2026-10-13 discloses a pricing bug that table could not see: the ledger had recorded 143 of 185 calls in a sampled run at $0.00 because pricing was attached to whichever part built the call rather than consulted in the ledger, so a `--usd` ceiling could not bind on the phase that makes most of them, and the release asks anyone enforcing a dollar budget to re-check it against a single run.

## Strengths

- The budget is enforced by the database schema, not a dashboard: a reserve-settle ledger with non-negative constraints, a 15 percent escrow held back for the final report, and hard ceilings on leads, tool calls, and wall clock.
- The verbatim-quote gate changes what can reach an answer: unsupported claims are dropped at extraction or marked in the report, never silently paraphrased into evidence.
- Local data stays local by construction, and the boundary is auditable after the fact through `mole crossings`.
- Publishing its own 51 percent contradiction-precision number is more candor than most self-evaluations in this category.

## Cautions

- One maintainer, three releases, and no independent evaluation: the 0 percent overshoot and claim-integrity numbers come from the project's own test corpus, and the overshoot figure was measured under the v0.2.0 accounting that v0.2.1 corrected.
- The strict pricing policy refuses `--usd` sessions when a model has no registered price, so unpriced models force token-budget mode where search costs cannot be bounded.
- The name is contested ground: an unrelated tw93/Mole and a macOS cleanup app called Mole shadow every search, and the launch thread's top replies called for a rename.
- The toolkit budget originally bounded nothing; the phase-review commit of 2026-08-12 records four independent reviews finding the reserve-settle path missing, fixed the same day.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are your own LLM and search API keys (Tavily, Brave, and alternatives), and the `--usd` or `--tokens` flag is the ceiling the run cannot cross.

## Compared to

- [Local Deep Research](../local-deep-research/index.md): the local-first literature loop with more engines and an encrypted document library; choose LDR for breadth, Mole when the hard budget ceiling and claim-level quote checking matter more.
- [GPT Researcher](../gpt-researcher/index.md): the cited-report baseline; Mole is stricter about spend and sourcing and lighter on integrations.
- [OpenResearch](../openresearch/index.md): the workspace that runs experiments on your own agents; Mole answers questions instead of executing code.

## Bottom line

**Recommended for engineers who want a deep-research appliance where overspend and unverifiable claims are blocked by the system rather than discouraged in a prompt.**
Not for anyone needing a mature, independently evaluated tool: the project is one maintainer and three releases old as of 2026-10-15.

## Changes

- 2026-10-12 - Created.
- 2026-10-15 - Recorded the v0.2.1 pricing fix: the ledger had left 143 of 185 calls in a sampled run unpriced, so a dollar ceiling could not bind on the phase that makes most calls, and flagged the 0 percent overshoot figure as measured under that earlier accounting.

## See also

- [Local Deep Research](../local-deep-research/index.md) - the local-first sibling at the same tier, encrypted libraries instead of enforced ledgers
- [GPT Researcher](../gpt-researcher/index.md) - the cited-report baseline Mole tightens
- [OpenResearch](../openresearch/index.md) - the experiment-running workspace loop
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/lajosdeme/mole - repository, Apache-2.0, 314 stars as of 2026-10-15, last push 2026-10-25 (push and release train re-checked via the API 2026-10-28)
- https://raw.githubusercontent.com/lajosdeme/mole/main/README.md - the loop, the reserve-settle ledger, the verbatim-quote gate, the privacy boundary, and the numbers table with its own failure rates (fetched 200, 2026-10-15)
- https://news.ycombinator.com/item?id=49303046 - the 100-point, 14-comment launch thread with the rename calls and the budget-enforcement question (fetched via the Algolia API, 2026-10-12)
- https://api.github.com/repos/lajosdeme/mole/releases - the release train through v0.2.1 (2026-10-13), whose note discloses the ledger pricing fix (fetched 200, 2026-10-15)
- https://github.com/lajosdeme/mole/commit/00b9f4e - the phase-review commit recording that the toolkit budget originally bounded nothing (fetched 200 via the API, 2026-10-12)
