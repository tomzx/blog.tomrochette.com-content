---
title: Fence
created: 2026-10-07
updated: 2026-11-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, security, cli, open-source]
readability: 3
audience_notes: >
  Engineers who want one tool-agnostic policy file around semi-trusted commands and coding agents, using the operating system's own sandboxing primitives.
  Assumes you know what sandbox-exec, bubblewrap, and Landlock are.
---

Fence is an Apache-2.0 CLI from Tusk that wraps any command or coding agent in a container-free OS-native sandbox, sandbox-exec on macOS and bubblewrap plus Landlock and seccomp on Linux, blocking network access by default and restricting filesystem writes under one tool-agnostic fence.json policy.

**Fence's bet is that a single policy file and the operating system's own primitives beat per-agent permission settings, and its maintainer states the limit plainly on launch day: reads are allow-by-default, so this is defense-in-depth for semi-trusted code, not a boundary against a determined attacker.**

## What it is

`fence <command>` runs the command with network blocked by default (a plain curl returns 403), allow-list templates for common needs (a `code` template opens npm, PyPI, and similar), command deny rules (rm -rf, and friends), and filesystem write restrictions, with an audit trail of what was blocked.
One fence.json applies to anything you run through it: npm install, claude, codex, make test, or bash, which is the tool-agnostic property harness built-ins cannot offer.
It doubles as a permission manager for coding agents, with documented wiring for Claude Code, Codex, Amp, Gemini CLI, GitHub Copilot, OpenCode, and Factory's Droid CLI, plus agent hooks and an import path from Claude Code's own settings.
The docs include a security model, Linux security features, and the bubblewrap mount sequence, unusual transparency for a 0.x tool.
Built by Tusk, the AI testing-agents company; the repository moved from Use-Tusk/fence to fencesandbox/fence, and Homebrew installs from the new location.

## Status

Quiet on main since September after a long steady run: 40 open issues, main's newest commit 2026-09-10, the repo-level pushes through 2026-11-10 dependency PRs and branch activity rather than maintainer commits, created 2025-12-18, with v0.1.67 (2026-09-01) still the newest of thirty releases and 992 stars as of 2026-10-16.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=fencesandbox/fence&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=fencesandbox/fence&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=fencesandbox/fence&type=date&legend=top-left" />
</picture>

The 78-point Show HN of 2026-01-20 is the community anchor, with the maintainer answering limit questions in the thread.
**A steady 0.1.x cadence that ran thirty releases deep has now stalled: no commit to main since 2026-09-10 and no release since v0.1.67 on 2026-09-01, with the October and November activity limited to dependency PRs and community contributions, and the organization rename remains a second churn event early adopters had to follow.**

## Strengths

- OS-native primitives mean the repo, tools, and environment stay intact, no images and no VMs, matching how agents actually work.
- Deny-by-default network and writes are the right defaults for the agent threat, with allow-list templates instead of raw flag soup.
- One policy file covers every agent and every command, which is the property that makes it cheaper than per-harness permission settings.
- The docs publish the security model and the Linux mount sequence, and the maintainer engages with limits in public.

## Cautions

- Reads are allow-by-default by the maintainer's own account, so a process running under Fence can still read what it can see; the stated target is semi-trusted code, not active attackers.
- macOS enforcement rides on sandbox-exec, which Apple has deprecated, the same exposure aigate carries.
- No VM or gVisor tier: the boundary shares the host kernel, so kernel exploits are out of scope.
- 0.x versioning after ten months, a recent organization rename, and no independent audit.

## Pricing

Free and open source under Apache-2.0, no paid tiers found as of 2026-10-07.
Fence is a standalone project from Tusk; the costs are local only.

## Compared to

- [nono](../nono/index.md): the Sigstore team's broker adds per-tool command sandboxes and per-endpoint credential proxies on the same class of kernel primitives; choose Fence for one simple invocation policy, nono for delegation-level control.
- [Drop](../drop/index.md): keeps your installed distribution inside a namespace environment with an optional gVisor step-up; Fence stays closer to per-command restriction without environment isolation.
- [aigate](../aigate/index.md): the dormant fourteen-star prior art in the same slot; Fence is the longer-maintained version of roughly this idea, though its train has quieted since September 2026.

## Bottom line

**Recommended for engineers who want one policy file to fence semi-trusted installs, scripts, and coding agents on macOS or Linux without containers.**
Not for containing actively malicious processes, and not on hosts where deprecated sandbox-exec is a compliance problem.

## Changes

- 2026-10-07 - Created from the entrant-resolution run, profiling Tusk's OS-native command sandbox with the maintainer's allow-by-default-reads limitation as the anchor caution.
- 2026-10-17 - Fixed the star-history picture block, whose light-scheme source and fallback carried the dark theme parameter (rotation re-verification; every cited URL re-fetched, v0.1.67 still the newest release).
- 2026-10-25 - Rotation re-verification: every cited URL re-fetched and alive (repository, docs site, the API records, the Show HN thread); v0.1.67 (2026-09-01) remains the newest of thirty releases, the main branch last moved 2026-10-14, and the boundary claims, agent support list, and the maintainer's allow-by-default-reads answers re-verified unchanged.
- 2026-11-07 - Out-of-rotation re-verification correcting the activity reading: the earlier main-last-moved-2026-10-14 claim had read the repo-level push instead of the default branch, whose newest commit is 2026-09-10, so the train has been quiet for eight weeks with the 2026-10-14 and 2026-11-03 pushes being dependency PRs (closed unmerged) and community PRs, v0.1.67 (2026-09-01) still the newest of thirty releases, and every cited URL re-fetched and alive (repository, docs site, the API records, the Show HN thread); the maintainer remains active on issues, and the Status reading moved from actively maintained to quiet-on-main watch.
- 2026-11-12 - Volatile refresh: the 2026-11-10 repo-level push checked and still branch activity (main's newest commit stays 2026-09-10), so the quiet-on-main watch reading holds with v0.1.67 (2026-09-01) still the newest release.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [nono](../nono/index.md) - the per-tool broker on the same kernel primitives
- [Drop](../drop/index.md) - the namespace environment alternative on Linux
- [aigate](../aigate/index.md) - the dormant reference design in the same slot

## References

- https://github.com/fencesandbox/fence - repository, README, organization-move notice, agent support list
- https://fencesandbox.com/docs - the introduction, mechanism (sandbox-exec, bubblewrap, Landlock, seccomp), and docs structure
- https://api.github.com/repos/fencesandbox/fence - stars, open issues, creation and push dates as of 2026-10-07
- https://api.github.com/repos/fencesandbox/fence/releases - the v0.1.67 release record
- https://hn.algolia.com/api/v1/items/46695467 - the 78-point Show HN of 2026-01-20, including the maintainer's reads-allow-by-default answers
