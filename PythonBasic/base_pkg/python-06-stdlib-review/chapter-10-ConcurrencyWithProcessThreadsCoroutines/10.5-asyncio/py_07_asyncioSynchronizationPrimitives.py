import asyncio, functools
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_lock():
    ### a normal function unlocks a Lock obj
    def unlock(lock):
        logging.debug('callback releasing lock')
        lock.release()
    
    async def coro1(lock):
        logging.debug('corol waiting for the lock')
        # ! Python > 3.8, `with await lock` is deprecated. use `async with lock`
        async with lock:
            logging.debug('corol acquired lock')
        logging.debug('corol released lock')
    
    async def coro2(lock):
        logging.debug('coro2 waiting for the lock')
        await lock
        try:
            logging.debug('coro2 acquired lock')
        finally:
            logging.debug('coro2 released lock')
            lock.release()
    
    async def main_job(loop):
        # creates and acquires a shared Lock object
        """
        a Lock can be used to guard access to a shared resource.
        Only the holder of the lock can use the resource.

        Multiple attempts to acquire the lock will block so that there is one, only one holder at a time.
        
        ? is this asyncio.Lock() mechnism same with threading.Lock() and multiprocessing.Lock()
        Table: asyncio.Lock() vs threading.Lock() vs multiprocessing.Lock()
        +-----------------------------+----------------------+----------------------+----------------------------+
        | diff                        | asyncio.Lock()       | threading.Lock()     | multiprocessing.Lock()     |
        +-----------------------------+----------------------+----------------------+----------------------------+
        | lock what?                  | resource             | resource             | resource
        +-----------------------------+----------------------+----------------------+----------------------------+
        | acquired once?              | ?                    | yes                  | yes
        +-----------------------------+----------------------+----------------------+----------------------------+
        | lock()?                     | lock()               | lock()               | lock()
        +-----------------------------+----------------------+----------------------+----------------------------+
        | release()?                  | release()            | release()            | release()
        +-----------------------------+----------------------+----------------------+----------------------------+
        | how to check lock status?   | locked()             | ?                    | ?
        +-----------------------------+----------------------+----------------------+----------------------------+
        | multiple acquire?           | locked()             | ?                    | ?
        +-----------------------------+----------------------+----------------------+----------------------------+
        | re-acquire?                 | ?                    | yes. RLock()         | ?
        +-----------------------------+----------------------+----------------------+----------------------------+

        """
        lock = asyncio.Lock()
        logging.debug('acquring the lock before starting coroutines')
        """
        a Lock can be invoked directly.
        ! using `await` to acquire it and calling the `release()` method when done
        just like `threading.Lock()` and `multiprocessing.Lock()`, context managers help a lot
        """
        await lock.acquire()
        logging.debug('lock acquired: {}'.format(lock.locked()))
        # schedules a callback to unlock the lock
        # ? it's a position arg, NOT a kwarg. why using `partial()` here tho?
        loop.call_later(.1, functools.partial(unlock, lock))
        # runs the coroutines that want to use the lock
        logging.debug('waiting for coroutines')
        await asyncio.wait([coro1(lock), coro2(lock)])

    # here is our beautiful Ms. Planner
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_lock()