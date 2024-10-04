import asyncio, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_wait():
    async def phase(i):
        logging.debug('in phase {}'.format(i))
        await asyncio.sleep(.1 * i)
        logging.debug('done with phase {}'.format(i))
        return 'phase {} result'.format(i)

    async def main_job(num_phases):
        logging.debug('starting main_job')
        """
        it is often useful to divide one operation into many parts,
        which are then executed separately.
        
        for example, this approach is an efficient way of downloading several remote resources
        or querying remote APIs.

        In situations where the order of execution doesn't matter, and where there may be an arbitrary number of operation,
        `wait()` can be used to pause one coroutine until the other background operations complete.
        """
        phases = [
            phase(i)
            for i in range(num_phases)
        ]
        logging.debug('waiting for phases to complete')
        """
        Internally, `wait()` uses a set to hold the Task instances it creates,
        which means that the instances start, and finish, in an unpredictable order. 
        The return value from `wait()` is a tuple containing two sets holding the finished and pending tasks.
        """
        completed, pending = await asyncio.wait(phases)
        pendings = [p.result() for p in pending]
        results = [t.result() for t in completed]
        logging.debug('pending: {!r}'.format(pendings))
        logging.debug('results: {!r}'.format(results))
    # creates an event loop
    event_loop = asyncio.get_event_loop()
    try:
        # registers all events onto the event loop
        event_loop.run_until_complete(main_job(3))
    finally:
        # close event loop. no more events
        event_loop.close()

if __name__ == "__main__":
    asyncio_wait()