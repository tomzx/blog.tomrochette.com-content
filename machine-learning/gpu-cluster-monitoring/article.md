---
title: GPU cluster monitoring
created: 2025-07-06
taxonomy:
  type: post
  status: draft
  tag: [Machine learning]
---

In this article I list the various metrics one should have when monitoring a GPU cluster to ensure efficient usage.

* Allocated GPUs are used
  * Used to detect jobs that may ask multiple GPUs but end up using 1 or only a few of them
* GPU utilization below threshold (e.g., 10%)
  * Used to detect workloads that do not make full use of the GPU or are allocated to an oversized GPU
* GPU utilization above threshold (90%)
  * Used to detect when GPU is saturated
* GPU memory utilization above threshold (e.g., 10%)
  * Used to detect workloads that do not make full use of the GPU or are allocated to an oversized GPU
* GPU memory utilization above threshold (e.g., 95%)
  * Used to detect when a job is about to run out of GPU memory