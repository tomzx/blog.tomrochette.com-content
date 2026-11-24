---
title: git-lrc
created: 2026-10-10
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Developers who want AI review at commit time on their own machines, and who can
  weigh a source-available tool whose reviews ride a vendor cloud by default.
---

git-lrc is a free commit-time AI code review CLI from Hexmos that hooks `git commit`, reviews the staged diff through its LiveReview cloud pipeline, and records a review, vouch, or skip attestation in the commit's git log.

## What it is

**The bet is that the commit, not the pull request, is the last moment where fixing agent-written code is cheap.**
A one-command install sets up a global git hook: every commit first opens a browser review UI with inline LLM comments over the staged diff, and the developer chooses commit, commit and push, or skip.
Newer surfaces round out the loop: an Issue Navigator filters findings by severity and risk category and can hand them straight to your coding agent, and every completed review also generates a short Summary Deck slide summary.
Each decision is written into the commit message (`ran (iter:3, coverage:85%)`, `vouched`, or `skipped`), so review behavior becomes part of repository history.
Reviews run on Gemini by default through the LiveReview cloud, with bring-your-own keys for OpenAI, Claude, DeepSeek, OpenRouter, Atlas Cloud, and Anthropic-compatible endpoints, and a bundled claude-lrc plugin exposes the same loop as Claude Code slash commands.
It is a Go binary from Hexmos (the company behind the LiveReview platform), source-available under a modified Sustainable Use License: no resale, no commercial redistribution of modified versions.

## Status

**Young, fast-moving, and adoption-evidenced mostly through its own surfaces.**
The repo (HexmosTech/git-lrc) was created February 8, 2026 and shows 1,470 stars and 191 forks as of 2026-10-11; it now carries 57 releases (v0.6.23, November 22, 2026, is latest), and the pushed date and main's latest commit both stand at November 22, the version bump and release notes for v0.6.23.
Both October 23 releases were security-driven: v0.6.16 fixed a CSRF vulnerability in the local review server that let a malicious web page trigger state-changing review actions (skip, commit, vouch, abort, and handoff), and v0.6.17 moved the Go toolchain to 1.26.10 for GO-2026-6809, a standard-library crypto/x509 vulnerability surfaced by govulncheck.
The releases resumed on November 20 with four tag-only versions that carry no GitHub release pages (v0.6.18 through v0.6.21, which together bump the pinned codebase-memory-mcp and fix it not upgrading when its pinned version moves, take Go to 1.26.11 for GO-2026-6859, and pin `--format json` on every blast-radius client call).
v0.6.22 (November 22) adds cross-repo blast radius to local reviews: `lrc review` sends the outbound HTTP calls it finds in the local code graph to LiveReview, which matches them against routes declared by the organization's related repositories and folds the result into the blast-radius report without cloning or indexing those repositories, with Math Mode explaining the score the scorer produced and four new flags (`--cross-repo`, on by default, `--cross-repo-timeout`, `--repo-url`, and `--save-blast-radius`).
v0.6.23 (November 22) republishes the v0.6.22 feature set from main so the published binaries and the mainline commit are the same code.

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
- Since v0.6.22 the default sends more: the cross-repo enrichment also ships the outbound HTTP calls found in the local code graph to LiveReview, best-effort under a 45-second default timeout, so `--cross-repo=false` is the switch a no-egress machine needs, while the pricing FAQ (fetched 2026-11-24) still says only the staged diff is analyzed and no full repository context is uploaded.
- The license is not open source: a modified Sustainable Use License forbids resale and commercial redistribution of modified versions, so "completely free" describes price, not freedom.
- Quality evidence is vendor-supplied; no independent benchmark or third-party assessment of its finding quality exists as of 2026-10-18, and an October 2026 third-party eval could not test it at all because it sends the diff to a LiveReview server.
- The Premium ladder is per reviewed LOC ($32 per 100k per month, doubling with each band), so heavy committers pay on a usage curve roborev, which bills your existing agent subscriptions instead, does not have.
- The local half is attack surface too: the v0.6.16 CSRF fix (October 23, 2026) means that until then a malicious web page could drive the local review server's state-changing actions, so the browser-facing review UI needs the same threat model as any privileged local service.

## Pricing

**LOC-banded subscriptions with a free BYOK tier, as of 2026-10-18 (free-tier contents re-read 2026-10-30; all prices re-read unchanged 2026-11-24).**
Free Individual covers 30,000 reviewed LOC per month; the pricing page now lists hosted LiveReview AI as included with no API key needed beside the bring-your-own-keys path, caps the tier at 3 team members, and bundles risk-based auto-approve for safe pull requests.
Premium starts at $32 per month for 100k LOC and doubles in fixed bands ($64 per 200k, $128 per 400k, $256 per 800k, $512 per 1.6M, $1,024 per 3.2M) with unlimited users; Enterprise adds self-hosting, SSO, and custom deployment at contact pricing.
Only diff lines count against the LOC budget, not repository size, and the pricing FAQ states LiveReview is not SOC 2 Type II certified at this time.

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
- 2026-10-18 - Rotation re-verification: every cited URL re-fetched live, prices and release state unchanged (v0.6.15 still latest); recorded the Issue Navigator and Summary Deck surfaces, the added Atlas Cloud and Anthropic-compatible BYOK connectors, and a third-party eval's failed local run that confirms the cloud-routed default.
- 2026-10-24 - Volatile re-verification: recorded v0.6.16 (October 23), the CSRF fix for the local review server's state-changing actions, and v0.6.17 (October 23), the Go 1.26.10 toolchain bump for GO-2026-6809, with the release count at 55 and a new caution on the local server's attack surface; prices unchanged.
- 2026-10-30 - Rotation re-verification: every cited URL re-fetched live; prices and the release state unchanged (v0.6.17 still latest, pushed October 23, 55 releases), and the pricing page's Free tier recorded as it now reads: hosted LiveReview AI included with no API key needed beside the BYOK path, a 3-team-member cap, and risk-based auto-approve, with the pricing FAQ stating LiveReview is not SOC 2 Type II certified.
- 2026-11-05 - Volatile re-verification: pushed_at moved to November 3 on a side-branch push while main stays at October 23; v0.6.17 still the latest release.
- 2026-11-11 - Rotation re-verification: every cited URL re-fetched live (hexmos.com serves 403 to plain curl with the domain root included, a site-wide wall, while the pricing and product pages still fetch through and are unchanged); prices, tiers, and the release state unchanged (v0.6.17 still latest, 55 releases, pushed November 3, main still October 23), the Free tier's LiveReview-AI-included contents, the not-SOC-2-Type-II FAQ line, and the 9-point Show HN all standing; no factual drift.
- 2026-11-13 - Volatile re-verification: pushed_at moved to November 12 on a side-branch push while main stays at October 23; v0.6.17 still the latest release.
- 2026-11-20 - Rotation re-verification: every cited URL re-fetched live; prices and tiers unchanged (Free 30k LOC with LiveReview AI included, Premium $32 per 100k in fixed doubling bands, Enterprise custom, the not-SOC-2-Type-II FAQ line standing), the release state unchanged (v0.6.17 still latest, 55 releases, pushed November 12 on a side branch with main at October 23), the hexmos curl wall standing with both pages fetching through the alternate client, the README and the Agent Skills Hub eval results unchanged, and the 9-point Show HN unchanged; no factual drift.
- 2026-11-22 - Volatile re-verification: pushed_at moved to November 22 and main's latest commit moved from October 23 to November 20, a release-readiness commit requiring the local security scanners to pass before a release is cut, with v0.6.17 still the latest release at 55 releases.
- 2026-11-24 - Volatile re-verification: recorded v0.6.22 and v0.6.23 (both November 22, 57 releases), cross-repo blast radius in local reviews through LiveReview with Math Mode explaining the score and four new flags, v0.6.23 a republish from main, after four tag-only November 20 versions (v0.6.18 through v0.6.21) that carry no release pages; the pushed date and main's latest commit both moved to November 22; added the default-on cross-repo data flow to Cautions.

## See also

- [roborev](../roborev/index.md) - the fully local commit-time reviewer, the closest sibling
- [Kodus](../kodus/index.md) - the BYOK reviewer at the category's other open extreme
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - where git-lrc now sits among the category's members
- [Code Review Without Reading the Code](../../../code-review-without-reading-the-code/index.md) - the corpus case for machine-scale review

## References

- https://github.com/HexmosTech/git-lrc - repo facts: 1,470 stars, 191 forks, created 2026-02-08, pushed 2026-10-11, NOASSERTION license (GitHub API, as of 2026-10-11, push date re-checked 2026-10-18, 2026-10-30, 2026-11-11, 2026-11-13, 2026-11-22, and 2026-11-24, pushed 2026-10-23, then November 3 and November 12 on side branches, then November 22 with main's latest commit November 20, a release-readiness commit, then November 22 with main's latest commit November 22, the v0.6.23 version bump)
- https://raw.githubusercontent.com/HexmosTech/git-lrc/HEAD/README.md - the commit-hook mechanism, agent mode, claude-lrc companion, BYOK connectors (including Atlas Cloud and Anthropic-compatible endpoints), the Issue Navigator and Summary Deck surfaces, and the repository-rules surface, re-fetched 2026-10-30 and 2026-11-11 (unchanged)
- https://hexmos.com/livereview/git-lrc/pricing/ - the LOC pricing bands and tier contents, fetched 2026-10-11, re-fetched 2026-10-18, re-read 2026-10-30 (prices unchanged; the Free tier now lists hosted LiveReview AI with no API key needed, a 3-team-member cap, and risk-based auto-approve; the FAQ states LiveReview is not SOC 2 Type II certified), re-fetched 2026-11-11 and 2026-11-20 through the site's curl wall, all unchanged; re-fetched 2026-11-24 through the alternate fetch client, prices, tiers, and the SOC 2 FAQ line unchanged
- https://hexmos.com/livereview/git-lrc/ - the product page: install flow, the vouch-skip table, and the LiveReview platform relationship, fetched 2026-10-10, re-fetched 2026-10-18, 2026-10-30, 2026-11-11, and 2026-11-20 (unchanged)
- https://api.github.com/repos/HexmosTech/git-lrc/releases - 55 releases, v0.6.16 (CSRF fix) and v0.6.17 (Go toolchain bump) published October 23, 2026 (GitHub API, fetched 2026-10-24; 53 releases with v0.6.15 latest as of 2026-10-11, re-fetched 2026-10-18, unchanged then, re-fetched 2026-10-30, 2026-11-05, 2026-11-11, 2026-11-13, and 2026-11-22, v0.6.17 still latest each time; re-fetched 2026-11-24: 57 releases, v0.6.22 and v0.6.23 both published November 22, 2026, v0.6.23 latest)
- https://api.github.com/repos/HexmosTech/git-lrc/releases/tags/v0.6.22 - the v0.6.22 release notes: cross-repo blast radius in local reviews through LiveReview, Math Mode matching the scorer, the four new flags, and the release-safety rule, fetched 2026-11-24
- https://api.github.com/repos/HexmosTech/git-lrc/releases/tags/v0.6.23 - the v0.6.23 release notes: the v0.6.22 feature set rebuilt and republished from main, fetched 2026-11-24
- https://api.github.com/repos/HexmosTech/git-lrc/tags - the tag list carrying v0.6.18 through v0.6.21 (November 20, 2026), which have no GitHub release pages, fetched 2026-11-24
- https://api.github.com/repos/HexmosTech/git-lrc - repo: pushed_at November 22, main's latest commit November 22, the v0.6.23 version bump (on 2026-11-22 main's latest commit read November 20, the release-readiness commit; re-queried 2026-10-24, 2026-10-30, 2026-11-05, 2026-11-11, 2026-11-13, 2026-11-22, and 2026-11-24; 1,470 stars and 191 forks as of 2026-10-11)
- https://hn.algolia.com/api/v1/items/48555511 - the Show HN launch, 9 points, June 16, 2026, the thin-footprint signal, re-fetched 2026-10-30 and 2026-11-11
- https://raw.githubusercontent.com/zhuyansen/agent-skills-hub/main/ops/review-runs/RESULTS.md - the independent end-to-end eval that could not run git-lrc locally because it sends the diff to a LiveReview server, fetched 2026-10-18, re-fetched 2026-10-30 and 2026-11-11 (unchanged)
