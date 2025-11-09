---
title: Gitlab SSH post-quantum key exchange
created: 2025-11-08
taxonomy:
  type: post
  status: finished
  tag: [gitlab, ssh, post-quantum-cryptography, pqc, security]
---

A small PSA for Gitlab users who use SSH to connect to their Git repositories, if you get the following warning when trying to connect:

```
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
```

You should upgrade your Gitlab instance.
