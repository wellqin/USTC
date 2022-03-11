"""
! what?
the `multiprocessing` module includes an API for 
dividing work between multiple processes based on the API for `threading`

+------------------+-----------------------------------------------------------+-----------------+
| concepts         | explanation                                               | originated from |
+==================+===========================================================+=================+
| threading        | implements concurrency thru application threads           | CPU threads     |
+------------------+-----------------------------------------------------------+-----------------+
| mutliprocessing  | implements concurrency using system processes             | System processes|
+------------------+-----------------------------------------------------------+-----------------+
| asyncio          | use a single-threaded, single-process approach            | see below       |
|                  | in which parts of an application cooperate to switch      |                 |
|                  | tasks explicitly at optimal times.                        |                 |
+------------------+-----------------------------------------------------------+-----------------+
| concurrent.      | implements thread and process-based executors             |                 |
| futures          | for managing resources pools for running concurrent tasks |                 |
+------------------+-----------------------------------------------------------+-----------------+

! why?
in some cases, `multiprocessing` is a drop-in replacement,
and can be used instead of `threading` to take advantage of multiple CPU cores
and there by avoid computational bottlenecks accociated with Python's GIL(global interpreter lock)

NOTE:
插入式替换(drop-in replacement) is a term used in computer science and other fields.
it refers to the ability to replace one hardware (or software) components with another one
w/o any other code or configuration changes being required and resulting in no negative impacts.

usually, the replacement has some benefits including one or more of the following.
- increased security
- increased speed
- increased feature set
- increased compatibility (e.g. with other components or standards support)
- increased support (e.g. the old component may no longer be supported, maintained, or manufactured)

! how?

multiprocess
|-- multiprocess Basics
|-- importable Target functions
|-- determine the current process
|-- daemon processes
|-- wait for processes
|-- terminate processes
|-- process Exit Status
|-- logging
|-- subclass process
|-- pass between processes
|-- signal between processes
|-- control access to resources
|-- synchronize operations
|-- control concurrent access to resources
|-- manage shared state
|-- shared namespace
|-- process pools
|-- implement MapReduce

"""