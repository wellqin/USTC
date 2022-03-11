import logging, time
from concurrent import futures

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(threadName)s %(message)s')

def futures_context_manager():
    def task(n):
        logging.debug(f'{n}')

    with futures.ThreadPoolExecutor(max_workers=2) as ex:
        logging.debug('main: starting')
        results = ex.map(task, [i for i in range(1, 5)])
    logging.debug(f'results: {list(results)}')

if __name__ == "__main__":
    futures_context_manager()