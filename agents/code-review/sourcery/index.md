---
title: Sourcery
created: 2026-08-30
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers evaluating AI reviewers for GitHub or GitLab who also care about the tool's
  static-analysis roots and how a freemium open-source story maps onto private repos.
---

Sourcery is a hosted AI code reviewer for GitHub and GitLab (with IDE plugins and a security scanning layer) from the company behind the older Python refactoring tool of the same name.
Facts below verified as of 2026-09-24.

## What it is

**One brand, two products: the repo you star is the MIT-licensed Python refactoring lineage, the product you install is the proprietary review app.**
The reviewer summarizes every pull request, adds line-by-line suggestions, and now runs security scanners with findings triage, repository risk profiles, and an agent-assisted fix path per the docs.
Reviews run on OpenAI and Anthropic models, and the README commits to code not being stored beyond 30 days and never used for model training.
IDE surfaces cover PyCharm, VS Code, Sublime, and Vim, a wider editor spread than most reviewers in this category bother with.

## Status

**Old by category standards (repo since July 2019), active, and mid-size: 1,870 stars as of 2026-09-24, commits as recent as September 24, 2026.**
The PyPI package confirms the refactoring origin ("Magically refactor Python", 23 releases, now at 1.46.0).
Funding: not verifiable from primary sources, and TechCrunch's only "Sourcery" rounds belong to the unrelated 2014/2016 restaurant startup, so I record none.
The community footprint is modest: a 15-point Show HN for the refactoring era (27760608, July 7, 2021), a 3-point user comparison against Copilot (43944576, May 10, 2025), and a 1-point criticism thread (44224690, June 9, 2025) accusing the reviewer of being wrong and refusing to admit it.

## Strengths

- **Free forever on open source, the lowest-friction on-ramp of any hosted reviewer in this category.**
- Security scanning folded into the same seat: scanners, findings triage, risk profiles, and agent fixes.
- The Team tier bundles security scanning with team analytics and higher review limits, and Enterprise keeps BYO LLM keys beside self-hosting.
- Docs cover GitHub Enterprise Server and self-hosted GitLab, and Enterprise adds a self-hosting option, so it is not SaaS-only for locked-down shops.

## Cautions

- **The MIT badge on the repo covers the refactoring tool, not the reviewer, so starring the repo says nothing about the product's openness.**
- The one substantive independent user test I found on HN reports the reviewer confidently wrong and resistant to correction (44224690), which is exactly the failure mode that gets reviewers muted.
- No verified funding and a modest community footprint make the long-term trajectory hard to read.
- The paid tiers throttle usage (Team advertises higher review limits, no longer a fixed 3x multiple), so the cheap tiers are cheap partly by being slower.
- **The tier contents moved in late September 2026: nightly security scans now cover 50 repos where the earlier page promised scans for 200+ repos, and bring-your-own LLM keys moved from Team up to Enterprise.**

## Pricing

**Freemium per-seat with open source free, as of 2026-09-24.**
Pro is $12 per seat per month for private repos ($15 monthly), Team is $24 ($30 monthly) adding codebase security with nightly scans of 50 repos, a full issues dashboard, on-demand scans, team analytics, and higher review limits, and Enterprise adds self-hosting, GitHub Enterprise Server, SSO, bring-your-own LLM keys, a dedicated success manager, and invoice billing at custom pricing.
Open source repos are fully free.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Pro, Team | Baseline: Pro $12/seat/mo for private repos, Team $24/seat/mo with BYO LLM, Enterprise custom; open source repos fully free. Re-verified unchanged 2026-09-21. | [sourcery.ai/pricing](https://sourcery.ai/pricing/) |
| 2026-09-24 | Team, Enterprise | Tier contents reshuffled at unchanged prices: Team now includes nightly security scans of 50 repos (the earlier page promised scans for 200+ repos) and higher review limits (was 3x rate limits), and BYO LLM keys moved from Team to Enterprise. | [sourcery.ai/pricing](https://sourcery.ai/pricing/) |

## Compared to

- [CodeRabbit](../coderabbit/index.md): the scale and funding leader; Sourcery competes at half the entry price ($12 vs $24) and with the same free-for-OSS hook rather than with features.
- [Qodo](../qodo/index.md): the open-source PR-Agent half plus a commercial platform; choose Sourcery for the lighter hosted bundle, Qodo for self-hosted PR commands with any model.
- [Greptile](../greptile/index.md): codebase-graph reviews aimed at large codebases; Sourcery is the simpler, cheaper default for small teams.

## Bottom line

**Recommended for open-source maintainers and small teams that want a free or $12 reviewer with security scans bolted on.**
Not for large monorepo teams that need independent quality evidence or a vendor with verified financials.
My disagreeable take: free-for-open-source is the most underrated go-to-market weapon in this category, and I would rather a reviewer earn its reputation across a hundred thousand public repos anyone can inspect than across enterprise logos nobody can.

## Changes

- 2026-08-30 - Created when the entrant candidate pile was processed, as a Code review note.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-24 - Recorded the tier-content reshuffle at unchanged prices: Team's security scans now cover 50 repos nightly (was 200+), the rate-limit wording became "higher review limits" (was 3x), and BYO LLM keys moved from Team to Enterprise.

## See also

- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - where Sourcery now sits among the category's members
- [CodeRabbit](../coderabbit/index.md) - the incumbent whose pricing Sourcery undercuts
- [Qodo](../qodo/index.md) - the open-source half of the same market
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - what review is for when agents write the code
- [You Cannot Out-Review a Machine by Hand](../../../you-cannot-out-review-a-machine-by-hand/index.md) - why automated review exists at all

## References

- https://github.com/sourcery-ai/sourcery - repo, 1,870 stars, MIT, pushed September 24, 2026 (GitHub API, as of 2026-09-24)
- https://sourcery.ai/ - product page
- https://sourcery.ai/pricing/ - tiers as of 2026-09-24
- https://docs.sourcery.ai/reference/faq/ - docs FAQ covering plans, security scanning, BYO LLM, self-hosting (the former Product/Plans page redirects here)
- https://pypi.org/pypi/sourcery/json - the Python refactoring package, "Magically refactor Python", 23 releases
- https://hn.algolia.com/api/v1/items/27760608 - Show HN for the refactoring era, 15 points, July 7, 2021
- https://hn.algolia.com/api/v1/items/43944576 - user comparison of Sourcery vs Copilot, 3 points, May 10, 2025
- https://hn.algolia.com/api/v1/items/44224690 - critical thread, 1 point, June 9, 2025
