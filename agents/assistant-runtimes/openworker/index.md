---
title: OpenWorker
created: 2026-10-02
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtime, desktop, security, sandboxing]
readability: 3
audience_notes: >
  Engineers who want a governed desktop AI coworker that finishes whole tasks and are watching the assistant-runtime space.
  Assumes you know what a model API key and a local sandbox are.
---

OpenWorker is an MIT-licensed, open-source desktop AI coworker from Andrew Ng's team that runs assigned tasks to finished deliverables on your own machine, with every action governed and logged and sandboxed execution via NVIDIA's OpenShell.

**Its bet is that the assistant category's next step is specialist coworkers with governance built in: it ships security-review coworkers first, because attackers already have AI leverage and defenders should too.**

## What it is

A desktop app (macOS Apple Silicon, signed and notarized; Windows x64 builds not yet code-signed) in open beta, self-updating, from the DeepLearning.AI orbit.
It runs on your machine, takes a bring-your-own key for OpenAI, Anthropic, Google, or an open-weight provider, or runs fully local through Ollama, and ships specialist coworkers whose tools, working style, and check-ins come preconfigured for one job.
The launch cohort is security work: codebase and dependency review where findings combine deterministic scanners (semgrep) with model reasoning and proposed fixes are re-scanned and diff-reviewed before approval, plus cloud-posture audit and incident triage.
Every action an agent takes is governed and logged, approvals are configurable, and commands can run inside an NVIDIA OpenShell sandbox.

## Status

Early and moving fast: about 18,400 stars in its first twelve weeks as of 2026-10-06 (created 2026-07-20, pushed today), with v0.3.1 released 2026-10-05 and a public beta disclaimer on the README.

<a href="https://www.star-history.com/?repos=andrewyng%2Fopenworker&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=andrewyng/openworker&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=andrewyng/openworker&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=andrewyng/openworker&type=date&legend=top-left" />
 </picture>
</a>

v0.3.1 publishes the CLI as a container image on ghcr.io, so a coworker runs entirely inside an NVIDIA OpenShell sandbox with one command, and pins the desktop app's OpenShell option to OpenShell 0.1.2.
**The star count is an audience effect as much as an adoption signal: Andrew Ng's announcement drove the attention, while the independent Hacker News footprint is one 5-point thread plus a pair of 2-point follow-ups, so the tool's actual field usage is unproven.**
The project says rough edges are being polished; treat it as beta in fact, not just label.

## Strengths

- Governance is structural, not a settings page: logged actions, approval guidance, and sandboxed command execution are the default path.
- The security-coworker design enforces fixer-versus-checker separation, with deterministic scanners anchoring the model's findings.
- No model lock-in: frontier keys or fully local through Ollama, on a machine you control.
- Task-oriented framing (finished deliverables, standing automations with full transcripts) rather than another chat window.
- Backing and velocity: an Andrew Ng team shipping weekly-quality releases into a category it also teaches.

## Cautions

- Beta software with root-adjacent powers: an agent that reads your code, cloud config, and inbox deserves more scrutiny than its ten-week age suggests.
- macOS gets signed builds while Windows builds are unsigned, so the cross-platform story is uneven on the security-sensitive edges.
- The coworker roster beyond security is mostly roadmap; the launch promise is narrower than the homepage's everyday-work examples.
- Its governance vocabulary (approvals, logs, sandboxes) overlaps what your OS and IAM already enforce, and the two layers are not integrated.
- The 18k-star traction has no independent usage record behind it yet.

## Pricing

Free and open source under MIT.
You pay your model provider directly, or nothing if you run Ollama locally; there is no hosted tier and no OpenWorker subscription.

## Compared to

- [OpenClaw](../openclaw/index.md): the heavyweight personal assistant framework with channels, skills, and a huge ecosystem; choose OpenClaw for maximal capability, OpenWorker for governed, task-finished security work from day one.
- [Hermes Agent](../hermes/index.md): Nous Research's autonomous agent with self-created skills and messaging gateways; OpenWorker is the desktop-first, governance-first counterpart.
- [OpenShell](../../sandboxing/openshell/index.md): the NVIDIA sandbox OpenWorker builds on; use it directly if you want the isolation without the coworker.

## Bottom line

**Recommended for security-minded engineers who want a governed desktop coworker for review and triage work they can run on their own keys.**
Not for anyone needing a mature, broadly capable assistant today, or Windows-first teams that need signed builds.

## Changes

- 2026-10-02 - Created.
- 2026-10-03 - Corrected the Hacker News footprint claim to one 5-point thread plus a pair of 2-point follow-ups (the Algolia search returned a third thread the creation run missed), and refreshed the as-of numbers (about 18,400 stars, pushed 2026-10-02, v0.3.0 still latest).
- 2026-10-06 - Recorded v0.3.1 (2026-10-05), which publishes the CLI as a ghcr.io image so a coworker runs inside an OpenShell sandbox with one command and requires OpenShell 0.1.2, with refreshed adoption numbers.
- 2026-10-07 - Added the andrewyng/openworker star history chart to the Status section.

## See also

- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins
- [OpenClaw](../openclaw/index.md) - the ecosystem-heavy personal assistant incumbent
- [Hermes Agent](../hermes/index.md) - the autonomous research-agent counterpart
- [OpenShell](../../sandboxing/openshell/index.md) - the NVIDIA sandbox layer this runtime integrates
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://github.com/andrewyng/openworker - repository, MIT license, stars, beta disclaimer, use cases, and the governed-by-design section as of 2026-10-06
- https://openworker.com/ - product positioning, download platforms, and the specialist-coworker framing
- https://github.com/andrewyng/openworker/releases - the v0.3.0 release (2026-09-30) and v0.3.1 (2026-10-05, still latest as of 2026-10-06), the ghcr.io CLI image and the OpenShell 0.1.2 pin anchoring the version claims
- https://github.com/andrewyng/openworker/blob/main/docs/openshell.md - the NVIDIA OpenShell sandbox integration behind the isolation claims
- https://github.com/andrewyng/openworker/blob/main/docs/approval-guidance.md - the approval model behind the governance claims
