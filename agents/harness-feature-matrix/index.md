---
title: "Harness Feature Matrix"
created: 2026-08-24
updated: 2026-09-05
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, comparison, harnesses, coding-agents]
readability: 3
audience_notes: >
  Engineers shortlisting coding-agent harnesses who need the capability deltas at a glance.
  Assumes you know what MCP, AGENTS.md, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the twenty-five harnesses profiled in this section, feature by feature, so the shortlisting step does not require reading twenty-five notes.
Everything below was re-verified against live sources on 2026-09-05.

**No harness has everything, and the two axes that actually decide the purchase are client openness and who pays for tokens: everything else is converging.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [aider](../aider/index.md) | [Amp](../amp/index.md) | [Ante](../ante/index.md) | [Bullet](../bullet/index.md) | [Claude Code](../claude-code/index.md) | [Cline](../cline/index.md) | [Codex](../codex/index.md) | [Crush](../crush/index.md) | [DeepSeek Harness](../deepseek-harness/index.md) | [Exo](../exo/index.md) | [fx](../fx/index.md) | [Gemini CLI](../gemini-cli/index.md) | [goose](../goose/index.md) | [jcode](../jcode/index.md) | [Juggler](../juggler/index.md) | [Junie](../junie/index.md) | [Kilo Code](../kilo-code/index.md) | [Kimi Code](../kimi-code/index.md) | [OneCLI](../onecli/index.md) | [OpenCode](../opencode/index.md) | [OpenHands](../openhands/index.md) | [Pi](../pi/index.md) | [Qwen Code](../qwen-code/index.md) | [Warp Agent CLI](../warp-agent-cli/index.md) | [Zerostack](../zerostack/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Company | none (solo) | [Amp Frontier](https://ampcode.com) | [Antigma Labs](https://antigma.ai) | [TryBullet](https://www.codewithbullet.com) (YC S26, closed source) | [Anthropic](https://www.anthropic.com) | [Cline Bot](https://cline.bot) | [OpenAI](https://openai.com) | [Charm](https://charm.sh) | [DeepSeek](https://deepseek.com) | [Exo Labs](https://exoharness.ai) | [Vercel](https://vercel.com) | [Google](https://about.google) | [AAIF](https://aaif.io) (ex-Block) | [Solo Systems](https://jcode.sh) | [Julian Storer](https://juggler.studio/) (solo) | [JetBrains](https://www.jetbrains.com) | [Anaconda](https://www.anaconda.com) | [Moonshot AI](https://www.kimi.com) | [OneCLI](https://onecli.sh) (YC S26) | [Anomaly](https://anoma.ly) | [All Hands AI](https://all-hands.dev) | [Earendil](https://pi.dev) | [Alibaba](https://www.alibaba.com) | [Warp](https://www.warp.dev) | [Giuseppe Dellavedova](https://github.com/gi-dellav/zerostack) (solo, GPL-3.0) |
| Open client | ✓ Apache-2.0 | ✗ | ~ Apache-2.0 source, preview binaries | ✗ | ✗ | ✓ Apache-2.0 | ✓ Apache-2.0 | ~ FSL-1.1-MIT | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ MIT | ✓ AGPL-3.0 | ✗ | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✗ closed binary | ✓ GPL-3.0 |
| BYOK | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ AI Gateway key only | ✓ paid keys | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ BYOC at paid tiers | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Included subscription usage | ✗ | ✓ | ✓ | ✗ free, no subscriptions | ✓ | ~ via ClinePass | ✓ | ~ via Hyper | ✗ BYO keys only | ✗ API keys only | ~ Codex and Grok OAuth | ✗ enterprise only | ~ via ACP subs | ✓ OAuth and multi-account | ✓ | ✓ | ~ kilo credits | ~ via Kimi OAuth | ~ $5 credits at $0 tier | ~ via Zen | ✗ at-cost only | ✓ Claude, ChatGPT, Copilot | ~ free OAuth tier | ✓ | ✗ |
| Local models | ✓ | ✗ | ✓ embedded llama.cpp | ✗ hosted models only | ✗ | ✓ | ✗ | ✓ | ~ OpenAI-compatible endpoints | ✗ | ✗ none documented | ✗ | ✓ | ✓ Ollama and LM Studio | ✓ Ollama | ✓ Ollama and LM Studio, plus on-device Junie Local | ✓ Ollama and LM Studio | ✗ | ? | ✓ | ✓ LM Studio, Ollama, vLLM | ✓ llama.cpp | ✓ | ✗ | ✓ Ollama |
| MCP | ✗ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ~ stdio only | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✗ by design | ✓ | ? | ~ compile-time feature |
| AGENTS.md | ✗ | ✓ | ✓ | ? | ~ reads CLAUDE.md | ✓ plus .clinerules | ✓ | ✓ plus CRUSH.md | ? | ? | ✓ native | ~ GEMINI.md native | ✓ plus .goosehints | ✓ native plus ~/AGENTS.md | ? | ✗ uses guidelines.md | ✓ plus .kilocoderules | ? | ? | ✓ plus CLAUDE.md | ✗ uses .openhands | ? | ~ QWEN.md native | ? | ✓ plus ARCHITECTURE.md |
| Subagents | ✗ | ✓ | ✓ | ? | ✓ | ✓ teams | ✓ | ? | ✓ | ~ agent clones and lineage | ✓ persistent children | ✗ | ✓ | ✓ swarm workers | ~ read-only | ✗ | ✓ custom and built-in | ✓ coder, explore, plan | ? | ✓ | ~ delegates via ACP | ~ via extensions | ✓ teams | ~ multi-agent orchestration | ✓ |
| Hooks, skills, plugins | ~ lint and test only | ✓ plugins gate tools | ~ skills only | ? | ✓ hooks and skills | ✓ skills and SDK plugins | ✓ skills and marketplace | ✓ skills | ✓ plugins and skills | ~ self-editing tooling | ~ skills only | ? | ✓ hooks and plugins | ✓ hooks and embedding-gated skills | ~ extension SDK | ~ execution allowlists | ✓ skills and hooks | ✓ hooks and marketplace skills | ? | ✓ skills and plugins | ✓ hooks, skills, plugins | ✓ extensions and skills | ✓ hooks and auto-skills | ? | ~ hooks, prompt modes replace skills |
| Cloud execution | ✗ | ✓ orbs | ✗ local-first | ? | ✓ web and teleport | ✗ | ✓ | ✗ | ✗ | ✗ local, Docker required | ✗ | ~ CI GitHub Action | ✗ | ✗ self-hosted daemon only | ✗ self-hosted remote only | ~ remote control | ✓ cloud agents and tasks | ✗ | ✓ hosted VMs | ✗ share links only | ✓ OpenHands Cloud | ✗ | ✗ | ✓ cloud agents | ✗ local only |
| Scheduled runs | ✗ | ✓ self-set | ? | ? | ✓ routines | ✓ cron | ? | ✗ | ? | ? | ✗ | ✗ | ✗ | ~ ambient mode | ? | ✗ | ✓ cron builder | ? | ? | ~ via host apps | ✓ automations and webhooks | ✗ | ~ experimental cron | ? | ? |
| IDE integration | ✗ | ✗ | ✓ via ACP | ? | ✓ extensions | ✓ VS Code and JetBrains | ✓ extension | ✗ terminal only | ✓ ACP | ? | ✓ via ACP | ~ enterprise Code Assist | ~ experimental VS Code | ✗ terminal and paired clients | ? | ✓ | ✓ VS Code and JetBrains | ✓ via ACP | ? | ✓ VS Code and ACP | ✗ browser and terminal | ? community clients | ✓ VS Code, Zed, JetBrains | ? | ✓ via ACP |

## Reading the matrix

I read this table by columns rather than rows: pick the two rows you actually care about, then let the rest fall away.
The Company row is context, not a feature axis: it names the maker (or, for goose, the foundation that now stewards the code) and links each site.
**The open-client column splits the field into three groups, and each group answers a different buyer.**
aider, Cline, Codex, Exo, fx, Gemini CLI, goose, Juggler, jcode, Kimi Code, Kilo Code, OneCLI, OpenCode, OpenHands, Qwen Code, and Zerostack hand you auditable code; Crush is source-available with a competing-use restriction that expires per version, and Ante publishes Apache-2.0 source whose prebuilt binaries answer to separate preview terms; Amp, Bullet, Claude Code, Junie, and Warp Agent CLI are binaries you trust.

**Subscription versus keys is the second axis, and it is orthogonal to openness.**
Codex is open and subscription-fed; Amp is closed but takes your Anthropic key on usage billing; aider and Crush are keys-only, period; goose reuses the Claude, ChatGPT, or Gemini subscription you already pay for via ACP, and fx reuses ChatGPT and Grok subscriptions via OAuth, though every fx request still routes through Vercel AI Gateway.
The six new columns spread across the same axis: Ante and Juggler take subscriptions alongside keys, Warp folds all usage into its own credit meter, OneCLI starts teams at $0 with $5 of credits, Bullet is free with no subscriptions at all, and Zerostack stays keys-only.

**Local-model support now cleanly separates the BYOK purists (aider, Ante, Cline, Crush, goose, Juggler, jcode, Junie, Kilo Code, OpenCode, OpenHands, Qwen Code, Zerostack) from the platform players** whose value-add assumes their own model routing, a group Bullet and Warp Agent CLI now join.

**The feature everyone lacks is a different one, which is the tell that the category is immature in different places:** aider lacks the agent loop, Gemini CLI lacks a consumer future, Crush lacks documented subagents, OpenCode lacks its own cloud execution, and all three 2026 entrants lack cloud execution: Cline and Qwen Code run only where you stand, and goose keeps its IDE story experimental.
**The two newest columns redraw that map again:** Kilo Code bundles subagents, schedules, and cloud tasks into an editor-native open agent, which nothing else in this table does, while OpenHands skips AGENTS.md entirely because its `.openhands` customization replaces repo-instruction files.
**fx, the fourteenth column at the time it joined, redelines the axis itself:** it is the only harness here built to be a dependency instead of an environment, and the only open one whose tokens must cross its sponsor's gateway.
**jcode bets the constraint is hardware, not intelligence:** it is the only entry whose measured RAM floor, native memory graph, and same-repo swarm all assume you will run dozens of agents at once, and the only one that rebuilds its own binary on request.
**DeepSeek Harness is the everything-is-a-plugin bet:** fully open with subagents, skills, and ACP editor support already filled in, and question marks on MCP and AGENTS.md that an alpha project earns.
**Pi is the deliberate-omission bet:** the only entry with no MCP by design and no built-in subagents, paired with the widest subscription reuse in the table and local models through llama.cpp.
**Ante takes the footprint bet furthest:** the only column whose local inference engine lives inside the binary itself, though its prebuilt releases answer to preview terms the Apache-2.0 repo does not carry.
**Bullet is the latency bet:** free, closed, and the most transparent vendor self-report in the table, with question marks wherever its note cannot see.
**Juggler is the GUI bet:** conversation trees, durable sessions, and inspectable everything from a solo Go author, AGPL app code included.
**OneCLI is the security-team bet:** credentials injected at a gateway so agents never hold real secrets, priced in seats and credits rather than keys.
**Warp Agent CLI is the vendor-unbundle bet:** cloud agents and multi-agent orchestration on a closed binary, everything through Warp's meter.
**Zerostack is the GPL footprint bet:** subagents, worktrees, sandboxing, and hooks in a solo Rust binary, with MCP and other headline features behind compile-time flags.
**Kimi Code is the challenger-vendor bet:** the first column whose maker sells the cheap model it is tuned for, with subagents, hooks, and marketplace skills already filled in and question marks where its docs stay silent.
**Exo is the self-modification bet:** the only column whose harness policy is itself agent-editable, which earns it question marks on the conventional rows and a clone-and-lineage mechanic nobody else has.

## Choosing from the matrix

- Need an auditable client plus a subscription: Codex or Juggler, with Ante close if you build its Apache-2.0 source.
- Need local models plus MCP: Ante, Cline, Crush, goose, Junie, Kilo Code, OpenCode, OpenHands, or Qwen Code.
- Need scheduled autonomous work in the cloud: Amp, Claude Code, Kilo Code, or OpenHands.
- Need editor-embedded agents with deep analysis: Junie or Claude Code.
- Need rules portability across tools: Amp, Ante, Cline, Codex, Crush, fx, goose, Kilo Code, OpenCode, and Zerostack read AGENTS.md natively.
- Need an auditable agent platform you can self-host with cloud automation built in: OpenHands.
- Need an agent embedded inside your own tool, sandbox, or pipeline: fx.
- Need dozens of parallel agents on one machine, with memory and coordination built in: jcode.
- Need a graphical workbench where conversations branch and every tool call is inspectable: Juggler.
- Need team agents that never hold real credentials, enforced outside the model: OneCLI.
- Need cloud agents, orchestration, and billing from one vendor subscription: Warp Agent CLI.
- Need a free, latency-first second-opinion agent: Bullet.
- Need the smallest possible RAM floor on small machines or containers: Zerostack.
- Need a big-vendor CLI priced for challenger-model economics: Kimi Code.
- Want a harness the agent itself can rewrite, at your own risk: Exo.
- Need none of the above, just cheap precise edits on your keys: aider.

## See also

- [Harness Feature Matrix companion: surfaces](../surface-feature-matrix/index.md) - the same treatment for editors and environments
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map these columns come from
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the model side of the same decision
- [MCP](../mcp/index.md) - the protocol behind the MCP row
- [AGENTS.md](../agents-md/index.md) - the convention behind the AGENTS.md row

## References

- https://github.com/Aider-AI/aider - license and feature surface for the aider column
- https://ampcode.com/manual/ - modes, plugins, orbs for the Amp column
- https://github.com/AntigmaLabs/ante - license, architecture, and provider surface for the Ante column
- https://www.codewithbullet.com - product surface, benchmark, and free access for the Bullet column
- https://code.claude.com/docs/en/overview - surfaces, skills, routines for the Claude Code column
- https://docs.cline.bot/features/cline-rules - rules formats including native AGENTS.md for the Cline column
- https://developers.openai.com/codex/cli - CLI, skills, AGENTS.md for the Codex column
- https://docs.openhands.dev/llms.txt - component map, automations, local LLMs, and .openhands customization for the OpenHands column
- https://kilo.ai/docs/llms.txt - subagents, MCP, AGENTS.md support, schedules, and cloud tasks for the Kilo Code column
- https://www.anaconda.com/blog/anaconda-acquires-kilo-code - ownership context for the Kilo Code column
- https://goose-docs.ai/docs/guides/context-engineering/using-goosehints - AGENTS.md and .goosehints defaults for the goose column
- https://opencode.ai/docs/mcp-servers/ - MCP configuration for the OpenCode column
- https://github.com/JetBrains/junie - distribution model and MCP mentions for the Junie column
- https://github.com/onecli/onecli - license, gateway model, and pricing for the OneCLI column
- https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/ - QWEN.md and experimental cron for the Qwen Code column
- https://docs.warp.dev/agents/cli - CLI surface, cloud agents, and account model for the Warp Agent CLI column
- https://github.com/vercel-labs/fx - license, scale, and releases for the fx column
- https://fx.sh/docs/getting-started/authentication - the provider model behind the fx BYOK and subscription cells
- https://fx.sh/docs/configure-fx/models - the no-local-models cell for the fx column
- https://github.com/1jehuang/jcode - license, scale, providers, MCP limits, and swarm for the jcode column
- https://jcode.sh/docs - AGENTS.md, hooks, skills, local models, and remote daemon cells for the jcode column
- https://github.com/juggler-ai/juggler - license, extensions, and session model for the Juggler column
- https://github.com/deepseek-ai/deepseek-harness - license, plugin architecture, and surfaces for the DeepSeek Harness column
- https://github.com/earendil-works/pi - license, packages, subscription reuse, and the no-MCP policy for the Pi column
- https://github.com/gi-dellav/zerostack - license, feature list, and footprint claims for the Zerostack column
- https://github.com/MoonshotAI/kimi-code - license, subagents, MCP, hooks, and ACP cells for the Kimi Code column
- https://github.com/exoharness/exo - license, self-modification architecture, and requirements for the Exo column
- https://frontierharness.org - independent pass-rate and cost context for the Exo and Kimi Code columns
