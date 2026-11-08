---
title: Agent Barn
created: 2026-11-05
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, agent-operations, multi-tenant, kubernetes, self-hosted, open-source]
readability: 3
audience_notes: >
  Platform engineers who want AI agents as chat coworkers (Slack, Teams, Telegram, Discord) running inside their own Kubernetes cluster, with per-agent cost attribution and access roles, and who accept a 0.21.x product.
  Assumes you know what a Helm release and a virtual LLM API key are.
---

Agent Barn (aai-labs/agent-barn) is an Apache-2.0 open-source control plane from AAI Labs that runs AI agents as chat coworkers in Slack, Microsoft Teams, Telegram, and Discord, as one pod per agent on your own Kubernetes cluster, with per-agent token and spend attribution, organisation and per-agent access roles, and conversation, tool-call, and event audit trails.

**Its argument is that oversight should be a property of the deployment: credentials, model routing, history, and cost metering all live inside your namespace (per-agent LiteLLM virtual keys, your PostgreSQL, your cluster), so what each agent did and cost is attributable without sending anything to a second workspace.**

## What it is

A FastAPI control plane with a Next.js UI, deployed locally with one script (Docker Compose plus a k3d cluster) or to Kubernetes with Helm and Helmfile over PostgreSQL and Redis, with the product API, ingest API, communications gateway, memory gateway, and credential gateway as separate HTTP boundaries.
Every agent is a template (Markdown bundles: soul, identity, tools, boot, heartbeat) plus a model, communication connections, and credentialed skills; seeds include a PR reviewer, a documentation agent, an email reminder, a Jira task helper, and a scrum master, and a skill only attaches once its provider credential is present.
A LiteLLM proxy in your namespace mints one virtual key per agent, so token use and spend attribute to individual agents and organisations rather than one opaque monthly number, and each organisation sets a model default and allowlist.
Identity is multi-tenant from the start: fixed permission-backed organisation roles plus separate per-agent access roles and assignments, isolated at the data layer, with per-agent channel allowlists and DM policy beside them.
Audit is three trails pushed from the runtime: conversation history, a tool-call log, and a domain-event trail with a transactional outbox and a security-audit projection.
Two agent runtimes ship behind one protocol: OpenClaw as the default, where command approval is always automatic, and Hermes, which supports a per-agent command-approval mode.
Installs report pseudonymous business events to the vendor's PostHog project (EU) by default, with `ANALYTICS_ENABLED=false` as the documented opt-out; agent names, prompts, and content are excluded by design.
Built by AAI Labs, a company in Vilnius, Lithuania.

## Status

Active and young: 111 stars, 7 forks, and 19 open issues as of 2026-11-05 (17 open issues as of 2026-11-08), created 2026-05-05, with the repository push date of 2026-11-07 coming from a side branch and the default branch's latest commit on 2026-10-29, and a steady release train (v0.20.0 on 2026-10-21, v0.20.1 on 2026-10-26, v0.21.0 on 2026-10-29).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aai-labs/agent-barn&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aai-labs/agent-barn&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aai-labs/agent-barn&type=date&legend=top-left" />
</picture>

**The community footprint is close to absent in discussion (a Hacker News search returns no thread about this project) but present in coverage: the OECD.AI policy catalogue carries a descriptive entry, the docs site is fully written rather than a shell, and the vendor's LinkedIn launch post dates the public release to September 2026.**
The traction call this note rests on: six months to 111 stars is thin next to the planes above it in this category, but the combination of a weekly release train, production deployment guides that name their own gaps (no high availability, no autoscaling, no default database recovery), and independent third-party description clears the zero-coverage tail below this category's bar.

## Strengths

- Per-agent virtual keys on a LiteLLM proxy you operate make cost attribution a structural fact rather than a dashboard estimate, and each organisation's model allowlist is enforced at the same layer.
- The production guides are candid in the right direction: an operator-responsibility matrix states plainly that high availability, autoscaling, network isolation, and database recovery are not provided by the default charts and are your job.
- Skills are credential-gated, so an agent cannot reach a tool whose credential was never attached, and templates are versioned content that organisations fork rather than code to patch.
- Two upstream runtimes (OpenClaw and Hermes) behind one protocol mean the plane manages the fleet without marrying one agent implementation.

## Cautions

- It is 0.21.x: expect wire and schema churn, and pin deliberately.
- The default runtime's command approval is always automatic, so the per-agent approval mode that actually gates shell commands exists only on the Hermes runtime today; an OpenClaw fleet on this plane runs with auto-approved commands.
- Telemetry to the vendor's PostHog project is on by default (pseudonymous, EU-hosted, documented opt-out), which is a default worth knowing before any sensitive deployment.
- Zero Hacker News footprint and no independent security review; the multi-tenancy and audit claims are the vendor's own plus a descriptive catalogue entry.
- The default namespace is still `agent-farm` from before the rebrand, a small but confusing wart for anyone reading cluster state against the product name.

## Pricing

Free and open source under Apache-2.0, self-hosted on your Kubernetes infrastructure; your model spend (through OpenRouter via your own LiteLLM proxy) and your cluster are the costs.
AAI Labs operates its own hosted deployments, but no hosted price is published, so there is nothing to track.

## Compared to

- [Mission Control](../mission-control/index.md): both are self-hosted planes over runtimes, but Mission Control dispatchs tasks and gates completion on a review record, while Agent Barn hosts chat coworkers with per-agent cost metering and access roles; choose Mission Control for task workflows, Agent Barn for agents that live in Slack and Teams.
- [Paperclip](../paperclip/index.md): the company abstraction with org charts, budgets that pause agents, and a cloud path; Agent Barn is the lighter chat-coworker fleet with cost attribution but no org-chart model.
- [AgentField](../agentfield/index.md): turns agent functions into governed backend services with DID identity and receipts; Agent Barn turns chat-configured agents into Kubernetes pods with per-agent keys and access roles, no code SDK required.

## Bottom line

**Recommended for platform teams that want AI agents as chat coworkers inside their own cluster with per-agent cost attribution, credential-gated skills, and audit trails, and who accept a young 0.21.x product with defaults they must review.**
Not for teams that need per-command approval on the default runtime today, a stable 1.0, or a large community to escalate to.

## Changes

- 2026-11-05 - Created from the coordinator's cross-category handoff: admitted at 111 stars on the control-plane kind (per-agent costs, access roles, and audit trails governing an agent fleet on your own cluster), with the borderline-traction call recorded in Status and the zero-thread footprint stated as the missing signal.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Mission Control](../mission-control/index.md) - the closest self-hosted plane, task-dispatch flavored
- [Paperclip](../paperclip/index.md) - the company-scale control plane this sits below in scope
- [AgentField](../agentfield/index.md) - the agent-backend plane for code-first fleets

## References

- https://github.com/aai-labs/agent-barn - README: architecture, quickstart, runtimes, capabilities table, analytics disclosure, license
- https://api.github.com/repos/aai-labs/agent-barn - stars, forks, issues, creation and push dates as of 2026-11-05
- https://api.github.com/repos/aai-labs/agent-barn/releases - the v0.20.x to v0.21.0 release train
- https://agentbarn.dev - product site: the one-control-plane framing, runtime choice, and self-hosting promise
- https://agentbarn.dev/guides/self-hosting/deploy-kubernetes - the production deployment guide: services deployed, cluster prerequisites, and what Helmfile brings up
- https://oecd.ai/en/catalogue/tools/agent-barn - the OECD.AI catalogue entry, the independent third-party description this note cites
- https://hn.algolia.com/api/v1/search?query=agent%20barn&tags=story - the zero-relevant-thread community-footprint check as of 2026-11-05
