---
title: HOL Guard
created: 2026-10-09
updated: 2026-10-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, guardrails, receipts, open-source]
readability: 3
audience_notes: >
  Developers who want risky coding-agent actions (destructive commands, secret reads, package installs, MCP calls) allowed, held, or blocked before they run, and who are comparing the freemium guards.
  Assumes you know what a PreToolUse hook is and the difference between a gate and a sandbox.
---

HOL Guard (hashgraph-online/hol-guard) is an Apache-2.0 local-first runtime security gate from the HOL (Hashgraph Online) consortium that evaluates a coding agent's shell commands, file reads, MCP tool calls, prompts, and package or skill installs before they run, returning allow, observe, ask, or block, and records a local trail of security receipts.

**Its design point is a published coverage contract: instead of advertising blanket protection, it asserts per-harness which event surfaces it can see, whether approvals are native or fall back to a browser, and whether failure blocks or fails open, with each assertion dated, commit-linked, and given an expiry.**

## What it is

A local runtime installed per harness with one script (`curl -fsSL https://hol.org/guard/install.sh | bash -s -- --harness <name> --mode install --verify`) or from PyPI, with no account required for local use.
The stable coverage contract asserts fifteen harnesses (Codex, Claude Code, OpenCode, GitHub Copilot CLI, Cursor, Cline, Antigravity CLI, Hermes, OpenClaw, Antigravity, Kimi Code, Grok Build, Pi, Oh My Pi, and ZCode), each with its event surfaces, approval path, fail behavior, and named limitations.
Beyond command and secret guarding it inspects the supply chain around the agent: bundled skills, plugins, hooks, agent settings, and MCP server configuration, with a separate `plugin-scanner` CI action for publishers.
Guard Cloud is the commercial layer on top: synced and searchable module settings, org-wide policy that local devices cannot weaken, team dashboards, and receipt sync across machines, while enforcement stays local and works offline.
The vendor is HOL, a consortium (its site lists 34 ecosystem partners and 65 public repositories) that positions the guard as part of an agentic-AI standards effort rather than a single-company product.

## Status

Active and shipping fast: 879 stars, 153 forks, and 124 open issues as of 2026-10-14, created 2026-03-28, pushed 2026-10-14, with v3.43.1 (2026-10-12) the latest version tag, PyPI in step at 3.43.1, and an automated extension-artifacts release train running beside the version tags.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hashgraph-online/hol-guard&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hashgraph-online/hol-guard&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hashgraph-online/hol-guard&type=date&legend=top-left" />
</picture>

PyPI downloads are 76,527 over the last month as of 2026-10-09 (pypistats, unchanged when re-fetched 2026-10-10 and again 2026-10-11), and the product page still claims 2M+ Guard PyPI downloads plus "5.4K+ HOL GitHub stars", an org-wide figure across all HOL repositories rather than the Guard repo's own count.
The 2M+ total sits awkwardly against the measured rate: 76,527 in the month ending 2026-10-09 would need roughly two years at this pace to reach it inside a seven-month-old project, and the tracker figure staying bit-for-bit identical across two re-fetches suggests a lagging source, so treat the headline as self-reported marketing until either number moves.
The coverage assertions on the site still carry their 2026-09-09 verification with an expiry of 2026-10-09, and a re-fetch on 2026-10-14 found the page and its change history unchanged five days past that expiry, still asserting version 3.0.1 while the release train sits at v3.43.1, so the project is shipping faster than its own verification contract renews and every published coverage cell is lapsed until a re-review lands.
A Hacker News search returns no threads about Guard (the single loose query match is an unrelated project), so the adoption evidence is the download count, the release cadence, and Product Hunt testimonials rather than independent technical discussion.

## Strengths

- The coverage contract is the most candid enforcement documentation in this category: every harness row names what Guard cannot see (inline model edits without tool calls, background sessions without a terminal, prompt events on several harnesses) instead of implying complete coverage.
- Breadth beyond the command surface: package, skill, plugin, hook, and MCP-configuration inspection covers the supply-chain paths most command guards ignore entirely.
- The maintainer-side `plugin-scanner` action turns the same checks into a CI gate for plugin publishers, which is a different distribution surface than any other guard here.
- Local-first with an org overlay: Guard Cloud policy that local devices cannot weaken is the feature a team actually needs, and the FAQ states enforcement never depends on cloud connectivity.

## Cautions

- Depth varies by harness and the gaps are the story: Kimi Code, Grok Build, and ZCode fail open, Cursor terminal commands outside agent sessions bypass it, and Claude Code background sessions surface no hook events at all.
- The published assertions expired on 2026-10-09 and remained unrenewed when re-checked on 2026-10-14, still pinned to version 3.0.1 against a v3.43.1 train, so treat any specific coverage cell as lapsed rather than a standing guarantee.
- No independent audit or adversarial review exists; a Hacker News footprint of zero six months in means the security claims rest on the project's own evidence links.
- The freemium ladder (Solo $4.99, Pro $15, Team $30 per month) puts receipt sync and org policy behind payment, and the latest release page still carries an unresolved "attribution for this release is being verified" notice, a small but odd provenance wrinkle for a security product.

## Pricing

Guard Local is free and open source under Apache-2.0, no account required.
Paid tiers, published as structured data on the product page: Solo $4.99 per month, Pro $15 per month, Team $30 per month, and Enterprise by contact, adding receipt sync, org policy, dashboards, and alerts.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-09 | Free | Recorded at $0, Guard Local, Apache-2.0, no account | https://hol.org/guard |
| 2026-10-09 | Solo | Recorded at $4.99/month | https://hol.org/guard |
| 2026-10-09 | Pro | Recorded at $15/month | https://hol.org/guard |
| 2026-10-09 | Team | Recorded at $30/month | https://hol.org/guard |

## Compared to

- [CC Safety Net](../cc-safety-net/index.md): the closest neighbor, also a per-CLI hook guard, MIT and entirely free, with parse-then-decide command blocking across sixteen CLIs; choose CC Safety Net for the simplest free command-and-secrets guard, HOL Guard when you also want approvals, receipts, package and skill scanning, or org policy.
- [Veto](../veto/index.md): an authorization kernel you wrap tools with in code, with approval routing and offline-verifiable receipts; choose Veto for in-process gates on money-and-data actions, HOL Guard for hook-based coverage of desktop coding agents.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): the programmatic multi-language governance program; choose it when governance must live in your application code rather than in the agent's hook surface.

## Bottom line

**Recommended for developers who want one guard across many coding-agent CLIs that covers commands, secrets, packages, skills, and MCP configuration, with approvals and local receipts and a paid path to team policy.**
Not for org-scale governance (that is a control plane, not a workstation guard), and not where a fail-open harness surface is an unacceptable risk, since three asserted harnesses say so in the project's own contract.

## Changes

- 2026-10-09 - Created from the awesome-ai-governance entrant scan, profiling the consortium-backed coverage-contract guard with its freemium cloud.
- 2026-10-10 - Recorded the release train at v3.39.0 (2026-10-10) with PyPI trailing at 3.38.0, the coverage contract passing its 2026-10-09 expiry without a re-verification, and the product page's download claim moved to 2M+, a total the measured monthly rate cannot back.
- 2026-10-11 - Release train moved to v3.42.0 (2026-10-10, three stable releases that day, PyPI caught up), the coverage contract re-checked still expired and now pinned to version 3.0.1, and the 2M+ claim re-checked against the pypistats figure that stayed bit-for-bit identical across two re-fetches.
- 2026-10-13 - Release train moved to v3.43.1 (2026-10-12, PyPI caught up) with v3.44.0 alphas staging; scale refreshed (865 stars, 116 open issues, pushed 2026-10-13).
- 2026-10-14 - The coverage contract re-checked five days past its 2026-10-09 expiry and still unrenewed (page and change history unchanged, assertions pinned to 3.0.1 against the v3.43.1 train), the release references corrected from the v3.42.0 record to v3.43.1, and scale refreshed (879 stars, 124 open issues, pushed 2026-10-14).

## See also

- [CC Safety Net](../cc-safety-net/index.md) - the free MIT command guard this most directly extends
- [Veto](../veto/index.md) - the in-code authorization kernel with the same receipts idea
- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call

## References

- https://hol.org/guard - product page: coverage claims, pricing tiers as structured data, scale figures, Guard Cloud scope
- https://hol.org/guard/security/coverage - the per-harness coverage contract: event surfaces, approval paths, fail behavior, limitations, verified and expiry dates
- https://github.com/hashgraph-online/hol-guard - repository: README, install paths, plugin-scanner, license
- https://api.github.com/repos/hashgraph-online/hol-guard - stars, forks, issues, creation and push dates as of 2026-10-14
- https://api.github.com/repos/hashgraph-online/hol-guard/releases - v3.43.1 (2026-10-12) the latest version tag, with the automated extension-artifacts train beside it
- https://pypi.org/pypi/hol-guard/json - version 3.43.1, in step with the GitHub tag as of 2026-10-14
- https://pypistats.org/api/packages/hol-guard/recent - 76,527 downloads in the last month as of 2026-10-09, unchanged when re-fetched 2026-10-10 and 2026-10-11
- https://hn.algolia.com/api/v1/search?query=hol-guard&tags=story - the zero-thread community-footprint check as of 2026-10-09
