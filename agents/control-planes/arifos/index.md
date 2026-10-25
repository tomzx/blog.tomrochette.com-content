---
title: arifOS
created: 2026-10-16
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, governance-kernel, mcp, open-source]
readability: 3
audience_notes: >
  Engineers who want a deterministic judge between an agent's proposal and its execution, and who will read a self-audit before trusting a governance kernel.
  Assumes you know what an MCP tool call and a hash chain are.
---

arifOS (ariffazil/arifOS) is an AGPL-3.0 governance kernel for MCP agents that evaluates a proposed action against thirteen constitutional floors before it executes, returns one of seven verdicts (SEAL, HOLD, SABAR, PARTIAL, PROVISIONAL, HOLD_888, VOID), and writes each verdict to an append-only hash-chained ledger called VAULT999.

**Its separation of powers is the design point: proposer, judge, executor, and witness are four different components (the sibling projects A-FORGE, FRAME, and the AAA plane), and the judge never consults a model, so the same proposal always yields the same verdict.**

## What it is

A single-maintainer kernel you self-host or reach as the maintainer's public MCP endpoint (streamable HTTP, eight canonical verbs, published schemas), installable with `pip install arifos` and calendar-versioned (PyPI 1!2026.10.17).
The federation assigns roles so no component holds all the power: AAA does discovery and attention, arifOS judges, A-FORGE executes (file, service, and git mutations gated by per-action-class budgets, HMAC-signed requests, and a receipt per run), FRAME witnesses, and VAULT999 remembers, with proposer-judge-executor-witness separation stated as an invariant.
The thirteen floors are the policy gates, the README naming F2, F11, F12, and F13 as the ones currently failing, and the wire contract answers with seven verdicts rather than a boolean.
Verdicts land in VAULT999 (457,000-plus append-only records per the repository's own manifest) with decision context, evidence references, and provenance hashes, and an A2A v1.0 agent card exposes the kernel to agent-to-agent discovery.
The maintainer positions it as the layer between "agent wants to act" and "action is permitted", explicitly not a model, not an agent framework, and not a sandbox.

## Status

Active and early: 54 stars and 9 forks as of 2026-10-18, with 6 open issues and the latest push on 2026-10-25 as of 2026-10-25, created 2025-11-17, with the public kernel endpoint answering healthy when I checked on 2026-10-16.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ariffazil/arifOS&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ariffazil/arifOS&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ariffazil/arifOS&type=date&legend=top-left" />
</picture>

**The most striking artifact is the README's own verified-state block, machine-stamped by the project's probe scripts and reading like an adversarial audit the project ran on itself: the current self-measurement (stamped 2026-10-21) reads the kernel degraded with 10 of 13 floors measured pass and failing F1 and F8, while the pinned independent audit of 2026-10-11 still reads 2 pass, 4 fail (F2, F11, F12, F13), and 7 unmeasured, and the block itself warns that these are two different witness objects, with verified actor identity, receipt fidelity on the invocation-telemetry surface, and independent reconstruction all still failing in the audit line.**
That same block admits an earlier 13-of-13 floors reading was a false pass caused by a threshold defect, and states plainly that there are no customers, no pilots, no independent benchmark, no external security audit, and zero revenue.
A Hacker News search returns no threads about arifOS, so an eleven-month-old kernel has zero community footprint, and the awesome-ai-governance directory listing (added 2026-10-16) is the only third-party surface I found.

## Strengths

- The separation of powers is checkable architecture, not a promise: a judge that cannot execute, an executor that cannot self-authorize, and a witness on separate infrastructure are properties you can test.
- The judge is deterministic and model-free, so policy cannot drift with a model update and the verdict is reproducible from the proposal alone.
- The self-audit culture is unlike anything else in this category: the project publishes its own failing floors, a caught false pass, and a zero-revenue statement, which makes every other claim falsifiable.
- Receipt-first audit: consequential verdicts land in an append-only hash chain with evidence references, and CI gates enforce MCP conformance, vault integrity, and runtime drift.

## Cautions

- The kernel's own audit says actor identity is unverified on the live path (observed calls arrived unsigned) and a HOLD verdict was persisted as ok:true on the telemetry surface, so the receipts are not evidence-grade yet by the project's own reading.
- The independent audit still shows only 2 of 13 floors passing and 7 unmeasured, and the project's own rules are that unmeasured is not pass and that self-measurement is not an independent audit.
- One maintainer, zero community footprint, and AGPL-3.0, which some shops cannot ship.
- The vocabulary is dense and self-referential (floors, organs, federation contracts, verdict names like SABAR and HOLD_888), so evaluation costs more reading time than any other gate in this category, and the solo compose stack runs everything on one host, which the project itself discloses.

## Pricing

Free and open source under AGPL-3.0, self-hosted, with the maintainer's own deployment public on the internet.
No paid tier or price exists anywhere in the project, and the README's own audit records zero revenue, so there is nothing to track.

## Compared to

- [Veto](../veto/index.md): both return pre-execution verdicts with receipts, but Veto evaluates YAML rules over tool calls inside your process, while arifOS is a federation-level kernel with thirteen floors and a model-free judge; choose Veto for an embeddable gate, arifOS for a separation-of-powers kernel.
- [OpenAPPA](../openappa/index.md): information-flow labels over what an agent reads; arifOS judges what an agent proposes to do.
- [IBM ContextForge](../ibm-contextforge/index.md): the adopted MCP gateway layer; ContextForge authenticates and rate-limits traffic at the wire, arifOS judges each proposed action against policy floors before execution.

## Bottom line

**Recommended as the category's clearest separation-of-powers design and a watch-or-fork candidate; the self-audit makes it the easiest kernel here to evaluate, and the same audit is why it is not yet one to deploy.**
Not for anyone who needs verified actor identity, measured floors, or a community to escalate to today.

## Changes

- 2026-10-16 - Created from the awesome-ai-governance scan (PR #148, 2026-10-16), profiling the AGPL-3.0 MCP governance kernel with its own false-pass self-audit as the critical angle, and folding the sibling executor A-FORGE into the note per the sibling fold precedent.
- 2026-10-21 - The README's self-measurement block moved to 7 of 13 floors measured pass with the kernel self-reporting degraded (2026-10-20 stamp), against the unchanged 2026-10-11 independent audit reading of 2 pass, 4 fail, and 7 unmeasured; the status and caution rewritten to keep the two witness objects separate.
- 2026-10-23 - The self-measurement block moved again to 10 of 13 floors measured pass, failing F1 and F8, still self-reporting degraded (2026-10-21 stamp), with the independent audit reading unchanged and the PyPI package trailing at 1!2026.10.17 while repository tags reached v2026.10.23.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the embeddable verdict kernel this most closely parallels
- [OpenAPPA](../openappa/index.md) - the information-flow alternative on the data-reading axis
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for judging the call before it runs

## References

- https://github.com/ariffazil/arifOS - README: floors, verdicts, federation roles, verified-state block, A2A card, CI gates
- https://github.com/ariffazil/A-FORGE - the sibling executor: per-action-class budgets, HMAC-signed requests, receipt per run, never self-authorizes
- https://pypi.org/pypi/arifos/json - the calendar-versioned PyPI package, 1!2026.10.17
- https://arifos.arif-fazil.com/ - the kernel's documentation and deployment surface
- https://arifos.arif-fazil.com/health - the live endpoint answering healthy as of 2026-10-16
- https://github.com/agentrust-io/awesome-ai-governance - the directory listing that surfaced both repositories (PR #148, 2026-10-16)
- https://hn.algolia.com/api/v1/search?query=arifOS&tags=story - the zero-thread community-footprint check as of 2026-10-16
