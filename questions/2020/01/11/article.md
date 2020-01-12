---
title: Storing and updating large amount of data
created: 2020-01-11
taxonomy:
  type: post
  category: [Questions]
  status: finished
---

# Question
How can you efficiently store terabytes of data, with hundreds of gigabytes updated daily?

# Answer
This question comes from the idea that if we wanted to implement an artificial intelligence, it would have to be able to process a large amount of data, similar to how we need to process a stream of sensorial (sight, hearing, tasting, touch, smell) inputs actively more than 12 hours per day.

Assuming someone starts when an empty storage data could simply be added sequentially to the storage space. During downtime, a period of low necessity to write to the storage space, a second process could go through the existing data in order to detect duplication and to compress it.

A simple strategy could be to split the existing storage space in two and see whether the two parts are the same. If they are, then you can reduce the storage space by half. If that is not the case (which is highly likely), then the first and second parts are split in half again. This is a basic divide-and-conquer approach. Assuming that we're storing at a byte level, we would then use the blocks 2, 3 and 4 and compare them against block 1, block 2 with 3 and 4, block 3 with 4. This process can be repeated until we reach the single byte level, at which point it is not very useful anymore.

This approach as many weaknesses:
* It compares block of same sizes only, which means it cannot find a smaller block within a larger block and replace it with a common reference.
* It only compares aligned blocks, that means that if block 1 could be found as part of blocks 2 and 3, it will not find that match.

Given that we now have numerous compression algorithms available, it would be more sensible to rely on one of them.
