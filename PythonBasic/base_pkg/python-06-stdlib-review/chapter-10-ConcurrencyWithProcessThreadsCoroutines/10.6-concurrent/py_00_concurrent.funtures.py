"""
! what?
the concurrent.future module provides interfaces for 
running tasks using pools of `thread` or `process` workers.

The APIs are the same for both options,
so applications can switch between threads and processes with minimal changes

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
N/A stfu

! how?
concurrent.futures provides two types of classes for interacting with the pools.
`Executors` are used for managing pools of workers
`futures` are used for managing results computed by the workers

To use a pool of workers, 
an appication creates an instance of the appropriate executor class
and the submits tasks for it to run.

when each task is started, a `Future` instance is returned.
when the result of the task is needed, an application can use the `Future` to block unitl the result becomes available.

various APIs are provided that make it convient to wait for tasks to complete.
so `Future` objects do not need to be managed directly.

concurrent.futures
|-- use map() with a Basic thread pool
|-- schedule individual tasks
|-- wait for tasks in any order
|-- future callbacks
|-- cancel tasks
|-- exceptions in tasks
|-- context manager
|-- process pools

higher level than `threading` and `multiprocessing`
"""