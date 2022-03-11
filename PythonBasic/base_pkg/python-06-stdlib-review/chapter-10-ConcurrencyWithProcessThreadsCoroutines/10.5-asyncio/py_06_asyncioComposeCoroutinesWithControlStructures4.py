import asyncio, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_as_completed():
    async def phase(i):
        logging.debug('in phase {}'.format(i))
        await asyncio.sleep(.5 - (.1 * i))
        logging.debug('done with phase {}'.format(i))
        return 'phase {} result'.format(i)

    async def main_job(num_phases):
        logging.debug('starting main_job')
        phases = [
            phase(i)
            for i in range(num_phases)
        ]
        logging.debug('waiting for phases to complete')
        results = []
        """
        `as_completed()` is a generator that manages the execution of coroutines given to it
        and produces their results one at a time as each coroutine finishes running.

        As with wait(), order is not guaranteed by `as_completed()`,
        but it is not necessary to wait for all of the background operations to complete before taking other action.

        ? here is my question: difference between `wait()`, `gather()`, `as_completed()`?
        Table: asyncio.wait() vs asyncio.gather() vs asyncio.as_completed()
        +-----------------+------------------------+------------------+---------------------------+
        | diff            | wait()                 | gather()         | as_completed()            |
        +=================+========================+==================+===========================+
        | order?          | no guaranteed          | passed order     | no guaranteed             |
        +-----------------+------------------------+------------------+---------------------------+
        | cancellable?    | yes                    | no               | ?                         |
        +-----------------+------------------------+------------------+---------------------------+
        | return type?    | Tuple[Set, Set]        | List             | generator                 |
        +-----------------+------------------------+------------------+---------------------------+
        | operations?     | pause and wait other   | all results      | not necessary to wait     |
        +-----------------+------------------------+------------------+---------------------------+

        """
        for next_to_complete in asyncio.as_completed(phases):
            answer = await next_to_complete
            logging.debug('receive answer {!r}'.format(answer))
            results.append(answer)
        logging.debug('results: {!r}'.format(results))
        return results

    # creates an event loop
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(3))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_as_completed()