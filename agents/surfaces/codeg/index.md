---
title: Codeg
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, agentic-development-environments, open-source]
readability: 3
audience_notes: >
  Engineers running several coding-agent CLIs who want one workspace that keeps every session, searchable and resumable, regardless of which agent produced it.
  Assumes you know what ACP is and what an agent's local session history is.
---

Codeg is an Apache-2.0 multi-agent coding workspace, in Rust, that aggregates sessions from fifteen built-in agents plus any ACP agent into one searchable conversation layer, with a desktop app, a self-hosted server or Docker deployment, and native iOS and Android clients.

**Codeg's bet is that the session history your agents already write to disk is the durable asset, and that any surface which can import, search, resume, and hand those sessions between agents owns the workflow.**

## What it is

A workspace that renders every supported agent as the same structured conversation instead of a terminal: Claude Code, Codex, OpenCode, Pi, Grok Build, and thirteen more built in, plus any ACP-speaking agent.
The session layer is the differentiator: Codeg imports, searches, and resumes the history each agent keeps on disk, and hands a session to a different agent to continue.
On top of that sit a main-agent delegation model (Claude Code calling Codex or Gemini as its own subagent session), Project Boot scaffolding, chat channels over Telegram, Lark (Feishu), and iLink (Weixin), office document work through a bundled officecli, research skills, and cron automations.
It is written in Rust, licensed Apache-2.0, and deployed as a desktop app, a self-hosted server, or Docker.

## Status

**Active on a fast release train.**
The repository was created 2026-02-09 and shows 3,887 stars and 505 forks as of 2026-10-11, with commits landing the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=spacering-net/codeg&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=spacering-net/codeg&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=spacering-net/codeg&type=date&legend=top-left" />
</picture>

The train has quickened through October: v0.33.0 (October 2), v0.34.0 (October 7), v0.35.0 (October 10), and v0.35.1 (October 11) as the latest.
An Algolia search of Hacker News returned no story about this project as of 2026-10-11, only substring matches on "codegen", so the footprint is GitHub-side.

## Strengths

- **Session portability is the mechanism nobody else ships: your agent history stops being a private format per tool and becomes one searchable, transferable corpus.**
- The surface list is the category's widest: desktop, self-hosted server, Docker, iOS, and Android, with the mobile clients open source alongside the app.
- ACP support means the built-in fifteen never become the ceiling.
- Apache-2.0 and self-hostable, so the aggregation layer stays on machines you control.

## Cautions

- **Zero independent coverage is the caution: no Hacker News story, no third-party review found this run, so the aggregate-and-hand-off claims rest on the project's own documentation.**
- The feature set stretches well past coding (office documents, research skills, chat channels), which is the general-workspace gravity this category keeps resisting, though coding sessions remain the core here.
- v0.x at a two-releases-per-week pace means churn is the maintenance plan.
- MCP appears in the README but has no dedicated documentation this run found, and AGENTS.md support is undocumented.

## Pricing

Free and open source under Apache-2.0; no paid tier exists.

## Compared to

- [OpenChamber](../openchamber/index.md): the OpenCode-only cockpit with fusion and cron; OpenChamber goes deep on one harness, Codeg goes wide across many.
- [Nimbalyst](../nimbalyst/index.md): the visual-editing workspace; Nimbalyst makes you a co-editor of the artifacts, Codeg makes you the operator of the sessions.
- [Cate](../cate/index.md): the canvas supervisor; Cate shows agent state in space, Codeg unifies agent state into one timeline.

## Bottom line

**Recommended for engineers whose agent history is scattered across three or more CLIs and who want it searchable and resumable in one self-hosted place.**
Not for anyone who needs an independently reviewed tool, a 1.0 release, or an editor-first experience.

## Changes

- 2026-10-11 - Created from the category entrant scan, admitted on its differentiated session-aggregation-and-handoff mechanism, with the zero-coverage caution recorded.
- 2026-10-11 - Added the star history chart.

## See also

- [OpenChamber](../openchamber/index.md) - the single-harness incumbent this note joins as the many-harness aggregator
- [Nimbalyst](../nimbalyst/index.md) - the visual workspace neighbor, editor-first where Codeg is session-first
- [Cate](../cate/index.md) - the canvas supervisor over the same parallel-agent workload
- [ACP](../../protocols/acp/index.md) - the protocol that lets any agent join Codeg's fifteen built in

## References

- https://github.com/spacering-net/codeg - repository, README (fifteen built-in agents, structured conversation rendering, session import and handoff), Apache-2.0 license, 3,887 stars and 505 forks as of 2026-10-11
- https://api.github.com/repos/spacering-net/codeg - creation date 2026-02-09, language Rust, push date 2026-10-11, stars and forks as of 2026-10-11
- https://docs.codeg.app - the feature set: conversation aggregation, multi-agent delegation, project boot, chat channels over Telegram, Lark, and iLink, office documents, research skills, cron automations, and the open-source iOS and Android clients
- https://github.com/spacering-net/codeg/releases - v0.35.1 (2026-10-11) as the latest release, after v0.35.0 (October 10), v0.34.0 (October 7), and v0.33.0 (October 2)
- https://hn.algolia.com/api/v1/search?query=codeg&tags=story - the search that found no story about this project (only codegen substring noise), the missing-footprint evidence, fetched 2026-10-11
