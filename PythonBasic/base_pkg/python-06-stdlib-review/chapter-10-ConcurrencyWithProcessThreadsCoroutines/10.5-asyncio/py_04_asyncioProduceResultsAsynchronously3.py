import asyncio, functools
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_future_callback():
    # a normal callback function
    def callback(future, n):
        logging.debug('{}: future done: {}'.format(n, future.result()))
    # registers callbacks on Future
    async def register_callbacks(future):
        """
        ! simple task/action:  callback when Future obj is "done"
        """
        logging.debug('registering all callbacks on future')
        future.add_done_callback(functools.partial(callback, n=1))
        future.add_done_callback(functools.partial(callback, n=2))

    async def main_job(future):
        ### calll register_callbacks() tp do register stuff
        await register_callbacks(future)
        logging.debug('setting result of future')
        future.set_result('the result')
    
    # creates event loop
    event_loop = asyncio.get_event_loop()
    try:
        future = asyncio.Future()
        event_loop.run_until_complete(main_job(future))
    finally:
        event_loop.close()


if __name__ == "__main__":
    ### a Future can invoke callbacks when it is completed.
    asyncio_future_callback()