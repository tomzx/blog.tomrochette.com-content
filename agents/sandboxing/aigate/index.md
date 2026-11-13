---
title: aigate
created: 2026-08-30
updated: 2026-11-12
readability: 3
audience_notes: >
  Engineers who wrap coding agents in OS-level restriction and want to know what a small sandbox tool actually enforces.
  Assumes you know what namespaces, ACLs, and an egress allowlist are.
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, security, cli, open-source]
---

aigate is a free, MIT-licensed Go CLI that wraps any AI coding agent in an OS-level sandbox with kernel-enforced file restrictions, command blocking, and network egress allowlists, plus stdout secret masking and a local audit log.

**aigate earns its note despite fourteen stars because the mechanism is real and documented, and the 2026-11-10 release wave proved the caution this note has carried since August: v1.1.2 fixed a macOS ssh-agent leak that let any sandboxed agent reach your ssh keys, exactly the bypass a sandbox with no security process accumulates quietly, so the treat-it-as-a-reference-design verdict stands.**

## What it is

`aigate run -- <agent>` launches a tool inside a sandbox with deny rules for `.env`, secret directories, and key files, blocked commands (curl, wget, ssh), an egress domain allowlist, `allowed_paths` scoping that hides the rest of `$HOME`, stdout secret masking, and a JSONL audit log with a local dashboard.
The mechanism layers persistent POSIX ACLs with Linux mount, user, PID, and network namespaces via Bubblewrap, egress filtering through slirp4netns plus iptables, and Apple Seatbelt profiles on macOS, so the agent process cannot negotiate with the policy the way it could with a `.claudeignore`.
Tool-agnostic by design: one wrapper for Claude Code, Cursor, Copilot, Aider, or plain shell.
The 2026-11-10 wave added identities (isolated Claude Code and GitHub CLI logins per account, each invisible to the others) and the judge, an optional hook broker whose local rules and Cloudflare Clef or Jev model checks can deny or ask but never allow, with credentials and audit held outside the sandbox.
Linux-first (amd64, arm64), macOS supported, Windows binary undocumented; requires bubblewrap and slirp4netns plus a one-time `sudo aigate setup`.
MIT, by a small anonymous GitHub organization.

## Status

Tiny but no longer quiet: 14 stars, 1 fork as of 2026-10-11, created 2026-02-12, pushed 2026-11-10, 51 commits and 2 apparently related contributors (machado144 with 45, murilopmachado with 6), 2 open issues as of 2026-11-12.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AxeForging/aigate&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AxeForging/aigate&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AxeForging/aigate&type=date&legend=top-left" />
</picture>

v1.0.0 released 2026-07-19 and then nothing until 2026-11-10, when three releases cut the same day resumed the train: v1.1.0 (per-session Linux networks with loopback denied by default and a `--port` flag for one dev server, `allow_net` actually enforced under the stricter AppArmor bubblewrap profiles where it had silently not applied, the sandboxed command stripped of the privileges that could flush the firewall or unmount hidden files, plus `aigate init --upgrade` for the new masking presets), v1.1.1 (output streaming again with masking on, error messages that name the folders to allow when scope hides a program, dashboard cleanup), and v1.1.2 (security fixes: the macOS `SSH_AUTH_SOCK` no longer passed into sessions, where an agent could use your ssh keys, `deny_exec` applied under symlinked `/var` paths where blocked tools still ran, and Linux `deny_read` covering files that appear mid-session).
**A missing community footprint is still the headline, and it sharpened: no audit, no SECURITY.md, no advisory process, and v1.1.2's ssh-agent leak is precisely the kind of bypass that sat unreported here, self-disclosed in release notes rather than through any security channel.**

## Strengths

- Genuine layered kernel enforcement, not an allowlist the model can prompt its way around.
- Thoughtful operational details: `aigate doctor` with READY, DEGRADED, and BLOCKED verdicts and CI-friendly exit codes, per-project config, two-layer command blocking.
- Tool-agnostic wrapper, which harness built-ins cannot be.
- Usable secure defaults out of the box, plus secret masking and an audit log bigger tools lack.

## Cautions

- No security audit, no SECURITY.md, and no advisory process; v1.1.2's macOS ssh-agent leak shows the failure mode is not hypothetical, and the fixes travel in release notes, the same channel as features.
- Known incomplete enforcement by its own docs: resource limits configured but unenforced, macOS subcommand blocks degrade to pre-sandbox checks, running from `$HOME` defeats scope mode, masking is application-layer.
- macOS path relies on `sandbox-exec`, deprecated by Apple, and its network stays shared with the Mac (localhost services reachable when `allow_net` is empty); the per-session network isolation of v1.1.0 is Linux-only and needs slirp4netns.
- Bus factor of two (apparently related); the four-month dormancy right after launch is part of its history even after the resumed train.

## Pricing

Free and open source under MIT, no paid tiers, no pricing page.

## Compared to

- [OpenShell](../openshell/index.md): the vendor-backed, container-based system with L7 policy and a community; choose aigate for a dependency-light local wrapper, OpenShell for anything organizational.
- Docker containers: the proven, audited primitive; choose aigate when the agent must work in your real project directory with surgical denies rather than a whole container.
- Harness built-ins (Codex landlock and Seatbelt): first-party and always in sync but tied to one tool; aigate covers many tools uniformly.

## Bottom line

**Recommended as a study of what kernel-level agent sandboxing looks like at small scale, and for tinkerers on Linux who will read the source before trusting it.**
Not for anyone needing a security boundary they did not audit themselves; use [OpenShell](../openshell/index.md) or a harness built-in there.

## Changes

- 2026-08-30 - Created as the sandboxing note, kept despite a tiny footprint per the missing-footprint-is-a-signal rule.
- 2026-09-10 - Sandboxing reference canonicalized to learn.chatgpt.com/docs/sandboxing.
- 2026-10-02 - Added the dormancy evidence: no push since 2026-08-04, fifty-nine days of quiet as of this refresh; counts unchanged (14 stars, 0 issues).
- 2026-10-07 - Added the AxeForging/aigate star history chart to the Status section.
- 2026-10-09 - Quiet window extended to sixty-six days (last push still 2026-08-04); stars, forks, and issues unchanged.
- 2026-10-10 - Quiet window extended to sixty-seven days (last push still 2026-08-04); stars, forks, and issues unchanged.
- 2026-10-11 - Quiet window extended to sixty-eight days (last push still 2026-08-04); stars, forks, and issues unchanged.
- 2026-10-12 - Quiet window extended to sixty-nine days (last push still 2026-08-04); stars, forks, and issues unchanged.
- 2026-10-13 - Quiet window extended to seventy days (last push still 2026-08-04); stars, forks, and issues unchanged.
- 2026-10-19 - Rotation re-verification: every cited URL re-fetched (repository, README, user guide, the enforcement-matrix site, the v1.0.0 release page, the built-in sandboxing comparison, all alive); the push date holds at 2026-08-04 and the quiet window extends to seventy-six days as of 2026-10-19.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched (repository, README, user guide, the enforcement-matrix site, the v1.0.0 release page, the built-in sandboxing comparison, all alive); the push date holds at 2026-08-04 and the quiet window extends to eighty-eight days as of 2026-10-31.
- 2026-11-07 - Rotation re-verification: every cited URL re-fetched (repository, README, user guide, the enforcement-matrix site, the v1.0.0 release page, the built-in sandboxing comparison, all alive); the push date holds at 2026-08-04 and the quiet window extends to ninety-five days as of 2026-11-07.
- 2026-11-12 - Out-of-rotation re-verification for the 2026-11-10 release wave: every cited URL re-fetched and alive (repository, README, user guide, the enforcement-matrix site, the v1.0.0 release page, the built-in sandboxing comparison), and the dormancy reading replaced by the resumed train (v1.1.0, v1.1.1, and v1.1.2 all released 2026-11-10: per-session Linux networks with loopback denied, allow_net enforced under stricter AppArmor profiles, identities, the judge broker, and the macOS ssh-agent and symlinked-path security fixes), the commit count moving from twenty to fifty-one and open issues from zero to two, with the thesis, What-it-is, Status, and Cautions updated and the no-audit reading kept.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the vendor-backed counterpart
- [Codex](../../harnesses/codex/index.md) - the built-in sandboxing reference point
- [claude-code-hooks](../../executions/claude-code-hooks/index.md) - the application-layer alternative to kernel enforcement

## References

- https://github.com/AxeForging/aigate - repository, features, license, and the 14-star footprint this note records
- https://raw.githubusercontent.com/AxeForging/aigate/HEAD/README.md - the why-kernel argument and install flow
- https://raw.githubusercontent.com/AxeForging/aigate/HEAD/docs/user/README.md - the exact mechanism and its own enforcement caveats
- https://axeforging.github.io/aigate/ - the per-OS enforcement matrix
- https://github.com/AxeForging/aigate/releases/tag/v1.0.0 - the release history
- https://github.com/AxeForging/aigate/releases/tag/v1.1.0 - the v1.1.0 release notes: per-session networks, the enforcement fixes, identities, and the judge
- https://github.com/AxeForging/aigate/releases/tag/v1.1.2 - the v1.1.2 security fixes: the macOS ssh-agent leak, symlinked deny_exec paths, and mid-session deny_read coverage
- https://learn.chatgpt.com/docs/sandboxing - the built-in sandboxing comparison reference
