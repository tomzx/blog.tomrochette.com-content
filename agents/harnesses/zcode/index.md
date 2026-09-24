---
title: ZCode
created: 2026-09-21
updated: 2026-09-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, zai, desktop, open-source, security]
readability: 3
audience_notes: >
  Engineers considering Z.ai's official harness for GLM models, and anyone studying how a
  telemetry scandal and a forced open-sourcing interact. Assumes you know what a harness,
  a wire-level analysis, and a subscription plan mean.
---

ZCode is Z.ai's (Zhipu AI's) official AI coding workbench for GLM models: an Electron desktop app, a browser workspace, and a terminal CLI, open-sourced under Apache-2.0 on September 20, 2026, three days after a wire-level analysis caught it silently uploading whole workspaces to cloud storage.
Facts below verified as of 2026-09-22.

**ZCode is the fastest fall and forced opening in the harness field: launched July 1, caught exfiltrating Git history on September 18, and dumped as a flattened two-commit open-source repository on September 20 with 4,216 stars within a day.**

## What it is

A workbench rather than a pure terminal tool: desktop, web, and the `zcode` CLI share one TypeScript monorepo (6,973 files, about 1.03M lines in the open-source drop).
The pitch is multi-agent development on GLM-5.3 with Goals for long-running tasks, skills, bot control from WeChat, Feishu, and Telegram, and GLM-5.3-Flash built in for multimodal input.
It is tuned for and sold through the GLM Coding Plan, which also covers 20+ third-party agent tools.
The repository publishes Apache-2.0 source, but as a two-commit dump with flattened history, locked PRs, and disabled issues, so it is open code with a closed process.

## Status

**Active, controversial, and newly open.**
The harness launched July 1, 2026 as the official harness for GLM-5.2 and drew a 511-point Hacker News thread the same day ([HN](https://hn.algolia.com/api/v1/items/48753715)).
On September 18, 2026 a [wire-level analysis](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) showed the logged-in client packaging entire workspaces (about 87% .git content) and uploading them encrypted to Aliyun OSS with a server-held key, a behavior no UI toggle stopped and no privacy-policy line disclosed (333- and 261-point threads that day).
Z.ai admitted the uploads, attributed them to a Repo Wiki indexing feature, shipped client 3.14.0 with the pipeline removed, and open-sourced the workbench on September 20-21 with CAICT and NSFOCUS audits reporting the OSS bucket deleted ([HN](https://hn.algolia.com/api/v1/items/49782440)).
The repository shows 6,400 stars and 1,880 forks as of 2026-09-22, pushed 2026-09-21 (GitHub API); desktop installers are at v3.14.3.
Independent code review of the dump confirms the snapshot pipeline is gone and checkpoints run on purely local git, but deleting the bucket cannot answer what happened to data that left machines before September 18.

## Strengths

- First-party GLM tuning with multimodal Flash built in, at Coding Plan prices well under the Anthropic subscription.
- The surface is broad: desktop, web, CLI, chat-app bot steering, and Goals for long-running work.
- The open-source drop let independent reviewers verify the fix line by line, which is more than most incident responses offer.
- An ecosystem formed fast (community ACP servers, provider bridges for pi, and plugin kits on npm).

## Cautions

- **The trust incident is structural, not a bug**: a resident upload sidecar, server-held encryption keys, toggles that did nothing, and a privacy policy that never mentioned workspace snapshots.
- The flattened history and locked PRs make the open-source dump a legal exhibit as much as a project, so treat governance claims with suspicion until contributions actually flow.
- GLM-centric: BYOK and local models are undocumented as of 2026-09-21.
- The vendor's audit framing proves the bucket is empty now, not that earlier uploads were never retained or used.

## Pricing

The harness is free; usage goes through a GLM Coding Plan subscription: Lite $12.6/month with 10,000 weekly credits (listed against $18), Pro $56/month at 6x Lite usage (against $80), and Max $117.6/month at 14x (against $168), per the ZCode site as of 2026-09-22.
The plans also cover 20+ third-party agent tools, so the subscription is not ZCode-locked.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-21 | GLM Coding Plan | Baseline at note creation: Lite $12.6/mo (10,000 credits/week), Pro $56/mo (6x), Max $117.6/mo (14x), listed against $18/$80/$168. | [zcode.z.ai](https://zcode.z.ai/) |

## Compared to

- [Grok Build](../grok-build/index.md): the same wire-level-analysis story with the opposite sequel, a living repository with daily releases versus a one-way dump.
- [DeepSeek Harness](../deepseek-harness/index.md): the other Chinese-lab open-source harness; dsh was built in public as a plugin kernel, ZCode is a finished product published after an incident.
- [Claude Code](../claude-code/index.md): the subscription platform ZCode undercuts on price, and one of the tools the GLM Coding Plan also covers.

## Bottom line

Recommended only for engineers already sold on GLM models who want a desktop workbench and accept a vendor three days out from a data-exfiltration scandal.
Not for high-value proprietary code until an independent party verifies the current client's network behavior over time.
I would watch whether the open repository becomes a real project or stays a press release.

## Changes

- 2026-09-21 - Created after three sub-runs flagged the entrant, recording the July launch, the September 18 telemetry disclosure, and the September 20-21 open-source dump.
- 2026-09-22 - Recorded the star count rising from 4,216 to 6,400 and forks from 1,127 to 1,880 in the day after the dump, and desktop installers moving to v3.14.3.

## See also

- [Grok Build](../grok-build/index.md) - the parallel open-source-after-scrutiny arc at xAI
- [DeepSeek Harness](../deepseek-harness/index.md) - the other lab-published harness in this section
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the new column's shared rows
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this note joins

## References

- https://github.com/zai-org/ZCode - repository, license, 6,400 stars as of 2026-09-22 (GitHub API)
- https://raw.githubusercontent.com/zai-org/ZCode/main/README.en.md - surfaces and monorepo layout
- https://zcode.z.ai/ - product claims, GLM Coding Plan prices, v3.14.3 installers
- https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/ - the wire-level analysis, Z.ai's response, and the open-source code verification
- https://hn.algolia.com/api/v1/items/48753715 - the July 1, 2026 launch thread, 511 points
- https://hn.algolia.com/api/v1/items/49750694 - the 333-point disclosure thread, September 18
- https://hn.algolia.com/api/v1/items/49752422 - the 261-point disclosure thread, September 18
- https://hn.algolia.com/api/v1/items/49782440 - the open-sourcing thread, September 21
