---
title: "Clawk"
created: 2026-09-05
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, vm, security]
readability: 3
audience_notes: >
  Engineers who let coding agents run commands and want the isolation story, especially on macOS workstations.
  Assumes you know what a VM, a network allow-list, and ssh-agent forwarding are.
---

**Clawk gives a coding agent a disposable Linux VM instead of your laptop, so the permission prompt disappears because the blast radius already did.**
Facts below verified as of 2026-09-05.

## What it is

An Apache-2.0 Go tool that wraps Claude Code, Codex, pi, or a plain shell inside a disposable Linux VM on macOS (Linux support is experimental): your repository is mounted in, the agent runs as root in the guest, and no permission prompts appear because the host is out of reach.
The boundary is a network allow-list that blocks connections to unknown servers, plus ssh-agent forwarding so `git push` still works and your private keys never enter the VM.
There is no Dockerfile or devcontainer: the first boot builds a rootfs from any OCI image you point it at, later boots take seconds, and `clawk destroy && clawk` rebuilds a wrecked VM while `--resume` restores the conversation.

## Status

Launched July 2026 with real traction and currently paused in a pre-1.0 state: 1,007 stars and 38 forks, last push 2026-08-13 at v0.4.0, with the README carrying its own "pre-1.0, expect breaking changes" banner.
**The 226-point Show HN thread is the strongest community signal in the Sandboxing category's tail, and the discussion plus the README agree on the limits rather than hiding them.**
Three weeks without a push after a fast launch cadence is worth watching, but it is not yet a stall at these timescales.

## Strengths

- The threat model is stated with unusual candor: the allow-list blocks unknown servers, not approved ones, and anything the agent can read is something it could publish, and the README says so in its own voice.
- One command to a working agent, no setup files, and destroy-rebuild-resume semantics that treat the VM as genuinely disposable.
- Secrets architecturally stay on the host, with only the forwarded agent socket crossing the boundary.

## Cautions

- The sandbox is only as closed as its allow-list: github.com is pre-allowed, so exfiltration through the very forge you push to is in scope by design.
- Pre-1.0 with three weeks of quiet as of 2026-09-05, on a single primary platform (macOS), from a small team.
- The VM disk is lost on destroy by design; only host-side code and conversations survive.

## Pricing

Free and open source under Apache-2.0; the only costs are the VM resources on your own machine.

## Compared to

- [OpenShell](../openshell/index.md): NVIDIA's runtime adds declarative policy and an inference proxy that keeps API keys out; heavier, backed, and Linux-first.
- [Agent Sandbox](../agent-sandbox/index.md): the Kubernetes answer for fleet-scale isolation where a per-workstation VM is the wrong layer.
- [Codex](../codex/index.md): the built-in kernel-sandbox baseline inside one harness, no VM and no cross-harness reach.

## Bottom line

Recommended for macOS engineers who want to stop approving every command without handing over the laptop, and who accept pre-1.0 churn.
Not for Linux-primary teams (yet), and not for anyone threat-modeling a determined exfiltration attempt through allowed domains.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - where the disposable-VM column sits among the isolation layers
- [OpenShell](../openshell/index.md) - the vendor-backed runtime comparison
- [Claude Code](../claude-code/index.md) - the most common agent wrapped inside clawk
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - the unattended runs that make isolation necessary

## References

- https://github.com/clawkwork/clawk - repository, security model and its limits, install, platforms
- https://github.com/clawkwork/clawk/releases - the v0.2.0 through v0.4.0 release history
- https://hn.algolia.com/api/v1/items/48892859 - the 226-point Show HN launch thread
- https://github.com/clawkwork/clawk#security-model-and-its-limits - the stated limits grounding the cautions
- https://github.com/clawkwork/clawk#compared-to - the project's own comparison grounding Compared to
