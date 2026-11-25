---
title: Kortix
created: 2026-11-24
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, orchestration, multi-agent, agent-platform, event-driven, elastic-license]
readability: 3
audience_notes: >
  Engineers and team leads evaluating a self-hostable agent platform for always-on company agents, who
  already know what an agent harness, a webhook trigger, and a Docker Compose deployment are, and who need
  to weigh a non-OSI license and vendor-authored evidence against a 20k-star repository.
---

Kortix CompanyOS is the open-source agent platform from Kortix AI that runs always-on agents on their own cloud computers, started by schedules, webhooks, and messages, with one router agent handing work to swarms of custom agents defined as files in a git repository.

**Its bet is that a company's agents, skills, rules, and connectors should live in one repository as code, while the platform supplies what a single chat session cannot: event triggers, per-session computers that sleep and wake, and a person-approved change request before anything reaches main.**

## What it is

Kortix calls CompanyOS "the cloud-native agent harness for companies", and the repository description calls it "the open-source operating system for your company".
You write custom agents on pi, an open-source agent harness, and declare each with its prompt, model, permissions, skills, tools, and connectors as files in one git repository, so a `kortix.yaml` plus an agents tree is what you review and ship through the `kortix` CLI.
Every session runs on its own cloud computer that sleeps 15 to 20 minutes after the last turn and wakes on the next message or event with its history, and state lives in the repository, in Drive (the shared folders and company memory), in the session's workspace, and in the session record.
Triggers start agents from schedules, signed webhooks, connector events, App events, and merged change requests, with a filter in code that drops noise before any model runs.
You talk to one built-in agent, My Kortix, which hands writing, research, code, and app work to the agent built for it in a session of its own and reports back, and sessions hand work to each other in background swarms that the README says scale to "thousands of agents in parallel on one config".
An Outcome pairs a goal with a definition of done, and a separate verifier session that did none of the work decides whether each criterion passed.
Agents reach more than 3,000 apps through connectors plus MCP, OpenAPI, GraphQL, and raw HTTP, and people reach the agents from web, desktop, and mobile apps, the terminal, Slack, Microsoft Teams, and email.
The stack is TypeScript with a `dev` default branch, the license is Elastic License 2.0, and Kortix AI Corp was founded by Marko Kraemer and Domenico Gagliardi.

## Status

Active and shipping several releases a week on a 0.16.x train: v0.16.5 on 2026-11-25 (agents signing in to websites with a login the person fills in and the sandbox browser types, dictation on web, desktop, and mobile billed per second of audio in credits, artifact folders, stateless sandboxes the default on every deployment, and Kortix in Chrome and Network-Enforced Secrets on in every workspace) after v0.16.4 on 2026-11-22 (Kortix in Chrome public on the Chrome Web Store, configuration commits naming their author) after v0.16.2 (2026-11-20), v0.16.1 (2026-11-19), and v0.16.0 (2026-11-18), with the default branch pushed 2026-11-25 (GitHub API, as of 2026-11-25).
The repository was created 2024-10-05 and stands at 20,789 stars with 3,477 forks and 80 open issues as of 2026-11-24.
Its top contributor is the founder's account at 8,526 commits, beside an `agent-kortix` account at 2,217 and one other person above 3,000 (GitHub API, as of 2026-11-24).
**The identity is two pivots old in eighteen months: it launched in April 2025 as Suna, a generalist open-source agent, and became Kortix CompanyOS through pull request #11093, merged 2026-10-29.**
The old `kortix-ai/suna` path now resolves to the CompanyOS repository.
An earlier rebrand to "the open-source AI Operating System" landed on 2026-10-04 and was reverted the same day, per the v0.13.51 release notes.
The v0.14.0 release of 2026-10-16 replaced per-seat plans with one credits plan and made Enterprise a feature layer, so the commercial model moved twice in the same month as the name.
The independent record is thin: Hacker News carries four stories about it, none above 4 points (Suna's 2025-04-22 submission, a 2025-05-22 Show HN at 1 point, a 2025-06-29 post at 4 points, and a 2-point "Kortix" story on 2026-07-08), the 2025-11-18 relaunch announcement is a company press release carried on Yahoo Finance, and the rest is directory listings.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kortix-ai/CompanyOS&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kortix-ai/CompanyOS&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kortix-ai/CompanyOS&type=date&legend=top-left" />
</picture>

## Strengths

- **The session model separates compute from state**: an agent sleeps at no compute cost, wakes on an event with its full history, and continues in a fresh context by searching its own record when one fills, instead of running on a summary.
- Company as code is literal: agents, skills, rules, and connectors are versioned files you review like software, and `kortix init` and `kortix ship` treat the whole repository as one deployable.
- Changes land through a change request a person approves, with merge deny-by-default for agents, and an Outcome's verifier is a separate session, so an agent cannot mark its own goal done.
- Self-hosting runs the same images as the managed cloud from one Docker Compose stack in your own cloud account, VPC, or on-prem network.

## Cautions

- **Elastic License 2.0 is not an open-source license**: you may not provide the software to third parties as a hosted or managed service, and you may not circumvent its license-key functionality, so "open source" is the vendor's wording and GitHub reports NOASSERTION.
- The white-label route has a condition: it lifts the hosted-service limit only if Platinum is your exclusive compute provider.
- A self-hosted install is not a disconnected one, because agent sandboxes run on the provider you configure (Platinum by default) and the stack pulls its images from Docker Hub.
- The evidence is the vendor's: the parallel-scale claim, the case studies, and the SOC 2 Type I line all come from Kortix's own README, and the one third-party assessment I found notes that approval rules are off until you set them and that it has not tested the product.
- Expect positioning and pricing to move again, after Suna, the reverted operating-system rebrand, CompanyOS, and the per-seat to credits switch all landed inside eighteen months.

## Pricing

As of 2026-11-24 the cloud product has three plans.
Free costs $0 and includes 500 credits a month on your first workspace, with models on your own API key or ChatGPT subscription and no card needed.
Credits runs from $50 a month (5,000 credits) to $50,000 a month (5,000,000 credits) at 100 credits per dollar, where the default 2 vCPU, 4 GB, 20 GB agent computer uses about 11 credits an hour; members are unlimited, unused credits roll over one month, and top-ups never expire.
Model usage is billed separately: your own API keys are free for the first $1,000 a month and then carry a 5 percent fee paid from credits, and Kortix-managed models (DeepSeek, GLM) cost the provider's base price plus a 5.5 percent platform fee.
Enterprise is custom-priced and adds SAML SSO, SCIM directory sync, advanced RBAC, audit logs, Cloud, VPC, or on-prem deployment, an SLA, and a DPA.
Self-hosting carries no fee to Kortix; you pay the sandbox compute provider and the model provider.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-16 | Credits | per-seat plans retired for one credits plan from $50 a month with top-up bonuses and a 5.5 percent model fee; existing plans converted to credits at the same monthly price (v0.14.0) | https://kortix.com/changelog/releases/page/4 |
| 2026-11-24 | Free, Credits, Enterprise | baseline: Free $0 with 500 credits a month on the first workspace; Credits $50 to $50,000 a month at 100 credits per dollar; Enterprise custom | https://kortix.com/pricing |

## Compared to

**[Dify](../dify/index.md)** is the platform-tier precedent: a visual workflow and RAG builder under a modified Apache license, where Kortix sells always-on event-driven agents on per-session computers and keeps its license further from open source.
**[AutoGPT](../autogpt/index.md)** is the other autonomous-agent platform that grew a hosted tier; AutoGPT pairs a block-based builder with a marketplace, Kortix pairs a router agent with swarms of repository-defined agents.
**[Omnara](../omnara/index.md)** is the open-source control plane that turns agents into YAML configs supervised from dashboard, phone, and Slack; it leaves compute to your machine pools, where Kortix sells the computers.
Choose Kortix for event-triggered company agents on per-session cloud computers, Dify for visual business-app workflows under a friendlier license, and Omnara for a control plane over machines you already run.

## Bottom line

Recommended for teams that want always-on, event-triggered agents with company memory in a repository they own, and that can accept a non-OSI license, vendor-backed compute, and vendor-authored evidence.
Not for anyone who needs to offer it as a hosted service, to run it disconnected from Platinum and Docker Hub, or to cite an independent measurement before adopting.

## Changes

- 2026-11-24 - Created, landing the admission the cross-category scan routed to orchestration on 2026-11-12 on the platform-tier Dify precedent.
- 2026-11-25 - Volatile refresh: recorded v0.16.5 (2026-11-25, website logins for agents, dictation billed per second of audio in credits, artifact folders, stateless sandboxes the default on every deployment) on the 0.16.x train, the push date refreshed to 2026-11-25.

## See also

- [Dify](../dify/index.md) - the platform-tier precedent with the friendlier license and a visual builder instead of swarm sessions
- [AutoGPT](../autogpt/index.md) - the other autonomous-agent platform that rebuilt itself around a hosted tier
- [Omnara](../omnara/index.md) - the control plane over your own machine pools, where Kortix supplies the computers
- [Hive](../hive/index.md) - the other runtime whose lead agent spawns workers; Hive clones one Queen on one runtime, Kortix hands work out to separate computers
- [Sandcastle](../sandcastle/index.md) - the TypeScript library that also gives each agent a cloud sandbox, as a library rather than a platform

## References

- https://api.github.com/repos/kortix-ai/CompanyOS - repository metadata: created 2024-10-05, default branch dev, pushed 2026-11-24, 20,789 stars, 3,477 forks, 80 open issues, license detected NOASSERTION, as of 2026-11-24.
- https://raw.githubusercontent.com/kortix-ai/CompanyOS/dev/README.md - the cloud-native agent harness pitch, the session, trigger, swarm, and outcome model, the connector and reach tables, self-hosting with Platinum sandboxes, the security and SOC 2 line, and the white-label condition.
- https://raw.githubusercontent.com/kortix-ai/CompanyOS/dev/LICENSE - the Elastic License 2.0 terms, hosted-service and license-key limits included.
- https://kortix.com/docs/guide - the Outcomes guide: a separate verifier session that did none of the work decides each criterion, and only Kortix can change a goal's record.
- https://api.github.com/repos/kortix-ai/CompanyOS/releases?per_page=8 - the release feed, v0.16.5 (2026-11-25) back to v0.15.11 (2026-11-14); re-fetched 2026-11-25.
- https://api.github.com/repos/kortix-ai/CompanyOS/contributors?per_page=10 - the contributor split (markokraemer 8,526, Ino-Bagaric 3,714, agent-kortix 2,217).
- https://api.github.com/repos/kortix-ai/CompanyOS/pulls/11093 - the Kortix CompanyOS rebrand pull request, merged 2026-10-29.
- https://api.github.com/repos/kortix-ai/suna - the old repository path, which resolves to kortix-ai/CompanyOS.
- https://kortix.com/changelog/releases/page/5 - the v0.13.51 release notes of 2026-10-06, which list the 2026-10-04 AI Operating System rename and its same-day revert.
- https://kortix.com/changelog/releases/page/4 - the v0.14.0 release notes of 2026-10-16: one credits plan, Enterprise as a feature layer.
- https://kortix.com/pricing - the Free, Credits, and Enterprise plans, the credit and compute rates, and the model-billing rules, as of 2026-11-24.
- https://kortix.com/security - the vendor's security page: one isolated machine per session, merge deny-by-default for agents, SAML 2.0 and SCIM, and the SOC 2 Type I claim.
- https://finance.yahoo.com/news/kortix-relaunches-bring-open-source-180000954.html - the 2025-11-18 relaunch press release naming the founders and the April 2025 launch of Suna.
- https://theindependentai.com/tool/kortix - the third-party directory assessment: Elastic License 2.0 reading, the white-label condition, approval rules off until set, and no hands-on test, checked 2026-11-13.
- https://hn.algolia.com/api/v1/search?query=Kortix&hitsPerPage=20 - the four Hacker News stories about Suna and Kortix, none above 4 points.
