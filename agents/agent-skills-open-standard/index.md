---
title: Agent Skills open standard
created: 2026-08-24
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, skills, agent-extensions, open-standards]
readability: 3
audience_notes: >
  Engineers writing SKILL.md packages meant to run in more than one agent harness.
  Assumes familiarity with at least one coding agent and its context files.
---

The Agent Skills open standard (agentskills.io) defines an agent capability as a directory containing a SKILL.md: required `name` and `description` frontmatter, optional `license`, `compatibility`, `metadata`, and `allowed-tools`, then markdown instructions, with scripts, references, and assets as optional neighbors.
Facts below verified as of 2026-09-02.

**The standard spread faster than MCP because it is only files: no runtime, no protocol, no server, so a harness can implement it in an afternoon, and by mid-2026 OpenAI, Google, and the major third-party harnesses all had.**

## What it is

The format was developed by Anthropic, released as an open standard on 2025-12-18, and is stewarded publicly on GitHub (agentskills/agentskills) with a Discord and a `skills-ref` validation library.
Packaging rules are minimal: name is 1-64 lowercase-hyphen characters matching the directory, description is 1-1024 characters, and the body is unrestricted markdown, recommended under 500 lines and 5k tokens.
Discovery is by directory convention: each harness scans its own skills paths (`.claude/skills`, `.opencode/skills`, `.gemini/skills`), with `.agents/skills` emerging as the cross-tool path (Codex repo and user locations, Gemini CLI aliases, Cursor and Copilot via the Vercel CLI).
**Invocation is either explicit (slash commands, `$`, `@`) or implicit, the model matching the task against one description line.**

## Status

**Active, and effectively the winner.**
The agentskills.io client showcase lists Claude and Claude Code, ChatGPT and Codex, Gemini CLI, Cursor, GitHub Copilot and VS Code, OpenCode, Amp, Goose, Junie, Roo, Kiro, Trae, and dozens more.
Vercel's skills CLI installs into more than 70 agents.
Mintlify now auto-generates a skill at `.well-known/skills/default/skill.md` for every docs site it hosts and deprecated its January 2026 install.md convention in favor of skills.

## Strengths

- **Git-native: skills version, review, and diff like code, and no registry is required to distribute them.**
- Progressive disclosure bounds the cost: metadata is about 100 tokens at startup, and Codex caps the entire initial skill list at 2% of the context window (8,000 characters when unknown).
- Real vendor adoption: Microsoft, Supabase, Prisma, Vercel, and Anthropic ship official skills, visible on skills.sh.

## Cautions

- **The spec standardizes packaging, not behavior: whether a skill fires is model judgment over one description line, so the same skill behaves differently per harness and per model.**
- Frontmatter fragmentation: Claude Code-only fields (`context: fork`, hooks in skills, `disable-model-invocation`) and Codex's `agents/openai.yaml` live outside the spec, and the Vercel CLI's compatibility matrix shows `context: fork` working in Claude Code alone.
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

## See also

- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the product this standard was extracted from
- [Claude Code](../claude-code/index.md) - the harness with the richest skill extensions beyond the spec
- [Codex](../codex/index.md) - OpenAI's harness and its 2%-of-context skill budget
- [Teach Your Agent Skills to Use Tools That Render](../../agent-skills-that-render/index.md) - a corpus pattern for making skill output verifiable

## References

- https://agentskills.io/ - overview, progressive disclosure, client showcase
- https://agentskills.io/specification - fields, limits, recommended structure, validation
- https://developers.openai.com/codex/skills/ - Codex discovery paths, context budget, invocation, plugins
- https://geminicli.com/docs/cli/skills/ - consent-gated activation and discovery tiers
- https://opencode.ai/docs/skills/ - Claude-compatible and .agents paths, unknown-field behavior
- https://www.mintlify.com/blog/skill-md - third-party adoption, .well-known convention, install.md deprecation
- https://github.com/vercel-labs/skills - cross-harness compatibility matrix
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the untrusted-skill security risk behind the caution above
