import asyncio, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_ensure_future():
    async def wrapped():
        logging.debug('hi, in wrapped')
        return 'result'
    async def inner(task):
        logging.debug('inner: starting')
        logging.debug('inner: waiting for {!r}'.format(task))
        result = await task
        logging.debug('inner: task returned {!r}'.format(result))
    async def starter():
        logging.debug('starter: creating task')
        """
        ! the `ensure_future()` function returns a `Task` tied to the execution of a coroutine.
        That `Task` instance can be passed to code, which can wait for it w/o knowing how the original coroutine was constructed or called

        NOTE:
        Note that the coroutine given to ensure_future() does not start until something uses await, 
        which allows it to be executed.
        """
        task = asyncio.ensure_future(wrapped())
        logging.debug('starter: waiting for inner')
        await inner(task)
        logging.debug('start: inner returned')
    event_loop = asyncio.get_event_loop()
    try:
        logging.debug('entering event loop')
        result = event_loop.run_until_complete(starter())
        logging.debug('result: {!r}'.format(result))
    finally:
        event_loop.close() 


if __name__ == "__main__":
    ### this behavior is like decorator .. wtf ..
    asyncio_ensure_future()