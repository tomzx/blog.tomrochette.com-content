---
title: aicontainer
created: 2026-10-12
updated: 2026-10-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, devcontainer, containers, isolation, open-source]
readability: 3
audience_notes: >
  Engineers who run Claude Code, Codex, or OpenCode in auto-approve mode across
  several projects and want the dev container they already use to act as the boundary.
  Assumes you know what the devcontainer specification and the Docker socket are.
---

aicontainer is an MIT devcontainer-spec CLI that runs Claude Code, Codex, and OpenCode in bypass mode inside a per-project dev container, with the Docker socket proxied, host config sanitized, and nothing from your home mounted.

**It is the only member of the category that treats the Docker daemon itself as part of the threat model: by default the agent reaches it through a digest-pinned socket proxy exposing nothing but ping and version.**

## What it is

An npm-distributed CLI (`aic`, package aicontainer, bundled with @devcontainers/cli) that generates and maintains a `.devcontainer` per project and manages the agent's life inside it: `aic init`, `aic up`, `aic shell`, `aic sync`, and a `aic preflight` that prints the exact boundary for your actual config.
The boundary table answers, per surface, what crosses: the project directory read-write (with `.devcontainer/` and the repo's git control files read-only), host home and `.ssh` never, credentials never auto-forwarded (you log in once inside the container), and host git, Claude, Codex, and OpenCode config reduced to a fixed set of safe fields by a root-only, networkless one-shot sanitizer before the agent sees them.
An always-on block covers IPv4 and IPv6 link-local and common cloud-metadata endpoints; outbound network is otherwise open unless you opt in to the allowlist; a PreToolUse hook stops the agent from reading `.env` files; session transcripts persist in a path-unique per-project volume.
Solo author (Stefano Ginella), first published 2026-05-22, positioned by its own README as the same design as Trail of Bits's claude-code-devcontainer with Codex and OpenCode added, three explicit Docker-access modes, and managed shell startup.

## Status

The thinnest footprint in the category's admitted set after aigate: 21 stars as of 2026-10-16, solo author, created 2026-05-22, pushed 2026-10-14, MIT.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=stefanoginella/aicontainer&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=stefanoginella/aicontainer&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=stefanoginella/aicontainer&type=date&legend=top-left" />
</picture>

npm carries 0.12.1 (2026-10-14) after 0.12.0 and 0.11.0 the two days before, ending six weeks at 0.9.1, with 505 downloads in the trailing month (2026-09-13 to 2026-10-12), and I found no Hacker News thread for the project.
The 0.12 pair hardens the boundary further (root processes inside the container no longer search agent-writable PATH directories or write history to the shared volume) and fixes the agent-status relay behind the firewall.
Development is active to a degree the star count hides: commits landed through 2026-10-11, and the messages document threat-model reasoning (a probe that fails closed against Node-manager shims, an npm 12 packaging fix) in unusual detail.
**Twenty-one stars is a missing-community-footprint signal by the category's own standard, carried here by boundary documentation that reads like an audit candidate rather than by adoption.**

## Strengths

- The socket proxy: a digest-pinned Tecnativa docker-socket-proxy leaves only ping and version reachable by default, with `--docker-read` and `--docker` opting into sensitive APIs, so a container escape cannot drive the host daemon.
- The boundary is printed, not promised: `aic preflight` states what crosses for your actual config, and the same table renders after every `aic up`.
- The config sanitizer: host agent and git config pass through a root-only, networkless one-shot that strips inline credentials, MCP env and headers, and security-policy fields.
- Devcontainer-spec native: the boundary lives in the `.devcontainer/` your editor already understands, so VS Code's Reopen in Container workflow and the devcontainer toolchain apply unchanged.

## Cautions

- Twenty-one stars and 505 npm downloads a month: no community review has happened, and the solo maintainer is a bus factor of one.
- Outbound network is mostly open by default; the allowlist that restricts it is opt-in, which the README itself flags as the row most worth your attention.
- The `.env` block is a tool-layer hook, defense-in-depth rather than a filesystem guarantee, and a bypass-mode CLI that ignores hooks defeats it.
- The container boundary shares the host kernel, with no audit and no independent discussion of the claims.

## Pricing

Free and open source under MIT; the costs are Docker host resources and image builds.
No hosted tier or pricing page exists as of 2026-10-12.

## Compared to

- [Yolobox](../yolobox/index.md): the container wrapper with full sudo and an unmounted home; Yolobox is simpler, aicontainer adds socket proxying, config sanitizing, and the printed boundary table.
- [Container Use](../container-use/index.md): agent-created environments on their own branches for parallel work; aicontainer is one fixed dev environment per project.
- [Fence](../fence/index.md): the OS-native wrapper that needs no Docker at all; choose Fence when containers are the overhead you are avoiding.

## Bottom line

**Recommended for VS Code-centered engineers who want auto-approve CLIs across many projects with the Docker daemon and host config explicitly handled, and who will read the threat model themselves.**
Not for anyone needing a kernel or VM boundary, an audited isolation claim, or a project with a community behind it.

## Changes

- 2026-10-12 - Created from the 2026-10-12 awesome-claude-code scan, profiling the devcontainer-spec entrant with the socket-proxy boundary recorded as the distinguishing mechanism and the thin footprint recorded as the signal.
- 2026-10-13 - Recorded the release train resuming: npm 0.10.0 (2026-10-12) and 0.11.0 (2026-10-13) after six weeks at 0.9.1, with trailing-month downloads moving from 401 to 505.
- 2026-10-16 - Recorded 0.12.0 and 0.12.1 (both 2026-10-14), the root-PATH and root-history hardening fixes and the firewalled agent-status relay repair, with the star count refreshed to twenty-one.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Yolobox](../yolobox/index.md) - the other container-boundary member, coarser but more adopted
- [Container Use](../container-use/index.md) - the container boundary in its agent-created, per-branch form
- [aigate](../aigate/index.md) - the other small-footprint member kept for its reference design

## References

- https://github.com/stefanoginella/aicontainer - repository, README boundary table, threat model references, Docker-access modes, 20 stars, dates, license, as of 2026-10-12
- https://registry.npmjs.org/aicontainer - the npm package record, latest 0.12.1 (2026-10-14)
- https://api.npmjs.org/downloads/point/last-month/aicontainer - 401 trailing-month downloads (2026-09-11 to 2026-10-10)
- https://containers.dev/ - the devcontainer specification the project implements
- https://github.com/trailofbits/claude-code-devcontainer - the Trail of Bits devcontainer the README names as adjacent work, 951 stars
- https://hn.algolia.com/api/v1/search?query=aicontainer&tags=story - no dedicated thread (2026-10-12), the footprint record
