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

## 2-long binary string

| string | pattern |
|--------|---------|
| 00 | repeating |
| 01 | alternating |
| 10 | alternating |
| 11 | repeating |

With two bits, we introduce two patterns: repeating and alternating. Repeating means that the bits are repeated for the complete string. Alternating means that the bits are alternating between 0 and 1 given a certain periodicity.

## 3-long binary string

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

001, 011, 100, 110 can be described as alternating and repeating, which is more complex than the previous examples as it requires the composition of two operations.

4 complex examples

## 4-long binary string

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

Here we first observe the presence of the alternating pattern with a periodicity of 2. We also observe the first case of a mirror pattern with 0110 and 1001. It could be claimed that 010 and 101 is the uneven equivalent of the mirror pattern for 3-long binary strings. The remaining "complex" examples are again displaying alternating and repeating patterns at the lower level.

One observation is that the complex patterns appear to be the variants where 1 bit is the opposite of the remaining bits, the only special case so far being for the 3-long binary string where the pattern is considered alternating. Instead of considering it a complex pattern, it could be described as the operation "fill X bits with 0/1, then flip by Y".

From those few inductive iterations, we can see that the first and last string are always the repeating pattern. We also observe that the first half of the strings exhibit the same pattern of the second half of the strings, which is expected due to the binary nature of the string.

At this point there is still not enough information to be able to derive an answer to the original question, given that the strings can be described using 4 patterns: repeating, alternating, mirror, and fill & flip.

8 complex examples

## 5-long binary string

| string | pattern |
|--------|---------|
| 00000 | repeating |
| 00001 | fill & flip |
| 00010 | fill & flip |
| 00011 | alternating, periodicity=3,2 |
| 00100 | fill & flip |
| 00101 | complex |
| 00110 | complex, or alternating, periodicity=2 |
| 00111 | alternating, periodicity=2,3 |
| 01000 | fill & flip |
| 01001 | complex |
| 01010 | alternating |
| 01011 | complex |
| 01100 | complex, or alternating, periodicity=1,2,2 |
| 01101 | complex |
| 01110 | complex, or alternating, periodicity=1,3,1 |
| 01111 | fill & flip |

The second half of this table was not written down due to the previous observation that the patterns are the same, simply inverted.

At this stage, the complex patterns that emerge are difficult to express using the prior language. Composition needs to be used, e.g. 00101 can be described as 00 then 101.

14 complex examples
