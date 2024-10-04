from concurrent import futures
import random
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(process)d %(thread)d %(message)s')

def futures_as_completed():
    def task(n):
        time.sleep(random.random())
        return (n, n/10)

    ex = futures.ThreadPoolExecutor(max_workers=5)
    logging.debug('main: starting')
    wait_for = [
        ex.submit(task, i)
        for i in range(5, 0, -1)
    ]

    for f in futures.as_completed(wait_for):
        logging.debug('main: result: {}'.format(f.result()))

if __name__ == "__main__":
    futures_as_completed()