"""

Table: asyncio.Event vs asyncio.Lock vs asyncio.Condition
+---------------------------------------+-------------------+---------------+------------------------------------------+
| diff                                  | asyncio.Event     | asyncio.Lock  | asyncio.Condition                        |
+=======================================+===================+===============+==========================================+
| start as soon as Event/Lock changes?  | yes               | no            | yes                                      |
+---------------------------------------+-------------------+---------------+------------------------------------------+
| need to acquire a unique Event/Lock?  | no                | yes           | no                                       |
+---------------------------------------+-------------------+---------------+------------------------------------------+
| notify all waiting coroutines?        | yes               | yes           | no, controlled with an arg to `notify()` |
+---------------------------------------+-------------------+---------------+------------------------------------------+

"""

import asyncio, logging
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_condition():
    async def consumer(condition, n):
        async with condition:
            logging.debug('consumer {} is waiting'.format(n))
            """
            using `wait()` method to wait for a notification that it can proceed
            """
            await condition.wait()
            logging.debug('consumer {} triggered'.format(n))
        logging.debug('ending consumer {}'.format(n))

    async def manipulate_condition(condition):
        logging.debug('starting manipulate_condition')
        # pauses to let consumers start
        await asyncio.sleep(.1)   # <~ nothing different after commentout this line?

        for i in range(1, 3):
            async with condition:
                logging.debug('notifying {} consumers'.format(i))
                """
                notifying consumer 1, consumer 2 in turn
                """
                condition.notify(n=i)
            await asyncio.sleep(.1)
        
        async with condition:
            logging.debug('notifying remaining consumers')
            """
            notifying all of the remainig consumers
            """
            condition.notify_all()
        logging.debug('ending manupulate_condition')

    async def main_job(loop):
        # creates a condtion obj
        condition = asyncio.Condition()
        # sets up tasks watching the condition
        consumers = [
            consumer(condition, i)
            for i in range(5)
        ]
        # schedules a task to manipulate the condition variable
        loop.create_task(manipulate_condition(condition))
        # waits for the consumers to be done
        await asyncio.wait(consumers)
    # creates an event loop
    event_loop = asyncio.get_event_loop()
    try:
        # runs events
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        # close event loop, no more events
        event_loop.close()

if __name__ == "__main__":
    asyncio_condition()