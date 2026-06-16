---
title: "slack-cached - Cache Slack threads, channels, and users to a local SQLite database"
created: 2026-06-16
type: post
status: finished
tags: [python, slack, cli, developer-tools, sqlite, fully-ai-generated, llm=glm-5.2]
readability: 4
audience_notes: >
  Assumes the reader is a developer comfortable with the CLI, SQLite, and Slack concepts like channels and threads. Modeled on the existing gh-cached post on this blog.
---

Slack is where your team's decisions live, but the data doesn't belong to you.
Search is slow, threads scroll into oblivion, and the moment you leave a workspace the history is gone.
There's no official CLI, and the web client is the only first-class way to read anything.

I built [slack-cached](https://github.com/TomzxCode/slack-cached) to fix this.
It's a small Python CLI that caches Slack threads, channel messages, users, and channels to a local SQLite database.
Once cached, the data is yours: query it with SQL, grep it, feed it to an LLM, or just read it offline.

## The problem

Slack makes exporting and archival surprisingly hard.
Export tools exist for admins, but most members aren't admins.
The search box returns messages, but not in a form you can slice, join, or version.
Important decisions get buried in threads that nobody scrolls back to.

This gets worse when you want to do anything programmatic.
Building a knowledge base, summarizing a channel, or tracking decisions all require raw access to the messages.
Hitting the Slack API on demand works, but you pay the latency and rate-limit cost every time, and edits disappear if you only ever fetch live.

## How slack-cached works

```bash
$ uv sync
$ uv run slack-cached --help
usage: slack-cached [-h] {fetch,show,fetch-users,fetch-channels,show-users,show-channels,poll} ...

Cache Slack threads to a local SQLite database.
```

Cache a thread from a URL (no stdout, just a one-line summary on stderr):

```bash
$ slack-cached fetch https://acme.slack.com/archives/C0123ABCDEF/p1700000000123456
cached 3 messages (3 new/updated, full) for C0123ABCDEF/1700000000.123456
```

Or by explicit channel and timestamp; run it again and it only asks Slack for what changed:

```bash
$ slack-cached fetch --channel C0123ABCDEF --ts 1700000000.123456
cached 3 messages (3 new/updated, full) for C0123ABCDEF/1700000000.123456

$ slack-cached fetch --channel C0123ABCDEF --ts 1700000000.123456   # run again
cached 4 messages (1 new/updated, incremental) for C0123ABCDEF/1700000000.123456
```

Read it back, human-readable by default:

```bash
$ slack-cached show https://acme.slack.com/archives/C0123ABCDEF/p1700000000123456
Thread C0123ABCDEF/1700000000.123456
3 message(s)

[2023-11-14T22:13:20+00:00] Alice Smith (alice)
    Has anyone tried the new deploy script?

[2023-11-14T22:15:12+00:00] Bob Lee (bob)
    Yes, but you need to bump the token first.

[2023-11-14T22:16:45+00:00] Alice Smith (alice)
    Thanks!
```

`show` auto-fetches if the thread isn't cached yet, and renders real names like `Alice Smith (alice)` instead of raw user ids once you've cached users.
Pass `--json` to get the raw records for piping into other tools:

```bash
$ slack-cached show --json https://acme.slack.com/archives/C0123ABCDEF/p1700000000123456
{
  "channel": "C0123ABCDEF",
  "channel_name": "deploys",
  "thread_ts": "1700000000.123456",
  "message_count": 3,
  "messages": [
    {
      "ts": "1700000000.123456",
      "user": "U1",
      "text": "Has anyone tried the new deploy script?",
      "payload": { "ts": "1700000000.123456", "user": "U1", "type": "message" },
      "user_name": "Alice Smith (alice)"
    },
    {
      "ts": "1700000112.000200",
      "user": "U2",
      "text": "Yes, but you need to bump the token first.",
      "payload": { "ts": "1700000112.000200", "user": "U2", "type": "message" },
      "user_name": "Bob Lee (bob)"
    },
    {
      "ts": "1700000205.500300",
      "user": "U1",
      "text": "Thanks!",
      "payload": { "ts": "1700000205.500300", "user": "U1", "type": "message" },
      "user_name": "Alice Smith (alice)"
    }
  ]
}
```

## Channels, users, and polling

Cache every top-level message in a channel:

```bash
$ slack-cached fetch --channel C0123ABCDEF
cached 142 messages for C0123ABCDEF (38 fetched)
```

Add `--full-threads` to also pull every reply thread, so you get the full conversation tree:

```bash
$ slack-cached fetch --channel C0123ABCDEF --full-threads
cached 318 messages for C0123ABCDEF (214 fetched, 47 threads with replies fetched)
```

For continuous capture, `poll` watches multiple channels and fetches new messages on a schedule.
Progress goes to stderr, and (because of `--json`) one compact JSON object per cycle goes to stdout. `Ctrl+C` stops it gracefully:

```bash
$ slack-cached poll --channels C001,C002,C003 --interval 5m --last 5m --full-threads --json
polling 3 channel(s) every 5m (lookback: 5m, full_threads: True, concurrency: 3)
{"cycle": 1, "elapsed_seconds": 1.234, "channels": [{"channel": "C001", "fetched": 3, "total": 312}, {"channel": "C002", "fetched": 4, "total": 188}, {"channel": "C003", "fetched": 0, "total": 27}]}
cycle 1: 7 new message(s) across 3 channel(s) in 1.2s
^C
poll stopped after 1 cycle(s)
```

That stdout stream is easy to wire into a downstream pipeline or a knowledge-base builder.

Finally, cache the workspace's users and channels so threads can be rendered with real names:

```bash
$ slack-cached fetch-users
processed 184 users (184 added, 184 total in db)
$ slack-cached fetch-channels
processed 37 channels (37 added, 37 total in db)
```

```bash
$ slack-cached show-users
184 user(s)

U1  alice - Alice Smith
U2  bob - Bob Lee
...
```

```bash
$ slack-cached show-channels --json
{
  "channel_count": 37,
  "channels": [
    {
      "id": "C1",
      "name": "general",
      "is_private": false,
      "fetched_at": 1700000260.0,
      "payload": { "id": "C1", "name": "general", "is_channel": true }
    },
    ...
  ]
}
```

## The refresh strategy

`fetch` always reaches out to Slack, but it's incremental.
On a re-fetch, it calls `conversations.replies` with `oldest=<latest_cached_ts>`, so the API returns only new replies and any edits at the boundary.
Messages are upserted by `ts`, which means edits replace the old text in place instead of creating duplicates.

Rate limits are handled for you.
HTTP 429 / `ratelimited` responses are retried with exponential backoff, up to five attempts, respecting the `Retry-After` header.
That matters for `--full-threads` and `poll`, where you can easily fire hundreds of calls against a busy channel.

## Where the cache lives

The database defaults to `$XDG_CACHE_HOME/slack-cached/threads.db` (typically `~/.cache/slack-cached/threads.db`).
Override it per command with `--db /path/to/file.db`.
Because it's plain SQLite, you can open it directly and ask it anything Slack's search box can't:

```bash
$ sqlite3 ~/.cache/slack-cached/threads.db \
    "SELECT (u.real_name || ' (' || u.name || ')') AS who, COUNT(*) AS msgs
     FROM messages m JOIN users u ON m.user = u.id
     WHERE m.channel = 'C0123ABCDEF'
     GROUP BY who ORDER BY msgs DESC LIMIT 5;"
Alice Smith (alice)|142
Bob Lee (bob)|87
Carol Ng (carol)|53
```

That's the real point of the tool.
The cache is not an opaque blob; it's a table of messages you can `SELECT` from, join against users and channels, and export however you like.

## Authentication

Credentials load from environment variables first, then a config file at `$XDG_CONFIG_HOME/slack-cached/config`:

```ini
SLACK_TOKEN=xoxb-...
SLACK_COOKIE=...
SLACK_API_BASE_URL=https://slack.com/api
```

`SLACK_COOKIE` is there for `xoxc-` web-client tokens, which need the matching cookie to authenticate.
Every command also accepts `--api-base-url`, which is how the built-in fake Slack server plugs in.

## A fake Slack server, for free

The repo ships `slack-fake-server`, a deterministic fake Slack API for testing:

```bash
$ uv run slack-fake-server --port 8199 --num-threads 50 --rate-limits
2026-06-15T12:00:00Z [info     ] fake_slack_server_starting   host=127.0.0.1 port=8199 seed=42 users=8 channels=5 threads=50 rate_limits=True
```

It serves `conversations.list`, `conversations.replies`, `conversations.history`, and `users.list`, and can simulate Slack-tier rate limiting.
Point slack-cached at it and you can develop and test against a realistic API without touching your real workspace:

```bash
$ slack-cached fetch --api-base-url http://localhost:8199/api --channel C0123ABCDEF --full-threads
cached 318 messages for C0123ABCDEF (214 fetched, 47 threads with replies fetched)
```

## When this is useful

- **Knowledge bases and channel summaries.** Poll a set of channels, then build monthly digests or feed the SQLite cache to an LLM.
- **Decision tracking.** Important calls often happen in threads. Cache them so they survive workspace churn and account turnover.
- **Offline access and archival.** Keep a readable copy of the conversations you actually care about, independent of Slack's retention window.
- **Bulk analysis.** Once the data is in SQLite, you can answer questions with a query that Slack's search box can't express.

## Try it

```bash
$ git clone https://github.com/TomzxCode/slack-cached
$ cd slack-cached
$ uv sync
$ export SLACK_TOKEN=xoxb-...
$ slack-cached fetch-channels
processed 37 channels (37 added, 37 total in db)
$ slack-cached fetch --channel C0123ABCDEF --full-threads
cached 318 messages for C0123ABCDEF (214 fetched, 47 threads with replies fetched)
$ slack-cached show https://acme.slack.com/archives/C0123ABCDEF/p1700000000123456
Thread C0123ABCDEF/1700000000.123456
3 message(s)

[2023-11-14T22:13:20+00:00] Alice Smith (alice)
    Has anyone tried the new deploy script?

[2023-11-14T22:15:12+00:00] Bob Lee (bob)
    Yes, but you need to bump the token first.

[2023-11-14T22:16:45+00:00] Alice Smith (alice)
    Thanks!
```

[Repository and source code](https://github.com/TomzxCode/slack-cached), [documentation](https://tomzxcode.github.io/slack-cached/docs).


## References

- [TomzxCode/slack-cached README](https://github.com/TomzxCode/slack-cached) -- primary source for features, commands, and behavior.
- [slacrawl](https://github.com/openclaw/slacrawl) -- related prior art referenced by the project.
