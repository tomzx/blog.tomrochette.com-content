---
title: Flue
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, agent-frameworks, typescript, open-source]
readability: 3
audience_notes: >
  TypeScript engineers building durable agents who want sandbox choices designed into the framework.
  Assumes you know what a runtime sandbox adapter and durable execution are.
---

Flue is the Astro team's open-source TypeScript agent framework, pitched as the sandbox agent framework, where agents are React-style hook functions that run against pluggable sandboxes, from an in-memory virtual shell to remote provider VMs, with durable sessions that survive crashes and redeploys.
Facts below verified as of 2026-09-04.

**Flue's contribution to this category is a taxonomy, not a boundary: a documented three-tier sandbox model (virtual, local, remote) that names the trade every agent builder was making implicitly, and it will consume a sandbox like [OpenShell](../openshell/index.md) rather than replace one.**

## What it is

An agent harness where a `'use agent'` function composes capabilities through hooks: `useModel`, `useSandbox`, `useTool`, `useSkill`, `usePersistentState`, `useSubagent`, `useMcpConnection`, so an agent's tools attach conditionally and evolve mid-conversation.
Three sandbox tiers: an in-memory virtual sandbox (emulated bash and filesystem, no process spawned, opt-in network), a `local()` host sandbox with no isolation by design and an explicit env allowlist, and remote provider sandboxes via adapters for Daytona, E2B, Modal, and Cloudflare.
Sessions are durable streams addressable over HTTP, with channels for Slack, Teams, Discord, and GitHub, OpenTelemetry observability, and deploys to Node, Cloudflare Workers, GitHub Actions, and Docker.
Built on Pi for model providers, Vite for builds, Hono for routing; Apache-2.0, Node 22.19+.
Made by the Astro Technology Company team under Fred Schott, acquired by Cloudflare in January 2026, $7M seed background.

## Status

Young and fast: 8,118 stars, 477 forks, 42 open issues and PRs as of 2026-09-02, created 2026-02-07, 1,061 commits.
Flue 2.0 (2026-07-31) is the first stable release after a ground-up hooks rewrite; npm `@flue/runtime` 2.0.3 on 2026-08-05, no GitHub Releases.
**The single-author concentration is stark, about 98 percent of commits, and the API was rebuilt within six months of going public.**

## Strengths

- Production-dogfooded: it powers the triagebot that cut Astro's issue backlog from 200+ to about 20, open-sourced and documented.
- The three-tier sandbox model with sensible defaults (env allowlists, opt-in network, narrowest-environment guidance) is the clearest in the category.
- Durable execution is real: sessions survive crashes and redeploys, with per-conversation HTTP addressability.
- Credible stewardship under the Astro and Cloudflare umbrella with explicit no-lock-in goals.

## Cautions

- Single-author risk on nearly every commit.
- Hacker News commenters flagged test absence and asked what it solves that building it yourself does not.
- The 1.0 beta API was abandoned for a hooks rewrite, so expect further breaking change.
- `local()` gives agents your real host shell by design, so the framework is not an isolation boundary; security is entirely the adapter's job.

## Pricing

Free and open source under Apache-2.0, self-hosted, no paid tiers found.
Costs are your model keys and whatever remote sandbox provider you attach.

## Compared to

- [OpenShell](../openshell/index.md): the execution-environment layer with kernel enforcement; Flue sits a layer up and would consume it through an adapter.
- [agent-sandbox](../agent-sandbox/index.md): cluster-scale CRD management of sandbox pods; Flue offers no cluster-scale management but can target such infrastructure.
- Plain Docker plus hand-rolled plumbing: right when you only need a container; Flue pays off when you want durability, hooks, skills, MCP, and channels around it.

## Bottom line

**Recommended for TypeScript teams building long-lived agents who want sandbox semantics and durability as framework features rather than projects.**
Not for anyone needing the framework itself to be the security boundary, or betting on API stability in the first year after a rewrite.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the isolation layer Flue would adapt to
- [Pi](../pi/index.md) - the provider toolkit under Flue's model layer
- [agent-sandbox](../agent-sandbox/index.md) - the cluster-scale counterpart

## References

- https://github.com/withastro/flue - repository, hook model, packages, license
- https://flueframework.com/blog/flue-2/ - the 2.0 rewrite and first stable release
- https://flueframework.com/docs/guide/sandboxes/ - the three-tier sandbox model grounding this note
- https://news.ycombinator.com/item?id=47988501 - the skeptical thread on tests and value
- https://www.cloudflare.com/press/press-releases/2026/cloudflare-acquires-astro-to-accelerate-the-future-of-high-performance-web-development/ - the acquisition behind the stewardship
- https://thenewstack.io/cloudflare-astro-triage-bot/ - the production dogfooding evidence
