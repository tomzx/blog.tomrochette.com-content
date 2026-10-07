---
title: llamafile
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, local-inference, single-file]
readability: 3
audience_notes: >
  Engineers distributing or running open-weight models locally, and anyone comparing the local-serving family in this category.
  Assumes you know what a GGUF weights file is.
---

llamafile is Mozilla's single-file LLM distribution format: it folds llama.cpp and Cosmopolitan Libc into one executable so a weights file and its runtime become a single binary that runs on six operating systems with no installation.

**llamafile attacks distribution rather than serving: where Ollama, the family's incumbent, gives your machine a model registry and a daemon, llamafile gives one person a file they can hand to another person, which is why it remains the only member here whose unit of delivery is an email attachment.**

## What it is

A Mozilla Builders project launched November 2023, built by Justine Tunney (the Cosmopolitan Libc author) and now revamped by Mozilla.ai, licensed Apache-2.0 with its llama.cpp changes MIT so they can move upstream (26,190 stars, pushed 2026-10-07, as of 2026-10-07).
You point it at a GGUF weights file and get one cross-platform binary containing the weights, the inference engine, and a web UI, runnable on macOS, Linux, Windows, and the BSDs across six OS targets, on CPU or GPU, with no install step.
The same packaging ships whisperfile, a single-file speech-to-text and translation tool on whisper.cpp.
Release 0.10.6 (September 2026) moved to a new build system on the 0.10 line, and the project publishes pre-built llamafiles for popular models through Mozilla's docs.

## Status

Active under Mozilla.ai stewardship: created 2023-09-10, 26,190 stars, release 0.10.6 published 2026-09-15, as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=mozilla-ai/llamafile&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=mozilla-ai/llamafile&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=mozilla-ai/llamafile&type=date&legend=top-left" />
</picture>

The GitHub license field reads NOASSERTION because the repository combines Apache-2.0 with MIT-licensed llama.cpp changes; both Mozilla's announcement and the README badge state Apache-2.0 as the project license.
Development cadence is slower than the local-inference family's leaders (four releases in 2026), which is the trade of a format-stability project in a fast field.

## Strengths

- The lowest-friction distribution story in local inference: one file, no installer, no runtime setup, six OSes.
- Cosmopolitan's reproduction promise, a given llamafile running the same weights the same way indefinitely, is unique in a category where toolchains churn monthly.
- GPU and dlopen support inside a single binary, so it is not a toy CPU-only path.
- Mozilla stewardship and Apache-2.0 licensing make it the least commercially exposed member of the family.

## Cautions

- Massive single binaries (weights plus engine) are clumsy to update: a new model version means a new multi-gigabyte file, where Ollama pulls a manifest.
- No model registry or discovery layer; you bring your own GGUF or use Mozilla's pre-built set.
- Slower release cadence than llama.cpp itself, so fresh architecture support lags the upstream engine.
- The AVX2 requirement on x64 quick-install binaries excludes older Intel and AMD hardware and some VMs.

## Pricing

Free and open source (Apache-2.0, with llama.cpp changes MIT); there is no paid tier, so pricing does not apply.
Costs are your own hardware and the weights you bundle.

## Compared to

- [Ollama](../ollama/index.md): the registry-and-daemon incumbent; choose llamafile when the artifact must travel as one file, Ollama when a managed local model store matters more.
- [Magnitude](../magnitude/index.md): the self-optimizing inference engine; llamafile optimizes for distribution, Magnitude for kernel performance on your device.
- [LiteLLM](../litellm/index.md): the self-hosted gateway over cloud APIs; llamafile removes the cloud from the picture entirely.

## Bottom line

**Recommended for distributing a fixed model to non-technical recipients, offline environments, and archival use where the weights must stay runnable, and for the six-OS no-install demo.**
Not as a daily driver for people who churn models weekly, and not for serving agents that want a registry, quotas, or a daemon.

## Changes

- 2026-10-07 - Created.

## See also

- [Ollama](../ollama/index.md) - the registry-and-daemon counterpart in the local-serving family
- [Magnitude](../magnitude/index.md) - the performance-focused local inference engine
- [LiteLLM](../litellm/index.md) - the gateway alternative for teams routing cloud providers instead
- [Model Access Feature Matrix](../model-access-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/mozilla-ai/llamafile - repository, README, licensing badge, whisperfile, and the 0.10 build-system note (fetched 200, 2026-10-07)
- https://api.github.com/repos/mozilla-ai/llamafile - stars, created date, push date, and the NOASSERTION license field (fetched 200, 2026-10-07)
- https://hacks.mozilla.org/2023/11/introducing-llamafile/ - Mozilla's launch announcement: the six-OS goal, Justine Tunney's authorship, and the Apache-2.0 plus MIT split (fetched 200, 2026-10-07)
- https://docs.mozilla.ai/llamafile - the Mozilla.ai docs hub, pre-built llamafiles, and whisperfile surface (fetched 200, 2026-10-07)
- https://api.github.com/repos/mozilla-ai/llamafile/releases - the 0.10.6 release of 2026-09-15 and the 2026 cadence (fetched 200, 2026-10-07)
- https://raw.githubusercontent.com/mozilla-ai/llamafile/HEAD/README.md - the llama.cpp plus Cosmopolitan architecture and the AVX2 x64 compatibility note (fetched 200, 2026-10-07)
