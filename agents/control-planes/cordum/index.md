---
title: Cordum
created: 2026-10-07
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, governance, safety-kernel, approvals, claude-code]
readability: 3
audience_notes: >
  Engineers who want a job-dispatch control plane that holds risky agent actions before workers run, and teams deciding whether a source-available license is acceptable.
  Assumes you know what a safety gate, a human approval step, and a source-available license are.
---

Cordum (cordum-io/cordum) is a BUSL-1.1 source-available agent control plane from Cordum Inc. whose safety kernel evaluates every job and returns ALLOW, DENY, or REQUIRE_APPROVAL before a worker runs, with a Claude Code hook path (Cordum Edge) that applies the same model to local tool calls.

**Its pitch is policy before action: the scheduler and safety kernel sit in the dispatch path, so a destructive job is held for an approval bound to its exact action hash instead of logged after the fact.**

## What it is

A Docker Compose or Helm deployment of six services (API gateway, scheduler, safety kernel, workflow engine, context engine, React dashboard) connected over NATS and Redis, with workers joining through CAP (Cordum Agent Protocol) SDKs for Go, Python, and Node.
Declarative YAML policies map risk to verdicts, a policy simulator replays rules against historical jobs, and a built-in MCP server adds tenant-scoped tool discovery with an opt-in policy gate before tool calls.
Cordum Edge is the developer entry point: `cordumctl edge claude` installs a command hook and a local agent daemon so Claude Code shell and file actions are allowed, denied, or held for approval, and a destructive retry must match a resolved approval audit event for the same tenant, approval reference, and action hash.
The site now headlines the same model as the Action Firewall, and the vendor sibling CordClaw extends it to OpenClaw: an Apache-2.0 plugin and localhost daemon that hook the OpenClaw gateway at four points (agent start, prompt build, tool call, message write) and return one of five typed decisions (ALLOW, DENY, THROTTLE, REQUIRE_HUMAN, CONSTRAIN), with connected-mode routing through Cordum policy still marked in progress and result gating roadmap.
Enterprise features (SSO, SCIM, advanced RBAC, SIEM export, legal hold) ship in the core and unlock by license entitlement.

## Status

Active and young: 509 stars and 34 forks as of 2026-10-10, with 25 open issues and the latest push on 2026-10-27 as of 2026-10-28, created 2026-01-11, latest tagged release v1.2.0 (2026-10-17), with the CAP SDKs versioned separately at 2.17.0 (2026-07-22).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=cordum-io/cordum&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=cordum-io/cordum&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=cordum-io/cordum&type=date&legend=top-left" />
</picture>

**The community footprint is close to absent: the founder's Show HN for Cordum Edge drew 1 point and zero comments, so the adoption evidence is the star count and the release work rather than organic discussion.**
The vendor site is candid in one direction ("no anonymous-customer totals, invented benchmarks, or maturity shortcuts") while the README leans on unsourced Gartner statistics, so read the docs and the repository rather than either marketing surface.

## Strengths

- The three-verdict model is enforced at dispatch, before the worker starts, which is the correct place to stop damage and the same design point SIDJUA argued for while it was alive.
- Approval provenance is the strongest detail in the category: Edge does not trust an approval store alone, it requires the resolved approval audit event matching tenant, reference, and action hash.
- The deployment story is production plumbing from day one: cosign-signed multi-arch images, a Helm chart on Artifact Hub, TLS generation, and a smoke test that exercises an actual approval workflow.
- Edge gives Claude Code users the same gate locally today, which most planes here cannot offer without their platform.

## Cautions

- BUSL-1.1 is source-available, not open source: internal use is free, offering it as a competing hosted service is not, and the code converts to Apache-2.0 only at the 2029 change date.
- The quickstart ships default credentials (admin with a published dev password) and a compose path with user auth off, safe for a demo and wrong for exposure; the README says to change them, so read it before you expose anything.
- The public surface is essentially one founder's voice, the HN thread drew nobody, and 509 stars nine months in is modest, so treat adoption as unproven.
- The tagged release train went four months quiet (v1.1.0 in June) before v1.2.0 landed on 2026-10-17 with scheduler lock-fence and audit-exporter fixes, and the README's comparison table against Guardrails AI and NeMo Guardrails is the vendor's own drawing, not a benchmark.

## Pricing

Community is free and self-hosted with the full control plane, capped at 3 workers, 3 concurrent jobs, 500 requests per second, single-approver gates, and 7-day audit retention.
Team adds capacity (25 workers, 2,000 requests per second, multi-approver gates, 90-day retention, SSO) by contacting sales, with no dollar price published.
Enterprise is custom (unlimited workers, 10,000 requests per second, RBAC, audit export, legal hold, support SLA).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-07 | Community | Recorded at $0, self-hosted with capacity caps | https://cordum.io/pricing |

## Compared to

- [Agent Control](../agent-control/index.md): both gate before execution, but Agent Control decorates functions inside your code while Cordum governs jobs at a scheduler boundary and ships its own worker runtime; choose Agent Control for in-code hooks across frameworks, Cordum for fleet dispatch with approvals.
- [Veto](../veto/index.md): a local-first authorization kernel wrapping tool calls with receipts; choose Veto for a minimal in-process gate, Cordum when jobs need scheduling, workflows, and multi-approver gates.
- [Paperclip](../paperclip/index.md): the company control plane with budgets and org charts; Paperclip manages the work, Cordum gates the actions.

## Bottom line

**Recommended for teams standardizing approval-gated agent jobs across a fleet who accept a source-available license and want the Claude Code Edge path today.**
Not for OSI-only shops, and not for anyone who needs an adopted project with independent validation, because the community footprint is not there yet.

## Changes

- 2026-10-07 - Created from the awesome-ai-governance entrant scan, profiling the source-available dispatch-time control plane and its Claude Code Edge firewall.
- 2026-10-17 - Full rotation re-verification: every cited URL re-fetched and live, pricing unchanged, the CAP repo re-checked (Apache-2.0, pushed 2026-10-12, SDKs still 2.17.0), the vendor's new CordClaw OpenClaw adapter recorded per the sibling fold, and the site's Action-Firewall framing noted.
- 2026-10-21 - Release train moved to v1.2.0 (2026-10-17), scheduler lock-fence and audit-exporter fixes, ending the four-month v1.1.0 hold; the train-lags caution rewritten.
- 2026-10-28 - Full rotation re-verification: every cited URL re-fetched and live except the three cordum.io pages, which refused fetchers this run (403 to plain and browser user agents), so the vendor-site, pricing, and CordClaw state stands as last read 2026-10-17; v1.2.0 and the CAP SDKs (2.17.0 on both PyPI and npm) unchanged.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Agent Control](../agent-control/index.md) - the Apache-2.0 in-code decorator alternative
- [CrowdStrike Falcon Guardian](../crowdstrike-falcon-guardian/index.md) - the endpoint-anchored commercial counterpart
- [Model Context Protocol (MCP)](../../protocols/mcp/index.md) - the protocol whose server calls this gateway governs
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call

## References

- https://github.com/cordum-io/cordum - README: quickstart, services, Edge path, feature table, CAP section, license terms
- https://api.github.com/repos/cordum-io/cordum - stars, forks, issues, creation and push dates as of 2026-10-10
- https://cordum.io - product framing, the Edge-to-Platform adoption path, availability statements
- https://cordum.io/pricing - Community, Team, and Enterprise tiers with capacity caps
- https://cordum.io/cordclaw - the CordClaw OpenClaw adapter: hook points, five decision types, threat model, connected-mode status
- https://github.com/cordum-io/cap - the CAP protocol repository (Apache-2.0)
- https://api.github.com/repos/cordum-io/cordum/releases - v1.2.0, 2026-10-17, the latest tagged release
- https://pypi.org/pypi/cap-sdk-python/json - cap-sdk-python 2.17.0, uploaded 2026-07-22
- https://registry.npmjs.org/cap-sdk-node - cap-sdk-node 2.17.0, published 2026-07-22
- https://news.ycombinator.com/item?id=49880505 - the 1-point, zero-comment Show HN, the thin-footprint signal
- https://dev.to/yaron_torgeman_104570d968/-mcp-vs-cap-why-your-ai-agents-need-both-protocols-3g4l - the founder's MCP-versus-CAP deep dive grounding the protocol layering
