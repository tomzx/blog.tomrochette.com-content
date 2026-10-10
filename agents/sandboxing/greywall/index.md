---
title: Greywall
created: 2026-10-08
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, security, cli, open-source]
readability: 3
audience_notes: >
  Engineers who want deny-by-default OS-native fencing around coding agents and would rather watch what the agent tries before restricting it.
  Assumes you know what bubblewrap, Seatbelt, and a SOCKS5 proxy are.
---

Greywall is GreyhavenHQ's Apache-2.0 Go CLI that sandboxes coding agents on Linux and macOS with bubblewrap, Landlock, seccomp, and eBPF on Linux and Seatbelt on macOS, and it is a fork of Fence that adds what the parent lacks: a companion proxy (greyproxy) that swaps credentials at the HTTP layer, and an allow-by-default watch mode (greywatch) with a live dashboard.

**Greywall's contribution to this category is the observability half of the sandbox workflow, watch first and deny second, with learning mode turning the traces into least-privilege profiles, and its security model states the same ceiling its parent states, defense-in-depth for semi-trusted code, not a boundary against a determined attacker.**

## What it is

`greywall -- <command>` runs with filesystem and network denied by default, command deny rules, and built-in agent profiles for Claude Code, Codex, Cursor, Aider, Goose, Gemini CLI, OpenCode, Amp, Cline, Copilot, Kilo, Auggie, and Droid.
Every connection routes through greyproxy, a companion SOCKS5 proxy with a live allow-and-deny dashboard, so network policy is visible instead of silent.
Credential protection detects credential-bearing environment variables, replaces their values with placeholders, and greyproxy substitutes the actual values at the HTTP layer, so keys never enter the sandbox.
Attribution is stated in the README: Greywall is a fork of Fence, created by JY Tan at Tusk AI, and inspired by Anthropic's sandbox-runtime; installs come through a Homebrew tap, an install script, or Go, and a Go library surface exists.

## Status

Launched in March 2026 and quiet since: 309 stars, 37 forks, 26 open issues as of 2026-10-09, created 2026-03-04, pushed 2026-08-13, with v0.3.7 (2026-06-01) the last of an April-through-June release train.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=GreyhavenHQ/greywall&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=GreyhavenHQ/greywall&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=GreyhavenHQ/greywall&type=date&theme=dark&legend=top-left" />
</picture>

**The launch got no help from Hacker News: a 7-point Show HN on 2026-03-13, a 1-pointer and a 3-point greyscan submission four days later, and one independent review since.**
Fifty-seven days without a push as of 2026-10-09 leaves a small project with a complete docs site and a stalled train, and the companion greyproxy has been quiet since 2026-06-02.

## Strengths

- Watch-then-restrict is the right order for adopting a sandbox: greywatch runs an agent allow-by-default with every request logged on the dashboard, and learning mode traces filesystem access (strace on Linux, eslogger on macOS) into a least-privilege profile.
- Credential substitution puts the proxy-held-key design the hosted platforms advertise into a workstation CLI: placeholders in the environment, values injected by greyproxy at the HTTP layer.
- Five Linux enforcement layers (bubblewrap namespaces, Landlock, seccomp, eBPF monitoring, TUN capture), documented per OS in a feature matrix rather than marketed.
- The docs state the ceiling in plain words instead of overselling: defense-in-depth for semi-trusted commands, not strong isolation against actively malicious code.

## Cautions

- Fifty-seven days without a push as of 2026-10-09 and a release train that stopped at v0.3.7 on 2026-06-01; the fork inherits its parent's design but not its cadence, since Fence continued on its own org and reached v0.1.67 in September.
- macOS enforcement rides sandbox-exec, which Apple deprecated, the same exposure Fence and aigate carry, and macOS gets no transparent traffic capture because the tun2socks path is Linux-only.
- Kernel primitives only, no VM or gVisor tier, and no independent audit; greywall performs no domain filtering itself, delegating all of it to greyproxy.
- The near-zero Hacker News footprint at 307 stars cuts both ways: little criticism, but also no field reports from users.

## Pricing

Free and open source under Apache-2.0, with greyproxy under MIT; no paid tiers or hosted offering found as of 2026-10-08.

## Compared to

- [Fence](../fence/index.md): the parent project, still maintained on the fencesandbox org; choose Fence for the simpler original on an active train, Greywall for the proxy dashboard, credential substitution, watch, and learning modes.
- [nono](../nono/index.md): the Sigstore team's broker fences each delegated tool separately and scopes credentials per endpoint; Greywall fences per invocation and swaps credentials at its proxy.
- [Drop](../drop/index.md): the namespace wrapper that keeps your installed distro, with an optional gVisor step-up; Greywall is lighter on the filesystem layer and adds the observability loop Drop lacks.
- [aigate](../aigate/index.md): the dormant fourteen-star reference in the same slot; Greywall is what that idea looks like with documentation and a dashboard.

## Bottom line

**Recommended for engineers who want to see what an agent actually reaches before fencing it, and who accept a stalled fork with no audit.**
Not for containing actively malicious code (its own docs say so), and not as the boundary for anyone who needs a maintained release train today, which points back to [Fence](../fence/index.md) or [OpenShell](../openshell/index.md).

## Changes

- 2026-10-08 - Created from the orchestration worker's cross-category flag, resolved this run: the Fence fork with proxy-held credential substitution and the watch-then-restrict workflow, its quiet-since-August state recorded.
- 2026-10-09 - Quiet window extended to fifty-seven days (last push still 2026-08-13); stars refreshed (309), forks and issues unchanged.

## See also

- [Fence](../fence/index.md) - the parent project Greywall forked from
- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [nono](../nono/index.md) - the per-tool broker on the same kernel primitives
- [aigate](../aigate/index.md) - the dormant small-scale reference in the same slot
- [OpenShell](../openshell/index.md) - the vendor-backed runtime when policy needs organizational weight

## References

- https://github.com/GreyhavenHQ/greywall - repository, README, fork attribution, agent profiles, platform table
- https://api.github.com/repos/GreyhavenHQ/greywall - stars, forks, issues, creation and push dates as of 2026-10-08
- https://api.github.com/repos/GreyhavenHQ/greywall/releases - the v0.3.3 through v0.3.7 release record ending 2026-06-01
- https://github.com/GreyhavenHQ/greyproxy - the companion proxy, MIT, the credential-substitution target
- https://docs.greywall.io/greywall/security-model - the semi-trusted-code threat model statement
- https://docs.greywall.io/greywall/platform-support - the per-OS enforcement matrix
- https://docs.greywall.io/greywall/credential-protection - the placeholder-substitution mechanism
- https://greywall.io - the project site
- https://hn.algolia.com/api/v1/search?query=greywall&tags=story - the near-zero Hacker News footprint (7, 1, and 3 points)
- https://www.wshoffner.dev/blog/greywall - the one independent review, 2026-03-30
