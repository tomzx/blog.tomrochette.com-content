---
title: Centaur
created: 2026-11-06
updated: 2026-11-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, slack, self-hosted, durable-execution]
readability: 3
audience_notes: >
  Teams that want one shared agent their whole company can tag in Slack, run by a platform owner who can operate Kubernetes, Postgres, and a secrets vault.
  Assumes you know what a Kubernetes pod, a NetworkPolicy, and a reverse proxy do.
---

Centaur is a self-hosted agent platform from Paradigm and Tempo where a Slack mention or API call starts an isolated Kubernetes sandbox session running the coding harness of your choice, with credentials injected by a per-sandbox proxy so the agent never holds the raw values.

**It is the team-scale version of this category's message-thread trigger: one Slack thread is one sandboxed agent session, and its credential boundary is architecture, placeholders in the sandbox and injection at the network edge, the same stack Airut runs on a single operator's VM.**

## What it is

You tag @centaur in a Slack thread (or POST to its session API), and the platform assigns the thread its own Kubernetes pod with a shell, git, Python, Node.js, and Bun, running a CLI harness of your choice.
The README names Amp, Claude Code, and Codex, and the docs add documented paths for Hermes, Pi, and OMP harnesses.
A Rust control plane (api-rs) owns session lifecycle, durable transcripts in Postgres, tools, workflows, and auth, and every outbound request from a sandbox routes through its own iron-proxy pod, which swaps placeholder strings for the actual credentials only on requests to the hosts and header or query positions each secret is bound to.
Teams have also contributed ingress integrations for Linear, GitHub, Discord, and Microsoft Teams beside Slack, and the README quickstart now carries the Teams app credentials as an optional local boot.
Teams extend it by dropping Python tool plugins, SKILL.md skills, and Python workflow files into the repo, or by layering an organization overlay on top of the kernel.
Workflows are durable, Absurd-inspired Python functions that checkpoint every step to Postgres, can sleep for hours, wait on external events, run child agents, and fire on cron.
It is built by Paradigm with Tempo, open-sourced on 2026-05-21 after running in production at both companies since January 2026, and licensed under Apache-2.0 or MIT at your option.

## Status

**Active and institutionally backed, on a fast release line.**
1,422 stars as of 2026-11-06, 289 forks and 120 open issues and pull requests as of 2026-11-11 (GitHub API), created 2026-05-18 and pushed 2026-11-11.
The 2.0 rewrite landed on 2026-08-10: a smaller Rust control plane exposing four operations, permissions derived from the conversation's context (a direct message uses your connected accounts, a shared channel gets the team's grants), MCP support so local agents can call Centaur's tools, and Slack, Granola, Google Drive, Google Calendar, Linear, and Attio as indexed context sources.
The release train is dense (several Helm-chart cuts per day into the second week of November) and stayed on the centaur-0.1.x line: the calendar-versioning cut recorded on 2026-11-06 (v2026.11.6) did not stick, and centaur-0.1.213 published 2026-11-11 tops the train, Paradigm is hiring engineers to work on it full time, and both backers run it in production.
The independent footprint is two self-posted, zero-comment Show HN threads (1 and 2 points) as of 2026-11-07, no launch discussion, no third-party deployment write-ups, and the vendor figures (more than 80% of sessions in shared channels, over 99% of daily sessions completing) are Paradigm's own.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=paradigmxyz/centaur&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=paradigmxyz/centaur&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=paradigmxyz/centaur&type=date&legend=top-left" />
</picture>

## Strengths

- **The trigger is the team's existing collaboration surface, and the session is durable**: a thread keeps its sandbox, transcript, and results across restarts and deploys, and teammates see what the agent did without asking its owner.
- The credential boundary is architecture, not configuration: sandboxes hold placeholders bound to specific hosts and header positions, the per-sandbox proxy injects values in flight, a default-deny NetworkPolicy isolates pods, and the proxy logs every outbound request, so the audit trail is built in.
- Bring your own harness: one harness interface covers Amp, Claude Code, Codex, and others, so a team is not locked to one vendor's CLI.
- Tools and skills are organization-wide by default: add a Python tool or a SKILL.md once and every conversation inherits it, and MCP exposes the same tools to agents outside Centaur.

## Cautions

- **Self-hosting is heavy**: Kubernetes (a k3s host is the documented minimum), Helm, Postgres, a Slack app, and a 1Password vault for secrets add up to an operations burden a platform owner carries, not a laptop user.
- The default egress allowlist is open (the wildcard domain), a deliberate onboarding choice the docs call out themselves, so the credential boundary only buys full containment after an operator writes the allowlist.
- Every headline number is the vendor's own, and no independent coverage or deployment report exists as of 2026-11-07.
- The platform moves fast and has rewritten its core mid-life (the FastAPI 1.0 to Rust 2.0 migration has its own guide), and the README quickstart still carries a developer's local checkout path, a rough edge worth reading as churn.
- Provenance is crypto-native: Paradigm is a crypto venture firm and Tempo is its blockchain, so the roadmap follows those backers' workflows even though nothing in the project is token-tied.

## Pricing

Free, self-hosted, under Apache-2.0 or MIT.
There is no hosted tier; your costs are the Kubernetes cluster and Postgres you run, model inference for whichever harness you connect, and the secrets store (1Password in the reference setup).

## Compared to

- [Airut](../airut/index.md): the same message-thread-to-sandbox pattern with the same placeholder-credential proxy; Airut is a single operator's email-and-Slack gateway on one VM running Claude Code only, Centaur is team-shared, Slack-first, harness-agnostic, and Kubernetes-native.
- [Rivet Agents](../rivet-agents/index.md): both keep work alive across restarts; Rivet runs one durable process per agent key inside your backend code, Centaur runs one isolated sandbox per Slack thread under a platform you operate.
- [n8n](../n8n/index.md): the general webhook-and-SaaS automation canvas; Centaur is a purpose-built agent runtime where the collaboration thread is the trigger and harnesses, skills, and tools replace nodes.

## Bottom line

**Recommended for teams that want one shared agent in Slack, can operate Kubernetes and Postgres, and will write the egress allowlist on day one.**
Not for solo use (Airut is far lighter), not for anyone needing a hosted product, and not for teams unwilling to adopt a platform that has already rewritten its core once.
My disagreeable claim: Centaur and Airut are this category's two architecture-first guardrails, and Centaur's version adds per-principal grants and a default-deny network policy between sandboxes, which makes the pair worth studying before buying anything else here.

## Changes

- 2026-11-06 - Created from the 2026-11-05 cross-category handoff routed to executions on the Airut Slack-to-sandbox precedent.
- 2026-11-07 - Verified out of rotation with every cited URL re-fetched: the repo counters refreshed (284 forks, 120 open issues and pull requests, default-branch head confirming the 2026-11-06 push), the release train moved to calendar versioning with v2026.11.6 (2026-11-06) above centaur-0.1.205, and the contributed Teams, GitHub, Discord, and Linear ingress integrations recorded from the 2.0 announcement and the README's optional Teams boot; the README architecture claims, the dual license, both Paradigm posts, the security page, and the two zero-comment Show HN threads all re-confirmed.
- 2026-11-11 - Corrected the release-train record: the calendar-versioning switch did not stick, and the train returned to the centaur-0.1.x line (0.1.213 published 2026-11-11 atop several cuts per day); the counters refreshed (284 to 289 forks, pushed 2026-11-11, 120 open issues and pull requests unchanged).

## See also

- [Airut](../airut/index.md) - the single-operator sibling with the same architectural sandbox and credential proxy
- [Rivet Agents](../rivet-agents/index.md) - the other durable-execution member, process-per-agent instead of sandbox-per-thread
- [n8n](../n8n/index.md) - the webhook-first canvas alternative for external triggers
- [Claude Code](../../harnesses/claude-code/index.md) - the most-named harness behind Centaur's sandbox interface
- [Sandboxing](../../sandboxing/_index.md) - the category holding the boundary tools Centaur builds in

## References

- https://api.github.com/repos/paradigmxyz/centaur - counters (1,422 stars as of 2026-11-06, 289 forks, 120 open issues and pull requests, created 2026-05-18, pushed 2026-11-11), Rust, as of 2026-11-11
- https://raw.githubusercontent.com/paradigmxyz/centaur/main/README.md - the Slack-to-sandbox model, sandbox stack, harness list, tools and workflows, the optional Teams ingress, and the security summary (fetched 2026-11-06, re-fetched 2026-11-07)
- https://raw.githubusercontent.com/paradigmxyz/centaur/main/LICENSE - the dual Apache-2.0/MIT license text (fetched 2026-11-06, re-fetched 2026-11-07)
- https://centaur.run - the positioning, the Paradigm and Tempo backing, and the architecture pitch (fetched 2026-11-06, re-fetched 2026-11-07)
- https://centaur.run/security - the threat model, default-deny NetworkPolicy, iron-proxy placeholder credentials, and the docs' own caveats on the open egress default and shared secret store (critical source, fetched 2026-11-06, re-fetched 2026-11-07)
- https://www.paradigm.xyz/writing/open-sourcing-centaur-multiplayer-self-hosted-secure-agents - the 2026-05-21 open-sourcing announcement: architecture, Absurd-inspired durable workflows, production use at Paradigm and Tempo since January 2026 (fetched 2026-11-06, re-fetched 2026-11-07)
- https://www.paradigm.xyz/writing/centaur-2-0-permissions-context-and-mcp - the 2026-08-10 2.0 announcement: the Rust api-rs rewrite, context-derived permissions, MCP, the contributed Linear, GitHub, Discord, and Teams integrations, and the vendor session figures (fetched 2026-11-06, re-fetched 2026-11-07)
- https://api.github.com/repos/paradigmxyz/centaur/releases?per_page=5 - the release train: centaur-0.1.x cuts through 0.1.205 (2026-11-05), the one-off calendar cut v2026.11.6 (2026-11-06), then back to centaur-0.1.x with 0.1.213 (2026-11-11) newest (fetched 2026-11-06, re-fetched 2026-11-11)
- https://hn.algolia.com/api/v1/search?query=paradigm%20centaur&tags=story - the coverage search finding one self-posted 1-point link to Paradigm's own 2.0 post and no dedicated thread (fetched 2026-11-06, re-fetched 2026-11-07)
- https://hn.algolia.com/api/v1/search?query=centaur.run&tags=story - the second coverage query finding the self-posted 2-point site thread, completing the footprint record (fetched 2026-11-06, re-fetched 2026-11-07)
