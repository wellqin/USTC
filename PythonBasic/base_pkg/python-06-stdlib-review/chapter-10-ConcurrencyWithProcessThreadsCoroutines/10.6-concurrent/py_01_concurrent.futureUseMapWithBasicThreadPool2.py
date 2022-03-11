from concurrent import futures
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(processName)s %(message)s')

def futures_thread_pool_submit():
    def task(n):
        logging.debug('sleeping {}'.format(n))
        time.sleep(n/10)
        logging.debug('done with {}'.format(n))
        return n/10

    ex = futures.ThreadPoolExecutor(max_workers=2)
    logging.debug('main: starting')
    # ! uses `submit()` to schedule an individual task
    f  = ex.submit(task, 5)
    logging.debug('main: future: {}'.format(f))
    logging.debug('main: waiting for results')
    result = f.result()
    logging.debug('main: result: {}'.format(result))
    logging.debug('main: future after result: {}'.format(f))

if __name__ == "__main__":
    futures_thread_pool_submit()