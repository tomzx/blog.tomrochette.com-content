---
title: Tracekit
created: 2026-10-21
updated: 2026-10-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, receipts, audit, open-source]
readability: 3
audience_notes: >
  Engineers whose agents act on systems that matter and who need a record of what the agent did that survives the agent editing its own logs, with a gate that stops the worst calls before they run.
  Assumes you know what Certificate Transparency is and why ordinary tracing cannot answer for a log the agent can rewrite.
---

Tracekit (Cygnux-Labs/Tracekit) is an MIT signer and evidence log that decides each agent tool call before it runs (allow, deny, or ask a person), signs every call, decision, and result into an RFC 6962 Merkle log, and exports each run as a .tkb bundle that independent Python and TypeScript verifiers check offline.

**Its design point is borrowed from Certificate Transparency: the agent never holds a signing key and never numbers the records, so whether the log can be trusted stops depending on the agent's own report and starts depending on where the signer runs and who witnesses it.**

## What it is

Three pieces: an SDK or hook inside the agent (Python and TypeScript, with quickstarts for Claude Code, Codex CLI, Cursor, Gemini CLI, the OpenAI Agents SDK, LangChain, MCP, CrewAI, and about twenty-five integrations in all), a signer process placed out of the agent's reach, and the log.
The signer answers allow, deny, or ask for each call, signs the call, the decision, and the result as Ed25519 over RFC 8785 canonical JSON, and chains each record to the hash of the one before it, so a changed byte fails verification at that record.
Checkpoints are C2SP signed notes that independent witnesses cosign, and `tracekit export` produces one .tkb file per run that `tracekit verify` checks offline against pinned keys, answering VERIFIED, FAILED, or UNVERIFIABLE and naming the record that changed.
The signer-placement table is the threat model in miniature: laptop dev mode runs where the agent's own user can reach the key and records that fact, while separate-user, container, and central-HTTPS modes record stronger isolation.
The project is under a month old (repository created 2026-09-26) from Cygnux Labs, which offers a free two-week pilot, and the docs live in the repository wiki.

## Status

Active and very young: 138 stars, 9 forks, and 12 open issues as of 2026-10-21, created 2026-09-26, pushed 2026-10-20, with the PyPI package tracekit-ai at 1.4.1 (Beta, 2026-10-20) and five releases between 2026-10-16 and 2026-10-20.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Cygnux-Labs/Tracekit&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Cygnux-Labs/Tracekit&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Cygnux-Labs/Tracekit&type=date&legend=top-left" />
</picture>

**The README's own boundary table is the critical read: a verified run proves the record is intact, not that every action was captured, and the log catches tail truncation and re-signing with a stolen key only when a witness holds a copy of the head, but the witness and the monitor are both experimental and no public witness is running yet.**
The proof numbers (570 of 570 harmful calls stopped across 11 classes with one false alarm in 738, 0.91 milliseconds added per call at p99, 8 of 8 tamper attacks caught with a witness) are all self-reported.
A Hacker News search returns no threads about this project; the hits are an unrelated 2011 JavaScript stack-trace library and a different repository with the same name, so the community footprint is the repository alone.

## Strengths

- The trust model is stated in deployment terms rather than adjectives: the placement table names who can reach the keys and what isolation each mode records, and unwitnessed runs verify as dev.
- Gating and evidence are one artifact: the deny that stopped the call and the signed record that proves it land in the same log, which neither a tracer nor a bolt-on audit layer gives you.
- The standards stack (Ed25519, RFC 8785 canonical JSON, RFC 6962 Merkle trees, C2SP checkpoints) is checkable rather than proprietary, and the verifiers are separate implementations in two languages.
- The demo shows the exact failure the tool exists to catch: a scripted agent deletes orders, rewrites its own log, and verification fails at the tampered record.

## Cautions

- Three and a half weeks old, zero community footprint, and every security number is the project's own; nobody independent has tried to break the log.
- Without a witness, the two attacks that matter most (truncating the tail, re-signing with a stolen key) are exactly the ones the log cannot catch, and no public witness exists yet.
- Placement decides everything: the laptop dev mode records `same-user` isolation, which the README itself says a knowing agent could exploit by reading the key and re-signing.
- The name collides with an older JavaScript library and at least one other agent project, so searching for coverage takes care.

## Pricing

Free and open source under MIT, self-hosted, no account.
The vendor sells a free two-week pilot for teams whose agents act on systems an outsider audits; no dollar prices are published anywhere cited, so there is nothing to track.

## Compared to

- [Veto](../veto/index.md): both decide calls before they run with offline-verifiable receipts, but Veto evaluates your YAML rules inside your process, while Tracekit separates the signer from the agent so the agent cannot touch the record; choose Veto for an in-process gate, Tracekit when the record has to survive the agent.
- [arifOS](../arifos/index.md): the kernel that judges proposals against thirteen policy floors and publishes its own self-audit; choose arifOS for verdict governance, Tracekit when the tamper-evident record itself is the product.
- [Vestige](../vestige/index.md): the single-file hook gate with hash-chained receipts defending one workstation; choose Vestige for personal defense, Tracekit when an auditor, customer, or insurer must trust the record.

## Bottom line

**Recommended as the category's first Certificate-Transparency-style evidence plane, worth piloting where an agent's actions need a record a third party can trust, with the caveat that the witness tier the trust argument depends on does not exist publicly yet.**
Not for anyone who needs an independently reviewed gate today, and not for debugging a prototype, where the README itself points you to OpenTelemetry, Langfuse, or LangSmith.

## Changes

- 2026-10-21 - Created from the awesome-ai-governance scan (added to the source's Agent Action Records section on 2026-10-19), profiling the CT-style signer as the category's first witness-cosigned evidence log.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the in-process receipt gate this contrasts with on signer placement
- [arifOS](../arifos/index.md) - the other evidence-first kernel, with its self-audit as the critical angle
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for judging the call before it runs

## References

- https://github.com/Cygnux-Labs/Tracekit - README: design, signer-placement table, boundary table, standards, proof tables
- https://api.github.com/repos/Cygnux-Labs/Tracekit - stars, forks, issues, creation and push dates as of 2026-10-21
- https://api.github.com/repos/Cygnux-Labs/Tracekit/releases - v1.4.1 (2026-10-20) and the release train
- https://pypi.org/pypi/tracekit-ai/json - tracekit-ai 1.4.1, Beta
- https://github.com/Cygnux-Labs/Tracekit/wiki/Witnesses - checkpoint mechanics, the per-witness trust model, and the experimental status
- https://github.com/agentrust-io/awesome-ai-governance - the listing that surfaced it (Agent Action Records, added 2026-10-19)
- https://hn.algolia.com/api/v1/search?query=tracekit&tags=story - the zero-thread footprint check and the name collisions
