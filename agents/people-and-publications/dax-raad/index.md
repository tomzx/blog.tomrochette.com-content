---
title: Dax Raad
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, coding-agents, opencode, practitioner]
readability: 3
audience_notes: >
  Engineers evaluating OpenCode seriously and researchers checking a specific claim about Dax Raad.
  Assumes you know what OpenCode, SST, and a Show HN are.
---

Dax Raad (GitHub and X handle thdxr) is the builder behind SST and the open-source coding agent OpenCode at Anomaly, whose public record lives in repositories, Hacker News threads, and X posts rather than in any publication he owns.

**He is the harness author as terse public practitioner: one of the most instructive voices on what shipping and defending a top coding agent actually costs, and the hardest to follow because almost none of it is published in durable form.**

## What it is

A serial infrastructure builder's trail: SST (about 26.3k stars as of 2026-09-24), OpenAuth, OpenNext, and OpenCode, the MIT coding agent he launched with a Show HN in May 2025 and which now shows about 210k stars under Anomaly as of 2026-09-24.
The section's OpenCode note documents the tool's measured token leanness and its 2026 CVE and Anthropic-OAuth history.
His GitHub bio currently reads "building SST and @withbumi", pointing at Bumi, a healthcare software product.
There is no blog to subscribe to: his personal site thdxr.com has been dormant since October 2021 and its bio is stale.

## Status

Active as a maintainer, defender, and occasional poster, with a scattered publication footprint.
He answered a detailed July 2026 security takedown of OpenCode (wren.wtf's "Stop Using OpenCode") point by point in the Hacker News thread himself, citing v2 beta fixes, pruning disabled by default, and a cache-friendly system-prompt design.
He still submits stories to Hacker News (Rebase, July 2026) and surfaces in third-party accounts: commenters call him "creator of opencode" and "behind OC", and he has given podcast interviews (Pragmatic Engineer and Pragmatic Programmer, per commenters) plus YouTube interviews on OpenCode's architecture and business model.
He had 5.2k GitHub followers as of 2026-09-24.

## Strengths

- Ships infrastructure that wins at scale, from SST to one of this cycle's most-starred developer tools.
- Engages critics directly and technically in public, naming versions, defaults, and internal data rather than PR language.
- A cross-layer track record (serverless, auth, Next.js adapters, agents) means his agent opinions come from running the whole stack.
- The interview record carries his philosophy in durable long form for those who want it.

## Cautions

- **The Exo Labs founder claim attached to this note's commissioning brief could not be verified in any fetched source: exoharness.ai and exolabs.net name no founders, the exoharness/exo contributor list does not include him, and fetched Hacker News commentary instead associates Exo Labs with Alex Cheema, so do not cite this note for that claim.**
- His own reply to the OpenCode security takedown opened with "not too much actionable here", a confidence readers should discount given the CVE and OAuth removal history the corpus records.
- Following him is expensive: the thinking is scattered across X posts, thread replies, and podcasts, with no archive he controls.
- He is the vendor, so his assessments of OpenCode's tradeoffs are not neutral.

## Compared to

- [Mario Zechner](../mario-zechner/index.md): the mirror-image harness author; Zechner essays his design decisions at length, Raad answers in threads, so read Zechner for the philosophy and Raad for the defense under fire.
- [Simon Willison](../simon-willison/index.md): Willison archives everything on purpose, Raad publishes almost nothing on purpose; Willison when you need citations, Raad when you want the vendor's own words.
- [Armin Ronacher](../armin-ronacher/index.md): both are builder-critics, but Ronacher publishes monthly essays while Raad reacts in comment threads.

## Bottom line

**Recommended for engineers evaluating OpenCode seriously and for anyone studying how harness authors handle public security criticism.**
Not for readers who need a citable feed or essays, and not as a source on Exo Labs.

## Top 5 recommended reading

- [Show HN: OpenCode - TUI based coding agent](https://news.ycombinator.com/item?id=43988566) - His own launch announcement, the origin document of OpenCode with his answers on design choices in the thread.
- [Annoying and alarming things about OpenCode](https://news.ycombinator.com/item?id=48978112) - The thread where he answered the sharpest security critique of his tool point by point, naming versions, defaults, and internal data.
- [Building OpenCode with Dax Raad](https://www.youtube.com/watch?v=1VqKUrxR2C8) - The Pragmatic Engineer video interview, his most-watched long-form account of the terminal architecture and business model.
- [Building the Future of coding, OpenCode with Dax Raad](https://www.youtube.com/watch?v=IGsbARhERqc) - The NeetCode interview covering the Claude Code drama, agent design, and where he thinks programming is heading.
- [OpenCode](https://github.com/sst/opencode) - The tool itself, whose repository README is the canonical statement of what he built and why.

## Changes

- 2026-09-24 - Created, with the commissioned Exo Labs founder premise marked unverified against fetched sources.
- 2026-09-24 - Added the Top 5 recommended reading section.

## See also

- [OpenCode](../../harnesses/opencode/index.md) - the tool he created, with its measured and security record
- [Exo](../../harnesses/exo/index.md) - the harness his commissioning brief connected him to, documented there without founder claims
- [Mario Zechner](../mario-zechner/index.md) - the essaying counterpart among harness authors
- [Simon Willison](../simon-willison/index.md) - the archival counter-model to his scattered record
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where OpenCode sits among the harnesses

## References

- https://github.com/thdxr - profile: bio, 5.2k followers, pinned SST, OpenCode, OpenAuth, and OpenNext repositories
- https://thdxr.com/ - his personal site, dormant since October 2021, grounding the no-blog caution
- https://hn.algolia.com/api/v1/search?query=%22dax+raad%22&hitsPerPage=20 - third-party record: OpenCode creator, podcast and YouTube interviews, quoted posts
- https://hn.algolia.com/api/v1/search?tags=author_thdxr&hitsPerPage=15 - his Show HN launch of OpenCode and his own replies to critics
- https://wren.wtf/shower-thoughts/stop-using-opencode/ - the critical security takedown of OpenCode
- https://hn.algolia.com/api/v1/search?query=%22exo+labs%22&hitsPerPage=20 - fetched third-party attributions of Exo Labs to Alex Cheema
- https://github.com/exoharness/exo - the exoharness repository, whose contributor list does not include him
- https://withbumi.com - Bumi, the healthcare product his bio points to
