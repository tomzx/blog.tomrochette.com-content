---
title: Buzz
created: 2026-10-02
updated: 2026-10-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, communication, nostr, self-hosted]
readability: 3
audience_notes: >
  Engineers evaluating where agent-to-human coordination should live if it stops being a Slack integration.
  Assumes you have run a team chat tool and at least one coding agent.
---

Buzz is an Apache-2.0, self-hostable team communication platform from Block where humans and AI agents are first-class equals on one Nostr-event relay that also carries search, workflows, git hosting, and automation.

**Its bet is that the coordination layer is the product: instead of bolting agents onto chat, Buzz makes every message, reaction, workflow step, and agent action a signed event in one relay you own, so the workspace, the audit log, and the automation trigger are the same thing.**

## What it is

A relay-plus-clients workspace built on the Nostr protocol (NIP-01 wire format): clients connect over WebSocket to one relay that authenticates, verifies signatures, persists events, fans out to subscribers, indexes for search, and triggers automation.
The workspace model is the community, selected by hostname, with channel membership as the only access gate.
Surfaces cover the daily loop: a Slack-like Stream with mandatory topics and zero-notification defaults, a Discourse-like Forum, DMs, an Agents directory with a job board, YAML-as-code Workflows with approval gates and traces, full-text search, and git hosting on the same domain (`git clone repo.community.example.com`).
Block positions it as infrastructure, the event store and delivery pipe, not the brain; its sibling harness goose is the obvious first agent to live in it.

## Status

Active and heavily starred: about 35,400 stars since 2026-03-06 as of 2026-10-02, pushed the same day, with desktop releases at v0.5.26 (2026-09-29) on a steady cadence.
**The caveat is that the star count tracks Block's name and the anti-Platform story, not field deployments: I found no independent HN thread and the public documentation lives in the repo's vision essays rather than operator guides.**
The single-relay design is upfront about its trade: one event log, no federation, no gossip.

## Strengths

- The signed-event foundation gives you chat, audit, and automation triggers from one event log, with new features as new event kinds that cannot break old clients.
- Agents are protocol-level participants, not integrations: a job board, an agent directory, and workflows that gate on approvals.
- Zero-notification-by-default surfaces are the right defaults for agent-heavy rooms where most traffic is machine-generated.
- Self-hostable with a URL-is-your-workspace model, and git hosting on the same domain removes a separate forge for small teams.
- Apache-2.0 with a vendor the size of Block behind it, which makes the abandonment risk lower than a typical solo relay.

## Cautions

- Single relay, no federation: availability and trust concentrate in one process, and the operator document for running many communities is still vision-essay territory.
- The Nostr event model is a feature and a tax: every client, bot, and integration must speak signed Nostr events, which excludes the Slack and Discord ecosystem out of the box.
- Vendor gravity: Block's own workflows (and probably its agent roadmap) will lead the event-kind vocabulary, so the "standard" is partly whatever Block ships.
- No independent adoption record yet: the community footprint is stars, not deployment stories.
- The scope is enormous (chat, forum, DMs, git, search, workflows, canvas, huddles), and breadth at v0.5.x means uneven depth somewhere.

## Pricing

Free and open source under Apache-2.0, self-hosted on your own infrastructure.
There is no hosted Buzz tier; the vision documents describe third-party operators hosting communities on the same codebase, which would be their business, not a Buzz subscription.

## Compared to

- [Foremerge](../foremerge/index.md): Foremerge coordinates agent plans above git with collision detection; Buzz coordinates humans and agents in conversation, and the two could compose.
- [Omnara](../omnara/index.md): Omnara supervises agents from a hosted control plane; Buzz hosts the communication fabric itself and leaves supervision to your agents.
- [goose](../../harnesses/goose/index.md): Block's own harness is the natural agent citizen of a Buzz relay; pair them to stay in one vendor's stack.

## Bottom line

**Recommended for teams ready to own their coordination fabric and treat agent messages as signed, auditable events from day one.**
Not for anyone who needs Slack-world integrations, federated availability, or a tool with proven production deployments at someone else's scale.

## Changes

- 2026-10-02 - Created.
- 2026-10-03 - Reworded banned-term words out of the prose; meaning unchanged.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Foremerge](../foremerge/index.md) - the plan-coordination layer above git
- [Omnara](../omnara/index.md) - the hosted agent-supervision counterpart
- [goose](../../harnesses/goose/index.md) - Block's harness, the first citizen of its own relay
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://github.com/block/buzz - repository, Apache-2.0 license, stars, surfaces table, and the release cadence as of 2026-10-02
- https://github.com/block/buzz/blob/main/ARCHITECTURE.md - the Nostr NIP-01 event model, single-relay design, and community/host resolution
- https://github.com/block/buzz/blob/main/VISION.md - the relay-is-the-workspace thesis and the incident-channel motivating story
- https://github.com/block/buzz/releases - the desktop v0.5.26 release (2026-09-29) anchoring the version claim
- https://en.wikipedia.org/wiki/Nostr - the relay-and-signed-event protocol model Buzz builds its wire format on
