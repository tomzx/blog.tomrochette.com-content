---
title: Tensorflow
created: 2016-01-27
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

Tensorflow has rapidly grown in popularity due to the fact that is developed/supported by Google. As more and more developers move to the platform, it becomes essential to learn how it works and have a general idea of the various concepts it makes use of. This is a short article about some of these concepts.

## Learned in this study

## Things to explore

# Overview

* Computations are represented as graphs
* Graphs are executed in the context of `Sessions`

# Building a graph
* Start with ops that do not need any input (called `source ops`), such as `Constant`

# Session
* Graphs are executed within a session (context)
	`session = tf.session()`
* Sessions are given one or many tensor to resolve
	`session.run([tensorA, tensorB])`
* Once we're done with a session, it should be closed
	`session.close()`

# Tensors
**Rank:** The number of dimensions of a tensor.

| Rank | Math entity | Example |
|------|-------------|---------|
| 0    | Scalar      | s = 483 |
| 1    | Vector      | v = [1.1, 2.2, 3.3] |
| 2    | Matrix      | m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] |
| 3    | 3-Tensor    | t = [[[2], [4], [6]], [[8], [10], [12]], [[14], [16], [18]]] |

**Shape:** A vector describing the number of elements at each point within a dimension.

| Rank | Shape | Dimension number | Example |
|------|-------|------------------|---------|
| 0    | [] | 0-D | A 0-D tensor. A scalar. |
| 1    | [D0] | 1-D | A 1-D tensor with shape [5] = [1, 2, 3, 4, 5]. |
| 2    | [D0, D1] | 2-D | A 2-D tensor with shape [3, 4] = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]. |
| 3    | [D0, D1, D2] | 3-D | A 3-D tensor with shape [1, 4, 3] = [[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]]. |
| n    | [D0, D1, ..., Dn] | n-D | A tensor with shape [D0, D1, ... Dn]. |

**Type:** Type of the data contained within the tensor.

| Data type | Description |
|-----------|-------------|
| DT_FLOAT | 32 bits floating point. |
| DT_DOUBLE | 64 bits floating point. |
| DT_INT64 | 64 bits signed integer. |
| DT_INT32 | 32 bits signed integer. |
| DT_INT16 | 16 bits signed integer. |
| DT_INT8 | 8 bits signed integer. |
| DT_UINT8 | 8 bits unsigned integer. |
| DT_STRING | Variable length byte arrays. Each element of a Tensor is a byte array. |
| DT_BOOL | Boolean. |
| DT_COMPLEX64 | Complex number made of two 32 bits floating points: real and imaginary parts. |
| DT_QINT32 | 32 bits signed integer used in quantized Ops. |
| DT_QINT8 | 8 bits signed integer used in quantized Ops. |
| DT_QUINT8 | 8 bits unsigned integer used in quantized Ops. |

# Variables
* Variables must be initialized (`tf.initialize_all_variables()`)
* Initialization is an operation, and thus must be executed within a session

# Fetches
* All the ops needed to produce the values of requested tensors are run once (not once per requested tensor)

# Feeds
* Temporarily replaces the output of an operation with a tensor value (act as a placeholder)
* The feed data is provided as an argument to a `session.run()` call
	`sess.run([output], feed_dict={input1:[7.], input2:[2.]})`

# See also

# Sources

* https://www.tensorflow.org/
* https://medium.com/jim-fleming/loading-tensorflow-graphs-via-host-languages-be10fd81876f
