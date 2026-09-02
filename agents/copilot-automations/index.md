---
title: GitHub Copilot automations
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, executions, github-copilot, scheduling]
readability: 3
audience_notes: >
  Teams on paid Copilot plans considering letting GitHub's cloud agent run itself on a schedule or on repository events.
  Assumes you know what Copilot cloud agent is and how your repo's permissions work.
---

Copilot automations run GitHub's Copilot cloud agent automatically, on a schedule (hourly, daily, weekly) or in response to repository events (issue created, pull request opened or synchronized), without a person starting each task.
Facts below verified as of 2026-09-02.

**Automations are the easiest scheduled agent to turn on in the GitHub ecosystem, and their per-user visibility model makes them the hardest to govern.**

## What it is

You create an automation from a repository's Agents tab or the GitHub Copilot app by naming it, writing a prompt, picking triggers, a model, and the tools it may use.
Runs start Copilot cloud agent sessions in GitHub's ephemeral, Actions-powered environments, and can label issues, open draft pull requests, or push fixes to one repository.
It ships with GitHub, on Copilot Pro, Pro+, Max, Business, and Enterprise plans, and requires only write access to create.

## Status

**Active and shipped, with the rationale-and-approvals layer still in public preview.**
Documentation is extensive and the feature is on by default at the organization level (admins can disable it).
I found no independent benchmarking of automation quality; the community footprint is mostly GitHub's own docs and issue trackers, which is itself a signal worth noting.

## Strengths

- **Sensible unattended-run defaults**: events from users without write access are ignored by default (a prompt-injection mitigation), least-privilege tool selection is the main scoping control, and workflows do not run on automation PRs until someone with write access approves them.
- Attribution keeps review controls intact: PRs are attributed to the automation's creator, who then cannot approve them.
- Issue changes come with rationale and confidence ratings, and the default "Cautious" level applies only high-confidence changes automatically.
- Zero infrastructure: no runners, no tokens, no workflow files to maintain.

## Cautions

- **An automation is private to its creator**: administrators cannot see, audit, or review other people's automations, only the sessions they start, so org-level governance is effectively blind.
- Automations are not committed to git, so they are not code-reviewed or versioned alongside the repository they act on.
- Private or internal repositories only; public repositories are excluded entirely.
- Billing lands on the creator (Actions minutes plus AI credits), and GitHub's own docs warn that approvals are "a workflow convenience, not a security control".
- Each session is capped at 59 minutes and scoped to a single repository.

## Pricing

Included with paid Copilot plans; each run consumes GitHub Actions minutes and AI credits, billed to the creating user.
There is no separate automation fee, but a nightly test-fix automation is a recurring metered workload, not a free feature.

## Compared to

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): versioned in your repo, multi-engine, guardrail-heavy; choose it when automation logic should be reviewed like code.
- Claude Code routines: Anthropic's equivalent scheduled runs inside the Claude ecosystem.
- [OpenChamber](../openchamber/index.md): cron-scheduled prompts on your own machine with your own harness, no vendor metering.

## Bottom line

**Recommended for private-repo chores like nightly test triage and issue labeling, where the blast radius of one repository is acceptable.**
Not for public repositories (unavailable) or any team whose security team needs to audit what runs where.
My disagreeable claim: creator-private automations are disqualifying for team adoption until GitHub adds shared visibility, because an automation layer nobody else can inspect is exactly how silent drift starts.

## See also

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the in-repo, versioned, multi-engine alternative
- [VS Code + Copilot](../vscode-copilot/index.md) - the interactive surface of the same Copilot platform
- [Claude Code hooks](../claude-code-hooks/index.md) - event triggers inside a harness versus hosted scheduled runs
- [OpenChamber](../openchamber/index.md) - self-hosted scheduling with no per-run billing

## References

- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations - triggers, availability, visibility, security model
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations - creation flow, Run now testing, prompt warning
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations - the automations section of GitHub's risk model
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automation-rationale-and-approvals - confidence levels and the approvals caveat
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent - Actions-powered sessions, 59-minute cap, minutes and credits billing
