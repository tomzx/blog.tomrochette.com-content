---
title: Zed
created: 2026-08-23
updated: 2026-08-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, zed-industries]
readability: 3
audience_notes: >
  Engineers who care about editor latency and want AI optional rather than mandatory.
  Assumes you know what BYOK means and roughly what a GPU-rendered editor is.
---

Zed is the Rust-native editor from Zed Industries whose pitch is performance first, with an AI layer you can pay for, key in, or switch off entirely.
Facts below verified as of 2026-09-02.

**Zed is the performance ceiling of the editor category, and its free tier is the only one that is genuinely unlimited forever with your own keys or external agents, which matters more than any AI feature delta.**

## What it is

A Rust editor with multiplayer collaboration built in, edit predictions, a large extension system, and weekly releases.
The AI stack supports Zed-hosted models, BYOK across Anthropic, OpenAI, Google, Bedrock, Copilot, Deepseek, LM Studio, Mistral, Ollama, OpenRouter, and others, and external agents like Claude Agent and Codex CLI as documented residents.
**Turning AI off entirely is a documented setting, not a workaround.**

## Status

**Active and fast-moving.**
About 89.6k GitHub stars as of 2026-09-02, with commits landing daily.
The engineering runs deep enough to swap graphics libraries mid-flight (the blade-to-wgpu switch, February 2026) without abandoning the product.

## Strengths

- **The fastest editing experience in the category, by design**: Rust, GPU rendering, and a team that treats latency as the product.
- The free tier includes 2,000 edit predictions and unlimited use with your own keys or external agents.
- Pro model hosting bills at API list price plus 10%, the cheapest transparent markup among the major editors.
- ACP support (Zed co-created the protocol) makes it a host for any ACP-compatible agent, keeping the editor out of the vendor-marriage business.

## Cautions

- **The trust file is not spotless**: a 2024 thread documented the editor downloading binaries and NPM packages without consent, and teams with strict egress policies remember.
- Business at $30/seat still lacks SSO, SAML, and SCIM, documented as planned rather than shipped, as of 2026-09-02.
- AI features trail the dedicated platforms; there is no Cursor-style cloud fleet here.
- The licensing is mixed (the repository's root LICENSE file is Apache-2.0 while GitHub reports multiple licenses), so policy reviews take longer than the words "open source" suggest.

## Pricing

Personal is $0 forever, with 2,000 accepted edit predictions and unlimited use with your own keys or external agents.
Pro is $10/month including $5 of tokens, with usage beyond at API list price plus 10%.
Business is $30/seat/month for org model policies, data governance, and spend visibility, as of 2026-09-02.

## Compared to

- [VS Code + Copilot](../vscode-copilot/index.md): the ecosystem default; pick it for extensions and enterprise policy, Zed for speed.
- [Cursor](../cursor/index.md): the platform bet; Zed is the editor bet.
- [JetBrains IDEs](../jetbrains/index.md): analysis depth versus raw speed.

## Bottom line

**Recommended for engineers who measure editor latency and want AI optional rather than mandatory.**
Not for teams needing enterprise identity plumbing or a turnkey agentic platform.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [OpenCode](../opencode/index.md) - the ACP-aligned harness that runs inside Zed
- [The Shifting Bottleneck](../../the-shifting-bottleneck/index.md) - why raw editing speed stopped being the constraint for agent work
- [my-ai-workflow](../../my-ai-workflow/index.md) - keeping a lean tool in the rotation

## References

- https://zed.dev/pricing - tiers, edit prediction counts, list+10% hosting, SSO status, as of 2026-09-02
- https://github.com/zed-industries/zed - repository scale and license, as of 2026-09-02
- https://zed.dev/docs/ai/llm-providers - the BYOK provider list
- https://news.ycombinator.com/item?id=40902826 - the 2024 auto-download consent thread
- https://news.ycombinator.com/item?id=47002825 - the 2026 graphics-stack switch thread
