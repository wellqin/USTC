import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_create_task():
    async def task_func():
        logging.debug('in task_func')
        return 'the result'
    async def main_job(loop):
        logging.debug('creating task')
        task = loop.create_task(task_func())
        logging.debug('waiting for {!r}'.format(task))
        return_value = await task
        logging.debug('task completed {!r}'.format(task))
        logging.debug('return value: {!r}'.format(return_value))
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        event_loop.close()

if __name__ == "__main__":
    ### Tasks are one of the primary ways to interact with the event loop.
    ### Tasks wrap cotoutines and track when they are complete. 
    ### Because they are subclasses of Future, other coroutines can wait for tasks, and each task has a result that cane be retrieved after it completes.
    asyncio_create_task()