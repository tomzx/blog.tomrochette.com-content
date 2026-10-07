---
title: Omnigent
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harnesses, meta-harness, orchestration, policies, sandboxing]
readability: 3
audience_notes: >
  Engineers running more than one coding harness who want to swap, compose, and govern them from one
  layer.
  Assumes you know what a coding harness (Claude Code, Codex, Pi) and a policy gate are.
---

Omnigent is Databricks' open-source meta-harness: an orchestration layer that wraps Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and your own YAML-defined agents behind one uniform API, then adds policies, sandboxing, and real-time collaboration on top.

## What it is

**It sits above the harness, not beside it: sessions, policies, and history live in Omnigent, while the model-carrying harness underneath stays swappable with one-line changes.**
A runner wraps any agent in a sandboxed session with a uniform API, a local or deployed server provides policies and shared history, and every session is reachable from the terminal, the web, mobile, or the macOS desktop app.
Policies stack across server, agent, and session levels to cap spend, pause risky actions for approval, and broker credentials through an egress proxy so the agent never sees the token.
Agents are short YAML files (prompt, harness, tools, sub-agents); the same file runs on any supported harness, and example agents include Polly, a coding orchestrator that delegates to parallel worktree sub-agents and routes each diff to a reviewer from a different vendor.
Apache-2.0, Python 3.12+, installed via installer, uv, pip, or Homebrew; built by the Databricks AI team with Neon and contributors, announced June 13, 2026 by Matei Zaharia, Kasey Uhlenhuth, and Corey Zumar, in alpha.

## Status

**Active, well-resourced, and young, with traction that far outruns its independent discussion.**
10,635 stars and 1,701 forks as of 2026-10-07 (repository created 2026-06-11), PyPI 0.17.0 published 2026-10-06 after 40+ releases, and the default branch was pushed the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=omnigent-ai/omnigent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=omnigent-ai/omnigent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=omnigent-ai/omnigent&type=date&legend=top-left" />
</picture>

The HN footprint is thin: the top thread (the Databricks announcement, June 2026) reached 15 points with 4 comments, and resubmits stayed at 1 to 6 points.
The 1,814 open issues against 10.6k stars read as heavy use plus heavy traffic, under an alpha badge the README still wears.

## Strengths

- **Harness portability as the product**: the same agent YAML runs on claude, codex, cursor, hermes, pi, and opencode harnesses plus SDK harnesses, with a harness test bench that checks each one's capability matrix against observed behavior.
- Governance at the right layer: stateful contextual policies (cost budgets, tool restrictions, approval gates) enforced outside the prompt, where the agent cannot argue with them.
- Sandboxing with teeth: bubblewrap on Linux (mandatory), seatbelt on macOS, and cloud sandboxes on Modal, Daytona, Blaxel, E2B, Kubernetes, Databricks, and more, includable per session.
- Collaboration: live session sharing by URL, co-driving, forking, and the same session from terminal, web, phone, or desktop app.

## Cautions

- Alpha at 0.x: expect churn (40+ PyPI releases in under four months), and the README says so itself.
- It is another layer to own: a local server at minimum, optionally a deployed one, plus credential routing and sandbox providers; if you run one harness happily, this is overhead, and an HN commenter made exactly that trade against its sandbox abstraction.
- Windows support is explicitly degraded: no OS sandbox, no terminal wrappers, Job Object containment only.
- Most evidence is the vendor's own: the thin independent discussion means no second opinion on real-world governance behavior yet.

## Pricing

Apache-2.0 open source; no paid tiers surfaced as of 2026-10-06 (the site and README document no plans; the costs are your model tokens and any cloud sandbox hosting you attach), so pricing does not apply.

## Compared to

- [Pi](../pi/index.md): the minimal, extension-first single harness; choose Pi to go deep on one harness, Omnigent to rotate harnesses without rewriting agents.
- [OpenCode](../opencode/index.md): the provider-neutral single harness; Omnigent treats it as one more engine in the rotation.
- [Warp Agent CLI](../warp-agent-cli/index.md): the commercial, credit-metered agent platform; Omnigent is the open governance layer over the harnesses you already run.

## Bottom line

Recommended for teams running several coding harnesses that need shared policy, sandboxing, and session collaboration above them, and who accept alpha churn.
Not for developers happy inside one harness, and not for Windows-first setups that need OS-level isolation.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the omnigent-ai/omnigent star history chart to the Status section.

## See also

- [Pi](../pi/index.md) - the extension-first harness Omnigent can wrap
- [OpenCode](../opencode/index.md) - the provider-neutral harness in Omnigent's rotation
- [Claude Code](../claude-code/index.md) - the flagship harness most Omnigent sessions will drive
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - where the meta-harness column sits

## References

- https://api.github.com/repos/omnigent-ai/omnigent - repository facts (10,635 stars, 1,701 forks, Apache-2.0, Python, pushed 2026-10-07, as of 2026-10-07)
- https://raw.githubusercontent.com/omnigent-ai/omnigent/main/README.md - harness list, agent YAML, policies, sandboxes, install, Windows limits, collaboration
- https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents - Databricks origin (Zaharia, Uhlenhuth, Zumar, June 13, 2026), architecture, Apache-2.0 open-sourcing
- https://omnigent.ai - product site (alpha status, "Built by the Databricks AI team, Neon and the Omnigent Contributors")
- https://hn.algolia.com/api/v1/search?query=omnigent - the thin HN footprint (15-point top thread of June 2026; resubmits at 1 to 6 points)
- https://pypi.org/pypi/omnigent/json - PyPI 0.17.0 published 2026-10-06, Python 3.12+, release history
