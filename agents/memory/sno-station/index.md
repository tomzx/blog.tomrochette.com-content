---
title: Sno Station
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, cross-harness, encryption, open-source]
readability: 3
audience_notes: >
  Engineers running two or more coding or personal agents who want one shared memory
  across them, with handoff when a quota runs out, profiled against the other cross-harness
  stores and the single-harness capture plugins.
  Assumes you know what an agent harness and a local MCP-free CLI are.
---

Sno Station is Sno AI's Apache-2.0 local workstation that gives Codex, Claude Code, Hermes Agent, Cursor, and OpenClaw one encrypted shared memory, and adds quota-exhaustion handoffs, cross-agent peer review, and a nightly REM pass that strengthens what matters and retires what was replaced.

**Its bet is that the memory layer is what makes several agents one squad: handoffs, reviews, and overnight learning all read and write the same encrypted store, and deliberate forgetting is a feature rather than a bug.**

## What it is

A local install (one shell command, then `sno setup` connects every agent it finds) with no daemon and no account required, from Sno AI Corporation in California.
Each harness gets an adapter that reads and writes the one store; agents talk through the `sno reach` mailbox, and a handoff writes a note (done, half-done, exact commit) that the next agent picks up with context intact.
The nightly REM pass runs at most once a day per memory part (usually overnight, or earlier once about 100 new memories pile up), and Self Learning reads the day's sessions and proposes skill changes that nothing applies until you accept.
The store is SQLite encrypted at rest in SQLCipher v4-compatible mode, with a 256-bit key generated once into a local `settings.json` (mode 0600) that Sno never receives.
Retrieval is local first, then a pinned local model (`Horizon-Labs/multilingual-reranker-small`) reranks at most 32 candidates, with no prompt or memory text sent to Sno in any mode.
Three data modes surround that core: Local First uploads no memory text, Agent Native (the default) runs memory work on your own agent's model but uploads the day's sessions to Sno each night for Self Learning unless you turn it off, and REM Enhanced sends memory text to your own space in Sno's cloud for processing.

## Status

**Young, fast-rising, and entirely self-evidenced.**
929 stars and 364 forks on a repository created 2026-09-19 (public since 2026-09-18) and pushed 2026-10-24, Apache-2.0, as of 2026-10-28 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=sno-ai/sno-station&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=sno-ai/sno-station&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=sno-ai/sno-station&type=date&legend=top-left" />
</picture>

Latest release v1.6.0 (2026-10-23) keeps reranking local in every memory mode and makes search return existing results when the local model is still loading.
The what-runs-today table marks the five-harness shared memory, the mailbox, and Self Learning as released and proven end to end on clean machines.
The published evidence is the project's own: dated screenshots in `docs/evidence` show a quota watch handing a long build to another agent at 2 percent remaining, Self Learning catching a repeated mistake and putting a rule into the live skills by morning, and a next-day check measuring whether its own skill changes helped, with an `evals/` directory (LoCoMo, Memora, r-at-5, and its own bench) behind the memory claims.
I found no Hacker News thread and no independent writeup through 2026-10-28 searches, so 929 stars in five weeks rest on trending placements and promotional posts, the category's stars-ahead-of-discussion pattern at its youngest.

## Strengths

- **The consolidation-and-forgetting pass is built in**: REM strengthens and retires memories on a schedule, which is the row every other member of this category leaves to your application code.
- Quota handoff with context intact is a concrete answer to a problem every multi-agent user hits, and the recorded handover-note format (done, half-done, exact commit) is inspectable.
- **Encryption is real by default and precisely documented**: SQLCipher v4-compatible pages, a local-only key, a 0600 key file, and a security doc that names what the design does not protect (compromised machines, swap, malware, data you send to providers).
- Learning is gated: Self Learning proposes, you accept, and the project publishes its own self-repair evidence with dates.

## Cautions

- **Every published result is the project's own run of its own product**: the evidence pages are screenshots, the evals are self-run, and no independent coverage of any kind existed as of 2026-10-28.
- The default Agent Native mode uploads the day's sessions to Sno each night for Self Learning, so the "local" workstation has a default outbound path you must turn off in `~/.sno/settings.json`.
- The free tier is a weekly allowance (memory for about 150 messages, Self Learning from about 20 sessions), and an unlinked computer gets one tenth of it, a funnel toward the sno.ai account.
- Five-harness adapters on harnesses that move weekly is a maintenance bet, and the vendor's own framing ("not another AI memory tool") means scope may keep pulling toward a full workstation.

## Pricing

Freemium: the local product is free and Apache-2.0 and complete without the cloud.
The sno.ai cloud plans bill a weekly allowance as of 2026-10-28: Free $0 per month (1x memory, about 150 messages, and 1x Self Learning, about 20 sessions), Plus $19 per month (3x memory, about 450 messages, and 5x Self Learning, about 100 sessions), and Max $199 per month (45x memory, about 6,750 messages, and 65x Self Learning, about 1,300 sessions).
The allowance resets weekly; when it runs out a balance keeps Sno going, and with no balance your own agent's model takes over.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-28 | Free, Plus, Max | Baseline: Free $0/mo (weekly allowance: memory about 150 messages, Self Learning about 20 sessions), Plus $19/mo (3x/5x), Max $199/mo (45x/65x); local product free (Apache-2.0). | [sno.ai/en/pricing](https://www.sno.ai/en/pricing) |

## Compared to

- [PLUR](../plur/index.md): the other cross-harness shared store; PLUR is plain-text YAML engrams every harness reads directly, Sno Station is an encrypted store with a mailbox, handoffs, and a consolidation pass attached.
- [agentmemory](../agentmemory/index.md): the cross-agent observation server; agentmemory captures and compresses what happens going forward, Sno Station shares one store and adds the overnight strengthen-and-retire pass.
- [claude-mem](../claude-mem/index.md): the capture-and-compress leader bound to per-harness plugins; Sno Station is one store across five harnesses with no compression bill, but no independent record behind it.

## Bottom line

**Recommended for engineers running two or more of the five supported harnesses who want one encrypted memory with handoff and review, and who will treat every published number as the vendor's own until independent coverage exists.**
Not for privacy-strict environments that cannot accept the default nightly session upload, teams needing multi-user memory, or anyone whose harness set falls outside the five adapters.

## Changes

- 2026-10-28 - Created from the 2026-10-28 Awesome-Agent-Memory entrant scan (Sno Station added to the list's Open-Source products section on 2026-10-27), with eight fetched sources and the self-run-evidence-plus-missing-footprint combination recorded as the critical angle.

## See also

- [PLUR](../plur/index.md) - the other cross-harness shared store, plain YAML where this is encrypted and consolidated
- [agentmemory](../agentmemory/index.md) - the capture-based cross-agent server at the same one-store-for-all ambition
- [claude-mem](../claude-mem/index.md) - the single-harness capture-and-compress alternative
- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/sno-ai/sno-station - repository, Apache-2.0, 929 stars, 364 forks, created 2026-09-19, pushed 2026-10-24, as of 2026-10-28 (GitHub API)
- https://raw.githubusercontent.com/sno-ai/sno-station/main/README.md - the squad model, the REM data-flow modes, the what-runs-today table, the forgetting design, and the self-run evidence pages
- https://raw.githubusercontent.com/sno-ai/sno-station/main/docs/security.md - the encryption design (SQLCipher v4-compatible, local DEK, 0600 key file) and the stated limits
- https://www.sno.ai - the product site: positioning, the three modes, company (Sno AI Corporation, California)
- https://www.sno.ai/en/pricing - the Free, Plus, and Max plans and the weekly allowance mechanics, as of 2026-10-28
- https://github.com/sno-ai/sno-station/releases/tag/v1.6.0 - the v1.6.0 notes: local reranking in every mode and the model-loading fallback (2026-10-23)
- https://github.com/sno-ai/sno-station/tree/main/evals - the evals directory (LoCoMo, Memora, r-at-5, sno-memory-bench, rerank runs), all self-run
- https://hn.algolia.com/api/v1/search?query=%22sno%20station%22&tags=story - the footprint scan finding no thread (2026-10-28), the missing-coverage record
