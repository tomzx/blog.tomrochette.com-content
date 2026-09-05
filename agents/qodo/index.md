---
title: Qodo
created: 2026-08-30
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, open-source, developer-tools]
readability: 3
audience_notes: >
  Software engineers evaluating AI pull request reviewers, who know what a
  GitHub Action and a webhook are, have heard of CodeRabbit and Copilot code
  review, and want to compare licensing, self-hosting, and cost before
  installing a bot on their repositories.
---

Qodo is an AI code review and governance platform (formerly CodiumAI) whose MIT-licensed PR-Agent was marketed as the original open-source AI PR reviewer, and which has now donated that reviewer to the community while selling the heavier product above it.
Facts below verified as of 2026-09-05.

## What it is

**Two products share one name, and the gap between them is the whole story.**
The open-source half is PR-Agent (now under the PR-Agent GitHub organization), a community-maintained reviewer that runs /describe, /review, /improve, and /ask as PR comments or CLI calls against GitHub, GitLab, Bitbucket, Azure DevOps, and Gitea, self-hosted with any model LiteLLM can reach.
The commercial half is Qodo (the former Qodo Merge), a hosted review platform with a context engine, rules mined from PR history, cross-repo review, and dashboards.
The repo description draws the line in one sentence: "This project is not the Qodo free tier."

## Status

Active on both halves, and deliberately splitting apart.
The repo counts 12,861 stars and 1,805 forks as of 2026-09-05, MIT-licensed, pushed September 4, 2026, with v0.44.0 released Aug 30, 2026, and the former qodo-ai/pr-agent URL now redirects to the repo's new home in the standalone PR-Agent organization.
The company raised $11M in 2023, then $40M in September 2024 ($50M total), by which point TechCrunch already called it "Qodo, the startup previously known as CodiumAI".
The README states Qodo donated PR-Agent to the community, the project has its first external maintainer, and it is being donated to an open-source foundation.
The company's badges report 900.9K VS Code and 647.1K JetBrains extension installs plus roughly 12.8K Marketplace installs for the paid app, as of 2026-09-05.
On Hacker News the reviewer itself never caught fire (best thread 24 points, item 41500840), while company research posts reached 139 (item 44874736) and 87 points (item 41838348), and the Kudelski exploit write-up got 1 point (item 46824997).

## Strengths

- The only tool in this comparison series with a genuinely open, MIT-licensed core you can self-host and point at any model through LiteLLM.
- Each tool is a single LLM call at roughly 30 seconds, so cost is predictable, with token-aware PR compression for large diffs.
- The command surface is documented and boring: /describe, /review, /improve, /ask, /add_docs, /generate_labels, /similar_issue, /update_changelog.
- Since v0.39.0 the OSS agent feeds AGENTS.md and SKILL.md files to /review, /describe, and /improve by default, so it picks up repo conventions out of the box.
- The commercial platform adds what review programs actually fight about: rules mined from PR history, cross-repo review across Git providers, and BYOK or on-prem deployment.

## Cautions

- The README now calls the OSS project a "community-maintained legacy project" and contrasts it with the "feature-rich, context-aware" commercial offering, which is the vendor telling you where the real product lives.
- Kudelski Security walked from a PR comment to RCE and an AWS admin key on Qodo Merge Pro (all fixed as of October 2025), and the root cause, config overrides injected through PR comments and repo config files, is a design decision in the open tool too.
- A developer reported leaving the JetBrains plugin over near-zero public activity and piled-up issues (HN comment 45880645, November 2025).
- The "highest F1-score" claim on the homepage is measured on the company's own benchmark, not a neutral one.
- There is no permanent free tier for the commercial product, credits expire monthly, and the historical $19/month PR-Agent Pro plan is gone.
- /help_docs sits disabled in the OSS tool since v0.36.1 over a credential-exposure bug (issue #2445), a window into community-maintenance pace.
- The company renamed itself from CodiumAI and retro-edited old blog posts to insert "(now Qodo (formerly Codium))", which muddies citations of its own history.

## Pricing

PR-Agent is free under MIT, self-hosted with your own LLM keys.
The commercial product meters pooled credits at $0.012 each, with packs sized around 18, 36, or 144 reviews per month, under a Pro Team plan listed at $30 with monthly billing, no annual commitment, and up to 30 users, as of 2026-09-02.
Enterprise adds SSO/SAML, audit logs, BYOK, single-tenant SaaS or on-prem, cross-repo review, and negotiated pricing.
Qualified open-source projects get the commercial reviewer free through a Marketplace app powered by Google.
For history: in September 2024 the paid Chrome-extension tier was $19 per month for private repos (item 41443605), so the model has moved twice in two years.

## Compared to

[Greptile](../greptile/index.md) and [CodeRabbit](../coderabbit/index.md) are commercial-first rivals; if you need an MIT-licensed core you can self-host, Qodo is the one in this series that still ships it, and Kudelski's research series covers exploit chains in both Qodo and CodeRabbit.
[Open Code Review](../open-code-review/index.md) takes the no-vendor path, and the LaReview author's complaint that bots like PR-Agent "mostly comment file-by-file" and auto-post noise (item 46659042) is exactly the dissatisfaction that path answers.
[Ellipsis](../ellipsis/index.md) sat in the same PR-automation aisle before its 2026 pivot to agent infrastructure; its note carries the review-versus-hosting comparison.

## Bottom line

**Recommended for teams that want a self-hostable, MIT-licensed reviewer with a boring, inspectable command surface, and for enterprises that want rule enforcement and governance with BYOK or on-prem deployment. Not for developers hunting a permanent free tier for private repos, because that tier no longer exists.**
I also think the PR-Agent donation is less a gift than a repositioning: the repo itself says "community-maintained legacy project", and I read that as the vendor conceding that the single-LLM-call reviewer is a commodity, so anyone adopting the OSS half for the long haul is adopting code the company has already stopped competing on.

## See also

- [Greptile](../greptile/index.md) - the codebase-aware SaaS rival, for readers weighing hosted context depth against self-hosted control.
- [Open Code Review](../open-code-review/index.md) - the no-vendor path this donation-and-funnel story is a reaction to.
- [Copilot Automations](../copilot-automations/index.md) - GitHub-native review automation for readers staying inside one vendor.
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the shared-rows comparison where this note's cells are traced.
- [Agents.md](../agents-md/index.md) - why v0.39+ feeding AGENTS.md by default matters for repo-convention-aware review.

## References

- https://api.github.com/repos/qodo-ai/pr-agent - redirects to The-PR-Agent/pr-agent, the repo's new home; stars, forks, push date, MIT license, and the "This project is not the Qodo free tier" description, queried as of 2026-09-05.
- https://github.com/qodo-ai/pr-agent - README: donation to the community, tools table, platforms, release notes, sponsor status, "legacy project" wording.
- https://docs.pr-agent.ai/tools/ - the full OSS command surface, including the /help_docs disabling.
- https://www.qodo.ai/ - positioning, context engine, rules system, self-reported benchmark claim, credit FAQ, install badges.
- https://www.qodo.ai/pricing/ - Pro Team $30, $0.012 per credit, pack sizes, plan comparison, no permanent free tier, credits expiring monthly.
- https://www.qodo.ai/solutions/open-source/ - free commercial review for qualified OSS projects.
- https://www.codium.ai/blog/codiumai-powered-by-testgpt-accounces-beta-and-raised-11m/ - the $11M seed and the original test-generation mission.
- https://techcrunch.com/2024/09/30/qodo-raises-40m-series-a-to-bring-quality-first-code-generation-to-the-enterprise/ - the $40M Series A, $50M total, and the CodiumAI-to-Qodo rename.
- https://kudelskisecurity.com/research/qodo-dynaconf-aws-admin-key-leaked-twice - critical source: PR comment to RCE and AWS admin key on Qodo Merge Pro, fixed October 2025.
- https://hn.algolia.com/api/v1/search?query=pr-agent&tags=story - PR-Agent's thin HN footprint (18 stories, best 24 points) and the 2024 $19/month pricing quote.
- https://hn.algolia.com/api/v1/items/45880645 - critical developer comment on Qodo plugin maintenance, November 2025.
- https://www.qodo.ai/blog/codiumai-or-codeium-which-are-you-looking-for/ - the Codeium name confusion and the retro-edited "formerly Codium" branding.
- https://docs.qodo.ai/qodo-documentation - commercial surface: code review, governance, cross-repo review, rule miner.
