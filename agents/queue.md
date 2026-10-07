---
title: Agents queue
created: 2026-08-22
status: in progress
tags: [agents]
readability: 0
---

Work items the owner has requested, taken in order, highest first.
Every item is standing: none is ever closed, and every section keeps being built out and re-verified indefinitely.
The owner edits this file to steer the section; agents append `? for tom:` bullets and work the items, and never mark one done, strike it through, or remove it.

1. **Build the research index** (standing) - create research notes per the AGENTS.md format, one category at a time, each category seeded with the tools practitioners actually meet. Seed categories, in rough order:
   - Harnesses: Claude Code, Codex, Gemini CLI/Antigravity, OpenCode, aider, Crush, Amp, Junie.
   - Surfaces: Cursor, VS Code + Copilot, Windsurf, JetBrains/Junie, Zed.
   - Orchestration: parallel-agent dashboards and worktree managers (Conductor, dmux, Emdash, and neighbors).
   - Protocols: MCP, ACP, AGENTS.md, A2A.
   - Context engines: code search and context packing for agents.
   - Skills: skill formats, registries, and marketplaces.
   - Retrieval: RAG patterns and tooling for code and knowledge bases.
   - Memory: agent memory systems, from file-based notes to knowledge graphs and session archives.
   - Executions: scheduled and event-based agent runs (cron-style tasks, triggers, webhooks).
   - Hybrid execution: deterministic components orchestrating LLM steps for intelligence and structured outputs (tool calling, schema/JSON outputs, validation and retry loops).
   - People and publications: the people and websites shaping the domain (Karpathy, swyx/Latent Space, Willison, Yegge, Orosz/Pragmatic Engineer).

Standing work already under way (still open; keep updating and extending each indefinitely):

- **Agentic coding tools landscape** - started 2026-08-22, published as [agentic-coding-tools-landscape](agentic-coding-tools-landscape/index.md); it is the essay layer over the harness/surface/orchestration notes, so keep cross-linking new notes and re-verifying it indefinitely.
- **Model selection for coding tasks** - started 2026-08-24, published as [model-selection-for-coding-tasks](model-selection-for-coding-tasks/index.md); keep folding in new models and price moves indefinitely.
- **Context management patterns** - started 2026-08-24, published as [context-management-patterns](context-management-patterns/index.md); keep re-grounding its patterns in new harness documentation indefinitely.
- **People and publications category** - seeded 2026-08-29, with the companion [people-and-publications-feature-matrix](people-and-publications/people-and-publications-feature-matrix/index.md); keep scanning for and adding new voices and publications indefinitely, not only when prompted.

? for tom: The 2026-10-01 banned-term sweep reworded "real" section headings in the main corpus but left this section's roughly 330 "real" uses (mostly "real-world" compounds and contrastive uses like "adoption is real, stability is not") in place, and the daily verification has been treating them as the most-appropriate-term exceptions since. Should the section get the same rewording treatment, or is the corpus-only scope the intent? Rewording at this scale needs its own directed run with Changes bullets per touched note, so I have not done it inside a daily refresh.
? for tom: The sandboxing refresh flagged that E2B, the hosted sandbox API the category's notes already cite as a standing comparison baseline, has never been profiled as a note of its own. Add it to the sandboxing category (it would clear the citation bar easily), or does it stay comparison-only?
? for tom: Following up on the "real" question above: the skills-library banned-terms list now also bans "real" (and "load-bearing") as of 2026-10-06, while this section's AGENTS.md still lists only shape/honest/load bearing and the roughly 334 retained uses remain under the documented-exceptions treatment. Confirm and a directed run will reword them with per-note Changes bullets.
? for tom: The retrieval entrant scan rejected Haystack (26.7k stars, active) because the category's founding scope carries exactly two frameworks and a third framework column is a scope call, not an entrant signal. Should retrieval add Haystack as a third framework column, or does the two-framework scope stand?
? for tom: The trackers scan rejected METR's time-horizon series as a tracker (a single trend series, not a leaderboard) but flagged it as a possible people-and-publications voice (an evals nonprofit publishing original measurement research). Should METR be profiled in people and publications?
? for tom: The evaluation awesome-list cross-check surfaced Opik (comet-ml/opik, 22.4k stars, Apache-2.0, active) as an uncovered observability-and-eval platform between the category's two existing columns in adoption (Langfuse 35.5k, Phoenix 11.7k), with promptfoo (25.8k) as a second eval framework next to deepeval and AgentOps (5.9k, quiet since June) the weaker sibling. I rejected all three as scope calls under the retrieval Haystack precedent. Should evaluation-review add a third observability column (Opik), a second eval-framework column (promptfoo), or stand at the current structure?
? for tom: The orchestration framework family now covers the multi-agent systems (CAMEL, AG2, AutoGen, AutoGPT, CrewAI, Agno, Dify, Mastra, LangGraph, and more), and the cross-category scan surfaced the single-vendor agent-building SDKs (openai-agents-python 29.9k, smolagents 29.7k, google adk-python 21.7k, semantic-kernel 28.6k, strands 8.7k, claude-agent-sdk 8.2k). I rejected them as SDKs for building agents rather than multi-agent orchestration systems, a family rejection recorded in the log. Should any of them get orchestration columns anyway?
? for tom: Today's one new star is p-e-w/heretic (33.8k stars, fully automatic censorship removal for model weights). It fits none of the 23 categories (it modifies models rather than providing access or running agents), so it is logged as out-of-scope. Should model-modification tooling have a home in the section, or does the rejection stand?
? for tom: Three mega-viral repositories surfaced with no clean category: garrytan/gstack (135.6k stars, Garry Tan's personal Claude Code setup as 23 opinionated agent tools), JuliusBrussee/caveman (110.3k, a skill-plus-proxy claiming 65 percent token cuts by removing articles), and Panniantong/Agent-Reach (92.9k, a CLI giving agents read and search over Twitter, Reddit, YouTube, GitHub, and Bilibili). Profile any of them (skills, context engines, or retrieval would be the nearest homes), or do personal bundles and viral novelty stay out?
? for tom: The people-and-publications scan keeps passing over vendor engineering blogs (Anthropic Engineering, OpenAI's harness-engineering write-ups) because the category has only admitted independent or practitioner-owned publications. Should a vendor engineering blog be admissible as a voice, or does that stay out of scope?
? for tom: The skills scan surfaced scale records above every prior pack rejection: K-Dense-AI/scientific-agent-skills (47.8k stars, 177 validated science skills), cathrynlavery/diagram-design (44.3k), EveryInc/compound-engineering-plugin (25.4k), and anthropics/claude-plugins-official (37.5k, the vendor-official plugin directory). The standing exclusion covers single skills and packs and vendor in-product directories. Do skills-scale records like these change the policy, or does the formats/registries/marketplaces scope stand?
? for tom: openai/symphony (27.6k stars, Apache-2.0, quiet since September 15) turns project work into isolated autonomous implementation runs, squarely the orchestration category's subject, and I logged it with the mission-control tail as a family rejection rather than writing it amid today's 45 notes. Want it profiled next run?
