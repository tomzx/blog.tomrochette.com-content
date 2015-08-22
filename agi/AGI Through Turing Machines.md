# AGI Through Turing Machines

The simplest form of initial AGI software would have to be one that rewrite itself.

At the lowest level, computers are governed by a set of instructions, such as ADD, SUB, MUL, DIV, AND, OR, MOV, JMP and other similar instructions.

If we go even a level lower, we can refer to Turing machines, thus the elementary operations are moving left, moving right, reading from the current square on the tape (memory) and writing to the current square.

[A tape for data input/output, a head to read the data, a state register to store working information and and instruction table/program (describes how input data produces output data).]

Thus, the program would have to update itself during execution. However, merely updating the list/sequence of instructions of the program is not a display of intelligence.

The difficulty at this level of abstraction though is that nothing will appear intelligent. Moving left/right while reading and writing symbols on a square cannot display anything that would be qualified as intelligent.

Turing described a couple of instructions that are what I would consider low level intelligence.

First, moving itself is to some degree intelligence. Without movement, change cannot occur (although writing is also a change). *Left/Right movement is equivalent to moving from state A to state B (or to state C) in a state machine.*

Second, reading and writing is the second form of intelligence. Reading allows the agent to learn from the world while writing allows it to communicate with the world.

In itself, this basic machine can do two things:

* I/O with a target
* Change target

---

The list of instruction then become a set of steps the machine will walk through. Those steps ...