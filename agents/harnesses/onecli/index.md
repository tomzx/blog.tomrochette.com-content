---
title: OneCLI
created: 2026-08-30
updated: 2026-09-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, security, sandboxing, teams]
readability: 3
audience_notes: >
  Engineers and security leads evaluating team-scale agent deployment who know what
  a sandbox, a credential gateway, and BYOC mean, and who have been burned by prompt-based permissions.
---

OneCLI is an open-source YC S26 agent harness for teams that gives every employee a sandboxed personal agent whose tool calls pass through a credential-injecting gateway, so no agent ever holds a real secret.
Facts below verified as of 2026-09-22.

**OneCLI's bet is that enforcement belongs outside the model at the network layer, and after pivoting from vault to team harness it is the only entry in this section built for the security buyer first and the engineer second.**

## What it is

Apache-2.0, TypeScript core with Rust gateway heritage, self-hostable with a `git clone` plus pnpm quickstart or usable as hosted cloud.
It launched in March 2026 as a Rust credential vault for autonomous agents (Hermes, OpenClaw, NanoClaw), then pivoted to v2: one agent per employee, an isolated VM per agent, and one workspace-wide policy.
The gateway injects scoped credentials per request after authorization, so a stolen agent holds nothing worth stealing.
Team primitives include identity-provider provisioning, deterministic human-in-the-loop approvals in chat, Slack access, and audit logs.
The Launch HN title calls it an "OSS sandboxed agent harness for teams", and that framing is the product: the sandbox and gateway are the mechanism, the team is the customer.

## Status

Very active: v2.6.0 released September 8, 2026, five days after v2.5.0 on September 3, which itself followed v2.4.0, v2.3.1, and v2.3.0.
3,509 stars and 234 forks as of 2026-09-22, on a repository created March 8, 2026.
Three Hacker News threads of record: 161 points for the vault (March 12), 110 for the credential gateway (July 23), and 88 for the YC launch (August 19).
YC S26, San Francisco, founded by Jonathan Fishner (CEO) and Guy Ben Aharon (CTO).
In its vault era it was adopted by NanoClaw, per the NanoClaw note in this section.

## Strengths

- **The security model is architectural, not prompt-based**: credentials injected per request, rules enforced at the gateway, rate limits on runaway agents, approvals before sensitive actions.
- Team primitives nobody else in this section ships: IdP integration, per-employee agents, one policy surface, shared connections granted without ever being handed over.
- Genuinely open (Apache-2.0) with a documented community-edition self-host path, not just an open-core sticker.

## Cautions

- The coding-harness layer inside is deliberately thin; if you want a tunable local agent, this manages who may do what, not how well code gets written.
- The platform is six months old and the API moved from vault to team harness inside that window, so integration code will churn.
- 154 open issues and pull requests as of 2026-09-22.
- Pricing jumps from $0 (3 seats, 500 calls/month) to $149/month, and BYOC starts only at the paid tiers.

## Pricing

Free at $0 with $5 AI credits, 500 calls/month, 3 seats, and 3 agents.
Team is $149/month for 5 users and 10 agents when you bring your own model keys (BYOC), or $499/month with hosted models included.
Scale is $499/month for 10 users and 20 agents BYOC, or $1,999/month with hosted models.
Extra seats are $49/user/month with your own key or $199 with hosted models.
Enterprise custom, and platform self-hosting (your cloud, VPC, or on-prem) is quoted there.
The Apache-2.0 core remains self-hostable from source without a commercial license per the README.
All as of 2026-09-22.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-13 | All tiers | Baseline: Free $0 ($5 AI credits, 500 calls/mo, 3 seats), Team $149/mo BYOC or $499 with hosted models, Scale $499/$1,999, extra seats $49/$199 per user/mo, Enterprise custom. | [onecli.sh/pricing](https://onecli.sh/pricing) |

## Compared to

- [NanoClaw](../../assistant-runtimes/nanoclaw/index.md): the personal multi-agent runtime that adopted OneCLI's vault; NanoClaw serves one operator, OneCLI v2 serves the whole org.
- [Conductor](../../orchestration/conductor/index.md): team-scale parallel agent work without a credential gateway; pick Conductor for shipping velocity, OneCLI for least privilege.
- [Agent Sandbox](../../sandboxing/agent-sandbox/index.md): the isolation concepts OneCLI productizes into a managed platform.

## Bottom line

**Recommended for security-conscious teams deploying shared agents against company tools (GitHub, Gmail, Notion, CRM), especially with a self-host requirement.**
Not for solo engineers who want a coding harness, and not for anyone allergic to per-seat SaaS.
I think the prompt-based permission systems across every other harness in this section are security theater, and OneCLI is the only entry whose answer still works when the model is wrong.

## Changes

- 2026-08-30 - Created when the candidate-resolution run accepted it into Harnesses as the per-request credential-injection team harness.
- 2026-09-02 - Recorded the restructured hosted tiers that arrived with v2.4.0.
- 2026-09-16 - Refreshed repository counters (3,485 stars, 151 open issues and pull requests); pricing tiers re-verified unchanged.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the harness layer this team platform extends
- [NanoClaw](../../assistant-runtimes/nanoclaw/index.md) - the adopter of its earlier vault
- [Agent Sandbox](../../sandboxing/agent-sandbox/index.md) - the isolation concepts it productizes
- [Sandboxing Feature Matrix](../../sandboxing/sandboxing-feature-matrix/index.md) - the sandboxing treatment across the section
- [Conductor](../../orchestration/conductor/index.md) - team-scale agents without the gateway

## References

- https://github.com/onecli/onecli - repository state, license, stars, and v2 pivot story as of 2026-09-22
- https://github.com/onecli/onecli/releases - release cadence through v2.6.0 on September 8, 2026
- https://onecli.sh - product positioning, gateway model, and free tier as of 2026-09-22
- https://onecli.sh/pricing - tiers, BYOC versus hosted-model pricing, and seat limits as of 2026-09-22
- https://onecli.sh/docs - architecture: sandbox, gateway, policy, self-hosting
- https://www.ycombinator.com/companies/onecli - YC S26 batch, founders, and launch description
- https://news.ycombinator.com/item?id=49363710 - 88-point Launch HN, August 19, 2026
- https://news.ycombinator.com/item?id=47353558 - 161-point vault-era thread, March 12, 2026
- https://news.ycombinator.com/item?id=49023427 - 110-point credential-gateway thread, July 23, 2026
