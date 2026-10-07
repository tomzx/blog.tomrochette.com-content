---
title: OpenAPPA
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, information-flow-control, policy-enforcement, prompt-injection, rust]
readability: 3
audience_notes: >
  Engineers who need sensitive data to stay inside an authorized audience even when the agent is prompt-injected, and who can accept a preview-stage engine.
  Assumes you know what information-flow control and a reference monitor are.
---

OpenAPPA (archestra-ai/OpenAPPA) is an MIT-licensed Rust policy engine, built on the APPA information-flow algebra, that labels everything an agent reads with an audience and trust level and checks every tool call against declarative TOML policy before it runs.

**Its argument is that you cannot prompt-inject an algebra: instead of classifying intents or matching blocked patterns, the engine tracks where data came from and derives each decision from the trajectory's label, so the same event log always yields the same verdict.**

## What it is

Policy is one `appa.toml` describing data sources, audiences, trust levels, and authorities; every trajectory carries a security label (audience × trust) that only narrows as the agent reads.
The engine runs in-process or as a sidecar, decides from the event log alone with no network or file calls, and answers a block with a machine-readable remedy plan: sanitizers that redact a payload so it can flow to a wider audience, one-action authorities, or a disposable child branch that absorbs untrusted reads without poisoning the parent trajectory.
A Claude Code plugin (`appa plugin install claude-code`) is the fastest integration, and the sponsor's Archestra LLM proxy implements the same enforcement for any agent that talks to a model through it, including Claude Code, Claude Desktop, Cursor, Codex, OpenCode, Copilot CLI, and n8n.
`appa describe --check` and `appa replay` validate policy coverage in CI, so a team can block merges that leave tool paths uncovered.

## Status

Active and fast-growing for its age: 1,476 stars and 63 forks as of 2026-10-07 since creation on 2026-08-18, pushed 2026-10-06, latest release v0.31.1, positioned as a preview and an RFC where config and wire surfaces may break without shims.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=archestra-ai/OpenAPPA&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=archestra-ai/OpenAPPA&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=archestra-ai/OpenAPPA&type=date&legend=top-left" />
</picture>

**The formal claim has an actual paper behind it: APPA (arXiv 2607.24625, revised 2026-08-26) proves no-laundering and recovery-containment invariants and reports 6,600 benchmark episodes, and the work was accepted to the NeurIPS 2026 Workshop on Agents in the Wild.**
The community footprint is still thin (a 2-point, zero-comment HN thread on 2026-10-01), and every benchmark number is self-reported, though the suites (Bench-Corp, AgentThreatBench, Tau) are public and the baselines are named.

## Strengths

- Deterministic decisions computed from the event log alone are auditable in a way classifier-based auto-modes cannot be, since the same log always produces the same verdict.
- The remedy-plan design is the interesting part: blocks come with legal continuations (sanitizers, authorities, subagent isolation), which is how guarded runs complete 88 to 90 percent of tasks while recording zero successful attacks across 1,320 evaluations.
- Token overhead is measured rather than asserted: 4.22 percent over stock on Tau Bench.
- Policy coverage is checkable in CI, so completeness is provable before merge instead of asserted after an incident.

## Cautions

- Preview and RFC: config and wire surfaces may break without shims, so pin deliberately and read the changelog before upgrading.
- Development is sponsored by Archestra, whose proxy is the flagship integration; vendor neutrality is a design stance, and the benchmark baselines (Microsoft FIDES, Claude auto mode) are configured by the sponsor.
- The Claude Code plugin is described by the project itself as a playground, not the product, so production enforcement today means the Archestra proxy or an embedded runtime.
- Utility collapses without the recovery machinery: one Bench-Corp ablation falls from 88 percent completion to 35 percent without guided recovery, so evaluate with recovery enabled or expect stalls.

## Pricing

MIT licensed and free.
The sponsor's Archestra platform is a separate open-source project with its own commercial offering; no OpenAPPA-specific prices exist.

## Compared to

- [Veto](../veto/index.md): both are local-first gates, but Veto matches actions against YAML rules while OpenAPPA tracks data flows and labels; choose Veto for rules about specific actions, OpenAPPA when the threat is exfiltration of anything the agent read.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): the toolkit wraps calls with policy, identity, sandboxing, and audit across five languages; OpenAPPA is single-purpose and deeper on the data-flow axis.
- [CrowdStrike Falcon Guardian](../crowdstrike-falcon-guardian/index.md): the endpoint-commercial answer to the same exfiltration problem; OpenAPPA runs in your process instead of your sensor estate.

## Bottom line

**Recommended for teams whose dominant risk is sensitive data reaching unauthorized destinations, who can live with a preview engine and want deterministic, CI-checkable policy.**
Not for teams that need budgets, org models, or fleet approvals, because OpenAPPA deliberately governs data flows, not agent organizations, and not for anyone who requires a stable 1.0.

## Changes

- 2026-10-07 - Created from the entrant scan (an HN surfacing cross-checked against the awesome-ai-governance list), profiling the APPA information-flow engine.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the action-rule kernel this complements on the data-flow axis
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) - the broad multi-language policy alternative
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call

## References

- https://github.com/archestra-ai/OpenAPPA - README: the algebra, remedy plans, integrations, benchmarks summary, license
- https://api.github.com/repos/archestra-ai/OpenAPPA - stars, forks, creation and push dates as of 2026-10-07
- https://openappa.com/ - the flow-tracking argument, the label model, remedy plans
- https://openappa.com/evaluation - the 1,320-episode results, the FIDES and auto-mode comparisons, token overhead, ablations
- https://openappa.com/archestra - the sponsorship statement and the proxy-level integration
- https://arxiv.org/abs/2607.24625 - the APPA paper: invariants, recovery containment, 6,600 episodes, NeurIPS workshop acceptance
- https://api.github.com/repos/archestra-ai/OpenAPPA/releases - v0.31.1, the latest release
- https://news.ycombinator.com/item?id=49918330 - the 2-point, zero-comment thread, the thin community signal
