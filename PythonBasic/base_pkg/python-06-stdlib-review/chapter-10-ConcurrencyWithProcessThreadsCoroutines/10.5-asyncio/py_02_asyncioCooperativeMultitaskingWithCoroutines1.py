import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_coroutine():
    async def coroutine():
        """create a coroutine easy af"""
        logging.debug(f'in coroutine')    

    """
    * First step is to obtain a reference to the event loop.
    * The default loop type can be used, or a specific loop class can be instantiated.
    """
    event_loop = asyncio.get_event_loop()

    try:
        logging.debug(f'starting coroutine')
        logging.debug(f'entering event loop')
        """
        ! asyncio event loop can start a coroutine in several different ways.
        ! the simplest approach is to use `run_until_complete()`, passing the coroutine to this method directly.
        """
        event_loop.run_until_complete(coroutine())
    finally:
        logging.debug(f'closing event loop')
        event_loop.close()

if __name__ == "__main__":
    ### seems there is NO extra protection on "__main__"
    # this toy example is silly
    asyncio_coroutine()