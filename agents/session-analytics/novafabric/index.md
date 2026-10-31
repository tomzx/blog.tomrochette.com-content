---
title: NovaFabric
created: 2026-10-28
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, run-recording, replay, provenance, open-source]
readability: 3
audience_notes: >
  Engineers who need to prove, replay, and compare what an agent run did, weeks later, including to auditors without the tool installed.
  Assumes you know what an API call trace, a CI gate, and a detached signature are.
---

NovaFabric is an Apache-2.0 Python CLI that records any command's AI-agent run as a portable, secret-scanned Run Capsule you can replay in five modes, structurally diff against another run, trace for lineage, and export as a signed evidence bundle an auditor can verify without NovaFabric installed.

**Where the rest of this category indexes what coding agents already wrote to disk, NovaFabric wraps the run itself, so the evidence is a folder you own, sealed with your key, verifiable offline, and diffable run against run.**

## What it is

`nova capture <command>` injects a loader that hooks the OpenAI, Anthropic, and MCP SDKs plus the httpx, requests, aiohttp, and urllib3 clients, recording each call with OpenTelemetry GenAI fields; non-Python clients (the README names Claude Code, Cursor, and Node or Go agents) ride the api-proxy and mcp-proxy, and an SDK decorator covers in-process capture.
Capsules are written on success and on failure, carry a hash-chained redaction proof from an 18-rule secret scan (the README is explicit that this is secret-scanned, not guaranteed secret-free), and stay plain directories on your filesystem.
Replay has five named modes: forensic (read-only), mocked (recorded replies served back for CI re-execution), semantic, exact, and experimental intervention; the README does not claim exact replay of remote LLM calls.
`nova diff` aligns two runs call by call and fails a build on behavioral change with `--assert-no-regressions`; lineage queries export OpenLineage and W3C PROV; sealing is opt-in DSSE with a Merkle log and RFC 3161 timestamping; the exported Evidence Bundle verifies with sha256sum and an Ed25519 verifier and no NovaFabric runtime.
Extras add a local dashboard, aggregation queries, an experimental multi-user server with OIDC and RBAC, compliance exports, and Sigstore; the toolkit runs from a laptop to Docker, Kubernetes, and SLURM, online or air-gapped.
Made by Mohsen Seyedkazemi Ardebili, an independent consultant, under Apache-2.0, with an arXiv paper (2609.12582) on tamper-evident, replayable evidence for agent runs.

## Status

Beta and shipping at a clip its adoption has not caught up with: 7 stars, 1 fork, 1 open issue, created 2026-06-25, pushed 2026-10-29 (dependency bumps and a DuckDB 2.0 compatibility fix, unreleased), releases through v0.108.0 on 2026-10-25, as of 2026-10-31; PyPI serves 0.108.0 with 734 downloads in the trailing month to 2026-10-31.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=MSKazemi/novafabric&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=MSKazemi/novafabric&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=MSKazemi/novafabric&type=date&legend=top-left" />
</picture>

The status section labels server mode, the dashboard, and the cluster collector experimental, and the capsule and evidence-bundle formats stay unfrozen until the v1.0 schema freeze.
The project's own comparison table names where it loses (no hosted dashboard, no turnkey live analytics), and an arXiv paper grounds the tamper-evidence design.
I found no Hacker News story and no third-party review.
**A solo project whose documentation discipline outruns its adoption by three orders of magnitude, whose product is an evidence format that is not yet frozen.**

## Strengths

- Capture without code changes reaches non-Python agents through the proxies, which most SDK-only tracers cannot.
- A crash is captured evidence, not lost state: capsules are written on failure too.
- The diff gate turns replay infrastructure into a CI check on agent behavior change.
- Evidence Bundles verify with standard tools and no NovaFabric install, which is what makes them evidence.
- The standards stack is named and checkable (OTel GenAI, OpenLineage, in-toto DSSE, RFC 3161), with a conformance page listing how to check each claim.

## Cautions

- 7 stars, 1 fork, and no independent coverage: the verification story is the project's own conformance claims.
- Capsule and bundle formats are additive but not frozen until v1.0, so archived capsules may need migration.
- The secret scan matches known key formats only, so a capsule is scanned, not clean, by the README's own wording.
- Server mode, dashboard, and cluster collection are experimental; the single-player path is the usable one.
- One maintainer with a consultant's day job, at v0.108 in five months, is a pace that can stop as fast as it started.

## Pricing

Free and open source under Apache-2.0; no paid tier, no hosted service, and the core works fully offline.

## Compared to

- [Agent-Causality](../agent-causality/index.md): the causal sibling; Agent-Causality slices recorded runs for cause, NovaFabric preserves and diffs whole runs for proof.
- [claude-replay](../claude-replay/index.md): the other replay in this category; claude-replay renders a session for humans to watch, NovaFabric replays calls for machines to verify.
- [agentsview](../agentsview/index.md): the archive that reads the session files tools already wrote; NovaFabric needs to be in the run's path (loader or proxy) but captures what those files never hold.

## Bottom line

**Recommended for engineers who must reproduce or prove what a run did, weeks later and offline, and for gating agent behavior change in CI.**
Not for live cost dashboards, transcript search, or anyone who needs a frozen evidence format today.

## Changes

- 2026-10-28 - Created from the coordinator's entrant handoff, admitted on the Run Capsule mechanism, the five replay modes with the diff CI gate, and eight fetched sources.
- 2026-10-31 - Volatile re-verification: no release after v0.108.0 with dependency bumps and a DuckDB 2.0 compatibility fix landing unreleased 2026-10-29; open issues refreshed 6 to 1 and the trailing-month download figure re-verified unchanged at 734 (to 2026-10-31).

## See also

- [Agent-Causality](../agent-causality/index.md) - the causal-slicing companion admitted from the same source list
- [claude-replay](../claude-replay/index.md) - the human-facing replay artifact this tool's machine-verifiable capsules contrast with
- [agentsview](../agentsview/index.md) - the passive archive for sessions you did not wrap
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/MSKazemi/novafabric - 7 stars, 1 fork, Apache-2.0, created 2026-06-25, pushed 2026-10-29, as of 2026-10-31
- https://raw.githubusercontent.com/MSKazemi/novafabric/main/README.md - the capsule layout, capture paths, five replay modes, diff gate, sealing, comparison table, and status labels
- https://api.github.com/repos/MSKazemi/novafabric/releases - v0.108.0 (2026-10-25), v0.107.0 (2026-10-23), v0.106.1 (2026-10-23)
- https://pypi.org/pypi/novafabric/json - PyPI package, version 0.108.0, Python 3.12 or newer
- https://pypistats.org/api/packages/novafabric/recent - 734 downloads in the trailing month to 2026-10-31, unchanged since 2026-10-28, behind the adoption claim
- https://novafabric.ai/docs/ - the documentation hub this run verified live
- https://arxiv.org/abs/2609.12582 - the paper on tamper-evident, replayable evidence for agent runs
- https://hn.algolia.com/api/v1/search?query=novafabric&tags=story - zero stories, the empty independent footprint this note states
