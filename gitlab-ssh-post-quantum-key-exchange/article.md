---
title: Gitlab SSH post-quantum key exchange
created: 2025-11-08
taxonomy:
  type: post
  status: finished
  tag: [gitlab, ssh, post-quantum-cryptography, pqc, security]
  readability: 3
---

A small PSA for Gitlab users who use SSH to connect to their Git repositories.
If you get the following warning when trying to connect:

```
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
```

You should upgrade your Gitlab instance to the latest.
If you need to upgrade, you can use Gitlab's [upgrade path tool](https://gitlab-com.gitlab.io/support/toolbox/upgrade-path) which is very helpful to identify the correct upgrade steps to take.

You may also have to upgrade your operating system.
In my case I was still on Ubuntu 20.04 LTS it did not support post-quantum key exchange.

Note that if you do a release upgrade, you also should update the apt sources to point to the new release (e.g., going from focal to jammy) and upgrade gitlab using the updated source.
