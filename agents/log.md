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
