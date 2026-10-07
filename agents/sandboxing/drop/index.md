---
title: Drop
created: 2026-09-29
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, linux, open-source]
readability: 3
audience_notes: >
  Engineers on Linux who want OS-enforced isolation around coding agents and third-party programs without containers or virtual machines.
  Assumes you know what a user namespace, a mount namespace, and gVisor are.
---

Drop is Jan Wrobel's Apache-2.0, Go-based Linux sandbox that wraps any program or coding agent in a rootless environment built from your existing distribution: user, mount, PID, IPC, cgroup, and network namespaces plus dropped capabilities, with optional gVisor underneath and pasta networking that denies localhost services by default.

**Drop's bet is that isolation should not cost you your environment: it sandboxes inside the distribution you already run, no images and no VM required, and a 193-point launch says the gap between the thin wrappers and the VM tools was real.**

## What it is

A single prebuilt binary with a virtualenv-style workflow: `drop init` creates an environment with a TOML config, `drop run` starts a sandboxed shell in it, and environments are disposable while a shared `base.toml` means you configure once and spawn freely.
The sandbox gets its own writable home directory while the original home is hidden, selected files and directories mount read-only, the current working directory is read-write with `.git` read-only, and your username is preserved, so every program you already installed just works.
Underneath it uses your existing distribution rather than an image: namespaces isolate the process tree, all capabilities drop before exec so the sandboxed program cannot do privileged operations even within its own user namespace, and a mount namespace rearranges the root filesystem to hide the host.
Networking runs through pasta with access to localhost services denied by default, and an optional gVisor mode stops sandboxed programs from issuing syscalls to the host kernel directly.
The docs pitch two use cases: coding agents run with `--dangerously-skip-permissions` so a hallucinated `rm -rf ~` or a prompt injection hunting `~/.ssh` finds nothing, and third-party installs from PyPI or npm contained the way a supply-chain compromise deserves.
Install is a curl of a release binary for amd64 or arm64 plus the passt/pasta package, with documented AppArmor configuration for Ubuntu 24+ and SELinux configuration for Fedora.

## Status

Young tool, older project, one strong launch: 375 stars, 12 forks, 6 open issues as of 2026-10-06, created 2025-07-25, pushed 2026-10-02, latest release v0.3.0 on 2026-09-29.

[![Star History Chart](https://api.star-history.com/chart?repos=wrr/drop&type=date&legend=top-left)](https://www.star-history.com/?repos=wrr%2Fdrop&type=date&legend=top-left)

The Show HN thread on 2026-09-22 drew 193 points with substantive comparisons to bubblewrap and proot in the top replies.
v0.3.0 added a `drop edit` command for the TOML config, a reorganized documentation site at droprun.sh/docs/, and base.toml defaults for uv, pipx, go install, and Cargo that expose host-installed packages read-only while sandbox-only installs stay contained.
**The repository sat for fourteen months before the launch found it its audience, so the traction is one good Hacker News day, not a community, and the maintainer list is one person.**

## Strengths

- Keeps the working environment intact: host distro, installed tools, and username all survive the boundary, which neither a container nor a VM manages.
- A real kernel boundary by default: six namespace types plus a full capability drop, with gVisor one flag away when the threat model warrants a user-space kernel.
- Sensible defaults aimed at exactly this category's threats: localhost denied, `.git` read-only, home hidden, `~/.ssh` nonexistent.
- The TOML base-plus-override config makes per-project policy cheap instead of per-invocation flags.

## Cautions

- Pre-1.0 (v0.3.0), solo-maintained, and fourteen months old with a community measured in one launch thread.
- Namespace isolation shares the host kernel unless gVisor is enabled, which is the difference between containing a confused agent and containing a kernel exploit.
- Distro hardening is on you: Ubuntu 24+ needs an AppArmor profile change and Fedora an SELinux one, and skipping either weakens the setup.
- Linux-only (amd64 and arm64), with no macOS story at all, the opposite bet from Clawk.

## Pricing

Free and open source under Apache-2.0; the only costs are the pasta dependency and the machine you run it on.

## Compared to

- [aigate](../aigate/index.md): the other wrapper-style column, but maintained, documented, and launched; choose aigate only as a reading exercise, Drop for actual use.
- [Clawk](../clawk/index.md): trades the VM for namespaces, so Drop is lighter and keeps your Linux distro while Clawk is macOS-first and fully isolated.
- [OpenShell](../openshell/index.md): NVIDIA's runtime adds declarative egress policy and credential interception at an inference proxy; Drop hides the filesystem and blocks localhost but has no L7 policy layer, so pick OpenShell for organizational policy, Drop for a personal workstation.
- [Agent Sandbox](../agent-sandbox/index.md): the Kubernetes answer when these workstation sandboxes need to become governed fleet infrastructure.

## Bottom line

**Recommended for Linux developers who want their coding agent fenced in by the kernel without giving up their installed environment, with gVisor enabled when the work is untrusted.**
Not for macOS, and not as a hardened boundary for hostile code until the solo-maintainer risk and the missing audit are priced in.

## Changes

- 2026-09-29 - Created from the entrant-resolution run, profiling the rootless namespace sandbox that uses the host distribution.
- 2026-10-02 - Recorded the v0.3.0 release of 2026-09-29 (drop edit command, reorganized docs site, package-manager base.toml defaults) and refreshed counts (350 stars, 5 open issues, pushed 2026-09-29).
- 2026-10-07 - Added the wrr/drop star history chart to the Status section.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the vendor-backed policy runtime comparison
- [Clawk](../clawk/index.md) - the disposable-VM alternative on macOS
- [aigate](../aigate/index.md) - the tiny kernel-wrapper prior art

## References

- https://droprun.sh - the project site, its two use cases, and the mechanism summary
- https://github.com/wrr/drop - repository, README, license, adoption numbers
- https://raw.githubusercontent.com/wrr/drop/HEAD/README.md - the quick start, sandbox overview, and per-distro hardening requirements
- https://droprun.sh/docs/sandbox-overview - the filesystem layout and isolation documentation
- https://hn.algolia.com/api/v1/items/49801329 - the 193-point Show HN launch thread
