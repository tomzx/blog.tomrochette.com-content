---
title: Anthropic Agent Skills
created: 2026-08-24
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, skills, anthropic, agent-extensions]
readability: 3
audience_notes: >
  Engineers who already drive Claude Code or the Claude API and are deciding whether to package team knowledge as skills.
  Assumes familiarity with CLAUDE.md-style context files and progressive disclosure.
---

Agent Skills is Anthropic's format for packaging reusable agent capabilities: a folder whose SKILL.md holds YAML metadata plus markdown instructions, with optional scripts and resources loaded on demand.
Facts below verified as of 2026-09-05.

**This is the packaging format that became the de facto industry standard, because Anthropic released it as an open standard two months after launch and OpenAI, Google, and the major third-party harnesses all adopted it.**

## What it is

A skill's frontmatter requires only `name` and `description`; the body holds instructions, and the folder can bundle scripts, references, and assets.
Loading follows progressive disclosure: metadata (about 100 tokens per skill) sits in the system prompt, the body loads when the model decides the skill is relevant, and bundled files load only when referenced.
**The same folder works across claude.ai paid plans, Claude Code (personal, project, enterprise, and plugin locations), and the API.**
The `anthropics/skills` repository ships the spec, a template, and example skills, mostly Apache 2.0, though the production document skills (docx, pdf, pptx, xlsx) are source-available rather than open source.

## Status

**Active and expanding.**
Launched 2025-10-16; on 2025-12-18 Anthropic published the format as the open Agent Skills standard (agentskills.io), added organization-wide skill management, and opened a partner directory.
The example repository shows 174.3k stars and 20.7k forks but only 54 commits as of 2026-09-05, which tells me it is a distribution artifact, not where the product is built.
Claude Code iterates fast on top: custom commands were merged into skills, and skill behavior changed across v2.1.196 through v2.1.218 (subagent execution, bundled-skill overrides, frontmatter parsing).

## Strengths

- **Progressive disclosure keeps long reference material nearly free until it is used, which always-loaded CLAUDE.md content cannot do.**
- One format spans chat, CLI, and API, with versioned skill management through the Skills API (`/v1/skills`).
- Skills can bundle executable scripts for steps where deterministic code beats token generation.
- The extracted open standard makes the same skill portable to Codex, Gemini CLI, OpenCode, Cursor, Copilot, and more.

## Cautions

- **Anthropic's own engineering post warns that malicious skills can direct exfiltration and recommends installing only from trusted sources; treating skill installs as a supply-chain decision is mandatory, not optional.**
- The spec allows six frontmatter fields while Claude Code accepts roughly twenty (`context: fork`, `disable-model-invocation`, `hooks`, `model`, `paths`), so skills using them silently degrade outside Claude Code.
- claude.ai upload and the Skills API hard-reject non-spec frontmatter, so a SKILL.md cannot carry Claude Code extensions onto those surfaces.
- API skills require the code execution tool and run in Anthropic's container, up to 20 skills per request, which couples the format to Anthropic's runtime.
- The document skills in the public repo are source-available, not open source.

## Pricing

The format is free; skills are content that ships with it.
**On subscriptions (Pro, Max, Team, Enterprise) skills are included; on the API you pay per token plus code execution.**
The example repo is Apache 2.0 except the source-available document skills.

## Compared to

- MCP: skills package procedures as files; MCP connects live tools and data; Anthropic positions them as complements, and I agree, most "which one" debates are category errors.
- CLAUDE.md and friends: always-in-context rules versus on-demand expertise.
- Plugins (Claude Code, Codex): distribution bundles that can contain skills plus hooks and MCP servers; heavier and harness-specific.

## Bottom line

**Recommended for any team on Claude surfaces with repeatable procedures worth versioning; not for one-off prompts, and not a substitute for MCP tools.**
The claim I will defend: for most teams skills matter more than plugins or MCP servers, because procedure is what a team actually accumulates, and a reviewed SKILL.md in git is more trustworthy than any marketplace install.

## See also

- [Claude Code](../claude-code/index.md) - the harness that gave this format its largest distribution surface
- [Teach Your Agent Skills to Use Tools That Render](../../agent-skills-that-render/index.md) - a corpus pattern for making skill output verifiable
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where the skills layer sits in the harness map

## References

- https://claude.com/blog/skills - launch announcement (2025-10-16) and the 2025-12-18 open-standard update
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - progressive disclosure architecture, code execution, security guidance
- https://code.claude.com/docs/en/skills - Claude Code surfaces: locations, bundled skills, spec versus extension frontmatter
- https://github.com/anthropics/skills - example repo scale and license split, 174.3k stars as of 2026-09-05
- https://docs.claude.com/en/api/skills-guide - Skills API: container parameter, 20 skills per request, code execution requirement
- https://agentskills.io/ - the extracted open standard and its client showcase
