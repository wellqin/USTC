import asyncio, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_gather_results_from_coroutines():
    async def phase1():
        logging.debug('in phase1')
        await asyncio.sleep(2)
        logging.debug('done with phase1')
        return 'phase1 result'
    async def phase2():
        logging.debug('in phase2')
        await asyncio.sleep(1)
        logging.debug('done with phase2')
        return 'phase2 result'
    async def main_job():
        logging.debug('starting main')
        logging.debug('waiting for phases to complete')
        """
        ! the tasks created by `gather()` are not exposed,
        so they cannot be canceled.
        
        ! the return value is a list of results presented in the same order as the arguments passed to `gather()`,
        regardless of the order in which the background operations actually completed.
        """
        results = await asyncio.gather(
            phase1(),
            phase2(),
        )
        logging.debug('results: {!r}'.format(results))
    # creates an event loop
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job())
    finally:
        event_loop.close()


if __name__ == "__main__":
    asyncio_gather_results_from_coroutines()