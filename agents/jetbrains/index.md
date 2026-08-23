---
title: JetBrains IDEs
created: 2026-08-23
updated: 2026-08-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, jetbrains]
readability: 3
audience_notes: >
  Engineers living in IntelliJ-family IDEs who want the current map of JetBrains' AI layer.
  Assumes you know what an IDE inspection is and what BYOK means.
---

JetBrains IDEs are the analysis-heavy editors for Java, Kotlin, Python, and friends, whose AI layer now spans AI Assistant and the Junie agent from IDE to CI.
Facts below verified as of 2026-08-23.

**JetBrains is the only major IDE vendor whose entire AI layer is removable and provider-agnostic, and it got there by backlash: the late-2023 forced-bundling outcry is why you can now uninstall the whole thing.**

## What it is

The IDEs are proprietary (Community editions excepted) and built on the IntelliJ platform's inspection and refactoring engine.
**The AI stack has two layers: AI Assistant for chat and completion, and Junie, the plan-first agent that ships in the IDEs, in CI, and as an LLM-agnostic CLI.**
ACP-speaking harnesses (OpenCode among them) can host inside JetBrains IDEs, so the editor works with rival agents.
Pricing runs through JetBrains AI Pro and AI Ultimate subscriptions metered in AI credits, with Junie BYOK at provider rates as the escape hatch.

## Status

**Active and shipping.**
Junie went from IDE agent (January 2025) to GA (April 2025) to an LLM-agnostic CLI with plan files and CI integration; the harness side is profiled in the [Junie](../junie/index.md) note.
The AI layer was unbundled into a separate, removable plugin in March 2024 after the backlash.

## Strengths

- **The deepest static-analysis grounding in the business**: a decade of inspections feeds edits the way LSP feeds lighter editors.
- One vendor covers IDE, terminal CLI, and CI pipelines with a single AI identity.
- Removability means policy-restricted teams can run the IDEs AI-free without forks or workarounds.
- Junie's plan artifacts land in the repository as reviewable files.

## Cautions

- **Community mindshare is the gap**: launch threads for JetBrains AI drew a fraction of the attention Claude Code or Cursor get, and vendor benchmarks fill the silence.
- The client is proprietary, so unlike VS Code or Zed you cannot audit the editor.
- Subscription credits are thin enough that BYOK is effectively required for heavy work (verified counts are in the [Junie](../junie/index.md) note).
- The December 2023 bundling thread ("cannot be completely removed") is old, but it set the trust baseline some engineers still apply.

## Pricing

AI Pro is $8.33 per user/month (annual) and AI Ultimate is $25 per user/month, metered in AI credits, as of 2026-08-23.
**Junie BYOK bypasses metering at provider rates**, and the tier starts free with 5 credits and no card.

## Compared to

- [VS Code + Copilot](../vscode-copilot/index.md): breadth and openness versus depth of analysis; polyglot teams drift to VS Code, Java and Kotlin shops stay.
- [Cursor](../cursor/index.md): the AI-first bet versus the IDE-first bet.
- [Zed](../zed/index.md): raw speed versus inspection depth.

## Bottom line

**Recommended for teams whose languages are JetBrains-strong and who want one analysis engine under chat, agent, and refactor.**
Not for anyone who needs an open editor or a large community ecosystem.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [Junie](../junie/index.md) - the agent that ships inside these IDEs
- [Iterating on Agent Skills](../../iterating-on-agent-skills/index.md) - the skill formats the AI layer consumes
- [my-ai-workflow](../../my-ai-workflow/index.md) - keeping a heavy IDE and a lean agent in the same rotation

## References

- https://www.jetbrains.com/ai/ - the AI product family entry point
- https://junie.jetbrains.com/ - plans, credits, and BYOK, as of 2026-08-23
- https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/ - Junie's January 2025 launch
- https://news.ycombinator.com/item?id=39238666 - the bundling outcry thread (February 2024)
- https://news.ycombinator.com/item?id=39636060 - the March 2024 unbundling thread
