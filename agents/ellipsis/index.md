---
title: Ellipsis
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Written for software engineers and engineering leaders evaluating AI code
  review or coding-agent infrastructure, who already know what a PR review bot
  is and what agents like Claude Code and Codex do, and who need to know what
  Ellipsis is today rather than what it was in 2024.
---

Ellipsis (ellipsis.dev) is a YC-backed company that launched in 2023 as an automated PR review and bug-fix bot and, as of July 2026, has pivoted to the Ellipsis Agent Cloud, a managed cloud platform for running coding agents such as Claude Code and Codex in governed sandboxes.
Facts below verified as of 2026-09-04.

## What it is

Ellipsis AI Inc (New York, founded 2023, YC Winter 2024, founders Hunter Brooks and Nick Bradford) sells a platform where every coding agent is a YAML file in your repo, and each session runs in its own sandbox with scoped credentials, hard budget caps, and searchable transcripts.
Sessions start from GitHub, Slack, Linear, or Sentry events, cron schedules, the `agent` CLI, or a REST API, and the platform fronts Claude Code, Codex, Copilot, Gemini, Cursor, Grok Code, Antigravity, OpenCode, and Pi.
Code review survives as a configurable agent use case, not the fixed install-and-forget bot of 2024, and the platform deploys either in Ellipsis's cloud or into your own AWS VPC.
The core product is proprietary: its GitHub org publishes only tooling, an agent CLI, a homebrew tap, an AWS installer, and Python plus TypeScript SDK mirrors, five public repos in total as of 2026-09-02.

## Status

**Active and pivoted.**
The July 28, 2026 post "Introducing the Ellipsis Agent Cloud" says it plainly: Ellipsis "launched in 2023 as one of the first AI Code Review bots", but teams no longer want a product that "just worked", so the company rebuilt itself as agent infrastructure and released the `agent` CLI.
The homepage, docs, and pricing all describe the agent cloud as of 2026-09-02, and the GitHub org pushed to its CLI and SDK repos on 2026-09-01.
Funding is a $2M seed announced June 19, 2024, with YC partners and the Pioneer Fund among the investors; I found no later round on any page I fetched.
The blog is thin, three original posts since January 2025 and a gap from April 2025 to July 2026, so public cadence evidence is sparse even though the product is clearly alive.
The community footprint is one strong Show HN from May 9, 2024 (Algolia item 40309719, 121 points, 64 comments) and a quieter February 2024 one (item 39526616, 18 points, 11 comments).

## Strengths

- Agents as code: each agent is a versioned YAML file changed by pull request, so configuration gets reviewed like any other code.
- Governance is built in: per-session scoped tokens, budget caps enforced before a sandbox starts, and full searchable transcripts of every session.
- Harness-agnostic: the same interface fronts Claude Code, Codex, OpenCode, and others, so the platform layer does not lock you to one agent vendor.
- Security posture: zero source retention (code is deleted with the sandbox), SOC 2 Type I certified with Type II in progress as of 2026-09-02, and a BYOC path into your own AWS VPC.
- The founders were candid in 2024 that frontier LLMs were not good enough to write code autonomously, only to review it, which matched the product to what models could actually do.

## Cautions

- The 2024 review bot no longer exists as a product; the launch post says the install-and-forget model "is not the case anymore", so getting review out of Ellipsis means writing and maintaining YAML.
- The public footprint is thin: a ten-month blog gap, five public repos, and an agent CLI at 2 stars as of 2026-09-02, so third-party validation is limited.
- Headline claims are company data: "merge pull requests 13% faster" comes from the seed post, and "most popular AI Code Review agent among YC founders" comes from the company's own launch post.
- HN critics were blunt about the review era, calling the PR summaries noise and telling maintainers "please stop making open source worse".
- The founder admitted on that thread that the company had no hard numbers ("all our data is qualitative") as of May 2024.
- Cost risk sits with you: token spend is usage-based on top of metered compute, and optional support packages start at $5,000/month.

## Pricing

Tokens are billed at cost with no markup, plus a 10% platform fee, with CPU at $0.142/vCPU-hour and memory at $0.024/GB-hour, as of 2026-09-02.
There are no per-seat fees and no idle charges, and a $100 credit covers the start.
The same published pricing covers the managed SaaS and a BYOC deployment into your own AWS account.
Optional enterprise support packages run $5,000 (Standard), $7,500 (Advanced), and $15,000 (Premier) per month.
This replaces the May 2024 model, which was $20/seat/month for the review bot.

## Compared to

[Greptile](../greptile/index.md) is the closest sibling that stayed a review product: it reviews PRs against the whole codebase without you owning agent config, which is exactly what Ellipsis gave up.
[CodeRabbit](../coderabbit/index.md) and [Qodo](../qodo/index.md) sell finished review and test agents, so try them first if you want zero YAML.
Ellipsis's real 2026 competition is not review bots but agent infrastructure: the company itself publishes compare pages against running Claude Code on GitHub Actions, which is the option many teams will try first because their organization already pays for it.

## Bottom line

**Recommended for teams running fleets of coding agents that need budgets, permissions, and searchable logs around Claude Code or Codex. Not for teams that want an install-and-forget AI reviewer, because Ellipsis no longer sells that product.**
I will take the unpopular position that leaving review was the right call: a fixed review bot was always a feature, not a company, and Ellipsis read that earlier than most of the 2024 class.

## See also

- [Greptile](../greptile/index.md) - the AI code review sibling that stayed a review product, the closest match to what Ellipsis abandoned.
- [OpenCodeReview](../open-code-review/index.md) - another AI review entry in this section, useful to contrast productized review with agent-defined review.
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the tracker that situates agent clouds like Ellipsis in the wider tooling map.
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - the feature matrix for this category, where agent cloud platforms are compared row by row.

## References

- https://www.ellipsis.dev/ - current product surface: agent cloud framing, $100 credit, SOC 2 status, supported agents, fetched 2026-09-02.
- https://www.ellipsis.dev/pricing - the token-plus-10% model, compute rates, BYOC terms, and support package tiers, fetched 2026-09-02.
- https://www.ellipsis.dev/docs - docs on environments, sandboxes, sessions, the CLI, and the API, fetched 2026-09-02.
- https://www.ellipsis.dev/blog - publishing cadence and post dates, fetched 2026-09-02.
- https://www.ellipsis.dev/blog/the-ellipsis-agent-cloud - the July 28, 2026 pivot announcement by the founder, fetched 2026-09-02.
- https://www.ellipsis.dev/blog/ellipsis-raises-a-2m-seed-round - the $2M seed, investor list, and the 13% faster-merge claim, fetched 2026-09-02.
- https://www.ycombinator.com/companies/ellipsis - YC batch (W24), founding date, founders, team size, and active status, fetched 2026-09-02.
- https://hn.algolia.com/api/v1/items/40309719 - the May 9, 2024 Show HN (121 points, 64 comments) with the praise and criticism threads, fetched 2026-09-02.
- https://hn.algolia.com/api/v1/search?query=ellipsis&tags=story - the Algolia search that located both Show HN items, fetched 2026-09-02.
- https://github.com/ellipsis-dev - the public org (five repos including Python and TypeScript SDK mirrors, CLI pushed 2026-09-01), verified via the GitHub API on 2026-09-02.
