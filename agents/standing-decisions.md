---
title: Standing decisions digest
created: 2026-10-14
updated: 2026-10-15
status: finished
tags: [agents]
readability: 0
---

One line per standing decision, maintained by the daily refresh.
The log (`log.md`) stays the audit trail; this digest never contradicts it.
Line format: `- YYYY-MM-DD | category | decision | one-line reason or trigger` (date = last confirmation).

## Scope rulings

- 2026-10-13 (ruled 2026-10-06) | retrieval | founding scope carries exactly two framework columns (LangChain, LlamaIndex); a third framework is an owner scope call, not an entrant signal | Haystack rejected under it, queue q#4 open
- 2026-10-13 (ruled 2026-10-07) | evaluation-review | founding structure stands: Opik, promptfoo, and AgentOps are third-column or second-framework scope calls, not entrant signals | adoption between existing columns does not override structure, queue q#6 open
- 2026-09-29 (ruled 2026-09-27) | orchestration | category scope includes multi-agent frameworks | owner approved the AMO directory's in-scope gaps; the framework tier (CrewAI, AutoGPT, AutoGen, Dify, and peers) admitted 2026-09-29
- 2026-10-10 | orchestration | self-evolving workflow frameworks slot in orchestration's framework family, not automated research | EvoAgentX routed and admitted here
- 2026-09-27 | assistant-runtimes | category scope includes local-first platforms | Open WebUI, AnythingLLM, and PrivateGPT admitted in the stars-scan resolution
- 2026-09-26 | model-access | vendor consumer subscriptions that ship an agent are access products; editor-bundled access (Cursor, Copilot) stays in surfaces pending owner direction | claude-plans and chatgpt-plans admitted on the owner's reading
- 2026-09-26 | model-access | rejected by kind: consumer assistants without a coding-agent story, pay-per-token inference hosts, enterprise clouds, gray-market discount marketplaces | Poe, Perplexity, Together, Fireworks, Groq, DeepInfra, Bedrock, Vertex, Azure, codingplan.io-style resellers
- 2026-09-27 | model-access | scope includes the self-hosted gateway software layer | litellm admitted; experiential followed the same day
- 2026-10-14 | model-access | serving stacks, chat UIs, engines, and model publishers family-route out of model access | lemonade and llama-swap held as same-slot duplicates; Decision 3.0 (HF model collection) held 2026-10-14
- 2026-10-13 (ruled 2026-10-10) | surfaces | end-user app-building platforms and general-purpose agent workspaces stay out; coding support is the category spine | tambo rejected on the app-building kind call; OpenBitFun rejected as a Cowork-style workspace, queue q#14 open
- 2026-09-12 (ruled 2026-08-24) | orchestration | terminal-family parallel-agent tools and standalone ADEs place in orchestration over surfaces | dmux and claude-squad set it, Conductor and Superset carried it, JetBrains Air applied it
- 2026-09-16 (ruled 2026-08-22) | cross-category | vendor sibling products fold into the sibling note by default | gemini-cli/Antigravity set it; applied to oh-my-pi, Codex App, OpenCode Desktop, Warp Factories, LiteParse, cursor CLI and routines; oh-my-pi left the fold on its own bar clearance 2026-10-10
- 2026-09-21 (ruled 2026-09-18) | hybrid-execution | model-layer members are admissible | Jev entered first; laya superseded the 2026-09-20 wave rejection once the model-layer objection no longer held
- 2026-09-16 | hybrid-execution | engine internals stay cited inside member notes, below the application-layer scope | xgrammar and vLLM structured outputs live inside outlines
- 2026-09-16 | automated-research | closed capability-research instruments qualify where no self-hostable runtime exists | Pion placed here over assistant runtimes
- 2026-10-04 (ruled 2026-09-24) | model-benchmark-matrix | the matrix is model-only: harness benchmarks and harness-variance studies stay out as pointers | FrontierHarness Eval, HarnessTax, JevBench, the Scaffold Effect study
- 2026-10-10 | code-review | review surfaces that judge nothing are evaluation-review members, not code-review | PR Lens shelved beside Hunk; ReviewBench confirmed evaluation-review territory 2026-10-07
- 2026-10-10 | spec-driven-development | entrants route by primary artifact: a spec contract is spec-driven even when tracker-adjacent | Intent-Router shelved here over task management; WrenAI likewise context engines over hybrid execution
- 2026-10-13 (ruled 2026-10-11) | context-engines | archived-by-owner tools are admissible on founding role and scale, not by default | Vanna admitted archived; ByteRover rejected on the distinguished precedent
- 2026-10-07 | protocols | servers and utility layers are not protocols | IBM mcp-context-forge routed to control planes instead (admitted there 2026-10-11); agnix and rulesync rejected
- 2026-10-10 (ruled 2026-10-07) | control-planes | a member must govern something: provenance recorders stay below the plane | git-ai and Invariant rejected on it
- 2026-10-07 | sandboxing | hosted-only services and environment images without an isolation boundary stay out | Deno Sandbox under the Modal precedent; AIO Sandbox an environment image, not a boundary
- 2026-10-10 | executions | data-engineering-first platforms stay out | kestra (29.5k) rejected and re-confirmed as data-engineering-first
- 2026-10-13 (named 2026-10-05) | people-and-publications | a voice is admissible only when their breakout first surfaces inside the section's coverage window; long-established and interview-only voices fail | applied in every weekly voice scan
- 2026-10-06 | trackers-and-leaderboards | single trend series are not trackers and evals nonprofits are people-category candidates | METR's time-horizon series rejected as a tracker, queue q#5 open
- 2026-10-17 | memory | the OKF-implementation family folds into the okf-agent-memory note as ecosystem evidence | mcp-memory (218 stars, dormant since 2026-08-30) and Kage held on it
- 2026-10-18 | memory | positional star ranks ("Nth of M members") are no longer maintained in note prose; the claim churned five correction rounds in two notes and went stale at every admission | memU and screenpipe rank lines dropped
- 2026-10-17 | memory | Vestige pivoted from queryless memory to a fail-closed action firewall (Strata log v4.0.0 landing 2026-09-30, the Operator gate and $149 tier v4.2.0 2026-10-06) and routes out of memory on the primary-artifact reading | admitted to control-planes the same run, 4-point Show HN July 2026 pre-pivot
- 2026-10-17 | skills | the OKF delivery-toolkit kind routes to the memory category's okf-agent-memory ecosystem family, not to skills (the skills are the delivery mechanism, and OKF packages knowledge about systems, not agent capabilities) | scaccogatto/okf-skills (417 stars) folded there 2026-10-17

## Standing family rejections

- 2026-10-12 (ruled 2026-10-07) | orchestration | single-vendor agent-building SDKs rejected as SDKs, not multi-agent orchestration systems | openai-agents-python, smolagents, adk-python, semantic-kernel, strands, claude-agent-sdk; microsoft/agent-framework and deepagents held under it, queue q#7 open
- 2026-10-18 (ruled 2026-10-07) | orchestration | mission-control dashboards and tails rejected against the absorbed canonical family | claudecodeui, open-multi-agent, background-agents, RunMaestro, agent-office, clodfarm, zeron, OpenAgents Workspace held; openai/symphony the flagged carve-out, queue q#12 open
- 2026-10-14 (ruled 2026-10-07) | assistant-runtimes | the absorbed runtime family holds: cowork desktops and claw successors resolve into existing notes, no new columns | rowboat, leon, cloudflare-os, nullclaw, LobsterAI, jev-chat-jarvis, openfang, xiryn, orkas, openpaw held; openhuman scale call open, queue q#13
- 2026-10-12 | orchestration | the 2023 dormant wave of agent repositories stays rejected | re-confirmed with fresh counts in the kaushikb11/awesome-llm-agents scan
- 2026-09-27 | cross-category | browser automation stays out of scope and no browser-agents category opens; final, not open to re-review | owner ruling on the browser-use question (116k stars declined)
- 2026-10-13 (ruled 2026-10-07) | retrieval | data infrastructure, document parsers, vector stores, and crawlers stay out of the category | pathway, CocoIndex, Omnigraph on the data-infrastructure precedent; Crawl4AI on the Firecrawl crawler rejection; DSPy under the framework family; the parser slot (kreuzberg, opendataloader-pdf, marker family) held, queue q#17 open
- 2026-10-13 (ruled 2026-09-07) | skills | the standing exclusion covers single skills, packs, community waves, and vendor in-product directories; scope is formats, registries, and marketplaces, plus optimizer and discovery tooling | scale records K-Dense 47.8k, rea.tools 109.9k, mattpocock/skills 286k escalate via queue q#11 and q#20
- 2026-10-13 | assistant-runtimes | the rafska chat-UI set (LM Studio, jan, ChatBox, text-generation-webui, SillyTavern, Page Assist) finally rejected on category kind | trigger recorded, see re-review triggers
- 2026-10-05 (ruled 2026-09-29) | orchestration | the AMO thin-record tail stays rejected | Wave, Culture, SwarmClaw, NarraNexus, Bunkhouse, handoff, Companies.sh, zachealy1/orchestrator, RustyClaw held on the handoff thin-record profile
- 2026-10-13 (ruled 2026-10-07) | cross-category | personal bundles and viral novelty repositories stay unprofiled pending the owner's ruling | gstack, caveman, Agent-Reach logged out-of-scope; ECC (278k) held on the same question, queue q#9 open
- 2026-10-12 (ruled 2026-09-27) | cross-category | the owner's own tools stay out at zero third-party adoption | llm-conversations-viewer, tps-viewer, TomzxCode/agentic; owner-tools exception asked in queue q#24
- 2026-10-07 | cross-category | model-modification tooling fits no category and stays out pending the owner's ruling | p-e-w/heretic (33.8k) logged out-of-scope, queue q#8 open
- 2026-10-10 (ruled 2026-10-06) | control-planes | closed commercial governance products stay out | Autoheal precedent holds the awesome-ai-governance closed tier at zero admissions
- 2026-10-16 | control-planes | the awesome-ai-governance open-source thin tail stays below the admission bar | conarium, verax, cedulon, quilzo, sunglasses, and Mandare (0 stars, 3 weeks old) at 0-10 stars each with no coverage, reopen on traction or independent coverage; arifOS resolved above the bar 2026-10-16
- 2026-10-12 (ruled 2026-09-21) | hybrid-execution | applications, runtime bridges, and name-alike tooling on a category member stay ecosystem evidence inside its note | jev-ultrafast folded into jev; jev-chat, vllm-jev, LLM2Jev held
- 2026-09-21 (ruled 2026-09-18) | skills | session-portability tools are out of the skills scope | Skillsync rejected by four category runs

## Owner questions governing scope

(q#N is the Nth `? for tom:` bullet in queue.md, in file order.)

- q#4 (2026-10-06) | retrieval | should Haystack become a third framework column, or does the two-framework scope stand
- q#5 (2026-10-06) | people-and-publications | should METR be profiled as a voice after its tracker rejection
- q#6 (2026-10-07) | evaluation-review | add a third observability column (Opik), a second eval-framework column (promptfoo), or stand at current structure; AgentOps rides the same question
- q#7 (2026-10-07) | orchestration | should any single-vendor agent-building SDK get an orchestration column
- q#8 (2026-10-07) | cross-category | should model-modification tooling (heretic) get a home in the section
- q#9 (2026-10-07) | cross-category | profile the mega-viral trio (gstack, caveman, Agent-Reach) or do personal bundles and viral novelty stay out
- q#10 (2026-10-07) | people-and-publications | is a vendor engineering blog admissible as a voice
- q#11 (2026-10-07) | skills | do the skills-scale records (K-Dense 47.8k, diagram-design 44.3k, compound-engineering-plugin 25.4k, claude-plugins-official 37.5k) change the pack policy
- q#12 (2026-10-07) | orchestration | should openai/symphony be profiled despite the mission-control tail rejection
- q#13 (2026-10-10) | assistant-runtimes | does openhuman (41.8k) break the absorbed-family rejection at OpenClaw-class scale
- q#14 (2026-10-10) | surfaces | which shelf (or rejection) holds for OpenBitFun, a fourth Cowork desktop candidate
- q#15 (2026-10-10) | cross-category | wire the four first dedicated lists (awesome-jev, awesome-software-factories, awesome-autoresearch, awesome-harness-engineering) into the category-source list
- q#16 (2026-10-10) | skills | admit the generator kind (Skill_Seekers) or hold the formats, registries, marketplaces scope
- q#17 (2026-10-10) | retrieval | do CocoIndex, Crawl4AI, or DSPy deserve their own columns, or do the family scopes stand
- q#19 (2026-10-11) | evaluation-review | add a security-evaluation family (AgentFence, AgentDojo, garak, DeepTeam) or hold the output-judging scope
- q#20 (2026-10-11) | skills | do the grown pack-scale records (addyosmani/agent-skills 105k, mattpocock/skills 286k, morluto/rea 109.9k) change the pack policy
- q#21 (2026-10-11) | code-review | wire the vendor-run, stale kodustech/awesome-ai-code-review list or stay on broad sources
- q#22 (2026-10-11) | harnesses | if a harnesses list gets wired, is the target stale walkinglabs or active ai-boost (name collision)
- q#24 (2026-10-12) | task-management | owner-tools exception (disclosed ownership, bar still applied) or the TomzxCode/agentic rejection stands
- q#25 (2026-10-14) | cross-category | leave the browser-automation family (browser-use and peers) out of scope or open a browser-automation family
- q#26 (2026-10-14) | automated-research | wire either, both, or neither of the two autoresearch lists (webfuse-com, WecoAI)
- q#27 (2026-10-16) | executions | wire serenakeyitan/awesome-agent-loops (214 stars, stale since 2026-06-22, recipe collection) into the category-source list or stay on broad sources
- q#28 (2026-10-16) | trackers-and-leaderboards | wire onejune2018/Awesome-LLM-Eval (659 stars, stale since 2025-11-24, academic-eval focus) into the category-source list or stay on broad sources

## Re-review triggers

- 2026-10-17 (ruled 2026-09-06) | memory | okf-agent-memory trigger fired and resolved: admitted at 814 stars on both trigger arms, three independent citations in the 392-point documentation-over-recall thread plus a second implementation (fellowgeek/mcp-memory) | supersedes the 2026-10-07 re-rejection
- 2026-10-12 | task-management | TomzxCode/agentic reopens on independent adoption or third-party coverage | rejected on the citation bar, owner's own tool
- 2026-10-13 | assistant-runtimes | the rafska chat-UI set reopens on renewed adoption (inferred) | the final rejection carries a recorded trigger the log does not name
- 2026-09-24 | people-and-publications | the humanlayer (dex-horthy) rejection is closed: overridden by owner admission, no trigger remains | the 2026-09-08 no-sustained-publication rejection was overridden 2026-09-24
- 2026-08-30 | cross-category | concord and huzzah reopen only on new independent coverage | closest below-bar calls of the 2026-08-30 candidate pile
- 2026-10-07 (ruled 2026-09-21) | cross-category | coverage-triggered holds reopen on independent coverage | thruwire/foreman, magpie, golive-skill, traycer, brooks-lint
- 2026-09-25 | hybrid-execution | MoJev reopens on independent traction | uncategorized at 29 stars, self-published
- 2026-10-15 | hybrid-execution | TypeChat reopens on a first tagged release or npm publication | 2026-10-15 re-confirmed rejection (zero releases ever), but the 10-13 push added three named TypeScript-team maintainer commits and a Programs blog post
- 2026-10-16 | assistant-runtimes | OpenAgent reopens on independent coverage or crossing the member floor | 5,698 stars but below the category floor (smallest member Octop about 9.2k), zero independent coverage, keyword-stuffed topics
- 2026-10-16 | software-factory | uzi (vtmocanu) reopens on independent coverage or a stable release | 91 stars, MIT, alpha, nightly RC train, only a self-authored write-up, below the Orbi precedent (213 stars rejected 2026-10-11)
- 2026-09-25 | trackers-and-leaderboards | bestvaluemodel reopens on a license (sustained operation demonstrated: pushed 2026-10-16 with weeks of daily refreshes) | one-day-old derivative of member Artificial Analysis at rejection
- 2026-09-25 | trackers-and-leaderboards | llm-list.com reopens on independent coverage | fully derivative of models.dev, OpenRouter, Arena, Artificial Analysis, and Hugging Face
- 2026-09-27 | hybrid-execution | drawgent reopens on a primary mirror | license and stars unverifiable from tangled.org-only hosting
- 2026-09-27 | harnesses | drawgent reopens on a primary mirror | license and stars unverifiable from tangled.org-only hosting
- 2026-10-16 | memory | Mnemoverse reopens on traction or independent coverage | 27 stars, 4 forks, hosted-first thin record far below the category floor (smallest member Emulo at 294)
- 2026-09-27 | skills | dotskills reopens on sustained traction | curated pack overlapping the Agent-Native column
- 2026-09-27 | executions | octopool reopens on traction | weeks-old ecosystem utility, thin docs
- 2026-09-27 | memory | library-mcp reopens if a writeup ships | dormant five months, thin documentation
