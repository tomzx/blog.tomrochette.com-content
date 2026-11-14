---
title: OpenCode skills and plugins
created: 2026-08-24
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, skills, plugins, opencode, agent-extensions]
readability: 3
audience_notes: >
  Engineers extending OpenCode who must choose between a SKILL.md folder and a TypeScript hook for a given problem.
  Assumes familiarity with the Agent Skills format and OpenCode's config layout.
---

OpenCode extends through two separate mechanisms: Agent Skills (SKILL.md folders surfaced to the model through a native `skill` tool, with per-skill permissions) and plugins (JavaScript or TypeScript modules that hook lifecycle events, loaded from local files or npm).

**OpenCode splits extensibility cleanly where other harnesses blur it: declarative markdown for knowledge the model should follow, real code for behavior the harness must enforce, and that split is the pattern I would copy.**

## What it is

Skills load from `.opencode/skills`, `~/.config/opencode/skills`, and the Claude-compatible (`.claude/skills`) and agent-compatible (`.agents/skills`) paths, project and global, discovered by walking from the working directory up to the worktree root.
All frontmatter is optional at runtime, with `name`, `description`, and `metadata` documented and portability fields like `license` and `compatibility` accepted but not interpreted; as of 2026-11-07 the unified skills docs page no longer carries the OpenCode-1 disclaimer and documents the v2 surface directly: single-file skills, HTTP skill catalogs configured in `opencode.json`, ID-precedence discovery, explicit `@skill-id` prompt loads, and a `metadata.opencode/autoinvoke: false` (or `disable-model-invocation`) opt-out from the model-facing list.
The model loads a skill on demand by calling the `skill` tool, and permissions can allow, deny, or ask per pattern, be overridden per agent, or the tool can be disabled entirely.
Plugins are JS/TS modules from `.opencode/plugins` or npm (installed via Bun at startup) hooking events like `tool.execute.before`, `session.idle`, or `experimental.session.compacting`, and they can register custom tools.

## Status

**Active; the skills and plugins docs are maintained closely, both re-fetched unchanged in substance on 2026-11-14.**
The host project (anomalyco/opencode) shows about 213.3k stars under MIT as of 2026-10-13, and the v2 line is now the shipping release train: v2.2.0 through v2.3.0 published 2026-10-27 to 11-13 (v2.2.6 on 11-06, v2.2.7 on 11-10, v2.3.0 on 11-13), with the 1.x line quiet beside it since v1.19.5 (2026-10-28), after the v2 redesign had lived only in its own docs tree.
The ecosystem page lists 31 community plugins, 10 projects, and 2 agent collections under separate section headers (recounted 2026-11-14; the page states no count itself), the same 43 rows the 10-24 reading counted as "43 plugins" before the page was re-sectioned.
There is no first-party skill marketplace; distribution rides plain git or third parties like skills.sh.

## Strengths

- **It reads `.claude/skills` directly, so spec-subset Claude Code skills work unmodified.**
- The per-skill allow/deny/ask permission model is finer-grained than Claude Code's, which gates tools but not skill loads.
- Plugins do what markdown cannot: rewrite tool arguments, inject environment variables, replace compaction prompts, add tools.
- npm distribution reuses the normal JS supply chain (registry, lockfiles, audits).

## Cautions

- **Unknown frontmatter is ignored silently, so Claude Code extensions (`context: fork`, hooks in skills, `disable-model-invocation`) do nothing here; the Vercel CLI's compatibility matrix confirms OpenCode lacks both `context: fork` and hooks.**
- Skills load by model judgment on the description; the slash-command mechanism this note recorded on 2026-10-16 is gone from the docs, the 10-30 "OpenCode 1 uses no metadata keys" line is gone too (the unified page now documents the v2 surface directly), and the surviving opt-outs are the `opencode/autoinvoke`/`disable-model-invocation` keys plus explicit `@skill-id` prompting, so there is still no skill versioning.
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

## Changes

- 2026-08-24 - Created in the Skills category seed.
- 2026-08-26 - Restored the mandatory Not-for-Y bottom-line clauses in a review-driven maintenance pass.
- 2026-09-25 - Refreshed the volatile numbers (209,897 host stars; the ecosystem page, updated 2026-09-24, still lists roughly 40 plugins).
- 2026-10-16 - Rotation re-verification corrected the invocation claim: the skills docs now document `metadata` keys (`opencode/slash`, `opencode/autoinvoke`) that expose a skill as an explicit `/<name>` TUI command; every cited URL re-fetched live (39 plugins on the ecosystem page, docs pages updated 2026-10-15).
- 2026-10-24 - Rotation re-verification reversed the 10-16 invocation reading: the rewritten skills docs (last updated 2026-10-23) state OpenCode 1 uses no metadata keys for slash commands or automatic skill selection, and the new v2 docs tree documents the replacement surface (`opencode/autoinvoke: false` and `disable-model-invocation` opt-outs, explicit `@skill-id` prompt loads, HTTP skill catalogs, single-file skills); the ecosystem count moved to 43 plugins and the host release to v1.19.4 (2026-10-22).
- 2026-10-31 - The v2 line became the shipping release train: v2.2.0 through v2.2.5 published 2026-10-27 to 10-30 (the 1.x line still releasing v1.19.5 on 10-28), so the v2 redesign is no longer docs-only; the same rotation pass corrected the 10-24 ecosystem reading, finding the page re-sectioned into Plugins, Projects, and Agents, with 31 plugin rows plus 10 project and 2 agent entries (the same 43 rows previously counted as "43 plugins"); every cited URL re-fetched live and all other claims held.
- 2026-11-07 - Out-of-rotation correction on a moving source: the unified skills docs page no longer carries the "OpenCode 1 uses no metadata keys" disclaimer and now documents the v2 catalog surface directly (HTTP catalogs in opencode.json, `opencode/autoinvoke` and `disable-model-invocation` opt-outs, `@skill-id` loads, ID precedence, "all frontmatter is optional at runtime"); the What-it-is and caution lines re-grounded on today's fetch, conclusion unchanged, and every other cited URL re-fetched live with claims held.
- 2026-11-14 - Rotation re-verification: every cited URL re-fetched live; the release train moved to v2.3.0 (published 2026-11-13) via v2.2.6 and v2.2.7 with the 1.x line quiet since v1.19.5, the skills docs pages re-fetched unchanged in substance with the What-it-is frontmatter clause corrected to all-optional at runtime, the plugins docs reorganized config-first with a `plugin` CLI (claims held), the ecosystem counts held (31 plugins, 10 projects, 2 agents, recounted 11-14), and the Vercel CLI compatibility matrix still shows no `context: fork` or hooks support in OpenCode.

## See also

- [OpenCode](../../harnesses/opencode/index.md) - the harness this extends
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the spec OpenCode implements a subset of
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - where most of the format's richer features live
- [skills.sh](../skills-sh/index.md) - the third-party distribution layer for these skills
- [Crush](../../harnesses/crush/index.md) - the sibling harness from the same 2025 split, also reading a skills directory

## References

- https://opencode.ai/docs/skills/ - skill paths, frontmatter, permissions, the skill tool; the unified page as of 2026-11-14 documents the v2 catalog surface directly (HTTP catalogs, the autoinvoke and disable-model-invocation opt-outs, `@skill-id` loads) with no OpenCode-1 metadata disclaimer, and states all frontmatter is optional at runtime (re-fetched 2026-11-14, claims held)
- https://opencode.ai/v2/docs/skills/ - the v2 skills docs: HTTP catalogs, single-file skills, ID precedence, the autoinvoke/disable-model-invocation opt-outs, and explicit `@skill-id` loading (fetched 2026-10-24, re-fetched 2026-10-31 and 2026-11-14, identical content to the unified page)
- https://opencode.ai/docs/plugins/ - plugin model, event hooks, npm installation, custom tools (re-fetched 2026-11-14, claims held; the page is now organized around the `opencode.json` plugins array and a `plugin` add/list/check/update/remove CLI with version pinning)
- https://opencode.ai/docs/ecosystem/ - community inventory under Plugins, Projects, and Agents section headers: 31 plugin rows, 10 projects, 2 agent collections recounted 2026-11-14 (the page states no count)
- https://github.com/anomalyco/opencode - host project scale and MIT license as of 2026-10-24; release trains re-verified 2026-11-14 (v2.2.6 on 11-06, v2.2.7 on 11-10, v2.3.0 on 11-13, the 1.x line quiet since v1.19.5 on 10-28)
- https://agentskills.io/ - lists OpenCode among the standard's clients
- https://github.com/vercel-labs/skills - compatibility matrix (`context: fork` and hooks unsupported in OpenCode, re-fetched 2026-11-14, unchanged)
