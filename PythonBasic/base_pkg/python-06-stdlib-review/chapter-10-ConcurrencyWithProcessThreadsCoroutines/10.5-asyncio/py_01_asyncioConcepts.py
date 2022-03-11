"""
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

"""
