import asyncio, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_wait_timeout():
    async def phase(i):
        logging.debug('in phase {}'.format(i))
        try:
            await asyncio.sleep(.1 * i)
        except asyncio.CancelledError:
            logging.debug('phase {} canceled'.format(i))
            raise
        else:
            logging.debug('done with phase {}'.format(i))
            return 'phase {} result'.format(i)
    async def main_job(num_phases):
        logging.debug('starting main_job')
        phases = [
            phase(i)
            for i in range(num_phases)
        ]
        logging.debug('waiting 0.1 for phases to complete')
        """
        If wait() is used with a timeout value, 
        ! only pending operations will remain after the timeout occurs.
        """
        completed, pending = await asyncio.wait(phases, timeout=.1)
        logging.debug('{} completed and {} pending'.format(len(completed), len(pending)))
        # cancel remaining tasks so they do not generate errors
        # as we exit w/o finishing them
        """
        ! the remaining background operations should handled explicitly for several reasons.
        although pending tasks are suspended when `wait()` returns, they will resume as soon as control reverts to the event loop.

        ! w/o another call to `wait()`, nothing will receive the output of the tasks;
        that is, the tasks will run and consume resources with no benefit. 

        ! also, asyncio emits a warning if there are pending tasks when the program exits.
        these warnings may be printed on the console, where uses of the application will see them.

        ! therefore, it is best to either to cancel any remaining background operations,
        or to use `wait()` to let them finish running.
        """
        if pending:
            logging.debug('canceling tasks')
            for p in pending:
                p.cancel()
        logging.debug('exiting main_job')
    # creates an event loop
    event_loop = asyncio.get_event_loop()
    try:
        # runs events
        event_loop.run_until_complete(main_job(3))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_wait_timeout()