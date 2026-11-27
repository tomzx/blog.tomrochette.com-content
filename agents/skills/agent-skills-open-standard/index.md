---
title: Agent Skills open standard
created: 2026-08-24
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, skills, agent-extensions, open-standards, llm=glm-5.3-flash, llm=glm-5.4]
readability: 3
audience_notes: >
  Engineers writing SKILL.md packages meant to run in more than one agent harness.
  Assumes familiarity with at least one coding agent and its context files.
---

The Agent Skills open standard (agentskills.io) defines an agent capability as a directory containing a SKILL.md: required `name` and `description` frontmatter, optional `license`, `compatibility`, `metadata`, and `allowed-tools`, then markdown instructions, with scripts, references, and assets as optional neighbors.

**The standard spread faster than MCP because it is only files: no runtime, no protocol, no server, so a harness can implement it in an afternoon, and by mid-2026 OpenAI, Google, and the major third-party harnesses all had.**

## What it is

The format was developed by Anthropic, released as an open standard on 2025-12-18, and is stewarded publicly on GitHub (agentskills/agentskills) with a Discord and a `skills-ref` validation library.
Packaging rules are minimal: name is 1-64 lowercase-hyphen characters matching the directory, description is 1-1024 characters, and the body is unrestricted markdown, recommended under 500 lines and 5k tokens.
Discovery is by directory convention: each harness scans its own skills paths (`.claude/skills`, `.opencode/skills`, `.gemini/skills`), with `.agents/skills` emerging as the cross-tool path (Codex repo and user locations, Gemini CLI aliases), and Cursor now scans it natively alongside `.cursor/skills` plus the Claude and Codex directories per its own docs (fetched 2026-10-05).
**Invocation is either explicit (slash commands, `$`, `@`) or implicit, the model matching the task against one description line.**

## Status

**Active, and effectively the winner.**
The agentskills.io client showcase lists Claude and Claude Code, ChatGPT and Codex, Gemini CLI, Cursor, GitHub Copilot and VS Code, OpenCode, Amp, Goose, Junie, Roo, Kiro, Trae, and dozens more (the roster's markdown render went client-side by 2026-11-19; the names remain in the page's HTML).
The format has also reached the review layer: CodeRabbit's changelog (November 19, 2026, fetched 2026-11-25) says a SKILL.md in an agent's skills folder at the repository root, such as `.claude/skills/code-review/SKILL.md`, is read automatically as a code guideline that applies to the whole repository, so a SKILL.md written for a coding agent now steers a third-party reviewer's comments too.
Vercel's skills CLI installs into 79 agents as of 2026-11-19 (re-counted from the agent table, which moved from the README to docs/agents.md; still 66 rows naming 79 individual `--agent` targets, and the README headline still agrees at four named agents plus "75 more").
Mintlify now auto-generates a skill at `.well-known/skills/default/skill.md` for every docs site it hosts and deprecated its January 2026 install.md convention in favor of skills.
A package maintainer's field report agrees on mechanism: Backpack for Laravel's 2026-10-20 post ranks a Laravel Boost plugin (guidelines and per-topic skills injected into the agent's context at install and matched to the installed version) as its biggest win over a docs MCP server and llms.txt, because the agent does not have to decide to fetch what is already in context when work starts.

## Strengths

- **Git-native: skills version, review, and diff like code, and no registry is required to distribute them.**
- Progressive disclosure bounds the cost: metadata is about 100 tokens at startup, and Codex caps the entire initial skill list at 2% of the context window (8,000 characters when unknown).
- Real vendor adoption: Microsoft, Supabase, Prisma, Vercel, and Anthropic ship official skills, visible on skills.sh.

## Cautions

- **The spec standardizes packaging, not behavior: whether a skill fires is model judgment over one description line, so the same skill behaves differently per harness and per model.**
- Frontmatter fragmentation: Claude Code-only fields (`context: fork`, hooks in skills) and Codex's `agents/openai.yaml` live outside the spec, the Vercel CLI's compatibility matrix shows `context: fork` working in Claude Code alone, and Cursor now accepts its own extras (`paths`, `disable-model-invocation`, `icon`, `color`) beyond the spec's six, so the portable core keeps shrinking relative to what each harness actually reads.
- Security posture varies wildly: Gemini CLI asks user consent before injecting a skill and granting it file access, OpenCode supports per-skill allow/deny/ask patterns, Claude Code sanitizes synced skills, and Codex adds enterprise skill controls; Anthropic's own engineering post frames the underlying problem as executing untrusted packages.
- The spec has no versioning or dependency story; third parties (skills.sh, Skilleton) bolt their own on top.

## Pricing

Not applicable.
**The specification, the docs, and the validator are free and open.**

## Compared to

- MCP: a protocol for live tool and data connections versus files of procedure; complementary by design.
- AGENTS.md and CLAUDE.md: always-in-context rules versus on-demand expertise.
- Plugins (Claude Code, Codex, OpenCode): distribution bundles that can contain skills plus hooks and MCP servers, at the cost of harness-specific formats.

## Bottom line

**Recommended as the default packaging for any procedure you want an agent to repeat.**
Not for live tool and data connections or anything needing runtime guarantees, which is what MCP is for.
My disagreeable claim: SKILL.md is quietly becoming the interface between software vendors and agents, and any docs team without a published skill file will be effectively invisible to coding agents by 2027.

## Changes

- 2026-08-24 - Created in the Skills category seed.
- 2026-08-26 - Restored the mandatory not-for bottom-line clause and added Anthropic's untrusted-skills engineering post as its critical source.
- 2026-10-05 - Cursor's own docs now document native Agent Skills support (`.agents/skills` plus `.cursor/`, `.claude/`, and `.codex/` paths, `paths` and `disable-model-invocation` frontmatter, `/skill` invocation, and a `/migrate-to-skills` built-in in 2.4), so the discovery sentence no longer treats Cursor as a Vercel-CLI-only adopter and the fragmentation caution reflects Cursor's beyond-spec fields.
- 2026-10-06 - Added Agent Plugins to See also: the multi-vendor packaging standard that bundles this format with MCP servers into one installable plugin; the 79-agent README count re-verified.
- 2026-10-08 - The Vercel CLI's agent-target count moved back to 79, with the README headline and table now agreeing, correcting the 80 recorded on 2026-10-07.
- 2026-10-24 - Rotation re-verification: every cited URL re-fetched live and all claims held (the spec's field limits and 500-line recommendation, the client showcase roster, Codex's 2%-of-context cap, Gemini's consent gate, OpenCode's ignore-unknown-fields behavior, Cursor's beyond-spec fields, Mintlify's .well-known convention and install.md deprecation, the Vercel CLI at 79 agents).
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched live and all claims held again (the spec's six fields with the name rules and 500-line recommendation, the Codex 2%-of-context cap with its new skills.max_context_tokens override, Gemini's consent gate and .agents/skills alias with the Antigravity-transition banner now on the docs, OpenCode's ignore-unknown-fields line, Mintlify's convention and deprecation, Cursor's beyond-spec fields with nested-directory scoping added, the Vercel CLI README still naming four agents plus 75 more, and Anthropic's untrusted-skill guidance); no claims moved.
- 2026-11-07 - Rotation re-verification: every cited URL re-fetched live and all claims held a fourth time (the spec's six fields with the name rules and the 500-line recommendation unchanged, the client showcase roster live, the Codex 2%-of-context cap with the skills.max_context_tokens override documented, Gemini's consent gate and .agents/skills alias with the Antigravity-transition banner still up, OpenCode's permission model and @skill-id loads with the unified docs page now carrying the v2 catalog surface, Mintlify's .well-known convention and install.md deprecation, Cursor's beyond-spec fields and /migrate-to-skills in 2.4, the Vercel CLI README still naming four agents plus 75 more, and Anthropic's untrusted-skill guidance); no claims moved.
- 2026-11-13 - Rotation re-verification: every cited URL re-fetched live and all claims held a fifth time (the spec's six fields with the name rules and the 500-line recommendation unchanged, the client showcase roster live, the Codex 2%-of-context cap with the skills.max_context_tokens override documented, Gemini's consent gate and .agents/skills alias with the Antigravity-transition banner still up, OpenCode's permission model, v2 catalog surface, and @skill-id loads, Mintlify's .well-known convention and install.md deprecation, Cursor's beyond-spec fields and /migrate-to-skills in 2.4, the Vercel CLI README still naming four agents plus 75 more with the agent table's individual flags re-counted at 79, and Anthropic's untrusted-skill guidance); no claims moved.
- 2026-11-19 - Rotation re-verification: every cited URL re-fetched live and all claims held a sixth time (the spec's six fields with the name rules, the compatibility 500-character limit, and the 500-line recommendation unchanged, the client showcase roster live in the page's HTML with its markdown render now client-side shuffled, the Codex 2%-of-context cap with the skills.max_context_tokens override documented, Gemini's consent gate and .agents/skills alias with the Antigravity-transition banner still up, OpenCode's v2 catalog surface with all frontmatter optional at runtime, Mintlify's .well-known convention and install.md deprecation, Cursor's beyond-spec fields and /migrate-to-skills in 2.4, the Vercel CLI's agent table now at docs/agents.md still carrying 66 rows naming 79 targets with the README headline at four named plus 75 more, and Anthropic's untrusted-skill guidance, which moved from the /engineering/ to the /research/ path and serves 200 on the redirect); no claims moved.
- 2026-11-27 - Added a package maintainer's field report as ecosystem evidence: Backpack for Laravel's 2026-10-20 post ranks a Laravel Boost plugin (guidelines and per-topic skills injected at install, matched to the installed version) above a docs MCP server and llms.txt, because instructions already in context need no fetch decision.
- 2026-11-25 - Recorded the format reaching the review layer: CodeRabbit's changelog entry of 2026-11-19 reads a SKILL.md in an agent's skills folder at the repository root as a code guideline for its reviews, so a skill written for a coding agent also steers a third-party reviewer's comments.

## See also

- [Agent Plugins](../agent-plugins/index.md) - the multi-vendor packaging standard that bundles this format with MCP servers into one installable plugin
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the product this standard was extracted from
- [Claude Code](../../harnesses/claude-code/index.md) - the harness with the richest skill extensions beyond the spec
- [Codex](../../harnesses/codex/index.md) - OpenAI's harness and its 2%-of-context skill budget
- [Teach Your Agent Skills to Use Tools That Render](../../../agent-skills-that-render/index.md) - a corpus pattern for making skill output verifiable

## References

- https://agentskills.io/ - overview, progressive disclosure, client showcase (re-fetched 2026-11-13; re-fetched 2026-11-19, the showcase's markdown render now client-side shuffled with the roster still in the HTML)
- https://agentskills.io/specification - fields, limits, recommended structure, validation (re-fetched 2026-11-13; re-fetched 2026-11-19, unchanged)
- https://developers.openai.com/codex/skills/ - Codex discovery paths, context budget, invocation, plugins (re-fetched 2026-11-13; re-fetched 2026-11-19, unchanged)
- https://geminicli.com/docs/cli/skills/ - consent-gated activation and discovery tiers (re-fetched 2026-11-07 and 2026-11-13; re-fetched 2026-11-19, the Antigravity-transition banner still up, unchanged)
- https://opencode.ai/docs/skills/ - Claude-compatible and .agents paths, permission patterns, catalogs (re-fetched 2026-11-13; re-fetched 2026-11-19, the unified page still documenting the v2 catalog surface, `opencode/autoinvoke` and `disable-model-invocation`, and `@skill-id` loads, with all frontmatter optional at runtime)
- https://www.mintlify.com/blog/skill-md - third-party adoption, .well-known convention, install.md deprecation (re-fetched 2026-11-13; re-fetched 2026-11-19, unchanged)
- https://www.coderabbit.ai/changelog - CodeRabbit's changelog: the Agent Skills as review guidelines entry (November 19, 2026), a SKILL.md in an agent's skills folder at the repository root read automatically as a code guideline applying to the whole repository (fetched 2026-11-25)
- https://github.com/vercel-labs/skills - cross-harness compatibility matrix and the 79-agent README count (re-fetched 2026-11-13; re-fetched 2026-11-19, the agent table now living at docs/agents.md with 66 rows naming 79 targets and the README headline at four named plus 75 more)
- https://cursor.com/docs/context/skills - Cursor's native Agent Skills docs: directories, beyond-spec frontmatter, invocation, migration skill (fetched 2026-10-06, re-verified live 2026-10-24, re-fetched 2026-11-07, 2026-11-13, and 2026-11-19, unchanged)
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the untrusted-skill security risk behind the caution above (re-fetched 2026-11-13; re-fetched 2026-11-19, now serving 200 on a redirect to anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills, the post's new home)
- https://backpackforlaravel.com/articles/opinions/llms-txt-and-mcp-didn-t-move-the-needle-for-us-here-s-what-did - Backpack for Laravel maintainer Cristian Tabacitu's field report of 2026-10-20 (fetched 2026-11-27): a Laravel Boost plugin's install-time guidelines and per-topic skills ranked above a docs MCP server and llms.txt
