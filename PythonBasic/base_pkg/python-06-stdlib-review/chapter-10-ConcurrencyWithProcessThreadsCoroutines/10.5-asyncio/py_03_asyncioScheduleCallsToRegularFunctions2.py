"""
Table: difference between asyncio.get_event_loop.call_soon() and asyncio.get_event_loop.call_later()

+---------------+------------------------------------------------+---------------------------------------------------------------------------+
| diff          | call_soon()                                    | call_later()                                                              |
+===============+================================================+===========================================================================+
| args          | Any extra position args after the function     | the 1st arg to this method is the delay in seconds,                       |
|               | are passed to the callback when it's invoked   | the 2nd arg is th callback, any args after callback is passed to callback |
+---------------+------------------------------------------------+---------------------------------------------------------------------------+
| kwargs        | to pass keyword args to the callback,          |                                                                           |
|               | use `partial()`                                |                                                                           |
+---------------+------------------------------------------------+---------------------------------------------------------------------------+


"""


import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_call_later():
    def callback(n):
        logging.debug(f'callback {n} invoked')

    async def main_job(loop):
        logging.debug('register callbacks')
        # ? why output order is 3 - 2 -1?
        # registers callback in event loop
        loop.call_later(0.2, callback, 1)
        # register callback in event loop
        loop.call_later(0.1, callback, 2)
        # register another callback in event loop
        loop.call_soon(callback, 3) # ! implies minimum seconds later, event loop will callback.
        # gets control after sleep .4 seconds
        await asyncio.sleep(.4)

    event_loop = asyncio.get_event_loop()
    try:
        logging.debug('entering event loop')
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        logging.debug('exiting event loop')
        event_loop.close()

if __name__ == "__main__":
    asyncio_call_later()