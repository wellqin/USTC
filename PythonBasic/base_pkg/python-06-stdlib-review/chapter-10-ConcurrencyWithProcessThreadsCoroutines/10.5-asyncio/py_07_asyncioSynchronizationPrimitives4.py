import asyncio, logging

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def asyncio_queue():
    async def consumer(n, q):
        logging.debug('consumer {}: starting'.format(n))
        while True:
            logging.debug('consumer {}: waiting for item'.format(n))
            """
            adding items with `put()` and removing items with `get()`are both asynchronous operations, 
            since the queue size might be fixed(blocking an additional) or 
            the queue might be empty(blocking a call to fetch an item)
            """
            item = await q.get()
            logging.debug('consumer {}: has item {}'.format(n, item))
            if item is None:
                q.task_done()
                break
            else:
                await asyncio.sleep(.01 * item)
                q.task_done()
        logging.debug('consumer {}: ending'.format(n))

    async def producer(q, num_workers):
        logging.debug('producer: starting')
        # add some numbers to the queue to simulate jobs
        for i in range(num_workers * 3):
            """
            adding items with `put()` and removing items with `get()`are both asynchronous operations, 
            since the queue size might be fixed(blocking an additional) or 
            the queue might be empty(blocking a call to fetch an item)
            """
            await q.put(i)
            logging.debug('producer: added task {} to the queue'.format(i))
        # add None entries in the queue to signal the consumers to exit
        # ! N(None) == N(consumers). poison pill
        for i in range(num_workers):
             await q.put(None)
        logging.debug('producer: waiting for queue to empty')
        await q.join()
        logging.debug('producer: ending')
    
    async def main_job(loop, num_consumers):
        """
        
        Table: Queues
        +------------+-----------------------+-----------------------+-------------------------------+
        |            | asyncio               | threading             | multiprocessing               |
        +------------+-----------------------+-----------------------+-------------------------------+
        | Queue      | asyncio.Queue()       | threading.Queue()     | multiprocessing.Queue()       |
        +------------+-----------------------+-----------------------+-------------------------------+
        
        """
        # creates a queue with a fixed size so the producer will block until the consumers pull some items out
        q = asyncio.Queue(maxsize=num_consumers)
        # schedules the consumer tasks
        consumers = [
            loop.create_task(consumer(i, q))
            for i in range(num_consumers)
        ]
        # schedules the producer task
        prod = loop.create_task(producer(q, num_consumers))
        # waits for all of the coroutines to finish
        await asyncio.wait(consumers + [prod])
    
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop, 2))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_queue()