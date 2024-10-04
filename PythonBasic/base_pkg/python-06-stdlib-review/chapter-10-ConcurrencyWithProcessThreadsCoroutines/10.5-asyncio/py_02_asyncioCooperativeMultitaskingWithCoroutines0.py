"""

Coroutines are a language construct designed for concurrent operation. 

A coroutine function creates a coroutine object when called, 
and the caller can then run the code of the function using the coroutine’s `send()` method.

A coroutine can pause execution using the `await`keyword with another coroutine. 
While it is paused, the coroutine’s state is maintained,
allowing it to resume where it left off the next time it is awakened.

"""