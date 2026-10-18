---
title: Landrun
created: 2026-10-09
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, landlock, linux, open-source]
readability: 3
audience_notes: >
  Engineers on Linux who want the kernel's own Landlock LSM around any command or coding agent and want to know what one primitive can and cannot enforce.
  Assumes you know what an LSM, a filesystem access rule, and a TCP bind restriction are.
---

Landrun is a MIT-licensed Go CLI that sandboxes any Linux command with the kernel's Landlock LSM alone, no root, no containers, and no namespaces, granting filesystem read, write, and execute paths plus TCP bind and connect ports and IPC scoping through command-line flags.

**Landrun is this category's smallest mechanism attached to one of its largest footprints, a single-primitive wrapper whose 518-point launch and Ubuntu and Debian packages made it the default answer to sandboxing a command on Linux, and its ceiling is exactly that single primitive.**

## What it is

`landrun --rox /usr --rw . -- <command>` starts the command inside a Landlock domain with everything denied except what the flags grant: `--ro`, `--rox`, `--rw`, and `--rwx` paths, `--bind-tcp` and `--connect-tcp` ports, and, on the newest ABI, IPC scoping for abstract UNIX sockets and signals plus per-path UNIX socket grants.
With no rules given it applies maximum restrictions, and no environment variable crosses unless `--env` names it, so secret-bearing variables stay behind the boundary by default.
The released v0.1.17 targets Landlock ABI v9 (filesystem, TCP since ABI v4 on kernel 6.7+, IPC scoping since v6, denial audit logging since v7), with `--best-effort` degrading gracefully on older kernels, and the main branch now targets ABI v10, adding UDP bind and connect restrictions with port ranges on kernels 7.2+, none of it released yet.
Installation is go install, and the project is packaged in the Arch AUR, Slackware, Ubuntu 26.04, and Debian forky.
MIT, by Zouuup (Zoup on Hacker News), with no agent-specific features: it is a general-purpose command sandbox.

## Status

Large footprint, development resumed: 2,316 stars as of 2026-10-13, 3 open issues as of 2026-10-18, created 2025-03-21, with v0.1.17 (2026-07-22, the ABI v9 release) the latest of a long 0.1.x train.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Zouuup/landrun&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Zouuup/landrun&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Zouuup/landrun&type=date&legend=top-left" />
</picture>
The Show HN of 2025-03-22, submitted by the author, drew 518 points, the largest community thread of any wrapper-class member of this category, and the same author publishes the project's sharpest caution himself.
**After eighty-five quiet days the train resumed: a merged community pull request targeting Landlock ABI 10 with UDP network restrictions committed 2026-10-10, followed by TCP and UDP port-range flags and a go-landlock v0.10.1 bump on 2026-10-16, none of it released past v0.1.17.**
The quiet stretch read as a stable utility rather than a stalled project, and the resumed work supports that reading, but the wrapper slot around it stays crowded with maintained, agent-specific members, so the footprint remains a 2025 event the repo is only now following up.

## Strengths

- Genuine kernel enforcement with zero dependencies: Landlock is in the kernel, so there is no daemon, image, or namespace stack to install.
- Deny-by-default done strictly: no rules means everything denied, and environment variables do not cross unless named, which quietly solves the env-var exfiltration path.
- The ABI v9 surface (TCP ports, IPC scoping, UNIX socket grants, denial audit logging) is the widest Landlock coverage shipped in a CLI in this category.
- Distribution reach no peer here matches: it is in Ubuntu's and Debian's archives, so it is the Landlock tool people already have installed.

## Cautions

- Landlock cannot see network content, only TCP ports, so there is no domain allowlist and no egress policy; anything that can reach port 443 can reach everything on it.
- No namespaces and no user separation: the sandboxed process runs as the invoking user against the same kernel, so a kernel exploit is out of scope, the same ceiling Fence and nono carry.
- The author's own post states binaries are not trustworthy and frames the tool as the answer to supply-chain authority; no independent audit or adversarial review exists.
- Flag-only policy with no config file, no agent profiles, and no audit trail of its own beyond Landlock's denial logs, so adopting it for agents means hand-writing every invocation.
- The latest release still dates to July 2026 while main already targets ABI 10, and the top launch reply's question, why not bubblewrap and mount namespaces, remains the comparison Landrun still has to answer.

## Pricing

Free and open source under MIT, no paid tiers.
The costs are the Linux 5.13+ kernel (6.7+ for TCP controls) and the flag discipline.

## Compared to

- [Fence](../fence/index.md): the maintained, agent-wired wrapper layering sandbox-exec, bubblewrap, Landlock, and seccomp with one policy file; choose Landrun for the pure kernel primitive, Fence for agent workflows.
- [Drop](../drop/index.md): builds a full namespace environment around your distro with an optional gVisor step-up; Drop when you want your environment kept, Landrun when you want one command fenced.
- [aigate](../aigate/index.md): the dormant reference wrapper that adds ACLs, namespaces, egress allowlists, and masking; aigate is the richer design, Landrun the one with the community and the packages.

## Bottom line

**Recommended as the Linux kernel primitive for fencing a single command or script, and as the base layer to understand before any agent wrapper.**
Not as an agent boundary by itself: no egress policy, no audit trail, no profiles, and a kernel shared with the sandboxed process.

## Changes

- 2026-10-09 - Created from the arjan/awesome-agent-sandboxes re-scan, profiling the Landlock-only kernel wrapper with the category's largest wrapper-class footprint and the author's own supply-chain caution.
- 2026-10-10 - Quiet window extended to seventy-nine days (last push still 2026-07-23); stars refreshed (2,315) and open issues to seven.
- 2026-10-11 - Quiet window extended to eighty days (last push still 2026-07-23); open issues moved from seven to eight, stars and forks unchanged.
- 2026-10-12 - Quiet window extended to eighty-one days (last push still 2026-07-23); stars refreshed (2,318), forks and issues unchanged.
- 2026-10-13 - Quiet window extended to eighty-two days (last push still 2026-07-23); stars refreshed (2,316), forks and issues unchanged.
- 2026-10-18 - Recorded the quiet window ending: a merged community pull request targeting Landlock ABI 10 with UDP network restrictions (committed 2026-10-10), then TCP and UDP port-range flags and a go-landlock v0.10.1 bump (2026-10-16), none released past v0.1.17, with open issues moving from eight to three.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Fence](../fence/index.md) - the maintained multi-primitive wrapper above the same Landlock layer
- [Drop](../drop/index.md) - the namespace environment with the gVisor step-up
- [aigate](../aigate/index.md) - the dormant richer-mechanism reference in the same slot
- [OpenShell](../openshell/index.md) - the vendor runtime that turns Landlock-style policy into organizational YAML

## References

- https://github.com/Zouuup/landrun - repository, README, distro packages, license
- https://raw.githubusercontent.com/Zouuup/landrun/HEAD/README.md - the flag reference, default-deny env behavior, and kernel requirements
- https://hn.algolia.com/api/v1/items/43445662 - the 518-point Show HN launch and the bubblewrap comparison in the top reply
- https://zoup.org/landrun-binaries-are-not-trustworthy/ - the author's own supply-chain authority argument, the critical source
- https://api.github.com/repos/Zouuup/landrun/releases/latest - the v0.1.17 Landlock ABI v9 release record
