---
title: NemoClaw
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, nvidia, openclaw, hermes, deep-agents, open-source]
readability: 3
audience_notes: >
  Engineers who want to run an always-on assistant (OpenClaw, Hermes, or LangChain Deep Agents) inside an OpenShell sandbox without assembling the integration themselves.
  Assumes you know what an inference proxy and a sandbox policy blueprint are.
---

NemoClaw is NVIDIA's Apache-2.0 reference stack that installs, hardens, and operates supported AI assistants (OpenClaw by default, plus Hermes and LangChain Deep Agents Code) inside OpenShell sandboxes, adding guided onboarding, managed inference, network policy, and lifecycle operations on top of the isolation boundary OpenShell enforces.

**NemoClaw is not another isolation boundary, it is the opinionated packaging of one: its versioned blueprint encodes a hardened image, stricter default policy, and credential custody so the assistant runtimes can be operated by people who never write a policy YAML file.**

## What it is

A TypeScript CLI (`nemoclaw`, with per-agent aliases such as `nemohermes` and `nemo-deepagents`) that installs OpenShell, part of NVIDIA's Agent Toolkit, and applies a selected agent integration layer plus a versioned blueprint whose digest is verified before use.
The docs position it precisely in a three-piece stack: OpenClaw is the assistant inside the container, OpenShell is the execution environment (sandbox lifecycle, filesystem, network, and process policy, inference routing), and NemoClaw is the host-side reference stack that orchestrates the other two.
Beyond the OpenShell community sandbox it strips build toolchains and network probes from the runtime image, applies a read-only system-path layout, filters sensitive host environment variables out of the sandbox build, creates provider entries automatically, and offers Balanced, Restricted, or Open policy presets.
Supported agents are OpenClaw (default), Hermes, and LangChain Deep Agents Code, with Pi as a release candidate; install is `curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash` or a starter prompt a local coding agent executes with per-command approvals.
Apache-2.0, from NVIDIA, which describes the project as alpha with best-effort maintainer review of issues and pull requests.

## Status

Large and fast for an alpha: 22,674 stars, 3,131 forks, 777 open issues and PRs as of 2026-10-07, created 2026-03-15, pushed 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=NVIDIA/NemoClaw&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=NVIDIA/NemoClaw&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=NVIDIA/NemoClaw&type=date&theme=dark&legend=top-left" />
</picture>

The launch carried it: a 385-point, 261-comment Hacker News thread on 2026-03-18, with the announcement submission the day before at 18 points.
**The release story is thinner than the star count: the repository held a single prerelease tag (`ci-native-podman-e2e-2026-10-01`) as of 2026-10-07, and the README still says alpha, so the seven months of growth measure attention, not a shipped 1.0.**

## Strengths

- Removes the integration work the OpenShell path demands: an onboarding wizard, express install profiles for DGX Spark, DGX Station, and Windows WSL, and host readiness reporting.
- Credential discipline end to end: provider keys stay at OpenShell's inference proxy, key-bearing host env vars are filtered from the build, and the one credential-collecting helper is digest-pinned and served through a loopback-only form.
- Hardened by default rather than by configuration: toolchains and `netcat` removed from the image, read-only system paths, process limits, network policy that grows with messaging and web-search choices.
- Ecosystem pull for the assistant world: [OpenClaw](../../assistant-runtimes/openclaw/index.md) and [Hermes](../../assistant-runtimes/hermes/index.md) get an NVIDIA-backed, policy-managed deployment path with messaging-channel onboarding.

## Cautions

- Self-declared alpha with best-effort support, and one prerelease tag as of 2026-10-07, so treat the API and blueprint format as moving.
- Choosing NemoClaw means choosing OpenShell: the blueprint is bound to one boundary, and the docs route custom images or non-reference workloads back to OpenShell alone.
- The primary install is `curl | bash`, and the headline onboarding flow asks a coding agent to drive system changes, a supply-chain-sensitive pattern whose digest pinning covers only the credential helper and form, not the installer.
- 777 open issues and PRs on a seven-month-old repository as of 2026-10-07, a support load NVIDIA reviews on a best-effort basis.

## Pricing

Free and open source under Apache-2.0, no paid tiers found as of 2026-10-07.
Costs are the host you run it on (a DGX box if you want the express paths) and the model tokens your assistant burns.

## Compared to

- [OpenShell](../openshell/index.md): the boundary underneath; choose OpenShell alone for custom images, your own policy layout, or a workload outside the reference stack, and NemoClaw for the packaged, hardened OpenClaw/Hermes/Deep Agents path.
- [Microsandbox](../microsandbox/index.md): the local-first embeddable runtime with agent-created sandboxes but no managed-inference custody; choose Microsandbox to embed isolation in a product, NemoClaw to operate a resident assistant.
- [Clawk](../clawk/index.md): the disposable per-agent VM for coding work sessions; NemoClaw targets always-on assistants rather than a workstation you rent out one session at a time.

## Bottom line

**Recommended for people running OpenClaw or Hermes who want NVIDIA's tested policy, inference routing, and onboarding instead of assembling OpenShell by hand, with alpha risk priced in.**
Not for production-critical assistants while the project declares alpha, or for anyone whose isolation boundary of choice is not OpenShell.

## Changes

- 2026-10-07 - Created from the daily-refresh entrant resolution, profiling NVIDIA's OpenShell reference stack with its blueprint hardening, managed-inference credential custody, and the single-prerelease release story.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the boundary NemoClaw packages and the alternative when you want to integrate it yourself
- [OpenClaw](../../assistant-runtimes/openclaw/index.md) - the default assistant this stack sandboxes
- [Hermes](../../assistant-runtimes/hermes/index.md) - the second supported assistant runtime

## References

- https://github.com/NVIDIA/NemoClaw - repository: supported agents, alpha status, community channels, current priorities
- https://docs.nvidia.com/nemoclaw/latest/ - documentation home: onboarding flow, agent selection, providers, credential helper, policy tiers
- https://docs.nvidia.com/nemoclaw/latest/about/ecosystem.html - the stack scope table and the NemoClaw-versus-OpenShell hardening comparison
- https://raw.githubusercontent.com/NVIDIA/NemoClaw/main/README.md - the README's supported-agent list, security process, and alpha description
- https://api.github.com/repos/NVIDIA/NemoClaw - stars, forks, issues, creation and push dates as of 2026-10-07
- https://api.github.com/repos/NVIDIA/NemoClaw/releases - the single prerelease tag record as of 2026-10-07
- https://hn.algolia.com/api/v1/items/47427027 - the 385-point launch thread of 2026-03-18, the largest of the NemoClaw submissions
