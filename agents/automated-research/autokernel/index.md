---
title: AutoKernel
created: 2026-10-23
updated: 2026-10-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, gpu, kernel-optimization, autoresearch]
readability: 3
audience_notes: >
  ML systems engineers who want faster GPU kernels and want to see what an unattended
  optimization loop actually keeps. Assumes you know what a Triton kernel and a benchmark
  harness are.
---

AutoKernel is RightNow AI's MIT-licensed autoresearch loop for GPU kernels: point it at a PyTorch model with a coding agent, and it profiles, extracts, and iteratively optimizes Triton or CUDA C++ kernels against a fixed correctness-first benchmark, keeping only the changes that measure faster.

**AutoKernel carries the Karpathy keep-or-revert loop into the domain engineers feel in wall-clock time, and its judge is the strongest in the community tier: a five-stage correctness harness that must pass before any speedup counts, so a fast-but-wrong kernel reverts instead of shipping.**

## What it is

A Python framework (created 2026-03-11, MIT) by RightNow AI, a YC-backed company that calls itself "the kernel lab behind instant AI".
The pipeline is five scripts: `profile.py` ranks a model's kernels by GPU time, `extract.py` generates starter Triton or CUDA C++ kernels for the bottlenecks, the coding agent (Claude, Codex, or any agent reading `program.md`) edits `kernel.py` one kernel at a time and runs `bench.py`, `orchestrate.py` schedules the next kernel by Amdahl's law, and `verify.py` replugs the winners and reports end-to-end speedup.
Each experiment takes about 90 seconds, roughly 320 overnight, and every result lands in a plain `results.tsv` with throughput, latency, percent of peak, speedup, and a correctness verdict.
Nine kernel types ship as starters (matmul, softmax, layernorm, rmsnorm, flash attention, fused MLP, cross entropy, rotary embedding, reduce), and a KernelBench bridge scores against Stanford's 250-plus-problem benchmark with the `fast_p` metric, while `export_hf.py` ships winners to the Hugging Face Kernels Hub.

## Status

Active: 1,603 stars, 163 forks, 16 open issues, created 2026-03-11, last pushed 2026-10-23, as of 2026-10-23.
There are no git tags or GitHub releases; the README's own changelog runs v1.0.0 through v1.3.0 (the latest adding AMD ROCm support for MI300X-class GPUs and a batch of correctness fixes).
The launch thread reached 47 points and 10 comments on Hacker News on 2026-03-11, and the authors' paper (arXiv 2603.21331, March 2026) reports H100 results of 5.29x over PyTorch eager on RMSNorm and 2.82x on softmax, ahead of `torch.compile` max-autotune on most tested configurations, as of 2026-10-23.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=RightNow-AI/autokernel&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=RightNow-AI/autokernel&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=RightNow-AI/autokernel&type=date&theme=dark&legend=top-left" />
</picture>

**The skeptical reads are on the record and unanswered: launch-thread commenters asked why the paper never benchmarks against classical autotuning such as TVM's Ansor, and one measured CUTLASS roughly 3x faster than AutoKernel's result on 4k fp16 GEMM, while another pointed at DeepMind's AlphaEvolve improving matrix-multiply kernels a generation earlier.**

## Strengths

- The correctness gate is the design's core: smoke, shape-sweep, numerical-stability, determinism, and edge-case checks run before timing, so the loop cannot optimize into garbage.
- Amdahl's law orchestration chases end-to-end impact rather than per-kernel glory, moving on when a kernel's remaining share makes speedups irrelevant.
- Scope discipline keeps the loop inspectable: the agent touches one file, results live in a TSV a human can diff, and every experiment costs about 90 seconds.
- The KernelBench bridge and the Hugging Face Kernels export connect the loop to the field's standard benchmark and to a one-line distribution path.

## Cautions

- The headline speedups are the authors' own, measured against PyTorch eager and `torch.compile`, not against CUTLASS or Ansor-class autotuners, and the launch thread's CUTLASS rebuttal has no README answer.
- RightNow AI is a vendor: the repository serves its kernel-lab story, enterprise optimization funnels through a contact form, and the bench defaults favor the hardware classes (H100, A100, RTX 4090) the company targets.
- The loop assumes an NVIDIA GPU (AMD ROCm since v1.3.0) plus a coding-agent subscription, so the entry cost is a hardware bill, not an API bill.
- Version traffic lives only in a README changelog with no tags or releases, so pinning a version means pinning a commit.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your own GPU time and your coding-agent subscription (Claude Code, Codex, or an equivalent).
RightNow AI sells enterprise kernel optimization through a contact form with no published prices, and its System Zero and RunInfra products are separate.

## Compared to

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the founding keep-or-revert loop on a training script's loss curve; AutoKernel ports the same loop to kernels and adds the correctness gate and Amdahl orchestration.
- [AutoContext](../autocontext/index.md): the other promote-only-if-it-wins harness; AutoContext replays matched candidate and incumbent trials before promoting context changes, AutoKernel trusts the single fixed bench on one file.
- [AIDE ML](../aide-ml/index.md): the metric-judged tree search over whole ML solutions; AutoKernel keeps one lineage per kernel and spends its complexity budget on the correctness harness instead of search breadth.

## Bottom line

**Recommended for ML systems engineers with idle NVIDIA GPUs who want measured kernel speedups with every experiment auditable in a diffable log.**
Not for production performance work that needs speedups validated against CUTLASS-class libraries, and not for teams without a coding-agent subscription to drive the loop.

## Changes

- 2026-10-23 - Created.

## See also

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the founding loop AutoKernel ports to GPU kernels
- [AutoContext](../autocontext/index.md) - the stricter promotion-gate cousin for context and training changes
- [AIDE ML](../aide-ml/index.md) - the metric-judged tree-search ancestor
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/RightNow-AI/autokernel - README: the five-script pipeline, nine kernel types, KernelBench bridge, design choices, and the v1.0.0-to-v1.3.0 changelog (fetched 200 via the GitHub API, 2026-10-23)
- https://api.github.com/repos/RightNow-AI/autokernel - stars, forks, open issues, created and pushed dates, MIT license, and topics for the as-of status (fetched 200, 2026-10-23)
- https://arxiv.org/abs/2603.21331 - the authors' paper: five-stage correctness harness, 9,000 lines of Python, and the H100 claims (5.29x eager on RMSNorm, 2.82x on softmax) (fetched 200 via the arXiv API, 2026-10-23)
- https://hn.algolia.com/api/v1/search?query=autokernel&tags=story - the 47-point, 10-comment launch thread of 2026-03-11 and the small May paper listing (fetched 200, 2026-10-23)
- https://hn.algolia.com/api/v1/items/47332688 - the launch thread's critical comments: the Ansor comparison gap, the CUTLASS 3x GEMM rebuttal, and the AlphaEvolve precedent (fetched 200, 2026-10-23)
- https://www.rightnowai.co/ - the company: "the kernel lab behind instant AI", YC backing, and the System Zero product line (fetched 200, 2026-10-23)
- https://www.rightnowai.co/forge - the enterprise offer, now a redirect into the contact funnel with no published prices (fetched 308 to 200, 2026-10-23)
