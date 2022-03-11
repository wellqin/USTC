import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_coroutine_chain():
    """
    ! observe the pattern here.
    ! main job have two phases, and also phase2 relies on phase1
        outer
            |
            phase1 -- result1
            |
            phase2 -- result2
    """
    async def outer():
        logging.debug('in outer')
        logging.debug('waiting for result1')
        """
        ? why using `await` instead of creating a new coroutine for phase1 and phase2?
        * because control flow is already inside of a coroutine being managed by the loop, 
        * it's not necessary to tell the loop to manage the new coroutines.
        """
        result1 = await phase1()
        logging.debug('waiting for result2')
        result2 = await phase2(result1)
        return (result1, result2)
    pass

    async def phase1():
        logging.debug('in phase1')
        return 'result1'
    async def phase2(arg):
        logging.debug('in phase2')
        return f'result2 derived from {arg}'
    
    # first step, get_event_loop
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        logging.debug('return value: {!r}'.format(return_value))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_coroutine_chain()