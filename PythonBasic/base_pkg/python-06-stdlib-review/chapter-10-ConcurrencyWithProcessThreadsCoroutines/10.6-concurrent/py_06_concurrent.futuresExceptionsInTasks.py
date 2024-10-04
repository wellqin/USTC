import logging, time
from concurrent import futures

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(threadName)s %(message)s')

def futures_future_exception():
    def task(n):
        logging.debug(f'{n}: sleeping')
        time.sleep(.5)
        logging.debug(f'{n}: done')
        raise ValueError(f'the value {n} is NOT good')
        # return n / 10

    ex = futures.ThreadPoolExecutor(max_workers=2)
    logging.debug('main: starting')
    f  = ex.submit(task, 5)
    error = f.exception()
    logging.debug(f'main: error: {error}')

    try:
        result = f.result()
        logging.debug(f'result: {result}')
    except ValueError as e:
        logging.debug(f'main: saw error "{e}" when accessing result')


if __name__ == "__main__":
    futures_future_exception()