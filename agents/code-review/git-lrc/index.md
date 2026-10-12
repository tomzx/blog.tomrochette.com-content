---
title: git-lrc
created: 2026-10-10
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Developers who want AI review at commit time on their own machines, and who can
  weigh a source-available tool whose reviews ride a vendor cloud by default.
---

git-lrc is a free commit-time AI code review CLI from Hexmos that hooks `git commit`, reviews the staged diff through its LiveReview cloud pipeline, and records a review, vouch, or skip attestation in the commit's git log.

## What it is

**The bet is that the commit, not the pull request, is the last moment where fixing agent-written code is cheap.**
A one-command install sets up a global git hook: every commit first opens a browser review UI with inline LLM comments over the staged diff, and the developer chooses commit, commit and push, or skip.
Each decision is written into the commit message (`ran (iter:3, coverage:85%)`, `vouched`, or `skipped`), so review behavior becomes part of repository history.
Reviews run on Gemini by default through the LiveReview cloud, with bring-your-own keys for OpenAI, Claude, DeepSeek, and OpenRouter, and a bundled claude-lrc plugin exposes the same loop as Claude Code slash commands.
It is a Go binary from Hexmos (the company behind the LiveReview platform), source-available under a modified Sustainable Use License: no resale, no commercial redistribution of modified versions.

## Status

**Young, fast-moving, and adoption-evidenced mostly through its own surfaces.**
The repo (HexmosTech/git-lrc) was created February 8, 2026 and shows 1,470 stars, 191 forks, and 53 releases (v0.6.15, October 5, 2026, is latest) as of 2026-10-11, pushed October 10.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=HexmosTech/git-lrc&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=HexmosTech/git-lrc&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=HexmosTech/git-lrc&type=date&legend=top-left" />
</picture>

The Show HN launch (June 16, 2026) drew 9 points and no surviving comment thread, so the visible community footprint is thin, and I state that as a finding: the traction evidence is Product Hunt and launch-directory badges, the homepage's small-company trusted-by wall, and the vendor's own claims, not independent discussion.

## Strengths

- **The vouch-skip ledger is accountability infrastructure: review behavior is recorded per commit in git history, not in someone else's dashboard.**
- Setup is one command and machine-wide, riding the one workflow step (commit) every developer already performs.
- Agent mode reviews non-interactively with JSON output and writes an `agent-reviewed` attestation, so coding agents and CI can complete the same loop.
- A local blast-radius scorer (built on the codebase-memory-mcp graph) ranks hunks by reach and review priority independently of the LLM review.

## Cautions

- **The reviews leave your machine by default: diffs go to Hexmos's LiveReview cloud for coordination even on the free tier, and self-hosting waits for Enterprise.**
- The license is not open source: a modified Sustainable Use License forbids resale and commercial redistribution of modified versions, so "completely free" describes price, not freedom.
- Quality evidence is vendor-supplied; no independent benchmark or third-party assessment of its finding quality exists as of 2026-10-11.
- The Premium ladder is per reviewed LOC ($32 per 100k per month, doubling with each band), so heavy committers pay on a usage curve roborev, which bills your existing agent subscriptions instead, does not have.

## Pricing

**LOC-banded subscriptions with a free BYOK tier, as of 2026-10-11.**
Free Individual covers 30,000 reviewed LOC per month with your own AI keys; Premium starts at $32 per month for 100k LOC and doubles in fixed bands ($64 per 200k, $128 per 400k, $256 per 800k, $512 per 1.6M, $1,024 per 3.2M) with unlimited users; Enterprise adds self-hosting, SSO, and custom deployment at contact pricing.
Only diff lines count against the LOC budget, not repository size.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-10 | Free, Premium, Enterprise | Baseline: Free 30k LOC/mo with BYOK, Premium from $32/mo per 100k LOC in fixed doubling bands, Enterprise custom. | [hexmos.com pricing](https://hexmos.com/livereview/git-lrc/pricing/) |

## Compared to

- [roborev](../roborev/index.md): the other commit-time reviewer; roborev reviews with your own locally installed agents under MIT, while git-lrc routes through Hexmos's cloud with a source-available core.
- [CodeRabbit](../coderabbit/index.md): the hosted PR incumbent; git-lrc moves the checkpoint before the PR exists and prices by workload rather than seat.
- [OpenCodeReview](../open-code-review/index.md): the deterministic-pipeline CLI for PRs and diffs in CI; git-lrc is the habit loop at commit time instead.

## Bottom line

**Recommended for developers who want a one-command commit gate that records who reviewed what in the git log itself.**
Not for teams that need code to stay on their machines below an Enterprise contract, or that require an OSI-approved license.
My disagreeable take: recording review attestations in commit messages is the most underrated idea in this category, because it survives tool churn, but the cloud-routed pipeline undercuts the local-first story the commit hook sells.

## Changes

- 2026-10-10 - Created after the entrant scan resolved the HexmosTech/git-lrc candidate from the GitHub topic scan; six sources fetched this run, including the thin Show HN thread as the footprint signal.

## See also

- [roborev](../roborev/index.md) - the fully local commit-time reviewer, the closest sibling
- [Kodus](../kodus/index.md) - the BYOK reviewer at the category's other open extreme
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - where git-lrc now sits among the category's members
- [Code Review Without Reading the Code](../../../code-review-without-reading-the-code/index.md) - the corpus case for machine-scale review

## References

- https://github.com/HexmosTech/git-lrc - repo facts: 1,470 stars, 191 forks, created 2026-02-08, pushed 2026-10-10, NOASSERTION license (GitHub API, as of 2026-10-11)
- https://raw.githubusercontent.com/HexmosTech/git-lrc/HEAD/README.md - the commit-hook mechanism, agent mode, claude-lrc companion, BYOK connectors, and the repository-rules surface
- https://hexmos.com/livereview/git-lrc/pricing/ - the LOC pricing bands and tier contents, fetched 2026-10-11
- https://hexmos.com/livereview/git-lrc/ - the product page: install flow, the vouch-skip table, and the LiveReview platform relationship, fetched 2026-10-10
- https://api.github.com/repos/HexmosTech/git-lrc/releases - 53 releases, v0.6.15 (2026-10-05) latest (GitHub API, as of 2026-10-11)
- https://hn.algolia.com/api/v1/items/48555511 - the Show HN launch, 9 points, June 16, 2026, the thin-footprint signal
