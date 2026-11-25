---
title: Reef
created: 2026-11-25
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, automated-research, continual-learning, self-improvement, harness-evolution, open-source]
readability: 3
audience_notes: >
  Engineers who serve their own agent through a self-hosted endpoint and want it to keep improving from the feedback its traffic produces.
  Assumes you know what an inference server, a training framework, and an agent harness are.
---

Reef is the Human-Agent Society's Apache-2.0 infrastructure for continually self-improving agents: an inference server that records every response, matches later feedback to it through a receipt, and publishes accepted updates to the agent's model weights or harness as versioned releases.

**Unlike the task-queue and code-tree loops elsewhere in this category, it learns from live served traffic, and the evaluator is where trust sits: a candidate replaces the serving artifact only when evaluation accepts it, and the release chain is append-only, so a rejected candidate cannot touch serving, while a wrong evaluator is obeyed exactly.**

## What it is

A Python package (`reef-infra` 0.1.3, Python 3.12 or newer) installed from PyPI or a source checkout that needs the `git-lfs` system package for its artifact repositories.
Its learning cycle has four steps: Serve (agent requests and interaction records), Observe (feedback matched to recorded interactions), Grow (an update produced from eligible records), and Commit (the configured selection policy applied and accepted updates published).
It has two learning surfaces: model weights, trained with Slime and SGLang (or Tinker, since October 2026), and the agent harness, a tree of text files holding prompts, rules, and skills that a method edits and the evaluation re-runs the agent against.
A third path, test-time training, runs open-ended discovery recipes against a measurable objective.
Its inference endpoints are OpenAI-, Anthropic-, and Responses-compatible (`/v1/chat/completions`, `/v1/responses`, `/v1/messages`), so an existing application points at Reef and starts producing training signal.
The same organization builds [CORAL](../coral/index.md), and the site records Coral test-time training landing as a beta recipe on September 9, 2026.

## Status

Active and fast-moving: 7,627 stars, 734 forks, created 2026-08-31, with 202 open issues and 45 contributors, as of 2026-11-25.
The release train runs v0.0.2 (September 2), v0.1.0 (September 23), v0.1.1 (September 25), v0.1.2 (October 2), and v0.1.3 (October 14, 2026), the latest, and main's newest commit dates to November 25, 2026.
The site reports 400 commits and 415 merged pull requests in the 31 days to November 25, 2026.
The README's November 2026 news says the project is being refactored to a control plane plus workers architecture and that some recipes and examples can fail on `main` until the refactor is complete.
The same month a scenario gained traffic splitting across its served artifacts, a Semantic Router integration, and a `python` harness adapter that evolves a Python program; October brought Tinker as a training component, Modal Sandboxes for episodes and agents, an artifact repository on Hugging Face, and the OPD recipe.
No Hacker News story surfaced in this run's search; the footprint is maker-authored (the X post the README calls its launch post, which I did not fetch, and a September 15, 2026 Hugging Face article by the authors), two third-party write-ups, and directory listings.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Human-Agent-Society/reef&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Human-Agent-Society/reef&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Human-Agent-Society/reef&type=date&legend=top-left" />
</picture>

## Strengths

- Serving comes first: every response returns an `x-reef-agent-record-id` receipt, and a later report cites the receipts it grades, so the training signal is tied to the exact interaction that produced it.
- One artifact model covers checkpoints, LoRA adapters, harness trees, and routing policies, all versioned in Git LFS with an append-only release chain per scenario.
- The harness path needs no local training GPUs: a model endpoint, representative tasks, and an evaluator are enough.
- The harness tree is served with no endpoint, key, or model inside, and the README tells you to write it outside the project the agent works in, because a session can write files in its own project.

## Cautions

- The project is twelve weeks old and pre-1.0: v0.1.3's upgrade notes change configuration and extension interfaces and drop legacy layouts, and PyPI carries a yanked 0.2.0 whose reason reads "Published before 0.2 was ready. Please use 0.1.3."
- The November 2026 refactor is unfinished, and the maintainers themselves warn that recipes and examples can fail on `main` until it is.
- The weight-training path needs the GPU stack: the TTT-Discover example requires Linux, four NVIDIA GPUs, and Docker.
- The evaluator is the whole safety boundary: a candidate replaces the serving version only if evaluation accepts it, so a narrow evaluation set makes the release chain execute the wrong objective reliably.
- Third-party coverage is thin and the maker's "first open-source infrastructure" claim is contested phrasing (Karne's write-up opens on it), and the same write-up names the operational caveat that an installed harness runs code from the install environment as you.

## Pricing

Free and open source under Apache-2.0; the site lists no paid tier, so pricing does not apply.
Costs are your own model API calls for the harness path, your GPU compute for the weight path, and any sandbox provider you route episodes through.

## Compared to

- [AutoContext](../autocontext/index.md): the promotion-gate precedent, a self-improvement harness that keeps only context and training changes that beat the incumbent on matched, replayed trials; Reef is the serving layer underneath, collecting the trials from live traffic and versioning weights beside harness trees.
- [CORAL](../coral/index.md): the organization sibling, which evolves a population of coding agents against a grader in isolated worktrees; Reef's roadmap carries "Multi-agent test-time training with CORAL" as an open item.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the keep-or-revert loop over one training script judged by a validation curve; Reef generalizes the judge to a configurable evaluator over served artifacts, which moves trust from a number to whoever wrote the evaluator.

## Bottom line

**Recommended for teams that already serve an agent through a self-hosted endpoint and want receipt-linked, versioned updates to its weights or harness without building the feedback plumbing.**
Not for anyone who needs a stable interface this quarter, and not for a project whose feedback has no trustworthy evaluator.

## Changes

- 2026-11-25 - Created.

## See also

- [AutoContext](../autocontext/index.md) - the promotion-gated self-improvement harness this note's routing follows
- [CORAL](../coral/index.md) - the same organization's multi-agent evolution framework
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the keep-or-revert ancestor of the judging pattern
- [Kapso](../kapso/index.md) - the campaign framework with a declared evaluator
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Human-Agent-Society/reef - repository: Apache-2.0, 7,627 stars, 734 forks, created 2026-08-31, pushed 2026-11-25, 202 open issues, 45 contributors (as of 2026-11-25; fetched 200 through the GitHub API, 2026-11-25)
- https://github.com/Human-Agent-Society/reef/blob/main/README.md - the four-step cycle, the two learning surfaces, compatible endpoints, the harness-evolution path, the recipes table, and the November 2026 news (refactor warning, traffic splitting, Semantic Router, the python harness adapter) (fetched 200 through the README API, 2026-11-25)
- https://reefinfra.ai/ - the site's release news, activity figures, and the Coral test-time training beta (fetched 200, 2026-11-25)
- https://reefinfra.ai/docs/getting-started/quickstart/ - the quickstart: serve inference and report feedback against the receipt (fetched 200, 2026-11-25)
- https://reefinfra.ai/docs/user-guide/recipes/tttd/ - the TTT-Discover example's tasks (Erdős minimum-overlap, circle packing) and its hardware requirement (fetched 200, 2026-11-25)
- https://huggingface.co/blog/quao627/your-inference-server-is-secretly-a-learner-reef - the authors' Hugging Face article (September 15, 2026, by Ao Qu, Hanfei Yu, and coauthors): receipts, Git LFS artifacts (checkpoints, LoRA adapters, harness trees, routing policies), the compare-and-swap append-only release chain, and hot weight updates (fetched 200, 2026-11-25)
- https://api.github.com/repos/Human-Agent-Society/reef/issues/25 - the roadmap: three focus areas, the CORAL test-time-training item, and `TBD` meaning open for ownership (fetched 200, 2026-11-25)
- https://api.github.com/repos/Human-Agent-Society/reef/releases/latest - v0.1.3 (October 14, 2026) and its upgrade notes (fetched 200, 2026-11-25)
- https://pypi.org/pypi/reef-infra/json - the 0.1.3 package, the Python 3.12 floor, and the yanked 0.2.0 with its reason (fetched 200, 2026-11-25)
- https://xiaohu.ai/en/article/reef-continual-self-improving-agents/ - third-party write-up naming Ao Qu at MIT and the record-only proxy start (fetched 200, 2026-11-25)
- https://aniketkarneai.com/blog/2026-09-30-reef-continual-self-improving-agent-infrastructure/ - the critical source: the contested "first" claim and the install-environment caveat (fetched 200, 2026-11-25)
- https://hn.algolia.com/api/v1/search?query=reef%20self-improving&tags=story - the search returning one unrelated hit and no Reef story (fetched 200, 2026-11-25)
- https://raw.githubusercontent.com/yibie/awesome-autoresearch/main/README.md - the list entry that surfaced the candidate (fetched 200, 2026-11-25)
