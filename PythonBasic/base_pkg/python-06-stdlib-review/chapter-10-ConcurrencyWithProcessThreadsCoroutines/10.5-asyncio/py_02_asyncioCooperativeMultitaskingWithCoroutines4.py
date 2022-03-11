"""
Python >= 3.5, native
    using `async def` to define a coroutine
    using `await` to yield control 

Python < 3.5,
    using `asyncio.coroutine` decorator
    using `yield from` (read this from <<fluent python>>)

same effect

"""

import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
)

# fml
@asyncio.coroutine
def outer():
    logging.debug('in outer')
    logging.debug('waiting for result1')
    # result1 = event_loop.run_until_complete(phase1())
    result1 = yield from phase1()
    logging.debug('waiting for result2')
    # result2 = event_loop.run_until_complete(phase2())
    result2 = yield from phase2(result1)
    return (result1, result2)

@asyncio.coroutine
def phase1():
    logging.debug('in phase1')
    return 'result1'

@asyncio.coroutine
def phase2(arg):
    logging.debug('in phase2')
    return 'result2 derived from {}'.format(arg)

def main():
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        logging.debug('return value: {!r}'.format(return_value))
    finally:
        """
        loop.close()
        Close the event loop.

        The loop must not be running when this function is called. 
        Any pending callbacks will be discarded.
        
        This method clears all queues and shuts down the executor, 
        but does not wait for the executor to finish.

        This method is idempotent and irreversible. 
        No other methods should be called after the event loop is closed.
        """
        event_loop.close()  # ? what would happen if i dont do this? stack overflow? leakage?

if __name__ == "__main__":
    main()