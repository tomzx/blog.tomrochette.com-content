---
title: Z.ai GLM
created: 2025-12-24
---

- GLM 4.7 feels a bit less smart than Claude Sonnet 4.5
	- A bit too strict on instructions following and does not appear to think about the consequence of its changes (e.g., keep `__init__.py` files empty, ends up deleting the code in them but not updating code that may rely on what was in those files)
- More reactive to errors rather than being proactive (e.g., will try running `uv run ruff` to discover that `ruff` isn't installed)
- Speed is comparable to Claude Sonnet 4.5 and acceptable
- Code quality looks comparable to Claude Sonnet 4.5
