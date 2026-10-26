---
title: PIC Standard
created: 2026-10-11
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, agent-security, verification, provenance, open-standard]
readability: 3
audience_notes: >
  Engineers wiring agents to tools that can spend money, export data, or destroy state, who want a
  verification contract at the tool-call boundary, profiled against MCP and the control-plane layer above it.
  Assumes you know what a tool call and a signature keyring are.
---

PIC Standard is an Apache-2.0 protocol for pre-execution action gating: before a high-impact tool call runs, the agent must emit a signed Action Proposal declaring intent, impact, provenance, and evidence, which a local verifier checks fail-closed against a keyring of trusted signers.

**Its bet is that the dangerous moment is the instant before execution, and that guarding it takes a verification contract the agent cannot self-certify, not better system prompts or a policy engine above the harness.**

## What it is

A protocol plus a Python reference implementation (`pip install pic-standard`, `pic-cli verify`), with a TypeScript verifier (`pic-standard-ts`) that passes the same conformance corpus for canonicalization, core, and trust sanitization as of v0.9.1 (2026-10-14).
The contract: a proposal carries intent, an impact class (money, privacy, irreversible, compute), provenance entries with trust levels, claims backed by evidence, and the bound tool call; for high-impact actions at least one claim must cite evidence from trusted provenance or the verifier returns block.
v0.9.1 completed tool binding at the enforcement boundary: the MCP guard and HTTP bridge now bind the sanitized live tool arguments to the verified `action.args` under canonical digest equality, fail-closed, so a call whose arguments diverge from what was verified blocks instead of running.
The evidence model distinguishes hash evidence (integrity only, never a trust upgrade) from signature evidence (authority-bearing through the configured keyring), a rule tightened in v0.8.3 after issue 133.
Specification discipline is unusually formal for the footprint: RFC-0001 as a defensive publication with a SHA-256 anchored artifact, a frozen Canonical JSON v1 spec, PIC-Core and PIC-Evidence drafts in BCP 14 normative language, 91 conformance vectors with an eight-token diagnostic taxonomy, differential CI comparing the Python and TypeScript envelopes, an OpenAPI bridge contract, and signed releases.
The author positions it against identity and delegation work explicitly: PIC decides whether a call is justified to execute now, not who the agent is.

## Status

**Pre-1.0, actively hardened, with the thinnest adoption footprint of any protocol in this category.**
69 stars (2026-10-13), 47 forks, and 19 open issues and pull requests, created 2026-01-08, pushed 2026-10-21, as of 2026-10-22 (GitHub API).
PyPI shows v0.9.1 (uploaded 2026-10-14); pypistats still serves 697 downloads in the month ending 2026-10-10, its newest window as of 2026-10-16.
The public thread count is one: a Show HN at 1 point (2026-01-13).
Depth signals offset the reach signals: an independent public-material-only stress test of v0.8.3 by HERMETICUM B.C.E. S.r.l. is recorded with its findings adapted into attributed conformance vectors, external contributors landed conformance vectors and Windows CI, and the project publicly calls for co-maintainers.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=pic-standard/pic-standard&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=pic-standard/pic-standard&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=pic-standard/pic-standard&type=date&legend=top-left" />
</picture>

## Strengths

- **The hash-versus-signature evidence rule is the note's best idea**: integrity never upgrades trust, only a keyring signature does, which kills the most likely shortcut in any provenance scheme.
- Fail-closed by construction, with conformance vectors for the falsifiers (hash-only trust upgrades, duplicate IDs, lone surrogates, overpadded signatures) rather than prose assurances.
- The v0.9.0 cross-implementation milestone is the discipline this category's other young specs lack: a second verifier passing the same corpus, with differential CI holding them together.
- Integration guides exist for the stacks agents actually run in: LangGraph, an MCP guard, OpenClaw, and Cordum.

## Cautions

- **Adoption has not started**: 69 stars, a 1-point Show HN, and under a thousand monthly PyPI installs mean no independent deployment record speaks for the protocol.
- v0.9.0 was a breaking release for conformant producers (the semi_trusted trust value now fails validation), and the strict_trust default flipped to secure in the same cycle, so early embedders absorb churn.
v0.9.1 continued the pattern at the boundary: a proposal-backed call whose live arguments diverge from the verified action.args now blocks (PIC_ARG_BINDING_MISMATCH) where it previously ran.
- One contributor accounts for 141 of roughly 177 commits, the evidence-mode TypeScript parity is still open, and the specs themselves are drafts that become normative only at v1.0.
- The gate only binds callers that opt in; an agent framework that skips the verifier is outside the contract entirely.

## Pricing

Pricing does not apply: the protocol, reference implementation, conformance corpus, and TypeScript verifier are free and Apache-2.0, verified locally with no cloud component.

## Compared to

- [MCP](../mcp/index.md): MCP is the transport that carries the tool call; PIC sits before execution and would block the call MCP would otherwise deliver, and the project ships the MCP guard integration for exactly that seam.
- [Unified Harness Protocol (UHP)](../uhp/index.md): the other young spec in this category built around a conformance suite; UHP standardizes serving harnesses, PIC standardizes refusing tool calls, and both lean on conformance corpora instead of adoption.
- [Cordum](../../control-planes/cordum/index.md): the policy and approval plane above the gate; PIC verifies one proposal's provenance and evidence, Cordum enforces policy across runs, and the integration doc wires one into the other.

## Bottom line

**Recommended for teams building internal agent gateways where a wrong tool call costs money or data, who want a checkable verification contract today and can carry a pre-1.0 dependency.**
Not for teams needing an adopted standard with production references, browser or delegation lanes (A2A territory), or a gate that applies to frameworks that never call the verifier.
My disagreeable claim: this is the protocol layer agent security actually needs, which is why its non-adopter status is a market failure to watch rather than a verdict on the design.

## Changes

- 2026-10-11 - Created after the control-planes resolution routed the protocol here, with the thin-footprint-versus-formal-discipline gap recorded as the critical angle.
- 2026-10-16 - The v0.9.1 release (2026-10-14) landed after the last verification, so the maturity record moved from v0.9.0 to v0.9.1: structured `pic-cli verify --json` output, an optional MCP guard `on_allow` hook, and live-argument binding at the guard and bridge boundary (fail-closed via PIC_ARG_BINDING_MISMATCH), with the conformance corpus grown additively from 84 to 91 vectors and the wire format unchanged; the stale 67-star figure in Cautions was aligned to the recorded 69 baseline.
- 2026-10-22 - Rotation re-verification: every cited URL re-fetched live with no dead sources, the spec train re-confirmed at v0.9.1 with the RFC anchor, the frozen canonicalization spec, and the 91-vector corpus unchanged, PyPI still at 0.9.1 with 697 monthly downloads, and the footprint still the single 1-point Show HN; the repository refreshed (pushed 2026-10-21, 47 forks, 19 open issues).
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup (the light-theme source carried the dark-theme parameter; it now points at the default chart, matching the 2026-10-25 fallback fix).

## See also

- [MCP](../mcp/index.md) - the tool transport this contract gates
- [Unified Harness Protocol (UHP)](../uhp/index.md) - the other conformance-first young spec in this category
- [Cordum](../../control-planes/cordum/index.md) - the control plane that consumes PIC verifications
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/pic-standard/pic-standard - repository facts: 69 stars, 48 forks, Apache-2.0, created 2026-01-08, pushed 2026-10-13 (GitHub API, as of 2026-10-13)
- https://raw.githubusercontent.com/pic-standard/pic-standard/main/README.md - the contract fields, the Slack payment example, evidence semantics, and the v0.9.0 milestone (fetched 2026-10-11)
- https://raw.githubusercontent.com/pic-standard/pic-standard/main/docs/spec-status.md - the version table from RFC-0001 through v0.9.1, the wire-format stability record, and the spec-track statuses
- https://github.com/pic-standard/pic-standard/releases/tag/v0.9.1 - the v0.9.1 release notes: the on_allow hook, live-argument binding, and the 84-to-91 conformance expansion (fetched 2026-10-16)
- https://raw.githubusercontent.com/pic-standard/pic-standard/main/docs/independent-reviews/hermeticum-v0.8.3.md - the HERMETICUM stress-test provenance note: scope, non-certification statement, and attribution
- https://github.com/pic-standard/pic-standard-ts - the TypeScript verifier: corpus coverage for canonicalization, core, and trust sanitization, evidence mode open (GitHub API, as of 2026-10-11)
- https://pypi.org/pypi/pic-standard/json - version 0.9.1 uploaded 2026-10-14
- https://pypistats.org/api/packages/pic-standard/recent - 697 downloads in the month ending 2026-10-10
- https://hn.algolia.com/api/v1/search?query=%22PIC%20Standard%22%20agent&tags=story - the footprint scan: one 1-point Show HN (2026-01-13)
