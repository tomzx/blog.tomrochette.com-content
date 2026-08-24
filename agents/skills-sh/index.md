---
title: skills.sh
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, skills, registries, vercel, agent-extensions]
readability: 3
audience_notes: >
  Engineers choosing where to discover and install SKILL.md packages across several agent harnesses.
  Assumes familiarity with the Agent Skills format and npm-style CLIs.
---

skills.sh is Vercel's directory and leaderboard for the open skills ecosystem: it ranks SKILL.md packages by install telemetry from its open-source CLI (`npx skills add <owner>/<repo>`), which installs into more than 70 agent harnesses.
Facts below verified as of 2026-08-24.

**It won the registry slot not through curation but by wrapping git: any repository is already a package, the CLI symlinks it into every harness, and the resulting install counts became the ecosystem's ranking, with security review still catching up.**

## What it is

Launched 2026-01-20 by Vercel's labs team; the CLI is MIT-licensed with 29.5k stars, 2.5k forks, and 474 commits as of 2026-08-24.
The CLI resolves GitHub shorthand and URLs, GitLab, any git URL, local paths, and direct archive URLs (downloads capped at 10 MiB by default), then symlinks or copies skills into per-agent directories.
The site adds the leaderboard, per-agent and per-topic pages, badges, and packs (one install command bundling public and private skills).
**Ranking comes from anonymous CLI telemetry (opt-out via `DISABLE_TELEMETRY`), not from vetting or ratings.**

## Status

**Active and dominant among third-party registries.**
Top of the all-time leaderboard as of 2026-08-24: find-skills (vercel-labs) at 3.1M installs, grill-me (mattpocock/skills) at 946.4K, frontend-design (anthropics/skills) at 810.5K.
Official publisher entries include microsoft/azure-skills, supabase, prisma, and heygen-com/hyperframes.
The nearest standalone competitor I could verify, skillregistry.io, lists 61 skills and 14,782 total downloads as of 2026-08-24, two orders of magnitude smaller.

## Strengths

- **One command, every harness: the per-agent path table means a single install reaches Claude Code, Codex, Cursor, OpenCode, Copilot, Gemini, and dozens more.**
- Zero publishing step: the registry indexes git itself, including `.claude-plugin` manifests, so there is no upload surface to go stale.
- Per-skill security columns aggregate Gen Agent Trust Hub, Socket, and Snyk results directly on the page.

## Cautions

- **Install counts measure fashion, not fitness: telemetry counts CLI runs, anyone can drive their own numbers, and the docs state plainly that the quality and security of listed skills are not guaranteed.**
- The audit page shows the gap: every open.feishu.cn entry was still Pending, and Snyk flags Critical on microsoft/azure-skills azure-validate and High on azure-resource-visualizer as of 2026-08-24.
- Skills are instructions and scripts that agents execute, a risk Anthropic's engineering post calls out for skills generally, so a leaderboard install is a supply-chain decision.
- Telemetry is opt-out rather than opt-in, and one company controls the ranking surface of a nominally open ecosystem.

## Pricing

Free.
**The directory and CLI cost nothing, the CLI is MIT, and I found no paid placement or paid tier; skills carry their own licenses.**

## Compared to

- Vendor directories (Anthropic's partner directory, the ChatGPT/Codex plugin directory): curated and trusted, but single-ecosystem.
- skillregistry.io: a hosted upload registry pitched as "Dockerhub for Skill.md", with 61 skills as of 2026-08-24, tiny by comparison.
- Skilleton: lockfile-based, telemetry-free skill management that pins skills to commits, built explicitly as a critique of install-count culture.

## Bottom line

**Recommended as the discovery layer for cross-harness teams, provided you pin commits and read the SKILL.md before it touches a repo with production secrets.**
My disagreeable claim: marketplaces are the least interesting part of this ecosystem, the ten skills your team writes itself will beat the leaderboard's top ten, and I would not let an agent auto-install from it.

## See also

- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format this registry distributes
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the largest publisher on the leaderboard
- [OpenCode](../opencode/index.md) - one of the many harnesses the CLI installs into
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the distribution layer sitting over the harness map

## References

- https://vercel.com/blog/introducing-skills - launch announcement (2026-01-20)
- https://skills.sh/ - leaderboard, install counts, supported agents, as of 2026-08-24
- https://skills.sh/docs - ranking method (CLI telemetry) and the security disclaimer
- https://skills.sh/audits - Gen/Socket/Snyk audit columns, Pending and Critical entries, as of 2026-08-24
- https://github.com/vercel-labs/skills - CLI source, agent path table, telemetry opt-out, 29.5k stars as of 2026-08-24
- https://skillregistry.io/ - nearest standalone competitor, 61 skills as of 2026-08-24
- https://github.com/Fcmam5/skilleton - lockfile-style, no-telemetry alternative
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the underlying untrusted-skill risk
