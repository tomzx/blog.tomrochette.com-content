---
title: "Skills Feature Matrix"
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, skills, agent-extensions]
readability: 3
audience_notes: >
  Engineers deciding how to package, run, and distribute agent skills, who need the deltas between the open standard, Anthropic's format, OpenCode's mechanism, and the skills.sh registry at a glance.
  Assumes you have written a SKILL.md or configured at least one harness; each column links to a full note with sources.
---

This matrix compares the four Skills-category notes in this section, the open standard, Anthropic's vendor format, OpenCode's native mechanism, and Vercel's skills.sh registry, feature by feature, so choosing an extension path does not require reading four notes.
Everything below was verified against live sources on 2026-08-24.

**The format war is already over and SKILL.md won it, so every decision that remains lives above the format, who gates execution, who ranks discovery, and who versions what your agent runs, and the registry column worries me more than the vendor column.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Agent Skills standard](../agent-skills-open-standard/index.md) | [Anthropic Agent Skills](../anthropic-agent-skills/index.md) | [OpenCode skills and plugins](../opencode-skills-and-plugins/index.md) | [skills.sh](../skills-sh/index.md) |
| --- | --- | --- | --- | --- |
| Kind | open spec | vendor format | harness mechanism | registry and CLI |
| Steward | public GitHub org | Anthropic | anomalyco project | Vercel labs |
| Open source | ✓ spec and validator | ~ mostly, doc skills closed | ✓ MIT | ✓ CLI MIT |
| Runtimes | ✓ dozens listed | Claude chat, Code, API | OpenCode only | ~ installs into 70+ |
| Frontmatter beyond spec | ✗ six fields, by design | ✓ ~20 in Claude Code | ✗ unknown fields ignored | ~ indexes .claude-plugin |
| Permissions or sandboxing | ~ harness-defined | ~ API container | ✓ allow/deny/ask per skill | ✗ audit columns only |
| Distribution and install | git, no registry needed | repo, upload, Skills API | git; npm for plugins | ✓ npx into 70+ agents |
| Telemetry or ranking | ✗ out of scope | ~ curated partner directory | ✗ none first-party | ✓ install counts, opt-out |
| Versioning and pinning | ✗ none | ~ Skills API versions | ✗ none | ~ git refs, no lockfile |
| Explicit invocation | ~ explicit or implicit | ~ slash commands in Code | ✗ model-judgment only | n/a (registry) |
| Vendor neutrality | ~ Anthropic-origin, public | ✗ Claude-coupled | ✗ OpenCode-only, portable files | ~ all vendors, one ranker |
| Cost | free | ~ included on plans, tokens on API | free (pay tokens) | free |

## Reading the matrix

**The Kind row says this is not four competitors but one stack: a spec, a vendor implementation, a harness implementation, and a distributor.**
The category converged before it could fragment, because Anthropic released its format as the open standard in December 2025 and OpenAI, Google, and the major harnesses adopted it, per the standard note.

**Convergence is real but stops at the spec subset.**
Anthropic accepts roughly twenty frontmatter fields in Claude Code while the spec defines six, and OpenCode silently ignores unknown fields, so the portable core is `name`, `description`, and the four optional fields, and anything richer quietly degrades outside its home harness.

**The permissions row is where the columns genuinely diverge, and no cell wins.**
The spec leaves security to each harness (Gemini consent, OpenCode patterns, Codex enterprise controls), Anthropic couples API skills to its own container, OpenCode alone gates skill loads with per-pattern allow/deny/ask, and skills.sh aggregates scanner columns after the fact.

**Distribution is git all the way down, and the registry added ranking, not vetting.**
The standard needs no registry at all, skills.sh won the slot by wrapping git and symlinking into more than 70 harnesses, its leaderboard counts opt-out CLI telemetry rather than ratings, and one company controls the ranking surface of a nominally open ecosystem, which is the cell I would watch.

**Everything is free, and the missing row is versioning.**
No column costs anything to use, but the spec has no version or dependency story, OpenCode has none, Anthropic versions only through its Skills API, and pinning is left to git discipline or third parties like Skilleton.

## Choosing from the matrix

- Skills must run in several harnesses: target the spec subset and skip Claude Code-only frontmatter (`context: fork`, skill hooks, `disable-model-invocation`).
- All-Claude team wanting the richest behavior: Anthropic's format with Code extensions, accepting that claude.ai upload and the API hard-reject those fields.
- Need enforced policy, not just prompts: OpenCode, with skills for procedure and plugins for policy under per-skill allow/deny/ask.
- Discovering third-party skills: skills.sh, then pin commits and read the SKILL.md before it touches a repo with production secrets.
- Need managed versions across an organization: Anthropic's Skills API is the only first-party versioning in the matrix.
- Shipping skills for your own product: publish them in your repo or docs (`.well-known`), since the standard note argues docs teams without a skill will be invisible to agents by 2027.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the terminal-agent matrix whose hooks-and-skills row this expands
- [OpenCode skills and plugins](../opencode-skills-and-plugins/index.md) - the deepest single-harness column here
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the spec every other column implements or distributes
- [skills.sh](../skills-sh/index.md) - the distribution and ranking layer
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map this category sits in

## References

- https://agentskills.io/ - the spec, its six fields, and the client showcase behind the runtimes row
- https://code.claude.com/docs/en/skills - Claude Code frontmatter extensions and skill surfaces
- https://opencode.ai/docs/skills/ - skill paths, permission patterns, and the skill tool
- https://opencode.ai/docs/plugins/ - the plugin half of the OpenCode column
- https://skills.sh/docs - telemetry ranking method and the security disclaimer
- https://github.com/vercel-labs/skills - agent path table, 70+ install targets, telemetry opt-out
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the untrusted-skill security framing behind the permissions row
