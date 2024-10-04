"""

if a task is canceled while it is waiting for another concurrent operation to finish,
the task is notified of its cancellation 
through a `CancelledError` exception raised at the point where it is waiting

"""

import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_cancel_task2():
    async def task_func():
        logging.debug('in task_func, sleeping')
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            logging.debug('task_func was canceled')
            raise
        return 'the result'
    
    ### ! i have no f*cking idea when to create `async def`, when to create regular `def`
    def task_canceller(t):
        logging.debug('in task_canceller')
        t.cancel()
        logging.debug('canceled the task')

    async def main_job(loop):
        logging.debug('creating task')
        task = loop.create_task(task_func())
        loop.call_soon(task_canceller, task)
        try:
            await task
        except asyncio.CancelledError:
            logging.debug('main_job() also sees task as canceled')

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_cancel_task2()