---
title: Agent-Native
created: 2026-09-13
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, agent-extensions, builder-io, app-frameworks]
readability: 3
audience_notes: >
  Engineers picking a starter set of agent skills or wondering whether Builder.io's Agent-Native stack deserves a place in their harness.
  Assumes familiarity with SKILL.md packaging and at least one coding agent.
---

Agent-Native is Builder.io's two-piece ecosystem: an MIT TypeScript framework (github.com/BuilderIO/agent-native) for apps where the agent and the UI call the same actions, and a curated pack of fifteen skills (github.com/BuilderIO/skills) that wires coding agents into those apps and adds workflow disciplines.

**The pack is the half harness users meet first: fifteen SKILL.md directories that install anywhere the Agent Skills standard reaches, part workflow doctrine, part on-ramp to Builder.io's stack.**

## What it is

The framework defines each capability once as an action with a schema: the agent calls it as a tool, the UI calls it from code, and both paths get the same validation and permissions, exposed over HTTP, MCP, A2A, and a CLI.
The apps built on it (Slides, Plans, Mail, and a wider gallery) are what the bridge skills drive: `/an` opens a granted app beside the conversation, `/webmcp` prefers a page's MCP tools over browser automation.
The rest of the pack is portable doctrine: `/agent-watchdog` audits another agent's work, `/plan-arbiter` chooses between competing plans, `/read-the-damn-docs` forces a docs pass before guessing, `/stay-within-limits` pauses execution at 95% usage, with `/visual-plan` and `/visual-recap` as human review surfaces.
Install is `npx @agent-native/skills@latest add`, which writes to the shared `.agents` path (Codex, Pi, Cursor, OpenCode, Copilot) plus Claude Code's native path, and the catalog repo doubles as a Claude Code and Cowork plugin marketplace; the npm package itself publishes from the framework monorepo.

## Status

**Active and fast-moving, with a thin independent footprint.**
Both repos claim MIT in their READMEs: the skills catalog at 4.5k stars and 228 forks, the framework at 7.1k stars and 642 forks, as of 2026-10-06.

[![Star History Chart](https://api.star-history.com/chart?repos=BuilderIO/agent-native&type=date&legend=top-left)](https://www.star-history.com/?repos=BuilderIO%2Fagent-native&type=date&legend=top-left)

The npm package was created 2026-06-10, sits at 0.3.24 with builds shipping several times a day, and pulled 16,552 downloads in the week of 2026-09-28 to 2026-10-04 (fetched 2026-10-06).
No Hacker News threads and no independent coverage surfaced in this run's searches, so the audience so far is GitHub and npm.

## Strengths

- **The shared-action model sidesteps UI automation entirely: the agent never clicks, it calls the same validated function the UI calls.**
- Roughly half the pack is framework-independent judgment discipline (watchdog, plan arbiter, docs-first, usage limits) that runs in any SKILL.md harness for free.
- Cross-harness by construction: the shared `.agents` path and the Vercel CLI plain-copy route mean no harness lock-in at install time.

## Cautions

- **The pack's gravity is Builder.io's stack: `/an` registers the hosted Dispatch MCP endpoint, `/visual-plan` defaults to hosted share links (plan content to a hosted database, local-files mode is opt-in), and the installer offers managed AGENTS.md/CLAUDE.md instruction blocks.**
- 0.3.x with multiple releases a day is churn rather than stability, and the discipline skills are prompts, not enforcement, so whether `/plow-ahead` plows or stalls is model judgment.
- `/rewind` needs the separate signed Clips Desktop app on macOS with screen capture on your workstation; the install flow gates it, but it is capture software.
- The thin community footprint (no HN threads, no third-party reviews found as of 2026-09-22) means no independent security eyes yet.
- **The framework repo's license signal degraded just before this verification: GitHub no longer detects a license file there and its package.json now says ISC while the README still says MIT, so verify before relying on the MIT claim.**

## Pricing

Free.
Both READMEs say MIT (though the framework repo's GitHub license detection and package.json now disagree, see Cautions), the hosted Dispatch endpoint and plans hosting cost nothing today, and I found no paid tier as of 2026-09-22.

## Compared to

- skills.sh: the ecosystem's registry and ranking versus one vendor's curated pack with an opinionated installer; complementary, and skills.sh's plain-copy CLI installs this pack (minus `/rewind` configuration).
- Agent Skills open standard: the pack is spec-conformant SKILL.md directories, so it consumes the standard rather than competing with it.
- Anthropic Agent Skills: the other vendor pack, Claude-coupled where this one is cross-harness; both steer toward their vendor's surface.

## Bottom line

**Recommended as a cherry-pick source: take the discipline skills (`/agent-watchdog`, `/plan-arbiter`, `/read-the-damn-docs`) into any harness, and take the app bridges only if you actually use Agent-Native apps.**
Not for teams that refuse vendor-managed instruction blocks or hosted MCP endpoints in their agent config.
My disagreeable claim: the apps and the framework are the least durable half, the workflow-discipline skills would survive Builder's app bet failing, and the pack is an onboarding funnel wearing a toolbox costume.

## Changes

- 2026-09-13 - Created.
- 2026-09-22 - The framework repo jumped from 5.4k to 6.3k stars in one day, and its license signal degraded: GitHub no longer detects a license file there and package.json now says ISC while the README still says MIT.
- 2026-09-25 - Refreshed the volatile numbers (catalog 4,412 stars, framework 6,777 stars and 6,012 commits, GitHub license detection still absent) and recorded the npm package crossing to 0.3.1.
- 2026-09-26 - Recorded the npm package crossing to 0.3.5 and refreshed the volatile numbers (catalog 4,434 stars and 161 commits, framework 6,828 stars, 613 forks, and 6,114 commits); the framework repo's GitHub license detection is still absent.
- 2026-09-27 - Recorded the npm package crossing to 0.3.7 with weekly downloads up to 17,974 and refreshed the volatile numbers (catalog 4,443 stars, framework 6,849 stars, GitHub license detection still absent).
- 2026-09-29 - Recorded the npm package crossing to 0.3.10 with weekly downloads up to 24,886 and refreshed the volatile numbers (catalog 4,462 stars, framework 6,898 stars and 622 forks); the framework repo's GitHub license detection is still absent and its package.json still says ISC.
- 2026-10-03 - Recorded the npm package crossing to 0.3.22 with weekly downloads at 27,350 and refreshed the volatile numbers (catalog 4,511 stars and 227 forks, framework 7,043 stars and 636 forks); the framework repo's GitHub license detection is still absent and its package.json still says ISC.
- 2026-10-07 - Added the BuilderIO/agent-native star history chart to the Status section.

## See also

- [skills.sh](../skills-sh/index.md) - the registry layer this pack sits alongside
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the packaging spec the pack follows
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the other vendor pack in the category
- [MCP](../../protocols/mcp/index.md) - the protocol the hosted Dispatch endpoint and app bridges ride
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this category sits in

## References

- https://github.com/BuilderIO/skills - the catalog repo: the fifteen skills, installer options, marketplace packaging, 4.5k stars as of 2026-10-06
- https://github.com/BuilderIO/agent-native - the framework repo: shared-action architecture, app gallery, README says MIT but GitHub license detection still returns nothing (package.json says ISC), 7.1k stars as of 2026-10-06
- https://www.agent-native.com/ - the framework landing
- https://registry.npmjs.org/@agent-native/skills - package metadata: created 2026-06-10, latest 0.3.24, published from the monorepo, as of 2026-10-06
- https://api.npmjs.org/downloads/point/last-week/@agent-native/skills - 16,552 weekly downloads, window 2026-09-28 to 2026-10-04, fetched 2026-10-06
- https://hn.algolia.com/api/v1/search?query=%22builder.io%22%20skills&tags=story - the zero-hit search behind the missing-footprint statement
