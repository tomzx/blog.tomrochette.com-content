---
title: Andrej Karpathy
created: 2026-08-29
updated: 2026-08-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, people, publications, developer, model-researcher]
readability: 3
audience_notes: >
  Engineers who want the conceptual vocabulary for how AI changes software, from the person who named Software 3.0, vibe coding, and the agentic-engineering line.
  Assumes you know who Andrej Karpathy is: OpenAI co-founder and former Tesla AI lead, now at Anthropic.
---

Andrej Karpathy names the eras: he coined "vibe coding", drew the line between vibe coding and agentic engineering, and reframed the current era as Software 3.0 in his 2026 essays.
Facts below verified as of 2026-08-30.

**Karpathy is less a chronicler than a vocabulary-setter: his Software 3.0 framing, that the context window is now the program and verifiability defines what AI can automate, is the lens this whole section's subject matter is read through.**

## What it is

A founding member of OpenAI, former Director of AI at Tesla, and now (May 2026) a member of Anthropic's pre-training team.
He publishes conceptual essays (Software 2.0, Software 3.0, the LLM-as-OS point) and open-source teaching projects (micrograd, nanoGPT, AutoResearch), and ran the AI-education startup Eureka Labs before joining Anthropic.
His public output is the canonical reference for how software engineering itself is being reorganized around agents.

## Status

Active and central.
As of 2026-08-29 he is at Anthropic's pre-training team, refreshing his thesis in the Sequoia Ascent 2026 essay that defines Software 3.0.
His June 2026 blog post lays out verifiability as the automation boundary, and his AutoResearch project demonstrates agents running research loops overnight, so his writing and his builds move together.

## Strengths

- He sets the framing the rest of the field adopts: Software 3.0, agentic engineering, the context-window-as-program model.
- His theses are concrete and falsifiable, tied to the models he works on and the code he ships.
- Draws the practical line between vibe coding (prompt and pray) and disciplined agentic engineering, a distinction this section's notes presuppose.
- Pairs strong conceptual writing with working open-source implementations.

## Cautions

- He sits at the frontier labs, so his claims about agent capability reflect frontier-model economics, not the typical mid-market reality.
- Frequency is low: he publishes essays and talks rather than a daily or weekly cadence, so he is not a current-events feed.
- His vocabulary-setting role means he is widely paraphrased; verifying against his primary writing matters.

## Pricing

Free.
Essays, talks, and repositories are all public and free, with no newsletter paywall.

## Compared to

- [Steve Yegge](../steve-yegge/index.md): both name the era and build code; Karpathy from frontier research, Yegge from shipping in public.
- [Simon Willison](../simon-willison/index.md): the daily practitioner notes versus the periodic conceptual essay; read both for currency and for vocabulary.
- [Latent Space](../latent-space/index.md): Latent Space gives his Software 3.0 talk the interview treatment and spreads the framing.

## Bottom line

**Recommended for engineers who want the durable concepts behind the daily tool churn, from the person who keeps naming the eras.**
Not for people who need a current-events feed or want vendor-neutral, non-frontier framing.

## See also

- [Context Management Patterns](../context-management-patterns/index.md) - the context-window-as-program thesis in operational form
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the landscape his agentic-engineering line sits above
- [OpenClaw](../openclaw/index.md) - the assistant-family trajectory he discusses as part of the agent era
- [The Codebase Gardener](../../the-codebase-gardener/index.md) - the human role that survives the era he names

## References

- https://karpathy.ai/ - his main site and the canonical reading list
- https://karpathy.bearblog.dev/sequoia-ascent-2026/ - the Sequoia Ascent 2026 essay defining Software 3.0
- https://karpathy.medium.com/software-2-0-a64152b37c35 - the original Software 2.0 essay
- https://github.com/karpathy/autoresearch - the overnight agent research project
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f - the LLM-Wiki knowledge-base pattern
- https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/ - independent coverage of his move to Anthropic
