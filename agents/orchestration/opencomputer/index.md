---
title: OpenComputer
created: 2026-11-27
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, orchestration, slack, cloud-agents, open-source, devin-alternative]
readability: 3
audience_notes: >
  Engineers whose team hands coding work to a cloud agent from Slack and wants the stack to run in the company's own cloud account.
  Assumes you know what Slack app mentions are, what a rootless container is, and that Claude Code and Codex are CLIs you can bring your own subscription to.
---

OpenComputer is Digger's Apache-2.0, self-hostable cloud coding agent: mention `@Computer` in a Slack thread and it runs Claude Code, Codex, or OpenCode on a cloud Linux machine in your cloud account or the vendor's, then opens a pull request.

**It has no agent of its own; the product is the computer the harness runs on, one always-on VM per team with a session container per Slack thread, and that choice, not the harness, is what its speed claims rest on.**

## What it is

A single VM per organization runs the gateway (Calvin, a bridge that listens for Slack events) and one rootless Podman container per session, writing state to local disk first and then to a git-backed store, while the rest of the stack (Slack events, dashboard, API) runs on Cloudflare Workers and Durable Objects.
You hand it work by Slack mention or by API, from a web dashboard or CLI, and every thread gets its own copy of the repos on its own branch.
It wraps the provider's own CLI, so you bring your Claude or ChatGPT subscription, your own API key, or the vendor's tokens at API prices.
Built by Digger, the team behind the open-source infrastructure-as-code orchestrator, and open-sourced on 2026-11-13 after starting as a persistent-VM sandbox product.

## Status

Young and vendor-owned: 1,827 stars and 233 forks as of 2026-11-27, 102 open issues, created 2025-12-09, pushed 2026-11-27, with the top three contributors each above 400 commits (GitHub API, as of 2026-11-27).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=diggerhq/opencomputer&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=diggerhq/opencomputer&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=diggerhq/opencomputer&type=date&legend=top-left" />
</picture>

The main branch is the release signal: the newest tagged release, v0.6.0.50 (2026-11-09), predates the 2026-11-13 open-source launch, and the `oc v0.6.0.x` train from August to November belongs to the earlier compute-product era, which the site still sells as persistent VMs (Free, Medium $300 a month, Large $3,000 a month, as of 2026-11-27).
Main moved fast in the days after launch, with self-hosting commits landing 2026-11-27 (the Computer gateway under Miniflare on one VM, a host-install script).
The footprint is one thread: a self-submitted 131-point Show HN on 2026-11-20 with 36 comments, mostly naming complaints and questions the founders answered, with no independent hands-on report inside it, plus two third-party write-ups, a competitor's roundup (Munder Difflin, 2026-11-21) and a vendor-blog analysis (MewCP, 2026-11-21).
The LavX News write-up the 2026-11-26 scan recorded was not found this run.

## Strengths

- Self-hosting reaches the compute layer: one VM in your Azure, AWS, GCP, or OCI account plus Cloudflare Workers, with the VM locked to outbound-only access.
- Harness neutrality: you choose Claude Code or Codex per request and keep the subscription you already pay for, with the vendor's tokens at API prices and no markup as the alternative.
- The shared warm VM is the engineering idea: repo clones, toolchains, and package caches stay on a fast local disk, and sessions move between VMs because every turn is backed up to a repository.

## Cautions

- Sessions start in `bypassPermissions`, so the agent runs commands without asking; the docs assign isolation to the container, not to a permission mode.
- Self-hosting carries a long dependency list: a Cloudflare account with a zone you control, a WorkOS account for sign-in, Slack and GitHub apps you create, and an Anthropic API key, with Fly and Kubernetes support still announced as coming.
- Every benchmark is the vendor's own: first push in 24 seconds against 53 to 72 seconds for others and all four pull requests in 56 seconds against 85 to 185 seconds, on a dependency-bump task, where the MewCP analysis notes OpenComputer finished 5 of 6 runs against Devin's 5 of 5.
- No shell access into a session is listed, Linux only, and Slack plus the API as the trigger surface; Discord and T3 Code integration were "on the roadmap" in the launch thread.
- The name collides with the OpenComputers Minecraft mod and e2b's Open Computer Use, and the thread's open debate was whether an infra provider can sell "open source Devin".

## Pricing

Free and open source under Apache-2.0; self-hosting is free besides your own cloud, Cloudflare, WorkOS, and model costs.
The vendor cloud bills per Slack workspace in work minutes as of 2026-11-27: a 3-day free trial with 600 work minutes, Pro at $20 a month with 2,000 work minutes, Max at $200 a month with 25,000, and $0.01 per extra minute.
The model is $0 extra with a Claude or ChatGPT subscription, or your own key, or vendor tokens at API prices.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-27 | Cloud (hosted) | Baseline at admission: 3-day trial with 600 work minutes; Pro $20/mo per Slack workspace with 2,000 work minutes; Max $200/mo with 25,000; $0.01 per extra minute. | https://opencomputer.dev/compare/opencomputer-vs-devin/ |

## Compared to

- [Paseo](../paseo/index.md): a self-hosted daemon driving the agents on machines you own from desktop, web, and phone; choose Paseo when the agents should run where you sit or on your own boxes with a mobile client, OpenComputer when the team's entry point is a Slack thread and the machine is in a cloud account.
- [Omnara](../omnara/index.md): a control plane where agents are YAML and supervision happens from dashboard, phone, CLI, API, or Slack; choose Omnara for a vendor-neutral supervision layer over many harnesses, OpenComputer for one packaged cloud agent plus the compute under it.
- [Switch](../../executions/switch/index.md): the Slack-to-sandbox chat bridge line; both start work from a Slack mention, but Switch is a bridge into sandboxes while OpenComputer ships its own harness, machine, and pull-request flow.
- [OpenHands](../../harnesses/openhands/index.md): an agent with its own harness and models; choose OpenHands for a harness you can read and change, OpenComputer when you want Claude Code or Codex themselves running in a cloud your company controls.

## Bottom line

**Recommended for Slack-centered teams that want Claude Code or Codex working in a cloud account they control, on subscriptions they already pay for.**
Not for anyone who needs a review gate before commands run, macOS or Windows environments, or an independent benchmark.

## Changes

- 2026-11-27 - Created in the Orchestration category from the 2026-11-26 routing, recording the Slack-driven cloud agent, the self-hosting dependency list, the `bypassPermissions` caution, and the vendor-only benchmark record.

## See also

- [Paseo](../paseo/index.md) - the self-hosted daemon alternative whose phones and own-machine execution it lacks
- [Omnara](../omnara/index.md) - the supervision control plane over many harnesses
- [Switch](../../executions/switch/index.md) - the Slack-to-sandbox bridge on the executions line
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/diggerhq/opencomputer - stars, forks, license, creation and push dates, as of 2026-11-27
- https://github.com/diggerhq/opencomputer - the README: the Slack entry point, the Calvin gateway, rootless Podman per session, and the git-backed store
- https://api.github.com/repos/diggerhq/opencomputer/releases?per_page=8 - the `oc v0.6.0.x` train, v0.6.0.50 (2026-11-09) back to v0.6.0.43 (2026-08-21), as of 2026-11-27
- https://opencomputer.dev - the site: the earlier persistent-VM product, its Free, Medium $300 a month, and Large $3,000 a month tiers, and the comparison pages, as of 2026-11-27
- https://opencomputer.dev/blog/opencomputer-open-source-devin-alternative/ - the 2026-11-13 launch post: the three architectures tried, the 640 session-hours cost claim, and the 3-day, 600 work-minute trial
- https://opencomputer.dev/compare/opencomputer-vs-devin/ - the vendor's Devin comparison grounding the Pro $20 and Max $200 workspace pricing and the Slack-plus-API trigger surface, as of 2026-11-27
- https://docs.opencomputer.dev/self-hosting/overview - the self-hosting requirement list and the `bypassPermissions` session default
- https://news.ycombinator.com/item?id=50581403 - the self-submitted 131-point, 36-comment Show HN of 2026-11-20, with the founders' answers and the naming debate
- https://munderdiffl.in/blog/devin-alternatives/ - a competitor's 2026-11-21 roundup that places OpenComputer as "Devin's Slack flow, in open source"
- https://mewcp.com/articles/opencomputer-is-an-open-source-devin-alternative-you-can-self-host-3fc1b9 - the 2026-11-21 third-party analysis of the benchmark table and the 5-of-6 completion rate
