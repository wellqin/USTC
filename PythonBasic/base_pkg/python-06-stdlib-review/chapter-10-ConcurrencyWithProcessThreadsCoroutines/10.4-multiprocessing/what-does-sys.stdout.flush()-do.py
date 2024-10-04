"""
Q: wtf does sys.stdout.flush() do?

A: geeksforgeeks explanation
link: https://www.geeksforgeeks.org/python-sys-stdout-flush/

A data buffer is a region of physical memory storage use to temporarily store data 
when it is being moved from one place to another.

The data is stored in a buffer as it is retrieved from an input device 
or just before it is sent to an output device 
or when moving data between processes with a computer.

Python's standard out is buffered.
This means that it collects some data before it is written to standard out
and when the buffer gets filled, then it is written on the terminal or any other output stream.


+---------------+-------------+
|               | has buffer? |
+===============+=============+
| sys.stdout    | Yes         |
+---------------+-------------+
| sys.stderr    | No          |
+---------------+-------------+
| sys.stdin     | Yes         | @https://stackoverflow.com/questions/37726138/disable-buffering-of-sys-stdin-in-python-3
+---------------+-------------+

"""

import time, sys


"""
when the snippet is executed, then the numbers from 0 to 9 are printed 
after every second on a new line.
i.e., the output is automatically flushed out.

This is because, by default `end` parameter of print statement is set to "\n"
which flushes the output.

"""
for i in range(10):
    print(i)
    sys.stdout.flush()
    time.sleep(1)


"""
the following example shows, if we change the default behavior of `end` argument,
after 10 seconds, 0-9 are suddently comes out

this is because the output is buffered and it is not flushed by any means.
"""
for i in range(10):
    print(i, end='-')
    time.sleep(1)

"""
so, using sys.stdout.flush() to forcibly flush out buffer.
"""

for i in range(10):
    print(i, end='-')
    sys.stdout.flush()
    time.sleep(1)