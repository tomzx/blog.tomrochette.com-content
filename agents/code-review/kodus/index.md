---
title: Kodus
created: 2026-08-30
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, open-source, developer-tools]
readability: 3
audience_notes: >
  Engineers and engineering leads evaluating self-hostable or open-source AI reviewers,
  comfortable reading a dual license and comparing a BYOK platform fee against per-seat SaaS.
---

Kodus is an open-source AI code reviewer named Kody (AGPL-3.0 plus a commercial enterprise-edition dual license) that reviews pull requests on GitHub, GitLab, Bitbucket, Azure Repos, and Forgejo/Gitea, self-hosted or via Kodus Cloud, with whatever model you bring.

## What it is

**The pitch is control: your model, your keys, your costs, with zero markup on tokens.**
The README frames Kody as learning your team's workflow and reviewing for quality, security, and performance, with custom rules written in plain language.
Surfaces are PR comments on five git providers (GitHub, GitLab, Bitbucket, Azure Repos, and Forgejo/Gitea per the docs and homepage FAQ), a CLI for local and CI runs, and Kodus Cloud (app.kodus.io) for teams that do not want to operate it.
BYOK covers OpenAI, Anthropic, Google Gemini, Vertex AI, Novita, and any OpenAI-compatible endpoint, and the README names Claude, GPT-5, Gemini, Llama, GLM, and Kimi as options.

## Status

**Active and small: commits this week, with 1,461 stars and 172 forks as of 2026-10-11.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kodustech/kodus-ai&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kodustech/kodus-ai&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kodustech/kodus-ai&type=date&legend=top-left" />
</picture>

The repo (kodustech/kodus-ai) was created March 28, 2025 and was pushed to on October 23, 2026.
Funding: I could not verify any funding round from a primary source, so I record none.
The community footprint is thin, and I state that as a finding: five HN launches between 1 and 5 points, the largest being a 5-point Show HN for the CLI (47248299, March 4, 2026) and a 4-point one for the AGPL/BYOK repositioning (48049508, May 7, 2026).
A Discord community exists, but I found no independent reviews or benchmarks corroborating the quality claims.

## Strengths

- **Model-agnostic BYOK with a published zero-markup price calculator, which no incumbent in this category offers.**
- Forge breadth matches the category's widest: GitHub, GitLab, Bitbucket, Azure Repos, and Forgejo/Gitea, the same five-provider spread PR-Agent covers.
- Real self-hosting, with a deploy guide and a documented one-heartbeat-per-day anonymous telemetry opt-out.
- **The vendor now publishes measurements instead of only claims: CodeReviewBench scores models on actual PR diffs (30 PRs, 95 confirmed bugs, best recall 44.2 percent, every scorecard versioned in a repo), the State of AI Code Review report analyzes 180,739 production suggestions (71.8 percent of flagged PRs merge with a flag open), and a tools benchmark runs Kody against CodeRabbit, GitHub Copilot, and Cursor on the same 38 known-issue PRs with Kody first at 30 of 38 and every run's PR public, all under a stated vendor-run disclosure.**
- CLI plus CI/CD support puts review in the pipeline, not just in PR comments.

## Cautions

- **The dual license has teeth: anything under ee/ paths is commercially licensed, so the AGPL guarantee is narrower than the badge suggests.**
- No verifiable funding and a thin community footprint make bus factor and longevity open questions.
- Quality claims ("reviews like your senior dev wrote them") are vendor marketing; CodeReviewBench is vendor-run and single-harness by its own disclosure, the tools benchmark is vendor-run and self-favoring (Kody leads every severity band, and its methodology text contradicts itself, nine selected PRs in one paragraph, 38 analyzed in the results), so none of it fills the independent-benchmark gap.
- Self-hosting transfers model cost and operations to you, which is the point, but it is a real cost.

## Pricing

**Open core with a free tier, a BYOK developer fee, and a transparent no-markup pledge, as of 2026-10-11.**
The tiers changed in early September 2026: Community is free for indie devs and small teams (self-hosted or hosted, up to 10 Kody rules), Teams BYOK is $10 per developer per month ($8 effective when billed annually) plus your raw token costs with unlimited rules and plugins, and Enterprise is custom with SSO, RBAC, SOC 2, and dedicated support.
The BYOK calculator keeps the no-markup FAQ commitment and prices example stacks (for example $450 per month for 30 developers on Gemini Pro or ChatGPT 5.1).
Self-hosting under AGPL-3.0 is free, minus your own model bills.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09 | All tiers | Early-September tier restructure: Community free (up to 10 Kody rules), Teams BYOK $10/dev/mo ($8 annual) plus raw tokens, Enterprise custom; self-hosting free under AGPL-3.0. | [kodus.io/pricing](https://kodus.io/pricing/) |

## Compared to

- [CodeRabbit](../coderabbit/index.md): the funded, polished default; choose Kodus when model choice, cost transparency, or self-hosting outranks polish.
- [OpenCodeReview](../open-code-review/index.md): the other OSS, bring-your-own-model path, Apache-2.0 and CLI-first where Kodus is AGPL and PR-app-first.
- [Greptile](../greptile/index.md): hosted-only and rules-driven, the opposite answer to the same cost-control question.

## Bottom line

**Recommended for teams that want AI review on Bitbucket or Azure Repos, or anywhere, with their own model keys and no token markup.**
Not for teams that need a vendor with verified funding, an audited security posture, or contractual longevity.
My disagreeable take: I trust a reviewer whose business model survives zero token markup more than one whose margin depends on it, because a SaaS that resells model usage is structurally tempted to skimp on tokens, and skimped tokens are exactly how reviewers quietly get worse.

## Changes

- 2026-08-30 - Created in the Code review category as the AGPL dual-license BYOK reviewer note.
- 2026-09-02 - Recorded the pricing restructure (Community free, Teams BYOK $10 per developer, Enterprise) and updated matrix pricing cells.
- 2026-09-05 - Added the Teams $8 per developer annual option alongside the $10 monthly rate.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-24 - Refreshed the repo numbers to 1,416 stars and 159 forks with a same-day push; tiers and prices unchanged.
- 2026-10-07 - Added the kodustech/kodus-ai star history chart to the Status section.
- 2026-10-07 - Recorded the vendor's new research surfaces (CodeReviewBench and the State of AI Code Review report) in Strengths and Cautions with the vendor-run caveat, and refreshed the repo to 1,452 stars pushed October 7.
- 2026-10-11 - Recorded the vendor's third research surface, the tools benchmark against CodeRabbit, GitHub Copilot, and Cursor (Kody first at 30 of 38 known issues), noted its self-favoring design and self-contradictory methodology text in Cautions, and refreshed repo counts.
- 2026-10-20 - Rotation re-verification: corrected forge breadth to five providers (the docs and homepage FAQ name Forgejo/Gitea alongside GitHub, GitLab, Bitbucket, and Azure Repos; the note said four), moved the push date to October 20 with no release after web-1.2.7, and re-fetched every cited URL live; prices, tiers, and benchmark figures unchanged.
- 2026-10-22 - Volatile re-verification: corrected the release record, the previous run's no-release-after-web-1.2.7 note was written before three routine releases published later that October 20 (2.2.7 backend fixes, web-1.2.8, mcp-manager-2.1.3), and the push date moved to October 22; prices and benchmark figures unchanged.

## See also

- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - where Kodus now sits among the category's members
- [CodeRabbit](../coderabbit/index.md) - the incumbent Kodus explicitly positions itself against
- [OpenCodeReview](../open-code-review/index.md) - the other open-source, bring-your-own-model reviewer
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - what review is for when agents write the code
- [You Cannot Out-Review a Machine by Hand](../../../you-cannot-out-review-a-machine-by-hand/index.md) - why automated review exists at all

## References

- https://github.com/kodustech/kodus-ai - repo, 1,461 stars, 172 forks, AGPL-3.0 + EE dual license, pushed October 23, 2026 (GitHub API, as of 2026-10-11, push date re-checked 2026-10-20, 2026-10-22, and 2026-10-24; since the previously recorded October 20 batch, four routine service releases published: 2.2.8, web-1.2.9, and mcp-manager-2.1.4 on October 22, selfhosted-2.2.6 on October 23)
- https://kodus.io/ - product page and positioning; the supported-providers FAQ names GitHub, GitLab, Bitbucket, Azure DevOps, and Forgejo/Gitea, fetched 2026-10-20
- https://kodus.io/pricing/ - Community free, Teams BYOK $10/dev, Enterprise custom, no-markup FAQ, as of 2026-10-02, re-verified unchanged 2026-10-11 and 2026-10-20
- https://codereviewbench.com/ - the vendor-run model benchmark: 30 PRs, 95 golden bugs, best recall 44.2 percent, single-harness disclosure, fetched 2026-10-07, re-verified 2026-10-11 and 2026-10-20
- https://kodus.io/benchmark-ai-code-review/ - the vendor-run tools benchmark: Kody 30 of 38 known issues, Cursor 22, Copilot 20, CodeRabbit 15, per-run PRs public, methodology text internally inconsistent, fetched 2026-10-11, re-fetched unchanged 2026-10-20
- https://kodus.io/data/ - the State of AI Code Review report: 180,739 suggestions, 71.8 percent of flagged PRs merged with a flag open, CC BY 4.0, fetched 2026-10-07, re-fetched unchanged 2026-10-20
- https://docs.kodus.io/ - documentation hub and self-host guide; the integration card names GitHub, GitLab, Bitbucket, Azure Repos, and Forgejo, re-fetched 2026-10-20
- https://docs.kodus.io/how_to_deploy/en/deploy_kodus/telemetry - self-hosted anonymous heartbeat and opt-out
- https://hn.algolia.com/api/v1/items/43572816 - Show HN launch, 3 points, April 3, 2025
- https://hn.algolia.com/api/v1/items/48049508 - Show HN, AGPLv3/BYOK, 4 points, May 7, 2026
- https://hn.algolia.com/api/v1/items/47248299 - Show HN for the Kodus CLI, 5 points, March 4, 2026
- https://hn.algolia.com/api/v1/items/46944149 - Show HN, "Open-Source Alternative to CodeRabbit", 1 point, February 9, 2026
