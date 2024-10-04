import multiprocessing, time
import logging, sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s, %(module)s, %(message)s',
)
def worker():
    logging.debug(f'Doing some work')
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()