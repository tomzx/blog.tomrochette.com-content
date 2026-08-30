---
title: Kilo Code
created: 2026-08-27
updated: 2026-08-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, open-source, vscode, byok]
readability: 3
audience_notes: >
  Engineers who liked Roo Code or Cline and want to know which branch of that lineage is alive.
  Assumes you know what a VS Code extension agent is and what BYOK billing means.
---

Kilo Code is an open-source (MIT) agentic coding assistant for VS Code, JetBrains IDEs, and the terminal, born in early 2025 as a feature-merge fork of Cline and Roo Code and acquired by Anaconda on July 15, 2026.
Facts below verified as of 2026-08-30.

**Kilo Code is the live continuation of the Roo-and-Cline extension lineage now folded into an enterprise Python vendor's portfolio, and the open question after that acquisition is whether extension-first users keep first-class status.**

## What it is

One MIT codebase delivered as VS Code and JetBrains extensions plus a CLI, carrying the Plan/Act discipline, approval gates, checkpoints, and rule-file conventions of its two ancestors.
The docs stack superset features on top: custom subagents (built-in ones included), MCP servers, skills with remote paths, hooks, git worktrees per task, cloud agents and tasks, and a schedule builder that compiles to raw cron.
Rules are portable: it reads AGENTS.md natively, supports `.kilocoderules`, and imports `.cursorrules` and `.windsurfrules`.
Any-model BYOK works alongside Kilo's own metered credits, with local models via Ollama or LM Studio documented.

## Status

**Active under new ownership.**
The repository shows about 27k stars under MIT as of 2026-08-27 and was pushed the same day; component tags ship on their own clocks (a JetBrains plugin tag landed the day of verification).
Anaconda announced the acquisition on July 15, 2026 and already lists Kilo among its products; kilocode.ai redirects to kilo.ai, where the vendor positions it as an all-in-one agentic engineering platform.

## Strengths

- **The broadest feature surface of any editor-native open agent in this section**: subagents, cloud tasks, scheduled runs, hooks, skills, worktrees in one install.
- AGENTS.md-first rules portability eases moving between harnesses.
- Documentation depth is unusual: hundreds of pages including troubleshooting and cost-control guides.
- A genuinely free usage path exists, not just a trial.

## Cautions

- **Popularity claims are ahead of observable evidence**: the repo calls itself "the most popular open source coding agent", but its star count trails Cline and OpenCode by wide margins as of verification, so treat installs-dependent claims as marketing until independently confirmed.
- Acquisition direction risk: Anaconda sells enterprise governance, so priorities may drift from extension developers toward platform buyers.
- Brand churn during the transition (Kilo Code to Kilo, domain move) means links and guidance written before July 2026 rot fast.
- Community footprint stayed modest across five launches: the biggest thread remains the 98-point March 2025 speedrun launch, and the acquisition drew 16 points in July 2026.

## Pricing

Free and open source for individuals; model usage is billed separately via your own keys or prepaid Kilo credits.
Teams: $15/user/month adding shared agent modes, analytics, centralized billing, and shared BYOK.
Enterprise: custom SSO/OIDC/SCIM, audit logs, private gateway, SLAs.
Costs split three ways (platform plan, AI inference, cloud compute), quoted separately.

## Compared to

- [Roo Code](../roo-code/index.md): the ancestor kept here as a sunset record; where Roo pivoted away, Kilo carried the extension forward.
- [Cline](../cline/index.md): the other parent lineage, leaner and more conservative; Kilo bets on supersets, Cline on restraint.
- [Claude Code](../claude-code/index.md): the integrated-platform rival; choose Kilo when you want editor-native control on your own keys.

## Bottom line

**Recommended for engineers who want the Cline-Roo toolset with every modern agentic attachment, under MIT, in the editor they already use.**
Not for teams needing a stable multi-year vendor story right now, because ownership just changed twice in effect (product into Anaconda, brand into Kilo), and I would let the post-acquisition roadmap settle before standardizing on it.

## See also

- [Roo Code](../roo-code/index.md) - the ancestor's sunset record, the before-picture of this note
- [Cline](../cline/index.md) - the sibling lineage that stayed independent
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - where this column sits against the other twelve harnesses
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map that places this consolidation

## References

- https://github.com/Kilo-Org/kilocode - repository scale, license, description as of 2026-08-27
- https://kilo.ai/pricing - tiers, credit model, and the Anaconda acquisition banner
- https://www.anaconda.com/blog/anaconda-acquires-kilo-code - the acquisition announcement primary source
- https://news.ycombinator.com/item?id=43483802 - the launch-era community record (98 points)
- https://news.ycombinator.com/item?id=43951329 - the feature-merge origin naming Cline and Roo
- https://news.ycombinator.com/item?id=48923038 - the acquisition discussion thread
