"""
! what?
threading module provides APIs for managing several threads of execution,
which allows a program to run multiple operations concurrently in the same process space.

NOTE: to be fair, the concept of threading is rather abstract.
i remember i saw a vid about this in YT

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

! how?


threading
|-- thread objects
|-- determine the current thread
|-- daemon versus non-daemon threads
|-- enumerate all threads
|-- subclass thread
|-- timer threads
|-- signal between threads
|-- control access to resource
|-- synchronize threads
|-- limit concurrent access to resources
|-- thread specific data

"""