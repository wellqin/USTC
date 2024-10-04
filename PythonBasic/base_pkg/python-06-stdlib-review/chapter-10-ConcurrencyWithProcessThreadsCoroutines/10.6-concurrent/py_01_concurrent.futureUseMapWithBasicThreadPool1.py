from concurrent import futures
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(asctime)s) %(processName)s %(message)s')

def futures_thread_pool_map():
    def task(n):
        logging.debug('sleeping {}'.format(n))
        """
        uses time.sleep() to pause a different amount of time to demonstrate
        """
        time.sleep(n/10)
        logging.debug('done with {}'.format(n))
        return n/10

    ex = futures.ThreadPoolExecutor(max_workers=2)
    logging.debug('main: starting')
    """
    regardless of the order of execution of concurrent tasks,
    ! `map()` always returns the values in order based on the inputs.
    
    ! the return value from `map()` is actually a special type of iterator that knows to wait for each response 
    ! as the main program iterates over it
    """
    results = ex.map(task, range(5, 0, -1))
    logging.debug('main: unprocessed results {}'.format(results))
    logging.debug('main: waiting for real results')
    real_results = list(results)
    logging.debug('main: results: {}'.format(real_results))

if __name__ == "__main__":
    ### seems concurrent.futures has no extra protection on "__main__"
    futures_thread_pool_map()