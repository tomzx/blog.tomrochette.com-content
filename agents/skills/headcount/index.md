---
title: Headcount
created: 2026-09-27
updated: 2026-10-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, claude-code, agent-organization, plugin-marketplace]
readability: 3
audience_notes: >
  Engineers structuring a multi-agent Claude Code or ChatGPT setup who want departments and ownership boundaries instead of one flat pile of prompts.
  Assumes familiarity with SKILL.md files and Claude Code plugin marketplaces.
---

Headcount is an MIT-licensed plugin marketplace for Claude Code and ChatGPT that organizes 172 skills into 16 corporate departments under a chief executive, each department independently installable and addressed as `department:skill`.

**The real discipline is not the org chart, it is the exclusive-write-surface rule underneath it: agents split by which paths they own rather than by topic, and CI enforces one owner per path.**

## What it is

A Markdown-only repository built by Chris Brock, packaged as sixteen plugins plus a searchable org chart page on GitHub Pages.
Skills load on request match (`security:threat-modeling`, `finance:unit-economics`) or by direct invocation (`/finance:financial-modeling`), so a project installs only the departments it needs.
Security and Legal & Risk are reviewer-class: their blocking findings cannot be overruled by the department under review, which is why they report to the chief executive.
Skills that answer questions an outside authority settles cite those authorities, 184 sources so far, each annotated with what you may legally do with it (125 of the 184 are quotable).
Each department also ships an agent charter in `.claude/agents/`, so a department can be delegated to as a subagent with its own write surface.

## Status

Active: 1,966 stars and 309 forks as of 2026-10-05, created 2026-08-28, repo pushed 2026-09-17, no releases or version tags yet.
The skill count keeps moving: a third-party count found 143 skills on August 30, press coverage said 146 on August 31, and the README now claims 172 across the same 16 departments.
No Hacker News thread surfaced under its name in my searches as of 2026-10-04; traction is GitHub, the org chart page, and third-party writeups.
One external contribution (ChatGPT and Codex manifests) is credited in the README.

## Strengths

- **The write-surface split is checkable in a way topic splits are not: `docs/AGENT-SURFACES.md` maps every path to one owner and `scripts/check-all.sh` fails the change when the map drifts.**
- Per-department installation keeps the context small, which is the standard failure mode of every mega-repo of prompts.
- Department namespacing kills skill-name collisions outright, without needing a registry.
- The sources catalog states usage rights per authority, which most citation lists never bother to record.
- Documentation discipline is unusual for the genre: decision log, worked use cases, generated README, weekly link checks.

## Cautions

- **Reviewer-class is prompt engineering, not enforcement: nothing in the repository can actually stop a model from writing a file, and the Zentor review reads the blocking findings correctly as strong defaults rather than controls.**
- The counted numbers drift between the GitHub description (15+ departments, 125+ skills), the badges (16 and 172), and third-party counts, so quote the README tables, not the description.
- The value is unproven without the boring test: run a task with and without a department installed and diff the transcripts; several skills may restate what the model already does.
- Installing all sixteen departments rebuilds the context bloat the per-department design was meant to avoid.
- Single maintainer, no releases, eighteen days without a push as of 2026-10-05, so treat it as a snapshot, not a product.

## Pricing

Free.
MIT licensed, no paid tier, no account; you still pay for the Claude Code or ChatGPT subscription the skills run inside, as of 2026-09-27.

## Compared to

- Agent-Native: Builder.io's pack sells a vendor app stack with workflow doctrine on the side; headcount sells a neutral corporate taxonomy with no product behind it.
- Anthropic Agent Skills: the format and marketplace mechanism headcount packages itself for.
- skills.sh: discovery and ranking for the open skills ecosystem; headcount is a curated org inside that ecosystem, findable there rather than competing with it.

## Bottom line

Recommended as a cherry-pick source: take the write-surface rule and the reviewer-class pattern even if you never install a department.
Worth installing whole if you run a one-person company through Claude Code and want territory-based routing with cited authorities.
Not for teams that need actual enforcement, audit trails, or versioned releases, because none exist here.
My disagreeable claim: the sixteen-department metaphor is mostly packaging, the two reviewer-class departments and the surface map are the parts that would survive, and the other fourteen are a well-edited prompt library wearing a reporting line.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars candidates were processed.

## See also

- [Agent-Native](../agent-native/index.md) - the other curated pack in this category, vendor funnel versus neutral org chart
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the SKILL.md format and marketplace mechanism headcount is built from
- [skills.sh](../skills-sh/index.md) - the registry layer where packs like this are discovered and ranked
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the packaging spec the department skills follow
- [Claude Code](../../harnesses/claude-code/index.md) - the primary harness the marketplace installs into

## References

- https://api.github.com/repos/cbrock84/headcount - 1,966 stars, 309 forks, MIT, pushed 2026-09-17 (200, fetched 2026-10-05)
- https://raw.githubusercontent.com/cbrock84/headcount/main/README.md - 16 departments, 172 skills, 184 cited sources, reviewer-class rules, CI checks (200)
- https://zentor.ai/blog/headcount-claude-code - third-party review (August 30, updated September 24) with critical readings of reviewer-class and star counts (200)
- https://cbrock84.github.io/headcount/org-chart.html - the searchable org chart page, generated from the repo tree (200)
- https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-31-an-entire-agent-company-org-chart-shipped-as-a-claude-code-p - press writeup (August 31, 146 skills) that calls the early attention unproven (200)
- https://hn.algolia.com/api/v1/search?query=headcount&tags=story - the zero-hit search behind the missing-footprint statement (200, fetched 2026-09-27)
