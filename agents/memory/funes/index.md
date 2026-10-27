---
title: Funes
created: 2026-10-16
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, session-memory, local-first, mcp, hugging-face]
readability: 3
audience_notes: >
  Engineers running several coding agents who want recall of what past sessions actually
  said, without an LLM rewriting it into facts.
  Assumes you know what embeddings, BM25, and MCP are.
---

Funes is Hugging Face's Apache-2.0 Rust binary that indexes past sessions from Claude Code, Codex, pi, and Hermes into one local Lance dataset of verbatim chunks, and serves them back through pull-only recall where every hit carries exact session-and-turn provenance.

**Its bet is that memory should defer to the reader: nothing is distilled at write time, recall happens only when asked, and the actual passage, not a summary, is what comes back.**

## What it is

A single binary from Hugging Face, built and mostly written by David Corvoysier (dacorvo): indexing is a deterministic pipeline (parse, chunk, embed with a pinned local model, write to a Lance dataset), so no model summarizes or extracts facts on the way in.
Each memory fixes one embedding model (an English or a multilingual one, chosen at first index); recall fuses vector and BM25 search, reranks a deep pool with a local cross-encoder, and reweights hits by recency.
`funes add` wires an agent in one command: the read tools, per-turn indexing hooks, and, with a memory bound, publication at session boundaries to a Hugging Face dataset repo you own, private by default.
Beyond the four maintained integrations the surfaces are a read-only MCP server (recall, get, status), a JSONL turns format any producer can write, and community integrations for OpenCode and jcode maintained by their authors.

## Status

**Active, young, and moving fast, with adoption that is still mostly repository stars.**
569 stars, 51 forks, and 11 open issues and pull requests on a repository created 2026-06-18 and pushed 2026-10-22, Apache-2.0, as of 2026-10-27 (GitHub API).
The release train runs weekly: v1.7.0 memories compaction (2026-10-07), v1.8.0 multilingual embedder (2026-10-08), v1.9.0 GPU indexing and host binding (2026-10-14), and v1.9.1 (2026-10-20) a small maintenance release on top, with dacorvo holding 873 of the 927 recorded contributions across twelve contributors.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=huggingface/funes&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=huggingface/funes&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=huggingface/funes&type=date&legend=top-left" />
</picture>

The September 3 announcement drew two small Hacker News threads (11 and 6 points, one comment each) and little else, and as of 2026-10-16 the category's own Awesome-Agent-Memory list does not carry it, so the footprint is the repository, the published demo dataset (71,648 chunks, 865 downloads last month), and one adversarial measurement.
The sharpest critical material is partly the project's own: RATIONALE.md reports that a batch of recall-quality enhancements (abstention thresholds, MMR diversity, near-duplicate collapse, semantic expansion, deeper pools) moved recall not at all against its labeled anchor, and that the shipped cross-encoder scored no better than the fused order at seconds per recall.
The README discloses that every Hub request carries an anonymous install id (opt out with `DO_NOT_TRACK=1` or `FUNES_NO_TELEMETRY=1`), and the installer's checksum shares the bucket it verifies, so it does not authenticate the source.
In the announcement comments, deja's author measured funes 1.3.0 on 19,195 sessions: hit@1 9 of 100 with defaults at 6.3 seconds per query after a 2h03m index, against plain-BM25 deja at 18 of 100 in 24 milliseconds, and the maintainer's reply concedes BM25 matches on lookup-style corpora, arguing funes pays off when the answer is hard to find.

## Strengths

- **Verbatim memory with provenance**: every hit is the passage as written, citing its session and turn, and `get` reassembles the full turn, so nothing depends on an extraction model's fidelity.
- One memory spans four harnesses and any MCP client, and every hit names the agent it came from, so switching agents loses nothing.
- **The Hub layer is the category's novel move**: your memory publishes as a dataset repo you own (private by default), which gives cross-machine and team recall through storage you control instead of a memory service account.
- Publishing fails closed: credentials are redacted at index time, an always-on TruffleHog-backed gate withholds any chunk still holding a secret, and `funes scrub` cleans rows already stored.

## Cautions

- **The project's own A/B runs found its retrieval extras buy cost, not recall**: the cross-encoder scored no better than the fused order at seconds per recall, and the outside measurement put queries at 6.3 seconds against plain BM25's 24 milliseconds.
- The default 30-day recency half-life halved rank-1 on history older than a month in that measurement, and most of a long-lived corpus is older than a month.
- Pull-only recall means the agent must choose to ask: nothing resurfaces a past failure unprompted, which is the behavior injection-style memory exists to provide.
- **The push gate cannot unpublish**: a secret that reached a remote memory persists in dataset history until you rotate the credential, scrub, delete the repo, and repush, per SECURITY.md.
- A memory binds one embedding model, so changing models means rebuilding (the memory is a disposable derived artifact, and the transcripts remain the source of truth), and the community OpenCode and jcode integrations are author-maintained with no review from Hugging Face.
- Recalling from someone else's published memory is untrusted input: SECURITY.md itself warns a malicious memory could carry prompt injection, and advises per-call reads over binding.

## Pricing

Pricing does not apply: the binary is free and Apache-2.0 with no hosted tier.
Embedding and reranking run on your hardware, and the optional Hub layer stores the dataset in your own account under ordinary Hub limits and your own token scopes.

## Compared to

- [PLUR](../plur/index.md): the opposite contract on timing, where PLUR injects shared engrams automatically and funes never volunteers anything, answering only when called; sharing rides your own Hub dataset repo rather than git remotes.
- [claude-mem](../claude-mem/index.md): the capture-and-compress school, per harness, with your tokens doing the distilling; funes spans four harnesses on one verbatim index and spends no tokens at ingest.
- [deja](../deja/index.md): the other no-LLM local recall engine, retroactive over forty-plus agents' transcripts where funes hooks four harnesses live, with a documented head-to-head in the announcement comments that deja's plain BM25 won on speed and hit@1 for lookup questions.

## Bottom line

**Recommended for engineers running Claude Code, Codex, pi, or Hermes (or any MCP client) across several machines who want auditable recall of what was actually said, and a team or public memory living in a Hub dataset they own.**
Not for workflows that need memory surfaced without being asked, for users who need sub-second recall over large corpora today, or for anyone unwilling to opt out of the install-id telemetry (or to skip publishing sessions that might hold an unredacted secret).

## Changes

- 2026-10-16 - Created from the 2026-10-16 cross-category resolution (the HermesGate small-but-distinct precedent), with twelve fetched sources and the negative self-run A/B results, the deja author's adversarial measurement, and the missing independent coverage recorded as the critical angle.
- 2026-10-24 - Recorded v1.9.1 (October 20), a small maintenance release on the weekly train (recall now ends with what to try when hits miss, a `--repo` flag, and bind and refresh fixes).
- 2026-10-27 - Rotation re-verification: every cited URL re-fetched live (all twelve reachable), no release after v1.9.1, the repository snapshot refreshed (pushed 2026-10-22, 51 forks, 11 open issues), and the contribution snapshot refreshed to dacorvo's 873 of 927 recorded contributions across twelve contributors.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [PLUR](../plur/index.md) - the injection counterpart to the pull-only contract
- [claude-mem](../claude-mem/index.md) - the capture-and-compress school this design refuses
- [deja](../deja/index.md) - the retroactive no-LLM recall engine whose author measured funes
- [agentmemory](../agentmemory/index.md) - the other local cross-harness memory server

## References

- https://api.github.com/repos/huggingface/funes - repository metadata: 569 stars, 48 forks, 12 open issues, created 2026-06-18, pushed 2026-10-16, Apache-2.0, Rust, as of 2026-10-16
- https://raw.githubusercontent.com/huggingface/funes/main/README.md - architecture, installer and its checksum caveat, commands, install-id telemetry disclosure, Hub publication, and the turns format
- https://api.github.com/repos/huggingface/funes/releases - the release train: v1.7.0 (2026-10-07), v1.8.0 (2026-10-08), v1.9.0 (2026-10-14), v1.9.1 (2026-10-20)
- https://api.github.com/repos/huggingface/funes/contributors - dacorvo's 841 of 891 recorded contributions
- https://raw.githubusercontent.com/huggingface/funes/main/docs/RATIONALE.md - the four design choices, the provider-field critique, and the negative A/B results on recall enhancements and the cross-encoder
- https://raw.githubusercontent.com/huggingface/funes/main/docs/add.md - the four supported agents, memory binding, private-by-default repos, the TruffleHog fail-closed push gate, and the read-only MCP server
- https://raw.githubusercontent.com/huggingface/funes/main/SECURITY.md - the three-layer secrets defense, the cannot-unpublish caveat, scrub, and the third-party-memory prompt-injection warning
- https://raw.githubusercontent.com/huggingface/funes-integrations/main/COMMUNITY.md - the four maintained integrations and the community OpenCode and jcode listings
- https://huggingface.co/datasets/huggingface/funes-memory - the published demo memory: 71,648 chunks, BAAI/bge-small-en-v1.5, 168 MB, 865 downloads last month, as of 2026-10-16
- https://huggingface.co/blog/funes - the 2026-09-03 announcement by David Corvoysier, the handoff-versus-recall benchmark, and the comment thread carrying deja's adversarial measurement and the maintainer's reply
- https://hn.algolia.com/api/v1/search?query=funes%20huggingface&tags=story - the footprint scan: two small threads (11 and 6 points, one comment each), September only, as of 2026-10-16
- https://raw.githubusercontent.com/TeleAI-UAGI/Awesome-Agent-Memory/main/README.md - the category's mapped source list, which does not carry funes as of 2026-10-16
