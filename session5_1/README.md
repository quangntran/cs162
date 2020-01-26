## Design Patterns - Template

### Template - Queue
Read up on the implementation of the various Python Queue classes:
https://github.com/python/cpython/blob/3.5/Lib/queue.py
Don't pay too much attention to the low-level details, instead focus on the
high-level design of the three classes in that file.

In particular, notice how the `PriorityQueue` and `LifoQueue` have been
implemented.  This should highlight the power of a good design using object-
oriented techniques.

### Template - Simulation

The template design pattern is a powerful design pattern that usually forms the
basis of most frameworks.  In `template.py` a simple simulation framework is
given.  (Notice that the `AbstractSimulation` class doesn't need to know
anything about the `CannonBall` class, which inherits from
`AbstractSimulation`.)

### Template - unittest
A very useful framework that has been built into the python libraries itself
is `unittest`.  This module builds a simple framework for testing code.
One does this by writing small examples where one knows the input, as well as
what the output should be.  Creating many such different tests (each test
testing a different aspect of functionality) makes it very easy to detect
when a bug has been introduced.  One should just get into the habit of writing
tests with the functionality that you are developing, and one must also run
those tests before pushing any new features live.

*Unit testing is very important and will be fully covered in a later unit which
focuses on the automated testing and deployment of a system. You are still
encouraged to write unit tests for your project in the meantime!*

## Questions
**Bring both your code, and the output from running your code, to class.**

1. Explain the difference between a normal queue, a priority queue, and a LIFO
queue.  Give a real-world example where one might find each type of queue.

2. Create your own python file `rule90.py` and import the `AbstractSimulation`
from `template.py`.  Now write an implementation of Wolfram's Rule 90 cellular
automaton.  Further details on Rule 90 can be found at:
https://en.wikipedia.org/wiki/Rule_90
Your implementation must inherit from `AbstractSimulation`, and should be
runnable using the `run()` method. If it simplifies your code, then you can
assume a finite-sized list of automata.  You can also choose the simplest
initialization for your automaton.

3. Using your code from the previous session on creating a `ClockIterator`,
write test code for the situations given below.
    1. The first thing returned from a `ClockIterator` should be the string  "00:00".
    2. The 60th thing returned  from a `ClockIterator` should be the string "00:59".
    3. The 61st thing returned  from a `ClockIterator` should be the string "01:00".
    4. The 1440th thing returned  from a `ClockIterator` should be the string "23:59".
    5. The 1441st thing returned  from a `ClockIterator` should be the string "00:00".

4. Think about the subsystem for the final project that you are working on.  
What unit tests could you write to test the functionality of that system.  
Remember to keep the tests as small and targeted as possible!  Write up a short
description of those tests and bring them to class in a format suitable for
pasting in a google doc.

5. (Optional) The queue class is thread safe.  Search the internet to find out
what this means.  What is required to make `put()` and `get()` thread safe?
