---
title: Agents log
created: 2026-08-22
status: in progress
tags: [agents, llm=glm-5.3]
readability: 0
---

Append-only log of every change agents make in this section.
One entry per run: date, articles touched, one line per change, model id.
Changes to this section that do not appear here were made by a human and must be preserved, not reverted.

## 2026-08-22

- Scaffolded the section: AGENTS.md, _index.md, log.md [glm-5.3]

## 2026-08-22 (daily refresh)

- agentic-coding-tools-landscape: created queue item 1 tracker (finished), a four-layer map of the agentic dev tool landscape as of 2026-08-22; all 17 external URLs fetched and verified during this run, 4 internal links resolve to committed articles [glm-5.3]
- _index.md: listed the new article [glm-5.3]
- AGENTS.md queue: appended `? for tom:` because the companion article the-agentic-development-environment-landscape/ is untracked, so cross-linking it would fail CI [glm-5.3]
- Queue items 2 (model selection) and 3 (context management) untouched, left for their own runs to keep this one at quality [glm-5.3]

## 2026-08-22 (owner edit)

- Moved the article queue out of AGENTS.md into agents/queue.md; queue item 1 marked done [owner, glm-5.3]
- Reworked the section on the rywalker.com/research model: added research notes as a content type (structured skeleton, citation standards) to AGENTS.md, added agents/methodology.md, rewrote queue.md around building a research index by category, restructured _index.md into essays + research index, made the daily refresh a stalest-category-first rolling re-verification [owner, glm-5.3]
- Diagnosed why /agents/ did not render like sibling sections: the root AGENTS.md file was built by Hugo as a page claiming the /agents/ URL, displacing the section _index.md; fixed by adding build render/list never front matter to both AGENTS.md files (Hugo ignores them now, tools still read them), and added visible/menu to _index.md for consistency with work/ and processes/ [owner, glm-5.3]
- Removed type: post from every file in the section and added an AGENTS.md rule never to set a type: articles here are section pages, not posts [owner, glm-5.3]

## 2026-08-22 (daily refresh, harnesses)

- Research index: seeded the Harnesses category (queue item 1) with eight notes, each with 5 sources fetched and verified during this run: claude-code, codex, gemini-cli, opencode, aider, crush, amp, junie [glm-5.3]
- gemini-cli: status recorded as superseded for individuals, Google stopped serving free and AI Pro/Ultra users on 2026-06-18 per the developers.googleblog.com transition post (Antigravity CLI is the successor); enterprise licenses and paid API keys continue [glm-5.3]
- agentic-coding-tools-landscape: cross-linked all eight harness notes, corrected the Gemini CLI line that still advertised the dead consumer free tier, updated the subscription-versus-BYOK split sentence, set updated field [glm-5.3]
- _index.md: added the research index section with the eight harness notes alphabetically [glm-5.3]
- opencode: recorded CVE-2026-22812 (unauthenticated server, mitigated in v1.1.10) and the March 2026 Anthropic legal-request removal of Claude Pro/Max OAuth (PR 18186) [glm-5.3]
- claude-code: recorded the June 2026 prompt-steganography finding and the July 2026 systima token-overhead measurements (~33k baseline tokens vs OpenCode ~7k) [glm-5.3]
- amp: recorded the December 2025 Sourcegraph spinout (Amp Frontier Corporation) and current subscription tiers [glm-5.3]
- Committed the owner's uncommitted queue.md edit adding four seed categories (Retrieval, Memory, Executions, Hybrid execution), unchanged, attributed here [owner, glm-5.3]
- Queue items 2 (model selection) and 3 (context management) remain blocked on their named dependencies (harness notes now exist for item 2; context engine notes still missing for item 3); left for their own runs [glm-5.3]
- Verification: all internal link targets checked on disk, front matter parsed as YAML, one-sentence-per-line and no-em-dash checks passed across all new and edited files [glm-5.3]

## 2026-08-23 (style conformance pass, claude-code)

- claude-code: bolded the key insight of each section (sessions portability, status verdict, strengths lead, cautions lead, pay-per-token path, bottom line) to match the per-section bolding convention used across the corpus; meaning unchanged [glm-5.3]
- claude-code: split the two longest sentences (What it is surfaces sentence, Cautions proxy-study sentence) into one sentence per line, per the short-direct-sentences rule [glm-5.3]
- claude-code: named the referent in the OpenCode comparison ("the study above" to "the July 2026 proxy study") [glm-5.3]
- claude-code: set updated to 2026-08-23 per the revise rule; status, tags, and all other front matter unchanged [glm-5.3]
- Verification: all 4 internal link targets exist on disk, 4 of 5 reference URLs fetched 200 during this run, the fifth (thereallo.dev) returns a Cloudflare challenge to automated fetches and was verified in the 2026-08-22 run, front matter parses, no em-dashes, one sentence per line [glm-5.3]

## 2026-08-23 (style conformance pass, codex)

- codex: bolded the key insight of each section (cloud runs the same agent, status verdict, strengths lead, cautions lead, Free-tier inclusion, bottom line) to match the per-section bolding convention used across the corpus; meaning unchanged [glm-5.3]
- codex: named the referent in the April 2025 caution ("that thread" to "that launch thread") [glm-5.3]
- codex: set updated to 2026-08-23 per the revise rule; status, tags, and all other front matter unchanged [glm-5.3]
- Verification: all 6 internal link targets exist on disk, all 5 reference URLs fetched 200 during this run, front matter parses, no em-dashes, one sentence per line [glm-5.3]

## 2026-08-23 (style conformance pass, crush)

- crush: hyperlinked the in-body source mentions (FSL-1.1-MIT license, Catwalk, "Crush, come home", the launch thread, the README) per the create-article link-all-sources rule [glm-5.3]
- crush: bolded the key insight of each section (LSP-enhanced TUI identity, status verdict, strengths lead, cautions lead, BYOK pricing path, bottom line) to match the per-section bolding convention used across the corpus; meaning unchanged [glm-5.3]
- crush: split the two longest sentences (opencode-ai continuation, Hyper pricing) into one sentence per line, per the short-direct-sentences rule [glm-5.3]
- crush: replaced two showy words ("terminal aesthetes" to "engineers who want the best-looking terminal", "zero spectacle" to "no frills") per the plain-vocabulary rule, and wrapped crushrc in code ticks [glm-5.3]
- crush: set updated to 2026-08-23 per the revise rule; status, tags, and all other front matter unchanged [glm-5.3]
- Verification: all 6 internal link targets exist on disk, all 5 reference URLs fetched 200 during this run, front matter parses, no em-dashes, no banned terms, one sentence per line [glm-5.3]

## 2026-08-23 (style conformance pass, junie)

- junie: bolded the key insight of each section (ACP skill sharing, status verdict, strengths lead, cautions lead, BYOK pricing path, bottom line) to match the per-section bolding convention used across the corpus; meaning unchanged [glm-5.3]
- junie: split the What it is sentence combining ACP sharing and remote control into one sentence per line, and named the referent ("It plans" to "Junie plans") [glm-5.3]
- junie: set updated to 2026-08-23 per the revise rule; status, tags, and all other front matter unchanged [glm-5.3]
- Verification: all 7 internal link targets exist on disk, all 5 reference URLs fetched 200 during this run, front matter parses, no em-dashes, one sentence per line [glm-5.3]

## 2026-08-23 (style conformance pass, opencode)

- opencode: bolded the key insight of each section (one-codebase surfaces, status verdict, strengths lead, cautions lead, BYOK pricing path, bottom line) to match the per-section bolding convention used across the corpus; meaning unchanged [glm-5.3]
- opencode: hyperlinked the in-body source mentions (July 2026 proxy study, CVE-2026-22812 disclosure, March 2026 Anthropic legal requests) per the create-article link-all-sources rule [glm-5.3]
- opencode: named the referents ("this is the continuation" to "OpenCode is the continuation", "will not drive it" to "will not drive OpenCode", "its auto-started server" to "the auto-started server", "it is off by default" to "the server is off by default"), moved the pin-your-version advisory to its own bullet per the one-sentence-per-line rule, and smoothed "Claude Code's about 33k" to "about 33k for Claude Code" [glm-5.3]
- opencode: set updated to 2026-08-23 per the revise rule; status, tags, and all other front matter unchanged [glm-5.3]
- Verification: all 6 internal link targets exist on disk, all 5 reference URLs fetched 200 during this run, front matter parses, no em-dashes, no banned terms, one sentence per line [glm-5.3]

## 2026-08-23 (daily refresh, harnesses re-verification + surfaces seed)

- Research index: re-verified the Harnesses category (the stalest and only category with notes) against live sources; 39 of 40 reference URLs returned 200, and the fortieth (thereallo.dev, cited by claude-code) fetched successfully via the browser path this run [glm-5.3]
- aider: status downgraded from "active and mature, but slower" to "development stalled" on GitHub API evidence fetched this run (no default-branch commits since 2026-05-22, last tagged release v0.86.0 from 2025-08-09); added a maintenance-risk caution and extended the bottom line; volatile numbers re-dated to 2026-08-23 [glm-5.3]
- codex: refreshed volatile numbers to about 115k stars, 17.5k forks, about 9.7k commits as of 2026-08-23 via the GitHub API [glm-5.3]
- amp, claude-code, crush, gemini-cli, junie, opencode: re-verified with no material change (stars within stated bounds, Amp pricing tiers unchanged, all links live); left untouched, and the new-entrant scan found none worth a note, Antigravity CLI stays covered inside the gemini-cli note per the queue's grouping [glm-5.3]
- Research index: seeded the Surfaces category (queue item 1) with five notes, each citing 5+ sources all fetched and verified during this run: cursor, vscode-copilot, windsurf, jetbrains, zed [glm-5.3]
- windsurf: recorded the 2025 collapse-and-rescue arc (OpenAI $3B agreement May, deal off with the CEO leaving for Google July 11, Cognition definitive agreement July 14 citing $82M ARR, employee equity dispute thread) and the June 2, 2026 Devin Desktop rebrand per Cognition's posts and docs.windsurf.com; windsurf.com itself returns 429 to every automated fetch, stated in the note with pricing left unverified [glm-5.3]
- agentic-coding-tools-landscape: replaced the stale "Windsurf still plays the AI-editor game" line with the Devin Desktop fact, cross-linked all five new surface notes, bumped the as-of date and updated field to 2026-08-23 [glm-5.3]
- _index.md: added the Surfaces category (five notes, alphabetical) and updated the aider summary to record the stall [glm-5.3]
- Queue item 1 remains open with Orchestration as the next seed category; items 2 and 3 untouched; the standing `? for tom:` about the untracked the-agentic-development-environment-landscape/ remains unanswered, so it is still not linked [glm-5.3]
- Verification: all internal link targets across the section's 15 files exist on disk, front matter parses as YAML, no em-dashes, no banned terms, one sentence per line [glm-5.3]

## 2026-08-24 (surfaces expansion, owner-requested)

- Owner request in chat: the Surfaces category was missing entries, "Google Antimatter" and "Open Chamber" named explicitly plus a scan for other popular/relevant surfaces; Antimatter does not exist (no DNS, no docs page, the Google surface is Antigravity), OpenChamber verified real, so both were covered under their actual names [glm-5.3]
- Research index: added five Surfaces notes, each citing 5+ sources all fetched and verified during this run: antigravity, openchamber, kiro, trae, void [glm-5.3]
- antigravity: recorded the four-surface platform (2.0 command center, IDE, CLI, SDK), the free tier's model list and weekly limits, the enterprise Google Cloud path, and the incident record (Nov 2025 prompt-injection exfiltration finding, Dec 2025 drive-deletion report, Feb 2026 bans, May 2026 bait-and-switch thread) [glm-5.3]
- openchamber: recorded the MIT session cockpit around the OpenCode SDK (session goals, five-model fusion, cron scheduling, private relay), v1.20.0 released 2026-08-22, 9.1k stars, and the friction record from the corpus retrospective; cross-linked six-months-with-openchamber [glm-5.3]
- kiro: recorded the spec-first IDE, credit tiers (free 50 to Power $200 with $0.04 add-on credits), the ACP-compatible-IDE clause, and the Aug 2025 prompt-injection code execution writeup [glm-5.3]
- trae: recorded the ByteDance tiers (Lite $3 through Ultra $100), SOLO mode and TraeWork cloud tasks, the separate MIT trae-agent repo, and the 954-point telemetry analysis as required reading [glm-5.3]
- void: recorded the Apache-2.0 fork's proven demand (948-point thread) against the stall (last release v1.3.4 April 2025, last push June 2026, a Dec 2025 "after Void slowed down" Show HN); status set to dormant-leaning [glm-5.3]
- agentic-coding-tools-landscape: extended the Surfaces section with Antigravity and the four-way tail (Kiro, Trae, OpenChamber, Void), bumped as-of date and updated field to 2026-08-24 [glm-5.3]
- _index.md: Surfaces category now lists ten notes alphabetically [glm-5.3]
- The owner-requested feature-matrix tables (implemented/not-implemented comparison articles per category) remain queued for a follow-up run, deliberately deferred until the Surfaces set was final [glm-5.3]
- Verification: all internal link targets across the section's 20 files exist on disk (including ../../six-months-with-openchamber and ../../send-implementation-not-issue), all cited URLs fetched 200 this run (two HN items initially 429 from burst throttling, both 200 on retry), front matter parses, no em-dashes, no banned terms, one sentence per line [glm-5.3]

## 2026-08-24 (research index seeding, all remaining categories + queue essays)

- Research index: seeded the eight remaining queue categories (Orchestration, Protocols, Context engines, Skills, Retrieval, Memory, Executions, Hybrid execution) with 34 notes, each citing 5+ sources fetched and verified during its own run [glm-5.3]
- Orchestration: claude-squad, conductor, crystal, dmux, emdash, vibe-kanban; crystal recorded deprecated 2026-02 for Nimbalyst and vibe-kanban community-maintained since Bloop shut down 2026-04, both kept as death records [glm-5.3]
- Protocols: mcp, acp, agents-md, a2a [glm-5.3]
- Context engines: augment-code, greptile, repomix, sourcegraph-code-context; the rumored Sourcegraph "Mercer" agent was unverifiable (404, no primary-source mention) and is not asserted anywhere [glm-5.3]
- Skills: anthropic-agent-skills, opencode-skills-and-plugins, skills-sh, agent-skills-open-standard [glm-5.3]
- Retrieval: llamaindex, langchain, semantic-code-search, tree-sitter-chunking [glm-5.3]
- Memory: mem0, letta, zep, file-based-agent-memory [glm-5.3]
- Executions: claude-code-hooks, copilot-automations, github-agentic-workflows, n8n [glm-5.3]
- Hybrid execution: openai-structured-outputs, anthropic-structured-outputs, instructor, outlines [glm-5.3]
- Queue item 2 published: model-selection-for-coding-tasks (essay, task-class tiers plus per-token economics, links all eight harness notes) [glm-5.3]
- Queue item 3 published: context-management-patterns (essay, pattern families grounded in harness docs, links the context engine and retrieval notes) [glm-5.3]
- queue.md: items 2 and 3 marked done [glm-5.3]
- _index.md: added both essays and the eight new categories; the five notes from the surfaces-expansion run earlier today were already indexed there, OpenChamber keeps its Surfaces placement from that run [glm-5.3]
- agentic-coding-tools-landscape: left untouched; cross-linking the 34 new notes into the tracker is left to the next daily refresh as its own focused pass [glm-5.3]
- Process: notes were written by 12 parallel opencode runs (two relaunched after fetch rate-limit deaths); every run was constrained to create only its own new note files and run no git commands [glm-5.3]
- Verification: all 36 new files carry the mandatory tags with no type field, 5+ references each, no em-dashes or banned terms, and every internal link target across the section exists on disk [glm-5.3]
- Not committed: all changes left in the working tree for owner review [glm-5.3]

## 2026-08-24 (comparison matrices, owner-requested)

- Owner request from earlier in the day, delivered this run: created the feature-matrix articles (implemented/not-implemented comparison tables per category) as two new pages, harness-feature-matrix (8 harnesses x 11 feature rows) and surface-feature-matrix (10 surfaces x 11 feature rows), with a four-state legend (yes/no/partial/unverified) and every cell traced to sources in the notes or references [glm-5.3]
- Cell verification fetches this run: cursor.com/docs/settings/api-keys (200, Cursor BYOK), antigravity MCP docs (present), opencode.ai/docs/providers (Ollama and LM Studio, local models) and /docs/mcp-servers (200, after /docs/mcp moved), JetBrains/junie repo MCP mentions, docs.trae.ai/ide/mcp and /ide/agent-rules (Trae MCP and 40 AGENTS.md mentions), kiro.dev/docs MCP mentions, zed.dev/docs/ai/agents AGENTS.md mention, cursor.com/docs/context/rules (57 AGENTS.md mentions); Antigravity AGENTS.md support found no mention and is marked unverified rather than asserted absent [glm-5.3]
- Reading the trees: 12 parallel-run notes from the previous entry were committed by the owner as 5b2679e7 before this run; the working tree was clean at sync, one transient status race on model-selection-for-coding-tasks/index.md resolved to identical content [glm-5.3]
- _index.md: added a Comparison matrices subsection under Essays and trackers listing both pages [glm-5.3]
- Verification: all internal link targets across the section's 59 index files exist on disk (the 34 notes from 5b2679e7 plus both matrices), front matter parses with no type field, mandatory tags present, no em-dashes, no banned terms, one sentence per line in prose [glm-5.3]
- Style fix: emdash note line 61 used "laptop-shaped" ("shape" is a banned term repo-wide); reworded to "assumes the work happens on your laptop", caught by the pre-commit style sweep that ran alongside the matrix commit [glm-5.3]

## 2026-08-24 (cmux note, owner-requested)

- Owner request in chat: cover cmux; research found three products by that name, so the note covers the dominant one (manaflow-ai/cmux, the libghostty macOS terminal for parallel agents, about 26.4k stars) and disambiguates the other two inside the note (craigsc/cmux "tmux for Claude Code", and the separate October 2025 Show HN Coding Agent Multiplexer), plus the unrelated Go connection multiplexer [glm-5.3]
- cmux: recorded the attention-routing thesis (notification rings and unread panel as the actual product), the open-core split (GPL-3.0-or-later terminal free, cloud VMs and CodeRouter at $24/month from cmux.com/pricing fetched this run), the fast-cadence evidence (18 releases in two days at launch, v0.64.x, nightly), the three-contributor concentration under Manaflow Inc., and the August 2026 SSH-freeze friction thread [glm-5.3]
- _index.md: cmux added to the Orchestration category, alphabetically after claude-squad [glm-5.3]
- Placement decision: Orchestration rather than Surfaces, matching dmux and claude-squad (terminal-family parallel-agent tools) rather than the editor and environment entries [glm-5.3]
- Verification: all 6 cited URLs fetched 200 this run (one HN item 429 on burst, 200 on retry), all internal link targets exist on disk, front matter parses, no em-dashes, no banned terms, one sentence per line [glm-5.3]

## 2026-08-24 (model selection guide, Kimi and GLM coverage)

- model-selection-for-coding-tasks: added the Kimi and GLM lineups per owner request; all four new pricing/provider URLs fetched and verified during this run (Moonshot K3 and K2.7 Code pricing pages, Z.ai pricing page, OpenCode providers directory) [glm-5.3]
- New section "The challengers reset the price floor": GLM-5.3/5.2/5.1 at $1.40/$4.40 with GLM-5 at $1/$3.20, kimi-k2.7-code at $0.95/$4.00 with 256K context and a 2x-price HighSpeed variant, kimi-k3 at $3/$15 with flat-price 1M context and always-on reasoning, GLM-4.7-Flash free; disagreeable claim added that the rational token-payer default is now a challenger model through OpenCode [glm-5.3]
- Table extended with three rows; the cached-reads bullet corrected from "one tenth everywhere" to one tenth at the big three and Kimi K3 versus about one fifth at GLM and K2.7 Code; the whole-repo bullet now records Kimi K3 as the second flat-1M option [glm-5.3]
- Decision guide: added price-floor BYOK and whole-repository-read bullets; re-verify list widened from three to five provider pricing pages [glm-5.3]
- Verification: no broken internal links, front matter parses, no em-dashes or banned terms, one sentence per line, references now 10 [glm-5.3]

## 2026-08-24 (model selection guide, DeepSeek V4 coverage)

- model-selection-for-coding-tasks: added the DeepSeek V4 lineup per owner request; the pricing page fetched and verified during this run [glm-5.3]
- v4-pro at $1.32/$3.96 peak with all hours outside weekday 01:00-04:00 and 06:00-10:00 UTC billed at half ($0.66/$1.98 off-peak), v4-flash at $0.44/$1.32 peak and $0.22/$0.66 off-peak, both flat 1M context with 384K max output, thinking mode default, cache hits at $0.044/$0.014 (about one thirtieth, the deepest in the guide), and an Anthropic-format endpoint for Claude-speaking harnesses [glm-5.3]
- Disagreeable claim updated to name deepseek-v4-pro in the default-loop trio; the Gemini Flash "cheapest input" line corrected (v4-flash beats it with no expiry); decision-guide bullets and the re-verify list (now six providers) updated; off-peak scheduling added to What to Do Next [glm-5.3]
- Verification: no broken internal links, no em-dashes or banned terms, one sentence per line, references now 11 [glm-5.3]

## 2026-08-24 (feature matrices, remaining categories, owner-requested)

- Owner request in chat: extend the feature-matrix treatment to every remaining research index category; created eight matrices in the harness/surface format (intro thesis, legend, table, reading, choosing, see also, references), each cell tracing to its linked note [glm-5.3]
- orchestration-feature-matrix: seven tools (claude-squad, cmux, conductor, crystal, dmux, emdash, vibe-kanban) with the death and orphan stories carried into the reading section [glm-5.3]
- protocols-feature-matrix: thesis that the four stack rather than compete and adoption falls up the stack (near-universal MCP, 60k-project AGENTS.md, rising ACP, no native A2A speaker among the harnesses); consolidations recorded (IBM ACP into A2A, Junie protocol into ACP) [glm-5.3]
- context-engines-feature-matrix, skills-feature-matrix, retrieval-feature-matrix, memory-feature-matrix, executions-feature-matrix, hybrid-execution-feature-matrix: four columns each, rows adapted per category (guarantee mechanism for hybrid execution, memory model and lock-in for memory, trigger and execution location for executions) [glm-5.3]
- _index.md: all eight matrices listed under Comparison matrices [glm-5.3]
- Process: written by 8 parallel opencode runs (orchestration relaunched once after a fetch rate-limit death); reference URLs inherit verification from the category notes except where a run fetched fresh; runs created only their own file and ran no git commands [glm-5.3]
- Verification: all 8 files carry mandatory tags with no type field, 6-8 references each, no em-dashes or banned terms, and every internal link target across the section exists on disk [glm-5.3]

## 2026-08-24 (daily refresh, harnesses re-verification + three entrants)

- Stalest category computed as Harnesses (amp at 2026-08-22, the rest 08-22/08-23); re-verified all 8 member notes against live sources [glm-5.3]
- Link check: 39 of 40 reference URLs fetched 200 this run; the fortieth (thereallo.dev, cited by claude-code) still returns a Cloudflare challenge to automated fetches, same behavior as the previous two runs, verified 2026-08-22 [glm-5.3]
- aider: stall re-confirmed via the GitHub API (pushed_at still 2026-05-22, latest tagged release still v0.86.0 from 2025-08-09); left untouched [glm-5.3]
- amp: pricing tiers re-verified unchanged; recorded the widened linked-subscription set (X Premium+/SuperGrok and SpaceX AI alongside ChatGPT, per the pricing page and homepage fetched this run); verified-as-of line and updated field bumped [glm-5.3]
- claude-code: repository scale refreshed to about 142.8k stars and about 15.2k open issues and pull requests as of 2026-08-24 (GitHub API); the old "5k+ open issues" materially understated the tracker [glm-5.3]
- codex: repository scale refreshed to about 116.7k stars and 17.8k forks as of 2026-08-24 (GitHub API); pricing page re-verified unchanged [glm-5.3]
- crush, gemini-cli, junie, opencode: re-verified with no material change (stars within stated bounds, releases current, all links live); left untouched per the no-change precedent [glm-5.3]
- New-entrant scan added three harness notes, each citing 6-7 sources all fetched this run: cline (about 66.8k stars, VS Code-extension-born runtime now CLI+kanban+SDK, 5,083,914 marketplace installs), goose (about 53.4k stars, Block's Rust agent moved to the Agentic AI Foundation at the Linux Foundation on 2026-04-07), qwen-code (about 27.3k stars, Alibaba's Gemini CLI fork with the 2,000 requests/day launch free tier) [glm-5.3]
- cline: ClinePass ($9.99/month open-weights subscription across Z.ai, Moonshot, DeepSeek, MiniMax, MiMo, Qwen) and the not-open-sourced JetBrains plugin recorded; vendor 8M+ install claim checked against the marketplace's 5.1M [glm-5.3]
- goose: the AAIF move announcement and the ACP subscription-reuse path recorded; the "60% of Block" adoption figure marked as third-party course-site sourcing, not Block's own [glm-5.3]
- qwen-code: the April 2026 Taiwan-correction behavior report and Alibaba-hosted install/OAuth routing recorded as cautions; the README's Claude Code parity table marked vendor-asserted [glm-5.3]
- agentic-coding-tools-landscape: independent-tail section extended with the three entrants [glm-5.3]
- _index.md: Harnesses category now lists 11 notes alphabetically [glm-5.3]
- Queue: items 2 and 3 done previously; the standing `? for tom:` about untracked the-agentic-development-environment-landscape/ remains unanswered, so it stays unlinked [glm-5.3]
- No self-directed essay this run: the entrant scan plus re-verification filled the day, and nothing else clears the quality bar; extending harness-feature-matrix with the three new columns is left for a focused pass [glm-5.3]
- Verification: all 74 section files link-checked with 0 broken internal targets, front matter parses as YAML with no type field, mandatory tags present, no em-dashes or banned terms, one sentence per line [glm-5.3]

## 2026-08-25 (owner edit, rules change)

- AGENTS.md: owner-directed in chat; added a Comparison matrices section requiring every feature matrix to update in the same run its category's membership changes (new note, move, or retirement), with new-category seeding allowed to defer the matrix only if the deferral is logged [owner, glm-5.3]
- AGENTS.md: daily refresh step 6 now includes the matrix sync alongside the _index.md update, and step 4 verification now checks that every feature matrix matches its category's current membership [owner, glm-5.3]
- No article content touched this run; the harness-feature-matrix columns for cline, goose, and qwen-code (added 2026-08-24) remain the outstanding work the new rule governs, for the next daily refresh [glm-5.3]

## 2026-08-25 (matrix refresh, owner-requested)

- Owner request in chat: refresh all ten feature matrices; ran the membership check from the new AGENTS.md rule, and exactly one matrix lagged its category, harness-feature-matrix missing the three harness notes added 2026-08-24; the other nine (surfaces, orchestration, protocols, context engines, skills, retrieval, memory, executions, hybrid execution) each link every current category member, so they were left untouched [glm-5.3]
- harness-feature-matrix: extended from 8 to 11 columns (cline, goose, qwen-code inserted alphabetically), all 33 new cells traced to sources fetched this run; as-of date and updated field bumped to 2026-08-25 [glm-5.3]
- Cell verification fetches this run: cline rules docs (native AGENTS.md plus .clinerules, auto-detected .cursorrules and .windsurfrules; read via the docs mdx source after the JS-rendered page came back empty), goose using-goosehints guide (CONTEXT_FILE_NAMES default ["AGENTS.md", ".goosehints"] with nested loading), goose sitemap plus subagents, hooks, plugins, and experimental VS Code extension pages, qwen settings page (QWEN.md convention, 18 mentions, and experimental.cron default false for in-session cron tools) [glm-5.3]
- Notable cells: cline reads AGENTS.md natively (unlike the 2025 extension era), goose reuses Claude/ChatGPT/Gemini subscriptions via ACP, qwen's scheduled runs marked ~ experimental because the cron tools ship default-off, all three entrants scored ✗ on cloud execution [glm-5.3]
- Reading and Choosing sections updated for eleven harnesses: open-client groups now seven auditable clients, local-model purists list widened, the everyone-lacks-a-different-feature thesis extended to the three entrants, one new choosing bullet for AGENTS.md rules portability (cline, goose, opencode) [glm-5.3]
- References extended from 6 to 9 with the three new column sources [glm-5.3]
- Verification: matrix table is 13 rows x 12 cells with consistent column counts, all 74 section files link-checked with 0 broken internal targets, front matter parses with no type field, no em-dashes or banned terms, one sentence per line [glm-5.3]

## 2026-08-25 (matrix viewer component, owner-requested)

- Owner request in chat: build a custom component for reading the growing matrices; implemented in the site repository (blog.tomrochette.com), outside this content repo, so nothing under agents/ changed except this log and the methodology note [glm-5.3]
- Site changes: a table render hook wrapping every Markdown table in a scrollable region (pinned header row and label column, zebra rows; tables with six or more columns tagged wide), CSS in the auto-bundled custom.css using the theme's light and dark neutral variables, and a deferred vanilla-JS layer adding column-picker chips and a row filter to wide tables only, with per-browser persistence and guards preventing hiding the label column or the last visible column [glm-5.3]
- Content stays plain Markdown tables: the cell-traces-to-note convention, CI link checks, and readable diffs are unaffected; methodology.md updated with a Matrix presentation section documenting the split [glm-5.3]
- Verification: site built with Hugo v0.166 (643ms), matrix pages emit the wide wrapper with role, aria-label, and tabindex, small tables emit the plain wrapper, table links render unchanged, the script passes node --check, and the minified fingerprinted asset loads deferred [glm-5.3]

## 2026-08-25 (matrix viewer, value-based column filter, owner-requested)

- Owner request in chat: let readers hide columns by a row's value, example given: keep only surfaces supporting local models; implemented in the site repository's tables.js, no content files changed beyond this log and the methodology sentence [glm-5.3]
- Behavior: clicking a body cell in a wide table keeps only the columns whose cell in that row shares the clicked cell's state glyph (the four legend states), Shift-click keeps the opposite, clicking the same cell again or the filter chip clears it; the active filter shows as a chip naming the row and state, the active row's label is emphasized, and the filter intersects with the persisted column-picker selection and the row search; the value filter itself is transient and not persisted [glm-5.3]
- Verification: script logic smoke-tested with a minimal DOM harness in Node (initial all-visible, filter by a \u2717 cell keeps only matching columns, second click clears, Shift-click keeps the complement), node --check passes on source and built bundle, Hugo build clean [glm-5.3]

## 2026-08-25 (daily refresh, surfaces re-verification)

- Stalest category computed as Surfaces (cursor, jetbrains, vscode-copilot, windsurf, zed at 2026-08-23, never targeted by a refresh run; Harnesses tied on oldest date but was refreshed 2026-08-24); re-verified all 10 member notes against live sources [glm-5.3]
- Link check: all 45 cited URLs fetched 200 this run (25 vendor/docs pages, 20 Hacker News threads spaced to avoid burst throttling), plus repository state via the GitHub API; windsurf.com still returns 429 to every automated fetch, same as documented, and is not cited [glm-5.3]
- cursor, vscode-copilot, windsurf, jetbrains, zed, antigravity, void: re-verified with no material change (stars within stated bounds, pricing tiers unchanged, all links live); left untouched [glm-5.3]
- kiro: corrected the status attribution, the release cadence lives on the vendor changelog (weekly, latest 2.19.1 on August 21, 2026, fetched this run) not the GitHub tracker, which has been quiet since June 22, 2026; changelog added as a reference; verified-as-of dates and updated field bumped [glm-5.3]
- trae: recorded the trae-agent stall, last commit February 5, 2026 and no tagged release ever published (GitHub API, as of 2026-08-25); the open-source sidecar bullet now reads as a snapshot, not a maintained dependency; verified-as-of dates and updated field bumped [glm-5.3]
- openchamber: volatile numbers refreshed to about 9.2k stars and 964 forks as of 2026-08-25, v1.20.0 still the latest release, commits landing the morning of verification; verified-as-of dates and updated field bumped [glm-5.3]
- New-entrant scan: PearAI (765 stars, slowing since June) and Qoder (no meaningful public footprint) fail the credibility bar, no other credible surface entrant found; no note added [glm-5.3]
- Category fit re-checked: all 10 members stay in Surfaces (OpenChamber keeps its placement, Windsurf stays as the pivot record, Void stays as the dormancy record); surface-feature-matrix verified to list all 10 current members, unchanged [glm-5.3]
- Queue: the standing `? for tom:` about untracked the-agentic-development-environment-landscape/ remains unanswered, so it stays unlinked; no other actionable item [glm-5.3]
- No self-directed essay this run: the category re-verification plus three note corrections filled the day, and nothing else clears the quality bar [glm-5.3]
- Verification: all 70 section files pass front matter parsing with no type field, mandatory tags present, no em-dashes, no banned terms or compounds, one sentence per line, and 0 broken internal link targets [glm-5.3]

## 2026-08-26 (research note, cognee, owner-prompted)

- Owner prompt in chat ("no new topic to investigate?"): ran an entrant scan beyond the surfaces category; candidates verified via the GitHub API were Roo Code (24.3k stars but no pushes since 2026-05-15, needs its own investigation), Continue (35.6k stars, active), spec-kit (131k stars, active), and cognee (30.3k stars, active); none covered anywhere in the corpus [glm-5.3]
- Research index: added the cognee note to Memory, citing 7 sources all fetched this run (repo, landing, pricing, docs, PyPI JSON API, two Show HN threads); recorded the thin HN footprint (9- and 6-point threads) as the community signal, the whole-engine Apache-2.0 licensing, v1.5.3 released August 23, 2026, and the flat cloud pricing ($2.50 per 1M tokens plus $5 per workspace) [glm-5.3]
- memory-feature-matrix: extended from 4 to 5 columns (cognee inserted second, after Files), contradiction-handling and audit-trail cells marked ? rather than asserted, reading section gains the whole-engine-open exception sentence, choosing section gains the flat-billing bullet, references extended to 10; updated field bumped [glm-5.3]
- _index.md: cognee added to the Memory list, alphabetically first [glm-5.3]
- Date correction: the previous entry in this log is dated 2026-08-25 but that run and this one both occurred on 2026-08-26; the as-of dates inside kiro, trae, and openchamber from that run were also written as 2026-08-25 when the fetches happened on 2026-08-26; recorded here rather than churning three files by one day [glm-5.3]
- Roo Code stall, Continue, and spec-kit left as scan candidates for future runs: one note done well beats three done thin [glm-5.3]
- Verification: all 71 section files pass front matter parsing with no type field, mandatory tags present, no em-dashes, no banned terms, one sentence per line, and 0 broken internal link targets; all 7 new reference URLs fetched 200 this run [glm-5.3]

## 2026-08-26 (research note, spec-kit, new category, owner-prompted)

- Owner prompt in chat ("would it be relevant to cover spec options, spec-kit, Kiro?"): Kiro is already covered as a Surfaces note centered on spec mode, so the gap is spec-kit and the spec-driven development movement it anchors; no existing article in the section or tracked corpus covers it (the-future-of-code-review and send-implementation-not-issue engage adjacent ideas and are cross-linked) [glm-5.3]
- Research index: seeded the Spec-driven development category with the spec-kit note, citing 8 sources all fetched 200 this run (repo plus GitHub API, official docs, GitHub launch post, lead maintainer's anniversary post, marmelab critique, three HN threads including the 225-point waterfall-strikes-back one) [glm-5.3]
- spec-kit: recorded first commit August 21, 2025, v1.0.0 and v1.0.1 both shipped August 21, 2026, 131,489 stars and about 11.8k forks as of 2026-08-26, original creators moved on per the anniversary post, the 30-plus integration surface, and the constitution/specify/plan/tasks/implement/converge workflow [glm-5.3]
- Matrix deferral, per the seeding rule: the new category starts with one member, so its feature matrix is deferred to a dedicated follow-up run once Tessl and the SDD CLI ecosystem get notes; Kiro stays in Surfaces (an IDE whose spec workflow is a feature) and is cross-referenced rather than moved [glm-5.3]
- _index.md: new Spec-driven development category listed after Hybrid execution [glm-5.3]
- Verification: all 72 section files pass front matter parsing with no type field, mandatory tags present, no em-dashes, no banned terms (the upstream README and anniversary post use them; the note quotes neither), one sentence per line, and 0 broken internal link targets [glm-5.3]

## 2026-08-26 (review-driven maintenance pass, owner-prompted)

- Owner prompted a full section review; review found 7 must-fix and ~18 should-fix items, all addressed this run [x-preview-f-free]
- goose and agentic-coding-tools-landscape: reconciled the AAIF timeline that split the section; Block contributed goose at the foundation's formation on December 9, 2025 (per the aaif.io press release, fetched live), and April 7, 2026 is the migration-completion date per goose-docs.ai/blog; both articles now carry both dates [x-preview-f-free]
- harness-feature-matrix: replaced dead cline-rules docs URL with docs.cline.bot/features/cline-rules (fetched 200); added Junie to the local-models-plus-MCP list so guidance matches its own cells; expanded the rules-portability list to include Amp, Codex, and Crush per the AGENTS.md row; added first-person reading line [x-preview-f-free]
- surface-feature-matrix: added first-person reading line per writing rules [x-preview-f-free]
- retrieval-feature-matrix: fixed self-contradiction claiming legacy LangChain code-splitter docs no longer resolve while citing that same URL; reworded to frozen documentation (URL verified 200) [x-preview-f-free]
- aider: replaced mis-cited HN reference (43708025 is the Codex CLI launch thread) with HN 43672712 "Wasting Inferences with Aider" (verified via Algolia API), keeping the note at five sources; aligned header verification date to 2026-08-23; first-person line in Bottom line [x-preview-f-free]
- codex: qualified the overbroad only-open-source-CLI thesis to what distinguishes it from Gemini CLI (an Apache-2.0 CLI individuals can still run); aligned repo-stats reference date; first-person split in Bottom line [x-preview-f-free]
- gemini-cli: mirrored fix, strength bullet now claims first rather than only; linked Antigravity sibling note in Compared to; first-person admission on past recommendations [x-preview-f-free]
- claude-code: grounded the March 2026 sourcemap-leak caution with the dated March 31 event plus HN 47584540 as reference (2,095 points, verified via API); swapped the 403-returning reallo.dev citation for its archive.org snapshot (fetched 200); first-person line in Bottom line [x-preview-f-free]
- cline: linked the previously named-but-unreferenced Ask HN token-usage thread (48525711, verified via Algolia) both inline and in references; first-person line in Bottom line [x-preview-f-free]
- amp: first-person line in Bottom line per writing rules [x-preview-f-free]
- n8n: grounded the community-strengths claim by adding both cited HN threads as references (launch 21191676 at 728 points, Series C 45525336 at 235 points, point counts verified via API) [x-preview-f-free]
- claude-squad: converted malformed plain-text Compared-to paths to markdown links; rewrote two unsourced ecosystem claims into git-semantics and product facts; dropped the meta-label before the disagreeable claim; added updated field [x-preview-f-free]
- file-based-agent-memory: corrected the HN 46294274 label to match the letta note (Letta Code launch thread); replaced the loose /doctor-style trimming analogy with a grounded pruning sentence [x-preview-f-free]
- model-selection-for-coding-tasks: clarified the $100 crossover math (50M raw input tokens at $2/M versus about 20M blended tokens at agentic output ratios) so it no longer reads against its own table; added DeepSeek to the challengers mention [x-preview-f-free]
- agents-md: fixed the our-note antecedent to name the July 2026 proxy study and the Claude Code note; indented the ETH Zurich continuation under its Cautions bullet; added updated field [x-preview-f-free]
- agent-skills-open-standard, opencode-skills-and-plugins, skills-sh: restored the mandatory Not-for-Y bottom-line clauses; agent-skills-open-standard additionally gained Anthropic's untrusted-skills engineering post as its critical source [x-preview-f-free]
- semantic-code-search: stated the missing independent-footprint signal explicitly per the citation standard instead of implying third-party evidence exists; added updated field [x-preview-f-free]
- cursor: resolved the Grok ownership contradiction (xAI listed as third-party while calling Grok Cursor's own) by tying Grok to the SpaceXAI partnership [x-preview-f-free]
- _index.md one-liners refreshed where they lagged revised content: harness matrix now eleven harnesses verified 2026-08-25, memory matrix four services, codex description matches its qualified thesis [x-preview-f-free]
- Every touched article gained llm=x-preview-f-free alongside glm-5.3 (never removed) and updated set to 2026-08-26; untouched notes deliberately left without updated pending an owner decision on backfilling [x-preview-f-free]
- Verification: 71 section files pass front matter parsing, zero broken internal link targets, zero em-dashes or banned terms, one sentence per line; all newly added external URLs fetched 200 or verified via the HN Algolia API this run [x-preview-f-free]

## 2026-08-26 (daily refresh, orchestration re-verification + extension-generation exits)

- Stalest category computed as Orchestration: its notes sit at creation date 2026-08-24 with no `updated` field and it was never targeted by a refresh run, while Harnesses (08-23/08-24 notes) and Surfaces (08-23 notes) both had dedicated re-verification runs since; re-verified all 7 member notes against live sources [glm-5.3]
- Link check: all 39 orchestration reference URLs verified this run (34 fetched 200 directly; HN throttled this IP to 429 on every direct fetch, so the five cited threads were verified via the Algolia items API, titles, points, and dates all matching); conductor.build now 307-redirects to www.conductor.build and emdash.ai to emdash.com, both resolving 200 [glm-5.3]
- claude-squad, cmux, conductor, crystal, dmux, emdash: re-verified with no material change (stars within stated bounds, crystal still dead with last push 2026-02-26, conductor changelog still at 0.82.0, cmux pushing the morning of verification); left untouched per the no-change precedent [glm-5.3]
- vibe-kanban: sharpened the community-maintenance claim on evidence, no push since 2026-04-24, npm still at 0.1.44, open issues 383 to 533 between 2026-08-24 and 2026-08-26 (GitHub API); status bold line rewritten, the nobody-is-paid caution extended, verified-as-of and updated bumped [glm-5.3]
- emdash: references moved to the canonical emdash.com domain (the .ai host 301-redirects, both fetched 200 this run); verified-as-of and updated bumped [glm-5.3]
- New-entrant scan for Orchestration: Backlog.md verified credible (6.5k stars, active) but is process/task tooling rather than a parallel-agent dashboard, so it is recorded here as a candidate for the Spec-driven development category instead of joining this one; no orchestration entrant cleared the bar [glm-5.3]
- Queue item 1 (standing research index): wrote the two scan candidates left by the 2026-08-26 cognee run, both Surfaces death records with 7-8 sources each, all fetched 200 or Algolia-verified this run [glm-5.3]
- continue: recorded the Cursor acquisition (announced 2026-06-15 per the homepage banner and HN 48548758), the read-only README with final 2.0.0 (telemetry and auth removed, tagged 2026-06-19), 35,644 stars, 4,001,358 marketplace installs at a 3.26 rating as of 2026-08-26, and the quiet Ask HN funeral thread; the earlier scan's "active" reading corrected here [glm-5.3]
- roo-code: recorded the scheduled sunset (announcement 2026-04-20, archived because roocode.com now sells the pivot product; support ended 2026-05-15 with Cloud and Router shut down and refunds), last release v3.54.0 and last push both 2026-05-15, 24,325 stars, 1,956,325 installs at a 4.72 rating, the AGENTS.md-reading rules system, and the pivot to roomote.dev with its "we don't believe IDEs are the future of coding" rationale [glm-5.3]
- surface-feature-matrix: extended from 10 to 12 columns (Continue and Roo Code inserted alphabetically) in the same run per the matrix rule; 22 new cells traced to sources fetched this run (Continue rules docs for the AGENTS.md cell, Roo custom-instructions docs for its AGENTS.md and .roorules cells, Roo MCP overview, Ollama guides both sides); reading section gains the death-records paragraph; verified-date line and references extended [glm-5.3]
- agentic-coding-tools-landscape: surfaces tail extended with the two 2026 exits and the Cline consolidation sentence; as-of line qualified [glm-5.3]
- _index.md: Continue and Roo Code added to Surfaces alphabetically, surface matrix one-liner now twelve surfaces verified 2026-08-26, vibe-kanban one-liner updated to the orphaned framing [glm-5.3]
- Matrix membership check: surface-feature-matrix columns match the 12 on-disk surfaces exactly; orchestration-feature-matrix still matches its 7 members; queue unchanged (the standing `? for tom:` about untracked the-agentic-development-environment-landscape/ remains unanswered, so it stays unlinked) [glm-5.3]
- No self-directed essay this run: the category re-verification plus two death-record notes with their matrix columns filled the day at quality [glm-5.3]
- Verification: 73 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets across the section, no em-dashes or banned terms in changed files, one sentence per line, and every URL cited by new or edited content fetched 200 or was verified via the HN Algolia API during this run [glm-5.3]

## 2026-08-27 (owner-prompted, task management category + gastown placement)

- Owner request in chat: collect the LLM task trackers (backlog.md, beads named) and place Gastown; research found the task-tracker layer to be three credible tools plus one orchestration system, all uncovered in the corpus [glm-5.3]
- Research index: seeded the Task management category with three notes, each citing 6-7 sources fetched 200 or verified via the HN Algolia API this run: backlog-md, beads, task-master [glm-5.3]
- beads: recorded the gastownhall org rename from steveyegge (the old API path 301-redirects), the Dolt-backed architecture (embedded or server, sync via bd dolt push/pull), 26,630 stars and v1.2.2 of 2026-08-15, the missing Show HN launch thread stated as the community signal, and the ecosystem as caution (beads_rust freezing classic beads at 1,062 stars, the 84-point markdown-replacement thread as the critical source) [glm-5.3]
- task-master: recorded the productization, the repo quiet since 2026-04-28 with the last release 0.43.1 on 2026-03-31 while npm still does 82,718 downloads a month, the license now MIT with Commons Clause Condition v1.0 (fetched from the LICENSE file), and the Hamster (Wheel Go Fast, Inc.) commercial successor at Free and $40 per creator per month [glm-5.3]
- backlog-md: recorded the three-checkpoint review model (spec, plan, code), the dogfooding claim, terminal kanban plus local web UI, 6,551 stars with a 254-point launch thread and 50,970 npm downloads a month [glm-5.3]
- gastown: placed in Orchestration per the owner's question, because the repo self-describes as a multi-agent workspace manager (Mayor, polecats, worktree hooks, Refinery Bors-style merge queue) rather than a task tracker; recorded 17,801 stars, v1.2.1 of 2026-06-06, the HN footprint (354, 403, 253, 113-point threads), Maggie Appleton's field analysis as the observational source (costs, meme coin, design-as-bottleneck), and the credits-governance issue 3649 [glm-5.3]
- orchestration-feature-matrix: extended from 7 to 8 columns (Gas Town inserted alphabetically after Emdash) in the same run per the matrix rule, all 10 cells traced to the gastown README and the Appleton analysis fetched this run; reading gains the merge-queue exception line, choosing gains the 20-agent bullet, the emdash reference moved to the canonical emdash.com, updated bumped [glm-5.3]
- Task management category matrix: deferred per the seeding rule (three members, one shared-rows design pending); the deferral is recorded here [glm-5.3]
- agentic-coding-tools-landscape: orchestration paragraph gains the Gas Town exception sentence naming the tracker layer, updated bumped [glm-5.3]
- _index.md: new Task management category (three notes, alphabetical) listed after Spec-driven development; Gas Town added to Orchestration; orchestration matrix one-liner now eight tools [glm-5.3]
- Verification: all 78 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets, no em-dashes or banned terms (two slips caught and reworded mid-run), and every cited URL fetched 200 or Algolia-verified this run [glm-5.3]

## 2026-08-27 (owner-prompted, paperclip and the Control planes category)

- Owner request in chat: create a category for Paperclip AI if not already covered; the corpus mentioned it only inside an untracked owner draft (i-specify-open-source-projects-i-dont-maintain), so nothing existed under agents/ and the category was created [glm-5.3]
- Research index: seeded the Control planes category with the paperclip note, citing 7 sources all fetched 200 or Algolia-verified this run (repo and API, homepage, docs, releases API, the 3-point Show HN, the OpenClaw API for the comparison) [glm-5.3]
- paperclip: recorded the company-versus-employee framing ("if OpenClaw is an employee, Paperclip is the company"), the heartbeat-and-checkout execution model with 409 conflict semantics, the four pillars, the sandbox providers, 79,465 stars and 14,557 forks since 2026-03-02 with 5,417 open issues, the date-versioned v2026.824.1 release, the cloud waitlist, the near-empty HN footprint stated as the distribution signal, and the quickstart's trusted-loopback default flagged as the main caution [glm-5.3]
- Placement decision: a new Control planes category rather than Orchestration or Executions, because Paperclip orchestrates business goals (org charts, budgets, approvals, multi-company) rather than repo worktrees or single scheduled triggers; OpenClaw stays unnoted (already covered by two corpus articles) and is named inside the note instead, per the gemini-cli/Antigravity grouping precedent [glm-5.3]
- Control planes matrix: deferred per the seeding rule (one member); the deferral is recorded here [glm-5.3]
- _index.md: Control planes category listed after Task management [glm-5.3]
- Verification: all 79 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets (learnings-from-openclaw linked as a committed corpus article, openclaw-triage-pipeline deliberately unlinked because it is untracked), no em-dashes or banned terms, one sentence per line [glm-5.3]

## 2026-08-27 (owner-prompted, matrices for every category)

- Owner request in chat: task management gets its own matrix, and AGENTS.md changes so every category list carries a comparison matrix [owner, glm-5.3]
- AGENTS.md, Comparison matrices section (owner-directed edit, the first since the 2026-08-25 rules change): every research index category now has a companion matrix, created in the same run the category is seeded even for a single member (the single column is the scaffold the next member extends, gap named in prose); the seeding-deferral sentence is removed [owner, glm-5.3]
- task-management-feature-matrix: created with three columns (Backlog.md, beads, Task Master) and ten rows, thesis that storage, files versus database, decides the concurrency everything else decorates; every cell traced to the member notes; the four reference URLs fetched 200 this run; Task Master's storage cell verified against the repo tree (.taskmaster/ with tasks, config, state) and its concurrency cell honestly marked ? [glm-5.3]
- spec-driven-development-feature-matrix: created as a single-column scaffold for spec-kit, delivering the deferral recorded on 2026-08-26 now that deferrals no longer exist; nine rows, the Tessl/OpenSpec/Kiro gap named in prose, four reference URLs fetched 200 this run [glm-5.3]
- control-planes-feature-matrix: created as a single-column scaffold for paperclip, delivering the deferral recorded earlier today; ten rows centered on the governance, budgets, and multi-company rows that define the category against Orchestration; three reference URLs fetched 200 this run [glm-5.3]
- _index.md: all three matrices listed under Comparison matrices [glm-5.3]
- All thirteen research categories now have matrices: harness, surface, orchestration, protocols, context engines, skills, retrieval, memory, executions, hybrid execution, task management, spec-driven development, control planes [glm-5.3]
- Verification: all 82 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets across the section, every matrix column set matches its category membership on disk, no em-dashes or banned terms, one sentence per line [glm-5.3]

## 2026-08-27 (owner-prompted, assistant runtimes: OpenClaw and the -claw variants)

- Owner request in chat: cover the OpenClaw variants (nanoclaw, zeroclaw, picoclaw, etc.); all three named variants verified real and large (30.6k, 32.7k, 29.9k stars), plus the "etc." resolved as microclaw (732, inspired by nanoclaw), SmolClaw and FemtoClaw (sub-scale curiosities kept in prose), and the clawsec security suite that names the family [glm-5.3]
- Research index: seeded the Assistant runtimes category with four notes, each citing 5-6 sources fetched 200 or Algolia-verified this run: openclaw (the root, added as the anchor the variants are read against), nanoclaw, zeroclaw, picoclaw [glm-5.3]
- openclaw: recorded the Gateway architecture, MIT under the OpenClaw Foundation, 387,777 stars and 81,419 forks since 2025-11-24, and the 2026 provider-restriction saga (Google 802 pts, Anthropic 1,099 pts, the same-week privilege-escalation report 514 pts, commits-mentioning-OpenClaw refusals 1,349 pts) as the category's defining caution [glm-5.3]
- nanoclaw: recorded the audit-first thesis (the author's half-million-line rebuke of the root), per-agent Linux containers, OneCLI Agent Vault credential injection, skill-installed channels, Claude Agent SDK nativity with codex/opencode/ollama drop-ins, and the 533-point launch thread as "Clawdbot in 500 lines" [glm-5.3]
- zeroclaw: recorded the compile-time ownership thesis, single Rust binary, dual MIT/Apache-2.0, about 20 providers and 30+ channels including voice and hardware tools, the Android port (303 stars), and the thin HN footprint (threads at 2-8 points) stated as the missing-community-coverage signal [glm-5.3]
- picoclaw: recorded Sipeed's Go-from-scratch implementation (explicitly inspired by NanoBot, 47,454 stars, not an OpenClaw fork), the $10 RISC-V boards with 10-20MB RAM footprint, the LicheeRV-Claw hardware bundle, 20k stars in 17 days, and both README banners (no production before v1.0; no official cryptocurrency, picoclaw.io only) as the attention-outpacing-governance record [glm-5.3]
- assistant-runtimes-feature-matrix: created in the same run per the matrix rule, four columns and twelve rows with the trust-ladder thesis (ecosystem, auditable codebase, static binary, firmware image); every reference fetched this run [glm-5.3]
- paperclip: the Compared-to OpenClaw entry now links the new note instead of the bare GitHub URL [glm-5.3]
- control-planes-feature-matrix: the un-profiled-neighbors paragraph now points at the Assistant runtimes category instead of describing OpenClaw as note-less [glm-5.3]
- _index.md: Assistant runtimes category added (four notes, alphabetical) and the matrix listed under Comparison matrices [glm-5.3]
- openclaw-triage-pipeline remains untracked and unlinked, per the standing CI rule; learnings-from-openclaw is the linked corpus anchor [glm-5.3]
- Verification: all 87 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets, every matrix column set matches its category membership (14 categories, 14 matrices), no em-dashes or banned terms, one sentence per line [glm-5.3]

## 2026-08-27 (owner-prompted, spec-driven development alternatives)

- Owner request in chat: cover the other spec-driven development alternatives; the previously named-but-unprofiled neighbors (Tessl, OpenSpec, the SDD CLI ecosystem) were researched, plus a scan that surfaced BMad; an AWS context-forge repo could not be verified under that name (GitHub 404) and is not asserted anywhere [glm-5.3]
- The interrupted control-planes scan (previous owner prompt) got as far as identifying Hermes Agent (Nous Research, 52-pt launch thread) before this request redirected the run; Hermes stays an unlogged scan candidate for the control-planes build-out [glm-5.3]
- Research index: Spec-driven development extended from one to four members, each citing 5-6 sources fetched 200 or Algolia-verified this run: openspec, bmad-method, tessl [glm-5.3]
- openspec: recorded Fission AI's delta-proposal model (/opsx:propose writes proposal, specs, design, tasks; /opsx:archive folds the delta into a living ledger), the brownfield-first philosophy, 66,398 stars since 2025-08-05, 1,610,142 npm downloads last month, MIT, and the empty HN footprint stated as the thin-verification caution [glm-5.3]
- bmad-method: recorded the agile right-sizing thesis (small changes straight to build, deep planning for big ones) as the answer to the waterfall-strikes-back critique, the clarify-plan-build-learn loop, durable-context briefs, the module ecosystem (Builder, Test Architect, Loop for unattended epics, Game Dev), MIT under BMad Code LLC (API says NOASSERTION, LICENSE file fetched and confirms MIT), 52,371 stars since 2025-04-13, and the thin HN footprint (2-4 point threads) [glm-5.3]
- tessl: recorded Guy Podjarny's $125M Series A (November 2024) for the spec-centric platform, Skills on Tessl as a skills package manager (January 2026), Martin Fowler's 128-point third-party analysis naming Kiro, Spec Kit, and Tessl the three pillars, and the 71-star quiet-since-March CLI as the deliberate thin-OSS posture; pricing left explicitly unverified [glm-5.3]
- spec-driven-development-feature-matrix: rebuilt from the single-column scaffold to four columns (BMad, OpenSpec, Spec Kit, Tessl) in the same run per the matrix rule, eleven rows across the ownership (repo versus platform) and ceremony-sizing axes; all six references fetched this run [glm-5.3]
- spec-kit: the Tessl line in Compared to now links the new note instead of deferring [glm-5.3]
- _index.md: Spec-driven development lists four notes, matrix one-liner updated [glm-5.3]
- Verification: all 90 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets, every matrix column set matches its category membership (14 categories, 14 matrices), no em-dashes or banned terms, one sentence per line [glm-5.3]

## 2026-08-27 (owner-prompted, paperclip alternatives: the finished scan)

- Owner follow-up: the control-planes scan interrupted by the spec-driven request was completed this run; candidates verified via the GitHub and HN Algolia APIs were Hermes Agent (237,130 stars), TinyAGI fka TinyClaw (3,610 stars, stalled), claw-empire (1,359, stalled since March), desplega-ai/agent-swarm (723, active), multigent (61), Cabinet (knowledge-base product, different problem), and kastra (policy enforcement, a governance slice) [glm-5.3]
- hermes: added to Assistant runtimes rather than Control planes, because the repo is a personal agent runtime (single Python gateway, chat channels, any model), not a company orchestrator; recorded the learning loop (autonomous skill creation, self-improvement, FTS5 session search, Honcho user modeling, agentskills.io compatibility), seven execution backends with serverless idle, 237,130 stars and 47,995 forks since 2025-07-22, 36,374 open issues, the 52-point launch thread, the Grafana and Fleet ecosystem threads, and the edited plagiarism-claims issue 10232 as the stewardship caution [glm-5.3]
- tinyagi: added to Control planes as the category's first stall record; recorded the fka TinyClaw origin (jlia0's Claude Code wrapper, now redirecting), the multi-team chain-and-fan-out model, the SQLite queue with dead-letter management, TinyOffice, v0.0.20 of 2026-03-26 as the final release with the last push 2026-03-30, and the consolidation reading (five months of silence while Paperclip reached 79k stars) [glm-5.3]
- assistant-runtimes-feature-matrix: extended from four to five columns (Hermes inserted after the root) in the same run per the matrix rule; the reading section gains the learning-loop-versus-trust-ladder line [glm-5.3]
- control-planes-feature-matrix: extended from one to two columns (TinyAGI), the single-column scaffold language replaced with the two-column consolidation comparison, and the long tail (claw-empire, agent-swarm, multigent, Cabinet, kastra) named in prose with reasons each stays unnoted [glm-5.3]
- _index.md: Hermes listed in Assistant runtimes (five notes), TinyAGI in Control planes (two notes), the assistant runtimes matrix one-liner updated [glm-5.3]
- Verification: all 92 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets, every matrix column set matches its category membership (14 categories, 14 matrices), no em-dashes or banned terms, one sentence per line [glm-5.3]

## 2026-08-27 (owner-prompted, table filter controls on every matrix)

- Owner follow-up on why only the harness, surface, and orchestration matrices had filtering: the site-layer viewer gated its interactive controls on the wide-table tag (six or more columns), and every other matrix has five or fewer; owner approved opening it up [glm-5.3]
- Site repository (blog.tomrochette.com, outside this content repo): tables.js now enhances every .tbl-wrap table (column-picker chips, row search, value-based column filter) instead of only .tbl-wide ones; the wide class keeps its single remaining job, sticky header and label column for six-plus-column tables; verified via node --check, a Hugo rebuild whose tables.min bundle selects .tbl-wrap with zero tbl-wide references, and the existing guards (label column and last visible column cannot be hidden); committed and pushed as 62b574f7 [glm-5.3]
- methodology.md: the Matrix presentation section now states every table gets the controls, with the pinned header and label column remaining the six-plus-column extra [glm-5.3]
- Verification: methodology diff matches the shipped behavior; no other content files touched this run [glm-5.3]

## 2026-08-27 (daily refresh, harnesses re-verification + two entrants)

- Stalest category computed as Harnesses: its oldest updated dates tie Surfaces at 2026-08-23, but Surfaces received its dedicated refresh run on 2026-08-25 while Harnesses last had one on 2026-08-24; re-verified all 11 member notes against live sources [glm-5.3-flash]
- Link check: every reference URL of the eleven harness notes fetched 200 this run (15 HN threads via the Algolia items API with titles and points matching), except web.archive.org's main host, which is unreachable from this environment at connection level (000 even on root); the claude-code archive snapshot was confirmed available and status 200 through the archive.org availability API [glm-5.3-flash]
- codex: repository stats refreshed to about 119.1k stars, about 18.2k forks, and about 9.9k commits as of 2026-08-27 (GitHub API); the three doc references moved to learn.chatgpt.com because developers.openai.com/codex migrated there (target content verified on the fetched page) [glm-5.3-flash]
- claude-code: reference canonicalized from anthropic.com/claude-code to claude.com/product/claude-code after Anthropic's domain move; the about-15.2k open issues and pull requests claim re-checked at 15,173 via the search API [glm-5.3-flash]
- amp: spinout link and reference canonicalized to ampcode.com/news/amp-frontier-corporation after a redirect revealed the new slug [glm-5.3-flash]
- goose: aaif.io formation-announcement reference canonicalized to /news/linux-foundation-announces-formation-of-aaif [glm-5.3-flash]
- aider: stall re-confirmed (pushed_at still 2026-05-22); crush, gemini-cli, junie, opencode, qwen-code, cline: re-verified with no material change, left untouched per precedent (cline's marketplace page no longer server-renders install counts, so the 5.1M figure keeps its August 24 date) [glm-5.3-flash]
- New-entrant scan surfaced two credible harness additions, each written to full citation standards with all sources fetched this run: kilo-code and openhands [glm-5.3-flash]
- kilo-code: recorded the MIT feature-merge fork of Cline and Roo Code (launch-era threads March 2025), about 27k stars pushed the day of verification, the Anaconda acquisition of July 15, 2026 per the primary blog post (Kilo already in Anaconda's product nav, kilocode.ai redirects to kilo.ai), Free/Teams $15/Enterprise pricing with the three-way cost split, and the vendor popularity claim marked unproven against observable stars [glm-5.3-flash]
- openhands: recorded the renamed OpenDevin at about 85.3k stars MIT, v1.15.0 of August 21, 2026, the $18.8M Series A led by Madrona of November 18, 2025 plus the AMD local-agents collaboration, the Agent Canvas plus Agent Server architecture with local GUI and CLI V0 deprecated in the docs, ACP hosting of rival harnesses inside Canvas, and the thin post-rename community footprint stated as a signal (a 70-point 2022 HN thread named OpenHands is unrelated and was excluded) [glm-5.3-flash]
- harness-feature-matrix: extended from 11 to 13 columns in the same run per the matrix rule, all 22 new cells traced to sources fetched this run (both projects' llms.txt doc indexes: Kilo AGENTS.md support, MCP, custom subagents, cron schedules, cloud tasks, Ollama and LM Studio; OpenHands MCP, hooks, skills, plugins, automations, local-LLM pages, .openhands customization); reading and choosing sections updated for thirteen, references extended by the two doc indexes and the Anaconda post [glm-5.3-flash]
- agentic-coding-tools-landscape: independent tail gains Kilo Code and OpenHands lines, the Roo-Cline exit sentence now names the fork descendant that merged their lineages, verified-dates line extended [glm-5.3-flash]
- _index.md: both notes listed alphabetically in Harnesses, matrix one-liner updated to thirteen harnesses verified 2026-08-27, landscape one-liner re-dated [glm-5.3-flash]
- Style sweep caught three pre-existing shape compounds ("subscription-shaped work" in codex, "fork and reshape" in nanoclaw, "reshape deployment thinking" in picoclaw) which were reworded; touched files gained llm=glm-5.3-flash alongside earlier tags (none removed) [glm-5.3-flash]
- No self-directed essay this run: the category re-verification plus two entrant notes with their matrix columns filled the day at quality [glm-5.3-flash]
- Verification: 93 article files plus section control files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets across the section, every matrix column set matches its category membership (14 categories, 14 matrices), no em-dashes or banned terms in changed files, one sentence per line [glm-5.3-flash]

## 2026-08-27 (correction to the daily refresh entry above)

- harness-feature-matrix: the entry above claimed every touched file gained llm=glm-5.3-flash; the matrix itself was missed at first, caught on self-check and added in commit c21a253b [glm-5.3-flash]

## 2026-08-29 (owner-prompted, software factory category)

- Owner request in chat: introduce a Software factory category and decide whether disler/super-simple-software-factory (SSSF) fits there; research confirmed it is the canonical instantiation of the concept and placed it as the founding member [big-pickle]
- Placement decision: a new Software factory category rather than Hybrid execution, Skills, or Spec-driven development, because SSSF's center is a repeatable code-owned SDLC pipeline packaged as a skill, not structured-output orchestration, a skill format, or a spec artifact; it joins the corpus's software-factory tag and its Code Factories essays (../../code-factories-factorio etc.), which it cross-links [big-pickle]
- super-simple-software-factory: research note created per the skeleton, citing 5 sources fetched or verified this run; recorded 764 stars and 189 forks since creation 2026-08-02 with last push 2026-08-04, single commit on main, no releases, the example branch with a stamped demo app, MIT, the code-owns-the-loop thesis over bounded agent phases, typed JSON envelopes and gates, same-session correction, WAL SQLite trace, the pi-only coding agent (claude_code stubbed, README pi link 404), the no-sandbox/no-merge/no-approval gap, and the placeholder test gates [big-pickle]
- software-factory-feature-matrix: created as a single-column scaffold for sssf in the same run per the matrix rule, ten rows centered on the loop-owner, agent-boundary, and sandbox rows, the gaps named in prose; three references verified this run [big-pickle]
- _index.md: Software factory category added to the research index and the matrix listed under Comparison matrices [big-pickle]
- Verification: all section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets (both code-factories corpus anchors and the spec-driven/hybrid-execution/executions links confirmed on disk), every matrix column set matches its category membership (15 categories, 15 matrices), no em-dashes or banned terms, one sentence per line [big-pickle]

## 2026-08-29 (owner-prompted, software factory alternatives)

- Owner follow-up: find other software-factory-style projects and assess credibility; a web search plus GitHub API scan surfaced and triaged the long tail, then two credible members cleared the bar and were written to full citation standards with all sources fetched or verified this run [big-pickle]
- Scorecard of scanned candidates: fluent and har admitted; smartcomputer-ai/lightspeed (91 stars, deterministic Temporal harness, general orchestration rather than a factory) kept out with the reasons in the matrix long-tail; determinagent (10 stars, library), agentic-software-factory (1 star, inflated agent counts), ai-factory (4 stars, NOASSERTION license), and Takk8IS/software-factory (0 stars, NOASSERTION) did not clear the citation or credibility bar [big-pickle]
- fluent: research note added as the category's self-improving member; recorded 84 stars and 1 fork since creation 2026-07-10, 1,450 commits, v0.2.0 of 2026-08-15, Apache-2.0 Rust binary plus skill for Codex/Claude Code/Pi (macOS only), the Observations-to-Merge-Candidate loop with EARS Behavior Specs, isolated worktrees with AWS Fargate remote execution, the deterministic final Tester bound to the reviewed commit, and the Learner writing reusable Expertise as the self-improvement lead [big-pickle]
- har: research note added as the harness-style member; recorded 82 stars and 10 forks since creation 2026-06-28, 351 commits, v1.0.0 of 2026-08-28 with daily releases, Apache-2.0 TypeScript CLI plus MCP server (npm @osfactory/har), the .har contract replacing scattered run knowledge, per-agent worktree/port/database slots, deterministic verify with a per-commit evidence trail, Mission Control dashboard, and Kerno sponsorship [big-pickle]
- software-factory-feature-matrix: rebuilt from the single-column scaffold to three columns (SSSF, Fluent, HAR) in the same run per the matrix rule, with the who-owns-the-loop thesis, the isolation row separating factories from single-agent calls, Fluent's self-improvement lead, SSSF's pi-only dependency as the reason to look past headline ease, and the rejected long tail named in prose so no future run re-adds it silently [big-pickle]
- super-simple-software-factory: Compared-to rewritten to name the new peers (Fluent's ceremony, HAR's fleet harness) alongside the cross-category comparisons [big-pickle]
- _index.md: Fluent and HAR listed alphabetically in Software factory, matrix one-liner updated to the three-way who-owns-the-loop framing [big-pickle]
- Verification: all section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets (all four code-factories corpus anchors and the intra-category links confirmed on disk), every matrix column set matches its category membership (15 categories, 15 matrices), no em-dashes or banned terms, one sentence per line [big-pickle]

## 2026-08-29 (owner-prompted, people and publications category)

- Owner request in chat: introduce a category that collects the websites and people shaping the domain as it evolves; selected the people-plus-outputs scope and a full seed plus companion matrix confirmed via two clarifying questions [big-pickle]
- Placement decision: a new People and publications category, because the five members are cross-cutting carriers of signal who do not fit any tool category; the category spans hands-on practice, industry synthesis, and conceptual vocabulary rather than a single tool type [big-pickle]
- simon-willison: research note created, the daily hands-on chronicler, citing six sources verified this run (blog, TIL, LLM CLI, predictions post, agentic-engineering guide, and a critical press take on vibe coding) [big-pickle]
- latent-space: research note created, the AI engineering newsletter-podcast-conference of record by swyx and Alessio, recorded 198,000+ subscribers and the multi-event AI Engineer series, sources verified this run [big-pickle]
- the-pragmatic-engineer: research note created, Gergely Orosz's org-and-data view, noting the paywalled core and the annual AI tooling surveys, sources verified this run [big-pickle]
- steve-yegge: research note created, the operative who builds what he predicts (Gas Town, brute squad), linked to the existing gastown and beads notes, sources verified this run [big-pickle]
- andrej-karpathy: research note created, the vocabulary-setter (vibe coding, Software 3.0, agentic engineering), now at Anthropic pre-training, sources verified this run [big-pickle]
- people-and-publications-feature-matrix: created with five columns in the same run per the matrix rule, segmented on the focus axis (hands-on, industry, vocabulary) with the missing enterprise-hands-on cell named as the scaffold for a future member, references verified this run [big-pickle]
- _index.md: People and publications category added to the research index (five notes listed alphabetically) and the matrix listed under Comparison matrices [big-pickle]
- queue.md: new category appended to the standing seed-categories list and marked done with the date and matrix slug [big-pickle]
- Verification: all section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets (intra-category, gastown, beads, landscape, and corpus anchors all confirmed on disk), the new matrix's column set matches its category membership (16 categories, 16 matrices), no em-dashes or banned terms, one sentence per line [big-pickle]

## 2026-08-29 (daily refresh, deep re-verification + fx entrant)

- Scan: all 96 article files as they stand after this run pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets, every matrix column set matches its category membership, no em-dashes or banned terms, one sentence per line [glm-5.3-flash]
- Deep refresh of the stalest cluster (updated 2026-08-23): crush, jetbrains, junie, opencode, vscode-copilot, windsurf, zed re-verified against live sources; every cited URL fetched 200 this run (9 HN threads via the Algolia items API, titles and points matching), plus GitHub API checks for the five repo-citing notes [glm-5.3-flash]
- crush, jetbrains, junie, opencode, windsurf, zed: re-verified with no material change (stars within stated bounds, junie pricing re-confirmed at $8.33/$25 with 10/35 credits, zed pricing page re-confirms all tiers and the planned-not-shipped SSO/SAML/SCIM line); left untouched per the no-change precedent [glm-5.3-flash]
- vscode-copilot: the April 22, 2026 self-serve pause is now documented as covering Copilot Business and Copilot Enterprise with sign-ups reopening soon for card and PayPal payers; contraction sentence rewritten, stars re-dated to about 190k as of 2026-08-29, reference dates bumped, updated field set, llm=glm-5.3-flash added [glm-5.3-flash]
- New-entrant scan (12-day HN window plus GitHub checks) surfaced one credible harness: fx (vercel-labs/fx) [glm-5.3-flash]
- fx: research note added to Harnesses, citing 9 sources all fetched this run (repo plus GitHub API, the site, four docs pages, the 317-point launch thread via Algolia, vercel.com/oss); recorded the embed-first thesis (about 6.19 MiB Zig binary, 10 microsecond cold start, Wasm build), the three-credential model (Vercel AI Gateway, Codex OAuth, Grok OAuth) with locally stored tokens, native AGENTS.md, Claude-family skill directories, persistent-child subagents, the fx acp server, and the every-request-routes-through-AI-Gateway caution; 2,589 stars, v0.0.7 of 2026-08-29 [glm-5.3-flash]
- harness-feature-matrix: extended from 13 to 14 columns in the same run per the matrix rule, all 11 fx cells traced to the docs pages fetched this run; reading section gains the embed-first line, choosing gains the embedded-agent bullet, references extended by 3, verified-date line names the fx column's own date [glm-5.3-flash]
- agentic-coding-tools-landscape: harness tail gains the fx line, verified-dates line extended, updated bumped to 2026-08-29 [glm-5.3-flash]
- Attribution note: the vscode-copilot, landscape, harness-matrix, and _index.md changes above were left uncommitted in the working tree while this run proceeded, and the concurrent big-pickle software-factory run committed them in ba32d985 alongside its own work; this entry records the authorship [glm-5.3-flash]
- The standing `? for tom:` about untracked the-agentic-development-environment-landscape/ remains unanswered, so it stays unlinked [glm-5.3-flash]
- No self-directed essay this run: the deep re-verification plus the fx note with its matrix column filled the day at quality [glm-5.3-flash]

## 2026-08-29 (correction to the daily refresh entry above)

- The attribution note above was wrong: only the _index.md changes went in with ba32d985; the vscode-copilot, agentic-coding-tools-landscape, and harness-feature-matrix changes were still uncommitted and landed now in their own commit [glm-5.3-flash]

## 2026-08-29 (people and publications category expansion)

- Owner request in chat and the standing category directive both call for building out the People and publications category; the five-member seed left the enterprise-hands-on cell and the model, evaluation, systems, and education bands open, and these six members fill them [big-pickle]
- hamel-husain: research note added as the evaluation-and-verification band, the data-driven method for deciding whether an AI product works, citing the Field Guide, the evals post, the Maven course (4,500+ students from 500+ companies), and a critical Arize take on why evals fail, sources verified this run [big-pickle]
- lilian-weng: research note added as the durable research-reference band, whose LLM Powered Autonomous Agents post is the canonical survey of planning, memory, and tool use, sources verified this run [big-pickle]
- chip-huyen: research note added as the systems-survey band, the most-read O'Reilly AI book of 2025, sources verified this run [big-pickle]
- nathan-lambert: research note added as the model-and-post-training band, the open-ecosystem voice from inside the labs, recording the Get Good at Agents and Claude Code pieces and the RLHF Book, sources verified this run [big-pickle]
- deeplearning-ai-andrew-ng: research note added as the education-and-on-ramp band, the voice that popularized the four agentic design patterns and published the AI Engineering Skills Map, sources verified this run [big-pickle]
- ai-jason: research note added as the video-practitioner band, the channel that shows agent workflows and context engineering working end to end, recording 230K subscribers and 99 videos, sources verified this run [big-pickle]
- people-and-publications-feature-matrix: extended from five to eleven columns in the same run per the matrix rule, with the thesis re-segmented onto five focus bands (hands-on, evaluation, model-and-research, industry, systems-and-education), the been-empty enterprise-hands-on cell re-named as the remaining scaffold, and all eleven reader-slot rows filled from the member notes [big-pickle]
- _index.md: the six new notes listed alphabetically in People and publications, and the matrix one-liner bumped from five to eleven voices [big-pickle]
- queue.md: left untouched; the People and publications category item is already marked done, and expanding a done category is self-directed growth, so no new queue line applies (matching how the fluent and har additions did not touch the queue) [big-pickle]
- Verification: all section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets (all intra-category links and corpus anchors confirmed on disk), the matrix column set matches its category membership (11 members, 11 columns), no em-dashes or banned terms, one sentence per line [big-pickle]

## 2026-08-29 (caleb writes code added to people and publications)

- Owner request in chat names the channel directly (youtube.com/@calebwritescode); added as the twelfth member of People and publications, filling the same-week video release-explainer slot next to AI Jason's workflow-builder one [big-pickle]
- caleb-writes-code: research note added for the YouTube explainer channel of Caleb Eom; identity, description ("part editorial, part informational on AI"), join date 2025-03-16, and LinkedIn/X/Patreon links fetched from the channel about page, scale fetched from a live counter (105,664 subscribers, about 6.3M views, 114 videos, as of 2026-08-29), cadence and topics fetched from the channel RSS (uploads about twice a week, latest 2026-08-27) [big-pickle]
- caleb-writes-code critical grounding: 11 of the last 15 upload descriptions carry a sponsor or affiliate read (computed from the RSS descriptions this run), no Hacker News threads and no substantive Reddit discussions were found, and one third-party analytics site's stale inactivity prose contradicts its own FAQ and the live feed, all recorded as cautions [big-pickle]
- people-and-publications-feature-matrix: extended from eleven to twelve columns in the same run per the matrix rule, Caleb Writes Code column placed after AI Jason in the hands-on cluster, hands-on reading line rewritten to name the two distinct video modes, choosing list gains the release-explainer bullet [big-pickle]
- _index.md: Caleb Writes Code listed alphabetically between Andrew Ng and Chip Huyen, matrix one-liner bumped from eleven to twelve voices [big-pickle]
- Verification: front matter parses with no type field and mandatory tags, all internal links resolve on disk, matrix columns match category membership (12 members, 12 columns), no em-dashes or banned terms, one sentence per line [big-pickle]

## 2026-08-30 (jcode added to harnesses)

- Owner request in chat: cover jcode (github.com/1jehuang/jcode); placed in Harnesses, verified this run via repo page, GitHub API, jcode.sh (home, docs, about, pricing), the grigio.org independent comparison, and two HN threads via the Algolia items API [glm-5.3-flash]
- jcode: research note created; recorded the resource-efficiency thesis (27.8 MB PSS with embedding off, ~10 MB per added session, 14 ms to first frame, all self-published), the embedding memory graph, native swarm, self-dev mode, confidence stepping and auto-poke, 671-token system prompt, session portability, 30-plus providers with subscription OAuth and multi-account switching, stdio-only MCP, $10/month hosted inference, YC S26 solo founder, 18,796 stars and 2,144 forks and v0.81.1 of 2026-08-26 as of verification, and the thin independent footprint (two HN threads at 3 and 5 points, zero comments) as a stated signal [glm-5.3-flash]
- harness-feature-matrix: extended from fourteen to fifteen columns in the same run per the matrix rule, jcode placed between goose and Junie, all eleven cells traced to the note's sources; verified-date line names the jcode column's own date; open-client and local-model group lists updated; choosing list gains the parallel-agents bullet; references extended by 2 [glm-5.3-flash]
- agentic-coding-tools-landscape: harness tail gains the jcode line, verified-dates sentence extended, updated bumped to 2026-08-30 [glm-5.3-flash]
- _index.md: jcode listed alphabetically in Harnesses, matrix one-liner bumped to fifteen harnesses verified 2026-08-30 [glm-5.3-flash]
- Verification: all 112 section files pass front matter parsing with no type field and mandatory tags, 0 broken internal link targets in the touched files, matrix columns match category membership (15 members, 15 columns, 15 cells per row), no em-dashes or banned terms, one sentence per line [glm-5.3-flash]
