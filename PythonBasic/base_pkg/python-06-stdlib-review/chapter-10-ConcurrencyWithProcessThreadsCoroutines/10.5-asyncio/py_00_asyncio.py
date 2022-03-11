"""
! what?
asyncio module provides tools for building concurrent applications using coroutines.
while the `threading` module implements concurrency through application threads, and `multiprocessing`
implements concurrency using system processes.

asyncio uses a single-threaded, single-process approach in which parts of an application
cooperate to switch tasks explicitly at optimal times.

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
a chess genius is gonna play with 10 people. one game takes around 3 hours.
the game host wanna terminate these chess games in one day.
what is your solution in this case?

illustration as follows.
            3   
        2       4
    1               5
0        genius         6
                    7
        10      8
            9

            
! how?

asyncio

mechanism
The mechanism for yielding control back to the event loop depends on Python’s coroutines, 
special functions that give up control to the caller without losing their state.

Coroutines are quite similar to generator functions; in fact, generators can be used to implement
coroutines in versions of Python earlier than 3.5 without native support for coroutine objects.

生产计划员
`asyncio` also provides a class-based abstraction layer for protocols and transports for
writing code using callbacks instead of writing coroutines directly.

生产计划
A `future` is a data structure representing the result of work that has not been completed
yet. The event loop can watch for a Future object to be set to done, thereby allowing one
part of an application to wait for another part to finish some work. Besides futures, asyncio
includes other concurrency primitives such as locks and semaphores.

A `Task` is a subclass of Future that knows how to wrap and manage the execution of a
coroutine. An event loop schedules tasks to run when the resources they need are available,
and to produce a result that can be consumed by other coroutines.


asyncio: Asynchronous I/O, Event Loop, and Concurrency Tools
|-- Asynchronous Concurrency Concepts
|-- Cooperative Multitasking with Coroutines
|-- Scheduling Calls to regular functions
|-- Producing Results Asynchronously
|-- Executing Tasks Concurrently
|-- Composing Coroutines with Control Structures
|-- Synchronization Primitives
|-- Asynchronous I/O with Protocol Class Abstractions
|-- Asynchronous I/O using coroutines and streams
|-- Using SSL
|-- Interacting with Domain Name Services
|-- Wokring with Subprocesses
|-- Receiving Unix Signals
|-- Combining Coroutines with Threads and Processes
|-- Debugging with asyncio

"""
