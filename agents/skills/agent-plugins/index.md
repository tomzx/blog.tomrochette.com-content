---
title: Agent Plugins
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, plugins, open-standards, packaging]
readability: 3
audience_notes: >
  Engineers packaging skills and MCP servers for more than one agent client, who need to know what the new plugin envelope standardizes and what it leaves to each vendor.
  Assumes familiarity with SKILL.md and at least one MCP server.
---

Agent Plugins is an open, vendor-neutral standard, proposed by Vercel and published as version 1.0.0 on 2026-08-06, that packages Agent Skills and MCP server configurations into one portable directory with a root `plugin.json` manifest.

**It is the packaging layer this ecosystem was missing, and its restraint is the design: six competing vendors agreed precisely because it defines only the folder layout, the manifest, and how clients discover and load the two portable component types.**

## What it is

A plugin is a directory: `plugin.json` at the root, skills under `skills/` (conformant to the Agent Skills spec), MCP servers in `mcp.json` (stdio, Streamable HTTP, or legacy HTTP+SSE), and reverse-domain namespace folders where clients bolt on their own extras without touching the portable core.
The manifest is closed: ten permitted top-level fields, only `$schema` and `name` required, and any schema violation other than an unknown top-level field rejects the plugin.
Distribution, installation, permissions, marketplaces, commands, hooks, and agents are all explicitly out of scope.
Vercel initiated the proposal and refined it with AWS, Anysphere (Cursor), GitHub, Microsoft, and OpenAI, and the initial Technical Steering Committee draws its core maintainers from AWS, Cursor, Microsoft, OpenAI, and Vercel.

## Status

**Active and vendor-backed, and still under a year old.**
The specification repository (agentplugins/agent-plugins-spec) shows 1,360 stars and 75 forks as of 2026-10-07, created 2026-04-03 and last pushed 2026-09-28, with the spec, JSON schemas, conformance suite, example plugin, and site in five public repos under one organization.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentplugins/agent-plugins-spec&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentplugins/agent-plugins-spec&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentplugins/agent-plugins-spec&type=date&legend=top-left" />
</picture>

At launch, ChatGPT and Codex, Cursor, GitHub Copilot, Kiro, and VS Code supported the format, while Anthropic and Google appeared on neither the partner list nor the steering committee.
In practice the `plugins` CLI translates the format into Claude Code, Codex, Cursor, GitHub Copilot, VS Code, Grok Build, and Kimi Code, so plugins install into Claude Code today even though Claude Code does not natively parse `plugin.json`.

## Strengths

- **The closed manifest with a versioned `$schema` is the first packaging contract in this ecosystem that fails loudly: a stray field copied from a package.json gets reported, not silently ignored.**
- The containment rules (plugin-relative paths, `${PLUGIN_ROOT}` and `${PLUGIN_DATA}` expansion, per-component failure isolation) read like they came from client implementers rather than a paper exercise.
- Skills keep the Agent Skills format unchanged, so an ordinary SKILL.md folder migrates by moving under `skills/`.
- Governance is public: a Technical Charter, open GitHub Discussions, and openly licensed spec and schemas.

## Cautions

- **Anthropic and Google are not launch partners, so the format's fate depends on clients that did not sign it, and the SKILL.md format inside every plugin is Anthropic's, which makes the absence odd as well as risky.**
- The root `plugin.json` name collides with Claude Code's `.claude-plugin/plugin.json`, a different file with a different schema, and little coverage flags the trap.
- Packaging and transport are solved, but discovery and trust are not: there is no resolution story, no security story, and permissions stay client-defined, so the same plugin holds different privileges per client.
- Coverage disagrees with the spec on one point: a widely-cited guide says unknown top-level fields are rejected outright, while the spec text says clients report and ignore them, and the spec governs.

## Pricing

Not applicable.
The specification, schemas, guides, and conformance tooling are free and openly licensed.

## Compared to

- [Agent Skills open standard](../agent-skills-open-standard/index.md): the skill format Agent Plugins packages; an envelope, not a competing format.
- Claude Code plugins: `.claude-plugin/plugin.json` marketplaces solve the same bundling job for one vendor; Agent Plugins is the portable version, weaker but cross-client.
- MCP: the wire protocol for live tool connections; Agent Plugins references it for behavior and standardizes only the packaging around it.

## Bottom line

**Recommended as the packaging target when one artifact must carry skills plus MCP config across the launch clients, and keep your skills as plain spec-conformant SKILL.md folders either way, since that is what makes every translation layer work.**
Not for teams needing enforced permissions, discovery, or trust, none of which the standard defines.
My disagreeable claim: the interesting question is no longer whether skills and MCP are the durable primitives but who solves resolution and trust for the plugin layer, and a steering committee of five vendors has no structural incentive to be the neutral third party that does it.

## Changes

- 2026-10-06 - Created in the daily refresh's skills entrant scan.
- 2026-10-07 - Added the agentplugins/agent-plugins-spec star history chart to the Status section.

## See also

- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the skill format every plugin packages
- [skills.sh](../skills-sh/index.md) - the distribution layer whose CLI already bridges `.claude-plugin` manifests
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the vendor format that became the skills half of every plugin
- [MCP](../../protocols/mcp/index.md) - the protocol standardizing what Agent Plugins packages
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this packaging layer sits over

## References

- https://agent-plugins.org/ - the spec site: package model, component types, open governance, and the five-vendor TSC (fetched 2026-10-06)
- https://agent-plugins.org/specification - the normative v1.0.0 spec: the closed ten-field manifest, required `$schema` and `name`, report-and-ignore for unknown fields, MCP transports, and the `PLUGIN_ROOT`/`PLUGIN_DATA` environment contract (fetched 2026-10-06)
- https://vercel.com/blog/introducing-agent-plugins - the launch announcement (2026-08-06): Vercel initiated, refined with AWS, Anysphere, GitHub, Microsoft, and OpenAI, and the launch client list (fetched 2026-10-06)
- https://api.github.com/repos/agentplugins/agent-plugins-spec - the specification repo: 1,360 stars, 75 forks, created 2026-04-03, pushed 2026-09-28 (GitHub API, as of 2026-10-07)
- https://agenticskills.io/learn/what-are-agent-plugins - the critical reading: the `plugin.json` naming collision, the absent Anthropic and Google, the CLI-versus-native-support distinction, and what remains unsolved (fetched 2026-10-06)
