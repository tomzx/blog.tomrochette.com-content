---
title: Yolobox
created: 2026-10-09
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, containers, docker, isolation, open-source]
readability: 3
audience_notes: >
  Engineers who want to run coding agents in full-permission yolo mode inside a container instead of approving every command, and want the boundary stated plainly.
  Assumes you know what a Docker volume mount and a container escape are.
---

Yolobox is Finbarr's MIT-licensed CLI that runs coding agents (Claude Code, Codex, Kimi Code, Gemini, Antigravity, OpenCode, Copilot, Pi, or any command) inside a Docker container where the agent has full sudo, the project is mounted at the same path it has on the host, and your home directory is not mounted at all.

**Yolobox trades the permission prompt for a container wall: the agent gets root in the box while your home stays home, and its own security model draws the line at accidents, not attackers.**

## What it is

`yolobox claude` (or `codex`, `gemini`, `kimi`, `agy`, `antigravity`, or a bare command) starts a container running as a sudoer user with the current project mounted at its host path, so absolute-path tooling and sessions survive, while SSH keys, dotfiles, cloud configs, and unrelated projects stay invisible unless you opt in.
Persistent named volumes keep installed tools and session state across runs, `--exclude` and `--copy-as` narrow what the agent sees of the project, and network access is on unless you turn it off.
Claude, Codex, and Kimi Code get built-in yolobox guidance so the agent understands the sandbox it is running in, a small touch no other member of this category ships.
Install is Homebrew or an install script; the trust boundary is the container runtime itself, per the docs' Security Model page.
MIT, solo author (Finbarr), docs at yolobox.dev.

## Status

Young and shipping hard: 650 stars, pushed 2026-10-07 as of 2026-10-09, created 2026-01-09, with thirty releases on the train and v0.19.7 (2026-10-07) the latest.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=finbarr/yolobox&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=finbarr/yolobox&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=finbarr/yolobox&type=date&legend=top-left" />
</picture>
The Show HN of 2026-01-12, submitted by the author, drew 122 points, and the replies compare it with Apple's container framework and point to neighbors rather than finding holes.
**A release every few days since January with no 1.0 and no audit says the tool works and the boundary is exactly as strong as your container runtime, which the project says itself.**

## Strengths

- The least-ceremony yolo-mode workflow in the category: one command per agent, state that persists, and nothing in home reachable by default.
- The Security Model page states what the container does and does not protect in plain lists instead of marketing.
- Same-path mounting keeps sessions and absolute-path tools continuous, which VM and namespace alternatives break.
- Built-in guidance for the three major agents about their own sandbox is unique here and reduces the confused-agent failure mode.

## Cautions

- Container-grade boundary only: kernel exploits, container escapes, and a deliberately hostile agent are out of scope by the project's own docs, which tell you to move up to stronger isolation for hostile code.
- The project directory is mounted read-write and network is on by default, so exfiltration through the repo and the open network is in scope.
- Docker is a workstation dependency, and on macOS the boundary doing the work is the VM layer under Docker, not the container.
- Credentials in dotfiles are safe by default, but anything the agent legitimately needs, a project .env or mounted secret, crosses into root-equivalent reach.
- Pre-1.0 with a near-daily release train, one maintainer, and no independent audit.

## Pricing

Free and open source under MIT; the costs are Docker, disk, and the images you pull.

## Compared to

- [Clawk](../clawk/index.md): the VM answer on macOS with a stronger boundary and a quieter train; Clawk for full machine isolation, Yolobox for the maintained container path.
- [Drop](../drop/index.md): keeps your installed distro behind namespaces with no container and an optional gVisor step-up; Drop for staying in your environment, Yolobox for full-sudo workflows.
- [Fence](../fence/index.md): deny-by-default per command without containers; Fence when the agent should have less, Yolobox when the agent should have everything inside a wall.

## Bottom line

**Recommended for engineers who want to stop approving every command and accept container-grade isolation with their home directory kept out.**
Not for hostile code, by its own docs, and not on hosts where Docker is unavailable or noncompliant.

## Changes

- 2026-10-09 - Created from the arjan/awesome-agent-sandboxes re-scan, profiling the container wrapper for full-permission agent runs with the docs' accidents-not-attackers ceiling.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Clawk](../clawk/index.md) - the disposable-VM alternative with a stronger boundary
- [Drop](../drop/index.md) - the namespace environment that keeps your distro
- [OpenSandbox](../opensandbox/index.md) - the platform-grade container boundary for teams
- [Brig](../brig/index.md) - the microVM step-up when container escape is the fear

## References

- https://github.com/finbarr/yolobox - repository, README, agent shortcuts, install
- https://yolobox.dev - the docs site and the problem-and-solution framing
- https://yolobox.dev/security - the Security Model page: trust boundary, protects and does-not-protect lists, trust-expanding flags
- https://hn.algolia.com/api/v1/items/46592344 - the 122-point Show HN launch
- https://api.github.com/repos/finbarr/yolobox/releases - the thirty-release train to v0.19.7 (2026-10-07)
