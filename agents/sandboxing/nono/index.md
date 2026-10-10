---
title: nono
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, security, kernel, open-source]
readability: 3
audience_notes: >
  Engineers who want an agent fenced at the kernel level and care most about what happens when the agent calls git, gh, curl, or kubectl.
  Assumes you know what Landlock, seccomp, and an L7 proxy are.
---

nono is a capability-based sandbox CLI and SDK family from nolabs-ai, the team behind Sigstore, that sandboxes an AI agent session at the kernel level and, distinctively, launches each delegated tool the agent calls under its own command sandbox with separate filesystem, network, and credential policy.

**nono's design point is that the agent's session sandbox is not enough: each delegated tool gets its own sandbox, so git sees only the repo and git config, gh receives a token through a credential proxy scoped to selected API methods and paths, and the agent can widen none of it from inside its session.**

## What it is

A Rust core with an installable CLI (curl script, Homebrew, Nix flake) plus Go, TypeScript, and Python SDKs over FFI, so the same policies can gate an agent harness or an application's own LLM calls.
The session sandbox uses kernel primitives, and the broker wraps each controlled tool in a command policy of its own: the tool does not inherit the session's broad grants, working-directory access, raw credential paths, or network access unless its profile says so.
Profiles can chain policies (git may call ssh under a chained policy while direct ssh from the agent stays denied) and route credentials through an L7-filtering proxy that enforces which API methods and paths a token may touch.
The project also advertises an immutable cryptographic audit chain and atomic rollback, and the registry namespace moved from `always-further` to `nolabs-ai` in the run-up to 1.0.
Apache-2.0, built by the Sigstore team, with an OpenSSF Best Practices badge and testimonials from staff and principal security engineers at Datadog and Okta on the README.

## Status

Fast-growing with no Hacker News help: 4,408 stars, 241 open issues and PRs, pushed 2026-10-05 as of 2026-10-09, created 2026-01-31.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=nolabs-ai/nono&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=nolabs-ai/nono&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=nolabs-ai/nono&type=date&theme=dark&legend=top-left" />
</picture>

The release train is active and pre-1.0: v0.77.0 on 2026-09-11, v0.78.0 on 2026-09-16, and v0.79.0 on 2026-09-30, with the README carrying an APIs-are-stabilizing note ahead of a 1.0.
**Hacker News never embraced it: four submissions between 2026-02-01 and 2026-02-04 drew 4, 1, and 2 points, an August resubmission drew 3, and the stars grew without a front-page thread, so the evidence base is the repo, the docs, and named enterprise testimonials rather than public debate.**

## Strengths

- The finest-grained policy model in this category: per-tool command sandboxes with chained policies, rather than one blanket agent sandbox.
- The credential proxy answers key exfiltration per endpoint, which is stricter than vaults that inject a whole key.
- Credible security pedigree (the Sigstore team) plus an OpenSSF badge and a stated audit chain.
- SDK surface (Go, TypeScript, Python, Rust core) means the policies are callable from product code, not just a terminal.

## Cautions

- Pre-1.0 with an explicit API-change warning, and the namespace migration (`always-further` to `nolabs-ai`) is churn early adopters must handle.
- Kernel-primitive isolation shares the host kernel; there is no VM or gVisor tier, so a kernel exploit is out of scope for this boundary.
- No independent audit or adversarial write-up exists that I could find, and the HN footprint is four near-zero threads.
- The marketing register on the README ("pioneered the zero-latency, zero-setup agent sandbox", "copied by many") is self-assessment, not evidence.

## Pricing

Free and open source under Apache-2.0, no paid tiers or hosted offering found as of 2026-10-07.

## Compared to

- [OpenShell](../openshell/index.md): NVIDIA's runtime adds container and MicroVM boundaries and holds model keys at an inference proxy; nono stays at kernel primitives but scopes every tool's credentials per endpoint, so choose OpenShell for VM strength, nono for delegation control.
- [Drop](../drop/index.md): the namespace wrapper that keeps your host distribution with no per-tool brokering; simpler, and its threat model stops at the session boundary.
- [Fence](../fence/index.md): the other OS-primitives CLI; Fence applies one policy per invocation, while nono brokers each delegated tool separately and proxies its credentials.

## Bottom line

**Recommended for engineers whose main fear is the agent misusing the tools it delegates to, and who want per-tool, per-endpoint credential policy from a team with a security track record.**
Not for anyone who needs VM-grade boundaries today or an externally audited 1.0.

## Changes

- 2026-10-07 - Created from the entrant-resolution run, profiling the Sigstore team's per-command sandbox broker with its credential proxy and the no-HN-growth finding.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the VM-backed policy runtime with the model-key proxy
- [Fence](../fence/index.md) - the invocation-level sibling using the same OS primitives
- [Drop](../drop/index.md) - the session-scoped namespace alternative

## References

- https://github.com/nolabs-ai/nono - repository, mechanism, testimonials, OpenSSF badge, namespace-migration notice
- https://docs.nono.sh/ - the CLI, Rust core, and Go/TypeScript/Python SDK surface
- https://api.github.com/repos/nolabs-ai/nono - stars, open issues, creation and push dates as of 2026-10-07
- https://api.github.com/repos/nolabs-ai/nono/releases - the v0.77.0 through v0.79.0 release record
- https://hn.algolia.com/api/v1/items/46849615 - the 4-point Show HN of 2026-02-01, the largest of four near-zero threads
