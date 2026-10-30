---
title: Vestige
created: 2026-10-17
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, receipts, memory, open-source]
readability: 3
audience_notes: >
  Developers who run Claude Code or OpenClaw on their own machine and want a fail-closed gate that stops destructive commands and records what it decided, and who are weighing the freemium guards.
  Assumes you know what a PreToolUse hook is and that a hash chain is not a digital signature.
---

Vestige (samvallad33/vestige) is an AGPL-3.0 local fail-closed runtime firewall for AI agents: a PreToolUse hook gate called Operator Lite that judges each tool call against 42 deterministic rules (27 blocking, 15 shadow) before it runs, and a signed append-only log called Strata that records a receipt for every decision the gate and the memory server make.

**The project is also a pivot case study: it launched in July 2026 as a queryless memory layer for agent fleets, rebuilt its store as the Strata receipt log in v4.0.0, and shipped the execution gate as the headline product in v4.2.0, so the memory layer is now the supporting cast of an action firewall.**

## What it is

Operator Lite is one stdlib-only Python file that installs to `~/.operator/gate`, registers the Claude Code PreToolUse hook, and blocks from the first tool call; `operator-gate replay` scores your last 30 days of Claude Code history through the same rules without executing any of it, and `mode shadow` switches the gate back to recording without blocking.
The built-in rules are 27 STOP rules (OP-000 to OP-025 plus the owner's planted canary), covering gate self-edits, workspace and root deletion, wiping the Vestige store or the agent's own transcripts and shell history, blind recursive deletes, history destruction, force-pushes to shared branches, unreviewed publishes, paid deploys and infrastructure teardown, destructive SQL, persistence and scheduler installs, reverse shells, cloud-metadata endpoints, unrestorable loss, machine wreck, repo code run through git options, vulnerable writes, agent arming, piped downloads, harmful chains, a second spelling of a stopped action, found keys, protected files, remote deletes, a runaway brake, and the watch turnover after each compaction; the 15 shadow flags cover work-loss git operations, secret writes, persistence, and MCP argument exfiltration.
The parser canonicalizes commands before risk tagging, so quote reassembly, `$IFS`, `$(echo rm)` as the program, ANSI-C escapes, base64-decoded pipelines, brace and glob expansion, subshell time-bombs, and heredocs are decoded and judged; a 50-case GuardFall bypass corpus must pass 50 of 50 in CI.
Ports beyond Claude Code cover OpenClaw (a ClawHub plugin), Cursor, OpenCode, Gemini CLI, Windsurf, and Cline, on macOS, Linux, and newer Windows.
Behind the gate sits the memory server: four local binaries serving an MCP endpoint where every write is gated and returns a receipt against the Strata signed append-only log, with `causal_walk` and `vestige prove` tracing a failure backward over recorded edges to a commit and testing the lead against your own test suite.
Since v6.0.0 a `reflex` tool, called by the agent's own hooks rather than listed in the tool schema, carries every hook firing to that server: each gate receipt is verified against the digest chain and saved as a stop memory tied to its rule and told to the stopped agent once, every firing lands in a hash-chained Hook Ledger, failed calls are paired with the fix that later succeeded, and a context manifest folds memories the agent already holds out of later results.
The single-maintainer paid tier, Vestige Operator, is a closed archive sold once for $149 with a 30-day refund and every later version included, adding owner-written laws, a Board view of stops, the weekly Letter, onboarding, and one record of stops across every session, host, and agent CLI on the machine; the free gate's second-spelling rule keeps its memory per session, and the upgrade command verifies the archive's SHA-256 before unpacking it.

## Status

Active and fast-moving: 651 stars and 72 forks as of 2026-10-18, with 106 open issues and pull requests and the latest push on 2026-10-29 as of 2026-10-30, created 2026-01-25, with v6.0.0 (2026-10-28) the latest tagged release.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=samvallad33/vestige&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=samvallad33/vestige&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=samvallad33/vestige&type=date&legend=top-left" />
</picture>

The pivot timeline comes from the changelog: the Show HN of 2026-07-21 introduced the project as a queryless memory layer, v4.0.0 (2026-09-30) moved every write onto the gated Strata log and removed embeddings and SQLite from the default binaries, and v4.2.0 (2026-10-06) shipped Operator Lite as a standalone gate alongside the $149 Operator tier.
**The community footprint is thin: the only discussion I found is that 4-point Show HN thread, whose three comments are friendly chatter with zero technical critique, so there is no independent security review and no adversarial read of the parser claims anywhere.**
The changelog's own security entries are the closest thing to review evidence: they record a dashboard API that any web page could POST to before 4.1.0, a command-injection path through an untrusted checkout's git config, and credential keys stored unblocked before the 4.1.x gate, all found and fixed by the maintainer rather than by outsiders.

## Strengths

- Watching before trusting survives the switch to block-by-default: `replay` scores a month of your own history through the same rules without executing it and drafts candidate laws from what it saw, and `mode shadow` still turns blocking off when you want it.
- The boundary section is candid where it costs: receipts are hash-chained digests rather than signatures, the gate only blocks what is routed through hooked tools, and parse failures fail open except for plainly destructive text.
- The obfuscation-resistant canonicalizer and the 46-case GuardFall corpus give the parser claims a checkable form, which most hook guards in this category lack.
- One file, standard library only, no account and no cloud for enforcement; the receipt chain and the Strata log stay local.

## Cautions

- One maintainer, no independent audit, and an AGPL-3.0 license some shops cannot ship.
- It cannot see around hooks: a tool call that bypasses the hook surface is invisible to the gate, which the project says plainly.
- Parse failures fail open, so a hostile payload that defeats the parser is allowed, and the deterministic rule set stops a fixed list of command patterns rather than reasoning about intent.
- The paid Operator tier is a closed binary delivered from Payhip, and the Payhip page refuses fetchers, so the price and the upgrade terms are verifiable only through the README and changelog.
- The memory-layer history still dominates the project's discoverability (the npm package is `vestige-mcp-server`), so documentation about the gate and documentation about the memory server are easy to conflate.

## Pricing

Operator Lite is free and open source under AGPL-3.0, no account.
Vestige Operator is $149 once, with every later version included and a 30-day refund, delivered as a downloadable archive.
The memory server is part of the free AGPL-3.0 build.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-17 | Operator | Recorded at $149 one-time, every later version included | https://github.com/samvallad33/vestige |

## Compared to

- [CC Safety Net](../cc-safety-net/index.md): the widest free parse-then-decide guard, MIT, sixteen agent CLIs, no paid tier and no receipts; choose CC Safety Net for breadth at zero cost, Vestige for shadow-mode replay, receipts, and the causal walk behind the gate.
- [HOL Guard](../hol-guard/index.md): approvals, supply-chain inspection, org policy on Guard Cloud, and a published coverage contract; choose HOL Guard when team policy and per-harness coverage assertions matter, Vestige for a single-file personal gate with a one-time purchase instead of a subscription.
- [Veto](../veto/index.md): an authorization kernel you wrap tools with in code, with approval routing and portable receipts; choose Veto for in-process gates on money-and-data actions across frameworks, Vestige for hook-level defense of one developer machine.

## Bottom line

**Recommended for Claude Code and OpenClaw users who want a shadow-first local firewall with receipts, a replayable history of near-misses, and a one-time paid upgrade instead of a subscription.**
Not for org-scale governance (that is a control plane, not a workstation gate), not for anyone who needs an independent security review first, and not where fail-open parsing is an unacceptable failure mode.

## Changes

- 2026-10-17 - Created from the memory routing resolution, profiling the fail-closed Operator gate and the Strata receipt log after the pivot from queryless memory, with the changelog pivot timeline as the critical angle.
- 2026-10-19 - Release train moved to v5.0.0 (2026-10-18), the PRECEDENT release: a read-only `precedent` tool over the gate's stop receipts, a `gather` issue hunt, a WebGPU dashboard rebuild, and two maintainer-found hook security fixes (a command-injection path in a hook script and hooks running Python without isolated mode).
- 2026-10-25 - Release train moved to v5.0.1 (2026-10-23): Retroactive Salience Backfill returns to the Strata memory path, so new information can raise or lower the salience of earlier memories.
- 2026-10-30 - Release train moved to v6.0.0 (2026-10-28): the Reflex tool carries every hook firing into the server, where gate receipts become stop memories and every firing lands in a hash-chained Hook Ledger under a context manifest with failure pairing, stale-belief push, and compaction survival, and Operator Lite absorbs every per-call rule the paid gate had (42 rules, 27 STOP and 15 SHADOW, planted canaries included), leaving Operator to sell laws, the Board, the weekly Letter, onboarding, and the cross-session stop record.

## See also

- [CC Safety Net](../cc-safety-net/index.md) - the free multi-CLI command guard this sits next to on the same hook surface
- [HOL Guard](../hol-guard/index.md) - the freemium guard with the published coverage contract and org cloud
- [Veto](../veto/index.md) - the in-code authorization kernel with the same receipts idea
- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [AgentMemory](../../memory/agentmemory/index.md) - the memory shelf this project pivoted away from, and what its Strata log would have competed with
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call

## References

- https://github.com/samvallad33/vestige - README: the firewall framing, Operator Lite install and rules, Operator tier, memory server, integrations, license
- https://api.github.com/repos/samvallad33/vestige - stars, forks, issues, creation and push dates as of 2026-10-17
- https://api.github.com/repos/samvallad33/vestige/releases - release metadata, v6.0.0 (2026-10-28) the latest tagged release
- https://github.com/samvallad33/vestige/releases/tag/v6.0.0 - the Reflex release notes: the Hook Ledger, stop memories, the context manifest, and the per-call rules moving into the free gate
- https://github.com/samvallad33/vestige/releases/tag/v5.0.0 - the PRECEDENT release notes: precedent tool, gather, dashboard rebuild, hook security fixes
- https://raw.githubusercontent.com/samvallad33/vestige/main/CHANGELOG.md - the pivot timeline (memory to Strata to Operator Lite), the $149 Operator pricing change, and the project's own fixed-vulnerability history
- https://raw.githubusercontent.com/samvallad33/vestige/main/operator-lite/README.md - the gate's rule table, replay command, parser claims, platforms, and the receipts-are-digests admission
- https://hn.algolia.com/api/v1/search?query=vestige&tags=story - the community-footprint check as of 2026-10-17
- https://news.ycombinator.com/item?id=48993285 - the 4-point, three-comment Show HN for the pre-pivot memory layer, the thin-footprint signal
