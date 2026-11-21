---
title: cubic
created: 2026-11-21
updated: 2026-11-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers choosing a hosted AI code reviewer who want the record on the closed-source
  product Cohere acquired on November 13, 2026, including what its benchmark claims can
  and cannot support.
---

cubic is a closed-source AI code review platform (a GitHub app with a pre-push CLI, desktop review apps, and nightly whole-codebase scans, built by the London team behind the mrge GitHub org) that Cohere acquired on November 13, 2026 to anchor its secure-coding vertical.

## What it is

**The pitch is review with whole-codebase context plus a human-friendly review surface, now with a frontier-model vendor behind it.**
Reviews run in an isolated container against the whole codebase and the team's rules, not just the diff, and the sandbox is torn down afterward with the code deleted per the YC launch post.
It learns rules from the team's past review comments, takes plain-English rules, auto-approves low-risk pull requests behind a 1-to-5 merge-confidence score, and hands findings to coding agents (Claude Code, Codex, Cursor) to fix.
Surfaces: PR comments through a GitHub app, a CLI that runs the same review before you push, a web and desktop review UI ("Linear for PRs": changes in reading order, architecture diagrams, a review inbox, two-way GitHub sync), nightly agent scans that open tickets and one-click fixes, and an MCP server beside Jira, Linear, Asana, and Confluence integrations.
It is proprietary SaaS from cubic (YC Spring 2025, London, six people at the acquisition, founder and CEO Paul Sanglé-Ferrière), whose public GitHub presence is the mrge-io org's MCP wrapper, a Kiro plugin, and benchmark mirror repos.

## Status

**Acquired and absorbed: Cohere bought cubic on November 13, 2026, terms undisclosed, its fourth acquisition of the year.**
Cohere's announcement says the team establishes Cohere's secure coding vertical, that the review agents "consistently ranked among the strongest performers on code review benchmarks", and that the product was built for on-premises and air-gapped enterprise deployments; cubic's own post promises the product keeps running and stays fully supported.
The product has no public repository to chart, so adoption reads from customers and benchmarks: Cal.com, n8n, Legora, Resend, and Cal.com appear on its surfaces, and GitHub's ReviewBench included it among the commercial entries GitHub pre-ran itself (a June 2026 test date, per The New Stack).
The Hacker News footprint on the acquisition is zero threads (Algolia search, 2026-11-21), so the deal's coverage lives in BetaKit, Dealroom, Seeking Alpha, and trade press, not community debate.

## Strengths

- **Benchmark evidence is genuinely third-party and dated: Martian's independent leaderboard had cubic at 65.7 percent F1 (73.2 precision, 59.6 recall) as quoted in its March 25, 2026 post, ahead of GitHub Copilot at 62.6, CodeRabbit at 60.2, Qodo at 59.0, and Cursor Bugbot at 57.0, on actual pull requests.**
- Whole-codebase context with cross-repo break detection (flagging a change that breaks code in another repo) is a substantive differentiator against diff-only reviewers.
- The human-side surface (reading-order changes, diagrams, merge-confidence scores, auto-approve of safe PRs) attacks the rubber-stamping problem, not only the finding problem.
- Nightly full-codebase scans with ticket creation and background fixes put it in the continuous-audit lane, not just PR comments.
- Now Cohere-owned, with model access and enterprise distribution a six-person startup could not match.

## Cautions

- **The "#1 on every independent benchmark" homepage claim is a vendor claim resting on its own March post about Martian's leaderboard, and the category's other public benchmarks cut against reading it plainly: the Agent Skills Hub eval (October 10) found none of its sixteen tested instruments beating a bare Claude Code control, and GitHub's ReviewBench opened with GitHub's own Copilot as its top entry (40.1 grounded F1) while cubic's entry was pre-ran by GitHub itself in June.**
- CodeRabbit's note records that vendor claiming number one on the same Martian benchmark by online F1 across nearly 300,000 pull requests, so two members of this category both claimed Martian's top spot in March 2026 on different metrics, both vendor-reported.
- Closed source end to end: your code transits a vendor cloud (with a stated no-storage, no-training policy and SOC 2 per trade coverage), and the acquisition gives Cohere every incentive to steer the product toward its platform.
- No community footprint on Hacker News for either the product or the acquisition, so the evidence base is vendor surfaces and deal press.
- The six-person team now works inside an 800-plus-person company with its own model agenda, so product priorities are Cohere's, not cubic users'.

## Pricing

**Per-seat SaaS with a free trial, as of 2026-11-21.**
Team is $40 per developer per month billed monthly with a minus-20-percent yearly rate, covering 40,000 reviewed lines per developer, auto-fix, five custom review agents, auto-approvals, and five private wikis.
Pro is $99 monthly at the same yearly discount, with 80,000 lines, ten custom review agents, codebase scans for three repos, Confluence and MCP integrations, and premium support.
Max is $200 monthly with twice the review allowance.
Trade coverage of the acquisition records a free starter tier and reads the yearly rates as $30, $79, and $160.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-21 | Team, Pro, Max | Baseline at note creation: Team $40, Pro $99, Max $200 per developer per month billed monthly, minus 20 percent billed yearly; free trial, no credit card. | [cubic.dev/pricing](https://www.cubic.dev/pricing) |

## Compared to

- [CodeRabbit](../coderabbit/index.md): the other commercial anchor, with learned rules and a far bigger install base; cubic bets on whole-codebase context and the human review surface, and now has Cohere behind it.
- [Greptile](../greptile/index.md): the hosted reviewer selling whole-repo graph context and learned rules as its differentiator; cubic's whole-codebase claim is the same bet with an acquirer's war chest.
- [Graphite Diamond](../graphite-diamond/index.md): the category's prior consolidation case, reviewed inside Cursor's platform; cubic is the same pattern one vendor later, and its note is the template for what to watch.

## Bottom line

**Recommended for GitHub-centric teams that want a hosted reviewer with whole-codebase context, auto-approve, and nightly scans, and that are comfortable with a Cohere-owned closed product.**
Not for teams that need open source, GitLab-first workflows, or benchmark results they can reproduce themselves.
My disagreeable take: cubic is the first reviewer in this category acquired for its benchmark record rather than its install base, and the right question for Cohere is whether the ranking survives the absorption, because acquirers historically optimize their acquisitions toward platform pull, not benchmarks.

## Changes

- 2026-11-21 - Created after the 2026-11-21 dedicated-list search surfaced the Cohere acquisition and reopened the 2026-08-30 weak-tail rejection on traction; twelve sources fetched this run, including the zero-thread HN acquisition search as the community-footprint signal.

## See also

- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - the category matrix this note joins
- [CodeRabbit](../coderabbit/index.md) - the rival claiming the same benchmark's top spot on a different metric
- [Graphite Diamond](../graphite-diamond/index.md) - the category's prior acquisition-consolidation case
- [ReviewBench](../../evaluation-review/reviewbench/index.md) - GitHub's benchmark, which ran cubic under vendor-conflict cautions
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - the corpus essay this category answers

## References

- https://www.cubic.dev/ - the product surface: whole-codebase review, plain-English rules, auto-approve with merge confidence, nightly scans, CLI, desktop apps, the Cal.com testimonial, fetched 2026-11-21
- https://www.cubic.dev/pricing - Team $40, Pro $99, Max $200 per developer per month billed monthly with minus-20-percent yearly rates, fetched 2026-11-21
- https://www.cubic.dev/blog/cubic-joins-cohere - the founder's acquisition post: the product keeps running and stays fully supported, fetched 2026-11-21
- https://www.cubic.dev/blog/cubic-is-the-best-ai-code-reviewer-on-martian-s-benchmark - the March 25, 2026 benchmark post: 65.7 percent F1 leading the Martian table ahead of Copilot, CodeRabbit, Qodo, and Bugbot, fetched 2026-11-21
- https://cohere.com/blog/cohere-expands-its-sovereign-ai-platform-with-aisle-and-cubic - the acquirer's announcement (November 13, 2026): the secure-coding vertical, the benchmark ranking claim, the on-premises and air-gapped deployment lineage, fetched 2026-11-21
- https://betakit.com/cohere-buys-ai-code-review-startup-cubic-as-acquisition-spree-continues/ - the third-party deal record: terms undisclosed, London-based per YC, fourth 2026 acquisition (fetched through search full text 2026-11-21; the site 403s plain curl, the wall recorded)
- https://secnews.co.uk/2026/11/cohere-acquires-cubic-london-ai-code-review/ - the critical detail source: YC Spring 2025, team of six, the free starter tier and yearly-rate reading, SOC 2 and no-storage claims, and the announcement post's silence on pricing and data terms, fetched 2026-11-21
- https://www.ycombinator.com/companies/cubic - YC Spring 2025, London, team size 6, founder Paul Sanglé-Ferrière, the merge-28-percent-faster claim and the launch demo pull request, fetched 2026-11-21
- https://api.github.com/orgs/mrge-io - the org behind cubic.dev (website field cubic.dev), holding the cubic MCP wrapper, the Kiro plugin, and benchmark mirror repos, fetched 2026-11-21
- https://api.github.com/repositories/350360184/pulls/20771 - the cal.com launch-demo pull request behind the YC post's see-it-in-action link, closed, created 2025-04-18, fetched 2026-11-21
- https://codereview.withmartian.com - the Martian benchmark site (a client-rendered shell to fetchers, so its current board is grounded in the two vendors' March 2026 posts rather than quoted), fetched 2026-11-21
- https://hn.algolia.com/api/v1/search?query=cubic%20cohere&tags=story - the zero-hit acquisition search, the community-footprint signal (queried 2026-11-21)
