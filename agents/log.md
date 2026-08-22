---
title: Agents log
created: 2026-08-22
status: in progress
tags: [agents]
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
