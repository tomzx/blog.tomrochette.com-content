---
title: SettleBridge
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, agent-settlement, trust, escrow, policy-enforcement, audit]
readability: 3
audience_notes: >
  Engineers building agent-to-agent commerce who need to know whether value should move, and who must confirm licensing before adopting an open-core product.
  Assumes you know the A2A protocol exists and that settlement, authorization, and payments are three different layers.
---

SettleBridge (a2a-settlement/settlebridge-ai) is a trust and policy gateway that sits between an agent and the A2A Settlement Exchange, enforcing reputation thresholds, spending caps, and provenance requirements before any agent-to-agent settlement proceeds.

**Its thesis is that an agent economy needs a settlement layer above payments and authorization, so SettleBridge gates whether an economic obligation may be committed and records a Merkle-linked audit trail of the decision.**

## What it is

The gateway is a Python and FastAPI service with a React dashboard, a hot-reloading policy engine, a Redis-backed reputation cache, health monitoring of the upstream exchange and mediator, threshold-based alert rules, and a structured audit log.
It deploys via Docker Compose, a Helm chart, or an AWS CloudFormation script, and the product page advertises 16 management API endpoints.
An optional bounty marketplace (`MARKETPLACE_ENABLED=true`) adds escrow-backed contracts, a claim and submission flow, and an AI-assisted bounty drafting assistant.
It is built on the open A2A-SE (A2A Settlement Extension) standard, which the same organization publishes under MIT, and the gateway sits on top of the upstream exchange, mediator, and auth projects rather than replacing them.
The vendor is Truthsetter LLC.

## Status

Early and low-traffic but actively maintained.
The gateway repository was created 2026-03-08 and sits at 1 star, 0 forks, and 1 open issue as of 2026-10-06, with 76 commits and a last push on 2026-09-25; the A2A-SE standard repository has 2 stars.

<a href="https://www.star-history.com/?repos=a2a-settlement%2Fsettlebridge-ai&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=a2a-settlement/settlebridge-ai&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=a2a-settlement/settlebridge-ai&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=a2a-settlement/settlebridge-ai&type=date&legend=top-left" />
 </picture>
</a>

The website, pricing page, marketplace, and documentation are live and detailed, so this is a product with a real surface rather than an abandoned experiment.
**The community footprint is effectively absent: a Hacker News search for SettleBridge returns nothing, and the whole organization is in the low single digits of stars.**
One comparison worth naming: this is a young, standards-first effort where the software is secondary to the spec, so its survival depends more on A2A-SE adoption than on the gateway's own traction.

## Strengths

- The only tool I found in this category whose subject is settlement (escrow, release, refund, dispute, finality) rather than tool-call authorization, which is a genuinely distinct and underserved layer.
- Cryptographic audit design: Merkle tree integrity, append-only entries, and CSV or JSON export aimed at SEC 17a-4, SOX, and NIST examination.
- Open-core with three real deployment paths and a published benchmark of time-to-first-interaction, so the quickstart is credible.
- Standards-anchored: the A2A-SE specification is archived on Zenodo and positions itself against AP2 and x402 explicitly.

## Cautions

- License metadata is inconsistent and I could not resolve it: the website and pricing page call Community Apache-2.0, the GitHub README badge says MIT, the GitHub API reports no detected license, and the `LICENSE` path on `main` returns 404. Confirm the actual terms before shipping.
- The public repositories are essentially unadopted (1 star), so no independent security review or third-party usage evidence exists yet.
- The exchange charges a 0.25% treasury fee per settled transaction on top of any enterprise gateway cost, which is a real cost-of-goods line item for high volume.
- The claimed compliance mappings (SEC 17a-4, SOX) are vendor assertions, not audited certifications.

## Pricing

Community is free forever with the full gateway, policy engine, audit logging, and rate-limited exchange access.
Enterprise is $2,500 per month per gateway with 24/7 support, SLAs, security patches within 24 hours, and custom policies.
The Exchange charges 0.25% of each settled transaction as an ATE treasury fee.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Community | Introduced at $0, full gateway, rate-limited exchange access | https://settlebridge.ai/pricing |
| 2026-09-27 | Enterprise | Introduced at $2,500/month per gateway | https://settlebridge.ai/pricing |
| 2026-09-27 | Exchange | Introduced at 0.25% ATE treasury fee per settled transaction | https://settlebridge.ai/pricing |

## Compared to

- [Veto](../veto/index.md): pre-execution authorization for a single agent's tool call; choose Veto to stop a refund or export, and SettleBridge when two independent agents must commit and settle value.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): in-process policy, identity, and audit across frameworks; choose AGT for governance of your own agents, and SettleBridge for trust across organizational boundaries.
- [SIDJUA](../sidjua/index.md): a self-hosted company of governed agents with budgets; choose SIDJUA for internal agent operations, and SettleBridge for commerce between agents you do not control.

## Bottom line

**Recommended for teams building agent-to-agent commerce that need escrow, reputation, and a cryptographic audit trail above the A2A protocol. Not for single-agent work or internal tool governance, and not until the license terms are confirmed from the repository itself.**

## Changes

- 2026-09-27 - Created.
- 2026-10-02 - Added the missing llm=glm-5.3-flash tag from this maintenance run; license metadata re-checked and still unresolved (GitHub reports none, the LICENSE path still returns 404).
- 2026-10-07 - Added the a2a-settlement/settlebridge-ai star history chart to the Status section.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category compared on shared rows
- [Veto](../veto/index.md) - the tool-call authorization layer this complements
- [SIDJUA](../sidjua/index.md) - the self-hosted governed-agent alternative
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) - the in-process governance alternative
- [Developer Trust Profiles](../../../developer-trust-profiles/index.md) - the corpus treatment of reputation as a control surface

## References

- https://settlebridge.ai/ - product framing, gateway components, open-core claim
- https://settlebridge.ai/pricing - Community, Enterprise, and Exchange pricing with dollar and percentage amounts
- https://github.com/a2a-settlement/settlebridge-ai - README: architecture, configuration, bounty marketplace, license statement
- https://api.github.com/repos/a2a-settlement/settlebridge-ai - stars, forks, issues, push dates, and the null license field as of 2026-10-06
- https://docs.a2a-settlement.org/docs/agent-settlement/ - A2A-SE: settlement lifecycle, three-layer model, interoperability
- https://api.github.com/repos/a2a-settlement/a2a-settlement - the MIT-licensed standard repository behind the gateway
- https://raw.githubusercontent.com/Agent-Analytics/awesome-multi-agent-orchestrators/main/README.md - the curated directory that flags the license metadata as inconsistent
