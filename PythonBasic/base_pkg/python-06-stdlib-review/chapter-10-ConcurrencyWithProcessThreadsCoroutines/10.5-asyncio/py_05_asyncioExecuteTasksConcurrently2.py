import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_cancel_task():
    ### task func
    async def task_func():
        # do sth
        logging.debug('in task_func')
        return 'the result'
    async def main_job(loop):
        # create a task
        logging.debug('creating a task')
        task = loop.create_task(task_func())
        # cancel the task before it completes
        logging.debug('canceling the task')
        task.cancel()
        logging.debug('canceled task : {!r}'.format(task))
        # start task
        try:
            await task
        except asyncio.CancelledError:
            logging.debug('caught error from canceled task')
        else:
            logging.debug('task result: {!r}'.format(task.result()))
    
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        event_loop.close()


if __name__ == "__main__":
    asyncio_cancel_task()