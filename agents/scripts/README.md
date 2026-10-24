# agents/scripts - preprocessing helpers

Small, standalone Python scripts that fetch data from the sites the agents
section scans regularly and emit compact, structured output (JSON or plain
text). Use them instead of reading full pages or API responses in a worker,
so an agent processes only the facts it needs.

All scripts print a one-line summary on stderr and write their payload to
stdout (or `--out FILE`). They use `gh` (authenticated) for GitHub and
`urllib` for everything else, and need no extra dependencies.

## Scripts

- `fetch_stars.py` - owner's GitHub stars newer than a checkpoint
  (`agents/starred-checkpoint.txt`), compact JSON. Stops paging once it
  reaches the checkpoint.
- `fetch_repo_state.py` - batched `pushed_at`, star count, open issues,
  archived flag, and latest release tag/date for a list of repos.
- `extract_awesome_list.py` - fetches an awesome list's README and emits
  the GitHub repos it links, with titles and one-line descriptions.
- `fetch_url_text.py` - fetch any URL, strip HTML, collapse whitespace,
  truncate. `--extract prices` keeps only price-bearing sentences.

## Typical use

```sh
# New stars since the last run:
agents/scripts/fetch_stars.py --checkpoint agents/starred-checkpoint.txt \
  --write-checkpoint /tmp/new-checkpoint.txt

# State of every subject repo in a category:
agents/scripts/fetch_repo_state.py --file /tmp/repos.txt --out /tmp/state.json

# Entries in an awesome list, minus already-known repos:
agents/scripts/extract_awesome_list.py VoltAgent/awesome-agent-skills \
  --exclude /tmp/known-repos.txt

# Condensed pricing page:
agents/scripts/fetch_url_text.py https://example.com/pricing --extract prices
```

## Conventions

- Output is compact JSON (no spaces) or plain text, one payload per run.
- Nothing here writes under `agents/` except via explicit `--out`; the
  coordinator owns shared files.
- Scripts are read-only with respect to the repository.
