---
title: OpenCode skills and plugins
created: 2026-08-24
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, skills, plugins, opencode, agent-extensions]
readability: 3
audience_notes: >
  Engineers extending OpenCode who must choose between a SKILL.md folder and a TypeScript hook for a given problem.
  Assumes familiarity with the Agent Skills format and OpenCode's config layout.
---

OpenCode extends through two separate mechanisms: Agent Skills (SKILL.md folders surfaced to the model through a native `skill` tool, with per-skill permissions) and plugins (JavaScript or TypeScript modules that hook lifecycle events, loaded from local files or npm).
Facts below verified as of 2026-08-24.

**OpenCode splits extensibility cleanly where other harnesses blur it: declarative markdown for knowledge the model should follow, real code for behavior the harness must enforce, and that split is the pattern I would copy.**

## What it is

Skills load from `.opencode/skills`, `~/.config/opencode/skills`, and the Claude-compatible (`.claude/skills`) and agent-compatible (`.agents/skills`) paths, project and global, discovered by walking from the working directory up to the worktree root.
Frontmatter requires `name` and `description`, accepts `license`, `compatibility`, and `metadata`, and ignores unknown fields; names must match their directory.
The model loads a skill on demand by calling the `skill` tool, and permissions can allow, deny, or ask per pattern, be overridden per agent, or the tool can be disabled entirely.
Plugins are JS/TS modules from `.opencode/plugins` or npm (installed via Bun at startup) hooking events like `tool.execute.before`, `session.idle`, or `experimental.session.compacting`, and they can register custom tools.

## Status

**Active; the skills docs were last updated 2026-08-23.**
The host project (anomalyco/opencode) shows about 200k stars under MIT as of 2026-08-24.
The ecosystem page lists roughly 40 community plugins (Helicone, Sentry, Firecrawl, Tavily, Daytona sandboxing, subscription-auth bridges).
There is no first-party skill marketplace; distribution rides plain git or third parties like skills.sh.

## Strengths

- **It reads `.claude/skills` directly, so spec-subset Claude Code skills work unmodified.**
- The per-skill allow/deny/ask permission model is finer-grained than Claude Code's, which gates tools but not skill loads.
- Plugins do what markdown cannot: rewrite tool arguments, inject environment variables, replace compaction prompts, add tools.
- npm distribution reuses the normal JS supply chain (registry, lockfiles, audits).

## Cautions

- **Unknown frontmatter is ignored silently, so Claude Code extensions (`context: fork`, hooks in skills, `disable-model-invocation`) do nothing here; the Vercel CLI's compatibility matrix confirms OpenCode lacks both `context: fork` and hooks.**
- Skills load only through the model's judgment on the description; there is no documented explicit user invocation and no skill versioning.
- An npm plugin is arbitrary code executed at startup with your privileges; the docs' own examples (an `.env` read blocker) exist because that surface needs guarding.
- The config surface moves fast and the project carries breaking-change warnings, so pin versions.

## Pricing

Free and MIT; you pay model providers, or OpenCode Zen, for tokens.
**Skills and plugins cost nothing to install, though some community plugins wrap paid services (Firecrawl, Tavily) with their own billing.**

## Compared to

- Claude Code skills and plugins: richer skill frontmatter and bundled skills, but the extensions stay harness-locked.
- Codex skills and plugins: the same standard subset plus a universal plugin directory spanning ChatGPT and Codex.
- MCP servers (also supported here): choose plugins to change harness behavior, MCP to hand the model a new tool.

## Bottom line

**Recommended for teams standardizing on SKILL.md that still need real hooks; write skills for procedure, plugins for policy.**
Not for teams that need stable extension APIs between releases; the surface moves fast enough to break you.
My disagreeable claim: plugins, not skills, are OpenCode's actual differentiator, because every harness now reads the same SKILL.md subset, so choosing a harness on skills support alone is a mistake.

## See also

- [OpenCode](../opencode/index.md) - the harness this extends
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the spec OpenCode implements a subset of
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - where most of the format's richer features live
- [skills.sh](../skills-sh/index.md) - the third-party distribution layer for these skills
- [Crush](../crush/index.md) - the sibling harness from the same 2025 split, also reading a skills directory

## References

- https://opencode.ai/docs/skills/ - skill paths, frontmatter, permissions, the skill tool
- https://opencode.ai/docs/plugins/ - plugin model, event hooks, npm installation, custom tools
- https://opencode.ai/docs/ecosystem/ - community plugin inventory
- https://github.com/anomalyco/opencode - host project scale and MIT license, as of 2026-08-24
- https://agentskills.io/ - lists OpenCode among the standard's clients
- https://github.com/vercel-labs/skills - compatibility matrix (`context: fork` and hooks unsupported in OpenCode)
