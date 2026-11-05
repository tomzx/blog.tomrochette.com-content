---
title: GitHub Copilot automations
created: 2026-08-24
updated: 2026-11-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, executions, github-copilot, scheduling, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Teams on paid Copilot plans considering letting GitHub's cloud agent run itself on a schedule or on repository events.
  Assumes you know what Copilot cloud agent is and how your repo's permissions work.
---

Copilot automations run GitHub's Copilot cloud agent automatically, on a schedule (hourly, daily, weekly), in response to repository events (issue created, pull request opened or synchronized), or on an authenticated API call, without a person starting each task.

**Automations are the easiest scheduled agent to turn on in the GitHub ecosystem, and governance now hinges on one permanent choice made at creation: a personal automation stays invisible to the rest of the team, while a shared one is team-visible and auditable but bills and acts under the repository's identity.**

## What it is

You create an automation (from a repository's Agents tab, the GitHub Copilot app, VS Code's Agents window, or the REST API) by naming it, choosing a **personal** or **shared** type, writing a prompt, picking triggers, a model, and the tools it may use, with optional search-query and files-changed filters narrowing the event triggers and optional per-run, daily, weekly, and monthly AI-credit limits bounding its spend.
The type is permanent: it cannot be changed after creation.
Every automation can also fire programmatically through an authenticated API call that can pass extra context into the prompt.
Runs start Copilot cloud agent sessions in GitHub's ephemeral, Actions-powered environments, and can label issues, open draft pull requests, or push fixes to one repository.
It ships with GitHub, on Copilot Pro, Pro+, Max, Business, and Enterprise plans, and requires only write access to create.

## Status

**Active and shipped, with the rationale-and-approvals layer still in public preview.**
Documentation is extensive and the feature is on by default at the organization level (admins can disable it).
The docs now split automations into personal and shared types at creation, the remedy to the creator-private model this note documented for most of its life.
I found no independent benchmarking of automation quality; the community footprint is mostly GitHub's own docs and issue trackers, which is itself a signal worth noting.

## Strengths

- **Sensible unattended-run defaults**: events from users without write access are ignored by default (a prompt-injection mitigation), least-privilege tool selection is the main scoping control, and workflows do not run on automation PRs until someone with write access approves them.
- Attribution keeps review controls intact: personal-automation PRs are attributed to the creator, who then cannot approve them, and shared-automation PRs under Copilot's identity require an extra approval by default.
- Issue changes come with rationale and confidence ratings, and the default "Cautious" level applies only high-confidence changes automatically.
- Zero infrastructure: no runners, no tokens, no workflow files to maintain.

## Cautions

- **Visibility depends on the type, and only shared fixes the blind spot**: a personal automation is private to its creator (administrators and teammates cannot see, audit, or review its definition), while a shared automation is visible to everyone with read access and editable by anyone with write access; the sessions either type starts are visible to everyone with repository access, so the blind spot covers the trigger and tool configuration of personal automations only.
- Because the type is chosen at creation and cannot change, a team that defaults to personal keeps recreating the governance hole one automation at a time.
- Automations are not committed to git, so they are not code-reviewed or versioned alongside the repository they act on.
- Private or internal repositories only; public repositories are excluded entirely.
- Billing for a personal automation lands on its creator (AI credits), a shared automation bills the repository owner, and Actions minutes bill to the repository owner either way; GitHub's own docs warn that approvals are "a workflow convenience, not a security control".
- Each session is capped at 59 minutes and scoped to a single repository.

## Pricing

Included with paid Copilot plans; each run consumes GitHub Actions minutes and AI credits, billed to the creating user for a personal automation and to the repository owner for a shared one.
Per-run (minimum 30 credits), daily, weekly, and monthly AI-credit limits can bound the spend per automation.
There is no separate automation fee, but a nightly test-fix automation is a recurring metered workload, not a free feature.

## Compared to

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): versioned in your repo, multi-engine, guardrail-heavy; choose it when automation logic should be reviewed like code.
- [Claude Code routines](../claude-code-routines/index.md): Anthropic's equivalent scheduled runs inside the Claude ecosystem, still creator-private where Copilot automations now offer a shared, team-visible type.
- [OpenChamber](../../surfaces/openchamber/index.md): cron-scheduled prompts on your own machine with your own harness, no vendor metering.

## Bottom line

**Recommended for private-repo chores like nightly test triage and issue labeling, where the blast radius of one repository is acceptable.**
Not for public repositories (unavailable), and not for teams that stay on personal automations while their security team needs to audit what runs where.
My disagreeable claim: shared automations fix the visibility hole on paper, but the default path still creates a creator-private automation, so most teams will keep getting exactly the uninspectable layer that starts silent drift; the fix exists and it is opt-in.

## Changes

- 2026-08-24 - Created in the Executions category during the research index seeding.
- 2026-10-06 - Recorded the event-trigger filters (search query and files changed), linked the new Claude Code routines note as the Claude-side equivalent, and re-verified all five sources; the core claims hold unchanged.
- 2026-10-07 - Corrected the visibility caution against the current docs: automation definitions are invisible to administrators and teammates, but the sessions an automation starts are visible to everyone with repository access, so the governance blind spot covers the configuration, not the runs.
- 2026-10-17 - Fully re-verified in rotation with all five sources re-fetched: the creator-private definition model with visible sessions, the write-access defaults, the public-preview rationale layer, the 59-minute cap, and the approvals caveat all re-confirmed unchanged.
- 2026-10-20 - Repointed the four GitHub docs references to their current paths after a docs reorganization (the old paths now redirect); each new target re-fetched and its claim re-confirmed (59-minute cap, creator-private definitions, the approvals caveat, the automations risk section).
- 2026-10-26 - Fully re-verified in rotation with every cited URL re-fetched: the private-or-internal-only availability, the write-access creation and untrusted-event defaults, the schedule and event trigger list with search and files-changed filters, the creator-private definitions with visible sessions, the public-preview rationale layer with the Cautious default, the verbatim approvals caveat, the 59-minute session cap, and the minutes-plus-AI-Credits billing to the creator all re-confirmed unchanged.
- 2026-11-05 - Fully re-verified in rotation with every cited URL re-fetched: recorded the personal-versus-shared automation types (chosen at creation, permanent, shared team-visible and editable with Copilot identity and owner billing beside the creator-private personal type), the API trigger with optional context, VS Code and REST creation surfaces, optional per-run and daily, weekly, and monthly AI-credit limits (per-run minimum 30), and the billing split (personal AI credits to the creator, shared to the repository owner, Actions minutes to the repository owner); the private-or-internal availability, the write-access creation and untrusted-event defaults, the not-committed-to-git storage, the public-preview rationale layer with the Cautious default, the verbatim approvals caveat, and the 59-minute cap all re-confirmed.

## See also

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the in-repo, versioned, multi-engine alternative
- [VS Code + Copilot](../../surfaces/vscode-copilot/index.md) - the interactive surface of the same Copilot platform
- [Claude Code hooks](../claude-code-hooks/index.md) - event triggers inside a harness versus hosted scheduled runs
- [OpenChamber](../../surfaces/openchamber/index.md) - self-hosted scheduling with no per-run billing

## References

- https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations - triggers, availability, visibility, personal and shared types, API trigger, security model (re-fetched 2026-11-05)
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations - creation flow, personal/shared choice, Run now testing, AI-credit limits, prompt warning (re-fetched 2026-11-05)
- https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations - the automations section of GitHub's risk model (re-fetched 2026-11-05)
- https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automation-rationale-and-approvals - confidence levels and the approvals caveat (re-fetched 2026-11-05)
- https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github - Actions-powered sessions, 59-minute cap, minutes and credits billing (re-fetched 2026-11-05)
