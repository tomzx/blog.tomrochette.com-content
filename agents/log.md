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
