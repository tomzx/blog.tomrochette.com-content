---
title: "Executions Feature Matrix"
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, executions, scheduling, workflow-automation]
readability: 3
audience_notes: >
  Engineers deciding where unattended agent execution should live, inside a harness, in GitHub's cloud, in a compiled workflow, or on a self-hosted platform.
  Assumes you know what GitHub Actions, webhooks, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the four execution substrates profiled in this section, the mechanisms that make an agent run without a person starting each task.
Everything below was verified against live sources on 2026-08-30.

**What decides between these four is not agent quality but where the trigger definition lives and who can inspect it, and on that axis Copilot automations fail for any team today, a stronger verdict than their zero-setup convenience deserves.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Claude Code hooks](../claude-code-hooks/index.md) | [Copilot automations](../copilot-automations/index.md) | [GitHub Agentic Workflows](../github-agentic-workflows/index.md) | [n8n](../n8n/index.md) |
| --- | --- | --- | --- | --- |
| Kind | harness feature | cloud service | compiled framework | platform, self-host or cloud |
| Trigger types | lifecycle events (~30) | repo events, schedules | repo events, schedules | webhooks, schedules, chat, app events |
| Where execution runs | your machine, web sessions too | GitHub ephemeral runners | Actions runners, self-host ok | self-host or n8n Cloud |
| Open source | ✗ proprietary CLI | ✗ | ✓ MIT | ~ fair-code license |
| Agent lock-in | Claude Code only | Copilot agent only | 5 engines, more imported | any provider, BYOK |
| Guardrails and permissions | permission system, managed hooks | least-privilege tools, no self-approval | safe outputs, firewall, threat scans | webhook auth, IP allowlists |
| Versioned with the repo | ~ project-scope settings | ✗ not in git | ✓ Markdown in repo | ~ versioned publishes |
| Scheduled runs | ✗ (routines separate) | ✓ hourly to weekly | ✓ Actions cron | ✓ hourly to custom cron |
| Pricing | in plan, usage-metered handlers | paid plan, minutes and credits | free tool, minutes and inference | free self-host, per execution cloud |

## Reading the matrix

**The Kind row is the real table of contents: two of these are subscription features (hooks ship inside Claude Code, automations ship inside paid Copilot plans) and two are ownable infrastructure (an MIT-licensed compiler, a self-hostable platform), and they answer different questions.**
The subscription pair presumes you already live in that ecosystem; the infrastructure pair is a decision about where agent work may run at all.

**Trigger types split the category into inside the session and outside it: only hooks see the agent's own lifecycle (tool calls, compaction, permission requests), and only n8n reaches past the repository to webhooks, chat channels, and 1,500+ integrations.**
The two GitHub offerings share the middle ground, repository events and schedules, which is why the choice between them is governance rather than capability.

**The open-source row carries a correction the community keeps getting wrong: gh-aw is the only truly open one (MIT), n8n is fair-code under the Sustainable Use License and says so itself, and the subscription pair is closed.**
Where execution runs compounds the difference: automations only ever run in GitHub's ephemeral environments, gh-aw can move to self-hosted or ARC runners, and n8n runs wherever you deploy it, including your own hardware.

**Guardrails differ in kind, not degree: gh-aw compiles a safe-outputs gate into the workflow itself, automations lean on attribution and write-access approvals, hooks lean on the permission system, and n8n leans on webhook authentication.**
The notes document fail-open behavior in two of the four (the hooks `if` filter and n8n's `Only Run If` conditional), and GitHub itself calls its approvals "a workflow convenience, not a security control", so none of these is a security boundary on its own.

**The versioned-with-the-repo row is where automations lose me: an automation layer that admins cannot audit and that is not committed to git is a governance hole, while gh-aw's compiled Markdown is exactly the review artifact a team needs.**
hooks sit in between, since project-scope settings can be committed and user scope cannot, and n8n versions every publish as revertible snapshots without touching your git.

## Choosing from the matrix

- Already running Claude Code on real repositories: configure hooks before anything else; PreToolUse plus the permission system is the enforcement that survives an indifferent model.
- Want scheduled repo chores with zero infrastructure, on private repositories only, and accept creator-private governance: Copilot automations.
- Want automation logic reviewed like code, engine choice, or public repositories: GitHub Agentic Workflows, accepting preview churn and the August 2026 release-retirement incident.
- Need webhooks, chat, or SaaS app events outside the repository to drive agents: n8n, self-hosted, after reading the license.
- Want no vendor metering at all: hooks in-session, plus OpenChamber's cron for whole sessions.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the same treatment for terminal harnesses
- [Claude Code](../claude-code/index.md) - the harness whose hooks fill the first column
- [OpenChamber](../openchamber/index.md) - self-hosted cron scheduling for coding sessions, no per-run billing
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the sibling matrix for editors and environments
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map these columns come from

## References

- https://code.claude.com/docs/en/hooks - event surface and handler types for the hooks column
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations - triggers, visibility, and security model for the automations column
- https://github.github.com/gh-aw/ - frontmatter triggers, schedules, engines, guardrails, and runners for the gh-aw column
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent - Actions-powered sessions, the 59-minute cap, and billing
- https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ - webhook trigger semantics for the n8n column
- https://docs.n8n.io/privacy-and-security/sustainable-use-license.md - the not-open-source licensing cell
