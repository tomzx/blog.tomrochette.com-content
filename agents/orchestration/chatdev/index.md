---
title: ChatDev
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python, openbmb]
readability: 3
audience_notes: >
  Engineers weighing the large multi-agent frameworks and wondering what ChatDev's 34k stars buy today.
  Assumes you know what a multi-agent framework is and have met AutoGen or CrewAI.
---

ChatDev is OpenBMB's Apache-2.0 multi-agent platform, reborn on 2026-01-07 as ChatDev 2.0 (DevAll), a zero-code YAML workflow engine for building and running multi-agent systems, after the 2023 virtual-software-company original that made its name.

## What it is

The 1.0 lineage is the ACL 2024 paper from Tsinghua's THUNLP and ModelBest: CEO, CTO, and Programmer agents role-play a software company through chat chains, and the project became one of the most-starred artifacts of the 2023 wave.
ChatDev 2.0 keeps that history as one demo workflow and pivots the repository to a platform: a FastAPI backend and Vue 3 web console where agents, Python, tooling, and human nodes are wired into YAML workflow graphs, with memory and thinking modules, MCP tool integration, a drag-and-drop canvas, and a Python SDK on PyPI (`chatdev` 0.1.0).
It needs Python 3.12+, Node 18+, and your own model keys, runs from `make dev` or Docker Compose, and OpenClaw can create and invoke ChatDev workflows as skills.

## Status

Active on the new platform: 34,603 stars on a repository created 2023-08-28, main pushed 2026-10-16, with the classic product maintained on a `chatdev1.0` branch since the 2.0 release (GitHub API, as of 2026-10-28).
Releases are tag-only, v2.2.0 the newest tag with no GitHub release objects.
**The star-to-scrutiny gap is the caution: a 24-point Show HN in 2023 and a 2-point thread for the 2.0 launch are the whole HN record, so 34.6k stars ride the 2023 wave rather than any public debate, the same uncorroborated-stars band as Hive, Ruflo, Yao, and ClawTeam.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=OpenBMB/ChatDev&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=OpenBMB/ChatDev&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=OpenBMB/ChatDev&type=date&legend=top-left" />
</picture>

## Strengths

- The deepest research pedigree in the framework tier: the ACL 2024 paper plus follow-ups on experiential co-learning, MacNet scaling, and Puppeteer orchestration give it a real citation trail.
- 2.0's workflow engine is a genuine generalization: Tarjan cycle detection, Map/Tree dynamic parallel execution, pluggable memory stores, and a documented YAML authoring contract.

## Cautions

- The pivot is young and the old product is a branch: the software-company pipeline that earned the stars survives only as `ChatDev_v1.yaml` inside a platform whose featured demos are data visualization, 3D generation, and deep research.
- The paper's own evaluation produced small apps (average 132 lines), and a published paper review reported a failed run on the reviewer's machine, so the demo-to-production distance is real.
- 1.0 executed generated code directly on the user's machine with no sandbox, a critique worth checking against any workflow that runs Python nodes.

## Pricing

Does not apply: Apache-2.0, self-hosted, and you bring your own model keys.

## Compared to

MetaGPT is the same 2023 software-company genre and went dormant; ChatDev is the one that moved to a maintained platform, at half MetaGPT's stars.
CrewAI fits when you want roles and crews in Python code; ChatDev 2.0 fits when you want zero-code YAML workflows in a web console.
Archon is the closer neighbor in spirit, YAML workflows around coding agents, where ChatDev 2.0 generalizes past software development to any multi-agent scenario.

## Bottom line

Recommended for research and experimentation on multi-agent workflow design, and for reading 1.0 as the clearest artifact of the 2023 role-play wave.
Not for teams wanting a maintained software-company pipeline, because that product is the maintenance branch, and not for anyone who needs independently validated adoption.

## Changes

- 2026-10-28 - Created.

## See also

- [MetaGPT](../metagpt/index.md) - the dormant 2023 peer that stayed a software company instead of pivoting.
- [AutoGen](../autogen/index.md) - the conversational multi-agent incumbent whose self-archival marks the tier's generational shift.
- [CrewAI](../crewai/index.md) - the funded role-and-crew framework that inherited the tier's production mindshare.
- [Archon](../archon/index.md) - the YAML workflow engine built around coding agents rather than generic agents.

## References

- https://github.com/OpenBMB/ChatDev - repository, the 2.0 announcement, license, and the star count (as of 2026-10-28).
- https://arxiv.org/abs/2307.07924 - the ChatDev paper (ACL 2024) grounding the chat-chain lineage.
- https://raw.githubusercontent.com/OpenBMB/ChatDev/main/docs/user_guide/en/index.md - the DevAll backend user guide grounding the workflow-engine description.
- https://pypi.org/project/chatdev/ - the Python SDK, 0.1.0, released 2026-03-21.
- https://hn.algolia.com/api/v1/search?query=ChatDev&tags=story - the 24-point 2023 Show HN and the 2-point 2.0 thread grounding the scrutiny-gap caution.
- https://edforson.substack.com/p/paper-review-chatdev - the critical paper review grounding the sandbox and failed-run cautions.
