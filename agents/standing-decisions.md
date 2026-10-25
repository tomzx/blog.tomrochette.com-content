---
title: Standing decisions digest
created: 2026-10-14
updated: 2026-10-24
status: finished
tags: [agents]
readability: 0
---

One line per standing decision, maintained by the daily refresh.
The log under `agents/logs/` stays the audit trail; this digest never contradicts it.
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
- 2026-10-21 | model-access | serving stacks, chat UIs, engines, and model publishers family-route out of model access | lemonade and llama-swap held as same-slot duplicates; NVIDIA dynamo (datacenter-scale inference serving, starred 2026-10-21) held on the family route; Decision 3.0 (HF model collection) held 2026-10-14
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
- 2026-10-21 | spec-driven-development | the thin-tail precedent (0-10 stars, no independent coverage, reopen on traction or coverage) applies to spec-standard and blueprint kinds | ANSS (6 stars), internal-tool-blueprints (0 stars), one-man-startup (9 stars), and aide (1 star, zero coverage, spec-toolkit kind) rejected on it
- 2026-10-06 | trackers-and-leaderboards | single trend series are not trackers and evals nonprofits are people-category candidates | METR's time-horizon series rejected as a tracker, queue q#5 open
- 2026-10-17 | memory | the OKF-implementation family folds into the okf-agent-memory note as ecosystem evidence | mcp-memory (218 stars, dormant since 2026-08-30) and Kage held on it
- 2026-10-18 | memory | positional star ranks ("Nth of M members") are no longer maintained in note prose; the claim churned five correction rounds in two notes and went stale at every admission | memU and screenpipe rank lines dropped
- 2026-10-17 | memory | Vestige pivoted from queryless memory to a fail-closed action firewall (Strata log v4.0.0 landing 2026-09-30, the Operator gate and $149 tier v4.2.0 2026-10-06) and routes out of memory on the primary-artifact reading | admitted to control-planes the same run, 4-point Show HN July 2026 pre-pivot
- 2026-10-17 | skills | the OKF delivery-toolkit kind routes to the memory category's okf-agent-memory ecosystem family, not to skills (the skills are the delivery mechanism, and OKF packages knowledge about systems, not agent capabilities) | scaccogatto/okf-skills (417 stars) folded there 2026-10-17
- 2026-10-21 | evaluation-review | lukstei/slop-grader admitted as the document-and-diff grader beside Jevals, the category's second Jev-based member | skills-worker handoff resolved on the citation bar; the thin one-thread HN footprint is stated in the note, on the HermesGate precedent
- 2026-10-21 | spec-driven-development | context-engineering layers route here when the artifact is a typed spec set plus a convergence check that names the guilty side | archcore admitted on the Intent-Router primary-artifact precedent; the looptroop-ai/LoopTroop duplicate admission was retracted the same run, the orchestration member stands as the primary frame
- 2026-10-21 | control-planes | Tracekit admitted as the category's eleventh gate at 138 stars | governs calls before execution with a CT-style witness-cosigned evidence log, unlike any member; the experimental no-public-witness gap is stated in the note
- 2026-10-22 | hybrid-execution | the Decision Index 0.4 Full score is fully private (60 percent same-skills, 40 percent new-domains, the public index shown but uncounted), so member rows cite the 0.4.1 reading | board regenerated 2026-10-22 with 226 configurations, GLiDE V1.2 first at 71.52, Jev 1.14 forty-first
- 2026-10-22 | hybrid-execution | TypeChat's npm-publication reopen trigger counts a revival-era publication only, not the pre-revival npm line | the npm typechat package (latest 0.1.4, 2026-08-21) predates the 2026-10-13 revival push, asked in queue
- 2026-10-22 | cross-category | npm weekly download figures carry zero-day gaps, so adoption claims prefer the trailing-month window | context7's npm week to 2026-10-18 reported 482,795 with three zero days inside the window while the trailing month read 2,640,895
- 2026-10-22 | cross-category | notch supervision surfaces, passive notification and approval-forwarding UIs over orchestration members, reject as tails under the mission-control dashboards-and-tails family | perch (asafofer/perch, 22 stars, zero coverage) held on it
- 2026-10-22 | cross-category | guides, cookbooks, prompt references, and pattern collections are content, not tools, and stay unprofiled regardless of scale | the unmatched broad-source tail (claude-howto 42.5k, claude-code-system-prompts 13k, loop-engineering 11.6k, infrastructure-showcase 10k) reads out on it
- 2026-10-23 | automated-research | single-harness personal autoresearch ports with no independent coverage stay unprofiled | the webfuse-com/awesome-autoresearch scan's pi/mlx/webgpu/sudoku-class tail read out on it
- 2026-10-23 | cross-category | benchmark and evaluation-harness repositories are not research loops and route to evaluation-review | the webfuse-com scan surfaced mle-bench, AgentBench, MLAgentBench, ML-Bench, and mlrbench
- 2026-10-23 | automated-research | dormant members below 500 stars with no independent coverage close until new coverage lands, per the concord-and-huzzah rule | applied to Sibyl-Research-Team/AutoResearch-SibylSystem, MLR-Copilot, ResearchAgent, ML-Agent, autoresearcher, self_improving_coding_agent
- 2026-10-23 | evaluation-review | a member's subject repository moving to a redirecting path is a note-level provenance fact, not a scope change | hermes-labs-ai/hermes-gate now redirects to roli-lpci/hermes-gate; the note's twin-repo caution was rewritten to the present fact in rotation
- 2026-10-25 | automated-research | a member repository's transfer into an institutional organization is a recorded note fact, with the star-history chart and references moved to the canonical path the same run | AutoSci moved from skyllwt to PKU-DAIR (the Peking University DAIR lab of senior author Bin Cui), old URLs redirect and the README still points at them
- 2026-10-23 | model-access | upstream -pro model ids (OpenAI GPT-5.6/6 Sol/Luna/Terra Pro) are provider-side serving tiers, not aggregator-only lines; the category records them in openrouter with the same-price-more-reasoning-tokens cost trap named | resolved the 2026-10-22 section-root sighting on OpenRouter endpoints evidence (OpenAI flex/fast/ultrafast and Azure endpoints, dated snapshot ids, base-identical pricing)
- 2026-10-23 | session-analytics | CodexMonitor admitted as the category's first dormant member; dormancy within two months of a vendor surface launch is the note's finding, not a rejection reason | the 4,348-star Codex command center went quiet days after Hacker News compared it with the official Codex app
- 2026-10-23 | session-analytics | ax's session-graph core makes it session-analytics despite the repository's observability-plus-memory self-description | the memory half is session-derived introspection (retro loop, AGENTS.md fixes, skill triage), not a cross-project memory layer
- 2026-10-23 | spec-driven-development | a renamed-and-rebranded candidate re-resolves on current evidence; the old rejection carries by mechanism, not by name | BusinessLens rejected below the bar 2026-10-13, admitted as pdd-kit on the rebrand, the shipped site, and continued daily development
- 2026-10-23 | task-management | ccpm admitted as the category's forge-native kind | coordinator handoff resolved; MIT skill running PRDs onto GitHub Issues with worktree parallelism, 8,414 stars, a 175-point Show HN thread, and independent critical coverage clear the citation bar
- 2026-10-23 | trackers-and-leaderboards | the category keeps no dedicated awesome-list source; the broad sources suffice | the two candidates found 2026-10-23 fail the bar, BenchGecko/awesome-llm-benchmarks stale since creation 2026-03-27, leoncuhk/awesome-llm-bench a daily mirror of member BenchLM
- 2026-10-23 | cross-category | the andyrewlee 2026-10-22 additions resolve on standing families | Delegatus on the thin-record tail, deepseek-harness-action as wrapper tooling on an unprofiled subject, Harness by Autonomous routed to orchestration on the standalone-ADE precedent (admission resolved by the next run)

## Standing family rejections

- 2026-10-12 (ruled 2026-10-07) | orchestration | single-vendor agent-building SDKs rejected as SDKs, not multi-agent orchestration systems | openai-agents-python, smolagents, adk-python, semantic-kernel, strands, claude-agent-sdk; microsoft/agent-framework and deepagents held under it, queue q#7 open
- 2026-10-18 (ruled 2026-10-07) | orchestration | mission-control dashboards and tails rejected against the absorbed canonical family | claudecodeui, open-multi-agent, background-agents, RunMaestro, agent-office, clodfarm, zeron, OpenAgents Workspace, Ignite, Solenta, Agent Console, UpComputer held; openai/symphony the flagged carve-out, queue q#12 open
- 2026-10-14 (ruled 2026-10-07) | assistant-runtimes | the absorbed runtime family holds: cowork desktops and claw successors resolve into existing notes, no new columns | rowboat, leon, cloudflare-os, nullclaw, LobsterAI, jev-chat-jarvis, openfang, xiryn, orkas, openpaw held; openhuman scale call open, queue q#13
- 2026-10-12 | orchestration | the 2023 dormant wave of agent repositories stays rejected | re-confirmed with fresh counts in the kaushikb11/awesome-llm-agents scan
- 2026-09-27 | cross-category | browser automation stays out of scope and no browser-agents category opens; final, not open to re-review | owner ruling on the browser-use question (116k stars declined)
- 2026-10-13 (ruled 2026-10-07) | retrieval | data infrastructure, document parsers, vector stores, and crawlers stay out of the category | pathway, CocoIndex, Omnigraph on the data-infrastructure precedent; Crawl4AI on the Firecrawl crawler rejection; DSPy under the framework family; the parser slot (kreuzberg, opendataloader-pdf, marker family) held, queue q#17 open
- 2026-10-13 (ruled 2026-09-07) | skills | the standing exclusion covers single skills, packs, community waves, and vendor in-product directories; scope is formats, registries, and marketplaces, plus optimizer and discovery tooling | scale records K-Dense 47.8k, rea.tools 109.9k, mattpocock/skills 286k escalate via queue q#11 and q#20
- 2026-10-13 | assistant-runtimes | the rafska chat-UI set (LM Studio, jan, ChatBox, text-generation-webui, SillyTavern, Page Assist) finally rejected on category kind | trigger recorded, see re-review triggers
- 2026-10-19 (ruled 2026-09-29) | orchestration | the AMO thin-record tail stays rejected | Wave, Culture, SwarmClaw, NarraNexus, Bunkhouse, handoff, Companies.sh, zachealy1/orchestrator, RustyClaw held on the handoff thin-record profile; the 2026-10-19 AMO wave adds STARK OS, AIWorks, Coterie, SpaceApp, Alchemist Coder, SuperAgent, Sqwakie, and Brow
- 2026-10-19 (ruled 2026-10-07) | cross-category | personal bundles and viral novelty repositories stay unprofiled pending the owner's ruling | gstack, caveman, Agent-Reach logged out-of-scope; ECC (278k) and Cubicle Crew (29 stars, pixel-art agent-office visualization) held on the same question, queue q#9 open
- 2026-10-12 (ruled 2026-09-27) | cross-category | the owner's own tools stay out at zero third-party adoption | llm-conversations-viewer, tps-viewer, TomzxCode/agentic; owner-tools exception asked in queue q#24
- 2026-10-07 | cross-category | model-modification tooling fits no category and stays out pending the owner's ruling | p-e-w/heretic (33.8k) logged out-of-scope, queue q#8 open
- 2026-10-18 (ruled 2026-10-06) | control-planes | closed commercial governance products stay out | Autoheal precedent holds the awesome-ai-governance closed tier at zero admissions; Aident Loadout (aident.ai hosted MCP credential vault, no public repository) rejected on it 2026-10-18, also not an evaluation instrument (eval worker concurrence)
- 2026-10-19 | control-planes | the awesome-ai-governance open-source thin tail stays below the admission bar | conarium, verax, cedulon, quilzo, sunglasses, and Mandare (0 stars, 3 weeks old) at 0-10 stars each with no coverage, reopen on traction or independent coverage; arifOS resolved above the bar 2026-10-16; Ironheights (0 stars, a skill scanner that tests rather than governs) added 2026-10-19 on the governs-something ruling
- 2026-10-12 (ruled 2026-09-21) | hybrid-execution | applications, runtime bridges, and name-alike tooling on a category member stay ecosystem evidence inside its note | jev-ultrafast folded into jev; jev-chat, vllm-jev, LLM2Jev held
- 2026-09-21 (ruled 2026-09-18) | skills | session-portability tools are out of the skills scope | Skillsync rejected by four category runs
- 2026-10-19 | cross-category | terminal-output theming mods for member tools are appearance edits with no category kind | prismantis (134 stars) rejected on it; the claude-code list's new Mods section is where future additions will land
- 2026-10-21 | memory | the TeleAI list's thin-tail and closed-hosted new entries stay below the bar | Fraise (8 stars vs the 294 floor, no persistence, 1-point self-published Show HN), MemorySync (closed hosted-only API, no open engine, 22-point self-published Show HN), MoobFS (2 stars, research filesystem, self-declared not for production), and LLMSlim (17 stars, zero coverage) rejected, reopen on traction, coverage, or an OSS engine
- 2026-10-21 | spec-driven-development | trigger-and-schedule workflow automation is not spec-driven regardless of the list section it sits in | frink's primary artifact is a triggered agent workflow, reported to orchestration
- 2026-10-21 | control-planes | Praesidia joins the closed tier | proprietary platform, design-partner-only SDKs, demo-gated pricing, Autoheal precedent
- 2026-10-21 | assistant-runtimes | Orkas-VideoStudio resolves outside the category, the absorbed-family shelf keeps Orkas and its extracted toolkit is skills-kind | README states it is the extracted video agent of the absorbed Orkas desktop, agent-agnostic install into coding agents; routing flagged to skills
- 2026-10-21 | assistant-runtimes | openhuman stays held on the absorbed-family shelf pending q13 | 42.2k stars is a tenth of OpenClaw-class so the scale trigger as framed has not fired; evidence gathered for the owner
- 2026-10-21 | harnesses | generalist enterprise-automation agent frameworks are not harnesses-kind | cuga-project/cuga-agent rejected on it (web/API surfaces, AppWorld/WebArena benchmarks, no repository loop), extending the 2026-10-12 deepagents ruling; the shelf question is queued for the owner
- 2026-10-21 | cross-category | vendor field reports about a member tool fold into that member's note as ecosystem evidence | the WarpBench report folds into warp; q#10 (vendor blog as voice) untouched
- 2026-10-21 | software-factory | factory-kind candidates dormant 6+ months reject on the CodeMachine precedent without re-deriving coverage | Antfarm (2,495 stars, dormant since 2026-02-26) resolved on it; the list's own unmaintained tag is the matching signal
- 2026-10-21 | session-analytics | Aident Loadout stays out of session-analytics | an actions-and-credentials gateway with an audit feature, no session recording, indexing, cost, or live-observation cell; the 2026-10-18 control-planes closed-tier rejection stands
- 2026-10-21 | skills | Orkas-VideoStudio stays out beside its held Orkas desktop sibling | the vendor-sibling fold and the standing pack exclusion both apply to the extracted video-agent toolkit; resolved at coordinator level from the assistant-runtimes worker's routing
- 2026-10-21 | orchestration | worktree-manager CLIs slot in orchestration beside Worktrunk, not surfaces or sandboxing | gwq admitted on the terminal-family precedent (worktrees are not isolation boundaries), closing the software-factory and scanner routing flags
- 2026-10-21 | sandboxing | a repository rename resolves against the prior name's history only when that name was itself a resolved candidate; a prose mention is not a resolution | the loom-to-Overalls handoff: loom was only a mention in the geoffrey-huntley note, so overalls was judged fresh and admitted (1,557 stars, Firecracker microVM platform, research preview 2026-11-03)
- 2026-10-23 | cross-category | Mods-section additions in the claude-code list resolve as single-mod kinds under the skills exclusion | review-inbox (2 stars) the first confirmed instance, Molecular Animation (2 stars) out of scope on top of it
- 2026-10-24 | code-review | the vendor-run kodustech/awesome-ai-code-review list stays unwired as a mapped source; the category stays on broad sources | stale since 2026-06-28, HEAD carries dead, 404, and 1-star entries; evidence recorded for the open q21, its one live entrant Nayjest/Gito admitted 2026-10-24
- 2026-10-24 | memory | the TeleAI list's 2026-10-21 to 2026-10-23 additions resolve on standing families | TriMem, MemRec, BetaMem, and EvoKernel are paper-section entries rather than tools, Monolithos is closed-hosted with no open engine, Big Agentic Brain (18 stars) and agent-memory-recall (0 stars) sit below the 294-star floor
- 2026-10-24 | memory | the awesome-mcp-servers 2026-10-23 wave's memory-server cluster stays below the bar | open-memex (6 stars), MemCore (1), swarmmemo (2), IHMT-MEMORY (38), compound-memory (1) on the 294-star thin-tail floor, synapse-memory and alethech unverifiable (404); reopen on traction or coverage
- 2026-10-24 | orchestration | standalone ADEs and multi-machine command centers admit on the dmux/claude-squad/Conductor/Superset line even with vendor-hosted distribution, with coverage quality recorded as the caution | OpenHarness (autonomous-ai/openharness, 1,358 stars as of 2026-10-24) admitted with launch-echo-only coverage and vendor-only benchmarks; hosted-relay accounts and the name collision noted
- 2026-10-24 | orchestration | evidence-carrying coding agents with per-task worktree workers are orchestration kind, judged past the small-member floor with the missing-footprint signal stated | Swarm Orchestrator (moonrunnerkc/swarm-orchestrator, 112 stars, 672 npm downloads a month, one contributor) admitted; anything below v13 of the package name is a different program and stays rejected elsewhere
- 2026-10-24 | orchestration | Ivy Tendril (Ivy-Interactive/Ivy-Tendril) admitted on cross-category carry | plan-to-PR supervision of many CLI agents in parallel worktrees with human-gated review; surfaces rejected (no editor surface), software-factory rejected (loop is human-gated, not self-owning)

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
- 2026-10-18 (ruled 2026-09-21) | cross-category | coverage-triggered holds reopen on independent coverage; brooks-lint's trigger fired 2026-10-18 on the Agent Skills Hub eval (5/8 defects, flagged security blind spot) and resolved with the rejection standing (one mixed third-party measurement, planning-stage kind, no findable primary footprint) | thruwire/foreman, magpie, golive-skill, traycer remain open on coverage
- 2026-09-25 | hybrid-execution | MoJev reopens on independent traction | uncategorized at 29 stars, self-published
- 2026-10-15 | hybrid-execution | TypeChat reopens on a first tagged release or npm publication | 2026-10-15 re-confirmed rejection (zero releases ever), but the 10-13 push added three named TypeScript-team maintainer commits and a Programs blog post
- 2026-10-16 | assistant-runtimes | OpenAgent reopens on independent coverage or crossing the member floor | 5,698 stars but below the category floor (smallest member Octop about 9.2k), zero independent coverage, keyword-stuffed topics
- 2026-10-16 | software-factory | uzi (vtmocanu) reopens on independent coverage or a stable release | 91 stars, MIT, alpha, nightly RC train, only a self-authored write-up, below the Orbi precedent (213 stars rejected 2026-10-11)
- 2026-09-25 | trackers-and-leaderboards | bestvaluemodel reopens on a license (sustained operation demonstrated: pushed 2026-10-16 with weeks of daily refreshes) | one-day-old derivative of member Artificial Analysis at rejection
- 2026-09-25 | trackers-and-leaderboards | llm-list.com reopens on independent coverage | fully derivative of models.dev, OpenRouter, Arena, Artificial Analysis, and Hugging Face
- 2026-10-24 (ruled 2026-09-27) | hybrid-execution | drawgent reopens on a primary mirror | license and stars unverifiable from tangled.org-only hosting; re-checked 2026-10-24, GitHub repository search returns zero drawgent repositories and tangled.org/drawgent 404s, unmet
- 2026-10-24 (ruled 2026-09-27) | harnesses | drawgent reopens on a primary mirror | license and stars unverifiable from tangled.org-only hosting; re-checked 2026-10-24, no mirror exists, unmet
- 2026-10-16 | memory | Mnemoverse reopens on traction or independent coverage | 27 stars, 4 forks, hosted-first thin record far below the category floor (smallest member Emulo at 294)
- 2026-09-27 | skills | dotskills reopens on sustained traction | curated pack overlapping the Agent-Native column
- 2026-09-27 | executions | octopool reopens on traction | weeks-old ecosystem utility, thin docs
- 2026-09-27 | memory | library-mcp reopens if a writeup ships | dormant five months, thin documentation
