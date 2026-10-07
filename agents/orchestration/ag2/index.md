---
title: AG2
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python, fork, autogen]
readability: 3
audience_notes: >
  Engineers maintaining AutoGen-lineage code or choosing a multi-agent framework,
  who need to know which fork of the AutoGen story is alive and who backs it.
  Assumes basic Python and familiarity with the AutoGen name.
---

AG2 is the community-run fork of AutoGen that continued the original line as an open-source AgentOS after Microsoft froze AutoGen and pointed its users at Microsoft Agent Framework.

## What it is

The repository, created 2024-11-11, describes itself as "AG2 (formerly AutoGen)" and continues the conversational multi-agent framework that Microsoft's original project abandoned to the v0.4 rewrite and later the Microsoft Agent Framework merge.
It is Apache-2.0, Python-first, installable as `ag2` from PyPI, and documents itself at docs.ag2.ai with a playground and examples repository beside it.
For this category it fills the successor slot on the community side of the AutoGen story: the [AutoGen](../autogen/index.md) note records the vendor path, this note records the fork path.

## Status

Active and shipping: 4,979 stars, a push on 2026-10-06, release v1.1.2 on 2026-10-03, and `ag2` 1.1.2 on PyPI as of 2026-10-07 (GitHub API, PyPI), on a repository created 2024-11-11.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ag2ai/ag2&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ag2ai/ag2&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ag2ai/ag2&type=date&theme=dark&legend=top-left" />
</picture>

**The launch footprint is nearly invisible, a 2-point Hacker News thread in November 2024, so the fork's adoption spread through the existing AutoGen community rather than through press, and its roughly 5k stars measure inherited mindshare more than new converts.**
Three names now cover one lineage (AutoGen, AG2, Microsoft Agent Framework), and the maintenance-mode badge on the upstream is what makes AG2 the live community line rather than a rival.

## Strengths

- Continuity for AutoGen 0.2-era and v0.4-era codebases that do not want to migrate to Microsoft Agent Framework.
- Active releases and PyPI publishes on a steady cadence through 2026.
- Clean Apache-2.0 licensing with no commercial gate on the framework itself.

## Cautions

- Identity confusion is the operating cost: three projects share the AutoGen story, and search results mix them freely.
- The fork's governance and backing are thinner than the vendor successor's, which matters for teams that need long-term support promises.
- Community momentum flows to the framework with the most docs and hiring, and Microsoft owns that side of the split.

## Pricing

Free, open source under Apache-2.0; no paid tier found.

## Compared to

AutoGen upstream is the frozen project this fork continues; read its note for the maintenance-mode record.
Microsoft Agent Framework is the vendor successor with the enterprise support path; choose it when vendor backing outweighs migration cost.
CrewAI is the role-based alternative when crews and roles fit better than conversation-based agents.

## Bottom line

Recommended for teams holding AutoGen-lineage code who want the community line to keep moving without a vendor migration.
Not for greenfield projects that can pick a single supported path from day one.

## Changes

- 2026-10-07 - Created.

## See also

- [AutoGen](../autogen/index.md) - the frozen upstream whose maintenance-mode declaration is the reason this fork exists.
- [CrewAI](../crewai/index.md) - the role-based alternative in the same Python framework family.
- [CAMEL](../camel/index.md) - the other 2023-lineage framework that kept shipping while AutoGen froze.
- [Agno](../agno/index.md) - the AgentOS-positioned platform competing for the same "operating system for agents" framing.

## References

- https://github.com/ag2ai/ag2 - the repository, its "formerly AutoGen" framing, stars, license, and release line.
- https://docs.ag2.ai/ - the project documentation.
- https://www.ag2.ai/ - the project site and playground links.
- https://pypi.org/project/ag2/ - the PyPI package and its current 1.1.2 version.
- https://news.ycombinator.com/item?id=42131736 - the 2-point November 2024 launch thread, the record of how little press attention the fork got.
