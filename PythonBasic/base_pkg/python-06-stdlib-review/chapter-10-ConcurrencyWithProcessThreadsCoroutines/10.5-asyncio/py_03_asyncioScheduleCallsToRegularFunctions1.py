import asyncio, functools
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_call_soon():
    ### a normal callback function
    def callback(arg, *, kwarg='default'):
        logging.debug('callback invoked with {} and {}'.format(arg, kwarg))

    ### a coroutine wraps and calls soon
    async def main(loop):
        logging.debug('registering callbacks')
        """
        ! if the timing of the callback does not matter, 
        * `call_soon()` can be used to schedule the call for the next iteration of the loop
        ! any extra positional arguments after the function are passed to the callback when it is invoked.
        * To pass keyword arguments to the callback, use `partial()` from the `functools` mmodule
        """
        loop.call_soon(callback, 1)
        wrapped = functools.partial(callback, kwarg='not default')
        loop.call_soon(wrapped, 2)
        await asyncio.sleep(.1)

    ### gets event loop
    event_loop = asyncio.get_event_loop()
    try:
        logging.debug('entering event loop')
        ### inputs event
        ### ! wtf is this line? infinite-loop?!
        event_loop.run_until_complete(main(event_loop))
    finally:
        logging.debug('closing event loop')
        event_loop.close()

if __name__ == "__main__":
    asyncio_call_soon()