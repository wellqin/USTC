import multiprocessing
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
)

def worker():
    name = multiprocessing.current_process().name
    logging.debug(f'{name:<10} starting')
    time.sleep(2)
    logging.debug(f'{name:<10} exiting')

def my_service():
    name = multiprocessing.current_process().name
    logging.debug(f'{name:<10} starting')
    time.sleep(3)
    logging.debug(f'{name:<10} exiting')

if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
    )
    worker_1 = multiprocessing.Process(
        name='worker 1',
        target=worker,
    )
    worker_2 = multiprocessing.Process(
        # name='worker 2', # using default name
        target=worker,
    )

    worker_1.start()
    worker_2.start()
    service.start()
