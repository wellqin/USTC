import asyncio, time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

# wrap this shit up
def asyncio_call_at():
    # a normal callback function does sth
    def callback(n, t, eventloop):
        logging.debug(f'callback {n} invoked at {eventloop} does sth at {t}')

    # registers events into event loop obj
    async def main_job(loop):
        # i wanna see possible difference btwn time.time() vs loop.time()
        # ? Q: why?
        # * Because it's fun
        now = loop.time()
        logging.debug(f'time.time: {time.time()}')
        logging.debug(f'loop.time: {now}')
        loop.call_at(now + 0.4, callback, 1, now + 0.1, loop)
        loop.call_at(now + 0.2, callback, 2, now + 0.2, loop)
        loop.call_soon(callback, 3, now + 0.3, loop)
        await asyncio.sleep(1)

    # gets event loop
    event_loop = asyncio.get_event_loop()
    # all set, let event loop run
    try:
        logging.debug('entering loop..')
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        logging.debug('existing loop..')
        event_loop.close() # no more events

if __name__ == "__main__":
    asyncio_call_at()