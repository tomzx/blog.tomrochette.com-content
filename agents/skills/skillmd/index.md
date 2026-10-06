---
title: SkillMD
created: 2026-10-05
updated: 2026-10-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, registries, skill-verification]
readability: 3
audience_notes: >
  Engineers choosing where to discover and install SKILL.md packages when the install decision is also a security decision.
  Assumes familiarity with the Agent Skills format and npm-style CLIs.
---

SkillMD is an open skills registry at skillmd.com that indexes public SKILL.md files at scale and differentiates on published verification: per-skill lint verdicts, capability flags, and third-party scanner results (NVIDIA SkillSpector and Cisco AI Defense Skill Scanner) shown on each skill page, installable through its own MIT CLI, MCP server, Claude Code plugin marketplace, or GitHub Action.

**The verification-first registry now operates at the scale where it competes with skills.sh, but its verified core is a rounding error of its index: 1,948 safety-reviewed skills out of about 1.13 million listed as of 2026-10-05, so the verdict badge is an aspiration, not a guarantee.**

## What it is

The registry (skillmd.com) crawls and accepts SKILL.md files and reports 1,132,702 skills from 30,609 authors as of 2026-10-05.
The toolchain (github.com/skillmds/skillmd, MIT) is what runs on your machine: a `skillmd` CLI (npm `skillmds`, v1.3.3, 2,102 downloads in the month to 2026-10-03), an MCP server (`npx -y skillmds`), a Claude Code plugin marketplace, and a GitHub Action, plus a JSON search API and OAuth-protected endpoints aimed at agents.
Skills land in each detected agent's own directory (`.claude/skills/`, `.cursor/skills/`, `.agents/skills/`), and every listed skill is pinned to a commit.
The maintainer also publishes the ecosystem's most self-critical data: their directory-landscape post estimates 83.4 percent of indexed skills declare no license and roughly 47 percent of public SKILL.md files are byte-identical copies of another file.

## Status

**Active and growing, with a thin independent footprint.**
The toolchain repo was created 2026-08-25 and shows 1 star and 8 open issues, pushed 2026-09-29; the npm CLI has shipped 33 versions since 2026-06-29.
The site's own claimed index grew from 860,000 skills (its September 19 directory post) to 1,132,702 as of 2026-10-05, and that post itself warns that directory counts are claims, not measurements, skills.sh included.
No Hacker News thread surfaced under its name in my searches as of 2026-10-05; the largest near-match is the 48-point "Skill.md: An open standard" story about the format, not this registry.
The business model is unstated; installing needs no account and the site quotes no price.

## Strengths

- **It is the only directory of its size that publishes what it checked and how, per skill, instead of a claimed security stance.**
- Install paths that go beyond a copy button: CLI, MCP server, plugin marketplace, and CI action, all writing into the agents' native skills directories.
- Agent-facing surface: JSON API, OpenAPI spec, `.well-known` agent-skills index, and an MCP server card, so an agent can search and install without a human.
- The self-published ecosystem data (license gaps, duplication rates) is decision-useful even for people who never install from it.

## Cautions

- **The safety-review claim does not survive contact with its own numbers: the homepage says every skill passes a safety review before it becomes publicly visible, while the same page reports 1,948 reviewed out of 1,132,702 listed, so treat the verdicts as a curated subset, not a property of the catalog.**
- The toolchain repo's 1 star and the near-zero HN footprint mean no independent security eyes on the verification pipeline itself.
- Its blog states Agent Skills is stewarded through the Agentic AI Foundation, but the AAIF's own project list carries AGENTS.md, MCP, goose, and agentgateway, not Agent Skills, so treat the blog's ecosystem claims as unverified.
- Index counts are self-reported and the site says so itself; the 860k-to-1.13M jump in two weeks is crawl churn as much as ecosystem growth.
- A registry this young is one team's roadmap; skills.sh at least has Vercel behind it.

## Pricing

Free.
**No account is needed to search or install, the toolchain is MIT, and the site quotes no paid tier as of 2026-10-05.**

## Compared to

- skills.sh: the telemetry-ranked incumbent; SkillMD trades usage signal for published verification, and both index the same public GitHub repositories.
- skillregistry.io: the hosted upload registry positioning itself as definitive; tiny, no published method, and orders of magnitude smaller than either.
- Skilleton: the lockfile-based, telemetry-free manager; SkillMD is the hosted-registry version of the same verification-first instinct.

## Bottom line

**Recommended as a second opinion before installing an unfamiliar skill: search it there, read the lint and scanner verdicts, then pin the commit.**
Not as a replacement for reading the SKILL.md yourself, and not because its catalog is bigger or safer at scale, because neither is demonstrated.
My disagreeable claim: SkillMD's 1,948 reviewed skills matter more than either registry's million-skill index, and the winner of this layer is whoever verifies the long tail, not whoever crawls it.

## Changes

- 2026-10-05 - Created in the daily refresh's skills entrant scan.

## See also

- [skills.sh](../skills-sh/index.md) - the telemetry-ranked incumbent registry
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format every directory indexes
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the vendor pack and partner directory
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this distribution layer sits over

## References

- https://skillmd.com/ - the registry surface: 1,132,702 skills, 1,948 safety-reviewed, 30,609 authors, API and MCP endpoints (fetched 2026-10-05)
- https://github.com/skillmds/skillmd - the toolchain repo: MIT, 1 star, 8 open issues, created 2026-08-25, pushed 2026-09-29 (GitHub API, as of 2026-10-05)
- https://raw.githubusercontent.com/skillmds/skillmd/main/README.md - CLI, MCP server, plugin marketplace, GitHub Action, per-agent install directories
- https://skillmd.com/blog/agent-skills-directories-compared - the self-critical directory landscape post: 47 percent byte-identical duplication, 83.4 percent license gaps, counts-as-claims disclaimer (September 19, 2026, fetched 2026-10-05)
- https://registry.npmjs.org/skillmds - CLI package: latest 1.3.3, 33 versions, created 2026-06-29 (fetched 2026-10-05)
- https://api.npmjs.org/downloads/point/last-month/skillmds - 2,102 downloads, window 2026-09-04 to 2026-10-03 (fetched 2026-10-05)
- https://hn.algolia.com/api/v1/search?query=skillmd&tags=story - the footprint scan behind the missing-footprint statement (fetched 2026-10-05)
