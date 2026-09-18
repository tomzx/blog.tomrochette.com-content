---
title: "Skills Feature Matrix"
created: 2026-08-24
updated: 2026-09-13
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, skills, agent-extensions]
readability: 3
audience_notes: >
  Engineers deciding how to package, run, and distribute agent skills, who need the deltas between the open standard, Anthropic's format, OpenCode's mechanism, and the skills.sh registry at a glance.
  Assumes you have written a SKILL.md or configured at least one harness; each column links to a full note with sources.
---

This matrix compares the six Skills-category notes in this section, Builder.io's curated pack, the open standard, Anthropic's vendor format, OpenCode's native mechanism, Microsoft's skill optimizer, and Vercel's skills.sh registry, feature by feature, so choosing an extension path does not require reading six notes.
Everything below was re-verified against live sources on 2026-09-18.

**The format war is already over and SKILL.md won it, so every decision that remains lives above the format, who gates execution, who ranks discovery, and who versions what your agent runs, and the registry column worries me more than the vendor column.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Agent-Native](../agent-native/index.md) | [Agent Skills open standard](../agent-skills-open-standard/index.md) | [Anthropic Agent Skills](../anthropic-agent-skills/index.md) | [OpenCode skills and plugins](../opencode-skills-and-plugins/index.md) | [SkillOpt](../skillopt/index.md) | [skills.sh](../skills-sh/index.md) |
| --- | --- | --- | --- | --- | --- | --- |
| Kind | curated skill pack and app framework | open spec | vendor format | harness mechanism | skill optimizer | registry and CLI |
| Steward | Builder.io | public GitHub org | Anthropic | anomalyco project | Microsoft Research | Vercel labs |
| Open source | ✓ both repos MIT | ✓ spec and validator | ~ mostly, doc skills closed | ✓ MIT | ✓ MIT | ✓ CLI MIT |
| Runtimes | ✓ .agents-path agents (Codex, Pi, Cursor, OpenCode, Copilot), Claude Code, Cowork | ✓ dozens listed | Claude chat, Code, API | OpenCode only | ~ any SKILL.md harness, shells for 5 | ~ installs into 79 |
| Frontmatter beyond spec | ~ spec fields only, plus managed AGENTS.md/CLAUDE.md instruction blocks | ✗ six fields, by design | ✓ ~20 in Claude Code | ✗ unknown fields ignored | ~ standard-compatible output | ~ indexes .claude-plugin |
| Permissions or sandboxing | ~ readback-verify and stop-before-fallback conventions, no gating | ~ harness-defined | ~ API container | ✓ allow/deny/ask per skill | ✗ evaluation-gated, not sandboxed | ✗ audit columns only |
| Distribution and install | ✓ npx installer, plugin marketplaces, git, skills CLI plain-copy | git, no registry needed | repo, upload, Skills API | git; npm for plugins | PyPI plus generated best_skill.md | ✓ npx into 79 agents |
| Telemetry or ranking | ✗ none found first-party | ✗ out of scope | ~ curated partner directory | ✗ none first-party | ✗ none first-party | ✓ install counts, opt-out |
| Versioning and pinning | ~ npm dist-tags and git refs, no lockfile | ✗ none | ~ Skills API versions | ✗ none | ✗ none | ~ git refs, no lockfile |
| Explicit invocation | ✓ slash commands for every skill | ~ explicit or implicit | ~ slash commands in Code | ✗ model-judgment only | ~ trained skill invokes like any skill | n/a (registry) |
| Vendor neutrality | ✗ pack runs anywhere, gravity is Builder.io's stack | ~ Anthropic-origin, public | ✗ Claude-coupled | ✗ OpenCode-only, portable files | ✓ model-agnostic | ~ all vendors, one ranker |
| Cost | free (MIT, hosted surfaces free as of the date) | free | ~ included on plans, tokens on API | free (pay tokens) | free, training tokens on your bill | free |

## Reading the matrix

**The Kind row says this is not six competitors but one stack: a spec, a vendor implementation, a harness implementation, a quality gate, a distributor, and a curated pack.**
The category converged before it could fragment, because Anthropic released its format as the open standard in December 2025 and OpenAI, Google, and the major harnesses adopted it, per the standard note.
**SkillOpt is the stack's quality layer: it treats the other columns' artifacts as trainable parameters, so the question shifts from who distributes skills to who validates them.**

**Convergence is real but stops at the spec subset.**
Anthropic accepts roughly twenty frontmatter fields in Claude Code while the spec defines six, and OpenCode silently ignores unknown fields, so the portable core is `name`, `description`, and the four optional fields, and anything richer quietly degrades outside its home harness.

**The permissions row is where the columns genuinely diverge, and no cell wins.**
The spec leaves security to each harness (Gemini consent, OpenCode patterns, Codex enterprise controls), Anthropic couples API skills to its own container, OpenCode alone gates skill loads with per-pattern allow/deny/ask, and skills.sh aggregates scanner columns after the fact.

**Distribution is git all the way down, and the registry added ranking, not vetting.**
The standard needs no registry at all, skills.sh won the slot by wrapping git and symlinking into more than 70 harnesses, its leaderboard counts opt-out CLI telemetry rather than ratings, and one company controls the ranking surface of a nominally open ecosystem, which is the cell I would watch.

**The Agent-Native column is the first pack in the matrix, and it reads differently from the five infrastructure columns: it consumes the spec's portable core, adds no enforcement of its own, and its pull is toward Builder.io's own stack, the hosted Dispatch MCP endpoint and the hosted plans app its flagship skills default to.**
The cell to watch is stewardship: two MIT repos at 4-5k stars with no independent coverage as of 2026-09-18, so the pack is one company's opinion on a multiple-nightlies-a-day cadence.

**Everything is free, and the missing row is versioning.**
No column costs anything to use, but the spec has no version or dependency story, OpenCode has none, Anthropic versions only through its Skills API, and pinning is left to git discipline or third parties like Skilleton.

## Choosing from the matrix

- Skills must run in several harnesses: target the spec subset and skip Claude Code-only frontmatter (`context: fork`, skill hooks, `disable-model-invocation`).
- All-Claude team wanting the richest behavior: Anthropic's format with Code extensions, accepting that claude.ai upload and the API hard-reject those fields.
- Need enforced policy, not just prompts: OpenCode, with skills for procedure and plugins for policy under per-skill allow/deny/ask.
- Discovering third-party skills: skills.sh, then pin commits and read the SKILL.md before it touches a repo with production secrets.
- Want a curated starter set with workflow opinions: Agent-Native's pack, cherry-picking the discipline skills and declining the managed AGENTS.md/CLAUDE.md blocks if vendor-managed instructions are not your thing.
- Need managed versions across an organization: Anthropic's Skills API is the only first-party versioning in the matrix.
- Shipping skills for your own product: publish them in your repo or docs (`.well-known`), since the standard note argues docs teams without a skill will be invisible to agents by 2027.

## Changes

- 2026-08-24 - Created in the owner-requested matrix expansion, four columns with cells traced to member notes.
- 2026-08-30 - Extended from four to five columns with SkillOpt, the stack prose naming the new quality layer.
- 2026-09-13 - Extended from five to six columns with Agent-Native, the first curated pack column.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the terminal-agent matrix whose hooks-and-skills row this expands
- [OpenCode skills and plugins](../opencode-skills-and-plugins/index.md) - the deepest single-harness column here
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the spec every other column implements or distributes
- [skills.sh](../skills-sh/index.md) - the distribution and ranking layer
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this category sits in

## References

- https://agentskills.io/ - the spec, its six fields, and the client showcase behind the runtimes row
- https://code.claude.com/docs/en/skills - Claude Code frontmatter extensions and skill surfaces
- https://opencode.ai/docs/skills/ - skill paths, permission patterns, and the skill tool
- https://opencode.ai/docs/plugins/ - the plugin half of the OpenCode column
- https://skills.sh/docs - telemetry ranking method and the security disclaimer
- https://github.com/vercel-labs/skills - agent path table, 70+ install targets, telemetry opt-out
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the untrusted-skill security framing behind the permissions row
- https://github.com/microsoft/SkillOpt - the SkillOpt column: the training loop, the validation gate, and the best_skill.md artifact
- https://github.com/BuilderIO/skills - the Agent-Native pack column: the fifteen-skill catalog, installer, and marketplace packaging
- https://github.com/BuilderIO/agent-native - the framework behind the pack: the shared-action model and app gallery
