---
title: Quantum computing
created: 2019-12-21
taxonomy:
  type: post
  category: []
  status: draft
---

# Notes

## 0 and 1 cbits (classical bits)
$$
\left| 0 \right> =
\begin{pmatrix}
1\\
0
\end{pmatrix}
$$

$$
\left| 1 \right> =
\begin{pmatrix}
0\\
1
\end{pmatrix}
$$

* Quantum computers only use reversible operations
* Identity and Negation are reversible
* Constant-0 and Constant-1 aare not reversible

## Tensor product of vectors
$$
\begin{pmatrix}
x_0\\x_1
\end{pmatrix}
\otimes
\begin{pmatrix}
y_0\\y_1
\end{pmatrix}
=
\begin{pmatrix}
x_0
\begin{pmatrix}
y_0\\y_1
\end{pmatrix}\\x_1
\begin{pmatrix}
y_0\\y_1
\end{pmatrix}
\end{pmatrix}
=
\begin{pmatrix}
x_0y_0\\
x_0y_1\\
x_1y_0\\
x_1y_1
\end{pmatrix}
$$

$$
\begin{pmatrix}
1\\2
\end{pmatrix}
\otimes
\begin{pmatrix}
3\\4
\end{pmatrix}
=
\begin{pmatrix}
3\\
4\\
6\\
8
\end{pmatrix}
$$

# References
* https://www.youtube.com/watch?v=F_Riqjdh2oM
