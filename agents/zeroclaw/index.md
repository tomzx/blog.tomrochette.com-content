---
title: ZeroClaw
created: 2026-08-27
updated: 2026-08-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, assistant-runtimes, personal-assistants, rust, open-source]
readability: 3
audience_notes: >
  Engineers who want a personal agent runtime as a single static binary they can drop on any machine, including a Raspberry Pi.
  Assumes you know why a compiled binary changes the trust conversation and what BYOK means.
---

ZeroClaw is zeroclaw-labs' personal agent runtime: a single Rust binary (dual MIT/Apache-2.0) that talks to about 20 model providers, reaches the world through 30+ channels, and acts through tools including hardware, all on your own machine.
Facts below verified as of 2026-08-27.

**ZeroClaw bets the frontier is compile-time: one Rust binary with no runtime sprawl is the ownership answer for people who do not trust a Node process with their messages, and its motto (you own the agent, the data, and the machine) is a requirements list the others treat as marketing.**

## What it is

Install with a curl script (or a Rust-free PowerShell path on Windows), run `zeroclaw quickstart`, and one binary becomes the assistant: providers span Anthropic, OpenAI, Ollama, and roughly twenty others, channels span Discord, Telegram, Matrix, email, voice, webhooks, and your own CLI, and tools cover shell, browser, HTTP, hardware, and custom MCP servers.
Everything runs locally with your keys in your workspace, and the docs ship as a translated book with the architecture and a stated four-opinion philosophy.
An Android port ([ZeroClaw-Android](https://github.com/Natfii/ZeroClaw-Android), 303 stars) runs agents 24/7 on your phone with a native Rust core and 25+ providers, and community threads run it on a Raspberry Pi.

## Status

Active and large, but quietly so.
As of 2026-08-27: 32,662 stars and 4,915 forks since creation on 2026-02-13, pushed the morning of verification, 804 open issues, Apache-2.0/MIT dual licensed.
**Its HN footprint is nearly empty (threads at 2 to 8 points), so the star growth ran through Discord and word of mouth, a missing community discussion record that is itself the signal to verify before relying on it.**

## Strengths

- Single-binary deployment kills the dependency conversation: copy, run, done, on a Pi if you like.
- 30+ channels including voice and webhook paths, the widest surface in the lightweight family.
- Dual licensing and edition-2024 Rust signal engineering seriousness.
- The hardware tool path (and the Android port) makes it the variant for physical projects.

## Cautions

- Thin independent coverage: almost no third-party writing or discussion to check claims against.
- Hardware tools are a foot-gun by design; the trust question moves from the codebase to the tool grant.
- 804 open issues against a labs team you cannot size from outside.
- The security suite ecosystem (clawsec) names OpenClaw, PicoClaw, and NanoClaw but not ZeroClaw, so the audit tooling has not caught up.

## Pricing

Free and open source under MIT OR Apache-2.0.
No paid tier as of 2026-08-27.

## Compared to

- [NanoClaw](../nanoclaw/index.md): the other shrink-the-root bet, via containers and auditable code instead of compilation; choose NanoClaw to read the code, ZeroClaw to stop needing to.
- [OpenClaw](../openclaw/index.md): the ecosystem root; choose it for companion apps and channel depth.
- [PicoClaw](../picoclaw/index.md): also a single binary, but Go and hardware-first with a vendor behind it.

## Bottom line

**Recommended for Rust shops, Pi deployments, and anyone whose answer to "can I trust it" is "I can deploy it".**
Not for ecosystems (it has none yet) or for anyone who needs third-party verification before trusting a runtime.
The disagreeable claim I will defend: an assistant you cannot read is safer as a static binary than as a container you also cannot read, and ZeroClaw is the only family member candid about that trade.

## See also

- [OpenClaw](../openclaw/index.md) - the root runtime
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the family compared
- [NanoClaw](../nanoclaw/index.md) - the read-the-code alternative
- [PicoClaw](../picoclaw/index.md) - the even smaller sibling

## References

- https://github.com/zeroclaw-labs/zeroclaw - README: runtime model, providers, channels, tools
- https://api.github.com/repos/zeroclaw-labs/zeroclaw - stars, forks, issues as of 2026-08-27
- https://docs.zeroclawlabs.ai/master/en/introduction.html - the documentation book
- https://github.com/Natfii/ZeroClaw-Android - the Android port (303 stars)
- https://news.ycombinator.com/item?id=47047192 - the launch-era thread (6 points, the thin-footprint evidence)
