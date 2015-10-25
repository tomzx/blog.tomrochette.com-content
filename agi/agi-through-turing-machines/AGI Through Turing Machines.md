---
title: AGI Through Turing Machines
created: 2015-08-16
taxonomy:
  category: [artificial general intelligence]
  status: in progress
---

## Learned in this study

## Things to explore

# Overview

The simplest form of initial AGI software would have to be one that rewrite itself.

At the lowest level, computers are governed by a set of instructions, such as `ADD`, `SUB`, `MUL`, `DIV`, `AND`, `OR`, `MOV`, `JMP` and other similar instructions.

If we even go a level lower, we can refer to Turing machines, for which the elementary operations are moving left, moving right, reading from the current square on the tape (memory) and writing to the current square.

[A tape for data input/output, a head to read the data, a state register to store working information and and instruction table/program (describes how input data produces output data).]

The program would have to update itself during execution. However, merely updating the list/sequence of instructions of the program is not a display of intelligence.

The difficulty at this level of abstraction is that nothing will appear intelligent. Moving left/right while reading and writing symbols on a square cannot be qualified as intelligent.

Turing described a couple of instructions that are what I would consider low level intelligence. (reference?)

First, moving itself is to some degree intelligence. Without movement, change cannot occur *(although writing is also a change)*. *Left/Right movement is equivalent to moving from state A to state B (or to state C) in a state machine.*

Second, reading and writing is the second form of low level intelligence. Reading allows the agent to learn from the world while writing allows it to communicate with the world.

In itself, this basic machine can do two things:

* I/O (read/write) with a target (the tape)
* Change target (move the tape left/right, changing the cell we are interacting with)

---

The list of instruction then become a set of steps the machine will walk through. Those steps ...

---

![](images/Self_improving_machine.png)

# See also

* [Seed AI](../seed-ai)

# Sources
