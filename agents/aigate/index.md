---
title: aigate
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, security, cli, open-source]
readability: 3
audience_notes: >
  Engineers who wrap coding agents in OS-level restriction and want to know what a small sandbox tool actually enforces.
  Assumes you know what namespaces, ACLs, and an egress allowlist are.
---

aigate is a free, MIT-licensed Go CLI that wraps any AI coding agent in an OS-level sandbox with kernel-enforced file restrictions, command blocking, and network egress allowlists, plus stdout secret masking and a local audit log.
Facts below verified as of 2026-09-04.

**aigate earns its note despite fourteen stars because the mechanism is real and documented, and the fourteen stars are themselves the finding: a kernel-enforced sandbox with no security process is where bypass bugs would go unreported, so treat it as a reference design, not a boundary.**

## What it is

`aigate run -- <agent>` launches a tool inside a sandbox with deny rules for `.env`, secret directories, and key files, blocked commands (curl, wget, ssh), an egress domain allowlist, `allowed_paths` scoping that hides the rest of `$HOME`, stdout secret masking, and a JSONL audit log with a local dashboard.
The mechanism layers persistent POSIX ACLs with Linux mount, user, PID, and network namespaces via Bubblewrap, egress filtering through slirp4netns plus iptables, and Apple Seatbelt profiles on macOS, so the agent process cannot negotiate with the policy the way it could with a `.claudeignore`.
Tool-agnostic by design: one wrapper for Claude Code, Cursor, Copilot, Aider, or plain shell.
Linux-first (amd64, arm64), macOS supported, Windows binary undocumented; requires bubblewrap and slirp4netns plus a one-time `sudo aigate setup`.
MIT, by a small anonymous GitHub organization.

## Status

Tiny and quiet, and the numbers are the story: 14 stars, 1 fork, 0 issues as of 2026-09-02, created 2026-02-12, 20 commits total, 2 apparently related contributors.
v1.0.0 released 2026-07-19 with a few commits since.
**A missing community footprint is itself a signal worth stating: no audits, no advisories, no external users visible, and no SECURITY.md.**

## Strengths

- Genuine layered kernel enforcement, not an allowlist the model can prompt its way around.
- Thoughtful operational details: `aigate doctor` with READY, DEGRADED, and BLOCKED verdicts and CI-friendly exit codes, per-project config, two-layer command blocking.
- Tool-agnostic wrapper, which harness built-ins cannot be.
- Usable secure defaults out of the box, plus secret masking and an audit log bigger tools lack.

## Cautions

- No security audit and no visible security process, fatal for something whose entire value is being the trust boundary.
- Known incomplete enforcement by its own docs: resource limits configured but unenforced, macOS subcommand blocks degrade to pre-sandbox checks, running from `$HOME` defeats scope mode, masking is application-layer.
- macOS path relies on `sandbox-exec`, deprecated by Apple; network filtering silently degrades without slirp4netns.
- Bus factor of one or two people; abandonment risk is the base rate for this profile.

## Pricing

Free and open source under MIT, no paid tiers, no pricing page.

## Compared to

- [OpenShell](../openshell/index.md): the vendor-backed, container-based system with L7 policy and a community; choose aigate for a dependency-light local wrapper, OpenShell for anything organizational.
- Docker containers: the proven, audited primitive; choose aigate when the agent must work in your real project directory with surgical denies rather than a whole container.
- Harness built-ins (Codex landlock and Seatbelt): first-party and always in sync but tied to one tool; aigate covers many tools uniformly.

## Bottom line

**Recommended as a study of what kernel-level agent sandboxing looks like at small scale, and for tinkerers on Linux who will read the source before trusting it.**
Not for anyone needing a security boundary they did not audit themselves; use [OpenShell](../openshell/index.md) or a harness built-in there.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the vendor-backed counterpart
- [Codex](../codex/index.md) - the built-in sandboxing reference point
- [claude-code-hooks](../claude-code-hooks/index.md) - the application-layer alternative to kernel enforcement

## References

- https://github.com/AxeForging/aigate - repository, features, license, and the 14-star footprint this note records
- https://raw.githubusercontent.com/AxeForging/aigate/HEAD/README.md - the why-kernel argument and install flow
- https://raw.githubusercontent.com/AxeForging/aigate/HEAD/docs/user/README.md - the exact mechanism and its own enforcement caveats
- https://axeforging.github.io/aigate/ - the per-OS enforcement matrix
- https://github.com/AxeForging/aigate/releases/tag/v1.0.0 - the release history
- https://developers.openai.com/codex/sandboxing - the built-in sandboxing comparison reference
