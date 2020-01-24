---
title: Complex and unpredictable binary strings
created: 2020-01-23
taxonomy:
  type: post
  category: [Questions, Computer Science]
  status: finished
---

# Question
What is the most complex sequence that can be made from a n-long binary string?

# Answer
0....0 and 1....1 are easily compressible, thus what is the most unpredictable sequence?

Let's proceed by induction.
0, 1 - 0 and 1 have a 50% to be selected in a 1-long binary string, thus they are the most complex examples of a 1-long binary string.

| string | pattern |
|--------|---------|
| 00 | repeating |
| 01 | alternating |
| 10 | alternating |
| 11 | repeating |

00, 01, 10, 11 - 00, 11 are repeating. 01, 10 are alternating.

| string | pattern |
|--------|---------|
| 000 | repeating |
| 001 | complex |
| 010 | alternating |
| 011 | complex |
| 100 | complex |
| 101 | alternating |
| 110 | complex |
| 111 | repeating |

000, 001, 010, 011, 100, 101, 110, 111 - 000, 111 are repeating. 010, 101 are alternating. 001, 011, 100, 110. Those values can be described as alternating and repeating, which is more complex than the previous examples as it requires the composition of two operations.

| string | pattern |
|--------|---------|
| 0000 | repeating |
| 0001 | complex |
| 0010 | complex |
| 0011 | alternating, periodicity=2 |
| 0100 | complex |
| 0101 | alternating, periodicity=1 |
| 0110 | mirror |
| 0111 | complex |
| 1000 | complex |
| 1001 | mirror |
| 1010 | alternating, periodicity=1 |
| 1011 | complex |
| 1100 | alternating, periodicity=2 |
| 1101 | complex |
| 1110 | complex |
| 1111 | repeating |

0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111 - 0000, 1111 are repeating, 0101, 1010 are alternating with periodicity 1, 0011, 1100 are alternating with periodicity 2. 0110, 1001, are mirrored (from the middle). 0001, 0010, 0100, 0111, 1000, 1011, 1101, 1110 are again composed, at the lower level, of repeating and alternating.

One observation is that the complex patterns appear to be the variants where 1 bit is the opposite of the remaining bits, the only special case so far being for the 3-long binary string where the pattern is alternating. However, in this specific case, the operation could be simply "fill X bits with 0/1, then flip by Y".
